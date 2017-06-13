from Bio import SeqIO

handle = open("../pdbs/1a49.pdb", "rU")

for record in SeqIO.parse(handle, "pdb-seqres"):
    print(">" + record.id + "\n" + record.seq)

handle.close()