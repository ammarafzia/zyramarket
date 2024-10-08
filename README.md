# Tugas 2
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

**UNTUK TUGAS 3 ADA DI MAIN**
____________________________________________________________________________________________________________________________________
# Tugas 4

**Nomor1**

**Apa perbedaan antara HttpResponseRedirect() dan redirect()?**

httpResponseRedirect () adalah kelas yang mengembalikan respons HTTP dengan status kode 302 (Found), yang digunakan untuk mengalihkan pengguna ke URL baru. httpResponseRedirect Ini memerlukan URL sebagai argumen dan sering digunakan setelah memproses data, seperti saat mengirim formulir. Sedangkan dengan Redirect untuk mengembalikan httpResponseRedirect yang berfungsi akan lebih fleksibel karena dapat menerima berbagai jenis argumen, termasuk model, nama yang ditampilkan, atau URL. 

**Nomor2**

**Jelaskan cara kerja penghubungan model Product dengan User!**

Model product sebagai produk yang terdapat di dalam web, yang biasa berisi atribut nama produk, deskripsi produk dan harga produk 
Model user sebagai pengguna dari web, yang biasanya sudah disediakan oleh django seperti “from django.contrib.auth.models” yang berfungsi untuk mengelola data pengguna, seperti username, email dan password. 
penghubungan model product dengan user dalam django melalui ForeignKey atau bisa dengan tipe lain seperti OneToOneField dan ManyToManyField. Pada model product, bisa memiliki field user dengan tipe ForeignKey yang terhubung ke model user, pada kode “on_delete=models.CASCADE” akan memastikan bahwa jika dihapus, maka produk yang terkait dengan pengguna juga akan ikut terhapus secara otomatis 

**Nomor3**

**Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Authentication  adalah proses verifikasi identitas pengguna dengan cara memastikan bahwa pengguna yang mencoba untuk mengakses sistem oleh dirinya sendiri. Seperti, ketika pengguna memasukan username dan password 
Sedangkan Authorization adalah proses memastikan pengguna yang sudah terverifikasi izin untuk mengakses atau melakukan tindakan apapun yang ingin dilakukan.
Saat pengguna login, proses pertama yang terjadi adalah authentication karena sistem akan memeriksa apakah data pengguna seperti username dan password yang dimasukan sesuai dengan yang terdapat di database. Jika memiliki kesamaan antara data pengguna dan database, pengguna sudah terverifikasi dan dapat melanjutkan ke sistem.
Setelah pengguna berhasil login dan  terverifikasi, kemudian sistem akan melakukan authorization untuk menentukan dan juga membatasi apa saja yang bisa diakses oleh pengguna. 
Dalam implementasi django untuk autentikasi, Django  menggunakan fungsi authenticate() untuk memverifikasi username dan password, Jika memiliki kesamaan antara data pengguna dan database, pengguna sudah terverifikasi dan dapat melanjutkan ke sistem. sedangkan dalam implementasi django untuk authorization, Django menggunakan fungsi @login_required dan mengimpor sebuah decorator yang bisa mengharuskan pengguna masuk (login) terlebih dahulu sebelum dapat mengakses suatu halaman web. 

**Nomor4**

**Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django dapat menyimpan data pengguna di dalam cookies yang dapat diakses pada requests selama waktu yang ditentukan. Ketika berhasil login, Django membuat login untuk pengguna, yang berisi informasi tentang status login. Django kemudian mengirimkan cookie yang berisi ID sesi kepada browser pengguna. Cookie ini memungkinkan Django untuk mengidentifikasi pengguna yang sama di kunjungan berikutnya tanpa perlu meminta mereka untuk login lagi, selama cookie tersebut masih valid.
Cookies memiliki beberapa kegunaan lain, seperti cookies bisa melacak aktivitas pengguna di situs web, menyimpan informasi tentang barang barang yang ditambahkan ke keranjang belanja, sehingga bisa melanjutkan belanja di lain waktu dan cookies juga menyimpan pilihan pengguna, seperti bahasa atau tema yang ingin digunakan.
Cookies memang memiliki banyak kegunaan, tapi tidak semua cookies aman digunakan. misalnya , Third-Party Cookies yang akan melacak aktivitas pengguna secara online dan menampilkan iklan yang tidak relevan, serta mengganggu privasi pengguna

**Nomor5**

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

**Membuat fungsi registrasi, login dan logout:**
Fungsi registrasi 

