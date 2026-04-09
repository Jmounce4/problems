class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        
        obstaclesSet = set()
        for x, y in obstacles:
            obstaclesSet.add((x, y))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        current_place = (0, 0)
        max_distance = 0

        for command in commands:
            if command == -1:
                current_direction = (current_direction + 1) % 4
                continue

            if command == -2:
                current_direction = (current_direction + 3) % 4
                continue

            if command > 0:
                #moveTo = directions[current_direction] * command
                #print(moveTo)
                temp_place = current_place
                for step in range(command):
                    next_place = tuple(sum(pair) for pair in zip(temp_place, directions[current_direction]))
                    
                    if next_place not in obstaclesSet:
                        print('no obstacle')
                        temp_place = next_place
                        dist = temp_place[0]**2+temp_place[1]**2
                        max_distance = max(max_distance, dist)
                        print(temp_place)
                        
                    else:
                        #current_place = temp_place
                        break
                
                current_place = temp_place

        print(current_place[0])
        print(current_place[1])
        return max_distance
