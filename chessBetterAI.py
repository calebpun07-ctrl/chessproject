import random
from tkinter.tix import InputOnly

from functions import checkSpaceClear,checkPieceSymbol,checkPieceBlackSymbol,checkSpaceClear,checkPieceWhiteSymbol, chekchek2, findPeice, showOpenMoves, pickmove, find_black_pieces, find_white_pieces
# should get every possible move then return a random one
listOfPossibleMove = []

def AdvancedAImakemoveBlack():
    A = False
    ourpeices = find_black_pieces()
    
    checkmove = False
    while checkmove == False:
        movefound = False
        while movefound == False:
            # print('ourpeices:' + str(ourpeices))
            randomPeaice = random.choice(ourpeices)
            if A == True:
                randomPeaice = findPeice("♔")
                randomPeaice.append('♔')
                print('King cords:' + str(randomPeaice))
                
                 #fix
            #ok the goal of pickmoveAI has changed. it will now return all the possible moves of the selected peice
            thing = pickmoveAI(randomPeaice)
            
            if thing != False:
                listOfPossibleMove = thing
                movefound == True
                break
                
            elif thing == False:
                continue

        move = random.choice(listOfPossibleMove) #pick a random move
        #building bricks
        #needs to be starting cords, peice ending cords
        brick = [randomPeaice[0],randomPeaice[1],randomPeaice[2]]
        
        brick.append(move[0]+1)
        brick.append(move[1]+1)
        
        i = input('It is blacks turn rn. We would like to make this move:' + str(brick))
        
        return brick

def AdvancedAImakemoveBlack1(): # this the new one and we are working on making it work however i am on a call right now and cannot focus
    ourpeices = find_black_pieces()
    counter = 0
    A = False
    listOfPossibleMove = []
    peiceWcaptures = []
    checkmove = False
    while checkmove == False: #wtf checkmove is always false
        movefound = False
        while movefound == False:
            list = ourpeices
            list2 = find_black_pieces()
            for n in list2:
                a = list2.index(n)
                list[a] = pickmoveAI(n) #might need to change
            nocaptures = True
            list3 = find_white_pieces()
            for i in list:
                if i == []:
                    continue
                else:
                    location = list.index(i)
                    temp2 = list3[location]
                    temp = [temp2[0],temp2[1]]
                    temp.append(i[2])
                    temp.append(i[0]+1)
                    temp.append(i[1]+1)
                    
                    peiceWcaptures.append(temp)
                    nocaptures = False #this means that there is a capture to do
            
            if nocaptures: #this is when there are no captures
                #then do teh normal check for all moves
                
                while movefound == False:
                    randomPeaice = random.choice(find_black_pieces())

                    thing = pickmoveAI(randomPeaice)
                    
                    if thing != False:
                        listOfPossibleMove = thing
                        
                        # print('list of possible:' + str(listOfPossibleMove) + str(thing))
                        movefound == True
                        
                        break
                        
                    elif thing == False:
                        continue
            
            elif not nocaptures:
                rand2 = random.choice(peiceWcaptures)

                return rand2
                
                #get the index of the the possible captures, elmiated the non captures
                #ranomdly slected on of thos emoves
                #return that move

                #THE END GOAL OF THIS IS TO HAVE A: randomly select a peice that has one or move captures and B:a list of said possible captures
            else:
                print('something happend'+listOfPossibleMove)
            
            # print('list of possible:' + str(listOfPossibleMove) + str(nocaptures))
            move = random.choice(listOfPossibleMove)
            #building bricks
            #needs to be starting cords, peice ending cords
            brick = [randomPeaice[0],randomPeaice[1],randomPeaice[2]]
            
            brick.append(move[0]+1)
            brick.append(move[1]+1)
            
            print(f'It is whites turn rn. We would like to make this move: {brick}')

            return brick


def AdvancedAImakemoveWhite1():
    ourpeices = find_white_pieces()
    counter = 0
    A = False
    checkmove = False
    while checkmove == False:
        movefound = False
        while movefound == False:
            randomPeaice = random.choice(ourpeices)

            if A == True:
                randomPeaice = findPeice("♚")
                randomPeaice.append('♚')
                print('King cords:' + str(randomPeaice))
                
                 #fix
            #ok the goal of pickmoveAI has changed. it will now return all the possible moves of the selected peice
            
            thing = pickmoveWhiteMoves(randomPeaice)
            
            if thing != False:
                listOfPossibleMove = thing
                movefound == True
                break
                
            elif thing == False:
                continue
        move = random.choice(listOfPossibleMove)
        #building bricks
        #needs to be starting cords, peice ending cords
        brick = [randomPeaice[0],randomPeaice[1],randomPeaice[2]]
        
        brick.append(move[0]+1)
        brick.append(move[1]+1)
        
        print('It is whites turn rn. We would like to make this move:')
        print(brick)

        return brick

