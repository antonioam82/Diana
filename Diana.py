import subprocess
import time
from conversaciones import despedidas
import pickle
speak=wc.Dispatch("Sapi.SpVoice")
#CHAT-BOT
#a=input("Escribe algo: ")
program=pickle.load(open("apps","rb"))

def yyes(t):
    while t!="yes" and t!="y" and t!="no" and t!="n":
        speak.Speak("Write just yes, y, no or n according to your ellection: ")
        t=input("Write just \'yes\', \'y\', \'no\' or \'n\' according to your ellection: ")
    return t

def titulo():
    print("AAM's")
    print(" _______    ____   _______   _      __   _______ ")
    print("|   __  \  |    | /   _   \ |  \   |  | /   _   \ ")
    print("|  |  \  \ |    ||   |_|   ||   \  |  ||   |_|   |")
    print("|  |   \  \|    ||    _    ||    \ |  ||    _    |")
    print("|  |   /  /|    ||   / \   ||     \|  ||   / \   |")
    print("|  |__/  / |    ||  |   |  ||  |\     ||  |   |  |")
    print("|_______/  |____||__|   |__||__| \____||__|   |__|")
    print("--------------------------------------------------")
    print("--------------------------------------------------")

titulo()
time.sleep(1)
momento=time.localtime()
if momento[3]>=12 and momento[3]<22:
    print("GOOD AFTERNOON");speak.Speak("good afternoon")
elif momento[3]>=1 and momento[3]<12:
    print("GOOD MORNING");speak.Speak("good morning")
elif momento[3]>=22 and momento[3]<=23:
    print("GOOD NIGHT");speak.Speak("good night")
    

print("do you want to play a game or use an application?")
speak.Speak("do you want to play a game or use an application?")
texto=yyes(input().lower())
subprocess.call(["cmd.exe","/C","cls"])
while True:
    titulo()
    if texto=="yes" or texto=="y":
        print("which one?");speak.Speak("which one?")
        texto=input()
        #while texto!="PPTLSgame" and texto!="adivina numero" and texto!="pickle_creator" and texto!="ejal":
        while not texto in program:
            print("WHAT?")
            speak.Speak("what?")
            texto=input()
        if texto=="PPTLSgame":
            import PPTLSgame
        elif texto=="adivina numero":
            import desafio
        elif texto=="pickle_creator":
            import pickle_creator
        elif texto=="ejal":
            import ejal
        elif texto=="timer":
            import timer
        print("do you want to play another game or application?");speak.Speak("do you want to play another game or application?")
        texto=yyes(input().lower())
        if texto=="yes" or texto=="y":
            subprocess.call(["cmd.exe","/C","cls"])
            continue
        else:
            break
    if texto=="no" or texto=="n":
        break
    else:
        print("WHAT?");speak.Speak("what?")
        texto=input()
        continue
   
print("OK");speak.Speak("OK")
despedida=random.choice(despedidas)
speak.Speak(despedida)
    

