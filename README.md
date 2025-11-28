# 🤖 Bot do Telegram — Sistema Cliente/Servidor com Sockets TCP

Este projeto implementa um sistema completo de **monitoramento remoto** baseado em comunicação **cliente/servidor via Sockets TCP**, integrado a um **Bot do Telegram** que permite enviar comandos e receber respostas diretamente pelo chat.

A solução foi desenvolvida para ser **simples, funcional e expansível**, permitindo gerenciar vários clientes simultaneamente.

---

## 🧩 Arquitetura do Sistema

O sistema é composto por três módulos principais:

### 🔹 Cliente (Agente)
- Conecta-se automaticamente ao servidor.
- Envia hostname, IP, usuário logado e outras informações.
- Aguarda comandos do servidor e retorna os dados solicitados.
- Faz reconexão automática em caso de falha.

### 🔹 Servidor
- Aceita múltiplas conexões simultâneas.
- Mantém tabela de clientes conectados.
- Encaminha comandos para os clientes.
- Retorna respostas diretamente ao Bot do Telegram.

### 🔹 Bot do Telegram
- Interface principal para o administrador.
- Envia comandos ao servidor e exibe respostas do cliente.
- Permite monitoramento completo via Telegram.

---

## 🔄 Fluxo de Comunicação

1. O **cliente** conecta-se ao **servidor** e registra suas informações.
2. O **bot do Telegram** recebe comandos do usuário.
3. O bot envia o comando ao **servidor**.
4. O servidor repassa o comando ao **cliente** correto.
5. O cliente executa e envia a resposta ao servidor.
6. O servidor devolve a resposta ao bot.
7. O bot apresenta o resultado ao usuário.

---

## ✨ Funcionalidades

### 🟦 Cliente (Agente)
- Registro automático no servidor.
- Execução contínua em segundo plano.
- Retorno de informações como:
  - Sistema operacional
  - Programas instalados
  - Usuário logado
  - Histórico de navegação
- Reconexão automática.

### 🟥 Servidor
- Gerencia múltiplos clientes simultaneamente.
- Mantém status online/offline atualizado.
- Interage diretamente com o bot do Telegram.
- Processa e encaminha comandos.

### 🟩 Bot do Telegram

Comandos disponíveis:

| Comando | Função |
|--------|--------|
| `/start` | Inicia a interação |
| `/?` | Lista os comandos disponíveis |
| `/clientes` | Lista os clientes conectados |
| `/info` | Mostra informações detalhadas do cliente |
| `/status` | Verifica se o cliente está ativo |
| `/ping` | Testa comunicação com o cliente |
| `/programas` | Lista programas instalados |
| `/historico` | Mostra histórico de navegação |
| `/usuario` | Exibe o usuário logado |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Sockets TCP**
- **Threading**
- **Telegram Bot API**
- **Subprocess**
- **Platform**
- **Time**
- **Requests**
- **OS**

---

## 🚀 Como Executar o Projeto

### 1️⃣ Servidor

```sh
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
pip install -r requirements.txt

Configure o token do bot no arquivo config.py:

TOKEN = "SEU_TOKEN_AQUI"


Execute o servidor:

python servidor-bot.py

2️⃣ Cliente
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git


Configure o IP do servidor:

SERVER_IP = "IP_DO_SERVIDOR"
SERVER_PORT = 5000


Execute o cliente:

python cliente.py

3️⃣ Interagir pelo Telegram

Abra o Telegram.

Procure pelo bot @thaynahakanbot.

Envie /start.

Utilize os comandos disponíveis.

🎥 Demonstração

Passos para teste:

Inicie o servidor.

Execute ao menos um cliente.

Abra o bot no Telegram.

Use comandos como /info, /status, /clientes.

Observe as respostas em tempo real.

📝 Considerações Finais

Este projeto oferece uma arquitetura sólida e prática para monitoramento remoto multinível, utilizando Sockets TCP, Threads e Telegram Bot.

Sinta-se à vontade para contribuir, abrir issues, criar melhorias e adaptar à sua necessidade.




![imagembot](https://github.com/user-attachments/assets/9c3960fd-7c3c-450c-ac18-c4c7937d2b43)


