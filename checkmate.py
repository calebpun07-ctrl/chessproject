from functions import chekchek,checkPieceBlackSymbol,checkPieceWhiteSymbol, checkPieceSymbol, pickmoveKing, find_black_pieces, check4chek, checkPiece,fillSpot, checkSpaceClear, clearSpot, fillboard, find_white_pieces, pickpiece, showBoard, board, startGame , pickmove, findPeice

def thefinalfunction():
    ourpeices = find_white_pieces()

    for peice in ourpeices: #runs through every single white piece
        movefound = False
        while movefound == False:

            #ok the goal of pickmoveAI has changed. it will now return all the possible moves of the selected peice
            thing = pickmoveWhite(peice)
            
            if thing != False:
                listOfPossibleMove = thing
                movefound == True
                break
                
            elif thing == False:
                continue

        #building bricks
        #needs to be starting cords, peice ending cords
        longAbsVarbilename = []
        for move in listOfPossibleMove: 
            brick = [peice[0],peice[1],peice[2]] 
            brick.append(move[0]+1) 
            brick.append(move[1]+1) # makes a [x,y, peice, fake x, fake y,]
            checkval = chekchek(brick, 1, False)
            
            if checkval != True:
                #this should return a value that gets you out of check
                print(f"You are in check, not checkmate. Here is how you can get out {brick}")
                return brick

    print("GAME OVER, WHITE LOSES BY CHECKMATE")
    return False

def thefinalfunctionblack():
    ourpeices = find_black_pieces()

    for peice in ourpeices: #runs through every single white piece
        movefound = False
        while movefound == False:

            #ok the goal of pickmoveAI has changed. it will now return all the possible moves of the selected peice
            thing = pickmoveBlack(peice) #NEED TO MAKE PICKMOVEBLACK
            
            if thing != False:
                listOfPossibleMove = thing
                movefound == True
                break
                
            elif thing == False:
                continue

        #building bricks
        #needs to be starting cords, peice ending cords
        longAbsVarbilename = []
        for move in listOfPossibleMove:
            brick = [peice[0],peice[1],peice[2]]
            brick.append(move[0]+1)
            brick.append(move[1]+1)
            checkval = chekchek(brick, 1, False)
            
            if checkval != True:
                #this should return a value that gets you out of check
                print(f"You are in check, not checkmate. Here is how you can get out {brick}")
                return brick

    print("GAME OVER, BLACK LOSES BY CHECKMATE")
    return False

'''
ok plan is:
add all possible moves into one file. 
Then it runs through every single move until out of check.
should work

AImake move white plan:
instead of a random one, it will just take each white peice value and do that for every single one
and make those moves and moe to the next one
'''
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
        if level[1] -1 != -1: #diagonal to left
            if checkPieceBlackSymbol(level[0]-1,level[1]-1):
                allowedCaptures.append([level[0], level[1]])
        
        if level[1] +1 != 8: #diagonal to right
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

black_pieces = {'♔', '♕', '♗', '♘', '♖', '♙'}

def pickmoveBlack(level): #UNFINSIHED
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
                    break  
                if checkSpaceClear(moverow, movecol):
                    allowedMoves.append([moverow, movecol])
                else:
                    if checkPieceBlackSymbol(moverow, movecol):
                        allowedCaptures.append([moverow, movecol])
                    scc = True  

        for x in allowedCaptures:
            allowedMoves.append(x)

        if allowedMoves == []:
            return False

        return allowedMoves

    elif piece == '♘':

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

    elif piece == '♗':
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


