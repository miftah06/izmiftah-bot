<?php
// Fungsi untuk menghasilkan kode aktivasi acak
function generateActivationCode($length = 6) {
    $characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    $code = '';
    for ($i = 0; $i < $length; $i++) {
        $code .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $code;
}

// Generate kode aktivasi baru
$activationCode = generateActivationCode();

// Simpan kode aktivasi ke dalam kode12345.json
$file = 'kode12345.json';
$data = json_encode(['activation_code' => $activationCode]);

if (file_put_contents($file, $data)) {
    echo 'Kode aktivasi berhasil dihasilkan dan disimpan ke ' . $file;
} else {
    echo 'Gagal menyimpan kode aktivasi.';
}
?>
