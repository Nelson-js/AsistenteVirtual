import requests

from app.core.config import (
    MOODLE_URL,
    MOODLE_TOKEN
)


class MoodleService:


    def llamar(self, funcion, parametros=None):

        if parametros is None:
            parametros = {}

        data = {

            "wstoken": MOODLE_TOKEN,
            "wsfunction": funcion,
            "moodlewsrestformat": "json"

        }

        data.update(parametros)


        url = MOODLE_URL + "/webservice/rest/server.php"


        response = requests.post(
            url,
            data=data
        )


        print("================================")
        print("URL:", url)
        print("STATUS:", response.status_code)
        print("CONTENT-TYPE:", response.headers.get("content-type"))
        print("RESPUESTA MOODLE:")
        print(response.text[:1000])
        print("================================")


        return response.json()



    def obtener_contenido_curso(self, curso_id):

        return self.llamar(

            "core_course_get_contents",

            {
                "courseid": curso_id
            }

        )