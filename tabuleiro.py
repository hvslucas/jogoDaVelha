# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        # soma diagonal principal
        somaDP = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]

        # soma diagonal secundária
        somaDS = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]

        if somaDP == Tabuleiro.JOGADOR_0 * 3 or  somaDS == Tabuleiro.JOGADOR_0 * 3:
            return Tabuleiro.JOGADOR_0
        if somaDP == Tabuleiro.JOGADOR_X * 3 or somaDS == Tabuleiro.JOGADOR_X * 3:
            return Tabuleiro.JOGADOR_X

        
        #verifica linhas e colunas

        for i in range(3):
            # soma linha
            somaLinha = self.matriz[i][0] + self.matriz[i][1] + self.matriz[i][2]

            # Verifica coluna   
            somaColuna = self.matriz[0][i] + self.matriz[1][i] + self.matriz[2][i]

            if somaLinha == Tabuleiro.JOGADOR_0 * 3 or somaColuna == Tabuleiro.JOGADOR_0 * 3:
                return Tabuleiro.JOGADOR_0
            
            if somaLinha == Tabuleiro.JOGADOR_X * 3 or somaColuna == Tabuleiro.JOGADOR_X * 3:
                return Tabuleiro.JOGADOR_X
            
        
        return Tabuleiro.DESCONHECIDO