<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Mengambil kode pembayaran yang diunggah
    $uploadedFile = $_FILES['upload']['tmp_name'];

    // Lakukan verifikasi kode pembayaran
    $verificationResult = verifyPaymentCode($uploadedFile);

    if ($verificationResult) {
        // Jika kode pembayaran valid, alihkan ke 12345.php
        header("Location: bayarko.php");
        exit();
    } else {
        // Jika kode pembayaran tidak valid, tampilkan pesan kesalahan
        $errorMessage = "Kode pembayaran tidak valid. Silakan coba lagi.";
    }
}

// Fungsi untuk memverifikasi kode pembayaran
function verifyPaymentCode($file) {
    // Membaca isi file yang diunggah
    $uploadedCode = file_get_contents($file);

    // Menghapus karakter whitespace dan newline dari kode
    $uploadedCode = trim($uploadedCode);

    // Memeriksa apakah kode pembayaran dimulai dengan "izmiftah" dan diikuti oleh 9 digit angka
    if (preg_match('/^izmiftah\d{9}$/', $uploadedCode)) {
        return true; // Kode pembayaran valid
    } else {
        return false; // Kode pembayaran tidak valid
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akun Anda</title>
    <script>
        function openPopup() {
            // Membuka tautan t.me/izmiftah di jendela popup baru
            window.open("payment.php", "_blank", "width=600,height=400");
        }

        function showQRCode() {
            // Menampilkan gambar QR Code
            var qrCode = document.getElementById("qrcode");
            qrCode.style.display = "block";
            // Memuat kode.php di dalam webview setelah QR Code ditampilkan
            loadWebView();
        }

        function loadWebView() {
            // Memuat kode.php di dalam webview
            var webView = document.getElementById("webview");
            webView.src = "kode.php";
        }
    </script>
	<style>
	
			/* Styling Body */
		body {
			font-family: Arial, Helvetica, sans-serif;
			background-color: #f2f2f2;
			margin: 0;
			padding: 0;
		}

		/* Styling Container */
		.container {
			background-color: #fff;
			max-width: 400px;
			margin: 0 auto;
			padding: 20px;
			border-radius: 5px;
			box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
			text-align: center;
		}

		/* Styling Heading */
		h1 {
			color: #333;
		}

		/* Styling Paragraph */
		p {
			color: #555;
		}

		/* Styling Admin Message */
		.admin-message {
			color: #27ae60;
			font-weight: bold;
		}

		/* Styling User Message */
		.user-message {
			color: #3498db;
			font-weight: bold;
		}

		/* Styling Buttons */
		button {
			background-color: #3498db;
			color: #fff;
			padding: 10px 20px;
			border: none;
			border-radius: 3px;
			cursor: pointer;
			transition: background-color 0.3s;
			margin-top: 10px;
		}

		button:hover {
			background-color: #2980b9;
		}

		/* Styling QR Code Image */
		#qrcode {
			max-width: 200px;
			margin: 20px auto;
			display: block;
		}
	
	</style>
</head>
<body>

<div class="container">
    <h1>Selamat datang di halaman Aktivasi Token</h1>
    <?php
    if (isset($errorMessage)) {
        echo '<p style="color: red;">' . $errorMessage . '</p>';
    }
    ?>
    <form method="post" enctype="multipart/form-data">
        <label for="upload">Unggah Kode Pembayaran:</label>
        <input type="file" name="upload" id="upload" required>
        <input type="submit" value="Aktivasi">
    </form>
</div>

<div class="container">
    <h1>Pemberitahuan</h1>
    <?php
    // Anda dapat menambahkan logika untuk menentukan apakah pengguna adalah admin atau tidak
    // Contoh: $isAdmin = true;
    $isAdmin = false;

    if ($isAdmin) {
        echo '<p>Anda adalah seorang admin. Anda memiliki akses khusus.</p>';
    } else {
        echo '<p>silahkan melakukan pembayaran terlebih dahulu lalu ke QRIS lalu upload kode bayar yang di berikan di chat.</p>';
    }
    ?>
</div>

<a href="javascript:void(0);" onclick="openPopup()">Buka tautan chat</a>
<br>
<button onclick="showQRCode()">Tampilkan QRIS pembayaran</button>
<br>
<iframe id="webview" style="display: none; width: 100%; height: 300px;"></iframe>
<br>
<img id="qrcode" src="qris.png" alt="QR Code" style="display: none;">
</body>
</html>
