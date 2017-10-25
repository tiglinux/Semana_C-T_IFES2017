# -*-coding:utf-8 -* # Codificação para permitir acentos e a linguagem Latina

import serial	# importar a biblioteca Serial para comunicação


porta = "/dev/ttyACM0"	# Endereço da portaSerial
conexao = serial.Serial(porta,9600) #Abre portaSerial a 9600 bps


verifica_porta = conexao.isOpen() #Retorna TRUE OR FALSE para ConexaoSerial

def verifica_porta():	# Função python para Verificar se a PortaSerial esta conectada.
	if verifica_porta == True:
		print("Porta esta aberta!")
	elif verifica_porta == False :
		print("PortaSerial está fechada!")
	else:
		print("PortaSerial está desconectada!")

verifica_porta()	#Chama a função de Verificação da PortaSerial com o Arduino!
