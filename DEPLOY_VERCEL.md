# Guia de Deploy em Vercel - Aluguel Manager

Este guia descreve como publicar o sistema Aluguel Manager na Vercel com seu domínio customizado **mesquitaimoveis.manus.space**.

## 📋 Pré-requisitos

1. **Conta GitHub** (gratuita em https://github.com)
2. **Conta Vercel** (gratuita em https://vercel.com)
3. **Domínio registrado** (mesquitaimoveis.manus.space)
4. **Banco de Dados MySQL** em nuvem (recomendado: PlanetScale, AWS RDS ou similar)

## 🚀 Passo 1: Preparar o Banco de Dados em Nuvem

### Opção A: PlanetScale (Recomendado - Gratuito)
1. Acesse https://planetscale.com e crie uma conta.
2. Crie um novo banco de dados chamado `aluguel_manager`.
3. Copie a string de conexão MySQL (DATABASE_URL).
4. Execute as migrações SQL fornecidas no projeto.

### Opção B: AWS RDS
1. Crie uma instância MySQL no AWS RDS.
2. Configure a segurança e copie a string de conexão.

## 🔧 Passo 2: Fazer Upload do Código para GitHub

1. **Crie um repositório no GitHub**:
   - Acesse https://github.com/new
   - Nome: `aluguel-manager`
   - Descrição: "Sistema de Gerenciamento de Aluguéis"
   - Deixe como **Public** ou **Private** (sua escolha)
   - Clique em "Create repository"

2. **Faça push do código**:
   ```bash
   cd /caminho/para/aluguel-manager
   git remote add origin https://github.com/seu-usuario/aluguel-manager.git
   git branch -M main
   git push -u origin main
   ```

## 🎯 Passo 3: Deploy na Vercel

1. **Acesse https://vercel.com/dashboard**
2. Clique em **"New Project"**
3. Selecione **"Import Git Repository"**
4. Procure por `aluguel-manager` e clique em **"Import"**
5. Configure as variáveis de ambiente:
   - `DATABASE_URL`: Sua string de conexão MySQL
   - `JWT_SECRET`: Uma chave secreta (ex: `sua-chave-super-secreta-2024`)
   - `LOCAL_AUTH_PASSWORD`: `admin123` (ou outra senha)
   - `NODE_ENV`: `production`
6. Clique em **"Deploy"**

## 🌐 Passo 4: Conectar o Domínio

1. **Na Vercel**, vá para **"Settings"** > **"Domains"**
2. Clique em **"Add Domain"**
3. Digite: `mesquitaimoveis.manus.space`
4. Siga as instruções para apontar o DNS:
   - Se seu domínio está no **Manus**, adicione os registros DNS fornecidos pela Vercel.
   - Se está em outro registrador, configure os CNAME records.

## 📝 Variáveis de Ambiente

Certifique-se de configurar todas essas variáveis na Vercel:

```env
DATABASE_URL=mysql://usuario:senha@host:3306/aluguel_manager
JWT_SECRET=sua-chave-secreta-super-segura-aqui
LOCAL_AUTH_PASSWORD=admin123
NODE_ENV=production
```

## 🔐 Segurança

- **Nunca** compartilhe suas variáveis de ambiente.
- Use senhas fortes para `JWT_SECRET` e `LOCAL_AUTH_PASSWORD`.
- Mantenha seu banco de dados MySQL seguro com firewall.

## 🆘 Troubleshooting

### Erro: "Database connection failed"
- Verifique se a string `DATABASE_URL` está correta.
- Certifique-se de que o banco de dados está acessível da Vercel (firewall).

### Erro: "Build failed"
- Verifique se todas as dependências estão no `package.json`.
- Rode `pnpm install && pnpm build` localmente para testar.

### Domínio não funciona
- Aguarde 24-48 horas para propagação DNS.
- Verifique os registros DNS na Vercel.

## 📞 Suporte

Se tiver dúvidas, consulte:
- Documentação Vercel: https://vercel.com/docs
- Documentação PlanetScale: https://planetscale.com/docs
