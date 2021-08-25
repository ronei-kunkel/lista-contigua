from Produto import Produto

class Lista():
    #inserir posição x
    #remover posição x
    #localizar posicao de um elemento - ok
    #limpar - ok

    def __init__(self, tamanho) -> None:
        """Construtor de lista"""
        self.__tamanho = tamanho
        # self.__lista = [None] * tamanho
        # self.__primeiro = -1
        # self.__ultimo = -1
        self.teste = Produto('Lapis', 5)
        self.__lista = [self.teste, Produto('Ronei', 1), self.teste, Produto('Lápis', 3), self.teste, Produto('Borracha', 5), None, None, None, None]
        self.__primeiro = 0
        self.__ultimo = 5

    def __repr__(self) -> str:
        """Retorna a representação da lista"""
        string = '['
        if (self.getTamanhoUsado() == 0):
            return string + ']'
        else:
            return self.getRepresentacao(string) + ']'

    def getRepresentacao(self, string) -> str:
        """Retorna a representação da lista com elementos"""
        for i in range(self.getIndiceInicial(), self.getIndiceFinal() + 1):
            if (i == self.getIndiceFinal()):
                string += str(self.__lista[i])
            else:
                string += str(self.__lista[i]) + ', '
        return string

    def getTamanhoUsado(self) -> int:
        """Retorna o tamanho usado da lista"""
        if(self.getIndiceInicial() == -1 and self.getIndiceFinal() == -1):
            return 0
        else:
            return (self.getIndiceFinal() + 1) - self.getIndiceInicial()

    def getLista(self) -> list:
        """Retorna a lista"""
        return self.__lista

    def getTamanhoTotal(self) -> int:
        """Retorna o tamanho total da lista"""
        return self.__tamanho

    def getIndiceInicial(self) -> int:
        """Retorna o índice inicial do espaço usado na lista

        -1 para não atribuído"""
        return self.__primeiro

    def getIndiceFinal(self) -> int:
        """Retorna o índice final do espaço usado na lista

        -1 para não atribuído"""
        return self.__ultimo

    def increasePosicao(self, posicao) -> int:
        """Converte a posição passada para o índice equivalente"""
        return self.getIndiceInicial() + posicao - 1
    
    def reduceIndice(self, indice) -> int:
        """Converte o índice passado para a posicao equivalente relativa ao tamanho usado"""
        return self.getIndiceInicial() - indice + 1

    def getElementoNaPosicao(self, posicao) -> Produto:
        """Retorna o elemento na posicao passada

        ou False caso não encontrar"""
        posicao = self.increasePosicao(posicao)
        if (self.getTamanhoUsado() == 0 or posicao < self.getIndiceInicial() or posicao > self.getIndiceFinal()):
            return False
        return self.__lista[posicao]

    def getPosicoesDoElemento(self, elemento) -> any:
        """Retorna um array com as posições do elemento passado

        ou False caso não encontrar"""
        if not elemento in self.getLista():
            return False

        posicoes = []
        for i in range(self.getIndiceInicial(), self.getIndiceFinal() + 1):
            if (elemento == self.getElementoNaPosicao(i)):
                posicoes.append(i)
        return posicoes

    def clearLista(self) -> None:
        """Limpa o intervalo usado e a lista"""
        self.__lista = [None] * self.getTamanhoTotal()
        self.__primeiro = -1
        self.__ultimo = -1

    # def updateElementoNaPosicao(self, elemento, posicao) -> bool:
    #     """Atualiza um elemento na posicao"""

    #     #converte a posição para índice
    #     posicao = self.getIndice(posicao) + self.getIndiceInicial()

    #     #se não houver elementos na lista ou se a posição estiver fora do intervalo da lista o retorno é falso
    #     if (self.getTamanhoUsado() == 0 or posicao < self.getIndiceInicial() or posicao > self.getIndiceFinal()):
    #         return False

    #     self.__lista[posicao] = elemento
    #     return True

    # def getElementoNaPosicao(self, posicao) -> int:
    #     """Retrona o elemento na posição informada"""

    #     #converte a posição para índice 
    #     posicao = self.getIndice(posicao) + self.getIndiceInicial()

    #     #se não houver elementos na lista ou se a posição estiver fora do intervalo da lista o retorno é inexistente
    #     if (self.getTamanhoUsado() == 0 or posicao < self.getIndiceInicial() or posicao > self.getIndiceFinal()):
    #         return -1

    #     return self.__lista[posicao]


    # def setElementoNaPosicao(self, elemento,  posicao) -> None:
    #     """Insere um elemento em uma determinada posição remanejando a menor parte da lista"""
        
    #     pass