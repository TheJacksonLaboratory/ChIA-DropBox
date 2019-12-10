import numpy as np


def get_anchor_mids(loop_file):
    """
    """
    res = []
    
    with open(loop_file, 'r') as f:
        for line in f:
            entry = line.strip().split()
            a_chrom = entry[0]
            a_start = int(entry[1])
            a_end = int(entry[2])
            
            b_chrom = entry[3]
            b_start = int(entry[4])
            b_end = int(entry[5])
            
            pet = entry[6]
            
            a_mid = int(np.mean([a_start, a_end]))
            b_mid = int(np.mean([b_start, b_end]))
            
            row = [
                a_chrom, str(a_mid), str(a_mid + 1),
                b_chrom, str(b_mid), str(b_mid + 1),
                pet]
            
            res.append(row)
    
    out_file = loop_file + '.mids'
    
    with open(out_file, 'w') as f:
        for entry in res:
            f.write('\t'.join(entry) + '\n')
            

if __name__ == '__main__':
    
    loop_file = 'P2MC7N8HCORI_COMBINED.chr2R.short_format.bedpe.sorted.cut'
    get_anchor_mids(loop_file)
