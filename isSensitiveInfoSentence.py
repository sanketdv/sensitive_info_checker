def isSensitive(sentence):
    set = {'SECRET_KEY','SECRET_PASSWORD','SECRET_CVV',}
    all_words = sentence.split(" ")
    for word in all_words:
        if word in set:
            return True
    return False



def test_isSensitive():
    sensitive_sentence = open('sentence5.txt','r')
    for sentence in sensitive_sentence:
        assert(isSensitive(sentence))

