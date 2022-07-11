import json
#version 1.0
#Author(s): Rohan Panigrahi

class Dictionary:
    BCOdictExtraInfo = {
        "Alignment" : "Sequence alignment is a way of arranging protein sequences to identify regions of similarity that may be a consequence of evolutionary relationships between the sequences. Tool - Bowtie2",
        "Variant Calling" : "The Process of identifying variants from sequence data. Tool - Heptagon",
        "Filtering" : "The process of removing genes deemed irrelavent from the set of genes being analyzed. Tool - metaseqR",
        "Annotation" : "The process of identifying functional elements along the sequence of a genome, thus giving meaning to it. Tool - dbSNP",
        "Enrichment" : "A computational technique which determines whether a priori defined set of genes show statistically significant differential expression between two phenotypesTool - DAVID", 
        "Cluster" : "Clustering or cluster analysis is the process of grouping individuals or items with similar characteristics or similar variable measurements.  Tool - NCSS",
        "Data Visualization and Processing" : "The practice of translating information into visual context. Tool - Gwyddion",
        "Metagenomic Analysis" : "Metagenomics provide access to functional gene composition of microbial communities. Tool - Kraken2"
    }
    BCOdict = {
        "Alignment" : "Bowtie2",
        "Variant Calling" : "Heptagon",
        "Filtering" : "metaseqR",
        "Annotation" : "dbSNP",
        "Enrichment" : "DAVID", 
        "Cluster" : "NCSS",
        "Data Visualization and Processing" : "Gwyddion",
        "Metagenomic Analysis" : "Kraken2"
    }
    
    # Serializing json  
    json_object = json.dumps(BCOdict, indent = 4) 
    print(json_object)