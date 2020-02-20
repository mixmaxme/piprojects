<?php
if ($_GET['test']) {
  exec("test.sh");
}
?>

<a href="?test=true">Click Me!</a>
