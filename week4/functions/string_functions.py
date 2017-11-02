''' rewrite string methods
 0-9 codes: 48 - 57
 A-Z: 65-90, a-z: 97-122, shift = 32 '''

from keyword import kwlist


def my_capitalize(s):   
    
    # check first symbol
    first_symbol = s[0]
    if ord (first_symbol) >= 97 and ord (first_symbol) <= 122:   # in range of 97-122, lower case
        result_string = chr(ord(first_symbol) - 32)  # capitalize frist symbol
    else:
        result_string = first_symbol

    for symbol in s[1:]:
        if ord(symbol) >= 65 and ord(symbol) <= 90:    # If symbol letter in upper case
            result_string += chr(ord(symbol) + 32)
        else:
            result_string += symbol
    
    return result_string


def my_center(s, lenght, pad =' '):
    
    if (lenght - len(s)) % 2 == 0:     
    # if string > length calculate negative pads, that will be converted to empty string 
    # so original string will be returned
        right_pad = pad * int ( (lenght - len(s)) / 2) 
        left_pad = right_pad
    else:
        right_pad = pad * int( (lenght - len(s) + 1) / 2)
        left_pad = pad * int( (lenght - len(s) - 1) / 2)

    return left_pad + s + right_pad


def my_ljust(s, lenght, pad =' '):
    
    right_pad = pad * int(lenght - len(s))
    return s + right_pad
  

def my_rjust(s, lenght, pad =' '):
    
    left_pad = pad * int(lenght - len(s))
    return left_pad + s


def my_count(s, substring):
    
    count = 0
    i = 0

    if len(substring) > len(s):
        return count

    while (i < len(s)):
        sample = s[i:i+len(substring)]
        i += 1
        if substring == sample:
            count += 1
    return count


def my_startswith(s, substring):

    if s[0:len(substring)] == substring:
        return True
    else:
        return False


def my_endswith(s, substring):

    if s[-len(substring):] == substring:
        return True
    else:
        return False


def my_find(s, substring):
    
    pos = -1
    i = 0
    while (i < len(s)):
        sample = s[i:i+len(substring)]      
        if substring == sample:
            pos = i
            break
        i += 1
    return pos


def my_rfind(s, substring):

    pos = -1
    i = len(s)
    while (i >= 0):
        sample = s[i:i+len(substring)]
        if substring == sample:
            pos = i
            break
        i -= 1
    return pos



def my_isalnum(s):

    for symbol in s:
        is_digit = ord(symbol) > 47 and  ord(symbol) < 58
        is_uppercase = ord(symbol) > 64 and  ord(symbol) < 91
        is_lowercase = ord(symbol) > 96 and  ord(symbol) < 123

        is_alnum = is_digit or is_uppercase or is_lowercase

        if is_alnum == False:
            break

    return is_alnum


def my_isalpha(s):

    for symbol in s:
        is_uppercase = ord(symbol) > 64 and  ord(symbol) < 91
        is_lowercase = ord(symbol) > 96 and  ord(symbol) < 123
        is_alpha = is_uppercase or is_lowercase

        if is_alpha == False:
            break

    return is_alpha


def my_isdigit(s):

    for symbol in s:
        is_digit = ord(symbol) > 47 and  ord(symbol) < 58
        
        if is_digit == False:
            break

    return is_digit


def my_islower(s):

    for symbol in s:        
        is_uppercase = ord(symbol) > 64 and  ord(symbol) < 91
        is_lower = not is_uppercase

        if is_lower == False:
            break
    return is_lower

def my_isupper(s):

    for symbol in s:        
        is_lowercase = ord(symbol) > 96 and  ord(symbol) < 123
        is_upper = not is_lowercase

        if is_upper == False:
            break
    return is_upper


def my_lower(s):
    result_string = ''
    for symbol in s:
        if ord (symbol) > 64 and ord (symbol) < 91:
            result_string += chr(ord(symbol) + 32)
        else:
            result_string += symbol
    return result_string



def my_upper(s):
    result_string = ''
    for symbol in s:    
        if ord(symbol) > 96 and  ord(symbol) < 123:
            result_string += chr(ord(symbol) - 32)
        else:
            result_string += symbol
    return result_string


def my_join(sequence, sep = ' '):
    result_string = ''
    i =0
    
    while (i < len(sequence)):
        if i != len(sequence)-1:
            result_string += sequence[i] + sep
        else:
            result_string += sequence[i]
        i += 1
    return result_string


