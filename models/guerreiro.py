from .personagem import Personagem

class Guerreiro(Personagem):    #Guerreiro(nome, 120, 30, 30)
    def atacar(self, outro):
        dano = self.ataque - (outro.defesa // 2)
        if dano > 0:
            outro.receber_dano(dano)
            print(f"\n ⚔️ {self.nome} meteu a espadada no {outro.nome} e causou {dano} de dano, deixando {outro.nome} com {outro.vida} de vida")
        else:
            print(f"\n ⚔️ {self.nome} tentou atacar mas foi bloqueado pelo {outro.nome}.")