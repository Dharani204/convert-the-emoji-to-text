import random
#dictionary of emojis and their descriptions
emoji_dict ={
    "😀":"grinning face",
    "😃":"grinning face with big eyes",
    "😄":"grinning face with smiling eyes",
    "😁":"beaming face with smiling eyes",
    "😆":"grinning squinting face",
    "😅":"grinning face with sweat",
    "😂":"face with tears of joy",
    "🤣":"rolling on floor laudhing",
    "😎":"smiling face with sunglasses",
    "😍":"heart eyes",
    "😘":"face blowing a kiss",
    "😜":"winking face with tongue",
    "🤔":"thinking face",
    "😎":"cool face with sunglasses",
    "😢":"crying face",
    "😡":"pouting face",
    "🥺":"pleading face",
    "❤️":"red heart",
    "👍":"thumbs up",
    "🎉":"party popper",
    "🍕":"pizza",
    "🌟":"star",
    "🐶":"dog",
    "🚗":"car",
    "🔥":"fire",
}
#function to start the emoji to text game
def emoji_game():
    print("Welcome to the 'convert the Emoji to Text' Game!")
    print("In this game, you will be shown an emoji.Type the correct description to earn points.")
    print("Type 'quit' to exit the game.")
    print("-"*40)

    score=0 #keep track of the player's score
    emojis=list(emoji_dict.keys())

    while True:
        emoji=random.choice(emojis)
        print(f"Emoji: {emoji}")
        answer=input("Your Answer:").strip().lower()

        if answer=="quit":
            print(f"Game Over! Your Final Score: {score}")
            break

        if answer==emoji_dict[emoji]:
            print("Correct!🎉")
            score+=1
        else:
            print(f"Wrong! The correct answer is: '{emoji_dict[emoji]}'")

        print(f"Your Current Score: {score}") 
        print("-"*40)
    
#start the game
emoji_game()
    
    
   