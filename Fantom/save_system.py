import json
import os
from ui import print_menu

SAVE_FILE = "saved_games.json"

def input_int(prompt, default=0):
    while True:
        value = input(prompt)
        if value == "":
            return default
        if value.lstrip('-').isdigit():
            return int(value)
        print("❌ Введите число")

def input_bool(prompt):
    while True:
        value = input(prompt).lower()
        if value in ["да", "yes", "y", "1"]:
            return True
        if value in ["нет", "no", "n", "0"]:
            return False
        print("❌ Введите да/нет")

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
    
    genre_names = {
        "rpg": "🎮 RPG",
        "horror": "👻 Хоррор",
        "detective": "🕵️ Детектив",
        "Earth": "🌍 Earth",
        "Средневековье": "🏰 Средневековье",
        "hero_villain": "⚔️ Герой/Злодей",
        "friends": "👥 Друзья",
        "action": "💥 Экшен",
        "survival": "🏕️ Выживание"
    }
    
    for i, game in enumerate(games, 1):
        name = game['name'][:20] + "..." if len(game['name']) > 20 else game['name']
        genre_display = genre_names.get(game.get('genre_type'), f"[{game['platform']}]")
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
        platforms = {"1": "Мобайл", "2": "ПК", "3": "Гибрид"}
        if new_platform in platforms:
            game['platform'] = platforms[new_platform]
            print(f"✅ Платформа изменена на {platforms[new_platform]}")
        else:
            print("❌ Неверный выбор")
    
    elif choice == "3":
        new_age = input(f"Новый возраст (было: {game.get('age', 'Не указан')}): ")
        if new_age:
            game['age'] = new_age
            print(f"✅ Возраст изменён на '{new_age}'")
    
    elif choice == "4":
        new_id = input(f"Новый ID (было: {game.get('id', 'Не указан')}): ")
        if new_id and len(new_id) >= 7:
            game['id'] = new_id
            print(f"✅ ID изменён на '{new_id}'")
        elif new_id:
            print("❌ ID должен быть не менее 7 символов")
    
    elif choice == "5":
        for key in list(game.keys()):
            if key not in ['name', 'platform', 'age', 'id', 'genre_type']:
                current = game[key]
                if isinstance(current, bool):
                    status = "да" if current else "нет"
                    new_value = input(f"{key} (да/нет, сейчас: {status}): ")
                    if new_value:
                        game[key] = new_value.lower() in ["да", "yes", "y", "1"]
                        print(f"✅ {key} изменён")
                elif isinstance(current, int):
                    new_value = input(f"{key} (сейчас: {current}): ")
                    if new_value:
                        if new_value.lstrip('-').isdigit():
                            game[key] = int(new_value)
                            print(f"✅ {key} изменён")
                        else:
                            print(f"❌ {key}: введите число")
                else:
                    new_value = input(f"{key} (сейчас: {current}): ")
                    if new_value:
                        game[key] = new_value
                        print(f"✅ {key} изменён")
        
        print("✅ Сюжет обновлён!")
    
    if choice != "0":
        games[index] = game
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(games, f, ensure_ascii=False, indent=2)
        print("✅ Изменения сохранены!")
    
    input("\nНажмите Enter для продолжения...")