import cfg
import header
import functions

# CABEÇALHO
header.printHeader()

recordes = []
pontos = 0
rodadas = 0
jogador = input("Digite seu Nome:").upper()

while(pontos < cfg.pontosNecessarios):
    print("PONTOS: {0} | RODADAS: {1}\n".format(pontos, rodadas))
    print("Insira sua Jogada")
    escolha = input("PAPEL, PEDRA ou TESOURA?").upper()
    if(escolha == "PAPEL" or escolha == "PEDRA" or escolha == "TESOURA" ):
        bot = functions.bot()
        duelo = functions.batalha(escolha, bot)
        if (duelo == 3):
            print("Você: {0}\nBot: {1}\nVocê ganhou\n\n\n".format(escolha, bot))
        elif (duelo == 1):
            print("Você: {0}\nBot: {1}\nEmpate\n\n\n".format(escolha, bot))
        else:
            print("Você: {0}\nBot: {1}\nVocê perdeu\n\n\n".format(escolha, bot))
        pass
        pontos = pontos + duelo
        rodadas = rodadas + 1
    else:
        print("{0} -  Não é uma jogada valida!\n\n\n\n".format(escolha))
    pass

dados = str(rodadas) + " " + str(pontos)  + " " + str(jogador)
placar = functions.atualizarPlacar(dados)



    