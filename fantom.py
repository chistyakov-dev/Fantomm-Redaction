import json
import os
import time
import random
import shutil

SAVE_FILE = "saved_games.json"

def load_saved_games():
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_game(game_data):
    games = load_saved_games()
    games.append(game_data)
    with open(SAVE_FILE, 'w', encoding='utf-8') as f:
        json.dump(games, f, ensure_ascii=False, indent=2)
    print("✅ Игра успешно сохранена!")

def show_saved_games():
    games = load_saved_games()
    if not games:
        print("╔════════════════════════════════════╗")
        print("║ 📭 НЕТ СОХРАНЕННЫХ ИГР             ║")
        print("╚════════════════════════════════════╝")
        return None
    
    print("╔════════════════════════════════════════════╗")
    print("║ 📋 СПИСОК СОХРАНЁННЫХ ИГР                  ║")
    print("╠════════════════════════════════════════════╣")
    
    for i, game in enumerate(games, 1):
        name = game['name'][:20] + "..." if len(game['name']) > 20 else game['name']
        genre_display = ""
        if game.get('genre_type') == "rpg":
            genre_display = "🎮 RPG"
        elif game.get('genre_type') == "horror":
            genre_display = "👻 Хоррор"
        elif game.get('genre_type') == "detective":
            genre_display = "🕵️ Детектив"
        elif game.get('genre_type') == "Earth":
            genre_display = "🌍 Earth"
        elif game.get('genre_type') == "Средневековье":
            genre_display = "🏰 Средневековье"
        else:
            genre_display = f"[{game['platform']}]"
        print(f"║ {i}. {name:<20} {genre_display} ║")
    
    print("╚════════════════════════════════════════════╝")
    return games

def delete_saved_game(index):
    games = load_saved_games()
    if 1 <= index <= len(games):
        deleted = games.pop(index - 1)
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(games, f, ensure_ascii=False, indent=2)
        print(f"✅ Игра '{deleted['name']}' успешно удалена.")
        return True
    else:
        print("❌ Неверный номер игры.")
        return False

def edit_game(index):
    games = load_saved_games()
    game = games[index]
    
    print_menu(f"✏️ РЕДАКТИРОВАНИЕ: {game['name']}", [])
    print("Что вы хотите изменить?")
    print("1 — Название")
    print("2 — Платформу")
    print("3 — Возраст игроков")
    print("4 — ID игры")
    print("5 — Все параметры сюжета")
    print("0 — Отмена")
    
    choice = input("👉 Ваш выбор: ")
    
    if choice == "1":
        new_name = input(f"Новое название (было: {game['name']}): ")
        if new_name:
            game['name'] = new_name
            print(f"✅ Название изменено на '{new_name}'")
    
    elif choice == "2":
        print("1 — Мобайл\n2 — ПК\n3 — Гибрид")
        new_platform = input("Новая платформа: ")
        if new_platform == "1":
            game['platform'] = "Мобайл"
            print("✅ Платформа изменена на Мобайл")
        elif new_platform == "2":
            game['platform'] = "ПК"
            print("✅ Платформа изменена на ПК")
        elif new_platform == "3":
            game['platform'] = "Гибрид"
            print("✅ Платформа изменена на Гибрид")
    
    elif choice == "3":
        new_age = input(f"Новый возраст (было: {game.get('age', 'Не указан')}): ")
        if new_age:
            game['age'] = new_age
            print(f"✅ Возраст изменен на '{new_age}'")
    
    elif choice == "4":
        new_id = input(f"Новый ID (было: {game.get('id', 'Не указан')}): ")
        if new_id and len(new_id) >= 7:
            game['id'] = new_id
            print(f"✅ ID изменен на '{new_id}'")
        elif new_id:
            print("❌ ID должен быть не менее 7 символов")
    
    elif choice == "5":
        if game['genre_type'] == "hero_villain":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (Герой и злодей) ---")
            game['hero_name'] = input(f"Имя героя ({game['hero_name']}): ") or game['hero_name']
            game['villain_name'] = input(f"Имя злодея ({game['villain_name']}): ") or game['villain_name']
            game['hero_skill'] = input(f"Умение героя ({game['hero_skill']}): ") or game['hero_skill']
            game['villain_skill'] = input(f"Умение злодея ({game['villain_skill']}): ") or game['villain_skill']
            game['location'] = input(f"Локация ({game['location']}): ") or game['location']
            game['objective'] = input(f"Цель ({game['objective']}): ") or game['objective']
            game['win_action'] = input(f"Действие для победы ({game['win_action']}): ") or game['win_action']
            game['lose_action'] = input(f"Действие для поражения ({game['lose_action']}): ") or game['lose_action']
            
        elif game['genre_type'] == "friends":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (Два друга) ---")
            game['name_one'] = input(f"Имя первого друга ({game['name_one']}): ") or game['name_one']
            game['name_two'] = input(f"Имя второго друга ({game['name_two']}): ") or game['name_two']
            game['location'] = input(f"Локация ({game['location']}): ") or game['location']
            game['history'] = input(f"История ({game['history']}): ") or game['history']
            game['victory'] = input(f"Финал ({game['victory']}): ") or game['victory']
            
        elif game['genre_type'] == "action":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (Экшен) ---")
            game['hero_name'] = input(f"Имя героя ({game['hero_name']}): ") or game['hero_name']
            game['hero_weapon'] = input(f"Оружие ({game['hero_weapon']}): ") or game['hero_weapon']
            game['enemy_count'] = input(f"Количество врагов ({game['enemy_count']}): ") or game['enemy_count']
            game['boss_name'] = input(f"Имя босса ({game['boss_name']}): ") or game['boss_name']
            game['boss_ability'] = input(f"Способность босса ({game['boss_ability']}): ") or game['boss_ability']
            game['location'] = input(f"Локация ({game['location']}): ") or game['location']
            game['objective'] = input(f"Цель ({game['objective']}): ") or game['objective']
            game['win_action'] = input(f"Действие для победы ({game['win_action']}): ") or game['win_action']
            game['lose_action'] = input(f"Действие для поражения ({game['lose_action']}): ") or game['lose_action']
            
        elif game['genre_type'] == "survival":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (Выживание) ---")
            game['hero_name'] = input(f"Имя героя ({game['hero_name']}): ") or game['hero_name']
            
            try:
                new_food = input(f"Еда ({game['food']}): ")
                if new_food:
                    game['food'] = int(new_food)
                    
                new_water = input(f"Вода ({game['water']}): ")
                if new_water:
                    game['water'] = int(new_water)
                    
                new_medkits = input(f"Аптечки ({game['medkits']}): ")
                if new_medkits:
                    game['medkits'] = int(new_medkits)
                    
                new_days = input(f"Дней для выживания ({game['days_goal']}): ")
                if new_days:
                    game['days_goal'] = int(new_days)
            except ValueError:
                print("❌ Ошибка: введите число")
            
            game['danger'] = input(f"Опасность ({game['danger']}): ") or game['danger']
            
            fire_choice = input(f"Есть огонь? (да/нет) [сейчас: {'да' if game['has_fire'] else 'нет'}]: ")
            if fire_choice.lower() in ["да", "yes", "y"]:
                game['has_fire'] = True
            elif fire_choice.lower() in ["нет", "no", "n"]:
                game['has_fire'] = False
                
            shelter = input(f"Уровень убежища (1-3) [сейчас: {game['shelter_level']}]: ")
            if shelter in ["1", "2", "3"]:
                game['shelter_level'] = shelter
        
        elif game['genre_type'] == "rpg":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (RPG) ---")
            game['hero_name'] = input(f"Имя героя ({game['hero_name']}): ") or game['hero_name']
            game['hero_class'] = input(f"Класс ({game['hero_class']}): ") or game['hero_class']
            
            try:
                new_gold = input(f"Начальное золото ({game['starting_gold']}): ")
                if new_gold:
                    game['starting_gold'] = int(new_gold) if new_gold.isdigit() else game['starting_gold']
            except ValueError:
                print("❌ Ошибка: введите число")
            
            game['quest'] = input(f"Главный квест ({game['quest']}): ") or game['quest']
            game['companion'] = input(f"Спутник ({game['companion']}): ") or game['companion']
        
        elif game['genre_type'] == "horror":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (Хоррор) ---")
            game['hero_name'] = input(f"Имя героя ({game['hero_name']}): ") or game['hero_name']
            
            try:
                new_fear = input(f"Уровень страха ({game['fear_level']}): ")
                if new_fear:
                    game['fear_level'] = int(new_fear) if new_fear.isdigit() else game['fear_level']
                    
                new_batteries = input(f"Количество батареек ({game['batteries']}): ")
                if new_batteries:
                    game['batteries'] = int(new_batteries) if new_batteries.isdigit() else game['batteries']
            except ValueError:
                print("❌ Ошибка: введите число")
            
            game['monster'] = input(f"Тип монстра ({game['monster']}): ") or game['monster']
            game['location'] = input(f"Локация ({game['location']}): ") or game['location']
            game['objective'] = input(f"Цель ({game['objective']}): ") or game['objective']
        
        elif game['genre_type'] == "detective":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (Детектив) ---")
            game['detective_name'] = input(f"Имя детектива ({game['detective_name']}): ") or game['detective_name']
            game['location'] = input(f"Локация ({game['location']}): ") or game['location']
            game['history'] = input(f"История ({game['history']}): ") or game['history']
        
        elif game['genre_type'] == "Earth":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (Earth) ---")
            game['hero_name'] = input(f"Имя воина ({game['hero_name']}): ") or game['hero_name']
            game['weapons'] = input(f"Оружие ({game['weapons']}): ") or game['weapons']
            game['history'] = input(f"История ({game['history']}): ") or game['history']
        
        elif game['genre_type'] == "Средневековье":
            print("\n--- РЕДАКТИРОВАНИЕ СЮЖЕТА (Средневековье) ---")
            game['hero_name'] = input(f"Имя короля ({game['hero_name']}): ") or game['hero_name']
            game['kor_name'] = input(f"Название королевства ({game['kor_name']}): ") or game['kor_name']
            game['history'] = input(f"История ({game['history']}): ") or game['history']
        
        print("✅ Сюжет обновлен!")
    
    if choice != "0":
        games[index] = game
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(games, f, ensure_ascii=False, indent=2)
        print("✅ Изменения сохранены!")
    
    input("\nНажмите Enter для продолжения...")

