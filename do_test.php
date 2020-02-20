<?php
shell_exec("/var/www/html/wordclock_modes/test.sh");
header('Location: http://raspberrypi/wordclock_modes/choose_wordclock_mode.html?success=true');
?>
