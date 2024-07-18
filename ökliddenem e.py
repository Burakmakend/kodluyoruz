import math

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
def euclideanDistance(Nokta1, Nokta2):
    x1, y1 = Nokta1
    x2, y2 = Nokta2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

mesafe = [] 
for i in range(len(points)):
    
    for j in range(i+1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        mesafe.append(dist)
MinUzaklik = min(mesafe)
print("Minimum mesafe:", MinUzaklik)
print("Mesafeler: ", mesafe)
