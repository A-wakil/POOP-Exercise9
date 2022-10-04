import random
class Rock_paper_scissors():
  def __init__(self,rounds):
    self.round=rounds
    self.c_round=1
    self.bot_wins=0
    self.p_wins=0
    print("Welcome to the game!!!\nYou have {} Rounds\nPick an option below to start the game".format(self.round))
  def bot_choice(self):
    return random.choice(["rock","paper","scissors"])
  def player_choice(self):
    playerchoice=input("Rock, Paper, or Scissors: ")
    return playerchoice.lower()
  def winner_of_a_round(self,bot,player):
    if player==bot:
      return "This round is a tie"
    if player=="rock":
      if bot=="paper":
        self.bot_wins+=1
        return "Bot wins"
      elif bot=="scissors":
        self.p_wins+=1
        return "Player wins"
    elif player=="paper":
      if bot=="scissors":
        self.bot_wins+=1
        return "Bot wins"
      elif bot=="rock":
        self.p_wins+=1
        return "Player wins"
    elif player=="scissors":
      if bot=="rock":
        self.bot_wins+=1
        return "Bot wins"
      elif bot=="paper":
        self.p_wins+=1
        return "Player wins"
    else:
      self.bot_wins+=1
      return "Invalid response from player, bot gets a win idiot!!!"
  def overall_winner(self):
    if self.bot_wins > self.p_wins:
      return "The bot won the game"
    elif self.bot_wins < self.p_wins:
      return "Congratulations boy, YOU won the game"
    else:
      return "The game was a tie"
num=eval(input("How many rounds of the Rock-Paper-Scissors game do you want to play: "))
game= Rock_paper_scissors(num)
for i in range(game.round):
  print("Round {}".format(game.c_round))
  game.c_round+=1
  player=game.player_choice()
  bot=game.bot_choice()
  print("Bot's choice is: {}".format(bot))
  print(game.winner_of_a_round(bot,player))
print("bot won {} times".format(game.bot_wins))
print("player won {} times".format(game.p_wins))
print(game.overall_winner())
    
        
    
  