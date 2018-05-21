class ESC_DNAtranslate():
    def __init__(self, seq):
        self.fdna = seq
        self.cdna = self.make_complement(self.fdna)
        self.frna = self.rnatranslate(self.fdna)
        self.crna = self.rnatranslate(self.cdna)
        self.fpro = self.proteintranslate(self.fdna)
        self.cpro = self.proteintranslate(self.cdna)
        
    def make_complement(self, seq):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return "".join(complement.get(base, base) for base in reversed(seq))
    
    def rnatranslate(self, dna):
        return dna.replace("T", "U")

    def proteintranslate(self, dna):
        codontable = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
                      'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
                      'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
                      'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                      'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
                      'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
                      'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
                      'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                      'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
                      'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
                      'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
                      'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'-', 'TAG':'-',
                      'TGC':'C', 'TGT':'C', 'TGA':'-', 'TGG':'W'}
        return "".join(codontable.get(dna[n:n+3], 'X') for n in range(0, len(dna), 3))
    
    def get_fdna(self):
        return self.fdna

    def get_cdna(self):
        return self.cdna

    def get_frna(self):
        return self.frna

    def get_crna(self):
        return self.crna

    def get_fpro(self):
        return self.fpro

    def get_cpro(self):
        return self.cpro