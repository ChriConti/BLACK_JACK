import random
import pygame
import time

pygame.init()

clock = pygame.time.Clock()

# Funzione per creare un mazzo completo
def crea_mazzo():
    return [(valore, seme) for seme in semi for valore in valori]


# Funzione per rimescolare il mazzo
def rimescola_mazzo():
    global mazzo
    mazzo = crea_mazzo()
    random.shuffle(mazzo)
    print("Mazzo rimescolato")


# Funzione per iniziare un nuovo turno
def new_turn():
    global mano, banco, mazzo

    # Rimescolare il mazzo se è vuoto
    if len(mazzo) == 0:
        rimescola_mazzo()

    # Resettare le mani del giocatore e del banco
    mano = []
    banco = []

    # Distribuire le carte iniziali
    mano.append(pesca_carta())
    mano.append(pesca_carta())
    banco.append(pesca_carta())
    banco.append(pesca_carta())


# Funzione per pescare una carta, rimescola il mazzo se è vuoto
def pesca_carta():
    global mazzo
    if len(mazzo) == 0:
        rimescola_mazzo()
    carta = mazzo.pop(0)
    time.sleep(0.5)
    print(f"Pesca carta: {carta}")
    return carta


def carica_e_ridimensiona(path, scale_factor=0.5):
    image = pygame.image.load(path)
    size = image.get_size()
    scaled_size = (int(size[0] * scale_factor), int(size[1] * scale_factor))
    return pygame.transform.scale(image, scaled_size)


window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("BLACK JACK")

white = (255, 255, 255)
black = (0, 0, 0)

#carica sfondo
background = pygame.image.load("assets/background/tavolo_da_black_jack.png")
background = pygame.transform.scale(background, (window_width, window_height))
# Carica le immagini delle carte e ridimensionale
retro = pygame.image.load("assets/carte/retro.png")
retro = pygame.transform.scale(retro, (137, 189))

# fiori
asso_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/asso_fiori.png")
due_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/due_fiori.png")
tre_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/tre_fiori.png")
quattro_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/quattro_fiori.png")
cinque_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/cinque_fiori.png")
sei_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/sei_fiori.png")
sette_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/sette_fiori.png")
otto_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/otto_fiori.png")
nove_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/nove_fiori.png")
dieci_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/dieci_fiori.png")
fante_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/fante_fiori.png")
regina_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/regina_fiori.png")
re_fiori = carica_e_ridimensiona("assets/carte/carte_fiori/re_fiori.png")

# cuori
asso_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/asso_cuori.png")
due_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/due_cuori.png")
tre_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/tre_cuori.png")
quattro_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/quattro_cuori.png")
cinque_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/cinque_cuori.png")
sei_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/sei_cuori.png")
sette_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/sette_cuori.png")
otto_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/otto_cuori.png")
nove_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/nove_cuori.png")
dieci_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/dieci_cuori.png")
fante_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/fante_cuori.png")
regina_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/regina_cuori.png")
re_cuori = carica_e_ridimensiona("assets/carte/carte_cuori/re_cuori.png")

# quadri
asso_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/asso_quadri.png")
due_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/due_quadri.png")
tre_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/tre_quadri.png")
quattro_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/quattro_quadri.png")
cinque_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/cinque_quadri.png")
sei_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/sei_quadri.png")
sette_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/sette_quadri.png")
otto_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/otto_quadri.png")
nove_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/nove_quadri.png")
dieci_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/dieci_quadri.png")
fante_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/fante_quadri.png")
regina_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/regina_quadri.png")
re_quadri = carica_e_ridimensiona("assets/carte/carte_quadri/re_quadri.png")

# picche
asso_picche = carica_e_ridimensiona("assets/carte/carte_picche/asso_picche.png")
due_picche = carica_e_ridimensiona("assets/carte/carte_picche/due_picche.png")
tre_picche = carica_e_ridimensiona("assets/carte/carte_picche/tre_picche.png")
quattro_picche = carica_e_ridimensiona("assets/carte/carte_picche/quattro_picche.png")
cinque_picche = carica_e_ridimensiona("assets/carte/carte_picche/cinque_picche.png")
sei_picche = carica_e_ridimensiona("assets/carte/carte_picche/sei_picche.png")
sette_picche = carica_e_ridimensiona("assets/carte/carte_picche/sette_picche.png")
otto_picche = carica_e_ridimensiona("assets/carte/carte_picche/otto_picche.png")
nove_picche = carica_e_ridimensiona("assets/carte/carte_picche/nove_picche.png")
dieci_picche = carica_e_ridimensiona("assets/carte/carte_picche/dieci_picche.png")
fante_picche = carica_e_ridimensiona("assets/carte/carte_picche/fante_picche.png")
regina_picche = carica_e_ridimensiona("assets/carte/carte_picche/regina_picche.png")
re_picche = carica_e_ridimensiona("assets/carte/carte_picche/re_picche.png")


