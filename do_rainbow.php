<?php
shell_exec("/home/pi/piprojects/start_wordclock_scripts.sh -r");
header('Location: http://raspberrypi/testscript/choose_wordclock_mode.html?success=true');
?>
