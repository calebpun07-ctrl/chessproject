"""
anyone who sees this be warned
this can be confusing at some times. unfortunatly, a stupid highschooler began writing this, 
and many varible names are bad varible names. I am afriad to change them
i started this on a roadtrip in washinton on very windy roads.
good luck if you wish to optimize it
This file is also just the code for playing chess. this has nothing to do with the bot(ai)

after like two years, changed to using █ with color.
"""
# Define board size
rows, cols = 8, 8
global board
board = [["█"for _ in range(cols)] for _ in range(rows)]
#varbles
GEM = "genreic error message"
valid_pieces = {'♔', '♚', '♕', '♛', '♗', '♝', '♘', '♞', '♖', '♜', '♙', '♟'}
white_pieces = {'♚', '♛', '♝', '♞', '♜', '♟'}
black_pieces = {'♔', '♕', '♗', '♘', '♖', '♙'}
BLACK = "\033[30m"
RED = "\033[31m"
RESET = "\033[0m"
USE_COLOR = True
#this function starts teh game (VERY USEFUL DO NOT DELETE)
def startGame():
    """
    This function does nothing at all. literaly. 
    DO NOT DELETE
    """
    print("the game has begun\nit is whites turn")
    global turn
    turn = 1 #if you remove this the progarm break liek the coconut image

def dim(s): 
    """adds black to a blank space"""
    return (BLACK + s + RESET) if USE_COLOR else s # i never knew you could do colors in teh terminal like this

def red(peice):
    """adds red to peice to show capture"""
    return (RED + peice + RESET) if USE_COLOR else peice

def clearboard():
    global board
    rows, cols = 8, 8
    board = [["█"for _ in range(cols)] for _ in range(rows)]

def fillboard():
    """Fills the board 2d array with White and Black pieaces"""
    for col in range(cols):
        board[1][col] = '♙'  #White
        board[6][col] = '♟'  #Black

    #towers
    board[0][0] = board[0][7] = '♖'  
    board[7][0] = board[7][7] = '♜' 

    board[0][1] = board[0][6] = '♘' 
    board[7][1] = board[7][6] = '♞' 

    board[0][2] = board[0][5] = '♗' 
    board[7][2] = board[7][5] = '♝' 

    board[0][3] = '♕'  #j wait lol this is teh black queen
    board[7][3] = '♛'  #i forgot i sqitched them twice

    board[0][4] = '♔'  
    board[7][4] = '♚' 

def showBoard():
    """Auto 'clears' the board, then prints the chars in the board and dims every other char to make checker pattern"""
    print("\033[2J\033[H", end="\n")
    
    global board
    x = False
    n = 1
    for row in board:
        line = []
        if n%2 == 0: x = True
        else: x = False
        for col in row:
            if col=="█" or col=="▞":
                if x: line.append(dim(col)) 
                else: line.append(col)
                x = not x
            else:
                if x: line.append(col)
                else: line.append(col)
                x = not x
        print("       ",n,' '.join(str(piece) for piece in line)) # display peices and y axis
        n+=1
    print("          1 2 3 4 5 6 7 8\n") #display x axis

def validate_input(user_prompt, data_type='int', range=(float("-inf"), float("inf"))):
    """
    Validates a users input. 
        user_prompt: The question/input that gets repeated
        data_type: Whatever data type need to be validated. default is set to int.
        range: 
            for int, is the values that can be input can be within
            for str, is what the value is allowed to be (ex: yes, no)
    """
    while True:
        input_unchecked = input(user_prompt).strip()
        if (data_type == 'int'):
            if input_unchecked.isdigit():
                input_unchecked = int(input_unchecked)
                if range[0] <= input_unchecked <= range[1]: return int(input_unchecked)
                else: print(f"Number not in range. Please enter a number from {range[0]} to {range[1]}")
            else:
                print("Incorrect data type. Try again")
                continue
        
        elif data_type == 'str':
            if (input_unchecked not in range) and (range != (float("-inf"), float("inf"))):
                print(f"Please put {range}")
                continue
            return input_unchecked

