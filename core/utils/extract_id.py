import re

def extract_id(id_attr:str) -> int:
    item_id = int(re.search(r'\d+', id_attr).group())
    if item_id is None:
        raise ValueError(f"No numerical value was found in the id attribute : {id_attr}")
    return item_id