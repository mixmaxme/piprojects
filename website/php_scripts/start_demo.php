<?php
shell_exec("/home/pi/piprojects/start_wordclock_scripts.sh -d &");
header('Location: http://wordclock/clock_index.html?success=true');
exit();
?>
