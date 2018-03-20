<?php
session_start();
//pin 16 for solenoid
shell_exec("gpio -g mode 16 out");

if($_SESSION['login_token'] !== 1) {
	header('location: index.php');
}

if($_SESSION['double_refresh']  == 'yay') {
	$_SESSION['double_refresh'] = 'nay';
	header('location: main.php');
}

if(isset($_POST['uld'])){
		shell_exec("gpio -g  write 16 1");
		$_SESSION['double_refresh'] = 'yay';
}
if(isset($_POST['ld'])){
		shell_exec("gpio -g  write 16 0");
		$_SESSION['double_refresh'] = 'yay';
}
//get GPIO state current state
$solenoid = shell_exec("gpio -g  read 16");
?>
<!doctype html>
<html lang="en">
  <head>	
  		<title>AVDD</title>
    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/dashboard.css" rel="stylesheet">
  </head>
  	<body>
    <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0">
      <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#">AVDD</a>
      <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
      <ul class="navbar-nav px-3">
        <li class="nav-item text-nowrap">
          <a class="nav-link" href="#">Sign out</a>
        </li>
      </ul>
    </nav>
    
    	<div class="container-fluid">
      <div class="row">
      <form method="post">
        <nav class="col-md-2 d-none d-md-block bg-light sidebar">
          <div class="sidebar-sticky">
            <ul class="nav flex-column">
              <li class="nav-item">
                <button class="nav-link active" href="#">
                  <span data-feather="home"></span>
                  Dashboard <span class="sr-only">(current)</span>
                </button>
              </li>
              <li class="nav-item">
                <button name="uld" class="nav-link" href="#">
                  <span data-feather="unlock"></span>
                  Unlock Door
                </button>
              </li>
              <li class="nav-item">
                <button name="ld" class="nav-link" href="#">
                  <span data-feather="lock"></span>
                  Lock Door
                </button>
              </li>
              <li class="nav-item">
                <button class="nav-link" href="#">
                  <span data-feather="mic"></span>
                  Send Message to Patient
                </button>
              </li>
              <li class="nav-item">
                <button class="nav-link" href="#">
                  <span data-feather="speaker"></span>
                 Play Message from Patient
                </button>
              </li>
              <li class="nav-item">
                <button class="nav-link" href="#">
                  <span data-feather="clock"></span>
                 Set Access Rules
                </button>
              </li>
            </ul>
          </div>
        </nav>
        </form>
        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
          <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
     			<h1 class="h2">Dashboard</h1>
            <div class="btn-toolbar mb-2 mb-md-0">
              <div class="btn-group mr-2">
                <h1>Door Status :
                <span class="badge badge-secondary">
                	<?php 
                	echo $solenoid == 1 ? "Unlocked" : "Locked"; 
                	?>
                	</h1>
                	</div>
              </div>
            </div>
            <h2>Last Captured Attempt</h2>
            <img src="FaceRec/last_image.jpg" style="width:60%;">
            <h2>Access Attempts</h2>
          <div class="table-responsive">
            <table class="table table-striped table-sm">
              <thead>
                <tr>
                  <th>#</th>
                  <th>Header</th>
                  <th>Header</th>
                  <th>Header</th>
                  <th>Header</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1,001</td>
                  <td>Lorem</td>
                  <td>ipsum</td>
                  <td>dolor</td>
                  <td>sit</td>
                </tr>
                </tbody>
                </table>
          </div> 
      </div>
    </div>
    <script src="https://unpkg.com/feather-icons/dist/feather.min.js"></script>
    <script>
      feather.replace();
    </script>
    </body>
    </html>