def checkPiece(x: int,y: int):
    """
    Takes x and y values and then returns the string NAME of the peice, or if its a blank space returns 0 and if
    its a error returns 1. Used to check NAME!
    """

    piece = board[x][y]

    if piece == '♔' or piece == '♚':return "king"
    elif piece == '♕' or piece == '♛':return "queen" #j
    elif piece == '♗' or piece == '♝':return "bishop"
    elif piece == '♘' or piece == '♞':return "knight"
    elif piece == '♖' or piece == '♜':return "rook"
    elif piece == '♙' or piece == '♟':return "pawn"
    elif piece == "█": return 0
    else:
        print("uh oh caleb sucks a coding (this error message is brought to you by the checkPiece function and clabes lack of skill)")
        return 1

def checkPieceSymbol(x: int,y: int):
    """
    Takes cords (x and y), and returns the peice that is at those cords. if a blank space returns the blank space. Error returns a 1. more important function to check the piece of the peice
    """

    piece = board[x][y]
    if piece in valid_pieces: return piece
    elif piece == "█": return "█"
    else:
        print("uh oh caleb sucks a coding line 90")
        return 1

def checkPieceWhiteSymbol(x: int,y: int) -> bool:
    """returns true if its a white piece, false if not or error"""
    piece = board[x][y]

    if piece in white_pieces: return True
    else: return False

def checkPieceBlackSymbol(x: int,y: int) -> bool:
    """returns true if its a black piece, false if not or error"""
    piece = board[x][y]
    if piece in black_pieces: return True
    else: return False

def checkSpaceClear(x: int,y: int):
    """if the spots clear it returns true, if anything else it treturns false    """
    space = checkPieceSymbol(x,y)
    if space == "█": return True
    else: return False

def checkUserMoveAllowed(listofallowed: list, usermove: list) -> bool:
    """used for making sure the user picks a move from the options given. used when the we are GETTING the move from the user. paras take a list and a the users move, as a 2d list """
    for cord in listofallowed:
        if (cord == usermove[0]) or (cord == usermove): return True
    return False

def check4chek(whoseturn: int) -> bool:
    """Returns false if king is in check. returns true if the user is not in check. """
    if whoseturn == 1:
        posofallblack = find_black_pieces()
        for sugar in posofallblack:
            if pickmoveKing(sugar, 2): return False
        return True

    elif whoseturn == 2:
        posofallwhite = find_white_pieces()
        for choclate in posofallwhite:
            if pickmoveKing(choclate, 1): return False
        return True

def chekchek(nosebleed, turn: int, showboard = True) ->bool: #this function takes the move of teh user and makes teh move
    """
    this function takes the move of the user and makes said move. if the move results in check and returns True to stop pick move, and tells user that they failed to get out of check
    if showboard is true, then itll show the baord and print teh you cailed ot get out
    of check. if it is set to not then it wont
    """
    spot = nosebleed 
    holder = checkPieceSymbol(spot[0], spot[1])
    holder2 = checkPieceSymbol(spot[3]-1, spot[4]-1)
    clearSpot(spot[0], spot[1])
    fillSpot(spot[3],spot[4],spot[2], False) #puts peice in place
    thing = check4chek(turn) #checks if its in check
    if thing: return False #its not in check
    elif thing == False: # its in check
        #replace the peicace that it was in 
        fillSpot(spot[0]+1,spot[1]+1,holder, False)
        fillSpot(spot[3],spot[4],holder2, False)
        if showboard:
            showBoard()
            print("You failed to get out of check, try again")
        return True

def TheFinalFunction(whoseturn:int) ->bool:
    """Uses pickmoveKing."""
    #checkmate function
    if whoseturn == 1:
        for sugar in find_black_pieces():
            if pickmoveKing(sugar, 2): return False
        return True

    if whoseturn == 2:
        for choclate in find_white_pieces():
            if pickmoveKing(choclate, 1): return False
        return True

