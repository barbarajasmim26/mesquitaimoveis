import pandas as pd
import mysql.connector
from datetime import datetime
import re

# Configurações do Banco de Dados
DB_CONFIG = {
    "host": "localhost",
    "user": "aluguel",
    "password": "admin123",
    "database": "aluguel_manager"
}

FILE_PATH = "/home/ubuntu/upload/CópiadePlanilhaaluguel2026.xlsx"

def clean_money(value):
    if pd.isna(value) or value == "-":
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    # Remove R$, espaços e converte vírgula em ponto
    cleaned = re.sub(r'[^\d,.-]', '', str(value)).replace(',', '.')
    try:
        return float(cleaned)
    except:
        return 0.0

def parse_date(value):
    if pd.isna(value) or str(value).strip() == "":
        return None
    try:
        if isinstance(value, datetime):
            return value.date()
        return pd.to_datetime(value).date()
    except:
        return None

def map_status(status_str):
    if not status_str or pd.isna(status_str):
        return "pendente"
    s = str(status_str).lower().strip()
    if "pago" in s and "não" not in s:
        return "pago"
    if "não pago" in s or "nao pago" in s:
        return "nao_pago"
    if "caução" in s or "caucao" in s:
        return "caucao"
    return "pendente"

def import_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    xl = pd.ExcelFile(FILE_PATH)
    
    # Mapeamento de meses na planilha para números
    MESES_MAP = {
        "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
        "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
    }

    for sheet_name in xl.sheet_names:
        print(f"Processando aba: {sheet_name}")
        
        # Ler a aba pulando as linhas de cabeçalho extras (geralmente as 2 primeiras)
        df = pd.read_excel(xl, sheet_name=sheet_name, skiprows=2)
        
        # Identificar o endereço do imóvel (geralmente na primeira linha da aba original)
        df_raw = pd.read_excel(xl, sheet_name=sheet_name, header=None)
        endereco_imovel = str(df_raw.iloc[1, 0]) if len(df_raw) > 1 else sheet_name
        
        # Inserir ou obter Imóvel
        cursor.execute("SELECT id FROM imoveis WHERE nome = %s", (sheet_name,))
        row = cursor.fetchone()
        if row:
            imovel_id = row[0]
        else:
            cursor.execute("INSERT INTO imoveis (nome, endereco) VALUES (%s, %s)", (sheet_name, endereco_imovel))
            imovel_id = cursor.lastrowid
            
        # Iterar sobre os inquilinos
        for _, row in df.iterrows():
            nome = row.get("Nome")
            if pd.isna(nome) or str(nome).strip() == "" or "Nome" in str(nome):
                continue
                
            casa = str(row.get("Casa", ""))
            data_entrada = parse_date(row.get("Data de entrada"))
            data_saida = parse_date(row.get("Data de saída"))
            caucao = clean_money(row.get("Caução"))
            aluguel = clean_money(row.get("Aluguel"))
            dia_pagamento = str(row.get("Data de pagamento", ""))
            
            # Inserir Inquilino
            cursor.execute("""
                INSERT INTO inquilinos (nome, imovelId, numeroCasa, caucao, aluguelMensal, diaPagamento, dataEntrada, dataSaida, ativo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'sim')
            """, (nome, imovel_id, casa, caucao, aluguel, dia_pagamento, data_entrada, data_saida))
            inquilino_id = cursor.lastrowid
            
            # Processar Pagamentos (Colunas de Janeiro a Dezembro)
            for mes_nome, mes_num in MESES_MAP.items():
                status_val = row.get(mes_nome)
                if pd.notna(status_val):
                    status = map_status(status_val)
                    # Assumindo ano 2025 conforme o título da planilha
                    cursor.execute("""
                        INSERT INTO pagamentos (inquilinoId, ano, mes, status)
                        VALUES (%s, %s, %s, %s)
                    """, (inquilino_id, 2025, mes_num, status))
                    
    conn.commit()
    cursor.close()
    conn.end()
    print("Importação concluída com sucesso!")

if __name__ == "__main__":
    import_data()
