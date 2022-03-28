<?php

/*
1. $i = 0 (initialisation)
2. $i < 10 (sinon on sort de la boucle)
3. echo "$i\n";
4. $i++
5. retour à l'étape 2.
*/

// boucle for
for ($i = 0; $i < 10; $i++) {
    echo "$i\n";
}

// boucle while
$i = 0;

while ($i < 10) {
    echo "$i\n";

    $i++;
}
