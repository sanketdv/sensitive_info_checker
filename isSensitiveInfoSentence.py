def isSensitive(sentence):
    set = {'SECRET_KEY','SECRET_PASSWORD','SECRET_CVV',}
    all_words = sentence.split(" ")
    for word in all_words:
        if word in set:
            return True
    return False
        


sensitive_sentence = open('path/to/your/file.txt','r')
for sentence in sensitive_sentence:
        result = isSensitive(sentence)
        if result == True:
            print(True)
        else:
             print(False)