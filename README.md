# Overview
Python code that turns a list of lists of dictionaries into Flux's annotated CSV format.

This is useful for interoperating with the Girraffe library, or other libraries that use the annotated CSV format.

# Examples
In all cases, you start with a list of lists of dictionaries. Currently, the code assumes that all of the dictionaries have the same schema, and there is currently no error handling in place if this is not the case:

```python
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
```
You can create csv in one shot, turning it into one big string with the convert() function:
```python
>>> import py2fluxcsv
>>> multi_table_dict = [[{
...     "t": "1",
...     "int": 1,
...     "string": "one"
... }, {
...     "t": "1",
...     "int": 2,
...     "string": "two"
... }],
... [{
...     "t": "2",
...     "int": 1,
...     "string": "one"
... }, {
...     "t": "2",
...     "int": 2,
...     "string": "two"
... }]]
>>> csv = py2fluxcsv.convert(multi_table_dict)
>>> print(csv)
,result,table,t,int,string
,_result,0,1,1,one
,_result,0,1,2,two

,result,table,t,int,string
,_result,1,2,1,one
,_result,1,2,2,two
```
This may have performance and memory implications for large lists of data, so, as an alternative, you can use CSVIter to convert one dictionary at a time:
```python
>>> csv_iter = py2fluxcsv.CSVIter(multi_table_dict)
>>> for s in csv_iter:
...     #write out to a buffer or stream
...     print(s)
... 
,result,table,t,int,string
,_result,0,1,1,one

,_result,0,1,2,two


,result,table,t,int,string
,_result,1,2,1,one

,_result,1,2,2,two
```
