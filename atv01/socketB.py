import socket
import time

HOST_A = '192.168.0.47'
HOST_B = '192.168.0.50'
PORTA_A = 65432
PORTA_B = 65433


while True:
    # Passo 1: Age como CLIENTE - Envia uma mensagem
    try:
        time.sleep(1)  # Aguarda para garantir que o Servidor A esteja pronto
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST_A, PORTA_A))
            mensagem = input('Processo B: Digite sua mensagem para A: ')
            s.sendall(mensagem.encode())
            print(
                f"Processo B: Mensagem enviada para o Processo A: '{mensagem}'")
    except ConnectionRefusedError:
        print("Processo B: Conexão com o Processo A recusada. Tentando novamente...")
        time.sleep(1)
        continue
    except Exception as e:
        print(f"Processo B: Erro no modo cliente: {e}")
        time.sleep(1)
        continue

    # Passo 2: Age como SERVIDOR - Recebe uma mensagem
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST_B, PORTA_B))
            s.listen()
            print("Processo B: Servidor escutando...")
            conn, addr = s.accept()
            with conn:
                print(f"Processo B: Conexão recebida de {addr}")
                data = conn.recv(1024)
                if not data:
                    continue
                print(f"Processo B: Mensagem recebida: '{data.decode()}'")
    except Exception as e:
        print(f"Processo B: Erro no modo servidor: {e}")
        time.sleep(1)
        continue
