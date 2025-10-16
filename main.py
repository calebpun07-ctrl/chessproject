from functions import red, dim, clearboard, check4chek, checkPiece,fillSpot, checkSpaceClear, clearSpot, fillboard, find_white_pieces, pickpiece, showBoard, startGame , pickmove, findPeice
from simplestuff import playTheGameButAdvanced2AI, clearBoardStart, movemove,playTheGameBut2AI, movemove2, playTheGame, testerSetup, playTheGameButEASY, playTheGameButAI
from checkmate import thefinalfunction, thefinalfunctionblack

'''
♔ ♕ ♗ ♘ ♖ ♙ black
♚ ♛ ♝ ♞ ♜ ♟ white
'''

fillboard()
fillSpot(5,5,"♔")
fillSpot(4,6,"♖")
# fillSpot(1,5,"♙")
# fillSpot(2,2,"♚")
# fillSpot(2,3,"♔")

# playTheGameButAdvanced2AI()
# playTheGameBut2AI()
# TheFinalFunction(1)
# playTheGameButAdvanced2AI()
playTheGame()


