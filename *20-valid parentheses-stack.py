class Solution:
    def isValid(self, s: str) -> bool:
        stack = []   # initialize a stack: From outside to inwards. Insert-push, Delete-pop
        mapping = {")": "(", "}": "{", "]": "["}  # hash map
        for char in s:
            if char not in mapping:  # if char is not an opening bracket
                stack.append(char)  # push char onto the stack
            else:
                top_element = stack.pop() if stack else '#'    # if stack: not empty
                if mapping[char] != top_element:
                    return False
        return not stack  # if the stack is empty, then have a valid expression



   

   
