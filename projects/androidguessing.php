<?php
            require_once('../header.php');
?>       
<?php
            require_once('../header.php');
?>       
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Vishal Ranjan</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
  <style>
 
    .client {
        margin-right: 5px;
    }
    hr { 
        display: block;
        margin-top: 0.5em;
        margin-bottom: 0.5em;
        margin-left: auto;
        margin-right: auto;
        border-style: inset;
        border-width: 1.5px;
        border-color: orange;
    }
</style>
</head>
<body>
<br>
<div>
<h2 style="color: orange; text-align: center;"><strong>Guessing Game </strong> </h2>
<br>
<div class="container">
<!--<p class="margin-clear"><strong> This was a course project where we had to make game. We created a shooting game where the main character  has a sword and can kill the enemies. In every level, the enemies will become stronger. </strong></p>
                      <br> 
</div>
-->               
</div>
<br>
<div class="container">
  
  <div id="myCarousel" class="carousel slide" data-ride="carousel">
    <!-- Indicators -->
    <ol class="carousel-indicators">
      <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
      <li data-target="#myCarousel" data-slide-to="1"></li>
      <li data-target="#myCarousel" data-slide-to="2"></li>
      <li data-target="#myCarousel" data-slide-to="3"></li>
      <li data-target="#myCarousel" data-slide-to="4"></li>
      <li data-target="#myCarousel" data-slide-to="5"></li>
      <li data-target="#myCarousel" data-slide-to="6"></li>
      <li data-target="#myCarousel" data-slide-to="7"></li>
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner">
      <div class="item active">
        <img src="AndroidPictures/GuessingGame/Guessing1.PNG" alt="guessing1" style="width:100%; height: 600px;">
      </div>

      <div class="item">
        <img src="AndroidPictures/GuessingGame/Guessing2.PNG" alt="guessing2" style="width:100%; height: 600px;">
      </div>
    
      <div class="item">
        <img src="AndroidPictures/GuessingGame/Guessing3.PNG" alt="guessing3" style="width:100%;height: 600px;">
      </div>
      <div class="item">
        <img src="AndroidPictures/GuessingGame/Guessing4.png" alt="guessing4" style="width:100%; height: 600px;">
      </div>
      <div class="item">
        <img src="AndroidPictures/GuessingGame/Guessing5.PNG" alt="guessing5" style="width:100%; height: 600px;">
      </div>
      <div class="item">
        <img src="AndroidPictures/GuessingGame/Guessing6.PNG" alt="guessing6" style="width:100%; height: 600px;">
      </div>
      <div class="item">
        <img src="AndroidPictures/GuessingGame/Guessing7.PNG" alt="guessing7" style="width:100%; height: 600px;">
      </div>
    </div>

    <!-- Left and right controls -->
    <a class="left carousel-control" href="#myCarousel" data-slide="prev">
      <span class="glyphicon glyphicon-chevron-left"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a class="right carousel-control" href="#myCarousel" data-slide="next">
      <span class="glyphicon glyphicon-chevron-right"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</div>
<br>

<?php
            require_once('../footer.php');
        ?>
</body>
</html>