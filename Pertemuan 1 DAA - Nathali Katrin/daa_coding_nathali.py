# -*- coding: utf-8 -*-
"""DAA Coding - Nathali

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xgZqtVEnhWWCAjcs6m3ZZ0QXRrdNvH2z
"""

# TUGAS CODING INPUT 2 BILANGAN DAN MENAMPILKAN BILANGAN TERBESAR

bilangan1 = float(input("Masukkan bilangan pertama: "))
bilangan2 = float(input("Masukkan bilangan kedua: "))

if bilangan1 > bilangan2:
    print("Bilangan terbesar adalah:", bilangan1)
elif bilangan2 > bilangan1:
    print("Bilangan terbesar adalah:", bilangan2)
else:
    print("Kedua bilangan sama besar.")