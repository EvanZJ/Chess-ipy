import chess
arr = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
        ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
        ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
        ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
        ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
        ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
        ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
        ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]] 
print(arr[0][1])

board = chess.Board()
selected_square = chess.parse_square("b1")
legal_moves = board.legal_moves
for move in legal_moves:
    if move.from_square == chess.parse_square("a2"):
        print(move.to_square)

board.push(chess.Move(chess.parse_square("a2"), chess.parse_square("a3")))
print(board)
print(board.ep_square)

white_box_coordinate = [["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
                        ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
                        ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
                        ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
                        ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
                        ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
                        ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
                        ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]

board.piece_map()

print(white_box_coordinate[0][1])

# my_dict = {
#     'key1': lambda: print('Lambda function 1 called'),
#     'key2': lambda: print('Lambda function 2 called'),
#     'key3': lambda: print('Lambda function 3 called')
# }

# # Call the lambda function associated with 'key1'
# my_dict['key1']()  # Output: Lambda function 1 called

# # Call the lambda function associated with 'key2'
# my_dict['key2']()  # Output: Lambda function 2 called

# # Call the lambda function associated with 'key3'
# my_dict['key3']()  # Output: Lambda function 3 called