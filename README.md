Nomor 1

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

<<<<<<< HEAD
Kelas : PBP B

=======
- Membuat proyek Django Baru, Pertama saya membuat sebuah proyek django baru bernama “zyramarket”. Proyek ini berfungsi sebagai kerangka kerja yang mengatur aplikasi. Kemudian pastikan proyek “zyramarket” berada di dalam direktori utama dan GitHub sudah terhubung untuk memantau perubahan kode secara efisien. 
- Membuat aplikasi baru, Saya membuat aplikasi “main” di dalam proyek Django dan buka file settings.py lalu tambahkan "main" ke dalam daftar INSTALLED_APPS yang berfungsi untuk memastikan aplikasi “main” terdaftar dengan proyek “zyramarket”
- Membuat folder template, Saya membuat folder baru “template” di dalam direktori main, di dalam folder tersebut berisi file HTML “main.html” yang akan berfungsi untuk menampilkan halaman web dari data yang kita buat.
- Setelah itu, buka file “models.py” di aplikasi “main”, saya membuat class MoodEntry yang akan saya definisi dengan cara membuat variabel baru sesuai dengan tipe tipe yang sudah disediakan seperti CharField,IntegerField, TextField. 
- Kemudian saya membuka  file ”views.py” yang berfungsi untuk menghubungkan view dan template, saya juga menambahkan fungsi show_main yang merupakan hasil modifikasi  “main.html” dengan template variabel. 
- Di dalam "main", saya membuat File “urls.py” di aplikasi "main" berfungsi untuk mengelola rute URL khusus untuk fitur-fitur di aplikasi itu sendiri Sementara itu, file “urls.py” di proyek "zyramarket" lalu saya menambahkan rute yang mengarah pada file “urls.py”. 
- Setelah semuanya sudah berjalan lancar, saya bisa Deployment ke PWS.

Nomor 2

**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

<img width="530" alt="image" src="https://github.com/user-attachments/assets/85080189-08dc-452d-b6c0-1fd035615713">

Tahap 1 : permintaan dari user (Klien)
Klien mengirimkan sebuah request ke server melalui internet. Misalnya, klien mengakses halaman tertentu di website Django.

Tahap 2 : masuk ke dalam internet
Permintaan ini akan diterima oleh server yang terhubung dengan internet dan server agar Django berjalan baik

Tahap 3 : pembahasan urls.py 
Di Django, permintaan pertama kali diproses oleh urls.py. File ini bertugas mencari kesamaan URL yang diminta klien dengan pola URL yang telah ditentukan. Misalnya, jika klien meminta /home/, urls.py akan memeriksa apakah ada pola URL yang cocok dan kemudian mengarahkan permintaan ke fungsi tampilan yang sesuai di views.py.

Tahap 4 : pembahasan views.py
Setelah urls.py menemukan kesamaan, permintaan tersebut diteruskan ke fungsi tampilan di views.py. yang bertanggung jawab untuk memproses logika yang diperlukan. Jika tampilan memerlukan data dari database, maka views.py akan berinteraksi dengan model di models.py untuk mengambil atau memodifikasi data.

Tahap 5 : pembahasan models.py
File ini mengelola interaksi dengan database. models.py berisi definisi dari struktur data yang digunakan oleh aplikasi Django untuk menyimpan dan mengelola data. Misalnya, jika tampilan membutuhkan data pengguna, views.py akan menggunakan model yang relevan di models.py untuk mengambil data tersebut.

Tahap 6 : Berkas HTML (index.html)
Setelah data diproses, views.py akan menkoneksi ke template index.html dengan data yang diperlukan. Template ini dikembalikan sebagai tanggapan yang berisi halaman web yang akan ditampilkan di browser klien.


Nomor 3

**Jelaskan fungsi git dalam pengembangan perangkat lunak!**

Git adalah alat yang membantu pengembang melacak perubahan kode, git bisa untuk bekerja bersama satu proyek tanpa saling mengganggu dengan menggunakan branch dan Git dapat membantu dalam melihat riwayat perubahan kode yang sudah terhapus dan mengembalikannya lagi.


Nomor 4

**Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Django sering dipilih sebagai framework pertama untuk belajar pengembangan perangkat lunak karena mudah digunakan dan sudah menyediakan banyak fitur yang lengkap. Django bisa langsung mulai membuat aplikasi web tanpa perlu pusing memikirkan banyak hal teknis seperti menghubungkan ke database atau membuat sistem login, karena semua itu sudah disiapkan. Django juga punya dokumentasi yang jelas,sehingga bisa dengan mudah menemukan solusi. 


Nomor 5

**Mengapa model pada Django disebut sebagai ORM?**

Fungsi ORM (Object-Relational Mapping) pada Django adalah untuk mempermudah pengembang dalam mengelola data di database dengan menggunakan konsep berorientasi objek. Dengan ORM, pengembang dapat bekerja dengan data sebagai objek Python, sementara Django akan memperbarui data dan mengubahnya menjadi perintah SQL yang dibutuhkan untuk berinteraksi dengan database. Ini memungkinkan pengembang untuk fokus pada logika aplikasi tanpa perlu memahami detail teknis SQL, sehingga membuat pengelolaan data menjadi lebih sederhana dan efisien.
>>>>>>> c9a98a0327056b922b1a2dd2be5d20d0fc12cabe
