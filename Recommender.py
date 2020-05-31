from py2neo import NodeMatcher


def styleRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based on the player's like for a character type
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    style = "_.style=~ '{:s}'".format(user_preferences["fight_style"])
    equalStyles = list(matcher.match("Character").where(style))
    print("Por tu preferencia de personajes de tipo", user_preferences["fight_style"] + ",", "te recomendamos:")
    printRecommendation(equalStyles, 2)


def playStyleRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based on the player's way of playing/fighting
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    jumps = "_.jumps=~ '{:s}'".format(user_preferences["jump"])
    oos = "_.oos=~ '{:s}'".format(user_preferences["out_of_shield"])
    weight = "_.weight=~ '{:s}'".format(user_preferences["speed_and_weight"])
    equal_styles = list(matcher.match("Character").where(jumps).where(oos).where(weight))
    if len(equal_styles) > 0:
        print("Por tu estilo de juego, te recomendamos:")
        printRecommendation(equal_styles, 2)


def tierRecommendations(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based on the player's tier preference/alikes
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    tier = "_.tier=~ '{:s}'".format(str(user_preferences["tier"]))
    equal_styles = list(matcher.match("Character").where(tier))
    if len(equal_styles) > 0:
        print("Otros personajes de tier", str(user_preferences["tier"]), "que te podrian interesar:")
        printRecommendation(equal_styles, 2)


def sagaRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based on the player's favorite/preferred saga
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    saga = "_.saga=~ '{:s}'".format(str(user_preferences["saga"]))
    equal_styles = list(matcher.match("Character").where(saga))
    if len(equal_styles) > 0:
        print("Personajes la saga", str(user_preferences["saga"]), "que te podrian interesar:")
        printRecommendation(equal_styles, 2)


def typeRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based on the player's preference for a character design
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    style = "_.types=~ '{:s}'".format(user_preferences["character_type"])
    equal_styles = list(matcher.match("Character").where(style))
    if len(equal_styles) > 0:
        print("Personajes que podrian interesarte por su diseño: ")
        printRecommendation(equal_styles, 2)


def mainRecommendation(user_preferences: dict, matcher: NodeMatcher, playerExperience: str):
    """Calculates a recommendation based on the player's responses (when none matches an existing character)
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
        *playerExperience (str)
    Returns:
        **
    """
    print("***************************************************\n          Recomendaciones principales\n"
          "***************************************************")
    style = "_.style=~ '{:s}'".format(user_preferences["fight_style"])
    jumps = "_.jumps=~ '{:s}'".format(user_preferences["jump"])
    oos = "_.oos=~ '{:s}'".format(user_preferences["out_of_shield"])
    weight = "_.weight=~ '{:s}'".format(user_preferences["speed_and_weight"])
    fighter_type = "_.types=~ '{:s}'".format(str(user_preferences["character_type"]))
    saga = "_.saga=~ '{:s}'".format(str(user_preferences["saga"]))
    tier = "_.tier=~ '{:s}'".format(str(user_preferences["tier"]))

    equal_styles = ["No existe un personaje con esas caracteristicas, pero te recomendamos \n"
                   "ver las siguientes secciones para ver otras recomendaciones :D"]

    if playerExperience == "new":
        equal_styles = list(matcher.match("Character").where(style).where(jumps).where(oos).where(weight)
                           .where(fighter_type).where(tier).where(saga))
    if len(equal_styles) == 0 or playerExperience == "casual":
        equal_styles = list(matcher.match("Character").where(style).where(jumps).where(oos).where(weight).where(tier)
                           .where(fighter_type))
    if len(equal_styles) == 0 or playerExperience == "pro":
        equal_styles = list(matcher.match("Character").where(style).where(jumps).where(oos).where(weight).where(tier))
    if len(equal_styles) == 0:
        equal_styles = list(matcher.match("Character").where(style).where(jumps).where(oos).where(weight))
    if len(equal_styles) == 0:
        equal_styles = list(matcher.match("Character").where(style).where(oos).where(weight))
    if len(equal_styles) == 0:
        equal_styles = list(matcher.match("Character").where(style).where(weight))
    printRecommendation(equal_styles, 3)


def printRecommendation(recommendation_list: list, total_number: int):
    """Prints recommendation for a player based on preferences
    Args:
        *recommendation_list (list)
        *total_number (int)
    Returns:
        **
    """
    total = 0
    for character in recommendation_list:
        print("<<" + character["name"] + ">>", "Tier: " + character["tier"], "Tipo de pelea: " + character["style"])
        total += 1
        if total == total_number:
            break
    print()

