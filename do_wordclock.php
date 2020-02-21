<?php
shell_exec("start_wordclock_scripts.sh -w");
header('Location: http://raspberrypi/choose_wordclock_mode.html?success=true');
?>
