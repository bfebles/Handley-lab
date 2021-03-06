#!/bin/bash
# Add variant type field
#Filter quality threshold

for i in *.snpEFF.ann.vcf; do

     F=${i%.snpEFF.ann.vcf};

     echo "Running:$F";

     java -jar /opt/apps/snpEff/SnpSift.jar varType $i > ${F}.snpsift.vcf;

     cat ${F}.snpsift.vcf | java -jar /opt/apps/snpEff/SnpSift.jar filter "(QUAL >= 5000)" > ${F}.snpsift.filtered.vcf;

     java -jar /opt/apps/snpEff/SnpSift.jar extractFields ${F}.snpsift.filtered.vcf CHROM POS REF ALT VARTYPE QUAL FILTER DP AF SB "ANN[0].GENE" "EFF[0].EFFECT" "EFF[0].IMPACT" "EFF[0].BIOTYPE" > ${F}.snpsift.tsv;

done
