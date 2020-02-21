<?php
exec("/var/www/html/start_wordclock_scripts.sh -r &");
header('Location: http://raspberrypi/wordclock_modes/choose_wordclock_mode.html?success=true');
?>
