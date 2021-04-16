from empresa_dao import EmpresaDAO
from empresa import Empresa
from empresa_duplicada_exception import EmpresaDuplicadaException


class ControladorSistemaEmpresas:
    def __init__(self):
        self.__empresa_dao = EmpresaDAO()

    def inclui_empresa(self, empresa: Empresa):
        try:
            self.__empresa_dao.get(empresa.cnpj)
        except KeyError:
            self.__empresa_dao.add(empresa)
        else:
            raise EmpresaDuplicadaException

    def exclui_empresa(self, empresa: Empresa):
        self.__empresa_dao.remove(empresa)

    def busca_empresa_pelo_cnpj(self, cnpj: int) -> Empresa:
        try:
            return self.__empresa_dao.get(cnpj)
        except KeyError:
            return None

    @property
    def empresas(self) -> list:
        return self.__empresa_dao.get_all()

    def calcula_total_impostos(self) -> float:
        total_impostos = 0
        for empresa in self.empresas:
            total_impostos += empresa.total_impostos()
        return total_impostos
