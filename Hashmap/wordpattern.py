pattern = "abba"
s = "dog cat cat dog"

words = s.split()

if len(pattern) != len(words):
    print(False)
else:
    num1 = {}  
    num2 = {}  
    result = True

    for i in range(len(pattern)):  
        c1 = pattern[i]   
        c2 = words[i]     

        if c1 in num1 and num1[c1] != c2:  
            result = False
            break
        if c2 in num2 and num2[c2] != c1:  
            result = False
            break

        num1[c1] = c2  
        num2[c2] = c1  

    print(result)
