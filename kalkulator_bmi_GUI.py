import tkinter as tk
from tkinter import messagebox, font

def hitung_bmi():
    try:
        berat = float(entry_berat.get())
        tinggi = float(entry_tinggi.get())

        bmi = berat / (tinggi ** 2)
        bawah = 18.5 * (tinggi ** 2)
        atas = 25 * (tinggi ** 2)

        hasil = f"✔ Nilai BMI Anda: {bmi:.2f} kg/m²\n\n" \
                f"📊 BMI Normal: 18.5 - 25 kg/m²\n" \
                f"🎯 Berat ideal: {bawah:.2f} kg - {atas:.2f} kg"
        messagebox.showinfo("Hasil BMI", hasil)
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Tampilan utama
window = tk.Tk()
window.title("💪 Kalkulator BMI")
window.geometry("350x250")
window.configure(bg="#f0f4f8")

# Custom font
judul_font = font.Font(size=14, weight="bold")
label_font = font.Font(size=10)

# Judul aplikasi
judul = tk.Label(window, text="Kalkulator BMI", font=judul_font, bg="#f0f4f8", fg="#2c3e50")
judul.pack(pady=10)

# Frame untuk form input
form_frame = tk.Frame(window, bg="#f0f4f8")
form_frame.pack(pady=5)

# Input berat badan
tk.Label(form_frame, text="Berat badan (kg):", bg="#f0f4f8", font=label_font).grid(row=0, column=0, sticky="w", pady=5)
entry_berat = tk.Entry(form_frame, width=20)
entry_berat.grid(row=0, column=1, pady=5)

# Input tinggi badan
tk.Label(form_frame, text="Tinggi badan (m):", bg="#f0f4f8", font=label_font).grid(row=1, column=0, sticky="w", pady=5)
entry_tinggi = tk.Entry(form_frame, width=20)
entry_tinggi.grid(row=1, column=1, pady=5)

# Tombol hitung
btn_hitung = tk.Button(window, text="Hitung BMI", command=hitung_bmi, bg="#3498db", fg="white", padx=10, pady=5)
btn_hitung.pack(pady=15)

# Menjalankan aplikasi
window.mainloop()
