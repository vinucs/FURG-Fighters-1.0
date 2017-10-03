#incoding: utf-8
from graphics import *
from math import sin
import time
import pygame
import random

start_time = time.time()
elapsed_time = time.time() - start_time
vencedor = 0
timer = 0
reset = 1
###Inicializa Mixer###

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
parametro = True

global cont23
cont23 = 0
borda_hp = Image(Point(220,509),"Arte/Buttons_and_Symbols/borda_hp.png")
borda_hp2 = Image(Point(740,509),"Arte/Buttons_and_Symbols/borda_hp.png")
borda_stamina = Image(Point(120,472),"Arte/Buttons_and_Symbols/borda_stamina.png")
borda_stamina2 = Image(Point(840,472),"Arte/Buttons_and_Symbols/borda_stamina.png")
borda_Ki = Image(Point(320,472),"Arte/Buttons_and_Symbols/borda_stamina.png")
borda_Ki2 = Image(Point(640,472),"Arte/Buttons_and_Symbols/borda_stamina.png")
versus = Image(Point(480,509),"Arte/Buttons_and_Symbols/versus.png")
round1 = Image(Point(480,280),"Arte/Buttons_and_Symbols/round1.png")
round2 = Image(Point(480,280),"Arte/Buttons_and_Symbols/round2.png")
final_round = Image(Point(480,280),"Arte/Buttons_and_Symbols/final_round.png")
fight5 = Image(Point(480,280),"Arte/Buttons_and_Symbols/fight.png")
imagem_fundo_dbz = Image(Point(760,300), "Arte/Buttons_and_Symbols/dbz.png")
imagem_fundo_sf = Image(Point(760,300), "Arte/Buttons_and_Symbols/sf.png")

def efeitos_menu(aba_atual,som,tipo):
    if som == True:
        if aba_atual == 6 and tipo == 0:
            efeito = pygame.mixer.Sound("music/menu/select_your_character.ogg")
            pygame.mixer.music.load("music/menu/char_selection.ogg")
            pygame.mixer.music.play(-1)
            efeito.play()
        elif aba_atual == 7 and tipo == 1:
            efeito = pygame.mixer.Sound("music/menu/confirma_mapa_som.ogg")
            efeito.play()
        if aba_atual == 8 and tipo == 1:
            efeito = pygame.mixer.Sound("music/menu/confirma_mapa_som.ogg")
            efeito.play()
        if aba_atual == 10 and tipo == 1:
            efeito = pygame.mixer.Sound("music/menu/confirma_mapa_som.ogg")
            efeito.play()
            
        
    

def Narrador(som,vencedor,contador_de_rounds):
    if som == True:
        if contador_de_rounds == 3:
           efeito = pygame.mixer.Sound("music/menu/final_round.ogg")
           efeito.play()
        if vencedor == 1:
            efeito = pygame.mixer.Sound("music/menu/you_win.ogg")
            efeito.play()
            return 0
        if vencedor == 2:
            efeito = pygame.mixer.Sound("music/menu/you_lose.ogg")
            efeito.play()
            return 0

def RoundShow(fight5,timer,contador_de_rounds,parametro2,parametro_FIGHT,t_inicial1,reset):
	if parametro_FIGHT == False:
		timer = time.time() - t_inicial1
	else:
		timer = 0
	if parametro2 == True:
		t_inicial1 = time.time()
		timer = time.time() - t_inicial1
		if contador_de_rounds == 0:
			round1.draw(janela)
		if contador_de_rounds == 1:
			round2.draw(janela)
		if contador_de_rounds == 2:
			final_round.draw(janela)
		parametro2 = False
		fight5.undraw()
		return timer,parametro2,parametro_FIGHT
	if timer>2:
		if parametro2 == False:
			round1.undraw()
			round2.undraw()
			final_round.undraw()
			if reset == 1:
				fight5.draw(janela)
			t_inicial1 = time.time()
			timer = 0
			if reset == 1:
				parametro_FIGHT = True
			return timer,parametro2,parametro_FIGHT
	return timer,parametro2,parametro_FIGHT

def fight(timer2,parametro_FIGHT,t_inicial_2,reset):
	timer2 = time.time() - t_inicial_2
	if reset == 1:
		t_inicial_2 = time.time()
		timer2 = time.time() - t_inicial_2
		reset = 0
		return timer2,parametro_FIGHT,reset,t_inicial_2
	if parametro_FIGHT == True:
		timer2 = time.time() - t_inicial_2
		if timer2>2:
			fight5.undraw()
			timer2 = 0
			parametro_FIGHT = False
			return timer2,parametro_FIGHT,reset,t_inicial_2
	return timer2,parametro_FIGHT,reset,t_inicial_2

def EscolheAcaoIA(dificuldade,posicao1,posicao2,delay_hit,start_time):    
    choice = random.randint(1,100)
    delay_hit =  time.time() - start_time
    if dificuldade == 1:
    	if posicao2.getX() >= posicao1.getX():
		    if (posicao2.getX()-posicao1.getX() < 150):
		        if delay_hit > 1.5:
		            if choice<=60:
		                delay_hit = 0
		                start_time = time.time()
		                return 88,delay_hit,start_time ### trocar pelo numero equivalente para chamar soco
		            elif choice>60 and choice<=90:
		                delay_hit = 0
		                start_time = time.time()
		                return 89,delay_hit,start_time ### trocar pelo numero equivalente para chamar chute
		            elif choice>90:
		                delay_hit = 0
		                start_time = time.time()
		                return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        else:
		            return 1,delay_hit,start_time
		    else:
		        if choice<=88:
		            if choice<=83:
		                return 113,delay_hit,start_time ### trocar pelo numero equivalente para chamar andar
		            else:
		                return 114,delay_hit,start_time
		        elif choice>88 and choice<=93:
		            return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        elif choice>93 and choice<=98:
		            return 104,delay_hit,start_time ### trocar pelo numero equivalente para chamar magia
		        elif choice>98:
		            return 90,delay_hit,start_time ### trocar pelo numero equivalente para chamar pula
        elif posicao1.getX() > posicao2.getX():
		    if (posicao1.getX()-posicao2.getX() < 150):
		        if delay_hit > 0.9:
		            if choice<=60:
		                delay_hit = 0
		                start_time = time.time()
		                return 88,delay_hit,start_time ### trocar pelo numero equivalente para chamar soco
		            elif choice>60 and choice<=90:
		                delay_hit = 0
		                start_time = time.time()
		                return 89,delay_hit,start_time ### trocar pelo numero equivalente para chamar chute
		            elif choice>90:
		                delay_hit = 0
		                start_time = time.time()
		                return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        else:
		            return 1,delay_hit,start_time
		    else:
		        if choice<=88:
		            if choice<=83:
		                return 114,delay_hit,start_time ### trocar pelo numero equivalente para chamar andar
		            else:
		                return 113,delay_hit,start_time
		        elif choice>88 and choice<=93:
		            return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        elif choice>93 and choice<=98:
		            return 104,delay_hit,start_time ### trocar pelo numero equivalente para chamar magia
		        elif choice>98:
		            return 90,delay_hit,start_time ### trocar pelo numero equivalente para chamar pula
    if dificuldade == 2	:
    	if posicao2.getX() >= posicao1.getX():
		    if (posicao2.getX()-posicao1.getX() < 150):
		        if delay_hit > 0.9:
		            if choice<=60:
		                delay_hit = 0
		                start_time = time.time()
		                return 88,delay_hit,start_time ### trocar pelo numero equivalente para chamar soco
		            elif choice>60 and choice<=90:
		                delay_hit = 0
		                start_time = time.time()
		                return 89,delay_hit,start_time ### trocar pelo numero equivalente para chamar chute
		            elif choice>90:
		                delay_hit = 0
		                start_time = time.time()
		                return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        else:
		            return 1,delay_hit,start_time
		    else:
		        if choice<=80:
		            if choice<=65:
		                return 113,delay_hit,start_time ### trocar pelo numero equivalente para chamar andar
		            else:
		                return 114,delay_hit,start_time
		        elif choice>80 and choice<=85:
		            return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        elif choice>85 and choice<=98:
		            return 104,delay_hit,start_time ### trocar pelo numero equivalente para chamar magia
		        elif choice>98:
		            return 90,delay_hit,start_time ### trocar pelo numero equivalente para chamar pula
        elif posicao1.getX() > posicao2.getX():
		    if (posicao1.getX()-posicao2.getX() < 150):
		        if delay_hit > 0.9:
		            if choice<=60:
		                delay_hit = 0
		                start_time = time.time()
		                return 88,delay_hit,start_time ### trocar pelo numero equivalente para chamar soco
		            elif choice>60 and choice<=90:
		                delay_hit = 0
		                start_time = time.time()
		                return 89,delay_hit,start_time ### trocar pelo numero equivalente para chamar chute
		            elif choice>90:
		                delay_hit = 0
		                start_time = time.time()
		                return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        else:
		            return 1,delay_hit,start_time
		    else:
		        if choice<=80:
		            if choice<=65:
		                return 114,delay_hit,start_time ### trocar pelo numero equivalente para chamar andar
		            else:
		                return 113,delay_hit,start_time
		        elif choice>80 and choice<=85:
		            return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        elif choice>85 and choice<=98:
		            return 104,delay_hit,start_time ### trocar pelo numero equivalente para chamar magia
		        elif choice>98:
		            return 90,delay_hit,start_time ### trocar pelo numero equivalente para chamar pula
    if dificuldade == 3:
    	if posicao2.getX() >= posicao1.getX():
		    if (posicao2.getX()-posicao1.getX() < 150):
		        if delay_hit > 0.6:
		            if choice<=70:
		                delay_hit = 0
		                start_time = time.time()
		                return 88,delay_hit,start_time ### trocar pelo numero equivalente para chamar soco
		            elif choice>70 and choice<=80:
		                delay_hit = 0
		                start_time = time.time()
		                return 89,delay_hit,start_time ### trocar pelo numero equivalente para chamar chute
		            elif choice>80:
		                delay_hit = 0
		                start_time = time.time()
		                return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        else:
		            return 1,delay_hit,start_time
		    else:
		        if choice<=70:
		            if choice<=70:
		                return 113,delay_hit,start_time ### trocar pelo numero equivalente para chamar andar
		            else:
		                return 114,delay_hit,start_time
		        elif choice>70 and choice<=72:
		            return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        elif choice>72 and choice<=93:
		            return 104,delay_hit,start_time ### trocar pelo numero equivalente para chamar magia
		        elif choice>93:
		            return 90,delay_hit,start_time ### trocar pelo numero equivalente para chamar pula
        elif posicao1.getX() > posicao2.getX():
		    if (posicao1.getX()-posicao2.getX() < 150):
		        if delay_hit > 0.6:
		            if choice<=60:
		                delay_hit = 0
		                start_time = time.time()
		                return 88,delay_hit,start_time ### trocar pelo numero equivalente para chamar soco
		            elif choice>60 and choice<=90:
		                delay_hit = 0
		                start_time = time.time()
		                return 89,delay_hit,start_time ### trocar pelo numero equivalente para chamar chute
		            elif choice>90:
		                delay_hit = 0
		                start_time = time.time()
		                return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        else:
		            return 1,delay_hit,start_time
		    else:
		        if choice<=80:
		            if choice<=65:
		                return 114,delay_hit,start_time ### trocar pelo numero equivalente para chamar andar
		            else:
		                return 113,delay_hit,start_time
		        elif choice>80 and choice<=85:
		            return 87,delay_hit,start_time ### trocar pelo numero equivalente para chamar defende
		        elif choice>85 and choice<=98:
		            return 104,delay_hit,start_time ### trocar pelo numero equivalente para chamar magia
		        elif choice>98:
		            return 90,delay_hit,start_time ### trocar pelo numero equivalente para chamar pula
            
