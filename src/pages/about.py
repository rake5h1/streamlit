import pathlib

from tinydb.queries import Query
import utils.display as udisp

import streamlit as st
from tinydb import TinyDB

beds=[]
for i in range(1000):
    beds.append(i)
    
available_beds=[]
db=TinyDB('beds.json')


find=Query()

def write():
    udisp.title_awesome("Available Beds")
    
    # for item in db:
    #     if item['bed'] in beds:
    #         st.write(f'Id:{int(item["id"])}-Bed:{int(item["bed"])}')
    items=db.all()
    for i in range (1,101):
        for item in items:
            if item['bed']==i:
                pass
            else:
                available_beds.append(i)
    id=st.number_input('Patient Id')
    bed=st.number_input('Assign Bed')
    if st.button('Clear Beds DB'):
        db.truncate()
    if st.button('Button'):
        db.insert({'id':id,'bed':bed})
    
    # db.insert({'bed':100})
    # for item in beds:
    #     if db.search(find.bed)
    #     st.write(item)
            

    