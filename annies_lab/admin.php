<?php
$conn = new mysqli("localhost", "lampuser", "StrongPassword123!", "annies_creations");

$result = $conn->query("SELECT * FROM design_requests");

echo "<h1>Client Requests</h1>";

while($row = $result->fetch_assoc()) {
    echo "<p><strong>{$row['customer_name']}</strong> ({$row['email']})<br>
    Type: {$row['design_type']}<br>
    Budget: {$row['budget']}<br>
    {$row['description']}</p><hr>";
}

$conn->close();
?>
