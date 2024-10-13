s = "paper"
t = "title"


def isIsomorphic(s, t):
  mapST, mapTS = {}, {}
  
  for i in range(len(s)):
    # cs = s[i]
    # ct = t[i]
    
    if (s[i] in mapST and mapST[s[i]] != t[i]) or (t[i] in mapTS and mapTS[t[i]] != s[i]):
      return False
      
    mapST[s[i]] = t[i] 
    mapTS[t[i]] = s[i] 
    
  return True
            

print(isIsomorphic(s, t))