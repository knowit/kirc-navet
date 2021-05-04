from datetime import datetime, timezone
import uuid
import json
import requests

valid_commands = ["color", "size", "bgcolor", "italic", "bold", "normal"]
commands_with_arg = ["color", "size", "bgcolor"]


def main():
    print("Velkommen til verdens enkleste meldingsklient.")
    print("Klienten kan avsluttes når som helst ved å holde inne CTRL + C.")
    style_dict = {'bold':'false', 'italic':'false'}
    
    while True:
        print()
        print("Skriv inn meldingen du ønsker å sende til køen. For at meldingen faktisk skal bli sendt må du trykke på enter-tasten.")
        user_input = input()
        message = ""

        # NB NB NB !!!! Vi må ta hensyn til 'normal' !!!!!!!!!!!!
        
        
        command = user_input.split(" ")[0][1:]
        if command in valid_commands:
            if command in commands_with_arg:
                # Parse både command og value, feks '/color red'
                style_dict[command] = user_input.split(" ")[1]
                message = ' '.join(user_input.split(" ")[2:])
            else: 
                # Parse kun kommando, '/italic'
                if command == "normal":
                    style_dict = {'bold':'false', 'italic':'false'}
                else:
                    if style_dict[command] == 'true':
                        style_dict[command] = 'false'
                    elif style_dict[command] == 'false':
                        style_dict[command] = 'true'
                    # style_dict[command] = not bool(style_dict[command])
                    else:
                        style_dict[command] = 'true'
                
                message = ' '.join(user_input.split(" ")[1:])
           
        # Denne funker nå? burde det
        # Tror alt er riktig nå :--)
        else:
            # Vanlig melding :O
            message = user_input
        
        if not message:
            continue

        strid = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()
        print(strid)

        print(style_dict)
        
        msg = {
            "message": message, 
            "id": strid,
            "timestamp": timestamp,
            "style": style_dict
        }
        
        
        resp = requests.post('https://874k6cttr9.execute-api.eu-central-1.amazonaws.com/dev/messages', json=msg)
        print(resp.json())
    print("Melding sendt!")
        
if __name__ == '__main__':
    main()