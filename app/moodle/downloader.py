import os
import requests


class Downloader:

    def descargar(
        self,
        url,
        token,
        destino
    ):

        parametros = {

            "token": token

        }


        response = requests.get(

            url,

            params=parametros

        )

        response.raise_for_status()

        os.makedirs(

            os.path.dirname(destino),

            exist_ok=True

        )

        with open(
            destino,
            "wb"
        ) as archivo:


            archivo.write(
                response.content
            )

        return destino