- Di dalam view.py pada subdirektori main, buat form untuk registrasi pengguna dengan menambahkan import UserCreationForm, form ini akan membuat user baru 
- Di dalam view.py, buat fungsi yang menangani permintaan registrasi. Fungsi ini akan memeriksa apakah form yang masuk valid atau tidak, lalu jika berhasil akan menyimpan user baru dan bisa melakukan login 
- Buat file baru register.html  pada directory main/templates untuk menampilkan form registrasi kepada pengguna
- Setelah membuat fungsi untuk register, di dalam file url.py tambahkan  path () di dalam urlpatterns untuk menghubungkan url /register/ dengan fungsi register
  
Fungsi login 

- Di dalam view.py pada subdirektori main, tambahkan impor untuk AuthenticationForm, authenticate, dan login.
- Di dalam view.py, buat fungsi untuk menangani permintaan login. Periksa login dat pengguna dan jika benar, akan masuk ke halaman utama.
- Buat file baru login.html  pada directory main/templates untuk menampilkan form form kepada pengguna
- Setelah membuat fungsi untuk login, di dalam file url.py tambahkan  path () di dalam urlpatterns untuk menghubungkan url /login/ dengan fungsi login

Fungsi log out

- Di views.py, buat fungsi untuk menangani permintaan logout dengan menggunakan logout(). Setelah logout, akan kembali ke halaman login.
- Tambahkan juga file html dan path() di urlpatterns  

**Mengontrol user untuk masuk ke home sebelum login**
- Di dalam view.py, tambahkan import untuk login_required dan tambahkan @login_required pada fungsi yang menampilkan halaman utama agar hanya pengguna yang terverifikasi yang dapat mengaksesnya.
- Coba untuk menjalankan proyek django dan akses link http://localhost:8000/. Disini saya bisa menambahkan data yang baru ingin saya masukan dan memeriksa apakah semua tombol login, register dan logout bisa digunakan dengan baik.

**Menghubungkan model product dengan user**
- Di dalam model.py, tambahkan kode untuk mengimpor model User dan di dalam fungsi product tambahkan  user = models.ForeignKey(User, on_delete=models.CASCADE) untuk mengaitkan setiap product dengan data yang di tambahkan pengguna
- Di dalam view.py, pada fungsi show_main  ubah menjadi 'name': request.user.username, yang berguna untuk menampilkan username pengguna yang login pada halaman utama 

**Menggunakan data dari cookies**

- Di dalam view.py, tambahkan import HttpResponseRedirect, reverse, dan datetime.
-  Di dalam fungsi login_user, buat cookie last_login untuk menyimpan waktu terakhir login pengguna. Selanjutnya, tambahkan informasi cookie last_login yang akan dikirim ke halaman utama agar pengguna dapat melihat kapan mereka terakhir kali masuk. Setelah itu, perbarui fungsi logout untuk menghapus cookie last_login saat pengguna melakukan logout. 
-  Melihat data terakhir log out, bisa menambahkan kode  "terakhir login: {{ last_login }}" di dalam main.html

**Setelah semua sudah berjalan lancar, website sudah bisa digunakan dengan baik**

berikut tampilan yang di local: 

