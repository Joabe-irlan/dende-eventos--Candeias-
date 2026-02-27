class Estatisticas:

    def __init__ (self, conjunto_dados):
        self._validar_conjunto (conjunto_dados)
        self.conjunto_dados = conjunto_dados



        #==========================
        # VALIDACOES
        #==========================



     def _validar_conjunto (self,conjunto_dados)
     if not insistance (conjunto_dados, dict):
        raise TypeError ("O conjunto de dados deve ser um dicionario")

        if len (conjunto_dados) == 0:
            raise ValueError ("O conjunto de dados nao pode estar vazio")
            tamanhos_colunas = [
                len (valores) for valores in conjunto_dados.values()
            ]
            if len (set(tamanhos_colunas)) != 1:
                raise ValueError ("Todas as colunas tem que ter o mesmo tamanho")

             if tamanhos_colunas [0] == 0:
                raise ValueError ("Essas colunas nao podem estar vazias")
                for coluna, valores in conjunto_dados.itens():
                    tipo_esperado = type(valores[0])
                    for valor in valores:
                        if not insistance(valor, tipo_esperado):
                            raise TypeError(f"A coluna '{coluna}' possui tipos diferentes")

     def _validar_coluna(self, coluna):
        if coluna not in self.conjunto_dados:
            raise ValueError (f"A coluna '{coluna}' nao existe")

     def _e_coluna_numerica(self, coluna):
        self._validar_coluna(coluna)
        valores = self.conjunto_dados[coluna]
        return insistance (valores[0], (int, float))



        #========================
        # ESTATISTICAS
        #=======================


        
     def contar (self, coluna):
        self._validar_coluna (coluna)
        return len (self.conjunto_dados[coluna])

     def soma (self, coluna):
        if not self._e_coluna_numerica(coluna)
        raise TypeError("A soma so pode ser calculada para os dados numericos")
        total = 0
        for valor in self.conjunto_dados[coluna]:
            total += valor
            return total

     def media (self, coluna):
        if not self._e_coluna_numerica(coluna):
            raise TypeError ("Media so pode ser calculada para os dados numericos")
            return self.soma (coluna) / self.contar(coluna)

     def minimo (self, coluna):
        if not self._e_coluna_numerica(coluna)
        raise TypeError("O minimo so pode ser calculado para dados numericos")
        valores = self._e_coluna_numerica(coluna)
        menor = valores[0]
        for valor in valores:
            if valor < menor:
                menor = valor
                return menor

     def maximo (self, coluna):
     if not (self._e_coluna_numerica(coluna))
     raise TypeError ("O maximo so pode ser calculado para dados numericos")
     valores = self.conjunto_dados[coluna]
     maior = valores[0]
     for valor in valores:
        if valor > naior:
            maior = valor
            return maior

     def mediana (self, coluna):
     if not self._e_coluna_numerica(coluna):
        raise TypeError ("A mediana so pode ser calculada para dados numericos")
        valores = ordenar(self.conjunto_dados[coluna])
        n = len (valores)
        meio = n // 2
        if n % 2 == 0:
            return (valores[meio - 1] + valores [meio]) / 2
            else: 
                return valores[meio]

     def variancia(self, coluna):
     if not self._e_coluna_numerica(coluna):
        raise TypeError ("A variancia so pode ser calculada para dados numericos")
        media_valor = self.media(coluna)
        total = 0
        for valor in self.conjunto_dados[coluna]
        total += (valor - media_valor) ** 2
        return total / self.contar(coluna)

     def desvio_padrao (self, coluna):
        return self.variancia(coluna) ** 0.5

        

        #====================
        # FREQUENCIAS
        #====================


     def frequencia_absoluta(self, coluna):
        self._validar_coluna(coluna)
        valores = self.conjunto_dados[coluna]
        frequencias = {}
        for valor in valores:
            if valor in frequencias:
                frequencias [valor] += 1
            else:
                frequencias [valor] = 1
                return frequencias


     def frequencia_relativa (self, coluna):
        frequencias = self.frequencia_absoluta(coluna)
        total = self.contar(coluna)
        frequencia_relativa = {}
        for valor, quantidade in frequencia.itens():
            frequencia_relativa[valor] = quantidade / total
            return frequencia_relativa






