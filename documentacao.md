# Documentação Completa - RPG de Texto Python (SOLID)

---

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

- **main.py**: Gerencia o fluxo principal do jogo, entrada do usuário e loop de batalha.
- **models/**: Contém todas as classes de personagens e subclasses.
- **README.md**: Guia rápido para execução e entendimento do projeto.
- **documentacao.md**: Documentação detalhada sobre arquitetura e funcionamento.

---

## Detalhamento das Classes

### Personagem

Classe base para todos os personagens do jogo.  
Responsável por atributos comuns e métodos utilitários.

**Atributos:**
- `nome`: Nome do personagem.
- `vida`: Vida atual.
- `vida_maxima`: Vida máxima.
- `ataque`: Valor de ataque.
- `defesa`: Valor de defesa.

**Métodos:**
- `receber_dano(quantidade_dano)`: Reduz vida do personagem, impedindo valores negativos.
- `curar(quantidade_cura)`: Recupera vida até o máximo permitido.
- `esta_vivo()`: Retorna se o personagem está vivo.
- `atacar(outro)`: Método abstrato, implementado nas subclasses.
- `status()`: Exibe status atual do personagem.
- `morreu()`: Retorna se o personagem morreu.

### Guerreiro

Subclasse de `Personagem`, representa o guerreiro.

**Atributos:**  
Herdados de Personagem.

**Métodos:**
- `atacar(outro)`: Calcula dano como `ataque - (defesa // 2)` do oponente. Garante que o dano seja positivo antes de aplicar. Exibe mensagem de ataque ou bloqueio.

### Mago

Subclasse de `Personagem`, representa o mago.

**Atributos:**  
Herdados de Personagem.

**Métodos:**
- `atacar(outro)`: Pode ter cálculo de dano especial, como ignorar parte da defesa ou causar dano extra.

### Arqueiro

Subclasse de `Personagem`, representa o arqueiro.

**Atributos:**  
Herdados de Personagem.

**Métodos:**
- `atacar(outro)`: Pode ter chance de ataque crítico ou dano variável.

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

## Princípios SOLID

- **Single Responsibility:** Cada classe tem uma responsabilidade única (ex: Personagem gerencia atributos e métodos comuns, subclasses implementam ataques específicos).
- **Open/Closed:** O sistema permite adicionar novas classes de personagem sem modificar as existentes.
- **Liskov Substitution:** Subclasses podem ser usadas no lugar da classe base sem alterar o funcionamento.
- **Interface Segregation:** Métodos são bem definidos e separados por responsabilidade.
- **Dependency Inversion:** O código depende de abstrações (`Personagem`), não de implementações concretas.

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
