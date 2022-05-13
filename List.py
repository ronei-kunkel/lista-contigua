from Product import Product

class List():
    """Responsável pela manipulação de uma lista contígua"""


    def __init__(self, length) -> None:
        """Construtor de lista"""
        self.__length = length
        self.__list = [None] * length
        self.__start = -1
        self.__end = -1


    def __repr__(self) -> str:
        """Retorna a representação da lista"""
        representation = '['
        if self.getUsedLength() == 0:
            return representation + ']'
        else:
            return self.getRepresentation(representation)


    def getRepresentation(self, representation: str) -> str:
        """Retorna a representação da lista com elementos"""
        for index in range(self.getPointerIndex('start'), self.getPointerIndex('end') + 1):
            if index == self.getPointerIndex('end'):
                representation += str(self.__list[index]) + ']'
            else:
                representation += str(self.__list[index]) + ','

        return representation


    def resetList(self) -> None:
        """Reinicia os ponteiros e a lista"""
        self.__list = [None] * self.getLength()
        self.__start = -1
        self.__end = -1


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


    def reducePointerIndex(self, pointer: str = 'end', units: int = 1) -> None:
        if pointer == 'end':
            self.__end = self.getPointerIndex('end') - units
        if pointer == 'start':
            self.__start = self.getPointerIndex('start') - units


    def getUsedLength(self) -> int:
        """Retorna o tamanho usado da lista"""
        if self.getPointerIndex('start') == -1 and self.getPointerIndex('end') == -1:
            return 0
        else:
            return (self.getPointerIndex('end') + 1) - self.getPointerIndex('start')


    def getList(self) -> object:
        """Retorna a lista"""
        return self.__list


    # def setList(self, list: list) -> None:
    #     """define a lista"""
    #     self.__list = list


    def getLength(self) -> int:
        """Retorna o tamanho total da lista"""
        return self.__length


    def positionToIndex(self, position: int) -> int:
        """Converte a posição numérica para o índice"""
        return position - 1


    def indexToPosition(self, index: int) -> int:
        """Converte o índice para a posição numérica"""
        return index + 1


    def getElementByPosition(self, position: int) -> object:
        """Retorna o elemento na posição passada \r\n
        ou None caso não encontrar \r\n
        ou False caso fora do intervalo da lista"""
        index = self.positionToIndex(position)
        if self.getUsedLength() == 0 or index < 0 or self.getLength() <= index:
            return False

        return self.__list[index]


    def getPositionsOfElement(self, element: object) -> list:
        """Retorna um array com as posições do elemento passado \r\n
        ou False caso não encontrar"""
        positions = []
        if not element in self.getList():
            return positions

        for element in range(self.getPointerIndex('start'), self.getPointerIndex('end') + 1):
            if (element == self.getElementByPosition(element)):
                positions.append(element)

        return positions


    def insertElement(self, element: object, position: any = None) -> bool:
        """Insere um elemento na lista"""
        if self.getUsedLength() == self.getLength():
            return False

        if position:
            index = self.positionToIndex(position)
            if index < 0 or self.getLength() <= index:
                return False

            self.__insertInto(element, index)

            return True
        self.__insertInto(element)

        return True


    def __insertInto(self, element: object, index: int = None) -> None:
        """Remaneja os elementos da lista para adicionar outro elemento na posição informada \r\n
        ou no final da lista por padrão caso não seja informada a posição"""
        if not index:
            if not self.haveEmptyPositionAfterEnd():
                self.moveElements('up', self.getPointerIndex('start'), self.getPointerIndex('end'))

            return self.insertIntoEnd(element)

        # index = self.positionToIndex(position)


    def setElementInPosition(self, element: object, position: int) -> None:
        self.__list[position] = element

        return True


    def haveEmptyPositionAfterEnd(self) -> bool:
        end = self.getPointerIndex('end')
        positionOfEnd = self.indexToPosition(end)

        return self.getElementByPosition(positionOfEnd)


    def insertIntoEnd(self, element: object) -> None:
        if self.getPointerIndex('end') == self.getLength():
            return False

        self.increasePointerIndex('end')

        return self.setElementInPosition(element, self.getPointerIndex('end'))


    def moveElements(self, direction: str, initialIndex: int, finalIndex: int) -> None:
        """Move recursivamente os elementos da lista que estão entre a posição inicial e a final informadas"""
        if direction == 'up':
            if initialIndex > finalIndex:
                return

            # pego meu elemento atual
            position = self.indexToPosition(initialIndex)
            currentElement = self.getElementByPosition(position)
            
            # insiro ele no indice superior

            # somo dois ao meu initialIndex


            



        if direction == 'down':
            pass
















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
