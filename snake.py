import pygame
import random

pygame.init()

clock = pygame.time.Clock()

LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake")

# estilo da fonte da pontuação
fonte = pygame.font.SysFont("Arial", 30)
fonte_grande = pygame.font.SysFont("Arial", 60)

#configurações
tamanho = 20
velocidade = 20

def resetar_jogo():
    
    # Posição inicial
    x = 300
    y = 400

    #DIREÇÃO INICIAL
    dx = velocidade
    dy = 0

    #Lista de  cobra
    cobra = []
    comprimento = 1

    #Pontos
    pontos = 0

    #comida
    comida_x = random.randrange(0, LARGURA, tamanho)
    comida_y = random.randrange(0, ALTURA, tamanho)

    

    game_over = False

    return (
        x,
        y,
        dx,
        dy,
        cobra,
        comprimento,
        pontos,
        comida_x,
        comida_y,
        game_over,
    
    )
(
    x,
    y,
    dx,
    dy,
    cobra,
    comprimento,
    pontos,
    comida_x,
    comida_y,
    game_over,
    
) = resetar_jogo()

rodando = True

while rodando:
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.KEYDOWN:
            if game_over:
                if evento.key == pygame.K_r:
                    (
                        x,
                        y,
                        dx,
                        dy,
                        cobra,
                        comprimento,
                        pontos,
                        comida_x,
                        comida_y,
                        game_over
                    ) = resetar_jogo()
            else:
                if evento.key == pygame.K_LEFT and dx == 0:
                    dx = -velocidade
                    dy = 0
                
                if evento.key == pygame.K_RIGHT and dx == 0:
                    dx = velocidade
                    dy = 0
                
                elif evento.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -velocidade
            
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = velocidade
        
    if not game_over:
           
        # MOVIMENTO
        x += dx
        y += dy
    
        # LIMITES DA TELA
        if (
            x < 0
            or x >= LARGURA
            or y < 0
            or y >= ALTURA
        ):
            game_over = True       
    
        #Cabeçadacobra
        cabeça = [x, y]
        cobra.append(cabeça)
    
        #MANTEM TAMANHO CORRETO
        if len(cobra) > comprimento:
            del cobra[0]
            
        #Colisao com o proprio corpo
        for segmento in cobra[:-1]:
            if segmento == cabeça:
                game_over = True
    
         #Verifica se comeu a comida
        if x == comida_x and y == comida_y:
        
            pontos += 1
            comprimento += 1
        
            print(f"Pontos: {pontos}")
        
            comida_x = random.randrange(0, LARGURA, tamanho)
            comida_y = random.randrange(0, ALTURA, tamanho)
        
    #DESENHO DA TELA
    tela.fill((0, 0, 0))
    
    #COBRA
    for segmento in cobra:
        pygame.draw.rect(
            tela,
            (0, 255, 0),
            (segmento[0], segmento[1], tamanho, tamanho)
        )
    for segmento in cobra[:-1]:
        if segmento == cobra:
            game_over = True
    
    #COMIDA
    pygame.draw.rect(
        tela,
        (255, 0, 0),
        (comida_x, comida_y, tamanho, tamanho)
    )
    
    #Pontuação
    texto_pontos = fonte.render(
        f"Pontos: {pontos}",
        True,
        (255, 255, 255)
    )
    
    tela.blit(texto_pontos, (10, 10))
    
    #Tela de Game Over
    if game_over:
        
        texto_game_over = fonte_grande.render(
            "GAME OVER",
            True,
            (255, 0, 0)
        )
        texto_reniciar = fonte.render(
            "Precione R para reiniciar",
            True,
            (255, 255, 255)
        )
        
        tela.blit(texto_game_over, (220, 220))
        tela.blit(texto_reniciar, (220, 300))
    
    pygame.display.update()
    
    clock.tick(10)
pygame.quit()
        