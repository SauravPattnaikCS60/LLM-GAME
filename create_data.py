from prompt import return_list_objects_prompt
from test_groq import run_groq_api

categories = ['Electronics','Everyday Use', 'Groceries','Stationary','Furniture']

def create_data_items():
    print(f'Total categories : {len(categories)}')

    for category in categories:
        print(f'Running : {category}')
        list_prompt = return_list_objects_prompt(category)
        response = run_groq_api(list_prompt,'llama-3.1-70b-versatile')
        with open(f'data/objects/{category}.txt','w') as f:
            f.write(response)

if __name__ == '__main__':
    create_data_items()

