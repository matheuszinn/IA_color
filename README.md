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

Equação:  ![image](https://user-images.githubusercontent.com/59948197/127053502-ce37c61b-96c8-4e81-b5f0-53282151f016.png)
>> Fonte: [Perceptron](https://pt.wikipedia.org/wiki/Perceptron)

#### Gráfico:
![image](https://user-images.githubusercontent.com/59948197/127053163-105ce3dd-00cf-4158-96d8-55258e3ea9f1.png)
>> Fonte: [Funcões de Ativação](https://ichi.pro/pt/funcoes-de-ativacao-99956793768697)

Após os treinamento, foi utilizada a estratégia *winner takes all* para a ativação do neurônio, ativando somento o neurônio mais estimulado. Esse neurônio terá saída 1, e os demais -1.

Isso permite que a rede sempre retorne uma cor dada um input.

![image](https://user-images.githubusercontent.com/59948197/127056009-736f680c-b7aa-4de5-9fe8-9950df0b2422.png)
>> Fonte: [A Quantum Model for Multilayer Perceptron](https://www.researchgate.net/publication/327392288_A_Quantum_Model_for_Multilayer_Perceptron)

Uma rede perceptron contém um peso para cada entrada, que podem ser inicializados aleatóreamente. Nesse caso, todas foram iniciadas em 0. Foi também adicionado um *bias* de valor 1 para cada neurônio.

### Entradas
![image](https://user-images.githubusercontent.com/59948197/127053030-9ccca83d-4a75-463c-80d2-ad2224ee3ddb.png)

Pode ser recebida uma entrada em forma de **RGB**, Hexadecimal ou deixar que seja gerado uma cor aleatória. Em qualquer um dos casos, os valores são transformados em 3 (componetne r,g e b), e normalizados para os valores de **[-1,1]**.

Logo após, são entrados valores de *taxa de aprendizagem* e *epochs*. A primeira é a taxa em que a rede vai aprender, influenciando diretamente nos pesos dos neurônios. A última por sua vez, é a quantidade de iterações que irão acontecer para o treino da rede neural. Os valores *default* encontrados para os valores foram:
- **0.01** para a taxa de aprendizagem
- **10** para *epochs*

Foram testados vários valores de taxa de aprendizagem, e esse foi encaontrado como um valor bom para uma acurácia rasoável na predição. O valor de epochs não foi testado, apenas arbitrario.

Dá pra ver na imagem que a cor passada foi algo entre rosa e vermelho, mas a rede classificou como vermelho.

![image](https://user-images.githubusercontent.com/59948197/127054678-17f36047-174c-486d-a6bf-eee11a6f090f.png)

Os valores **RGB** passados claramente resultam em um tom de cinza, mas o sistema não conhece cinza, logo, tenta classificar como algo que ele conhece, que é o branco. 

## Conclusão

Foi desenvolvida uma rede perceptron simples do zero, e por mais que exista muito espaço para melhorias,tanto no código, na acurácia etc, o resultado obtido é razoável e imagino que o esperado.
