import pandas as pd
import numpy as np
import investpy as inv
from datetime import datetime, timedelta 

def day_info(pesquisa):

    indices=inv.search_quotes(text=pesquisa,products=['indices'],countries=['brazil'],n_results=2)

    for indice in indices[0:1]:
        print('')

    dia_atual = (datetime.now()).strftime('%d/%m/%Y')

    dia_anterior = (datetime.now() - timedelta(7)).strftime('%d/%m/%Y')

    WIN=indice.retrieve_historical_data(from_date=dia_anterior,to_date=dia_atual)

    list = np.array(WIN.iloc[-1])

    df = pd.DataFrame([list], columns =['Open','High','Low','Close','Volume','Change Pct'])

    return df
