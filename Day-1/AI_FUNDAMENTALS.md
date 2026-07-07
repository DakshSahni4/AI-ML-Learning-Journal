# What is an LLM?
A LLM ( large language model) is a transformer-based deep learning architechture that is a next word predictor transformer. It is trained on massive text data, such as books, websites, social media like Reddit, to learn to write in a specific human language by learining the patterns of it.

An LLM can do multiple task without explictly training it for them:
- Language translation
- Question answers
- Write emails, code etc
- summarize documents
- Topic catrgorization

**How it works:**
1. It reads billions of text examples during training
2. It learns to predict the most likely next word in a sentence
3. By repeatedly predicting the next token, it genrates the complete response

# What are Embeddings?

Embeddings are dense vector representations of words in a language that captures their semantic meaning . Words with similiar meaning will have a have a similiar position in the multi-dimensional vector space.

**Why are embeddings useful?**

Embeddings are used to convert unstructured text data into structured numerical vectors that deep learning models can understand and process. Since deep learning models work with numbers rather than raw text, embeddings provide a way to represent the meaning of words, sentences, or documents in a numerical form.

# What is a Vector Database?

A Vector Database is a specialized database designed to store, manage, and search vector embeddings efficiently. Instead of searching for exact keyword matches, it finds data that is semantically similar by comparing the distance between embedding vectors.

A vector database is essential in AI applications because embeddings are high-dimensional numerical vectors, and traditional databases are not optimized to search through them efficiently. It enables fast similarity search, making it possible to retrieve the most relevant documents, images, or other data based on meaning rather than exact words.