def test_survival(game_data):
    food = game_data["food"]
    water = game_data["water"]
    medkits = game_data["medkits"]
    day = 1
    alive = True
    days_goal = game_data["days_goal"]
    has_fire = game_data["has_fire"]
    danger = game_data["danger"]

    print("╔════════════════════════════════════╗")
    print("║ 🎮 ТЕСТОВЫЙ РЕЖИМ: ВЫЖИВАНИЕ       ║")
    print("╚════════════════════════════════════╝")
    print(f"Вы — {game_data['hero_name']}. Цель: продержаться {days_goal} дней.")

    while day <= days_goal and alive:
        print(f"\n╔════════════════════════════════════╗")
        print(f"║ ДЕНЬ {day:<2}                         ║")
        print("╠════════════════════════════════════╣")
        print(f"║ 🍗 Еда: {food:<3}                      ║")
        print(f"║ 💧 Вода: {water:<3}                     ║")
        print(f"║ 💊 Аптечки: {medkits:<3}                  ║")
        print("╚════════════════════════════════════╝")
        
        water_cost = 2 if has_fire else 3
        food_cost = 2
        
        event = random.choice(["nothing", "find_food", "find_water", "injury", "thief", "danger_encounter"])
        
        if event == "find_food":
            found = random.randint(1, 5)
            food += found
            print(f"🍀 Вы нашли еду! +{found} еды.")
        elif event == "find_water":
            found = random.randint(1, 4)
            water += found
            print(f"💧 Вы нашли воду! +{found} воды.")
        elif event == "injury":
            print("╔════════════════════════════════════╗")
            print("║ 🤕 ТРАВМА                           ║")
            print("╠════════════════════════════════════╣")
            print("║ 1 — использовать аптечку           ║")
            print("║ 2 — не лечиться                    ║")
            print("╚════════════════════════════════════╝")
            use = input("👉 Ваш выбор: ")
            if use == "1" and medkits > 0:
                medkits -= 1
                print("💊 Аптечка использована, здоровье восстановлено.")
            else:
                print("❌ Вы не стали лечиться (или нет аптечек). Штраф к ресурсам.")
                food -= 1
                water -= 1
        elif event == "thief":
            stolen_food = random.randint(1, 3)
            stolen_water = random.randint(1, 2)
            food = max(0, food - stolen_food)
            water = max(0, water - stolen_water)
            print(f"👤 Воры украли часть припасов: -{stolen_food} еды, -{stolen_water} воды.")
        elif event == "danger_encounter":
            print(f"⚠️ Вы столкнулись с опасностью: {danger}!")
            print("╔════════════════════════════════════╗")
            print("║ 1 — сражаться                      ║")
            print("║ 2 — убежать                         ║")
            print("╚════════════════════════════════════╝")
            choice = input("👉 Ваш выбор: ")
            if choice == "1":
                food -= 1
                water -= 1
                if random.random() > 0.3:
                    print("⚔️ Вы отбили атаку, но потратили силы.")
                else:
                    print("💔 Вы ранены.")
                    print("╔════════════════════════════════════╗")
                    print("║ 1 — использовать аптечку           ║")
                    print("║ 2 — нет                            ║")
                    print("╚════════════════════════════════════╝")
                    use = input("👉 Ваш выбор: ")
                    if use == "1" and medkits > 0:
                        medkits -= 1
                        print("💊 Аптечка использована.")
                    else:
                        food -= 2
                        water -= 2
                        print("❌ Вы серьёзно пострадали. Ресурсы сильно уменьшены.")
            else:
                print("🏃 Вы убежали, но потеряли часть припасов в спешке.")
                food -= 1
                water -= 1
        
        food -= food_cost
        water -= water_cost
        
        if food <= 0 or water <= 0:
            print("\n💀 Вы погибли от истощения... Игра окончена.")
            alive = False
            break
        
        print(f"После дня: еда {food}, вода {water}, аптечки {medkits}")
        
        print("╔════════════════════════════════════╗")
        print("║ ЧТО ДЕЛАЕМ НА НОЧЬ?                ║")
        print("╠════════════════════════════════════╣")
        print("║ 1 — отдыхать                       ║")
        print("║ 2 — искать ресурсы                 ║")
        print("║ 3 — лечиться                       ║")
        print("╚════════════════════════════════════╝")
        action = input("👉 Ваш выбор: ")
        
        if action == "2":
            found_food = random.randint(0, 3)
            found_water = random.randint(0, 2)
            food += found_food
            water += found_water
            print(f"Вы нашли {found_food} еды и {found_water} воды.")
            if random.random() < 0.2:
                print("❌ Но вы поранились!")
                medkits -= 1 if medkits > 0 else 0
        elif action == "3":
            if medkits > 0:
                medkits -= 1
                print("💊 Вы подлечились. Здоровье улучшилось.")
                food += 1
            else:
                print("❌ Нет аптечек.")
        
        day += 1
    
    if alive and day > days_goal:
        print(f"\n✨ ПОБЕДА! Вы продержались {days_goal} дней!")
    elif not alive:
        print("💔 Вы не смогли выжить...")

