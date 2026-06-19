import json
import os
from ui import print_menu

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
        genre_display = {
            "rpg": "🎮 RPG",
            "horror": "👻 Хоррор",
            "detective": "🕵️ Детектив",
            "Earth": "🌍 Earth",
            "Средневековье": "🏰 Средневековье"
        }.get(game.get('genre_type'), f"[{game['platform']}]")
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
    
    elif choice == "2":
        print("1 — Мобайл\n2 — ПК\n3 — Гибрид")
        new_platform = input("Новая платформа: ")
        platforms = {"1": "Мобайл", "2": "ПК", "3": "Гибрид"}
        if new_platform in platforms:
            game['platform'] = platforms[new_platform]
    
    elif choice == "3":
        new_age = input(f"Новый возраст (было: {game.get('age', 'Не указан')}): ")
        if new_age:
            game['age'] = new_age
    
    elif choice == "4":
        new_id = input(f"Новый ID (было: {game.get('id', 'Не указан')}): ")
        if new_id and len(new_id) >= 7:
            game['id'] = new_id
    
    elif choice == "5":
        for key in list(game.keys()):
            if key not in ['name', 'platform', 'age', 'id', 'genre_type']:
                new_value = input(f"{key} (было: {game[key]}): ")
                if new_value:
                    if isinstance(game[key], int):
                        try:
                            game[key] = int(new_value)
                        except:
                            pass
                    elif isinstance(game[key], bool):
                        game[key] = new_value.lower() in ["да", "yes", "y", "true"]
                    else:
                        game[key] = new_value
    
    if choice != "0":
        games[index] = game
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(games, f, ensure_ascii=False, indent=2)
        print("✅ Изменения сохранены!")
    
    input("\nНажмите Enter для продолжения...")