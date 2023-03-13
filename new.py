import pyttsx3


text_speech = pyttsx3.init()

def user(n):
    match(n):
        case"yes":
            return ("hai")

        case "no":
            return("lie")

        case "please":
            return("kuda-sai")

        case "thank you":
            return("ari-gato")

        case "excuse me":
            return("sumi-masen")

        case "sorry":
            return("gomen-nasai")

        case "you are welcome":
            return("doita-shima-shite")

        case "good morning":
            return("ohayo-gozaimasu")

        case "hello":
            return("koni-chi-wa")

        case "good night":
            return("oya-sumi na-sai")

        case "do you speak english":
            return("Eigo-o-hana-sema-su-ka")

        case "what is your name":
            return("o-namae-wa-nan-desreturn")

        case "my name is abc":
            return("wata-shi-no-namae wa abc desu")

        case "how are you":
            return("o-genki-desu-ka")

        case "i am fine thank you":
            return("o-kake-sa-made-gen-ki-desu")

        case "i am very glad to meet you":
            return("O-ai-dekite-tote-mo-ureshī-desu")

        case "i dont understand":
            return("wa-kari-mase-n")

        case "what did you say":
            return("nante-iima-shita-ka")

        case "i understand you":
            return("yoku-wa-kari-masen")

        case "you look beautiful":
            return("Anata-wa-utsu-kushī")

        case other:
            return ("conversion not available")
def main(n,m):
    # n = int(input("How many times u want to use this program: "))
    n = int(n)
    for i in range(n):
        # m = input("Enter the word u want to translate: ")
        ans=user(m)

        text_speech.say(ans)
        text_speech.runAndWait()
        return ans