def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def print_menu(title, options, width=None):
    if width is None:
        width = get_terminal_width()
        width = min(width, 60)
        width = max(width, 40)
    
    print("╔" + "═" * (width - 2) + "╗")
    
    # Жирный шрифт эмулируется заглавными буквами
    title_padding = width - len(title) - 4
    left_pad = title_padding // 2
    right_pad = title_padding - left_pad
    print("║" + " " * left_pad + title + " " * right_pad + "║")
    
    print("╠" + "═" * (width - 2) + "╣")
    
    for option in options:
        option_text = f"{option[0]} {option[1]}"
        if len(option_text) > width - 4:
            option_text = option_text[:width - 7] + "..."
        spaces = width - len(option_text) - 4
        print("║ " + option_text + " " * spaces + "║")
    
    print("╚" + "═" * (width - 2) + "╝")

def show_start_screen():
    width = get_terminal_width()
    width = min(width, 70)
    width = max(width, 50)
    
    print("╔" + "═" * (width - 2) + "╗")
    print("║" + " " * (width - 2) + "║")
    
    # Жирный шрифт для заголовка
    title = "⚡ FANTOM REDACTION ⚡"
    title_padding = width - len(title) - 2
    left_pad = title_padding // 2
    right_pad = title_padding - left_pad
    print("║" + " " * left_pad + title + " " * right_pad + "║")
    
    print("║" + " " * (width - 2) + "║")
    
    subtitle = "Многофункциональный движок для создания игр"
    if len(subtitle) > width - 4:
        subtitle = subtitle[:width - 7] + "..."
    sub_padding = width - len(subtitle) - 2
    left_sub = sub_padding // 2
    right_sub = sub_padding - left_sub
    print("║" + " " * left_sub + subtitle + " " * right_sub + "║")
    
    print("║" + " " * (width - 2) + "║")
    
    author = "от Cheymi Platforms"
    auth_padding = width - len(author) - 2
    left_auth = auth_padding // 2
    right_auth = auth_padding - left_auth
    print("║" + " " * left_auth + author + " " * right_auth + "║")
    
    print("║" + " " * (width - 2) + "║")
    print("╠" + "═" * (width - 2) + "╣")
    print("║" + " " * (width - 2) + "║")
    
    # Жирный шрифт для статистики
    stat_title = "📊 СТАТИСТИКА"
    stat_padding = width - len(stat_title) - 2
    left_stat = stat_padding // 2
    right_stat = stat_padding - left_stat
    print("║" + " " * left_stat + stat_title + " " * right_stat + "║")
    
    games = load_saved_games()
    games_count = len(games)
    mobile_count = sum(1 for g in games if g.get('platform') == "Мобайл")
    pc_count = sum(1 for g in games if g.get('platform') == "ПК")
    hybrid_count = sum(1 for g in games if g.get('platform') == "Гибрид")
    
    print(f"║ 📁 Всего игр создано: {games_count:<3}" + " " * (width - 28) + "║")
    print(f"║ 📱 Мобайл игр: {mobile_count:<3}" + " " * (width - 25) + "║")
    print(f"║ 💻 ПК игр: {pc_count:<3}" + " " * (width - 23) + "║")
    print(f"║ 🔄 Гибридных игр: {hybrid_count:<3}" + " " * (width - 29) + "║")
    
    print("║" + " " * (width - 2) + "║")
    print("╠" + "═" * (width - 2) + "╣")
    print("║" + " " * (width - 2) + "║")
    
    # Жирный шрифт для быстрого старта
    fast_title = "🎮 БЫСТРЫЙ СТАРТ"
    fast_padding = width - len(fast_title) - 2
    left_fast = fast_padding // 2
    right_fast = fast_padding - left_fast
    print("║" + " " * left_fast + fast_title + " " * right_fast + "║")
    
    if games_count > 0:
        last_title = "Последние созданные игры:"
        print("║ " + last_title + " " * (width - len(last_title) - 4) + "║")
        for i, game in enumerate(games[-3:], 1):
            game_text = f"{i}. {game['name'][:25]}"
            if len(game_text) > width - 6:
                game_text = game_text[:width - 9] + "..."
            print("║ " + game_text + " " * (width - len(game_text) - 4) + "║")
    else:
        welcome = "👋 Добро пожаловать! Создайте свою"
        print("║ " + welcome + " " * (width - len(welcome) - 4) + "║")
        first_game = "первую игру!"
        print("║ " + first_game + " " * (width - len(first_game) - 4) + "║")
    
    print("║" + " " * (width - 2) + "║")
    print("╚" + "═" * (width - 2) + "╝")
    print()
    
    print("🔄 Загрузка", end="")
    for i in range(3):
        time.sleep(0.3)
        print(".", end="")
    print(" Готово!\n")
    time.sleep(3.0)

show_start_screen()

