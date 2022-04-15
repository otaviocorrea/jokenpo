import settings
import os.path
from random import randint

# Defines the BOT Play
def get_bot_choice():
  return settings.options[randint(0,2)]

# Compares the Player's move with the Bot's
# and defines the points to be added or subtracted   
def battle(player_choice, bot_choice):
  if (player_choice == bot_choice):
      pontos = settings.points_on_tie
  elif (player_choice == 1 and bot_choice == 2):
      pontos = settings.points_when_winning
  elif (player_choice == 2 and bot_choice == 3):
      pontos = settings.points_when_winning
  elif (player_choice == 3 and bot_choice == 1):
      pontos = settings.points_when_winning
  else:
      pontos = settings.points_on_losing
  pass
  return pontos

# Update Scoreboard in TXT file
def updateScore(dados):
  lista = []
  final = ""

  if(not os.path.exists('rank.txt')):
    file = open("rank.txt", "+w")
    file.write('')

  for line in open('rank.txt'):
    lista.append(line)

  dados = "\n" + str(dados)
  lista.append(dados)
  
  for i in lista:
    final = final + i

  print("📜 Play history: ")
  print(final)

  placar = open("rank.txt", "+w")
  placar.write(final)