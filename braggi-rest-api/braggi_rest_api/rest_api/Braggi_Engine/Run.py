#%%

from rest_api.Braggi_Engine import Text_Processing_Engine
from rest_api.Braggi_Engine import Classifier

def Run_Model(user_in, Trained=True):
    if Trained == False:
        intents = Text_Processing_Engine.intents_loader()
        words, intent_classes, sentence_corpus = Text_Processing_Engine.intents_parser(intents)
        train_x, train_y = Text_Processing_Engine.init_training_data(words, intent_classes,sentence_corpus)
        model = Classifier.model(train_x, train_y)
        model = Classifier.model_train(model, train_x, train_y)
        Classifier.model_save(model, words, intent_classes, train_x, train_y)

        if user_in != 'admin-override-input=null':
            response = Classifier.response(model, intents, words, intent_classes, user_in)
            return response[0]

    else:
        intents = Text_Processing_Engine.intents_loader()
        words, intent_classes, train_x, train_y = Classifier.model_load()
        model = Classifier.model(train_x, train_y)
        model.load('./rest_api/Braggi_Engine/model.tflearn')

        response = Classifier.response(model, intents, words, intent_classes, user_in)
        return response[0]
