from gtts import gTTS
import vlc
import inquirer
import time

LANGUAGES_OPTIONS = [
    ("Português", "pt"),
    ("Francês", "fr"),
    ("Espanhol", "es"),
    ("Inglês", "en"),
    ("Italiano", "it"),
    ("Japonês", "ja"),
]

def choose_language(choices):
    perguntas = [inquirer.List(
        'language', message="Escolha um idioma que você gostaria que seu audio fosse criado", choices=choices)]
    resposta = inquirer.prompt(perguntas)
    return resposta['language']


class Help:
    def __init__(self, language) -> None:
        self.phrase = []
        self.audio_count = 0
        self.language = language
        self.audio_path = f"audio_{self.audio_count}.mp3"

    def ask_for_chars(self):
        chars = input(
            "Agora, precisamos que você digite o que você deseje que nosso programa fale (aperte ENTER para confirmar): \n")

        self.phrase.append(" " + chars)

        self.ask_to_keep()

        if (self.keep):
            self.ask_for_chars()

    def create_phrase(self):
        self.ask_for_chars()
        audio_path = self._generate_audio()
        print(f"Audio gerado com sucesso em: {audio_path}")

        if (self.ask_to_play_audio()):
            self.play_audio(audio_path)

        if (self.ask_to_another()):
            self.create_phrase()

    def _generate_audio(self):
        final_phrase = ""
        for phrase in self.phrase:
            final_phrase += phrase
        self.audio = gTTS(
            text=final_phrase, lang=self.language)
        audio_path = self.audio_path
        self.audio.save(audio_path)
        self.audio_count += 1
        self.audio_path = f"audio_{self.audio_count}.mp3"
        self.phrase = []

        return audio_path

    def ask_to_keep(self):
        perguntas = [inquirer.List(
            'keep', message="Deseja adicionar mais alguma coisa?", choices=[("Sim", True), ("Não", False)])]
        resposta = inquirer.prompt(perguntas)
        self.keep = resposta['keep']

    def ask_to_another(self):
        perguntas = [inquirer.List(
            'another', message="Deseja gerar outro audio?", choices=[("Sim", True), ("Não", False)])]
        resposta = inquirer.prompt(perguntas)
        return resposta['another']
    
    def ask_to_play_audio(self):
        perguntas = [inquirer.List(
            'play', message="Deseja tocar o audio gerado?", choices=[("Sim", True), ("Não", False)])]
        resposta = inquirer.prompt(perguntas)
        return resposta['play']
    
    def play_audio(self, audio_path):
         vlc_instance = vlc.Instance()
         player = vlc_instance.media_player_new()
         media = vlc_instance.media_new(audio_path)
         player.set_media(media)
         player.play()
         time.sleep(1.5)
         duration = player.get_length() / 1000
         time.sleep(duration)


def main():
    print("Seja bem vindo ao HELP! Aqui conseguimos transformar o seu texto em fala!")
    print("Primeiro de tudo precisamos definir algumas coisas: \n")
    
    language = choose_language(LANGUAGES_OPTIONS)

    audio_generator = Help(language)

    audio_generator.create_phrase()

    print("Obrigado por usar nossa ferramenta! 😄")


if __name__ == "__main__":
    main()
