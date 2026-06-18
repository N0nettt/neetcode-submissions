class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for (p, s) in zip(position, speed)]
        cars.sort(key= lambda x: x[0], reverse=True)

        stack = []
        

        for i in range(0, len(cars)):
            position, speed = cars[i][0], cars[i][1]
            time = (target-position) / speed

            if not stack:
                stack.append(time)
            
            if stack and stack[-1] < time:
                stack.append(time)

        return len(stack)