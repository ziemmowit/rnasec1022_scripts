import csv
import sys

def get_first(arg):
    if not ";" in arg:
        return arg
    else:
        return arg.split(';')[0]

def get_genes_dict(filepath):
    gene_dict = dict();
    with open('mart_export.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for idx, row in enumerate(csv_reader):
            if idx > 0:
                strand = "+"
                if int(row[4]) < 0:
                    strand = "-"
                gene_dict[row[0]] = {'gene_name': row[1], 'start': row[2], 'end': row[3], 'strand': strand, 'chrom': row[5]}
    return gene_dict

file_path = sys.argv[1]
genes_data = get_genes_dict('mart_export.txt')
arr = []
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for idx, row in enumerate(csv_reader):
        if idx > 1:
            gene_data = genes_data[row[0]]
            annotation = row[0]
            gene_name = gene_data['gene_name']
            #chrom = get_first(row[1])
            chrom = gene_data['chrom']
            #start = get_first(row[2])
            start = gene_data['start']
            #end = get_first(row[3])
            end = gene_data['end']
            #strand = get_first(row[4])
            strand = gene_data['strand']
            #length = row[5]
            length = int(end) - int(start)
            counts = int(row[6])
            arr.append([annotation, gene_name, chrom, start, end, strand, counts])

sorted = sorted(arr, key=lambda x: x[5], reverse=True)
for row in sorted:
    print(row[0]+";"+row[1]+";"+row[2]+";"+row[3]+";"+row[4]+";"+row[5]+";"+str(row[6]))
#print(chrom + ";"+start+";"+end+";"+strand+";"+counts+";"+annotation)
#for i in {1..34};do python3 parse.py s$i.txt > o/s$i.csv;done;
#for i in {1..34};do featureCounts -T 2 -a homosapiens.gtf -o s$i.txt s$i.Aligned.sortedByCoord.out.bam;done;