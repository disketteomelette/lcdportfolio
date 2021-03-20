# coding=ASCII
import urllib3
from datetime import date
from datetime import datetime
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD
lcd = Adafruit_CharLCD(rs=26, en=19,
                       d4=13, d5=6, d6=5, d7=11,
                       cols=16, lines=2)
sumaganancia = 0
ec = 0

def sacaprecio(par, cantidad, inversion):
  global sumaganancia
  global ec
  http = urllib3.PoolManager()
  r = http.request('GET', "https://api.coinbase.com/v2/prices/" + par + "/spot")
  # print(r.status)
  datos = r.data
  array = datos.split(",")
  amount = array[2]
  pr = amount.split('"')
  ec = float(pr[3])
  final = ec * float(cantidad)
  final = round(final, 2)
  resultado = final - inversion
  resultado = round(resultado, 2)
  sumaganancia = sumaganancia + resultado
  if "-" in str(resultado):
    simbolo = chr(163)
  else:
    simbolo = chr(162)
  return(str(final) + " " + simbolo + " " + str(resultado))

def muestra(lineauno, lineados):
  lcd.clear()
  lcd.message(str(lineauno) + "\n" + str(lineados))
  sleep(1)

# START

muestra (chr(243) + " LCDPortfolio " + chr(243), "  jcrueda.com")

# LOOP
while 1 == 1:
  now = datetime.now()
  muestra(chr(243) + " LCDPortfolio " + chr(243), now)
  sleep(5)
  # You can add lines to check each crypto. You'll need:
  # - Which name will show - [NAME-OF-THE-COIN]
  # - Pair of coins in Coinbase API format (BTC-EUR, LINK-EUR, BNT-EUR ...) - [PAIR-OF-COINS]
  # - Amount of coins you hold (i.ex. 0.01) - [AMOUNT-OF-COINS]
  # - Money amount in fiat that you have invested in this currency (i.ex. 400) [MONEY-INVESTED-IN-FIAT]
  #   muestra(chr(243) + " [NAME-OF-THE-COIN] " + chr(243), sacaprecio("[PAIR-OF-COINS]", [AMOUNT-OF-COINS], [MONEY-INVESTED-IN-FIAT]))
  muestra(chr(243) + " BTC " + chr(243), sacaprecio("BTC-EUR", 0.01368274, 600))
  muestra(chr(243) + " ETH " + chr(243), sacaprecio("ETH-EUR", 0.27858103, 400))
  muestra(chr(243) + " NU " + chr(243), sacaprecio("NU-EUR", 166.808203, 100))
  muestra(chr(243) + " ZEC " + chr(243), sacaprecio("ZEC-EUR", 0.047, 2))
  muestra(chr(243) + " UNI " + chr(243), sacaprecio("UNI-EUR", 0.063630, 1.4))
  # Getting net income substracting taxes (in Spain, small gains are about 19% = 0.19)
  neto = sumaganancia - (sumaganancia * 0.19)
  # Show incomes
  muestra("GROSS: " + str(sumaganancia), "  NET: " + str(round(neto, 2)))
  sleep(4)
  sumaganancia = 0
