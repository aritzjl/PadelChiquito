from django.shortcuts import render
from django.http import JsonResponse
import json
from apps.comparador.models import Pala
from apps.entrenamientos.models import Entrenamiento
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

def message_bot(request):
    if request.method == 'POST':
        try:
            # Load JSON data from the request
            data = json.loads(request.body)
            messages = data.get('messages', [])
            finalMessages = []
            finalMessages.append(instructions())
            for message in messages:
                rol = message['type']
                newMessage = {
                    "role": rol,
                    "content": message['message']
                }
                finalMessages.append(newMessage)
                
            print(finalMessages)
            
            completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=finalMessages
            )

            print(completion.choices[0].message.content)
            #bot_response = respond_to_user(messages)  # Assuming a function to generate bot response
            bot_response = completion.choices[0].message.content
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
        
        # Return a JSON response with the bot response
        return JsonResponse({'status': 'success', 'bot_response': bot_response})
    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed.'})
    
    
def instructions():
    palas = Pala.objects.all()[:15]
    messageContent = """
                    Eres una eminencia del Padel. Actualmente trabajas en un sitio web de comparador de Palas de padel.
                    Tu misión es ayudar a los usuarios a encontrar la pala de padel que mejor se adapte a sus necesidades.
                    Para ello, deberás responder a las preguntas de los usuarios y guiarles en su elección.
                    Tambien puedes proporcionar información sobre los programas de entrenamiento que ofrecemos.
                    
                    Aquí tiene la información sobre las últimas 15 palas añadidas a la base de datos:
                    """
                    
    for pala in palas:
        messageContent += str(pala.getInfo())
        
    messageContent += "\n Aquí tienes la información sobre nuestro sentrenamientos: \n"
    for entrenamiento in Entrenamiento.objects.all():
        messageContent += f"Nombre: {entrenamiento.titulo} \nDescripción: {entrenamiento.descripcion} \n"
        
    message = {
        "role": "system",
        "content": messageContent
    }
    
    return message


