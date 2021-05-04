from datetime import datetime, timezone
import uuid
import json
import requests

class style:
    def __init__(self) :
        self.color = "Black"
        self.size = "12px"
        self.bgcolor = "White"
        self.italic = False
        self.bold = False


    def setDefault(self) :
        self.color = "Black"
        self.size = "12px"
        self.bgcolor = "White"
        self.italic = False
        self.bold = False

    def setStyle(self, color, size, bgcolor, italic, bold):
        self.color = color
        self.size = bgcolor + "px"
        self.italic = italic
        self.bold = bold

    def setColor(self, color):
        self.color = color

    def setSize(self, size):
        self.size = size

    def setBgcolor(self, bgcolor):
        self.bgcolor = bgcolor

    def changeBold(self):
        self.bold = not self.bold

    def changeItalic(self):
        self.italic = not self.italic

    # ---- Mulig at vi ikke trenger ----
    # def pyToJSON(self):
    #     json.dumps({"/color": self.color, "/size": self.size, "/bgcolor": self.bgcolor})

def check_commando(commando, value): #endret til set-/change-metoder
    global styleObject
    if (commando.lower() == "color"):
        styleObject.setColor(value)
        
    elif (commando.lower() == "size"):
        styleObject.setSize(value)

    elif (commando.lower() == "bgcolor"):
        styleObject.setBgcolor(value)
        
    elif (commando.lower() == "italic"):
        styleObject.changeItalic()

    elif (commando.lower() == "bold"):
        styleObject.changeBold()
    else:
        print("Feil på kommandonavnet") #Kanskje litt dårlig tekst :)

styleObject = style()

def main():
    print("Velkommen til verdens enkleste meldingsklient.")
    print("Klienten kan avsluttes når som helst ved å holde inne CTRL + C.")
    
    validCommando = {"color", "bgcolor", "italic", "bold", "size"}
    style = {}

    while True:
        print()
        print("Skriv inn meldingen du ønsker å sende til køen. For at meldingen faktisk skal bli sendt må du trykke på enter-tasten.")
        user_input = input()
        #color:"#fffff"
        #color White
        #color #ffffff
        if user_input.startswith("/"):
            bits = user_input[1:].split(":")
            commando = bits[0]

            if commando is "normal":
                styleObject.setDefault()
                continue
            
            value = None
            if len(bits) == 2:
                value = bits[1]

            if commando in validCommando:
                check_commando(commando, value)
                continue
        else:
            id = str(uuid.uuid4())
            timestamp = datetime.now(timezone.utc).astimezone().isoformat()
            msg = {
                "message": user_input, 
                "id": id, 
                "timestamp": timestamp,
                "style": json.dumps(styleObject.__dict__, indent = 4) 
                }
            resp = requests.post('https://9jg82y3ww7.execute-api.eu-central-1.amazonaws.com/dev/messages', json=msg)
            print(msg)
            print("Melding sendt!")
        
if __name__ == '__main__':
    main()

