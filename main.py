from _ml import MLAgent, train, save, load, train_and_plot, RandomAgent, validate, plot_validation

from _core import is_winner, opponent, start

import random
 
 
class MyAgent(MLAgent):
   def evaluate(self, board):
      if is_winner(board, self.symbol):
       reward = 1
      elif is_winner(board,
 opponent[self.symbol]):
       reward = -1
      else:
        reward = 0
      return reward

print("1: 2 spelers \n 2: speel tegen een getrainde computer \n 3: speel tegen een getrainde AI \n 4: train een AI en kijk hoe goed die het doet \n Kies wat je wilt spelen:")
choice = input()

train_agent = False
play_agent = False
score_agent = False
graph = False


if choice == '1':
  start()

if choice == '2':
  my_agent = MyAgent()

  train(my_agent, 30000)

  save(my_agent, 'MyAgent_30000')


if choice == '2':
   my_agent = load('MyAgent_30000')

   my_agent.learning = False

   start(player_x=my_agent)    

if score_agent == True:
   my_agent = load('MyAgent_30000')
   my_agent.learning = False

   validation_agent = RandomAgent()

   validation_result = validate(x=my_agent, agent_o=validation_agent, iterations=100)

   plot_validation(validation_result)


if graph == True:
   random.seed(1)

   my_agent = MyAgent(alpha=0.2, epsilon=0.8)
   random_agent = RandomAgent()

   train_and_plot(
       agent=my_agent,
       validation_agent=random_agent,
       iterations=50,
       trainings=100,
       validations=1000)