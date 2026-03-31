# 🏠 Guia de Deploy - Aluguel Manager em mesquitaimoveis.com

Este é o guia completo para publicar seu sistema de gerenciamento de aluguéis no domínio **mesquitaimoveis.com**.

---

## 📋 Resumo do Processo

| Etapa | O que fazer | Tempo |
|-------|-----------|-------|
| 1 | Criar conta Vercel | 5 min |
| 2 | Criar repositório GitHub | 5 min |
| 3 | Configurar banco de dados em nuvem | 10 min |
| 4 | Fazer deploy na Vercel | 5 min |
| 5 | Conectar domínio mesquitaimoveis.com | 15 min |
| **TOTAL** | | **40 min** |

---

## 🔧 Pré-requisitos

- ✅ Domínio **mesquitaimoveis.com** já registrado
- ✅ Conta **GitHub** (gratuita)
- ✅ Conta **Vercel** (gratuita)
- ✅ Banco de dados MySQL em nuvem

---

## 🚀 PASSO 1: Preparar o Banco de Dados em Nuvem

### Opção A: PlanetScale (RECOMENDADO - Gratuito)

1. Acesse: https://planetscale.com
2. Clique em **"Sign up"** e crie sua conta
3. Clique em **"Create a new database"**
4. Nome: `aluguel_manager`
5. Region: Escolha a mais próxima do Brasil (São Paulo)
6. Clique em **"Create database"**
7. Vá para **"Connect"** e copie a string de conexão:
   ```
   mysql://username:password@host/aluguel_manager
   ```
   **Guarde essa string!** Você vai precisar dela.

8. Execute as migrações SQL:
   - Abra a pasta `drizzle/` do projeto
   - Execute os arquivos `.sql` em ordem (0000, 0001, 0002, etc.)
   - Ou use: `pnpm run db:push`

---

## 📦 PASSO 2: Fazer Upload do Código para GitHub

### 2.1 Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name**: `aluguel-manager`
   - **Description**: `Sistema de Gerenciamento de Aluguéis Mesquita`
   - **Visibility**: Escolha **Private** (mais seguro)
3. Clique em **"Create repository"**

### 2.2 Fazer Push do Código

Execute esses comandos no seu computador:

```bash
# Navegue até a pasta do projeto
cd /caminho/para/aluguel-manager

# Adicione o repositório remoto
git remote add origin https://github.com/SEU-USUARIO/aluguel-manager.git

# Renomeie a branch para main
git branch -M main

# Faça push do código
git push -u origin main
```

**Pronto!** Seu código está no GitHub.

---

## 🎯 PASSO 3: Deploy na Vercel

### 3.1 Conectar GitHub à Vercel

1. Acesse: https://vercel.com
2. Clique em **"Sign up"** (ou faça login)
3. Escolha **"Continue with GitHub"**
4. Autorize a Vercel a acessar seu GitHub

### 3.2 Criar Novo Projeto

1. Clique em **"New Project"**
2. Clique em **"Import Git Repository"**
3. Procure por `aluguel-manager`
4. Clique em **"Import"**

### 3.3 Configurar Variáveis de Ambiente

Na tela de configuração, adicione essas variáveis:

| Variável | Valor | Exemplo |
|----------|-------|---------|
| `DATABASE_URL` | Sua string do PlanetScale | `mysql://user:pass@host/aluguel_manager` |
| `JWT_SECRET` | Chave secreta forte | `sua-chave-super-secreta-2024-xyz123` |
| `LOCAL_AUTH_PASSWORD` | Senha de login | `admin123` |
| `NODE_ENV` | production | `production` |

### 3.4 Deploy

1. Clique em **"Deploy"**
2. Aguarde 3-5 minutos
3. Quando terminar, você verá: ✅ **"Congratulations! Your project has been successfully deployed"**

**Copie o link de acesso temporário** (algo como `aluguel-manager-xyz.vercel.app`)

---

## 🌐 PASSO 4: Conectar o Domínio mesquitaimoveis.com

### 4.1 Na Vercel

1. Vá para o seu projeto na Vercel
2. Clique em **"Settings"**
3. Clique em **"Domains"**
4. Clique em **"Add Domain"**
5. Digite: `mesquitaimoveis.com`
6. Clique em **"Add"**

### 4.2 Configurar DNS

A Vercel vai mostrar dois registros DNS para você adicionar:

```
Type: CNAME
Name: www
Value: cname.vercel-dns.com

Type: A
Name: @
Value: 76.76.19.89
```

### 4.3 Adicionar Registros no Seu Registrador

Onde você registrou o domínio (GoDaddy, Namecheap, etc.):

1. Acesse o painel de controle do domínio
2. Vá para **"DNS Records"** ou **"Gerenciar DNS"**
3. Adicione os registros que a Vercel forneceu
4. Salve as mudanças

**Aguarde 24-48 horas** para a propagação DNS.

---

## ✅ Pronto!

Seu sistema agora está acessível em:
- **https://mesquitaimoveis.com**
- **https://www.mesquitaimoveis.com**

### 🔐 Credenciais de Login

- **Senha**: `admin123` (ou a que você configurou em `LOCAL_AUTH_PASSWORD`)

### 📍 Rotas Disponíveis

- `/` - Dashboard
- `/alertas` - Alertas de Aluguéis Vencidos
- `/imoveis` - Gerenciar Imóveis
- `/inquilinos` - Gerenciar Inquilinos
- `/pagamentos` - Controle de Pagamentos
- `/recibos` - Gerar Recibos em PDF
- `/relatorios` - Relatórios
- `/importar` - Importar Dados

---

## 🆘 Troubleshooting

### ❌ "Database connection failed"
- Verifique se a `DATABASE_URL` está correta
- Certifique-se de que o PlanetScale está acessível

### ❌ "Build failed on Vercel"
- Verifique o log de build
- Rode `pnpm install && pnpm build` localmente

### ❌ "Domínio não funciona"
- Aguarde a propagação DNS (até 48 horas)
- Verifique os registros DNS na Vercel

### ❌ "Erro 404 em /alertas"
- Limpe o cache do navegador (Ctrl + Shift + Delete)
- Faça um novo push para o GitHub para triggerar rebuild

---

## 📞 Próximos Passos

1. ✅ Teste o login com a senha configurada
2. ✅ Importe seus dados de aluguéis
3. ✅ Configure alertas para aluguéis vencidos
4. ✅ Gere seus primeiros recibos em PDF
5. ✅ Compartilhe o link com sua equipe

---

## 🔐 Dicas de Segurança

- ✅ Use senhas fortes para `JWT_SECRET`
- ✅ Mantenha o repositório GitHub como **Private**
- ✅ Nunca compartilhe suas variáveis de ambiente
- ✅ Use HTTPS sempre (Vercel faz isso automaticamente)

---

**Sucesso no deploy! 🚀**
