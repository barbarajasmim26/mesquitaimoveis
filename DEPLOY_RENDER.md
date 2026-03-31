# 🚀 Guia de Deploy - Aluguel Manager no Render.com

Este guia detalha como realizar o deploy do sistema **Aluguel Manager** na plataforma **Render.com**, incluindo todas as configurações necessárias para um ambiente de produção estável e funcional no seu domínio **mesquitaimoveis.com**.

---

## 📋 Visão Geral do Render.com

O Render.com é uma plataforma de nuvem unificada que permite hospedar aplicações web, bancos de dados e outros serviços. Ele simplifica o deploy contínuo a partir de repositórios Git, automatizando o processo de build e disponibilizando sua aplicação online.

---

## 🔧 Pré-requisitos

- ✅ Conta **GitHub** (onde o código será hospedado).
- ✅ Conta **Render.com** (gratuita ou paga, dependendo da necessidade).
- ✅ Domínio **mesquitaimoveis.com** registrado e acesso ao painel de DNS.
- ✅ Banco de dados **MySQL** em nuvem (ex: PlanetScale, Render Managed Database, AWS RDS).

---

## 🚀 Passos para o Deploy

### 1. Preparar o Banco de Dados MySQL

Se você já tem um banco de dados MySQL no PlanetScale ou AWS RDS, use-o. Caso contrário, o Render oferece um serviço de banco de dados gerenciado:

1.  No painel do Render, vá em **"New"** > **"MySQL"**.
2.  Configure o nome, usuário e senha.
3.  **Copie a URL de conexão** do MySQL. Ela será usada como `DATABASE_URL`.
4.  **Importe o backup do banco de dados** (`aluguel_manager_backup.sql`) para o seu novo banco de dados MySQL. Você pode usar ferramentas como MySQL Workbench ou o cliente `mysql` via linha de comando.

### 2. Fazer Upload do Código para o GitHub

1.  **Crie um repositório privado no GitHub** (se ainda não o fez) chamado `aluguel-manager`.
2.  **Faça o upload de todo o conteúdo do arquivo ZIP** que você recebeu para este repositório. Certifique-se de que a pasta `patches/`, `pnpm-lock.yaml`, `package.json`, `vite.config.ts`, `client/` e `server/` estejam presentes.

### 3. Criar um Novo Serviço Web no Render

1.  No painel do Render, clique em **"New"** > **"Web Service"**.
2.  **Conecte seu repositório GitHub** `aluguel-manager`.
3.  **Configure o serviço web** com as seguintes opções:

    | Configuração         | Valor Sugerido                                    |
    | :------------------- | :------------------------------------------------ | 
    | **Name**             | `aluguel-manager`                                 |
    | **Region**           | Escolha a mais próxima dos seus usuários (ex: `Ohio (us-east-2)`) |
    | **Branch**           | `main`                                            |
    | **Root Directory**   | `/` (se o projeto estiver na raiz do repositório) |
    | **Runtime**          | `Node`                                            |
    | **Build Command**    | `pnpm install && pnpm build`                      |
    | **Start Command**    | `pnpm start`                                      |
    | **Instance Type**    | `Free` (para testes) ou `Starter` (para produção) |

### 4. Configurar Variáveis de Ambiente

No Render, vá para a seção **"Environment"** do seu serviço web e adicione as seguintes variáveis:

| Variável              | Valor                                                                                                                              |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `DATABASE_URL`        | A URL de conexão do seu banco de dados MySQL (ex: `mysql://user:pass@host/aluguel_manager`)                                        |
| `JWT_SECRET`          | Uma chave secreta forte e única (ex: `sua-chave-secreta-muito-longa-e-complexa-para-jwt`)                                            |
| `LOCAL_AUTH_PASSWORD` | A senha para o login local no sistema (ex: `admin123`)                                                                             |
| `NODE_ENV`            | `production`                                                                                                                       |
| `PORT`                | `10000` (O Render usa essa porta internamente. O sistema será exposto na porta 80/443 publicamente)                               |

### 5. Conectar o Domínio mesquitaimoveis.com

1.  No Render, vá para a seção **"Settings"** do seu serviço web.
2.  Em **"Custom Domains"**, clique em **"Add Custom Domain"**.
3.  Digite `mesquitaimoveis.com` e `www.mesquitaimoveis.com`.
4.  O Render fornecerá os registros DNS (geralmente `CNAME` ou `A record`) que você precisará adicionar no painel do seu registrador de domínio (onde você comprou `mesquitaimoveis.com`).
5.  **Aguarde a propagação do DNS** (pode levar de alguns minutos a algumas horas).

---

## ✅ Verificação Final

Após a propagação do DNS, seu sistema estará acessível em `https://mesquitaimoveis.com` e `https://www.mesquitaimoveis.com`.

-   **Login**: Use a senha configurada em `LOCAL_AUTH_PASSWORD` (padrão: `admin123`).
-   **Rotas**: `/`, `/alertas`, `/imoveis`, `/inquilinos`, `/pagamentos`, `/recibos`, `/relatorios`, `/importar`.

---

## 🆘 Troubleshooting Comum

-   **Build falhou**: Verifique os logs de build no Render. Certifique-se de que todas as dependências estão no `package.json` e que o `pnpm-lock.yaml` está correto.
-   **Erro de conexão com o banco de dados**: Verifique a `DATABASE_URL` e as permissões do usuário do banco de dados. Certifique-se de que o banco de dados está acessível externamente.
-   **Domínio não funciona**: Verifique se os registros DNS foram configurados corretamente no seu registrador de domínio e aguarde a propagação.
-   **Erro 404 em rotas**: Limpe o cache do navegador. Verifique se o `Start Command` está correto e se o servidor está rodando na porta esperada pelo Render (PORT `10000`).

---

**Autor**: Manus AI
**Data**: 30 de Março de 2026
