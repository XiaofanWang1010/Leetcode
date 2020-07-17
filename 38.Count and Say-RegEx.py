# 38.Count and Say: RegEx, check if a string contains the specified search pattern. 
# Regular Expression, is a sequence of characters that forms a search pattern.
# (.): this is a group that contains any char
# \2: signal a special sequence, escape special characters
# *: zero or more occurrences

class Solution:
    def countAndSay(self, n:int) -> str:
        import re  # import re module, which can be used to work with RegEx
        currSeq = '1'   # txt 
        pattern = r'((.)\2*)'  # match from 0 to n repetitions of group2

        for i in range(n-1):
            nextSeq = []  # stack
            for g1, g2 in re.findall(pattern, currSeq):  # findall: return a list containing all matches

                # append the pair of <count, digit>
                nextSeq.append(str(len(g1)))
                nextSeq.append(g2)

                # prepare for the next iteration
            currSeq = ''.join(nextSeq)
        return currSeq 
                