def my_istitle (s):

    separator_list = []
    words_list = []
    separator_indexies = [0]
    
    for symbol in s: # init separators list
        is_uppercase = ord(symbol) > 64 and  ord(symbol) < 91
        is_lowercase = ord(symbol) > 96 and  ord(symbol) < 123
        is_letter = is_uppercase or is_lowercase
        
        if not is_letter and symbol not in separator_list:
            separator_list.append(symbol)

    print (separator_list)
    i = 0  
    # find separators
    while (i < len(s)):
        if s[i] in separator_list:
            separator_indexies.append(i)
        i += 1

    if len (separator_indexies) > 1:
        separator_indexies.append(len(s)-1)  
        j = 0

        # initialize words list
        while (j < len(separator_indexies)-1):  # -1 to make sure, that j+1 is in list

            if j == 0:
                l_index = separator_indexies[j]
                r_index = separator_indexies[j+1]
            elif  j == len(separator_indexies) - 2: # last separator in the list
                l_index = separator_indexies[j] + 1
                r_index = separator_indexies[j+1] +1
            else:
                l_index = separator_indexies[j]+1
                r_index = separator_indexies[j+1]
            word = s[l_index:r_index]
        
            if len(word) > 0:
                words_list.append(word)
            j += 1
    else:
        words_list.append(s) #single word string

    print('words', words_list)
    
    for word in words_list: # check words first letter and tale
        first_l = word[0]
        w_tale = word[1:]
        first_l_is_title = False
        tale_is_not_title = True
        
        if  ord(first_l) > 64 and  ord(first_l) < 91:
            first_l_is_title = True        

        for letter in w_tale:
            if not (ord(letter) > 64 and  ord(letter) < 91):
                tale_is_not_title = True
            else:
                tale_is_not_title = False
                break

        if first_l_is_title  and tale_is_not_title == True:
            word_is_title = True
        else:
            word_is_title = False
            break                
                      
    return word_is_title
        

def my_split(s, sep = ' '):
       
    words_list = []

    i = 0
    prev_ind, next_ind = 0, 0
        
    while(i < len(s)):

        if s[i] == sep:

            if sep in s[i+1: ]:

                next_ind = i
                word = s[prev_ind : next_ind]
                
                if len(word) > 0:
                    words_list.append (word)
                
                prev_ind = next_ind +1
            
            else:
                last_sep_ind = i
                word_before_last = s[prev_ind : last_sep_ind] 
                last_word = s[last_sep_ind + 1: ]

                if len(word_before_last) > 0:
                    words_list.append(word_before_last)
                if len(last_word) > 0:
                    words_list.append(last_word)
                break
        i += 1

    return words_list

            
def my_isidentifier(s):
    
    flag_not_identifier = 0

    if  my_isdigit(s[0]) :
        flag_not_identifier +=1

    for symbol in s: # isalnum + underscore

        is_digit = ord(symbol) > 47 and  ord(symbol) < 58
        is_uppercase = ord(symbol) > 64 and  ord(symbol) < 91
        is_lowercase = ord(symbol) > 96 and  ord(symbol) < 123
        is_underscore = ord(symbol) == 95

        is_all_correct = is_digit or is_uppercase or is_lowercase or is_underscore

        if is_all_correct == False:
            flag_not_identifier += 1
            break

    if s in kwlist:
        flag_not_identifier += 1 # check not keyword

    if flag_not_identifier == 0: # result check
        return True
    else:
        return False


def my_replace (s, substring, replace_string):

    result_string = ''
    marked_list = []
    i = 0

    while (i < len(s)):
        sample = s[i:i+len(substring)]

        if substring == sample:

            marked_list.append(s[i:i+len(substring)])
            i += len(substring) 

        else:
            if len (marked_list) > 0 and marked_list[-1] != substring: # add string sample with no replace substrings as list element
                no_replace_sample = str(marked_list[-1]) + s[i]
                marked_list[-1]  = no_replace_sample                
            else:
                marked_list.append(s[i]) # append first char if not substring
            
            i += 1

    for elem in marked_list:
        if elem != substring:
            result_string += elem
        else:
            result_string += replace_string

    return result_string


def my_swapcase(s):

    result_string =''

    for symbol in s:
        if ord (symbol) > 64 and ord (symbol) < 91: # uppercase
            result_string += chr(ord(symbol) + 32) # turn upperswitch to lower
        elif ord(symbol) > 96 and ord(symbol) < 123:
            result_string += chr(ord(symbol) - 32)  # turn lower to upper
        else:
            result_string += symbol
    
    return result_string


#  --------- Call functionts section
s = input ("Type your string or 'Enter' to use default one:\n")

if len(s) < 1: # set default string
    s = 'hello world'

# print ('My capitalize:', my_capitalize(s))
# print ('My center:', my_center(s, 41, '-') )
# print ('My ljust:', my_ljust(s, 15, '-') )
# print ('My ljust:', my_rjust(s, 15, '-') )
# print ('My count:', my_count(s, 'hell') )
# print ('My my_startswith:', my_startswith(s, 'hell') )
# print ('My my_endswith:', my_endswith(s, ' world') )
# print ('My my_find:', my_find(s, 'd'))
# print ('My my_rfind:', my_rfind(s, 'w'))
# print ('my_isalnum:', my_isalnum(s))
# print ('my_isalpha:', my_isalpha(s))
# print ('my_isdigit:', my_isdigit(s))
# print ('my_islower:', my_islower(s))
# print ('my_isupper:', my_isupper(s))
# print ('my_lower:', my_lower(s))
# print ('my_upper:', my_upper(s))
# d = ['a', 'b', 'cc', '22'] ; print ('my_join:', my_join(d, '--'))
# print ('my_istitle:', my_istitle(s))
# print ('my_split:', my_split(s, '-'))
# print ('my_isidentifier:', my_isidentifier(s))
# print ('my_isidentifier:', my_isidentifier(s))
# print ('my_replace', my_replace(s, 'l', '(:_:)'))
# print ('my_swapcase:', my_swapcase(s))
