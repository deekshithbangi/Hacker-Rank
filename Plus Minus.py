def plusMinus(a):
    n = len(a) 
    positives,negatives,zeros = 0, 0,0
    for i in a:
        if i > 0:
            positives+=1
        elif i < 0:
            negatives +=1
        elif i == 0:
            zeros+=1
            
    print("{:.6f}".format(positives/n)) # either print("%.6f" % (positives/n))
    print("{:.6f}".format(negatives/n))
    print("{:.6f}".format(zeros/n))