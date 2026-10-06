games = ['Sims', 'Zomboid', 'Zelda']

# add game
def addGame():
    game = input('Game name: ')
    games.append(game)
    print('Game added.')

# view game
def viewGame(game):
    print(game)

# search game
def searchGame(game):
    try:
        return games.index(game)
    except ValueError:
        print('Game not found.')
        return None

# edit game
def editGame():
    game = input('\nEnter game name to edit: ')
    gameIndex = searchGame(game)
    if gameIndex == None:
        return
    games[gameIndex] = input('Enter new game name: ')
    print('Game edited.')
    
# delete game
def deleteGame():
    game = input('\nEnter game name to delete: ')
    gameIndex = searchGame(game)
    if gameIndex == None:
        return
    games.pop(gameIndex)
    print('Game deleted.')
    
# navigation menu
def menu():
    use = True
    while use == True:
        print('\nMENU:')
        userChoice = input()
        match userChoice.upper():
            case 'ADD':
                addGame()
            case 'VIEW':
                print('\nBACKLOG:')
                for game in games:
                    viewGame(game)
            case 'EDIT':
                editGame()
            case 'DEL':
                deleteGame()
            case 'EXIT':
                use = False

menu()