import http.client
import ssl

from app.infraestructura.mensajeria.AServicioMensajeria import AServicioMensajeria
from app.infraestructura.mensajeria.ConstantesMensajeria import ConstantesMensajeria

class ServicioMensajeria(AServicioMensajeria):

    def enviarPorMensajeria(self, numero, body):
        conn = self.configurarMensajeria.request("POST", f"/{ConstantesMensajeria.INSTANCIA}/messages/chat", self.armarURL(numero, body), self.armarHeaders())
        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))

    @staticmethod
    def configurarMensajeria():
        return http.client.HTTPSConnection(ConstantesMensajeria.HOST,context = ssl._create_unverified_context())

    @staticmethod
    def armarURL (numero, body):
        payload = f"token={ConstantesMensajeria.TOKEN}&to={numero}&body={body}"
        return payload.encode('utf8').decode('iso-8859-1')

    @staticmethod
    def armarHeaders():
        return { 'content-type': "application/x-www-form-urlencoded" }
