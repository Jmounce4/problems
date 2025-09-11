class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (n + 1)  
        dp[1] = 1

        for day in range(1, n + 1):
            for share in range(day + delay, min(n + 1, day + forget)):
                dp[share] = (dp[share] + dp[day]) % MOD


        result = 0
        for day in range(n - forget + 1, n + 1):
            result = (result + dp[day]) % MOD

        return result
            


#Exceeds Time Limit, but solution that assigns individual people and their values!

secretDict = {}
        counter = 1
        total = 1
        secretDict[counter] = [delay, forget]
        for i in range(1, n+1):
            new_entries = {}
            removed = []
            for j in list(secretDict.keys()):


            
                if secretDict[j][1] == 0:
                    total-=1
                    removed.append(j)
                    continue

                if secretDict[j][0] <= 0:
                    counter+=1
                    total+=1
                    new_entries[counter] = [delay-1, forget-1]

                
                    

                secretDict[j][0] -= 1
                secretDict[j][1] -= 1
                    
                
            #for r in removed:
                #del secretDict[r]
            secretDict.update(new_entries)

        return (len(secretDict) - len(removed))
