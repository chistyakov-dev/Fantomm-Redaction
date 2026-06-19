import random
from ui import print_menu

class SurvivalGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "survival"
    
    def create(self):
        print("\n=== ВЫЖИВАНИЕ ===")
        self.hero_name = input("🧙 Имя героя: ")
        print("\n--- Начальные ресурсы ---")
        self.food = int(input("🍗 Еда (число): ") or 10)
        self.water = int(input("💧 Вода (число): ") or 10)
        self.medkits = int(input("💊 Аптечки (число): ") or 3)
        self.danger = input("👾 Основная опасность: ")
        self.days_goal = int(input("⏳ Сколько дней нужно продержаться: ") or 7)
        
        print("\n--- Дополнительные условия ---")
        self.has_fire = input("🔥 Есть доступ к огню? (да/нет): ").lower() in ["да", "yes", "y"]
        self.shelter_level = input("🏕️ Уровень убежища (1-3): ")
        while self.shelter_level not in ["1", "2", "3"]:
            self.shelter_level = input("Пожалуйста, введите 1, 2 или 3: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Вы — {self.hero_name} в суровых условиях.")
        print(f"Вам угрожает {self.danger}. Нужно продержаться {self.days_goal} дней.")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "hero_name": self.hero_name,
            "food": self.food,
            "water": self.water,
            "medkits": self.medkits,
            "danger": self.danger,
            "days_goal": self.days_goal,
            "has_fire": self.has_fire,
            "shelter_level": self.shelter_level,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        food = self.food
        water = self.water
        medkits = self.medkits
        day = 1
        alive = True
        
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ: ВЫЖИВАНИЕ", [])
        print(f"Вы — {self.hero_name}. Цель: продержаться {self.days_goal} дней.")

        while day <= self.days_goal and alive:
            print(f"\n╔════════════════════════════════════╗")
            print(f"║ ДЕНЬ {day}                             ║")
            print(f"║ 🍗 Еда: {food} | 💧 Вода: {water} | 💊 Аптечки: {medkits} ║")
            
            water_cost = 2 if self.has_fire else 3
            food_cost = 2
            
            event = random.choice(["nothing", "find_food", "find_water", "injury", "thief"])
            
            if event == "find_food":
                found = random.randint(1, 5)
                food += found
                print(f"🍀 Вы нашли еду! +{found}")
            elif event == "find_water":
                found = random.randint(1, 4)
                water += found
                print(f"💧 Вы нашли воду! +{found}")
            elif event == "injury":
                print("🤕 Травма! Использовать аптечку?")
                use = input("1 - да, 2 - нет: ")
                if use == "1" and medkits > 0:
                    medkits -= 1
                else:
                    food -= 1
                    water -= 1
            elif event == "thief":
                food = max(0, food - random.randint(1, 3))
                water = max(0, water - random.randint(1, 2))
                print("👤 Воры украли часть припасов!")
            
            food -= food_cost
            water -= water_cost
            
            if food <= 0 or water <= 0:
                print("\n💀 Вы погибли от истощения...")
                alive = False
                break
            
            day += 1
        
        if alive and day > self.days_goal:
            print(f"\n✨ ПОБЕДА! Вы продержались {self.days_goal} дней!")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()