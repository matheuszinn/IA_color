# IA_color
repositório para uma atividade de Inteligência artificial

### Descrição da atividade:

A atividade consiste em desenvolver uma rede neural perceptron simples que consiga reconhecer as cores: 

- Vermelho
- Verde
- Azul
- Preto
- Branco
- Amarelo
- Magenta
- Ciano

A entrada são três valores no intervalo [-1,1], equivalentes aos valores rgb, e a camada de saída contém oito neurônios, sem camadas ocultas. Cada neurônio vai representar uma cor(classe).

## Atividade 

Foi utilizada uma função de ativação linear para os neurônios durante o treinamento, que consiste em uma função que não altera a saída de um neurônio.

Equação:  $ {\displaystyle \phi (\mathbf {v} )=a+\mathbf {v} '\mathbf {b} } $

Gráfico: ![]('./assets/grafico.png')


Após os treinamento, foi utilizada a estratégia *winner takes all* para a ativação do neurônio, ativando somento o neurônio mais estimulado. Esse neurônio terá saída 1, e os demais -1.

Isso permite que a rede sempre retorne uma cor dada um input.


### Entradas

![]('./assets/inputs.png')