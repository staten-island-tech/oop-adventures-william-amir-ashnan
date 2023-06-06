from game import main, Tutorial
answer=input("Do you want to play the Spider-Man game tutorial? yes/no")
if answer.lower() == "yes":
    print("Welcome to the tutorial, in this game you can attack, defend, or heal.")
    Tutorial()
    print("You have finished he tutorial which means now you can start the main game.")
    print("Welcome to Queens, you must protect the city and help all the citizens live in peace and harmony. As your journey continues, you will act as Spider-Man and will face villians from different stand points. Remember you have weapons and an occasional powerup to fight the villains. If your health is low, eat a slice of Joe’s pizza to regain health. Good Luck! The citizens of Queens are counting on you.")
    main()
if answer.lower() == "no":
    print("Welcome to Queens, you must protect the city and help all the citizens live in peace and harmony. As your journey continues, you will act as Spider-Man and will face villians from different stand points. Remember you have weapons and an occasional powerup to fight the villains. If your health is low, eat a slice of Joe’s pizza to regain health. Good Luck! The citizens of Queens are counting on you.")
    main()
