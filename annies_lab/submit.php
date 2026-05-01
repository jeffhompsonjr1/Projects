<?php
$conn = new mysqli("localhost", "lampuser", "StrongPassword123!", "annies_creations");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$name = htmlspecialchars($_POST['name']);
$email = htmlspecialchars($_POST['email']);
$design_type = htmlspecialchars($_POST['design_type']);
$budget = htmlspecialchars($_POST['budget']);
$description = htmlspecialchars($_POST['description']);

$sql = "INSERT INTO design_requests (customer_name, email, design_type, budget, description)
VALUES ('$name', '$email', '$design_type', '$budget', '$description')";

if ($conn->query($sql) === TRUE) {
    echo "Request submitted successfully!";
} else {
    echo "Error: " . $conn->error;
}

$conn->close();
?>
