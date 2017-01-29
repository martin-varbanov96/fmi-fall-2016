max_weight=14

class element:
    def __init__(self,n="" w=0,v=0):
        name=n
        weight=w
        value=v


elements=list()
dirt=element("dirt",4,0)    
computer =element("computer",10,30) 
fork=element("fork",5,1)
problem_set=element("problem_set",0,-10)

# Fork - Weight: 5, Value: 1
# Problem Set - Weight: 0, Value: -10