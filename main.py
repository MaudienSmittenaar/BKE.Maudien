import random
from bke import EvaluationAgent, start

#class MyRandomAgent(EvaluationAgent):
 # def evaluate(self, board, my_symbol, opponent_symbol):
  #  return random.randint(1, 500)
  
class MyCapableAgent(EvaluationAgent):
  def getBoardCopy(board):
    boardCopy = []
    for i in board:
       boardCopy.append(i)
     return boardCopy

   def isWinner(bo, le):
     return ((bo[7] == le and bo[8] == le and bo[9] == le) or
     (bo[4] == le and bo[5] == le and bo[6] == le) or
     (bo[1] == le and bo[2] == le and bo[3] == le) or
     (bo[7] == le and bo[4] == le and bo[1] == le) or
     (bo[8] == le and bo[5] == le and bo[2] == le) or
     (bo[9] == le and bo[6] == le and bo[3] == le) or
     (bo[7] == le and bo[5] == le and bo[3] == le) or
     (bo[9] == le and bo[5] == le and bo[1] == le))

   def evaluate(self, board, my_symbol, opponent_symbol):
     for i in range (0,9):
       boardCopy = MyCapableAgent.getBoardCopy(board)
       if boardCopy[i] != None:
         boardCopy[i] = my_symbol
         if MyCapableAgent.isWinner(boardCopy, my_symbol):
           return i

     return random.randint(0,8)



 #my_random_agent = MyRandomAgent()
 my_agent = MyCapableAgent()
start(player_o = my_agent)