def selecionaMAPA(mapa):
    if mapa == 1:
    	numero_de_frames = 16
        Imagem_mapa = Image(Point(480,0),"stage/Punk_Toilet_Map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 2:
    	numero_de_frames = 16
        Imagem_mapa = Image(Point(480,0),"stage/Bonito_tarde.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 3:
    	numero_de_frames = 8
        Imagem_mapa = Image(Point(480,0),"stage/Porto_Map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 4:
        numero_de_frames = 8
        Imagem_mapa = Image(Point(480,0), "stage/Air_Crystal_Map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 5:
    	numero_de_frames = 36
        Imagem_mapa = Image(Point(480,0),"stage/Tribal_Map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 6:
    	numero_de_frames = 8
        Imagem_mapa = Image(Point(480,0),"stage/Korea_Map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 8:
    	numero_de_frames = 16
        Imagem_mapa = Image(Point(480,0),"stage/graveyard_map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 7:
    	numero_de_frames = 15
        Imagem_mapa = Image(Point(480,0),"stage/boat_map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 9:
    	numero_de_frames = 8
        Imagem_mapa = Image(Point(480,0),"stage/Riot_Map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 10:
    	numero_de_frames = 8
        Imagem_mapa = Image(Point(480,0),"stage/Y_Train_Map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 11:
    	numero_de_frames = 20
        Imagem_mapa = Image(Point(480,0),"stage/Kids_Map.png")
        return Imagem_mapa,numero_de_frames
    if mapa == 12:
    	numero_de_frames = 24
        Imagem_mapa = Image(Point(480,0),"stage/Bet_Map.png")
        return Imagem_mapa,numero_de_frames

def ApagaTudo(aba_atual,cont):
    apagaMapas(aba_atual)
    botao_confirmar2.undraw()
    Fundo[cont].undraw()
    logo.undraw()
    seta.undraw()
    seta_back.undraw()
    moldura.undraw()
    botao_confirmar.undraw()
    escolha_mapa.undraw()
    if aba_atual == 7:
        punk_toilet_fundo.undraw()
        porto_fundo.undraw()
        bonito_tarde_fundo.undraw()
        air_crystal_fundo.undraw()
    if aba_atual == 8:
        tribal_fundo.undraw()
        korea_fundo.undraw()
        boat_fundo.undraw()
        graveyard_fundo.undraw()
    if aba_atual == 10:
        riot_fundo.undraw()
        y_train_fundo.undraw()
        kids_fundo.undraw()
        bet_fundo.undraw()
        
###Recebe valores do teclado###

def controle(t, p,num_jogadores,parametro_IA):
    if num_jogadores == 2:
        tecla[0] = []
        tecla[1] = []
        if(40 in t):
            tecla[0].append(1)
        if(38 in t):
            tecla[0].append(2)
        if(43 in t):
            tecla[0].append(3)
        if(42 in t):
            tecla[0].append(4)
        if(39 in t):
            tecla[0].append(5)
        if(65 in t):
            tecla[0].append(6)
        if(44 in t):
            tecla[0].append(7)
        if(45 in t):
            tecla[0].append(8)
        if(114 in t):
            tecla[1].append(1)
        if(113 in t):
            tecla[1].append(2)
        if(88 in t):
            tecla[1].append(3)
        if(87 in t):
            tecla[1].append(4)
        if(116 in t):
            tecla[1].append(5)
        if(90 in t):
            tecla[1].append(6)
        if(89 in t):
            tecla[1].append(7)
        if(104 in t):
            tecla[1].append(8)
        if(end_game == 0 and reinicia_round == 0):
            analise(estado_player[0] , estado_player[1], p[0], p[1], p[2])
        p[0] = fundo.getAnchor()
        p[1] = posicao_p1
        p[2] = posicao_p2
        return p,timer
    elif num_jogadores == 1:
        tecla[0] = []
        tecla[1] = [0]
        if(40 in t):
	        tecla[0].append(1)
        if(38 in t):
	        tecla[0].append(2)
        if(43 in t):
	        tecla[0].append(3)
        if(42 in t):
	        tecla[0].append(4)
        if(39 in t):
	        tecla[0].append(5)
        if(65 in t):
	        tecla[0].append(6)
        if(44 in t):
	        tecla[0].append(7)
        if(45 in t):
	        tecla[0].append(8)
        if(parametro_IA == 114):
            tecla[1].append(1)
        if(parametro_IA == 113):
            tecla[1].append(2)
        if(parametro_IA == 88):
            tecla[1].append(3)
        if(parametro_IA == 87):
            tecla[1].append(4)
        if(parametro_IA == 116):
            tecla[1].append(5)
        if(parametro_IA == 90):
            tecla[1].append(6)
        if(parametro_IA == 89):
            tecla[1].append(7)
        if(parametro_IA == 104):
            tecla[1].append(8)
        if(end_game == 0 and reinicia_round == 0):
	        analise(estado_player[0] , estado_player[1], p[0], p[1], p[2])
        p[0] = fundo.getAnchor()
        p[1] = posicao_p1
        p[2] = posicao_p2
        return p,timer
        

def analise(e1, e2, pm, p1, p2):
	global player1
	global player2
	global tempo_mov_p1
	global tempo_mov_p2
	global tempo_pulo_p1
	global tempo_pulo_p2
	global tempo_especial_p1
	global tempo_especial_p2
	global t_def_p1
	global t_def_p2
	global player1_Ki
	global player2_Ki
	if(3 in tecla[0] and 7 in tecla[0]):
		print "error"
	elif(1 in tecla[0] and 2 in tecla[0]):
		print "error"
	elif(e1 != 3 and e1 != 7 and e1 != 8 and e1 != 9 and e1 != 10 and e1 != 11 and e1 != 12):
		if(1 in tecla[0] and (4 not in tecla[0]) and (5 not in tecla[0])):
			move_p1(6, 0)
			if(e1 != 6):
				if(e1 != 1):
					draw_sprite(1,1)
					undraw(estado_player[0], 1, lado_sprite[0])
				estado_player[0] = 1
		if(2 in tecla[0] and (4 not in tecla[0]) and (5 not in tecla[0])):
			move_p1(-6, 0)		
			if(e1 != 6):
				if(e1 != 2):
					draw_sprite(2,1)
					undraw(e1, 1, lado_sprite[0])
				estado_player[0] = 2
		if((3 in tecla[0]) and e1 != 6 and (4 not in tecla[0]) and (5 not in tecla[0])):
			punch(1)
			som_estado(1,player1,1)
			undraw(estado_player[0], 1, lado_sprite[0])
			tempo_mov_p1 = time.clock()
			estado_player[0] = 3		
		if((4 in tecla[0]) and e1 != 6 and (5 not in tecla[0]) and (estado_stamina[0] == 1)):
			if(e1 != 4):
				t_def_p1 = time.clock()
				defender(1)
				undraw(estado_player[0], 1, lado_sprite[0])
			estado_player[0] = 4
		if((5 in tecla[0]) and e1 != 6 and (4 not in tecla[0])):
			if(e1 != 5):
				agachar(1)
				undraw(estado_player[0], 1, lado_sprite[0])
			estado_player[0] = 5
		if((6 in tecla[0]) and e1 != 6 and (4 not in tecla[0]) and (5 not in tecla[0])):
			undraw(estado_player[0], 1, lado_sprite[0])
			estado_player[0] = 6
			if(lado_sprite[0] == 0):
				sprite_jump[0] = trocar_sprite(sprite_jump[0], 6, 0)
			else:
				sprite_jump[0] = trocar_sprite(sprite_jump[0], -7, 0)
			tempo_pulo_p1 = time.clock()
		if((7 in tecla[0]) and e1 != 6 and (4 not in tecla[0]) and (5 not in tecla[0])):
			kick(1)
			som_estado(1,player1,2)
			undraw(estado_player[0], 1, lado_sprite[0])
			tempo_mov_p1 = time.clock()
			estado_player[0] = 7
		if((8 in tecla[0]) and e1 != 6 and (4 not in tecla[0]) and (5 not in tecla[0]) and especial_ativo[0] == 0 and hitespecial1_ativo[0] == 0 and player1_Ki > 24):
			player1_Ki -= 25
			som_estado(1,player1,3)
			especial_move_to_player(1, lado_sprite[0])
			lado_energia[0] = lado_sprite[0]
			especial_1(1)
			undraw(estado_player[0], 1, lado_sprite[0])
			tempo_mov_p1 = time.clock()
			estado_player[0] = 8	
	if(3 in tecla[1] and 7 in tecla[1]):
		print "error"
	elif(1 in tecla[1] and 2 in tecla[1]):
		print "error"
	elif(e2 != 3 and e2 != 7 and e2 != 8 and e2 != 9 and e2 != 10 and e2 != 11 and e1 != 12):		
		if(1 in tecla[1]and (4 not in tecla[1]) and (5 not in tecla[1])):
			if(p2.getX() - p1.getX() < 750):
				if(p2.getX() < 860):
					move_p2(6, 0)
				else:
					aux_mapa = move_mapa(-6)
					if(aux_mapa == 1):
						move_p1(-6, 0)
			if(e2 != 6):
				if(e2 != 1):
					draw_sprite(1,2)
					undraw(estado_player[1], 2, lado_sprite[1])
				estado_player[1] = 1
		if(2 in tecla[1]and (4 not in tecla[1]) and (5 not in tecla[1])):
			if(p2.getX() - p1.getX() > -750):
				if(p2.getX() > 100):
					move_p2(-6, 0)
				else:
					aux_mapa = move_mapa(6)
					if(aux_mapa == 1):						
						move_p1(6, 0)
			if(e2 != 6):
				if(e2 != 2):
					draw_sprite(2,2)
					undraw(estado_player[1], 2, lado_sprite[1])
				estado_player[1] = 2
		if((3 in tecla[1]) and e2 != 6 and (4 not in tecla[1]) and (5 not in tecla[1])):
			punch(2)
			som_estado(2,player2,1)	
			undraw(estado_player[1], 2, lado_sprite[1])
			tempo_mov_p2 = time.clock()
			estado_player[1] = 3	
		if((4 in tecla[1]) and e2 != 6 and (5 not in tecla[1]) and (estado_stamina[1] == 1)):
			if(e2 != 4):
				t_def_p2 = time.clock()
				defender(2)	
				undraw(estado_player[1], 2, lado_sprite[1])
			estado_player[1] = 4
		if((5 in tecla[1]) and e2 != 6 and (4 not in tecla[1])):
			if(e2 != 5):
				agachar(2)
				undraw(estado_player[1], 2, lado_sprite[1])
			estado_player[1] = 5
		if((6 in tecla[1]) and e2 != 6 and (4 not in tecla[1]) and (5 not in tecla[1])):
			if(lado_sprite[1] == 0):
				sprite_jump[1] = trocar_sprite(0, 6, 1)
			else:
				sprite_jump[1] = trocar_sprite(0, -7, 1)
			undraw(estado_player[1], 2, lado_sprite[1])
			estado_player[1] = 6
			tempo_pulo_p2 = time.clock()
		if((7 in tecla[1]) and e2 != 6 and (4 not in tecla[1]) and (5 not in tecla[1])):
			kick(2)
			som_estado(2,player2,2)
			undraw(estado_player[1], 2, lado_sprite[1])
			tempo_mov_p2 = time.clock()
			estado_player[1] = 7
		if((8 in tecla[1]) and e2 != 6 and (4 not in tecla[1]) and (5 not in tecla[1]) and especial_ativo[1] == 0 and hitespecial1_ativo[1] == 0 and player2_Ki > 24):
			player2_Ki -= 25
			som_estado(2,player2,3)
			especial_move_to_player(2, lado_sprite[1])
			lado_energia[1] = lado_sprite[1]
			especial_1(2)
			undraw(estado_player[1], 2, lado_sprite[1])
			tempo_mov_p2 = time.clock()
			estado_player[1] = 8

def draw_sprite(e, jogador):
	if(e == 0):
		if(jogador == 1):
			if(lado_sprite[0] == 0):
				sprite_parado[0] = trocar_sprite(sprite_parado[0], 0, 0)
			else:
				sprite_parado[0] = trocar_sprite(sprite_parado[0], -1, 0)
		else:
			if(lado_sprite[1] == 0):
				sprite_parado[1] = trocar_sprite(sprite_parado[1], 0, 1)
			else:
				sprite_parado[1] = trocar_sprite(sprite_parado[1], -1, 1)
	elif(e == 1):
		if(jogador == 1):
			if(lado_sprite[0] == 0):
				sprite_walkDireita[0] = trocar_sprite(sprite_walkDireita[0], 1, 0)
			else:
				sprite_walkDireita[0] = trocar_sprite(sprite_walkDireita[0], -2, 0)		
		else:
			if(lado_sprite[1] == 0):
				sprite_walkDireita[1] = trocar_sprite(sprite_walkDireita[1], 1, 1)
			else:
				sprite_walkDireita[1] = trocar_sprite(sprite_walkDireita[1], -2, 1)
	elif(e == 2):
		if(jogador == 1):
			if(lado_sprite[0] == 0):
				sprite_walkEsquerda[0] = trocar_sprite(sprite_walkEsquerda[0], 2, 0)
			else:
				sprite_walkEsquerda[0] = trocar_sprite(sprite_walkEsquerda[0], -3, 0)
		else:
			if(lado_sprite[1] == 0):
				sprite_walkEsquerda[1] = trocar_sprite(sprite_walkEsquerda[1], 2, 1)
			else:
				sprite_walkEsquerda[1] = trocar_sprite(sprite_walkEsquerda[1], -3, 1)
	elif(e == 4):
		defender(jogador)
	elif(e == 5):
		agachar(jogador)

def undraw(i, jogador, e_lado):
	if(jogador == 1):
		if(e_lado == 0):
			c = 0
			while(c < len(player[0][i])):
				player[0][i][c].undraw()
				c += 1
		else:
			c = 0
			while(c < len(player[0][(i*-1)-1])):
				player[0][(i*-1)-1][c].undraw()
				c += 1
	else:
		if(e_lado == 0):
			c = 0
			while(c < len(player[1][i])):
				player[1][i][c].undraw()
				c += 1
		else:
			c = 0
			while(c < len(player[1][(i*-1)-1])):
				player[1][(i*-1)-1][c].undraw()
				c += 1

def undraw_especial(jogador):
	c1 = 0
	while(c1 < len(especial[jogador])):
		c2 = 0
		while(c2 < len(especial[jogador][c1])):
			especial[jogador][c1][c2].undraw()
			c2 += 1
		c1 += 1

def move_p1(px, py):
	if(px > 0):
		if(posicao_p1.getX() - posicao_p2.getX() < 750):
			if(posicao_p1.getX() < 860):
				posicao_p1.move(px,0)
				c1 = 0
				while(c1 < len(player[0])):
					c2 = 0
					while(c2 < len(player[0][c1])):
						player[0][c1][c2].move(px,0)
						c2 += 1
					c1 += 1	
				c1 = 0
				while(c1 < len(p_winner[0])):
					p_winner[0][c1].move(px,0)
					p_winner[1][c1].move(px,0)
					c1 += 1
			else:
				aux_mapa = move_mapa(-px)
				if(aux_mapa == 1):
					move_p2(-px, 0)	
	elif(px < 0):
		if(posicao_p1.getX() - posicao_p2.getX() > -750):
			if(posicao_p1.getX() > 100):
				posicao_p1.move(px,0)
				c1 = 0
				while(c1 < len(player[0])):
					c2 = 0
					while(c2 < len(player[0][c1])):
						player[0][c1][c2].move(px,0)
						c2 += 1
					c1 += 1	
				c1 = 0
				while(c1 < len(p_winner[0])):
					p_winner[0][c1].move(px,0)
					p_winner[1][c1].move(px,0)
					c1 += 1
			else:
				aux_mapa = move_mapa(-px)
				if(aux_mapa == 1):						
					move_p2(-px, 0)
	if(py != 0):
		posicao_p1.move(0,py)
		c1 = 0
		while(c1 < len(player[0])):
			c2 = 0
			while(c2 < len(player[0][c1])):
				player[0][c1][c2].move(0,py)
				c2 += 1
			c1 += 1	
		c1 = 0
		while(c1 < len(p_winner[0])):
			p_winner[0][c1].move(0,py)
			p_winner[1][c1].move(0,py)
			c1 += 1

def move_p2(px, py):
	if(px > 0):
		if(posicao_p2.getX() - posicao_p1.getX() < 750):
			if(posicao_p2.getX() < 860):
				posicao_p2.move(px,0)
				c1 = 0
				while(c1 < len(player[1])):
					c2 = 0
					while(c2 < len(player[1][c1])):
						player[1][c1][c2].move(px,0)
						c2 += 1
					c1 += 1	
				c1 = 0
				while(c1 < len(p_winner[2])):
					p_winner[2][c1].move(px,0)
					p_winner[3][c1].move(px,0)
					c1 += 1
			else:
				aux_mapa = move_mapa(-px)
				if(aux_mapa == 1):
					move_p1(-px, 0)	
	elif(px < 0):
		if(posicao_p2.getX() - posicao_p1.getX() > -750):
			if(posicao_p2.getX() > 100):
				posicao_p2.move(px,0)
				c1 = 0
				while(c1 < len(player[1])):
					c2 = 0
					while(c2 < len(player[1][c1])):
						player[1][c1][c2].move(px,0)
						c2 += 1
					c1 += 1	
				c1 = 0
				while(c1 < len(p_winner[2])):
					p_winner[2][c1].move(px,0)
					p_winner[3][c1].move(px,0)
					c1 += 1
			else:
				aux_mapa = move_mapa(-px)
				if(aux_mapa == 1):						
					move_p1(-px, 0)
	if(py != 0):
		posicao_p2.move(0,py)
		c1 = 0
		while(c1 < len(player[1])):
			c2 = 0
			while(c2 < len(player[1][c1])):
				player[1][c1][c2].move(0,py)
				c2 += 1
			c1 += 1	
		c1 = 0
		while(c1 < len(p_winner[2])):
			p_winner[2][c1].move(0,py)
			p_winner[3][c1].move(0,py)
			c1 += 1	

def punch(jogador):
	if(jogador == 1):
		if(lado_sprite[0] == 0):
			sprite_punch[0] = trocar_sprite(0, 3, 0)
		else:
			sprite_punch[0] = trocar_sprite(0, -4, 0)
	else:
		if(lado_sprite[1] == 0):
			sprite_punch[1] = trocar_sprite(0, 3, 1)
		else:
			sprite_punch[1] = trocar_sprite(0, -4, 1)

def kick(jogador):
	if(jogador == 1):
		if(lado_sprite[0] == 0):
			sprite_chute[0] = trocar_sprite(0, 7, 0)
		else:
			sprite_chute[0] = trocar_sprite(0, -8, 0)
	else:
		if(lado_sprite[1] == 0):
			sprite_chute[1] = trocar_sprite(0, 7, 1)
		else:
			sprite_chute[1] = trocar_sprite(0, -8, 1)

def especial_1(jogador):
	if(jogador == 1):
		if(lado_sprite[0] == 0):
			sprite_especial1[0] = trocar_sprite(sprite_especial1[0], 8, 0)
		else:
			sprite_especial1[0] = trocar_sprite(sprite_especial1[0], -9, 0)
	else:
		if(lado_sprite[1] == 0):
			sprite_especial1[1] = trocar_sprite(sprite_especial1[1], 8, 1)
		else:
			sprite_especial1[1] = trocar_sprite(sprite_especial1[1], -9, 1)

def energia_1(jogador):
	if(jogador == 1):
		if(lado_energia[0] == 0):
			sprite_energia1[0] = trocar_especial(sprite_energia1[0], 0, 0)
		else:
			sprite_energia1[0] = trocar_especial(sprite_energia1[0], -1, 0)
	else:
		if(lado_energia[1] == 0):
			sprite_energia1[1] = trocar_especial(sprite_energia1[1], 0, 1)
		else:
			sprite_energia1[1] = trocar_especial(sprite_energia1[1], -1, 1)

def hitespecial1(j):
		if(lado_energia[j] == 0):
			sprite_ener1hit[j] = trocar_especial(sprite_ener1hit[j], 1, j)
		else:
			sprite_ener1hit[j] = trocar_especial(sprite_ener1hit[j], -2, j)

def defender(jogador):
	if(jogador == 1):
		if(lado_sprite[0] == 0):
			sprite_defender[0] = trocar_sprite(0, 4, 0)
		else:
			sprite_defender[0] = trocar_sprite(0, -5, 0)
	else:
		if(lado_sprite[1] == 0):
			sprite_defender[1] = trocar_sprite(0, 4, 1)
		else:
			sprite_defender[1] = trocar_sprite(0, -5, 1)

def agachar(jogador):
	if(jogador == 1):
		if(lado_sprite[0] == 0):
			player[0][5][0].draw(janela)
		else:
			player[0][-6][0].draw(janela)
		sprite_agachar[0] = 1
	else:	
		if(lado_sprite[1] == 0):
			player[1][5][0].draw(janela)
		else:
			player[1][-6][0].draw(janela)
		sprite_agachar[1] = 1

def get_up(j):
		if(lado_sprite[j] == 0):
			sprite_getUp[j] = trocar_sprite(0, 12, j)
		else:
			sprite_getUp[j] = trocar_sprite(0, -13, j)

def hit(jogador, dano, e):
	global delay_p1
	global delay_p2
	global tempo_hitHard1
	global tempo_hitHard2
	global aux_hitHard1
	global aux_hitHard2
	global velocidade_hitHard1
	global velocidade_hitHard2
	global aux_hitLeveAr1
	global aux_hitLeveAr2
	global velocidade_hitLeveAr1
	global velocidade_hitLeveAr2
	global player1_hp
	global player2_hp
	global player1_sta
	global player2_sta
	global player1_Ki
	global player2_Ki
	global t_def_p1
	global t_def_p2
	global limite_mapa
	if(jogador == 1):
		player2_Ki += 5
		if(estado_player[0] != 4 and estado_player[0] != 6 and estado_player[0] != 10 and estado_player[0] != 11 and estado_player[1] != 12):
			delay_p1 = time.clock()
			player1_hp -= dano
			barra_hp(1)
			if(player1_hp > 0):
				estado_player[0] = 9
				if(lado_sprite[0] == 0):
					sprite_danoLeve[0] = trocar_sprite(0, 9, 0)
				else:
					sprite_danoLeve[0] = trocar_sprite(0, -10, 0)
			else:
				estado_player[0] = 11
				tempo_hitHard1 = delay_p1
				if(lado_sprite[0] == 0):
					sprite_danoHard[0] = trocar_sprite(0, 11, 0)
				else:
					sprite_danoHard[0] = trocar_sprite(0, -12, 0)
			undraw(e, 1, lado_sprite[0])
		elif(estado_player[0] == 6):
			delay_p1 = time.clock()
			player1_hp -= dano
			barra_hp(1)
			if(player1_hp > 0):
				estado_player[0] = 10
				if(lado_sprite[0] == 0):
					sprite_danoLeveAr[0] = trocar_sprite(0, 10, 0)
				else:
					sprite_danoLeveAr[0] = trocar_sprite(0, -11, 0)
			else:
				estado_player[0] = 11
				tempo_hitHard1 = delay_p1
				if(lado_sprite[0] == 0):
					sprite_danoHard[0] = trocar_sprite(0, 11, 0)
				else:
					sprite_danoHard[0] = trocar_sprite(0, -12, 0)
			undraw(e, 1, lado_sprite[0])
		elif((estado_player[0] == 4) and (player1_sta - dano > 0)):
			print sprite_defender[0]
			if(time.clock() - t_def_p1 < 0.2):
				player2_sta -= 20
				barra_stamina(2)
				print "perfect"
			else:
				player1_sta -= 15
				barra_stamina(1)
			if(sprite_defender[0] != 0):
				if(lado_sprite[0] == 0):
					sprite_defender[0] = trocar_sprite(1, 4, 0)
				else:
					sprite_defender[0] = trocar_sprite(1, -5, 0)
		elif((estado_player[0] == 4) and (player1_sta - dano < 1)):
			if(time.clock() - t_def_p1 < 0.2):
				player2_sta -= 20
				barra_stamina(2)
				print "perfect"
				if(sprite_defender[0] != 0):
					if(lado_sprite[0] == 0):
						sprite_defender[0] = trocar_sprite(1, 4, 0)
					else:
						sprite_defender[0] = trocar_sprite(1, -5, 0)
			else:
				estado_player[0] = 11
				estado_stamina[0] = 0
				player1_sta = 0
				delay_p1 = time.clock()
				tempo_hitHard1 = delay_p1
				player1_hp -= dano
				barra_hp(1)
				if(lado_sprite[0] == 0):
					sprite_danoHard[0] = trocar_sprite(0, 11, 0)
				else:
					sprite_danoHard[0] = trocar_sprite(0, -12, 0)
				undraw(4, 1, lado_sprite[0])
		elif(estado_player[0] == 11 or estado_player[0] == 10):
			player1_hp -= dano
			barra_hp(1)
			delay_p1 = time.clock()
			if(player1_hp > 0 and estado_stamina[0] == 1):
				ls = lado_sprite[0]
				if(limite_mapa == 1):
					if(lado_sprite[0] == 1):
						ls = 1
						lado_sprite[0] = 0
					else:
						ls = 0
						lado_sprite[0] = 1
				estado_player[0] = 10
				velocidade_hitLeveAr1 = 8
				aux_hitLeveAr1 = 0.4
				undraw(e, 1, ls)
				if(lado_sprite[0] == 0):
					sprite_danoLeveAr[0] = trocar_sprite(0, 10, 0)
				else:
					sprite_danoLeveAr[0] = trocar_sprite(0, -11, 0)
			else:
				estado_player[0] = 11
				aux_hitHard1 = 0
				velocidade_hitHard1 = 6
				tempo_hitHard1 = delay_p1
				undraw(e, 1, lado_sprite[0])
				if(lado_sprite[0] == 0):
					sprite_danoHard[0] = trocar_sprite(0, 11, 0)
				else:
					sprite_danoHard[0] = trocar_sprite(0, -12, 0)
	else:
		player1_Ki += 5
		if(estado_player[1] != 4 and estado_player[1] != 6 and estado_player[1] != 10 and estado_player[1] != 11 and estado_player[1] != 12):
			delay_p2 = time.clock()
			player2_hp -= dano
			barra_hp(2)
			if(player2_hp > 0):
				estado_player[1] = 9
				if(lado_sprite[1] == 0):
					sprite_danoLeve[1] = trocar_sprite(sprite_danoLeve[1], 9, 1)
				else:
					sprite_danoLeve[1] = trocar_sprite(sprite_danoLeve[1], -10, 1)
			else:
				estado_player[1] = 11
				tempo_hitHard2 = delay_p2
				if(lado_sprite[1] == 0):
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], 11, 1)
				else:
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], -12, 1)
			undraw(e, 2, lado_sprite[1])
		elif(estado_player[1] == 6):
			delay_p2 = time.clock()
			player2_hp -= dano
			barra_hp(2)
			if(player2_hp > 0):
				estado_player[1] = 10
				if(lado_sprite[1] == 0):
					sprite_danoLeveAr[1] = trocar_sprite(sprite_danoLeveAr[1], 10, 1)
				else:
					sprite_danoLeveAr[1] = trocar_sprite(sprite_danoLeveAr[1], -11, 1)
			else:
				estado_player[1] = 11
				tempo_hitHard2 = delay_p2
				if(lado_sprite[1] == 0):
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], 11, 1)
				else:
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], -12, 1)
			undraw(e, 2, lado_sprite[1])
		elif((estado_player[1] == 4) and (player2_sta - dano > 0)):
			print sprite_defender[1]
			if(time.clock() - t_def_p2 < 0.5):
				player1_sta -= 20
				barra_stamina(1)
				print "perfect"
			else:
				player2_sta -= 15
				barra_stamina(2)
			if(sprite_defender[1] != 0):
				if(lado_sprite[1] == 0):
					sprite_defender[1] = trocar_sprite(1, 4, 1)
				else:
					sprite_defender[1] = trocar_sprite(1, -5, 1)
		elif((estado_player[1] == 4) and (player2_sta - dano < 1)):
			if(time.clock() - t_def_p2 < 0.5):
				player1_sta -= 20
				barra_stamina(1)
				print "perfect"
				if(sprite_defender[1] != 0):
					if(lado_sprite[1] == 0):
						sprite_defender[1] = trocar_sprite(1, 4, 1)
					else:
						sprite_defender[1] = trocar_sprite(1, -5, 1)
			else:
				estado_player[1] = 11
				estado_stamina[1] = 0
				player2_sta = 0
				delay_p2 = time.clock()
				tempo_hitHard2 = delay_p2
				player2_hp -= dano
				barra_hp(2)
				if(lado_sprite[1] == 0):
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], 11, 1)
				else:
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], -12, 1)
				undraw(4, 2, lado_sprite[1])
		elif(estado_player[1] == 11 or estado_player[1] == 10):
			player2_hp -= dano
			barra_hp(2)
			delay_p2 = time.clock()
			if(player2_hp > 0 and estado_stamina[1] == 1):
				ls = lado_sprite[1]
				if(limite_mapa == 1):
					if(lado_sprite[1] == 1):
						ls = 1
						lado_sprite[1] = 0
					else:
						ls = 0
						lado_sprite[1] = 1
				estado_player[1] = 10
				velocidade_hitLeveAr2 = 8
				aux_hitLeveAr2 = 0.4
				undraw(e, 2, ls)
				if(lado_sprite[1] == 0):
					sprite_danoLeveAr[1] = trocar_sprite(0, 10, 1)
				else:
					sprite_danoLeveAr[1] = trocar_sprite(0, -11, 1)
			else:
				estado_player[1] = 11
				aux_hitHard2 = 0
				velocidade_hitHard2 = 6
				tempo_hitHard2 = delay_p2
				undraw(e, 2, lado_sprite[1])
				if(lado_sprite[1] == 0):
					sprite_danoHard[1] = trocar_sprite(0, 11, 1)
				else:
					sprite_danoHard[1] = trocar_sprite(0, -12, 1)

def levando_hitLeve(t1, t2, e1, e2):
	if(e1 == 9):
		if(lado_sprite[0] == 0):
			move_p1(-2,0)
		else:
			move_p1(2,0)
		if((time.clock() - t1 > 0.15) and sprite_danoLeve[0] == 1):
			if(lado_sprite[0] == 0):
				sprite_danoLeve[0] = trocar_sprite(sprite_danoLeve[0], 9, 0)
			else:
				sprite_danoLeve[0] = trocar_sprite(sprite_danoLeve[0], -10, 0)
		if(time.clock() - t1 > 0.45):
			draw_sprite(0, 1)
			undraw(9, 1, lado_sprite[0])
			estado_player[0] = 0
	elif(e1 == 10):
		global velocidade_hitLeveAr1
		global aux_hitLeveAr1
		global posicao_originalY
		aux = 0
		if(lado_sprite[0] == 0):
			move_p1(-4, velocidade_hitLeveAr1)
		else:
			move_p1(4, velocidade_hitLeveAr1)
		tempo = time.clock() - t1
		velocidade_hitLeveAr1 = velocidade_hitLeveAr1 - 0.5*(tempo)
		if(posicao_p1.getY() < posicao_originalY):
			draw_sprite(0, 1)
			undraw(10, 1, lado_sprite[0])
			move_p1(0, posicao_originalY - posicao_p1.getY())
			estado_player[0] = 0
			sprite_danoLeveAr[0] = 0
			aux_hitLeveAr1 = 0.4
			velocidade_hitLeveAr1 = 6
		if(tempo > 0.4):
			if(tempo - aux_hitLeveAr1 > 0.08 and sprite_danoLeveAr[0] != 0):
				aux = 1
				aux_hitLeveAr1 += 0.08
		if(aux == 1 and sprite_danoLeveAr[0] != 0):
			if(lado_sprite[0] == 0):
				sprite_danoLeveAr[0] = trocar_sprite(sprite_danoLeveAr[0], 10, 0)
			else:
				sprite_danoLeveAr[0] = trocar_sprite(sprite_danoLeveAr[0], -11, 0)
	if(e2 == 9):
		if(lado_sprite[1] == 0):
			move_p2(-2,0)
		else:
			move_p2(2,0)
		if((time.clock() - t2 > 0.15) and sprite_danoLeve[1] == 1):
			if(lado_sprite[1] == 0):
				sprite_danoLeve[1] = trocar_sprite(sprite_danoLeve[1], 9, 1)
			else:
				sprite_danoLeve[1] = trocar_sprite(sprite_danoLeve[1], -10, 1)
		if(time.clock() - t2 > 0.45):
			draw_sprite(0, 2)
			undraw(9, 2, lado_sprite[1])
			estado_player[1] = 0
	elif(e2 == 10):
		global velocidade_hitLeveAr2
		global aux_hitLeveAr2
		aux = 0
		if(lado_sprite[1] == 0):
			move_p2(-4, velocidade_hitLeveAr2)
		else:
			move_p2(4, velocidade_hitLeveAr2)
		tempo = time.clock() - t2
		velocidade_hitLeveAr2 = velocidade_hitLeveAr2 - 0.5*(tempo)
		if(posicao_p2.getY() < posicao_originalY):
			draw_sprite(0, 2)
			undraw(10, 2, lado_sprite[1])
			move_p2(0, posicao_originalY - posicao_p2.getY())
			estado_player[1] = 0
			sprite_danoLeveAr[1] = 0
			aux_hitLeveAr2 = 0.4
			velocidade_hitLeveAr2 = 6
		if(tempo > 0.4):
			if(tempo - aux_hitLeveAr2 > 0.08 and sprite_danoLeveAr[1] != 0):
				aux = 1
				aux_hitLeveAr2 += 0.08
		if(aux == 1 and sprite_danoLeveAr[1] != 0):
			if(lado_sprite[1] == 0):
				sprite_danoLeveAr[1] = trocar_sprite(sprite_danoLeveAr[1], 10, 1)
			else:
				sprite_danoLeveAr[1] = trocar_sprite(sprite_danoLeveAr[1], -11, 1)

def levando_hitHard(t1, t2, e1, e2):
	global end_game
	global velocidade_hitHard1
	global velocidade_hitHard2
	global tempo_hitHard1
	global tempo_hitHard2
	global aux_hitHard1
	global aux_hitHard2
	global tempo_getUp1
	global tempo_getUp2
	global velocidade_getUp1
	global velocidade_getUp2
	global player1_hp
	global player2_hp
	aux = t1
	if(e1 == 11):
		if(aux_hitHard1 == 0 or aux_hitHard1 == 1 or aux_hitHard1 == 2):
			if(lado_sprite[0] == 0):
				move_p1(-4, velocidade_hitHard1)
			else:
				move_p1(4, velocidade_hitHard1)
			tempo = time.clock() - tempo_hitHard1
			velocidade_hitHard1 = velocidade_hitHard1 - 0.4*(tempo)
		if(sprite_danoHard[0] == 6):
			aux_hitHard1 = 1
		if(posicao_p1.getY() < posicao_originalY and aux_hitHard1 == 1):
			aux_hitHard1 = 2
			move_p1(0, posicao_originalY - posicao_p1.getY())
			velocidade_hitHard1 = 2
			tempo_hitHard1 = time.clock()
			if(lado_sprite[0] == 0):
				sprite_danoHard[0] = trocar_sprite(sprite_danoHard[0], 11, 0)
			else:
				sprite_danoHard[0] = trocar_sprite(sprite_danoHard[0], -12, 0)
		if(posicao_p1.getY() < posicao_originalY and aux_hitHard1 == 2):
			aux_hitHard1 = 3
			move_p1(0, posicao_originalY - posicao_p1.getY())
		if(sprite_danoHard[0] == 0):
			aux_hitHard1 = 4
		if(sprite_danoHard[0] == 0 and aux_hitHard1 == 4):
			if(player1_hp > 0):
				get_up(0)
				undraw(11, 1, lado_sprite[0])
				tempo_getUp1 = time.clock()
				velocidade_getUp1 = 4
				estado_player[0] = 12
				sprite_danoHard[0] = 0
				aux_hitHard1 = 0
				velocidade_hitHard1 = 6
				aux = time.clock()
			else:
				end_game = 2
		if(sprite_danoHard[0] != 6 and aux_hitHard1 == 0 and sprite_danoHard[0] != 0):
			if(time.clock() - t1 > 0.15):
				if(lado_sprite[0] == 0):
					sprite_danoHard[0] = trocar_sprite(sprite_danoHard[0], 11, 0)
				else:
					sprite_danoHard[0] = trocar_sprite(sprite_danoHard[0], -12, 0)
				aux = time.clock()
		if(sprite_danoHard[0] != 0 and aux_hitHard1 == 3):
			if(time.clock() - t1 > 0.15):
				if(lado_sprite[0] == 0):
					sprite_danoHard[0] = trocar_sprite(sprite_danoHard[0], 11, 0)
				else:
					sprite_danoHard[0] = trocar_sprite(sprite_danoHard[0], -12, 0)
				aux = time.clock()
	if(e2 == 11):
		if(aux_hitHard2 == 0 or aux_hitHard2 == 1 or aux_hitHard2 == 2):
			if(lado_sprite[1] == 0):
				move_p2(-4, velocidade_hitHard2)
			else:
				move_p2(4, velocidade_hitHard2)
			tempo = time.clock() - tempo_hitHard2
			velocidade_hitHard2 = velocidade_hitHard2 - 0.4*(tempo)
		if(sprite_danoHard[1] == 6):
			aux_hitHard2 = 1
		if(posicao_p2.getY() < posicao_originalY and aux_hitHard2 == 1):
			aux_hitHard2 = 2
			move_p2(0, posicao_originalY - posicao_p2.getY())
			velocidade_hitHard2 = 2
			tempo_hitHard2 = time.clock()
			if(lado_sprite[1] == 0):
				sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], 11, 1)
			else:
				sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], -12, 1)
		if(posicao_p2.getY() < posicao_originalY and aux_hitHard2 == 2):
			aux_hitHard2 = 3
			move_p2(0, posicao_originalY - posicao_p2.getY())
		if(sprite_danoHard[1] == 0):
			aux_hitHard2 = 4
		if(sprite_danoHard[1] == 0 and aux_hitHard2 == 4):
			if(player2_hp > 0):
				get_up(1)
				undraw(11, 2, lado_sprite[1])
				tempo_getUp2 = time.clock()
				velocidade_getUp2 = 4
				estado_player[1] = 12
				sprite_danoHard[1] = 0
				aux_hitHard2 = 0
				velocidade_hitHard2 = 6
				return (aux, time.clock())
			else:
				end_game = 2
		if(sprite_danoHard[1] != 6 and aux_hitHard2 == 0 and sprite_danoHard[1] != 0):
			if(time.clock() - t2 > 0.15):
				if(lado_sprite[1] == 0):
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], 11, 1)
				else:
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], -12, 1)
				return (aux, time.clock())
		if(sprite_danoHard[1] != 0 and aux_hitHard2 == 3):
			if(time.clock() - t2 > 0.15):
				if(lado_sprite[1] == 0):
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], 11, 1)
				else:
					sprite_danoHard[1] = trocar_sprite(sprite_danoHard[1], -12, 1)
				return (aux, time.clock())
	return (aux, t2)

