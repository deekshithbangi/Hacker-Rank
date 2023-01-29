def countApplesAndOranges(s, t, a, b, apples, oranges):
    newapples, neworanges = 0,0
    
    for i in range(len(apples)):
        if apples[i]+a>=s and apples[i]+a<=t: 
            newapples+=1
    
    for i in range(len(oranges)):
        if oranges[i]+b>=s and oranges[i]+b<=t: 
            neworanges+=1
            
    print(newapples)
    print(neworanges)