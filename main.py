outfilename = "results.txt"


def main(seq, k):
    kmers_dict = count_kmers(seq, k)
    print(kmers_dict)
    write2file(kmers_dict, outfilename)


def main_non_dict(seq, k):
    kmer_list, counts = count_kmers_non_dict(seq, k)
    write2file_non_dict(kmer_list, counts, outfilename)


def count_kmers(seq, k):
    count_dict = {}
    for i in range(len(seq) - k + 1):
        cur_seq = seq[i:i + k].upper()
        if check_if_contains_non_dna(cur_seq):
            continue
        if cur_seq in count_dict:
            count_dict[cur_seq] += 1
        else:
            count_dict[cur_seq] = 1
    return count_dict


def write2file(kmers_dict, outfilename):
    sorted_keys = sorted(kmers_dict)
    with open(outfilename, "w") as file:
        for key in sorted_keys:
            file.write(f"{key}:{kmers_dict[key]}\n")


def count_kmers_non_dict(seq, k):
    seq_list = []
    count_list = []
    for i in range(len(seq) - k + 1):
        cur_seq = seq[i:i + k].upper()
        if check_if_contains_non_dna(cur_seq):
            continue
        if cur_seq not in seq_list:
            seq_list.append(cur_seq)
            seq_list.sort()
            count_list.insert(seq_list.index(cur_seq), 1)
        else:
            count_list[seq_list.index(cur_seq)] += 1
    return [seq_list, count_list]



def write2file_non_dict(kmer_list, counts, outfilename):
    with open(outfilename, "w") as file:
        for i in range(len(kmer_list)):
            file.write(f"{kmer_list[i]}:{counts[i]}\n")


def check_if_contains_non_dna(cur_seq):
    contains_non_dna = False
    for c in cur_seq:
        if c not in ['A', 'T', 'C', 'G']:
            contains_non_dna = True
            continue
    return contains_non_dna

if __name__ == '__main__':
    main(
        'ctccaaagaaattgtagttttcttctggcttagaggtagatcatcttggtccaatcagactgaaatgccttgaggctagatttcagtctttgtGGCAGCTGgtgaatttctagtttgccttttcagctagggattagctttttaggggtcccaatgcctagggagatttctaggtcctctgttccttgctgacctccaat'
        , 2)
