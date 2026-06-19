from ui import print_menu

class DetectiveGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "detective"
    
    def create(self):
        print("\n=== ДЕТЕКТИВ ===")
        self.detective_name = input("🕵️‍♂️ Имя детектива: ")
        self.location = input("🏞️ Где будете расследовать: ")
        self.history = input("📖 Краткая история о детективе: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Детектив {self.detective_name} расследует дело в {self.location}.")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "detective_name": self.detective_name,
            "location": self.location,
            "history": self.history,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
        print(f"Вы — детектив {self.detective_name}.")
        print(f"Вы расследуете дело в {self.location} о краже.")
        print_menu("ВЫБОР", [
            ("1", "Спросить у работников"),
            ("2", "Бросить дело")
        ])
        
        vybor = input("👉 Ваш выбор: ")
        if vybor == "1":
            print("Эллиот видел вора и нашел его визитку.")
            print_menu("ВЫБОР", [
                ("1", "Вызвать полицию"),
                ("2", "Искать самому")
            ])
            vyybor = input("👉 Ваш выбор: ")
            if vyybor == "1":
                print("🎉 Полиция нашла преступника!")
            elif vyybor == "2":
                print("💔 Вы не нашли преступника...")
        elif vybor == "2":
            print("💔 Вы бросили дело...")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()