def find_black_pieces():
    """Returns a list of black pieces. each index has (y,x,piece)"""
    blackpiecespositions = []
    for y in range(8):  # go through rows
        for x in range(8):  # go through columns
            if board[y][x] in black_pieces:
                blackpiecespositions.append((y, x, board[y][x]))
    return blackpiecespositions

def find_white_pieces() -> list:
    """Returns a list of white pieces. each index has (y,x,piece)"""
    white_pieces = {'♚', '♛', '♝', '♞', '♜', '♟'}
    white_pieces_positions = []
    for y in range(8):  # yet again through rows
        for x in range(8):  # yet go the through columns
            if board[y][x] in white_pieces:
                white_pieces_positions.append((y, x, board[y][x]))
    return white_pieces_positions

def findPeice(peice):
    """Taking the str of a peice, will return the cords of nearest one, starting from the top left down"""
    rat = peice
    for y in range(8):
        for x in range(8):
            if board[y][x] == rat:
                honey = [y,x]
                return honey      

def clearSpot(y,x):
    """Sets spot at y,x to a blank space"""
    board[y][x] = "█"

def fillSpot(y,x, piece, show=True): #piece must be a real peice not some lame name
    """fills spot, takes fake cords. then shows the board. Defaultly shows the board, if show is set to false it will not"""
    board[y-1][x-1] = piece
    if show:showBoard()

def showOpenMoves(allowedMoves: list, captures = []):
    """Takes a list of cordiantes and fills each cord with a X. then it clears them. This is so that a X never stays on teh board outside fo this function. 
    I would like to add showing capture in RED"""
    for pinapple in allowedMoves:
        fillSpot(pinapple[0]+1,pinapple[1]+1, "X",False)
    showBoard()
    for applepin in allowedMoves:
        clearSpot(applepin[0],applepin[1])

def getusermovesforpickmove(allowedMoves) ->list: #saved like 200 lines of code - nope im back it does not work - it works now
    """Takes a list of allowed moves and keeps asking until you give a varible withing allowed moves. Used within pickmove(). returns a list with the [y,x] varibles"""
    moveToCordsY = validate_input('What y level for yours: ', 'int')
    moveToCordsX = validate_input('What x level for yours: ', 'int')

    moveToll = checkUserMoveAllowed(allowedMoves,[moveToCordsY-1,moveToCordsX-1])
    while moveToll == False: #loop to check if users move was vaild
        showBoard()
        print('either code is broken or that wasnt a vaild move bro. either way, not cool')
        moveToCordsY = int(input('What y level for yours: '))
        moveToCordsX = int(input('What x level for yours: '))
        moveToll = checkUserMoveAllowed(allowedMoves,[moveToCordsY-1,moveToCordsX-1])
    moveToCords = [moveToCordsY, moveToCordsX]
    
    return moveToCords

def return_user_move(allowedMoves, allowedCaptures, VW, turn):
    """To be run after code has checked all the spots a peice can move. Will showopenmoves, then get move from user, and complete the check for check, and the return the list of [x,y,peaice,x,y]"""
    moves = allowedMoves
    vanillawafer = VW
    showOpenMoves(moves)
    moves.extend(allowedCaptures)
    vanillawafer.extend(getusermovesforpickmove(moves))
    if chekchek(vanillawafer, turn):
        return False
    return vanillawafer

def pickpiece(turnnum): 
    """
    Code to get what piece the user wants to move

    Returns a list with the cordinates of the users piece and the piece itself.
    [y,x,piece] (also realcords)
    """
    if turnnum == 1:
        j= white_pieces
        player = 'White'
    else:
        j= black_pieces
        player = 'Black'
    
    while True: # it will alwas run this once
        print(f"Pick a {player} peice you would like to use")
        ylevel = validate_input("y cord first:", 'int', (1,8))
        xlevel = validate_input("x cord now:", 'int', (1,8))

        level = [ylevel -1,xlevel -1] #adds the real cords to list
        piece = checkPieceSymbol(ylevel -1,xlevel -1) 
        if piece == "█":
            showBoard()
            print(f"You selected a blank space. Please select one of {player}'s peices")
            continue
        elif piece not in j:
            showBoard()
            print(f"You need to select one of {player}'s peices")
            continue
        else:
            piecename = checkPiece(ylevel -1,xlevel -1)
            isCorrect = validate_input(f"you have selected {piece} ({piecename}) on {str(level[0]+1)},{str(level[1]+1)} .\nWas this correct? (y/n)", 'str', ['y', 'n'])
            if isCorrect == 'n':
                showBoard()
                print("starting over... make better chocies")
                continue
            elif isCorrect == 'y':
                break

    level.append(piece)
    print(level)
    return level

