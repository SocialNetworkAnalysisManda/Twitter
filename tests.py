def happy_or_sad(x):
    total_happy = 0
    for k in range(x):
        result_dict = {k : 1}
        num = str(k)
        iterations = 0
        while True:
            result = 0
            for digit in num:
                result += int(digit)**2
            if result == 1:
                emotion = 'Happy'
                break
            if result in result_dict:
                emotion = 'Sad'
                break
            else:
                result_dict[result] = 1
                num = str(result)
            iterations += 1
        
        #print(k, 'is', emotion, 'after', iterations, 'iterations')
        if emotion == 'Happy':
            total_happy += 1
    
    return total_happy

for i in range(0,1000,40):
    print(i, end=": ")
    total = happy_or_sad(i)
    print(total*'x')