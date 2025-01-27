from survey import AnonymousSurvey
import pytest

@pytest.fixture
def language_survey():
    """Una encuesta que estarà disponible para todas las funciones de prueba."""
    question = "¿Què idioma aprendiste primero a hablar?"
    language_survey = AnonymousSurvey(question)
    return language_survey



def test_store_single_response(language_survey):
    """Prueba que una respuesta ùnica se almacena correctamente."""
    language_survey.store_response('ingles')
    assert 'ingles' in language_survey.responses

def test_store_three_responses(language_survey):
    """Prueba que tres respuestas individuales se almacenen correctamente."""
    responses = ['ingles', 'español', 'latino']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses