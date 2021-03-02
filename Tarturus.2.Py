import random
import time

def printAndSleep( theText, theTime ):
     print(theText)
     time.sleep(theTime)

def printIntro():
    global pName

    print("")
    printAndSleep("You step off a bus, hands cuffed together and youre wearing a bright orange jumpsuit",3)
    printAndSleep("Before you were 12 others and the Warden",2)
    printAndSleep("'Good Morning, welcome to my home.' he said",2)
    printAndSleep("'We're a family here, you're nothing but a pet'",2)
    printAndSleep("'If a dog hurt a family member, they'd get put down.'",3)
    printAndSleep("'And so do you'",2)
    printAndSleep("He continues for a moment before sending you to your cells",3)
    printAndSleep("As you dwell in your cell, you hear a whisper from the cell next to you.",3)
    printAndSleep("'What's your name kid.' He asks trying to lean his head through his bars",3)

    pName = input ("My name is: ")
    
    printAndSleep("'Well " + pName + ", you're gonna die in here...",3)
    printAndSleep("'Charming.' You say leaning closer to your bars",2)
    printAndSleep("...Unless you join me and my boys.'",2)
    printAndSleep("You think to yourself for a moment. He wasn't on the bus, meaning he has been here longer than you",4)
    printAndSleep("But there's no garuntee of safety, and he could just be desperate. You look back at him.",3)
    printAndSleep("'Im listening.'",1)
    printAndSleep("He giggles before saying that to get in with him, you'll have to kill a guard.",3)

def getPlayerChoice(  ):
    global pName
    choice = input("You have 3 options, to decline [D], accept [A], or talk back later [L] (Do Capitals)")
    if choice == 'D':
        printAndSleep("'I respect it. Good luck" + pName + ", You'll need it.'",3)
        goLeftA()
    elif choice == 'A':
        printAndSleep("'Welcome to the family " + pName ,2)
        goRightA()
    elif choice == 'L':
        printAndSleep("'I respect it, take as long as you need.. that is if you have that long.'",3)
        goBackA()
    else:
        printAndSleep("'English [Samuel L Jackson] do you speak it?! That's it, watch your back..",3)
        printAndSleep("Later that night he shanked you in the showers",2)
    
def goLeftA():
    global pName
    printAndSleep("You move back and dwell on the choice you had just made",3)
    printAndSleep("Everyone is then summoned to the yard for recreation",3)
    printAndSleep("You waltz around nervously. It feels like everywhere you look, there are eyes",4)
    printAndSleep("You bump into a hand full of prisoners playing rugbuy",3)
    printAndSleep("One guy just pummels his way through to the end goal",3)
    printAndSleep("Those behind them were left bloody and broken",2)
    printAndSleep("You get out of there before they invite you to play",3)
    printAndSleep("Those sitting in the shade are covered head to toe in tattoos",3)
    printAndSleep("Those against the gate wall are making deals with guards",3)
    printAndSleep("Then you feel a tap on your shoulder. You spin around in fear",3)
    printAndSleep("Its john. Oh no",1)
    printAndSleep("'Feels like highschool all over again doesn't it. Barry? uh Henry?",3)
    printAndSleep("'" + pName + "'",1)
    printAndSleep("'Thats it. Well, made an new friends son?'",2)
    printAndSleep("You stand quiet. Shaking in your boots",2)
    printAndSleep("'That's ashame. Let papa bear look after you for now'",3)
    printAndSleep("'I think I'm ok for now'",2)
    printAndSleep("'Sure thing pedro. I bet i'll be seeing you very soon tho'",3)
    printAndSleep("After the yard you run to a guard in private",3)
    printAndSleep("'I need to speak with the Warden. Now'",3)
    printAndSleep("Later on, you sit down with the warden",2)
    printAndSleep("'Good afternoon" + pName + ",what is it that you want'",3)
    printAndSleep("'Please! I need protection. I'm gonna die in here'",3)
    printAndSleep("'I can't help you with that. You're on your own'",3)
    printAndSleep("'Please, i'll do anything.'",2)
    printAndSleep("'There is something. But it's basically suicide'",3)
    printAndSleep("'So is being in here'",1)
    printAndSleep("'In that case I'll put you in genpop if you do something for me'",3)
    printAndSleep("'What is it?'",1)
    printAndSleep("'You know that guy next to your cell?'",2)
    printAndSleep("'Yeah..",1)
    printAndSleep("'Well he is responsible for basically all the drugs inside these walls'",3)
    printAndSleep("'You're gonna bring down his operation for me. Only then will you get your genpop cell'",2)
    choice = input("Do you team up with the Warden [W] or do you join the mystery man's gang[J] (Do Capitals)")
    if choice == 'W':
        goLeftB()
    elif choice == 'J':
        goLeftC()
    else:
        printAndSleep("'I do not speak your language of BS. Get him out of my sight will ya?'",2)
        printAndSleep("Later that night. 'John' came into your cell and shived you",1)
        printAndSleep("THE END")
    
