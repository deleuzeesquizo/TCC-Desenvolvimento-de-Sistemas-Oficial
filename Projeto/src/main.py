
"""

acredito eu q o comando de voz vai aq, qlq coisa so me corrigir dps.

"""
import requests
import pyttsx3
import speech_recognition as sr

# Função para fazer uma pesquisa na web via SerpAPI
def pesquisa_web(query):
    api_key = '1a29a1f354f88b5316934486fa71fcbf8edffec55803fe542cf3428dcf63760e'  # Substitua pela sua chave da API
    url = 'https://serpapi.com/search'
    
    params = {
        'q': query,
        'api_key': api_key
    }

    try:
        resposta = requests.get(url, params=params)
        dados = resposta.json()

        # Verificar se a resposta foi bem-sucedida
        if resposta.status_code == 200 and dados.get('organic_results'):
            # Extrair o resumo ou descrição do primeiro resultado encontrado
            resultado = dados['organic_results'][0]
            if 'snippet' in resultado:
                return resultado['snippet']  # Retorna o resumo (snippet)
            else:
                return "Desculpe, não consegui encontrar uma resposta precisa."
        else:
            return "Desculpe, não consegui encontrar resultados para sua pesquisa."
    except Exception as e:
        return f'Ocorreu um erro: {e}'

# Função que usa a pesquisa na web para responder a uma pergunta
def obter_resposta(texto):
    if 'previsão do tempo' in texto.lower():
        return pesquisa_web('previsão do tempo São Paulo')  # Pesquisa sobre o clima em São Paulo
    elif 'hora' in texto.lower():
        return 'Desculpe, não consigo acessar a hora em tempo real.'
    else:
        return pesquisa_web(texto)  # Faz pesquisa para outras perguntas

# Função para falar a resposta
def falar(resposta):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Velocidade da fala
    engine.setProperty('volume', 1)  # Volume de 0 a 1
    engine.say(resposta)
    engine.runAndWait()

# Função para ouvir o usuário
def ouvir():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Desculpe, não entendi.")
            return ""
        except sr.RequestError:
            print("Erro ao se comunicar com o serviço de reconhecimento de voz.")
            return ""

# Loop principal
while True:
    print("Por favor, faça uma pergunta:")
    pergunta = ouvir()
    if pergunta:
        resposta = obter_resposta(pergunta)
        print(f"Resposta: {resposta}")
        falar(resposta)
    else:
        falar("Não consegui entender sua pergunta.")
