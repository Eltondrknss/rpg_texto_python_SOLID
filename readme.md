## Descrição Geral

Este projeto é um RPG de texto desenvolvido em Python, com foco em boas práticas de programação orientada a objetos e princípios SOLID. O jogador pode escolher entre diferentes classes de herói e enfrentar batalhas automáticas contra inimigos gerados pelo sistema. O jogo é totalmente executado no terminal, com mensagens temáticas e feedbacks dinâmicos.

---

## Funcionalidades

- Escolha de nome e classe do personagem (Mago, Guerreiro ou Arqueiro).
- Geração automática de inimigos.
- Sistema de batalha por turnos, com cálculo de dano e defesa.
- Mensagens temáticas para cada ação.
- Encapsulamento dos atributos dos personagens.
- Fácil expansão para novas classes e mecânicas.
- Código modular e organizado.

---

## Estrutura do Projeto

```
RPG_SOLID/
│
├── main.py                # Ponto de entrada do jogo
├── models/
│   ├── personagem.py      # Classe base Personagem
│   ├── guerreiro.py       # Classe Guerreiro
│   ├── mago.py            # Classe Mago
│   ├── arqueiro.py        # Classe Arqueiro
│   └── ...                # Outras classes e utilitários
├── README.md              # Guia rápido do projeto
├── documentacao.md        # Documentação detalhada
```


---

## Classes

### Personagem

Classe base para todos os personagens do jogo.  
Responsável por atributos comuns e métodos utilitários.

### Guerreiro

Subclasse de `Personagem`, representa o guerreiro.

### Mago

Subclasse de `Personagem`, representa o mago.

### Arqueiro

Subclasse de `Personagem`, representa o arqueiro.

---

## Fluxo do Jogo

1. O jogador inicia o programa e digita seu nome.
2. Escolhe uma classe de personagem.
3. O sistema gera um inimigo automaticamente.
4. Os personagens lutam em turnos, alternando ataques.
5. Cada ataque calcula o dano com base nos atributos de ataque e defesa.
6. Mensagens temáticas são exibidas a cada ação.
7. O jogo termina quando um dos personagens morre, exibindo o resultado final.

---

## Execução

1. Instale Python 3.x em seu computador.
2. Clone o repositório:

```bash
git clone https://github.com/Eltondrknss/rpg_texto_python_SOLID
```

3. Entre na pasta do projeto:

```bash
cd rpg-texto-python
```

4. Execute o jogo:

```bash
python main.py
```

5. Siga as instruções no terminal para jogar.
