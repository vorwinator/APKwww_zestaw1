lista = [
  {1:"raz",2:"dwa"},
  {"jedynyki":"dwójki"},
  {"1":"2"}
]

wynik = ""

for i in lista:
  for k in i:
    wynik=wynik+" "+str(k)+" "+i[k]+" "

print(wynik)