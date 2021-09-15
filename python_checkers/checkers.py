# Lauren Askew (lna5qy) and William Bigger (wmb8yt)

import pygame
import gamebox

"""Our proposed project is blitz checkers. The optional features that we plan to implement are the ability to play with
another player, timers in the form of a chess timer for each player, an enemy in the form of another player, and
restricting the players to possible moves of checkers. In the case that we need an additional feature, we plan to
implement the ability for players to come back to their match after closing the game (intersession progress)."""

# start() and timer() variables
game_start = 0
screen_elements = []
white_playing = True
white_ticks = 10
white_minutes = 10
black_ticks = 10
black_minutes = 10
winner = ''
white_piececheck = 0
black_piececheck = 0

# Define camera size and grid size
camera = gamebox.Camera(800, 600)
grid_size = 50
# Make string to indicate current grid space selected
selected_grid = ""
possible_grid = ""
remove = False

# Create coordinates for 64 A1 through H8 and store in dictionary with the index being the key
# and the x and y value in a list as the value
coordinates = dict([])
for i in range(8):
    for j in range(8):
        if (125 + (j*grid_size) > 100) and (125 + (j*grid_size) < 500):
            coordinates[chr(65 + i) + str(j+1)] = [225 + (i*grid_size), 125 + (j*grid_size)]
###

# Creates the chess board (64 squares) and puts them in list called boards
boards = []
for j in range(4):
    for i in range(4):
        boards.append(gamebox.from_color(225 + (2*i*grid_size), 125 + (2*j*grid_size), "white", grid_size, grid_size))
        boards.append(gamebox.from_color(275 + (2*i*grid_size), 125 + (2*j*grid_size), "brown", grid_size, grid_size))
        boards.append(gamebox.from_color(225 + (2*i*grid_size), 175 + (2*j*grid_size), "brown", grid_size, grid_size))
        boards.append(gamebox.from_color(275 + (2*i*grid_size), 175 + (2*j*grid_size), "white", grid_size, grid_size))
###

# Create chess pieces as sprites with their current coordinate in the 1st index place
chess_pieces = {}
# chess_pieces[coordinate][2] is a boolean meaning is_king (value is false when the piece is created)
"""Create white pieces"""
for i in range(4):
    chess_pieces[chr(65 + (i * 2)) + str(8)] = [gamebox.from_image(coordinates[chr(65 + (i * 2)) + str(8)][0],
                                                                   coordinates[chr(65 + (i * 2)) + str(8)][1],
                                                                   "white_pawn.png"), "white", False]
    chess_pieces[chr(66 + (i*2)) + str(7)] = [gamebox.from_image(coordinates[chr(66 + (i*2)) + str(7)][0],
                                                                 coordinates[chr(66 + (i*2)) + str(7)][1],
                                                                 "white_pawn.png"), "white", False]
    chess_pieces[chr(65 + (i*2)) + str(6)] = [gamebox.from_image(coordinates[chr(65 + (i * 2)) + str(6)][0],
                                                                 coordinates[chr(65 + (i * 2)) + str(6)][1],
                                                                 "white_pawn.png"), "white", False]
"""Create black pieces"""
for i in range(4):
    chess_pieces[chr(66 + (i * 2)) + str(1)] = [gamebox.from_image(coordinates[chr(66 + (i * 2)) + str(1)][0],
                                                                   coordinates[chr(66 + (i * 2)) + str(1)][1],
                                                                   "pawn.png"), "black", False]
    chess_pieces[chr(65 + (i * 2)) + str(2)] = [gamebox.from_image(coordinates[chr(65 + (i * 2)) + str(2)][0],
                                                                   coordinates[chr(65 + (i * 2)) + str(2)][1],
                                                                   "pawn.png"), "black", False]
    chess_pieces[chr(66 + (i * 2)) + str(3)] = [gamebox.from_image(coordinates[chr(66 + (i * 2)) + str(3)][0],
                                                                   coordinates[chr(66 + (i * 2)) + str(3)][1],
                                                                   "pawn.png"), "black", False]
# Scale all chess pieces to appropriate size
for pieces in chess_pieces.values():
    pieces[0].scale_by(.15)
