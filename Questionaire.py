# Questions used to get the user preferences
recommendationQuestions = {
    "player_experience_questions": [
        "He jugado Super Smash Bros antes: \n (1) Si \n (2) No \n>> ",
        "Tengo experiencia con videojuegos:\n (1) Si \n (2) No\n>> ",
        "Considero que mi nivel en Super Smash Bros. es: \n (1) A penas conozco el juego \n (2) No soy tan bueno \n"
        " (3) Soy promedio \n (4) Soy bueno \n (5) Jugador profesional\n>> "],

    "fight_style_questions": [
        "Preferiría que mi personaje  pelee con: \n (1) Cuerpo a cuerpo \n (2) Espada \n (3) Proyectiles\n>> ",
        "En los juegos de pelea prefiero: \n (1) Alguien que pelee de cerca \n (2) Alguien que cuente con herramientas"
        " para luchar \n (3) Un personaje que pueda disparar\n>> "],

    "speed_of_play_questions": [
        "Prefiero un personaje con peso:\n (1) Pesado \n (2) Normal \n (3) Ligero\n>> ",
        "Me gusta poder moverme rapido por el mapa: \n (1) Si \n (2) No\n>> ",
        "Me cuesta mantener el ritmo y velocidad: \n (1) Si \n (2) No\n>> "],

    "out_of_shield_questions": [
        "Utilizo mucho el escudo durante juegos de pelea:\n (1) Si \n (2) No \n>> ",
        "Es importante para mi tener ataques rapidos:\n (1) Si \n (2) No\n>> ",
        "Me gustaria tener una manera de atacar rapidamente saliendo del escudo: \n (1) Si \n (2) No\n>> "],

    "tier_questions": [
        "Se que es un tier en Super Smash Bros: \n (1) Si \n (2) No\n>> ",
        "Me importa la clasificacion de nivel de un personaje: \n (1) Si \n (2) No\n>> ",
        "Prefiero que mi personaje sea considerado como (sin importar el nivel del jugador): \n (1) El mejor \n "
        "(2) Bueno \n (3) Normal \n (4) No tan bueno\n (5) De los más bajos\n>> "],

    "jump_questions": [
        "Me cuesta regresar al mapa cuando me caigo:\n (1) Si \n (2) No\n>> ",
        "Prefiero un personaje que tenga:  \n (2) 2 Saltos \n (3) 3 saltos\n (4) 4 saltos\n (5) Mas de 4 saltos\n>> "],

    # For inexperienced players, we take into account these questions

    "saga_questions": [
        "De los siguientes videojuegos prefiero: \n (1)Starfox           (2)Bayonetta     (3)Super Mario Bros  "
        "(4)F-Zero           (5)Fire Emblem\n (6)Kid Icarus        (7)Donkey Kong   (8)Duck Hunt         "
        "(9)Metroid          (10)The Legend of Zelda\n (11)Pokemon          (12)Ice Climbers (13)Splatoon         "
        "(14)Animal Crossing (15)Street Fighter\n (16)King of Fighters (17)Kirby        (18)Punch-Out!       "
        "(19)Mega Man        (20)Game and Watch\n (21)Earthbound       (22)Pikmin       (23)N.E.S"
        "            (24)Castlevania     (25)Xenoblade Chronicles\n (26)Metal Gear Solid (27)Wii Fit      (28)Sonic    "
        "        (29)Dragon Quest    (30)Persona\n (31)Mii              (32)No conozco estos juegos\n>> "],

    "character_type": [
        "Me importa el diseño de mi personaje: \n (1) Si \n (2) No\n>> ",
        "Me gustan las cosas de fantasia: \n (1) Si \n (2) No\n>> ",
        "Me gustan los animales: \n (1) Si \n (2) No\n>> ",
        "Prefiero jugar con personajes que son: \n (1) Humanos \n (2) Animales \n (3) Fantásticos\n>> "]
}

# User preferences used to generate a user node in the database
user_preferences = {"experience": None, "fight_style": None, "speed_and_weight": None, "out_of_shield": None,
                    "tier": None, "jump": None, "saga": None, "character_type": None}

saga_dictionary = {1: "Starfox", 2: "Bayonetta", 3: "Super Mario Bros", 4: "F-Zero", 5: "Fire Emblem", 6: "Kid Icarus",
                   7: "Donkey Kong", 8: "Duck Hunt", 9: "Metroid", 10: "The Legend of Zelda"}


def getAnswers(question_dictionary: dict):
    keys = question_dictionary.keys()
    for question_type in keys:
        # Gets the answer and compounds it
        question_list = question_dictionary.get(question_type)
        if question_type.lower() == "player_experience_questions":
            playerExperience(question_list)
        elif question_type.lower() == "fight_style_questions":
            fightStyle(question_list)
        elif question_type.lower() == "speed_of_play_questions":
            speedOfPlay(question_list)
        elif question_type.lower() == "out_of_shield_questions":
            outOfShield(question_list)
        elif question_type.lower() == "tier_questions":
            tier(question_list)
        elif question_type.lower() == "jump_questions":
            jumps(question_list)
        elif question_type.lower() == "saga_questions":
            saga(question_list)
        elif question_type.lower() == "character_type":
            characterType(question_list)
        else:
            print("No es un atributo valido para clasificar personajes ")
    return user_preferences


