import matplotlib.pyplot as plt
import pandas as pd

sequences = pd.read_csv('data/marine_sequences.csv')

gc_contents = {}
for index, row in sequences.iterrows():
  species = row['Species']
  sequence = row['Sequence']
  g_count = sequence.upper().count('G')
  c_count = sequence.upper().count('C')
  sequence_length = len(sequence)
  if sequence_length > 0:
    gc_content = (g_count + c_count) / sequence_length * 100
  else:
    gc_content = 0
  gc_contents[species] = gc_content

print("GC content for each species:")
for species, gc in gc_contents.items():
    print(f"{species}: {gc:.2f}% GC content")

species_names = list(gc_contents.keys())
gc_values = list(gc_contents.values())

plt.bar(species_names, gc_values)
plt.xlabel("Species")
plt.ylabel("GC Content (%)")
plt.title("GC Content of DNA Sequences")
plt.show()