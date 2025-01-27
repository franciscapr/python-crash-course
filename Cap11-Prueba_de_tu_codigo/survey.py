class AnonymousSurvey:
    """Recoge respuestas anònimas a una pruegunta de encuesta."""

    def __init__(self, question):
        """Almacena una pregunta y se prepara para almacenar respuestas."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Muestra la pregunta de la encuesta."""
        print(self.question)

    def store_response(self, new_response):
        """Almacena una respuesta a la encuesta."""
        self.responses.append(new_response)

    def show_results(self):
        """Muestra todas las respuestas que se han dado."""
        print("Resultados de la encuesta.")
        for response in self.responses:
            print(f"- {response}")