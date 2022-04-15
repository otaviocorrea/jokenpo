import os
import settings
import header
import functions

os.system('clear')
header.printHeader()

spots = 0
rounds = 0
player = input("Type your name: ").upper()

while(spots < settings.pointsNeeded):
	print("\nSPOTS: {0} | ROUNDS: {1}\n".format(spots, rounds))
	print("Insert your move: ")
	player_choice = int(input("\n📄 PAPER (1) | 🪨 STONE (2) | ✂️ SCISSORS (3): "))
	if(player_choice in settings.options):
		bot_choice = functions.get_bot_choice()
		duel = functions.battle(player_choice, bot_choice)
		if (duel == settings.points_when_winning):
			print("\n😎 You: {0}\n🤖 Bot: {1}\n\n.:: You won 🥇\n".format(player_choice, bot_choice))
		elif (duel == settings.points_on_tie):
			print("\n😎 You: {0}\n🤖 Bot: {1}\n\n.:: A tie 😕\n".format(player_choice, bot_choice))
		else:
			print("\n😎 You: {0}\n🤖 Bot: {1}\n\n.:: You lost 😞\n".format(player_choice, bot_choice))
		pass
		spots = spots + duel
		rounds = rounds + 1
	else:
		print("\n 🚨 {0} - It's not a valid move! 🚨\n\n".format(player_choice))
	pass

dados = str(rounds) + " " + str(spots)  + " " + str(player)
placar = functions.updateScore(dados)