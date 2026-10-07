from connection import *
games = []

# ADD
def addGameUI():
    name = input('Game name: ')
    genre = input('Genre: ')
    addGame(name, genre)

# VIEW
def viewGameUI(game):
    gameDetails = viewGame(game)
    if gameDetails:
        print(gameDetails['name'])
        print(gameDetails['genre'])
        if gameDetails['complete'] == 0:
            print('Not completed')
        else:
            print('Completed')
        if gameDetails['review'] is not None:
            print(gameDetails['review'])
        else:
            print('No review given.')

def viewAllGamesUI():
    games = viewAllGames()
    for game in games:
        print(game['name'])
        print(game['genre'])
        if game['complete'] == 0:
            print('Not completed')
        else:
            print('Completed')
        if game['review'] is not None:
            print(game['review'])
        else:
            print('No review given.')
        print('')
        
def searchGameUI(game):
    try:
        return games.index(game)
    except ValueError:
        print('Game not found.')
        return None

# EDIT
def editGameUI():
    game = input('\nEnter game name to edit: ')
    gameIndex = searchGameUI(game)
    if gameIndex == None:
        return
    games[gameIndex] = input('Enter new game name: ')
    print('Game edited.')

# DEL
def deleteGameUI():
    game = input('\nEnter game name to delete: ')
    deleteGame(game)
    
def menu():
    use = True
    while use == True:
        print('\nMENU:')
        userChoice = input()
        match userChoice.upper():
            case 'ADD':
                addGameUI()
            case 'VIEW':
                print('VIEW GAME')
                viewGameUI(input('Enter game name:  '))
            case 'VIEW ALL':
                print('\nVIEW BACKLOG:')
                viewAllGamesUI()
            case 'EDIT':
                editGameUI()
            case 'DEL':
                deleteGameUI()
            case 'EXIT':
                use = False

createTable()
menu()