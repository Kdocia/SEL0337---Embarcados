# Importa a classe LED da biblioteca gpiozero para controlar LEDs
from gpiozero import LED
# Importa a função sleep do módulo time para introduzir atrasos
from time import sleep

# Cria uma instância da classe LED associada ao pino GPIO 17
led = LED(17)

# Loop infinito para acender e apagar o LED
while True:
    # Liga o LED
    led.on()
    # Aguarda por 1 segundo
    sleep(1)
    # Desliga o LED
    led.off()
    # Aguarda por mais 1 segundo
    sleep(1)
