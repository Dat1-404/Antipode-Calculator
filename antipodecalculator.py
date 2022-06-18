lat1 = input('Enter the LATITUDE of your coordinate:\n')
long1 = input('Enter the LONGTITUDE of your coordinate:\n')
coordinate1 = str(lat1) + ", " + str(long1)
linkog = "https://www.google.com/maps/search/" + coordinate1.replace(" ","")
input1 = input("This is your selected coordinate: " + coordinate1 + "\n This is the location of those coordinates: "+linkog+"\n Is that correct? (say yes to continue, no to restart, any other answer will also make the program restart)\n")

if (input1 == "yes"):
   if "-" in lat1:
    lat2 = float(lat1) * -2
    lat2 = float(lat1) + lat2
   else:
    lat2 = float(lat1) * 2
    lat2 = float(lat1) - lat2
   if "-" in long1:
    long2 = float(long1) * -2
    long2 = float(long1) + long2
    long2 = 180 - long2
   else:
    long2 = float(180) - float(long1)
    long2 = long2 * 2
    longde = long2
    long2 = float(180) - float(long1)
    long2 = long2 - longde
   coordinate2 = str(lat2) + ", " + str(long2)
   
   linkre = "https://www.google.com/maps/search/" + coordinate2.replace(" ","")
   print("Orginal coordinates: " + coordinate1 + "\n")
   print("Location of the original coordinates: "+linkog+"\n")
   print("Result coordinates: "+coordinate2+"\n")
   print("Location of the result coordinates: "+linkre+"\n")
   checkclose = input("Press enter to close")
    

else:
    import os
    os.system("python antipodecalculator.py")
    print("Restarting:\n")
    exit()
