class Product():

    def __init__(self, name, price) -> None:
        """Construtor de produto"""
        self.__name = name
        self.__price = price

    def __repr__(self) -> str:
        """Representação de produto"""
        return str(self.getName()) + ': $' + str(self.getPrice())

    def getName(self) -> str:
        """Retorna o nome do produto"""
        return self.__name

    def setName(self, name) -> None:
        """Define o nome do produto"""
        self.__name = name

    def getPrice(self) -> float:
        """Retorna o preço do produto"""
        return self.__price

    def setPrice(self, price) -> None:
        """Define o preço do produto"""
        self.__price = price