# write a function to reverse a list
def reverse_list(x):
    # create an empty list
    y = []
    # loop through the list
    for i in x:
        # append the item to the front of the list
        y.insert(0, i)
    # return the reversed list
    return y
    