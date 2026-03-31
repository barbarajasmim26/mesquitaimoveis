# Sistema de Gerenciamento de Aluguéis — TODO

## Schema & Banco de Dados
- [x] Tabela `imoveis` (id, nome, endereco, numero)
- [x] Tabela `inquilinos` (id, nome, telefone, email, imovel_id, numero_casa, caucao, aluguel_mensal, data_entrada, data_saida, dia_pagamento)
- [x] Tabela `pagamentos` (id, inquilino_id, ano, mes, status: pago/nao_pago/caucao)
- [x] Migração SQL aplicada via webdev_execute_sql

## Backend (tRPC Routers)
- [x] Router `imoveis`: listar, criar, editar, excluir
- [x] Router `inquilinos`: listar, criar, editar, excluir, buscar por imóvel
- [x] Router `pagamentos`: listar por inquilino/mês/ano, registrar/atualizar status
- [x] Router `dashboard`: estatísticas gerais (total imóveis, inquilinos ativos, pagamentos do mês)
- [x] Router `relatorios`: inadimplência, histórico, financeiro mensal/anual
- [x] Router `importacao`: importar dados da planilha Excel

## Frontend — Design Brutalista
- [x] Configurar tipografia brutalista (fonte massiva sans-serif, preto/branco)
- [x] Atualizar index.css com tokens de design brutalista
- [x] DashboardLayout com sidebar brutalista
- [x] Página Dashboard (visão geral, KPIs, imóveis ativos)
- [x] Página Imóveis (listagem, cadastro, edição)
- [x] Página Inquilinos (listagem, cadastro, edição com filtros)
- [x] Página Pagamentos (controle mensal por inquilino, grid de meses)
- [x] Página Relatórios (inadimplência, histórico, financeiro)
- [x] Importação da planilha Excel (upload e processamento)
- [x] Filtros e busca global (por imóvel, inquilino, status)
- [x] Interface responsiva para mobile

## Relatórios PDF
- [x] Relatório financeiro mensal com gráficos
- [x] Relatório financeiro anual com estatísticas
- [x] Relatório de inadimplência

## Testes
- [x] Testes vitest para routers principais
- [x] Verificação de importação da planilha


## Melhorias Visuais
- [x] Cores semânticas: verde (pago), vermelho (atraso), amarelo (pendente)
- [x] Indicadores visuais de risco e status nos pagamentos
- [x] Alertas de contratos a vencer este mês
- [x] Badges e ícones para status de pagamento
- [x] Destaque visual para inadimplentes


## Melhorias Adicionais
- [x] Alertas de vencimento em tempo real na coluna Status/Alertas
- [x] Mostrar "VENCIDO" em vermelho se contrato venceu
- [x] Mostrar "VENCE HOJE" se vencer hoje
- [x] Mostrar dias restantes (Xd) se vencer em até 7 dias
- [x] Mostrar "VENCE" em laranja se vencer este mês


## Sistema de Recibos
- [x] Página de Recibos com editor visual
- [x] Gerar PDF de recibo com dados do inquilino
- [x] Histórico de recibos por inquilino

- [ ] Criar utilitário de cálculo de vencimento com normalização por data
- [ ] Adicionar testes para regras de alerta (vencido, vence hoje, <=7 dias)
- [ ] Expandir alertas de vencimento para o Dashboard

- [ ] Implementar backend de recibos (schema + queries + router)
- [ ] Substituir impressão por geração real de PDF com export
- [ ] Adicionar histórico de recibos por inquilino com filtros
- [ ] Adicionar estados de loading/error na página Recibos

- [x] Adicionar visualização de PDF no navegador antes de baixar

- [x] Extrair assinatura manuscrita de Maria Eneide do PDF e incluir no recibo
