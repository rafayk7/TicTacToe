import random

def genBoard():
   #Generate an empty board
   return [0,0,0,0,0,0,0,0,0]

def printBoard(T):
   #Print the board in a user-friendly manner
   if len(T) != 9:
      return False
   for i in T:
      if (i != 0) and (i != 1) and (i != 2):
         return False

   msg=[]
   pos=0
   for i in T:
      if (i==1):
         msg += ["X"]
      elif (i==2):
         msg += ["O"]
      else:
         msg += list(str(pos))
      pos+=1

   s = " " + msg[0] + " | " + msg[1] + " | " + msg[2]
   print(s)
   print("---|---|---")
   s = " " + msg[3] + " | " + msg[4] + " | " + msg[5]
   print(s)
   print("---|---|---")
   s = " " + msg[6] + " | " + msg[7] + " | " + msg[8]
   print(s)
   return True


def analyzeBoard(t):
   #Check for wins, analyze the diagonals, horizontals and verticals. Return the winner (which is whatever is in that position)
    if t[0] == t[1] == t[2] != 0:
        return t[0]
    if t[3] == t[4] == t[5] != 0:
        return t[3]
    if t[6] == t[7] == t[8] != 0:
        return t[6]
    if t[0] == t[3] == t[6] != 0:
        return t[0]
    if t[1] == t[4] == t[7] != 0:
        return t[1]
    if t[2] == t[5] == t[8] != 0:
        return t[2]
    if t[0] == t[4] == t[8] != 0:
        return t[0]
    if t[2] == t[4] == t[6] != 0:
        return t[2]

    n_opens=0
    for i in t:
       if i==0:
          n_opens+=1
    if n_opens == 0:
        return 3
    else:
        return 0

def findOpponent(player):
   if player==1:
      opponent = 2
   elif player==2:
      opponent= 1
   return opponent

def checkError(T):
   good=1
   prod = 1
   if len(T)!=9:
      good=0

   #Check if there is an empty spot
   for element in T:
      prod=prod*element
   if (prod!=0):
      good=0
   for element in T:
      if (element!=0) and (element!=1) and (element!=2):
         good=0
   return good

def genNonLoser(T, player):
   good=checkError(T)
   opponent = findOpponent(player)
   returned = 0
   if good==1:
      board = T
      for i in range(len(board)):
         if board[i]==0:
            board[i] = opponent
            if analyzeBoard(board)==opponent:
               return i
               returned = 1
            else:
               board[i]=0
      if returned==0:
         return -1
   else:
      return -1

def genWinningMove(T, player):
   good = checkError(T)
   returned = 0
   if good==1:
      board = T
      for i in range(len(board)):
         if board[i]==0:
            board[i] = player
            if analyzeBoard(board)==player:
               return i
               returned = 1
            else:
               board[i]=0
      if returned == 0:
         return -1
   else:
      return -1

def genRandomMove(T, player):
   good = checkError(T)
   good_indices = []
   if good==1:
      for i in range(len(T)):
         if T[i]==0:
            good_indices = good_indices + [i]
      moveindex = random.randint(0,len(good_indices)-1)
      move = good_indices[moveindex]
      return move
   else:
      return -1

def genOpenMove(T, player):
   open = []
   good = checkError(T)
   if good==1:
      for i in range(len(T)):
         if T[i]==0:
            open = open +[i]
      move = open[0]
      return move
   else:
      return -1


