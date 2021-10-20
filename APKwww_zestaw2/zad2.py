def slownik(data_text):
    wynik=dict()
    wynik['Długość']=len(data_text)
    wynik['Lista liter']=set(data_text)
    wynik['Wielkie litery']=data_text.upper()
    wynik['Małe litery']=data_text.lower()
    return wynik

print(slownik('teKst'))