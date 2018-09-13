<?php
 if ($_SESSION['loggedin'] == false ||  !isset($_SESSION['loggedin']) {
     header('Location : index.php');
 }
?>
<html>
    <head><title>Login successful</title></head><body><centre> <h1>Login successful</h1></centre></body>
</html>
