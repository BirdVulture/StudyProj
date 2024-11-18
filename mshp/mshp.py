#урок1
s = input()
s = s.strip(" ")
s = s.lower()
s = s.replace("ну", "") 
s = s.replace("типо", "") 
s = s.replace("как бы", "")
print(s)



