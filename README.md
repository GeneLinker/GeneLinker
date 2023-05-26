## Welcome to GeneLinker

# Why GeneLinker?

GeneLinker is an open-source package dedicated to secure data sharing of genomic data. It allows you to maintain control of your sequence data, while still allowing potential users to search it and retrieve standardized product passport information for each gene. Learn more at our [site](genelinker.com)

# How Do I Get Started?

This repository only contains a proof of concept implementation which will be expanded in the coming weeks. The most important thing to understand is that you and your broker will be able to communicate via a standardized protocol. The GeneLinker code will allow you to only communicate back key metadata to the broker, not your actual sequences. An example of how this might be possible is provided in our POC App

## Running the POC app

# First steps

1. Install dependencies

```
pip install flask 
pip install biopython
python app.py reference2.fasta
```

2. Visit site: http://localhost:5000/index.html

3. Use api key of key1 and search for MADW or similar sequence

# What just happened?

You can see that only a product passport has been communicated back to the caller of this API.

# What's next?

GeneLinker will soon contain additional functionality for communication of a more robust product passport as well as further best practices for secure and federated search. Please stay tuned and contact us at team@genelinker.com if you wish to be part of this effort.
