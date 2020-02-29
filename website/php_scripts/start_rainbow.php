<?php
shell_exec("/var/www/html/start_wordclock_scripts.sh -r");
header('Location: http://192.168.178.26/clock_index.html?success=true');
?>
