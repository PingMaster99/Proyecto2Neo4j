recommendationQuestions = {
    "player_experience_questions": [
        "He jugado Super Smash Bros antes: \n (1) Si \n (2) No",
        "Tengo experiencia con videojuegos:\n (1) Si \n (2) No",
        "Considero que mi nivel en Super Smash Bros. es: \n (1) Jugador profesional \n (2) Soy bueno \n"
        " (3) Juego a veces \n (4) No soy tan bueno \n (5) A penas conozco el juego"],

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




def getAnswer(question_dictionary: dict, question_type: str):
    # Gets the answer and compounds it
    question_list = question_dictionary.get(question_type)
    if question_type.lower() == "player_experience_questions":
        playerExperience(question_list)
    elif question_type.lower() == "fight_style_questions":
        fightStyle(question_list)

    return 2

def playerExperience(question_list: list):
    question_list[0]

def fightStyle(question_list: list):
    question_list[0]