while True:
    print_menu("🎮 МЕНЮ ИГРЫ", [
        ("1", "Создать игру"),
        ("2", "Настройки"),
        ("3", "Загрузить игру"),
        ("4", "Управление сохранениями"),
        ("5", "Редактировать игру"),
        ("0", "Выход")
    ])
    game = input("👉 Ваш выбор: ")
    
    if game == "1":
        game_name = input("📝 Введите название для вашей игры: ")
        print(f"✓ Название игры: {game_name}\n")
        
        while True:
            game_version = input("📱 Выберите платформу:\n1 — Мобайл\n2 — ПК\n3 — Гибрид\n👉 Ваш выбор: ")
            plot = input("📖 Напишите жанр вашей игры: ")
            print("✓ Жанр игры:", plot)
            wozrast_name = input("Напишите возрастное ограничение в вашей игре: ")
            print(f"Возраст игрока: {wozrast_name}\n")
            ID_name = input("Создайте для своей игры уникальный ID, введите не менее 7 символов:\n")
            print(f"ID: {ID_name}")
            platform = ""
            if game_version == "1":
                platform = "Мобайл"
                print("📱 Вы выбрали разработку для мобильных устройств")
                print("🔄 Запуск настройки мобильной версии...")
                print("✅ Мобильная версия успешно настроена!\n")
                break
            elif game_version == "2":
                platform = "ПК"
                print("💻 Вы выбрали разработку для ПК")
                print("🔄 Запуск настройки ПК версии...")
                print("✅ ПК версия успешно настроена!\n")
                break
            elif game_version == "3":
                platform = "Гибрид"
                print("🔄 Вы выбрали гибридную разработку (мобайл + ПК)")
                print("🔄 Запуск настройки гибридной версии...")
                print("✅ Гибридная версия успешно настроена!\n")
                break
            else:
                print("❌ Неверный выбор. Введите 1, 2 или 3.\n")
        
        print_menu("📖 ВЫБОР СЮЖЕТА", [
            ("1", "Герой и злодей"),
            ("2", "Два друга"),
            ("3", "Экшен"),
            ("4", "Выживание"),
            ("5", "RPG"),
            ("6", "Хоррор"),
            ("7", "Детектив"),
            ("8", "Earth"),
            ("9", "Средневековье")
        ])
        genre = input("👉 Ваш выбор: ")
        
        if genre == "1":
            hero_name = input("🧙 Имя главного героя: ")
            villain_name = input("👿 Имя главного злодея: ")
            hero_skill = input("⚡ Умение героя: ")
            villain_skill = input("💀 Умение злодея: ")
            location = input("🏞️ Где происходит действие: ")
            objective = input("🎯 Что должен сделать герой: ")
            win_action = input("✅ Напишите его действие для победы: ")
            lose_action = input("❌ Напишите его действие для поражения: ")
            
            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "hero_villain",
                "hero_name": hero_name,
                "villain_name": villain_name,
                "hero_skill": hero_skill,
                "villain_skill": villain_skill,
                "location": location,
                "objective": objective,
                "win_action": win_action,
                "lose_action": lose_action,
                "age": wozrast_name,
                "id": ID_name
            }
            
            print(f"\n✅ Игра '{game_name}' успешно создана!")
            print(f"📜 Краткое описание: Вы — {hero_name}, обладающий умением {hero_skill}. Действие происходит в {location}. Вам нужно {objective}.")
            
            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)
            
            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
                print(f"Вы — {hero_name}. Ваше умение: {hero_skill}.")
                print(f"Вы находитесь в {location}. Вам нужно {objective}.")
                print("Что вы будете делать?")
                print(f"1. {win_action}")
                print(f"2. {lose_action}")
                action = input("👉 Ваш выбор (1 или 2): ")
                if action == "1":
                    print("✨ Победа! Вы успешно справились с задачей.")
                elif action == "2":
                    print("💔 Поражение... Вы проиграли.")
                else:
                    print("❓ Непонятный выбор. Игра прервана.")
            else:
                print("Ок, тест пропущен.")
        
        elif genre == "2":
            name_one = input("👤 Имя первого друга: ")
            name_two = input("👤 Имя второго друга: ")
            location = input("🏞️ Где происходит действие: ")
            history = input("📖 Краткая история двух друзей: ")
            victory = input("🏁 Как всё закончится: ")
            
            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "friends",
                "name_one": name_one,
                "name_two": name_two,
                "location": location,
                "history": history,
                "victory": victory,
                "age": wozrast_name,
                "id": ID_name
            }
            
            print(f"\n✅ Игра '{game_name}' успешно создана!")
            print(f"📜 Краткое описание: Основной сюжет развивается вокруг {name_one} и {name_two}, действие происходит в {location}.")
            
            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)
            
            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
                print(f"Вы — {name_one} и {name_two}.")
                print(f"Вы находитесь в {location}. Ваша история: {history}")
                print("Представьте, что вы поссорились. Что вы сделаете?")
                print_menu("ВЫБОР", [
                    ("1", "подарить подарок и извиниться первым"),
                    ("2", "не общаться")
                ])
                vybor = input("👉 Ваш выбор: ")
                if vybor == "1":
                    print("✨ Победа! Вы успешно помирились.")
                elif vybor == "2":
                    print("💔 Поражение... Дружба разрушена.")
                else:
                    print("❓ Непонятный выбор. Игра прервана.")
            else:
                print("Ок, тест пропущен.")
        
        elif genre == "3":
            hero_name = input("🧙 Имя героя: ")
            hero_weapon = input("🔫 Оружие героя: ")
            enemy_count = input("👥 Количество врагов (число): ")
            boss_name = input("👾 Имя босса: ")
            boss_ability = input("💥 Способность босса: ")
            location = input("🏞️ Локация: ")
            objective = input("🎯 Цель миссии: ")
            win_action = input("✅ Напишите его действие для победы (например, 'использовать супер-оружие'): ")
            lose_action = input("❌ Напишите его действие для поражения (например, 'попасть в ловушку'): ")
            
            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "action",
                "hero_name": hero_name,
                "hero_weapon": hero_weapon,
                "enemy_count": enemy_count,
                "boss_name": boss_name,
                "boss_ability": boss_ability,
                "location": location,
                "objective": objective,
                "win_action": win_action,
                "lose_action": lose_action,
                "age": wozrast_name,
                "id": ID_name
            }
            
            print(f"\n✅ Игра '{game_name}' (Экшен) успешно создана!")
            print(f"📜 Краткое описание: Вы — {hero_name} с оружием {hero_weapon}. Вам предстоит сразиться с {enemy_count} врагами и боссом {boss_name}, который умеет {boss_ability}. Действие происходит в {location}. Цель: {objective}.")
            
            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)
            
            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
                print(f"Вы — {hero_name}, вооруженный {hero_weapon}.")
                print(f"На вас нападают {enemy_count} врагов, а из тени появляется босс {boss_name} с умением {boss_ability}.")
                print(f"Локация: {location}. Цель: {objective}.")
                print("Что вы будете делать?")
                print(f"1. {win_action}")
                print(f"2. {lose_action}")
                action = input("👉 Ваш выбор (1 или 2): ")
                if action == "1":
                    print("✨ Эпическая победа! Вы уничтожили всех врагов и спасли мир!")
                elif action == "2":
                    print("💔 Сокрушительное поражение... Ваша миссия провалена.")
                else:
                    print("❓ Непонятный выбор. Игра прервана.")
            else:
                print("Ок, тест пропущен.")
        
        elif genre == "4":
            hero_name = input("🧙 Имя героя: ")
            print("\n--- Начальные ресурсы (рекомендуется от 5 до 20) ---")
            food = input("🍗 Еда (число): ")
            water = input("💧 Вода (число): ")
            medkits = input("💊 Аптечки (число): ")
            danger = input("👾 Основная опасность (например, 'дикие звери', 'холод', 'нехватка ресурсов'): ")
            days_goal = input("⏳ Сколько дней нужно продержаться (число): ")
            
            print("\n--- Дополнительные условия ---")
            has_fire = input("🔥 Есть ли доступ к огню? (да/нет): ").lower() in ["да", "yes", "y"]
            shelter_level = input("🏕️ Уровень убежища (1 - шалаш, 2 - землянка, 3 - бункер): ")
            while shelter_level not in ["1", "2", "3"]:
                shelter_level = input("Пожалуйста, введите 1, 2 или 3: ")
            
            try:
                food = int(food) if food.isdigit() else 10
                water = int(water) if water.isdigit() else 10
                medkits = int(medkits) if medkits.isdigit() else 3
                days_goal = int(days_goal) if days_goal.isdigit() else 7
            except ValueError:
                food, water, medkits, days_goal = 10, 10, 3, 7
            
            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "survival",
                "hero_name": hero_name,
                "food": food,
                "water": water,
                "medkits": medkits,
                "danger": danger,
                "days_goal": days_goal,
                "has_fire": has_fire,
                "shelter_level": shelter_level,
                "age": wozrast_name,
                "id": ID_name
            }
            
            print(f"\n✅ Игра '{game_name}' (Выживание) успешно создана!")
            print(f"📜 Краткое описание: Вы — {hero_name} в суровых условиях. Вам угрожает {danger}. Нужно продержаться {days_goal} дней.")
            print(f"📦 Начальные ресурсы: еда {food}, вода {water}, аптечки {medkits}.")
            print(f"🏕️ Убежище уровня {shelter_level}, огонь: {'есть' if has_fire else 'нет'}.")
            
            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)
            
            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                test_survival(game_data)
            else:
                print("Ок, тест пропущен.")
        
        elif genre == "5":
            hero_name = input("🧙 Имя героя: ")
            hero_class = input("🏹 Выберите класс (воин, маг, лучник): ")
            starting_gold = input("💰 Начальное золото: ")
            quest = input("📜 Главный квест: ")
            companion = input("👥 Имя спутника: ")

            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "rpg",
                "hero_name": hero_name,
                "hero_class": hero_class,
                "starting_gold": starting_gold,
                "quest": quest,
                "companion": companion,
                "age": wozrast_name,
                "id": ID_name
            }

            print(f"\n✅ Игра '{game_name}' (RPG) успешно создана!")
            print(f"📜 Краткое описание: Вы — {hero_name}, класс {hero_class}. У вас {starting_gold} золота. Ваш спутник — {companion}. Главный квест: {quest}.")

            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)

            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ (RPG)", [])
                print(f"Вы — {hero_name}, класс {hero_class}. У вас {starting_gold} золота.")
                print(f"Ваш спутник: {companion}. Главный квест: {quest}.")
                print("Вы отправляетесь в путь. Встречаете разбойников.")
                print_menu("ВЫБОР", [
                    ("1", "сразиться"),
                    ("2", "договориться")
                ])
                action = input("👉 Ваш выбор: ")
                if action == "1":
                    print("⚔️ Вы победили, но потеряли 10 золота.")
                elif action == "2":
                    print("🤝 Вы откупились 20 золота и продолжили путь.")
                else:
                    print("❓ Непонятный выбор.")
            else:
                print("Ок, тест пропущен.")
        
        elif genre == "6":
            hero_name = input("🧙 Имя героя: ")
            print("\n--- Параметры ужаса ---")
            fear_level = input("😱 Начальный уровень страха (0-100, например 30): ")
            batteries = input("🔋 Количество батареек для фонарика: ")
            monster = input("👾 Тип монстра (призрак, маньяк, зомби и т.п.): ")
            location = input("🏚️ Локация (заброшенный дом, лес, больница): ")
            objective = input("🎯 Цель (например, 'найти выход', 'пережить ночь'): ")

            try:
                fear_level = int(fear_level) if fear_level.isdigit() else 30
                batteries = int(batteries) if batteries.isdigit() else 3
            except ValueError:
                fear_level, batteries = 30, 3

            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "horror",
                "hero_name": hero_name,
                "fear_level": fear_level,
                "batteries": batteries,
                "monster": monster,
                "location": location,
                "objective": objective,
                "age": wozrast_name,
                "id": ID_name
            }

            print(f"\n✅ Игра '{game_name}' (Хоррор) успешно создана!")
            print(f"📜 Краткое описание: Вы — {hero_name} в {location}. Вас преследует {monster}. Цель: {objective}.")
            print(f"😱 Начальный страх: {fear_level}, 🔋 батареек: {batteries}.")

            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)

            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ (ХОРРОР)", [])
                print(f"Вы — {hero_name}. Локация: {location}. Монстр: {monster}.")
                print(f"Уровень страха: {fear_level}, батареек: {batteries}.")
                print("Вы слышите шорох...")
                print_menu("ВЫБОР", [
                    ("1", "проверить"),
                    ("2", "спрятаться")
                ])
                action = input("👉 Ваш выбор: ")
                if action == "1":
                    fear_level += 20
                    batteries -= 1
                    print("😨 Вы увидели монстра! Страх вырос, батарейка потрачена.")
                elif action == "2":
                    fear_level += 5
                    print("😰 Вы затаились, страх немного вырос.")
                else:
                    print("❓ Непонятный выбор.")

                if fear_level >= 100:
                    print("💔 Вы обезумели от страха... Игра окончена.")
                elif batteries <= 0:
                    print("🔋 Батарейки кончились. Монстр настиг вас в темноте...")
                else:
                    print(f"✨ Вы продержались! Итог: страх {fear_level}, батареек {batteries}.")
            else:
                print("Ок, тест пропущен.")
        
        elif genre == "7":
            detective_name = input("🕵️‍♂️ Как будут звать детектива: ")
            location = input("🏞️ Где будете расследовать дело: ")
            history = input("📖 Напишите краткую историю о детективе: ")
            
            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "detective",
                "detective_name": detective_name,
                "location": location,
                "history": history,
                "age": wozrast_name,
                "id": ID_name
            }
            
            print(f"\n✅ Игра '{game_name}' (Детектив) успешно создана!")
            print(f"📜 Краткое описание: Детектив {detective_name} - {history}, вы расследуете дело в {location}.")
            
            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)
            
            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ (ДЕТЕКТИВ)", [])
                print(f"Вы — детектив {detective_name}.")
                print(f"Вы расследуете дело в {location}. Ваша история: {history}")
                print(f"🕵️‍♀️ Ваше Расследование: {detective_name}, взялся за расследование дела №553 о краже пачки чипсов из магазина. Преступник был в маске, его засекли камеры видеонаблюдения, как убрал чипсы под куртку. Ваша задача - выбрать, что будете делать. ")
                print_menu("ВЫБОР", [
                    ("1", "Попробовать спросить у работников магазина, видели ли они его"),
                    ("2", "Не расследовать")
                ])
                vybor = input("👉 Ваш выбор: ")
                if vybor == "1":
                    print("Все работники магазина не видели его, кроме Эллиота. В тот момент он вешал ценник на полку. Эллиот сказал, что у вора выпала визитная карточка - его зовут Андрей Шишков. Что вы сделаете?")
                    print_menu("ВЫБОР", [
                        ("1", "Обратиться к помощи полиции"),
                        ("2", "Попробовать найти его самому")
                    ])
                    vyybor = input("👉 Ваш выбор: ")
                    if vyybor == "1":
                        print("🎉 Поздравляем, полиция нашла преступника, он понёс наказание в виде штрафа! А вам дали премию.")
                    elif vyybor == "2":
                        print("К сожалению, вы детектив, а не Шерлок Холмс. Ваше дело передали другому, вы остались без премии...")
                    else:
                        print("❓ Непонятный выбор.")
                elif vybor == "2":
                    print("💔 Вы забросили дело, даже не начав его. Проигрыш...")
                else:
                    print("❓ Непонятный выбор. Игра прервана.")
            else:
                print("Ок, тест пропущен.")
        
        elif genre == "8":
            hero_name = input("🧙 Имя воина: ")
            weapons = input("🗡 Его оружие: ")
            history = input("Напишите краткую историю, как герой стал(а) воином.")

            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "Earth",
                "hero_name": hero_name,
                "weapons": weapons,
                "history": history,
                "age": wozrast_name,
                "id": ID_name
            }

            print(f"\n✅ Игра '{game_name}' (Earth) успешно создана!")
            print(f"📜 Краткое описание: Вы — {hero_name}, ваша история: {history}. Вас призвали на войну с инопланетным разумом.")

            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)

            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ (EARTH)", [])
                print(f"📜 Краткое описание: Вы — {hero_name}, ваша история: {history}. Вас призвали на войну с инопланетным разумом.")
                vybor = input("1 - пойти биться, 2 - лежать и отдыхать.\n👉 Ваш выбор: ")
                if vybor == "1":
                    print("⚔️ Вы прибыли в зону боевых действий, инопланетянин бежит на вас, что будете делать?")
                    vyybor = input("1 - Атаковать его выбранным оружием, 2 - отпрыгнуть в сторону.\n👉 Ваш выбор: ")
                    if vyybor == "1":
                        print("Вы не успели достать оружие, вас убили, вы проиграли...")
                    elif vyybor == "2":
                        print("Вы спаслись от гибели. Инопланетян остаётся немного. Есть план:")
                        vyyybor = input("1 - попросить их вежливо уйти, 2 - продолжить борьбу:\n👉 Ваш выбор: ")
                        if vyyybor == "1":
                            print("Вы смогли договориться! Инопланетяне улетели с Земли, ПОБЕДА!")
                        elif vyyybor == "2":
                            print("Борьба понесла много потерь, вас ранили, но вы всё равно ПОБЕДИЛИ!")
                        else:
                            print("❓ Непонятный выбор.")
                    else:
                        print("❓ Непонятный выбор.")
                elif vybor == "2":
                    print("▶️ К сожалению инопланетяне истребили всё человечество... Вы проиграли.")
                else:
                    print("❓ Непонятный выбор.")
            else:
                print("Ок, тест пропущен.")
        
        elif genre == "9":
            hero_name = input("👑 Имя короля: ")
            kor_name = input("🏰 Название королевства: ")
            enemy_kingdom = input("⚔️ Враждебное королевство: ")
            history = input(f"Напишите краткую историю, как {hero_name} стал(а) королём королевства.")

            game_data = {
                "name": game_name,
                "platform": platform,
                "genre_type": "Средневековье",
                "hero_name": hero_name,
                "kor_name": kor_name,
                "history": history,
                "age": wozrast_name,
                "id": ID_name
            }

            print(f"\n✅ Игра '{game_name}' (Средневековье) успешно создана!")
            print(f"📜 Краткое описание: Вы — {hero_name}, ваша история: {history}. Вы стали королём королевства {kor_name}.")

            save_choice = input("\n💾 Сохранить игру? (да/нет): ")
            if save_choice.lower() in ["да", "yes", "y"]:
                save_game(game_data)

            test_choice = input("🎮 Протестировать? (да/нет): ")
            if test_choice.lower() in ["да", "yes", "y"]:
                print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ (СРЕДНЕВЕКОВЬЕ)", [])
                print(f"📜 Краткое описание: Вы — {hero_name}, ваша история: {history}. Вы стали королём королевства {kor_name}.")
                print(f"Итак, в вашем королевстве проблема с урожаем, что будете делать?")
                vybor = input("1 - попросить помощи у другого королевства, 2 - Поддержка населения путём использования гос. резервов.\n👉 Ваш выбор: ")
                if vybor == "1":
                    print("⚔️ Другое королевство воспользовалось вашей ситуацией и напало на вас, воины были голодными и слабыми, вас захватили. ВЫ ПРОИГРАЛИ...")
                elif vybor == "2":
                    print("Это хорошо, но еды на всех не хватит, что делать с тем, что у нас неплодородные земли?")
                    vyyybor = input("1 - обменять ресурсы с другим королевством, которых в достатке на еду, 2 - запретить вывоз зерна:\n👉 Ваш выбор: ")
                    if vyyybor == "1":
                        print("Вы смогли договориться! Теперь еды хватит всем, а также вы улучшили отношения с королевством ПАНГДИОМАС.")
                    elif vyyybor == "2":
                        print("Вывоз зерна был запрещён, но у нас неплодородные земли, растить негде, из-за голода погибло много людей, расцвело воровство, ВЫ ПРОИГРАЛИ...")
                    else:
                        print("❓ Непонятный выбор.")
                else:
                    print("❓ Непонятный выбор.")
            else:
                print("Ок, тест пропущен.")
        
        else:
            print("❌ Неверный выбор жанра.")
        
        continue_choice = input("\n🔄 Хотите создать еще одну игру? (да/нет): ")
        if continue_choice.lower() not in ["да", "yes", "y"]:
            print("👋 Спасибо за использование FANTOM Redaction! До свидания!")
            break
    
    elif game == "2":
        while True:
            print_menu("⚙️ НАСТРОЙКИ", [
                ("м", "Мощность"),
                ("о", "О нас"),
                ("я", "Язык"),
                ("г", "Графика"),
                ("5", "Вернуться назад")
            ])
            settings = input("👉 Ваш выбор: ")
            
            if settings.lower() == "м":
                print_menu("🔧 НАСТРОЙКИ МОЩНОСТИ", [
                    ("⚡ Текущий режим:", "Стандарт"),
                    ("📊 Доступные режимы:", ""),
                    (" 🌱", "Эконом — экономия заряда"),
                    (" ⚡", "Стандарт — оптимальная работа"),
                    (" 🚀", "Максимальная — высокая производительность")
                ])
                input("\nНажмите Enter для продолжения...")
            
            elif settings.lower() == "о":
                print_menu("ℹ️ О НАС", [
                    ("FANTOM Redaction", ""),
                    ("многофункциональный движок", ""),
                    ("для создания игр", ""),
                    ("от Cheymi Platforms", ""),
                    ("", ""),
                    ("📅 Версия:", "V3.0.8"),
                    ("👥 Разработчик:", "Егор Чистяков"),
                ])
                input("\nНажмите Enter для продолжения...")
            
            elif settings.lower() == "x" or settings == "5":
                print("🔙 Возврат в главное меню...\n")
                break
            
            elif settings == "я":
                print_menu("🌐 НАСТРОЙКИ ЯЗЫКА", [
                    ("1", "Русский"),
                    ("2", "English"),
                    ("3", "Қазақша")
                ])
                lang_choice = input("👉 Ваш выбор: ")
                if lang_choice in ["1", "2", "3"]:
                    print("✅ Язык изменен (функция в разработке)")
                else:
                    print("❌ Неверный выбор")
            
            elif settings == "г":
                print_menu("🎮 НАСТРОЙКИ ГРАФИКИ", [
                    ("1", "Низкая (для слабых устройств)"),
                    ("2", "Средняя (рекомендуется)"),
                    ("3", "Высокая (для мощных ПК)")
                ])
                graphics_choice = input("👉 Ваш выбор: ")
                if graphics_choice in ["1", "2", "3"]:
                    print("✅ Настройки графики сохранены")
                else:
                    print("❌ Неверный выбор")
            
            else:
                print("❌ Неверный выбор. Попробуйте снова.\n")
    
    elif game == "3":
        games = show_saved_games()
        if games:
            try:
                print_menu("🎮 ЗАГРУЗКА ИГРЫ", [
                    ("0", "Отмена")
                ])
                choice = input("👉 Введите номер игры (0 — отмена): ")
                if choice == "0":
                    continue
                
                choice = int(choice)
                if 1 <= choice <= len(games):
                    loaded_game = games[choice - 1]
                    
                    print_menu(f"✅ {loaded_game['name']}", [])
                    print(f"📱 Платформа: {loaded_game['platform']}")
                    print(f"🆔 ID: {loaded_game.get('id', 'Нет')}")
                    print(f"👤 Возраст: {loaded_game.get('age', 'Нет')}")
                    
                    if loaded_game.get('genre_type') == "friends":
                        print(f"📜 Сюжет: Друзья")
                        print(f"👥 {loaded_game['name_one']} и {loaded_game['name_two']}")
                        print(f"🌍 {loaded_game['location']}")
                        print(f"📖 {loaded_game['history']}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            print_menu("🎮 ТЕСТ (ЗАГРУЖЕННАЯ ИГРА)", [])
                            print(f"Вы — {loaded_game['name_one']} и {loaded_game['name_two']}.")
                            print(f"Локация: {loaded_game['location']}")
                            print(f"История: {loaded_game['history']}")
                            print("\nПредставьте, что вы поссорились. Что вы сделаете?")
                            print_menu("ВЫБОР", [
                                ("1", "подарить подарок"),
                                ("2", "не общаться")
                            ])
                            vybor = input("👉 Ваш выбор: ")
                            if vybor == "1":
                                print("✨ Победа! Друзья помирились.")
                            elif vybor == "2":
                                print("💔 Поражение... Дружба разрушена.")
                            else:
                                print("❓ Непонятный выбор.")
                    
                    elif loaded_game.get('genre_type') == "action":
                        print(f"🧙 Герой: {loaded_game['hero_name']}")
                        print(f"🔫 Оружие: {loaded_game['hero_weapon']}")
                        print(f"👾 Враги: {loaded_game['enemy_count']}")
                        print(f"👾 Босс: {loaded_game['boss_name']}")
                        print(f"💥 Способность: {loaded_game['boss_ability']}")
                        print(f"🌍 {loaded_game['location']}")
                        print(f"🎯 {loaded_game['objective']}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            print_menu("🎮 ТЕСТ (ЗАГРУЖЕННАЯ ИГРА — ЭКШЕН)", [])
                            print(f"Вы — {loaded_game['hero_name']} с {loaded_game['hero_weapon']}.")
                            print(f"Врагов: {loaded_game['enemy_count']}, босс {loaded_game['boss_name']} готовится к атаке!")
                            print(f"Локация: {loaded_game['location']}. Цель: {loaded_game['objective']}.")
                            print("\nЧто вы будете делать?")
                            print(f"1. {loaded_game['win_action']}")
                            print(f"2. {loaded_game['lose_action']}")
                            action = input("👉 Ваш выбор: ")
                            if action == "1":
                                print("✨ Эпическая победа! Миссия выполнена!")
                            elif action == "2":
                                print("💔 Поражение... Вы проиграли.")
                            else:
                                print("❓ Непонятный выбор.")
                    
                    elif loaded_game.get('genre_type') == "survival":
                        print(f"🧙 Герой: {loaded_game['hero_name']}")
                        print(f"🍗 Еда: {loaded_game['food']} | 💧 Вода: {loaded_game['water']} | 💊 Аптечки: {loaded_game['medkits']}")
                        print(f"👾 Опасность: {loaded_game['danger']}")
                        print(f"⏳ Цель: продержаться {loaded_game['days_goal']} дней")
                        print(f"🏕️ Убежище уровня {loaded_game['shelter_level']}, огонь: {'есть' if loaded_game['has_fire'] else 'нет'}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            test_survival(loaded_game)
                    
                    elif loaded_game.get('genre_type') == "rpg":
                        print(f"🧙 Герой: {loaded_game['hero_name']} ({loaded_game['hero_class']})")
                        print(f"💰 Золото: {loaded_game['starting_gold']}")
                        print(f"👥 Спутник: {loaded_game['companion']}")
                        print(f"📜 Квест: {loaded_game['quest']}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            print_menu("🎮 ТЕСТ (ЗАГРУЖЕННАЯ ИГРА — RPG)", [])
                            print(f"Вы — {loaded_game['hero_name']}, класс {loaded_game['hero_class']}. У вас {loaded_game['starting_gold']} золота.")
                            print(f"Ваш спутник: {loaded_game['companion']}. Главный квест: {loaded_game['quest']}.")
                            print("Вы отправляетесь в путь. Встречаете разбойников.")
                            print_menu("ВЫБОР", [
                                ("1", "сразиться"),
                                ("2", "договориться")
                            ])
                            action = input("👉 Ваш выбор: ")
                            if action == "1":
                                print("⚔️ Вы победили, но потеряли 10 золота.")
                            elif action == "2":
                                print("🤝 Вы откупились 20 золота и продолжили путь.")
                            else:
                                print("❓ Непонятный выбор.")
                    
                    elif loaded_game.get('genre_type') == "horror":
                        print(f"🧙 Герой: {loaded_game['hero_name']}")
                        print(f"😱 Уровень страха: {loaded_game['fear_level']}, 🔋 батареек: {loaded_game['batteries']}")
                        print(f"👾 Монстр: {loaded_game['monster']}")
                        print(f"🏚️ Локация: {loaded_game['location']}")
                        print(f"🎯 Цель: {loaded_game['objective']}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            print_menu("🎮 ТЕСТ (ЗАГРУЖЕННЫЙ ХОРРОР)", [])
                            fear = loaded_game['fear_level']
                            bat = loaded_game['batteries']
                            print(f"Вы — {loaded_game['hero_name']}. Локация: {loaded_game['location']}. Монстр: {loaded_game['monster']}.")
                            print(f"Страх: {fear}, батареек: {bat}.")
                            print_menu("ВЫБОР", [
                                ("1", "идти на звук"),
                                ("2", "ждать")
                            ])
                            action = input("👉 Ваш выбор: ")
                            if action == "1":
                                fear += 15
                                bat -= 1
                                print("Вы наткнулись на монстра! Страх +15, батарейка -1.")
                            else:
                                fear += 10
                                print("Ожидание усилило тревогу. Страх +10.")
                            if fear >= 100:
                                print("💔 Вы не выдержали ужаса...")
                            elif bat <= 0:
                                print("🔋 Тьма поглотила вас...")
                            else:
                                print(f"✅ Вы выжили! Страх: {fear}, батареек: {bat}.")
                    
                    elif loaded_game.get('genre_type') == "detective":
                        print(f"🕵️ Детектив: {loaded_game['detective_name']}")
                        print(f"🏞️ Локация: {loaded_game['location']}")
                        print(f"📖 История: {loaded_game['history']}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            print_menu("🎮 ТЕСТ (ЗАГРУЖЕННЫЙ ДЕТЕКТИВ)", [])
                            print(f"Вы — детектив {loaded_game['detective_name']}.")
                            print(f"Вы расследуете дело в {loaded_game['location']}. Ваша история: {loaded_game['history']}")
                            print(f"🕵️‍♀️ Вы взялись за расследование дела №553 о краже пачки чипсов из магазина. Что будете делать?")
                            print_menu("ВЫБОР", [
                                ("1", "Спросить у работников"),
                                ("2", "Бросить дело")
                            ])
                            vybor = input("👉 Ваш выбор: ")
                            if vybor == "1":
                                print("Эллиот видел вора и нашел его визитку. Имя - Андрей Шишков.")
                                print_menu("ВЫБОР", [
                                    ("1", "Вызвать полицию"),
                                    ("2", "Искать самому")
                                ])
                                vyybor = input("👉 Ваш выбор: ")
                                if vyybor == "1":
                                    print("🎉 Полиция нашла преступника! Дело раскрыто!")
                                elif vyybor == "2":
                                    print("💔 Вы не нашли преступника... Дело закрыто.")
                            elif vybor == "2":
                                print("💔 Вы бросили дело...")
                    
                    elif loaded_game.get('genre_type') == "Earth":
                        print(f"🧙 Воин: {loaded_game['hero_name']}")
                        print(f"🗡 Оружие: {loaded_game['weapons']}")
                        print(f"📖 История: {loaded_game['history']}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            print_menu("🎮 ТЕСТ (ЗАГРУЖЕННАЯ ИГРА — EARTH)", [])
                            print(f"📜 Краткое описание: Вы — {loaded_game['hero_name']}, ваша история: {loaded_game['history']}. Вас призвали на войну с инопланетным разумом.")
                            vybor = input("1 - пойти биться, 2 - лежать и отдыхать.\n👉 Ваш выбор: ")
                            if vybor == "1":
                                print("⚔️ Вы прибыли в зону боевых действий, инопланетянин бежит на вас, что будете делать?")
                                vyybor = input("1 - Атаковать с помощью оружия, 2 - отпрыгнуть в сторону.\n👉 Ваш выбор: ")
                                if vyybor == "1":
                                    print("Вы не успели достать оружие, вас убили, вы проиграли...")
                                elif vyybor == "2":
                                    print("Вы спаслись от гибели. Инопланетян остаётся немного. Есть план:")
                                    vyyybor = input("1 - попросить их вежливо уйти, 2 - продолжить борьбу:\n👉 Ваш выбор: ")
                                    if vyyybor == "1":
                                        print("Вы смогли договориться! Инопланетяне улетели с Земли, ПОБЕДА!")
                                    elif vyyybor == "2":
                                        print("Борьба понесла много потерь, вас ранили, но вы всё равно ПОБЕДИЛИ!")
                                    else:
                                        print("❓ Непонятный выбор.")
                                else:
                                    print("❓ Непонятный выбор.")
                            elif vybor == "2":
                                print("▶️ К сожалению инопланетяне истребили всё человечество... Вы проиграли.")
                            else:
                                print("❓ Непонятный выбор.")
                    
                    elif loaded_game.get('genre_type') == "Средневековье":
                        print(f"👑 Король: {loaded_game['hero_name']}")
                        print(f"🏰 Королевство: {loaded_game['kor_name']}")
                        print(f"📖 История: {loaded_game['history']}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            print_menu("🎮 ТЕСТ (ЗАГРУЖЕННАЯ ИГРА — СРЕДНЕВЕКОВЬЕ)", [])
                            print(f"📜 Краткое описание: Вы — {loaded_game['hero_name']}, ваша история: {loaded_game['history']}. Вы стали королём королевства {loaded_game['kor_name']}.")
                            print(f"Итак, в вашем королевстве проблема с урожаем, что будете делать?")
                            vybor = input("1 - попросить помощи у другого королевства, 2 - Поддержка населения путём использования гос. резервов.\n👉 Ваш выбор: ")
                            if vybor == "1":
                                print("⚔️ Другое королевство воспользовалось вашей ситуацией и напало на вас, воины были голодными и слабыми, вас захватили. ВЫ ПРОИГРАЛИ...")
                            elif vybor == "2":
                                print("Это хорошо, но еды на всех не хватит, что делать с тем, что у нас неплодородные земли?")
                                vyyybor = input("1 - обменять ресурсы с другим королевством, которых в достатке на еду, 2 - запретить вывоз зерна:\n👉 Ваш выбор: ")
                                if vyyybor == "1":
                                    print("Вы смогли договориться! Теперь еды хватит всем, а также вы улучшили отношения с королевством ПАНГДИОМАС.")
                                elif vyyybor == "2":
                                    print("Вывоз зерна был запрещён, но у нас неплодородные земли, растить негде, из-за голода погибло много людей, расцвело воровство, ВЫ ПРОИГРАЛИ...")
                                else:
                                    print("❓ Непонятный выбор.")
                            else:
                                print("❓ Непонятный выбор.")
                    
                    else:
                        print(f"🧙 Герой: {loaded_game['hero_name']}")
                        print(f"👿 Злодей: {loaded_game['villain_name']}")
                        print(f"⚡ Умение героя: {loaded_game['hero_skill']}")
                        print(f"💀 Умение злодея: {loaded_game['villain_skill']}")
                        print(f"🌍 {loaded_game['location']}")
                        print(f"🎯 {loaded_game['objective']}")
                        
                        test_choice = input("\n🎮 Протестировать? (да/нет): ")
                        if test_choice.lower() in ["да", "yes", "y"]:
                            print_menu("🎮 ТЕСТ (ЗАГРУЖЕННАЯ ИГРА)", [])
                            print(f"Вы — {loaded_game['hero_name']} (умение {loaded_game['hero_skill']}).")
                            print(f"Противник — {loaded_game['villain_name']} (умение {loaded_game['villain_skill']}).")
                            print(f"Локация: {loaded_game['location']}. Цель: {loaded_game['objective']}.")
                            print("\nЧто вы будете делать?")
                            print(f"1. {loaded_game['win_action']}")
                            print(f"2. {loaded_game['lose_action']}")
                            action = input("👉 Ваш выбор: ")
                            if action == "1":
                                print("✨ Победа!")
                            elif action == "2":
                                print("💔 Поражение...")
                            else:
                                print("❓ Непонятный выбор.")
                else:
                    print("❌ Неверный номер игры")
            except ValueError:
                print("❌ Пожалуйста, введите число")
        input("\nНажмите Enter для продолжения...")
    
    elif game == "4":
        games = show_saved_games()
        if games:
            print_menu("🗑️ УДАЛЕНИЕ ИГР", [
                ("0", "Отмена")
            ])
            try:
                choice = input("👉 Введите номер игры для удаления: ")
                if choice == "0":
                    continue
                
                choice = int(choice)
                if 1 <= choice <= len(games):
                    confirm = input(f"Удалить игру '{games[choice-1]['name']}'? (да/нет): ")
                    if confirm.lower() in ["да", "yes", "y"]:
                        delete_saved_game(choice)
                    else:
                        print("❌ Удаление отменено.")
                else:
                    print("❌ Неверный номер игры")
            except ValueError:
                print("❌ Пожалуйста, введите число")
        input("\nНажмите Enter для продолжения...")
    
    elif game == "5":
        games = show_saved_games()
        if games:
            try:
                choice = input("👉 Введите номер игры для редактирования (0 — отмена): ")
                if choice == "0":
                    continue
                choice = int(choice)
                if 1 <= choice <= len(games):
                    edit_game(choice - 1)
                else:
                    print("❌ Неверный номер игры")
            except ValueError:
                print("❌ Пожалуйста, введите число")
    
    elif game in ["0", "exit", "выход"]:
        print("👋 Спасибо за использование FANTOM Redaction! До свидания!")
        break
    
    else:
        print("❌ Неверный ввод. Пожалуйста, введите 1, 2, 3, 4, 5 или 0 для выхода.\n")