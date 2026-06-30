import json
import os
import random

NOTES_FILE = "notes.json"

def load_notes():
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

class GitFan:
    def __init__(self):
        self.name = "GitFan"
        self.version = "1.0.0"
        self.greetings = [
            "Привет! Я GitFan. Спрашивай про движок и игры.",
            "Здравствуй! GitFan на связи. Чем могу помочь?",
            "Йо! GitFan здесь. Показываю игры, сюжеты, статистику — обращайся.",
            "Доброго времени суток! GitFan готов к работе."
        ]
        self.goodbyes = [
            "До встречи! Удачи с играми.",
            "Пока! Буду ждать твоего возвращения.",
            "Увидимся! GitFan уходит в спящий режим.",
            "Всего доброго! Приходи ещё."
        ]
        self.unknown_responses = [
            "Я не совсем понял. Напиши «помощь» чтобы увидеть что я умею.",
            "Хмм, не знаю такой команды. Попробуй «помощь».",
            "Этого я пока не умею. Но могу показать список команд — просто напиши «помощь»."
        ]
    
    def greet(self):
        print()
        print("   ┌──────────────────────────────┐")
        print("   │                              │")
        print("   │   🤖 GITFAN ONLINE           │")
        print("   │   Текстовый ассистент        │")
        print("   │   для FANTOM REDACTION       │")
        print("   │                              │")
        print("   └──────────────────────────────┘")
        print()
        print(f"   {random.choice(self.greetings)}")
        print()
    
    def say_goodbye(self):
        print(f"   {random.choice(self.goodbyes)}")
        print()
    
    def show_help(self):
        print()
        print("   ┌─────────────────────────────────────┐")
        print("   │ 📋 ЧТО Я УМЕЮ                       │")
        print("   ├─────────────────────────────────────┤")
        print("   │ 🎮 список игр                       │")
        print("   │ 🎮 покажи игры                      │")
        print("   │                                     │")
        print("   │ 🔍 жанр [название]                  │")
        print("   │ 🔍 найди хорроры                    │")
        print("   │                                     │")
        print("   │ 📖 сюжет [название игры]            │")
        print("   │ 📖 расскажи про [название игры]     │")
        print("   │                                     │")
        print("   │ 📊 статистика                       │")
        print("   │                                     │")
        print("   │ 📝 заметки                          │")
        print("   │                                     │")
        print("   │ ℹ️ помощь                            │")
        print("   │ ℹ️ что ты умеешь                     │")
        print("   │                                     │")
        print("   │ 👋 пока                              │")
        print("   │ 👋 меню                              │")
        print("   └─────────────────────────────────────┘")
        print()
    
    def process(self, user_input, games_data=None, notes_data=None):
        text = user_input.lower().strip()
        
        if any(word in text for word in ["привет", "здравствуй", "прив", "хай", "йо", "добрый"]):
            print(f"   {random.choice(self.greetings)}")
            return "continue"
        
        if any(word in text for word in ["пока", "выход", "выйти", "меню", "вернись", "назад"]):
            self.say_goodbye()
            return "menu"
        
        if any(word in text for word in ["помощь", "команды", "что ты умеешь", "что умеешь", "помоги"]):
            self.show_help()
            return "continue"
        
        if any(word in text for word in ["список", "игры", "сохранения", "покажи игры", "мои игры"]):
            self._show_games(games_data)
            return "continue"
        
        if any(word in text for word in ["жанр", "найди", "покажи rpg", "покажи хоррор", "фильтр"]):
            self._filter_by_genre(text, games_data)
            return "continue"
        
        if any(word in text for word in ["сюжет", "описание", "расскажи", "про"]):
            self._show_plot(text, games_data)
            return "continue"
        
        if any(word in text for word in ["статистика", "стата", "сколько игр", "всего"]):
            self._show_stats(games_data)
            return "continue"
        
        if any(word in text for word in ["заметки", "мои заметки", "покажи заметки"]):
            self._show_notes(notes_data)
            return "continue"
        
        if any(word in text for word in ["кто ты", "как зовут", "твоё имя", "имя"]):
            print(f"   Я GitFan — виртуальный помощник движка FANTOM REDACTION.")
            print(f"   Моя задача: помогать тебе ориентироваться в твоих играх.")
            print(f"   Версия: {self.version}")
            return "continue"
        
        if any(word in text for word in ["спасибо", "благодарю", "спс"]):
            responses = [
                "Всегда пожалуйста!",
                "Рад помочь!",
                "Не за что, обращайся ещё!",
                "Для меня это в удовольствие."
            ]
            print(f"   {random.choice(responses)}")
            return "continue"
        
        print(f"   {random.choice(self.unknown_responses)}")
        return "continue"
    
    def _show_games(self, games_data):
        if not games_data:
            print("   📭 У тебя пока нет сохранённых игр.")
            print("   Создай первую — я сразу её увижу!")
            return
        
        print()
        print(f"   🎮 ТВОИ ИГРЫ ({len(games_data)} шт.):")
        
        genre_names = {
            "rpg": "🎮 RPG", "horror": "👻 Хоррор", "detective": "🕵️ Детектив",
            "Earth": "🌍 Earth", "Средневековье": "🏰 Средневековье",
            "hero_villain": "⚔️ Герой/Злодей", "friends": "👥 Друзья",
            "action": "💥 Экшен", "survival": "🏕️ Выживание"
        }
        
        for i, game in enumerate(games_data, 1):
            name = game['name'][:22] + "…" if len(game['name']) > 22 else game['name']
            genre = genre_names.get(game.get('genre_type'), game.get('platform', '—'))
            print(f"   {i}. {name}  {genre}")
        print()
    
    def _filter_by_genre(self, text, games_data):
        genre_keywords = {
            "rpg": "rpg", "хоррор": "horror", "horror": "horror",
            "детектив": "detective", "earth": "Earth", "земля": "Earth",
            "средневековье": "Средневековье",
            "герой и злодей": "hero_villain", "друзья": "friends",
            "экшен": "action", "выживание": "survival"
        }
        
        found_genre = None
        for keyword, genre_type in genre_keywords.items():
            if keyword in text:
                found_genre = genre_type
                break
        
        if not found_genre:
            print("   ❓ Какой жанр искать? Например: «жанр хоррор»")
            return
        
        if not games_data:
            print("   📭 У тебя пока нет сохранённых игр.")
            return
        
        filtered = [g for g in games_data if g.get('genre_type') == found_genre]
        
        genre_names = {
            "rpg": "RPG", "horror": "Хоррор", "detective": "Детектив",
            "Earth": "Earth", "Средневековье": "Средневековье",
            "hero_villain": "Герой и злодей", "friends": "Друзья",
            "action": "Экшен", "survival": "Выживание"
        }
        
        if not filtered:
            print(f"   📭 Игр в жанре «{genre_names.get(found_genre, found_genre)}» пока нет.")
            return
        
        print()
        print(f"   🎮 Игры в жанре «{genre_names.get(found_genre, found_genre)}» ({len(filtered)} шт.):")
        for i, game in enumerate(filtered, 1):
            print(f"   {i}. {game['name']}")
        print()
    
    def _show_plot(self, text, games_data):
        if not games_data:
            print("   📭 У тебя пока нет сохранённых игр.")
            return
        
        words = text.split()
        trigger_words = ["сюжет", "описание", "расскажи", "про"]
        name_parts = [w for w in words if w not in trigger_words]
        
        if not name_parts:
            print("   ❓ Про какую игру рассказать? Напиши «сюжет [название]»")
            return
        
        search_name = " ".join(name_parts).lower()
        
        found = None
        for game in games_data:
            if search_name in game['name'].lower():
                found = game
                break
        
        if not found:
            print(f"   ❓ Не нашёл игру с названием похожим на «{' '.join(name_parts)}»")
            return
        
        print()
        print(f"   📖 СЮЖЕТ: {found['name']}")
        print(f"   📱 Платформа: {found['platform']}")
        print(f"   👤 Возраст: {found.get('age', '—')}")
        
        gt = found.get('genre_type')
        
        if gt == "hero_villain":
            print(f"   🧙 Герой: {found.get('hero_name', '—')}")
            print(f"   👿 Злодей: {found.get('villain_name', '—')}")
            print(f"   ⚡ Умение героя: {found.get('hero_skill', '—')}")
            print(f"   💀 Умение злодея: {found.get('villain_skill', '—')}")
            print(f"   📍 Локация: {found.get('location', '—')}")
            print(f"   🎯 Цель: {found.get('objective', '—')}")
        elif gt == "friends":
            print(f"   👥 Друзья: {found.get('name_one', '—')} и {found.get('name_two', '—')}")
            print(f"   📍 Локация: {found.get('location', '—')}")
            print(f"   📖 История: {found.get('history', '—')}")
        elif gt == "action":
            print(f"   🧙 Герой: {found.get('hero_name', '—')}")
            print(f"   🔫 Оружие: {found.get('hero_weapon', '—')}")
            print(f"   👥 Врагов: {found.get('enemy_count', '—')}")
            print(f"   👾 Босс: {found.get('boss_name', '—')}")
            print(f"   📍 Локация: {found.get('location', '—')}")
            print(f"   🎯 Цель: {found.get('objective', '—')}")
        elif gt == "survival":
            print(f"   🧙 Герой: {found.get('hero_name', '—')}")
            print(f"   🍗 Еда: {found.get('food', '—')}")
            print(f"   💧 Вода: {found.get('water', '—')}")
            print(f"   💊 Аптечки: {found.get('medkits', '—')}")
            print(f"   👾 Опасность: {found.get('danger', '—')}")
            print(f"   ⏳ Дней: {found.get('days_goal', '—')}")
        elif gt == "rpg":
            print(f"   🧙 Герой: {found.get('hero_name', '—')} ({found.get('hero_class', '—')})")
            print(f"   💰 Золото: {found.get('starting_gold', '—')}")
            print(f"   👥 Спутник: {found.get('companion', '—')}")
            print(f"   📜 Квест: {found.get('quest', '—')}")
        elif gt == "horror":
            print(f"   🧙 Герой: {found.get('hero_name', '—')}")
            print(f"   👾 Монстр: {found.get('monster', '—')}")
            print(f"   😱 Страх: {found.get('fear_level', '—')}")
            print(f"   🔋 Батарейки: {found.get('batteries', '—')}")
            print(f"   📍 Локация: {found.get('location', '—')}")
            print(f"   🎯 Цель: {found.get('objective', '—')}")
        elif gt == "detective":
            print(f"   🕵️ Детектив: {found.get('detective_name', '—')}")
            print(f"   📍 Локация: {found.get('location', '—')}")
            print(f"   🔍 Преступление: {found.get('crime', '—')}")
            print(f"   👥 Подозреваемых: {found.get('suspect_count', '—')}")
            print(f"   🔎 Улика 1: {found.get('clue_1', '—')}")
            print(f"   🔎 Улика 2: {found.get('clue_2', '—')}")
            print(f"   🔄 Поворот: {found.get('twist', '—')}")
        elif gt == "Earth":
            print(f"   🧙 Воин: {found.get('hero_name', '—')}")
            print(f"   🗡 Оружие: {found.get('weapons', '—')}")
            print(f"   📖 История: {found.get('history', '—')}")
        elif gt == "Средневековье":
            print(f"   👑 Король: {found.get('hero_name', '—')}")
            print(f"   🏰 Королевство: {found.get('kor_name', '—')}")
            print(f"   📖 История: {found.get('history', '—')}")
        
        print()
    
    def _show_stats(self, games_data):
        if not games_data:
            print("   📊 Статистика пуста — пока у тебя нет сохранённых игр.")
            return
        
        total = len(games_data)
        
        genre_counts = {}
        platform_counts = {}
        for game in games_data:
            gt = game.get('genre_type', 'неизвестно')
            genre_counts[gt] = genre_counts.get(gt, 0) + 1
            pl = game.get('platform', 'неизвестно')
            platform_counts[pl] = platform_counts.get(pl, 0) + 1
        
        genre_names = {
            "rpg": "RPG", "horror": "Хоррор", "detective": "Детектив",
            "Earth": "Earth", "Средневековье": "Средневековье",
            "hero_villain": "Герой/Злодей", "friends": "Друзья",
            "action": "Экшен", "survival": "Выживание"
        }
        
        print()
        print(f"   📊 СТАТИСТИКА")
        print(f"   📁 Всего игр: {total}")
        print(f"   📱 Мобайл: {platform_counts.get('Мобайл', 0)}")
        print(f"   💻 ПК: {platform_counts.get('ПК', 0)}")
        print(f"   🔄 Гибрид: {platform_counts.get('Гибрид', 0)}")
        print(f"   ———")
        for gt, count in genre_counts.items():
            name = genre_names.get(gt, gt)
            print(f"   {name}: {count}")
        print()
    
    def _show_notes(self, notes_data):
        if not notes_data:
            print("   📝 У тебя пока нет заметок.")
            print("   💡 Создать можно в главном меню: 6 — Заметки")
            return
        
        print()
        print(f"   📝 ТВОИ ЗАМЕТКИ ({len(notes_data)} шт.):")
        for note in notes_data:
            title = note['title'][:30] + "…" if len(note['title']) > 30 else note['title']
            print(f"   📄 {note['id']}. {title}")
            print(f"      📅 {note.get('created_at', '—')}")
        print()


