from pynput import mouse
import tkinter as tk
from tkinter import font, messagebox

# Koordinatları saklama listesi
coordinates = []

# Koordinatları güncelleyecek fonksiyon
def on_click(x, y, button, pressed):
    if pressed and not coordinates_window.winfo_containing(x, y):
        # Koordinatları listeye ekle
        coordinates.append((x, y))
        # Koordinatları ekrana yazdır
        coordinates_text.insert(tk.END, f"Mouse konumu: (x: {x}, y: {y})\n")
        coordinates_window.lift()  # İkinci pencereyi öne getir
        coordinates_text.yview(tk.END)  # Metin alanını aşağı kaydır

# Koordinatları temizle
def clear_coordinates():
    coordinates_text.delete("1.0", tk.END)

# Koordinatları kopyala
def copy_coordinates():
    coords = coordinates_text.get("1.0", tk.END).strip()
    if coords:
        coordinates_window.clipboard_clear()  # Panoyu temizle
        coordinates_window.clipboard_append(coords)  # Koordinatları panoya ekle
        messagebox.showinfo("Başarılı", "Koordinatlar panoya kopyalandı.")

# Tkinter penceresini oluştur
coordinates_window = tk.Tk()
coordinates_window.title("61lothien YouTube")
coordinates_window.geometry("300x300")
coordinates_window.configure(bg="#2E2E2E")  # Koyu arka plan

# Pencereyi her zaman üstte tut
coordinates_window.attributes("-topmost", True)

# Kaydırma çubuğu eklemek için bir çerçeve oluştur
frame = tk.Frame(coordinates_window, bg="#2E2E2E")
frame.pack(fill=tk.BOTH, expand=True)

# Kaydırma çubuğu oluştur
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Metin alanını oluştur ve kaydırma çubuğuyla bağla
coordinates_text = tk.Text(frame, bg="#FFFFFF", font=("Arial", 12), yscrollcommand=scrollbar.set, wrap=tk.WORD)
coordinates_text.pack(fill=tk.BOTH, expand=True)
coordinates_text.config(fg="#000000", insertbackground='black', padx=5, pady=5)  # Yazı rengi siyah

# Kaydırma çubuğuna metin alanını bağla
scrollbar.config(command=coordinates_text.yview)

# Butonlar için çerçeve
button_frame = tk.Frame(coordinates_window, bg="#2E2E2E")
button_frame.pack(fill=tk.X, padx=5, pady=5)

# Koordinatları temizle butonu
clear_button = tk.Button(button_frame, text="Koordinatları Temizle", command=clear_coordinates, bg="#FF5733", fg="white", font=("Arial", 10, "bold"), relief=tk.FLAT)
clear_button.pack(side=tk.LEFT, padx=5)

# Kopyala butonu
copy_button = tk.Button(button_frame, text="Kopyala", command=copy_coordinates, bg="#33B5FF", fg="white", font=("Arial", 10, "bold"), relief=tk.FLAT)
copy_button.pack(side=tk.LEFT, padx=5)

# Pencereyi sağ üstte aç
screen_width = coordinates_window.winfo_screenwidth()
screen_height = coordinates_window.winfo_screenheight()
coordinates_window.geometry(f"300x300+{screen_width - 300}+0")  # Sağ üst köşe

# Mouse dinleyiciyi başlat
listener = mouse.Listener(on_click=on_click)
listener.start()

# Tkinter döngüsünü başlat
coordinates_window.mainloop()
