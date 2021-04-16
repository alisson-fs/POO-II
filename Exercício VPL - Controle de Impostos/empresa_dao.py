import pickle
from empresa import Empresa


class EmpresaDAO:
    def __init__(self,
                 datasource='empresa.pkl'):
        self.__datasource = datasource
        self.__object_cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        a = open(self.__datasource, 'wb')
        pickle.dump(self.__object_cache, a)
        a.close()

    def __load(self):
        a = open(self.__datasource, 'rb')
        self.__object_cache = pickle.load(a)
        a.close()

    def add(self, empresa: Empresa):
        if isinstance(empresa, Empresa):
            self.__object_cache[empresa.cnpj] = empresa
            self.__dump()
        else:
            raise TypeError

    def remove(self, empresa: Empresa):
        self.__object_cache.pop(empresa.cnpj)
        self.__dump()

    def get(self, cnpj: int):
        return self.__object_cache[cnpj]

    def get_all(self):
        empresas = []
        for empresa in self.__object_cache.values():
            empresas.append(empresa)
        return empresas
