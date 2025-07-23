import socket
import chess

HOST = '127.0.0.1'  # IP do servidor
PORT = 65432        # Mesma porta usada pelo servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    board=chess.Board()
    while True:

        msg = input("Digite um lance (ou 'sair'): ")
        if msg.lower() == 'sair':
            break

        s.sendall(msg.encode())
        server_move = s.recv(1024).decode("utf-8")

        if server_move == "Lance ilegal":
            print("Lance ilegal")
            continue

        server_move_uci=chess.Move.from_uci(server_move)
        board.push(server_move_uci)
        print(f"Lance confirmado: {server_move}")
        print(board)
