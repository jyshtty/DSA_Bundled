class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        l = len(position)
        pair = [(p,s) for p,s in zip(position, speed)]

        # You must process cars from closest to target → farthest from target.
        pair.sort(reverse=True)

        time = (target - pair[0][0]) // pair[0][1]
        stack = [time]

        for i in range(1,l):
            time = (target - pair[i][0]) / pair[i][1]

            if stack[-1] < time:
                stack.append(time)
        
        return len(stack)


            
            
        