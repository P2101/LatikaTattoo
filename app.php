<?php
    foreach (glob("imgs/*.jpg") as $filename) { 
        echo "<img src='imgs/" . basename($filename) . "'><br> "; 
    }
?>