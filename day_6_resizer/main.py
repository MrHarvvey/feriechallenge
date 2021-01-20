"""Napisz program, który w wybranej lokalizacji odczyta wszystkie pliki graficzne (w określonych formatach, np. jpg, png, bmp itp.), następnie zmniejszy ich rozdzielczość o 50% i zapisze je w podkatalogu “smaller” z odpowiednimi nazwami. Wykorzystaj pillow lub inną bibliotekę do pracy z obrazami.


Propozycja rozszerzenia: Oblicz ile miejsca na dysku można oszczędzić po kompresji (odczytaj rozmiar plików w pierwotnym folderze oraz "smaller" i porównaj obie wartości - bezwzględnie i w %)"""


import glob
from PIL import Image
import os


def resize_photos():
    for idx, name in enumerate(glob.glob('big_photos/*')):
        new_name = f"small/{idx}_" + str(name[11:])
        image = Image.open(name)
        half_height, half_weight = int((image.size[0])/2), int((image.size[1])/2)
        tup = tuple((half_height,half_weight))
        new_image = image.resize(tup)
        image.save(new_name)

def check_percent_size():
    for file in glob.glob('big_photos/*'):
        big_size =+ int(os.stat(file).st_size)
    for file in glob.glob('small/*'):
        small = + int(os.stat(file).st_size)
    print(f"The size of your files has been reduced by: {int(small/big_size *100)} percent")

check_percent_size()


resize_photos()