# NAG-IoT
## PROJEKT SAMSON


### 1a) Pro Raspberry Pi doporučujeme standardní instalaci Raspbian.

Pre Raspberry Pi sme zvolili operačný systém Raspbian, ktorý je dostupný na
stiahnutie z oficiálnych stránok. Ten sme pomocou programu etcher nahrali na SD kartu a vložili do Raspberry Pi 3 model B.
Zariadenie sme používali v tzv. Headless režime teda nepripojili sme k
nemu monitor. Pri tomto použití je len nutné si dať pozor aby sme umiestnili do
adresára SD karty súbor SSH, ktorý necháme prázdny. Tento súbor zapne SSH
server na RPI a umožnuje nám vzdialenú správu.
Pri tomto použití je nutné zistiť IP adresu RaspberryPI v sieti, použili sme IP scanner pre lokálnu sieť.
Na Raspberry Pi sme sa pripojili pomocou programu MobaXterm
Vývojové prostredia sme neinštalovali, keďže programy sme písali na notebookoch a následne ich len skopírovali do Raspberry Pi
