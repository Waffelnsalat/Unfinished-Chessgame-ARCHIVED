import pygame

# global imported values
global old_col
global old_row

# other values to save
playing_player = "white"

# Initialize Pygame
pygame.init()

# Set the dimensions of the chessboard
board_width = 960
board_height = 960

# Define the colors of the chessboard
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0, 100)

# Create the Pygame window
screen = pygame.display.set_mode((board_width, board_height))

# Set the title of the window
pygame.display.set_caption("Chess Board")

# Define the size of each square on the chessboard
square_size = board_width // 8

# Create a variable to keep track of the color of each square
square_color = white

# Create a 2D list to represent the chessboard and initialize it with empty values
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


# Define a function to get the position of the mouse click on the chessboard
def get_board_position(mouse_pos1):
    row1 = mouse_pos1[1] // square_size
    col1 = mouse_pos1[0] // square_size
    return row1, col1


# Define a function to get the position of the mouse click on the chessboard
def get_valid_moves(piece, row2, col2):
    valid_moves1 = []
    if playing_player == "white":
        if piece == 'Pw':
            # Check if the pawn can move one square forward
            if chess_board[row2 - 1][col2] == '':
                valid_moves1.append((row2 - 1, col2))
            # Check if the pawn can move two squares forward
            if row2 == 6 and chess_board[row2 - 2][col2] == '':
                valid_moves1.append((row2 - 2, col2))
            # Check if the pawn can capture an enemy piece to the left
            if col2 > 0 and chess_board[row2 - 1][col2 - 1] != '' and chess_board[row2 - 1][col2 - 1][1] == 'b':
                valid_moves1.append((row2 - 1, col2 - 1))
            # Check if the pawn can capture an enemy piece to the right
            if col2 < 7 and chess_board[row2 - 1][col2 + 1] != '' and chess_board[row2 - 1][col2 + 1][1] == 'b':
                valid_moves1.append((row2 - 1, col2 + 1))
            # Check for en passant on the left
            if row2 == 3 == last_pawn_move[0] == int(before_pawn_move[0]) + 2:
                if col2 > 0 and chess_board[row2][col2 - 1] != '' and chess_board[row2][col2 - 1][1] == 'b':
                    valid_moves1.append((row2 - 1, col2 - 1))
            # Check for en passant on the right
            if row2 == 3 == last_pawn_move[0] == int(before_pawn_move[0]) + 2:
                if col2 > 0 and chess_board[row2][col2 + 1] != '' and chess_board[row2][col2 + 1][1] == 'b':
                    valid_moves1.append((row2 - 1, col2 + 1))

        elif piece == 'Rw':
            # Check valid moves for a rook
            for i in range(row2 - 1, -1, -1):
                # Check moves up
                if chess_board[i][col2] == '':
                    valid_moves1.append((i, col2))
                elif chess_board[i][col2] != '' and chess_board[i][col2][1] == 'b':
                    valid_moves1.append((i, col2))
                    break
                elif chess_board[i][col2][1] == 'w':
                    break
            for i in range(row2 + 1, 8):
                # Check moves down
                if chess_board[i][col2] == '':
                    valid_moves1.append((i, col2))
                elif chess_board[i][col2] != '' and chess_board[i][col2][1] == 'b':
                    valid_moves1.append((i, col2))
                    break
                elif chess_board[i][col2][1] == 'w':
                    break
            for j in range(col2 - 1, -1, -1):
                # Check moves left
                if chess_board[row2][j] == '':
                    valid_moves1.append((row2, j))
                elif chess_board[row2][j] != '' and chess_board[row2][j][1] == 'b':
                    valid_moves1.append((row2, j))
                    break
                elif chess_board[row2][j][1] == 'w':
                    break
            for j in range(col2 + 1, 8):
                # Check moves right
                if chess_board[row2][j] == '':
                    valid_moves1.append((row2, j))
                elif chess_board[row2][j] != '' and chess_board[row2][j][1] == 'b':
                    valid_moves1.append((row2, j))
                    break
                elif chess_board[row2][j][1] == 'w':
                    break
        elif piece == 'Kw':
            # Check valid moves for a king
            for i in range(max(0, row2 - 1), min(8, row2 + 2)):
                for j in range(max(0, col2 - 1), min(8, col2 + 2)):
                    if chess_board[i][j] == '':
                        valid_moves1.append((i, j))
                    elif chess_board[i][j][1] == 'b':
                        valid_moves1.append((i, j))
                    else:
                        continue
            # Check for right rochade
            if not first_move_done['Kw'][0] and not first_move_done['Rw'][1]:
                if chess_board[7][6] == "" and chess_board[7][5] == "":
                    valid_moves1.append((7, 6))
            if not first_move_done['Kw'][0] and not first_move_done['Rw'][0]:
                if chess_board[7][3] == "" and chess_board[7][2] == "" and chess_board[7][1] == "":
                    valid_moves1.append((7, 2))

        elif piece == 'Nw':
            # Check valid moves for a knight
            for i, j in [(row2 - 2, col2 - 1), (row2 - 2, col2 + 1), (row2 - 1, col2 - 2),
                         (row2 - 1, col2 + 2), (row2 + 1, col2 - 2),
                         (row2 + 1, col2 + 2), (row2 + 2, col2 - 1), (row2 + 2, col2 + 1)]:
                if 0 <= i <= 7 and 0 <= j <= 7:
                    if chess_board[i][j] == '':
                        valid_moves1.append((i, j))
                    elif chess_board[i][j][1] != piece[1] and chess_board[i][j][1] == 'b':
                        valid_moves1.append((i, j))
        elif piece == 'Qw':
            # Check valid moves for a queen (combination of rook and bishop moves)
            for i in range(row2 - 1, -1, -1):
                # Check moves up
                if chess_board[i][col2] == '':
                    valid_moves1.append((i, col2))
                elif chess_board[i][col2][1] == 'b':
                    valid_moves1.append((i, col2))
                    break
                else:
                    break
            for i in range(row2 + 1, 8):
                # Check moves down
                if chess_board[i][col2] == '':
                    valid_moves1.append((i, col2))
                elif chess_board[i][col2][1] == 'b':
                    valid_moves1.append((i, col2))
                    break
                else:
                    break
            for j in range(col2 - 1, -1, -1):
                # Check moves left
                if chess_board[row2][j] == '':
                    valid_moves1.append((row2, j))
                elif chess_board[row2][j][1] == 'b':
                    valid_moves1.append((row2, j))
                    break
                else:
                    break
            for j in range(col2 + 1, 8):
                # Check moves right
                if chess_board[row2][j] == '':
                    valid_moves1.append((row2, j))
                elif chess_board[row2][j][1] == 'b':
                    valid_moves1.append((row2, j))
                    break
                else:
                    break
            for i, j in zip(range(row2 - 1, -1, -1), range(col2 - 1, -1, -1)):
                # Check moves up and left
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'b':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(row2 + 1, 8), range(col2 - 1, -1, -1)):
                # Check moves down and left
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'b':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(row2 - 1, -1, -1), range(col2 + 1, 8)):
                # Check moves up and right
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'b':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(row2 + 1, 8), range(col2 + 1, 8)):
                # Check moves down and right
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'b':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
        elif piece == 'Bw':
            # Check valid moves for a bishop
            # Check moves up and to the left
            i, j = row2 - 1, col2 - 1
            while i >= 0 and j >= 0:
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'b':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
                i -= 1
                j -= 1
            # Check moves up and to the right
            i, j = row2 - 1, col2 + 1
            while i >= 0 and j < 8:
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'b':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
                i -= 1
                j += 1
            # Check moves down and to the left
            i, j = row2 + 1, col2 - 1
            while i < 8 and j >= 0:
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'b':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
                i += 1
                j -= 1
            # Check moves down and to the right
            i, j = row2 + 1, col2 + 1
            while i < 8 and j < 8:
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'b':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
                i += 1
                j += 1
        # Add more code to get valid moves for other chess pieces here
        return valid_moves1
    # Same for the black pieces
    if playing_player == "black":
        if piece == 'Pb':
            # Check if the pawn can move one square forward
            if chess_board[row2 + 1][col2] == '':
                valid_moves1.append((row2 + 1, col2))
            # Check if the pawn can move two squares forward
            if row2 == 1 and chess_board[row2 + 2][col2] == '':
                valid_moves1.append((row2 + 2, col2))
            # Check if the pawn can capture an enemy piece to the left
            if col2 > 0 and chess_board[row2 + 1][col2 - 1] != '' and chess_board[row2 + 1][col2 - 1][1] == 'w':
                valid_moves1.append((row2 + 1, col2 - 1))
            # Check if the pawn can capture an enemy piece to the right
            if col2 < 7 and chess_board[row2 + 1][col2 + 1] != '' and chess_board[row2 + 1][col2 + 1][1] == 'w':
                valid_moves1.append((row2 + 1, col2 + 1))
            # Check for en passant on the left
            if row2 == 4 == last_pawn_move[0] == int(before_pawn_move[0]) - 2:
                if col2 > 0 and chess_board[row2][col2 - 1] != '' and chess_board[row2][col2 - 1][1] == 'w':
                    valid_moves1.append((row2 + 1, col2 - 1))
            # Check for en passant on the right
            if row2 == 4 == last_pawn_move[0] == int(before_pawn_move[0]) - 2:
                if col2 > 0 and chess_board[row2][col2 + 1] != '' and chess_board[row2][col2 + 1][1] == 'w':
                    valid_moves1.append((row2 + 1, col2 + 1))
        elif piece == 'Rb':
            # Check valid moves for a rook
            for i in range(row2 - 1, -1, -1):
                # Check moves up
                if chess_board[i][col2] == '':
                    valid_moves1.append((i, col2))
                elif chess_board[i][col2] != '' and chess_board[i][col2][1] == 'w':
                    valid_moves1.append((i, col2))
                    break
                elif chess_board[i][col2][1] == 'b':
                    break
            for i in range(row2 + 1, 8):
                # Check moves down
                if chess_board[i][col2] == '':
                    valid_moves1.append((i, col2))
                elif chess_board[i][col2] != '' and chess_board[i][col2][1] == 'w':
                    valid_moves1.append((i, col2))
                    break
                elif chess_board[i][col2][1] == 'b':
                    break
            for j in range(col2 - 1, -1, -1):
                # Check moves left
                if chess_board[row2][j] == '':
                    valid_moves1.append((row2, j))
                elif chess_board[row2][j] != '' and chess_board[row2][j][1] == 'w':
                    valid_moves1.append((row2, j))
                    break
                elif chess_board[row2][j][1] == 'b':
                    break
            for j in range(col2 + 1, 8):
                # Check moves right
                if chess_board[row2][j] == '':
                    valid_moves1.append((row2, j))
                elif chess_board[row2][j] != '' and chess_board[row2][j][1] == 'w':
                    valid_moves1.append((row2, j))
                    break
                elif chess_board[row2][j][1] == 'b':
                    break
        elif piece == 'Kb':
            # Check valid moves for a king
            for i in range(max(0, row2 - 1), min(8, row2 + 2)):
                for j in range(max(0, col2 - 1), min(8, col2 + 2)):
                    if chess_board[i][j] == '':
                        valid_moves1.append((i, j))
                    elif chess_board[i][j][1] == 'w':
                        valid_moves1.append((i, j))
                    else:
                        continue
        elif piece == 'Nb':
            # Check valid moves for a knight
            for i, j in [(row2 - 2, col2 - 1), (row2 - 2, col2 + 1), (row2 - 1, col2 - 2), (row2 - 1, col2 + 2),
                         (row2 + 1, col2 - 2),
                         (row2 + 1, col2 + 2), (row2 + 2, col2 - 1), (row2 + 2, col2 + 1)]:
                if 0 <= i <= 7 and 0 <= j <= 7:
                    if chess_board[i][j] == '':
                        valid_moves1.append((i, j))
                    elif chess_board[i][j][1] != piece[1] and chess_board[i][j][1] == 'w':
                        valid_moves1.append((i, j))
        elif piece == 'Qb':
            # Check valid moves for a queen (combination of rook and bishop moves)
            for i in range(row2 - 1, -1, -1):
                # Check moves up
                if chess_board[i][col2] == '':
                    valid_moves1.append((i, col2))
                elif chess_board[i][col2][1] == 'w':
                    valid_moves1.append((i, col2))
                    break
                else:
                    break
            for i in range(row2 + 1, 8):
                # Check moves down
                if chess_board[i][col2] == '':
                    valid_moves1.append((i, col2))
                elif chess_board[i][col2][1] == 'w':
                    valid_moves1.append((i, col2))
                    break
                else:
                    break
            for j in range(col2 - 1, -1, -1):
                # Check moves left
                if chess_board[row2][j] == '':
                    valid_moves1.append((row2, j))
                elif chess_board[row2][j][1] == 'w':
                    valid_moves1.append((row2, j))
                    break
                else:
                    break
            for j in range(col2 + 1, 8):
                # Check moves right
                if chess_board[row2][j] == '':
                    valid_moves1.append((row2, j))
                elif chess_board[row2][j][1] == 'w':
                    valid_moves1.append((row2, j))
                    break
                else:
                    break
            for i, j in zip(range(row2 - 1, -1, -1), range(col2 - 1, -1, -1)):
                # Check moves up and left
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'w':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(row2 + 1, 8), range(col2 - 1, -1, -1)):
                # Check moves down and left
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'w':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(row2 - 1, -1, -1), range(col2 + 1, 8)):
                # Check moves up and right
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'w':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
            for i, j in zip(range(row2 + 1, 8), range(col2 + 1, 8)):
                # Check moves down and right
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'w':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
        elif piece == 'Bb':
            # Check valid moves for a bishop
            # Check moves up and to the left
            i, j = row2 - 1, col2 - 1
            while i >= 0 and j >= 0:
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'w':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
                i -= 1
                j -= 1
            # Check moves up and to the right
            i, j = row2 - 1, col2 + 1
            while i >= 0 and j < 8:
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'w':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
                i -= 1
                j += 1
            # Check moves down and to the left
            i, j = row2 + 1, col2 - 1
            while i < 8 and j >= 0:
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'w':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
                i += 1
                j -= 1
            # Check moves down and to the right
            i, j = row2 + 1, col2 + 1
            while i < 8 and j < 8:
                if chess_board[i][j] == '':
                    valid_moves1.append((i, j))
                elif chess_board[i][j][1] == 'w':
                    valid_moves1.append((i, j))
                    break
                else:
                    break
                i += 1
                j += 1
        # Return the valid Moves for black
        return valid_moves1


