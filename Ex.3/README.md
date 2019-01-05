# NAG-IoT
## PROJEKT SAMSON


### 3a - Pripojte a vyskúšajte OLED displej.

Pre túto úlohu sme použili OLED display a rotačný enkodér. Obe súčiastky sme zapojili k Raspberry. Vytvorili sme jednoduchý program, ktorý na display vypisoval číslo. Ak sme rotačný enkodér točili v smere hodinových ručičiek, číslo zobrazované na display, postupne zväčšovalo svoju hodnotu o 1. Ak sme rotačný enkodér točili proti smeru hodinových ručičiek, číslo zobrazované na display, postupne zmenšovalo svoju hodnotu o 1.

##### Súbor s kódom sa nazýva : 3a.py

##### Použité knižnice :
* gaugette.ssd1306
* gaugette.platform
* gaugette.gpio
* RPi.GPIO
* time
* sys

<img src="https://i.ibb.co/sQgxF3X/3A-1.png"/>
<img src="https://i.ibb.co/jkfbzcr/3A-2.png"/>
<img src="https://i.ibb.co/nPBgHjn/3A-3.png"/>



### 3b – Pripojte senzor BMP180

Senzor BMP 180 dokáže merať 4 fyzikálne veličiny. Atmosférický tlak, atmosférický tlak pri výške mora, teplotu a nadmorskú výšku. Tento senzor má 4 vodiče. Jeden je GND teda uzemnenie, ďalší sa napojí na pin s označením 3V3, a ďalšie 2 sa napoja na GPIO piny. Po zapojení sme zhotovili program, ktorý zmeria nadmorskú výšku a tlak pri nadmorskej výške mora a následne hodnoty vypíše do konzoly.

###### Súbor s kódom sa nazýva : 3b.py

##### Použité knižnice :
* Adafruit_BMP.BMP085
* time

<img src="https://i.ibb.co/tcYQbPJ/3B.png"/>



### 3c – Pripojte teplomer DALLAS 18B20

Pre zapojenie teplomeru sme potrebovali aj rezistor s odporom 4K7ohmov. Teplomer má 3 vodiče, krajné vodiče sú GND teda uzemnenie a prívod elektriny teda 3V3 GPIO pin. Stredný vodič sme napojili na GPIO pin, pomocou ktorého dostávame hodnoty z teplomera. Teplotu sme taktiež nechali vypisovať do konzoly.

###### Súbor s kódom sa nazýva : 3c.py

##### Použité knižnice :
* os
* glob
* time


<img src="https://i.ibb.co/9gL31GY/3C.png"/>




### 3d - Zostavte aplikáciu, ktorá na OLED displeji zobrazí merané dáta a ďalšie informácie (čas, dátum, status spojenia so súťažným serverom a podobné).

Pri tejto úlohe sme spojili zapojenia z predchádzajúcich úloh a vytvorili program, ktorý tieto dáta zobrazoval na display. Keďže meraných dát je veľa, tak sme už v tejto úlohe použili rotačný enkodér aby sme mohli medzi jednotlivými dátami vyberať, ktoré sa zobrazí na display.

###### Súbor s kódom sa nazýva : 3d.py

##### Použité knižnice :
* GPIO
* sleep
* os
* glob
* time
* gaugette.gpio
* gaugette.ssd1306
* gaugette.platform
* Adafruit_BMP.BMP085


<img src="https://i.ibb.co/fM4J6d8/3d-1.png"/>
<img src="https://i.ibb.co/nL2Fptm/3d-2.png"/>
<img src="https://i.ibb.co/GvRKhvs/3d-3.png"/>
<img src="https://i.ibb.co/tq11nNs/3d-4.png"/>



 
### 3e – Hodnoty na displeji prepínajte tlačidlami alebo rotačným enkodérom

Pre túto úlohu sme nemuseli meniť nič pretože sme ju splnili už v úlohe 3d. Použili sme rotačný enkodér, pretože dát bolo príliš veľa a vytvárať rôzne programy pre jednotlivé dáta by bolo neefektívne.


