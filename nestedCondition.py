player_level = 25
has_premium = True
character_type = "warrior"

if player_level >= 20:
    if has_premium:
        if character_type == "mage":
            print("Unlock: Archmage class available")
        else:
            print("Unlock: Elite warrior class available")
    else:
        print("Premium membership required for advanced classes")
else:
    if has_premium:
        print("Level up to 20 for premium class options")
    else:
        print("Basic classes only - upgrade level and membership")