def goLeftB():
    global pName
    printAndSleep("'Alright then. A deals a deal. You stop his operation and I get you your protection'",2)
    printAndSleep("You leave the Admin wing and talk to the mystery guy",2)
    printAndSleep("you walk over to the mystery guy and lie to him",2)
    printAndSleep("'I've made up my mind. I want to join your gang'",2)
    printAndSleep("'Ahhh nice to have you on board Petee.'",2)
    printAndSleep("'..I know I said you'd have to kill a piggy but I'm busy right now. So we'll hold tryouts tomorow'",3)
    printAndSleep("'Where are you going?' you ask",2)
    printAndSleep("'Ah I like your eagerness but I don't need anyone dead till tomorow. Don't worry, you're safe with us for the time being'",3)
    printAndSleep("'Wait but where are you going?'",1)
    printAndSleep("'You ask an annoyingly amount of questions Patrick. Don't worry Patricia, I'm just going to the toilet",3)
    printAndSleep("You tail him to the toilets without him knowing. You see him walk into the prison showers but not change clothes",3)
    printAndSleep("He pulls out a tile in the floor and fiddles around before filling the tile back up",2)
    printAndSleep("You hide away in a stall and make zero sounds",2)
    printAndSleep("You hear the bathroom doors open and close so you step out. You walk over to the tile and inside were kilos of methanphenamine",3)
    printAndSleep("You hear the bathroom doors open again and start to panick. You try closing the tile but 'John' already spots you",3)
    printAndSleep("'Oh patty. Now I know why you joined..",3)
    printAndSleep("'Don't worry I hide all my drugs in bathrooms. If i told you where then I'd have to kill you'",3)
    printAndSleep("'HAHA I'm not gonna kill you. I need you for something bigger. So lets make a deal",2)
    printAndSleep("'You stick with me and I'll pump you up with this stuff.. Deal?",2)
    printAndSleep("You have no other choice but to lie. 'Deal'",2)
    printAndSleep("'That's the spirit Phillip.' He then kicks the tile closed and walks you out of the bathroom.",2)
    printAndSleep("'Look Percy, I'm not gonna act like what you have to do is easy. It's not gonna be moral.. But it's gonna be fun. really really FUN",3)
    printAndSleep("A very large man runs around the corner, panicked shoutting 'BOSS! BOSS!'",2)
    printAndSleep("'What's wrong buddy?'",1)
    printAndSleep("'It's the Warden's, I think he's onto us. There's a guard in the Laundry Room'",2)
    printAndSleep("'Cheer up big man. That whole room just became a free fire zone' he says menacingly",2)
    printAndSleep("'Don't worry about him, I've planned for this. Our new friend here is up for the job'",2)
    printAndSleep("John looks at you with a harley smile but the 6'11 guy in front of you just glares down at you",3)
    printAndSleep("'He better be cause that one guard could screw this up' he says stomping back around the corner",2)
    printAndSleep("'HAHA I always loved the sound his footsteps make. Ok well hange of plans, you're killing a guard tomorrow not later'",3)
    printAndSleep("But who knows, time flies fast when you're having FUN. I have to go again sorry to disappoint'",2)
    printAndSleep("This is your chance to go to the Warden and tell him",2)
    printAndSleep("You sneak past any inmates and get to the Admin wing. You storm into the Warden's office",2)
    printAndSleep("'I know where it is. He keeps his stashes of meth in the prison showers. The ones i saw was underneath some tiles but there may be more'",3)
    printAndSleep("'Alright then snitch, a deals a deal. A guard will escort you to your new cell.'",2)
    printAndSleep("'Well done" + pName + "'",1)
    printAndSleep("You transfer cell and wait out the rest of your sentence in peace",3)
    printAndSleep("THE END",1)

