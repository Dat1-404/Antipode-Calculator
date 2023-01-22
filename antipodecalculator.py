running = True

while running == True :
   ifinput1 = True
   while ifinput1 == True: 
      coordinate1 = str(input("Enter your coordinate: \n"))
      if ", " in coordinate1 :
         coordinate1list = coordinate1.split(", ")
      else :
         coordinate1list = coordinate1.split(",")
      lat1 = coordinate1list[0]
      long1 = coordinate1list[1]
      linkog = "https://www.google.com/maps/search/" + coordinate1.replace(" ","")
      input1 = str(input("This is your selected coordinate: " + coordinate1 + "\n This is the location of those coordinates: "+linkog+"\n Is that correct? (say yes to continue, no to restart, any other answer will also make the program restart)\n"))
      if input1 == "yes" or input1 == "y" :
         ifinput1 = False
      elif input1 == "no" or input1 == "n" :
         ifinput1 =True
      else :
         print('Not a valid option. Please enter "yes" or "y" for yes or "no" or "n" for no.')

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
   ifinput2 = True
   while ifinput2 == True :
      checkclose = str(input("Would you like to calculate the antipode of another coordinate? Say yes or no."))
      
      if checkclose == "yes" or checkclose == "y" :
         ifinput2 = False
      elif checkclose == "no" or checkclose == "n" :
         running = False
         ifinput2 = False
      else :
         print('Not a valid option. Please enter "yes" or "y" for yes or "no" or "n" for no.')
