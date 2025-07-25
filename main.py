from fabricas import FabricaDePersonagens

fabrica = FabricaDePersonagens()

# inicia o jogo e a seleção de personagem
print("\nBEM VINDO AO SIMULADOR DE BATALHAS RPG DE TEXTO DO ELTON\n")
jogador_nome = input("Digite o nome do seu jogador: ")

print(f"\n Escolha sua classe :"
      "\n 1 - ⚔️  Guerreiro"
      "\n 2 - 🧙‍♂️  Mago"
      "\n 3 - 🏹  Arqueiro")

classe_escolhida = input("\n Digite o número da classe escolhida: ")

# instancia um jogador com a classe escolhida e cria um inimigo predefinido
try:
    jogador = fabrica.criar_personagem(classe_escolhida, jogador_nome)
    inimigo = fabrica.criar_personagem('inimigo', 'Jubileu')

# em caso de falha, apresenta ao usuário
except ValueError as e:
    print(e)

# loop de batalha enquanto um dos dois personagens está vivo
while jogador.esta_vivo() and inimigo.esta_vivo():
    jogador.atacar(inimigo)
    if inimigo.esta_vivo():
        inimigo.atacar(jogador)

# mensagem de fim de jogo
print("\nFIM DA BATALHA\n")

if jogador.morreu():
     print(f"{jogador.nome} morreu.\n")

if inimigo.morreu():
    print(f"{jogador.nome} venceu a luta! Parabéns, {jogador_nome}.\n")
