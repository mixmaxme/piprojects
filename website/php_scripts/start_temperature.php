<?php
shell_exec("/home/pi/piprojects/start_wordclock_scripts.sh -t");
header('Location: http://raspberrypi/clock_index.html?success=true');
?>