def AdvancedAImakemoveWhite():
    ourpeices = find_white_pieces()
    counter = 0
    A = False
    listOfPossibleMove = []
    peiceWcaptures = []
    checkmove = False
    while checkmove == False: #wtf checkmove is always false
        movefound = False
        while movefound == False:
            list = ourpeices
            list2 = find_white_pieces()
            for n in list2:
                a = list2.index(n)
                list[a] = pickmoveWhiteCaptures(n)
            nocaptures = True
            list3 = find_white_pieces()
            for i in list:
                if i == []:
                    continue
                else:
                    location = list.index(i)
                    temp2 = list3[location]
                    temp = [temp2[0],temp2[1]]
                    temp.append(i[2])
                    temp.append(i[0]+1)
                    temp.append(i[1]+1)
                    
                    peiceWcaptures.append(temp)
                    nocaptures = False #this means that there is a capture to do
            
            if nocaptures: #this is when there are no captures
                #then do teh normal check for all moves
                
                while movefound == False:
                    randomPeaice = random.choice(find_white_pieces())

                    thing = pickmoveWhiteMoves(randomPeaice)
                    
                    if thing != False:
                        listOfPossibleMove = thing
                        
                        # print('list of possible:' + str(listOfPossibleMove) + str(thing))
                        movefound == True
                        
                        break
                        
                    elif thing == False:
                        continue
            
            elif not nocaptures:
                rand2 = random.choice(peiceWcaptures)

                return rand2
                
                #get the index of the the possible captures, elmiated the non captures
                #ranomdly slected on of thos emoves
                #return that move

                #THE END GOAL OF THIS IS TO HAVE A: randomly select a peice that has one or move captures and B:a list of said possible captures
            else:
                print('something happend'+listOfPossibleMove)
            
            # print('list of possible:' + str(listOfPossibleMove) + str(nocaptures))
            move = random.choice(listOfPossibleMove)
            #building bricks
            #needs to be starting cords, peice ending cords
            brick = [randomPeaice[0],randomPeaice[1],randomPeaice[2]]
            
            brick.append(move[0]+1)
            brick.append(move[1]+1)
            
            print(f'It is whites turn rn. We would like to make this move: {brick}')

            return brick

