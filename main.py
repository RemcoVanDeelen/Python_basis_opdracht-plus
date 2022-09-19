from random import randint
global p_tot, player, deck
# Foute inputs worden gelezen als "pas" of "nee"


def hit():                                 # definitie van kaarten pakken
    c_num = randint(0, len(deck)-1)
    card = deck[c_num]
    deck.pop(c_num)
    return card


def turn():                                # definitie van passen en meppen
    global p_tot
    if input("\nWil je een 'pas' of een 'mep'? \n>").lower() == "mep":
        player.append(hit())
        p_tot += player[len(player)-1]
        print("Je krijgt een {}. \n"
              "Je totaal is {}".format(player[len(player)-1], p_tot))
        if p_tot > 21:
            if input("\nHelaas, je totaal is meer dan 21. \n"
                     "Wil je nog een keer spelen (J/N)? \n>").lower() == "j":
                play()
            else:
                print("\nDankjewel voor het spelen van Zwarte Krik!")
                exit()

        turn()


def play():                                 # Het spel zelve
    global p_tot, player, deck
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
            2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    # --- Fase 1 ---
    # Player start:
    player = [hit(), hit()]
    p_tot = player[0] + player[1]
    print("\nWelkom bij Zwarte Krik!")

    print("\nJe krijgt een {} en een {}. \n"
          "Je totaal is {}.".format(player[0], player[1], p_tot))
    if p_tot > 21:                          # Waarom is er een 0,77% kans dat je verliest zonder iets te doen? .
        if input("\nHelaas, je totaal is meer dan 21. \n"
                 "Wil je nog een keer spelen (J/N)? \n>").lower() == "j":
            play()
        else:
            print("\nDankjewel voor het spelen van Zwarte Krik!")
            exit()

    # GM start:
    gm = [hit(), hit()]
    gm_tot = gm[0] + gm[1]
    print("\nDe spelleider heeft een {} en een gesloten kaart op tafel liggen. \n"
          "Het totaal is geheim.".format(gm[0]))

    # --- Fase 2 ---
    turn()

    # --- Fase 3 ---
    print("\nHet is nu de beurt van de spelleider. \n"
          "De verborgen kaart was een {}. \n"
          "Het totaal is {}".format(gm[1], gm_tot))

    while gm_tot < 15:                      # bij spelleder mep:
        gm.append(hit())
        gm_tot += gm[len(gm)-1]
        print("\nDe spelleider mept. \n"
              "Krijgt een {}. \n"
              "Het totaal is {}.".format(gm[len(gm)-1], gm_tot))

    if gm_tot > 21:                         # wanneer spelleider > 21:
        if input("\nGefeliciteerd! \n"
                 "Het totaal is meer dan 21.  Jij wint!\n"
                 "Wil je nog een keer spelen (J/N)? \n>").lower() == "j":
            play()
        else:
            print("\nDankjewel voor het spelen van Zwarte Krik!")
            exit()

    print("\nDe spelleider past.")           # spelleider past

    # --- Eind fase ---
    print("\nTotaal spelleider is {}. \n"
          "Jouw totaal is {}.".format(gm_tot, p_tot))
    if p_tot > gm_tot:
        print("Jij wint! Gefeliciteerd.")
    elif p_tot == gm_tot:
        print("Het is gelijk! De spelleider wint. Sorry.")
    else:
        print("De spelleider wint. Sorry.")

    if input("\nWil je nog een keer spelen (J/N)? \n>").lower() == "j":
        play()
    else:
        print("\nDankjewel voor het spelen van Zwarte Krik!")
        exit()


play()
