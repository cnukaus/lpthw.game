import lexicon
from nose import *
global equals
equals = tests.assert_equals

class __main__(object):
                def __init__(self, DEBUG, AUTO_TEST=True):
                                if AUTO_TEST:
                                                self.test_all(DEBUG=DEBUG)
                def __assert_eq_lexicon_one_scan__(self, to_scan, iterable_expected_output, debug=True):
                                equals(lexicon.scan(to_scan), [tuple(iterable_expected_output)], DEBUG=debug)
                def test_all(self, DEBUG=False):
                                print "Number testing start"
                                self.__assert_eq_lexicon_one_scan__("123456789", ["number", "123456789"], debug=DEBUG)
                                print "Number testing end, verb testing start"
                                self.__assert_eq_lexicon_one_scan__("open", ["verb", "open"], debug=DEBUG)
                def __repr__(self):
                                raise Exception("__repr__ was called, hide __repr__ by setting '__main__()' to variable")
if __name__=="__main__":
                x=raw_input("Debug? (1/0 OR True/False) ")
                try:
                                exec "x=%s(%s(x))"%tuple([__name__, "bool"])
                except ValueError:
                                exec "x=%s(%s(x))"%tuple([__name__, "int"])
                print "END, access __main__() by using variable 'x'"
