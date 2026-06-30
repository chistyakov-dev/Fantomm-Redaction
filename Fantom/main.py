import os
import time
from ui import print_menu, show_start_screen
from save_system import load_saved_games, save_game
from notes import notes_menu, load_notes

from genres.hero_villain import HeroVillainGenre
from genres.friends import FriendsGenre
from genres.action import ActionGenre
from genres.survival import SurvivalGenre
from genres.rpg import RPGGenre
from genres.horror import HorrorGenre
from genres.detective import DetectiveGenre
from genres.earth import EarthGenre
from genres.medieval import MedievalGenre
from gitfan import GitFan, show_gitfan_boot
from ui import print_menu, show_start_screen

def after_create(game_obj, game_data):
    save_choice = input("\n💾 Сохранить игру? (да/нет): ")
    if save_choice.lower() in ["да", "yes", "y"]:
        save_game(game_data)
    
    test_choice = input("🎮 Протестировать? (да/нет): ")
    if test_choice.lower() in ["да", "yes", "y"]:
        game_obj.test()

show_start_screen()

gitfan = GitFan()

while True:
    print_menu("🎮 МЕНЮ ИГРЫ", [
        ("1", "Создать игру"),
        ("2", "Настройки"),
        ("3", "Загрузить игру"),
        ("4", "Управление сохранениями"),
        ("5", "Редактировать игру"),
        ("6", "Заметки"),
        ("7", "GitFan"),
        ("0", "Выход")
    ])
    game = input("👉 Ваш выбор: ")
    
    if game == "1":
        game_name = input("📝 Введите название для вашей игры (0 — отмена): ")
        if game_name == "0":
            continue
        print(f"✓ Название игры: {game_name}\n")
        
        cancelled = False
        while True:
            game_version = input("📱 Выберите платформу:\n1 — Мобайл\n2 — ПК\n3 — Гибрид\n0 — Отмена\n👉 Ваш выбор: ")
            if game_version == "0":
                cancelled = True
                break
            
            wozrast_name = input("Напишите возрастное ограничение (0 — отмена): ")
            if wozrast_name == "0":
                cancelled = True
                break
            
            ID_name = input("Создайте уникальный ID, не менее 7 символов (0 — отмена):\n")
            if ID_name == "0":
                cancelled = True
                break
            
            platform = ""
            if game_version == "1":
                platform = "Мобайл"
                break
            elif game_version == "2":
                platform = "ПК"
                break
            elif game_version == "3":
                platform = "Гибрид"
                break
            else:
                print("❌ Неверный выбор. Введите 1, 2 или 3.\n")
        
        if cancelled:
            print("❌ Создание отменено.\n")
            continue
        
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
        
        genre_classes = {
            "1": HeroVillainGenre,
            "2": FriendsGenre,
            "3": ActionGenre,
            "4": SurvivalGenre,
            "5": RPGGenre,
            "6": HorrorGenre,
            "7": DetectiveGenre,
            "8": EarthGenre,
            "9": MedievalGenre
        }
        
        if genre in genre_classes:
            game_obj = genre_classes[genre](game_name, platform, wozrast_name, ID_name)
            game_data = game_obj.create()
            if game_data is None:
                print("❌ Создание отменено.\n")
                continue
            after_create(game_obj, game_data)
        else:
            print("❌ Неверный выбор жанра.")
        
        continue_choice = input("\n🔄 Хотите создать еще одну игру? (да/нет): ")
        if continue_choice.lower() not in ["да", "yes", "y"]:
            print("👋 Спасибо за использование! До свидания!")
            break
    
    elif game == "2":
     while True:
        print_menu("⚙️ НАСТРОЙКИ", [
            ("о", "О нас"),
            ("т", "Тема оформления"),
            ("5", "Вернуться назад")
        ])
        settings = input("👉 Ваш выбор: ")
              
        if settings.lower() == "о":
            print_menu("ℹ️ О НАС", [
                ("FANTOM Redaction", ""),
                ("от Cheymi Platforms", ""),
                ("📅 Версия:", "V4.0"),
                ("Telegram-канал:", "https://t.me/CheymiPlatforms"),
                ("👥 Разработчик:", "Егор Чистяков aka chistdev")
            ])
            input("\nНажмите Enter для продолжения...")
        
        elif settings.lower() == "т":
            from ui import themes_menu
            themes_menu()
        
        elif settings.lower() == "x" or settings == "5":
            break
    
    elif game == "3":
        from save_system import show_saved_games
        
        games = show_saved_games()
        if games:
            try:
                choice = input("👉 Введите номер игры (0 — отмена): ")
                if choice == "0":
                    continue
                
                choice = int(choice)
                if 1 <= choice <= len(games):
                    loaded_game = games[choice - 1]
                    
                    print_menu(f"✅ {loaded_game['name']}", [])
                    print(f"📱 Платформа: {loaded_game['platform']}")
                    
                    genre_map = {
                        "hero_villain": HeroVillainGenre,
                        "friends": FriendsGenre,
                        "action": ActionGenre,
                        "survival": SurvivalGenre,
                        "rpg": RPGGenre,
                        "horror": HorrorGenre,
                        "detective": DetectiveGenre,
                        "Earth": EarthGenre,
                        "Средневековье": MedievalGenre
                    }
                    
                    if loaded_game['genre_type'] in genre_map:
                        game_obj = genre_map[loaded_game['genre_type']]("", "", "", "")
                        game_obj.load_and_test(loaded_game)
            except ValueError:
                print("❌ Пожалуйста, введите число")
        input("\nНажмите Enter для продолжения...")
    
    elif game == "4":
        from save_system import show_saved_games, delete_saved_game
        
        games = show_saved_games()
        if games:
            try:
                choice = input("👉 Введите номер игры для удаления (0 — отмена): ")
                if choice == "0":
                    continue
                
                choice = int(choice)
                if 1 <= choice <= len(games):
                    confirm = input(f"Удалить игру '{games[choice-1]['name']}'? (да/нет): ")
                    if confirm.lower() in ["да", "yes", "y"]:
                        delete_saved_game(choice)
                    else:
                        print("❌ Удаление отменено.")
            except ValueError:
                print("❌ Пожалуйста, введите число")
        input("\nНажмите Enter для продолжения...")
    
    elif game == "5":
        from save_system import show_saved_games, edit_game
        
        games = show_saved_games()
        if games:
            try:
                choice = input("👉 Введите номер игры для редактирования (0 — отмена): ")
                if choice == "0":
                    continue
                choice = int(choice)
                if 1 <= choice <= len(games):
                    edit_game(choice - 1)
            except ValueError:
                print("❌ Пожалуйста, введите число")
    
    elif game == "6":
        notes_menu()
    
    elif game == "7":
        show_gitfan_boot()
        games = load_saved_games()
        notes = load_notes()
        
        while True:
            user_input = input("   💬 Вы: ")
            if user_input.strip() == "":
                continue
            
            result = gitfan.process(user_input, games, notes)
            
            if result == "menu":
                break
    
    elif game in ["0", "exit", "выход"]:
        print("👋 Спасибо за использование! До свидания!")
        break
    
    else:
        print("❌ Неверный ввод.\n")