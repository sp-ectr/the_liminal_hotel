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


# УЛИКИ = КАРТОЧКИ ПЕРСОНАЖЕЙ (полароидные снимки на доске расследования)
# Открываются в сюжете через TimeEngine.unlock_clue("<clue_id>")
    ClueDatabase.register(Clue(
        clue_id="desi",
        title=_("Дезмонд Ларкспур"),
        description=_("Постоялец отеля. Держится неестественно спокойно и, кажется, знает о петлях больше, чем говорит."),
        thumb="gui/investigation_board/desi.png",
        pos=(450, 480),
        category="person",
        connections=[]
    ))

    ClueDatabase.register(Clue(
        clue_id="eli",
        title=_("Илай Рурк"),
        description=_("Мастер на все руки отеля. Его инструменты пропали из подсобки в ночь инцидента."),
        thumb="gui/investigation_board/eli.png",
        pos=(780, 460),
        category="person",
        connections=[]
    ))

    ClueDatabase.register(Clue(
        clue_id="dr_dimaano",
        title=_("Доктор Эверетт Димаано"),
        description=_("Хирург. Привёл меня в сознание после аварии и наблюдал, пока я не встала на ноги. Держит дистанцию: «мы друг другу случайные прохожие, а не попутчики». Позже его можно найти в баре."),
        thumb="gui/investigation_board/dr_dimaano.png",
        pos=(1140, 470),
        category="person",
        connections=[]
    ))

    ClueDatabase.register(Clue(
        clue_id="mr_renard",
        title=_("Мистер Ренар"),
        description=_("Владелец отеля. Улыбается чаще, чем говорит правду, и ни разу не назвал одно и то же время инцидента."),
        thumb="gui/investigation_board/mr_renard.png",
        pos=(1480, 490),
        category="person",
        connections=[]
    ))