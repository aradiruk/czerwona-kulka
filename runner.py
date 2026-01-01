import pygame
import random
import math

# --- USTAWIENIA OKNA ---
SZEROKOSC = 800   # szerokość okna gry pikselach
WYSOKOSC = 400    # wysokość okna gry pikselach
FPS = 60          # liczba klatek na sekundę (szybkość gry)

# --- KOLORY W FORMACIE RGB ---
BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
CZERWONY = (200, 0, 0)


def rysuj_kulke(ekran, x, y, faza):
    """
    Rysuje czerwoną kulkę - naszą postać.
    x, y - środek kulki
    faza - która część animacji (0 lub 1)
    """

    promien = 30  # wielkość kulki (promień)

    # RYSOWANIE KULKI (postać gracza)
    pygame.draw.circle(ekran, CZERWONY, (x, y), promien)

    # RYSOWANIE OKA
    oko_x = x + 8   # oko trochę na prawo
    oko_y = y - 6   # i trochę do góry
    pygame.draw.circle(ekran, CZARNY, (oko_x, oko_y), 4)

    # RYSOWANIE UŚMIECHU
    # pygame.draw.arc(RYSUJEMY_TU, KOLOR, [X, Y, SZER, WYS], KAT_START, KAT_STOP, GRUBOSC)

    if faza == 0:
        # uśmiech animacja — trochę inny kształt
        pygame.draw.arc(ekran, CZARNY, (x+6, y - 5, 25, 25), 3.14, 3.14 * 1.5, 2)
    else:
        pygame.draw.arc(ekran, CZARNY, (x+6, y - 5, 25, 20), 3.14, 3.14 * 1.5, 2)


def main():
    pygame.init()  # uruchomienie pygame
    ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))  # tworzymy okno gry
    pygame.display.set_caption("Czerwona Kulka - Dino Style")  # nazwa okna
    zegar = pygame.time.Clock()  # zegar do kontrolowania FPS

    czcionka = pygame.font.SysFont("Arial", 24)  # ustawienie czcionki

    # PARAMETRY KULKI (gracza)
    kulka_x = 100  # stała pozycja w poziomie
    podloga_y = WYSOKOSC - 50  # wysokość podłogi
    kulka_y = podloga_y - 10  # aktualna wysokość kulki
    predkosc_y = 0  # prędkość pionowa
    grawitacja = 1  # siła opadania
    w_powietrzu = False  # czy kulka skacze?

    # PROSTOKAT KULKI - używany do kolizji
    kulka_szer = 60
    kulka_wys = 60

    # LISTA PRZESZKÓD
    przeszkody = []
    predkosc_przeszkod = 6  # prędkość przesuwania się przeszkód
    czas_do_nowej = 1500  # co ile ms tworzymy nową przeszkodę
    ostatnia_przeszkoda = pygame.time.get_ticks()  # czas ostatniej przeszkody

    wynik = 0  # wynik gracza

    licznik_klatek = 0  # do animacji
    faza = 0  # aktualna faza animacji

    uruchomiona = True  # flaga - czy gra działa?

    # --- GŁÓWNA PĘTLA GRY ---
    while uruchomiona:
        zegar.tick(FPS)  # utrzymujemy stałe tempo gry

        # OBSŁUGA ZDARZEŃ (klawiatura, zamknięcie okna)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                uruchomiona = False  # zamknięcie gry
            if event.type == pygame.KEYDOWN:
                # jeśli gracz naciśnie spację lub strzałkę do góry → skok
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    if not w_powietrzu:  # tylko gdy kulka na ziemi
                        predkosc_y = -18  # siła skoku
                        w_powietrzu = True

        # GRAWITACJA — kulka opada po skoku
        predkosc_y += grawitacja
        kulka_y += predkosc_y

        # SPRAWDZAMY, CZY DOTKNĘLIŚMY ZIEMI
        if kulka_y >= podloga_y - 30:
            kulka_y = podloga_y - 30  # przywracamy pozycję na podłodze
            predkosc_y = 0
            w_powietrzu = False

        # TWORZENIE NOWYCH PRZESZKÓD
        teraz = pygame.time.get_ticks()
        if teraz - ostatnia_przeszkoda > czas_do_nowej:
            ostatnia_przeszkoda = teraz
            szer = random.randint(20, 50)  # losowa szerokość
            wys = random.randint(30, 80)  # losowa wysokość
            przes = pygame.Rect(SZEROKOSC, podloga_y - wys, szer, wys)
            przeszkody.append(przes)

        # PRZESUWANIE PRZESZKÓD W LEWO
        for przes in przeszkody:
            przes.x -= predkosc_przeszkod

        # USUWANIE PRZESZKÓD POZA EKRANEM
        przeszkody = [p for p in przeszkody if p.right > 0]

        # SPRAWDZANIE KOLIZJI
        kulka_rect = pygame.Rect(
            kulka_x - kulka_szer // 2,
            kulka_y - kulka_wys // 2,
            kulka_szer,
            kulka_wys
        )
        for przes in przeszkody:
            if kulka_rect.colliderect(przes):
                uruchomiona = False  # KONIEC GRY

        # ZWIĘKSZAMY WYNIK
        wynik += 1

        # ANIMACJA — zmieniamy fazę co kilka klatek
        licznik_klatek += 1
        if not w_powietrzu:  # tylko gdy kulka biegnie po ziemi
            if licznik_klatek % 10 == 0:
                faza = 1 - faza  # zmieniamy fazę 0 ↔ 1

        # --- RYSOWANIE NA EKRANIE ---
        ekran.fill(BIALY)  # tło

        # RYSOWANIE PODŁOGI
        pygame.draw.line(ekran, CZARNY, (0, podloga_y), (SZEROKOSC, podloga_y), 2)

        # RYSOWANIE PRZESZKÓD
        for przes in przeszkody:
            pygame.draw.rect(ekran, CZARNY, przes, 2)

        # RYSOWANIE KULKI
        rysuj_kulke(ekran, kulka_x, kulka_y, faza)

        # WYŚWIETLANIE WYNIKU
        tekst = czcionka.render(f"Wynik: {wynik}", True, CZARNY)
        ekran.blit(tekst, (10, 10))

        pygame.display.flip()  # aktualizacja ekranu

    pygame.quit()  # wyłączenie pygame
    print("Koniec gry! Wynik:", wynik)


if __name__ == "__main__":
    main()  # start gry
