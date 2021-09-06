import winsound

# sound helper functions
def play_wind():
    winsound.PlaySound("wind.wav", winsound.SND_ASYNC | winsound.SND_FILENAME)

def play_knock():
    winsound.PlaySound("knock.wav", winsound.SND_FILENAME)

def stop_sound():
    winsound.PlaySound(None, winsound.SND_ASYNC)


# diffrent game scenes
def scene_one(player_name):

    play_wind()
    print(f"""
    Hallo {player_name}
    Du stehst auf einer Wiese und vor dir ist ein einzelner, efeubewachsener Turm.
    Am Fusse des Turmes ist eine Türe. Etwas oberhalb findest du ein 
    geöffnetes Fenster. Um den Turm herum führt ein Weg, welcher zu 
    einem Wald führt.

    Was wirst du als nächstes tun?

    \tknock door - An der Türe klopfen
    \tclimb window - Durchs Fenster klettern
    \twalk around - Um den Turm herum laufen
    """)

    done = False
    
    while not done:
        user_input = input("> ")
        if user_input == 'knock door':
            stop_sound()
            scene_two()
            done = True
        elif user_input == 'climb window':
            stop_sound()
            scene_three()
            done = True
        elif user_input == 'walk around':
            stop_sound()
            scene_four()
            done = True
        else:
            print("""
            Du hast etwas falsch gemacht, versuchs nochmal!
            """)

def scene_two():
    print("Du gehst auf die Türe zu und klopfst dreimal.")
    play_knock()
    print("...")


def scene_three():
    print("""
    Du kletterst am Efeu hinauf zum Fenster.
    ...
    """)

def scene_four():
    print("""
    Langsam gehst du um den Turm herum.
    ...
    """)

def main():
    # ask user for name
    print('wie heisst du?')
    player_name = input("> ")

    # start game
    scene_one(player_name)


if __name__ == "__main__":
    main()
