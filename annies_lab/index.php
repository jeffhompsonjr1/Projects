<!DOCTYPE html>
<html>
<head>
    <title>Annie's Creations</title>
    <link rel="stylesheet" href="style.css">

    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Poppins:wght@300;400;600&family=Dancing+Script:wght@600&display=swap" rel="stylesheet">
</head>

<body>

<nav class="navbar">
    <div class="logo">
        <span>Annie's</span>
        <small>CREATIONS</small>
    </div>

    <div class="nav-links">
        <a href="index.php" class="active">Home</a>
        <a href="portfolio.php">Portfolio</a>
        <a href="services.php">Services</a>
        <a href="contact.php">Request a Design</a>
        <a href="contact.php">Contact</a>
    </div>
</nav>

<section class="hero">
    <div class="flower-left">✿</div>

    <div class="hero-content">
        <h1>Annie's</h1>
        <h2>CREATIONS</h2>
        <p class="tagline">Art with heart. Designs that speak.</p>
        <p class="hero-text">
            Custom artwork and creative designs made to bring your ideas to life.
            Every piece is made with passion, creativity, and a personal touch.
        </p>
        <a href="contact.php" class="btn">Request a Design</a>
    </div>

    <div class="sketch-card">
        <div class="paper">
            <p>custom art</p>
            <span>✿</span>
        </div>
    </div>
</section>

<section class="about">
    <div class="about-image">
        <img src="images/artist.jpg" alt="Artist workspace">
    </div>

    <div class="about-text">
        <h3>Hello, I'm Annie ♡</h3>
        <h4>Artist. Designer. Dreamer.</h4>
        <p>
            I specialize in creating custom designs that reflect your story and vision.
            From logos and digital art to event flyers, personalized items, and gifts —
            each design is crafted with care and creativity.
        </p>
        <a href="services.php" class="btn secondary">Learn More About My Services</a>
    </div>
</section>

<section class="services-band">
    <h3>What I Can Create For You</h3>

    <div class="service-grid">
        <div class="service-card">
            <div class="icon">🌿</div>
            <h4>Custom Digital Art</h4>
            <p>Unique artwork tailored to your ideas.</p>
        </div>

        <div class="service-card">
            <div class="icon">🌸</div>
            <h4>Logo Designs</h4>
            <p>Memorable logos for brands and businesses.</p>
        </div>

        <div class="service-card">
            <div class="icon">📝</div>
            <h4>Event Flyers</h4>
            <p>Beautiful flyers for any occasion.</p>
        </div>

        <div class="service-card">
            <div class="icon">🎁</div>
            <h4>Custom Gifts</h4>
            <p>Thoughtful, one-of-a-kind creations.</p>
        </div>

        <div class="service-card">
            <div class="icon">🎨</div>
            <h4>Social Media Designs</h4>
            <p>Graphics to grow your online presence.</p>
        </div>
    </div>
</section>

<section class="cta">
    <h3>Have an idea in mind? ♡</h3>
    <p>I’d love to hear about your project and help create something amazing.</p>
    <a href="contact.php" class="btn">Start Your Design Request</a>
</section>

<footer>
    <div class="footer-logo">Annie's Creations</div>
    <p>© <?php echo date("Y"); ?> Annie's Creations. All Rights Reserved.</p>
</footer>

</body>
</html>
