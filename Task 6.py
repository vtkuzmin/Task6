
# coding: utf-8

# In[14]:


import math

def main():
    # dictionary where the type is the key
    d = {}
    #  we will read the file line by line and update the dictionary
    with open("log.txt") as f:
        for line in f:
            a = line.rstrip().split(",")
            if a[1] in d:
                d[a[1]][0] += int(a[2])
                d[a[1]][1] += 1
            else:
                d[a[1]] = [int(a[2]), 1]
    
    # calculate the fraction and the confidence interval            
    for key in d:
        p = d[key][0]/d[key][1]
        inter = 1.96*math.sqrt(p*(1-p)/(d[key][1]))
        print "The fraction of mobile queries for", key, "is", p, "The 95% confidence interval: [", p-inter, ";", p+inter, "]"
        
    # calculate the statistics to test the hypothesis  
    k1 = d['/index'][0]
    n1 = d['/index'][1]
    k2 = d['/test'][0]
    n2 = d['/test'][1]
    w1 = k1/n1
    w2 = k2/n2
    p = (k1+k2)/(n1+n2)
    
    t = (w1-w2)/math.sqrt(p*(1-p)*(1/n1 + 1/n2))
    
    if abs(t) < 1.96:
        print "The hypothesis that the fractions are equal is not rejected as", abs(t), "< 1.96" 
    

if __name__ == '__main__':
    main()

