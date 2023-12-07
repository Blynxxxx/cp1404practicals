COLOR_TO_CODE = {"Amber": "#ffbf00", "Apricot": "#fbceb1", "Aqua": "#00ffff", "Aquamarine1": "#7fffd4",
                 "Aquamarine2": "#76eec6", "Aquamarine4": "#458b74", "Army Green": "#4b5320", "Black": "#000000",
                 "Gray": "#bebebe", "Ginger": "#b06500"}

color = input("Input color: ")
while color != "":
    try:
        print(f"{color} code is {COLOR_TO_CODE[color]}")
    except KeyError:
        print("Invalid color")
    color = input("Input color: ")
