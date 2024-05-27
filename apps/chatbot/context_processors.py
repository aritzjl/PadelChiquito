# en context_processors.py

def global_variables(request):
    botActivo = False
    return {'bot': botActivo}
