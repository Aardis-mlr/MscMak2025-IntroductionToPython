"""write_genes.py takes an annotation file and
writes gene names to file
Usage:
    python write_genes.py <>"""
import sys

# print(gene_file)
# print(out_file)
dna_list=list('ACGT')
def getGenList(gene_file):
    with open (gene_file, 'r') as humchr:
        tag = False #Start by setting the tag to false
        gene_list=[]
        for line in humchr:
                if line.startswith('Gene'):
                    tag = True
                if tag:
                    line_split = line.split()
                    if len(line_split) != 0:
                        if '-' in line_split[0]:
                            continue
                        else:
                            gene_list.append(line_split[0])
    return gene_list[3:][:-2]

    clean_gene_list = getGenList()

def writeGeneList(clean_gene_list):
    with open(out_file, 'w') as gene_names:   #creating a new file called gene_names
        for gene in clean_gene_list:
                gene_names.writelines(gene+'\n')
    print('Genes have been written successfully!!')
if len(sys.argv) < 3:
    print(__doc__)
else:
    gene_file = sys.argv[1]
    out_file = sys.argv[2]
    clean_gene_list = getGenList(gene_file)
    writeGeneList(clean_gene_list, out_file)
    