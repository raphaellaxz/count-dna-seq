def load_txt_file(inputfilename):
    seq = ""
    with open(inputfilename, "r") as file:
        for line in file:
            seq += line.rstrip()
    return seq
