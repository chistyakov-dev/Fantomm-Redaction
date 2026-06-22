from ui import print_menu

class ActionGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "action"
    
    def create(self):
        print("\n=== ШАБЛОН: ЭКШЕН ===")
        self.hero_name = input("🧙 Имя героя: (0 - отмена) ")
        if self.hero_name == "0":
            return None
        self.hero_weapon = input("🔫 Оружие героя: ")
        self.enemy_count = input("👥 Количество врагов: ")
        self.boss_name = input("👾 Имя босса: ")
        self.boss_ability = input("💥 Способность босса: ")
        self.location = input("🏞️ Локация: ")
        self.objective = input("🎯 Цель миссии: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Вы — {self.hero_name} с оружием {self.hero_weapon}.")
        print(f"Вам предстоит сразиться с {self.enemy_count} врагами и боссом {self.boss_name}.")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "hero_name": self.hero_name,
            "hero_weapon": self.hero_weapon,
            "enemy_count": self.enemy_count,
            "boss_name": self.boss_name,
            "boss_ability": self.boss_ability,
            "location": self.location,
            "objective": self.objective,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
        print(f"Вы — {self.hero_name}, вооруженный {self.hero_weapon}.")
        print(f"На вас нападают {self.enemy_count} врагов, появляется босс {self.boss_name}!")
        print(f"Локация: {self.location}. Цель: {self.objective}.")
        print("Что вы будете делать?")
        print("1 - Начнёте битву")
        print("2 - Убежите")
        
        action = input("👉 Ваш выбор: ")
        if action == "1":
            print("✨ Погнали! В начале нужно разобраться с помощниками босса.")
            vybor = input("выберите: 1 - использовать ваш личный приём или 2 - просто биться: ")
            
            if vybor == "1":
                print("Прекрасно, все вырублены, но с боссом такое не получится.")
                vyybor = input(f"Выбор: 1 - использовать {self.hero_weapon} против босса или 2 - драться без него: ")
                
                if vyybor == "1":
                    print("✨ Победа! Босс был повержен.")
                elif vyybor == "2":
                    print("💔 В обычном бою босс оказался сильнее, вы проиграли...")
                else:
                    print("❓ Непонятный выбор.")
            elif vybor == "2":
                print("💔 Вас быстро одолели, вы проиграли...")
            else:
                print("❓ Непонятный выбор.")
                
        elif action == "2":
            print("Толпа была слишком огромна, вы проиграли...")
        else:
            print("❓ Непонятный выбор.")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()