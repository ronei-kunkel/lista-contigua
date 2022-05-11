from Product import Product

class List():
    #inserir posição x
    #remover posição x
    #localizar posicao de um elemento - ok
    #limpar - ok

    # def __init__(self, length) -> None:
        # """Construtor de lista"""
        # self.__length = length
        # self.__list = [None] * self.getLength()
        # self.__start = -1
        # self.__end = -1


    def __init__(self, length) -> None:
        """Construtor para testar desenvolvimento"""
        self.__length = length
        self.testProduct = Product('Lapis', 5)
        self.testProduct1 = Product('testeeee', 20)
        self.__list = [None, Product('Ronei', 1), self.testProduct, Product('Lápis', 3), self.testProduct, Product('Borracha', 5), self.testProduct1, None, None, None]
        self.__start = 0
        self.__end = 9


    def getTestProduct(self) -> object:
        """Retorna o produto de teste"""
        return self.testProduct


    def __repr__(self) -> str:
        """Retorna a representação da lista"""
        representation = ''
        if self.getUsedLength() == 0:
            return representation
        else:
            return self.getRepresentation(representation)


    def getRepresentation(self, representation) -> str:
        """Retorna a representação da lista com elementos"""
        for element in range(self.getStartIndex(), self.getEndIndex() + 1):
            if element == self.getEndIndex():
                representation += str(self.__list[element]) + '\r\n'
            else:
                representation += str(self.__list[element]) + '\r\n'
        return representation


    def getUsedLength(self) -> int:
        """Retorna o tamanho usado da lista"""
        if self.getStartIndex() == -1 and self.getEndIndex() == -1:
            return 0
        else:
            return (self.getEndIndex() + 1) - self.getStartIndex()


    def getList(self) -> object:
        """Retorna a lista"""
        return self


    def getLength(self) -> int:
        """Retorna o tamanho total da lista"""
        return self.__length


    def getStartIndex(self) -> int:
        """Retorna o índice inicial do espaço usado na lista

        -1 para não atribuído"""
        return self.__start


    def getEndIndex(self) -> int:
        """Retorna o índice final do espaço usado na lista

        -1 para não atribuído"""
        return self.__end


    def positionToIndex(self, position) -> int:
        """Converte a posição passada para o índice equivalente"""
        return self.getStartIndex() + position - 1


    def indexToPosition(self, index) -> int:
        """Converte o índice passado para a posicao equivalente relativa ao tamanho usado"""
        return self.getStartIndex() - index + 1


    def getElementByPosition(self, position) -> Product:
        """Retorna o elemento na posicao passada

        ou False caso não encontrar"""
        position = self.positionToIndex(position)
        if self.getUsedLength() == 0 or position < self.getStartIndex() or position > self.getEndIndex():
            return False
        return self.__list[position]


    def getPositionsByElement(self, element) -> any:
        """Retorna um array com as posições do elemento passado

        ou False caso não encontrar"""
        if not element in self.getList():
            return False

        positions = []
        for element in range(self.getStartIndex(), self.getEndIndex() + 1):
            if (element == self.getElementByPosition(element)):
                positions.append(element)
        return positions


    def clearList(self) -> None:
        """Limpa o intervalo usado e a lista"""
        self.__list = [None] * self.getLength()
        self.__start = -1
        self.__end = -1


    def insertElement(self, element, position = None) -> None:
        print(self.getUsedLength())
        print(self.getLength())
        exit()

        if self.getUsedLength() == self.getLength():
            return False



        if not position:
            self.insertIntoEnd(element)

        self.insertIntoPosition(element)








    # def 

    # def updateElementoNaPosicao(self, elemento, position) -> bool:
    #     """Atualiza um elemento na posicao"""

    #     #converte a posição para índice
    #     position = self.getIndice(position) + self.getStartIndex()

    #     #se não houver elementos na lista ou se a posição estiver fora do intervalo da lista o retorno é falso
    #     if (self.getUsedLength() == 0 or position < self.getStartIndex() or position > self.getEndIndex()):
    #         return False

    #     self.__list[position] = elemento
    #     return True

    # def getElementByPosition(self, position) -> int:
    #     """Retrona o elemento na posição informada"""

    #     #converte a posição para índice 
    #     position = self.getIndice(position) + self.getStartIndex()

    #     #se não houver elementos na lista ou se a posição estiver fora do intervalo da lista o retorno é inexistente
    #     if (self.getUsedLength() == 0 or position < self.getStartIndex() or position > self.getEndIndex()):
    #         return -1

    #     return self.__list[position]

