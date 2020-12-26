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
</head>
<body>

<br>
<div>
<h2 style="color: orange; text-align: center;"><strong>Bison Computing Website </strong> </h2>
<div class="container">
<p class="margin-clear">An user friendly website which I created in my last internship. I created a sign up and login system where users can sign up and login with the same credentials. The website is user interactive where they can select different options based on the maximum limit. Apart from this, users can save their options or send the choices to the specific email. 
                        The passwords are stored in the database as an encrypted form. 
                        <br>
</div>
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
    </ol>

    <!-- Wrapper for slides -->
    <div class="carousel-inner">
      <div class="item active">
        <img src="img1.PNG" alt="Los Angeles" style="width:100%; height: 600px;">
      </div>

      <div class="item">
        <img src="img2.PNG" alt="Chicago" style="width:100%; height: 600px;">
      </div>
    
      <div class="item">
        <img src="img3.PNG" alt="New york" style="width:100%;height: 600px;">
      </div>
      <div class="item">
        <img src="img4.PNG" alt="New york" style="width:100%; height: 600px;">
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
