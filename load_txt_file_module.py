FILE_TYPE_FASTA = "fasta"
FILE_TYPE_FASTQ = "fastq"
FILE_TYPE_TXT = "txt"


def load_file(input_file_name):
    if input_file_name.endswith(FILE_TYPE_FASTA):
        return load_fasta_file(input_file_name)
    elif input_file_name.endswith(FILE_TYPE_FASTQ):
        return load_fastq_file(input_file_name)
    else:
        return load_txt_file(input_file_name)


def load_txt_file(input_file_name):
    seq = ""
    with open(input_file_name, "r") as file:
        for line in file:
            seq += line.rstrip()
    return [seq]


def load_fasta_file(fasta_file):
    seq = []
    with open(fasta_file, "r") as file:
        cur_seq = ""
        for line in file:
            if line[0] in ">":
                if cur_seq != "":
                    seq.append(cur_seq)
                cur_seq = ""
                continue
            cur_seq += line.rstrip()
        seq.append(cur_seq)
    return seq


def load_fastq_file(fastq_file):
    seq = []
    with open(fastq_file, "r") as file:
        cur_seq = ""
        is_seq_line = False
        for line in file:
            if is_seq_line:
                cur_seq += line.rstrip()
                is_seq_line = False
            elif is_fastq_id_line(line):
                if cur_seq != "":
                    seq.append(cur_seq)
                    cur_seq = ""
                is_seq_line = True
            elif is_fastq_quality_id(line):
                is_seq_line = False
        seq.append(cur_seq)
    return seq


def is_fastq_id_line(line):
    return line[0] == "@"


def is_fastq_quality_id(line):
    return line[0] == "+"


if __name__ == '__main__':
    load_file("tiny_reads.fastq")