def pickmoveAI(level):
    
    #checks for trun, then picks avalible spots for user to choose
    allowedMoves = []
    allowedCaptures = []
    userMove = []
    piece = level[2] 
    
    if piece == '♙':
        # this is for the pawn forward two moves
        if checkSpaceClear(level[0]+1,level[1]): 
            allowedMoves.append([level[0]+1, level[1]])
            if checkSpaceClear(level[0]+2,level[1]) and level[0] ==1:  
                allowedMoves.append([level[0]+2, level[1]])
        
        if level[1] -1 != -1: #diagnal to left
            if checkPieceWhiteSymbol(level[0]+1,level[1]-1):
                allowedCaptures.append([level[0]+1, level[1]-1])
        
        if level[1] +1 != 8: #diagnal to right
            if checkPieceWhiteSymbol(level[0]+1,level[1]+1):
                allowedCaptures.append([level[0]+1, level[1]+1])

        for x in allowedCaptures:
            allowedMoves.append(x)

        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures

        if allowedMoves == []:
            return False

        return allowedMoves
    #rook took longest only because i had no idea what i was doing
    elif piece == '♖':
        #varbles
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for rawrow, hidcol in directions:
            moverow, movecol = level[0], level[1]
            scc = False

            while not scc:
                moverow += rawrow
                movecol += hidcol
                
                if not (0 <= moverow <= 7 and 0 <= movecol <= 7):
                    break  # Exit if out of bounds

                if checkSpaceClear(moverow, movecol):
                    allowedMoves.append([moverow, movecol])

                else:
                    if checkPieceWhiteSymbol(moverow, movecol):
                        # print('YYYYYYYAAAAAAAAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY')
                        allowedCaptures.append([moverow, movecol])
                    scc = True  # Stop moving in this direction if we hit a piece
            
        for x in allowedCaptures:
            allowedMoves.append(x)

        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures

        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♘':
        
        nightnight = [(-2, 1), (-2, -1), (2, 1), (2, -1),(-1, 2), (-1, -2), (1, 2), (1, -2)]

        for cherry in nightnight:
            yaxe = level[0] + cherry[0]
            xaxe = level[1] + cherry[1]
            # Check if the move is within the bounds of the board
            if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                    if not checkSpaceClear(yaxe, xaxe):  # capture
                        if checkPieceWhiteSymbol(yaxe, xaxe):
                            allowedCaptures.append([yaxe, xaxe])
                    else:  # go empty square
                        allowedMoves.append([yaxe, xaxe])

        for x in allowedCaptures:
            allowedMoves.append(x)

        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures
            
        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♗':

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

        for rawrow, hidcol in directions:
            moverow, movecol = level[0], level[1]
            orca = False

            while not orca:
                moverow += rawrow
                
                movecol += hidcol
                
                if not (0 <= moverow <= 7 and 0 <= movecol <= 7):
                    break  # Exit if out of bounds

                if checkSpaceClear(moverow, movecol):
                    allowedMoves.append([moverow, movecol])

                else:
                    if checkPieceWhiteSymbol(moverow, movecol):
                        allowedCaptures.append([moverow, movecol])
                    orca = True  # Stop moving in this direction if we hit a piece


        for x in allowedCaptures:
            allowedMoves.append(x)
        
        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures
            
        if allowedMoves == []:
            return False

        return allowedMoves
    
    elif piece == '♕':
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for rawrow, hidcol in directions:
            moverow, movecol = level[0], level[1]
            scc = False

            while not scc:
                moverow += rawrow
                
                movecol += hidcol
                
                if not (0 <= moverow <= 7 and 0 <= movecol <= 7):
                    break  # Exit if out of bounds

                if checkSpaceClear(moverow, movecol):
                    allowedMoves.append([moverow, movecol])

                else:
                    if checkPieceWhiteSymbol(moverow, movecol):
                        allowedCaptures.append([moverow, movecol])
                    scc = True  # Stop moving in this direction if we hit a piece

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

        for ramrow, hidcol in directions:
            moverow, movecol = level[0], level[1]
            orca = False

            while not orca:
                moverow += ramrow
                
                movecol += hidcol
                
                if not (0 <= moverow <= 7 and 0 <= movecol <= 7):
                    break  # Exit if out of bounds

                if checkSpaceClear(moverow, movecol):
                    allowedMoves.append([moverow, movecol])

                else:
                    if checkPieceWhiteSymbol(moverow, movecol):
                        allowedCaptures.append([moverow, movecol])
                    orca = True  # Stop moving in this direction if we hit a piece

        for x in allowedCaptures:
            allowedMoves.append(x)
        
        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures
            
        if allowedMoves == []:
            return False

        return allowedMoves
    
    #king and knight took shortest amount of time to code (not counting queen)
    elif piece == '♔':

        if level[0]-1 != -1:
            
            if checkSpaceClear(level[0]-1, level[1]):
                allowedMoves.append([level[0]-1, level[1]])
            else:
                if checkPieceWhiteSymbol(level[0]-1, level[1]):
                    allowedCaptures.append([level[0]-1, level[1]])

            if level[1]-1 != -1:
                if checkSpaceClear(level[0]-1, level[1]-1):
                    allowedMoves.append([level[0]-1, level[1]-1])
                else:
                    if checkPieceWhiteSymbol(level[0]-1, level[1]-1):
                        allowedCaptures.append([level[0]-1, level[1]-1])

            if level[1]+1 != 8:
                if checkSpaceClear(level[0]-1, level[1]+1):
                    allowedMoves.append([level[0]-1, level[1]+1])
                else:
                    if checkPieceWhiteSymbol(level[0]-1, level[1]+1):
                        allowedCaptures.append([level[0]-1, level[1]+1])

        if level[0]+1 != 8:
            
            if checkSpaceClear(level[0]+1, level[1]):
                allowedMoves.append([level[0]+1, level[1]])
            else:
                if checkPieceWhiteSymbol(level[0]+1, level[1]):
                    allowedCaptures.append([level[0]+1, level[1]])

            if level[1]-1 != -1:
                if checkSpaceClear(level[0]+1, level[1]-1):
                    allowedMoves.append([level[0]+1, level[1]-1])
                else:
                    if checkPieceWhiteSymbol(level[0]+1, level[1]-1):
                        allowedCaptures.append([level[0]+1, level[1]-1])

            if level[1]+1 != 8:
                if checkSpaceClear(level[0]+1, level[1]+1):
                    allowedMoves.append([level[0]+1, level[1]+1])
                else:
                    if checkPieceWhiteSymbol(level[0]+1, level[1]+1):
                        allowedCaptures.append([level[0]+1, level[1]+1])
        
        if level[1]-1 != -1:
            if checkSpaceClear(level[0], level[1]-1):
                allowedMoves.append([level[0], level[1]-1])
                if level[1]-2 != -1 and checkSpaceClear(level[0], level[1]-3) and checkSpaceClear(level[0], level[1]-2) and checkPieceSymbol(0,0) == "♖":
                    allowedMoves.append([level[0], level[1]-2])
            else:
                if checkPieceWhiteSymbol(level[0], level[1]-1):
                    allowedCaptures.append([level[0], level[1]-1])

        if level[1]+1 != 8:
            if checkSpaceClear(level[0], level[1]+1):
                allowedMoves.append([level[0], level[1]+1])
                if level[1]+2 != 8 and checkSpaceClear(level[0], level[1]+2) and checkPieceSymbol(7,7) == "♖":
                    allowedMoves.append([level[0], level[1]+2])
            else:
                if checkPieceWhiteSymbol(level[0], level[1]+1):
                    allowedCaptures.append([level[0], level[1]+1])
        
        for x in allowedCaptures:
            allowedMoves.append(x)
        
        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures
            
        if allowedMoves == []:
            return False

        return allowedMoves
        
    else:
        print('GEM')

