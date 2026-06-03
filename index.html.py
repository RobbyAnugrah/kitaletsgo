<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kitaletsgo - Open Trip & Rental Outdoor</title>
    <style>
        /* Pengaturan Dasar & Tema Biru */
        :root {
            --primary-blue: #0056b3;
            --secondary-blue: #e6f2ff;
            --dark-text: #333;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            color: var(--dark-text);
            line-height: 1.6;
        }
        html {
            scroll-behavior: smooth;
        }

        /* Navigasi */
        header {
            background-color: var(--primary-blue);
            color: white;
            padding: 15px 20px;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: auto;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
            letter-spacing: 1px;
        }
        .menu a {
            color: white;
            text-decoration: none;
            margin-left: 20px;
            font-weight: 500;
            transition: 0.3s;
        }
        .menu a:hover {
            color: #b3d4ff;
        }

        /* Konten Utama */
        .container {
            max-width: 1000px;
            margin: auto;
            padding: 40px 20px;
        }
        h2 {
            color: var(--primary-blue);
            border-bottom: 2px solid var(--primary-blue);
            padding-bottom: 10px;
            margin-bottom: 20px;
        }
        .bg-light {
            background-color: var(--secondary-blue);
        }

        /* Tabel & List */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            background: white;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: var(--primary-blue);
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        /* Tombol WhatsApp */
        .wa-btn-container {
            text-align: center;
            margin-top: 30px;
        }
        .btn-wa {
            display: inline-block;
            background-color: #25D366;
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 50px;
            font-weight: bold;
            font-size: 18px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: 0.3s;
        }
        .btn-wa:hover {
            background-color: #128C7E;
        }

        /* Footer */
        footer {
            background-color: #003d82;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 40px;
        }
    </style>
</head>
<body>

    <header>
        <nav>
            <div class="logo">KITALETSGO</div>
            <div class="menu">
                <a href="#biodata">Biodata</a>
                <a href="#pricelist">Pricelist Rental</a>
                <a href="#jadwal">Jadwal Trip</a>
                <a href="#tutorial">Cara Pesan</a>
            </div>
        </nav>
    </header>

    <!-- Section Biodata -->
    <div id="biodata" class="container">
        <h2>Biodata Kitaletsgo</h2>
        <p><strong>Kitaletsgo</strong> adalah penyedia layanan jasa perjalanan luar ruang (<i>outdoor</i>) dan pendakian gunung yang berdedikasi memberikan pengalaman eksplorasi alam yang aman, nyaman, dan tak terlupakan. Kami tidak hanya mengorganisir perjalanan ekspedisi, tetapi juga menyediakan penyewaan perlengkapan <i>outdoor</i> berkualitas dengan harga terjangkau.</p>
    </div>

    <!-- Section Pricelist Rental -->
    <div id="pricelist" class="bg-light">
        <div class="container">
            <h2>Pricelist Rental Outdoor</h2>
            <table>
                <thead>
                    <tr>
                        <th>Nama Barang</th>
                        <th>Harga / Hari</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Tenda Dome (Kapasitas 6 Orang)</td>
                        <td>Rp 60.000</td>
                    </tr>
                    <tr>
                        <td>Sleeping Bag (Polar)</td>
                        <td>Rp 15.000</td>
                    </tr>
                    <tr>
                        <td>Carrier 60L</td>
                        <td>Rp 45.000</td>
                    </tr>
                    <tr>
                        <td>Nesting + Kompor Portable</td>
                        <td>Rp 25.000</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Section Jadwal Trip -->
    <div id="jadwal" class="container">
        <h2>Jadwal Open Trip</h2>
        <table>
            <thead>
                <tr>
                    <th>Destinasi Gunung</th>
                    <th>Tanggal Pelaksanaan</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Gunung Rinjani (Via Sembalun)</td>
                    <td>Segera Hadir</td>
                    <td>Pendaftaran Dibuka</td>
                </tr>
                <tr>
                    <td>Gunung Sindoro</td>
                    <td>Segera Hadir</td>
                    <td>Pendaftaran Dibuka</td>
                </tr>
                <tr>
                    <td>Gunung Sumbing</td>
                    <td>Segera Hadir</td>
                    <td>Pendaftaran Dibuka</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- Section Tutorial Pesan -->
    <div id="tutorial" class="bg-light">
        <div class="container">
            <h2>Tutorial Pemesanan</h2>
            <ol>
                <li><strong>Pilih Layanan:</strong> Tentukan apakah Anda ingin mendaftar <i>Open Trip</i> atau menyewa perlengkapan <i>outdoor</i>.</li>
                <li><strong>Cek Ketersediaan:</strong> Hubungi admin kami melalui WhatsApp untuk mengecek slot trip atau ketersediaan barang.</li>
                <li><strong>Isi Formulir:</strong> Admin akan memberikan format pemesanan. Silakan isi data diri dan rincian pesanan.</li>
                <li><strong>Pembayaran:</strong> Lakukan pembayaran DP (Down Payment) ke rekening yang tertera untuk mengamankan pesanan Anda.</li>
                <li><strong>Konfirmasi:</strong> Kirimkan bukti transfer, dan pesanan Anda otomatis terkonfirmasi!</li>
            </ol>
            
            <div class="wa-btn-container">
                <!-- Ganti 628XXXXXXXXXX dengan nomor WhatsApp Anda -->
                <a href="https://wa.me/6281234567890?text=Halo%20Admin%20Kitaletsgo,%20saya%20ingin%20bertanya%20seputar%20trip/rental." class="btn-wa" target="_blank">
                    Hubungi via WhatsApp
                </a>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2026 Kitaletsgo. All Rights Reserved.</p>
    </footer>

</body>
</html>