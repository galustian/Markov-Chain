import pickle
import sys
import nltk


def predict_word(pickle_name, word_list):
    transition_matrix = None
    input_ = ''
    
    # check if word occurs in matrix & set set transition_matrix and input_ (according to word_list length)
    if len(word_list) == 1:
        transition_matrix = pickle.load(open(pickle_name, 'rb'))
        input_ = word_list[0]
        if input_ not in transition_matrix: return 'No Suggestion'
    else:
        transition_matrix = pickle.load(open(pickle_name, 'rb'))
        input_ = ' '.join(word_list)
        if input_ not in transition_matrix: return 'No Suggestion'
    
    prediction = ''
    highest_freq = -1

    transition_words = transition_matrix[input_]
    
    for transition_word, frequency in transition_words.items():
        if frequency > highest_freq:
            highest_freq = frequency
            prediction = transition_word
    
    return prediction


if __name__ == '__main__':
    prediction = None
    words_list = nltk.word_tokenize(' '.join(sys.argv[1:]))

    if len(words_list) > 1:    
        prediction = predict_word('two-way-transition-matrix.p', words_list[-2:])
    elif len(words_list) == 1:
        prediction = predict_word('one-way-transition-matrix.p', words_list) # expects a list
    else:
        prediction = {}
    
    print(prediction)