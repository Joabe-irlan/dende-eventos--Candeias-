class Codificador:

    def codificador_label (self, valores):

         categorias = {}
         resultado = []
         indice = 0

         for valor in valores:
             if valor not in categorias:
                categorias [valor] = indice
                indice += 1

                resultado.append (categorias[valor])

         return resultado

     def codificando_one_hot (self, valores):

         categorias = list(set(valores))
         matriz = []

         for valor in valores:
            linha = []

         for categoria in categorias:
             
             if valor == categoria:
                linha.append(1)
             else:
                linha.append(0)

         matriz.append(linha)
         return matriz       



