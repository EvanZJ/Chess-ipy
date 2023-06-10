import chess
board = chess.Board()
selected_square = chess.parse_square("h1")
legal_moves = board.legal_moves
print(legal_moves)
print(selected_square)