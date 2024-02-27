<?php

// Your Midtrans credentials
$server_key = 'Mid-server-fEdz_IL0hWPSMUh_4o53f35O';
$client_key = 'Mid-client-qASKWiC6dUiyVRZb';

// Generate Payment QR Code
$payment_data = array(
    'transaction_details' => array(
        'order_id' => 'izmiftah-bot-isisaldo123',
        'gross_amount' => 5000,
    ),
);

// Request to Midtrans API to get QR Code URL
$midtrans_endpoint = 'https://api.midtrans.com/v2/charge';
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $midtrans_endpoint);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'Content-Type: application/json',
    'Authorization: Basic ' . base64_encode($server_key . ':')
));
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payment_data));
$result = curl_exec($ch);
curl_close($ch);

$response = json_decode($result, true);

// Check if QR Code URL is generated successfully
if (isset($response['snap_redirect_url'])) {
    // Auto-redirect to the generated URL
    header('Location: ' . $response['snap_redirect_url']);
} else {
    echo "Failed to generate payment QR code. Please try again later.";
}

// Redirect to akun.php
// Add any necessary data you want to pass to akun.php
header("Location: bayarko.php");

// Return statement
return;

?>