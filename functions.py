import cfg
import os.path
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
        pontos = cfg.pontosEmpatar
    elif (jogador == "PAPEL" and bot == "PEDRA"):
        pontos = cfg.pontosGanhar
    elif (jogador == "PEDRA" and bot == "TESOURA"):
        pontos = cfg.pontosGanhar
    elif (jogador == "TESOURA" and bot == "PAPEL"):
        pontos = cfg.pontosGanhar
    else:
        pontos = cfg.pontosPerder
    pass
    return pontos

# Atualiza o Placar no arquivo TXT
def atualizarPlacar(dados):
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

    print(final)

    placar = open("rank.txt", "+w")
    placar.write(final)