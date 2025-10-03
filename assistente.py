import speech_recognition as sr
from gtts import gTTS
import pygame
import tempfile
import os
import logging
import webbrowser
import wikipedia
import pyjokes

# Configuração de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Definir idioma principal (ajustável para "pt" ou "en")
LANGUAGE = "pt"

# Inicializa pygame mixer para tocar áudio
pygame.mixer.init()

def speak(text, lang=LANGUAGE):
    """Converte texto em fala"""
    try:
        tts = gTTS(text=text, lang=lang)

        # Cria um arquivo temporário e fecha imediatamente (para liberar no Windows)
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_audio.close()

        # Salva o áudio no arquivo temporário
        tts.save(temp_audio.name)

        # Carrega e toca o áudio
        pygame.mixer.music.load(temp_audio.name)
        pygame.mixer.music.play()

        # Espera o áudio terminar
        while pygame.mixer.music.get_busy():
            continue

        # Remove o arquivo temporário depois de tocar
        os.remove(temp_audio.name)

    except Exception as e:
        logging.error(f"Erro ao falar: {e}")

def listen(lang=LANGUAGE):
    """Escuta o microfone e retorna o texto reconhecido"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        logging.info("Ouvindo...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio, language=lang).lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        logging.error(f"Erro de requisição: {e}")
        return ""

def execute_command(command, lang=LANGUAGE):
    """Executa os comandos de voz reconhecidos"""
    if any(word in command for word in ["youtube", "abrir youtube", "open youtube"]):
        speak("Abrindo o YouTube" if lang.startswith("pt") else "Opening YouTube", lang)
        webbrowser.open("https://www.youtube.com")

    elif any(word in command for word in ["wikipedia", "pesquisar", "search"]):
        speak("O que você quer pesquisar?" if lang.startswith("pt") else "What do you want to search?", lang)
        query = listen(lang)
        if query:
            try:
                wikipedia.set_lang("pt" if lang.startswith("pt") else "en")
                summary = wikipedia.summary(query, sentences=2)
                speak(summary, lang)
            except Exception:
                speak("Não encontrei resultados" if lang.startswith("pt") else "No results found", lang)

    elif any(word in command for word in ["piada", "joke"]):
        joke = pyjokes.get_joke(language="pt" if lang.startswith("pt") else "en")
        speak(joke, lang)

    elif any(word in command for word in ["finalizar", "sair", "encerrar", "exit", "quit", "close"]):
        speak("Encerrando, até logo!" if lang.startswith("pt") else "Shutting down, goodbye!", lang)
        return False  # Sai do loop

    else:
        speak("Não entendi o comando." if lang.startswith("pt") else "I didn't understand the command.", lang)

    return True  # Continua rodando

def main(lang=LANGUAGE):
    speak("Assistente iniciado. Pode falar comigo!" if lang.startswith("pt") else "Assistant started. You can talk to me!", lang)

    running = True
    while running:
        command = listen(lang)
        if command:
            logging.info(f"Comando reconhecido: {command}")
            running = execute_command(command, lang)

if __name__ == "__main__":
    main(LANGUAGE)