def goLeftC():
    global pName
    printAndSleep("'No.. NO! People here hate snitches. I'm finding my own way to make it out alive'",2)
    printAndSleep("'Sure. Go right on ahead pal. I'l just start filling in the paper work for your death. Buh-bye now'",2)
    printAndSleep("You go back to the centre hold where you see the mystery man and his gang",2)
    printAndSleep("'H-hello.. um may I please join. I've changed my mind... sorry please dont kill me'",2)
    printAndSleep("Then an extremely large man, possibly  7 foot tall gets up and glares at you",2)
    printAndSleep("'Hey, hey, hey.. We're all friends here, right? No need for any bad blood'",2)
    printAndSleep("He pulls him back and lets you have a seat",1)
    printAndSleep("'Ok buddy. Let's talk business. The deal stays the same. You kill a guard, we let you in'",2)
    printAndSleep("'I'll do anything I swear'",1)
    printAndSleep("'Perfect, then its time to move up our schedule. Boys, follow me'",2)
    printAndSleep("Everyone steps up from the table and he leads you all outside the door to the laundry room",3)
    printAndSleep("'You see that guard? Go get him for me pretty please?'",2)
    printAndSleep("He hands you a shiv and pats you on the back as you walk inside",3)
    printAndSleep("You walk back out after fulfilling your end of the deal then everyone else walks inside",2)
    printAndSleep("'Good to have you on board buddy'",1)
    printAndSleep("Everyone starts removing a laundry machine to reveal a wide hole in the wall that they've made",3)
    printAndSleep("'Oh hey" + pName + ", Now might be a good time to mention that that guy has 2 kids and a dead wife...",3)
    printAndSleep("'Well i guess he had those things HAHAHAH what a knee slapper'",2)
    printAndSleep("'We didn't have to kill him though. Are you doing this for fun?!'",2)
    printAndSleep("'No not at all. This was just for fun though'",3)
    printAndSleep("He then stabs you and dumps your body with the guard while everyone else escapes via the hole",3)
    printAndSleep("'Au revoir' he says kissing you goodbye",3)
    printAndSleep("THE END",1)
          
