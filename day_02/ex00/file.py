from copy import deepcopy


def empty(input_dict: dict) -> dict:
    """
    Remove the 'gold_ingots' key from the input dictionary 
    and return the modified dictionary.

    Parameters:
        input_dict (dict): The dictionary to be modified.

    Returns:
        dict: The modified dictionary with 'gold_ingots' key removed.
    """
    dict_copy = deepcopy(input_dict)
    if 'gold_ingots' in dict_copy:
        del dict_copy['gold_ingots']
    return dict_copy


def add_ingot(input_dict: dict) -> dict:
    """
    Takes an input dictionary and returns a modified copy of the dictionary.
    Increments the 'gold_ingots' value in the input_dict by 1,
    or initializes it to 1 if it doesn't exist.

    Parameters:
        input_dict (dict): The dictionary to modify.

    Returns:
        dict: The modified dictionary.
    """
    dict_copy = deepcopy(input_dict)
    if 'gold_ingots' in dict_copy and dict_copy['gold_ingots'] is not None:
        dict_copy['gold_ingots'] += 1
    else:
        dict_copy['gold_ingots'] = 1
    return dict_copy


def get_ingot(input_dict: dict) -> int:
    """
    Takes an input dictionary and returns a modified copy of the dictionary.
    
    Parameters:
        input_dict (dict): The dictionary to be copied and modified.
        
    Returns:
        int: The modified copy of the dictionary.
    """
    dict_copy = deepcopy(input_dict)
    if 'gold_ingots' in dict_copy:
        if dict_copy['gold_ingots'] > 0:
            dict_copy['gold_ingots'] -= 1
        else:
            dict_copy['gold_ingots'] = 0
    return dict_copy


def main():
    purse = {}
    print(add_ingot(get_ingot(add_ingot(empty(purse)))))



if __name__ == "__main__":
    main()
