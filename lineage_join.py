#!/usr/bin/env python



import os
from pathlib import Path
import pandas as pd

cwd = os.getcwd()
path = Path(cwd)
outdir = str(path.parent)

pangolin = pd.read_csv('lineage_report.csv')
nextclade = pd.read_csv('nextclade_results.tsv', sep = '\t')
pangolin.rename(columns={'taxon': 'seqName','lineage':'Pangolin_lineage'},inplace=True)
final_lineage = pd.merge(left=pangolin,right=nextclade,left_on='seqName',right_on='seqName')
final_lineage.insert(2, 'clade', final_lineage.pop("clade"))
final_lineage.to_csv('final_lineage.csv',index=False)
    
