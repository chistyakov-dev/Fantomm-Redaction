from ui import print_menu

class HeroVillainGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "hero_villain"
    
    def create(self):
        print("\n=== ШАБЛОН: ГЕРОЙ И ЗЛОДЕЙ ===")
        self.hero_name = input("🧙 Имя вашего главного героя: ")
        self.villain_name = input("👿 Имя главного злодея: ")
        self.hero_skill = input("⚡ Умение героя: ")
        self.villain_skill = input("💀 Умение злодея: ")
        self.location = input("🏞️ Где происходит действие: ")
        self.objective = input("🎯 Что должен сделать герой: ")
        self.win_action = input("✅ Действие для победы: ")
        self.lose_action = input("❌ Действие для поражения: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Вы — {self.hero_name}, обладающий умением {self.hero_skill}.")
        print(f"Действие происходит в {self.location}. Вам нужно {self.objective}.")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "hero_name": self.hero_name,
            "villain_name": self.villain_name,
            "hero_skill": self.hero_skill,
            "villain_skill": self.villain_skill,
            "location": self.location,
            "objective": self.objective,
            "win_action": self.win_action,
            "lose_action": self.lose_action,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
        print(f"Вы — {self.hero_name}. Ваше умение: {self.hero_skill}.")
        print(f"Вы находитесь в {self.location}. Вам нужно {self.objective}.")
        print("Что вы будете делать?")
        print(f"1. {self.win_action}")
        print(f"2. {self.lose_action}")
        
        action = input("👉 Ваш выбор (1 или 2): ")
        if action == "1":
            print("✨ Победа! Вы успешно справились с задачей.")
        elif action == "2":
            print("💔 Поражение... Вы проиграли.")
        else:
            print("❓ Непонятный выбор.")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()