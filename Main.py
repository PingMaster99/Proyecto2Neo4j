import GenerateDatabase as database
from Questionaire import getAnswers, recommendationQuestions
# Deletes previous database versions if present
database.delete()
# Generates the initial database
database.generateDatabase()
# Gets the user preferences
user_preferences = getAnswers(recommendationQuestions)
