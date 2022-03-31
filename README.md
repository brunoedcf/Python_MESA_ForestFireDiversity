# Forest-Fire-Diversity

Para executar usar "mesa runserver forest_fire"

Projeto de simulação em python usando o framework mesa para testar a hipótese de que quanto maior a diversidade de espécies em uma floresta, maior a sua resistência à incêndios.

Na interface pode-se escolher entre a opção sem diversidade (padrão) ou com diversidade (modificado), além da densidade da floresta gerada.

Tarefa 5.3: 
 
Foi implementado o reflorestamento das árvores que sobraram após o término do incêndio.
Cada árvore sobrevivente tem a possibilidade de reflorestar uma árvore queimada numa célula vizinha.
Quando uma árvore é reflorestada, a mesma também tem possibilidade de reflorestar as demais.

O objetivo é observar quantos "steps" são necessários para a "cura" total da floresta.
