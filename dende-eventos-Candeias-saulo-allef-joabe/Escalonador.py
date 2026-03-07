class Escalonador:

    def normalizar_min_max (self, valores):

        minimo = min(valores)
        maximo = max(valores)

        resultado =[]

        for valor in valores:
            normalizado = (valor - minimo)  /  (maximo - minimo)
            resultado.append(normalizado)

         return resultado


     def padronizar_score(self, valores):

         media = sum(valores)  / len (valores)
        

         soma = 0
         for valor in valores:
            soma += (valor - media)  ** 2
            
         variancia = soma / len(valores)
         desvio_padrao = variancia ** 0.5

         resultado = []

         for valor in valores:
            s = (valor - media) / desvio_padrao
            resultado.append (s)

         return resultado     
