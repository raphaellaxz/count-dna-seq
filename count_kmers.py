import sys
import load_txt_file_module
import main


def count_kmers():
    file_name = sys.argv[1]
    file_name_list = file_name.split(".")
    count_list = map(lambda kStr: int(kStr), sys.argv[2].split(','))
    seqs = []
    if len(sys.argv) >= 4 and sys.argv[3] == "-t":
        seqs = load_txt_file_module.load_file(file_name)
    else:
        seqs = load_txt_file_module.load_file(file_name)
    for k in count_list:
        result_kmers_dict = {}
        for seq in seqs:
            result_kmers_dict = merge_dict(result_kmers_dict, main.count_kmers(seq, k))
        main.write2file(result_kmers_dict, f"{file_name_list[0]}_{k}-mer-frequency.txt")


def merge_dict(dict1, dict2):
    for key in dict1:
        if key in dict2:
            dict2[key] += dict1[key]
        else:
            dict2[key] = dict1[key]
    return dict2


if __name__ == '__main__':
    count_kmers()
