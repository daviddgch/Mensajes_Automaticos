from abc import abstractmethod


@abstractmethod
class ATareasAutomaticas():


    def iniciarTareasAutomaticas(self):
        pass

    def pararTareasAutomaticas(self):
        pass

    def agregarTareaAutomaticas(self):
        pass

    def estaCorriendo(self):
        pass