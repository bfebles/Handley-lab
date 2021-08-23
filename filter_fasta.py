#!/usr/bin/env python

import os
from pathlib import Path
from Bio import SeqIO

cwd = os.getcwd()
path = Path(cwd)
outdir = str(path.parent)

with open ("filtered_seq.fa", 'w') as out_handle:
    for record in SeqIO.parse("final_sequences.fa", "fasta"):
        if record.seq.count('N')<= 10000:
            out_handle.write(record.format("fasta"))
