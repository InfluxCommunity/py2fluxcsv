import os


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
