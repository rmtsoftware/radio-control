#!/bin/bash

sudo chmod 766 /dev/ttyUSB0

# Активируйте виртуальное окружение
source venv/bin/activate

# Запустите ваш скрипт
python3 main.py