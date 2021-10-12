studenci = [
  (151126,"Roman Mohyła"),
  (111222,"Ktoś Tam"),
  (333444,"Kogoś Nikogoś")
]

print(studenci)

#zad9
słownik = dict((x,y) for x,y in studenci)

print(słownik)
słownik['wiek']=23
słownik['email']="test@gmail.com"
słownik['data urodzenia']=1998
słownik['adres']= 'Olsztyn'
print(słownik)