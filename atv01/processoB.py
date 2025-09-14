import socket
import threading
import time

HOST_B = '0.0.0.0'
HOST_A = '192.168.1.100'
PORTA_A = 65432
PORTA_B = 65433


def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST_B, PORTA_B))
        s.listen()
        print(f"Processo B: Servidor escutando em {HOST_B}:{PORTA_B}")
        conn, addr = s.accept()
        with conn:
            print(f"Processo B: Conexão recebida de {addr}")
            data = conn.recv(1024)
            print(f"Processo B: Mensagem recebida: '{data.decode()}'")


def cliente():
    time.sleep(1)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST_A, PORTA_A))
        mensagem = "Olá do Processo B!"
        s.sendall(mensagem.encode())
        print(f"Processo B: Mensagem enviada para o Processo A: '{mensagem}'")


thread_servidor = threading.Thread(target=servidor)
thread_cliente = threading.Thread(target=cliente)

thread_cliente.start()
thread_servidor.start()

thread_cliente.join()
thread_servidor.join()

print("Processo B: Atividade concluída.")
