def complement_seq(dnaseq):
    dnaseq = dnaseq.upper()
    complement = []
    for nt in dnaseq:
        if nt == "C":
            complement.append("G")
        if nt == "G":
            complement.append("C")
        if nt == "A":
            complement.append("T")
        if nt == "T":
            complement.append("A")
    complement = "".join(complement)
    return complement

def reverse_complement(dnaseq):
    dnaseq = dnaseq.upper()
    dnaseq.split(" ")
    rev = dnaseq[::-1]
    revcompl = complement_seq(rev)
    return revcompl

print("Hello, this a simple genomic tool to get the reverse complement strand of a DNA sequence")
seq= input("Enter the forward strand in order to get the reversed complement strand: \n")
print(reverse_complement(seq))
