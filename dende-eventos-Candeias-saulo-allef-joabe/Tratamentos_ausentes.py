class TratamentoAusentes:

 def calcular_media(self, valores):

     soma = 0
     quantidade = 0

     for valor in valores:
        if valor os not None:
            soma += valor
            quantidade += 1


     if quantidade == 0 :
        return 0

        return soma / quantidade


 def calcular_mediana (self, valores):
    
     numeros =[]

     for valor in valores:
        if valor is not None:
            numeros.append (valor)

     numeros.sort()

     tamanho = len(numeros)

     if tamanho == 0:
        return 0 

     if tamanho %2 == 0:
        return (numeros[tamanho // 2 - 1] + numeros [tamanho // 2]) / 2 
     else:
        return numeros [tamanho // 2]



 def preencher_com_media(self, coluna):

     media = self.calcular_media (coluna)
     nova_coluna = []

     for valor in coluna:
        if valor is None:
            nova_coluna.append(media)
         else:
            nova_coluna.append(valor)

     return nova_coluna



def preencher_com_mediana (self, coluna):
    
     mediana = self.calcular_mediana (coluna)

     nova_coluna = []

     for valor in coluna:
        if valor is None:
            nova_coluna.append(mediana)
         else:
            nova_coluna.append(valor)

      return nova_coluna      



 