def goRightA():
    global pName
    printAndSleep("You move back and dwell on the choice you had just made",1)
    printAndSleep("Some time passes and all the prisoners are summoned to the cafeteria",2)
    printAndSleep("But before you could grab your tray, a guard calls you to the Admin wing",2)
    printAndSleep("You enter a room and in front of you was the Warden",1)
    printAndSleep("'Please," + pName + ".Take a seat'",1)
    printAndSleep("'Look. I know why you're in prison. You were a snitch..",1)
    printAndSleep("'I need someone like that. Word is, that you're apart of John's gang, that true?'",3) 
    printAndSleep("'His name is John? Lame.' You say",1)
    printAndSleep("'Not quite.. He suffers from Antisocial Personality Disorder. He hits 7 out of 7 requirements..",2)
    printAndSleep("'1. Failure to fit with social norms, 2. Irritability, 3. Reckless disregard for safety'",3)
    printAndSleep("'4. Impulsivity, 5. Lack of remorse, 6. Consistent irresponibility'",2)
    printAndSleep("'And finally 7. Decietfulness'",2)
    printAndSleep("'He doesn't remember his name, there was no previous record of him, his fingerprints were burnt off.'",2)
    printAndSleep("'So what did he do to be here?' you ask",1)
    printAndSleep("'HA. What didn't he do to get here. Murder, Robbery, Armed assault...",2)
    printAndSleep("'If you help me, I'll put you in gen pop. No one will be able to touch you there.'",1)  
    choice = input("Do you betray 'John' [B] or do you stay loyal [L] (Do capitals)")
    if choice == 'B':
        print("'Alright then, do you need anything' he asks")
        printAndSleep("'Yeah, keep my Genpop cell nice and warm for me'",1)
        goRightB()
    elif choice == 'L':
        printAndSleep("'Do you know what you just did?'",1)
        printAndSleep("'You think you're safe but he'll leave you the moment he gets the chance'",1)
        goRightE()
    else:
        printAndSleep("'If that's all you have to say then you can get out'",1)
        printAndSleep("Later that night he shanked you in the showers",1)

def goRightB():
     printAndSleep("You step back into the cafeteria and you see 'John' waving at you",2)
     printAndSleep("You are stopped from sitting and 'John' gets up and walks to you",2)
     printAndSleep("'What were you doing coming out of the Admin Wing huh?' he asks, cletching his shiv",3)
     printAndSleep("You smack him with the tray and beat him him. Picking up his shiv holding it to his neck",4)
     choice = input("Do you kill 'John'[K] or do you spare him[S] (Captials plz)")
     if choice == 'K':
          goRightC()
     elif choice == 'S':
          goRightD()
     else:
         printAndSleep("You hesitated on making a choice and took too long. You were swiftly killed by 'John'",4)
         printAndSleep("THE END",1)
                    
def goRightC():
     printAndSleep("You get back up quickly ready to fight everyone... but no one gets up",3)
     printAndSleep("They all stare blankly, then someone in your gang starts chanting your name. Soon it's everyone",4)
     printAndSleep("A guard comes and detains you, bringing you to the Warden's office. Sits you down",3)
     printAndSleep("'So you actually pulled it off... well, theres a guard outside ready to escort you to genpop'",3)
     printAndSleep("'Yeah uh.. you can cancel that. I think i quite like it now'",3)
     printAndSleep("'What are you saying?'",1)
     printAndSleep("'I'm saying, that i am staying here and filling for 'John'",3)
     printAndSleep("'You're joking.. right?",1)
     printAndSleep("'Not at all Mr.Warden. You're looking at whose at the helm now'",3)
     printAndSleep("THE END")

def goRightD():
    printAndSleep("'You step back and run to your cell",2)
    printAndSleep("Soon after, a guard escorts you to the Admin WIng",2)
    printAndSleep("'A deals a deal sixer. Which you didn't fulfil.' the warden states",3)
    printAndSleep("'What?! He's in the infirmary. What more do you want?'",3)
    printAndSleep("'I 'wanted' you to give me something to work with'",2)
    printAndSleep("'He'll just recover and things go back to normal'",2)
    printAndSleep("Please! I'm begging you, i'll die out there' you plead",3)
    printAndSleep("'Yeah well... maybe he should've. Send him out please'",3)
    printAndSleep("A guard takes you back and in front of your cell was the gang waiting",3)
    printAndSleep("The guard pushes you into them and says 'Good luck'",2)
    printAndSleep("THE END",1)

