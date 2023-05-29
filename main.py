import random
import PySimpleGUI as sg

def gerar_frase_harry_potter():
    # Lista de frases inspiradas em Harry Potter em inglês
    frases_ingles = [
        "“It does not do to dwell on dreams and forget to live.” - Albus Dumbledore",
        "“Happiness can be found, even in the darkest of times, if one only remembers to turn on the light.” - Albus Dumbledore",
        "“It is our choices, Harry, that show what we truly are, far more than our abilities.” - Albus Dumbledore",
        "“We’ve all got both light and dark inside us. What matters is the part we choose to act on.” - Sirius Black",
        "“Words are, in my not-so-humble opinion, our most inexhaustible source of magic.” - Albus Dumbledore",
        "“The ones that love us never really leave us.” - Sirius Black",
        "“You are protected, in short, by your ability to love!” - Albus Dumbledore",
        "“Differences of habit and language are nothing at all if our aims are identical and our hearts are open.” - Albus Dumbledore",
        "“We do not need magic to transform our world. We carry all the power we need inside ourselves already.” - J.K. Rowling",
        "“To the well-organized mind, death is but the next great adventure.” - Albus Dumbledore",
        "“It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.” - Albus Dumbledore",
        "“We must all face the choice between what is right and what is easy.” - Albus Dumbledore",
        "“Dark and difficult times lie ahead. Soon we must all face the choice between what is right and what is easy.” - Albus Dumbledore",
        "“We are only as strong as we are united, as weak as we are divided.” - Albus Dumbledore",
        "“It matters not what someone is born, but what they grow to be.” - Albus Dumbledore",
        "“Fear of a name increases fear of the thing itself.” - Albus Dumbledore",
        "“Do not pity the dead, Harry. Pity the living, and, above all, those who live without love.” - Albus Dumbledore",
        "“The mind is not a book, to be opened at will and examined at leisure.” - Severus Snape",
        "“Numbing the pain for a while will make it worse when you finally feel it.” - Albus Dumbledore",
        "“After all, to the well-organized mind, death is but the next great adventure.” - Albus Dumbledore"
    ]

    # Lista de frases inspiradas em Harry Potter em português
    frases_portugues = [
        "“Não adianta ficar sonhando e esquecer de viver.” - Albus Dumbledore",
        "“A felicidade pode ser encontrada mesmo nas horas mais sombrias, se você se lembrar de acender a luz.” - Albus Dumbledore",
        "“São as nossas escolhas, Harry, que mostram quem realmente somos, muito mais do que as nossas habilidades.” - Albus Dumbledore",
        "“Todos nós temos luz e trevas dentro de nós. O que importa é o lado o qual escolhemos agir.” - Sirius Black",
        "“As palavras são, na minha opinião, a nossa mais inesgotável fonte de magia.” - Albus Dumbledore",
        "“Aqueles que nos amam nunca nos deixam de verdade.” - Sirius Black",
        "“Você está protegido, em resumo, pela sua capacidade de amar!” - Albus Dumbledore",
        "“Diferenças de hábitos e línguas não significam nada se nossos objetivos forem os mesmos e nossos corações estiverem abertos.” - Albus Dumbledore",
        "“Não precisamos de magia para transformar nosso mundo. Já carregamos todo o poder necessário dentro de nós mesmos.” - J.K. Rowling",
        "“Para uma mente bem estruturada, a morte é apenas a próxima grande aventura.” - Albus Dumbledore",
        "“É preciso coragem para enfrentar nossos inimigos, mas é preciso ainda mais coragem para enfrentar nossos amigos.” - Albus Dumbledore",
        "“Todos nós devemos enfrentar a escolha entre o que é certo e o que é fácil.” - Albus Dumbledore",
        "“Tempos sombrios e difíceis estão por vir. Em breve, teremos que escolher entre o que é certo e o que é fácil.” - Albus Dumbledore",
        "“Só somos fortes quando estamos unidos, tão fracos quanto estamos divididos.” - Albus Dumbledore",
        "“O que realmente importa não é o que uma pessoa nasce, mas o que ela se torna.” - Albus Dumbledore",
        "“O medo de um nome só aumenta o medo da coisa em si.” - Albus Dumbledore",
        "“Não tenha pena dos mortos, Harry. Tenha pena dos vivos, e, acima de tudo, daqueles que vivem sem amor.” - Albus Dumbledore",
        "“A mente não é um livro para ser aberto quando quisermos, mas um organismo vivo que se desenvolve e responde às circunstâncias.” - Severus Snape",
        "“Entorpecer a dor por um tempo só vai fazer com que ela seja pior quando finalmente a sentirmos.” - Albus Dumbledore",
        "“Afinal, para uma mente bem estruturada, a morte é apenas a próxima grande aventura.” - Albus Dumbledore"
    ]

    # Solicitar o nome do usuário
    nome = sg.popup_get_text("Digite o seu nome:")

    # Gerar um índice aleatório para selecionar a frase
    indice = random.randint(0, len(frases_ingles) - 1)

    # Obter a frase em inglês e em português
    frase_ingles = frases_ingles[indice]
    frase_portugues = frases_portugues[indice]

    # Exibir a mensagem em uma janela pop-up
    layout = [
        [sg.Text(f"Oii, Bruxa(o) {nome}!")],
        [sg.Text(f"Vamos ver o que a bola de cristal vê para {nome}:")],

        [sg.Button("OK")]
    ]

    window = sg.Window("Mensagem de Harry Potter", layout)
    event, _ = window.read()
    window.close()

    # Imagem
    image_path = "harry_potter.png"

    # Exibir a imagem em uma janela pop-up
    layout_imagem = [
        [sg.Image(image_path)],
        [sg.Button("OK")]
    ]
    window_imagem = sg.Window("Imagem de Harry Potter", layout_imagem)
    event, _ = window_imagem.read()
    window_imagem.close()

    layout = [

        [sg.Text(f"Essa frase foi sorteada para você {nome}:")],
        [sg.Text(frase_ingles)],
        [sg.Text(frase_portugues)],
        [sg.Button("OK")]
    ]

    window = sg.Window("Mensagem de Harry Potter", layout)
    event, _ = window.read()
    window.close()




# Chamada da função para gerar a frase inspirada em Harry Potter
gerar_frase_harry_potter()
