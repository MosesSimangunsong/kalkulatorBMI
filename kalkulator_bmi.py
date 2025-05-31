#PROGRAM PERHITUNGAN BMI

print ("Perhitungan BMI (Body Mass Index)")
print ("---------------------------------")

berat_badan = input ("Masukkan berat badan Anda (Kilogram): ")
berat_badan = float (berat_badan)

tinggi_badan = input ("Masukkan tinggi badan Anda (Meter):")
tinggi_badan = float (tinggi_badan)

print (berat_badan)
print (tinggi_badan)

bmi = ((berat_badan)/ (tinggi_badan**2))

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5 * (tinggi_badan**2)
berat_badan_ideal['atas'] = 25 * (tinggi_badan**2)



print(f"Nilai BMI Anda adalah{bmi : .2f} kg/m^2")
print("Nilai BMI normal adalah 18.5 kg/m^2 - 25 kg/m^2")

print (f"Berat badan ideal untuk anda adalah dalam rentang {berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg")

print ("Terimakasih sudah menggunakan program ini :)")
print ("Acumalaka wak wak wak")