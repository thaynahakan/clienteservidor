🤖 Bot do Telegram — Sistema Cliente/Servidor com Sockets TCP

Este projeto implementa um sistema completo de monitoramento remoto baseado em comunicação cliente/servidor via Sockets TCP, integrado a um Bot do Telegram que permite enviar comandos e receber respostas diretamente pelo chat.

A solução foi pensada para ser simples, funcional e expansível, permitindo gerenciar vários clientes simultaneamente.

🧩 Arquitetura do Sistema

O projeto é composto por três partes principais:

🔹 Cliente (Agente)

Conecta-se automaticamente ao servidor.

Envia informações do sistema: hostname, IP, usuário logado.

Aguarda comandos do servidor e responde com os dados solicitados.

Rebate tenta reconectar caso a conexão caia.

🔹 Servidor

Aceita múltiplas conexões simultâneas.

Roteia comandos enviados pelo bot aos clientes.

Mantém o status (online/offline) dos clientes.

Envia as informações coletadas de volta ao bot.

🔹 Bot do Telegram

Interface principal do administrador.

Recebe comandos, encaminha ao servidor e retorna a resposta.

Permite verificar status, listar clientes, solicitar informações e muito mais.

🔄 Fluxo de Comunicação

O cliente conecta-se ao servidor e registra suas informações.

O bot do Telegram recebe comandos do usuário.

O bot envia esses comandos ao servidor.

O servidor direciona o comando ao cliente correto.

O cliente executa o comando e envia a resposta ao servidor.

O servidor devolve a resposta ao bot.

O bot mostra o resultado ao usuário no Telegram.

✨ Funcionalidades
🟦 Cliente (Agente)

Registro automático (hostname, IP, usuário).

Execução contínua em segundo plano.

Resposta a comandos remotos:

Informações do sistema

Programas instalados

Histórico de navegação

Status de conexão

Reconexão automática em caso de queda.

🟥 Servidor

Gerencia múltiplas conexões simultâneas (multi-thread).

Mantém a tabela de clientes online/offline.

Roteia comandos para os clientes ativos.

Interface com o bot do Telegram.

🟩 Bot do Telegram

Comandos disponíveis:

Comando	Função
/start	Inicia interação
/?	Lista comandos disponíveis
/clientes	Mostra todos os clientes conectados
/info	Exibe informações detalhadas do cliente
/status	Mostra status do cliente
/ping	Testa comunicação
/programas	Retorna lista de programas instalados
/historico	Envia histórico de navegação do cliente
/usuario	Retorna o usuário logado
🛠️ Tecnologias Utilizadas

Python 3.x

Sockets TCP

Threading

Telegram Bot API

Subprocess / platform / os

Requests

time & socket

🚀 Como Executar o Projeto
1️⃣ Configurar o Servidor
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
pip install -r requirements.txt


Configure o token do bot em config.py:

TOKEN = "SEU_TOKEN_AQUI"


Execute o servidor:

python servidor-bot.py

2️⃣ Configurar os Clientes

Em cada máquina cliente:

git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git


Edite o arquivo config.py:

SERVER_IP = "IP_DO_SERVIDOR"
SERVER_PORT = 5000


Execute o cliente:

python cliente.py

3️⃣ Interagir via Telegram

Abra o Telegram.

Procure pelo bot @thaynahakanbot.

Envie /start.

Use os comandos para controlar os clientes.

🎥 Demonstração

Passos para demonstrar:

Inicie o servidor.

Conecte ao menos um cliente.

Abra o bot no Telegram.

Execute comandos como /info, /status, /clientes, etc.

Veja as respostas do sistema em tempo real.

📝 Considerações Finais

Este projeto oferece uma base sólida para um sistema de monitoramento remoto, utilizando ferramentas simples (sockets + Telegram) e arquitetura modular. É ideal para estudos, laboratórios e aplicações personalizadas.

Sinta-se à vontade para contribuir, sugerir melhorias e adaptar ao seu próprio cenário! 🚀
![imagembot](https://github.com/user-attachments/assets/9c3960fd-7c3c-450c-ac18-c4c7937d2b43)


