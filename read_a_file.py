# write a function to read a file
def read_a_file(x):
    # open the file
    with open(x, "r") as f:
        # read the file
        y = f.read()
    # return the file
    return y
    