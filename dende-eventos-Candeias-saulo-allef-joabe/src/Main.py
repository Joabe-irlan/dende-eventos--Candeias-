from Preprocessamento import Preprocessamento

def mostrar_dados(dados):
     # vai mostrar os dados de forma organizada

     colunas = list(dados.keys())
     tamanhos = len(dados[colunas [0]])

     print (" | ". join(colunas))
           #separador -> usado para organizar os dados

     for i in range (tamanho):
        linha = []

     for coluna in colunas:
        linha.append(str(dados[coluna] [i]))

     print (" | ".join(linha))
        #usado para separar as linhas


 def Main():

     print ()    #=======================================
     print ()    #usado para corrigir e preparar os dados
     print ()    #=======================================

     dados = {
         "artista": ["Artista A", "Artista B", "Artista C", "Artista B"],
         "popularidade": [80, 65, 90, None],
         "dancabilidade": [0.75, 0.60, 0.83, 0.60]
     }

     print ("Conjunto de dados original:\n")
     mostrar_dados(dados)
     preprocessador = Preprocessamento()

     print() #para remover duplicatas
     dados = preprocessador.remover_duplicatas(dados)

     mostrar_dados(dados)

     print() #tratar os valores ausentes
     dados = preprocessador.tratar_ausentes_media(dados, "popularidade")
     
     mostrar_dados(dados)

     print() #normalizar os dados
     dados = preprocessador.normalizar_colunas(dados, "popularidade")
     
     mostrar_dados(dados)

     print() #codifica as categorias
     dados = preprocessador.codificar_label(dados, "artista")

     mostrar_dados(dados)

     print() #final do processo

 if __name__ == "__main__":
    main()    