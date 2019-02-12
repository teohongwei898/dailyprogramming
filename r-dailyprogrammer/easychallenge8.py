def bottles(runs):
while runs >= 1:
    print (str(runs) + " bottles of beer on the wall, " + str(runs) + " bottles of beer..."),
    runs -= 1
    if runs == 1:
        break
    print (" You take one down, pass it around. " + str(runs) + " bottles of beer on the wall")
print (" You take one down, pass it around. " + str(runs) + " bottle of beer on the wall") 
bottles(input())
