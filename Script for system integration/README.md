# Instruction on using the script for system integration

1) Create (or import from the database) the working dataset as "corpus". It should contain the following columns: "geonameid", "alternate_name" (**please rename as "name"**), "region", "country", "population". A merge of a few (in our case, four) datasets might be required to achieve this.

2) Run the following code:
   
   `%load_ext autoreload`
   
   `%autoreload 2`

4) From the script import the "clear_text" function.

5) Apply it to the "name" column of the working dataset.

6) Turn the column into values using:

   `names = corpus.name.drop_duplicates().values`

7) Create embeddings with the Sentence Transformer:

   `labse = SentenceTransformer('sentence-transformers/LaBSE)`
   
   `embeddings = labse.encode(names)`

9) Enter a query (for example, **'Киров'**) and run the code:

   `result = pd.DataFrame(util.semantic_search(labse.encode('Киров'), embeddings)[0])`
   
   `result = result.assign(name=names[result.corpus_id])`

11) From the script import "MyClass"

12) To get the required list of tuples run the code (where the "result" and "corpus" are the datasets from line 7 and line 4, respectively):
   
    `MyClass(result).geo(corpus)`

   
   
