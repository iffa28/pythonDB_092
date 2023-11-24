import tkinter as tk
import sqlite3
from tkinter import messagebox

def simpan_data_ke_sqlLite(nama_siswa,biologi,fisika,inggris,prediksi_fakultas):
    #membuka atau membuat database SQLite
    con = sqlite3.connect("prediksifakultas.db")
    cursore = con.cursor()

    # Membuat Table jika Table belum di buat
    cursore.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nama_siswa INTEGER,
                    biologi INTEGER,
                    fisika INTEGER,
                    inggris INTEGER,
                    prediksi_fakultas TEXT)''')
    
    # Memasukkan data mata pelajaran ke dalam tabel
    cursore.execute('''INSERT INTO nilai_siswa(nama_siswa,biologi,fisika,inggris,prediksi_fakultas) VALUES (?, ?, ?, ?, ?)''', 
                     (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))
    
    #Melakukan commit dan menutup koneksi
    con.commit()
    con.close()
    
#fungsi untuk menampilkan
def show():
    namaSiswa = entry_siswa.get()
    mapel1 = entry_biologi.get()
    mapel2 = entry_fisika.get()
    mapel3 = entry_inggris.get()
    prediksi = prediksi_fakultas (mapel1, mapel2, mapel3)

    hasilsiswa = f"Nama Siswa: {namaSiswa}"
    hasil1 = f"Biologi: {mapel1}"
    hasil2 = f"Fisika: {mapel2}"
    hasil3 = f"Inggris: {mapel3}"
    hasilprediksi = f"Prediksi Fakultas: {prediksi}"

    label_hasilsiswa.config (text=hasilsiswa)
    label_hasil1.config(text=hasil1)
    label_hasil2.config(text=hasil2)
    label_hasil3.config(text=hasil3)
    label_hasilprediksi.config(text=hasilprediksi)

    if not mapel1 and not mapel2 and not mapel3 and not namaSiswa:
        frame_hasil.pack_forget()
    else:
        frame_hasil.pack()
        simpan_data_ke_sqlLite(namaSiswa,mapel1,mapel2,mapel3,prediksi)
        messagebox.showinfo("Info","Data Tersimpan")

#Membuat instance Tkinter
root = tk.Tk()
root.title("Aplikasi Perdiksi Nilai")
root.geometry("400x600")
root.resizable(False,False)

#Label Judul
label_judul = tk.Label(root, text="PREDIKSI FAKULTAS", font=("Times",14,"bold"))
label_judul.pack(pady=20)

# Buat Frame inputan
frame_input = tk.LabelFrame(root, labelanchor="n",pady=10, padx=10)
frame_input.pack()

# Label Nama Mahasiswa
label_nama_siswa = tk.Label(frame_input, text="Nama Siswa: ")
label_nama_siswa.grid(row=0, column=0, pady=10)
entry_siswa = tk.Entry(frame_input)
entry_siswa.grid(row=0,column=1)

# Label Biologi
label_biologi = tk.Label(frame_input, text="Biologi: ")
label_biologi.grid(row=1, column=0, pady=10)
entry_biologi = tk.Entry(frame_input)
entry_biologi.grid(row=1,column=1)

# Label Fisika
label_fisika = tk.Label(frame_input, text="Fisika: ")
label_fisika.grid(row=2, column=0, pady=10)
entry_fisika = tk.Entry(frame_input)
entry_fisika.grid(row=2,column=1)

# Label Inggris
label_inggris = tk.Label(frame_input, text="Inggris: ")
label_inggris.grid(row=3, column=0, pady=10)
entry_inggris = tk.Entry(frame_input)
entry_inggris.grid(row=3,column=1)

#untuk prediksi fakultas
def prediksi_fakultas(biologi, fisika, inggris):
    if fisika < biologi > inggris:
        return "Kedokteran"
    elif biologi < fisika > inggris:
        return "Teknik"
    elif biologi < inggris > fisika:
        return "Bahasa"
    else:
        return"Tidak dapat diprediksi"
    
# Tombol Hasil
btn_hasil = tk.Button(root, text="Submit", command=show)
btn_hasil.pack(pady=10)

frame_hasil = tk.LabelFrame(root,labelanchor="n", padx=10,pady=10)
frame_hasil.pack_forget() 
    
    
# Label Hasil
label_hasilsiswa = tk.Label(frame_hasil, text="")
label_hasilsiswa.pack()

label_hasil1 =  tk.Label(frame_hasil,text="")
label_hasil1.pack()

label_hasil2 =  tk.Label(frame_hasil,text="")
label_hasil2.pack()

label_hasil3 =  tk.Label(frame_hasil,text="")
label_hasil3.pack()

label_hasilprediksi = tk.Label(frame_hasil,text="")
label_hasilprediksi.pack()


# Jalankan Aplikasi
root.mainloop()