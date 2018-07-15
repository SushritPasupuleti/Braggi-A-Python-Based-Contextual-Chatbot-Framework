#%%
import nltk
from nltk.stem.lancaster import LancasterStemmer
import json
import numpy as np
import random

stemmer = LancasterStemmer()

def intents_loader():
    '''Imports the Main "intents.json" File.'''
    #/braggi_rest_api/rest_api/Braggi_Engine/Intent_Models/intents.json
    with open('./rest_api/Braggi_Engine/Intent_Models/intents.json') as json_data:
        intents = json.load(json_data)
        return intents

def intents_parser(intents):
    '''Preprocess the "intents.json" file to prepare the dataset for training and analysis.'''
    words = []
    intent_classes = []
    sentences_corpus = []
    ignore_words = ['?','!']

    # loop through each sentence in our intents' patterns
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # tokenize the sentences
            word = nltk.word_tokenize(pattern)
            words.extend(word)
            sentences_corpus.append((word, intent['tag']))

            if intent['tag'] not in intent_classes:
                intent_classes.append(intent['tag'])

    # stem and lower each word from the word list 
    # remove duplicates
    words = [stemmer.stem(word.lower()) for word in words if word not in ignore_words]
    words = sorted(list(set(words)))
    intent_classes = sorted(list(set(intent_classes)))

    return words, intent_classes, sentences_corpus

def stem_sentence(sentence_corpus):
    '''Toeknize and Stem all the sentences'''
    sentence_words = nltk.word_tokenize(sentence_corpus)
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence_corpus, words, debug=False):
    '''Create the bag of words. A one hot coded input matrix.'''
    sentence_words = stem_sentence(sentence_corpus)
    bag = [0]*len(words)

    for s in sentence_words:
        for i,w in enumerate(words):
            if w==s:
                bag[i] = 1
                if debug:
                    print("found",w)

    return(np.array(bag))

def init_training_data(words, intent_classes, sentence_corpus):
    '''Initialize the training data for the Deep Neural Network'''
    training = []
    output = []
    output_empty = [0] * len(intent_classes)

    for doc in sentence_corpus:
        bag = []
        pattern_words = doc[0]
        pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
        for word in words:
            bag.append(1) if word in pattern_words else bag.append(0)

        output_row = list(output_empty)
        output_row[intent_classes.index(doc[1])] = 1
        
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training)

    train_x = list(training[:,0])
    train_y = list(training[:,1])
    return train_x, train_y
