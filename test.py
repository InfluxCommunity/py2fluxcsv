import unittest
import py2fluxcsv
import io
import os


class TestConversions(unittest.TestCase):
    def test_single_value(self):
        l = [[{"val": 1}]]
        csv = py2fluxcsv.convert(l)
        self.assertEqual(csv, single_val_csv)

    def test_multiple_tables(self):
        l = multi_table_dict
        self.assertEqual(py2fluxcsv.convert(l), multi_row_csv)

    def test_buffer(self):
        csv_iter = py2fluxcsv.CSVIter(multi_table_dict)
        a = ""
        for s in csv_iter:
            a += s
        self.assertEqual(a, multi_row_csv)


multi_table_dict = [[{
    "t": "1",
    "int": 1,
    "string": "one"
}, {
    "t": "1",
    "int": 2,
    "string": "two"
}],
                    [{
                        "t": "2",
                        "int": 1,
                        "string": "one"
                    }, {
                        "t": "2",
                        "int": 2,
                        "string": "two"
                    }]]

single_val_csv = ''',result,table,val
,_result,0,1
'''

multi_row_csv = ''',result,table,t,int,string
,_result,0,1,1,one
,_result,0,1,2,two

,result,table,t,int,string
,_result,1,2,1,one
,_result,1,2,2,two
'''

if __name__ == '__main__':
    unittest.main()
