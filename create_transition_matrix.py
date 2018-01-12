import glob
import nltk
import pickle

one_way_transition_matrix = {}
two_way_transition_matrix = {}

# updates the one_way matrix!
def update_one_way_matrix(article_words):
    global one_way_transition_matrix
    article_words_len = len(article_words)

    for i, word in enumerate(article_words):
        if i == article_words_len-1: break # last word has no next word
        next_word = article_words[i+1]
        
        if word not in one_way_transition_matrix:
            one_way_transition_matrix[word] = {}
            one_way_transition_matrix[word][next_word] = 1
        elif next_word not in one_way_transition_matrix[word]:
            one_way_transition_matrix[word][next_word] = 1
        else:
            one_way_transition_matrix[word][next_word] += 1

def update_two_way_matrix(article_words):
    global two_way_transition_matrix
    article_words_len = len(article_words)

    for i in range(0, article_words_len-2):
        two_words = ' '.join(article_words[i:i+2])
        next_word = article_words[i+2]

        if two_words not in two_way_transition_matrix:
            two_way_transition_matrix[two_words] = {}
            two_way_transition_matrix[two_words][next_word] = 1
        elif next_word not in two_way_transition_matrix[two_words]:
            two_way_transition_matrix[two_words][next_word] = 1
        else:
            two_way_transition_matrix[two_words][next_word] += 1



def create_matrix(file_names):
    # for every article
    for f_name in file_names:
        with open(f_name, 'r') as f:
            article_text = f.read()
        
        article_text = article_text.lower()
        article_words = nltk.word_tokenize(article_text)
        article_words = [word for word in article_words if word != ',']

        print("Update Two-Way-Matrix for Article:", f_name)
        update_two_way_matrix(article_words)
        
        print("Update One-Way-Matrix for Article:", f_name)
        update_one_way_matrix(article_words)


if __name__ == '__main__':
    file_names = glob.glob('wikipedia-articles/*.txt')
    create_matrix(file_names)
    pickle.dump(two_way_transition_matrix, open('two-way-transition-matrix.p', 'wb'))
    pickle.dump(one_way_transition_matrix, open('one-way-transition-matrix.p', 'wb'))