last_pawn_move = ""
before_pawn_move = ""


def save_last_pawn_move(piece, new_row, new_col, old_row3, old_col3):
    global last_pawn_move
    global before_pawn_move
    if piece == "Pw" or "Pb":
        last_pawn_move = new_row, new_col
        before_pawn_move = old_row3, old_col3
    else:
        last_pawn_move = ""
        before_pawn_move = ""


for row in range(8):
    for col in range(8):
        # Call the get_valid_moves() function to get the valid moves for the chess piece
        valid_moves = get_valid_moves(chess_board[row][col], row, col)
        # Draw a square on the chessboard
        rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
        pygame.draw.rect(screen, square_color, rect)

        # Draw a green overlay on squares that are valid moves for the selected chess piece
        if (row, col) in valid_moves:
            pygame.draw.rect(screen, (100, 200, 0), rect)

        # Draw the chess piece on the square if it is not empty
        if chess_board[row][col] != '':
            # Load the image of the chess piece
            piece_image = pygame.image.load(f"{chess_board[row][col]}.png")
            # Resize the image to fit on the square
            piece_image = pygame.transform.scale(piece_image, (square_size, square_size))
            # Draw the image on the square
            screen.blit(piece_image, rect)

        # Switch the color of the square
        square_color = white if square_color == black else black

        # Switch the color of the first square in the next row
        square_color = white if square_color == black else black

