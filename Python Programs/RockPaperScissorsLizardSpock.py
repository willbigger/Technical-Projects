# William Bigger Sep 2019
game = input("Press enter to start")
print('Enter "stop" to end the game after any round')


def winner(player):
    global game
    print('Congrats', player + ", you're the winner")
    game = input('To stop type "stop", otherwise press enter to continue the game: ')


def hide():
    for i in range(10):
        print("")


def tie():
    global game
    game = input('There was a tie, press "enter", or if you want to stop the game just type "stop": ')


def unknown():
    global game
    print("You didn't type rock, paper, or scissors. Check your spelling or something")
    game = input('Press "enter", or if you want to stop the game just type "stop": ')


def compare(first, second):
    if first == second:
        tie()
    elif first == 'rock':
        if second == 'paper':
            winner("Player2")
        elif second == 'scissors':
            winner("Player1")
        elif second == 'spock':
            winner("Player2")
        elif second == 'lizard':
            winner("Player1")
        else:
            unknown()
    elif first == 'paper':
        if second == 'scissors':
            winner("Player2")
        elif second == 'rock':
            winner("Player1")
        elif second == 'spock':
            winner("Player1")
        elif second == 'lizard':
            winner("Player2")
        else:
            unknown()
    elif first == 'scissors':
        if second == 'rock':
            winner("Player2")
        elif second == 'paper':
            winner("Player1")
        elif second == 'spock':
            winner("Player2")
        elif second == 'lizard':
            winner("Player1")
        else:
            unknown()
    elif first == 'spock':
        if second == 'paper':
            winner("Player2")
        elif second == 'scissors':
            winner("Player1")
        elif second == 'rock':
            winner("Player1")
        elif second == 'lizard':
            winner("Player2")
        else:
            unknown()
    elif first == 'lizard':
        if second == 'paper':
            winner("Player1")
        elif second == 'scissors':
            winner("Player2")
        elif second == 'spock':
            winner("Player1")
        elif second == 'rock':
            winner("Player2")
        else:
            unknown()
    else:
        unknown()


while game != 'stop':
    if game == 'stop':
        break
    user1 = input("Player1, choose rock, paper, scissors, lizard, spock: ")
    hide()
    user2 = input("Player2, choose rock, paper, scissors, lizard, spock: ")
    compare(user1, user2)