###


def get_numbers():
    """
    Returns a list of all the coordinates of the chess pieces' locations
    :return: a list of coordinates (list of lists with lengths 2)
    """
    list_coordinates = []
    for key, value in coordinates.items():
        if key in chess_pieces.keys():
            list_coordinates.append(value)
    return list_coordinates


def start():
    """
    Creates a list of the elements to be drawn on the start screen
    :return: Nothing
    """
    screen_elements.append(gamebox.from_color(400, 300, "blue", 750, 550))
    screen_elements.append(gamebox.from_text(400, 150, "Blitz Checkers", 70, "white", True))
    screen_elements.append(gamebox.from_text(400, 200, "For two players", 50, "white"))
    screen_elements.append(gamebox.from_text(400, 250, "Lauren Askew (lna5qy) and William Bigger (wmb8yt)", 30,
                                             "white"))
    screen_elements.append(gamebox.from_text(400, 450, "Press Tab to start", 40, "white"))
    title_pawn1 = gamebox.from_image(450, 350, "white_pawn.png")
    title_pawn2 = gamebox.from_image(350, 350, "pawn.png")
    title_pawn1.scale_by(0.5)
    title_pawn2.scale_by(0.5)
    screen_elements.append(title_pawn1)
    screen_elements.append(title_pawn2)


def timer():
    """
    Creates two timers that go down by the second for the player whose move it is and declares a winner if one player
    runs out of time.
    :return: Nothing
    """
    global white_ticks, white_minutes, black_ticks, black_minutes, winner
    if white_playing and white_minutes + white_ticks != -1:
        white_ticks -= 1
        if white_minutes != 0 and white_ticks == -1:
            white_ticks = 1799
            white_minutes -= 1
        elif white_minutes == 0 and white_ticks == 0:
            white_ticks = 0
    elif not white_playing and black_minutes + black_ticks != -1:
        black_ticks -= 1
        if black_minutes != 0 and black_ticks == -1:
            black_ticks = 1799
            black_minutes -= 1
    if white_minutes == 0 and white_ticks == 0:
        winner = 'black'
    if black_minutes == 0 and black_ticks == 0:
        winner = 'white'
    white_seconds = str(int((white_ticks / ticks_per_second))).zfill(2)
    black_seconds = str(int((black_ticks / ticks_per_second))).zfill(2)
    white_time_box = \
        gamebox.from_text(100, 550, "White Timer: " + str(white_minutes) + ':' + white_seconds, 24, "white")
    black_time_box = gamebox.from_text(100, 50, "Black Timer: " + str(black_minutes) + ':' + black_seconds, 24, "black")
    camera.draw(white_time_box)
    camera.draw(black_time_box)


def find_middle(first, second):
    """
    Finds the middle square between possible grid and selected grid
    :param first: possible grid
    :param second: selected grid
    :return: middle coordinate
    """
    sg_letter = ord(first[:1])
    pg_letter = ord(second[:1])
    sg_number = int(first[1:])
    pg_number = int(second[1:])
    if sg_letter > pg_letter:
        place = chr(sg_letter - 1)
    else:
        place = chr(pg_letter - 1)
    if sg_number > pg_number:
        place += str(sg_number - 1)
    else:
        place += str(pg_number - 1)
    return place


def check_color(location):
    """
    returns the color of a piece at a location and returns and empty string in there's no piece there evaluates False
    :param location: location of piece
    :return: white, black, or nothing
    """
    answer = ""
    for key, value in coordinates.items():
        if (location == value or key == location) and key in chess_pieces.keys():
            answer = chess_pieces[key][1]
    return answer


