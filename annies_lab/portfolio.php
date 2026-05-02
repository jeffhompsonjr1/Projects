<!DOCTYPE html>
<html>
<head>
    <title>Portfolio - Annie's Creations</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

<nav class="navbar">
    <div class="logo">
        <span>Annie's</span>
        <small>CREATIONS</small>
    </div>

    <div class="nav-links">
        <a href="index.php">Home</a>
        <a href="portfolio.php" class="active">Portfolio</a>
        <a href="services.php">Services</a>
        <a href="contact.php">Request a Design</a>
    </div>
</nav>

<section class="portfolio">
    <h1>My Work</h1>

    <div class="gallery">

        <?php
        $dir = "images/";
        $files = scandir($dir);

        foreach($files as $file) {
            if($file != "." && $file != "..") {
                echo "<div class='img-box'>";
                echo "<img src='$dir$file'>";
                echo "</div>";
            }
        }
        ?>

    </div>
</section>

</body>
</html>
