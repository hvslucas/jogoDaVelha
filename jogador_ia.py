# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int): # type: ignore
        
        # R1 

        verificacao = [Tabuleiro.JOGADOR_0, Tabuleiro.JOGADOR_X]

        for v in verificacao:
            
            # linhas
            for i in range(3):
                soma = 0
                a = -1
                b = -1
                for j in range(3):
                    if self.tabuleiro.matriz[i][j] == v:
                        soma += 1
                    if self.tabuleiro.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                        a = i
                        b = j
                
                if (soma == 2 and a != -1 and b != -1):
                    return (a, b)
            
            #colunas
            for i in range(3):
                soma = 0
                a = -1
                b = -1
                for j in range(3):
                    if self.tabuleiro.matriz[j][i] == v:
                        soma += 1
                    if self.tabuleiro.matriz[j][i] == Tabuleiro.DESCONHECIDO:
                        a = j
                        b = i
                
                if (soma == 2 and a != -1 and b != -1):
                    return (a, b)
                
            # diagonal principal
            temp = 0
            a = -1
            for i in range(3):
                if self.tabuleiro.matriz[i][i] == v:
                    temp += 1
                if self.tabuleiro.matriz[i][i] == Tabuleiro.DESCONHECIDO:
                    a = i
            if (temp == 2 and a != -1):
                return (a, a)
    
            # diagonal secundária
            temp = 0
            a = -1
            for i in range(3):
                if self.tabuleiro.matriz[i][2-i] == v:
                    temp += 1
                if self.tabuleiro.matriz[i][2-i] == Tabuleiro.DESCONHECIDO:
                    a = i
            if (temp == 2 and a != -1):
                return (a, 2-a)
            
        # R2

        for i in range(3):
            for j in range(3):
                if self.tabuleiro.matriz[i][j] == Tabuleiro.DESCONHECIDO:
                    
                    self.tabuleiro.matriz[i][j] = Tabuleiro.JOGADOR_0  

                    cont = 0 

                    # verificar linhas
                    for l in range(3):
                        soma = 0
                        vazios = 0
                        for c in range(3):
                            if self.tabuleiro.matriz[l][c] == Tabuleiro.JOGADOR_0:
                                soma += 1
                            elif self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                                vazios += 1
                        if soma == 2 and vazios == 1:
                            cont += 1

                    # verificar colunas
                    for c in range(3):
                        soma = 0
                        vazios = 0
                        for l in range(3):
                            if self.tabuleiro.matriz[l][c] == Tabuleiro.JOGADOR_0:
                                soma += 1
                            elif self.tabuleiro.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                                vazios += 1
                        if soma == 2 and vazios == 1:
                            cont += 1

                    # diagonal principal
                    soma = 0
                    vazios = 0
                    for d in range(3):
                        if self.tabuleiro.matriz[d][d] == Tabuleiro.JOGADOR_0:
                            soma += 1
                        elif self.tabuleiro.matriz[d][d] == Tabuleiro.DESCONHECIDO:
                            vazios += 1
                    if soma == 2 and vazios == 1:
                        cont += 1

                    # diagonal secundária
                    soma = 0
                    vazios = 0
                    for d in range(3):
                        if self.tabuleiro.matriz[d][2 - d] == Tabuleiro.JOGADOR_0:
                            soma += 1
                        elif self.tabuleiro.matriz[d][2 - d] == Tabuleiro.DESCONHECIDO:
                            vazios += 1
                    if soma == 2 and vazios == 1:
                        cont += 1

                    self.tabuleiro.matriz[i][j] = Tabuleiro.DESCONHECIDO

                    if cont >= 2:
                        return (i, j)


        # R3 

        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)
        
        # R4

        if self.matriz[0][0] == Tabuleiro.JOGADOR_X and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        
        if self.matriz[0][2] == Tabuleiro.JOGADOR_X and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        
        if self.matriz[2][0] == Tabuleiro.JOGADOR_X and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)
        
        if self.matriz[2][2] == Tabuleiro.JOGADOR_X and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        
        # R5

        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]

        cantos_livres = [(i, j) for (i, j) in cantos if self.matriz[i][j] == Tabuleiro.DESCONHECIDO]

        if len(cantos_livres) > 0:
            p = randint(0, len(cantos_livres)-1)
            return cantos_livres[p]

        # R6

        lista = []
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None