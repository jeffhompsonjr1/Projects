<!DOCTYPE html>
<html>
<head>
    <title>Request a Design</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<header>
    <h1>Request a Custom Design</h1>
</header>

<nav>
    <a href="index.php">Home</a>
    <a href="portfolio.php">Portfolio</a>
    <a href="services.php">Services</a>
    <a href="contact.php">Request a Design</a>
</nav>

<section>

<form action="submit.php" method="POST">
    Name:<br>
    <input type="text" name="name"><br><br>

    Email:<br>
    <input type="email" name="email"><br><br>

    Design Type:<br>
    <input type="text" name="design_type"><br><br>

    Budget:<br>
    <input type="text" name="budget"><br><br>

    Description:<br>
    <textarea name="description"></textarea><br><br>

    <input type="submit" value="Submit Request">
</form>

</section>

</body>
</html>
