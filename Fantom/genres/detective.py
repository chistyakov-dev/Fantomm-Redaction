from ui import print_menu
import random

class DetectiveGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "detective"
    
    def create(self):
        print("\n=== ШАБЛОН: ДЕТЕКТИВ ===")
        self.detective_name = input("🕵️‍♂️ Имя вашего детектива: - (0 - отмена) ")
        if self.detective_name == "0":
            return None
        self.location = input("🏞️ Где будет проходить расследование: ")
        self.crime = input("🔍 Какое преступление произошло: ")
        self.suspect_count = input("👥 Сколько подозреваемых: ")
        self.history = input("📖 Краткая история о вашем детективе: ")
        self.clue_1 = input("🔎 Первая ключевая улика: ")
        self.clue_2 = input("🔎 Вторая улика (второстепенная): ")
        self.twist = input("🔄 Неожиданный поворот в деле: ")
        self.victory_text = input("🎉 Финал при раскрытии дела: ")
        self.fail_text = input("💔 Финал при провале: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Детектив {self.detective_name} расследует {self.crime} в {self.location}.")
        print(f"👥 Подозреваемых: {self.suspect_count}")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "detective_name": self.detective_name,
            "location": self.location,
            "crime": self.crime,
            "suspect_count": self.suspect_count,
            "history": self.history,
            "clue_1": self.clue_1,
            "clue_2": self.clue_2,
            "twist": self.twist,
            "victory_text": self.victory_text,
            "fail_text": self.fail_text,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        print_menu("🕵️ ТЕСТ: РАССЛЕДОВАНИЕ", [])
        print(f"🕵️ Детектив: {self.detective_name}")
        print(f"📍 Локация: {self.location}")
        print(f"🔍 Дело: {self.crime}")
        print(f"👥 Подозреваемых: {self.suspect_count}")
        print(f"\n📖 {self.history}")
        
        print(f"\n🕵️ {self.detective_name} прибывает на место преступления.")
        print(f"🔎 При осмотре вы находите: {self.clue_1}")
        
        print_menu("🔍 ПЕРВЫЙ ШАГ", [
            ("1", "Допросить всех подозреваемых"),
            ("2", "Детально изучить первую улику"),
            ("3", "Обыскать место преступления ещё раз")
        ])
        
        step1 = input("👉 Ваш выбор: ")
        
        if step1 == "1":
            print(f"\n👥 Вы допрашиваете {self.suspect_count} подозреваемых.")
            print("Показания путаются. Один из них явно что-то скрывает.")
            print(f"💡 В разговоре всплывает деталь: {self.clue_2}")
        elif step1 == "2":
            print(f"\n🔎 Вы тщательно изучаете: {self.clue_1}")
            print(f"💡 Это приводит к неожиданному открытию: {self.clue_2}")
        elif step1 == "3":
            print(f"\n🔍 При повторном обыске вы замечаете: {self.clue_2}")
            print("Эту деталь вы упустили в первый раз.")
        else:
            print("\n❓ Вы медлите. Время работает против вас.")
        
        print(f"\n📋 Собраны улики: {self.clue_1} и {self.clue_2}")
        print(f"🔄 Неожиданный поворот: {self.twist}")
        
        print_menu("⚖️ РЕШАЮЩИЙ МОМЕНТ", [
            ("1", "Обвинить главного подозреваемого"),
            ("2", "Устроить следственный эксперимент"),
            ("3", "Пойти по новому следу")
        ])
        
        step2 = input("👉 Ваш выбор: ")
        
        if step2 == "1":
            print(f"\n⚖️ Вы выдвигаете обвинение, опираясь на {self.clue_1} и {self.clue_2}.")
            if random.random() > 0.4:
                print(f"🎉 {self.victory_text}")
            else:
                print(f"💔 {self.fail_text}")
        elif step2 == "2":
            print(f"\n🧪 Вы воссоздаёте картину преступления с учётом: {self.twist}")
            if random.random() > 0.3:
                print(f"🎉 Эксперимент удаётся! {self.victory_text}")
            else:
                print(f"💔 Улики рассыпаются. {self.fail_text}")
        elif step2 == "3":
            print(f"\n🔎 Новая зацепка ведёт в неожиданное место.")
            if random.random() > 0.5:
                print(f"🎉 Интуиция не подвела! {self.victory_text}")
            else:
                print(f"💔 След оказался ложным. {self.fail_text}")
        else:
            print(f"\n⏰ Время вышло. {self.fail_text}")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()