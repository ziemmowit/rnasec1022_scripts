import csv
import sys
from subprocess import Popen, PIPE
from Bio.Seq import Seq

if len(sys.argv) < 3:
    print("Error: invalid num of arguments.")
    print("Try: $add_sequences peak_file genome_file")
    exit()

peak_file = sys.argv[1]
genome_file = sys.argv[2]

with open(peak_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for idx, row in enumerate(csv_reader):
        if idx > 1:
            chrom = "chr"+row[0]
            start = row[1]
            end = str(int(start) + 25)
            strand = row[2]
            
            cmd = './twoBitToFa '+genome_file+':'+chrom+':'+start+'-'+end+' temp.fa'
            process = Popen(cmd, shell=True, stdout=PIPE)
            process.wait()

            with open('temp.fa') as file:
                for idx, line in enumerate(file):
                    if idx != 0:
                        sequence = line.replace("\n", "").upper()

            if strand == '-':
                seq = Seq(sequence)
                sequence = str(seq.reverse_complement())

            row.append(sequence)
            print("\t".join(row))

#for i in {1..34};do python3 add_sequences.py ../storage_docker/peaks_s$i/s$i_scores.tsv ../hg38.2bit  > ../storage_docker/peaks_s$i/s$i_scores_withSeq.tsv;done;