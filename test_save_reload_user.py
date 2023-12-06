#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.state import State

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new State --")
my_state = State()
my_state.state_id = "AZZA "
my_state.name = "Mohamed"
my_state.save()
print(my_state)