def pickmoveWhiteMoves(level):
    allowedMoves = []
    piece = level[2]      
    
    if piece == '♟':
        # this is for the pawn forward two moves
        if checkSpaceClear(level[0]-1,level[1]): 
            allowedMoves.append([level[0]-1,level[1]])
            if checkSpaceClear(level[0]-2,level[1]) and level[0] ==6:  
                allowedMoves.append([level[0]-2,level[1]])

        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♜':
    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for rawrow, hidcol in directions:
            move_row, move_col = level[0], level[1]
            scc = False

            while not scc:
                move_row += rawrow
                
                move_col += hidcol
                
                if not (0 <= move_row <= 7 and 0 <= move_col <= 7):
                    break  # Exit if out of bounds

                if checkSpaceClear(move_row, move_col):
                    allowedMoves.append([move_row, move_col])

                else:
                    scc = True  
                    
        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♞':

        nightnight = [(-2, 1), (-2, -1), (2, 1), (2, -1),(-1, 2), (-1, -2), (1, 2), (1, -2)]

        for cherry in nightnight:
            yaxe = level[0] + cherry[0]
            xaxe = level[1] + cherry[1]
            #check if the move is within the bounds of the board
            if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                    if checkSpaceClear(yaxe, xaxe):  # Possible capture
                        
                        allowedMoves.append([yaxe, xaxe])

        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♝':
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

        for rawrow, hidcol in directions:
            move_row, move_col = level[0], level[1]
            orca = False

            while not orca:
                move_row += rawrow
                
                move_col += hidcol
                
                if not (0 <= move_row <= 7 and 0 <= move_col <= 7):
                    break  # Exit if out of bounds

                if checkSpaceClear(move_row, move_col):
                    allowedMoves.append([move_row, move_col])

                else:
                    orca = True  # Stop moving in this direction if we hit a piece
        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♛':
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for rawrow, hidcol in directions:
            move_row, move_col = level[0], level[1]
            scc = False

            while not scc:
                move_row += rawrow
                move_col += hidcol
                
                if not (0 <= move_row <= 7 and 0 <= move_col <= 7):
                    break  # Exit if out of bounds

                if checkSpaceClear(move_row, move_col):
                    allowedMoves.append([move_row, move_col])

                else:
                    scc = True  

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

        for rawrow, hidcol in directions:
            move_row, move_col = level[0], level[1]
            orca = False

            while not orca:
                move_row += rawrow
                
                move_col += hidcol
                
                if not (0 <= move_row <= 7 and 0 <= move_col <= 7):
                    break  # Exit if out of bounds

                if checkSpaceClear(move_row, move_col):
                    allowedMoves.append([move_row, move_col])

                else:
                    orca = True  # Stop moving in this direction if we hit a piece
        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♚':
        if level[0]-1 != -1:
            
            if checkSpaceClear(level[0]-1, level[1]):
                allowedMoves.append([level[0]-1, level[1]])

            if level[1]-1 != -1:
                if checkSpaceClear(level[0]-1, level[1]-1):
                    allowedMoves.append([level[0]-1, level[1]-1])
                
            if level[1]+1 != 8:
                if checkSpaceClear(level[0]-1, level[1]+1):
                    allowedMoves.append([level[0]-1, level[1]+1])
                
        if level[0]+1 != 8:
            
            if checkSpaceClear(level[0]+1, level[1]):
                allowedMoves.append([level[0]+1, level[1]])
            

            if level[1]-1 != -1:
                if checkSpaceClear(level[0]+1, level[1]-1):
                    allowedMoves.append([level[0]+1, level[1]-1])
                

            if level[1]+1 != 8:
                if checkSpaceClear(level[0]+1, level[1]+1):
                    allowedMoves.append([level[0]+1, level[1]+1])
                
        
        if level[1]-1 != -1:
            if checkSpaceClear(level[0], level[1]-1):
                allowedMoves.append([level[0], level[1]-1])
                if level[1]-2 != -1 and checkSpaceClear(level[0], level[1]-3) and checkSpaceClear(level[0], level[1]-2) and checkPieceSymbol(0,0) == "♜":
                    allowedMoves.append([level[0], level[1]-2])
           

        if level[1]+1 != 8:
            if checkSpaceClear(level[0], level[1]+1):
                allowedMoves.append([level[0], level[1]+1])
                if level[1]+2 != 8 and checkSpaceClear(level[0], level[1]+2) and checkPieceSymbol(7,7) == "♖":
                    allowedMoves.append([level[0], level[1]+2])

        if allowedMoves == []:
            return False

        return allowedMoves
            
    else:
        print('GEM')

