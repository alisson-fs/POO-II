class CategoriaProduto:
    def __init__(self, titulo: str):
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
        