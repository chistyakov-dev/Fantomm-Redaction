from ui import print_menu

class FriendsGenre:
    def __init__(self, game_name, platform, age, id):
        self.game_name = game_name
        self.platform = platform
        self.age = age
        self.id = id
        self.genre_type = "friends"
    
    def create(self):
        print("\n=== ДВА ДРУГА ===")
        self.name_one = input("👤 Имя первого друга: ")
        self.name_two = input("👤 Имя второго друга: ")
        self.location = input("🏞️ Где происходит действие: ")
        self.history = input("📖 Краткая история двух друзей: ")
        self.victory = input("🏁 Как всё закончится: ")
        
        print(f"\n✅ Игра '{self.game_name}' успешно создана!")
        print(f"📜 Описание: Основной сюжет развивается вокруг {self.name_one} и {self.name_two},")
        print(f"действие происходит в {self.location}.")
        
        return self.get_game_data()
    
    def get_game_data(self):
        return {
            "name": self.game_name,
            "platform": self.platform,
            "genre_type": self.genre_type,
            "name_one": self.name_one,
            "name_two": self.name_two,
            "location": self.location,
            "history": self.history,
            "victory": self.victory,
            "age": self.age,
            "id": self.id
        }
    
    def test(self):
        print_menu("🎮 ТЕСТОВЫЙ РЕЖИМ", [])
        print(f"Вы — {self.name_one} и {self.name_two}.")
        print(f"Вы находитесь в {self.location}. Ваша история: {self.history}")
        print("Представьте, что вы поссорились. Что вы сделаете?")
        print_menu("ВЫБОР", [
            ("1", "подарить подарок и извиниться первым"),
            ("2", "не общаться")
        ])
        
        vybor = input("👉 Ваш выбор: ")
        if vybor == "1":
            print("✨ Победа! Вы успешно помирились.")
        elif vybor == "2":
            print("💔 Поражение... Дружба разрушена.")
        else:
            print("❓ Непонятный выбор.")
    
    def load_and_test(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        self.test()