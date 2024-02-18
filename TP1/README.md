# PL2024 TPC1

**Titulo** Parser em python que processa dados de um csv e apresenta algumas estatisticas

**Autor** Pedro Carneiro, a100652

Foi desenvolvido um script em python que lê o ficheiro "emd.csv" que contém dados médicos de inúmeros atletas de Braga, e apresenta os seguintes dados após processamento:
    **1**- Lista ordenada alfabeticamente das modalidades desportivas;
    **2**- Percentagens de atletas aptos e inaptos para a prática desportiva;
    **3**- Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...

**1:**
    Para este, conforme se foi percorreu o csv foram adicionados a um array o nome das modalidades caso este array ainda não contenha esse nome. Quando a leitura termina, este array é ordenado com a ordem natural das strings, e apresentado ao utilizador. 

**2:**
    Ao longo da leitura do ficheiro foi se incrementando o contador de altetas aptos e inaptos, no fim dividiu-se ambos os contadores pelo total e apresentou-se ao utilizador

**3:**
    Foi criado um array com dimensão 20 que equivale a uma idade máxima de atleta 100 anos. Ao encontrar uma idade, esta é dividida como inteiro e incrementada nessa posicao do array. No fim, para cada posição foi calculada a sua percentagem e apresentada ao utilizador.