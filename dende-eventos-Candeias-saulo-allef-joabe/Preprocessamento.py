from Tratamento_ausentes import TratamentoAusentes
from Escalonador import Escalonador
from Codificador import Codificador


class Preprocessamento:

    def __init__(self):

         self.TratamentoAusentes = TratamentoAusentes()
         self.Escalonador = Escalonador()
         self.Codificador = Codificador ()


     def remover_duplicatas (self, dados):

         linhas_unicas = set()
         novo_conjuntodedados = {coluna: [] for coluna in dados} 

         tamanho = len (next(iter(dados.values())))

         for i in range (tamanho):

             linha = tuple(dados[coluna] [i] for coluna in dados)

             if linha not in linhas_unicas:
                linhas_unicas.add(linha)

             for coluna in dados:
                novo_conjuntodedados[coluna].append(dados[coluna][i])

         return novo_conjuntodedados


     def tratar_ausentes_media(self, dados, coluna):

         dados[coluna] = self.TratamentoAusentes.preencher_com_media(dados[coluna])
         return dados

     def normalizar_colunas(self, dados, coluna):

         dados[coluna] = self.Escalonador.normalizar_min_max(dados[coluna])
         return dados

     def padronizar_coluna(self, dados, coluna):

         dados[coluna] = self.Escalonador.padronizar_coluna(dados[coluna])
         return dados

     def codificar_label (self, dados, coluna):

         dados[coluna] = self.Codificador.codificar_label(dados[coluna])
         return dados                    