pygame.display.flip()

# Set up the clock
clock = pygame.time.Clock()
fps = 60

# Run the game loop
selected_piece = None
valid_moves = []
running = True

while running:
    # Update the clock
    milliseconds = clock.tick(fps)
    seconds = milliseconds / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_board_position(mouse_pos)
            # If a chess piece is not selected, select the clicked piece
            if selected_piece is None and chess_board[row][col] != '':
                # Set the selected piece and valid moves
                selected_piece = chess_board[row][col]
                valid_moves = get_valid_moves(selected_piece, row, col)
                # Update the old row and column indices
                old_row, old_col = row, col
            # If a chess piece is already selected, move it to the clicked square if it is a valid move
            elif selected_piece is not None and valid_moves and (row, col) in valid_moves:
                chess_board[row][col] = selected_piece
                chess_board[old_row][old_col] = ''
                save_last_pawn_move(selected_piece, row, col, old_row, old_col)
                # check for rochade
                if selected_piece == "Kw" and not first_move_done['Kw'][0] and not first_move_done['Rw'][1]:
                    selected_piece = chess_board[7][7]
                    chess_board[7][5] = selected_piece
                    chess_board[7][7] = ""
                elif selected_piece == "Kw" and not first_move_done['Kw'][0] and not first_move_done['Rw'][0]:
                    selected_piece = chess_board[7][0]
                    chess_board[7][3] = selected_piece
                    chess_board[7][0] = ""
                has_moved(selected_piece, row, col)
                print(first_move_done)
                # Check if it was an en passant Move
                if selected_piece == "Pw":
                    if chess_board[row + 1][col] == "Pb":
                        chess_board[row + 1][col] = ""
                elif selected_piece == "Pb":
                    if chess_board[row - 1][col] == "Pw":
                        chess_board[row - 1][col] = ""
                selected_piece = None
                pygame.time.wait(100)  # Wait for 50 milliseconds (0.05 seconds)
                valid_moves = []
                if playing_player == "white":
                    playing_player = "black"
                else:
                    playing_player = "white"
            else:
                selected_piece = None
                valid_moves = get_valid_moves(chess_board[row][col], row, col)

    # Loop through each row and column of the chessboard and redraw the squares and chess pieces
    for row in range(8):
        for col in range(8):
            # Draw a square on the chessboard
            rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
            pygame.draw.rect(screen, square_color, rect)

            # Draw a green overlay on squares that are valid moves for the selected chess piece
            if valid_moves and (row, col) in valid_moves:
                pygame.draw.rect(screen, (100, 200, 0), rect)

            # Draw the chess piece on the square if it is not empty
            if chess_board[row][col] != '':
                # Load the image of the chess piece
                piece_image = pygame.image.load(f"{chess_board[row][col]}.png")
                # Resize the image to fit on the square
                piece_image = pygame.transform.scale(piece_image, (square_size, square_size))
                # Draw the image on the square
                screen.blit(piece_image, rect)

            # Switch the color of the square for the next iteration
            square_color = white if square_color == black else black

        # Switch the color of the first square in the next row
        square_color = white if square_color == black else black

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
