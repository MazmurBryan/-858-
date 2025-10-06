import os

def clear_screen():
    # Hapus tampilan sebelumnya (Windows / Linux / Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

# ===================== MENU UTAMA =====================

def menu_awal_858():
    clear_screen()
    print("Transfer Pulsamu dan menangkan iPhone 15")
    print("1. Transfer Pulsa")
    print("2. Masa Aktif")
    print("3. Minta Pulsa")
    print("4. Auto TP")
    print("5. Delete Auto TP")
    print("6. List Auto TP")
    print("7. Cek Kupon Undian TP")
    print("0. Keluar")

# ===================== MENU 1: TRANSFER PULSA =====================

def menu_1():
    clear_screen()
    print("=== TRANSFER PULSA ===")
    tujuan = input("Masukkan nomor tujuan (contoh: 08xxxx atau 628xxxx): ")
    nominal = input("Masukkan nominal transfer (contoh: 10000): ")

    clear_screen()
    print("=== KONFIRMASI ===")
    print(f"Nomor Tujuan : {tujuan}")
    print(f"Nominal      : Rp{nominal}")
    print("\n1. Konfirmasi")
    print("2. Batal")
    konfirmasi = input("Pilih (1/2): ")

    clear_screen()
    if konfirmasi == "1":
        print(f"Transfer pulsa ke {tujuan} sebesar Rp{nominal} BERHASIL.")
    else:
        print("Transaksi dibatalkan.")

    input("\nTekan Enter untuk kembali ke menu utama...")

# ===================== MENU 2: MASA AKTIF =====================

def menu_masa_aktif():
    while True:
        clear_screen()
        print("Beli Masa Aktif (dari tgl terakhir)")
        print("1. 5hr  / Rp2500")
        print("2. 10hr / Rp4rb")
        print("3. 15hr / Rp6rb")
        print("4. 30hr / Rp14rb")
        print("5. 90hr / Rp33rb")
        print("6. 180hr/ Rp62rb")
        print("7. Next")
        print("0. Home")
        print("10. Gift")

        pilih = input("\nPilih paket masa aktif: ").strip()

        if   pilih == "1": return konfirmasi_masa_aktif("5 Hari",   "2.500")
        elif pilih == "2": return konfirmasi_masa_aktif("10 Hari",  "4.000")
        elif pilih == "3": return konfirmasi_masa_aktif("15 Hari",  "6.000")
        elif pilih == "4": return konfirmasi_masa_aktif("30 Hari",  "14.000")
        elif pilih == "5": return konfirmasi_masa_aktif("90 Hari",  "33.000")
        elif pilih == "6": return konfirmasi_masa_aktif("180 Hari", "62.000")
        elif pilih == "7":
            clear_screen()
            print("Halaman Next belum diimplementasikan.")
            input("\nTekan Enter untuk kembali...")
        elif pilih == "10":
            clear_screen()
            print("Gift Masa Aktif belum diimplementasikan.")
            input("\nTekan Enter untuk kembali...")
        elif pilih == "0":
            return  # kembali ke menu utama
        else:
            print("Pilihan tidak valid.")
            input("\nTekan Enter untuk kembali...")

def konfirmasi_masa_aktif(hari, harga):
    clear_screen()
    print(f"Anda akan membeli Masa Aktif {hari} Rp{harga}")
    print("(Akumulasi Masa Aktif Maks 365 Hari)")
    print("1. Ya")
    print("9. Back")
    print("0. Home")

    konfirmasi = input("\nPilih: ").strip()

    if konfirmasi == "1":
        clear_screen()
        print(f"Pembelian Masa Aktif {hari} seharga Rp{harga} BERHASIL.")
        input("\nTekan Enter untuk kembali ke menu utama...")
        return
    elif konfirmasi == "9":
        # kembali ke daftar paket
        return menu_masa_aktif()
    else:
        # 0/Home atau input lain -> kembali ke menu utama
        return

# ===================== MENU 5: DELETE AUTO TP =====================
def menu_delete_auto_tp():
    global auto_tp_list

    clear_screen()
    print("=== DELETE AUTO TP ===")

    # cek ada list auto tp atau g
    if len(auto_tp_list) == 0:
        print("Tidak ada data Auto TP.")
        return

    # tampilkan list auto tp
    i = 0
    while i < len(auto_tp_list):
        print(str(i + 1) + ". Nomor:", auto_tp_list[i]["nomor"],
              "| Jumlah: Rp" + str(auto_tp_list[i]["jumlah"]),
              "| Tanggal:", auto_tp_list[i]["tanggal"])
        i = i + 1

    # pilih yang mau dihapus
    pilih = int(input("Masukkan nomor Auto TP yang ingin dihapus: "))
    index = pilih - 1

    if index >= 0 and index < len(auto_tp_list):
        hapus = auto_tp_list[index]
        del auto_tp_list[index]
        print("Auto TP ke", hapus["nomor"], "berhasil dihapus.")
    else:
        print("Pilihan tidak valid.")


# ===================== MENU 6: LIST AUTO TP =====================
auto_tp_list = [
    {"nomor": "081234567890", "jumlah": 10000, "tanggal": 19},
    {"nomor": "082345678901", "jumlah": 20000, "tanggal": 15}
]

def menu_list_auto_tp():
    clear_screen()
    print("=== LIST AUTO TP ===")

    if len(auto_tp_list) == 0:
        print("Tidak ada Auto TP yang aktif.")
    else:
        i = 0
        while i < len(auto_tp_list):
            print(str(i + 1) + ". Nomor:", auto_tp_list[i]["nomor"],
                  "| Jumlah: Rp" + str(auto_tp_list[i]["jumlah"]),
                  "| Tanggal:", auto_tp_list[i]["tanggal"])
            i = i + 1

    input("\nTekan Enter untuk kembali ke menu utama...")
    
# ===================== MENU 7: CEK KUPON UNDIAN Transfer Pulsa =====================
def cekKuponUndianTransferPulsa() :
    # memberikan informasi tentang menu
    print("Anda memiliki 10 Kupon Undian TP." \
    "\nUndian berlaku hingga 31/10/2025" \
    "\nInfo: telkomsel.com/undian" \
    "\nTerima Kasih telah menggunakan layanan Transfer Pulsa Telkomsel")

    # inputan untuk kembali ke program utama
    input("\nTekan Enter untuk kembali ke menu utama...")
    return

# ===================== MAIN LOOP =====================

def main():
    while True:
        menu_awal_858()
        pilihan = input("Pilih menu (0-7): ").strip()

        if   pilihan == "1": menu_1()
        elif pilihan == "2": menu_masa_aktif()
        elif pilihan in {"3", "4"}:
            clear_screen()
            print(f"Menu {pilihan} belum diimplementasikan.")
            input("\nTekan Enter untuk kembali ke menu utama...")
        elif pilihan == "5": menu_delete_auto_tp()
        elif pilihan == "6": menu_list_auto_tp()
        elif pilihan == "7" :
            clear_screen()
            cekKuponUndianTransferPulsa()
        elif pilihan == "0":
            clear_screen()
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
            input("\nTekan Enter untuk mencoba lagi...")

if __name__ == "__main__":
    main()

