init -1 python:
    class Clue:
        """
        Модель детективной улики на доске расследования
        """
        def __init__(self, clue_id, title, description, thumb, full_image=None, pos=(0, 0), category="item", connections=None):
            self.clue_id = clue_id
            self.title = title
            self.description = description
            self.thumb = thumb                          # Превью на доске
            self.full_image = full_image or thumb       # Картинка для детального осмотра
            self.pos = pos                              # Координаты (x, y) на доске
            self.category = category                    # "item", "person", "document", "location"
            self.connections = connections or []        # Список ID связанных улик


    class ClueDatabase:
        """
        Справочник всех улик в игре, не связан с сохранениями
        """
        _registry = {}

        @classmethod
        def register(cls, clue):
            cls._registry[clue.clue_id] = clue

        @classmethod
        def get(cls, clue_id):
            return cls._registry.get(clue_id)

        @classmethod
        def get_all(cls):
            return list(cls._registry.values())

        @classmethod
        def get_by_ids(cls, clue_ids):
            """Возвращает список объектов улик по переданному набору ID"""
            if not clue_ids:
                return []
            return [cls._registry[cid] for cid in clue_ids if cid in cls._registry]

        @classmethod
        def get_unique_connections(cls, unlocked_ids):
            """
            Возвращает список уникальных пар связей ((x1, y1), (x2, y2))
            только между теми уликами которые открыл игрок
            """
            edges = set()
            unlocked_clues = cls.get_by_ids(unlocked_ids)

            for clue in unlocked_clues:
                for target_id in clue.connections:
                    if target_id in unlocked_ids and target_id in cls._registry:
                        target_clue = cls._registry[target_id]
                        edge_key = tuple(sorted([clue.clue_id, target_id]))
                        edges.add((edge_key, clue.pos, target_clue.pos))
            return edges


# ЗАГЛУШКА

    # 1. Латунный ключ (связан с квитанцией)
    ClueDatabase.register(Clue(
        clue_id="master_key",
        title=_("Латунный ключ от 203"),
        description=_("Тяжёлый ключ с потёртой биркой '203'. Был спрятан в нижнем ящике стойки регистрации."),
        thumb="gui/window_icon.png",
        pos=(500, 350),
        category="item",
        connections=["torn_receipt"]
    ))

    # 2. Обрывок квитанции
    ClueDatabase.register(Clue(
        clue_id="torn_receipt",
        title=_("Обгоревшая квитанция"),
        description=_("Квитанция об оплате номера 203 на имя неизвестного постояльца. Дата полустёрта."),
        thumb="gui/window_icon.png",
        pos=(950, 420),
        category="document",
        connections=[]
    ))

    # 3. Фотография постояльца
    ClueDatabase.register(Clue(
        clue_id="guest_photo",
        title=_("Фотография постояльца"),
        description=_("Снимок сделан на полароид в холле отеля три дня назад. Лицо человека выглядит встревоженным."),
        thumb="gui/window_icon.png",
        pos=(1400, 300),
        category="person",
        connections=[]
    ))