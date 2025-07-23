from fabricas import FabricaDePersonagens

fabrica = FabricaDePersonagens()

print("\nBEM VINDO AO SIMULADOR DE BATALHAS RPG DE TEXTO DO ELTON\n")
jogador_nome = input("Digite o nome do seu jogador: ")

print(f"\n Escolha sua classe :"
      "\n 1 - ⚔️  Guerreiro"
      "\n 2 - 🧙‍♂️  Mago"
      "\n 3 - 🏹  Arqueiro")

classe_escolhida = input("\n Digite o número da classe escolhida: ")

try:
    jogador = fabrica.criar_personagem(classe_escolhida, jogador_nome)
    inimigo = fabrica.criar_personagem('inimigo', 'Jubileu')

except ValueError as e:
    print(e)

while jogador.esta_vivo() and inimigo.esta_vivo():
    jogador.atacar(inimigo)
    if inimigo.esta_vivo():
        inimigo.atacar(jogador)

print("\nFIM DA BATALHA\n")

if jogador.morreu():
     print(f"{jogador.nome} morreu.\n")

if inimigo.morreu():
    print(f"{jogador.nome} venceu a luta! Parabéns, {jogador_nome}.\n")