def highlight_possibilities(location, color):
    global remove
    """
    computes the list of possible moves of chess pieces
    :param location: current location of piece
    :param color: white or black
    :return: a list of possible grids
    """
    list_possibilities = []
    if color == "black" or chess_pieces[location][2]:
        list_possibilities.append([coordinates[location][0] + grid_size, coordinates[location][1] + grid_size])
        list_possibilities.append([coordinates[location][0] - grid_size, coordinates[location][1] + grid_size])
    if color == "white" or chess_pieces[location][2]:
        list_possibilities.append([coordinates[location][0] + grid_size, coordinates[location][1] - grid_size])
        list_possibilities.append([coordinates[location][0] - grid_size, coordinates[location][1] - grid_size])
    for k in range(len(list_possibilities)):
        if color == "black" or chess_pieces[location][2]:
            if [(coordinates[location][0] + (2*grid_size)), (coordinates[location][1] + (2*grid_size))] not in \
                    get_numbers() and check_color([(coordinates[location][0] + grid_size),
                                                   (coordinates[location][1] + grid_size)]) != color and \
                    [(coordinates[location][0] + grid_size), (coordinates[location][1] + grid_size)] in get_numbers():
                list_possibilities.append([coordinates[location][0] + (2 * grid_size),
                                           coordinates[location][1] + (2 * grid_size)])
                remove = True
            if [(coordinates[location][0] - (2*grid_size)), (coordinates[location][1] + (2*grid_size))] not in \
                    get_numbers() and check_color([(coordinates[location][0] - grid_size),
                                                   (coordinates[location][1] + grid_size)]) != color and \
                    [(coordinates[location][0] - grid_size), (coordinates[location][1] + grid_size)] in get_numbers():
                list_possibilities.append([coordinates[location][0] - (2 * grid_size),
                                           coordinates[location][1] + (2 * grid_size)])
                remove = True
        if color == "white" or chess_pieces[location][2]:
            if [(coordinates[location][0] + (2*grid_size)), (coordinates[location][1] - (2*grid_size))] not in \
                    get_numbers() and check_color([(coordinates[location][0] + grid_size),
                                                   (coordinates[location][1] - grid_size)]) != color and \
                    [(coordinates[location][0] + grid_size), (coordinates[location][1] - grid_size)] in get_numbers():
                list_possibilities.append([coordinates[location][0] + (2 * grid_size),
                                           coordinates[location][1] - (2 * grid_size)])
                remove = True
            if [(coordinates[location][0] - (2*grid_size)), (coordinates[location][1] - (2*grid_size))] not in \
                    get_numbers() and check_color([(coordinates[location][0] - grid_size),
                                                   (coordinates[location][1] - grid_size)]) != color and \
                    [(coordinates[location][0] - grid_size), (coordinates[location][1] - grid_size)] in get_numbers():
                list_possibilities.append([coordinates[location][0] - (2 * grid_size),
                                           coordinates[location][1] - (2 * grid_size)])
                remove = True
    for o in range(4):
        for place in list_possibilities:
            if place not in coordinates.values() or place in get_numbers():
                list_possibilities.remove(place)
    return list_possibilities


def move_piece(location):
    """
    Function moves one chess piece according to its kind
    and changes the dictionary key to reflect the new location of the piece
    :param location: current location of the piece
    :return: None, only changes piece location and piece key in dictionary chess_pieces to new position
    """
    if location in chess_pieces.keys():
        chess_pieces[location][0].x = coordinates[possible_grid][0]
        chess_pieces[location][0].y = coordinates[possible_grid][1]
        for key, values in coordinates.items():
            if values[0] == chess_pieces[location][0].x and values[1] == chess_pieces[location][0].y:
                chess_pieces[key] = chess_pieces[location]
        del chess_pieces[location]


