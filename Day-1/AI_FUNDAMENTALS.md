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

# What is a RAG?

RAG (Retrieval-Augmented Generation) is an AI technique that improves the accuracy of a Large Language Model (LLM) by allowing it to retrieve relevant information from an external knowledge source before generating a response

Instead of relying only on what it learned during training, the LLM first searches for relevant information and then uses that information to answer the user's question

**Why do we need RAG?**

LLMs has two major limitations:
- Knowledge Cutoff - it only knows information it was trained on.
- Hallucinations - it can confidently genrate incorrect information.

To overcome these 2 limitations RAG is used which gives LLM the information required to answer the prompt

**How RAG works?**
1. Gather all the documents you want the LLM to know
2. Split the Documents into chunks
3. Convert each chunk into a embedding
4. Store embedding in a Vector Database
5. User asks a Question ?
6. Convert the question into an embedding
7. Similiarity Search
8. Send retrieved chunks to the LLM
9. Genrate the final answer
