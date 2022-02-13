# Computational Biogerontology Project 

So the idea is that we've got a bunch of drugs that have been show to extend lifespans in all the model animals and now we want to attempt to map them back onto the targets to identify aging pathways and mechanisms.

1. Download the drug age dataset and get associated chemical structures from drugs.
2. Cheminformatics sweep of aging drugs vs PDB + compound ligands. See if we can find some known binders we have a structure for.
3. Do a similarity search of the binding pockets of the known protein structures to AlphaFold modeled proteomic dataset for Humans + Animals.
4. Identify possible targets of the anti-aging compounds.
5. Read lots of papers on different deep learning, graph based approaches to knowledge based force fields people are using and don't even worry about MD or optimizing the protein structure. Sweep across the similar pockets of the human + model organism homology modeled proteomes.

### Download DrugAge
Download the data from [Humand Ageing Genomic Resources (HAGR)](https://genomics.senescence.info/download.html) into into [data](./data).