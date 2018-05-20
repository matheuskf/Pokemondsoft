#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 10:05:31 2018

@author: luvi
"""

import pygame
import sys
from pygame.locals import *
import random
blue = (0,0,255)
red = (220,20,60)
green = (0,255,0)
class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width, height])
        self.image.fill(blue)
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x

class Entrada(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width, height])
        self.image.fill(red)
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x

class Grama (pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([width, height])
        self.image.fill(green)
        self.rect= self.image.get_rect()
        self.rect.y=y
        self.rect.x=x

class Player(pygame.sprite.Sprite):
    def __init__(self, imagemplayer, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.velocidadex=0
        self.velocidadey=0
        self.image = pygame.image.load(imagemplayer)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def velocidade(self, velx, vely):
        self.velocidadex=velx
        self.velocidadey=vely
    
            
    def update (self, Parede, Entrada, Grama):
        self.rect.x +=self.velocidadex
        block_hit_list=pygame.sprite.spritecollide(self, Parede, False)
        for block in block_hit_list:
            if self.velocidadex>0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
                
        self.rect.y +=self.velocidadey        
        block_hit_list=pygame.sprite.spritecollide(self, Parede, False)
        for block in block_hit_list:
            if self.velocidadey>0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

#================================================================                
        entrada_hit_list=pygame.sprite.spritecollide(self, Entrada, False)
        for block in entrada_hit_list:
            return 1
        
#=================================================================
        grama_hit_list=pygame.sprite.spritecollide(self, Grama, False)
        for block in grama_hit_list:
            if random.randint(0,100)<0.5:
                return 2
            else:
                return 0
        return 0
#=======================================================================
pygame.init()

tela = pygame.display.set_mode((900, 706), 0, 32)
pygame.display.set_caption('Inspermon')
relogio= pygame.time.Clock()
 #elif pressed_keys[K_UP]:
           # Player.rect.y-Player.velocidadey
      #  elif pressed_keys[K_DOWN]:
            #Player.rect.y+Player.velocidadey
mapa= pygame.image.load("mapa_inicial.jpg").convert()
sala=pygame.image.load("sala.jpg").convert()
batalha=pygame.image.load("Waterloo.jpg").convert()
player= Player("character.png",420,420,)
all_sprite_list = pygame.sprite.Group()

#========================================
lista_paredes=pygame.sprite.Group()
parede_ladoE=Parede(0,0,10, 700)
lista_paredes.add(parede_ladoE)
all_sprite_list.add(parede_ladoE)


parede_TOPO=Parede(0,0,900,10)
lista_paredes.add(parede_TOPO)
all_sprite_list.add(parede_TOPO)

parede_BAIXO=Parede(0,700,960,10)
lista_paredes.add(parede_BAIXO)
all_sprite_list.add(parede_BAIXO)

parede_ladoD=Parede(900,0,10,790)
lista_paredes.add(parede_ladoD)
all_sprite_list.add(parede_ladoD)

parede_insper=Parede(360,240,200,170)
lista_paredes.add(parede_insper)
all_sprite_list.add(parede_insper)

parede_loja=Parede(720,250,200,130)
lista_paredes.add(parede_loja)
all_sprite_list.add(parede_loja)

parede_hospital=Parede(710,590,190,110)
lista_paredes.add(parede_hospital)
all_sprite_list.add(parede_hospital)

#=======================================
#casa
lista_casa=pygame.sprite.Group()

insper=Entrada(410,410,40,10)
lista_casa.add(insper)
all_sprite_list.add(insper)

loja=Entrada(800,380,40,10)
lista_casa.add(loja)
all_sprite_list.add(loja)

hospital_S=Entrada(800,570,40,10)
lista_casa.add(hospital_S)
all_sprite_list.add(hospital_S)

hospital_L=Entrada(705,670,10,40)
lista_casa.add(hospital_L)
all_sprite_list.add(hospital_L)

#=========================================
#Grama
lista_grama=pygame.sprite.Group()

grama=Grama(10,10,350,700)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(360,420,50,300)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(360,10,160,230)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(360,10,160,230)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(520,10,380,20)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(560,70,240,180)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(560,250,155,90)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(840,20,60,220)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(840,390,60,190)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(710,380,90,200)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(560,380,150,290)
lista_grama.add(grama)
all_sprite_list.add(grama)

grama=Grama(450,420,110,250)
lista_grama.add(grama)
all_sprite_list.add(grama)

#=========================================

character_group=pygame.sprite.Group()
character_group.add(player)
all_sprite_list.add(player)
#===========================================================================================================
rodando= True
frame=0
while rodando:
    for event in pygame.event.get():
        
        # Verifica se o evento atual é QUIT (janela fechou).
        if event.type == QUIT:
            # Neste caso, marca o flag rodando como False, 
            # para sair do loop de jogo.
            rodando = False
    if event.type == pygame.KEYDOWN:  
        pressed_keys = pygame.key.get_pressed() 
        if pressed_keys[K_UP]:
            player.velocidade(0,-3)
        elif pressed_keys[K_DOWN]:
            player.velocidade(0,3)
        elif pressed_keys[K_RIGHT]:
            player.velocidade(3,0)
        elif pressed_keys[K_LEFT]:
            player.velocidade(-3,0)
    if event.type == pygame.KEYUP:
        if pressed_keys[K_UP]:
         player.velocidade(0,0)
        elif pressed_keys[K_DOWN]:
         player.velocidade(0,0)
        elif pressed_keys[K_RIGHT]:
            player.velocidade(0,0)
        elif pressed_keys[K_LEFT]:
            player.velocidade(0,0)
        
               
 
   
    print(player.rect.x)
    print(player.rect.y)

    if frame==0:
        frame+=player.update(lista_paredes,lista_casa,lista_grama)
        tela.blit(mapa, (0, 0))

        # Pinta os elementos do grupo de bolinhas na tela auxiliar.
        all_sprite_list.draw(tela)

        # Troca de tela na janela principal.
        pygame.display.flip()
    elif frame==1:
        print('oi')
        pygame.display.flip() 
        tela.blit(sala, (0, 0))
        for event in pygame.event.get():
            if event == pygame.KEYDOWN:
                if event.key == ord ('a'):
                    frame = 0
        pygame.display.flip()
    
    elif frame==2:
        print('war')
        pygame.display.flip() 
        tela.blit(batalha, (0, 0))
        for event in pygame.event.get():
            if event == pygame.KEYDOWN:
                if event.key == ord ('a'):
                    frame = 0
        pygame.display.flip()
        
       
       
        
    
    
    
    relogio.tick(60)

    # === FIM DA TERCEIRA PARTE ===
    # Agora volta para o início do loop e faz mais um passo do jogo.

pygame.display.quit()