# Bot do Telegram - cliente/servidor -
Descrição

Este projeto implementa um sistema cliente/servidor para monitoramento remoto de agentes (clientes) utilizando sockets TCP e integração com um bot do Telegram. O servidor gerencia múltiplos clientes conectados e executa comandos remotamente para coletar informações como histórico de navegação, detalhes do sistema operacional e programas instalados.

Arquitetura do Sistema

Componentes

Cliente (Agente): Aplicação que se conecta ao servidor e responde a comandos enviados.
Servidor: Gerencia conexões de múltiplos clientes e executa comandos recebidos via bot do Telegram.
Bot do Telegram: Interface para interação com o servidor, permitindo que usuários enviem comandos e recebam respostas diretamente pelo Telegram.
Fluxo de Comunicação

O cliente inicia e tenta se conectar ao servidor.
O servidor aceita a conexão e mantém a comunicação com o cliente.
O bot do Telegram recebe comandos do usuário e os encaminha para o servidor.
O servidor processa os comandos, os envia ao cliente e retorna a resposta ao bot do Telegram.
O bot responde ao usuário no Telegram com as informações solicitadas.
Funcionalidades

Cliente (Agente)

Registro Automático: Ao iniciar, o cliente se conecta ao servidor e informa seu hostname, IP e usuário logado.
Execução em Segundo Plano: O cliente opera continuamente aguardando comandos do servidor.
Responde a Comandos: O cliente executa comandos recebidos e retorna os resultados ao servidor.
Reenvio Automático: Em caso de falha de conexão, o cliente tenta se reconectar automaticamente.
Servidor-bot

Gerencia Múltiplos Clientes: Aceita conexões de vários agentes simultaneamente.
Monitoramento Ativo: Mantém o status atualizado dos clientes e detecta quando ficam offline.
Interação via Telegram: Executa comandos enviados pelo bot do Telegram e retorna os resultados.
Bot do Telegram

Comandos Disponíveis:
/start - Inicia a interação com o bot.
/? - Exibe a lista de comandos disponíveis.
/clientes - Lista os clientes conectados ao servidor.
/info - Obtém informações detalhadas do sistema do cliente especificado.
/status - Verifica se o cliente está ativo.
/ping - Testa a comunicação com o cliente.
/programas - Lista os programas instalados no cliente.
/historico - Retorna o histórico de navegação do cliente.
/usuario - Obtém informações do usuário logado no cliente.
Tecnologias Utilizadas

Python 3.x - Linguagem principal.
Sockets TCP - Comunicação entre cliente e servidor.
Threading - Gerenciamento de múltiplos clientes simultaneamente.
API do Telegram - Para interação com o bot.
Bibliotecas: requests, socket, threading, time, subprocess, platform, os.
Como Executar o Projeto

1. Configurar o Servidor

Clone o repositório.
Instale as dependências:
pip install -r requirements.txt
Configure o token do bot no arquivo config.py:
TOKEN = "SEU_TOKEN_AQUI"
Execute o servidor:
python servidor-bot.py
2. Configurar os Clientes

Em cada máquina cliente, clone o repositório.
Configure o endereço do servidor no arquivo config.py:
SERVER_IP = "IP_DO_SERVIDOR"
SERVER_PORT = 5000
Execute o cliente:
python cliente.py
3. Interagir via Telegram

No Telegram, encontre o bot thaynahakanbot
Envie /start para iniciar a comunicação.
Utilize os comandos disponíveis para interagir com o sistema.
Demonstração do Projeto

Para demonstrar o funcionamento do sistema:

Execute o servidor.
Conecte pelo menos um cliente.
Envie comandos pelo bot do Telegram.
Verifique as respostas retornadas no Telegram.
Considerações Finais

Este projeto fornece um ambiente de monitoramento remoto simples e eficiente utilizando sockets TCP e Telegram. A abordagem facilita o controle de múltiplos clientes de forma centralizada e segura.
![imagembot](https://github.com/user-attachments/assets/9c3960fd-7c3c-450c-ac18-c4c7937d2b43)


