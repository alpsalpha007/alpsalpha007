#def cubedNumbs(numbs):
#    result = []
#    for i in numbs:
#        result.append(i*i*i)
#    return result 

#myNumbs = cubedNumbs([25, 44, 32, 65, 99])
#print(myNumbs)
#like this it will print  the following [15625, 85184, 32768, 274625, 970299] using lists 

#now we try again using generators

def cubedNumbs(numbs):
    for i in numbs:
        yield(i*i*i) #this key word yield is what makes it a generator
     

myNumbs = cubedNumbs([25, 44, 32, 65, 99])
print next (myNumbs)
