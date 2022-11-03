# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com


# Menginput
bil = int(input("Masukan Bilangan : "))
pan = int(input("Masukan Pangkat : "))

# Mengkonversi
pangkat = pow(bil,pan)
akar = pow(bil,1/pan)


# Menampilkan Hasil
print('==========================================================')
print('Maka Hasil ',bil,'pangkat',pan,'adalah',pangkat)
print('Maka Hasil  Akar Pangkat',pan,'dari',bil,'adalah',akar)
print('==========================================================')
