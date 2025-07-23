import socket
import chess

board=chess.Board()


# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP local
PORT = 65432        # Porta do servidor

# Criação do socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Esperando jogador...")
    conn, addr = s.accept()
    with conn:
        print(f'Recebendo movimentos de {addr}')
        while True:
            player_move = conn.recv(1024).decode('utf-8')
            print(player_move)
            if not player_move:
                break

            player_move_uci=chess.Move.from_uci(player_move)
            if player_move_uci in board.legal_moves:
                board.push(player_move_uci)
                print(f"Lance: {player_move}")
                conn.sendall(player_move.encode())
            else:
                print(f"Lance  ilegal: {player_move}")
                conn.sendall('Lance ilegal'.encode())