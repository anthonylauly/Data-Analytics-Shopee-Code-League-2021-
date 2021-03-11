# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:16:58 2021

@author: antho
"""
import pandas as pd
import numpy as np
from tqdm import tqdm

shopee = pd.read_json('contacts.json')
shopee = shopee.values

connect_values = {}

def add_to_dict(dictionary, key, val):
    if key != '' and key != ' ':
        if key in dictionary.keys():
            dictionary[key].add(val)
        else:
            dictionary[key] = {val}
            
for row in shopee:
    add_to_dict(connect_values, row[1], row[0])
    add_to_dict(connect_values, row[2], row[0])
    add_to_dict(connect_values, row[4], row[0])

connections = {}

for value in tqdm(connect_values.values()):
    value_copy = value.copy()
    for ids in value:
        if ids in connections.keys():
            value_copy.update(connections.get(ids))
            
    for ids in value_copy:
        connections[ids] = value_copy

subm = []

for key, val in tqdm(sorted(connections.items()), total=len(connections.items())):
    contacts = np.sum(shopee[list(val), 3])
    trace = "-".join([str(_id) for _id in sorted(val)])
    answer = "{}, {}".format(trace, contacts)
    subm.append({"ticket_id": key,  "ticket_trace/contact": answer})
    

subm = pd.DataFrame(subm)

subm.to_csv('shopee_subm.csv', index=False, header=True)
