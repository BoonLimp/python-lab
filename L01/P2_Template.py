red = int(input("R Channel[0-255]: "))
green = int(input("G Channel[0-255]: "))
blue = int(input("B Channel[0-255]: "))
y = int(0.2126*red + 0.7152*green + 0.0722*blue)
print("Y = ", y )