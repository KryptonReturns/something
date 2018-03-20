<?php 
	session_start();
	$message = 	"";
	if( isset($_POST['user'])  && isset($_POST['pass'])) {
		if($_POST['user'] == "caregiver" && $_POST['pass'] == "kypton"){
				$_SESSION['login_token'] = 1;				
				header("location: main.php");
		}else if($_POST['user'] == "caregiver" && $_POST['pass'] == "krypton"){
			$message = "Mighty Software Pirates... no Rrrrs";	
		}else{
			$message = "Incorrect Username or Password";		
		}
	}

?>
<html>
<head>
	<link rel="stylesheet" href="css/bootstrap.min.css"  crossorigin="anonymous">
	<link rel="stylesheet" href="css/signin.css"  crossorigin="anonymous">
	<script src="js/bootstrap.min.js"  crossorigin="anonymous"></script>
	<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"  crossorigin="anonymous"></script>
</head>
<body class="text-center">
	<form class="form-signin" method="post">
      <img class="mb-4" src="images/logo.png" alt="" width="72">
      <h1 class="h3 mb-3 font-weight-normal">Welcome to Automated Virtual Dementia Door</h1>
      <label for="inputEmail" class="sr-only">User Name</label>
      <input type="text" name="user" id="inputEmail" class="form-control" placeholder="User Name" required autofocus>
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" name="pass" id="inputPassword" class="form-control" placeholder="Password" required>
      <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      <div class="checkbox mb-3">
        <label>
        	<?php echo $message; 	?>
        </label>
        </div>   
      <p class="mt-5 mb-3 text-muted">Lead Programmer: Khushal Khan Liwal 2018-2019</p> 
    </form>
</body>
</html>

