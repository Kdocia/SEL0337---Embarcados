# Para descobrir qual a codificação da Tag com texto gravado anteriormente
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

#desabilitar os avisos
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#Definição dos pinos de LED
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

#cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()
print("Aproxime a tag do leitor para leitura.")

#id de tags armazenados
lista_ID = {'221839533466'}

try:
    while True: #loop
        id,texto = leitor.read() #cria as variáveis "id" e "texto", e as atribui as leituras da id e do texto coletado da tag pelo leitor, respectivamente
        id = str(id)
        if id in lista_ID:
                GPIO.output(20,GPIO.HIGH)
                print('Acesso Liberado')
                sleep(2)
                GPIO.output(20,GPIO.LOW)
                sleep(1)
        else:
                GPIO.output(21,GPIO.HIGH)
                print('Acesso Negado')
                sleep(2)
                GPIO.output(21,GPIO.LOW)
                sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()  # toda vez que interrompermos o programa com crtl C o pino vai ser limpado automaticmanete
