import paho.mqtt.client as mqtt
import sys
import json
from datetime import datetime

import bd

# definições
Broker = 'test.mosquitto.org'
PortaBroker = 1883
#tempo máximo em segundos permitido entre os pacotes do protocolo MQTT enviados pelo cliente
KeepAliveBorker = 60
TopicoSubscribe = "MQAr/PMS5003"
data = datetime.today()



####################### Callback - conexão ao broker realizada   ###########################
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado de conexão: " + str(rc))
    print("Data: " + str(datetime.now()))
    # faz subscribe automático no tópico
    client.subscribe(TopicoSubscribe)


####################### callback - mensagem recebida do Broker   ###########################
def on_message(client, userdata, msg):
    global data
    # msg.payload é uma vetor de bytes, para transformar em str, precisamos apenas trocas ' por "
    msg_str = msg.payload.decode('utf-8').replace("'", '"')
    # transformar dados em dicionário
    dados = json.loads(msg_str)
    hoje = datetime.now()

    #salva os dados recebidos de concentração
    bd.salvar_concentracao(dados,hoje)

    #verifica se chegou ao final do dia
    if data.date() != hoje.date():
        #Calcula e salva os indices
        bd.salvar_indice(data.date())
        #atualiza para data atual
        data = hoje


#############################################################################################
#################################### Programa Principal #####################################
#############################################################################################


#inicia uma conexão com o banco de dados

try:
    print("[STATUS] Inicializando MQTT...")
    # inicializa MQTT
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(Broker, PortaBroker, KeepAliveBorker)
    client.loop_forever()
except KeyboardInterrupt:
    print("\nCtrl+C pressionado, encerrando aplicação e saindo...")
    sys.exit(0)
