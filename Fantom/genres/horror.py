
from ui import print_menu

class HorrorGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "horror"
    
    def create(self):
        print("\n=== ШАБЛОН: ХОРРОР ===")
        self.hero_name = input("🧙 Имя героя: ")
        print("\n--- Параметры ужаса ---")
        self.fear_level = int(input("😱 Начальный уровень страха (0-100): ") or 30)
        self.batteries = int(input("🔋 Количество батареек: ") or 3)
        self.monster = input("👾 Тип монстра: ")
        self.location = input("🏚️ Локация: ")
        self.objective = input("🎯 Цель: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Вы — {self.hero_name} в {self.location}.")
        print(f"Вас преследует {self.monster}. Цель: {self.objective}.")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "hero_name": self.hero_name,
            "fear_level": self.fear_level,
            "batteries": self.batteries,
            "monster": self.monster,
            "location": self.location,
            "objective": self.objective,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        fear = self.fear_level
        bat = self.batteries
        
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
        print(f"Вы — {self.hero_name}. Локация: {self.location}. Монстр: {self.monster}.")
        print("Вы слышите шорох...")
        print_menu("ВЫБОР", [
            ("1", "проверить"),
            ("2", "спрятаться")
        ])
        
        action = input("👉 Ваш выбор: ")
        if action == "1":
            fear += 20
            bat -= 1
            print("😨 Вы увидели монстра!")
        elif action == "2":
            fear += 5
            print("😰 Вы затаились.")
        
        if fear >= 100:
            print("💔 Вы обезумели от страха...")
        elif bat <= 0:
            print("🔋 Батарейки кончились. Монстр настиг вас...")
        else:
            print(f"✅ Вы выжили! Страх: {fear}, батареек: {bat}")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()