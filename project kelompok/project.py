import os
from babel.numbers import format_currency

class Salary:
    def __init__(self):
        self.basic_salary = 0
        self.years_of_service = 0
        self.marital_status = ""
        self.number_of_children = 0
        self.service_allowance = 0
        self.spouse_allowance = 0
        self.children_allowance = 0
        self.family_allowance = 0
        self.family_savings = 0
        self.total_salary = 0

    def clear_terminal(self):
        """
        Fungsi untuk membersihkan terminal
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def to_rupiah(self, amount):
        """
        Fungsi untuk mengubah angka menjadi format mata uang rupiah

        Args:
            amount (int): Angka yang akan diubah menjadi format mata uang rupiah

        Returns:
            string: Format mata uang rupiah

        Examples:
            >>> to_rupiah(1000000)
            Rp 1.000.000,00
        """
        
        return format_currency(amount, 'Rp ', locale='id_ID')

    def print_centered(self, text, width=60):
        """
        Fungsi untuk mencetak teks yang di tengah

        Args:
            text (string): Teks yang akan dicetak
            width (int, optional): Lebar teks yang akan dicetak. Default 60.

        Examples:
            >>> self.print_centered("Hello World")
            =                       Hello World                        =
        """
        centered_text = text.center(width-2, " ")
        print("="+centered_text+"=")

    def get_integer_input(self, prompt):
        """
        Fungsi untuk mendapatkan inputan angka dari user

        Args:
            prompt (string): Pesan yang akan ditampilkan untuk user

        Returns:
            int: Angka yang dimasukkan oleh user
            
        Raises:
            ValueError: Jika user memasukkan inputan yang bukan angka
            
        Examples:
            >>> get_integer_input("Masukkan angka : ")
            Masukkan angka : 10
            10
        """
        while True:
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError:
                self.clear_terminal()
                print("Masukkan angka yang valid!")

    def calculate_family_allowance(self):
        """
        Fungsi untuk menghitung tunjangan keluarga
        
        Args:
            self (Salary): Objek dari class Salary
            
        Returns:
            tuple: Tuple yang berisi tunjangan masa kerja, tunjangan istri, tunjangan anak, tunjangan keluarga, tabungan berkeluarga, dan total gaji
        """
        
        service_allowance = 500000 if self.years_of_service > 10 else 100000
        spouse_allowance, children_allowance, family_allowance, family_savings, total_salary = 0, 0, 0, 0, 0

        if self.marital_status == "y":
            spouse_allowance = 0.1 * self.basic_salary
            children_allowance = self.number_of_children * 0.025 * self.basic_salary
            family_allowance = spouse_allowance + children_allowance
            total_salary = self.basic_salary + service_allowance + family_allowance
        else:
            family_savings = 0.05 * self.basic_salary
            total_salary = self.basic_salary + service_allowance + family_savings

        return service_allowance, spouse_allowance, children_allowance, family_allowance, family_savings, total_salary

    def display_app_header(self):
        """
        Fungsi untuk menampilkan header aplikasi
        """
        print("=" * 60)
        self.print_centered("Program Menentukan Gaji Karyawan")
        self.print_centered("Kelompok : 4")
        self.print_centered("Anggota  : DZAKIAH, SITI HUSNUL, LUTFI, M.KHALID ,M.FAUZAN ")
        print("=" * 60)

    def display_details(self):
        """
        Fungsi untuk menampilkan rincian gaji yang diterima karyawan
        
        Examples:
            >>> display_details()
            Rincian gaji jika kamu memilih status menikah
            ============================================================
            =              Rincian gaji yang kamu terima               =
            ============================================================
            =                Lama masa bekerja 11 tahun                =
            =              Status Menikah : Sudah Menikah              =
            =               Gaji Pokok : Rp 5.000.000,00               =
            =           Tunjangan Masa Kerja : Rp 500.000,00           =
            =             Tunjangan Istri : Rp 500.000,00              =
            =              Tunjangan Anak : Rp 375.000,00              =
            =        Jumlah Tunjangan Keluarga : Rp 875.000,00         =
            =   Total Gaji yang kamu dapatkan adalah Rp 6.375.000,00   =
            ============================================================
            
            >>> display_details()
            Rincian gaji jika kamu memilih status belum menikah
            ============================================================
            =              Rincian gaji yang kamu terima               =
            ============================================================
            =                Lama masa bekerja 5 tahun                 =
            =              Status Menikah : Belum Menikah              =
            =               Gaji Pokok : Rp 3.000.000,00               =
            =           Tunjangan Masa Kerja : Rp 100.000,00           =
            =           Tabungan Berkeluarga : Rp 150.000,00           =
            =   Total Gaji yang kamu dapatkan adalah Rp 3.250.000,00   =
            ============================================================
        """
        print("=" * 60)
        self.print_centered("Rincian gaji yang kamu terima")
        print("=" * 60)
        self.print_centered(f"Lama masa bekerja {self.years_of_service} tahun")
        self.print_centered("Status Menikah : Sudah Menikah" if self.marital_status == "y" else "Status Menikah : Belum Menikah")
        self.print_centered("Gaji Pokok : " + self.to_rupiah(self.basic_salary))
        self.print_centered("Tunjangan Masa Kerja : " + self.to_rupiah(self.service_allowance))

        if self.marital_status == "y":

            self.print_centered("Tunjangan Istri : " + self.to_rupiah(self.spouse_allowance))
            self.print_centered("Tunjangan Anak : " + self.to_rupiah(self.children_allowance))
            self.print_centered("Jumlah Tunjangan Keluarga : " + self.to_rupiah(self.family_allowance))
        else:
            self.print_centered("Tabungan Berkeluarga : " + self.to_rupiah(self.family_savings))

        self.print_centered("Total Gaji yang kamu dapatkan adalah " + self.to_rupiah(self.total_salary))
        print("=" * 60)

    def main(self):
        isClose = False
        while not isClose:
            self.clear_terminal()
            self.display_app_header()
            
            self.basic_salary = self.get_integer_input("Masukkan Gaji Pokok : ")
            self.years_of_service = self.get_integer_input("Masukkan Masa kerja (tahun) : ")
            self.marital_status = input("Pilih Status Menikah y(untuk menikah) dan n(belum menikah) : ")

            if self.marital_status not in ["y", "n"]:
                print("Pilihan tidak valid. Gunakan 'y' atau 'n'.")
                continue

            self.number_of_children = 0
            if self.marital_status == "y":
                self.number_of_children = self.get_integer_input("Masukkan jumlah anak : ")
            (
                self.service_allowance,
                self.spouse_allowance,
                self.children_allowance,
                self.family_allowance,
                self.family_savings,
                self.total_salary
            ) = self.calculate_family_allowance()
            self.display_details()
            finish = input("Ketik y(untuk mengulang aplikasi ke awal) dan n(untuk keluar aplikasi) : ")
            isClose = finish != "y"

if __name__ == "__main__":
    salary_app = Salary()
    salary_app.main()