def pickmoveWhiteCaptures(level):
    
    allowedCaptures = []
    piece = level[2]      
    
    if piece == '♟':
        #capturing
        if level[1] -1 != -1: #diagnal to left
            if checkPieceBlackSymbol(level[0]-1,level[1]-1):
                allowedCaptures.append([level[0]-1, level[1]-1, piece])
        
        if level[1] +1 != 8: #diagnal to right
            if checkPieceBlackSymbol(level[0]-1,level[1]+1):
                allowedCaptures.append([level[0]-1, level[1]+1, piece])
        rand = []
        if not allowedCaptures:
            return rand
        else:
            rand = random.choice(allowedCaptures)

            return rand

    elif piece == '♜':
    
        #varbles
        n=1
        toDaDown = level[0]-n #silly ol caleb mixed up x and y
        scc = False
        while toDaDown !=-1 and scc == False:
            # y cords to the left take it back now yall
            if checkSpaceClear(toDaDown,level[1]) == False:
                if checkPieceBlackSymbol(toDaDown,level[1]):
                    allowedCaptures.append([toDaDown,level[1], piece])
                    scc = True
                else:
                    scc = True

            toDaDown = level[0]-n
            n+= 1
        
        #y cords to the right
        scc = False
        n=1
        toDaUp = level[0]+n
        while toDaUp != 8 and scc == False: #toda up is the boandarys of the thing, scc make ssure that tehre is a piece.
            if checkSpaceClear(toDaUp,level[1]) == False: #making sure rooks dont hit walls
                if checkPieceBlackSymbol(toDaUp,level[1]):
                    allowedCaptures.append([toDaUp,level[1], piece])
                    scc = True
                else: #final check on making sur eteh rooks cant teleport
                    scc = True
            toDaUp = level[0]+n
            n+= 1
            
        
        scc = False
        n=1
        takeItLeft = level[1]-n
        while takeItLeft != -1 and scc == False:
            #y cords to the down and up
            if checkSpaceClear(level[0],takeItLeft) == False:
                if checkPieceBlackSymbol(level[0],takeItLeft):
                    allowedCaptures.append([level[0],takeItLeft, piece])
                    scc = True
                else:
                    scc = True
            takeItLeft = level[1]-n
            n+= 1
            
        scc = False
        n = 1
        takeItRight = level[1]+n
        while takeItRight != 8 and not scc:
            if not checkSpaceClear(level[0],takeItRight): #checking for captures
                if checkPieceBlackSymbol(level[0],takeItRight):
                    allowedCaptures.append([level[0],takeItRight, piece])
                    scc = True
                else: #final check on making sur eteh rooks cant teleport cant have teleporting rooks in my town
                    scc = True
            takeItRight = level[1]+n
            n+= 1

        rand = []
        if not allowedCaptures:
            return rand
        else:
            rand = random.choice(allowedCaptures)

            return rand

    elif piece == '♞':

        nightnight = [(-2, 1), (-2, -1), (2, 1), (2, -1),(-1, 2), (-1, -2), (1, 2), (1, -2)]

        for cherry in nightnight:
            yaxe = level[0] + cherry[0]
            xaxe = level[1] + cherry[1]
            #check if the move is within the bounds of the board
            if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                    if not checkSpaceClear(yaxe, xaxe):  # Possible capture
                        if checkPieceBlackSymbol(yaxe, xaxe):
                            allowedCaptures.append([yaxe, xaxe, piece])
 
        rand = []
        if not allowedCaptures:
            return rand
        else:
            rand = random.choice(allowedCaptures)
            # print(rand)
            return rand

    elif piece == '♝':
        moveUp = level[0]-1
        moveDown = level[0]+1
        moveLeft = level[1]-1
        moveRight = level[1]+1

        #top corner left
        orca = False
        while moveUp != -1 and moveLeft != -1 and orca == False:
            if checkPieceBlackSymbol(moveUp,moveLeft):
                allowedCaptures.append([moveUp,moveLeft, piece])
                orca = True
            elif checkPieceWhiteSymbol(moveUp,moveLeft):
                orca = True

            moveUp -= 1
            moveLeft -= 1

        moveUp = level[0]-1
        moveLeft = level[1]-1

        #top corner right
        orca = False
        while moveUp != -1 and moveRight != 8 and orca == False:
            if checkPieceBlackSymbol(moveUp,moveRight):
                allowedCaptures.append([moveUp,moveRight, piece])
                orca = True
            elif checkPieceWhiteSymbol(moveUp,moveLeft):
                orca = True

            moveUp -= 1
            moveRight += 1

        moveUp = level[0]-1
        moveRight = level[1]+1

        #bottom corner left
        orca = False
        while moveDown != 8 and moveLeft != -1 and orca == False:
            
            if checkPieceBlackSymbol(moveDown,moveLeft):
                allowedCaptures.append([moveDown,moveLeft, piece])
                orca = True
            elif checkPieceWhiteSymbol(moveDown,moveLeft):
                orca = True

            moveDown += 1
            moveLeft -= 1
        
        moveDown = level[0]+1

        #top corner NF
        orca = False
        while moveDown != 8 and moveRight != 8 and orca == False:
            
            if checkPieceBlackSymbol(moveDown,moveRight):
                allowedCaptures.append([moveDown,moveRight, piece])
                orca = True
            elif checkPieceWhiteSymbol(moveDown,moveRight):
                orca = True

            moveDown += 1
            moveRight += 1

        rand = []
        if not allowedCaptures:
            return rand
        else:
            rand = random.choice(allowedCaptures)

            return rand

    elif piece == '♛':

        #varbles
        n=1
        toDaDown = level[0]-n #silly ol caleb mixed up x and y
        scc = False
        while toDaDown !=-1 and scc == False:
            # y cords to the left take it back now yall
            if checkSpaceClear(toDaDown,level[1]) == False:
                if checkPieceBlackSymbol(toDaDown,level[1]):
                    allowedCaptures.append([toDaDown,level[1], piece])
                    scc = True
                else:
                    scc = True

            toDaDown = level[0]-n
            n+= 1
        
        #y cords to the right
        scc = False
        n=1
        toDaUp = level[0]+n
        while toDaUp != 8 and scc == False: #toda up is the boandarys of the thing, scc make ssure that tehre is a piece.
            if checkSpaceClear(toDaUp,level[1]) == False: #making sure rooks dont hit walls
                if checkPieceBlackSymbol(toDaUp,level[1]):
                    allowedCaptures.append([toDaUp,level[1], piece])
                    scc = True
                else: #final check on making sur eteh rooks cant teleport
                    scc = True
            toDaUp = level[0]+n
            n+= 1
            
        scc = False
        n=1
        takeItLeft = level[1]-n
        while takeItLeft != -1 and scc == False:
            #y cords to the down and up
            if checkSpaceClear(level[0],takeItLeft) == False:
                if checkPieceBlackSymbol(level[0],takeItLeft):
                    allowedCaptures.append([level[0],takeItLeft, piece])
                    scc = True
                else:
                    scc = True
            takeItLeft = level[1]-n
            n+= 1
            
        scc = False
        n = 1
        takeItRight = level[1]+n
        while takeItRight != 8 and not scc:
            if not checkSpaceClear(level[0],takeItRight): #checking for captures
                if checkPieceBlackSymbol(level[0],takeItRight):
                    allowedCaptures.append([level[0],takeItRight, piece])
                    scc = True
                else: #final check on making sur eteh rooks cant teleport cant have teleporting rooks in my town
                    scc = True
            takeItRight = level[1]+n
            n+= 1

        moveUp = level[0]-1
        moveDown = level[0]+1
        moveLeft = level[1]-1
        moveRight = level[1]+1

        #top corner left
        orca = False
        while moveUp != -1 and moveLeft != -1 and orca == False:
            if checkPieceBlackSymbol(moveUp,moveLeft):
                allowedCaptures.append([moveUp,moveLeft, piece])
                orca = True
            elif checkPieceWhiteSymbol(moveUp,moveLeft):
                orca = True

            moveUp -= 1
            moveLeft -= 1

        moveUp = level[0]-1
        moveLeft = level[1]-1

        #top corner right
        orca = False
        while moveUp != -1 and moveRight != 8 and orca == False:
            if checkPieceBlackSymbol(moveUp,moveRight):
                allowedCaptures.append([moveUp,moveRight, piece])
                orca = True
            elif checkPieceWhiteSymbol(moveUp,moveLeft):
                orca = True

            moveUp -= 1
            moveRight += 1

        moveUp = level[0]-1
        moveRight = level[1]+1

        #bottom corner left
        orca = False
        while moveDown != 8 and moveLeft != -1 and orca == False:
            
            if checkPieceBlackSymbol(moveDown,moveLeft):
                allowedCaptures.append([moveDown,moveLeft, piece])
                orca = True
            elif checkPieceWhiteSymbol(moveDown,moveLeft):
                orca = True

            moveDown += 1
            moveLeft -= 1
        
        moveDown = level[0]+1

        #top corner NF
        orca = False
        while moveDown != 8 and moveRight != 8 and orca == False:
            
            if checkPieceBlackSymbol(moveDown,moveRight):
                allowedCaptures.append([moveDown,moveRight, piece])
                orca = True
            elif checkPieceWhiteSymbol(moveDown,moveRight):
                orca = True

            moveDown += 1
            moveRight += 1

        rand = []
        if not allowedCaptures:
            return rand
        else:
            rand = random.choice(allowedCaptures)

            return rand       

    elif piece == '♚':
        if level[0]-1 != -1:
            
            if checkPieceBlackSymbol(level[0]-1, level[1]):
                allowedCaptures.append([level[0]-1, level[1], piece])

            if level[1]-1 != -1:
            
                if checkPieceBlackSymbol(level[0]-1, level[1]-1):
                    allowedCaptures.append([level[0]-1, level[1]-1, piece])

            if level[1]+1 != 8:
                
                    if checkPieceBlackSymbol(level[0]-1, level[1]+1):
                        allowedCaptures.append([level[0]-1, level[1]+1, piece])

        if level[0]+1 != 8:
        
            if checkPieceBlackSymbol(level[0]+1, level[1]):
                allowedCaptures.append([level[0]+1, level[1], piece])

            if level[1]-1 != -1:
                if checkPieceBlackSymbol(level[0]+1, level[1]-1):
                    allowedCaptures.append([level[0]+1, level[1]-1, piece])

            if level[1]+1 != 8:
            
                if checkPieceBlackSymbol(level[0]+1, level[1]+1):
                    allowedCaptures.append([level[0]+1, level[1]+1, piece])
        
        if level[1]-1 != -1:
        
            if checkPieceBlackSymbol(level[0], level[1]-1):
                allowedCaptures.append([level[0], level[1]-1, piece])

        if level[1]+1 != 8:
        
            if checkPieceBlackSymbol(level[0], level[1]+1):
                allowedCaptures.append([level[0], level[1]+1, piece])

        rand = []
        if not allowedCaptures:
            return rand
        else:
            rand = random.choice(allowedCaptures)

            return rand
            
    else:
        print('GEM')
