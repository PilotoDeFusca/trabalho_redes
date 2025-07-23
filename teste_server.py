import socket
import chess



# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP local
PORT = 65432        # Porta do servidor

# Criação do socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    #Escuta
    while True:  
        s.listen()
        print("Esperando jogador...")

        #Aceita a conexão com o jogador
        conn, addr = s.accept()

        #Conectado ao jogador
        with conn:
            print(f'Recebendo movimentos de {addr}')

            #Inicia o tabuleiro global
            board=chess.Board()

            #Receber o lance do jogador ou sair
            while True:
                player_move = conn.recv(1024).decode('utf-8')
                if not player_move:
                    break

                #Verifica o lance e responde
                player_move_uci=chess.Move.from_uci(player_move)
                if player_move_uci in board.legal_moves:
                    board.push(player_move_uci)
                    print(f"Lance: {player_move}")
                    conn.sendall(player_move.encode())
                else:
                    print(f"Lance  ilegal: {player_move}")
                    conn.sendall('Lance ilegal'.encode())

        #Jogador sai, retorna a escutar
        print('Jogador desconectado')