"""
Day 31 - Merge dictionaries.
Merge two dictionaries.
"""

dict1 = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

dict2 = {
    "keyA": "valueA",
    "keyB": "valueB",
    "keyC": "valueC",
    "keyD": "valueD",
    "keyE": "valueE"
}

dictMerged = {**dict1 , **dict2}
print (dictMerged)