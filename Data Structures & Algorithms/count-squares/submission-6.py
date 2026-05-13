class CountSquares:

    def __init__(self):
        self.countPoints = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.countPoints[tuple(point)] += 1
        self.points.append(point) 
        print(self.countPoints[tuple(point)])
        print(self.points)

    def count(self, point: List[int]) -> int:
        qx, qy = point[0], point[1]

        res = 0
        for x, y in self.points:
            if abs(qy - y) == abs(qx - x) and qx != x:
                point1, point2 = (x, qy), (qx, y)

                res += self.countPoints[(point1)] * self.countPoints[(point2)]

        return res
        
