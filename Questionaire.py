recommendationQuestions = {
    "player_experience_questions": [
        "He jugado Super Smash Bros antes: \n (1) Si \n (2) No \n>> ",
        "Tengo experiencia con videojuegos:\n (1) Si \n (2) No",
        "Considero que mi nivel en Super Smash Bros. es: \n (1) A penas conozco el juego \n (2) No soy tan bueno \n"
        " (3) Soy promedio \n (4) Soy bueno \n (5) Jugador profesional"],

    "fight_style_questions": [
        "Preferiría que mi personaje  pelee con: \n (1) Espada \n (2) Cuerpo a cuerpo\n (3) Proyectiles",
        "En los juegos de pelea prefiero: \n (1) Alguien que pelee de cerca \n (2) Alguien que cuente con herramientas"
        " para luchar \n (3) Un personaje que pueda disparar"],

    "speed_of_play_questions": [
        "Prefiero un personaje con peso: (1) Pesado \n (2) Normal \n (3) Ligero",
        "Me gusta poder moverme rapido por el mapa: \n (1) Si \n (2) No",
        "Me cuesta mantener el ritmo y velocidad: \n (1) Si \n (2) No"],

    "out_of_shield_questions": [
        "Utilizo mucho el escudo durante juegos de pelea: (1) Si \n (2) No \n",
        "Es importante para mi tener ataques rapidos: (1) Si \n (2) No",
        "Me gustaria tener una manera de atacar rapidamente saliendo del escudo: \n (1) Si \n (2) No"],

    "tier_questions": [
        "Se que es un tier en Super Smash Bros: \n (1) Si \n (2) No",
        "Me importa la clasificacion de nivel de un personaje: \n (1) Si \n (2) No",
        "Prefiero que mi personaje sea considerado como (sin importar el nivel del jugador): \n (1) El mejor \n "
        "(2) Bueno \n (3) Normal \n (4) De los más bajos"],

    "jump_questions": [
        "Me cuesta regresar al mapa cuando me caigo: (1) Si \n (2) No",
        "Prefiero un personaje que tenga: \n (1) Mas de 4 saltos \n (2) Entre 3 y 4 saltos \n (3) 2 saltos"],

    # For inexperienced players, we take into account these questions

    "saga_questions": [
        "Prefiero los videojuegos de: \n (1) Mario \n (2) Pokemon \n (3) Animal Crossing \n (4) Pikmin \n "
        "(5) Fire Emblem \n (6) Zelda \n (7) Final Fantasy \n (8) Kid Icarus \n (9) Metroid \n "
        "(10) No conozco estos juegos"],

    "character_type": [
        "Me importa el diseño de mi personaje: \n (1) Si \n (2) No",
        "Me gustan las cosas de fantasia: \n (1) Si \n (2) No",
        "Me gustan los animales: \n (1) Si \n (2) No",
        "Prefiero jugar con personajes que son: \n (1) Humanos \n (2) Fantasticos \n (3) Animales"]
}


def getAnswers(question_dictionary: dict, question_type: str):
    # Gets the answer and compounds it
    question_list = question_dictionary.get(question_type)
    if question_type.lower() == "player_experience_questions":
        playerExperience(question_list)
    elif question_type.lower() == "fight_style_questions":
        fightStyle(question_list)


def playerExperience(question_list: list):
    total_points = 0
    print("En esta seccion de preguntas, veremos tu nivel en el juego")

    user_selection = -1

    # Question 1
    while not verifyInput(user_selection, 1, 2):
        try:
            user_selection = int(input(question_list[0]))
        except:
            continue

        twoOptionInput(user_selection, total_points, 5)  # Question with a weight of 5
    user_selection = -1  # Restart the selection

    # Question 2
    while not verifyInput(user_selection, 1, 2):
        try:
            user_selection = int(input(question_list[1]))
        except:
            continue

        twoOptionInput(user_selection, total_points, 2)  # Question with a weight of 2
    user_selection = -1

    # Question 3
    while not verifyInput(user_selection, 1, 5):
        try:
            user_selection = int(input(question_list[2]))
        except:
            continue

        multipleOptionInput(user_selection, total_points, 1)  # Question with a weight of 1

    if total_points <= 11:
        print("Pro")
        # TODO add attribute of pro player
    elif total_points <= 5:
        print("Casual")
        # TODO add attribute of casual player
    else:
        print("New in the game")
        # TODO add attribute of new player




def fightStyle(question_list: list):
    user_input = -1
    point_total = 0
    weight = 5
    index = 0
    while not verifyInput(user_input, 1, 3):
        try:
            user_input = int(input(question_list[index]))
        except Exception:
            continue

        multipleOptionInput(user_input, point_total, weight)
        index += 1
    question_list[0]


def verifyInput(user_input: int, minimum: int, maximum: int):
    if minimum <= user_input <= maximum:
        return True
    else:
        return False


def twoOptionInput(user_input: int, point_total: int, weight: int):
    if user_input == 1:
        point_total += (1 * weight)


def multipleOptionInput(user_input: int, point_total: int, weight: int):
    point_total += (user_input * weight)