def show_gitfan_boot():
    print()
    print("         ┌──────────────────────────────────────┐")
    print("         │                                      │")
    print("         │         ██████╗ ██╗████████╗         │")
    print("         │        ██╔════╝ ██║╚══██╔══╝         │")
    print("         │        ██║  ███╗██║   ██║            │")
    print("         │        ██║   ██║██║   ██║            │")
    print("         │        ╚██████╔╝██║   ██║            │")
    print("         │         ╚═════╝ ╚═╝   ╚═╝            │")
    print("         │                                      │")
    print("         │           FANTOM REDACTION           │")
    print("         │                                      │")
    print("         │    ┌──────────────────────────┐      │")
    print("         │    │    ╭─────────────────╮    │      │")
    print("         │    │    │                 │    │      │")
    print("         │    │    │   ███████████   │    │      │")
    print("         │    │    │   ███ ███ ███   │    │      │")
    print("         │    │    │   ███████████   │    │      │")
    print("         │    │    │                 │    │      │")
    print("         │    │    │   ███████████   │    │      │")
    print("         │    │    │   ██       ██   │    │      │")
    print("         │    │    │                 │    │      │")
    print("         │    │    ╰─────────────────╯    │      │")
    print("         │    │        ██████            │      │")
    print("         │    │      ██████████          │      │")
    print("         │    │        ██████            │      │")
    print("         │    │        ██████            │      │")
    print("         │    │     ██        ██         │      │")
    print("         │    └──────────────────────────┘      │")
    print("         │                                      │")
    print("         │   ┌──────────────────────────────┐   │")
    print("         │   │  Твой порядок — моя работа   │   │")
    print("         │   └──────────────────────────────┘   │")
    print("         │                                      │")
    print("         └──────────────────────────────────────┘")
    print()
    print("   GitFan online. Работай много, скоро отдых.")
    print("   Что будем делать?")
    print()