import shutil
import time
import json
import os

SETTINGS_FILE = "settings.json"

THEMES = {
    "dark": {
        "name": "Тёмная",
        "border": "╔╗╚╝╠╣║═",
        "reset": "\033[0m",
        "border_color": "\033[90m",
        "title_color": "\033[97m",
        "text_color": "\033[37m",
        "accent_color": "\033[96m"
    },
    "light": {
        "name": "Светлая",
        "border": "╔╗╚╝╠╣║═",
        "reset": "\033[0m",
        "border_color": "\033[37m",
        "title_color": "\033[30m",
        "text_color": "\033[90m",
        "accent_color": "\033[34m"
    },
    "cyberpunk": {
        "name": "Киберпанк",
        "border": "╔╗╚╝╠╣║═",
        "reset": "\033[0m",
        "border_color": "\033[32m",
        "title_color": "\033[92m",
        "text_color": "\033[32m",
        "accent_color": "\033[93m"
    },
    "retro": {
        "name": "Ретро",
        "border": "╔╗╚╝╠╣║═",
        "reset": "\033[0m",
        "border_color": "\033[33m",
        "title_color": "\033[93m",
        "text_color": "\033[33m",
        "accent_color": "\033[37m"
    }
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {"theme": "dark"}
    return {"theme": "dark"}

def save_settings(settings):
    with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
        json.dump(settings, f, ensure_ascii=False, indent=2)

def get_theme():
    settings = load_settings()
    theme_name = settings.get("theme", "dark")
    return THEMES.get(theme_name, THEMES["dark"])

def apply_theme(theme_name):
    if theme_name in THEMES:
        settings = load_settings()
        settings["theme"] = theme_name
        save_settings(settings)
        return True
    return False

def c(text, color_code):
    return f"{color_code}{text}\033[0m"

def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except:
        return 80

def print_menu(title, options, width=None):
    theme = get_theme()
    
    if width is None:
        width = get_terminal_width()
        width = min(width, 60)
        width = max(width, 40)
    
    tc = theme["border_color"]
    tr = theme["reset"]
    
    print(tc + "╔" + "═" * (width - 2) + "╗" + tr)
    
    title_padding = width - len(title) - 4
    left_pad = title_padding // 2
    right_pad = title_padding - left_pad
    print(tc + "║" + tr + " " * left_pad + theme["title_color"] + title + tr + " " * right_pad + tc + "║" + tr)
    
    print(tc + "╠" + "═" * (width - 2) + "╣" + tr)
    
    for option in options:
        option_text = f"{option[0]} {option[1]}"
        if len(option_text) > width - 4:
            option_text = option_text[:width - 7] + "..."
        spaces = width - len(option_text) - 4
        print(tc + "║" + tr + " " + theme["text_color"] + option_text + tr + " " * spaces + tc + "║" + tr)
    
    print(tc + "╚" + "═" * (width - 2) + "╝" + tr)

def show_start_screen():
    theme = get_theme()
    width = get_terminal_width()
    width = min(width, 70)
    width = max(width, 50)
    
    tc = theme["border_color"]
    tr = theme["reset"]
    ta = theme["accent_color"]
    tt = theme["title_color"]
    tx = theme["text_color"]
    
    print(tc + "╔" + "═" * (width - 2) + "╗" + tr)
    print(tc + "║" + tr + " " * (width - 2) + tc + "║" + tr)
    
    title = "⚡ FANTOM REDACTION ⚡"
    title_padding = width - len(title) - 2
    left_pad = title_padding // 2
    right_pad = title_padding - left_pad
    print(tc + "║" + tr + " " * left_pad + tt + title + tr + " " * right_pad + tc + "║" + tr)
    
    print(tc + "║" + tr + " " * (width - 2) + tc + "║" + tr)
    
    subtitle = "Многофункциональный текстовый движок для создания игр"
    if len(subtitle) > width - 4:
        subtitle = subtitle[:width - 7] + "..."
    sub_padding = width - len(subtitle) - 2
    left_sub = sub_padding // 2
    right_sub = sub_padding - left_sub
    print(tc + "║" + tr + " " * left_sub + tx + subtitle + tr + " " * right_sub + tc + "║" + tr)
    
    print(tc + "║" + tr + " " * (width - 2) + tc + "║" + tr)
    
    author = "by Cheymi Platforms"
    auth_padding = width - len(author) - 2
    left_auth = auth_padding // 2
    right_auth = auth_padding - left_auth
    print(tc + "║" + tr + " " * left_auth + ta + author + tr + " " * right_auth + tc + "║" + tr)
    
    print(tc + "║" + tr + " " * (width - 2) + tc + "║" + tr)
    print(tc + "╚" + "═" * (width - 2) + "╝" + tr)
    print()
    
    print(ta + "🔄 Загрузка" + tr, end="")
    for i in range(3):
        time.sleep(0.2)
        print(ta + "." + tr, end="")
    print(ta + " Готово!" + tr + "\n")
    time.sleep(0.5)

def themes_menu():
    theme = get_theme()
    
    while True:
        print_menu("🎨 ТЕМЫ ОФОРМЛЕНИЯ", [
            ("1", f"Тёмная {'✅' if theme['name'] == 'Тёмная' else ''}"),
            ("2", f"Светлая {'✅' if theme['name'] == 'Светлая' else ''}"),
            ("3", f"Киберпанк {'✅' if theme['name'] == 'Киберпанк' else ''}"),
            ("4", f"Ретро {'✅' if theme['name'] == 'Ретро' else ''}"),
            ("0", "Назад")
        ])
        
        choice = input("👉 Ваш выбор: ")
        
        theme_map = {
            "1": "dark",
            "2": "light",
            "3": "cyberpunk",
            "4": "retro"
        }
        
        if choice in theme_map:
            apply_theme(theme_map[choice])
            theme = get_theme()
            print(f"✅ Тема '{THEMES[theme_map[choice]]['name']}' применена!")
            input("\nНажмите Enter...")
        elif choice == "0":
            break
        else:
            print("❌ Неверный выбор")