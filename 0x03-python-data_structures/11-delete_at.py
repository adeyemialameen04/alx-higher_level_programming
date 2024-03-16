def delete_at(my_list=[], idx=0):
    # Check if idx is within the range of the list indices
    if 0 <= idx < len(my_list):
        # Delete the item at the specified index
        del my_list[idx]

    # Return the modified list
    return my_list
