import math

def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

def balok(p,l,t):
    hasil = p * l * t
    return hasil

def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil

print(prisma(3,3,3))

def tabung (jari_jari, tinggi):
    luas_tabung = 2 * math.pi * jari_jari * tinggi
    hasil= ( 2 * math.pi * jari_jari * tinggi)
    return luas_tabung

def kerucut (jari_jari, tinggi):
    luas_kerucut=math.pi * jari_jari**2 
    hasil= (math.pi * jari_jari**2)
    

