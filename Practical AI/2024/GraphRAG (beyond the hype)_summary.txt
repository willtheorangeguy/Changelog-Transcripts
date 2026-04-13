• Introduction to the Practical AI podcast
• Annie Sexton discusses Fly.io and its features
• Fly.io's partnership with Tigris for object storage
• Benefits of using Fly.io, including flexibility and ease of use
• Deployment of applications on Fly.io, including global anycast load balancing and instant wire guard VPN connections
• Introduction to the next episode of Practical AI podcast
• Vector databases and trade-offs between different types
• Transition to a data company working with a new type of data
• Introduction to Kuzu, an open-source embedded graph database
• Graphs and knowledge graphs: definition, representation, and application
• Combination of vector search and graph databases for advanced retrieval systems
• The speaker mentions the difference between machine learning and AI but doesn't consider it important for their discussion.
• Graph databases are compared to relational databases, with graph databases being better suited for data with complex relationships.
• Examples of industries where graph databases can be useful include medicine and finance due to interconnected data points.
• A Property Graph Data Model is mentioned as the most popular model used in graph databases, invented by Neo4j.
• The speaker highlights the intuitive nature of graph databases for querying connected data.
• Concrete examples are given, including personnel-related data and a hypothetical biomedical scenario.
• Data lakes and relational databases as primary stores for certain datasets
• Using graph databases to represent data in different scenarios (healthcare, finance, traffic networks)
• Knowledge graphs and their application in complex data modeling
• Property graph model for tabular data or records
• Universal One speech AI model by Assembly AI
• Playground interface for interacting with Assembly AI models and API without coding
• Retrieval Augmented Generation (RAG) is explained as combining retrieval capabilities with generative models
• RAG emerged prior to the term Large Language Model (LLM) in early 2020 due to generative model improvements
• Generative models are not new, but their generation capability is what's novel in RAG
• Early RAG approaches used sequence-to-sequence language models and dense embeddings for retrieval
• The arrival of vector databases in 2021 made RAG scalable and easier to use
• Limitations of traditional RAG include relying on sentence-level embeddings and keyword-based search methods
• Hybrid search combines sparse and dense vector search, but can also have limitations
• Exploring explicit relationships between entities is a further option being explored
• The relationship between a professor and their students can be implicit in text, but graph-based methods like Graph RAG can model relationships explicitly
• Vector search may not capture relationships correctly, leading to hallucinations in LLM output
• Graph RAG combines vector embedding with graph traversal to provide additional context for generation
• Hallucination is an inherent risk when using LLMs for text generation, regardless of the source of information
• The benefit of Graph RAG is that it increases factual accuracy by explicitly capturing relationships not captured in vector embeddings
• Implementing Graph RAG requires a data side setup with indexing and retrieval stages
• Extracting entities and relationships from unstructured data
• Using LLMs to help with information extraction
• Storing extracted triples in a graph database
• Option to store vector embeddings in a separate vector database
• Indexing stage: extracting entities, relationships, and vectors for future retrieval
• Serving stage: user query is transformed into an embedding, similarity search on vector database, and graph query on graph database
• Combining retrievals using re-ranker to provide additional context to LLM
• Example of practical application with Kuzu graph database and LanceDB vector database
• Using a text sample about Madam Curie to demonstrate extraction of relationships between entities
• Pierre Curie's collaborations with Madam Curie and Paul Langevin
• Using vector search vs graph search in retrieval accuracy
• Combining vector search and graph reversals to improve retrieval accuracy
• Graph RAG (Retriever-Augmented Generator) as a suite of tools for enhancing retrieval and generation
• Challenges in constructing graphs from existing data, including quality of the graph and extracting triples/relationships from unstructured text
• Use of frameworks like Lama Index and Langchain to aid in graph construction and entity extraction
• Reproducibility issues with LLMs
• Alternative models for extracting triples from text (e.g. Rebel, Relic)
• Spacey NLP library and its add-on modules (Gliner, Glyrel) for entity recognition and relationship extraction
• Comparing use of LLMs vs. custom models for data extraction
• Future directions for graph-based search and AI development
• OpenAI's O1 model demonstrates reasoning capabilities
• LLMs may eventually replace custom models and machine learning tasks
• Graph-based agents are being explored, with potential for more powerful systems
• Knowledge graphs and symbolic systems could be combined with statistical models
• GraphRag is a small part of the broader field of graph databases and their applications