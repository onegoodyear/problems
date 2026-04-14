class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([[x,y] for x,y in zip(position, speed)])
        q = []
        for car in reversed(cars):
            if q and q[-1][1] < car[1]:
                if (car[0]-q[-1][0])/(q[-1][1]-car[1]) <= (target-q[-1][0])/q[-1][1]:
                    continue
            q.append(car)
        
        return len(q)