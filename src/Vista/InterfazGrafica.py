import tkinter as tk
import pygame
import os

# Define la matriz del tablero
tablero = [[1, 1, 3, 1, 1, 1, 1, 1],
           [1, 2, 0, 0, 2, 0, 0, 1],
           [4, 0, 1, 1, 1, 0, 0, -1],
           [1, 0, 1, 0, 0, 0, 1, 1],
           [1, 2, 1, 3, 1, 1, 1, 1]]

# Directorio de assets
asset_dir = "assets"


# Función para cargar imágenes según el código y escalarlas al tamaño de la casilla
def cargar_imagen(codigo, cell_width, cell_height):
    image = pygame.image.load(os.path.join(asset_dir, f"{codigo}.png"))
    return pygame.transform.scale(image, (cell_width, cell_height))

# Función que se ejecuta cuando se hace clic en el botón "Jugar"
# Función que se ejecuta cuando se hace clic en el botón "Jugar"
def iniciar_juego():
    # Oculta el panel principal
    main_frame.pack_forget()

    # Crea un nuevo frame para el juego
    game_frame.pack()

    # Inicializa Pygame
    pygame.init()

    # Configura el tamaño del grid (i y j)
    i = len(tablero)
    j = len(tablero[0])

    # Calcula el tamaño de cada celda del grid
    cell_width = 800 // j
    cell_height = 600 // i

    # Crea una ventana de Pygame en el panel
    screen = pygame.display.set_mode((800, 600))

    # Color de fondo blanco
    background_color = (255, 255, 255)

    # Grosor del borde de las celdas
    border_thickness = 2

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dibuja el fondo blanco
        screen.fill(background_color)

        # Dibuja el grid con las imágenes escaladas
        for row in range(i):
            for col in range(j):
                image = cargar_imagen(tablero[row][col], cell_width, cell_height)
                screen.blit(image, (col * cell_width, row * cell_height))
                # Dibuja el borde de la celda
                pygame.draw.rect(screen, (0, 0, 0), (col * cell_width, row * cell_height, cell_width, cell_height), border_thickness)

        pygame.display.flip()

    pygame.quit()

    # Vuelve al panel principal después de que el juego termine
    game_frame.pack_forget()
    main_frame.pack()



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
playButton = tk.Button(main_frame, text="Jugar", foreground="green", width=20, height=5, command=iniciar_juego)
exitButton = tk.Button(main_frame, text="Salir", foreground="red", width=20, height=5, command=quit)

# Posición de botones en el panel principal
playButton.pack()
exitButton.pack()

# Mostramos la ventana principal
mainWindow.mainloop()