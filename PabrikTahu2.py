class Node:
    def __init__(self, bulan, tahun, saldo_tetap, pemasukan, pengeluaran):
        self.bulan = bulan
        self.tahun = tahun
        self.saldo = saldo_tetap
        self.pemasukan = pemasukan
        self.pengeluaran = pengeluaran
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def tambah_data_kas(self, bulan, tahun, saldo_tetap, pemasukan, pengeluaran):
        new_node = Node(bulan, tahun, saldo_tetap, pemasukan, pengeluaran)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def dapatkan_data_kas(self, bulan, tahun):
        current = self.head
        while current:
            if current.bulan == bulan and current.tahun == tahun:
                return current
            current = current.next
        return None

    def update_data_kas(self, bulan, tahun, pemasukan=None, pengeluaran=None, saldo=None):
        current = self.head
        while current:
            if current.bulan == bulan and current.tahun == tahun:
                if pemasukan is not None:
                    current.pemasukan = pemasukan
                if pengeluaran is not None:
                    current.pengeluaran = pengeluaran
                if saldo is not None:
                    current.saldo = saldo - current.pengeluaran + current.pemasukan
                return True
            current = current.next
        return False

    def hapus_data_kas(self, bulan, tahun):
        current = self.head
        if current.bulan == bulan and current.tahun == tahun:
            self.head = current.next
            return True
        while current.next:
            if current.next.bulan == bulan and current.next.tahun == tahun:
                current.next = current.next.next
                return True
            current = current.next
        return False

bukukas = LinkedList()
bukukas.tambah_data_kas("Desember",2023,1000000,2000000,1600000)

while True:
    print("Selamat Datang")
    print("Menu")
    print("1. Lihat Buku Kas")
    print("2. Tambahkan Data Baru")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    pilih = str(input("Masukkan Pilihan : "))

    if pilih == "1":
        print("")       
        print("Data Kas Bulanan:")
        current = bukukas.head
        while current:
            print(f"Bulan: {current.bulan}, Tahun: {current.tahun}")
            print("Saldo:", current.saldo)
            print("Pemasukan:", current.pemasukan)
            print("Pengeluaran:", current.pengeluaran)
            print("")
            current = current.next

    elif pilih == "2":
        bulan = str(input("Masukkan Bulan Transaksi : "))
        tahun = int(input("Masukkan Tahun Transaksi : "))
        pemasukan = int(input("Masukkan Pemasukan Transaksi : "))
        pengeluaran = int(input("Masukkan Pengeluaran Transaksi : "))
        
        saldo_terakhir = 0
        if bukukas.head:
            current = bukukas.head
            while current.next:
                current = current.next
            saldo_terakhir = current.saldo        
        saldo_baru = saldo_terakhir + pemasukan - pengeluaran
        bukukas.tambah_data_kas(bulan, tahun, saldo_baru, pemasukan, pengeluaran)
        print("Data Berhasil Ditambahkan.")
        print("")

    elif pilih == "3":
        bulan_hapus = str(input("Masukkan Nama Bulan dari Data yang ingin Dihapus : "))
        tahun_hapus = int(input("Masukkan Tahun dari Data yang ingin dihapus : "))
        if bukukas.hapus_data_kas(bulan_hapus, tahun_hapus):
            print("Data kas berhasil dihapus.")
            print("")
        else:
            print("Data tidak ditemukan.")
            print("")

    elif pilih == "4":
        bulan_update = str(input("Masukkan Nama Bulan yang ingin Diperbarui : "))
        tahun_update = int(input("Masukkan Tahun yang ingin diperbarui : "))
        if bukukas.dapatkan_data_kas(bulan_update, tahun_update):
            pemasukan_baru = int(input("Masukkan Jumlah Pemasukan Baru : "))
            pengeluaran_baru = int(input("Masukkan Jumlah Pengeluaran Baru : "))
            saldo_baru = int(input("Masukkan Saldo Baru : "))
            if bukukas.update_data_kas(bulan_update, tahun_update, pemasukan_baru, pengeluaran_baru, saldo_baru):
                print("Data kas berhasil diperbarui.")
            else:
                print("Gagal memperbarui data.")
        else:
            print("Data tidak ditemukan.")
    
    elif pilih == "5":
        break