def pickmove(level, whoseturn):
    """
    Final function for main "functions". Takes user input of peice and its location, along with the turn number, 
    and returns varible vanillawafer, in format [y,x,piece,y,x] (or maybe flipped), where the first two are teh peice moving and the last two are where the peice goes.
    """
    vanillawafer = level
    #checks for trun, then picks avalible spots for user to choose
    allowedMoves = []
    allowedCaptures = []
    userMove = []
    piece = level[2] 
        
    if whoseturn == 1: # white turn
        if piece == '♟':
            print("possible moves")
            # this is for the pawn forward two moves
            if checkSpaceClear(level[0]-1,level[1]): 
                allowedMoves.append([level[0]-1,level[1]])
                if checkSpaceClear(level[0]-2,level[1]) and level[0] ==6:  
                    # print(level[0]-1, ",", level[1]+1) lol back when i would print stuff
                    allowedMoves.append([level[0]-2,level[1]])
            
            #capturing
            if level[1] -1 != -1: #diagnal to left
                if checkPieceBlackSymbol(level[0]-1,level[1]-1):
                    allowedCaptures.append([level[0], level[1]])
            
            if level[1] +1 != 8: #diagnal to right
                if checkPieceBlackSymbol(level[0]-1,level[1]+1):
                    allowedCaptures.append([level[0], level[1]+2])

            showOpenMoves(allowedMoves)
            allowedMoves.extend(allowedCaptures)
            
            placholderlist = getusermovesforpickmove(allowedMoves)

            for x in placholderlist:
                vanillawafer.append(x)

            if chekchek(vanillawafer,1):    
                return False

            return vanillawafer

        elif piece == '♜':
            print("possible moves")
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1]
                while True:
                    moverow += rawrow
                    movecol += hidcol
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol): allowedMoves.append([moverow, movecol])
                    else:
                        if checkPieceBlackSymbol(moverow, movecol):
                            allowedCaptures.append([moverow, movecol])
                        break  # Stop moving in this direction if we hit a piece

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)

        elif piece == '♞':
            print("possible moves")
            nightnight = [(-2, 1), (-2, -1), (2, 1), (2, -1),(-1, 2), (-1, -2), (1, 2), (1, -2)]
            
            for cherry in nightnight:
                yaxe = level[0] + cherry[0]
                xaxe = level[1] + cherry[1]
                #check if the move is within the bounds of the board
                if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                        if not checkSpaceClear(yaxe, xaxe):  # Possible capture
                            if checkPieceBlackSymbol(yaxe, xaxe):
                                allowedCaptures.append([yaxe, xaxe])
                        else:  #move to an emtpy square
                            allowedMoves.append([yaxe, xaxe])

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)

        elif piece == '♝':
            print("possible moves")
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1]
                while True:
                    moverow += rawrow
                    movecol += hidcol
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol): allowedMoves.append([moverow, movecol])
                    else:
                        if checkPieceBlackSymbol(moverow, movecol):
                            allowedCaptures.append([moverow, movecol])
                        break  # Stop moving in this direction if we hit a piece

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)

        elif piece == '♛':
            print("possible moves")
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += rawrow
                    movecol += hidcol
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol): allowedMoves.append([moverow, movecol])
                    else:
                        if checkPieceBlackSymbol(moverow, movecol):
                            allowedCaptures.append([moverow, movecol])
                        break  # Stop moving in this direction if we hit a piece

            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

            for ramrow, hidcol in directions:
                moverow, movecol = level[0], level[1]
                
                while True:
                    moverow += ramrow
                    movecol += hidcol 
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol): allowedMoves.append([moverow, movecol])
                    else:
                        if checkPieceBlackSymbol(moverow, movecol):
                            allowedCaptures.append([moverow, movecol])
                        break  # Stop moving in this direction if we hit a piece

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)
     
        elif piece == '♚':
            print("possible moves")
            kingking = [(-1, 1), (-1, -1), (1, 1), (1, -1),(0, -1), (0, 1), (-1, 0), (1, 0)]
            
            for cherry in kingking:
                yaxe = level[0] + cherry[0]
                xaxe = level[1] + cherry[1]
                #check if the move is within the bounds of the board
                if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                        if not checkSpaceClear(yaxe, xaxe):  # Possible capture
                            if checkPieceBlackSymbol(yaxe, xaxe):
                                allowedCaptures.append([yaxe, xaxe])
                        else:  #move to an emtpy square
                            allowedMoves.append([yaxe, xaxe])
            
            showOpenMoves(allowedMoves)
            allowedMoves.extend(allowedCaptures)

            moveToCordsY = int(input('What y level for yours: '))
            moveToCordsX = int(input('What x level for yours: '))

            userMove.append([moveToCordsY-1,moveToCordsX-1])
            
            moveToll = checkUserMoveAllowed(allowedMoves,userMove)
            while moveToll == False:
                print('either code is broken or that wasnt a vaild move bro. either way, not cool')
                moveToCordsY = int(input('What y level for yours: '))
                moveToCordsX = int(input('What x level for yours: '))
                userMove[0]=[moveToCordsY,moveToCordsX]
                moveToll = checkUserMoveAllowed(allowedMoves,userMove)

            if userMove[0] == [level[0], level[1]-2]:
                fillSpot(8,4, '♜')
                clearSpot(7,0)
            
            if userMove[0] == [level[0], level[1]+2]:
                fillSpot(8,6, '♜')
                clearSpot(7,7)

            vanillawafer.append(moveToCordsY)
            vanillawafer.append(moveToCordsX)
            
            if chekchek(vanillawafer,1):
                
                return False

            return vanillawafer
            
        else:
            print("ok now you broke the game, you picked a black peice, try again")
            return False
            
    elif whoseturn == 2: # blacks turn
        if piece == '♙':
            print("possible moves")
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

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)

        #rook took longest only because i had no idea what i was doing
        elif piece == '♖':
            print("possible moves")
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

            for ramrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += ramrow 
                    movecol += hidcol
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol): allowedMoves.append([moverow, movecol])
                    else:
                        if checkPieceWhiteSymbol(moverow, movecol): allowedCaptures.append([moverow, movecol])
                        break  # Stop moving in this direction if we hit a piece

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)

        elif piece == '♘':
            print("possible moves")
            
            nightnight = [(-2, 1), (-2, -1), (2, 1), (2, -1),(-1, 2), (-1, -2), (1, 2), (1, -2)]

            for cherry in nightnight:
                yaxe = level[0] + cherry[0]
                xaxe = level[1] + cherry[1]
                # Check if the move is within the bounds of the board
                if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                        if not checkSpaceClear(yaxe, xaxe):  # capture
                            if checkPieceBlackSymbol(yaxe, xaxe):
                                allowedCaptures.append([yaxe, xaxe])
                        else:  # go empty square
                            allowedMoves.append([yaxe, xaxe])

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)

        elif piece == '♗':
            print("possible moves")
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

            for ramrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += ramrow
                    movecol += hidcol
                   
                    if not (0 <= moverow <=7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol): allowedMoves.append([moverow, movecol])
                    else:
                        if checkPieceWhiteSymbol(moverow, movecol):
                            allowedCaptures.append([moverow, movecol])
                        break  # Stop moving in this direction if we hit a piece

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)
        
        elif piece == '♕':
            print("possible moves")

            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += rawrow
                    movecol += hidcol
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol): allowedMoves.append([moverow, movecol])
                    else:
                        if checkPieceWhiteSymbol(moverow, movecol): allowedCaptures.append([moverow, movecol])
                        break  # Stop moving in this direction if we hit a piece

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += rawrow
                    movecol += hidcol
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol): allowedMoves.append([moverow, movecol])
                    else:
                        if checkPieceWhiteSymbol(moverow, movecol): allowedCaptures.append([moverow, movecol])
                        break  # Stop moving in this direction if we hit a piece

            return return_user_move(allowedMoves, allowedCaptures, vanillawafer, whoseturn)
        
        #king and knight took shortest amount of time to code (not counting queen)
        elif piece == '♔':
            print("possible moves")

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

            showOpenMoves(allowedMoves)
            
            moveToCordsY = int(input('What y level for yours: '))
            moveToCordsX = int(input('What x level for yours: '))

            userMove.append([moveToCordsY-1,moveToCordsX-1])

            for x in allowedCaptures: #add in those captures
                allowedMoves.append(x)

            moveToll = checkUserMoveAllowed(allowedMoves,userMove)
            while moveToll == False:
                print('either code is broken or that wasnt a vaild move bro. either way, not cool')
                moveToCordsY = int(input('What y level for yours: '))
                moveToCordsX = int(input('What x level for yours: '))
                userMove[0]=[moveToCordsY,moveToCordsX]
                moveToll = checkUserMoveAllowed(allowedMoves,userMove)

            if userMove[0] == [level[0], level[1]+2]:
                fillSpot(1,6, '♖')
                clearSpot(1,7)

            if userMove[0] == [level[0], level[1]-2]:
                fillSpot(1,4,"♖")
                clearSpot(0,0)

            vanillawafer.append(moveToCordsY)
            vanillawafer.append(moveToCordsX)
            
            return vanillawafer
        
        else:
            print("why did you have to pick a white peice, try again")
            return False
        
    else:
        print(GEM +"line 1279")

