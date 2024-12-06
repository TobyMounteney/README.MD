file = open('namesandgrades.txt', x)

file.write("Paul\n Computing, 50, 25.\n Networking, 60, 25 \n Dissertation, 70, 50")
with open("namesandgrades.txt", "a") as f:
  print("Paul, 75, Merit ", file=f)
  file.write(computinggrade)

file.close()
