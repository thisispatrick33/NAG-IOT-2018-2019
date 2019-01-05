# NAG-IoT
## PROJECT SAMSON

### 4a - Naučte sa prenášať dáta na server (spôsob komunikácie a formát požadovaných dát je upresnený v návode pre študentov).

Pre túto úlohu sme využili doterajšie zapojenie a na server sme sa pokúsili preniesť hodnotu nameranú senzorom BMP180, presnejšie teplotu. Tento kód sme potom využili aj v nasledujúcej úlohe. 

###### Súbor s kódom sa nazýva : 4a.py

##### Použité knižnice :
* requests
* Adafruit_BMP.BMP085
* time


<img src="https://i.ibb.co/nnRMrFV/4a.png"/>



### 4b - Dáta z pripojených senzorov prenášajte na server trvale v pravidelných intervaloch.

Pri tejto úlohe sme vytvorili program, ktorý pracoval na princípe programu z predchádzajúcej úlohy, avšak neposielal len jeden údaj, ale všetky. Okrem hodnôt meraných teplomerom sme sa rozhodli na server prenášať aj teplotu procesora Raspberry, či odozvu zo servera v ms. Keďže dáta máme prenášať v pravidelných časových intervaloch, rozhodli sme sa napojiť k senzorom aj RGB LED diódu, ktorá indikuje stav programu, pokiaľ svieti na bielo znamená to, že program práve prenáša dáta na server, ak bliká na zeleno znamená to, že program čaká kým vyprší čas na prenos dát na server.

###### Súbor s kódom sa nazýva : 4b.py

##### Použité knižnice :
* requests
* Adafruit_BMP.BMP085
* os
* glob
* time
* subprocess
* sys
* RPi.GPIO



<img src="https://i.ibb.co/cx5f0sq/4b.png"/>




### 4c - Nastavení preveďte tak, aby vybrané hodnoty boli zobrazené na mape na stránke nag-iot.zcu.cz.

Pri tejto úlohe nebolo potreba meniť niečo na zapojení, alebo vytvárať špeciálny program. Jediné čo sme museli urobiť bolo pri vytváraní premennej na stránke nag-iot.zcu.cz zaškrtnúť políčko zobrazovať hodnotu na mape.
