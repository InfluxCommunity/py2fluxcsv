import os

def convert(input_list):
    all_tables = ""
    for i, l in enumerate(input_list):
        if(i > 0):
            all_tables += os.linesep
        all_tables += list_to_csv(i, l)
    return all_tables

def list_to_csv(i, dictionaries):
    header = ",result,table"
    keys = dictionaries[0].keys()
    for key in keys:
        header += ",{}".format(key)

    lines = header + os.linesep
    for d in dictionaries:
        line = ",_result"
        line += ",{}".format(i)
        for key in keys:
            line += ",{}".format(d[key])
        line += os.linesep
        lines += line
    
    return lines
