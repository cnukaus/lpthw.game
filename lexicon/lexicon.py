class UnsettableError(Exception):
                pass
class LexiconTuple(object):
                def __init__(self, word, word_type):
                                self.word=word
                                self.word_type=word_type
                def get_type(self):
                                return self.word_type
                def set_type(self, new_type):
                                self.word_type=new_type
                def get_word(self):
                                return self.word
                def set_word(self, new_word):
                                self.word=new_word
                def get_tuple(self):
                                return tuple([self.word_type, self.word])
class VerbTuple(LexiconTuple):
                def __init__(self, word):
                                self.word=word
                                self.word_type="verb"
                def set_type(self, new_type):
                                raise UnsettableError("Cannot set type of a verb")
class NounTuple(LexiconTuple):
                def __init__(self, word):
                                self.word=word
                                self.word_type="noun"
                def set_type(self, new_type):
                                raise UnsettableError("Cannot set type of a noun")
class ErrorTuple(LexiconTuple):
                def __init__(self, word):
                                self.word=word
                                self.word_type="error"
                def set_type(self, new_type):
                                raise UnsettableError("Cannot set type of ErrorTuple (type=error)")
class NumberTuple(LexiconTuple):
                def __init__(self, word):
                                self.word=word
                                self.word_type="number"
                def set_type(self, new_type):
                                raise UnsettableError("Cannot set type of a number")

TO_TUPLE_DICT={"go": VerbTuple("go"), "open": VerbTuple("open"), "bear": NounTuple("bear"), "player": NounTuple("player"), "door": NounTuple("door"), "smack": VerbTuple("smack"), "nose": NounTuple("nose")}
def word_scan(word, tuple_dict=TO_TUPLE_DICT, return_tuple=True):
                try:
                                end=tuple_dict[word]
                except:
                                # check for number
                                try:
                                                x=int(word)
                                                del x
                                                end=NumberTuple(word)
                                except:
                                                # isn't in dict and isn't number, must be error
                                                end=ErrorTuple(word)
                if return_tuple:
                                return end.get_tuple()
                return end
def scan(string):
                returns=[]
                try:
                                string.append(1)
                                b=string.pop()
                                del b
                                def word_scan(word, tuple_dict=TO_TUPLE_DICT, return_tuple=True):
                                                try:
                                                                end=tuple_dict[word]
                                                except:
                                                                # check for number
                                                                try:
                                                                                x=int(word)
                                                                                del x
                                                                                end=NumberTuple(word)
                                                                except:
                                                                                # isn't in dict and isn't number, must be error
                                                                                end=ErrorTuple(word)
                                array=string
                                del string
                                for i in array:
                                                returns.append(word_scan(i))
                                return returns
                except:
                          pass      
                for i in string.split(" "):
                                def word_scan(word, tuple_dict=TO_TUPLE_DICT, return_tuple=True):
                                                try:
                                                                end=tuple_dict[word]
                                                except:
                                                                # check for number
                                                                try:
                                                                                x=int(word)
                                                                                del x
                                                                                end=NumberTuple(word)
                                                                except:
                                                                                # isn't in dict and isn't number, must be error
                                                                                end=ErrorTuple(word)
                                                if return_tuple:
                                                                return end.get_tuple()
                                                return end
                                returns.append(word_scan(i))
                return returns
