import ccxt

test_key = "xxx"
test_secret = "xxx"
testing = True

exchange = ccxt.binance({
    'apiKey':test_key,
    'secret':test_secret,
    'options':{
        'defaultType':'future'
    }
})

exchange.set_sandbox_mode(testing)

## order LONG SHORT

def openLong(sym,amt):
    exchange.set_leverage(leverage=10,symbol=sym)

    exchange.create_order(
        symbol=sym,
        type="market",
        side="buy",
        amount=amt, # 0.1/20 = 0.005 BTC usd ?
        params={
            "positionSide":"LONG"
        }
    )

def tpslLong(sym,amt): #sell คืนในฝั่ง long
    exchange.set_leverage(leverage=10,symbol=sym)

    exchange.create_order(
        symbol=sym,
        type="market",
        side="sell",
        amount=amt, # 0.1/20 = 0.005 BTC usd ?
        params={
            "positionSide":"LONG"
        }
    )    

def openShort(sym,amt):
    exchange.set_leverage(leverage=10,symbol=sym)

    exchange.create_order(
        symbol=sym,
        type="market",
        side="sell",
        amount=amt, # 0.1/20 = 0.005 BTC usd ?
        params={
            "positionSide":"SHORT"
        }
    )

def tpslShort(sym,amt): #buy คืนในฝั่ง short
    exchange.set_leverage(leverage=10,symbol=sym)

    exchange.create_order(
        symbol=sym,
        type="market",
        side="buy",
        amount=amt, # 0.1/20 = 0.005 BTC usd ?
        params={
            "positionSide":"SHORT"
        }
    ) 