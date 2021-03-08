# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:16:58 2021

@author: antho
"""
import pandas as pd
import numpy as np
from tqdm import tqdm

shopee = pd.read_json('contacts.json')
shopee['connection'] = [[] for _ in range(len(shopee))]
shopee['contacts_sum'] = pd.Series(np.zeros(len(shopee)))

email_not_nan = shopee.loc[shopee.Email != '']     
email_groupby = email_not_nan.groupby('Email').agg({'Id': list, 'Contacts': 'sum'})
email_groupby.reset_index(drop=False,inplace=True)

phone_not_nan = shopee.loc[shopee.Phone != ''] 
phone_groupby = phone_not_nan.groupby('Phone').agg({'Id': list, 'Contacts': 'sum'})
phone_groupby.reset_index(drop=False,inplace=True)

order_not_nan = shopee.loc[shopee.OrderId != ''] 
order_groupby = order_not_nan.groupby('OrderId').agg({'Id': list, 'Contacts': 'sum'})
order_groupby.reset_index(drop=False,inplace=True)

shopee = shopee.merge(email_groupby, left_on='Email', right_on='Email', 
                    how='left', suffixes=('', '_email_concat'))
shopee['Id_email_concat'] = shopee['Id_email_concat'].apply(lambda d: d if isinstance(d, list) else [])

shopee = shopee.merge(phone_groupby, left_on='Phone', right_on='Phone', 
                    how='left', suffixes=('', '_phone_concat'))
shopee['Id_phone_concat'] = shopee['Id_phone_concat'].apply(lambda d: d if isinstance(d, list) else [])

shopee = shopee.merge(order_groupby, left_on='OrderId', right_on='OrderId', 
                    how='left', suffixes=('', '_order_concat'))
shopee['Id_order_concat'] = shopee['Id_order_concat'].apply(lambda d: d if isinstance(d, list) else [])

for i in tqdm(range(len(shopee))):
    same_contacts = pd.concat([pd.Series(shopee.Id_email_concat[i]), 
                               pd.Series(shopee.Id_phone_concat[i]),
                               pd.Series(shopee.Id_order_concat[i])])
    
    shopee.connection[i] = same_contacts.unique()
    
    for j in shopee.loc[i, 'connection']:
        shopee.contacts_sum[i] += shopee.Contacts[j]

subm = shopee.loc[:, ['Id', 'connection', 'contacts_sum']]

subm['connection_string'] = ['a' for _ in range(len(subm))]

for i, connec in tqdm(enumerate(subm.connection)):
    connec_str = ""
    for conn in connec:
        if conn != connec[-1] :
            connec_str += f"{conn}-"
        else:
            connec_str += f"{conn}"
    subm.connection_string[i] = connec_str + ", " + str(int(subm.contacts_sum[i]))
    
subm.drop(['connection', 'contacts_sum'], axis=1, inplace=True)
subm.columns = ['ticket_id', 'ticket_trace/contact']

subm.to_csv('shopee_subm.csv', index=False, header=True)
