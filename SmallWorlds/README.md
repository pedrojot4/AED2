# Small Worlds

Para cada uma das 5 redes escolhidas, fazer um gráfico bipartido
sobre a assortatividade em relação ao grau dos nós da rede. Faça
as figuras em um layout de grid. 

## YouTube
<img src="https://github.com/pedrojot4/AED2/blob/main/SmallWorlds/graficos/Youtube.png">

## Wikipedia
<img src="https://github.com/pedrojot4/AED2/blob/main/SmallWorlds/graficos/Wikipedia.png">

## Twitter
<img src="https://github.com/pedrojot4/AED2/blob/main/SmallWorlds/graficos/Twitter.png">

## Google
<img src="https://github.com/pedrojot4/AED2/blob/main/SmallWorlds/graficos/Google.png">

## Facebook
<img src="https://github.com/pedrojot4/AED2/blob/main/SmallWorlds/graficos/Facebook.png">

## Conclusão

As redes sociais desempenham um papel essencial na vida contemporânea, conectando pessoas em todo o mundo e moldando a forma como compartilham informações, se relacionam e acessam o conhecimento. Cada uma dessas redes tem sua própria estrutura e dinâmica, que podem ser interpretadas através da análise de seus gráficos. Ao comparar as redes do YouTube, Wikipedia, Twitter, Google Web Graph e Social Circles do Facebook, surgem insights interessantes sobre as diferenças e semelhanças entre essas plataformas.

Começando pelo YouTube, um dos maiores sites de compartilhamento de vídeos, seu gráfico revela algumas características distintas. A tendência decrescente é uma característica compartilhada com outras redes, indicando que a maioria dos usuários tem um número limitado de conexões. No entanto, a estrutura é mais dispersa em comparação com as redes sociais, com menos pontos à direita. Isso sugere que, embora exista uma concentração de usuários com um pequeno número de seguidores, a diferença entre os usuários menos conectados e os mais conectados é menos acentuada no YouTube. Essa estrutura reflete a diversidade de conteúdo na plataforma, onde criadores de diferentes nichos podem ganhar seguidores substanciais, tornando o YouTube mais acessível a uma variedade de usuários.

A análise da Wikipedia revela uma estrutura que compartilha a tendência decrescente com as outras redes, mas com algumas diferenças notáveis. A concentração de pontos à esquerda sugere que a maioria dos editores tem um número relativamente baixo de votos e conexões. No entanto, a presença de alguns pontos mais à direita sugere que um pequeno número de editores altamente conectados ainda existe. A natureza colaborativa e descentralizada da Wikipedia permite que muitos contribuam, mas também destaca o papel essencial de editores experientes na manutenção da qualidade do conteúdo.

A análise do Twitter revela uma estrutura que compartilha a tendência decrescente com as outras redes, mas com algumas diferenças notáveis. A concentração de pontos à esquerda é menos pronunciada, sugerindo que no Twitter um número maior de usuários possui um número significativo de seguidores. Isso pode ser atribuído à natureza mais aberta e pública do Twitter, onde figuras públicas, celebridades e influenciadores têm a oportunidade de ganhar um grande número de seguidores devido à visibilidade e ao alcance global da plataforma.

Quando se trata do Google Web Graph, que representa a interconectividade dos sites na web, o gráfico exibe uma tendência decrescente, mas com uma estrutura menos acentuada. Os pontos no gráfico estão mais distribuídos ao longo da reta, sugerindo uma variedade mais equilibrada de sites na web. A natureza descentralizada da internet permite que muitos sites individuais tenham uma quantidade significativa de links, contribuindo para uma rede mais equilibrada e diversificada.

Por fim, ao analisar a rede Social Circles do Facebook, vemos que, embora seja menor em tamanho em comparação com o Twitter, ainda é uma rede complexa. Assim como o Twitter, possui dois componentes conectados, mas o tamanho do componente gigante abrange toda a rede. O coeficiente de clustering médio é mais alto no Facebook em comparação com o Twitter, sugerindo que os usuários do Facebook tendem a formar grupos mais densos. Isso está alinhado com a natureza da plataforma, onde as conexões frequentemente representam amizades reais e relações pessoais.

Ao comparar essas redes, podemos extrair insights valiosos sobre a forma como diferentes plataformas de mídia social são estruturadas e como os usuários interagem nelas. A diversidade de estruturas reflete a natureza única de cada plataforma e as oportunidades que oferecem aos usuários. O YouTube é mais aberto a uma variedade de criadores, enquanto a Wikipedia destaca a importância de editores experientes. O Twitter é mais aberto e público, o Google Web Graph reflete a natureza descentralizada da web e o Facebook enfatiza conexões pessoais e relacionamentos. Compreender essas diferenças é fundamental para pesquisadores, administradores de comunidades e analistas de dados que desejam entender melhor o funcionamento das redes sociais e como adaptar estratégias para cada plataforma.

