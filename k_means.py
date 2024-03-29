from collections import defaultdict
from math import sqrt
from functools import cache
import seaborn as sns

"""
2 10
2 5
8 4
5 8
7 5
6 4 
1 2
4 9
"""

"""
1 2
5 8
2 10
"""
print("Enter the records: ")
records = [(5, 4), (7, 7), (1, 3), (8, 6), (4, 9)]
# while True:
#     record = tuple(map(int, input().split()))
#     if not record:
#         break
#     records.append(record)

clusters = defaultdict(list)
points = [(1, 3), (4, 9)] # [tuple(map(int, point.split())) for point in input("Enter initial points: ").split(',')]
k = len(points)

@cache
def distance(X, Y, measure='mn'):
    dist = 0
    for u,v in zip(X, Y):
        dist += abs(u-v) if measure == 'mn' else sqrt(u**2 + v**2)
    return dist

def get_clusters(clusters):
    clusters = defaultdict(list)
    for record in records:
        clusters[min(points, key=lambda point : distance(record, point))].append(record)
    return clusters

def get_points(clusters):
    new_points = []
    for cluster in clusters.values():
        res = [0]*len(cluster[0])
        for point in cluster:
            for i in range(len(point)):
                res[i] += point[i]
        new_points.append(tuple(i/len(cluster) for i in res))
    return new_points
    
    
while True:
    prev = tuple(clusters.values())
    clusters = get_clusters(clusters)
    if prev == tuple(clusters.values()):
        break
    points = get_points(clusters)    
    
for i,cluster in enumerate(clusters.values(), 1):
    print(f"cluster {i} -> {cluster}")

print(records)
X, Y = zip(*records)
sns.scatterplot(x=X, y=Y)

    
