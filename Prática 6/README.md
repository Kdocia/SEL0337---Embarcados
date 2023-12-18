# Pŕatica: Introdução às interfaces de visão computacional, sistemas de‬ versionamento de arquivos e controle de acesso via Tags‬

## Controle de acesso via Tags com módulo‬ ‭RFID-RC522‬
O módulo RFID-RC522 é um dispositivo que permite a comunicação sem fio usando a tecnologia RFID (Radio-Frequency Identification). Ele é frequentemente utilizado para projetos de controle de acesso, onde cartões ou tags RFID são usados para permitir ou negar o acesso a determinadas áreas. O leitor RFID gera um campo eletromagnético por meio de uma antena e permanece constantemente aguardando que uma tag entre nesse campo. Quando isso ocorre, a tag recebe energia gerada pelo leitor, e os dois componentes dessa comunicação (leitor e tag) começam a trocar informações. Quando a comunicação se inicia, o leitor envia requisições de dados para a tag, e a tag então retorna com todas as informações disponíveis.

Para realizar essa comunicação foi utilizado a função SimpleMFRC522 da biblioteca mfrc522, que é uma abstração simplificada para interagir com um leitor RFID baseado no chip MFRC522. Essa biblioteca facilita a leitura e escrita de tags RFID usando o Raspberry Pi.

## Introdução às interfaces de Visão Computacional
Para essa etapa foi implementado o uso da biblioteca OpenCV, uma ferramenta amplamente utilizada em visão computacional. Em particular, o método Haar Cascade, empregado nesse contexto, destaca-se como um algoritmo de aprendizado de máquina. Esse método opera como um classificador, sendo capaz de identificar padrões faciais ao analisar a intensidade dos pixels em relação a um conjunto de dados predefinido.

O algoritmo Haar Cascade é uma técnica poderosa para detecção de objetos, sendo frequentemente aplicado na identificação e localização de faces em imagens. Seu funcionamento é baseado em padrões, conhecidos como "Haar features", que são características específicas extraídas de imagens. Essas características são combinadas de maneira ponderada para formar um classificador capaz de discernir entre regiões de interesse, como faces, e regiões não relevantes.

A interação entre a biblioteca OpenCV e o método Haar Cascade oferece uma abordagem robusta para a detecção facial em tempo real. Essa combinação é especialmente valiosa em projetos que requerem análise de vídeo ou imagens em busca de elementos específicos, como rostos, contribuindo para aplicações em reconhecimento facial, segurança e interações homem-máquina.
