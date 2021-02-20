import os
from io import StringIO

def convert(input_list):
    all_tables = ""
    for i, l in enumerate(input_list):
        if (i > 0):
            all_tables += os.linesep
        all_tables += list_to_csv(i, l)
    return all_tables

def list_to_csv(i, dictionaries):
    keys = keys_for_table(dictionaries)
    lines = header_for_table(keys)
    for d in dictionaries:
        lines += line_from_dict(i, keys, d)
    return lines

def header_for_table(keys):
    header = ",result,table"
    for key in keys:
        header += ",{}".format(key)
    header += os.linesep
    return header

def keys_for_table(dictionaries):
    return dictionaries[0].keys()

def line_from_dict(i, keys, d):
    line = ",_result"
    line += ",{}".format(i)
    for key in keys:
        line += ",{}".format(d[key])
    line += os.linesep
    return line

def write_to_buff(buff, input_list):
    for i, l in enumerate(input_list):
        keys = keys_for_table(l)
        buff.write(header_for_table(keys))
        if(i > 0):
            buff.write(os.linesep)
        buff.flush()
        for dictionary in l:
            buff.write(line_from_dict(i, keys, dictionary))
            buff.flush()

class CSVIter:
    def __init__(self, input_list):
        self._input_list = input_list
        self._table_index = 0
        self._dictionary_index = 0
        self.EOF = False
        self._current_keys = []
    
    def __iter__(self):
        return self
    
    def __next__(self):
        data = ""
        if self.EOF:
            raise StopIteration
            
        if self._dictionary_index == 0:
            self._current_keys = keys_for_table(self._input_list[self._table_index])
            if(self._table_index > 0):
                data += os.linesep
            data += header_for_table(self._current_keys)
            
        d = self._input_list[self._table_index][self._dictionary_index]
        data += line_from_dict(self._table_index, self._current_keys, d)

        self._dictionary_index += 1
        if self._dictionary_index == len(self._input_list[self._table_index]):
            self._dictionary_index = 0
            self._table_index += 1
            if self._table_index == len(self._input_list):
                self.EOF = True
        return data
            
        
                
