from datetime import datetime, timezone
import uuid
import json
import requests


def main():
    print("Velkommen til verdens enkleste meldingsklient.")
    print("Klienten kan avsluttes når som helst ved å holde inne CTRL + C.")
    while True:
        print()
        print("Skriv inn meldingen du ønsker å sende til køen. For at meldingen faktisk skal bli sendt må du trykke på enter-tasten.")
        user_input = input()
        
        split = user_input.split(" ")
        gyldige_kommandoer = ["color", "size", "bgcolor", "italic", "bold"]
        default_style = { 
            "color": "null",
            "size": "null",
            "bgcolor": "null",
            "italic": "false",
            "bold": "false"
        }
        style = default_style
        for elt in split:
            if elt[0] == "/":
                kommando = elt.split("=")[0][1:]
                if kommando == "normal":
                    style = default_style
                
                elif kommando not in gyldige_kommandoer:
                    print(kommando, " er ikke gyldig kommando")
                else:
                    style[kommando] = elt.split("=")[1]
                    
                user_input = user_input.replace(elt,"")

        print("ny style:"+ str(style))

        id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()
        msg = {
            "message": user_input,
            "id": id,
            "timestamp": timestamp,
            "style": style
            }
        resp = requests.post('https://lsn9wx5wqj.execute-api.eu-central-1.amazonaws.com/dev/messages', json=msg)
        print("Melding sendt!")

if __name__ == '__main__':
    main()