"""
STAY AWAY FROM THIS ONE 
STAY AWAY FROM THIS ONE 
if you touch it it will break like the last time
STAY AWAY FROM THIS ONE 
"""
def pickmoveKing(level, whoseturn): #GET AWAUY FROM THSI ONE
    #checks for trun, then picks avalible spots for user to choose
    piece = level[2]

    if whoseturn == 1: # white turn
        if piece == '♟':

            if level[1] -1 != -1: #diagnal to left
                if checkPieceSymbol(level[0]-1,level[1]-1) == "♔": return True
            elif level[1] +1 != 8: #diagnal to right
                if checkPieceSymbol(level[0]-1,level[1]+1) == "♔": return True
            else: return False

        elif piece == '♜':
       
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
            for row, col in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += row
                    movecol += col
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  #cut if out of 
                    if checkSpaceClear(moverow, movecol) == False:
                        if checkPieceSymbol(moverow, movecol) == "♔": return True
                        break  
            return False

        elif piece == '♞':     
            nightnight = [(-2, 1), (-2, -1), (2, 1), (2, -1),(-1, 2), (-1, -2), (1, 2), (1, -2)] 
            for cherry in nightnight:
                yaxe = level[0] + cherry[0]
                xaxe = level[1] + cherry[1]
                # is move is within the bounds of the board
                if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                        if not checkSpaceClear(yaxe, xaxe):  # capture
                            if checkPieceSymbol(yaxe, xaxe)== "♔":
                                return True
            return False

        elif piece == '♝':
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  
            
            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += rawrow
                    movecol += hidcol
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol) == False:
                        if checkPieceSymbol(moverow, movecol) == "♔": return True
                        break  # Stop moving in this direction if we hit a piece
            return False

        elif piece == '♛':
        
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  
            
            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += rawrow
                    movecol += hidcol
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol) == False:
                        if checkPieceSymbol(moverow, movecol) == "♔": return True
                        break  # Stop moving in this direction if we hit a piece

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

            for row, col in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += row
                    movecol += col
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  #cut if out of 
                    if checkSpaceClear(moverow, movecol) == False:
                        if checkPieceSymbol(moverow, movecol) == "♔": return True
                        break  # make sur ethy cant teleprot

            return False

        elif piece == '♚':
            kingking = [(-1, 1), (-1, -1), (1, 1), (1, -1),(0, -1), (0, 1), (-1, 0), (1, 0)]
            
            for cherry in kingking:
                yaxe = level[0] + cherry[0]
                xaxe = level[1] + cherry[1]
                #check if the move is within the bounds of the board
                if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                        if not checkSpaceClear(yaxe, xaxe):  # Possible capture
                            if (checkPieceSymbol(yaxe, xaxe)== "♚"): return True
            return False
