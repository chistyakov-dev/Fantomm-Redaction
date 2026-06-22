from ui import print_menu

class EarthGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "Earth"
    
    def create(self):
        print("\n=== ШАБЛОН: EARTH ===")
        self.hero_name = input("🧙 Имя вашего воина: (0 - отмена) ")
        if self.hero_name == "0":
            return None
        self.weapons = input("🗡 Его оружие: ")
        self.history = input("📖 Краткая история героя: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Вы — {self.hero_name}. На вашу планету напал инопланетный разум. ")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "hero_name": self.hero_name,
            "weapons": self.weapons,
            "history": self.history,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
        print(f"Вы — {self.hero_name}. На вашу планету напал инопланетный разум: ")
        vybor = input("1 - пойти биться, 2 - лежать и отдыхать: ")
        
        if vybor == "1":
            print("⚔️ Вы в зоне боевых действий, инопланетянин бежит на вас!")
            vyybor = input("1 - атаковать, 2 - отпрыгнуть: ")
            if vyybor == "1":
                print("Вы не успели достать оружие, вас убили...")
            elif vyybor == "2":
                print("Вы спаслись. Инопланетян остаётся немного.")
                vyyybor = input("1 - попросить их уйти, 2 - продолжить борьбу: ")
                if vyyybor == "1":
                    print("Инопланетяне улетели! ПОБЕДА!")
                elif vyyybor == "2":
                    print("Вы победили, но были ранены!")
        elif vybor == "2":
            print("▶️ Инопланетяне истребили человечество... Вы проиграли.")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()