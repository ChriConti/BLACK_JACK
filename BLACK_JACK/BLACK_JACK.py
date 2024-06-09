import random
import pygame

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("BLACK JACK")

white = (255, 255, 255)
black = (0, 0, 0)


def draw_game():
    window.fill(white)
    font = pygame.font.Font(None, 36)
    pointbanco =calcola_punteggio(banco)
    pointmano = calcola_punteggio(mano)
    # Render player hand
    player_hand_text = " Player: " + ", ".join([f"{v} di {s}" for v, s in mano])
    player_text = font.render(player_hand_text, True, black)
    player_point_text = font.render(str(pointmano), True, black)
    window.blit(player_text, (50, 50))
    window.blit(player_point_text, (20, 50))

    # Render dealer hand
    dealer_hand_text = " Dealer: " + ", ".join([f"{v} di {s}" for v, s in banco])
    dealer_text = font.render(dealer_hand_text, True, black)
    dealer_point_text = font.render(str(pointbanco), True, black)
    window.blit(dealer_text, (50, 150))
    window.blit(dealer_point_text, (20, 150))

    pygame.display.flip()


semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
valori = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

mazzo = []
mano = []
banco = []

punteggio_massimo = 21

for seme in semi:
    for valore in valori:
        mazzo.append((valore, seme))

dizionario = {
    'A': 11,
    'K': 10, 'Q': 10, 'J': 10,
    '10': 10, '9': 9, '8': 8, '7': 7, '6': 6,
    '5': 5, '4': 4, '3': 3, '2': 2
}


def calcola_punteggio(mano):
    punteggio = 0
    assi = 0
    for carta in mano:
        valore, seme = carta
        if valore == 'A':
            assi += 1
            punteggio += dizionario['A']
        else:
            punteggio += dizionario[valore]

    while punteggio > punteggio_massimo and assi > 0:
        punteggio -= 10
        assi -= 1

    return punteggio


random.shuffle(mazzo)

# Distribuzione iniziale delle carte
mano.append(mazzo.pop(0))
banco.append(mazzo.pop(0))
mano.append(mazzo.pop(0))
banco.append(mazzo.pop(0))

print("Mano del giocatore:", mano)
print("Prima carta del banco:", banco[0])

win = False
gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                mano.append(mazzo.pop(0))
                print("Mano del giocatore:", mano)
            elif event.key == pygame.K_s:
                print("Mano del banco:", banco)
                while calcola_punteggio(banco) < 17:
                    banco.append(mazzo.pop(0))
                    print("Mano del banco:", banco)
                if calcola_punteggio(mano) > calcola_punteggio(banco) or calcola_punteggio(banco) > punteggio_massimo:
                    win = True
                    gameover = True
                elif calcola_punteggio(mano) < calcola_punteggio(banco):
                    gameover = True

    if calcola_punteggio(mano) > punteggio_massimo:
        gameover = True

    draw_game()

pygame.time.wait(10000)
pygame.quit()

if win:
    print("Congratulations! You won!")
else:
    print("Game over. You lost.")
