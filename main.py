from connection import *

games = ['Sims', 'Zomboid', 'Zelda']

# add game
def addGameUI():
    name = input('Game name: ')
    genre = input('Genre: ')
    addGame(name, genre)

# view game
def viewGameUI(game):
    print(game)

# search game
def searchGameUI(game):
    try:
        return games.index(game)
    except ValueError:
        print('Game not found.')
        return None

# edit game
def editGameUI():
    game = input('\nEnter game name to edit: ')
    gameIndex = searchGameUI(game)
    if gameIndex == None:
        return
    games[gameIndex] = input('Enter new game name: ')
    print('Game edited.')
    
# delete game
def deleteGameUI():
    game = input('\nEnter game name to delete: ')
    gameIndex = searchGameUI(game)
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
                addGameUI()
            case 'VIEW':
                print('\nBACKLOG:')
                for game in games:
                    viewGameUI(game)
            case 'EDIT':
                editGameUI()
            case 'DEL':
                deleteGameUI()
            case 'EXIT':
                use = False

createTable()
menu()