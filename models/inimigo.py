from .personagem import Personagem

# inimigo = normal
class Inimigo(Personagem):
    def atacar(self, outro):
        dano = self.ataque - outro.defesa
        if dano > 0:
            outro.receber_dano(dano)
            print(f"\n 👹 {self.nome} meteu a porrada no {outro.nome} e causou {dano} de dano, deixando {outro.nome} com {outro.vida} de vida")
        else:
            print(f"\n 👹 {self.nome} tentou atacar mas foi bloqueado pelo {outro.nome}.")
