from create_data import categories
from test_groq import run_groq_api
import numpy as np
import ast
from prompt import return_prompt_game
import random

def invoke_main_pipeline():
    category = np.random.choice(categories)
    with open(f'data/objects/{category}.txt','r') as f:
        items =ast.literal_eval(f.read())
    
    item = np.random.choice(items)
    valid_options = [itm for itm in items if itm!=item]
    prompt = return_prompt_game(item)
    response = run_groq_api(prompt)
    options = [item] + list(np.random.choice(valid_options,3,replace=False))
    random.shuffle(options)
    return category, item, response, options
    
  
if __name__ == '__main__':
    item, question = invoke_main_pipeline()
    print(item)
    print(question)
    
    