#why do i say we so much when im just talking about me
    elif whoseturn == 2: # blacks turn
        if piece == '♙':
            if level[1] -1 != -1: #diagnal to left
                if checkPieceSymbol(level[0]+1,level[1]-1) == "♚": return True
            if level[1] +1 != 8: #diagnal to right
                if checkPieceSymbol(level[0]+1,level[1]+1) == "♚": return True
            return False

        #rook took longest only because i had no idea what i was doing                WARNING YOU ARE EDITING TEH PICKKIGN NOT PICK MOVE
        elif piece == '♖':

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
            for row, col in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += row
                    movecol += col
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  #cut if out of 
                    if checkSpaceClear(moverow, movecol) == False:
                        if checkPieceSymbol(moverow, movecol) == "♚": return True
                        break  # make sur ethy cant teleprot
            return False

        elif piece == '♘':
            nightnight = [(-2, 1), (-2, -1), (2, 1), (2, -1),(-1, 2), (-1, -2), (1, 2), (1, -2)]
            for cherry in nightnight:
                yaxe = level[0] + cherry[0]
                xaxe = level[1] + cherry[1]
                # Check if the move is within the bounds of the board
                if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                        if not checkSpaceClear(yaxe, xaxe):  # capture
                            if checkPieceSymbol(yaxe, xaxe)== "♚": return True
            return False

        elif piece == '♗':
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  
            
            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += rawrow
                    movecol += hidcol
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol) == False:
                        if checkPieceSymbol(moverow, movecol) == "♚": return True
                        break  # Stop moving in this direction if we hit a piece
            return False
        
        elif piece == '♕':
            #literlly just added rook and bishop
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  
            
            for rawrow, hidcol in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += rawrow
                    movecol += hidcol
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  # Exit if out of bounds
                    if checkSpaceClear(moverow, movecol) == False:
                        if checkPieceSymbol(moverow, movecol) == "♚": return True
                        break  # Stop moving in this direction if we hit a piece

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

            for row, col in directions:
                moverow, movecol = level[0], level[1] 
                while True:
                    moverow += row
                    movecol += col
                   
                    if not (0 <= moverow <= 7 and 0 <= movecol <= 7): break  #cut if out of 
                    if checkSpaceClear(moverow, movecol) == False:
                        if checkPieceSymbol(moverow, movecol) == "♚": return True
                        break  # make sur ethy cant teleprot
            return False
        
        elif piece == '♔':
            kingking = [(-1, 1), (-1, -1), (1, 1), (1, -1),(0, -1), (0, 1), (-1, 0), (1, 0)]
            for cherry in kingking:
                yaxe = level[0] + cherry[0]
                xaxe = level[1] + cherry[1]
                #check if the move is within the bounds of the board
                if 0 <= yaxe <= 7 and 0 <= xaxe <= 7:
                        if not checkSpaceClear(yaxe, xaxe):  # Possible capture
                            if (checkPieceSymbol(yaxe, xaxe)== "♚"): return True
            return False
        else:
            print("why did you have to pick a white peice, try again")
            return False
    else: print(GEM +' line 1816')

#fin