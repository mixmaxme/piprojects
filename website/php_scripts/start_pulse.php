<?php
shell_exec("/home/pi/piprojects/start_wordclock_scripts.sh -p &");
header('Location: http://raspberrypi/clock_index.html?success=true');
exit();
?>
