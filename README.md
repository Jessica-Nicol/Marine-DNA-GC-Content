# Marine DNA GC Content Analysis
### This project analyses the GC content in DNA sequences for different marine species. The data is taken from a CSV file using pandas and results are plotted onto a bar chart using matplotlib.pyplot
## The Dataset
The dataset used for this project can be found in the [marine_sequences.csv](marine_sequences.csv) file, each row represents a species and its corresponding DNA sequence.
## GC Content
The GC content is calculated by taking the number of Gs and the number of Cs in the sequence, dividing it by the number of total bases, and multiplying by 100.

GC content is important to analyse in DNA as it provides insight into genomes. Some reasons why this is important is analysing genome stability, comparative genetics, and environmental adaptaion.
## How to Run
1. Install the dependencies needed
```bash
pip install matplotlib pandas
```
2. Run the analysis script (gc_analysis.py)
## Visualisation
The bar chart displays species on the x-axis and their corresponding GC content (%) on the y-axis.