import random

def joonistaLaud(laud):
    print('\n' ' ' + laud[7] + ' | ' + laud[8] + ' | ' + laud[9])
    print('-----------') 
    print(' ' + laud[4] + ' | ' + laud[5] + ' | ' + laud[6])
    print('-----------')
    print(' ' + laud[1] + ' | ' + laud[2] + ' | ' + laud[3] + '\n')

def mangijaValik():    
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Soovid valida X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def kesKaibEsimesena():   
    if random.randint(0, 1) == 0:
        return 'arvuti'
    else:
        return 'mängija'

def kordusMang():
    print('Soovid uuesti mängida- jah / ei?')
    return input().lower().startswith('j')

def teeKaik(laud, letter, move):
    laud[move] = letter

def voitja(laud, taht):
    
    return ((laud[7] == taht and laud[8] == taht and laud[9] == taht) or 
    (laud[4] == taht and laud[5] == taht and laud[6] == taht) or 
    (laud[1] == taht and laud[2] == taht and laud[3] == taht) or 
    (laud[7] == taht and laud[4] == taht and laud[1] == taht) or 
    (laud[8] == taht and laud[5] == taht and laud[2] == taht) or 
    (laud[9] == taht and laud[6] == taht and laud[3] == taht) or 
    (laud[7] == taht and laud[5] == taht and laud[3] == taht) or 
    (laud[9] == taht and laud[5] == taht and laud[1] == taht)) 

def lauaKoopia(laud):
    lauaDublikaat = []

    for i in laud:
        lauaDublikaat.append(i)

    return lauaDublikaat

def vabaKoht(laud, move):
    return laud[move] == ' '

def getPlayerMove(laud):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not vabaKoht(laud, int(move)):
        print('Tee oma järgmine käik 1-9: ')
        move = input()
    return int(move)

def randomKaikListist(laud, movesList):
    voimalikKaik = []
    for i in movesList:
        if vabaKoht(laud, i):
            voimalikKaik.append(i)

    if len(voimalikKaik) != 0:
        return random.choice(voimalikKaik)
    else:
        return None

def getComputerMove(laud, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    
    for i in range(1, 10):
        copy = lauaKoopia(laud)
        if vabaKoht(copy, i):
            teeKaik(copy, computerLetter, i)
            if voitja(copy, computerLetter):
                return i
    
    for i in range(1, 10):
        copy = lauaKoopia(laud)
        if vabaKoht(copy, i):
            teeKaik(copy, playerLetter, i)
            if voitja(copy, playerLetter):
                return i

    # nurkade hõivamine
    move = randomKaikListist(laud, [1, 3, 7, 9])
    if move != None:
        return move

    # 5 hõivamine
    if vabaKoht(laud, 5):
        return 5

    # 2,4,6,8, hõivamine
    return randomKaikListist(laud, [2, 4, 6, 8])

def isBoardFull(laud):    
    for i in range(1, 10):
        if vabaKoht(laud, i):
            return False
    return True

while True:
    # lähtesta laud
    theBoard = [' '] * 10
    playerLetter, computerLetter = mangijaValik()
    turn = kesKaibEsimesena()
    print(turn + ' alustab.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'mängija':            
            joonistaLaud(theBoard)
            move = getPlayerMove(theBoard)
            teeKaik(theBoard, playerLetter, move)

            if voitja(theBoard, playerLetter):
                joonistaLaud(theBoard)
                print('Sa võitsid!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    joonistaLaud(theBoard)
                    print('Viik!')
                    break
                else:
                    turn = 'arvuti'

        else:
            move = getComputerMove(theBoard, computerLetter)
            teeKaik(theBoard, computerLetter, move)

            if voitja(theBoard, computerLetter):
                joonistaLaud(theBoard)
                print('Arvuti võitis!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    joonistaLaud(theBoard)
                    print('Viik!')
                    break
                else:
                    turn = 'mängija'

    if not kordusMang():
        break