def goRightE():
    printAndSleep("A guard removes you and takes you back to the cafeteria. 'John' waves at you from the corner of your eye",4)
    printAndSleep("'Pietro! Welcome back buddy. Come with me for our little expedition'",3)
    printAndSleep("He leads you to the laundry room and whispers to you",3)
    printAndSleep("'You see that guard in the corner there? Go make daddy proud'",3)
    printAndSleep("He hands you a shiv and slaps you in the butt as you walk towards him",3)
    printAndSleep("After bludgeoning the guard to death. He handshakes you and welcomes you to the gang",3)
    printAndSleep("He whistles out loud and the gang all walks in",2)
    printAndSleep("'Welcome to the party boys. Hey" + pName + ", help me with this please'",3)
    printAndSleep("You all remove a washing machine to reveal a large hole in the wall",3)
    printAndSleep("You and everyone else in your band of misfits all escape the stone walls of the prison",4)
    printAndSleep("THE END",1)

def goBackA():
    printAndSleep("You move and dwell on the choice you had just made",2)
    printAndSleep("Some time passes and all the prisoners are summoned to the cafeteria",3)
    printAndSleep("You line up to grab your food and you're shocked to see Gordan Ramsay filming his next kitchen nightmares episode in the prison",4)
    printAndSleep("You grab your tray and in the corner of your eye, you see a man waving to you",3)
    printAndSleep("It's the other prisoner from before. You sit down by his table nervously",3)
    printAndSleep("Beside you were 7 prisoners, all extremely large.",2)
    printAndSleep("'Gentlemen, gentlemen, relax. We don't need to act all scary to our friend here' the main guy said.",3)
    printAndSleep("'We just want you to feel comfartable, isn't that right boys?'",3)
    printAndSleep("The other's facial expressions to not change and nothing came out of their mouths",3)
    printAndSleep("You look around the cafeteria and barely any of the other fresh inmates are there",3)
    printAndSleep("'Oh are you looking for your bus buddies? They're in the infirmary..",3)
    printAndSleep("Some us, some not.. So what do you say, kid? Final chance, Yes? or no?",3)
    choice = input ("Do you say yes[Y] or no?[N]")
    if choice == 'Y':
        print("'Atta boy, we'll hold auditions in the morning. Just be a cutie for now'")
        goBackB()
    elif choice == 'N':
        printAndSleep("'Look kid, I don't like taking no for an answer.. And i did a lot not to kill you the first time, but that's it'",4)
        printAndSleep("You were slammed in the face with a tray and everyone at the table beat you to death",3)
        printAndSleep("THE END",1)
    else:
        printAndSleep("'English mother [Samuel L Jackson] do you speak it?! Screw it'",3)
        printAndSleep("You were slammed in the face with a tray and everyone at the table beat you to death",3)
        printAndSleep("THE END",1)

def goBackB():
    global pName

    printAndSleep("The next day John pulls you to laundry chamber",2)
    printAndSleep("'Time for tryouts my boy. You see that guard, give em' a big ol smile'",3)
    printAndSleep("You tackle the guard to the ground and push your blade against him",3)
    printAndSleep("'Oh hey kid? I think now might be a good time to tell you that he's has too kids and a dead wife'",4)
    printAndSleep("..Well, i guess he had those things.. haha oh well back to business'",3)
    printAndSleep("'Did good kid, now help me with this please'",2)
    printAndSleep("You and John push a washing machine aside and the rest of your gang starts digging at the wall behind",3)
    printAndSleep("'Good to have you on board" + pName + ". Please get rid of the pig, it's making a mess of the kitchen'",3)
    printAndSleep("You remove the body and see that a large hole has been made in the wall",3)
    printAndSleep("'Can't believe we getting out'",2)
    printAndSleep("'Yes WE, not You.' He then stabs you and pushes you down.",3)
    printAndSleep("You lay there watching everyone leave through the hole while you helplessly bleed out.",4)
    printAndSleep("THE END",1)


gameContinue = True
pName = None

while gameContinue == True:
    printIntro()
    getPlayerChoice()
    playAgain = input("[P] to play again")
    if playAgain != 'P':
        gameContinue = False
    else:
        print("Great, let's play again!")

input("[ENTER] to end.")