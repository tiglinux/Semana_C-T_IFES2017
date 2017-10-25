# -*-coding:utf-8 -* 

import serial

conexao = serial.Serial("/dev/ttyACM0",9600)



logico = True

def ativaLed(logico):
	while logico:
		print("")
		print("Digite 1 para Ligar LED1 , 2 para Desligar LED1 ou 3 para Ligar LED2 ,4 para Desligar LED2")
		print("5 para Ligar LED1 E LED2, 6 para Desligar LED1 e LED2")
		print("")
		print("Ou digite 0 para SAIR!")
		opcao = (str)(raw_input("Digite sua opção escolhida : "))
		if opcao == '1':
			conexao.write('1'.encode())
			print("LED1 LIGADO!")
		if opcao == '2':
			conexao.write('2'.encode())
			print("LED1 DESLIGADO!")
		if opcao == '3':
			conexao.write('3'.encode())
			print("LED 2 LIGADO!")
		if opcao == '4':
			conexao.write('4'.encode())
			print("LED 2 DESLIGADO!")
		if opcao == '5':
			conexao.write('5'.encode())
			print("LED 1 e LED2 LIGADOS!")
		if opcao == '6':
			conexao.write('6'.encode())
			print("LED1 e LED2 DESLIGADO!")
		if opcao =='0':
			print("BYE!!VOLTE SEMPRE xD")
			exit()
		if (not(opcao == '1' or opcao =='2' or opcao =='3'or opcao =='4' or opcao =='5' or opcao =='6' or opcao =='0')):
			print("Opcao Invalida,Tente Novamente!")
		
			
ativaLed(logico)

conexao.close()
