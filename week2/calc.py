while (True):

    print('Set operands and operator to calculate value:')

    op1 = input('First value:')
    operator1 = input('First operator:')
    op2 = input('Second value:')
        
    if op1 == '':
        print('First value cannot be an empty string!')
    elif operator1 == '':
        print('Operator cannot be an empty string!')
    elif op2 == '':
        print('Second value cannot be an empty string!')
    else:
        try:
            op1 = float(op1)
        except ValueError:
            print("First value: '%s', not a correct number. Only positive/negative int or float values are allowed!" % (op1))
        try:
            op2 = float(op2)
        except ValueError:
            print("Second value: '%s', not a correct number. Only positive/negative int or float values are allowed!" % (op2))

        if operator1 == '+' or operator1 == '-' or operator1 == '*' or operator1 == '/' or operator1 == '**' or operator1 == '%':
            operator1_is_valid = True
        else:
            operator1_is_valid = False
            print(" Operation: '%s' , is not correct. Allowed operations: '+',  , '-', '*', '/', '**',  '%%'. " % (operator1))

        
        print ('Your expression:', op1, operator1, op2)

        if op2 == 0 and operator1 == '/':
            print ('You cannot divide by zero!');

        # Valuate expression

        Result = None

        if operator1_is_valid == True:

            elif operator1 == '+':
                Result = op1 + op2
            elif operator1 == '-':
                Result = op1 - op2
            elif operator1 == '*':
                Result = op1 * op2
            elif operator1 == '/':
                Result = op1 / op2        
            elif operator1 == '**':
                Result = op1 ** op2
            elif operator1 == '%':
                Result = op1 % op2        

        print('Result:', Result)
