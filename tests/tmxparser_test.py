import unittest
import os

from tmxiterparse.tmxparser import TmxParser

def get_test_file_path(filename:str)-> str:
    return os.path.join(os.path.dirname(__file__), "data", filename)


class TmxParserTest(unittest.TestCase):

    def test_simple(self):
        with TmxParser(get_test_file_path("simple.xml")) as parser:
            self.assertEqual(parser.header["creationtool"], "XYZTool")
            self.assertEqual(parser.header["creationtoolversion"], "1.01-023")
            self.assertEqual(parser.header["datatype"], "PlainText")
            self.assertEqual(parser.header["segtype"], "sentence")
            self.assertEqual(parser.header["adminlang"], "en-us")
            self.assertEqual(parser.header["srclang"], "en")
            self.assertEqual(parser.header["o-tmf"], "ABCTransMem")
            
            tus = [ v for v in parser]
            self.assertEqual(len(tus), 1)

            self.assertEqual(tus[0].values[0].lang, "en")
            self.assertEqual(tus[0].values[0].value, "Hello world!")

            self.assertEqual(tus[0].values[1].lang, "fr")
            self.assertEqual(tus[0].values[1].value, "Bonjour tout le monde!")

if __name__ == '__main__':
    unittest.main()