def action_getUp(t1, t2, e1, e2):
	global tempo_getUp1
	global tempo_getUp2
	global velocidade_getUp1
	global velocidade_getUp2
	aux = t1
	if(player1 != 4 and player1 != 5 and player1 != 6 and player1 != 3 and e1 == 12):
		if(sprite_getUp[0] > sprite_getUp_p1 or sprite_getUp[0] == 0):
			if(lado_sprite[0] == 0):
				move_p1(-1, velocidade_getUp1)
			else:
				move_p1(1, velocidade_getUp1)
			tempo = time.clock() - tempo_getUp1 + ((sprite_getUp_p1 - 1)* 0.1)
			velocidade_getUp1 = velocidade_getUp1 - 0.2*(tempo)
		if(posicao_p1.getY() < posicao_originalY and sprite_getUp[0] == 0):
			move_p1(0, posicao_originalY - posicao_p1.getY())
			draw_sprite(0,1)
			undraw(12,1,lado_sprite[0])
			estado_player[0] = 0
			aux = time.clock()				
		if(time.clock() - t1 > 0.1 and sprite_getUp[0] != 0):
			if(lado_sprite[0] == 0):
				sprite_getUp[0] = trocar_sprite(sprite_getUp[0], 12, 0)
			else:
				sprite_getUp[0] = trocar_sprite(sprite_getUp[0], -13, 0)
			aux = time.clock()
	elif((player1 == 4 or player1 == 5 or player1 == 6 or player1 == 3) and e1 == 12):
		if(sprite_getUp[0] == 0):
			draw_sprite(0,1)
			undraw(12,1,lado_sprite[0])
			estado_player[0] = 0
			aux = time.clock()
		if(time.clock() - t1 > 0.2 and sprite_getUp[0] != 0):
			if(lado_sprite[0] == 0):
				sprite_getUp[0] = trocar_sprite(sprite_getUp[0], 12, 0)
			else:
				sprite_getUp[0] = trocar_sprite(sprite_getUp[0], -13, 0)
			aux = time.clock()
	if(player2 != 4 and player2 != 5 and player2 != 6 and player2 != 3 and e2 == 12):
			if(sprite_getUp[1] > sprite_getUp_p2 or sprite_getUp[1] == 0):
				if(lado_sprite[1] == 0):
					move_p2(-1, velocidade_getUp2)
				else:
					move_p2(1, velocidade_getUp2)
				tempo = time.clock() - tempo_getUp2 + ((sprite_getUp_p2 - 1)* 0.1)
				velocidade_getUp2 = velocidade_getUp2 - 0.2*(tempo)
			if(posicao_p2.getY() < posicao_originalY and sprite_getUp[1] == 0):
				move_p2(0, posicao_originalY - posicao_p2.getY())
				draw_sprite(0,2)
				undraw(12,2,lado_sprite[1])
				estado_player[1] = 0
				return (aux, time.clock())		
			if(time.clock() - t2 > 0.1 and sprite_getUp[1] != 0):
				if(lado_sprite[1] == 0):
					sprite_getUp[1] = trocar_sprite(sprite_getUp[1], 12, 1)
				else:
					sprite_getUp[1] = trocar_sprite(sprite_getUp[1], -13, 1)
				return (aux, time.clock())
	if((player2 == 4 or player2 == 5 or player2 == 6 or player2 == 3) and e2 == 12):
		if(sprite_getUp[1] == 0):
			draw_sprite(0,2)
			undraw(12,2,lado_sprite[1])
			estado_player[1] = 0
			return (aux, time.clock())
		if(time.clock() - t2 > 0.2 and sprite_getUp[1] != 0):
			if(lado_sprite[1] == 0):
				sprite_getUp[1] = trocar_sprite(sprite_getUp[1], 12, 1)
			else:
				sprite_getUp[1] = trocar_sprite(sprite_getUp[1], -13, 1)
			return (aux, time.clock())
	return (aux, t2)

def action_jump(e, velocidade, jogador):
	global tempo_pulo_p1
	global tempo_pulo_p2
	global aux_pulo_p1
	global aux_pulo_p2
	global posicao_originalY
	aux = 0
	if(jogador == 1):
		if(e == 6):
			move_p1(0, velocidade)
			tempo = time.clock() - tempo_pulo_p1
			velocidade = velocidade - 1*(tempo)
			if(posicao_p1.getY() < posicao_originalY):
				draw_sprite(0, 1)
				undraw(6, 1, lado_sprite[0])
				move_p1(0, posicao_originalY - posicao_p1.getY())
				estado_player[0] = 0
				sprite_jump[0] = 0
				aux_pulo_p1 = 0
				return 12
			if(tempo - aux_pulo_p1 > 0.16):
				aux = 1
				aux_pulo_p1 += 0.16
			if(aux == 1):
				if(lado_sprite[0] == 0):
					sprite_jump[0] = trocar_sprite(sprite_jump[0], 6, 0)
				else:
					sprite_jump[0] = trocar_sprite(sprite_jump[0], -7, 0)
		return velocidade
	elif(jogador == 2):
		if(e == 6):
			move_p2(0, velocidade)
			tempo = time.clock() - tempo_pulo_p2
			velocidade = velocidade - 1*(tempo)
			if(posicao_p2.getY() < posicao_originalY):
				draw_sprite(0, 2)
				undraw(6, 2, lado_sprite[1])
				move_p2(0, posicao_originalY - posicao_p2.getY())
				estado_player[1] = 0
				sprite_jump[1] = 0
				aux_pulo_p2 = 0
				return 12
			if(tempo - aux_pulo_p2 > 0.16):
				aux = 1
				aux_pulo_p2 += 0.16
			if(aux == 1):
				if(lado_sprite[1] == 0):
					sprite_jump[1] = trocar_sprite(sprite_jump[1], 6, 1)
				else:
					sprite_jump[1] = trocar_sprite(sprite_jump[1], -7, 1)
		return velocidade

def action_soco(t1, t2, e1, e2):
	global sprite_dano_soco_p1
	global sprite_dano_soco_p2
	global dano_soco1
	global dano_soco2
	aux = t1
	if(e1 == 3):
		if(player1 == 6 and sprite_punch[0] == 3):
			if(lado_sprite[0] == 0):
				move_p1(5, 0)
			else:
				move_p1(-5, 0)
		if(sprite_punch[0] != sprite_dano_soco_p1):
			if(time.clock() - t1 > 0.07):
				if(sprite_punch[0] == sprite_dano_soco_p1 - 1):
					ponto_hit, topo_hitbox, base_hitbox = atualizaDadosInteracaoHitbox(posicao_p1, posicao_p2,1,p1_info[1],p1_info[0],estado_player[1])
					dano = checarHit(posicao_p1,posicao_p2,ponto_hit,p1_info[2],topo_hitbox,base_hitbox,p1_info[5])
					if(dano == 1):
						hit(2, dano_soco1, estado_player[1])
						som_hit(som, "soco")
				if(lado_sprite[0] == 0):
					sprite_punch[0] = trocar_sprite(sprite_punch[0], 3, 0)
				else:
					sprite_punch[0] = trocar_sprite(sprite_punch[0], -4, 0)
				aux = time.clock()
		else:
			if(time.clock() - t1 > 0.5):
				if(lado_sprite[0] == 0):
					sprite_punch[0] = trocar_sprite(sprite_punch[0], 3, 0)
				else:
					sprite_punch[0] = trocar_sprite(sprite_punch[0], -4, 0)
				aux = time.clock()
		if(sprite_punch[0] == 0 and time.clock() - t1 < 0.04):
			draw_sprite(0, 1)
			undraw(3, 1, lado_sprite[0])
			estado_player[0] = 0
	if(e2 == 3):
		if(player2 == 6 and sprite_punch[1] == 3):
			if(lado_sprite[1] == 0):
				move_p2(5, 0)
			else:
				move_p2(-5, 0)
		if(sprite_punch[1] != sprite_dano_soco_p2):
			if(time.clock() - t2 > 0.07):
				if(sprite_punch[1] == sprite_dano_soco_p2 - 1):
					ponto_hit, topo_hitbox, base_hitbox = atualizaDadosInteracaoHitbox(posicao_p1, posicao_p2,2,p1_info[1],p1_info[0],estado_player[0])
					dano = checarHit(posicao_p1,posicao_p2,ponto_hit,p1_info[4],topo_hitbox,base_hitbox,p1_info[5])
					if(dano == 1):
						hit(1, dano_soco2, estado_player[0])
						som_hit(som, "soco")
				if(lado_sprite[1] == 0):
					sprite_punch[1] = trocar_sprite(sprite_punch[1], 3, 1)
				else:
					sprite_punch[1] = trocar_sprite(sprite_punch[1], -4, 1)
				return aux, time.clock()
		else:
			if(time.clock() - t2 > 0.5):
				if(lado_sprite[1] == 0):
					sprite_punch[1] = trocar_sprite(sprite_punch[1], 3, 1)
				else:
					sprite_punch[1] = trocar_sprite(sprite_punch[1], -4, 1)
				return aux, time.clock()
		if(sprite_punch[1] == 0 and time.clock() - t2 < 0.04):
			draw_sprite(0, 2)
			undraw(3, 2, lado_sprite[1])
			estado_player[1] = 0
			return aux, t2
	return aux, t2

def action_chute(t1, t2, e1, e2):
	global sprite_dano_chute_p1
	global sprite_dano_chute_p2
	global dano_chute1
	global dano_chute2
	aux = t1
	aux_p1 = 0
	if(e1 == 7):
		if((player1 == 2 and sprite_chute[0] == 1) or (player1 == 4 and sprite_chute[0] < 4) or (player1 == 5 and sprite_chute[0] < 3) or(player1 == 6 and sprite_chute[0] == 3)):
			if(lado_sprite[0] == 0):
				move_p1(5, 0)
			else:
				move_p1(-5, 0)
		if(sprite_chute[0] != sprite_dano_chute_p1):
			if(time.clock() - t1 > 0.07):
				if(sprite_chute[0] == 0):
					draw_sprite(0, 1)
					undraw(7, 1, lado_sprite[0])
					estado_player[0] = 0
					sprite_chute[0] = 0
					aux_p1 = 1
				if(sprite_chute[0] == sprite_dano_chute_p1 - 1):
					ponto_hit, topo_hitbox, base_hitbox = atualizaDadosInteracaoHitbox(posicao_p1, posicao_p2,1,p1_info[3],p1_info[0],estado_player[1])
					dano = checarHit(posicao_p1,posicao_p2,ponto_hit,p1_info[4],topo_hitbox,base_hitbox,p1_info[5])
					if(dano == 1):
						hit(2, dano_chute1, estado_player[1])
						som_hit(som, "chute")
				if(aux_p1 == 0):
					if(lado_sprite[0] == 0):
						sprite_chute[0] = trocar_sprite(sprite_chute[0], 7, 0)
					else:
						sprite_chute[0] = trocar_sprite(sprite_chute[0], -8, 0)
					aux = time.clock()
		else:
			if(time.clock() - t1 > 0.5):
				if(lado_sprite[0] == 0):
					sprite_chute[0] = trocar_sprite(sprite_chute[0], 7, 0)
				else:
					sprite_chute[0] = trocar_sprite(sprite_chute[0], -8, 0)
				aux = time.clock()
	if(e2 == 7):
		if((player2 == 2 and sprite_chute[1] == 1) or (player2 == 4 and sprite_chute[1] < 4) or (player2 == 5 and sprite_chute[1] < 3) or(player2 == 6 and sprite_chute[1] == 3)):
			if(lado_sprite[1] == 0):
				move_p2(5, 0)
			else:
				move_p2(-5, 0)
		if(sprite_chute[1] != sprite_dano_chute_p2):
			if(time.clock() - t2 > 0.07):
				if(sprite_chute[1] == 0):
					draw_sprite(0, 2)
					undraw(7, 2, lado_sprite[1])
					estado_player[1] = 0
					sprite_chute[1] = 0
					return aux, t2
				if(sprite_chute[1] == sprite_dano_chute_p2 - 1):
					ponto_hit, topo_hitbox, base_hitbox = atualizaDadosInteracaoHitbox(posicao_p1, posicao_p2,2,p1_info[3],p1_info[0],estado_player[0])
					dano = checarHit(posicao_p1,posicao_p2,ponto_hit,p1_info[4],topo_hitbox,base_hitbox,p1_info[5])
					if(dano == 1):
						hit(1, dano_chute2, estado_player[0])
						som_hit(som, "chute")
				if(lado_sprite[1] == 0):
					sprite_chute[1] = trocar_sprite(sprite_chute[1], 7, 1)
				else:
					sprite_chute[1] = trocar_sprite(sprite_chute[1], -8, 1)
				return aux, time.clock()
		else:
			if(time.clock() - t2 > 0.5):
				if(lado_sprite[1] == 0):
					sprite_chute[1] = trocar_sprite(sprite_chute[1], 7, 1)
				else:
					sprite_chute[1] = trocar_sprite(sprite_chute[1], -8, 1)
				return aux, time.clock()
	return aux, t2

def action_especial1(t1, t2, e1, e2):
	global sprite_dano_especial1_p1
	global sprite_dano_especial1_p2
	global tempo_especial_p1
	global tempo_especial_p2
	global tempo_energia1_p1
	global tempo_energia1_p2
	aux = t1
	if(e1 == 8):
		if(sprite_especial1[0] != sprite_dano_especial1_p1):
			if(time.clock() - t1 > 0.05):
				if(lado_sprite[0] == 0):
					sprite_especial1[0] = trocar_sprite(sprite_especial1[0], 8, 0)
				else:
					sprite_especial1[0] = trocar_sprite(sprite_especial1[0], -9, 0)
				aux = time.clock()
		else:
			if(especial_ativo[0] == 0 and hitespecial1_ativo[0] == 0):
				energia_1(1)
				tempo_energia1_p1 = time.clock()
				especial_ativo[0] = 1
			if(time.clock() - t1 > 0.5):
				if(lado_sprite[0] == 0):
					sprite_especial1[0] = trocar_sprite(sprite_especial1[0], 8, 0)
				else:
					sprite_especial1[0] = trocar_sprite(sprite_especial1[0], -9, 0)
				aux = time.clock()
		if(sprite_especial1[0] == 0 and time.clock() - t1 < 0.04):
			sprite_especial1[0] = 0
			draw_sprite(0, 1)
			undraw(8, 1, lado_sprite[0])
			estado_player[0] = 0
	if(e2 == 8):
		if(sprite_especial1[1] != sprite_dano_especial1_p2):
			if(time.clock() - t2 > 0.05):
				if(lado_sprite[1] == 0):
					sprite_especial1[1] = trocar_sprite(sprite_especial1[1], 8, 1)
				else:
					sprite_especial1[1] = trocar_sprite(sprite_especial1[1], -9, 1)
				return aux, time.clock()
		else:
			if(especial_ativo[1] == 0 and hitespecial1_ativo[1] == 0):
				energia_1(2)
				tempo_energia1_p2 = time.clock()
				especial_ativo[1] = 1
			if(time.clock() - t2 > 0.5):
				if(lado_sprite[1] == 0):
					sprite_especial1[1] = trocar_sprite(sprite_especial1[1], 8, 1)
				else:
					sprite_especial1[1] = trocar_sprite(sprite_especial1[1], -9, 1)
				return aux, time.clock()
		if(sprite_especial1[1] == 0 and time.clock() - t2 < 0.04):
			sprite_especial1[1] = 0
			draw_sprite(0, 2)
			undraw(8, 2, lado_sprite[1])
			estado_player[1] = 0
			return aux, t2
	return aux, t2

def move_especial(jogador):
	if(lado_energia[jogador] == 0):
		c1 = 0
		while(c1 < len(especial[jogador])):
			c2 = 0
			while(c2 < len(especial[jogador][c1])):
				especial[jogador][c1][c2].move(10,0)
				c2 += 1
			c1 += 1
	else:
		c1 = 0
		while(c1 < len(especial[jogador])):
			c2 = 0
			while(c2 < len(especial[jogador][c1])):
				especial[jogador][c1][c2].move(-10,0)
				c2 += 1
			c1 += 1	

def especial_end(sprite, jogador):
	if(lado_energia[jogador] == 0):
		if((especial[jogador][0][0].getAnchor()).getX() > 960):
			if(jogador == 0):
				undraw_especial(0)
				return 0
			if(jogador == 1):
				undraw_especial(1)
				return 0
		return 1
	else:
		if((especial[jogador][-1][0].getAnchor()).getX() < 0):
			if(jogador == 0):
				undraw_especial(0)
				return 0
			if(jogador == 1):
				undraw_especial(1)
				return 0
		return 1

def especial_move_to_player(jogador, lado_energia):
	global especialAltura_p1
	global especialAltura_p2
	if(jogador == 1):
		if(lado_energia == 0):
			especial[0] = list(posiciona_especial(sprites_especial_p1, Point(posicao_p1.getX() + 100, especialAltura_p1)))
		else:
			especial[0] = list(posiciona_especial(sprites_especial_p1, Point(posicao_p1.getX() - 100, especialAltura_p1)))
	if(jogador == 2):
		if(lado_energia == 0):
			especial[1] = list(posiciona_especial(sprites_especial_p2, Point(posicao_p2.getX() + 100, especialAltura_p2)))
		else:
			especial[1] = list(posiciona_especial(sprites_especial_p2, Point(posicao_p2.getX() - 100, especialAltura_p2)))

def verifica_hitespecial1(t, j):
	if(hitespecial1_ativo[j] == 1):
		if(time.clock() - t > 0.08):
			if(sprite_ener1hit[j] == 0):
				hitespecial1_ativo[j] = 0
				undraw_especial(j)
				return t
			if(lado_energia[j] == 0):
				sprite_ener1hit[j] = trocar_especial(sprite_ener1hit[j], 1, j)
			else:
				sprite_ener1hit[j] = trocar_especial(sprite_ener1hit[j], -2, j)
			return time.clock()
	return t
	

def trocar_sprite(n_sprites, e, jogador):
	if(n_sprites == 0):
		player[jogador][e][n_sprites].draw(janela)
		player[jogador][e][len(player[jogador][e])-1].undraw()
		return 1
	elif(n_sprites == (len(player[jogador][e])-1)):
		player[jogador][e][n_sprites].draw(janela)
		player[jogador][e][n_sprites -1].undraw()
		return 0
	else:
		player[jogador][e][n_sprites].draw(janela)
		player[jogador][e][n_sprites - 1].undraw()
		return n_sprites + 1

def trocar_especial(n_sprites, e, jogador):
	if(n_sprites == 0):
		especial[jogador][e][n_sprites].draw(janela)
		especial[jogador][e][len(especial[jogador][e])-1].undraw()
		return 1
	elif(n_sprites == (len(especial[jogador][e])-1)):
		especial[jogador][e][n_sprites].draw(janela)
		especial[jogador][e][n_sprites -1].undraw()
		return 0
	else:
		especial[jogador][e][n_sprites].draw(janela)
		especial[jogador][e][n_sprites - 1].undraw()
		return n_sprites + 1

def intro_sprite(c_intro, t_intro):
	if(time.clock() - t_intro > 0.15):
		if(c_intro < len(p1_intro)):
			p1_intro[c_intro - 1].undraw()
			p1_intro[c_intro].draw(janela)
		if(c_intro < len(p2_intro)):
			p2_intro[c_intro - 1].undraw()
			p2_intro[c_intro].draw(janela)
		return (c_intro + 1, time.clock())
	return (c_intro, t_intro)

def winner_sprite(n_sprites, jogador):
	if(n_sprites == 0):
		p_winner[jogador][n_sprites].draw(janela)
		p_winner[jogador][len(p_winner[jogador])-1].undraw()
		return 1
	elif(n_sprites == (len(p_winner[jogador])-1)):
		p_winner[jogador][n_sprites].draw(janela)
		p_winner[jogador][n_sprites -1].undraw()
		return 0
	else:
		p_winner[jogador][n_sprites].draw(janela)
		p_winner[jogador][n_sprites - 1].undraw()
		return n_sprites + 1

def barra_hp(player):
	global player1_hp
	global player2_hp
	global BarraHP1
	global BarraHP2
	if(player == 1):
		BarraHP1.undraw()
		if(player1_hp > 0):
			BarraHP1 = Rectangle(Point(20, 487), Point((player1_hp*4) + 20, 530))
			BarraHP1.setFill("yellow")
			BarraHP1.draw(janela)
	if(player == 2):
		BarraHP2.undraw()
		if(player2_hp > 0):
			BarraHP2 = Rectangle(Point(940, 487), Point(940 - (player2_hp*4), 530))
			BarraHP2.setFill("yellow")
			BarraHP2.draw(janela)

def barra_stamina(player):
	global player1_sta
	global player2_sta
	global BarraSTA1
	global BarraSTA2
	if(player == 1):
		BarraSTA1.undraw()
		if(player1_sta > 0 and estado_stamina[0] == 1):
			BarraSTA1 = Rectangle(Point(20, 460), Point((player1_sta*2) + 20, 484))
			BarraSTA1.setFill("green")
			BarraSTA1.draw(janela)
		if(player1_sta > 0 and estado_stamina[0] == 0):
			BarraSTA1 = Rectangle(Point(20, 460), Point((player1_sta*2) + 20, 484))
			BarraSTA1.setFill("red")
			BarraSTA1.draw(janela)		
	if(player == 2):
		BarraSTA2.undraw()
		if(player2_sta > 0 and estado_stamina[1] == 1):
			BarraSTA2 = Rectangle(Point(940, 460), Point(940 - (player2_sta*2), 484))
			BarraSTA2.setFill("green")
			BarraSTA2.draw(janela)
		if(player2_sta > 0 and estado_stamina[1] == 0):
			BarraSTA2 = Rectangle(Point(940, 460), Point(940 - (player2_sta*2), 484))
			BarraSTA2.setFill("red")
			BarraSTA2.draw(janela)

def barra_ki(player):
	global player1_Ki
	global player2_Ki
	global BarraKI1
	global BarraKI2
	if(player == 1):
		BarraKI1.undraw()
		if(player1_Ki > 0):
			BarraKI1 = Rectangle(Point(220, 460), Point((player1_Ki*2) + 220, 484))
			BarraKI1.setFill("Blue")
			BarraKI1.draw(janela)
	if(player == 2):
		BarraKI2.undraw()
		if(player2_Ki > 0):
			BarraKI2 = Rectangle(Point(740, 460), Point(740 - (player2_Ki*2), 484))
			BarraKI2.setFill("Blue")
			BarraKI2.draw(janela)

def aumenta_energia():
	global player1_Ki
	global player2_Ki
	if(player1_Ki < 100):
		player1_Ki += 0.01
		barra_ki(1)
	else:
		player1_Ki = 100
		barra_ki(1)
	if(player2_Ki < 100):
		player2_Ki += 0.01
		barra_ki(2)
	else:
		player2_Ki = 100
		barra_ki(2)

def verifica_defesa():
	if(estado_player[0] == 4):
		if(sprite_defender[0] == 0):
			if(estado_player[1] == 0 and hitespecial1_ativo[1] == 0):
				if(lado_sprite[0] == 0):
					sprite_defender[0] = trocar_sprite(0, 4, 0)
				else:
					sprite_defender[0] = trocar_sprite(0, -5, 0)
	if(estado_player[1] == 4):
		if(sprite_defender[1] == 0):
			if(estado_player[0] == 0 and hitespecial1_ativo[0] == 0):
				if(lado_sprite[1] == 0):
					sprite_defender[1] = trocar_sprite(0, 4, 1)
				else:
					sprite_defender[1] = trocar_sprite(0, -5, 1)

