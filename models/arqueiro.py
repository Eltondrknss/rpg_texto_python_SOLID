from .personagem import Personagem

# arqueiro = 10% de chance de ataque crítico (dano x2)
class Arqueiro(Personagem):
    def atacar(self, outro):
        from random import randint
        critico = randint(1,10) == 1
        dano = self.ataque - outro.defesa
        if critico:
            dano *= 2
            outro.receber_dano(dano)
            print(f"\n 🏹 {self.nome} ACERTOU UMA FLECHADA CRÍTICAAAAAAA 🏹🏹🏹 sobrou só {outro.vida} de vida pro {outro.nome}")
        elif dano > 0:
            outro.receber_dano(dano)
            print(f"\n 🏹 {self.nome} causou {dano} de dano com uma flechada, deixando {outro.nome} com {outro.vida} de vida")
        else:
            print(f"\n 🏹 {self.nome} errou a flechada e acertou um passarinho que estava voando por alí...")
