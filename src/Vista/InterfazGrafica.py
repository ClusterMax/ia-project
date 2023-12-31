import tkinter as tk
import pygame
import os
import Modelo.CostoUniformeRecursivo as cur


# Directorio de assets
asset_dir = os.path.join("src","assets")

clock = pygame.time.Clock()

class tablero:

    def __init__(self, tablero, posJugador=[2,7], posMeta=[2,0]):

        self.tablero = tablero
        self.posJugador = posJugador
        self.posMeta = posMeta
        

    # Función para cargar imágenes según el código y escalarlas al tamaño de la casilla
    def cargar_imagen(self, codigo, cell_width, cell_height):
        image = pygame.image.load(os.path.join(asset_dir, f"{codigo}.png"))
        return pygame.transform.scale(image, (cell_width, cell_height))
    

    def muestra_texto(self, pantalla,fuente,texto,color, dimensiones, x, y):
        tipo_letra = pygame.font.Font(fuente,dimensiones)
        superficie = tipo_letra.render(texto,True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (x, y)
        pantalla.blit(superficie,rectangulo)

    # Función que se ejecuta cuando se hace clic en el botón "Jugar"
    # Función que se ejecuta cuando se hace clic en el botón "Jugar"
    def iniciar_juego(self, main_frame, game_frame):
        # Oculta el panel principal
        main_frame.pack_forget()

        # Crea un nuevo frame para el juego
        game_frame.pack()

        # Inicializa Pygame
        pygame.init()

        # Configura el tamaño del grid (i y j)
        i = len(self.tablero)
        j = len(self.tablero[0])

        # Calcula el tamaño de cada celda del grid
        cell_width = 800 // j
        cell_height = 600 // i

        # Crea una ventana de Pygame en el panel
        screen = pygame.display.set_mode((800, 600))

        # Color de fondo blanco
        background_color = (255, 255, 255)

        # Grosor del borde de las celdas
        border_thickness = 2

        #Ruta a seguir
        ruta = cur.AlgoritmoCURecursivo(self.tablero, self.posJugador, self.posMeta)
        rutata = ruta.costoUniformeRecursivo()

        print(rutata)
        # Bucle principal del juego
        running = True
        fps = 500
        while running:
            fps = 450
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Dibuja el fondo blanco
            screen.fill(background_color)

            # Dibuja el grid con las imágenes escaladas
            for row in range(i):
                for col in range(j):
                    image = self.cargar_imagen(self.tablero[row][col], cell_width, cell_height)
                    screen.blit(image, (col * cell_width, row * cell_height))
                    # Dibuja el borde de la celda
                    pygame.draw.rect(screen, (0, 0, 0), (col * cell_width, row * cell_height, cell_width, cell_height), border_thickness)
            
            image = self.cargar_imagen(4, cell_width, cell_height)
            screen.blit(image, (self.posMeta[1] * cell_width, self.posMeta[0] * cell_height))
            # Dibuja el borde de la celda
            pygame.draw.rect(screen, (0, 0, 0), (self.posMeta[1] * cell_width, self.posMeta[0] * cell_height, cell_width, cell_height), border_thickness)

            image = self.cargar_imagen(-1, cell_width, cell_height)
            screen.blit(image, (self.posJugador[1] * cell_width, self.posJugador[0] * cell_height))
            # Dibuja el borde de la celda
            pygame.draw.rect(screen, (0, 0, 0), (self.posJugador[1] * cell_width, self.posJugador[0] * cell_height, cell_width, cell_height), border_thickness)

            pygame.display.flip()

            consolas = pygame.font.match_font('consolas')


            for paso in rutata:




                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        break
                if running != False:

                    if paso[1] == "vacio" or paso[1] =="meta":
                        columna = paso[0][1]
                        fila = paso[0][0]
                        image = self.cargar_imagen(-1, cell_width, cell_height)
                        screen.blit(image, ( columna * cell_width, fila * cell_height))
                        # Dibuja el borde de la celda
                        #clock.tick(5)
                    elif paso[1] == "gato":
                        columna = paso[0][1]
                        fila = paso[0][0]
                        image = self.cargar_imagen(8, cell_width, cell_height)
                        screen.blit(image, ( columna * cell_width, fila * cell_height))
                        # Dibuja el borde de la celda
                        #clock.tick(5)
                    
                    elif paso[1] =="amo":

                        fps -= 90
                        columna = paso[0][1]
                        fila = paso[0][0]
                        image = self.cargar_imagen(9, cell_width, cell_height)
                        screen.blit(image, ( columna * cell_width, fila * cell_height))
                    

                    
                    pygame.time.delay(fps)
                    pygame.display.flip()

                
                else:
                    break
                
        #pygame.quit()

        # Vuelve al panel principal después de que el juego termine
        game_frame.pack_forget()
        main_frame.pack()



    def start(self):

        # Creamos la ventana principal
        mainWindow = tk.Tk()
        mainWindow.geometry("800x600")

        # Creamos un frame principal
        main_frame = tk.Frame(mainWindow, width=800, height=600)
        main_frame.pack()

        game_frame = tk.Frame(mainWindow, width=800, height=600)

        gameLabel = tk.Label(main_frame, text="IA - PROYECT")
        gameLabel.config(font=("Courier", 18))
        gameLabel.pack()

        # Botón de jugar
        playButton = tk.Button(main_frame, text="Jugar", foreground="green", width=20, height=5, command=lambda: self.iniciar_juego(main_frame=main_frame, game_frame=game_frame))
        exitButton = tk.Button(main_frame, text="Salir", foreground="red", width=20, height=5, command= quit)

        # Posición de botones en el panel principal
        playButton.pack()
        exitButton.pack()

        # Mostramos la ventana principal
        mainWindow.mainloop()