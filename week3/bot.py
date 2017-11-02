chat_session_is_running = True
q_and_a = {}

print ('Welcome!')

while (chat_session_is_running == True):   
    question = input (' Bot: Ask your question here, please \n You: --> ')
    
    try:
        answer_q =  q_and_a[question]
    except:
        answer_q = None
    
    if answer_q is None:
        print ('hmm.. ')
        user_answer = input ("Type your answer for '%s' question: \n You: --> " % (question))
        q_and_a[question] = user_answer
    else:
        print('Answer is: ', answer_q)

    inp_exit = input("Want to continue asking? print 'y' - yes, 'n' - quit \n You: -->")

    if inp_exit == 'y':
        chat_session_is_running = True
    if inp_exit == 'n':
        chat_session_is_running = False        