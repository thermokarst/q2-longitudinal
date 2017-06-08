# q2-intervention
QIIME2 plugin for paired sample comparisons.

q2-intervention's actions support statistical and visual comparisons of paired samples, to determine if/how samples change between observational "states". "States" will most commonly be related to time, and the sample pairs should typically consist of the same individual subject  observed at two different time points. For example, patients in a clinical study whose stool samples are collected before and after receiving treatment.

"States" can also commonly be methodological, in which case sample pairs will usually be the same individual at the same time with two different methods. For example, q2-feature-classifier could compare the effects of different collection methods, storage methods, DNA extraction methods, or any bioinformatic processing steps on the feature composition of individual samples.

In the examples below, we use data from a longitudinal study of infants' and mothers' microbiota from birth through 2 years of life ([doi: 10.1126/scitranslmed.aad7121](http://stm.sciencemag.org/content/8/343/343ra82)).

## Examples

### Paired difference testing

Paired difference tests determine whether the value of a specific metric changed significantly between pairs of paired samples (e.g., pre- and post-treatment).

This visualizer currently supports comparison of feature abundance (e.g., microbial sequence variants or taxa) in a feature table, or of metadata values in a sample metadata file. Alpha diversity values (e.g., observed sequence variants) and beta diversity values (e.g., principal coordinates) are useful metrics for comparison with these tests, but those data must currently be added to a metadata file before analysis.

#### Paired differences in metadata

Here we use `paired-differences` to assess whether alpha diversity (sequence variants, here called `observed_otus`) changed significantly between 0 and 12 months of life in vaginally born and Cesarean-delivered infants, and whether the magnitude of change differed between these groups.

```
cd ~/Desktop/projects/q2-intervention/q2_intervention/test_data

qiime intervention paired-differences \
	--i-table ecam-table-taxa.qza \
	--m-metadata-file ecam_map_maturity.txt \
	--p-metric observed_otus \
	--p-group-category delivery \
	--p-state-category month \
	--p-state-pre 0 \
	--p-state-post 12 \
	--p-individual-id-category studyid \
	--o-visualization ecam-delivery-alpha \
	--p-no-drop-duplicates
```

#### Paired differences in feature table

We can also use this method to measure changes in the abundances of specific features of interest. In this example, we test whether the abundance of genus Bacteroides changed significantly between 6 and 18 months of life in vaginally born and Cesarean-delivered infants, and whether the magnitude of change differed between these groups. Note that `paired-differences` currently requires a feature table as input whether or not those data are actually used in the analysis.

```
qiime intervention paired-differences \
	--i-table ecam-table-taxa.qza \
	--m-metadata-file ecam_map_maturity.txt \
	--p-metric 'k__Bacteria;p__Bacteroidetes;c__Bacteroidia;o__Bacteroidales;f__Bacteroidaceae;g__Bacteroides;s__' \
	--p-group-category delivery \
	--p-state-category month \
	--p-state-pre 6 \
	--p-state-post 18 \
	--p-individual-id-category studyid \
	--o-visualization ecam-delivery \
	--p-no-drop-duplicates
```

### Paired pairwise distance testing

The `pairwise-distance` visualizer also assesses changes between paired samples from two different "states", but instead of taking a metadata category or feature ID as input, it operates on a distance matrix to assess the distance between "pre" and "post" sample pairs. The "within-subject" distance between paired samples from an individual are always calculated for each group in the metadata `group_category`; by default, "between-subject" distances between all individuals in a given `group_category` are also calculated and compared. Between-subject distances include all samples sharing the same `group_category` that are not pairs of "within-subject" samples from `state_pre` and `state_post`, but otherwise ignore the `state_category` and `individual_id_category` parameters, so will pair all samples from all time points (or whatever the comparison "state" is) in the distance matrix. Hence, users should carefully consider what type of comparison they wish to perform and, if appropriate, filter the distance matrix prior to using this visualizer. Filtering can be performed with `filter-distance-matrix` as described [here](https://docs.qiime2.org/2017.5/tutorials/filtering/#filtering-distance-matrices).

In this example, we test whether an individual's stool microbiota (as assessed by unweighted UniFrac distance) differs significantly between 0 and 12 months of life in vaginally born and Cesarean-delivered infants, and whether the within- and between-subject distances differed between these groups. 
```
qiime intervention pairwise-distance \
	--i-distance-matrix ecam-unweighted-distance-matrix.qza \
	--m-metadata-file ecam_map_maturity.txt \
	--p-group-category delivery \
	--p-state-category month \
	--p-state-pre 0 \
	--p-state-post 12 \
	--p-individual-id-category studyid \
	--o-visualization ecam-delivery-distance \
	--p-no-drop-duplicates
```

If between-subject distances are not important, the same visualization can be performed excluding these distances with the following command:
```
qiime intervention pairwise-distance \
	--i-distance-matrix ecam-unweighted-distance-matrix.qza \
	--m-metadata-file ecam_map_maturity.txt \
	--p-group-category delivery \
	--p-state-category month \
	--p-state-pre 0 \
	--p-state-post 12 \
	--p-individual-id-category studyid \
	--o-visualization ecam-delivery-distance-no-between \
	--p-no-drop-duplicates \
	--p-no-between-group-distance
```
### Linear mixed effects models

```
qiime intervention linear-mixed-effects \
	--i-table ecam-table-taxa.qza \
	--m-metadata-file ecam_map_maturity.txt \
	--p-metric observed_otus \
	--p-group-categories delivery,diet,sex,antiexposedall \
	--p-state-category month \
	--p-individual-id-category studyid \
	--o-visualization ecam-lme
```