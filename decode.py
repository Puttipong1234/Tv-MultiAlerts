import json

string_decode = '{"action":"OPEN LONG","exchange":"BINANCE","symbol":"BTCUSDT"}'

# sig = json.loads(string_decode)

print(json.loads(string_decode))