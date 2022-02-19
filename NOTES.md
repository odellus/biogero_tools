# Project Notes

## Reverse screening of aging related compounds  

So the idea is that we've got a bunch of drugs that have been show to extend lifespans in all the model animals and now we want to attempt to map them back onto the targets to identify aging pathways and mechanisms.

1. ~~Download the drug age dataset and get associated chemical structures from drugs.~~
2. Cheminformatics sweep of aging drugs vs PDB + compound ligands. See if we can find some known binders we have a structure for.
3. Do a similarity search of the binding pockets of the known protein structures to AlphaFold modeled proteomic dataset for Humans + Animals.
4. Identify possible targets of the anti-aging compounds.
5. Read lots of papers on different deep learning, graph based approaches to knowledge based force fields people are using and don't even worry about MD or optimizing the protein structure. Sweep across the similar pockets of the human + model organism homology modeled proteomes.


## References
1. [The DrugAge database of aging-related drugs](https://onlinelibrary.wiley.com/doi/full/10.1111/acel.12585)  

2. [Reverse Screening Methods to Search for the Protein Targets of Chemopreventive Compounds](https://www.frontiersin.org/articles/10.3389/fchem.2018.00138/full)  

3. [AlphaFill: enriching the AlphaFold models with ligands and co-factors](https://www.biorxiv.org/content/10.1101/2021.11.26.470110v1.full)  

4. [Is anti-ageing drug discovery becoming a reality?](https://www.tandfonline.com/doi/full/10.1080/17460441.2020.1702965)

5. [Identification of longevity compounds with minimized probabilities of side effects](https://link.springer.com/article/10.1007/s10522-020-09887-7)

## TODO
1. Use entrez API to get pubchem ids for drugs in DrugAge db and download structures /info from pubchem.
2. Take the known list of known binders for which we have a structure and expand the search a bit with chemically similar compounds.
3. Keep adding to the list of references. There have been a few methods I've seen that might be applied to this project that I haven't put in the references but instead just tweeted out.
4. Aside from just tweeting about the papers that are related to the project, try reading them also. I'm sure there's a lot of useful information contained within.


## Journal

19 Feb 2022

So far I'm at step 2 of the process, which is a cheminformatic sweep of the different compounds contained in DrugAge to get a list of potential binders that I can then sweep across the compounds contained in PDB or even some predicted docking datasets (alphafold + compound anyone?)

So I've been working on this. So far I've sent a punch of requests to ncbi and even added a `get_sdf(cids)` function which pulls a 3D SDF model back from pubchem. They have a structural search function which I can use to pull back even more compounds that are structurally similar to the compounds in DrugAge.