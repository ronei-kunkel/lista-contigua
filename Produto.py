class Produto():

    def __init__(self, nome, preco) -> None:
        """Construtor de produto"""
        self.__nome = nome
        self.__preco = preco

    def __repr__(self) -> str:
        """Representação de produto"""
        return str(self.getNome())

    def getNome(self) -> str:
        """Retorna o nome do produto"""
        return self.__nome

    def setNome(self, nome) -> None:
        """Define o nome do produto"""
        self.__nome = nome

    def getPreco(self) -> float:
        """Retorna o preço do produto"""
        return self.__preco

    def setPreco(self, preco) -> None:
        """Define o preço do produto"""
        self.__preco = preco