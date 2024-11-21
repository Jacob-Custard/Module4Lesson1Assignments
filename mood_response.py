def reply(emotion):                                                                                                      #defining a function
    if emotion.lower() == "happy":                                                                                       #series of 'if', 'elif' blocks deciding the user's input and providing a response based off that input
        return "That's wonderful, I hope you keep feeling that way!"
    elif emotion.lower() == "sad":
        return "I'm sorry to hear that, I hope you cheer up soon."
    elif emotion.lower() == "scared":
        return "Take heart, one cannot find courage without first finding fear."
    elif emotion.lower() == "angry":
        return "BLOOD FOR THE BLOOD GOD, SKULLS FOR THE SKULL THRONE!!!"
    else:
        return "I don't know that emotion, im just a machine after all."