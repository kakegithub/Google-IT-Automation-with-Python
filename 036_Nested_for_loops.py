for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
###############################################################################
teams = ["Dragons", "Wolves", "Pandas", "Unicorns"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)
###################################################################################
""" for element in long_list:
    do_something(element)

for element1 in long_list:
    for element2 in long_list:
        do_something(element1, element2)"""
#######################################################################################
estudiantes = {
    "grupo_a": ["Ana", "Juan", "Luis"],
    "grupo_b": ["Sofia", "Pablo", "Carmen"],
}

for grupo, nombres in estudiantes.items():
    print(f"Estudiantes del {grupo}:")
    for nombre in nombres:
        print(f"- {nombre}")
#########################################################################################3
# This code demonstrates the outer and inner loop iterations of a pair
# of nested for loops. Click "Run" to see the results. The outer loop
# will run twice for the range pointer positions [0, 1] in range(2).
# The inner loop will run 4 times for the range pointer positions
# [0, 1, 2, 3] in range(3+1) or range(4) each time the outer loop runs.
# So, the inner loop will execute 8 times in total.

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3 + 1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")
############################################################################################3
