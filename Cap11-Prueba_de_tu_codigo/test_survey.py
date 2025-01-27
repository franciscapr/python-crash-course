from survey import AnonymousSurvey

def test_store_single_response():
    """Prueba que una respuesta ùnica se almacena correctamente."""
    question = "¿Què idioma aprendiste primerp a hablar?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('ingles')
    assert 'ingles' in language_survey.responses

def test_store_three_responses():
    """Prueba que tres respuestas individuales se almacenen correctamente."""
    question = "¿Què idioma aprendiste primero a hablar"
    language_survey = AnonymousSurvey(question)
    responses = ['ingles', 'español', 'latino']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses