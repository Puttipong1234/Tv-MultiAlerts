from flask import Flask , request
import json

from cryptoTrade import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/webhook",methods = ["GET","POST"])
def webhook():
    if request.method == "POST":
        print("ได้รับคำสั่งซื้อขายจาก tradingview")
        signal = json.loads(request.data)
        print(signal)
        signal = signal["tradingview_alert"]
        
        # format data string --> json
        signal = signal.split("\n")[0] # {'action':'TPSL LONG','exchange':'BINANCE','symbol':'BTCUSDT'}
        signal = signal.replace("'",'"')
        signal = json.loads(signal)
        
        exchange = signal["exchange"]
        action = signal["action"]
        symbol = signal["symbol"]
        amt = signal["amount"]
        # filter exchange
        if exchange == "BINANCE":
                print(exchange)
                print(action)
                print(symbol)
                
                if "OPEN LONG" in action:
                        # trade order
                        openLong(symbol,float(amt))
                
                elif "TPSL LONG" in action:
                        # trade order
                        tpslLong(symbol,float(amt))
                
        
        
        return "200"
    
    return "Hello this is Free Tradingview Webhook Alert"

if __name__ == '__main__':
    app.run(debug=True)