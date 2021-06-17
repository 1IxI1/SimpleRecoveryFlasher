# SimpleRecoveryFlasher
A simple tool for flashing your recovery
(русское руководство ниже)

<img src="https://i.ibb.co/hR3SqRc/screenshot.png" width="200">


## Install

### Windows
  * Download zip archive and unzip it
  * Open `SimpleRecoveryFlasher.exe` from directory SimpleRecoveryFlasherWindows

### Linux
  * Install the adb to your distro:

    Ubuntu: `sudo apt install android-sdk-platform-tools`

    Arch: `yaourt -S android-sdk-platform-tools`
  
  * Clone repository: `git clone https://github.com/1IxI1/SimpleRecoveryFlasher && cd SimpleRecoveryFlasher/SimpleRecoveryFlasher`
  * Run: `sudo python3 SimpleRecoveryFlasher.py`

## Using notes

  * Recovery must be in .img format
  * Bootloader must be unloced

## Where I can get recovery in .img format?

### TWRP
  * Go to the https://twrp.me/Devices/, select your device, scroll down to section Download, download the last version in .img

### Orange fox
  * Go to the https://orangefox.download/, select your device and download zip archive
  * Unzip archive
  * The resulting folder will contain your recovery


## Why should I run a programm from the sudo?
  For working with adb. You can make sure that adb does not work from a normal user by entering the `fastboot devices` command with the phone connected in fastboot mode. Also, if you are afraid, you can read the source code in the .py file or not run the program at all.
  
  
## Donate
  Card number: `4757880020409662`
  
  
----------------------
  
  
# SimpleRecoveryFlasher (Русский)
Простой инструмент для прошивки вашего рекавери

<img src="https://i.ibb.co/m4mZ5d0/screenshot-ru.png" width="200">


## Установка

### Windows
  * Скачайте zip-архив и разархивируйте
  * Откройте `SimpleRecoveryFlasher.exe` из директории SimpleRecoveryFlasherWindows_ru

### Linux
  * Установите adb для вашего дистрибутива:

    Ubuntu: `sudo apt install android-sdk-platform-tools python3-tk`

    Arch: `yay -S android-sdk-platform-tools`
  
  * Клонируйте репозиторий: `git clone https://github.com/1IxI1/SimpleRecoveryFlasher && cd SimpleRecoveryFlasher/SimpleRecoveryFlasher_ru`
  * Запустите: `sudo python3 SimpleRecoveryFlasher.py`

## Примечания по использованию

  * Файл рекавери должен быть в формате .img
  * Загрузчик должен быть разблокирован

## Где я возьму рекавери в формате .img?

### TWRP
  * Перейдите на https://twrp.me/Devices/, выберите ваш деваайс, пролистайте до секции Download, скачайте нужную версию в .img

### Orange fox
  * Перейдите на https://orangefox.download/, выберите ваш девайс и скачайте zip-архив
  * Разархивируйте его
  * В полученной папке будет лежать ваше рекавери
  
  
## Почему я должен запускать скрипт от sudo?
  Для работы adb. Вы можете убедиться, что adb не работает от обычного пользователя, введя команду `fastboot devices` с присоеденённым телефоном в режиме fastboot. Так же, если вы боитесь, вы можете почитать исходный код в .py файле или же вовсе не запускать программу.
  
  
## Поддержать разработчика
  Номер карты: `4757880020409662`
