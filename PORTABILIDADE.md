# Guia de Portabilidade - Aluguel Manager

Este documento contém as instruções e os prompts necessários para recriar ou migrar o sistema **Aluguel Manager** para um novo ambiente.

## 🛠️ Stack Tecnológica
- **Frontend**: React 19, TypeScript, Tailwind CSS, Vite, Lucide React, Sonner (Toasts), Wouter (Roteamento).
- **Backend**: Node.js, Express, tRPC (API), Zod (Validação).
- **Banco de Dados**: MySQL / MariaDB (Drizzle ORM para migrações).
- **Geração de PDF**: html2pdf.js (Frontend).

## 🚀 Como Rodar o Projeto

### 1. Requisitos
- Node.js 20+
- MySQL ou MariaDB
- pnpm (recomendado) ou npm

### 2. Configuração do Banco de Dados
Crie um banco de dados chamado `aluguel_manager` e execute as migrações ou o script SQL fornecido no pacote.

### 3. Variáveis de Ambiente (.env)
Crie um arquivo `.env` na raiz com:
```env
DATABASE_URL="mysql://usuario:senha@localhost:3306/aluguel_manager"
JWT_SECRET="sua-chave-secreta-aqui"
LOCAL_AUTH_PASSWORD="sua-senha-de-login"
NODE_ENV="development"
```

### 4. Instalação e Execução
```bash
pnpm install
pnpm dev
```

## 📝 Prompts Utilizados para Criação

### Prompt de Arquitetura Inicial
> "Crie um sistema de gerenciamento de aluguéis usando React, Node.js e MySQL. O sistema deve ter um Dashboard com KPIs de receita e inadimplência, cadastro de Imóveis, Inquilinos e controle mensal de Pagamentos. Use um estilo visual 'Neo-Brutalismo' com bordas grossas e cores sólidas."

### Prompt para o Sistema de Recibos
> "Implemente um gerador de recibos em PDF no frontend usando html2pdf.js. O recibo deve ser profissional, com logo, assinatura e valor por extenso. Adicione a opção de customizar o nome do pagador e um botão para enviar os dados do recibo diretamente via WhatsApp."

### Prompt para Importação de Planilha
> "Crie um script em Python usando Pandas para ler uma planilha Excel com múltiplas abas (cada aba é um imóvel). O script deve identificar a linha de cabeçalho 'Nome' automaticamente e importar inquilinos, valores de aluguel, caução e o histórico de pagamentos de Janeiro a Dezembro para o banco MySQL."

## 🔒 Segurança e Customizações
- O sistema possui um **Login Local** simplificado.
- O nome **"Illoneide"** é filtrado automaticamente no gerador de recibos por questões de privacidade/segurança conforme solicitado.
- Alertas de **Aluguel Vencido** são exibidos automaticamente no Dashboard com base no status "Não Pago" do mês atual.
