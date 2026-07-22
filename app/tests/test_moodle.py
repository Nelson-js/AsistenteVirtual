from app.moodle.moodle_service import MoodleService


moodle = MoodleService()


resultado = moodle.obtener_contenido_curso(
    2
)


print(resultado)