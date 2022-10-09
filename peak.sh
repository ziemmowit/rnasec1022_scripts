#!/bin/bash
echo "Bash version ${BASH_VERSION}..."
for i in {2..34}
do
  echo "==========="
  echo "Peak no. $i"

  folder='peaks_s'$i
  aligned='s'$i'.Aligned.sortedByCoord.out.bam'
  unique='s'$i'_cDNA_unique.bed'
  multiple='s'$i'_cDNA_multiple.bed'
  skipped='s'$i'_cDNA_skipped.bam'
  peaks='s'$i'_peaks.bed'
  scores='s'$i'_scores.tsv'
  clusters='s'$i'_clusters.bed'
  annotated='s'$i'_annotated_sites_biotype.tab'
  summary_folder='s'$i'_summary'

  rm -r $folder
  mkdir $folder

  iCount xlsites $aligned $folder/$unique $folder/$multiple $folder/$skipped --group_by start --quant reads
  iCount peaks hsseg.gtf.gz $folder/$unique $folder/$peaks --scores $folder/$scores
  iCount clusters $folder/$unique $folder/$peaks $folder/$clusters
  iCount annotate hsseg.gtf.gz $folder/$unique $folder/$annotated
  mkdir $folder/$summary_folder
  iCount summary hsseg.gtf.gz $folder/$unique $folder/$summary_folder
done