<?php

// Fungsi untuk menghasilkan token acak
function generateToken($length = 12) {
    $characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    $token = '';
    for ($i = 0; $i < $length; $i++) {
        $token .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $token;
}

// Fungsi untuk memeriksa dan memperbarui kedaluwarsa token
function checkTokenExpiration($tokenFile) {
    if (file_exists($tokenFile)) {
        $tokenDetails = json_decode(file_get_contents($tokenFile), true);
        $expirationDate = DateTime::createFromFormat('Y-m-d H:i:s', $tokenDetails['expiration_date']);
        if (new DateTime() > $expirationDate) {
            $newToken = generateToken();
            $expirationDate = (new DateTime())->add(new DateInterval('P30D'));
            $tokenDetails = ['token' => $newToken, 'expiration_date' => $expirationDate->format('Y-m-d H:i:s')];
            file_put_contents($tokenFile, json_encode($tokenDetails));
        }
    } else {
        $newToken = generateToken();
        $expirationDate = (new DateTime())->add(new DateInterval('P30D'));
        $tokenDetails = ['token' => $newToken, 'expiration_date' => $expirationDate->format('Y-m-d H:i:s')];
        file_put_contents($tokenFile, json_encode($tokenDetails));
    }
}

try {
    $tokenFile = 'izmiftah123.json';
    $sessionKey = 'login_attempts';

    // Periksa apakah kunci sesi "login_attempts" sudah didefinisikan sebelumnya
    if (!isset($_SESSION[$sessionKey])) {
        $_SESSION[$sessionKey] = 0;
    }

    // Periksa dan perbarui kedaluwarsa token
    checkTokenExpiration($tokenFile);

    $tokenDetails = json_decode(file_get_contents($tokenFile), true);
    $currentToken = $tokenDetails['token'];
    $expirationDate = DateTime::createFromFormat('Y-m-d H:i:s', $tokenDetails['expiration_date']);

    // Periksa peran pengguna (misalnya, admin)
    $isAdmin = false; // Ganti dengan logika periksa peran admin sesuai dengan kebutuhan Anda

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $tokenAttempt = isset($_POST['token']) ? $_POST['token'] : '';

        if ($tokenAttempt === $currentToken) {
            $_SESSION['isLoggedIn'] = true;

            if ($isAdmin) {
                // Jika pengguna adalah admin, berikan kemampuan untuk mengirim email ke pengguna
                // Di sini Anda dapat menambahkan kode untuk mengirim email.
                // Setelah mengirim email, Anda dapat mengalihkan pengguna ke halaman bayarko.php.
                header("Location: bayarko.php");
                exit();
            } else {
                // Jika pengguna bukan admin, maka pengguna akan diarahkan ke folder akademiku
                header("Location: bayarko.php");
                exit();
            }
        } else {
            $_SESSION[$sessionKey]++;
            if ($_SESSION[$sessionKey] >= 3) {
                // Jika pengguna salah memasukkan token lebih dari 3 kali, arahkan ke halaman informasi.php setelah 3 detik
                echo '<script>
                        setTimeout(function() {
                            window.open("/akun.php", "_blank");
                        }, 3000);
                      </script>';
                exit();
            }
        }
    }

    if (isset($_SESSION['isLoggedIn']) && $_SESSION['isLoggedIn']) {
        // Jika pengguna sudah login, Anda bisa mengarahkannya ke halaman dashboard atau yang sesuai.
        // Misalnya, header('Location: /bayarko.php');
        exit();
    }

} catch (Exception $e) {
    // Tangani pengecualian
    echo 'Error: ' . $e->getMessage();
}
?>


<!-- Tampilan Form Login -->
<!DOCTYPE html>
<html>
<head>
    <title>Portal login</title>
    <!-- Gaya CSS elegan untuk halaman pembayaran -->
    <!-- Tambahkan gaya CSS yang sesuai di sini -->
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

        /* Styling Input and Label */
        label {
            display: block;
            text-align: left;
            margin: 10px 0;
            color: #555;
        }

        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        /* Styling Submit Button */
        input[type="submit"] {
            background-color: #3498db;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #2980b9;
        }

        /* Styling Error Message */
        p.error-message {
            color: red;
            font-weight: bold;
        }

        /* Styling Links */
        a {
            color: #3498db;
            text-decoration: none;
            transition: color 0.3s;
        }

        a:hover {
            color: #2980b9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Selamat datang di halaman Portal Login</h1>
        <p>Silakan masukkan token Akademiku Anda:</p>
        <form method="post">
            <label for="password">token password:</label>
            <input type="password" name="password" id="password" required>
            <input type="submit" value="Login">
        </form>
        <button onclick="openAkunPage()">link pembayaran</button>

        <script>
            function openAkunPage() {
                // Buka halaman akun.php dalam webview
                var webview = window.open('akun.php', '_blank', 'height=600,width=800');
                if (webview) {
                    webview.focus();
                } else {
                    alert('Webview tidak dapat dibuka. Harap periksa pengaturan peramban Anda.');
                }
            }
        </script>
    </div>
</body>
</html>
