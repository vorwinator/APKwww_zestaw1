import zad8

plik = zad8.FileManager("file_manager.txt")
plik.update_file("file_manager.txt", "\ndopisałem")
plik.read_file("file_manager.txt")