def tick(keys):
    global selected_grid, possible_grid, game_start, screen_elements, white_playing, winner, remove, white_piececheck,\
        black_piececheck

    # Used to check is the user moves to an allowed space
    possibilities = []
    ###

    # Boolean to remove piece
    remove = False
    ###

    # Background brown color
    camera.clear("orange")
    ###

    # Draws the board and the numbers and letter for indexing
    for board in boards:
        camera.draw(board)
    # Display currently selected grid location and highlight selected grid square
    camera.draw(gamebox.from_text(300, 550, "Grid: " + selected_grid, 35, "Black", bold=False))
    camera.draw(gamebox.from_text(500, 550, "Move: " + possible_grid, 35, "Black", bold=False))
    if len(selected_grid) == 2:
        camera.draw(gamebox.from_color(coordinates[selected_grid][0], coordinates[selected_grid][1],
                                       "blue", grid_size, grid_size))
    for k in range(8):
        camera.draw(gamebox.from_text(225 + (k * grid_size), grid_size + 25, chr(65 + k), 20, "Black", bold=False))
    for k in range(8):
        camera.draw(gamebox.from_text(175, 125 + (k * grid_size), str(k + 1), 20, "Black", bold=False))
    ###

    # highlight possible spaces
    if selected_grid in chess_pieces.keys():
        possibilities = \
            highlight_possibilities(selected_grid, chess_pieces[selected_grid][1])
        for index in possibilities:
            camera.draw(gamebox.from_color(index[0], index[1], "yellow", grid_size, grid_size))
    ###

    # Draws chess pieces
    for checkers in chess_pieces.values():
        camera.draw(checkers[0])
    ###

    ###
    if len(selected_grid) == 2 and len(possible_grid) == 2:
        if chess_pieces[selected_grid][1] == "white" and white_playing:
            if pygame.K_SPACE in keys:
                if selected_grid in chess_pieces.keys():
                    for places in possibilities:  # Checks to make sure the move grid is a legal move
                        if len(possible_grid) == 2:
                            if remove and find_middle(possible_grid, selected_grid) in chess_pieces.keys():
                                # find the middle of possible_grid and selected grid and removes the piece
                                del chess_pieces[find_middle(possible_grid, selected_grid)]
                            if coordinates[possible_grid] == places:
                                move_piece(selected_grid)
                                white_playing = not white_playing
                                selected_grid, possible_grid = "", ""
        elif chess_pieces[selected_grid][1] == "black" and not white_playing:
            if pygame.K_SPACE in keys:
                if selected_grid in chess_pieces.keys():
                    for places in possibilities:  # Checks to make sure the move grid is a legal move
                        if len(possible_grid) == 2:
                            if remove and find_middle(possible_grid, selected_grid) in chess_pieces.keys():
                                # find the middle of possible_grid and selected grid and removes the piece
                                del chess_pieces[find_middle(possible_grid, selected_grid)]
                            if coordinates[possible_grid] == places:
                                move_piece(selected_grid)
                                white_playing = not white_playing
                                selected_grid, possible_grid = "", ""
        else:
            camera.draw(gamebox.from_text(400, 575, 'It\'s not your turn!', 30, 'black'))
    ###

    # Checks to see if pawns crossed the board and changes them to kings
    for piece_position in chess_pieces.keys():
        if piece_position.find("1") != -1 and chess_pieces[piece_position][1] == "white":
            if not chess_pieces[piece_position][2]:
                chess_pieces[piece_position] = [gamebox.from_image(coordinates[piece_position][0],
                                                                   coordinates[piece_position][1],
                                                                   "white_king.png"),
                                                "white", True]
                chess_pieces[piece_position][0].scale_by(.15)
        if piece_position.find("8") != -1 and chess_pieces[piece_position][1] == "black":
            if not chess_pieces[piece_position][2]:
                chess_pieces[piece_position] = [gamebox.from_image(coordinates[piece_position][0],
                                                                   coordinates[piece_position][1], "king.png"),
                                                "black", True]
                chess_pieces[piece_position][0].scale_by(.15)
    ###

    # All the possible input which includes A-H and 1-8
    if pygame.K_a in keys:
        if len(selected_grid) == 0:
            selected_grid = "A"
        if len(selected_grid) == 2:
            possible_grid = "A"

    if pygame.K_b in keys:
        if len(selected_grid) == 0:
            selected_grid = "B"
        if len(selected_grid) == 2:
            possible_grid = "B"

    if pygame.K_c in keys:
        if len(selected_grid) == 0:
            selected_grid = "C"
        if len(selected_grid) == 2:
            possible_grid = "C"

    if pygame.K_d in keys:
        if len(selected_grid) == 0:
            selected_grid = "D"
        if len(selected_grid) == 2:
            possible_grid = "D"

    if pygame.K_e in keys:
        if len(selected_grid) == 0:
            selected_grid = "E"
        if len(selected_grid) == 2:
            possible_grid = "E"

    if pygame.K_f in keys:
        if len(selected_grid) == 0:
            selected_grid = "F"
        if len(selected_grid) == 2:
            possible_grid = "F"

    if pygame.K_g in keys:
        if len(selected_grid) == 0:
            selected_grid = "G"
        if len(selected_grid) == 2:
            possible_grid = "G"

    if pygame.K_h in keys:
        if len(selected_grid) == 0:
            selected_grid = "H"
        if len(selected_grid) == 2:
            possible_grid = "H"

    if pygame.K_1 in keys:
        if len(selected_grid) == 1:
            selected_grid += "1"
        if len(possible_grid) == 1:
            possible_grid += "1"

    if pygame.K_2 in keys:
        if len(selected_grid) == 1:
            selected_grid += "2"
        if len(possible_grid) == 1:
            possible_grid += "2"

    if pygame.K_3 in keys:
        if len(selected_grid) == 1:
            selected_grid += "3"
        if len(possible_grid) == 1:
            possible_grid += "3"

    if pygame.K_4 in keys:
        if len(selected_grid) == 1:
            selected_grid += "4"
        if len(possible_grid) == 1:
            possible_grid += "4"

    if pygame.K_5 in keys:
        if len(selected_grid) == 1:
            selected_grid += "5"
        if len(possible_grid) == 1:
            possible_grid += "5"

    if pygame.K_6 in keys:
        if len(selected_grid) == 1:
            selected_grid += "6"
        if len(possible_grid) == 1:
            possible_grid += "6"

    if pygame.K_7 in keys:
        if len(selected_grid) == 1:
            selected_grid += "7"
        if len(possible_grid) == 1:
            possible_grid += "7"

    if pygame.K_8 in keys:
        if len(selected_grid) == 1:
            selected_grid += "8"
        if len(possible_grid) == 1:
            possible_grid += "8"

    if pygame.K_BACKSPACE in keys:
        selected_grid, possible_grid = "", ""
    ###

    if pygame.K_TAB not in keys and not game_start:
        start()
    elif pygame.K_TAB in keys:
        screen_elements = []
        screen_elements.append(gamebox.from_color(400, 300, "grey", 750, 550))
        screen_elements.append(gamebox.from_text(400, 100, "Instructions", 60, "white", True))
        screen_elements.append(gamebox.from_text(400, 175, "Select a piece by typing in its coordinates (ex. A3).", 30,
                                                 "white"))
        screen_elements.append(gamebox.from_text(400, 225, "Possible moves for that piece will be yellow.", 30,
                                                 "white"))
        screen_elements.append(gamebox.from_text(400, 275, "Move that piece by typing in the coordinates of a possible "
                                                           "move and ", 30, "white"))
        screen_elements.append(gamebox.from_text(400, 300, "pressing Spacebar to stop your clock.", 30, "white"))
        screen_elements.append(gamebox.from_text(400, 350, "If you get a piece to the other player's end of the board, "
                                                           "it ", 30, "white"))
        screen_elements.append(gamebox.from_text(400, 375, "becomes a king and can move forwards and backwards.", 30,
                                                 "white"))
        screen_elements.append(gamebox.from_text(400, 425, "Take all of the other player's pieces before 10 minutes "
                                                           "are up to win!", 30, "white"))
        screen_elements.append(gamebox.from_text(400, 475, "Press Tab to start", 40, "white"))
        game_start += 1
        if game_start >= 2:
            screen_elements = []
    if screen_elements:
        for element in screen_elements:
            camera.draw(element)
    if not screen_elements:
        timer()
    white_piececheck = 0
    black_piececheck = 0
    for piece in chess_pieces.values():
        if piece[1] == 'white':
            white_piececheck += 1
        elif piece[1] == 'black':
            black_piececheck += 1
    if white_piececheck == 0:
        winner = 'black'
    elif black_piececheck == 0:
        winner = 'white'
    if winner:
        screen_elements.append(gamebox.from_color(400, 300, "grey", 750, 550))
        screen_elements.append(gamebox.from_text(400, 200, winner.title() + " Wins!", 70, winner))
    camera.display()


ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)
