# 🃏 SUPERTRUNFO - Jogo de Cartas em Pygame

Bem-vindo ao repositório do **SuperTrunfo**, um jogo de cartas digital criado com **Python** e **Pygame**! Inspirado nos clássicos jogos de cartas de comparação, este projeto oferece uma experiência interativa, com diferentes níveis de dificuldade e sons ambientes.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é simular o clássico jogo **Super Trunfo**, no qual os jogadores competem comparando atributos de cartas. O jogador com o valor mais alto no atributo escolhido vence a rodada. O jogo foi desenvolvido utilizando a biblioteca **Pygame**, com foco em uma interface intuitiva.

---

## 🌟 Funcionalidades Principais

- **Tela Inicial Animada:** Com fundo em movimento, música e botões de navegação.
- **Níveis de Dificuldade:** Fácil, Médio e Difícil — altera a quantidade de cartas para cada jogador.
- **Cartas com Vários Atributos:** Comparação baseada em Velocidade, Potencia, Economia e Frenagem
- **Som Personalizado:** Música ambiente e efeitos sonoros ao clicar em botões.
- **Modo CPU:** Enfrente a inteligência artificial controlada por lógica básica.

---

## 🖥️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pygame 2.6.1:** Para gráficos, sons e interação.
- **JSON:** Armazenamento das cartas e seus atributos.
- **Fontes Personalizadas:** Para dar identidade visual ao jogo.

---

## 📁 Estrutura de Pastas

```bash
SuperTrunfo/
│
├── main.py                      # Arquivo principal que executa o jogo
├── jogo.py                      # Logica do Baralho
├── carta.py                     # Classe Carta
├── jogador.py                   # Classes Jogador e JogadorCPU
├── tela_inicial.py              # Tela com animação de fundo e botões
├── tela_dificuldade.py          # Seleção de dificuldade
├── tela_jogo.py                 # Interface da partida e logica
├── tela_regras.py               # Tela com explicação das regras
│
├── cartas.json                  # Arquivo com dados das cartas
├── requirements.txt             # Dependências do projeto (Pygame)
│
├── imagens/                     # Imagens dos planos de fundo
├── fontes/                      # Fontes pixeladas personalizadas
└── audios/                      # Efeitos sonoros e música de fundo
```

## 💡 Melhorias Futuras

- ⏳ Implementar animações de vitória/derrota.
- ⏳ Criar diferentes modos de jogo (ex: multiplayer local).
- ⏳ Adicionar mais efeitos visuais e transições suaves.
- ⏳ Melhorar a inteligência da CPU.

## 🤝 Créditos

Projeto desenvolvido por:

- [@JpPrates21](https://github.com/JpPrates21)
- [@Jr-aguiar](https://github.com/Jr-aguiar)
- [@milioneluis](https://github.com/milioneluis)


