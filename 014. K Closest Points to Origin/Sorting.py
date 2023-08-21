from math import sqrt


def kClosest(points, k):
        # Length of the list
        n = len(points)
        
        # For each point, calculate its distance with the origin
        for i in range(n):
            # X and Y value for current point
            x,y = points[i][0], points[i][1]
            
            # Distance from origin
            distance = sqrt(x**2 + y**2)
            
            # Update the list to include both the distance and the point
            points[i] = (distance, points[i])
            
        
        # Sort the list on the basis on distance
        points.sort()
        
        # And finally, return the first "k" values from this sorted list
        return [pair[1] for pair in points[:k]]


points = [[3,3],[5,-1],[-2,4]]
k = 2

print("Output -> ", kClosest(points,k))