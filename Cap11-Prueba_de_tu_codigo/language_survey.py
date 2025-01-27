from survey import AnonymousSurvey

question = "¿Que idioma aprendista a hablar primero?"
language_survey = AnonymousSurvey(question)

language_survey.show_question()
print("Escribe 'q' en cualquier momento para salir.\n")
while True:
    response = input("Idioma: ")
    if response == 'q':
        break
    language_survey.store_response(response)

print("\n¡Gracias a todos los que participaren en la encuesta!")
language_survey.show_results()