# Funzione per disegnare il gioco
def draw_game(stay):
    window.blit(background, (0, 0))
    font = pygame.font.Font(None, 36)
    font_back = pygame.font.Font(None, 38)
    pointbanco = calcola_punteggio(banco)
    pointmano = calcola_punteggio(mano)

    # Disegnare la mano del giocatore
    x_offset = 100
    for i, (valore, seme) in enumerate(mano):
        card_image = dizionario_carte[(valore, seme)]
        window.blit(card_image, (x_offset + i * 100, 400))


    player_point_text = font.render("tot: " +str(pointmano), True, white)
    player_point_text_back = font_back.render("tot: " +str(pointmano), True, black)
    window.blit(player_point_text_back, (10, 400))
    window.blit(player_point_text, (12, 402))

    # Disegnare la mano del banco
    if stay:
        for i, (valore, seme) in enumerate(banco):
            card_image = dizionario_carte[(valore, seme)]
            window.blit(card_image, (x_offset + i * 100, 50))

    else:
        if banco:
            card_image = dizionario_carte[banco[0]]
            window.blit(card_image, (x_offset, 50))

        if len(banco) > 1:
            window.blit(retro, (x_offset + 100, 50))


    dealer_point_text = font.render("tot: "+str(pointbanco), True, white)
    dealer_point_text_back = font_back.render("tot: "+str(pointbanco), True, black)
    window.blit(dealer_point_text_back, (10, 50))
    window.blit(dealer_point_text, (12, 52))

    pygame.display.flip()


semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
valori = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

mazzo = []
mano = []
banco = []

punteggio_massimo = 21

dizionario_valori = {
    'A': 11,
    'K': 10, 'Q': 10, 'J': 10,
    '10': 10, '9': 9, '8': 8, '7': 7, '6': 6,
    '5': 5, '4': 4, '3': 3, '2': 2
}

dizionario_carte = {
    ('A', 'Fiori'): asso_fiori,
    ('2', 'Fiori'): due_fiori,
    ('3', 'Fiori'): tre_fiori,
    ('4', 'Fiori'): quattro_fiori,
    ('5', 'Fiori'): cinque_fiori,
    ('6', 'Fiori'): sei_fiori,
    ('7', 'Fiori'): sette_fiori,
    ('8', 'Fiori'): otto_fiori,
    ('9', 'Fiori'): nove_fiori,
    ('10', 'Fiori'): dieci_fiori,
    ('J', 'Fiori'): fante_fiori,
    ('Q', 'Fiori'): regina_fiori,
    ('K', 'Fiori'): re_fiori,

    ('A', 'Cuori'): asso_cuori,
    ('2', 'Cuori'): due_cuori,
    ('3', 'Cuori'): tre_cuori,
    ('4', 'Cuori'): quattro_cuori,
    ('5', 'Cuori'): cinque_cuori,
    ('6', 'Cuori'): sei_cuori,
    ('7', 'Cuori'): sette_cuori,
    ('8', 'Cuori'): otto_cuori,
    ('9', 'Cuori'): nove_cuori,
    ('10', 'Cuori'): dieci_cuori,
    ('J', 'Cuori'): fante_cuori,
    ('Q', 'Cuori'): regina_cuori,
    ('K', 'Cuori'): re_cuori,

    ('A', 'Quadri'): asso_quadri,
    ('2', 'Quadri'): due_quadri,
    ('3', 'Quadri'): tre_quadri,
    ('4', 'Quadri'): quattro_quadri,
    ('5', 'Quadri'): cinque_quadri,
    ('6', 'Quadri'): sei_quadri,
    ('7', 'Quadri'): sette_quadri,
    ('8', 'Quadri'): otto_quadri,
    ('9', 'Quadri'): nove_quadri,
    ('10', 'Quadri'): dieci_quadri,
    ('J', 'Quadri'): fante_quadri,
    ('Q', 'Quadri'): regina_quadri,
    ('K', 'Quadri'): re_quadri,

    ('A', 'Picche'): asso_picche,
    ('2', 'Picche'): due_picche,
    ('3', 'Picche'): tre_picche,
    ('4', 'Picche'): quattro_picche,
    ('5', 'Picche'): cinque_picche,
    ('6', 'Picche'): sei_picche,
    ('7', 'Picche'): sette_picche,
    ('8', 'Picche'): otto_picche,
    ('9', 'Picche'): nove_picche,
    ('10', 'Picche'): dieci_picche,
    ('J', 'Picche'): fante_picche,
    ('Q', 'Picche'): regina_picche,
    ('K', 'Picche'): re_picche
}


def calcola_punteggio(mano):
    punteggio = 0
    assi = 0
    for carta in mano:
        valore, seme = carta
        if valore == 'A':
            assi += 1
            punteggio += dizionario_valori['A']
        else:
            punteggio += dizionario_valori[valore]

    while punteggio > punteggio_massimo and assi > 0:
        punteggio -= 10
        assi -= 1

    return punteggio


# Distribuzione iniziale delle carte
rimescola_mazzo()

end_game = False
while not end_game:
    new_turn()
    print("Mano del giocatore:", mano)
    print("Prima carta del banco:", banco[0])
    win = False
    gameover = False
    stay = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
                end_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    mano.append(pesca_carta())
                    print("Mano del giocatore:", mano)
                elif event.key == pygame.K_s:
                    print("Mano del banco:", banco)
                    stay = True
                    while calcola_punteggio(banco) < 17:
                        banco.append(pesca_carta())
                        print("Mano del banco:", banco)
                    if calcola_punteggio(mano) > calcola_punteggio(banco) or calcola_punteggio(
                            banco) > punteggio_massimo:
                        win = True
                        gameover = True
                    elif calcola_punteggio(mano) < calcola_punteggio(banco):
                        gameover = True
                    elif calcola_punteggio(mano) == calcola_punteggio(banco):
                        gameover = True

        if calcola_punteggio(mano) > punteggio_massimo:
            gameover = True

        draw_game(stay)

        clock.tick(3)
    if win:
        print("Congratulations! You won!")
    else:
        print("Game over. You lost.")


pygame.time.wait(3000)
pygame.quit()
