import socket
import chess

HOST = '127.0.0.1'  # IP do servidor
PORT = 65432        # Mesma porta usada pelo servidor


#Conecta com servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    #Inicializa o tabuleiro
    board=chess.Board()
    print(board)

    #Envia o lance
    while True:
        msg = input("Digite um lance (ou 'sair'): ")
        if msg.lower() == 'sair':
            break
        s.sendall(msg.encode())

        #Recebe a resposta do servidor
        server_move = s.recv(1024).decode("utf-8")

        #Se lance ilegal, pede novo movimento
        if server_move == "Lance ilegal":
            print("Lance ilegal")
            continue
    
        #Se lance legal, realiza movimento no tabuleiro local
        server_move_uci=chess.Move.from_uci(server_move)
        board.push(server_move_uci)
        print(f"Lance confirmado: {server_move}")
        print(board)
