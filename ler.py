from gtts import gTTS as g
from playsound import playsound as p
from os import remove, system
from random import choice



saudacao = ['olá, pega um café pra mim e deixa eu te contar um pouco sobre meu criador!',
 'Sabia que eu fui criada por um programador python? Deixa eu te contar mais!', 
 'Oi, vou te contar como fui criada. Pega um café ai pra nós dois',
'Quer ouvir um resumo de como eu fui criada? ']
despedida = ['gostou? então dá um like... brincadeira', 'e aí? eu fiquei uma bot legal?', 'Gostou? então me mostra pras outras pessoas que gostam de tecnologia.',
 'meu programador é esforçado. Tem alguma vaga pra ele aí?', 'ajuda meu programador, quem sabe o novo bot tem seu nome']

system('clear')
audio = 'audio.mp3'
lingua = 'pt'
autor = 'autor.mp3'
finaliza = 'final.mp3'

# SE APRESENTANDO
def liza():
    print('\n')
    meutexto = g(choice(saudacao), lang=lingua )
    meutexto.save(audio)
    p(audio)

# LENDO SOBRE O CRIADOR
def ptexto():
    with open('leiame.txt', 'r') as arquivo:
        print(arquivo.read())

# FALANDO SOBRE O CRIADOR
def leitura():
    with open('leiame.txt', 'r') as arquivo:
        leia = g(arquivo.read(), lang=lingua)
        leia.save(autor)
        p(autor)

# FALA FINAL ANTES DE IR EMBORA
def final():
    fim = g(choice(despedida), lang=lingua, slow=False)
    fim.save(finaliza)
    p(finaliza)

# LENDO APRESENTAÇÃO
print('Oi, eu sou a L1Z4...')
print('Meu criador: Marcio Maia')
print('*'*25)
# CHAMANDO APRESENTAÇÃO
liza()
ptexto()
leitura() 
final()
remove(finaliza)
remove(audio)
remove(autor)
