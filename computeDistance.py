#computeDistance between two points
#Enter the first point
x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))
#Enter the second point
x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))
#Compute Distance
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print("The distance between the two points is: ", distance)
