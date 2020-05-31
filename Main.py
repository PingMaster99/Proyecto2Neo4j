import GenerateDatabase as database
import Recommender as recommender
from Questionaire import getAnswers, recommendationQuestions

# Prints welcome message, instructions, and ASCII art
print("**************************************************************************\n"
      "            Recomendador de main de Super Smash Bros Ultimate "
      "\n**************************************************************************\n Joonho Kim 18096\n"
      " Alejandro Álvarez 12429\n Pablo Ruiz 18259\n\n Instrucciones: \n Responda a las siguientes preguntas"
      " introduciendo el número en paréntesis de la opción que quiera seleccionar.\n Al terminar de responder, obtendrá"
      " recomendaciones según sus preferencias.\n Disfrute de un ASCII art mientras carga el programa: \n \nUUUUUUUU   "
      "  UUUUUUUUVVVVVVVV "
      "          VVVVVVVV      GGGGGGGGGGGGG\nU::::::U     U::::::UV::::::V           V::::::V   "
      "GGG::::::::::::G\nU::::::U     U::::::UV::::::V           V::::::V GG:::::::::::::::G\nUU:::::U     "
      "U:::::UUV::::::V           V::::::VG:::::GGGGGGGG::::G\n U:::::U     U:::::U  V:::::V           V:::::VG:::::G "
      "      GGGGGG\n U:::::D     D:::::U   V:::::V         V:::::VG:::::G              \n U:::::D     D:::::U    "
      "V:::::V       V:::::V G:::::G              \n U:::::D     D:::::U     V:::::V     V:::::V  G:::::G    "
      "GGGGGGGGGG\n U:::::D     D:::::U      V:::::V   V:::::V   G:::::G    G::::::::G\n U:::::D     D:::::U       "
      "V:::::V V:::::V    G:::::G    GGGGG::::G\n U:::::D     D:::::U        V:::::V:::::V     G:::::G        "
      "G::::G\n U::::::U   U::::::U         V:::::::::V       G:::::G       G::::G\n U:::::::UUU:::::::U          "
      "V:::::::V         G:::::GGGGGGGG::::G\n  UU:::::::::::::UU            V:::::V           GG:::::::::::::::G\n   "
      " UU:::::::::UU               V:::V              GGG::::::GGG:::G\n      UUUUUUUUU                  VVV         "
      "         GGGGGG   GGGG\n                    (Alejandro Alvarez, 2020)")
# Deletes previous database versions if present
database.delete()

# Generates the initial database
database.generateDatabase()

# Gets the user preferences
user_preferences = getAnswers(recommendationQuestions)

# Generates the user according to the preferences
database.generateUser(user_preferences)

# Top recommendation according to user preferences
recommender.mainRecommendation(user_preferences, database.matcher, user_preferences["experience"])

# Category recommendations
print("***************************************************\n          Recomendaciones por categoría\n"
      "***************************************************")

# Recommendation according to fight style
recommender.styleRecommendation(user_preferences, database.matcher)

# Recommendation according to play style
recommender.playStyleRecommendation(user_preferences, database.matcher)

# Recommendation according to tier
recommender.tierRecommendations(user_preferences, database.matcher)

# If player is casual or new, design and saga recommendations are shown according to their experience
if user_preferences["experience"] == "casual" or user_preferences["experience"] == "new":
    recommender.sagaRecommendation(user_preferences, database.matcher)
    if user_preferences["experience"] == "new":
        recommender.typeRecommendation(user_preferences, database.matcher)

# Program ending
input("Presione enter para salir")
print("Gracias por utilizar el sistema de recomendacion de Smash Bros Ultimate :D")
