<?php
exec("/home/pi/piprojects/start_wordclock_scripts.sh -r &");
header('Location: http://raspberrypi/wordclock_modes/choose_wordclock_mode.html?success=true');
?>
