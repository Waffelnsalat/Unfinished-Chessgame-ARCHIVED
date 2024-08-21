chess_board = [['' for j in range(8)] for i in range(8)]

# Define the initial positions of the chess pieces
chess_board[0][0] = 'Rb'
chess_board[0][1] = 'Nb'
chess_board[0][2] = 'Bb'
chess_board[0][3] = 'Qb'
chess_board[0][4] = 'Kb'
chess_board[0][5] = 'Bb'
chess_board[0][6] = 'Nb'
chess_board[0][7] = 'Rb'
chess_board[1][0] = 'Pb'
chess_board[1][1] = 'Pb'
chess_board[1][2] = 'Pb'
chess_board[1][3] = 'Pb'
chess_board[1][4] = 'Pb'
chess_board[1][5] = 'Pb'
chess_board[1][6] = 'Pb'
chess_board[1][7] = 'Pb'
chess_board[6][0] = 'Pw'
chess_board[6][1] = 'Pw'
chess_board[6][2] = 'Pw'
chess_board[6][3] = 'Pw'
chess_board[6][4] = 'Pw'
chess_board[6][5] = 'Pw'
chess_board[6][6] = 'Pw'
chess_board[6][7] = 'Pw'
chess_board[7][0] = 'Rw'
chess_board[7][1] = 'Nw'
chess_board[7][2] = 'Bw'
chess_board[7][3] = 'Qw'
chess_board[7][4] = 'Kw'
chess_board[7][5] = 'Bw'
chess_board[7][6] = 'Nw'
chess_board[7][7] = 'Rw'

# Add a false value for each piece indicating whether it has moved from its starting position
first_move_done = {'Pw': [False] * 8, 'Pb': [False] * 8, 'Rw': [False] * 2, 'Rb': [False] * 2, 'Nw': [False] * 2,
                   'Nb': [False] * 2, 'Bw': [False] * 2, 'Bb': [False] * 2, 'Qw': [False], 'Qb': [False], 'Kw': [False],
                   'Kb': [False]}


def has_moved(piece, row4, col4):
    if 'P' in piece:
        if not first_move_done[piece][col4]:
            if abs(row4 - (6 if 'w' in piece else 1)) >= 2:
                first_move_done[piece][col4] = True
                return True
            elif abs(row4 - (6 if 'w' in piece else 1)) == 1:
                first_move_done[piece][col4] = True
                return True
        return first_move_done[piece][col4]
    elif 'K' in piece:
        if not first_move_done[piece][0]:
            first_move_done[piece][0] = True
            return True
        return first_move_done[piece][0]
    elif 'Q' in piece:
        if not first_move_done[piece][0]:
            first_move_done[piece][0] = True
            return True
        return first_move_done[piece][0]
    elif 'R' in piece:
        if col4 in [0, 7]:
            idx = 0 if col4 == 0 else 1
            if not first_move_done[piece][idx]:
                first_move_done[piece][idx] = True
                return True
            return first_move_done[piece][idx]
        return False
    elif 'B' in piece or 'N' in piece:
        return False

print(first_move_done)

if first_move_done["Kw"][0]:
    print("hello")
    print(first_move_done["Rw"])
