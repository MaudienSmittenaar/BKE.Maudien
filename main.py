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

#1: 2 spelers
#2: speel tegen een getrainde computer
#3: train een agent
#4: pilot piechart
#5: kijk welke hyperparameters de beste A.I. geven
print("1: Speel met 2 spelers \n 2: Speel tegen een getrainde computer \n 3: Train een A.I. \n 4: Check hoe goed bepaalde agent is \n 5: Testen hoe goed bepaalde hyperparameter combinaties werken. \n Kies wat je wilt spelen:")
choice = input()

train_agent = False
play_agent = False
score_agent = False
graph = False


if choice == '1':
  start()

if choice == '2':
  print("Tegen welke agent wil je spelen? Als je tegen de agent van dit programma wilt spelen, vul in: agent1")
  play_agent = input()

  my_agent = load(play_agent)

  my_agent.learning = False

  start(player_x=my_agent)    

if choice == '3':
  print("Hoe wil je je agent noemen?")
  name = input()

  print("Hoe vaak wil je jouw agent trainen?")
  training = int(input())

  print("Wilt u de hyperparameters aanpassen? (y/n)")
  if input() == "y":
    print("Uitleg voor hyperparameters tussen 1 en 0")
    chosen_alpha = float(input())
    chosen_epsilon = float(input())
    MyAgent(alpha=chosen_alpha, epsilon=chosen_epsilon)
  else: 
    my_agent = MyAgent()

  train(my_agent, training)
  save(my_agent, name)

  if choice == '4':
   print("Hoe heet de agent?")
   name = input()
   print("Wil je dat uw agent X of O is? Voor uw informatie: X begint altijd")
   symbol = input()

   my_agent = load(name)
   my_agent.learning = False

   validation_agent = RandomAgent()

if symbol == "x" or symbol == "X":
     validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=100)

if symbol == "o" or symbol == "O":
     validation_result = validate(agent_o=my_agent, agent_x=validation_agent, iterations=100)

plot_validation(validation_result)


if choice == "5":
   random.seed(1)

   print("Uitleg voor hyperparameters tussen 1 en 0")
   chosen_alpha = float(input())
   chosen_epsilon = float(input())

   my_agent = MyAgent(alpha=chosen_alpha, epsilon=chosen_epsilon)
   random_agent = RandomAgent()

   train_and_plot(
       agent=my_agent,
       validation_agent=random_agent,
       iterations=30,
       trainings=100,
       validations=1000)