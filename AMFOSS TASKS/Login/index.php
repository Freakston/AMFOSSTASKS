<!DOCTYPE HTML>
<?php
    session_start();
    $username ='username'
    $password ='password'
        
     if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] == true ){
        header('Location : succes.php');
    }    
     if (isset($_POST['username']) && isset($_POST['password']))
    {
     if ($_POST['username'] == $username && $_POST['password'] ==$password)
         
    { $_SESSION['loggedin'] = true;
      header('Location : success.php');
            
    }
    }
?>

<html>
<head><title>My login page</title></head>
<body>
        <form method="post" action='index.php'>
            Username-<br/>
            <input type="text" name="username"><br/>
            Password-<br/>
            <input type="password" name="password"><br/>
            <input type="submit" value="Login">
        </form>
</body>
</html>
