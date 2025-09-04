import random

from functions import checkSpaceClear,checkPieceSymbol,checkPieceBlackSymbol,checkSpaceClear,checkPieceWhiteSymbol, chekchek2, findPeice, showOpenMoves, pickmove, find_black_pieces, find_white_pieces
# should get every possible move then return a random one
listOfPossibleMove = []

def AImakemoveBlack():
    A = False
    ourpeices = find_black_pieces()
    checkmove = False
    while checkmove == False:
        movefound = False
        while movefound == False:
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
        # if chekchek2(brick,2):
        #     A = True
        #     print('location of piece:'+str(brick))
        #     a = input("test")
        #     continue
        print('It is blacks turn rn. We would like to make this move:')
        input(brick)
        return brick

def AImakemoveWhite():
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
            thing = pickmoveWhite(randomPeaice)
            
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
        # if chekchek2(brick,1):
        #     A = True
        #     print('location of piece:'+str(brick))
        #     a = input("test")
        #     checkmove = False
        #     continue
        print('It is whites turn rn. We would like to make this move:')
        input(brick)

        return brick

def pickmoveAI(level):
    
    #checks for trun, then picks avalible spots for user to choose
    allowedMoves = []
    allowedCaptures = []
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
                    if checkPieceBlackSymbol(moverow, movecol):
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

def pickmoveWhite(level):
    allowedMoves = []
    allowedCaptures = []
    piece = level[2]      
    
    if piece == '♟':
        # this is for the pawn forward two moves
        if checkSpaceClear(level[0]-1,level[1]): 
            allowedMoves.append([level[0]-1,level[1]])
            if checkSpaceClear(level[0]-2,level[1]) and level[0] ==6:  
                allowedMoves.append([level[0]-2,level[1]])
        
        #capturing
        if level[1] -1 != -1: #diagnal to left
            if checkPieceBlackSymbol(level[0]-1,level[1]-1):
                allowedCaptures.append([level[0], level[1]])
        
        if level[1] +1 != 8: #diagnal to right
            if checkPieceBlackSymbol(level[0]-1,level[1]+1):
                allowedCaptures.append([level[0], level[1]+2])

        for x in allowedCaptures:
            allowedMoves.append(x)

        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures

        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♜':
    
        #varbles
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for rawrow, hidcol in directions:
            moverow, movecol = level[0], level[1]
            scc = False

            while not scc:
                moverow += rawrow
                
                movecol += hidcol
                
                if not (0 <= moverow <= 7 and 0 <= movecol <= 7):
                    break  
                if checkSpaceClear(moverow, movecol):
                    allowedMoves.append([moverow, movecol])

                else:
                    if checkPieceBlackSymbol(moverow, movecol):
                        allowedCaptures.append([moverow, movecol])
                    scc = True  

        for x in allowedCaptures:
            allowedMoves.append(x)

        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures

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
                    if not checkSpaceClear(yaxe, xaxe):  # Possible capture
                        if checkPieceBlackSymbol(yaxe, xaxe):
                            allowedCaptures.append([yaxe, xaxe])
                    else:  #ove to an emtpy square
                        allowedMoves.append([yaxe, xaxe])

        for x in allowedCaptures:
            allowedMoves.append(x)

        #CODE TO MAKE AI SEMIINTELGINT
        if allowedCaptures != []:
            allowedMoves = allowedCaptures

        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♝':
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
                    if checkPieceBlackSymbol(moverow, movecol):
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

    elif piece == '♛':
        
        #literlly just added rook and bishop
        
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
                    if checkPieceBlackSymbol(moverow, movecol):
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
                    if checkPieceBlackSymbol(moverow, movecol):
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

    elif piece == '♚':
        if level[0]-1 != -1:
            
            if checkSpaceClear(level[0]-1, level[1]):
                allowedMoves.append([level[0]-1, level[1]])
            else:
                if checkPieceBlackSymbol(level[0]-1, level[1]):
                    allowedCaptures.append([level[0]-1, level[1]])

            if level[1]-1 != -1:
                if checkSpaceClear(level[0]-1, level[1]-1):
                    allowedMoves.append([level[0]-1, level[1]-1])
                else:
                    if checkPieceBlackSymbol(level[0]-1, level[1]-1):
                        allowedCaptures.append([level[0]-1, level[1]-1])

            if level[1]+1 != 8:
                if checkSpaceClear(level[0]-1, level[1]+1):
                    allowedMoves.append([level[0]-1, level[1]+1])
                else:
                    if checkPieceBlackSymbol(level[0]-1, level[1]+1):
                        allowedCaptures.append([level[0]-1, level[1]+1])

        if level[0]+1 != 8:
            
            if checkSpaceClear(level[0]+1, level[1]):
                allowedMoves.append([level[0]+1, level[1]])
            else:
                if checkPieceBlackSymbol(level[0]+1, level[1]):
                    allowedCaptures.append([level[0]+1, level[1]])

            if level[1]-1 != -1:
                if checkSpaceClear(level[0]+1, level[1]-1):
                    allowedMoves.append([level[0]+1, level[1]-1])
                else:
                    if checkPieceBlackSymbol(level[0]+1, level[1]-1):
                        allowedCaptures.append([level[0]+1, level[1]-1])

            if level[1]+1 != 8:
                if checkSpaceClear(level[0]+1, level[1]+1):
                    allowedMoves.append([level[0]+1, level[1]+1])
                else:
                    if checkPieceBlackSymbol(level[0]+1, level[1]+1):
                        allowedCaptures.append([level[0]+1, level[1]+1])
        
        if level[1]-1 != -1:
            if checkSpaceClear(level[0], level[1]-1):
                allowedMoves.append([level[0], level[1]-1])
                if level[1]-2 != -1 and checkSpaceClear(level[0], level[1]-3) and checkSpaceClear(level[0], level[1]-2) and checkPieceSymbol(0,0) == "♜":
                    allowedMoves.append([level[0], level[1]-2])
            else:
                if checkPieceBlackSymbol(level[0], level[1]-1):
                    allowedCaptures.append([level[0], level[1]-1])

        if level[1]+1 != 8:
            if checkSpaceClear(level[0], level[1]+1):
                allowedMoves.append([level[0], level[1]+1])
                if level[1]+2 != 8 and checkSpaceClear(level[0], level[1]+2) and checkPieceSymbol(7,7) == "♖":
                    allowedMoves.append([level[0], level[1]+2])
            else:
                if checkPieceBlackSymbol(level[0], level[1]+1):
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
