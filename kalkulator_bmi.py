#PROGRAM PERHITUNGAN BMI

print ("Perhitungan BMI (Body Mass Index)")
print ("---------------------------------")

berat_badan = float(input ("Masukkan berat badan Anda (Kilogram): "))

tinggi_badan = float (input ("Masukkan tinggi badan Anda (Meter):"))

print (berat_badan)
print (tinggi_badan)

bmi = ((berat_badan)/ (tinggi_badan**2))

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5 * (tinggi_badan**2)
berat_badan_ideal['atas'] = 25 * (tinggi_badan**2)

if bmi <18.5:
  kondisi = "Anda kekurangan berat badan"
elif bmi < 25:
  kondisi = "Nilai BMI Anda sudah normal"
elif bmi <30:
  kondisi = "Anda kelebihan berat badan"
else :
  kondisi = "Anda mengalami obesitas"

print("Hasil perhitungan BMI :")
print("------------------------")
print(f"Nilai BMI Anda adalah{bmi : .2f} kg/m^2")
print(kondisi)

print (f"Berat badan ideal untuk anda adalah dalam rentang {berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg")

print ("Terimakasih sudah menggunakan program ini :)")