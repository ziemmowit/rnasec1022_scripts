import csv
import sys

def get_annotations(filepath):
    ann_dict = dict();
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for idx, row in enumerate(csv_reader):
            if idx > 0:
                ann_dict[row[0]] = []
    return ann_dict

def get_gene_dict(filepath):
    gene_dict = dict()
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for idx, row in enumerate(csv_reader):
            if idx > 0:
                gene_dict[row[0]] = row[1]
    return gene_dict

def get_gene_name(annotation_name, gene_dict, used_genes):
    if gene_dict[annotation_name]:
        return gene_dict[annotation_name]
    else:
        return annotation_name

files = sys.argv[2:]
annotations = get_annotations(sys.argv[1])
gene_list = get_gene_dict(sys.argv[1])

if len(sys.argv) < 3:
    print("Error: invalid num of arguments.")
    print("Try: $joincounts ensembl_annotation_file counts_sample_1 [counts_samnple_n]")
    exit()

print(",".join(map(lambda f: f.split(".")[0],files)))

for file in files:
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for idx, row in enumerate(csv_reader):
            if idx > 1:
                annotation = row[0]
                counts = int(row[6])
                annotations[annotation].append(counts)

used_genes = []
for annotation in annotations:
     row_data = annotations[annotation]
     counts_as_int = map(lambda d: int(d),row_data[1:])
     if(sum(counts_as_int) > 0):
        gene_name = get_gene_name(annotation, gene_list, used_genes)
        if gene_name in used_genes:
            gene_name = gene_name + "--" + str(len(used_genes))
        else:
            used_genes.append(gene_name)
        print(gene_name+","+",".join(map(lambda d: str(d), row_data)))