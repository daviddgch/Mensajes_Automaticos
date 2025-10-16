from abc import abstractmethod


class AServicioMensajeria:

    @abstractmethod
    def enviarPorMensajeria (self, numero, body):
        pass
