import shutil
import time

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
    
    title = "⚡ FANTOMM REDACTION ⚡"
    title_padding = width - len(title) - 2
    left_pad = title_padding // 2
    right_pad = title_padding - left_pad
    print("║" + " " * left_pad + title + " " * right_pad + "║")
    
    print("║" + " " * (width - 2) + "║")
    
    subtitle = "Многофункциональный текстовый движок для создания игр"
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
    print("╚" + "═" * (width - 2) + "╝")
    print()
    
    print("🔄 Загрузка", end="")
    for i in range(3):
        time.sleep(0.3)
        print(".", end="")
    print(" Готово!\n")
    time.sleep(1.0)