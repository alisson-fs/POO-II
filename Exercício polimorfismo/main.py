from catalogo import Catalogo
from transporte_aereo import TransporteAereo
from transporte_terrestre import TransporteTerrestre
from transporte_aquatico import TransporteAquatico


catalogo = Catalogo()

aviao = TransporteAereo('Boeing 747', 8, 76, 95, 900, 9260, 77)
carro = TransporteTerrestre('Fusca 1300', 1.5, 4, 0.38, 110.5, 'Boxer de 4 cilindros', 'Aro 15 Modelo Original')
barco = TransporteAquatico('Titanic', 53, 269, 3, 39, 28, 10.5)

catalogo.insercao(aviao)
catalogo.insercao(carro)
catalogo.insercao(barco)

catalogo.apresentacao()
