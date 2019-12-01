import pygame
import random
from pygame.locals import *


# definindo função para fazer uma posição aleatória(x,y) onde colocarei minha maça.
def on_grid_random():
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)


#definindo função onde definirá quando será a colisão
def collision(c1, c2):  
    return (c1[0] == c2[0]) and (c1[1] == c2[1]) # vendo se em c1 e c2, as posicoes (x,y) são iguais
                                                 #se sim retorna true houve colisão, se não retorna false


# definindo uma Macro para o movimento da cobra.
UP = 0    #quando para cima 0
RIGHT = 1 #direita 1
DOWN = 2  #baixo 2
LEFT = 3  #quando para a esquera 3


pygame.init()
screen = pygame.display.set_mode(( 600 , 600 )) #selecionando o tamanho do display
pygame.display.set_caption( 'Snake' ) #nome do header do display
snake = [(200, 200), (210, 200), (220,200)] #definindo local onde ela iniciará coordenada(x,y)
snake_skin = pygame.Surface((10,10))         #definindo o tamanho do corpo a cobrinha
snake_skin.fill((255,255,255)) #definindo que a cor da cobrinha será branca.

apple_pos = on_grid_random()   #definindo o local da minha maça.
apple = pygame.Surface((10,10)) #definindo o tamanho da maça
apple.fill((255,0,0))           #definindo a cor da maça (vermelho)

my_direction = LEFT  # definindo direcao que a cobra irá começar a andar.

clock = pygame.time.Clock() #instanciando o clock que será oque definirá o tempo de andamento da cobrinha

while True :
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:  #se o tipo de evento for igual a quit(se a pessoa clicar em fechar)
            pygame.quit()       #terminar o pygame
            exit()
        if event.type == KEYDOWN:  #aqui verá se alguma tecla foi selecionada 
            if event.key == K_UP:     # se foi verificará uma por uma qual foi a tecla  
                my_direction = UP     # e qual for a selecionada será a minha nova direção.
            if event.key == K_DOWN:   
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos): # conferindo se houve colisão(cobra e maça)
        apple_pos = on_grid_random()   # se encontrou,vamos definir uma nova posição para a maça
        snake.append((0,0))            # cobra irá crescer

    # conferindo se a cobra colidiu com a parede
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        pygame.quit()
        exit()

    # conferindo se a cobrinha colidiu com ela mesma
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            pygame.quit()
            exit()

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1]) 
    # aqui será onde fará a cobra se mover (mudar a sua posição) entender melhor isso, importante
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10) 
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0,0,0))   #limpa a tela
    screen.blit(apple, apple_pos)  #printa,desenha a maça na tela
    for pos in snake:    
            screen.blit(snake_skin,pos)  #desenhando na tela a cobra nas posicoes.
    pygame.display.update()  # se não eu vou atualizando o meu display