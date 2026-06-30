import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_notes(notes):
    with open(NOTES_FILE, 'w', encoding='utf-8') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

def create_note():
    notes = load_notes()
    
    title = input("📝 Заголовок заметки: ")
    if not title:
        print("❌ Заголовок не может быть пустым")
        return
    
    print("📄 Содержимое (введите пустую строку для завершения):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    content = "\n".join(lines)
    
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "created_at": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "updated_at": datetime.now().strftime("%d.%m.%Y %H:%M")
    }
    
    notes.append(note)
    save_notes(notes)
    print(f"✅ Заметка '{title}' сохранена!")

def show_notes():
    notes = load_notes()
    if not notes:
        print("📭 Нет заметок")
        return None
    
    print("\n┌" + "─" * 40 + "┐")
    print("│" + " 📋 ВАШИ ЗАМЕТКИ".ljust(43) + "│")
    print("├" + "─" * 40 + "┤")
    
    for note in notes:
        title = note['title'][:25] + "…" if len(note['title']) > 25 else note['title']
        print(f"│ {note['id']}. {title}".ljust(42) + "│")
        print(f"│    {note['created_at']}".ljust(42) + "│")
    
    print("└" + "─" * 40 + "┘")
    return notes

def read_note():
    notes = show_notes()
    if not notes:
        return
    
    try:
        note_id = int(input("\n📖 Номер заметки для чтения (0 — отмена): "))
        if note_id == 0:
            return
        
        note = next((n for n in notes if n['id'] == note_id), None)
        if note:
            print(f"\n┌" + "─" * 50 + "┐")
            print(f"│ 📝 {note['title']}".ljust(53) + "│")
            print(f"│ 📅 {note['created_at']}".ljust(53) + "│")
            print(f"│ 🔄 {note['updated_at']}".ljust(53) + "│")
            print("├" + "─" * 50 + "┤")
            for line in note['content'].split('\n'):
                wrapped = line[:46] + "…" if len(line) > 46 else line
                print(f"│ {wrapped}".ljust(52) + "│")
            print("└" + "─" * 50 + "┘")
        else:
            print("❌ Заметка не найдена")
    except ValueError:
        print("❌ Введите число")

def edit_note():
    notes = show_notes()
    if not notes:
        return
    
    try:
        note_id = int(input("\n✏️ Номер заметки для редактирования (0 — отмена): "))
        if note_id == 0:
            return
        
        note = next((n for n in notes if n['id'] == note_id), None)
        if note:
            print(f"\n✏️ Редактирование: {note['title']}")
            
            new_title = input(f"Заголовок (было: {note['title']}): ")
            if new_title:
                note['title'] = new_title
            
            print("Содержимое (Enter — оставить как есть, пустая строка — закончить):")
            print(f"Было:\n{note['content']}\n")
            print("Новое содержимое:")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            if lines:
                note['content'] = "\n".join(lines)
            
            note['updated_at'] = datetime.now().strftime("%d.%m.%Y %H:%M")
            
            for i, n in enumerate(notes):
                if n['id'] == note_id:
                    notes[i] = note
                    break
            
            save_notes(notes)
            print(f"✅ Заметка '{note['title']}' обновлена!")
        else:
            print("❌ Заметка не найдена")
    except ValueError:
        print("❌ Введите число")

def delete_note():
    notes = show_notes()
    if not notes:
        return
    
    try:
        note_id = int(input("\n🗑️ Номер заметки для удаления (0 — отмена): "))
        if note_id == 0:
            return
        
        note = next((n for n in notes if n['id'] == note_id), None)
        if note:
            confirm = input(f"Удалить заметку '{note['title']}'? (да/нет): ")
            if confirm.lower() in ["да", "yes", "y"]:
                notes = [n for n in notes if n['id'] != note_id]
                for i, n in enumerate(notes):
                    n['id'] = i + 1
                save_notes(notes)
                print(f"✅ Заметка '{note['title']}' удалена!")
            else:
                print("❌ Удаление отменено")
        else:
            print("❌ Заметка не найдена")
    except ValueError:
        print("❌ Введите число")

def notes_menu():
    while True:
        print("\n┌" + "─" * 30 + "┐")
        print("│" + " 📒 ЗАМЕТКИ".ljust(33) + "│")
        print("├" + "─" * 30 + "┤")
        print("│ 1. Создать заметку".ljust(32) + "│")
        print("│ 2. Все заметки".ljust(32) + "│")
        print("│ 3. Прочитать заметку".ljust(32) + "│")
        print("│ 4. Редактировать".ljust(32) + "│")
        print("│ 5. Удалить заметку".ljust(32) + "│")
        print("│ 0. Назад".ljust(32) + "│")
        print("└" + "─" * 30 + "┘")
        
        choice = input("👉 Ваш выбор: ")
        
        if choice == "1":
            create_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            read_note()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "0":
            break
        else:
            print("❌ Неверный выбор")
        
        if choice in ["1", "2", "3", "4", "5"]:
            input("\nНажмите Enter...")