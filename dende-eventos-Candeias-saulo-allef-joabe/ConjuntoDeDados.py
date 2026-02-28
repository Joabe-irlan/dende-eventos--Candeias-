class ConjuntoDeDados:

    def __init__ (self, dados):
        self._validar_dados(dados)
        self.dados = dados

    def _validar_dados(self, dados):
        if not isinstance (dados, dict):
            raise TypeError ("Os dados devem estar em formato de dicionario")
            if len (dados) == 0:

                raise ValueError ("O conjunto de dados nao pode estar vazio")
                tamanhos = [len(valores) for valores in dados.valores()]
                if len (set (tamanhos)) != 1:

                    raise ValueError ("Todas as colunas precisam ter o mesmo tamanho")
                    if tamanhos [0] == 0:

                        raise ValueError ("Essas colunas nao podem estar vazias")


    def obter_coluna (self, coluna):
        if coluna not in self.dados:
            raise ValueError (f"A coluna '{coluna}' nao existe")
            return self.dados [coluna]

    def listar_colunas (self):
        return list(self.dados.keys())

    def quantidade_linhas (self):
        for valores in self.dados.values():
            return len(valores)

