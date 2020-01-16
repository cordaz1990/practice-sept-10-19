def subtract(d1, d2):
    res = dict()
    for key in d1:
      if key not in d2:
        res[key] = None
     
    return res
  
  
  def has_duplicates(t):
      d = {}
      for x in t:
        if x in d:
          return True
        d[x] = True
        
      return False
