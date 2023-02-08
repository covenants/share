# write a function to read a file
# Read a file and retun resul
def read_a_file(x):
    # open the file
    with open(x, "r") as f:
        # read the file
        y = f.read()
    # return the file
    return y
    