class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # If there are no attacks at all, return 0
        if not timeSeries:
            return 0
            
        total_time = 0
        
        # Look at each attack except the last one
        for i in range(len(timeSeries) - 1):
            current = timeSeries[i]      # When current attack happens
            next_attack = timeSeries[i + 1]  # When next attack happens
            
            # Check if poison from current attack is still active when next attack happens
            if next_attack < current + duration:
                # If yes, count only until next attack
                poison_time = next_attack - current
            else:
                # If no, count full duration
                poison_time = duration
                
            total_time += poison_time
        
        # Add the last attack's full duration
        total_time += duration
        
        return total_time

