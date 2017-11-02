values_l = []

while (True):
    
    inp = input ("Type your sequence one by one, 'done' to stop input: ")

    if inp != 'done':       
        values_l += [inp]
    else:
        # find len of sequense        
        print(values_l)  

        i = 0
        while (True):
            try:
                value = values_l[i]                
            except:
                # print('out of range')                
                print  ('Len of array: ', i)               
                break            
            i += 1
        
        q_inp = input("Wanna try once more? 'y'- yes, 'n' - no, quit --> ")

        if q_inp == 'y':
            values_l = []
            continue
        elif q_inp == 'n':    
            break
