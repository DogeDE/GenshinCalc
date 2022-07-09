pulls = 0
dailyprimo = 0

while True:
    daysuntilbanner = input(
        "How many days until the wanted characters' Banner?\n")
    if daysuntilbanner.isdigit() == False:
        print("Please input a number.")
        continue

    bannerincl = input(
        "Do you want to include the time of the characters' banner? (y/n)\n")[0]
    if bannerincl == 'y' or bannerincl == 'Y':
        bannerincl = True
    elif bannerincl == 'n' or bannerincl == 'N':
        bannerincl = False
    else:
        print("Please type 'y' or 'n'")
        continue

    welkin = input(
        "Have you bought the Blessing of the Welkin Moon? (y/n)\n")[0]
    if welkin == 'y' or welkin == 'Y':
        welkin = True
    elif welkin == 'n' or welkin == 'N':
        welkin = False
    else:
        print("Please type 'y' or 'n'")
        continue

    battlepass = input("Have you bought the Battle Pass? (y/n)\n")[0]
    if battlepass == 'y' or battlepass == 'Y':
        battlepass = True
    elif battlepass == 'n' or battlepass == 'N':
        battlepass = False
    else:
        print("Please type 'y' or 'n'")
        continue

    stardust = input(
        "Include the 5 monthly stardust pulls? (y/n)\n")[0]
    if stardust == 'y' or stardust == 'Y':
        stardust = True
    elif stardust == 'n' or stardust == 'N':
        stardust = False
    else:
        print("Please type 'y' or 'n'")
        continue
    break


dub = int(daysuntilbanner)

if welkin:
    dailyprimo = 150
else:
    dailyprimo = 60
if bannerincl:
    dub += 20
if battlepass:
    pulls += 8
if stardust:
    if dub < 31:
        pulls += 5
    else:
        dustProMonat = 5 * ((dub // 30) + 1)
        pulls += dustProMonat

result = str((dailyprimo * dub)/160 + pulls)

if bannerincl:
    print("You'll have " + result + " pulls at the end of the characters' banner.")
else:
    print("You'll have " + result + " pulls when the banner starts.")

input()
