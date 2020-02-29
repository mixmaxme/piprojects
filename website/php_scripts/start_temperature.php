<?php
shell_exec("/var/www/html/start_wordclock_scripts.sh -t");
header('Location: http://wordclock/clock_index.html?success=true');
?>
