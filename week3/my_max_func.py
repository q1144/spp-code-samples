
values_l = []
is_running = True

while (is_running == True):
    
    inp = input ("Type your sequence one by one, 'done' to stop input:")

    if inp != 'done':       
        try:
            clear_inp = float(inp)
        except:
            print ("Wrong input '%s'! Should be a numerical value string!" % (inp))                    
        values_l += [clear_inp]
    else:
        # find max value
        Result = None
        i = 0

        while i < len(values_l):
            if i ==0:
                max_v = values_l[0]
            if values_l[i] > max_v:
                max_v = values_l[i]
            i += 1                            
        
        Reslut = max_v

        print ('%s is a maximum value of list %s ' % (Reslut, values_l))    
        response  = input("Enter 'y' to process another sequence or 'n' to quit? -->")

        if response =='y':
            is_running = True
            values_l = []
        elif response =='n':
            is_running = False
else:
    print('Bye-bye, see you next time! :-)')