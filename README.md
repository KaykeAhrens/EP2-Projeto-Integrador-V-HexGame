# EP2-Projeto-Integrador-V-HexGame

# Engine de Games com Minimax

Você deverá fazer uma engine de games de IA que possa jogar de forma inteligente contra um humano. Deverá ter uma interface simples de exibição e entrada dos dados.

Deverá usar os conceitos do curso como espaço de estados, ações, funções de utilidade, função sucessora e heurísticas.

Lembre-se que um agente é mais do que um algoritmo, logo, deve-se pensar em heurísticas de primeira jogada e outras para que se reduza o espaço de busca.

Pode-se e deve-ser usar pesquisa da internet (referenciar as fontes) para a construção do seu agente.

### Modelagem - Montar uma apresentação e vídeo

- Introdução ao trabalho e explicação do game
- Espaço de estados: Como é modelado um estado com as posições?
    - Teoria do Minimax com PodaAlfabeta aplicando para o game
    - Próximos movimentos
    - Quando é um estado final?
    - Como vai se serializar o espaço de estados para criar novos?
- Como se calcula a função de utilidade?
    - Para este tipo de problema, a função utilidade não é possível ser -1, 0, 1 pela complexidade do jogo. Pede-se para que se pense um cálculo numérico com as peças e configurações
- Quais heurísticas podemos usar para primeira jogada ou final de jogo
- Referências: de onde tirou as informações?
    - Sites
    - Livros ou Revistas
    - Códigos-fonte

### Código fonte e código executado - Exibição do código e detalhamento

Deverá ser entregue o repositório no Github. 

**Não será permitido** de uso de bibliotecas de software de Inteligência Artificial, usar apenas a biblioteca padrão da linguagem.

O que será avaliado:

- Apresentação do tabuleiro, interação com o usuário
- Minimax, função de utilidade, Poda Alfa Beta
    - Qual a profundidade de Minimax ideal para o problema?
- Heurísticas para reduzir jogadas e escolha da primeira jogada

O que não será avaliado

- Componentes gráficos. Não me importa se vai ser gráfico 3D ou imprimir no terminal. (Sugestão: imprimir no terminal é trivial)
- Interação com o usuário: não se esperar nenhuma interface homem-máquina sofisticada. Se o usuário digitar qual o seu movimento usando o UCI algébrico, é o suficiente.