def playerExperience(question_list: list):
    total_points = 0
    print("Bienvenido, aquí comienza el cuestionario. Ingrese su respuesta en la seccion indicada por '>>'\n")

    # Question 1
    total_points = twoOptionInput(total_points, 5, question_list[0])  # Question with a weight of 5

    # Question 2
    total_points = twoOptionInput(total_points, 1,  question_list[1])  # Question with a weight of 1

    # Question 3
    total_points = multipleOptionInput(total_points, 1, question_list[2], 1, 5)  # Question with a weight of 1

    if total_points >= 10:
        user_preferences["experience"] = "pro"
    elif total_points >= 5:
        user_preferences["experience"] = "casual"
    else:
        user_preferences["experience"] = "new"


def fightStyle(question_list: list):
    total_points = 0
    print("En esta seccion, estudiaremos tu estilo de pelea\n")

    # Question 1
    total_points = multipleOptionInput(total_points, 5, question_list[0], 1, 3)  # Question with a weight of 5

    # Question 2
    total_points = multipleOptionInput(total_points, 3, question_list[1], 1, 3)  # Question with a weight of 3

    if total_points >= 19:
        user_preferences["fight_style"] = "Projectile"
    elif total_points >= 9:
        user_preferences["fight_style"] = "Sword"
    else:
        user_preferences["fight_style"] = "Brawler"


def speedOfPlay(question_list: list):
    total_points = 0

    # Question 1
    total_points = multipleOptionInput(total_points, 5, question_list[0], 1, 3)  # Weight of 5
    # Question 2
    total_points = twoOptionInput(total_points, 3, question_list[1])  # Weight of 3
    # Question 3
    total_points = twoOptionInput(total_points, 5, question_list[2])  # Weight of 5

    if total_points >= 14:
        user_preferences["speed_and_weight"] = "Light"
    elif total_points >= 6:
        user_preferences["speed_and_weight"] = "Normal"
    else:
        user_preferences["speed_and_weight"] = "Heavy"


def outOfShield(question_list: list):
    total_points = 0

    # Question 1
    total_points = twoOptionInput(total_points, 2, question_list[0])
    # Question 2
    total_points = twoOptionInput(total_points, 5, question_list[1])
    # Question 3
    total_points = twoOptionInput(total_points, 7, question_list[2])

    if total_points >= 7:
        user_preferences["out_of_shield"] = "Yes"
    else:
        user_preferences["out_of_shield"] = "No"


def tier(question_list: list):
    total_points = 0
    # Question 1
    total_points = twoOptionInput(total_points, 0, question_list[0])  # Weight 0, to put the user in context
    # Question 2
    total_points = twoOptionInput(total_points, 100, question_list[1])  # Weight 100
    # Question 3
    total_points = multipleOptionInput(total_points, 10, question_list[2], 1, 5)  # Weight 10

    if total_points == 110:
        user_preferences["tier"] = "S"
    elif total_points == 120:
        user_preferences["tier"] = "A"
    elif total_points == 130:
        user_preferences["tier"] = "B"
    elif total_points == 140:
        user_preferences["tier"] = "C"
    elif total_points == 150:
        user_preferences["tier"] = "D"


def jumps(question_list: list):
    total_points = 0

    # Question 1
    total_points = twoOptionInput(total_points, 10, question_list[0])

    # Question 2
    total_points = multipleOptionInput(total_points, 10, question_list[1], 2, 5)

    if total_points >= 50:
        user_preferences["jump"] = "6"
    elif total_points >= 40:
        user_preferences["jump"] = "4"
    elif total_points >= 30:
        user_preferences["jump"] = "3"
    else:
        user_preferences["jump"] = "2"


def saga(question_list: list):
    total_points = multipleOptionInput(0, 1, question_list[0], 1, 32)
    if total_points != 32:
        user_preferences["saga"] = saga_dictionary[total_points]


def characterType(question_list: list):
    total_points = 0

    # Question 1
    total_points = twoOptionInput(total_points, 100, question_list[0])  # Weight 100

    # Question 2
    total_points = twoOptionInput(total_points, 10, question_list[1])  # Weight 10

    # Question 3
    total_points = twoOptionInput(total_points, 10, question_list[2])  # Weight 10

    # Question 4
    total_points = multipleOptionInput(total_points, 20, question_list[3], 1, 3)  # Weight 20

    if total_points >= 160:
        user_preferences["character_type"] = "Fantasy"
    elif total_points >= 140:
        user_preferences["character_type"] = "Animal"
    elif total_points > 100:
        user_preferences["character_type"] = "Human"


def verifyInput(user_input: int, minimum: int, maximum: int):
    if minimum <= user_input <= maximum:
        return True
    else:
        return False


def twoOptionInput(point_total: int, weight: int, question: str):
    user_input = -1
    while not verifyInput(user_input, 1, 2):
        try:
            user_input = int(input(question))
        except:
            continue
    if user_input == 1:
        point_total += (1 * weight)
    return point_total


def multipleOptionInput(point_total: int, weight: int, question: str, min_value: int, max_value: int):
    user_input = -1
    while not verifyInput(user_input, min_value, max_value):
        try:
            user_input = int(input(question))
        except Exception:
            continue

    point_total += (user_input * weight)
    return point_total