def verifica_stamina():
	global player1_sta
	global player2_sta
	global lost_stamina1
	global lost_stamina2
	if(estado_stamina[0] == 1):
		if(player1_sta < 100 and player1_sta > 0):
			player1_sta += 0.1
			barra_stamina(1)
	else:
		if(estado_player[0] != 9 and estado_player[0] != 10 and estado_player[0] != 11 and lost_stamina1 == 0 and player1_sta < 0):
			hit(1, 0, estado_player[0])
			lost_stamina1 = 1
		player1_sta += 0.25
		barra_stamina(1)
		if(player1_sta > 100):
			player1_sta = 100
			lost_stamina1 = 0
			estado_stamina[0] = 1
			barra_stamina(1)
	if(player1_sta < 0):
		estado_stamina[0] = 0
	if(estado_stamina[1] == 1):
		if(player2_sta < 100 and player2_sta > 0):
			player2_sta += 0.1
			barra_stamina(2)
	else:
		if(estado_player[1] != 9 and estado_player[1] != 10 and estado_player[1] != 11 and lost_stamina2 == 0 and player2_sta < 0):
			hit(2, 0, estado_player[1])
			lost_stamina2 = 1
		player2_sta += 0.25
		barra_stamina(2)
		if(player2_sta > 100):
			player2_sta = 100
			lost_stamina2 = 0
			estado_stamina[1] = 1
			barra_stamina(2)
	if(player2_sta < 0):
		estado_stamina[1] = 0

def verificar_sprite_especial(t, j):
	if(time.clock() - t > 0.1):
		if(especial_ativo[j] == 1):
			if(lado_energia[j] == 0):
				sprite_energia1[j] = trocar_especial(sprite_energia1[j], 0, j)
			else:
				sprite_energia1[j] = trocar_especial(sprite_energia1[j], -1, j)
		return time.clock()
	else:
		return t

def verificar_sprite(t, j, p):
	if(time.clock() - t > 0.15):
		if(estado_player[j] == 0):
			if(lado_sprite[j] == 0):
				sprite_parado[j] = trocar_sprite(sprite_parado[j], 0, j)
			else:
				sprite_parado[j] = trocar_sprite(sprite_parado[j], -1, j)
		if(p != 4 and p!= 5 and p!= 3 and p!= 6):
			if(estado_player[j] == 1):
				if(lado_sprite[j] == 0):
					sprite_walkDireita[j] = trocar_sprite(sprite_walkDireita[j], 1, j)
				else:
					sprite_walkDireita[j] = trocar_sprite(sprite_walkDireita[j], -2, j)
			elif(estado_player[j] == 2):
				if(lado_sprite[j] == 0):
					sprite_walkEsquerda[j] = trocar_sprite(sprite_walkEsquerda[j], 2, j)
				else:
					sprite_walkEsquerda[j] = trocar_sprite(sprite_walkEsquerda[j], -3, j)
		else:
			if(estado_player[j] == 1 and sprite_walkDireita[j] == 1):
				if(lado_sprite[j] == 0):
					sprite_walkDireita[j] = trocar_sprite(sprite_walkDireita[j], 1, j)
				else:
					sprite_walkDireita[j] = trocar_sprite(sprite_walkDireita[j], -2, j)
			elif(estado_player[j] == 2 and sprite_walkEsquerda[j] == 1):
				if(lado_sprite[j] == 0):
					sprite_walkEsquerda[j] = trocar_sprite(sprite_walkEsquerda[j], 2, j)
				else:
					sprite_walkEsquerda[j] = trocar_sprite(sprite_walkEsquerda[j], -3, j)	
		return time.clock()
	else:
		return t

def trocar_lado(p1, p2):
	if(p1 - p2 <= 0):
		if(lado_sprite[0] == 1):
			if(estado_player[0] == 0 or estado_player[0] == 1 or estado_player[0] == 2 or estado_player[0] == 6 or estado_player[0] == 4 or estado_player[0] == 5):
				lado_sprite[0] = 0
				draw_sprite(estado_player[0], 1)
				undraw(estado_player[0], 1, 1)
				janela.update()
		if(lado_sprite[1] == 0):
			if(estado_player[1] == 0 or estado_player[1] == 1 or estado_player[1] == 2 or estado_player[1] == 6 or estado_player[1] == 4 or estado_player[1] == 5):
				lado_sprite[1] = 1
				draw_sprite(estado_player[1], 2)
				undraw(estado_player[1], 2, 0)
				janela.update()
	else:
		if(lado_sprite[0] == 0):
			if(estado_player[0] == 0 or estado_player[0] == 1 or estado_player[0] == 2 or estado_player[0] == 6 or estado_player[0] == 4 or estado_player[0] == 5):
				lado_sprite[0] = 1
				draw_sprite(estado_player[0], 1)
				undraw(estado_player[0], 1, 0)
				janela.update()
		if(lado_sprite[1] == 1):
			if(estado_player[1] == 0 or estado_player[1] == 1 or estado_player[1] == 2 or estado_player[1] == 6 or estado_player[1] == 4 or estado_player[1] == 5):
				lado_sprite[1] = 0
				draw_sprite(estado_player[1], 2)
				undraw(estado_player[1], 2, 1)
				janela.update()

def verifica_tecla(key, e, t, jogador):
	if(e == 1 or e == 2 or e == 4 or e == 5):
		if(key != [] or (4 in key)):
			return time.clock()
		if(time.clock() - t > 0.08):
			if(jogador == 1):
				draw_sprite(0, 1)
				estado_player[0] = 0
				undraw(e, jogador, lado_sprite[0])
			else:
				draw_sprite(0, 2)
				estado_player[1] = 0
				undraw(e, jogador, lado_sprite[1])
			return t
	return t

def atualizaDadosInteracaoHitbox(p1, p2,player,tamanho_hit,altura_personagem,estado):
    if player==1:
        if p2.getX()>p1.getX():
            if estado!=5: #se estado = 5, significa que o personagem esta agachado
                ponto_hit = p1.getX() + tamanho_hit
                topo_hitbox = p2.getY() + (altura_personagem/2) #do centro ate o topo da cabeca
                base_hitbox = p2.getY() - (altura_personagem/2) #do centro ate os pes
            else:
                ponto_hit = p1.getX() + tamanho_hit #do meio do sprite ate a ponta do punho ou pe
                topo_hitbox = p2.getY() - 10 #o centro nesse caso e a cabeca
                base_hitbox = p2.getY() - (altura_personagem/2) #do centro ate a base da hitbox       
        if p1.getX()>=p2.getX():
            if estado!=5:
                ponto_hit = p1.getX() - tamanho_hit #comprimento do tamanho ou braço
                topo_hitbox = p2.getY() + (altura_personagem/2) #do centro ate o topo da cabeca
                base_hitbox = p2.getY() - (altura_personagem/2) #do centro ate a base da hitbox
            else:
                ponto_hit = p1.getX() - tamanho_hit #comprimento do tamanho ou braço
                topo_hitbox = p2.getY() - 10 #do centro ate o topo da cabeca
                base_hitbox = p2.getY() - (altura_personagem/2) #do centro ate a base da hitbox
    	return ponto_hit,topo_hitbox,base_hitbox
    if player==2:
        if p2.getX()>p1.getX():
            if estado!=5: #se estado = 5, significa que o personagem esta agachado
                ponto_hit = p1.getX() + tamanho_hit
                topo_hitbox = p1.getY() + (altura_personagem/2) #do centro ate o topo da cabeca
                base_hitbox = p1.getY() - (altura_personagem/2) #do centro ate os pes
            else:
                ponto_hit = p1.getX() + tamanho_hit #do meio do sprite ate a ponta do punho ou pe
                topo_hitbox = p1.getY() - 10 #o centro nesse caso e a cabeca
                base_hitbox = p1.getY() - (altura_personagem/2) #do centro ate a base da hitbox       
        if p1.getX()>=p2.getX():
            if estado!=5:
                ponto_hit = p1.getX() - tamanho_hit #comprimento do tamanho ou braço
                topo_hitbox = p1.getY() + (altura_personagem/2) #do centro ate o topo da cabeca
                base_hitbox = p1.getY() - (altura_personagem/2) #do centro ate a base da hitbox
            else:
                ponto_hit = p1.getX() - tamanho_hit #comprimento do tamanho ou braço
                topo_hitbox = p1.getY() - 10 #do centro ate o topo da cabeca
                base_hitbox = p1.getY() - (altura_personagem/2) #do centro ate a base da hitbox
	return ponto_hit,topo_hitbox,base_hitbox 

def checarHit(p1, p2,ponto_hit,altura_hit,altura_hitbox,base_hitbox,distancia_meio_ate_fim_hitbox):
    if p2.getX()>p1.getX():
        distanciaX = (p2.getX()-distancia_meio_ate_fim_hitbox)-ponto_hit 
        distanciaTopoHitbox = altura_hitbox - altura_hit
        distanciaBaseHitbox = altura_hit - base_hitbox
        if (distanciaX<0) and (distanciaTopoHitbox>0 and distanciaBaseHitbox>0):
            return 1
        else:
            return 0
    elif p1.getX()>p2.getX():
        distanciaX = (p2.getX()+distancia_meio_ate_fim_hitbox)-ponto_hit #se a distancia da mao ou pe do boneco for 
        distanciaTopoHitbox = altura_hitbox - altura_hit
        distanciaBaseHitbox = altura_hit - base_hitbox
        if (distanciaX>0) and (distanciaTopoHitbox>0 and distanciaBaseHitbox>0):
            return 1
        else:
            return 0

def move_mapa(pm):
	global limite_mapa
	if(pm < 0):		
		if((fundo.getAnchor()).getX() > Limite_mapa_d):
			limite_mapa = 0
			fundo.move(pm,0)
			return 1
		limite_mapa = 1
		return 0
	else:
		if((fundo.getAnchor()).getX() < Limite_mapa_e):
			limite_mapa = 0
			fundo.move(pm,0)
			return 1
		limite_mapa = 1
		return 0		

def reiniciaRound(e1, e2):
	global tempo_getUp1
	global tempo_getUp2
	global velocidade_getUp1
	global velocidade_getUp2
	global delay_p1
	global delay_p2
	if(e1 == 11):
		get_up(0)
		undraw(11, 1, lado_sprite[0])
		tempo_getUp1 = time.clock()
		velocidade_getUp1 = 4
		estado_player[0] = 12
		delay_p1 = time.clock()
	elif(e2 == 11):
		get_up(1)
		undraw(11, 2, lado_sprite[1])
		tempo_getUp2 = time.clock()
		velocidade_getUp2 = 4
		estado_player[1] = 12
		delay_p2 = time.clock()

def restart_levanta(e1, e2):
	global reinicia_round
	if(e1 == 0 and e2 == 0):
		reinicia_round = 2

def move_restartRound(e1, e2):
	global reinicia_round
	global posicao_original_X1
	global posicao_original_X2
	if(posicao_p1.getX() > posicao_original_X1):
		if(posicao_p1.getX() - posicao_original_X1 < 6):
			if(e1 != 2):
				draw_sprite(2,1)
				undraw(e1, 1, lado_sprite[0])
				estado_player[0] = 2
			move_p1(-1,0)
		else:
			if(e1 != 2):
				draw_sprite(2,1)
				undraw(e1, 1, lado_sprite[0])
				estado_player[0] = 2
			move_p1(-6,0)
	if(posicao_p1.getX() < posicao_original_X1):
		if(posicao_original_X1 - posicao_p1.getX() < 6):
			if(e1 != 1):
				draw_sprite(1,1)
				undraw(e1, 1, lado_sprite[0])
				estado_player[0] = 1
			move_p1(1,0)
		else:
			if(e1 != 1):
				draw_sprite(1,1)
				undraw(e1, 1, lado_sprite[0])
				estado_player[0] = 1
			move_p1(6,0)
	if(posicao_p1.getX() == posicao_original_X1):
		if(e1 != 0):
			draw_sprite(0, 1)
			undraw(e1, 1, lado_sprite[0])
			estado_player[0] = 0
	if(posicao_p2.getX() > posicao_original_X2):
		if(posicao_p2.getX() - posicao_original_X2 < 6):
			if(e2 != 2):
				draw_sprite(2,2)
				undraw(e2, 2, lado_sprite[1])
				estado_player[1] = 2
			move_p2(-1,0)
		else:
			if(e2 != 2):
				draw_sprite(2,2)
				undraw(e2, 2, lado_sprite[1])
				estado_player[1] = 2
			move_p2(-6,0)
	if(posicao_p2.getX() < posicao_original_X2):
		if(posicao_original_X2 - posicao_p2.getX() < 6):
			if(e2 != 1):
				draw_sprite(1,2)
				undraw(e2, 2, lado_sprite[1])
				estado_player[1] = 1
			move_p2(1,0)
		else:
			if(e2 != 1):
				draw_sprite(1,2)
				undraw(e1, 2, lado_sprite[1])
				estado_player[1] = 1
			move_p2(6,0)
	if(posicao_p2.getX() == posicao_original_X2):
		if(e2 != 0):
			draw_sprite(0, 2)
			undraw(e2, 2, lado_sprite[1])
			estado_player[1] = 0
	if(posicao_p1.getX() == posicao_original_X1 and posicao_p2.getX() == posicao_original_X2 and estado_player[0] == 0 and estado_player[1] == 0):
		reinicia_round = 0

