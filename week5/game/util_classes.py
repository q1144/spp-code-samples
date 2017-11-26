class SupTools():


    def check_int(inp_value):
        
        try:
            inp_value = int(float(inp_value))
        except ValueError:
            print('Value should be a number!')
            return False
        
        if inp_value >= 0:
            return True
        else:
            print('Value should be equal or greater than 0!')
            return False


    def set_army_qnt():

        inp_correct = False
        while(not inp_correct):
            total_army_qnt = input ('Set total quantity of your army! \nArmy total: ->')
            inp_correct = SupTools.check_int(total_army_qnt)
        else:
            total_army_qnt = int(float(total_army_qnt))

        return total_army_qnt