## Tabela Markdown
| Network | Vertices | Edges | Assortativity | Connected | Size | Clustering |
|---------|----------|-------|---------------|-----------|------|------------|
| Youtube | 1134890 | 2987624 | -0.1138 | 2 | 1134890 (1.000) | 0.0808 |
| Wikipedia | 7115 | 103689 | -0.0673 | 2 | 7066 (0.993) | 0.1409 |
| Twitter  | 81306 | 1768149 | -0.1406 | 2 | 81306 (1.000) | 0.5653 |
| Google | 875713 | 5105039 | -0.0959 | 2 | 855802 (0.977) | 0.5143 |
| Facebook | 4039 | 88234 | -0.0569 | 2 | 4039 (1.000) | 0.6055 |

A tabela fornece uma visão interessante sobre várias redes conhecidas, como YouTube, Wikipedia, Twitter, Google e Facebook, destacando várias métricas que desempenham um papel fundamental na compreensão de suas estruturas e dinâmicas. Vamos analisar cada métrica e o que ela nos diz sobre essas redes.

Vertices (Vértices): O número de vértices em uma rede representa a quantidade de elementos ou nós que a compõem. Nesse contexto, o YouTube, uma plataforma de compartilhamento de vídeos, lidera com uma enorme quantidade de vértices, ultrapassando 1 milhão. Em contraste, o Facebook, uma rede social, tem um número relativamente baixo de vértices, com pouco mais de 4.000. Essa diferença reflete a diversidade de tamanhos e finalidades das redes, com o YouTube sendo uma plataforma massiva e o Facebook voltado para conexões pessoais.

Edges (Arestas): As arestas representam as conexões entre os nós na rede. Quanto mais arestas, maior a densidade da rede. Observamos que o Google possui uma quantidade surpreendente de mais de 5 milhões de arestas. Essa alta densidade pode ser atribuída à natureza da busca na web e à enorme quantidade de links que existem na internet. Em contraste, o Facebook, embora tenha menos vértices, possui uma quantidade considerável de arestas, indicando que os usuários estão interconectados em uma rede social complexa.

Assortativity (Assortatividade): A assortatividade mede a tendência dos nós em se conectarem a outros nós com características semelhantes. Um valor negativo, como o apresentado em todas as redes da tabela, indica uma tendência à dissortatividade. Isso significa que, nessas redes, os nós tendem a se conectar a outros nós com características diferentes. Esse fenômeno é especialmente evidente em redes sociais como Facebook e Twitter, onde as pessoas se conectam com outras que podem ter interesses variados.

Connected (Conectado): A coluna "Connected" indica que todas as redes têm uma conectividade completa, com um valor de "2". Isso significa que, em cada uma dessas redes, há pelo menos um caminho que conecta qualquer par de nós. A conectividade é fundamental para o funcionamento adequado de uma rede, permitindo que informações ou interações fluam livremente.

Size (Tamanho): A métrica "Size" informa o tamanho da maior componente conectada em cada rede. Quanto mais próximo de 1, maior a parte da rede que está interconectada. O Google, com sua esmagadora quantidade de vértices e arestas, possui uma maior componente conectada que abrange quase 98% da rede, demonstrando a sua coesão e acessibilidade. Já a Wikipedia, embora tenha um número considerável de vértices, possui uma maior componente conectada que cobre 99,3% da rede, indicando que a maior parte da plataforma está interconectada.

Clustering (Aglomeramento): O coeficiente de aglomeração mede o grau de agrupamento de nós em uma rede. Quanto mais próximo de 1, maior o grau de agrupamento. O Facebook destaca-se com um coeficiente de aglomeração de 0,6055, o mais alto de todas as redes na tabela. Isso significa que, em média, os amigos de uma pessoa na rede social também são amigos entre si. Esse fenômeno reflete a formação de grupos coesos e interconectados em redes sociais.

Em resumo, a análise dessas métricas revela informações valiosas sobre as diferentes redes representadas na tabela. Cada rede possui suas próprias características distintas, refletindo a sua finalidade e a natureza das conexões entre seus nós. Essas métricas fornecem uma base para compreender a topologia e a dinâmica dessas redes, o que é fundamental em áreas como análise de redes sociais, estudos de conectividade na web e muito mais. É importante lembrar que essas métricas podem ser aplicadas em diversos contextos, permitindo uma análise mais aprofundada das redes e das interações que ocorrem dentro delas.

## Video: https://www.loom.com/share/91a00be6b75a49f0b36812a6f5bb09d0?sid=a021f2cf-8673-4310-9808-6d509409d9ed



