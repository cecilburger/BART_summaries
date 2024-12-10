# BART Summaries
Program ini digunakan untuk menghasilkan rangkuman menggunakan model BART dengan opsi fine-tuning model untuk meningkatkan performa pada dataset khusus.

## Fitur
- Scraping data menggunakan `scraper.py`.
- Fine-tuning model BART pada dataset kustom menggunakan `fine_tuning.py`.
- Menjalankan aplikasi untuk menghasilkan rangkuman langsung dengan `app.py`.

## Prasyarat
Sebelum menjalankan program, pastikan Anda memiliki hal-hal berikut:
- **Sistem Operasi**: Windows/Linux/MacOS
- **Python**: Versi 3.8 atau lebih baru
- **Git**: Untuk cloning repository
- **Pip**: Untuk menginstal dependencies

## Instalasi
Ikuti langkah-langkah berikut untuk menginstal dan menjalankan program:

1. Clone repository ini:
   ```bash
   git clone https://github.com/cecilburger/BART_summaries.git
   cd BART_summaries
Buat dan aktifkan virtual environment (opsional):

Windows:
bash
Copy code
python -m venv env
env\Scripts\activate
Mac/Linux:
bash
Copy code
python3 -m venv env
source env/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Menjalankan Program
Program ini dapat dijalankan dengan beberapa langkah tergantung pada kebutuhan Anda.

1. Jalankan Scraper
Untuk mengumpulkan data, jalankan file scraper.py:

bash
Copy code
python scraper.py
2. (Opsional) Fine-tuning Model
Jika Anda ingin melakukan fine-tuning pada model BART menggunakan dataset kustom:

Pindah ke folder dataset:
bash
Copy code
cd dataset
Jalankan fine_tuning.py:
bash
Copy code
python fine_tuning.py
Dataset dan konfigurasi fine-tuning dapat disesuaikan di dalam folder dataset.

3. Menjalankan Aplikasi
Setelah data dan model siap, jalankan aplikasi utama:

bash
Copy code
python app.py
Aplikasi ini akan memulai layanan untuk menghasilkan rangkuman berdasarkan input yang diberikan.