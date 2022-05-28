from datetime import datetime
from regressão_linear import ia
from investing import day_info
from metatrader import iniciar, operar

print('Millenium inicializado!')

modelo = ia()

ativo = 'WINM22'

lote = 1

iniciar(55160350,"smc2Li6A",'XPMT5-DEMO',ativo)

while True:

    full_hour = datetime.now().strftime("%H:%M:%S")

    if full_hour >= '17:54:00' and full_hour <= '17:55:00':

        win_data = day_info('WINc1')

        predicao = ia().predict(win_data)[0] 

        close = win_data['Close'].to_dict()[0]

        operar(predicao,close,ativo,lote)    
