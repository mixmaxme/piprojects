<?php
exec("start_wordclock_scripts.sh -r &");
header('Location: http://raspberrypi/choose_wordclock_mode.html?success=true');
?>
