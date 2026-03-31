import { SignJWT } from './node_modules/jose/dist/node/index.js';
import mysql from './node_modules/mysql2/promise.js';

const JWT_SECRET = 'aluguel-manager-secret-key-2024';
const OPEN_ID = 'local-admin-owner';

async function main() {
  const conn = await mysql.createConnection('mysql://aluguel:aluguel123@localhost:3306/aluguel_manager');
  
  // Criar usuário admin
  await conn.execute(
    `INSERT INTO users (openId, name, email, role, lastSignedIn) VALUES (?, ?, ?, 'admin', NOW())
     ON DUPLICATE KEY UPDATE name=VALUES(name), role='admin', lastSignedIn=NOW()`,
    [OPEN_ID, 'Administrador', 'admin@local.dev']
  );
  
  console.log('Usuário admin criado!');
  
  // Gerar JWT
  const secretKey = new TextEncoder().encode(JWT_SECRET);
  const token = await new SignJWT({
    openId: OPEN_ID,
    appId: 'aluguel-manager-local',
    name: 'Administrador',
  })
    .setProtectedHeader({ alg: 'HS256', typ: 'JWT' })
    .setExpirationTime(Math.floor((Date.now() + 365 * 24 * 60 * 60 * 1000) / 1000))
    .sign(secretKey);
  
  console.log('TOKEN:', token);
  
  await conn.end();
}

main().catch(console.error);
