template_text = """

enable_alert_1 = input.bool(title = "__EXCHANGE__ : __SYMBOL__",defval = false,group = "กรุณาตั้งค่าคู่เทรดที่ต้องการ Alert")
amount_to_trade_1 = input.float(title = "contract" , defval = __AMOUNT__)
check_sym_1 = request.security(symbol = "__SYMBOL__" ,timeframe= timeframe.period,expression = check_condition())
if enable_alert_1 and check_sym_1 == "OPEN LONG"
    alert( freq = alert.freq_once_per_bar_close , message = '{"action":"OPEN LONG","exchange":"__EXCHANGE__","symbol":"__SYMBOL__","amount":"__AMOUNT__"}' )
if enable_alert_1 and check_sym_1 == "TPSL LONG"
    alert( freq = alert.freq_once_per_bar_close , message = '{"action":"TPSL LONG","exchange":"__EXCHANGE__","symbol":"__SYMBOL__","amount":"__AMOUNT__"}' )
    
    
    """

list_code_complete = []

import csv

filename = 'SYMBOL.csv'

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for index,row in enumerate(datareader):
        template_text_dum = ""
        template_text_dum = template_text.replace("1",str(index+1))
        template_text_dum = template_text_dum.replace("__EXCHANGE__",str(row[0]))
        template_text_dum = template_text_dum.replace("__SYMBOL__",str(row[1]))
        template_text_dum = template_text_dum.replace("__AMOUNT__",str(row[2]))
        list_code_complete.append(template_text_dum)

with open('output_code.txt', 'w',encoding="utf-8") as f:
    for i in list_code_complete:
        f.write(i)
        f.write('\n')