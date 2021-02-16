# trending-category-crawl

Untuk melakukan crawling trending topic twitter kemudian disimpan di database mysql
## Cara Penggunaan
- buat database mysql berisi tabel bernama key_indo dengan kolom no,waktu,trend,kategori,terbaru
- konfigurasi koneksi database di file twitter-mining-mysql.py
- atur waktu interval pada file run.py
- jalankan dengan `python run.py`
