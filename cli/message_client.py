from datetime import datetime, timezone
import uuid
import json
import requests
import re

#Hint: legg til en kommando som printer ut configen.

def init_attributes():
    return { "color" : "#000000",
             "size" : 12,
             "bgcolor" : "#FFFFFF",
             "italic" : False,
             "bold" : False }

def is_valid_color(color: str) -> bool: 
    # Enkel validering som ikke tar høyde for alt
    valid_colors = ["black", "white", "gray", "silver", "maroon", "red", "purple", "fushsia",
                    "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua"]
    return bool(re.search(r"#[0-9a-f]{6}$", color.lower())) or color in valid_colors

def parse_commands(user_input, attributes):
    if not user_input.startswith("/"):
        return user_input

    commands = user_input.split(" ")
    
    for i, command in enumerate(commands):
        print(command)
        if "=" in command:
            cmd, arg = command.split("=")
        else:
            cmd = command
            arg = ""
        
        if cmd is "/color":
            if not is_valid_color(arg):
                raise RuntimeError(f"Ugyldig fargeverdi: {arg}")
            attributes['color'] = arg
        elif cmd is "/size":
            try:
                attributes["size"] = int(arg)
            except:
                raise RuntimeError(f"Ugydlig tekststørrelse: {arg}")
        elif cmd is "/bgcolor":
            if not is_valid_color(arg):
                raise RuntimeError(f"Ugyldig fargeverdi: {arg}")
            attributes['bgcolor'] = arg
        elif cmd is "/italic":
            attributes["italic"] = not attributes["italic"]
        elif cmd is "/bold":
            attributes["bold"] = not attributes["bold"]
        elif cmd is "/normal":
            attributes = init_attributes()
        else:
            text = " ".join(commands[i+1:])
            break

    return text

def main():
    attributes = init_attributes()

    print("Velkommen til verdens enkleste meldingsklient.")
    print("Klienten kan avsluttes når som helst ved å holde inne CTRL + C.")
    while True:
        print()
        print("Skriv inn meldingen du ønsker å sende til køen. For at meldingen faktisk skal bli sendt må du trykke på enter-tasten.")
        user_input = input()
        id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).astimezone().isoformat()

        try:
            message_text = parse_commands(user_input, attributes)
        except RuntimeError as e:
            print(e.message())
            continue
            
        msg = {
            "message": message_text, 
            "id": id, 
            "timestamp": timestamp,
            "style": attributes, 
            }
        resp = requests.post('https://dedkmpx7d2.execute-api.eu-central-1.amazonaws.com/dev/messages', json=msg)
        print("Melding sendt!")
        
if __name__ == '__main__':
    main()