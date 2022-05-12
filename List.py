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


    def __init__(self, length: int) -> None:
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


    def getRepresentation(self, representation:str) -> str:
        """Retorna a representação da lista com elementos"""
        for element in range(self.getPointerIndex('start'), self.getPointerIndex('end') + 1):
            if element == self.getPointerIndex('end'):
                representation += str(self.__list[element]) + '\r\n'
            else:
                representation += str(self.__list[element]) + '\r\n'
        return representation


    def getPointerIndex(self, pointer: str) -> int:
        if pointer == 'end':
            return self.__end
        if pointer == 'start':
            return self.__start


    def increasePointerIndex(self, pointer: str = 'end', units: int = 1) -> None:
        if pointer == 'end':
            self.__end = self.getPointerIndex('end') + units
        if pointer == 'start':
            self.__start = self.getPointerIndex('start') + units


    def getUsedLength(self) -> int:
        """Retorna o tamanho usado da lista"""
        if self.getPointerIndex('start') == -1 and self.getPointerIndex('end') == -1:
            return 0
        else:
            return (self.getPointerIndex('end') + 1) - self.getPointerIndex('start')


    def getList(self) -> object:
        """Retorna a lista"""
        return self


    def getLength(self) -> int:
        """Retorna o tamanho total da lista"""
        return self.__length


    def positionToIndex(self, position: int) -> int:
        """Converte a posição numérica para o índice"""
        return self.getPointerIndex('start') + position - 1


    def indexToPosition(self, index: int) -> int:
        """Converte o índice para a posição numérica"""
        return self.getPointerIndex('start') - index + 1


    def getElementByPosition(self, position: int) -> Product:
        """Retorna o elemento na posição passada

        ou False caso não encontrar"""
        position = self.positionToIndex(position)
        if self.getUsedLength() == 0 or position < self.getPointerIndex('start') or position > self.getPointerIndex('end'):
            return False
        return self.__list[position]


    def getPositionsByElement(self, element: object) -> any:
        """Retorna um array com as posições do elemento passado

        ou False caso não encontrar"""
        if not element in self.getList():
            return False

        positions = []
        for element in range(self.getPointerIndex('start'), self.getPointerIndex('end') + 1):
            if (element == self.getElementByPosition(element)):
                positions.append(element)
        return positions


    def resetList(self) -> None:
        """Reinicia os ponteiros e a lista"""
        self.__list = [None] * self.getLength()
        self.__start = -1
        self.__end = -1






    def insertElement(self, element: object, position: any = None) -> None:
        """Insere um elemento na lista"""
        if self.getUsedLength() == self.getLength():
            return False

        if not position:
            self.insertIntoEnd(element)

        self.insertIntoPosition(element, position)


    def insertIntoEnd(element: object) -> bool:
        """Insere o elemento no final da lista"""
        



    def insertIntoPosition(element: object, position: int) -> bool:
        """Insere o elemento em uma posição determinada"""






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
