from .personagem import Personagem

class Mago(Personagem):     #Mago(nome, 100, 40, 20)
    def atacar(self, outro):
        dano = (self.ataque * 2) - outro.defesa
        if dano > 0:
            outro.receber_dano(dano)
            print(f"\n 🧙‍♂️ {self.nome} lançou uma bola de fogo e causou {dano} de dano, deixando {outro.nome} com {outro.vida} de vida")
        else:
            print(f"\n 🧙‍♂️ {self.nome} lançou uma bola de fogo mas errou feio...")
