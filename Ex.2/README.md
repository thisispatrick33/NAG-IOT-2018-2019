# NAG-IoT
## PROJECT SAMSON

### 2a - Ovládajte port vo výstupnom režime (LED, bzučiak).

Pre túto úlohu sme použili LED diódu. Táto dióda má 2 vodiče a to katódu a anódu. Katódu sme pripojili na GPIO GND, ktorý by sa 
dal nazvať aj uzemnenie. Anódu sme pripojili na GPIO, ktorý nám umožňuje LED diódu dynamický ovládať. Pomocou programovacieho jazyka Python 3 sme vytvorili program, ktorý LED diódu rozsvieti. Tak isto fungoval aj bzučiak ak sme ho nahradili LED diódou v zapojení.

###### Súbor s kódom sa nazýva : 2a.py

##### Použité knižnice :
* RPi.GPIO
* time

<img src="https://i.ibb.co/y874K2N/LED-BZUCIAK.png"/>



### 2b - Otestujte riadenie výkonu na GPIO porte pomocou PWM.

Pre túto úlohu sme použili rovnaké zapojenie ako pri predchádzajúcej úlohe. Teda LED diódu zapojenú na GPIO pin. Pomocou programovacieho jazyka Python 3 sme vytvorili program, ktorý LED diódu pomaly rozsvieti, počká 0.1 sekundy a potom LED diódu pomaly zhasne, pričom zase počká 0.1 sekundy. Pri tomto zapojení sme použili pri nastavovaní PWM – Pulse Width Modulation, frekvenciu 100 Hz.

###### Súbor s kódom sa nazýva : 2b.py

##### Použité knižnice :
* RPi.GPIO
* time

<img src="https://i.ibb.co/y874K2N/LED-BZUCIAK.png"/>




### 2c – Pripojte RGB LED a pomocí PWM namiešajte rôzne farby

Na rozdiel od LED diódy, ktorú sme použili v predchádzajúcich úlohách, RGB LED dióda má 4 vodiče a dokáže zobrazovať viac farieb. Jeden z týchto vodičov sa používa na uzemnenie (najdlhší vodič), ostatné 3 vodiče sa používajú na riadenie jednotlivých farieb RGB – červená, zelená a modrá.

###### Súbor s kódom sa nazýva : 2c.py

##### Použité knižnice :
* RPi.GPIO
* time
* sys

<img src="https://i.ibb.co/L5tGByF/RGB-LED.png"/>




### 2d - Otestujte port vo výstupnom režime (tlačidlo, dotykové tlačidlo nebo prepínač).

Na túto úlohu sme použili LED diódu z prvej úlohy a taktiež aj tlačidlo, ktoré majú obe dva vodiče. Jeden vodič LED diódy a jeden vodič tlačidla sme pripojili na GND, teda uzemnenie. A jeden vodič LED diódy a vodič tlačidla na rôzne GPIO piny. Z pinu v ktorom je zapojené tlačidlo budeme čítať stav tlačidla. Ak bude tlačidlo stlačené program rozsvieti LED diódu. Ak nebude tlačidlo stlačené, program LED diódu zhasne.

###### Súbor s kódom sa nazýva : 2d.py

##### Použité knižnice :
* RPi.GPIO
* time

<img src="https://i.ibb.co/09HKJJ8/BUTTON.png"/>
