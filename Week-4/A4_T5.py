# Make a program, which prompts user to insert three integers:

#     Starting point
#     Stopping point
#     Inspection point

# Test the points with following rules(Note! testing order matters):

#     Starting point must be less than stopping point
#         "Starting point value must be less than the stopping point value."
#     The inspection point must be within the range of the start and stop points.
#         "Inspection value must be within the range of start and stop."

# If any rule above is broken, print the violation message(s) to the user and then skip the next part till the "Program ending." print.

# Run two for-loops like shown in the example program runs if none of the rules above are broken. Inside the loops, compare the inspection point to the current iteration. Use break and continue commands if the current iteration is same as the inspection point. Otherwise print the current iteration on the same line.

# Note! There must be no trailing space character at the end of any row.




# Program starting.
print("Program starting.")
print("")
# Insert starting point: 3
Feed = input("Insert starting point: ")
PointStart = int(Feed)
# Insert stopping point: 8
Feed = input("Insert stopping point: ")
PointStop = int(Feed)
# Insert inspection point: 5
Feed = input("Insert inspection point: ")
PointIns = int(Feed)
print("")

Run = True
if(PointStart >= PointStop):
    print("Starting point value must be less than the stopping point value.")
    Run = False
if((PointStart > PointIns) or (PointIns > PointStop)):
    print("Inspection value must be within the range of start and stop.")
    Run = False   
# First loop - inspection with break:
# Second loop - inspection with continue:
if(Run):
    print("First loop - inspection with break:")
    for i in range(PointStart, PointStop):
        if(i == PointIns):
            break
        if(i == PointStart):
            print(i, end='')
        else:
            print(f"-{i}", end='')

    print("")
    print("Second loop - inspection with continue:")
    for i in range(PointStart, PointStop):
        if(i == PointIns):
            continue
        else:
            if(i == (PointStop-1)):
                print(i)
            else:    
                print(i, end='-')

print("")
# Program ending.
print("Program ending.")