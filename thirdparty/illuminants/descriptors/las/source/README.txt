[ESTRUTURA DE DIRET�RIOS]
A biblioteca possui a seguinte estrutura de diret�rios:

./app                --> ir� conter as fun��es principais do descritor
./bin                --> execut�veis do descritor
./include            --> cabe�alhos das fun��es (.h)
./lib                --> arquivo lib gerado ap�s a compila��o
./obj                --> objetos gerados ap�s a compila��o
./src                --> arquivos com fun��es de manipula��o de imagens, fun��es internas do descritor, etc

----------------------------------------------
Para implementar o seu descritor, use como exemplo o descritor GCH (Global Color Histogram) que vem junto com a biblioteca.
----------------------------------------------
[IMPLEMENTA��O]
- Criar um programa respons�vel pela extra��o de caracter�sticas (ex: gch_extraction.c) [dentro de 'app']
    - Entrada: imagem a ser processada (caminho no sistema de arquivos)
    - Sa�da: arquivo com as caracter�sticas extra�das (caminho no sistema de arquivos)

- Criar um programa respons�vel pelo c�lculo de dist�ncia (ex: gch_distance.c) [dentro de 'app']
    - Entradas: arquivo de caracter�sticas da imagem 1 e arquivo de caracter�sticas da imagem 2 (caminhos no sistema de arquivos)
    - Sa�da: dist�ncia entre as duas imagens (pode ser impressa na tela / use tipo 'double' para a dist�ncia)

