<?php
require '/PHPMailer/PHPMailer.php';
require '/PHPMailer/SMTP.php';


// Sertakan file autoload.php dari PHPMailer
require 'PHPMailer/autoload.php';

// Fungsi untuk mengirim email notifikasi
function sendEmailNotification($recipient, $subject, $message) {
    $mail = new PHPMailer(true);
    try {
        // Konfigurasi SMTP
        $mail->isSMTP();
        $mail->Host = 'smtp.office365.com'; // Ganti dengan alamat server SMTP Anda
        $mail->SMTPAuth = true;
        $mail->Username = 'admin@insancendikia.com'; // Ganti dengan username SMTP Anda
        $mail->Password = 'Cinta4545'; // Ganti dengan password SMTP Anda
        $mail->SMTPSecure = 'tls';
        $mail->Port = 587; // Port SMTP yang digunakan

        // Set pengirim dan penerima email
        $mail->setFrom('play@qql.icu', 'admin akademiku');
        $mail->addAddress($recipient);

        // Set subjek dan isi email
        $mail->Subject = $subject;
        $mail->Body = $message;

        // Kirim email
        $mail->send();
    } catch (Exception $e) {
        echo 'Pesan gagal terkirim: ' . $mail->ErrorInfo;
    }
}

// Cek apakah pengguna adalah admin (Anda dapat menambahkan logika autentikasi admin di sini)
$isAdmin = true;

if ($isAdmin) {
    // Jika pengguna adalah admin, lakukan tindakan admin di sini
    $adminMessage = 'Anda adalah seorang admin.';
    $adminSubject = 'Notifikasi Admin';
    $adminRecipient = 'admin@akademiku.store';
    sendEmailNotification($adminRecipient, $adminSubject, $adminMessage);
} else {
    // Jika pengguna bukan admin, lakukan tindakan pengguna biasa
    $userMessage = 'Selamat datang di akun Anda.';
    $userSubject = 'Notifikasi Pengguna';
    $userRecipient = 'user@akademiku';
    sendEmailNotification($userRecipient, $userSubject, $userMessage);

    // Arahkan pengguna ke /akademiku
    header('Location: /bayarko.php');
    exit();
	
}
?>

<!-- Tampilan halaman akun.php -->
<!DOCTYPE html>
<html>
<head>
    <title>Akun Anda</title>
    <!-- Gaya CSS untuk tampilan yang elegan -->
    <!-- Tambahkan gaya CSS yang sesuai di sini -->
</head>
<body>
    <div class="container">
        <h1>Selamat datang di halaman Akun Anda</h1>
        <?php
        if ($isAdmin) {
            echo '<p>Anda adalah seorang admin. Anda memiliki akses khusus.</p>';
        } else {
            echo '<p>Ini adalah akun Anda. Selamat menggunakan layanan kami.</p>';
        }
        ?>
    </div>
</body>
</html>
