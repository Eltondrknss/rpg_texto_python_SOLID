from models.guerreiro import Guerreiro
from models.arqueiro import Arqueiro
from models.mago import Mago
from models.inimigo import Inimigo

# cria uma nova instancia da classe escolhida em main.py
class FabricaDePersonagens:
    def criar_personagem(self, tipo, nome):
        if tipo == '1':
            return Guerreiro(nome, 120, 30, 30)
        elif tipo == '2':
            return Mago(nome, 100, 40, 20)
        elif tipo == '3':
            return Arqueiro(nome, 90, 35, 25)
        elif tipo.lower() == 'inimigo':
            return Inimigo("Jubileu", 100, 30, 20)

        # retorna erro em caso de escolha fora do escopo
        raise ValueError(f"Classe desconhecida: {tipo}")