![Screenshot 2024-09-25 083908](https://github.com/user-attachments/assets/12c30ce9-72ea-41e0-91cf-5829b2eb07a1)

berikut tampilang yang di pws : 

![Screenshot 2024-09-25 083931](https://github.com/user-attachments/assets/1b834f2d-10e5-4915-af85-ff0ecc8bb0bc)

___________________________________________________________________________________________________________________________________________
# Tugas 5

**Nomor1**

**Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

CSS berfungsi untuk mengatur tampilan elemen HTML, sebelumnya perlu tahu mana aturan yang harus diutamakan jika ada beberapa selector yang ada di elemen yang sama. Pertama, inline styles  karena ditulis langsung di dalam HTML dengan atribut “style” seperti kode ini h1 style="color: red;"Hello, World!/h1,  jadinya inline styles ini langsung berhubungan dengan elemen tersebut, cara kerja ini lebih spesifik dibandingkan dengan selector yang langsung tertuju pada elemen yang sama melalui ID, class dan tag. Kedua, ID Selector karena setiap ID harus unik dalam satu halaman, maka akan pengaruh. Lalu ada class dan Element Selector seperti (h1, p, div)

**Nomor2**

**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

Konsep dari responsive design penting karena memastikan tampilan seperti tata letaknya sesuai dengan ukuran perangkat yang digunakan dan fungsi dari sebuah situs dapat sempurna dengan ukuran layar dan perangkat. Pengembangan satu situs yang responsif lebih hemat waktu dan biaya dibandingkan membuat versi terpisah untuk setiap perangkat, sehingga aksesibilitasnya lebih luas tanpa mengorbankan fungsionalitas.

Contoh aplikasi sesudah menerapkan Responsive Design, Aplikasi instagram dan Airbnb karena Aplikasi ini memiliki desain yang responsif di versi webnya. Ketika dibuka di desktop atau mobile browser, tampilan web akan otomatis menyesuaikan dengan ukuran layar perangkat yang digunakan, memastikan gambar, teks, dan konten lain tetap terlihat jelas dan mudah diakses.

Contoh aplikasi sebelum menerapkan Responsive Design,Situs Web Sekolah Tertentu Banyak sekolah (terutama yang memiliki situs lama) karena belum menerapkan responsive design, situs ini cenderung hanya dioptimalkan untuk tampilan desktop.


**Nomor3**

**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

Margin adalah ruang kosong di luar elemen yang berfungsi untuk mengatur di luar elemen, yang memisahkan elemen tersebut dari elemen lain di sekitarnya. Margin mendorong elemen lain menjauh. Margin tidak memiliki warna dan benar-benar transparan. 
Border adalah garis yang mengelilingi elemen di antara padding dan margin yang berfungsi untuk menentukan ketebalan, gaya dan warna border.
adding adalah ruang di dalam elemen, yang terletak antara konten elemen (misalnya teks atau gambar) dengan border-nya. Padding menciptakan jarak antara isi elemen dengan tepi dalam elemen tersebut. Padding bisa memiliki warna yang sama dengan latar belakang elemen.


Ketika mengatur elemen, margin, border, dan padding saling bekerja sama untuk menentukan bagaimana elemen tersebut diposisikan dalam halaman.
.element { 
margin: 20px;  → Memberikan jarak antara elemen dengan elemen lain di luar batas elemen.
border: 2px solid red; → Menambahkan garis batas di sekitar elemen
padding: 10px; → Menambahkan jarak di dalam elemen di antara konten dan batas border. 
}

**Nomor4**

**Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

Flex box adalah sistem tata letak satu dimensi yang pengaturan elemen dalam baris atau kolom dengan cara fleksibel, bisa horizontal maupun vertikal, dengan menggunakan “display: flex;” yang berfungsi untuk mengaktifkan flexbox dan “flex-direction” untuk menentukan arah tata letak. Sedangkan Grid Layout adalah sistem  tata letak dua dimensi yang pengaturan elemen dalam baris dan kolom, ideal untuk menciptakan struktur yang lebih kompleks seperti header, sidebar, dan konten utama. Dengan menggunakan “display: grid;” dan “grid-template-columns” serta “grid-template-rows”, yang berfungsi untuk menentukan ukuran kolom dan baris yang dibutuhkan.


**Nomor5**

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**


**Menambahkan fungsi edit dan delete product**

Fungsi edit_product

- Di dalam file views.py, buat fungsi baru yang berfungsi untuk pengeditan produk. Membuat fungsi edit_product yang menerima ID produk dan request sebagai parameter.
- Dalam view ini, ambil data produk dari database berdasarkan ID dan buat form yang sudah terisi dengan data produk yang ada.
- Redirect ke halaman daftar produk setelah berhasil mengedit.
- Di url.py tambahkan import yang sudah fungsi nya
   
Fungsi delete_product

- Di dalam file view.py, buat fungsi baru yang berfungsi untuk menghapus produk. 
- Dalam view ini, ambil data produk dari database berdasarkan ID dan buat form yang sudah terisi dengan data produk yang ada.
- Redirect ke halaman daftar produk setelah berhasil menghapus.
- Di url.py tambahkan import yang sudah fungsi nya  



**Menambahkan  tailwind**

- Di dalam base.html pada subdirektori templates, tambahkan  <meta name="viewport"> dan nambahkan juga  kode untuk menyambungkan  template django dengan tailwind 
- Di dalam setting.py pada MIDDLEWARE 'whitenoise.middleware.WhiteNoiseMiddleware', dan merubah variabel seperti dibawah ini
  
STATIC_URL = '/static/'
if DEBUG:
   STATICFILES_DIRS = [
       BASE_DIR / 'static' # merujuk ke /static root project pada mode development
   ]
else:
   STATIC_ROOT = BASE_DIR / 'static'
   
- Setelah itu, buat folder baru yang bernama static di dalamnya terdapat folder CSS yang berisi file global.css

**Membuat Desain Halaman Daftar Product**

- Pada login.html dan register.html,Edit halaman login dan register dengan menambahkan elemen yang menarik tata letak yang bagus dan mengganti warna sesuai yang menarik.
- Tambahkan tombol "Edit" dan "Hapus" di setiap card produk yang memanggil fungsi yang sesuai saat diklik.

**Membuat Navigation Bar (Navbar)**

- Buat file baru navbar. Html untuk navigation bar di template utama.
- Tambahkan menu untuk fitur-fitur aplikasi seperti home, add product, login, logout dan tulisan welcome “user” dan pastikan navbar dapat berubah menjadi tampilan mobile ketika ukuran layar kecil.
- Buat tampilan untuk navbar mobile yang dapat digunakan ketika tombol diklik.
- Coba untuk menjalankan dan akses link ini http://localhost:8000/. Jika semua sudah sesuai dengan desain yang diinginkan sudah selesai .

Setelah semua sudah berjalan lancar, website sudah bisa digunakan dengan baik 


___________________________________________________________________________________________________________________________
# Tugas 6

**Nomor1**

**Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**

javaScript punya peran besar dalam pengembangan aplikasi web karena membuat halaman web jadi lebih menarik dan responsif. Dengan javascript, data bisa diproses langsung di browser pengguna tanpa harus terus menerus mengirim data ke server dan menunggu balasan dari server setiap kali pengguna melakukan sesuatu. JavaScript juga bisa digunakan di backend lewat node.js, jadi pengembangan bisa pakai satu bahasa saja untuk semuanya, baik pada bagian sisi server maupun di frontend. Selain itu, javaScript didukung semua browser, sehingga aplikasi bisa digunakan dari berbagai perangkat (laptop, smartphone) tanpa khawatir tampilan atau fungsinya rusak. JavaScript juga ada banyak library dan framework *seperti react* dan *Angular* yang membuat proses pengembangannya lebih cepat dan lebih baik.

**Nomor2**

 **Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**
 
Fungsi penggunaan await saat menggunakan fetch() adalah untuk menunggu proses proses asinkronus selesai sebelum melanjutkan ke baris kode berikutnya. fetch () akan mengembalikan Promises, yang berfungsi untuk melakukan operasi secara asinkronus(),  [ asinkronus () → yang berarti operasi tersebut dilakukan tanpa menghentikan aktivitas utama atau interaksi yang sedang berjalan] seperti mengambil data dari server. 
Dengan await, javaScript akan menunggu hingga fetch() selesai dan mengembalikan hasilnya, sehingga bisa langsung bekerja dengan data tersebut setelahnya. 
Jika kita tidak menggunakan await saat memanggil fetch(), program akan melanjutkan eksekusi tanpa menunggu hasil fetch(). Akibatnya, kita mungkin mencoba mengakses data dari respons yang belum diterima, yang bisa mengakibatkan kesalahan, misalnya data undefined atau Promise belum terpecahkan. Ini bisa menyebabkan bug, terutama jika kode berikutnya bergantung pada hasil dari operasi asynchronous tersebut.

**Nomor3**

 **Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?**
 
Berguna karena mekanisme Cross-Site Request Forgery (CSRF) di Django secara default memeriksa token CSRF pada setiap permintaan POST untuk mencegah serangan CSRF, dimana bisa juga mengirimkan permintaan berbahaya atas nama pengguna yang sedang login.  Kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST karena secara default Django memiliki mekanisme keamanan yang disebut Cross-Site Request Forgery (CSRF) protection. Mekanisme ini mencegah serangan CSRF di mana seorang penyerang bisa mengirimkan permintaan berbahaya atas nama pengguna yang sedang login.
Ketika menggunakan AJAX untuk mengirim POST request ke server, Django secara otomatis akan memeriksa apakah request tersebut menyertakan CSRF token yang valid,  jika CSRF token tidak disertakan atau tidak diatur dengan benar, Django akan menolak request tersebut sebagai tindakan perlindungan.
Dengan menggunakan  decorator csrf_exempt berfungsi untuk menonaktifkan pengecekan token CSRF untuk view tertentu, sehingga permintaan AJAX POST dapat dijalankan tanpa pemeriksaan CSRF, yang berguna untuk API atau endpoint yang tidak perlu dilindungi oleh mekanisme CSRF.

**Nomor4**

 **Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**
 
Pembersihan data yang hanya mengandalkan frontend  saja tidak cukup aman karena kode frontend bisa di salah gunakan oleh pengguna atau orang lain yang berniat jahat. Jika hanya ingin mengandalkan pembersihan di frontend, pengguna dapat memastikan validasi pada sisi klien dan mengirimkan data yang tidak valid atau berbahaya langsung ke server.
Dengan membersihkan dan memvalidasi data di backend, kita dapat memastikan bahwa data yang masuk ke sistem selalu sesuai, untuk melindungi aplikasi dari berbagai serangan, seperti injection (misalnya SQL injection atau XSS) dan data tampering, yang dapat merusak atau mengekspos data penting.

**Nomor5**

 **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**



