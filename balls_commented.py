import pygame  # Importuje bibliotekę pygame, która służy do tworzenia gier i grafiki 2D
import sys      # Importuje moduł sys, który umożliwia m.in. zamknięcie programu


# Definicja klasy Ball, która reprezentuje pojedynczą piłkę w grze
class Ball:
    # Konstruktor klasy Ball, wywoływany przy tworzeniu nowego obiektu Ball
    # image_path - ścieżka do pliku graficznego piłki
    # position   - lista [x, y] z pozycją startową piłki
    # speed      - lista [vx, vy] z prędkością piłki (piksele na klatkę)
    def __init__(self, image_path, position, speed):
        self.image = pygame.image.load(image_path)  # Wczytuje obrazek piłki z pliku
        self.rect = self.image.get_rect()            # Tworzy prostokąt (rect) o rozmiarze obrazka, używany do pozycjonowania
        self.rect.topleft = position                 # Ustawia lewy górny róg piłki na podaną pozycję startową
        self.speed = speed                           # Zapamiętuje prędkość piłki jako atrybut obiektu

    # Metoda aktualizująca pozycję piłki w każdej klatce animacji
    # screen_width  - szerokość ekranu (granica prawa)
    # screen_height - wysokość ekranu (granica dolna)
    def update(self, screen_width, screen_height):
        self.rect = self.rect.move(self.speed)  # Przesuwa prostokąt piłki o wektor prędkości [vx, vy]

        if self.rect.left < 0:                    # Jeśli lewa krawędź piłki wychodzi poza lewą ścianę
            self.rect.left = 0                    # Ustawia piłkę tuż przy lewej ścianie
            self.speed[0] = -self.speed[0]        # Odbija piłkę, odwracając poziomą składową prędkości
        elif self.rect.right > screen_width:      # Jeśli prawa krawędź piłki wychodzi poza prawą ścianę
            self.rect.right = screen_width        # Ustawia piłkę tuż przy prawej ścianie
            self.speed[0] = -self.speed[0]        # Odbija piłkę, odwracając poziomą składową prędkości

        if self.rect.top < 0:                     # Jeśli górna krawędź piłki wychodzi poza sufit
            self.rect.top = 0                     # Ustawia piłkę tuż przy suficie
            self.speed[1] = -self.speed[1]        # Odbija piłkę, odwracając pionową składową prędkości
        elif self.rect.bottom > screen_height:    # Jeśli dolna krawędź piłki wychodzi poza podłogę
            self.rect.bottom = screen_height      # Ustawia piłkę tuż przy podłodze
            self.speed[1] = -self.speed[1]        # Odbija piłkę, odwracając pionową składową prędkości


# Definicja klasy Game, która zarządza całą grą
class Game:
    WIDTH = 640           # Stała klasowa: szerokość okna gry w pikselach
    HEIGHT = 480          # Stała klasowa: wysokość okna gry w pikselach
    FPS = 50              # Stała klasowa: docelowa liczba klatek na sekundę
    BG_COLOR = (100, 100, 100)  # Stała klasowa: kolor tła w formacie RGB (szary)

    # Konstruktor klasy Game, inicjalizuje grę
    def __init__(self):
        pygame.init()                                               # Inicjalizuje wszystkie moduły biblioteki pygame
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))  # Tworzy okno gry o zadanych wymiarach
        self.fps_clock = pygame.time.Clock()                        # Tworzy zegar do kontrolowania liczby klatek na sekundę
        self.balls = []                                             # Inicjalizuje pustą listę, która będzie przechowywać piłki

    # Metoda dodająca obiekt piłki do listy piłek w grze
    def addBall(self, ball):
        self.balls.append(ball)  # Dodaje przekazany obiekt Ball na koniec listy self.balls

    # Metoda uruchamiająca główną pętlę gry
    def start(self):
        while True:                                     # Nieskończona pętla – gra działa aż do zamknięcia
            for event in pygame.event.get():            # Iteruje po wszystkich zdarzeniach w kolejce (kliknięcia, klawisze, itp.)
                if event.type == pygame.QUIT:           # Sprawdza, czy użytkownik kliknął przycisk zamknięcia okna
                    sys.exit()                          # Kończy działanie programu

            self.screen.fill(self.BG_COLOR)             # Wypełnia cały ekran kolorem tła (czyści poprzednią klatkę)

            for ball in self.balls:                     # Iteruje po wszystkich piłkach
                ball.update(self.WIDTH, self.HEIGHT)    # Aktualizuje pozycję każdej piłki (ruch + odbicia od ścian)
                self.screen.blit(ball.image, ball.rect) # Rysuje obrazek piłki na ekranie w jej aktualnej pozycji

            pygame.display.update()                     # Odświeża wyświetlany obraz (pokazuje nową klatkę)
            self.fps_clock.tick(self.FPS)               # Czeka tyle milisekund, ile potrzeba, aby utrzymać zadane FPS


# --- Kod główny programu ---

game = Game()  # Tworzy obiekt gry (inicjalizuje pygame i okno)

# Tworzy trzy piłki z różnymi obrazkami, pozycjami startowymi i prędkościami, a następnie dodaje je do gry
game.addBall(Ball("ball_soccer.png",     [0, 0],     [5, 5]))    # Piłka nożna: start w lewym górnym rogu, prędkość (+5, +5)
game.addBall(Ball("ball_basketball.png", [100, 200], [-4, 4]))   # Piłka do koszykówki: start w środku, prędkość (-4, +4)
game.addBall(Ball("ball_volleyball.png", [200, 50],  [8, -8]))   # Piłka do siatkówki: start w górze, prędkość (+8, -8)

game.start()  # Uruchamia główną pętlę gry
