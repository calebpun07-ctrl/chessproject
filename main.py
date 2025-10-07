from functions import red, dim, clearboard, check4chek, checkPiece,fillSpot, checkSpaceClear, clearSpot, fillboard, find_white_pieces, pickpiece, showBoard, board, startGame , pickmove, findPeice
from simplestuff import playTheGameButAdvanced2AI, clearBoardStart, movemove,playTheGameBut2AI, movemove2, playTheGame, testerSetup, playTheGameButEASY, playTheGameButAI
from checkmate import thefinalfunction, thefinalfunctionblack

'''
♔ ♕ ♗ ♘ ♖ ♙ black
♚ ♛ ♝ ♞ ♜ ♟ white
'''

print(red("adsdasdasdasdsa"))
fillboard()
fillSpot(7,1,"♜",False)
# fillSpot(8,5,"♙")
# fillSpot(5,1,"♙")
# fillSpot(1,5,"♙")
# fillSpot(2,2,"♚")
# fillSpot(2,3,"♔")

# showBoard()
# playTheGameButAdvanced2AI()
# playTheGameBut2AI()
# TheFinalFunction(1)
# playTheGameButAdvanced2AI()
playTheGame()


