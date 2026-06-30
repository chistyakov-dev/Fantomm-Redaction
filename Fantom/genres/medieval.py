from ui import print_menu

class MedievalGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "Средневековье"
    
    def create(self):
        print("\n=== ШАБЛОН: СРЕДНЕВЕКОВЬЕ ===")
        self.hero_name = input("👑 Имя вашего короля: (0 - отмена) ")
        if self.hero_name == "0":
            return None
        self.kor_name = input("🏰 Название королевства: ")
        self.history = input("📖 Краткая история вашего короля: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Вы — король {self.hero_name} королевства {self.kor_name}.")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "hero_name": self.hero_name,
            "kor_name": self.kor_name,
            "history": self.history,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
        print(f"Вы — король {self.hero_name} королевства {self.kor_name}.")
        print("В королевстве проблема с урожаем, что будете делать?")
        vybor = input("1 - попросить помощи у соседнего королевства, 2 - использовать гос. резервы: ")
        
        if vybor == "1":
            print("⚔️ Соседнее королевство напало на вас и захватило!")
        elif vybor == "2":
            print("Еды хватило не всем. Что делать с неплодородными землями?")
            vyyybor = input("1 - обменять ресурсы, 2 - запретить вывоз зерна: ")
            if vyyybor == "1":
                print("Вы договорились! Еды хватило всем!")
            elif vyyybor == "2":
                print("Начался голод, вы проиграли...")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()