init:
    $ config.window_title = "Out of Samsara"
    define e = Character('Я', color="#ffeb84")
    image bg uni = "bg samsara.jpg"
    image bg bosch = "bosch.jpeg"
    image trolley = "sprite.png"
    define diesirae = "diesirae.mp3"
    define luxaeterna = "luxaeterna.mp3"
init python:
    import random

    class EthicalSituation:
        def __init__(self, description, choices):
            self.description = description
            self.choices = choices
            self.selected_choice = None

        def get_description(self):
            return self.description

        def get_choices(self):
            return [choice['action'] for choice in self.choices]

        def choose(self, choice_index):
            self.selected_choice = choice_index

        def get_consequence(self):
            if self.selected_choice is not None:
                return self.choices[self.selected_choice]['consequence']
            return None

        def get_ideology(self):
            if self.selected_choice is not None:
                return self.choices[self.selected_choice]['consequence'].split('\n')[1].strip().split('> ')[1]
            return None

    # Создание набора этических ситуаций
    ethical_situations = [
        EthicalSituation(
            "По рельсам едет вагонетка. На её пути к рельсам привязаны пять человек. Но рядом есть рычаг, который может перенаправить вагонетку на другую ветку, где привязан один человек.",
            [
                {
                    "action": "Я тяну за рычаг",
                    "consequence": "Получено:\n> Утилитаризм\nЯ пытаюсь максимизировать общее благо, даже если это требует жертв."
                },
                {
                    "action": "Я ничего не делаю",
                    "consequence": "Получено:\n> Деонтология\nСоответствие моральным принципам для меня важнее последствий."
                }
            ]
        ),
        EthicalSituation(
            "Мне нужно выбрать между двумя дверями: за одной меня ждет невеста, за другой — смерть от тигра. Девушка, которая в меня влюблена, указывает на правую дверь. За ней другая невеста или тигр?",
            [
                {
                    "action": "Невеста",
                    "consequence": "Получено:\n> Оптимизм\nЯ верю в положительный исход."
                },
                {
                    "action": "Тигр",
                    "consequence": "Получено:\n> Пессимизм\nЯ жду, что случится что-то плохое."
                }
            ]
        ),
        EthicalSituation(
            "Я сомневаюсь, что реальность вокруг - настоящая. Возможно ли это проверить?",
            [
                {
                    "action": "Мои ощущения определяют объективную реальность",
                    "consequence": "Получено:\n> Прагматизм\nПрактика определяет, что такое истина."
                },
                {
                    "action": "Объективной реальности невозможно постичь",
                    "consequence": "Получено:\n> Скептицизм\nНевозможно познать объективную реальность."
                }
            ]
        ),
        EthicalSituation(
            "Я заменил все до одной части древнего корабля. Это тот же самый корабль?",
            [
                {
                    "action": "Корабль остался тем же",
                    "consequence": "Получено:\n> Эссенциализм\nИдея объекта первичнее материальной репрезентации."
                },
                {
                    "action": "Это другой корабль",
                    "consequence": "Получено:\n> Материализм\nИзменения в материальных составляющих объекта изменяют его сущность."
                }
            ]
        ),
        EthicalSituation(
            "Я встречаю Отто, который полагается только на свои записи, и Ингу, которая полагается на свою память. Являются ли они личностями в одинаковой степени?",
            [
                {
                    "action": "Записи Отто эквивалентны биологической памяти",
                    "consequence": "Получено:\n> Экстернализм\nПамять и сознание могут зависеть от внешних объектов и источников."
                },
                {
                    "action": "Только настоящая память Инги делает её личностью",
                    "consequence": "Получено:\n> Интернализм\nПамять и сознание зависят исключительно от внутренних состояний и процессов."
                }
            ]
        ),
        EthicalSituation(
            "Я сижу в темной пещере и вижу только тени объектов. Я могу выйти на свет и попытаться узнать истину, но это требует отказа от всех прежних убеждений.",
            [
                {
                    "action": "Я выхожу на свет",
                    "consequence": "Получено:\n> Платонизм\nИстинное знание находится за пределами чувственного опыта и постигается разумом."
                },
                {
                    "action": "Я продолжаю следить за тенями",
                    "consequence": "Получено:\n> Эмпиризм\nИстинное знание постигается через чувственный опыт."
                }
            ]
        ),
        EthicalSituation(
            "По рельсам едет вагонетка. Я могу толкнуть толстяка на пути вагонетки, чтобы спасти пятерых привязанных к рельсам.",
            [
                {
                    "action": "Я толкаю толстяка",
                    "consequence": "Получено:\n> Консеквенциализм\nМоральная ценность действия определяется его последствиями."
                },
                {
                    "action": "Я не вмешиваюсь",
                    "consequence": "Получено:\n> Деонтология\nСоответствие моральным принципам для меня важнее последствий."
                }
            ]
        ),
        EthicalSituation(
            "У меня есть коробка с жуком. У всех остальных тоже есть коробки с жуками, но они закрыты. Как нам договориться, что такое жук?",
            [
                {
                    "action": "Для меня каждый жук имеет тождественный референт",
                    "consequence": "Получено:\n> Реализм\nСуществуют универсалии, и термины имеют тождественные референты."
                },
                {
                    "action": "Мне важно только обозначение, обозначаемое несопоставимо",
                    "consequence": "Получено:\n> Номинализм\nУниверсалии не существуют вне нашего разума, и значение слов зависит только от контекста их использования."
                }
            ]
        ),
        EthicalSituation(
            "Имеет ли событие значение, если никто его не наблюдает?",
            [
                {
                    "action": "Событие имеет значение",
                    "consequence": "Получено:\n> Реализм\nРеальность существует независимо от нашего восприятия."
                },
                {
                    "action": "Событие не имеет значения",
                    "consequence": "Получено:\n> Субъективизм\nРеальность зависит от восприятия субъекта."
                }
            ]
        ),
        EthicalSituation(
            "На болоте меня на молекулы расщепила молния и был создан мой идентичный двойник, который ведет себя так же, как я. Он - это я?",
            [
                {
                    "action": "Мы один и тот же человек",
                    "consequence": "Получено:\n> Психологический континуизм\nЛичная идентичность сохраняется через психологическую непрерывность."
                },
                {
                    "action": "Мы разные люди",
                    "consequence": "Получено:\n> Телесный континуизм\nЛичная идентичность зависит от физической непрерывности тела."
                }
            ]
        ),
        EthicalSituation(
            "Я должен решить, стоит ли применять пытки к пленнику, который может знать местонахождение бомбы, способной уничтожить город. Бомба тикает.",
            [
                {
                    "action": "Я применяю пытки",
                    "consequence": "Получено:\n> Консеквенциализм\nМоральная ценность действия определяется его последствиями."
                },
                {
                    "action": "Я отказываюсь от пыток",
                    "consequence": "Получено:\n> Деонтология\nСоответствие моральным принципам для меня важнее последствий."
                }
            ]
        ),
        EthicalSituation(
            "Я был дворянином, но вдруг оказываюсь крестьянином. Почему так произошло?",
            [
                {
                    "action": "Такова моя судьба",
                    "consequence": "Получено:\n> Фатализм\nВсё, что со мной происходит, предопределено и неизбежно."
                },
                {
                    "action": "Мне нужно было бороться за прежнюю жизнь",
                    "consequence": "Получено:\n> Волюнтаризм\nМоя воля играет ключевую роль в том, как повернутся события."
                }
            ]
        ),
        EthicalSituation(
            "Я никогда не видел определенной градации синего цвета. Могу ли я её восстановить, если представлю весь остальной спектр?",
            [
                {
                    "action": "Воображение и разум могут заполнять пробелы восприятия",
                    "consequence": "Получено:\n> Рационализм\nРазум и воображение дополнят мой чувственный опыт и дадут знания о непостижимых вещах."
                },
                {
                    "action": "Только опыт может дать полное знание",
                    "consequence": "Получено:\n> Эмпиризм\nВсе знания происходят из опыта, градацию невозможно вообразить."
                }
            ]
        ),
        EthicalSituation(
            "Я представляю огромную мельницу, где работают все механизмы разума. Могут ли чисто механические процессы объяснить сознание?",
            [
                {
                    "action": "Сознание трансцендентно и недоступно описанию через реальные объекты",
                    "consequence": "Получено:\n> Дуализм\nСознание и разум не сводимы к физическим процессам и имеют иную природу."
                },
                {
                    "action": "Сознание можно объяснить через механизмы",
                    "consequence": "Получено:\n> Физикализм\nВсе ментальные процессы можно объяснить через физические и механические."
                }
            ]
        )
    ]

    def get_random_situation(remaining_situations):
        if remaining_situations:
            return random.choice(remaining_situations)
        return None

    def add_ideology(ideology, ideologies_count):
        if ideology in ideologies_count:
            ideologies_count[ideology] += 1
        else:
            ideologies_count[ideology] = 1