def som_ambiente(numero_mapa):
	if som == True:
		if(numero_mapa == 1):
		    pygame.mixer.music.load("music/stage/punk.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 2):
		    pygame.mixer.music.load("music/stage/bonito_tarde.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 3):
		    pygame.mixer.music.load("music/stage/port.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 4):
		    pygame.mixer.music.load("music/stage/air_crystal.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 5):
		    pygame.mixer.music.load("music/stage/tribal.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 6):
		    pygame.mixer.music.load("music/stage/south_korea.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 7):
		    pygame.mixer.music.load("music/stage/guile_theme.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 8):
		    pygame.mixer.music.load("music/stage/graveyard.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 9):
		    pygame.mixer.music.load("music/stage/kids.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 10):
		    pygame.mixer.music.load("music/stage/y_train.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 11):
		    pygame.mixer.music.load("music/stage/riot.mp3")
		    pygame.mixer.music.play(-1)
		elif(numero_mapa == 12):
		    pygame.mixer.music.load("music/stage/santana.mp3")
		    pygame.mixer.music.play(-1)
	    
	else:
		return 0

def som_hit(som,tipo_de_hit):
	if som == True:
	    if(tipo_de_hit == 'soco'):
	        efeito = pygame.mixer.Sound('music/hit/som_hit_universal_soco.ogg')
	        efeito.play()
	    if(tipo_de_hit == 'chute'):
		    efeito = pygame.mixer.Sound('music/hit/som_hit_universal_chute.ogg')
		    efeito.play()
	    if(tipo_de_hit == 'especial1'):
		    efeito = pygame.mixer.Sound('music/hit/som_hit_universal_magia.ogg')
		    efeito.play()
		    return 1

def som_estado(player,personagem,estado):
	print player,personagem,estado
	if som == True:
	    if player == 1:
	        if personagem == 1:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/ryu/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/ryu/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/ryu/hadouken_ryu.ogg')
		            efeito3.play()
		        return 0
	        if personagem == 2:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/ken/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/ken/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound("music/ken/hadouken_ken.ogg")
		            efeito3.play()
		        return 0
	        if personagem == 3:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/bison/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/bison/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/bison/magia.ogg')
		            efeito3.play()
		        return 0
	        if personagem == 4:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/goku/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/goku/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/goku/magia.ogg')
		            efeito3.play()
		        return 0
	        if personagem == 5:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/vegeta/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/vegeta/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/vegeta/vegeta_magia.ogg')
		            efeito3.play()
		        return 0
	        if personagem == 6:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/freeza/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/freeza/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/freeza/freeza_magia.ogg')
		            efeito3.play()
		        return 0
	    if player == 2:
	        if personagem == 1:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/ryu/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/ryu/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound("music/ryu/hadouken_ryu.ogg")
		            efeito3.play()
		        return 0
	        if personagem == 2:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/ken/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/ken/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound("music/ken/hadouken_ken.ogg")
		            efeito3.play()
		        return 0
	        if personagem == 3:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/bison/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/bison/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/bison/magia.ogg')
		            efeito3.play()
		        return 0
	        if personagem == 4:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/goku/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/goku/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/goku/magia.ogg')
		            efeito3.play()
		        return 0
	        if personagem == 5:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/vegeta/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/vegeta/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/vegeta/vegeta_magia.ogg')
		            efeito3.play()
		        return 0
	        if personagem == 6:
		        if(estado == 1):
		            efeito = pygame.mixer.Sound("music/freeza/soco.ogg")
		            efeito.play()
		            return 0
		        if(estado == 2):
		            efeito2 = pygame.mixer.Sound("music/freeza/soco.ogg")
		            efeito2.play()
		            return 0
		        if(estado == 3):
		            efeito3 = pygame.mixer.Sound('music/freeza/freeza_magia.ogg')
		            efeito3.play()
		        return 0

def criar_sprite_intro(p):
	sprites = []
	if(p == 1):
		arq = open("fighters/ryu/Ryu_1/ryu_intro_p1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 10):
		arq = open("fighters/ryu/Ryu_1/ryu_intro_p2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 2):
		arq = open("fighters/ken/ken_1/ken_intro_p1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 20):
		arq = open("fighters/ken/ken_1/ken_intro_p2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 3):
		arq = open("fighters/M.Bison/M.Bison_1/M.Bison_intro1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 30):
		arq = open("fighters/M.Bison/M.Bison_1/M.Bison_intro2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 4):
		arq = open("fighters/Goku_base/goku_1/goku_intro_p1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 40):
		arq = open("fighters/Goku_base/goku_1/goku_intro_p2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 5):
		arq = open("fighters/Vegeta/vegeta_1/vegeta_intro1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 50):
		arq = open("fighters/Vegeta/vegeta_1/vegeta_intro2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 6):
		arq = open("fighters/Freeza/freeza_1/freeza_intro1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites
	elif(p == 60):
		arq = open("fighters/Freeza/freeza_1/freeza_intro2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites.append(linhas[c].replace("\n", ""))
			c += 1
		return sprites

def aux_criar_sprites_winner(p):
	sprites = []
	sprites_d = []
	sprites_e = []	
	if(p == 1):
		arq = open("fighters/ryu/Ryu_1/ryu_win_d.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_d.append(linhas[c].replace("\n", ""))
			c += 1
		arq = open("fighters/ryu/Ryu_1/ryu_win_e.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_e.append(linhas[c].replace("\n", ""))
			c += 1
		sprites.append(sprites_d)
		sprites.append(sprites_e)
		return sprites
	if(p == 2):
		arq = open("fighters/ken/ken_1/ken_win_d.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_d.append(linhas[c].replace("\n", ""))
			c += 1
		arq = open("fighters/ken/ken_1/ken_win_e.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_e.append(linhas[c].replace("\n", ""))
			c += 1
		sprites.append(sprites_d)
		sprites.append(sprites_e)
		return sprites
	if(p == 3):
		arq = open("fighters/M.Bison/M.Bison_1/M.Bison_win1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_d.append(linhas[c].replace("\n", ""))
			c += 1
		arq = open("fighters/M.Bison/M.Bison_1/M.Bison_win2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_e.append(linhas[c].replace("\n", ""))
			c += 1
		sprites.append(sprites_d)
		sprites.append(sprites_e)
		return sprites
	if(p == 4):
		arq = open("fighters/Goku_base/goku_1/goku_win_d.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_d.append(linhas[c].replace("\n", ""))
			c += 1
		arq = open("fighters/Goku_base/goku_1/goku_win_e.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_e.append(linhas[c].replace("\n", ""))
			c += 1
		sprites.append(sprites_d)
		sprites.append(sprites_e)
		return sprites
	if(p == 5):
		arq = open("fighters/Vegeta/vegeta_1/vegeta_win1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_d.append(linhas[c].replace("\n", ""))
			c += 1
		arq = open("fighters/Vegeta/vegeta_1/vegeta_win2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_e.append(linhas[c].replace("\n", ""))
			c += 1
		sprites.append(sprites_d)
		sprites.append(sprites_e)
		return sprites
	if(p == 6):
		arq = open("fighters/Freeza/freeza_1/freeza_win1.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_d.append(linhas[c].replace("\n", ""))
			c += 1
		arq = open("fighters/Freeza/freeza_1/freeza_win2.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			sprites_e.append(linhas[c].replace("\n", ""))
			c += 1
		sprites.append(sprites_d)
		sprites.append(sprites_e)
		return sprites

def seleciona_especial(p):
	sprites = []
	sprites.append([])
	sprites.append([])
	if(p == 1 or p == 2):
		arq = open("fighters/ryu/Ryu_1/ryu_especial.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 3):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	if(p == 3):
		arq = open("fighters/M.Bison/M.Bison_1/M.Bison_especial.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 3):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	if(p == 4):
		arq = open("fighters/Goku_base/goku_1/goku_especial.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 3):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	if(p == 5):
		arq = open("fighters/Vegeta/vegeta_1/vegeta_especial.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 3):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	if(p == 6):
		arq = open("fighters/Freeza/freeza_1/freeza_especial.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 3):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites

def posiciona_especial(sprites_esp, posicao):
	esp = []
	num_sprites = list(sprites_esp[0])
	name_sprites = list(sprites_esp[1])
	cont_1 = 0
	aux = 0
	while(cont_1 < len(num_sprites)):
		esp.append([])
		cont_2 = 0
		while(cont_2 < eval(num_sprites[cont_1])):
			esp[cont_1].append(Image(posicao, name_sprites[aux]))
			aux += 1
			cont_2 += 1
		cont_1 += 1
	return esp

def aux_criar_personagem(p):
	sprites = []
	sprites.append([])
	sprites.append([])
	if(p == 1):
		arq = open("fighters/ryu/Ryu_1/ryu_luta.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 4):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	elif(p == 2):
		arq = open("fighters/ken/ken_1/ken_luta.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 4):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	elif(p == 3):
		arq = open("fighters/M.Bison/M.Bison_1/M.Bison_luta.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 4):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	elif(p == 4):
		arq = open("fighters/Goku_base/goku_1/sprite_gokubase.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 4):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	elif(p == 5):
		arq = open("fighters/Vegeta/vegeta_1/vegeta_luta.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 4):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites
	elif(p == 6):
		arq = open("fighters/Freeza/freeza_1/freeza_luta.txt", "r")
		linhas = arq.readlines()
		arq.close()
		c = 0
		while(c < len(linhas)):
			if(len(linhas[c]) < 4):
				n = linhas[c].replace("\n", "")
				sprites[0].append(n)
				linhas.pop(c)
			else:
				s = linhas[c].replace("\n", "")
				sprites[1].append(s)
				c += 1
		return sprites	

def ChamaMenu(contador,contador1,aba_atual,som,dificuldade,mapa):
    pygame.mixer.music.load("music/menu/menu_opening.ogg")
    pygame.mixer.music.play(-1)
    a,contador = SobeLogo(contador,contador1)
    som,dificuldade,player1,player2,mapa = Menu(contador,aba_atual,som,dificuldade,mapa)
    return som,dificuldade,player1,player2,mapa,contador

def SobeLogo(contador,contador1):
    a = 1
    start_time = 0
    elapsed_time = time.time() - start_time
    while a==1:
        while contador1<22:
            if elapsed_time > 0.1:
                contador = movimento_fundo_menus(Fundo[0],contador,frames_fundos[cont])
                janela.update()
                contador1 = moveLogo(logo,contador1)
                elapsed_time = 0
                start_time = time.time()
                contador = movimento_fundo_menus(Fundo[0],contador,frames_fundos[cont])
            elapsed_time = time.time() - start_time
        a = 0
        return a,contador    

def Menu(contador,aba_atual,som,dificuldade,mapa):
    global aux_map1
    global aux_map2
    global aux_map3
    global aux_map4
    num_jogadores = 0
    mapa = 0
    contador_de_frames = 0
    contador_de_frames2 = 0
    contador_de_frames4 = 0
    contador_de_frames5 = 0
    contador_de_frames6 = 0
    contador_de_frames7 = 0
    start_time = 0
    elapsed_time = time.time() - start_time
    start_time2 = 0
    elapsed_time2 = time.time() - start_time
    start_time3 = 0
    elapsed_time3 = time.time() - start_time

    while aba_atual!=9 and aba_atual!=15:
        if elapsed_time > 0.1:
            contador = movimento_fundo_menus(Fundo[cont],contador,frames_fundos[cont])
            elapsed_time = 0
            start_time = time.time()
        (retorno,som,dificuldade,contador,mapa,num_jogadores) = verificar_mouse(contador,janela.checkMouse(),aba_atual,som,dificuldade,mapa)
        if aba_atual==6 and personagem!=0:
            if elapsed_time3 > 0.1:
                if personagem == 1:
                        contador,contador_de_frames = movimento_selecao(contador,contador_de_frames,sprites_ryu,personagem,len(sprites_ryu))
                        elapsed_time3 = 0
                        start_time3 = time.time()
                if personagem == 2:
                        contador,contador_de_frames2 = movimento_selecao(contador,contador_de_frames2,sprites_ken,personagem,len(sprites_ken))
                        elapsed_time3 = 0
                        start_time3 = time.time()
                if personagem == 3:
                        contador,contador_de_frames7 = movimento_selecao(contador,contador_de_frames7,sprites_Mbison,personagem,len(sprites_Mbison))
                        elapsed_time3 = 0
                        start_time3 = time.time()
                if personagem == 4:
                        contador,contador_de_frames4 = movimento_selecao(contador,contador_de_frames4,sprites_goku,personagem,len(sprites_goku))
                        elapsed_time3 = 0
                        start_time3 = time.time()
                if personagem == 5:
                        contador,contador_de_frames5 = movimento_selecao(contador,contador_de_frames5,sprites_vegeta,personagem,len(sprites_vegeta))
                        elapsed_time3 = 0
                        start_time3 = time.time()
                if personagem == 6:
                        contador,contador_de_frames6 = movimento_selecao(contador,contador_de_frames6,sprites_freeza,personagem,len(sprites_freeza))
                        elapsed_time3 = 0
                        start_time3 = time.time()
        if (aba_atual == 8 and retorno == 7) or (aba_atual == 7 and retorno == 8) or (aba_atual == 8 and retorno == 10) or (aba_atual==10 and retorno == 8):
            aux_map1 = 0
            aux_map2 = 0
            aux_map3 = 0
            aux_map4 = 0
        if retorno != 9: #NONE NAO SERIA ITERAVEL, AI COLOQUEI UM INTEIRO
            aba_atual = retorno
        if aba_atual == 7 or aba_atual == 8 or aba_atual == 10:
            if elapsed_time2 > 0.1:
                aux_map1,aux_map2,aux_map3,aux_map4 = moveMapas(aba_atual,aux_map1,aux_map2,aux_map3,aux_map4)
                elapsed_time2 = 0
                start_time2 = time.time()
        elapsed_time = time.time() - start_time
        elapsed_time2 = time.time() - start_time2
        elapsed_time3 = time.time() - start_time3
    return som,dificuldade,player1,player2,mapa
 
def molduraPersonagens(personagem,posicao,player1):
    if player1 == 0:
        if personagem == posicao:
            molduraPersonagem.undraw()
            molduraPersonagem.draw(janela)
            return posicao
        if personagem == 1:
            if posicao == 2: #posicao 1 = 250,150
                molduraPersonagem.move(-133,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 1
            if posicao == 3: #posicao 1 = 710,150
                molduraPersonagem.move(-265,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 1
            if posicao == 4: #posicao 4 = 710,400
                molduraPersonagem.move(0,158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 1 
            if posicao == 5:
                molduraPersonagem.move(-133,158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 1
            if posicao == 6:
                molduraPersonagem.move(-265,158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 1
        if personagem == 2: #mapa 2 = 250,400
            if posicao == 1: #posicao 1 = 250,150
                molduraPersonagem.move(133,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 2
            if posicao == 3: #posicao 1 = 710,150
                molduraPersonagem.move(-132,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 2
            if posicao == 4: #posicao 4 = 710,400
                molduraPersonagem.move(133,158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 2 
            if posicao == 5:
                molduraPersonagem.move(0,158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 2
            if posicao == 6:
                molduraPersonagem.move(-132,158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 2  
        if personagem == 3:
            if posicao == 1:
                molduraPersonagem.move(265,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 3
            if posicao == 2:
                molduraPersonagem.move(132,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 3
            if posicao == 4:
                molduraPersonagem.move(265,158) 
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 3 
            if posicao == 5:
                molduraPersonagem.move(133,158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 3
            if posicao == 6:
                molduraPersonagem.move(0,158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 3  
        if personagem == 4:
            if posicao == 1: #posicao 1 = 250,150
                molduraPersonagem.move(0,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 4
            if posicao == 2: #posicao 1 = 710,150
                molduraPersonagem.move(-133,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 4
            if posicao == 3: #posicao 4 = 710,400
                molduraPersonagem.move(-265,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 4 
            if posicao == 5:
                molduraPersonagem.move(-133,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 4
            if posicao == 6:
                molduraPersonagem.move(-266,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 4
        if personagem == 5:
        
            if posicao == 1: #posicao 1 = 250,150
                molduraPersonagem.move(133,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 5
            if posicao == 2: #posicao 1 = 710,150
                molduraPersonagem.move(0,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 5
            if posicao == 3: #posicao 4 = 710,400
                molduraPersonagem.move(-133,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 5 
            if posicao == 4:
                molduraPersonagem.move(133,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 5
            if posicao == 6:
                molduraPersonagem.move(-133,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 5
        if personagem == 6:
            if posicao == 1: #posicao 1 = 250,150
                molduraPersonagem.move(265,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 6
            if posicao == 2: #posicao 1 = 710,150
                molduraPersonagem.move(132,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 6
            if posicao == 3: #posicao 4 = 710,400
                molduraPersonagem.move(0,-158)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 6 
            if posicao == 4:
                molduraPersonagem.move(266,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 6
            if posicao == 5:
                molduraPersonagem.move(133,0)
                molduraPersonagem.undraw()
                molduraPersonagem.draw(janela)
                return 6  
###############################################################################
    else:
        if personagem == posicao:
            molduraPersonagem2.undraw()
            molduraPersonagem2.draw(janela)
            return posicao
        if personagem == 1:
            if posicao == 2: #posicao 1 = 250,150
                molduraPersonagem2.move(-133,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 1
            if posicao == 3: #posicao 1 = 710,150
                molduraPersonagem2.move(-266,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 1
            if posicao == 4: #posicao 4 = 710,400
                molduraPersonagem2.move(0,160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 1 
            if posicao == 5:
                molduraPersonagem2.move(-133,160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 1
            if posicao == 6:
                molduraPersonagem2.move(-266,160)
                return 1
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)   
        if personagem == 2: #mapa 2 = 250,400
            if posicao == 1: #posicao 1 = 250,150
                molduraPersonagem2.move(133,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 2
            if posicao == 3: #posicao 1 = 710,150
                molduraPersonagem2.move(-133,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 2
            if posicao == 4: #posicao 4 = 710,400
                molduraPersonagem2.move(133,160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 2 
            if posicao == 5:
                molduraPersonagem2.move(0,160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 2
            if posicao == 6:
                molduraPersonagem2.move(-133,160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 2  
        if personagem == 3:
            if posicao == 1:
                molduraPersonagem2.move(266,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 3
            if posicao == 2:
                molduraPersonagem2.move(133,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 3
            if posicao == 4:
                molduraPersonagem2.move(264,160) 
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 3 
            if posicao == 5:
                molduraPersonagem2.move(133,160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 3
            if posicao == 6:
                molduraPersonagem2.move(0,160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 3  
        if personagem == 4:
            if posicao == 1: #posicao 1 = 250,150
                molduraPersonagem2.move(0,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 4
            if posicao == 2: #posicao 1 = 710,150
                molduraPersonagem2.move(-133,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 4
            if posicao == 3: #posicao 4 = 710,400
                molduraPersonagem2.move(-265,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 4 
            if posicao == 5:
                molduraPersonagem2.move(-133,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 4
            if posicao == 6:
                molduraPersonagem2.move(-265,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 4
        if personagem == 5:
            if posicao == 1: #posicao 1 = 250,150
                molduraPersonagem2.move(133,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 5
            if posicao == 2: #posicao 1 = 710,150
                molduraPersonagem2.move(0,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 5
            if posicao == 3: #posicao 4 = 710,400
                molduraPersonagem2.move(-133,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 5 
            if posicao == 4:
                molduraPersonagem2.move(133,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 5
            if posicao == 6:
                molduraPersonagem2.move(-132,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 5
        if personagem == 6:
            if posicao == 1: #posicao 1 = 250,150
                molduraPersonagem2.move(266,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 6
            if posicao == 2: #posicao 1 = 710,150
                molduraPersonagem2.move(133,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 6
            if posicao == 3: #posicao 4 = 710,400
                molduraPersonagem2.move(0,-160)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 6 
            if posicao == 4:
                molduraPersonagem2.move(265,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 6
            if posicao == 5:
                molduraPersonagem2.move(132,0)
                molduraPersonagem2.undraw()
                molduraPersonagem2.draw(janela)
                return 6  
 
 
def movimento_fundo_menus(nome_imagem,contador,numero_frames):
        nome_imagem.move(0,-561) #arrumar velocidade p/ fundo fogo
        contador += 1
        if contador == numero_frames:
            nome_imagem.move(0,561*numero_frames)
            contador = 0
            return contador
        return contador
    
def movimento_selecao(contador,contador_de_frames,frames_personagem,personagem,numero_frames):
    frames_personagem[contador_de_frames].draw(janela)
    frames_personagem[contador_de_frames-1].undraw()
    janela.update()
    contador_de_frames += 1
    contador = movimento_fundo_menus(Fundo[cont],contador,frames_fundos[cont])
    if contador_de_frames == numero_frames:
        contador_de_frames = 0
    return contador,contador_de_frames

        
            
def apagar_sprite_exibicao(personagem):
    cont = 0
    if personagem == 1:
        while cont<len(sprites_ryu):
            sprites_ryu[cont].undraw()
            cont += 1
    if personagem == 2:
        while cont<len(sprites_ken):
            sprites_ken[cont].undraw()
            cont += 1
    if personagem == 3:
        while cont<len(sprites_Mbison):
            sprites_Mbison[cont].undraw()
            cont += 1
    if personagem == 4:
        while cont<len(sprites_goku):
            sprites_goku[cont].undraw()
            cont += 1
    if personagem == 5:
        while cont<len(sprites_vegeta):
            sprites_vegeta[cont].undraw()
            cont += 1
    if personagem == 6:
        while cont<len(sprites_freeza):
            sprites_freeza[cont].undraw()
            cont += 1
    
            
def movimentaMolduraMapas(mapa,posicao): 
    #posicao 1 = 250,150
    #mapa 2 = 250,400
    #mapa 3 = 710,150
    #mapa 4 = 710,400
    if mapa == posicao:
        moldura.undraw()
        moldura.draw(janela)
        return posicao
    if mapa == 1:
        if posicao == 2: #posicao 1 = 250,150
            moldura.move(0,-250)
            moldura.undraw()
            moldura.draw(janela)
            return 1
        if posicao == 3: #posicao 1 = 710,150
            moldura.move(-460,0)
            moldura.undraw()
            moldura.draw(janela)
            return 1
        if posicao == 4: #posicao 4 = 710,400
            moldura.move(-460,-250)
            moldura.undraw()
            moldura.draw(janela)
            return 1   
    
    if mapa == 2: #mapa 2 = 250,400
        if posicao == 1: #posicao 1 = 250,150
            moldura.move(0,250)
            moldura.undraw()
            moldura.draw(janela)
            return 2
        if posicao == 3: #posicao 1 = 710,150
            moldura.move(-460,250)
            moldura.undraw()
            moldura.draw(janela)
            return 2
        if posicao == 4: #posicao 4 = 710,400
            moldura.move(-460,0)
            moldura.undraw()
            moldura.draw(janela)
            return 2      
    if mapa == 3:
        if posicao == 1:
            moldura.move(460,0)
            moldura.undraw()
            moldura.draw(janela)
            return 3
        if posicao == 2:
            moldura.move(460,-250)
            moldura.undraw()
            moldura.draw(janela)
            return 3
        if posicao == 4:
            moldura.move(0,-250) 
            moldura.undraw()
            moldura.draw(janela)
            return 3 
    if mapa == 4:
        if posicao == 1:
            moldura.move(460,250)
            moldura.undraw()
            moldura.draw(janela)
            return 4
        if posicao == 2:
            moldura.move(460,0)
            moldura.undraw()
            moldura.draw(janela)
            return 4
        if posicao == 3:
            moldura.move(0,250)  
            moldura.undraw()
            moldura.draw(janela)
            return 4
            
            
def CheckIngame(checarMouse,fcheck):
	if (checarMouse.getX() > trocar_area.getP1().getX()) and (checarMouse.getX() < trocar_area.getP2().getX()):
		if (checarMouse.getY() > trocar_area.getP1().getY()) and (checarMouse.getY() < trocar_area.getP2().getY()):
		    return 19
	if (checarMouse.getX() > sair_area.getP1().getX()) and (checarMouse.getX() < sair_area.getP2().getX()):
		if (checarMouse.getY() > sair_area.getP1().getY()) and (checarMouse.getY() < sair_area.getP2().getY()):
		    return 23
	if (checarMouse.getX() > voltar_area.getP1().getX()) and (checarMouse.getX() < voltar_area.getP2().getX()):
		if (checarMouse.getY() > voltar_area.getP1().getY()) and (checarMouse.getY() < voltar_area.getP2().getY()):
		    return 18	            
                   
def verificar_mouse(contador,checarMouse,aba_do_menu,som,dificuldade,mapa): #aba 0: tela_inicial | aba1: jogar | aba2: configuracoes aba3: sair | aba4: dificuldade |aba5: ESCOLHA DE SOM LIGADO OU DESLIGADO | aba6: ESCOLHA DE NUMERO DE JOGADORES
    global cont
    global aux
    global player1
    global player2
    global personagem
    global posicao
    global posicao1
    global num_jogadores
    
    if checarMouse != None:
        if aba_do_menu==-1:
            trocaAba(0,-1)
            return 0,som,dificuldade,contador,mapa,num_jogadores
        if aba_do_menu==0:
            if (checarMouse.getX() > botao_jogar_area.getP1().getX()) and (checarMouse.getX() < botao_jogar_area.getP2().getX()):
                if (checarMouse.getY() > botao_jogar_area.getP1().getY()) and (checarMouse.getY() < botao_jogar_area.getP2().getY()):
                    trocaAba(1,0)
                    return 1,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_configuracoes_area.getP1().getX()) and (checarMouse.getX() < botao_configuracoes_area.getP2().getX()):
                if (checarMouse.getY() > botao_configuracoes_area.getP1().getY()) and (checarMouse.getY() < botao_configuracoes_area.getP2().getY()):
                    trocaAba(2,0)
                    return 2,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_sair_area.getP1().getX()) and (checarMouse.getX() < botao_sair_area.getP2().getX()):
                if (checarMouse.getY() > botao_sair_area.getP1().getY()) and (checarMouse.getY() < botao_sair_area.getP2().getY()):
                    trocaAba(3,0)
                    return 3,som,dificuldade,contador,mapa,num_jogadores
        if aba_do_menu==1:
            if (checarMouse.getX() > botao_retorno_area.getP1().getX()) and (checarMouse.getX() < botao_retorno_area.getP2().getX()):
                if (checarMouse.getY() > botao_retorno_area.getP1().getY()) and (checarMouse.getY() < botao_retorno_area.getP2().getY()):
                    trocaAba(0,1)
                    return 0,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_um_jogador_area.getP1().getX()) and (checarMouse.getX() < botao_um_jogador_area.getP2().getX()):
                if (checarMouse.getY() > botao_um_jogador_area.getP1().getY()) and (checarMouse.getY() < botao_um_jogador_area.getP2().getY()):
                    num_jogadores = 1
                    Fundo[cont].undraw()
                    efeitos_menu(6,som,0)
                    Fundo[cont].move(0,contador*561)
                    cont += 1
                    contador = 0
                    Fundo[cont].draw(janela)
                    escolha_lutador.draw(janela)
                    trocaAba(6,1)
                    return 6,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_dois_jogadores_area.getP1().getX()) and (checarMouse.getX() < botao_dois_jogadores_area.getP2().getX()):
                if (checarMouse.getY() > botao_dois_jogadores_area.getP1().getY()) and (checarMouse.getY() < botao_dois_jogadores_area.getP2().getY()):
                    num_jogadores = 2
                    Fundo[cont].undraw()
                    Fundo[cont].move(0,contador*561)
                    cont += 1
                    contador = 0
                    Fundo[cont].draw(janela)
                    escolha_lutador.draw(janela) 
                    efeitos_menu(6,som,0)                   
                    trocaAba(6,1)

                    return 6,som,dificuldade,contador,mapa,num_jogadores
        if aba_do_menu==2:
            if (checarMouse.getX() > botao_retorno_area.getP1().getX()) and (checarMouse.getX() < botao_retorno_area.getP2().getX()):
                if (checarMouse.getY() > botao_retorno_area.getP1().getY()) and (checarMouse.getY() < botao_retorno_area.getP2().getY()):
                    trocaAba(0,2)
                    return 0,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_som_area.getP1().getX()) and (checarMouse.getX() < botao_som_area.getP2().getX()):
                if (checarMouse.getY() > botao_som_area.getP1().getY()) and (checarMouse.getY() < botao_som_area.getP2().getY()):
                    trocaAba(5,2)
                    return 5,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_dificuldade_area.getP1().getX()) and (checarMouse.getX() < botao_dificuldade_area.getP2().getX()):
                if (checarMouse.getY() > botao_dificuldade_area.getP1().getY()) and (checarMouse.getY() < botao_dificuldade_area.getP2().getY()):
                    trocaAba(4,2)
                    return 4,som,dificuldade,contador,mapa,num_jogadores
        if aba_do_menu==4:
            if (checarMouse.getX() > botao_facil_area.getP1().getX()) and (checarMouse.getX() < botao_facil_area.getP2().getX()):
                if (checarMouse.getY() > botao_facil_area.getP1().getY()) and (checarMouse.getY() < botao_facil_area.getP2().getY()):
                    trocaAba(0,4)
                    dificuldade = 1
                    return 0,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_normal_area.getP1().getX()) and (checarMouse.getX() < botao_normal_area.getP2().getX()):
                if (checarMouse.getY() > botao_normal_area.getP1().getY()) and (checarMouse.getY() < botao_normal_area.getP2().getY()):
                    trocaAba(0,4)
                    dificuldade = 2
                    return 0,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_dificil_area.getP1().getX()) and (checarMouse.getX() < botao_dificil_area.getP2().getX()):
                if (checarMouse.getY() > botao_dificil_area.getP1().getY()) and (checarMouse.getY() < botao_dificil_area.getP2().getY()):
                    trocaAba(0,4)
                    dificuldade = 3
                    return 0,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_retorno_area.getP1().getX()) and (checarMouse.getX() < botao_retorno_area.getP2().getX()):
                if (checarMouse.getY() > botao_retorno_area.getP1().getY()) and (checarMouse.getY() < botao_retorno_area.getP2().getY()):
                    trocaAba(2,4)
                    return 2,som,dificuldade,contador,mapa,num_jogadores
        if aba_do_menu==3:
            if (checarMouse.getX() > botao_sim_area.getP1().getX()) and (checarMouse.getX() < botao_sim_area.getP2().getX()):
                if (checarMouse.getY() > botao_sim_area.getP1().getY()) and (checarMouse.getY() < botao_sim_area.getP2().getY()):
                    janela.close()
            if (checarMouse.getX() > botao_nao_area.getP1().getX()) and (checarMouse.getX() < botao_nao_area.getP2().getX()):
                if (checarMouse.getY() > botao_nao_area.getP1().getY()) and (checarMouse.getY() < botao_nao_area.getP2().getY()):
                    trocaAba(0,3)
                    return 0,som,dificuldade,contador,mapa,num_jogadores
        if aba_do_menu==5:
            if (checarMouse.getX() > botao_ligado_area.getP1().getX()) and (checarMouse.getX() < botao_ligado_area.getP2().getX()):
                if (checarMouse.getY() > botao_ligado_area.getP1().getY()) and (checarMouse.getY() < botao_ligado_area.getP2().getY()):
                    som = True
                    pygame.mixer.music.load("music/menu/menu_opening.ogg")
                    pygame.mixer.music.play(-1)                    
                    trocaAba(0,5)
                    return 0,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_desligado_area.getP1().getX()) and (checarMouse.getX() < botao_desligado_area.getP2().getX()):
                if (checarMouse.getY() > botao_desligado_area.getP1().getY()) and (checarMouse.getY() < botao_desligado_area.getP2().getY()):
                    som = False
                    pygame.mixer.music.stop()
                    trocaAba(0,5)
                    return 0,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > botao_retorno_area.getP1().getX()) and (checarMouse.getX() < botao_retorno_area.getP2().getX()):
                if (checarMouse.getY() > botao_retorno_area.getP1().getY()) and (checarMouse.getY() < botao_retorno_area.getP2().getY()):
                    trocaAba(2,5)
                    return 2,som,dificuldade,contador,mapa,num_jogadores
        if aba_do_menu==6:
            if (checarMouse.getX() > botao_retorno_area.getP1().getX()) and (checarMouse.getX() < botao_retorno_area.getP2().getX()):
                if (checarMouse.getY() > botao_retorno_area.getP1().getY()) and (checarMouse.getY() < botao_retorno_area.getP2().getY()):
                    Fundo[cont].undraw()
                    Fundo[cont].move(0,contador*561)
                    posicao1 = molduraPersonagens(1,posicao1,player1)
                    player1 = 1
                    posicao1 = molduraPersonagens(1,posicao1,player1)
                    cont -= 1
                    contador = 0
                    Fundo[cont].draw(janela)
                    personagem = apagar_sprite_exibicao(personagem)
                    trocaAba(1,6)
                    player1 = 0
                    player2 = 0
                    personagem = 0
                    return 1,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > icone_ryu_area.getP1().getX()) and (checarMouse.getX() < icone_ryu_area.getP2().getX()):
                if (checarMouse.getY() > icone_ryu_area.getP1().getY()) and (checarMouse.getY() < icone_ryu_area.getP2().getY()):
                    apagar_sprite_exibicao(personagem)
                    botao_confirmar.undraw()
                    botao_confirmar.draw(janela)
                    imagem_fundo_sf.undraw()
                    imagem_fundo_dbz.undraw()
                    imagem_fundo_sf.draw(janela)
                    personagem = 1
                    posicao1 = molduraPersonagens(personagem,posicao1,player1)
                    return 6,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > icone_ken_area.getP1().getX()) and (checarMouse.getX() < icone_ken_area.getP2().getX()):
                if (checarMouse.getY() > icone_ken_area.getP1().getY()) and (checarMouse.getY() < icone_ken_area.getP2().getY()):
                    apagar_sprite_exibicao(personagem)
                    molduraPersonagens(personagem,posicao1,player1)
                    botao_confirmar.undraw()
                    botao_confirmar.draw(janela)
                    imagem_fundo_sf.undraw()
                    imagem_fundo_dbz.undraw()
                    imagem_fundo_sf.draw(janela)
                    personagem = 2
                    posicao1 = molduraPersonagens(personagem,posicao1,player1)
                    return 6,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > icone_bison_area.getP1().getX()) and (checarMouse.getX() < icone_bison_area.getP2().getX()):
                if (checarMouse.getY() > icone_bison_area.getP1().getY()) and (checarMouse.getY() < icone_bison_area.getP2().getY()):
                    apagar_sprite_exibicao(personagem)
                    botao_confirmar.undraw()
                    botao_confirmar.draw(janela)
                    imagem_fundo_sf.undraw()
                    imagem_fundo_dbz.undraw()
                    imagem_fundo_sf.draw(janela)
                    personagem = 3
                    posicao1 = molduraPersonagens(personagem,posicao1,player1)
                    return 6,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > icone_goku_area.getP1().getX()) and (checarMouse.getX() < icone_goku_area.getP2().getX()):
                if (checarMouse.getY() > icone_goku_area.getP1().getY()) and (checarMouse.getY() < icone_goku_area.getP2().getY()):
                    apagar_sprite_exibicao(personagem)
                    botao_confirmar.undraw()
                    botao_confirmar.draw(janela)
                    imagem_fundo_sf.undraw()
                    imagem_fundo_dbz.undraw()
                    imagem_fundo_dbz.draw(janela)
                    personagem = 4
                    posicao1 = molduraPersonagens(personagem,posicao1,player1)
                    return 6,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > icone_vegeta_area.getP1().getX()) and (checarMouse.getX() < icone_vegeta_area.getP2().getX()):
                if (checarMouse.getY() > icone_vegeta_area.getP1().getY()) and (checarMouse.getY() < icone_vegeta_area.getP2().getY()):
                    apagar_sprite_exibicao(personagem)
                    botao_confirmar.undraw()
                    botao_confirmar.draw(janela)
                    imagem_fundo_sf.undraw()
                    imagem_fundo_dbz.undraw()
                    imagem_fundo_dbz.draw(janela)
                    personagem = 5
                    posicao1 = molduraPersonagens(personagem,posicao1,player1)
                    return 6,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > icone_freeza_area.getP1().getX()) and (checarMouse.getX() < icone_freeza_area.getP2().getX()):
                    apagar_sprite_exibicao(personagem)
                    botao_confirmar.undraw()
                    botao_confirmar.draw(janela)
                    imagem_fundo_sf.undraw()
                    imagem_fundo_dbz.undraw()
                    imagem_fundo_dbz.draw(janela)
                    personagem = 6
                    posicao1 = molduraPersonagens(personagem,posicao1,player1)
                    return 6,som,dificuldade,contador,mapa,num_jogadores
            if personagem != 0:            
                if (checarMouse.getX() > botao_confirmar_area.getP1().getX()) and (checarMouse.getX() < botao_confirmar_area.getP2().getX()):
                    if (checarMouse.getY() > botao_confirmar_area.getP1().getY()) and (checarMouse.getY() < botao_confirmar_area.getP2().getY()):
                        if player1==0 or player2==0:
                            apagar_sprite_exibicao(personagem)
                            botao_confirmar.undraw()
                         
                        if player1 == 0:
                            posicao1 = molduraPersonagens(1,posicao1,player1)
                            molduraPersonagem.undraw()
                            player1 = personagem
                            personagem = 0
                            posicao1 = 1
                            return 9,som,dificuldade,contador,mapa,num_jogadores
                        if player2 == 0:
                            posicao1 = molduraPersonagens(1,posicao1,player1)
                            molduraPersonagem2.undraw()
                            player2 = personagem
                            apagar_sprite_exibicao(personagem)
                            trocaAba(7,6)
                            posicao1 = 1
                            personagem = 0
                            return 7,som,dificuldade,contador,mapa,num_jogadores
                        personagem = 0
        if aba_do_menu == 7:
            if (checarMouse.getX() > miniaturas_area[0].getP1().getX()) and (checarMouse.getX() < miniaturas_area[0].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[0].getP1().getY()) and (checarMouse.getY() < miniaturas_area[0].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 3
                    posicao = movimentaMolduraMapas(1,posicao)
                    return 7,som,dificuldade,contador,mapa,num_jogadores
                        
            if (checarMouse.getX() > miniaturas_area[1].getP1().getX()) and (checarMouse.getX() < miniaturas_area[1].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[1].getP1().getY()) and (checarMouse.getY() < miniaturas_area[1].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 1
                    posicao = movimentaMolduraMapas(2,posicao)
                    return 7,som,dificuldade,contador,mapa,num_jogadores
                    
                
            if (checarMouse.getX() > miniaturas_area[2].getP1().getX()) and (checarMouse.getX() < miniaturas_area[2].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[2].getP1().getY()) and (checarMouse.getY() < miniaturas_area[2].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 4
                    posicao = movimentaMolduraMapas(3,posicao)
                    return 7,som,dificuldade,contador,mapa,num_jogadores               
            if (checarMouse.getX() > miniaturas_area[3].getP1().getX()) and (checarMouse.getX() < miniaturas_area[3].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[3].getP1().getY()) and (checarMouse.getY() < miniaturas_area[3].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 2
                    posicao = movimentaMolduraMapas(4,posicao)
                    return 7,som,dificuldade,contador,mapa,num_jogadores
                    
            if (checarMouse.getX() > seta_area.getP1().getX()) and (checarMouse.getX() < seta_area.getP2().getX()):
                if (checarMouse.getY() > seta_area.getP1().getY()) and (checarMouse.getY() < seta_area.getP2().getY()):
                    trocaAba(8,7)
                    apagaMapas(7)
                    aux_map1 = 0
                    aux_map2 = 0
                    aux_map3 = 0
                    aux_map4 = 0
                    return 8,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > seta_area_back.getP1().getX()) and (checarMouse.getX() < seta_area_back.getP2().getX()):
                if (checarMouse.getY() > seta_area_back.getP1().getY()) and (checarMouse.getY() < seta_area_back.getP2().getY()):
                    trocaAba(6,7)
                    apagaMapas(7)
                    player1 = 0
                    player2 = 0
                    personagem = 0
                    
                    return 6,som,dificuldade,contador,mapa,num_jogadores
            if mapa!=0:
                    if (checarMouse.getX() > confirmar_area.getP1().getX()) and (checarMouse.getX() < confirmar_area.getP2().getX()):
                        if (checarMouse.getY() > confirmar_area.getP1().getY()) and (checarMouse.getY() < confirmar_area.getP2().getY()):
                            pygame.mixer.music.stop()
                            efeitos_menu(7,som,1)
                            ApagaTudo(7,1)
                            Fundo[cont].undraw()
                            Fundo[cont].move(0,contador*561)
                            return 15,som,dificuldade,contador,mapa,num_jogadores
                            
            if (checarMouse.getX() > seta_area_back.getP1().getX()) and (checarMouse.getX() < seta_area_back.getP2().getX()):
                if (checarMouse.getY() > seta_area_back.getP1().getY()) and (checarMouse.getY() < seta_area_back.getP2().getY()):
                    trocaAba(6,7)
                    return 8,som,dificuldade,contador,mapa,num_jogadores
        if aba_do_menu == 8:
            if (checarMouse.getX() > miniaturas_area[0].getP1().getX()) and (checarMouse.getX() < miniaturas_area[0].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[0].getP1().getY()) and (checarMouse.getY() < miniaturas_area[0].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 8
                    posicao = movimentaMolduraMapas(1,posicao)
                    return 8,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > miniaturas_area[1].getP1().getX()) and (checarMouse.getX() < miniaturas_area[1].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[1].getP1().getY()) and (checarMouse.getY() < miniaturas_area[1].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 5
                    posicao = movimentaMolduraMapas(2,posicao)
                    return 8,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > miniaturas_area[2].getP1().getX()) and (checarMouse.getX() < miniaturas_area[2].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[2].getP1().getY()) and (checarMouse.getY() < miniaturas_area[2].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 7
                    posicao = movimentaMolduraMapas(3,posicao)
                    return 8,som,dificuldade,contador,mapa,num_jogadores          
            if (checarMouse.getX() > miniaturas_area[3].getP1().getX()) and (checarMouse.getX() < miniaturas_area[3].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[3].getP1().getY()) and (checarMouse.getY() < miniaturas_area[3].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 6
                    posicao = movimentaMolduraMapas(4,posicao)
                    return 8,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > seta_area.getP1().getX()) and (checarMouse.getX() < seta_area.getP2().getX()):
                if (checarMouse.getY() > seta_area.getP1().getY()) and (checarMouse.getY() < seta_area.getP2().getY()):
                    apagaMapas(8)
                    trocaAba(10,8)
                    aux_map1 = 0
                    aux_map2 = 0
                    aux_map3 = 0
                    aux_map4 = 0
                    return 10,som,dificuldade,contador,mapa,num_jogadores
                
            if (checarMouse.getX() > seta_area_back.getP1().getX()) and (checarMouse.getX() < seta_area_back.getP2().getX()):
                if (checarMouse.getY() > seta_area_back.getP1().getY()) and (checarMouse.getY() < seta_area_back.getP2().getY()):
                
                    apagaMapas(8)
                    trocaAba(7,8)
                    aux_map1 = 0
                    aux_map2 = 0
                    aux_map3 = 0
                    aux_map4 = 0
                    return 7,som,dificuldade,contador,mapa,num_jogadores
            if mapa!=0:
                    if (checarMouse.getX() > confirmar_area.getP1().getX()) and (checarMouse.getX() < confirmar_area.getP2().getX()):
                        if (checarMouse.getY() > confirmar_area.getP1().getY()) and (checarMouse.getY() < confirmar_area.getP2().getY()):
                            pygame.mixer.music.stop()
                            efeitos_menu(8,som,1)
                            ApagaTudo(8,1)
                            Fundo[cont].undraw()
                            Fundo[cont].move(0,contador*561)
                            return 15,som,dificuldade,contador,mapa,num_jogadores
                           
        if aba_do_menu == 10:
            if (checarMouse.getX() > miniaturas_area[0].getP1().getX()) and (checarMouse.getX() < miniaturas_area[0].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[0].getP1().getY()) and (checarMouse.getY() < miniaturas_area[0].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    posicao = movimentaMolduraMapas(1,posicao)
                    mapa = 11
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    return 10,som,dificuldade,contador,mapa,num_jogadores    
            if (checarMouse.getX() > miniaturas_area[1].getP1().getX()) and (checarMouse.getX() < miniaturas_area[1].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[1].getP1().getY()) and (checarMouse.getY() < miniaturas_area[1].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 9
                    posicao = movimentaMolduraMapas(2,posicao)
                    return 10,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > miniaturas_area[2].getP1().getX()) and (checarMouse.getX() < miniaturas_area[2].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[2].getP1().getY()) and (checarMouse.getY() < miniaturas_area[2].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 12
                    posicao = movimentaMolduraMapas(3,posicao)
                    return 10,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > miniaturas_area[3].getP1().getX()) and (checarMouse.getX() < miniaturas_area[3].getP2().getX()):
                if (checarMouse.getY() > miniaturas_area[3].getP1().getY()) and (checarMouse.getY() < miniaturas_area[3].getP2().getY()):
                    #moldura.draw(janela), vai indicar a selecao do mapa
                    botao_confirmar2.undraw()
                    botao_confirmar2.draw(janela)
                    mapa = 10
                    posicao = movimentaMolduraMapas(4,posicao)
                    return 10,som,dificuldade,contador,mapa,num_jogadores
            if (checarMouse.getX() > seta_area_back.getP1().getX()) and (checarMouse.getX() < seta_area_back.getP2().getX()):
                if (checarMouse.getY() > seta_area_back.getP1().getY()) and (checarMouse.getY() < seta_area_back.getP2().getY()):
                    apagaMapas(10)
                    trocaAba(8,10)
                    aux_map1 = 0
                    aux_map2 = 0
                    aux_map3 = 0
                    aux_map4 = 0                    
                    return 8,som,dificuldade,contador,mapa,num_jogadores
            if mapa!=0:
                    if (checarMouse.getX() > confirmar_area.getP1().getX()) and (checarMouse.getX() < confirmar_area.getP2().getX()):
                        if (checarMouse.getY() > confirmar_area.getP1().getY()) and (checarMouse.getY() < confirmar_area.getP2().getY()):
                            pygame.mixer.music.stop()
                            efeitos_menu(10,som,1)
                            ApagaTudo(10,1)
                            Fundo[cont].undraw()
                            Fundo[cont].move(0,contador*561)
                            return 15,som,dificuldade,contador,mapa,num_jogadores
    return 9,som,dificuldade,contador,mapa,num_jogadores
                    
                    
def trocaAba(aba_clicada,aba_atual): #INICIAL 0, JOGAR 1, CONFIGURACOES 2, SAIR 3, 4 DIFICULDADE
    if aba_clicada == 0:
       if aba_atual == -1:
          botao_jogar.draw(janela)
          botao_configuracoes.draw(janela)
          botao_sair.draw(janela)
          return 0
       if aba_atual == 1:
            botao_retorno.undraw()
            botao_jogar.draw(janela)
            botao_configuracoes.draw(janela)
            botao_sair.draw(janela)
            botao_um_jogador.undraw()
            botao_dois_jogadores.undraw()
            logo.undraw()
            logo.draw(janela)
            return 0
       if aba_atual == 2:
            botao_jogar.draw(janela)
            botao_configuracoes.draw(janela)
            botao_sair.draw(janela)
            botao_retorno.undraw()
            botao_som.undraw()
            botao_dificuldade.undraw()
            logo.undraw()
            logo.draw(janela)
            return 0
       if aba_atual == 3:
            botao_jogar.draw(janela)
            botao_configuracoes.draw(janela)
            botao_sair.draw(janela)
            botao_sim.undraw()
            botao_nao.undraw()
            botao_retorno.undraw()
            certeza.undraw()
            logo.undraw()
            logo.draw(janela)
            return 0
       if aba_atual==4:
            botao_jogar.draw(janela)
            botao_configuracoes.draw(janela)
            botao_sair.draw(janela)
            botao_facil.undraw()
            botao_normal.undraw()
            botao_dificil.undraw()
            botao_retorno.undraw()
            logo.undraw()
            logo.draw(janela)
            return 0
       if aba_atual == 5:
            botao_jogar.draw(janela)
            botao_configuracoes.draw(janela)
            botao_sair.draw(janela)
            botao_desligado.undraw()
            botao_ligado.undraw()
            botao_retorno.undraw()
            logo.undraw()
            logo.draw(janela)
            return 0
    if aba_clicada == 1:
        if aba_atual == 0:
            botao_jogar.undraw()
            botao_configuracoes.undraw()
            botao_sair.undraw()
            logo.undraw()
            botao_retorno.draw(janela)
            botao_um_jogador.draw(janela)
            botao_dois_jogadores.draw(janela)
            return 0
        if aba_atual == 6:
            pygame.mixer.music.load("music/menu/char_selection.ogg")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/menu/menu_opening.ogg")
            pygame.mixer.music.play(-1)
            retangulo_personagens.undraw()
            retangulo_exibicao.undraw()
            logo.undraw()
            escolha_lutador.undraw()
            botao_um_jogador.undraw()      
            botao_um_jogador.draw(janela)
            botao_dois_jogadores.undraw()
            botao_dois_jogadores.draw(janela)
            botao_retorno.undraw()
            botao_retorno.draw(janela)    
            return 0
    if aba_clicada == 2:
        if aba_atual == 0:
            botao_jogar.undraw()
            botao_configuracoes.undraw()
            logo.undraw()
            botao_sair.undraw()
            botao_som.draw(janela)
            botao_dificuldade.draw(janela)
            botao_retorno.draw(janela)
            return 0
        if aba_atual == 4:
            botao_facil.undraw()
            botao_normal.undraw()
            botao_dificil.undraw()
            botao_som.draw(janela)
            botao_dificuldade.draw(janela)
            return 0
        if aba_atual == 5:
            botao_ligado.undraw()
            botao_desligado.undraw()
            botao_som.draw(janela)
            botao_dificuldade.draw(janela)
            return 0
    if aba_clicada == 3:
        if aba_atual == 0:
            botao_jogar.undraw()
            botao_configuracoes.undraw()
            logo.undraw()
            botao_sair.undraw()
            certeza.draw(janela)
            botao_sim.draw(janela)
            botao_nao.draw(janela)
            return 0
    if aba_clicada == 4:
        if aba_atual == 2:
            botao_som.undraw()
            botao_dificuldade.undraw()
            botao_facil.draw(janela)
            botao_normal.draw(janela)
            botao_dificil.draw(janela)
            return 0
    if aba_clicada == 5:
       if aba_atual == 2:
            botao_som.undraw()
            botao_dificuldade.undraw()
            botao_ligado.draw(janela)
            botao_desligado.draw(janela)
            return 0
    if aba_clicada == 6:
        if aba_atual == 1:
            botao_um_jogador_area.undraw()
            botao_dois_jogadores_area.undraw()
            botao_retorno.undraw()
            botao_retorno.draw(janela)
            botao_retorno.undraw()
            botao_retorno.draw(janela)
            botao_um_jogador.undraw()
            botao_dois_jogadores.undraw()
            retangulo_personagens.draw(janela)
            posicao1 = 1
            posicao1 = molduraPersonagens(personagem,posicao1,player1)
            return 0
        if aba_atual == 7:
            botao_retorno.draw(janela)
            botao_confirmar.undraw()
            seta.undraw()
            retangulo_personagens.draw(janela)
            escolha_lutador.draw(janela)
            seta_area.undraw()
            seta_back.undraw()
            escolha_mapa.undraw()
            miniaturas_area[0].undraw()
            miniaturas_area[1].undraw()
            miniaturas_area[2].undraw()
            miniaturas_area[3].undraw()
            bonito_tarde_fundo.undraw()
            air_crystal_fundo.undraw()
            porto_fundo.undraw()
            punk_toilet_fundo.undraw()
            posicao1 = 1
            posicao1 = molduraPersonagens(personagem,posicao1,player1)
            return 0
    if aba_clicada == 7:
        if aba_atual == 6:
            posicao1 = 1
            retangulo_personagens.undraw()
            botao_retorno.undraw()
            escolha_lutador.undraw()
            retangulo_exibicao.undraw()
            seta.undraw()
            imagem_fundo_dbz.undraw()
            imagem_fundo_sf.undraw()
            seta_back.undraw()
            seta.draw(janela)
            seta_back.draw(janela)
            escolha_mapa.undraw()
            escolha_mapa.draw(janela)
            apagar_sprite_exibicao(personagem)
            bonito_tarde_fundo.draw(janela)
            air_crystal_fundo.draw(janela)
            porto_fundo.draw(janela)
            punk_toilet_fundo.draw(janela)
            return 0  
        if aba_atual == 8:
            moldura.undraw()
            botao_confirmar.undraw()
            bonito_tarde_fundo.draw(janela)
            air_crystal_fundo.draw(janela)
            porto_fundo.draw(janela)
            escolha_mapa.undraw()
            escolha_mapa.draw(janela)
            punk_toilet_fundo.draw(janela)
            korea_fundo.undraw()
            graveyard_fundo.undraw()
            boat_fundo.undraw()
            tribal_fundo.undraw()
            return 0
    if aba_clicada == 8:
        if aba_atual == 7:
            moldura.undraw()
            bonito_tarde_fundo.undraw()
            air_crystal_fundo.undraw()
            porto_fundo.undraw()
            escolha_mapa.undraw()
            escolha_mapa.draw(janela)
            punk_toilet_fundo.undraw()
            tribal_fundo.draw(janela)
            boat_fundo.draw(janela)
            graveyard_fundo.draw(janela)
            korea_fundo.draw(janela)
            return 0
        if aba_atual == 10:
			seta.undraw()
			seta.draw(janela)
			moldura.undraw()
			y_train_fundo.undraw()
			bet_fundo.undraw()
			kids_fundo.undraw()
			riot_fundo.undraw()
			escolha_mapa.undraw()
			escolha_mapa.draw(janela)
			tribal_fundo.draw(janela)
			boat_fundo.draw(janela)
			graveyard_fundo.draw(janela)
			korea_fundo.draw(janela)
			return 0
    if aba_clicada == 10:
        if aba_atual == 8:
            seta.undraw()
            
            moldura.undraw()
            korea_fundo.undraw()
            graveyard_fundo.undraw()
            boat_fundo.undraw()
            tribal_fundo.undraw()
            escolha_mapa.undraw()
            escolha_mapa.draw(janela)
            kids_fundo.draw(janela)
            y_train_fundo.draw(janela)
            riot_fundo.draw(janela)
            bet_fundo.draw(janela)
            return 0      
            
            
            
def moveLogo(nome_logo, contador):
        nome_logo.move(0,28)
        contador += 1
        return contador
              
def moveMapas(aba_atual,aux_map1,aux_map2,aux_map3,aux_map4):
    if aba_atual == 7:
        porto[aux_map1].draw(janela)
        if aux_map1 != 0:
            porto[aux_map1-1].undraw()
        aux_map1 += 1
        
        punk_toilet[aux_map2].draw(janela)
        if aux_map2 != 0:
            punk_toilet[aux_map2-1].undraw()
        aux_map2 += 1
            
        air_crystal[aux_map3].draw(janela)
        if aux_map3 != 0:
            air_crystal[aux_map3-1].undraw()
        aux_map3 += 1
        
        bonito_tarde[aux_map4].draw(janela)
        if aux_map4 != 0:
            bonito_tarde[aux_map4-1].undraw()
        aux_map4 += 1
        if aux_map1 == 7:
            aux_map1 = 0
            porto[7].undraw()
            porto[6].undraw()
        if aux_map2 == 15:
            aux_map2 = 0
            punk_toilet[15].undraw()
            punk_toilet[14].undraw()
        if aux_map3 == 7:
            aux_map3 = 0
            air_crystal[7].undraw()
            air_crystal[6].undraw()
        if aux_map4 == 15:
            aux_map4 = 0
            bonito_tarde[15].undraw()
            bonito_tarde[14].undraw()
        return aux_map1,aux_map2,aux_map3,aux_map4
    if aba_atual == 8:
    
        graveyard[aux_map1].draw(janela)
        graveyard[aux_map1-1].undraw()
        aux_map1 += 1
        
        tribal[aux_map2].draw(janela)
        tribal[aux_map2-1].undraw()
        aux_map2 += 1
        
        boat[aux_map3].draw(janela)
        boat[aux_map3-1].undraw()
        aux_map3 += 1
            
        
        korea[aux_map4].draw(janela)
        korea[aux_map4-1].undraw()
        aux_map4 += 1
        if aux_map1 == 16:
            aux_map1 = 0
            graveyard[14].undraw()
            
        if aux_map2 == 35:
            aux_map2 = 0
            tribal[34].undraw()
            
        if aux_map3 == 14:
            aux_map3 = 0
            boat[13].undraw()
            
        if aux_map4 == 8:
            aux_map4 = 0
            korea[7].undraw()
        return aux_map1,aux_map2,aux_map3,aux_map4
    if aba_atual == 10:
        riot[aux_map2-1].undraw()
        riot[aux_map2].draw(janela)
        aux_map2 += 1
        
        kids[aux_map1-1].undraw()
        kids[aux_map1].draw(janela)
        aux_map1 += 1
        
        y_train[aux_map3-1].undraw()
        y_train[aux_map3].draw(janela)
        aux_map3 += 1
        
        bet[aux_map4-1].undraw()
        bet[aux_map4].draw(janela)
        aux_map4 += 1
        
        if aux_map2 == 8:
            aux_map2 = 0
        if aux_map1 == 20:
            aux_map1 = 0
        if aux_map3 == 8:
            aux_map3 = 0
        if aux_map4 == 24:
            aux_map4 = 0
        return aux_map1,aux_map2,aux_map3,aux_map4

        
def apagaMapas(aba_atual):
    aux = 0
    if aba_atual == 7:
        while aux<8:
            porto[aux].undraw()
            air_crystal[aux].undraw()
            aux += 1
        aux = 0
        while aux<16:
            punk_toilet[aux].undraw()
            bonito_tarde[aux].undraw()
            aux += 1
        return 0
    if aba_atual == 8:
        while aux<len(korea):
            korea[aux].undraw()
            aux += 1
        aux = 0
        while aux<len(boat):
            boat[aux].undraw()
            aux += 1
        aux = 0
        while aux<len(tribal):
            tribal[aux].undraw()
            aux += 1
        aux = 0
        while aux<len(graveyard):
            graveyard[aux].undraw()
            aux += 1
    if aba_atual == 10:
        while aux<len(kids):
            kids[aux].undraw()
            aux += 1
        aux = 0
        while aux<len(y_train):
            y_train[aux].undraw()
            aux += 1
        aux = 0
        while aux<len(bet):
            bet[aux].undraw()
            aux += 1
        aux = 0
        while aux<len(riot):
            riot[aux].undraw()
            aux += 1
    return 0
        
janela = GraphWin("FURG Fighters Alpha Release", 960,560, autoflush = False)
janela.setCoords(0,0,960,560) 
janela.setBackground("Black")

som = True #true = ligado, false = desligado
dificuldade = 2 #1 = facil, 2 = normal, 3 = dificil
numero_mapas = 2
Fundo = [0]*numero_mapas
frames_fundos = [0]*numero_mapas
frames_fundos[0] = 8
frames_fundos[1] = 25
Fundo[0] = Image(Point(480,0), "Arte/Backgrounds/menu.png")
Fundo[1] = Image(Point(480,0), "Arte/Backgrounds/tentativa1.png")
player1 = 0
player2 = 0
personagem = 0
cont = 0
Fundo[0].move(0,2243)
Fundo[1].move(0,7012)
Fundo[cont].draw(janela)
logo = Image(Point(480,-200), "Arte/Buttons_and_Symbols/simbolo_furg_fighters.png")
retangulo_personagens = Image(Point(280,300), "Arte/Buttons_and_Symbols/selecao_personagens.png")
logo.draw(janela)
contador = 0
contador1 = 0
aux = 0
num_jogadores = 0
sprites_ryu = [0]*5
sprites_ryu[0] = Image(Point(780,335),"fighters/ryu/Ryu_1/luta/ryupe1D.png")
sprites_ryu[1] = Image(Point(780,335),"fighters/ryu/Ryu_1/luta/ryupe2D.png")
sprites_ryu[2] = Image(Point(780,335),"fighters/ryu/Ryu_1/luta/ryupe3D.png")
sprites_ryu[3] = Image(Point(780,335),"fighters/ryu/Ryu_1/luta/ryupe4D.png")
sprites_ryu[4] = Image(Point(780,335),"fighters/ryu/Ryu_1/luta/ryupe5D.png")
sprites_ken = [0]*12
sprites_ken[0] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado1.png")
sprites_ken[1] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado2.png")
sprites_ken[2] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado3.png")
sprites_ken[3] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado4.png")
sprites_ken[4] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado5.png")
sprites_ken[5] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado6.png")
sprites_ken[6] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado7.png")
sprites_ken[7] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado8.png")
sprites_ken[8] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado9.png")
sprites_ken[9] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado10.png")
sprites_ken[10] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado11.png")
sprites_ken[11] = Image(Point(780,335), "fighters/ken/ken_1/luta/kenparado12.png")
sprites_Mbison = [0]*6
sprites_Mbison[0] = Image(Point(780, 335),"fighters/M.Bison/M.Bison_1/luta/MBisonparado1.png")
sprites_Mbison[1] = Image(Point(780, 335),"fighters/M.Bison/M.Bison_1/luta/MBisonparado2.png")
sprites_Mbison[2] = Image(Point(780, 335),"fighters/M.Bison/M.Bison_1/luta/MBisonparado5.png")
sprites_Mbison[3] = Image(Point(780, 335),"fighters/M.Bison/M.Bison_1/luta/MBisonparado6.png")
sprites_Mbison[4] = Image(Point(780, 335),"fighters/M.Bison/M.Bison_1/luta/MBisonparado5.png")
sprites_Mbison[5] = Image(Point(780, 335),"fighters/M.Bison/M.Bison_1/luta/MBisonparado2.png")
sprites_goku = [0]*6
sprites_goku[0] = Image(Point(780,335), "fighters/Goku_base/goku_1/luta/GokuBase_parado1.png")
sprites_goku[1] = Image(Point(780,335), "fighters/Goku_base/goku_1/luta/GokuBase_parado2.png")
sprites_goku[2] = Image(Point(780,335), "fighters/Goku_base/goku_1/luta/GokuBase_parado3.png")
sprites_goku[3] = Image(Point(780,335), "fighters/Goku_base/goku_1/luta/GokuBase_parado4.png")
sprites_goku[4] = Image(Point(780,335), "fighters/Goku_base/goku_1/luta/GokuBase_parado3.png")
sprites_goku[5] = Image(Point(780,335), "fighters/Goku_base/goku_1/luta/GokuBase_parado2.png")
sprites_freeza = [0]*10
sprites_freeza[0] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado1.png")
sprites_freeza[1] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado2.png")
sprites_freeza[2] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado3.png")
sprites_freeza[3] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado4.png")
sprites_freeza[4] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado5.png")
sprites_freeza[5] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado6.png")
sprites_freeza[6] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado7.png")
sprites_freeza[7] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado8.png")
sprites_freeza[8] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado9.png")
sprites_freeza[9] = Image(Point(730,335), "fighters/Freeza/freeza_1/luta/freezaparado10.png")
sprites_vegeta = [0]*6
sprites_vegeta[0] = Image(Point(780,335), "fighters/Vegeta/vegeta_1/luta/vegetaparado1.png")
sprites_vegeta[1] = Image(Point(780,335), "fighters/Vegeta/vegeta_1/luta/vegetaparado2.png")
sprites_vegeta[2] = Image(Point(780,335), "fighters/Vegeta/vegeta_1/luta/vegetaparado3.png")
sprites_vegeta[3] = Image(Point(780,335), "fighters/Vegeta/vegeta_1/luta/vegetaparado4.png")
sprites_vegeta[4] = Image(Point(780,335), "fighters/Vegeta/vegeta_1/luta/vegetaparado3.png")
sprites_vegeta[5] = Image(Point(780,335), "fighters/Vegeta/vegeta_1/luta/vegetaparado2.png")
icone_ryu_area = Rectangle(Point(82,303),Point(213,457))
icone_ken_area = Rectangle(Point(214,303),Point(345,457))
icone_bison_area = Rectangle(Point(346,303),Point(477,457))
icone_goku_area = Rectangle(Point(82,142),Point(213,302))
icone_vegeta_area = Rectangle(Point(214,142),Point(345,302))
icone_freeza_area = Rectangle(Point(346,142),Point(477,302))
retangulo_exibicao = Rectangle(Point(700,150),Point(900,500))
retangulo_exibicao.setFill("white")
botao_dificuldade_area = Rectangle(Point(315,233),Point(645,266))
botao_dificuldade = Image(Point(480,250), "Arte/Buttons_and_Symbols/dificuldade.png")
botao_jogar_area = Rectangle(Point(405,230),Point(553,280))
botao_jogar = Image(Point(480,250),"Arte/Buttons_and_Symbols/jogar.png")
botao_retorno_area = Rectangle(Point(460,30),Point(930,70))
botao_retorno = Image(Point(700,50), "Arte/Buttons_and_Symbols/retorno.png")
botao_configuracoes = Image(Point(480,200), "Arte/Buttons_and_Symbols/configuracoes.png")
botao_configuracoes_area = Rectangle(Point(290,180),Point(671,215))
botao_facil = Image(Point(480,290), "Arte/Buttons_and_Symbols/facil.png")
botao_facil_area = Rectangle(Point(402,266),Point(555,310))
botao_normal = Image(Point(480,220), "Arte/Buttons_and_Symbols/normal.png")
botao_normal_area = Rectangle(Point(392,200),Point(565,240))
botao_dificil = Image(Point(480,160), "Arte/Buttons_and_Symbols/dificil.png")
botao_dificil_area = Rectangle(Point(375,135),Point(582,180))
botao_som = Image(Point(480,200), "Arte/Buttons_and_Symbols/som.png") #200
botao_som_area = Rectangle(Point(430,180),Point(530,220))
botao_ligado = Image(Point(480,250), "Arte/Buttons_and_Symbols/ligado.png")
botao_ligado_area = Rectangle(Point(390,230),Point(570,280))
botao_desligado = Image(Point(480,200), "Arte/Buttons_and_Symbols/desligado.png")
botao_desligado_area = Rectangle(Point(340,180),Point(610,220))
botao_sair = Image(Point(480,150), "Arte/Buttons_and_Symbols/sair.png")
botao_sair_area = Rectangle(Point(420,130),Point(530,170))
certeza = Image(Point(480,240), "Arte/Buttons_and_Symbols/certeza.png")
botao_sim = Image(Point(400,150), "Arte/Buttons_and_Symbols/sim.png")
botao_sim_area = Rectangle(Point(355,130),Point(445,175))
botao_nao = Image(Point(600,150), "Arte/Buttons_and_Symbols/nao.png")
botao_nao_area = Rectangle(Point(555,130),Point(645,175))
botao_um_jogador_area = Rectangle(Point(380,230),Point(580,280))
botao_um_jogador = Image(Point(480,255), "Arte/Buttons_and_Symbols/umjogador.png")
botao_dois_jogadores_area = Rectangle(Point(380,140),Point(580,190))
botao_dois_jogadores = Image(Point(480,165), "Arte/Buttons_and_Symbols/doisjogadores.png")
botao_confirmar_area = Rectangle(Point(649,100),Point(911,140))
botao_confirmar = Image(Point(780,120),"Arte/Buttons_and_Symbols/confirmar.png")
botao_confirmar2 = Image(Point(480,280),"Arte/Buttons_and_Symbols/confirmar2.png")
confirmar_area = Rectangle(Point(405,271),Point(555,289))
escolha_mapa = Image(Point(470,530), "Arte/Buttons_and_Symbols/escolhamapa.png")
escolha_lutador = Image(Point(470,520), "Arte/Buttons_and_Symbols/escolha_lutador.png")
sair_area = Rectangle(Point(265,205),Point(695,280))
voltar_area = Rectangle(Point(265,305),Point(695,353))
trocar_area = Rectangle(Point(265,256),Point(695,304))
miniaturas_fundos = [0]*12
miniaturas_area = [0]*4
miniaturas_area[0] = Rectangle(Point(100,50),Point(400,250))
miniaturas_area[1] = Rectangle(Point(100,300),Point(400,500))
miniaturas_area[2] = Rectangle(Point(560,50),Point(860,250))
miniaturas_area[3] = Rectangle(Point(560,300),Point(860,500))
seta = Image(Point(915,275), "Arte/Buttons_and_Symbols/seta.png")
seta_back = Image(Point(45,275), "Arte/Buttons_and_Symbols/seta_back.png")
seta_area = Rectangle(Point(900,250),Point(930,300))
seta_area.setFill('white')
seta_area_back = Rectangle(Point(30,250),Point(60,300))
seta_area_back.setFill('white')
mapa = 0
contador_de_frames = 0
contador_de_frames2 = 0
contador_de_frames4 = 0
contador_de_frames5 = 0
contador_de_frames6 = 0
contador_de_frames7 = 0
aba_do_menu = -1
aba_clicada = 0
aba_atual = -1
parametro_IA = 0
moldura = Image(Point(250,150),"Arte/Buttons_and_Symbols/borda_mapa.png")
molduraPersonagem = Image(Point(146,380), "Arte/Buttons_and_Symbols/borda_p1.png")
molduraPersonagem2 = Image(Point(146,380), "Arte/Buttons_and_Symbols/borda_p2.png") 
posicao = 1
posicao1 = 1
aux_map1 = 0
aux_map2 = 0
aux_map3 = 0
aux_map4 = 0
porto = [None]*8
porto[0] = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto1.png")
porto[1] = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto2.png")
porto[2] = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto3.png")
porto[3] = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto4.png")
porto[4] = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto5.png")
porto[5] = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto6.png")
porto[6] = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto7.png")
porto[7] = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto8.png")
porto_fundo = Image(Point(250,150),"Arte/MAPS/Porto/Menu/porto8.png")
graveyard = [0]*16
graveyard[0] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard1.png")
graveyard[1] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard2.png")
graveyard[2] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard3.png")
graveyard[3] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard4.png")
graveyard[4] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard5.png")
graveyard[5] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard6.png")
graveyard[6] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard7.png")
graveyard[7] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard8.png")
graveyard[8] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard9.png")
graveyard[9] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard10.png")
graveyard[10] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard11.png")
graveyard[11] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard12.png")
graveyard[12] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard13.png")
graveyard[13] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard14.png")
graveyard[14] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard15.png")
graveyard[15] = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard16.png")
graveyard_fundo = Image(Point(250,150), "Arte/MAPS/graveyard/graveyard1.png")

kids = [0]*20
kids[0] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids0.png")
kids[1] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids1.png")
kids[2] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids2.png")
kids[3] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids3.png")
kids[4] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids4.png")
kids[5] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids5.png")
kids[6] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids6.png")
kids[7] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids7.png")
kids[8] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids8.png")
kids[9] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids9.png")
kids[10] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids10.png")
kids[11] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids11.png")
kids[12] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids12.png")
kids[13] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids13.png")
kids[14] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids14.png")
kids[15] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids15.png")
kids[16] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids16.png")
kids[17] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids17.png")
kids[18] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids18.png")
kids[19] = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids19.png")
kids_fundo = Image(Point(250,150), "Arte/MAPS/Kids/Menu/kids1.png")

tribal = [0]*36
tribal[0] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal0.png")
tribal[1] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal1.png")
tribal[2] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal2.png")
tribal[3] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal3.png")
tribal[4] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal4.png")
tribal[5] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal5.png")
tribal[6] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal6.png")
tribal[7] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal7.png")
tribal[8] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal8.png")
tribal[9] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal9.png")
tribal[10] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal10.png")
tribal[11] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal11.png")
tribal[12] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal12.png")
tribal[13] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal13.png")
tribal[14] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal14.png")
tribal[15] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal15.png")
tribal[16] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal16.png")
tribal[17] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal17.png")
tribal[18] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal18.png")
tribal[19] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal19.png")
tribal[20] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal20.png")
tribal[21] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal21.png")
tribal[22] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal22.png")
tribal[23] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal23.png")
tribal[24] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal24.png")
tribal[25] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal25.png")
tribal[26] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal26.png")
tribal[27] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal27.png")
tribal[28] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal28.png")
tribal[29] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal29.png")
tribal[30] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal30.png")
tribal[31] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal31.png")
tribal[32] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal32.png")
tribal[33] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal33.png")
tribal[34] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal34.png")
tribal[35] = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal35.png")
tribal_fundo = Image(Point(250,400),"Arte/MAPS/Tribal/Menu/tribal1.png")

punk_toilet = [None]*16
punk_toilet[0] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet1.png")
punk_toilet[1] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet2.png")
punk_toilet[2] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet3.png")
punk_toilet[3] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet4.png")
punk_toilet[4] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet5.png")
punk_toilet[5] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet6.png")
punk_toilet[6] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet7.png")
punk_toilet[7] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet8.png")
punk_toilet[8] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet9.png")
punk_toilet[9] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet10.png")
punk_toilet[10] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet11.png")
punk_toilet[11] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet12.png")
punk_toilet[12] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet13.png")
punk_toilet[13] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet14.png")
punk_toilet[14] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet15.png")
punk_toilet[15] = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet16.png")
punk_toilet_fundo = Image(Point(250,400),"Arte/MAPS/Punk/Menu/punk_toilet16.png")

riot = [0]*8
riot[0] = Image(Point(250,400),"Arte/MAPS/Riot/Menu/riot0.png")
riot[1] = Image(Point(250,400),"Arte/MAPS/Riot/Menu/riot1.png")
riot[2] = Image(Point(250,400),"Arte/MAPS/Riot/Menu/riot2.png")
riot[3] = Image(Point(250,400),"Arte/MAPS/Riot/Menu/riot3.png")
riot[4] = Image(Point(250,400),"Arte/MAPS/Riot/Menu/riot4.png")
riot[5] = Image(Point(250,400),"Arte/MAPS/Riot/Menu/riot5.png")
riot[6] = Image(Point(250,400),"Arte/MAPS/Riot/Menu/riot6.png")
riot[7] = Image(Point(250,400),"Arte/MAPS/Riot/Menu/riot7.png")
riot_fundo = Image(Point(250,400), "Arte/MAPS/Riot/Menu/riot1.png")

air_crystal = [None]*8
air_crystal[0] = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal1.png")
air_crystal[1] = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal2.png")
air_crystal[2] = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal3.png")
air_crystal[3] = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal4.png")
air_crystal[4] = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal5.png")
air_crystal[5] = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal6.png")
air_crystal[6] = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal7.png")
air_crystal[7] = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal8.png")
air_crystal_fundo = Image(Point(710,150), "Arte/MAPS/Air_Crystal/Menu/air_crystal8.png")

boat = [0]*14
boat[0] = Image(Point(710,150), "Arte/MAPS/Boat/boat0.png")
boat[1] = Image(Point(710,150), "Arte/MAPS/Boat/boat1.png")
boat[2] = Image(Point(710,150), "Arte/MAPS/Boat/boat2.png")
boat[3] = Image(Point(710,150), "Arte/MAPS/Boat/boat3.png")
boat[4] = Image(Point(710,150), "Arte/MAPS/Boat/boat4.png")
boat[5] = Image(Point(710,150), "Arte/MAPS/Boat/boat5.png")
boat[6] = Image(Point(710,150), "Arte/MAPS/Boat/boat6.png")
boat[7] = Image(Point(710,150), "Arte/MAPS/Boat/boat7.png")
boat[8] = Image(Point(710,150), "Arte/MAPS/Boat/boat8.png")
boat[9] = Image(Point(710,150), "Arte/MAPS/Boat/boat9.png")
boat[10] = Image(Point(710,150), "Arte/MAPS/Boat/boat10.png")
boat[11] = Image(Point(710,150), "Arte/MAPS/Boat/boat11.png")
boat[11] = Image(Point(710,150), "Arte/MAPS/Boat/boat12.png")
boat[12] = Image(Point(710,150), "Arte/MAPS/Boat/boat13.png")
boat[13] = Image(Point(710,150), "Arte/MAPS/Boat/boat14.png")
boat_fundo = Image(Point(710,150),"Arte/MAPS/Boat/boat1.png")

bet = [0]*24
bet[0] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet0.png")
bet[1] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet1.png")
bet[2] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet2.png")
bet[3] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet3.png")
bet[4] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet4.png")
bet[5] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet5.png")
bet[6] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet6.png")
bet[7] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet7.png")
bet[8] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet8.png")
bet[9] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet9.png")
bet[10] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet10.png")
bet[11] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet11.png")
bet[12] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet12.png")
bet[13] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet13.png")
bet[14] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet14.png")
bet[15] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet15.png")
bet[16] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet16.png")
bet[17] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet17.png")
bet[18] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet18.png")
bet[19] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet19.png")
bet[20] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet20.png")
bet[21] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet21.png")
bet[22] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet22.png")
bet[23] = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet23.png")
bet_fundo = Image(Point(710,150), "Arte/MAPS/Bet/Menu/bet1.png")



bonito_tarde = [None]*16
bonito_tarde[0] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde1.png")
bonito_tarde[1] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde2.png")
bonito_tarde[2] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde3.png")
bonito_tarde[3] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde4.png")
bonito_tarde[4] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde5.png")
bonito_tarde[5] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde6.png")
bonito_tarde[6] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde7.png")
bonito_tarde[7] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde8.png")
bonito_tarde[8] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde9.png")
bonito_tarde[9] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde10.png")
bonito_tarde[10] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde11.png")
bonito_tarde[11] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde12.png")
bonito_tarde[12] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde13.png")
bonito_tarde[13] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde14.png")
bonito_tarde[14] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde15.png")
bonito_tarde[15] = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde16.png")
bonito_tarde_fundo = Image(Point(710,400), "Arte/MAPS/Bonito_tarde/Menu/bonito_tarde16.png")

korea = [None]*8
korea[0] = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea0.png")
korea[1] = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea1.png")
korea[2] = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea2.png")
korea[3] = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea3.png")
korea[4] = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea4.png")
korea[5] = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea5.png")
korea[6] = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea6.png")
korea[7] = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea7.png")
korea_fundo = Image(Point(710,400), "Arte/MAPS/Korea/Menu/korea7.png")

y_train = [0]*8
y_train[0] = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train0.png")
y_train[1] = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train1.png")
y_train[2] = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train2.png")
y_train[3] = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train3.png")
y_train[4] = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train4.png")
y_train[5] = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train5.png")
y_train[6] = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train6.png")
y_train[7] = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train7.png")
y_train_fundo = Image(Point(710,400), "Arte/MAPS/Y_Train/Menu/y_train1.png")

p_mapa = Point(480,300)
###Cria mapa###
Limite_mapa_d = 128
Limite_mapa_e = 760
posicao_originalY = 190
posicao_original_X1 = 150
posicao_original_X2 = 810
youwin = Image(Point(480,290), "Arte/Buttons_and_Symbols/youwin.png")
youlose = Image(Point(480,290), "Arte/Buttons_and_Symbols/youlose.png")
player1wins = Image(Point(480,290), "Arte/Buttons_and_Symbols/player1wins.png")
player2wins = Image(Point(480,290), "Arte/Buttons_and_Symbols/player2wins.png")

while True:
	som,dificuldade,player1,player2,mapa,Fix = ChamaMenu(contador,contador1,aba_atual,som,dificuldade,mapa)
	janela.update()
	fundo,numero_frames = selecionaMAPA(mapa)
	fundo.move(0,561*(numero_frames/2))
	start_time5 = time.time()
	elapsed_time5 = time.time() - start_time

	###Selecionar posicao dos players 1 e 2###

	posicao_p1 = Point(posicao_original_X1, posicao_originalY)
	posicao_p2 = Point(posicao_original_X2, posicao_originalY)

	###Cria a lista dos sprites da intro para o player 1 e 2###

	sprite_intro = list(criar_sprite_intro(player1))
	p1_intro = []
	cont_1 = 0
	while(cont_1 < len(sprite_intro)):
		p1_intro.append(Image(posicao_p1, sprite_intro[cont_1]))
		cont_1 += 1

	sprite_intro = list(criar_sprite_intro(player2*10))
	p2_intro = []
	cont_1 = 0
	while(cont_1 < len(sprite_intro)):
		p2_intro.append(Image(posicao_p2, sprite_intro[cont_1]))
		cont_1 += 1

	###Cria a Lista com os sprites de vitoria do p1 e p2###

	p_winner = []
	sprites_win = aux_criar_sprites_winner(player1) + aux_criar_sprites_winner(player2)
	cont_1 = 0
	aux = 0
	while(cont_1 < len(sprites_win)):
		p_winner.append([])
		cont_2 = 0
		if(cont_1 < 2):
			while(cont_2 < len(sprites_win[cont_1])):
				p_winner[cont_1].append(Image(posicao_p1, sprites_win[cont_1][cont_2]))
				cont_2 += 1
		else:
			while(cont_2 < len(sprites_win[cont_1])):
				p_winner[cont_1].append(Image(posicao_p2, sprites_win[cont_1][cont_2]))
				cont_2 += 1
		cont_1 += 1

	###Cria a Listas dos sprites e dos especiais para o player 1 e 2###

	player = []
	player.append([])
	player.append([])
	especial = []
	especial.append([])
	especial.append([])

	###Cria os sprites de luta do player 1###

	sprites_p1 = aux_criar_personagem(player1)
	num_sprites = list(sprites_p1[0])
	name_sprites = list(sprites_p1[1])
	cont_1 = 0
	aux = 0
	while(cont_1 < len(num_sprites)):
		player[0].append([])
		cont_2 = 0
		while(cont_2 < eval(num_sprites[cont_1])):
		    player[0][cont_1].append(Image(posicao_p1, name_sprites[aux]))
		    aux += 1
		    cont_2 += 1
		cont_1 += 1

	p1_info= [0]*8
	p1_info[0] = 350 #altura do personagem
	p1_info[5] = 50 #distancia do centro ate a ponta
	p1_info[6] = 20 #tamanho do especial 1
	if(player1 == 1):
		p1_info[1] = 200 # tamanho do braco
		p1_info[3] = 140 #tamanho perna
		p1_info[2] = 200 # altura soco
		p1_info[4] = 225 #altura que o pe chega
		p1_info[7] = 150 #altura do especial 1
		sprite_dano_chute_p1 = 3
		sprite_dano_soco_p1 = 2
		sprite_dano_especial1_p1 = 4
		sprite_getUp_p1 = 9
		especialAltura_p1 = posicao_p1.getY()
		dano_soco1 = 6
		dano_chute1 = 8
		dano_especial1 = 12
	elif(player1 == 2):
		p1_info[1] = 200 # tamanho do braco
		p1_info[3] = 200 #tamanho perna
		p1_info[2] = 200 # altura soco
		p1_info[4] = 175 #altura que o pe chega
		p1_info[7] = 150 #altura do especial 1
		sprite_dano_chute_p1 = 7
		sprite_dano_soco_p1 = 2
		sprite_dano_especial1_p1 = 5
		sprite_getUp_p1 = 9
		especialAltura_p1 = posicao_p1.getY()
		dano_soco1 = 6
		dano_chute1 = 8
		dano_especial1 = 12
	elif(player1 == 3):
		p1_info[1] = 300 # tamanho do braco
		p1_info[3] = 300 #tamanho perna
		p1_info[2] = 200 # altura soco
		p1_info[4] = 200 #altura que o pe chega
		p1_info[7] = 200 #altura do especial 1
		sprite_dano_chute_p1 = 4
		sprite_dano_soco_p1 = 5
		sprite_dano_especial1_p1 = 7
		#sprite_getUp_p1 = 9
		especialAltura_p1 = posicao_p1.getY() + 20
		dano_soco1 = 6
		dano_chute1 = 8
		dano_especial1 = 12
	elif(player1 == 4):
		p1_info[1] = 140 # tamanho do braco
		p1_info[3] = 200 #tamanho perna
		p1_info[2] = 200 # altura soco
		p1_info[4] = 225 #altura que o pe chega
		p1_info[7] = 200 #altura do especial 1
		sprite_dano_chute_p1 = 4
		sprite_dano_soco_p1 = 4
		sprite_dano_especial1_p1 = 7
		#sprite_getUp_p1 = 0
		especialAltura_p1 = posicao_p1.getY() + 50
		dano_soco1 = 6
		dano_chute1 = 8
		dano_especial1 = 15
	elif(player1 == 5):
		p1_info[1] = 150 # tamanho do braco
		p1_info[3] = 180 #tamanho perna
		p1_info[2] = 160 # altura soco
		p1_info[4] = 180 #altura que o pe chega
		p1_info[7] = 220 #altura do especial 1
		sprite_dano_chute_p1 = 3
		sprite_dano_soco_p1 = 4
		sprite_dano_especial1_p1 = 4
		#sprite_getUp_p1 = 0
		especialAltura_p1 = posicao_p1.getY() + 30
		dano_soco1 = 6
		dano_chute1 = 8
		dano_especial1 = 15
	elif(player1 == 6):
		p1_info[1] = 150 # tamanho do braco
		p1_info[3] = 200 #tamanho perna
		p1_info[2] = 200 # altura soco
		p1_info[4] = 200 #altura que o pe chega
		p1_info[7] = 180 #altura do especial 1
		sprite_dano_chute_p1 = 4
		sprite_dano_soco_p1 = 4
		sprite_dano_especial1_p1 = 6
		#sprite_getUp_p1 = 0
		especialAltura_p1 = posicao_p1.getY()
		dano_soco1 = 6
		dano_chute1 = 8
		dano_especial1 = 15

	###Cria sprite dos especiais de energia do player 1###

	sprites_especial_p1 = seleciona_especial(player1)
	especial[0] = list(posiciona_especial(sprites_especial_p1, posicao_p1))

	####Cria os sprites de luta do player 2###

	sprites_p2 = aux_criar_personagem(player2)
	num_sprites = list(sprites_p2[0])
	name_sprites = list(sprites_p2[1])
	cont_1 = 0
	aux = 0
	while(cont_1 < len(num_sprites)):
		player[1].append([])
		cont_2 = 0
		while(cont_2 < eval(num_sprites[cont_1])):
		    player[1][cont_1].append(Image(posicao_p2, name_sprites[aux]))
		    aux += 1
		    cont_2 += 1
		cont_1 += 1

	p2_info= [0]*8
	p2_info[0] = 350 #altura do personagem
	p2_info[5] = 40 #distancia do centro ate a ponta
	p2_info[6] = 20 #tamanho do especial 1
	if(player2 == 1):
		p2_info[1] = 190 # tamanho do braco
		p2_info[3] = 140 #tamanho perna
		p2_info[2] = 200 #altura soco
		p2_info[4] = 225 #altura que o pe chega
		p2_info[7] = 150 #altura do especial 1
		sprite_dano_chute_p2 = 3
		sprite_dano_soco_p2 = 2
		sprite_dano_especial1_p2 = 4
		sprite_getUp_p2 = 5
		especialAltura_p2 = posicao_p2.getY()
		dano_soco2 = 6
		dano_chute2 = 8
		dano_especial2 = 12
	elif(player2 == 2):
		p2_info[1] = 190 # tamanho do braco
		p2_info[3] = 200 #tamanho perna
		p2_info[2] = 185 #altura soco
		p2_info[4] = 175 #altura que o pe chega
		p2_info[7] = 160 #altura do especial 1
		sprite_dano_chute_p2 = 7
		sprite_dano_soco_p2 = 2
		sprite_dano_especial1_p2 = 5
		sprite_getUp_p2 = 5
		especialAltura_p2 = posicao_p2.getY()
		dano_soco2 = 6
		dano_chute2 = 8
		dano_especial2 = 12
	elif(player2 == 3):
		p2_info[1] = 300 # tamanho do braco
		p2_info[3] = 300 #tamanho perna
		p2_info[2] = 200 #altura soco
		p2_info[4] = 200 #altura que o pe chega
		p2_info[7] = 200 #altura do especial 1
		sprite_dano_chute_p2 = 4
		sprite_dano_soco_p2 = 5
		sprite_dano_especial1_p2 = 7
		#sprite_getUp_p2 = 0
		especialAltura_p2 = posicao_p2.getY() + 20
		dano_soco2 = 6
		dano_chute2 = 8
		dano_especial2 = 12
	elif(player2 == 4):
		p2_info[1] = 140 # tamanho do braco
		p2_info[3] = 200 #tamanho perna
		p2_info[2] = 200 #altura soco
		p2_info[4] = 225 #altura que o pe chega
		p2_info[7] = 200 #altura do especial 1
		sprite_dano_chute_p2 = 4
		sprite_dano_soco_p2 = 4
		sprite_dano_especial1_p2 = 7
		#sprite_getUp_p2 = 0
		especialAltura_p2 = posicao_p2.getY() + 50
		dano_soco2 = 6
		dano_chute2 = 8
		dano_especial2 = 15
	elif(player2 == 5):
		p2_info[1] = 150 # tamanho do braco
		p2_info[3] = 180 #tamanho perna
		p2_info[2] = 160 #altura soco
		p2_info[4] = 180 #altura que o pe chega
		p2_info[7] = 220 #altura do especial 1
		sprite_dano_chute_p2 = 3
		sprite_dano_soco_p2 = 4
		sprite_dano_especial1_p2 = 4
		#sprite_getUp_p2 = 0
		especialAltura_p2 = posicao_p2.getY() + 30
		dano_soco2 = 6
		dano_chute2 = 8
		dano_especial2 = 15
	elif(player2 == 6):
		p2_info[1] = 150 # tamanho do braco
		p2_info[3] = 200 #tamanho perna
		p2_info[2] = 200 #altura soco
		p2_info[4] = 200 #altura que o pe chega
		p2_info[7] = 180 #altura do especial 1
		sprite_dano_chute_p2 = 4
		sprite_dano_soco_p2 = 4
		sprite_dano_especial1_p2 = 6
		#sprite_getUp_p2 = 0
		especialAltura_p2 = posicao_p2.getY()
		dano_soco2 = 6
		dano_chute2 = 8
		dano_especial2 = 15

	###Cria sprite dos especiais de energia do player 2###

	sprites_especial_p2 = seleciona_especial(player2)
	especial[1] = list(posiciona_especial(sprites_especial_p2, posicao_p2))

	###Cria as variáveis de estado dos players 1 e 2 e do mapa###

	###estado_player: 0 parado, 1 walkF, 2 walkB, 3 soco, 4 defesa, 5 agachar, 6 pular, 7 chute, 8 especial 1, 9dano leve, 10 dano leve no ar, 11 dano grande###

	estado_player = [0]*2
	sprite_parado = [0]*2
	sprite_walkDireita = [0]*2
	sprite_walkEsquerda = [0]*2
	sprite_punch = [0]*2
	sprite_defender = [0]*2
	sprite_agachar = [0]*2
	sprite_jump = [0]*2
	sprite_chute = [0]*2
	sprite_especial1 = [0]*2
	sprite_danoLeve = [0]*2
	sprite_danoLeveAr = [0]*2
	sprite_danoHard = [0]*2
	sprite_getUp = [0]*2
	lado_sprite = [0]*2
	lado_sprite[1] = 1
	especial_ativo = [0]*2
	sprite_energia1 = [0]*2
	hitespecial1_ativo= [0]*2
	sprite_ener1hit = [0]*2
	lado_energia = [0]*2
	lado_energia[1] = 1
	###Cria vetor que contém as posições de pm, p1 e p2###

	posicao = [0]*3	
	posicao[0] = p_mapa
	posicao[1] = posicao_p1
	posicao[2] = posicao_p2

	###Cria variaveis de posicao dos especiais de p1 e p2###

	posicao_especial1_p1 = especial[0][0][0].getAnchor()
	posicao_especial1_p2 = especial[1][0][0].getAnchor()

	###Cria variáveis do HP do jogador 1 e 2###

	player1_hp = 100
	player2_hp = 100

	BarraHP1 = Rectangle(Point(20,487), Point(420, 530))
	BarraHP1.setFill("yellow")
	BarraHP2 = Rectangle(Point(940,487), Point(540, 530))
	BarraHP2.setFill("yellow")

	###Cria variáveis da stamina do jogador 1 e 2###

	player1_sta = 100
	player2_sta = 100
	estado_stamina = [1]*2

	BarraSTA1 = Rectangle(Point(20,460), Point(220, 484))
	BarraSTA1.setFill("green")
	BarraSTA2 = Rectangle(Point(940,460), Point(740, 484))
	BarraSTA2.setFill("green")

	###Cria variaveis de energia do jogador 1 e 2###

	player1_Ki = 0
	player2_Ki = 0

	BarraKI1 = Rectangle(Point(220,460), Point(420, 484))
	BarraKI1.setFill("blue")
	BarraKI2 = Rectangle(Point(540,460), Point(740, 484))
	BarraKI2.setFill("blue")

	###Declara variáveis de inicio para o jogo###

	delay_p1 = 0
	delay_p2 = 0
	aux_hitLeveAr1 = 0.4
	aux_hitLeveAr2 = 0.4
	velocidade_hitLeveAr1 = 6
	velocidade_hitLeveAr2 = 6
	velocidade_hitHard1 = 6
	velocidade_hitHard2 = 6
	tempo_hitHard1 = 0
	tempo_hitHard2 = 0
	aux_hitHard1 = 0
	aux_hitHard2 = 0
	tempo_getUp1 = 0
	tempo_getUp2 = 0
	tempo_pulo_p1 = 0
	tempo_pulo_p2 = 0
	velocidade_pulo1 = 12	
	velocidade_pulo2 = 12
	aux_pulo_p1 = 0
	aux_pulo_p2 = 0
	tempo_mov_p1 = 0
	tempo_mov_p2 = 0
	tempo_especial_p1 = 0
	tempo_especial_p2 = 0
	tempo_energia1_p1 = 0
	tempo_energia1_p2 = 0
	tempo_hitenergia1_p1 = 0
	tempo_hitenergia1_p2 = 0
	lost_stamina1 = 0
	lost_stamina2 = 0
	t_move_p1 = 0
	t_move_p2 = 0
	t_def_p1 = 0
	t_def_p2 = 0
	t_veri_p1 = 0
	t_veri_p2 = 0
	limite_mapa = 0

	###Cria lista q indica quais teclas foram apertadas por p1 e p2###

	tecla = []
	tecla.append([])
	tecla.append([])

	###Selecionar som de fundo###
	
	som_ambiente(mapa)

	###Cria variáveis para o fps###

	t_fps = 0
	fps = 0
	FPS = Text(Point(950,540), str(fps))
	FPS.draw(janela)

	###Intro da luta###
	fundo.draw(janela)
	versus.undraw()
	versus.draw(janela)
	t_inicial_1 = 0
	timer_1 = time.time() - t_inicial_1
	timer_2 = 0
	t_inicial_2 = 0
	parametro_FIGHT = False
	parametro2 = True
	contador_de_rounds = 0
	timer_1,parametro2,parametro_FIGHT = RoundShow(fight5,timer_1,contador_de_rounds,parametro2,parametro_FIGHT,t_inicial_1,reset)
	t_before = 0
	end = 0
	cont_intro = 0
	tempo_intro = 0
	contador_de_rounds = 0
	win1 = 0
	win2 = 0
	teste = True
	if(len(p1_intro) > len(p2_intro)):
		aux_intro = len(p1_intro)
	else:
		aux_intro = len(p2_intro)
	while True:
		elapsed_time5 = time.time() - start_time5
		if elapsed_time5 > 0.1:
		    contador = movimento_fundo_menus(fundo,contador,numero_frames)
		    elapsed_time5 = 0
		    start_time5 = time.time()
		if(cont_intro >= len(p1_intro)):
		    t_move_p1 = verificar_sprite(t_move_p1, 0, player1)
		    p1_intro[-1].undraw()
		if(cont_intro >= len(p2_intro)):
		    t_move_p2 = verificar_sprite(t_move_p2, 1, player2)
		    p2_intro[-1].undraw()
		if(cont_intro == aux_intro):
		    t_intro = None
		    cont_intro = None
		    break
		if(time.clock() - t_before > 0.01666):
		    cont_intro, tempo_intro = intro_sprite(cont_intro, tempo_intro)
		    janela.update()
		    fps += 1
		    t_before = time.clock()
		if(time.clock() - t_fps > 1):	
		    FPS.undraw()
		    FPS = Text(Point(940,540), str(fps))
		    FPS.draw(janela)
		    fps = 0
		    t_fps = time.clock()
	###Luta começa###
	timer_2 = 0
	t_inicial = 0
	t_inicial2 = 0
	timer3 = 0
	check = 9
	contador_de_rounds = 0
	reinicia_round = 0
	end_game = 0	
	t_fps = time.clock()
	fps = 0
	aba_atual = 18
	aba_do_menu = 18
	t_before = time.clock()
	timer_1,parametro2,parametro_FIGHT = RoundShow(fight5,timer_1,contador_de_rounds,parametro2,parametro_FIGHT,t_inicial_1,reset)
	menu_ingame = Image(Point(480,280), "Arte/Buttons_and_Symbols/menu_ingame.png")
	while (contador_de_rounds<3) and (win1 < 2) and (win2 < 2):
		t_inicial_1 = time.time()
		timer_1 = time.time() - t_inicial_1
		###Zera variáveis de inicio para o jogo###
		delay_p1 = 0
		delay_p2 = 0
		aux_hitLeveAr1 = 0.4
		aux_hitLeveAr2 = 0.4
		velocidade_hitLeveAr1 = 8
		velocidade_hitLeveAr2 = 8
		velocidade_hitHard1 = 6
		velocidade_hitHard2 = 6
		tempo_hitHard1 = 0
		tempo_hitHard2 = 0
		aux_hitHard1 = 0
		aux_hitHard2 = 0
		tempo_getUp1 = 0
		tempo_getUp2 = 0
		tempo_pulo_p1 = 0
		tempo_pulo_p2 = 0
		velocidade_pulo1 = 12	
		velocidade_pulo2 = 12
		aux_pulo_p1 = 0
		aux_pulo_p2 = 0
		tempo_mov_p1 = 0
		tempo_mov_p2 = 0
		tempo_especial_p1 = 0
		tempo_especial_p2 = 0
		tempo_energia1_p1 = 0
		tempo_energia1_p2 = 0
		tempo_hitenergia1_p1 = 0
		tempo_hitenergia1_p2 = 0
		lost_stamina1 = 0
		lost_stamina2 = 0
		t_move_p1 = 0
		t_move_p2 = 0
		t_def_p1 = 0
		t_def_p2 = 0
		t_veri_p1 = 0
		t_veri_p2 = 0
		limite_mapa = 0	
		player1_hp = 100
		player2_hp = 100
		player1_sta = 100
		player2_sta = 100
		barra_hp(1)
		barra_hp(2)
		barra_stamina(1)
		barra_stamina(2)
		barra_ki(1)
		barra_ki(2)
		borda_hp.undraw()
		borda_hp2.undraw()
		borda_Ki2.undraw()
		borda_Ki.undraw()
		borda_stamina2.undraw()
		borda_stamina.undraw()
		borda_hp.draw(janela)
		borda_hp2.draw(janela)
		borda_Ki2.draw(janela)
		borda_Ki.draw(janela)
		borda_stamina2.draw(janela)
		borda_stamina.draw(janela)
		parametro = True
		if(contador_de_rounds != 0):
			reinicia_round = 1
			reiniciaRound(estado_player[0], estado_player[1])
		start_time7 = 0
		while parametro == True:
			timer_1,parametro2,parametro_FIGHT = RoundShow(fight5,timer_1,contador_de_rounds,parametro2,parametro_FIGHT,t_inicial_1,reset)
			if parametro_FIGHT == True:
				timer2,parametro_FIGHT,reset,t_inicial_2 = fight(timer_2,parametro_FIGHT,t_inicial_2,reset)
			check = 9
			menu_ingame.undraw()
			delay_hit = time.time() - start_time7
			if 9 in janela.checkKey():
				menu_ingame.draw(janela)
				teste = True
				while teste == True:
					check = CheckIngame(janela.getMouse(),check)
					if check != 9:
						if check == 18:
							teste = False
							menu_ingame.undraw()
						if check == 19:
							parametro = False
							contador_de_rounds = 3
							menu_ingame.undraw()
							break
						if check == 23:
							janela.close()
			else:
				elapsed_time5 = time.time() - start_time5
				if elapsed_time5 > 0.1:
					contador = movimento_fundo_menus(fundo,contador,numero_frames)
					elapsed_time5 = 0
					start_time5 = time.time()
					parametro_IA,delay_hit,start_time7 = EscolheAcaoIA(dificuldade,posicao[1],posicao[2],delay_hit,start_time7)
				if(time.clock() - t_before > 0.01666):
					posicao,timer = controle(janela.checkKey(), posicao,num_jogadores,parametro_IA)
					trocar_lado(posicao_p1.getX(), posicao_p2.getX())	
					t_move_p1 = verificar_sprite(t_move_p1, 0, player1)
					t_move_p2 = verificar_sprite(t_move_p2, 1, player2)
					if(reinicia_round == 0):
						t_veri_p1 = verifica_tecla(tecla[0], estado_player[0], t_veri_p1, 1)
						t_veri_p2 = verifica_tecla(tecla[1], estado_player[1], t_veri_p2, 2)
					elif(reinicia_round == 1):
						restart_levanta(estado_player[0], estado_player[1])
					elif(reinicia_round == 2):
						move_restartRound(estado_player[0], estado_player[1])
					velocidade_pulo1 = action_jump(estado_player[0], velocidade_pulo1, 1)
					velocidade_pulo2 = action_jump(estado_player[1], velocidade_pulo2, 2)
					tempo_mov_p1, tempo_mov_p2 = action_soco(tempo_mov_p1, tempo_mov_p2, estado_player[0], estado_player[1])
					tempo_mov_p1, tempo_mov_p2 = action_chute(tempo_mov_p1, tempo_mov_p2, estado_player[0], estado_player[1])
					tempo_mov_p1, tempo_mov_p2 = action_especial1(tempo_mov_p1, tempo_mov_p2, estado_player[0], estado_player[1])
					if(especial_ativo[0] == 1):
						tempo_energia1_p1 = verificar_sprite_especial(tempo_energia1_p1, 0)
						move_especial(0)
						especial_ativo[0] = especial_end(sprite_especial1[0], 0)
						if(lado_energia[0] == 0):
							ponto_hit, topo_hitbox, base_hitbox = atualizaDadosInteracaoHitbox(especial[0][0][0].getAnchor(), posicao_p2,1,p1_info[6],p2_info[0],estado_player[1])
							dano = checarHit(especial[0][0][0].getAnchor(),posicao_p2,ponto_hit,p1_info[7],topo_hitbox,base_hitbox,p2_info[5])
						else:
							ponto_hit, topo_hitbox, base_hitbox = atualizaDadosInteracaoHitbox(especial[0][-1][0].getAnchor(), posicao_p2,1,p1_info[6],p2_info[0],estado_player[1])
							dano = checarHit(especial[0][-1][0].getAnchor(),posicao_p2,ponto_hit,p1_info[7],topo_hitbox,base_hitbox,p2_info[5])
						if(dano == 1):
								hit(2, dano_especial1, estado_player[1])
								undraw_especial(0)
								especial_ativo[0] = 0
								hitespecial1_ativo[0] = 1
								som_hit(som,"especial1")
								hitespecial1(0)
								tempo_hitenergia1_p1 = time.clock()	
					if(especial_ativo[1] == 1):
						tempo_energia1_p2 = verificar_sprite_especial(tempo_energia1_p2, 1)
						move_especial(1)
						especial_ativo[1] = especial_end(sprite_especial1[1], 1)
						if(lado_energia[1] == 0):
							ponto_hit, topo_hitbox, base_hitbox = atualizaDadosInteracaoHitbox(posicao_p1, especial[1][0][0].getAnchor(),2,p2_info[6],p1_info[0],estado_player[0])
							dano = checarHit(posicao_p1,especial[1][0][0].getAnchor(),ponto_hit,p2_info[7],topo_hitbox,base_hitbox,p1_info[5])
						else:
							ponto_hit, topo_hitbox, base_hitbox = atualizaDadosInteracaoHitbox(posicao_p1, especial[1][-1][0].getAnchor(),2,p2_info[6],p1_info[0],estado_player[0])
							dano = checarHit(posicao_p1,especial[1][-1][0].getAnchor(),ponto_hit,p2_info[7],topo_hitbox,base_hitbox,p1_info[5])
						if(dano == 1):
								hit(1, dano_especial2, estado_player[0])
								undraw_especial(1)
								especial_ativo[1] = 0
								hitespecial1_ativo[1] = 1
								hitespecial1(1)
								som_hit(som,"especial1")
								tempo_hitenergia1_p2 = time.clock()	
					levando_hitLeve(delay_p1, delay_p2, estado_player[0], estado_player[1])
					delay_p1, delay_p2 = levando_hitHard(delay_p1, delay_p2, estado_player[0], estado_player[1])
					delay_p1, delay_p2 = action_getUp(delay_p1, delay_p2, estado_player[0], estado_player[1])
					tempo_hitenergia1_p1 = verifica_hitespecial1(tempo_hitenergia1_p1, 0)
					tempo_hitenergia1_p2 = verifica_hitespecial1(tempo_hitenergia1_p2, 1)
					verifica_defesa()
					verifica_stamina()
					aumenta_energia()
					fps += 1
					t_before = time.clock()
				if(time.clock() - t_fps > 1):	
					FPS.undraw()
					FPS = Text(Point(940,540), str(fps))
					FPS.draw(janela)
					fps = 0
					t_fps = time.clock()
				if((player1_hp < 1 or player2_hp < 1) and (end_game == 0)):
					end_game = 1
				if(end_game == 2 and player1_hp < 1):
					win2 += 1
					if(estado_player[0] == 11 and estado_player[1] == 0):
						break
				if(end_game == 2 and player2_hp < 1):
					win1 += 1
					if(estado_player[1] == 11 and estado_player[0] == 0):
						break
		###Luta Termina###
		if check != 19:
			if(player1_hp < 1):
				vencedor = 2
				if(lado_sprite[0] == 0):
					winner_player = 3
				else:
					winner_player = 2
			else:
				vencedor = 1
				if(lado_sprite[1] == 0):
					winner_player = 1
				
				else:
					winner_player = 0

			sprites_winner = winner_sprite(0, winner_player)
			if(winner_player == 3 or winner_player == 2):
				undraw(estado_player[1], 2, lado_sprite[1])
			else:
				undraw(estado_player[0], 1, lado_sprite[0])
			tempo_winner = time.clock()
			t_before = time.clock()
			t_fps = 0
			fps = 0
			if num_jogadores == 1:
				if vencedor == 1:
					youwin.draw(janela)
					Narrador(som,vencedor,contador_de_rounds)
				elif vencedor == 2:
					youlose.draw(janela)
					Narrador(som,vencedor,contador_de_rounds)
			elif num_jogadores == 2:
				if vencedor == 1:
					player1wins.draw(janela)
				else:
					player2wins.draw(janela)
			while True:
				janela.update()
				elapsed_time5 = time.time() - start_time5
				if elapsed_time5 > 0.1:
					contador = movimento_fundo_menus(fundo,contador,numero_frames)
					elapsed_time5 = 0
					start_time5 = time.time()
				if(time.clock() - t_before > 0.01666):
					if(sprites_winner != 0):
						if(time.clock() - tempo_winner > 0.2):
							sprites_winner = winner_sprite(sprites_winner, winner_player)
							tempo_winner = time.clock()
					else:
						break
					fps += 1
					t_before = time.clock()
				if(time.clock() - t_fps > 1):	
					FPS.undraw()
					FPS = Text(Point(940,540), str(fps))
					FPS.draw(janela)
					fps = 0
					t_fps = time.clock()
			youwin.undraw()
			youlose.undraw()
			player1wins.undraw()
			player2wins.undraw()
			BarraHP1.undraw()
			BarraHP2.undraw()
			BarraSTA1.undraw()
			BarraSTA2.undraw()
			versus.undraw()
			versus.draw(janela)
			parametro = True
			parametro2 = True
			parametro_FIGHT = False
			reset = 1
			player1_hp = 100
			player2_hp = 100
			player1_sta = 100
			player2_sta = 100
			end_game = 0
			contador_de_rounds += 1
			p_winner[winner_player][len(p_winner[winner_player]) - 1].undraw()
		
		
########
	time.sleep(1)
	aba_atual = -1
	versus.undraw()
	BarraHP1.undraw()
	BarraHP2.undraw()
	BarraKI1.undraw()
	BarraKI2.undraw()
	BarraSTA1.undraw()
	BarraSTA2.undraw()
	borda_hp.undraw()
	borda_hp2.undraw()
	borda_Ki2.undraw()
	borda_Ki.undraw()
	borda_stamina2.undraw()
	borda_stamina.undraw()
	FPS.undraw()
	fundo.undraw()
	undraw(estado_player[1], 2, lado_sprite[1])
	undraw(estado_player[0], 1, lado_sprite[0])
	if check!=19:
		p_winner[winner_player][len(p_winner[winner_player]) - 1].undraw()
	janela.update()
	pygame.mixer.music.stop()
	player1 = 0
	player2 = 0
	personagem = 0
	mapa = 0
	cont = 0
	Fundo[cont].draw(janela)
	logo.draw(janela)
	logo.move(0,-(22*28))
	contador1 = 0
	contador = 0
	aux = 0
	cont_x = 0
	youwin.undraw()
	aux_map1 = 0
	aux_map2 = 0
	aux_map3 = 0
	aux_map4 = 0
	Fundo[1] = Image(Point(480,0), "Arte/Backgrounds/tentativa1.png")
	Fundo[1].move(0,7012)
	molduraPersonagem = Image(Point(146,380), "Arte/Buttons_and_Symbols/borda_p1.png")
	molduraPersonagem2 = Image(Point(146,380), "Arte/Buttons_and_Symbols/borda_p2.png")
	moldura = Circle(Point(250,150), 20)
	posicao = 1
	posicao1 = 1
	num_jogadores = 0
	parametro2 = True
	t_inicial_1 = time.time()
	timer_1 = time.time() - t_inicial_1