- Se forem criadas fun��es auxiliares, voc� deve coloc�-las no diret�rio 'src' dentro de um arquivo com o nome do descritor (ex: gch.c). Neste caso voc� pode precisar de um arquivo de cabe�alhos (ex: gch.h). Coloque-o no diret�rio 'include' e adicione uma linha no arquivo 'libcolordescriptors.h' correspondendo ao seu arquivo de cabe�alhos (ex: #include "gch.h").

- Alterar o arquivo Makefile da raiz da biblioteca da seguinte maneira:
    - Abaixo da linha 26, cujo conte�do � "$(OBJ)/gch.o", adicione uma linha correspondente ao seu descritor. [n�o esquecer das '\' como separadores de linhas]
    - Abaixo da linha 44, cujo conte�do � "$(OBJ)/gch.o", adicione uma linha correspondente ao seu descritor. [n�o esquecer das '\' como separadores de linhas]
    - Copie as linhas 106-108, cujo conte�do �
        $(OBJ)/gch.o: $(SRC)/gch.c
            gcc $(FLAGS) -c $(SRC)/gch.c -I$(INCLUDE) \
            -o $(OBJ)/gch.o
    e cole-as logo abaixo trocando os valores "gch" para o nome do seu descritor (s�o 4 locais para trocar).

- Compilar o programa:
    - Entre no diret�rio 'app'
    - Digite 'make prog', sendo 'prog' o nome do arquivo '.c' que voc� deseja compilar (sem a extens�o '.c')
    - O execut�vel � gerado no diret�rio 'bin'


IMPORTANTE:
- Lembre-se sempre de liberar toda a mem�ria usada pelo seu descritor.
- Tente deixar sua implementa��o bastante r�pida, pois o tempo de execu��o do descritor ser� medido.


[Obs.: Uma outra alternativa para voc� implementar seu descritor, � usar apenas 1 arquivo '.c'. Neste caso, voc� deve colocar no '.c' todas as fun��es e estruturas que o descritor usa. Desta forma, voc� n�o vai precisar do Makefile da raiz nem da estrutura de diret�rios da biblioteca. Basta colocar tudo no arquivo '.c' e compilar diretamente com o gcc. As instru��es de compila��o do link abaixo tamb�m explicam como compilar o arquivo '.c' na hora de gerar o plugin]
[FIM IMPLEMENTACAO]
----------------------------------------------

Antes de gerar o plugin teste bem o seu descritor.
Lembre-se que voc� s� deve cadastrar o seu descritor na ferramenta quando tudo estiver bem testado. O cadastro do descritor na ferramenta apenas finaliza o seu processo de implementa��o, portanto, ele n�o � nenhum processo que visa ajudar voc� a melhorar a sua implementa��o. Quando cadastrado, sup�e-se que nada mais precise ser alterado na implementa��o.

----------------------------------------------
[GERA��O DO PLUGIN]
- Dentro de 'app', criar um arquivo que ir� conter ambas as fun��es de extra��o e dist�ncia do seu descritor (ex: gch_plugin.c). O cabe�alho e o funcionamento das fun��es deve respeitar as instru��es encontradas em:
    http://www.lis.ic.unicamp.br/~otavio/tests/ferramenta/cadastra_descritor.php

- N�o use 'make' para compilar. Siga as instru��es de compila��o do link acima.

- Assim que voc� der o upload do plugin, a ferramenta ir� verificar se a sua implementa��o possui as fun��es necess�rias e se elas est�o de acordo com as instru��es especificadas. A ferramenta tamb�m ir� testar a fun��o de extra��o de caracter�sticas e a fun��o de dist�ncia usando duas imagens de exemplo. Se o teste for bem sucedido, voc� dever� preencher alguns campos com informa��es sobre o descritor na p�gina seguinte. A sigla do descritor ser� atribu�da automaticamente a partir do nome do plugin enviado, portanto, use um nome sem acentos ou espa�os. Os outros campos s�o: Nome do descritor, Autor (coloque os nomes dos autores do artigo no qual voc� se baseou) e Tipo.

== OBS: Se a ferramenta apresentar a mensagem de erro "Poss�vel erro de compila��o" � prov�vel que voc� tenha compilado em 32 bits. A ferramenta s� ir� aceitar compila��o em 64 bits.
[FIM PLUGIN]

----------------------------------------------
[IMAGENS PPM]
Na hora de testar seu descritor voc� precisar� de imagens PPM, que s�o arquivos de imagens sem compacta��o. Caso voc� n�o tenha imagens deste tipo, use o programa 'convert' do Linux para conveter seus arquivos JPEG em PPM. Exemplo:
convert imagem.jpg imagem.ppm

----------------------------------------------
[ESTRUTURAS E FUN��ES DA BIBLIOTECA]

Abaixo est�o detalhes de algumas estruturas de dados fornecidas pela ferramenta. Use-as na sua implementa��o:

typedef struct _image {
  int *val;
  int ncols,nrows;
  int *tbrow;
} Image;

Esta estrutura representa uma imagem em n�veis de cinza, ou seja, cada pixel tem apenas um valor referente ao brilho.


typedef struct cimage {
  Image *C[3];
} CImage;

Esta estrutura representa uma imagem colorida (RGB). Como se pode ver, ela � composta de 3 imagens em n�veis de cinza, cada uma correspondendo a um dos canais R, G e B.

Observando estas estruturas, � poss�vel perceber que, apesar de uma imagem ser bidimensional (largura 'ncols' e altura 'nrows') n�o existe uma matriz na qual voc� pode acessar as posi��es x e y independentemente. Nestas estruturas as imagens s�o consideradas como matrizes linearizadas. Ou seja, � como se cada linha da imagem fosse concatenada ao final de outra linha, resultando num vetor. Se uma imagem tem, por exemplo, ncols=20 e nrows=50, a representa��o dela nesta estrutura ser� um vetor de nrows*ncols posi��es. A primeira linha da imagem (linha superior) ficar� nas posi��es 0 a 19, a segunda linha ficar� nas posi��es 20 a 39, e assim por diante.
No entanto, a estrutura possui um facilitador na hora de acessar os valores dos pixels da imagem. O vetor tbrow � usado para acessar uma linha da imagem de maneira eficiente. Ele possui nrows posi��es e cada posi��o i dele tem um valor referente a quantidade de pixels que existem na estrutura antes do in�cio da linha i. Por exemplo, se a imagem tem ncols=20 e nrows=50, o vetor tbrow na posi��o 3 ter� o seguinte valor: tbrow[3]=20+20+20=60. Quando voc� usa as fun��es de cria��o e leitura de imagens da biblioteca CreateImage, CreateCImage, ReadImage ou ReadCImage, os valores de tbrow j� v�em preenchidos, portanto voc� n�o precisa mexer neles.
Caso voc� precise acessar uma posi��o espec�fica (x,y) da imagem, basta fazer como o exemplo abaixo:

    valor_red = img->C[0]->val[y+img->C[0]->tbrow[x]];

onde img � a imagem, C[0] indica os valores do canal R (red), y � a coluna e x � a linha

Se voc� precisar de um la�o que percorre a imagem toda voc� pode usar uma das duas op��es abaixo:
1)
    for (i = 0; i < img->C[0]->nrows; i++) {
        for (j = 0; j < img->C[0]->ncols; j++) {
            r = img->C[0]->val[j+img->C[0]->tbrow[i]];
            g = img->C[1]->val[j+img->C[1]->tbrow[i]];
            b = img->C[2]->val[j+img->C[2]->tbrow[i]];
        }
    }

2)
    for (i = 0; i < n; i++) {   //n = nrows*ncols
        r = img->C[0]->val[i];
        g = img->C[1]->val[i];
        b = img->C[2]->val[i];
    }



Fun��es �teis:

CImage *CreateCImage(int ncols, int nrows)          //cria uma imagem colorida
CImage *ReadCImage(char *filename)                  //le uma imagem colorida
void    WriteCImage(CImage *cimg, char *filename)   //grava uma imagem colorida no disco
CImage *CImageRGBtoHSV(CImage *cimg)                //converte imagem RGB para HSV
void    DestroyCImage(CImage **cimg)                //libera a mem�ria de uma imagem colorida








