def usun(text, letter):
    return text.translate({ord(letter): None})
print(usun(usun('łyżki są do zupy ale niektórzy twierdzą że są do butów', 'o'), 'z'))