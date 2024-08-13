class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lowestCharInList = []
        flag = True
        itsTrue = []
        result = ""
        # for i in range(len(strs)):
        #     print(strs[i][i+2:i])
        #     print(strs[i][i+3:i])
        #     print()
        #     lowestCharInList.append(len(strs[i]))
            
        #     #if strs[i][0:i] == strs[i+1][0:i] == strs[i+2][0:i]:
        # print(min(lowestCharInList))
        # print(lowestCharInList.sort())
        # print(lowestCharInList)
        # indexToIterate = lowestCharInList.index(min(lowestCharInList))
        # maxToiterate = min(lowestCharInList)
         
        for i in range(len(strs)):
            try:
                if strs[i] == "":
                    return ""
                #print(strs[indexToIterate])
                if strs[0][0:1] == strs[i][0:2]:
                    print(strs[i][0:2])
                    result = strs[0][0:1]
                    
                    itsTrue.append("yes")                                    
                elif strs[1][0:2] == strs[i][0:2]:
                    result = strs[1][0:2]
                    itsTrue.append("yes")
                elif strs[0][0:2] == strs[i][0:2]:
                    print(strs[i][0:2])
                    result = strs[0][0:2]
                    
                    itsTrue.append("yes")
                else:
                    itsTrue.append("no")
            except:
                print("some error")        
        if len(strs[0]) == 1:
            return strs[0]
        elif len(set(itsTrue)) == 1:
            return print(result, "res")
        else:
            return ""            
        print(flag)
            
            
strs = ["cir","car"]       
        
solution = Solution()
print("fuckeruckas")
solution.longestCommonPrefix(strs)