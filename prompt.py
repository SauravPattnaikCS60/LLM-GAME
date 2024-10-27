
def return_prompt_game(object):
    objects_description_prompt = f'''
    You are a helpful AI assistant and your work is to help us in creating a fun game.
    You will be given an object as INPUT. This object will be a daily driver kind of object
    in people's lives. Your task is to create a funny witty DESCRIPTION of that object without revealing the INPUT.
    The objective is to create the description in such a manner that the description is funny
    and also it is little difficult to relate it to the input object. The descriptions that you create
    will be used by users to figure out what the object was.

    For creating DESCRIPTION please follow the below RULES:
    1. Do not give any vulgar or obscene DESCRIPTION.
    2. Do not give DESCRIPTION that are completly unrelated to the INPUT.
    3. Ensure to give DESCRIPTION that are challenging to the users but not too difficult.
    4. Try to give funny, witty descriptions of the INPUT.
    5. Do not mention the INPUT in the generated DESCRIPTION.
    6. The DESCRIPTION should be under 10 words.
    7. Just give the DESCRIPTION as output. Do not add any text before or after it.

    Abide by the above RULES when generating DESCRIPTION.

    INPUT : {object}
    DESCRIPTION : 
    '''
    return objects_description_prompt

def return_list_objects_prompt(category):
    
    prompt = f'''
    You are a helpful AI Assistant.You will be given a CATEGORY as input and your task
    is to create a LIST of most popular and well known 25 objects belonging to that CATEGORY.
    
    For creating a list of 25 objects please follow the below RULES:
    1. Only select those objects which are well known and strictly belong to that category.
    2. If unable to return a LIST of 25 objects, return whatever length is possible.
    3. Ensure to return the LIST as a valid python list.
    4. Just give the python list as output. Do not add any text before or after it.
    
    Abide by the above RULES when creating the LIST.
    
    CATEGORY : {category}
    OUTPUT : 
    '''
    return prompt