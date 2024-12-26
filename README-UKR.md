[<img src="https://img.shields.io/badge/python-3.11-blue">](https://www.python.org/downloads/) [<img src="https://img.shields.io/badge/python-3.12-blue">](https://www.python.org/downloads/) [<img src="https://img.shields.io/badge/python-3.13+-blue">](https://www.python.org/downloads/)

### [English version README](/README.md)

# [Blum Auto Clicker](https://t.me/blum/app?startapp=ref_hX75eRFPqv)

![image](https://github.com/user-attachments/assets/d9496bed-c1a0-4a1b-9673-1e64d0441621)

<div align="center">
<p>
<a href="https://github.com/devbutlazy/Blum-AutoClicker/stargazers"><img src="https://img.shields.io/github/stars/devbutlazy/Blum-AutoClicker?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=C9CBFF&labelColor=302D41" alt="stars"><a>&nbsp;&nbsp;
<a href="https://github.com/devbutlazy/Blum-AutoClicker/"><img src="https://img.shields.io/github/repo-size/devbutlazy/Blum-AutoClicker?style=for-the-badge&logo=hyprland&logoColor=f9e2af&label=Size&labelColor=302D41&color=f9e2af" alt="REPO SIZE"></a>&nbsp;&nbsp;
<a href="https://github.com/devbutlazy/Blum-AutoClicker/commits/main/"><img src="https://img.shields.io/github/last-commit/devbutlazy/Blum-AutoClicker?style=for-the-badge&logo=github&logoColor=eba0ac&label=Last%20Commit&labelColor=302D41&color=eba0ac" alt="Last Commit"></a>&nbsp;&nbsp;
<a href="https://github.com/devbutlazy/Blum-AutoClicker/LICENSE"><img src="https://img.shields.io/github/license/devbutlazy/Blum-AutoClicker?style=for-the-badge&logo=&color=CBA6F7&logoColor=CBA6F7&labelColor=302D41" alt="LICENSE"></a>&nbsp;&nbsp;
</p>
</div>

## ☕ Підтримайте мене
    USDT (ERC-20): 0x5F06C1c23aF7Cc644B8cBaF0e2b294CbA15CC745
    TON: UQD2g_C_aIeZ7-zAJ7uOQJUsr538vPcd_GljLeA-iRZL7tzF

## ⚡ Особливості v2
1. Робота над останніми оновленнями XMas 
2. Краще та швидше визначення точок
3. Емуляція людських кліків, іноді промахуючись при натисканні
4. Локалізація на різні мови
5. Підтримка 64Gram, Nekogram, Telegram Desktop


## 📕 Встановлення
> [!TIP]
> Дивіться відео з інструкціями на [YouTube](https://www.youtube.com/watch?v=euLpqjLB8jk)
  
Скопіюйте цей [**Repository**](https://github.com/devbutlazy/Blum-AutoClicker) і запустіть програму:
```shell
- - Увімкніть інструменти розробника в Експериментальних налаштуваннях у Telegram

~ >>> git clone https://github.com/devbutlazy/Blum-AutoClicker  
~ >>> cd Blum-AutoClicker

- Відкрийте вікно Blum
- Натисніть F12 і увімкніть Перевизначення на ./override
- Введіть «location.reload(true);» у консолі розробника

~/Blum-AutoClicker >>> python -m venv venv # Створіть віртуальне середовище
~/Blum-AutoClicker >>> venv\Scripts\activate # Активуйте віртуальне середовище
~/Blum-AutoClicker >>> pip install -r requirements.txt # Встановіть необхідні залежності
~/Blum-AutoClicker >>> python main.py # Запустіть програму та встановіть залежності
```

> [!TIP]
> Якщо у вас виникли помилки чи є ідеї то приєднуйтесь до **[Телеграм-каналу](https://t.me/blogbutlazy)** та **[Телеграм-чату](https://t.me/chatbutlazy)** і просіть допомоги там.


# ⭐ Розширені можливості (`core/config/config.json`)

- [x] Локалізація на різні мови. Ви можете знайти список доступних мов **[тут](/core/localization/langs)**.
```shell
# GNU/Linux
~/Blum-AutoClicker >>> python3 main.py --setlang lang # Замість lang вкажіть код мови яка є доступна
~/Blum-AutoClicker >>> python3 main.py --setlang ua # Приклад


# Windows
~/Blum-AutoClicker >>> python main.py --setlang lang # Замість lang вкажіть код мови яка є доступна
~/Blum-AutoClicker >>> python main.py --setlang ua # Приклад
```

- [x] Відображає конфігурацію підрахунку. Ви можете встановити кількість квитків, які будуть використані
```shell
# GNU/Linux
~/Blum-AutoClicker >>> python3 main.py --replays count # Встановіть кількість повторів
~/Blum-AutoClicker >>> python3 main.py --replays 50 # Приклад

# Windows
~/Blum-AutoClicker >>> python main.py --replays count # Встановіть кількість повторів
~/Blum-AutoClicker >>> python main.py --replays 50 # Приклад
```

- [x] Налаштування затримки між повторами
```shell
# GNU/Linux
~/Blum-AutoClicker >>> python3 main.py --delay delay_in_seconds # Встановіть затримку між повторами
~/Blum-AutoClicker >>> python3 main.py --delay 5 # Приклад

# Windows
~/Blum-AutoClicker >>> python main.py --delay delay_in_seconds # Встановіть затримку між повторами
~/Blum-AutoClicker >>> python main.py --delay 5 # Приклад
```

- [x] Оновлення при N-кількості ігор
```shell
# GNU/Linux
~/Blum-AutoClicker >>> python3 main.py --refresh count_of_games # Встановити через N-кількість ігор програма буде автоматично перезавантажуватися
~/Blum-AutoClicker >>> python3 main.py --refresh 10 # Приклад

# Windows
~/Blum-AutoClicker >>> python main.py --refresh count_of_games # Встановити через N-кількість ігор програма буде автоматично перезавантажуватися
~/Blum-AutoClicker >>> python main.py --refresh 10 # Приклад
```

> [!IMPORTANT]
> Ви можете відредагувати ці параметри конфігурації вручну у файлі `core/config/config.json`.


<br>


# ✍️ Внесок
Частиною того, що робить спільноту відкритого коду особливою, є внески. Будь-який внесок буде **дуже доречний!**.

Якщо у вас є ідеї або пропозиції, не соромтеся [відкрити тему](https://github.com/devbutlazy/Blum-AutoClicker/issues) or [submit a PR](https://github.com/devbutlazy/Blum-AutoClicker/pulls)

<br>

# 🤝 Особлива подяка
Без цих людей процес розвитку не відбувався б так швидко (або взагалі не відбувався б), тому я повинен згадати про них.
- [Nixxoq](https://github.com/nixxoq) - психологічна підтримка, допоміг з останнім оновленням (TC11RhiWns9tifP1F6eiek9dzBFtGCne5S)
- [BRamil](https://github.com/BRamil0) - переклав на Польску мову, допоміг з остальнім оновленням ([telegram](t.me/QulowDev))
- [qt333](https://github.com/qt333) - допоміг з "dogs" та розпізнаванням кнопок повторного відтворення
- [Gartner](https://t.me/waffenssgartner) - допомогіг з відеоінструкціями
- [Redish](https://github.com/xxmmcxx) - допоміг з перекладом на Перську мову
- [vjaykrsna](https://github.com/vjaykrsna) - helped with fixing the collecting only on left side issue

<br>


> [!NOTE]
> Цей репозиторій захищено **[Ліцензією MIT](https://opensource.org/license/mit)**, будь ласка, не міняйте ліцензію.
> <br>
> Перекладено [BRamil](https://github.com/BRamil0)
<p align="center">
	<img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" />
</p>
