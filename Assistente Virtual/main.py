# Projeto Assistente Virtual
# Passo 1 reconhecer a fala
# Bibliotecas Necessarias ( SpeechRocognition,PyAudio)
# Passo 2 Realizar açôes pelo comando de voz

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit

audio = sr.Recognizer() #reconhecer o Audio
maquina = pyttsx3.init()

def executa_comando():
    try:
    # Utilizar o With para o microfone 'desliga' sozinho e diminuir o codigo
        with sr.Microphone() as source:
            print("Pode falar My master")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            if 'tina' in comando: # utilizar um nome para pode realizar os comandos
                comando = comando.replacer("tina","") #remover o nome
                maquina.say(comando)
                maquina.runAndWait()

    except:
        print("Não funcionou o Microphone")

    return (comando)

def comando_voz_usuario():
    comando = executa_comando()
    if "horas" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        maquina.say("Agora são" + hora)
        maquina.runAndWait()
    elif "buscar" in comando:
        procurar = comando.replace("buscar", "")
        wikipedia.set_lang("pt")
        resultado = wikipedia.summary(procurar,2)
        maquina.say(resultado)
        maquina.runAndWait()
# Acessar o Youtube
    elif "toque" in comando:
        musica = comando.replace("toque","")
        resultado = pywhatkit.playonyt(musica)
        print(comando)
        maquina.say("tocando musica")
        maquina.runAndWait()
#Pesquisar no google
    elif "pesquisar" in comando:
        Google = comando.replace("pesquisar","")
        resultado = pywhatkit.search(Google)
        print(comando)
        maquina.say("Abrir Google")
        maquina.runAndWait()


comando_voz_usuario()










