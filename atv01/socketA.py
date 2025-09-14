import socket
import time

HOST_A = '192.168.0.47'
HOST_B = '192.168.0.50'
PORTA_A = 65432
PORTA_B = 65433


while True:
    # Passo 1: Age como SERVIDOR - Recebe uma mensagem
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST_A, PORTA_A))
            s.listen()
            print("Processo A: Servidor escutando...")
            conn, addr = s.accept()
            with conn:
                print(f"Processo A: Conexão recebida de {addr}")
                data = conn.recv(1024)
                if not data:
                    continue
                print(f"Processo A: Mensagem recebida: '{data.decode()}'")
    except Exception as e:
        print(f"Processo A: Erro no modo servidor: {e}")
        time.sleep(1)
        continue

    # Passo 2: Age como CLIENTE - Envia uma mensagem
    try:
        time.sleep(1)  # Aguarda para garantir que o Servidor B esteja pronto
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST_B, PORTA_B))
            mensagem = input('Processo A: Digite sua mensagem para B: ')
            s.sendall(mensagem.encode())
            print(
                f"Processo A: Mensagem enviada para o Processo B: '{mensagem}'")
    except ConnectionRefusedError:
        print("Processo A: Conexão com o Processo B recusada. Tentando novamente...")
        time.sleep(1)
        continue
    except Exception as e:
        print(f"Processo A: Erro no modo cliente: {e}")
        time.sleep(1)
        continue
