# weather-parser-gismeteo
Парсер погоды с Gismeteo на Python + Selenium. Сохраняет в Excel.

# 🌤️ Парсер погоды с Gismeteo

Простой парсер погоды на Python + Selenium.  
Запрашивает город, парсит температуру с Gismeteo и сохраняет в Excel.

---

## 🚀 Как запустить

1. **Установи зависимости**
   ```bash
   pip install selenium pandas openpyxl

    Запусти программу
    bash

    python main.py

    Введи город
    text

    какой город? Москва

    Результат

        В консоли: Москва : +22°C

        В Excel: файл pogoda.xlsx с колонками Город и Температура
