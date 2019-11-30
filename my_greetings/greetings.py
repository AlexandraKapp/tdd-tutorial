def greet(person: "Person", daytime:str = None) -> str:
    language = person.nationality

    if language == "German":
        if daytime == "morning":
            return ("Guten Morgen, %s!" % (person.firstname))
        else:
            return ("Hallo, %s!" % (person.firstname))
