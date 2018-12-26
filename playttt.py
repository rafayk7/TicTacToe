from tttlib import *

T = genBoard()

def auto(board):
   move = genWinningMove(board, 2)
   if move==-1:
      move = genNonLoser(board, 2)
      if move==-1:
         move = genRandomMove(board,2)
         return move
      else:
         return move
   else:
      return move

while True:
   printBoard(T)
   moveX = input("X move?")
   if (int(moveX)<=8 and int(moveX)>=0) and T[int(moveX)]==0:
      T[int(moveX)] = 1

   state = analyzeBoard(T)

   if state == 1:
      print("X won!")
      break
   elif state==3:
      print("Draw")
      break

   printBoard(T)
   moveO = auto(T)
   print(moveO)
   T[moveO] = 2
   state = analyzeBoard(T)
   if state==2:
      print("O won!")
      break
   if state==3:
      print("Draw")
      break
