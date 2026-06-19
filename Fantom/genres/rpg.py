from ui import print_menu

class RPGGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "rpg"
    
    def create(self):
        print("\n=== RPG ===")
        self.hero_name = input("🧙 Имя героя: ")
        self.hero_class = input("🏹 Класс (воин, маг, лучник): ")
        self.starting_gold = input("💰 Начальное золото: ")
        self.quest = input("📜 Главный квест: ")
        self.companion = input("👥 Имя спутника: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Вы — {self.hero_name}, класс {self.hero_class}.")
        print(f"Ваш спутник — {self.companion}. Главный квест: {self.quest}.")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "hero_name": self.hero_name,
            "hero_class": self.hero_class,
            "starting_gold": self.starting_gold,
            "quest": self.quest,
            "companion": self.companion,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
        print(f"Вы — {self.hero_name}, класс {self.hero_class}. У вас {self.starting_gold} золота.")
        print(f"Ваш спутник: {self.companion}. Главный квест: {self.quest}.")
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
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()