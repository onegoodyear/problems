def numberOfBoomerangs(points: [[int]]) -> int:
    distances = {}
    result = 0
    for root in points:
        for point in points:
            distance = (root[0]-point[0]) ** 2 + (root[1] - point[1]) ** 2
            if distance in distances:
                distances[distance] += 1
                result += distances[distance] * 2
            else:
                distances[distance] = 1
                result += 2
        distances = {}
    return result


print(numberOfBoomerangs([[1,1],[2,2],[3,3]]))