label start:
    scene bg uni
    show trolley with dissolve
    play music diesirae loop
    $ remaining_situations = ethical_situations[:]
    $ ideologies_count = {}
    $ current_situation = get_random_situation(remaining_situations)
    $ remaining_situations.remove(current_situation)
    e "Привет!"
    e "Привет?"
    e "Где я?"
    e "Как я здесь оказался?"
    e "Ты меня слышишь?"
    e "Кто я?"
    $ player_name = renpy.input("Меня зовут...")
    e "Нет. Здесь у меня нет имени."
    e "Передо мной появляются странные, фантастические картины, и они требуют моего участия."
    e "Они требуют, чтобы я сделал выбор."
    e "Мне нужно решить, что есть добро, а что — зло, что справедливо, а что — нет..."
    e "...может быть, тогда я пойму, кто я, и остановлю этот безумный цикл?"

    e "[current_situation.get_description()]"

    menu:
        "[current_situation.get_choices()[0]]":
            $ current_situation.choose(0)
            $ ideology = current_situation.get_ideology()
            $ add_ideology(ideology, ideologies_count)
            scene bg bosch with dissolve
            show trolley with dissolve
            e "[current_situation.get_consequence()]"
            jump next_situation
        "[current_situation.get_choices()[1]]":
            $ current_situation.choose(1)
            $ ideology = current_situation.get_ideology()
            $ add_ideology(ideology, ideologies_count)
            scene bg bosch with dissolve
            show trolley with dissolve
            e "[current_situation.get_consequence()]"
            jump next_situation

label next_situation:
    $ current_situation = get_random_situation(remaining_situations)
    if current_situation is None:
        jump end
    $ remaining_situations.remove(current_situation)
    scene bg uni with dissolve
    show trolley with dissolve
    e "[current_situation.get_description()]"

    menu:
        "[current_situation.get_choices()[0]]":
            $ current_situation.choose(0)
            $ ideology = current_situation.get_ideology()
            $ add_ideology(ideology, ideologies_count)
            scene bg bosch with dissolve
            show trolley with dissolve
            e "[current_situation.get_consequence()]"
            jump next_situation
        "[current_situation.get_choices()[1]]":
            $ current_situation.choose(1)
            $ ideology = current_situation.get_ideology()
            $ add_ideology(ideology, ideologies_count)
            scene bg bosch with dissolve
            show trolley with dissolve
            e "[current_situation.get_consequence()]"
            jump next_situation

label end:
    e "Все ответы даны... но были ли они правильными? А есть ли здесь вообще правильные ответы?"
    e "Кто я?"
    $ result = ", ".join([f"{ideology}: {count}" for ideology, count in ideologies_count.items()])
    e "[result]"
    return
