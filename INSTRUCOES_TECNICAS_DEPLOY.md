# 🚀 Guia Técnico de Deploy - Aluguel Manager (mesquitaimoveis.com)

Este documento fornece as instruções essenciais para um profissional de TI realizar o deploy do sistema **Aluguel Manager** no domínio **mesquitaimoveis.com**, garantindo total independência e removendo qualquer referência a ambientes de desenvolvimento temporários.

---

## 📋 Visão Geral do Projeto

O **Aluguel Manager** é um sistema web para gerenciamento de imóveis, inquilinos e pagamentos, com funcionalidades como:
- Dashboard com alertas de aluguéis vencidos.
- Cadastro e gestão de imóveis e inquilinos.
- Controle mensal de pagamentos.
- Geração de recibos em PDF com opção de envio via WhatsApp.
- Importação de dados via planilha Excel.

### 🛠️ Stack Tecnológica
- **Frontend**: React 19, TypeScript, Tailwind CSS, Vite.
- **Backend**: Node.js, Express, tRPC, Zod.
- **Banco de Dados**: MySQL / MariaDB (Drizzle ORM).

---

## 🔧 Requisitos do Servidor

Para um deploy bem-sucedido, o servidor deve atender aos seguintes requisitos:
- **Sistema Operacional**: Linux (Ubuntu, CentOS, etc.)
- **Node.js**: Versão 20 ou superior.
- **Gerenciador de Pacotes**: `pnpm` (recomendado) ou `npm`.
- **Banco de Dados**: MySQL ou MariaDB (versão 8+).
- **Servidor Web**: Nginx ou Apache (para proxy reverso e SSL).
- **Git**: Para controle de versão (opcional, mas recomendado para futuras atualizações).

---

## 🚀 Passos para o Deploy

### 1. Preparação do Servidor

Certifique-se de que o servidor tenha Node.js, pnpm e MySQL/MariaDB instalados e configurados.

```bash
# Exemplo de instalação de pnpm (se não estiver instalado)
curl -fsSL https://get.pnpm.io/install.sh | sh -

# Exemplo de instalação de MySQL (se não estiver instalado)
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

### 2. Configuração do Banco de Dados

1.  **Crie um banco de dados** e um usuário com permissões para ele:
    ```sql
    CREATE DATABASE aluguel_manager;
    CREATE USER 'aluguel'@'localhost' IDENTIFIED BY 'sua_senha_segura';
    GRANT ALL PRIVILEGES ON aluguel_manager.* TO 'aluguel'@'localhost';
    FLUSH PRIVILEGES;
    ```
    *Substitua `sua_senha_segura` por uma senha forte.*

2.  **Importe o backup dos dados** fornecido (`aluguel_manager_backup.sql`):
    ```bash
    mysql -u aluguel -p sua_senha_segura aluguel_manager < /caminho/para/aluguel_manager_backup.sql
    ```

### 3. Configuração do Projeto

1.  **Extraia o arquivo ZIP** (`aluguel-manager-pronto-deploy.zip`) para um diretório no servidor (ex: `/var/www/mesquitaimoveis`).
2.  Navegue até o diretório do projeto:
    ```bash
    cd /var/www/mesquitaimoveis
    ```
3.  **Instale as dependências**:
    ```bash
    pnpm install
    ```
4.  **Crie o arquivo de variáveis de ambiente** `.env` na raiz do projeto:
    ```env
    DATABASE_URL="mysql://aluguel:sua_senha_segura@localhost:3306/aluguel_manager"
    JWT_SECRET="uma-chave-secreta-muito-longa-e-complexa-para-jwt"
    LOCAL_AUTH_PASSWORD="admin123" # Senha para o login local
    NODE_ENV="production"
    ```
    *Substitua `sua_senha_segura` e `uma-chave-secreta-muito-longa-e-complexa-para-jwt` por valores seguros.*

### 4. Build e Início do Servidor

1.  **Compile o projeto** para produção:
    ```bash
    pnpm build
    ```
2.  **Inicie o servidor backend** (recomenda-se usar um gerenciador de processos como PM2):
    ```bash
    # Instalar PM2 globalmente (se não tiver)
    pnpm add -g pm2

    # Iniciar o servidor com PM2
    pm2 start server/_core/index.ts --name "aluguel-manager-backend" --interpreter tsx

    # Salvar a configuração do PM2 para reiniciar automaticamente
    pm2 save
    pm2 startup
    ```
    O servidor estará rodando na porta `3000` por padrão.

### 5. Configuração do Servidor Web (Nginx - Exemplo)

Para que o sistema seja acessível via `mesquitaimoveis.com` e tenha HTTPS, configure um proxy reverso com Nginx:

1.  **Crie um arquivo de configuração** para o Nginx (ex: `/etc/nginx/sites-available/mesquitaimoveis.com`):
    ```nginx
    server {
        listen 80;
        server_name mesquitaimoveis.com www.mesquitaimoveis.com;

        location / {
            proxy_pass http://localhost:3000; # Porta do seu backend Node.js
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
    }
    ```

2.  **Ative a configuração** e reinicie o Nginx:
    ```bash
    sudo ln -s /etc/nginx/sites-available/mesquitaimoveis.com /etc/nginx/sites-enabled/
    sudo nginx -t
    sudo systemctl restart nginx
    ```

3.  **Configure HTTPS com Certbot (Let's Encrypt)**:
    ```bash
    sudo snap install --classic certbot
    sudo certbot --nginx -d mesquitaimoveis.com -d www.mesquitaimoveis.com
    ```
    Siga as instruções do Certbot para finalizar a configuração SSL.

### 6. Configuração de DNS

No painel do seu registrador de domínio (onde você comprou `mesquitaimoveis.com`):
- Crie um registro **A** apontando `mesquitaimoveis.com` para o **endereço IP do seu servidor**.
- Crie um registro **CNAME** apontando `www.mesquitaimoveis.com` para `mesquitaimoveis.com`.

**Aguarde a propagação do DNS** (pode levar algumas horas).

---

## ✅ Verificação Final

Após todos os passos, o sistema estará acessível em `https://mesquitaimoveis.com`.

- **Login**: Use a senha configurada em `LOCAL_AUTH_PASSWORD` (padrão: `admin123`).
- **Rotas**: `/`, `/alertas`, `/imoveis`, `/inquilinos`, `/pagamentos`, `/recibos`, `/relatorios`, `/importar`.

---

## 🆘 Suporte

Em caso de dúvidas ou problemas, consulte a documentação das ferramentas utilizadas (Node.js, MySQL, Nginx, PM2) ou entre em contato com um profissional de TI.

---

**Autor**: Manus AI
**Data**: 30 de Março de 2026
