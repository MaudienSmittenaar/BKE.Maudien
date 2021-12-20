from _ml import MLAgent, train, save, load, train_and_plot, RandomAgent, validate, plot_validation
 from _core import is_winner, opponent, start

 import random
 @@ -13,16 +13,53 @@ def evaluate(self, board):
         else:
             reward = 0
         return reward





 train_agent = True
 play_agent = False
 score_agent = True
 graph = False



 if train_agent == True:
   my_agent = MyAgent(alpha=0.1, epsilon=0.8)

   train(my_agent, 30000)

   save(my_agent, 'MyAgent_30000')


 if play_agent == True:
   my_agent = load('MyAgent_30000')

   my_agent.learning = False

   start(player_x=my_agent)    

 if score_agent == True:
   my_agent = load('MyAgent_30000')
   my_agent.learning = False

   validation_agent = RandomAgent()

   validation_result = validate(agent_o=my_agent, agent_x=validation_agent, iterations=100)

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