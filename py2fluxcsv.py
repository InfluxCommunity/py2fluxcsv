import os
from io import StringIO

def convert(input_list):
    """Returns annotated csv for a list of lists of dictionaries."""
    all_tables = ""
    for i, l in enumerate(input_list):
        if (i > 0):
            all_tables += os.linesep
        all_tables += list_to_csv(i, l)
    return all_tables

def list_to_csv(i, dictionaries):
    """Converts a list of dictonaries to annotated CSV."""
    keys = keys_for_table(dictionaries)
    lines = annotation_for_table(keys)
    for d in dictionaries:
        lines += csv_for_dict(i, keys, d)
    return lines

def annotation_for_table(keys):
    """Creates the annotation for the keys of a dictionary.
    Used to create the annotation for a csv."""
    header = ",result,table"
    for key in keys:
        header += ",{}".format(key)
    header += os.linesep
    return header

def keys_for_table(dictionaries):
    """Gets the keys for a given list of dictionaries."""
    return dictionaries[0].keys()

def csv_for_dict(i, keys, d):
    """Gets the csv for a specific dictionary."""
    line = ",_result"
    line += ",{}".format(i)
    for key in keys:
        line += ",{}".format(d[key])
    line += os.linesep
    return line

"""An iterable class that returns annotated CSV one line at a time.
Designed for scenarios where it is undesirable to convert an entire list of
lists of dictionaries into one entire string. For example, when streaming
from an http server.
"""
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
            data += annotation_for_table(self._current_keys)
            
        d = self._input_list[self._table_index][self._dictionary_index]
        data += csv_for_dict(self._table_index, self._current_keys, d)

        self._dictionary_index += 1
        if self._dictionary_index == len(self._input_list[self._table_index]):
            self._dictionary_index = 0
            self._table_index += 1
            if self._table_index == len(self._input_list):
                self.EOF = True
        return data
            
        
                
