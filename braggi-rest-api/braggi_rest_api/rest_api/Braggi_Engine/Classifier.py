#%%
import numpy as np
import tensorflow as tf
import tflearn
import random
import pickle
from rest_api.Braggi_Engine import Text_Processing_Engine

def model(train_x,train_y):
    '''Model Definition of a Deep Neural Network, which is responsible for the Classification.
    Input matrix size is set dynamically.
    '''
    net = tflearn.input_data(shape=[None, len(train_x[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
    net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

    model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')
    return model

def model_train(model, train_x, train_y):
    model.fit(train_x, train_y, n_epoch=1000, batch_size=8, show_metric=True)
    return model

def model_load():
    '''Load our model from an existing 'pickle'(.pkl) file.'''
    data = pickle.load( open( "./rest_api/Braggi_Engine/training_data", "rb" ) )
    words = data['words']
    intent_classes = data['classes']
    train_x = data['train_x']
    train_y = data['train_y']
    return words, intent_classes, train_x, train_y

def model_save(model, words, intent_classes, train_x, train_y):
    '''Save our trained model to a 'pickle'(.pkl) file.'''
    model.save('./rest_api/Braggi_Engine/model.tflearn')
    pickle.dump( {'words':words, 'classes':intent_classes, 'train_x':train_x, 'train_y':train_y}, open( "./rest_api/Braggi_Engine/training_data", "wb" ) )

def classify(model,sentence, words, intent_classes):
    ERRORR_THRESHOLD = 0.25
    results = model.predict([Text_Processing_Engine.bag_of_words(sentence, words)])[0]
    results = [[i,r] for i,r in enumerate(results) if r > ERRORR_THRESHOLD]
    results.sort(key=lambda x:x[1], reverse=True)
    return_list = []

    for r in results:
        return_list.append((intent_classes[r[0]], r[1]))
    
    return return_list

def response(model, intents, words, intents_classes, sentence, userID='default', debug=False):
    '''Using the Outputs from the Neural Network, construct the corresponding response from the "intents.json" file.'''
    context = {}
    results = classify(model, sentence, words, intents_classes)

    if results:
        while results:
            for i in intents['intents']:
                if i['tag'] == results[0][0]:
                    if 'context_state.set' in i:
                        if debug : print('context:', i['context_state.set'])
                        context[userID] = i['context_state.set']
                    
                    if not 'context_state.filter' in i or (userID in context and 'context_state.filter' in i and i['context_state.filter'] == context[userID]):
                        if debug: print ('tag:', i['tag'])
                        return random.choices(i['responses'])
            results.pop(0)
