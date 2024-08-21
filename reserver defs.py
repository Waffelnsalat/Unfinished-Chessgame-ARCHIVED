
# Define a function to get the position of the mouse click on the chessboard
def get_board_position(mouse_pos):
    row = mouse_pos[1] // square_size
    col = mouse_pos[0] // square_size
    return (row, col)


# Define a function to get the position of the mouse click on the chessboard
def get_valid_moves(piece, row, col):
    valid_moves = []
    if piece == 'P':
        # Check if the pawn can move one square forward
        if chess_board[row-1][col] == '':
            valid_moves.append((row-1, col))
        # Check if the pawn can move two squares forward
        if row == 6 and chess_board[row-2][col] == '':
            valid_moves.append((row-2, col))
        # Check if the pawn can capture an enemy piece to the left
        if col > 0 and chess_board[row-1][col-1].islower():
            valid_moves.append((row-1, col-1))
        # Check if the pawn can capture an enemy piece to the right
        if col < 7 and chess_board[row-1][col+1].islower():
            valid_moves.append((row-1, col+1))
    elif piece == 'R':
        # Check valid moves for a rook
        for i in range(row-1, -1, -1):
            # Check moves up
            if chess_board[i][col] == '':
                valid_moves.append((i, col))
            elif chess_board[i][col].islower():
                valid_moves.append((i, col))
                break
            else:
                break
        for i in range(row+1, 8):
            # Check moves down
            if chess_board[i][col] == '':
                valid_moves.append((i, col))
            elif chess_board[i][col].islower():
                valid_moves.append((i, col))
                break
            else:
                break
        for j in range(col-1, -1, -1):
            # Check moves left
            if chess_board[row][j] == '':
                valid_moves.append((row, j))
            elif chess_board[row][j].islower():
                valid_moves.append((row, j))
                break
            else:
                break
        for j in range(col+1, 8):
            # Check moves right
            if chess_board[row][j] == '':
                valid_moves.append((row, j))
            elif chess_board[row][j].islower():
                valid_moves.append((row, j))
                break
            else:
                break
    # Add more code to get valid moves for other chess pieces here
    return valid_moves


for row in range(8):
    for col in range(8):
        # Call the get_valid_moves() function to get the valid moves for the chess piece
        valid_moves = get_valid_moves(chess_board[row][col], row, col)
        # Draw a square on the chessboard
        rect = pygame.Rect(col * square_size, row * square_size, square_size, square_size)
        pygame.draw.rect(screen, square_color, rect)

        # Draw a green overlay on squares that are valid moves for the selected chess piece
        if (row, col) in valid_moves:
            pygame.draw.rect(screen, green, rect)

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

