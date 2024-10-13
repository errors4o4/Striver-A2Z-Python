s = "defdefdefabcabc"
goal = "defdefabcabcdef"


def rotateString(s, goal):
  return len(s) == len(goal) and s in goal + goal



def rotateStrings(s, goal) :
    for i in range(len(goal)):
        if s[i] == goal[0]:
            if s[i:] + s[:i] == goal:
                return True
      
    return False




    
print(rotateString(s, goal))