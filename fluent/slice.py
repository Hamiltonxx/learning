invoice = """
0.....6.................................40........52........60........68........76........84........92
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  PowerBoost 500C                       $15.00    1    $15.00
1411  PiTFT Mini Kit 320x240                $34.95    1    $34.95
"""
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 60)
ITEM_TOTAL = slice(60, 68)

line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION], item[QUANTITY], item[ITEM_TOTAL])




