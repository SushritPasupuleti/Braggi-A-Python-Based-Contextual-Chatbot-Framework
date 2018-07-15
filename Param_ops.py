#%%
import re

#----Parameter Variables-----#
#stores all Parameters in dedicated files
#read and write changes during runtime
#add new parameters through scripts in conversational models when necessary
IntJSON = "./Memory_Models/Int.json"
TimeJSON = "./Memory_Models/Time.json"
DateJSON = "./Memory_Models/Date.json"
StrJSON = "./Memory_Models/Str.json"

def param_classify(param, input):
    '''Determines parameter's data type: Int, Time, Date, Str'''

    type_regex_arg = re.compile(r'^[A-Z][a-z]*.')
    param_type = re.findall(type_regex_arg, param)
    
    if param_type[0] == "Int":
        Int_param(param, input)
    if param_type[0] == "Time":
        Time_param(param, input)
    if param_type[0] == "Date":
        Date_param(param, input)
    if param_type[0] == "Str":
        Str_param(param, input)

def Int_param(param, input):
    '''Find the sub tag of the paramater'''

    sub_type_regex_arg = re.compile(r'.[A-Z][a-z]*')
    sub_type = re.findall(sub_type_regex_arg, param)

    if sub_type[0] == ".Price":
        pass
    if sub_type[0] == ".Quantity":
        pass
    if sub_type[0] == ".Age":
        pass

def Str_param(param, input):
    '''Find the sub tag of the paramater'''

    sub_type_regex_arg = re.compile(r'.[A-Z][a-z]*')
    sub_type = re.findall(sub_type_regex_arg, param)

    if sub_type[0] == "":
        pass

def Time_param(param, input):
    '''Find the sub tag of the paramater'''
    
    sub_type_regex_arg = re.compile(r'.[A-Z][a-z]*')
    sub_type = re.findall(sub_type_regex_arg, param)

    if sub_type[0] == "":
        pass

def Date_param(param, input):
    '''Find the sub tag of the paramater'''
    
    sub_type_regex_arg = re.compile(r'.[A-Z][a-z]*')
    sub_type = re.findall(sub_type_regex_arg, param)

    if sub_type[0] == "":
        pass
