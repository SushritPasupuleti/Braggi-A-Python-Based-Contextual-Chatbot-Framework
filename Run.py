#%%
import Text_Processing_Engine
import Classifier

sentence = "hey man!"
Trained = True

if Trained == False:
    intents = Text_Processing_Engine.intents_loader()
    words, intent_classes, sentence_corpus = Text_Processing_Engine.intents_parser(intents)
    train_x, train_y = Text_Processing_Engine.init_training_data(words, intent_classes,sentence_corpus)
    model = Classifier.model(train_x, train_y)
    model = Classifier.model_train(model, train_x, train_y)
    Classifier.model_save(model, words, intent_classes, train_x, train_y)
    response = Classifier.response(model, intents, words, intent_classes, sentence)
    print(response)

else:
    intents = Text_Processing_Engine.intents_loader()
    words, intent_classes, train_x, train_y = Classifier.model_load()
    model = Classifier.model(train_x, train_y)
    model.load('model.tflearn')

    response = Classifier.response(model, intents, words, intent_classes, sentence)
    print(response)