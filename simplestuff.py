from functions import showBoard, clearSpot, fillSpot, fillboard, pickmove, pickpiece, check4chek, chekchek
from chessAI import AImakemoveBlack, AImakemoveWhite
from chessBetterAI import AdvancedAImakemoveBlack, AdvancedAImakemoveWhite
from checkmate import thefinalfunction, thefinalfunctionblack

valid_pieces = {'♔', '♚', '♕', '♛', '♗', '♝', '♘', '♞', '♖', '♜', '♙', '♟'}

def playTheGame():
    # fillboard()
    showBoard()
    n = 0
    while True:
        if check4chek((n%2)+1) == False: # this one is a function that for now gets you automaticly out of check
            finland = thefinalfunction()
            if finland == False:
                print("game over.")
                break
            elif finland == True:
                vaildmoveinputed = False
                while vaildmoveinputed != True:
                    input("go")
                    #make loop to go theough and get user input until there input is one of the ways to get out of check.
            # movemove(finland)#remove once user input mad eor mad euse rinput finladn
            print("you are in check please get out of check or no")
            # n +=1
            continue

        spot = movemove2(n)
        movemove(spot)
        n +=1

def playTheGameButEASY():
    """
    This version of the game only runs for about 20 moves, does not check for check, simply gets the move and makes it. Does fill the board
    """
    fillboard()
    showBoard()
    turnNumber = 20
    for n in range(2,turnNumber):
        spot = movemove2(n)
        movemove(spot)
        turnNumber +=1

def playTheGameButAI():
    """
    Plays against the slightly good bot. Does fill the board.
    """
    fillboard()
    showBoard()
    turnNumber = 4
    for n in range(2,turnNumber):
        spot = movemove3(n)
        movemove(spot)
        turnNumber +=1

def playTheGameBut2AI():
    """
    Uses the two random AI's. Does fill the board. Prompts for input 
    after each move, if it is y, then it ends the loop. Otherwise just keep hitting enter
    """

    fillboard()
    turn_number = 2
    termitate = None
    while termitate != "y":
        # print(turn_number)
        spot = movemove2AI(turn_number)
        movemove(spot)
        termitate = input("pause:")
        turn_number +=1
    print('get terminateored')

def clearBoardStart():
    """
    Starts withe a clear board
    """
    showBoard()
    turnNumber = 20
    for n in range(2,turnNumber):
        if check4chek((n%2)+1) == False:
            print("you are in check please get out of check or no")
        spot = movemove2(n)
        movemove(spot)
        turnNumber +=1

def movemove(spot: list):
    """
    Using the list spot, clears the spot where the peice was
    and fills it at the place its going too. uses list format of:
    [7, 1, '♞', 6, 1]
    """
    clearSpot(spot[0], spot[1])
    fillSpot(spot[3],spot[4],spot[2])

def movemove2(n):
    spot = pickmove(pickpiece((n%2)+1),(n%2)+1)
    while spot == False:
        spot = pickmove(pickpiece((n%2)+1),(n%2)+1)
    
    return spot

def movemove3(n): #thsi is for teh one sided AI, updated with slightly intelgeint AI
    if (n%2)+1 == 1:
        spot = AdvancedAImakemoveWhite()
        return spot
    elif (n%2)+1 == 2:
        spot = pickmove(pickpiece(2),(n%2)+1)
        while spot == False:
            spot = pickmove(pickpiece(2),(n%2)+1)
        print(spot)
        return spot

def movemove2AI(n): #this is for the AI one
    """
    Returns 'spot', gotten from the 'AI' function. gives it back to playthegameAI
    """
    if (n%2)+1 == 1:
        spot = AImakemoveWhite()
        while chekchek(spot, 1, False):
            # print('white wanted to make this move but it resulted in check')
            # print(spot)
            spot = AImakemoveWhite()
        print("WHITE TURN")
        return spot
    elif (n%2)+1 == 2:
        spot = AImakemoveBlack()
        while chekchek(spot, 2, False):
            # print('black wanted to make this move but it resulted in check')
            # print(spot)
            spot = AImakemoveBlack()
        print("BLACK TURN")
        return spot

def playTheGameButAdvanced2AI(): #uses the capture orentied one
    """
    plays the game of chess using a bot. using movemvoe2AdvanceAI, if 
    it ever does not return a move (true or false) then it shows who loses
    """
    fillboard()
    salt = 2
    termitate = "n"
    while termitate != "y":
        print(salt) #shows the turn i think
        spot = movemove2AdvancedAI(salt) #this sends the turn to movemove2advanceAI
        if spot == False:
            print('white loses')
            break
        elif spot == True:
            print('black loses')
            break
        movemove(spot)
        termitate = input("pause:")

        if salt == 100:
            termitate = 'y'        
        salt +=1
    print('get terminateored')

def movemove2AdvancedAI(n): #this is for the AI one
    """
    Returns a move. if the move results in check, and then loops it
    until it gets out of check. that only works for white for now. for black it simply loops it
    """

    if (n%2)+1 == 1: #white turn
        spot = AdvancedAImakemoveWhite()
        while chekchek(spot, 1, False): #catches move if it is check
            print('white wanted to make this move but it resulted in check')
            check_for_check = thefinalfunction()
            print(f"Finland {check_for_check}") #find out exatully what to bug test instead of finland
            if check_for_check == False:
                return False
            movemove(check_for_check)
            input(spot)
            spot = AdvancedAImakemoveWhite() #loops it until it is not check
        print("WHITE TURN")
        return spot
    elif (n%2)+1 == 2:
        spot = AdvancedAImakemoveBlack()
        while chekchek(spot, 2, False):
            print('black wanted to make this move but it resulted in check')
            # TODO addd finalnad function   
            check_for_checkmate = thefinalfunctionblack()
            print(f"BLACK CHECKMATE CHECK: {check_for_checkmate}")
            if check_for_checkmate == False:
                return True #returns true if there is no thing black can do to get out of check
            movemove(check_for_checkmate)

            print(spot)
            spot = AdvancedAImakemoveBlack()
        print("BLACK TURN")
        return spot
    
#betatesterfunctins
def testerSetup():
    """
    Blank tester setup. You can put different peices on the board and then after that run the clearBoardStart
    """
    while True:
        print("you contol everything\npeices you could choose")
        
        print('♚', '♛', '♝', '♞', '♜', '♟', '♔', '♕', '♗', '♘', '♖', '♙')
        peiceslected = True
        while peiceslected:
            pickpeicetomove = input("What Peice would you like to palce: ")
            for cionfiencdx in valid_pieces:
                if pickpeicetomove == cionfiencdx:
                    peiceslected = False
        ycord = input('What y Cord:')
        xcord = input('What x Cord:')

        while ycord not in {1, 2, 3, 4, 5, 6, 7, 8} or xcord not in {1, 2, 3, 4, 5, 6, 7, 8}:
                print("not in range")  #need to find out
                ycord = input('What y Cord:')
                xcord = input('What x Cord:')
        fillSpot(ycord,xcord,pickpeicetomove)

        check = input('you done yet? or not (y/n)')
        if check == 'y':
            break
        elif check == 'n':
            print('ok\nready to add more')
        else:
            print('somthing happened.')
