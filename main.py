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
itterate = 150
training = 500000
play = "y"
while play == "y":
  print("\n 1: Spelen met 2 spelers \n 2: Spelen tegen een zeer goed getrainde computer \n 3: A.I. trainen \n 4: Controleer hoe goed een bepaalde agent is \n 5: Toetsen hoe goed combinaties van bepaalde hyperparameter werken \n Maak uw keuze: \n")
  choice = input()



  if choice == '1':
    start()

  if choice == '2':
    print("Tegen welke agent wenst u spelen? Wanneer u tegen de agent van dit programma wilt spelen, vul dan 'agent1'in.")
    play_agent = input()

    my_agent = load(play_agent)
    my_agent.learning = False
    start(player_x=my_agent)    

  if choice == '3':
    print("Hoe wilt u uw agent noemen?")
    name = input()
    while training >= 500000:
      print("Hoe vaak wilt u uw agent trainen? Dit is maximaal 500000 keer")
      training = int(input())

    print("Zou u de hyperparameters willen aanpassen? (y/n)")
    if input() == "y":
      print("Uitleg voor hyperparameters tussen 1 en 0")
      chosen_alpha = float(input())
      chosen_epsilon = float(input())
      my_agent = MyAgent(alpha=chosen_alpha, epsilon=chosen_epsilon)
    else: 
      my_agent = MyAgent()

    train(my_agent, training)
    save(my_agent, name)

    print("\nUw agent is succesvol getraind en hij is nu opgeslagen onder: " + name)

  if choice == '4':
    print("Heeft u de grafiek straks goed bekeken? Dan kunt u verder gaan door de grafiek weg te klikken.")
    print("Hoe wilt u uw agent noemen? Als u zelf nog geen agent heeft getraind kunt u 'agent1' trainen, anders de door uw genoemde agent.")
    name = input()
    print("Wilt u voor X of voor O spelen? Voor uw informatie: X begint altijd")
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
    print("Als de grafiek getekend is, klik het weg om verder te gaan")

    random.seed(1)

    print("Uitleg voor hyperparameters tussen 1 en 0")
    print("alpha:")
    chosen_alpha = float(input())
    print("epsilon:")
    chosen_epsilon = float(input())

    while itterate >= 51:
      print("Hoeveel iteraties wil je doen? U kunt maximaal 50 iteraties kiezen.")
      itterate = int(input())

    my_agent = MyAgent(alpha=chosen_alpha, epsilon=chosen_epsilon)
    random_agent = RandomAgent()

    train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=itterate,
      trainings=100,
      validations=1000)

  print("Wilt u verder gaan? (Voor ja type: 'y'. Voor nee type: 'n')")
  play = input()

play = "n"
print("Dankjewel voor het spelen! Tot ziens.")