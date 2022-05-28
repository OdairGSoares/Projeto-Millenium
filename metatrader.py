
import MetaTrader5 as mt5

def iniciar(login,senha,server,ativo):
    
    mt5.initialize(login=login,server=server,password=senha)

    mt5.symbol_select(ativo,True)

def operar(predicao,close,ativo,lote):

    if mt5.terminal_info().community_connection:

        if mt5.positions_total()==0 and mt5.orders_total()==0:

            if predicao > close:
                
                compra(1,ativo,lote)
            
            elif predicao < close:

                venda(1,ativo,lote)

        elif mt5.positions_total()!=0:

            posicao=list(list(mt5.positions_get())[0])[5]

            if posicao==0:

                if predicao < close:

                    mt5.Close(ativo)

                    venda(1,ativo,lote)

            elif posicao==1:

                if predicao > close:

                    mt5.Close(ativo)
                    
                    compra(1,ativo,lote)

            
def compra(deviation,ativo,lote):

    price=mt5.symbol_info_tick(ativo).ask

    deviation=1

    request={
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": ativo,
        "volume": float(lote),
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "magic": 234000,
        "deviation": deviation,
        "comment": "Daily Buy",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN
    }

    result=mt5.order_send(request)

    if result.comment!='Market is closed':

        print('===================================================')
        print(result.comment)
        print('===================================================')

def venda(deviation,ativo,lote):

    price=mt5.symbol_info_tick(ativo).bid

    request={
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": ativo,
        "volume": float(lote),
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,
        "magic": 234000,
        "deviation": deviation,
        "comment": "Daily Sell",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN
    }

    result=mt5.order_send(request)

    if result.comment!='Market is closed':

        print('===================================================')
        print(result.comment)
        print('===================================================')
