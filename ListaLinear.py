class Lista():

    #~~~~~~~~~~~~~~~~Checklist~~~~~~~~~~~~~~~#
    # ok -criar lista                        #
    # destruit lista                         #
    # ok -limpar lista                       #
    # inserir elemento por posicao           #
    # excluir elemento por posicao           #
    # ok -acessar elemento por posicao usada #
    # ok -alterar elemento por posicao usada #
    # combinar duas ou mais listas           #
    # classificar ou ordenar lista           #
    # copiar lista                           #
    # determinar cardinalidade da lista      #
    # acessar posicao por elemento           #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    def __init__(self, tamanho) -> None:
        """Construtor de lista"""
        self.__tamanho = tamanho
        self.__lista = [None] * self.getTamanhoTotal()
        self.__primeiro = -1
        self.__ultimo = -1
        # self.__lista = [None, None, 5, 12, 7, None, None, None, None, None]
        # self.__primeiro = 2
        # self.__ultimo = 4

    def __repr__(self) -> str:
        """Retorna a representação da lista"""
        string = '['
        if (self.getTamanhoUsado() == 0):
            return string + ']'
        else:
            return self.getRepresentacao(string) + ']'

    def getRepresentacao(self, string) -> str:
        """Retorna a representação da lista com elementos"""
        for i in range(self.__primeiro, self.__ultimo + 1):
            if (i == self.__ultimo):
                string += str(self.__lista[i])
            else:
                string += str(self.__lista[i]) + ','
        return string

    def getTamanhoUsado(self) -> int:
        """Retorna o tamanho usado da lista

        contagem iniciando em 1

        0 para não usado
        """
        if(self.getIndiceInicial() == -1 and self.getIndiceFinal() == -1):
            return 0
        elif (self.getIndiceFinal() == self.getIndiceInicial()):
            return 1
        else:
            return (self.__ultimo + 1) - self.__primeiro

    def getTamanhoTotal(self) -> int:
        """Retorna o tamanho total da lista 

        contagem iniciando em 1
        """
        return self.__tamanho

    def getIndiceInicial(self) -> int:
        """Retorna o índice inicial do espaço usado na lista

        contagem iniciando em 0
        
        -1 para não atribuído
        """
        return self.__primeiro

    def getIndiceFinal(self) -> int:
        """Retorna o índice final do espaço usado na lista

        contagem iniciando em 0

        -1 para não atribuído
        """
        return self.__ultimo

    def getIndice(self, posicao) -> int:
        """Retrona a conversão de posição de um array para o index de um array"""
        return posicao - 1

    def clearLista(self) -> None:
        """Limpa o intervalo usado e a lista"""
        self.__lista = [None] * self.getTamanhoTotal()
        self.__primeiro = -1
        self.__ultimo = -1

    def updateElementoNaPosicao(self, elemento, posicao) -> bool:
        """Atualiza um elemento na posicao"""

        #converte a posição para índice
        posicao = self.getIndice(posicao) + self.getIndiceInicial()

        #se não houver elementos na lista ou se a posição estiver fora do intervalo da lista o retorno é falso
        if (self.getTamanhoUsado() == 0 or posicao < self.getIndiceInicial() or posicao > self.getIndiceFinal()):
            return False

        self.__lista[posicao] = elemento
        return True

    def getElementoNaPosicao(self, posicao) -> int:
        """Retrona o elemento na posição informada"""

        #converte a posição para índice 
        posicao = self.getIndice(posicao) + self.getIndiceInicial()

        #se não houver elementos na lista ou se a posição estiver fora do intervalo da lista o retorno é inexistente
        if (self.getTamanhoUsado() == 0 or posicao < self.getIndiceInicial() or posicao > self.getIndiceFinal()):
            return -1

        return self.__lista[posicao]




    #funções manuais para fins de debug
    def setLista(self, lista) -> None:
        self.__lista = lista
    
    def setIndiceInicial(self, indice) -> None:
        self.__primeiro = indice

    def setIndiceFinal(self, indice) -> None:
        self.__ultimo = indice

    def getConteudo(self) -> str:
        """Retorna o conteúdo de toda a lista"""
        return self.__lista

    def getTamanhoTotalLogico(self) -> int:
        """Retorna o tamanho total da lista

        contagem iniciando em 0
        """
        return self.__tamanho - 1