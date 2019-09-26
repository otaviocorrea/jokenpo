from random import randint

# Define a Jogada do BOT
def bot():
    lista_bot = ['PAPEL', 'PEDRA', 'TESOURA']
    jogada_bot = lista_bot[randint(0,2)]
    return jogada_bot

# Compara a jogada do Jogador com a do Bot 
# e define os pontos a serem somados ou subtraidos    
def batalha(jogador, bot):
    if (jogador == bot):
        pontos = 1
    elif (jogador == "PAPEL" and bot == "PEDRA"):
        pontos = 3
    elif (jogador == "PAPEL" and bot == "TESOURA"):
        pontos = -2
    elif (jogador == "PEDRA" and bot == "PAPEL"):
        pontos = -2
    elif (jogador == "PEDRA" and bot == "TESOURA"):
        pontos = 3
    elif (jogador == "TESOURA" and bot == "PAPEL"):
        pontos = 3
    elif (jogador == "TESOURA" and bot == "PEDRA"):
        pontos = -2
    return pontos

# Atualiza o Placar no arquivo TXT
def atualizarPlacar(dados):
    lista = []
    final = ""

    for line in open('rank.txt'):
        lista.append(line)

    dados = "\n" + str(dados)
    lista.append(dados)
   
    for i in lista:
        final = final + i

    print(final)

    placar = open("rank.txt", "+w")
    placar.write(final)