import socket
import threading
import time

HOST_A = '0.0.0.0'  # Aceita conexões de qualquer IP
HOST_B = '192.168.1.200'  # IP da máquina onde o Processo B está
PORTA_A = 65432
PORTA_B = 65433


def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST_A, PORTA_A))
        s.listen()
        print(f"Processo A: Servidor escutando em {HOST_A}:{PORTA_A}")
        conn, addr = s.accept()
        with conn:
            print(f"Processo A: Conexão recebida de {addr}")
            data = conn.recv(1024)
            print(f"Processo A: Mensagem recebida: '{data.decode()}'")


def cliente():
    time.sleep(2)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_B, PORTA_B))
        mensagem = "Olá do Processo A!"
        s.sendall(mensagem.encode())
        print(f"Processo A: Mensagem enviada para o Processo B: '{mensagem}'")


thread_servidor = threading.Thread(target=servidor)
thread_cliente = threading.Thread(target=cliente)

thread_servidor.start()
thread_cliente.start()

thread_servidor.join()
thread_cliente.join()

print("Processo A: Atividade concluída.")
