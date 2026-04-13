• Definition of data and database
• Explanation of vectors in a compressed data representation with semantic information
• Introduction to vector databases as purpose-built databases for efficiently managing vectors at scale
• Discussion of semantics and its relation to query understanding and meaningful results
• Comparison of vector databases to other types of databases (relational, NoSQL)
• Origins of SQL databases in the 1970s with relational algebra formalization
• Relational data model and its limitations for handling complex, interdependent data
• Emergence of NoSQL movement in the mid-2000s due to inflexibility of schema-based approach
• Benefits of schema-less approaches, such as storing semi-structured JSON blobs and documents
• Challenges with NoSQL databases, including divergence from SQL language standard and lack of dependency among data
• Developer-friendly interfaces for databases
• SQL vs NoSQL database systems
• Evolution of NoSQL databases and the emergence of vector databases
• Vector databases as an extension to NoSQL or a distinct category
• History and development of full-text search in databases, including inverted indexes and algorithms like BN25
• Bag of words approach vs NLP analogy
• Transformer revolution and its impact on text encoding and semantics
• Vector databases and their connection to transformers
• Definition and explanation of vector-based semantic search
• Applications of vector databases in AI workflows, including querying data via natural language
• Current state of marketing in vector databases and their potential uses with large language models (LLNs)
• Discussing natural language processing (NLP) and its application in database queries
• Exploring the trade-offs between using existing databases versus purpose-built vector databases
• Considering the performance implications of adding vector functionality to existing databases (e.g., Postgres with PG Vector)
• Weighing the benefits and drawbacks of using an existing database versus a purpose-built one for vector-based applications
• Discussing the importance of scalability, efficiency, and access to latest algorithms in choosing a vector database solution
• Purpose-built solutions for vector search and information retrieval may be more effective than using general-purpose databases with added vector capabilities.
• Using a database that allows building custom embedding pipelines versus relying on built-in hosted pipelines is a trade-off to consider.
• Embedded API options from certain database vendors can simplify the process of working with vectors, but may not offer optimal performance.
• Embedding work should be done upstream to optimize efficiency and cost
• Vector databases have two key stages: input (indexing) and query (inference)
• Indexing is an upstream process, bringing data in and making it searchable
• Query stage involves transforming user input into a compatible vector embedding
• Trade-offs between indexing speed and query speed depend on use case and requirements
• Some vendors focus more on one end of the pipeline than the other
• Milvus is mentioned as a mature, open-source purpose-built database for vector storage
• Purpose-built versus existing database solutions
• External embedding pipeline versus built-in hosting pipeline
• Indexing speed versus querying speed
• Recall versus latency in search results
• In-memory index versus on-disk index
• Sparse versus dense vectors for underlying indexes
• Hybrid search combining full-text and vector search
• Importance of filtering: pre-filtering versus post-filtering
• HNSW (Hierarchical Navigable Small World graphs) vector indexes are popular but memory-hungry
• The "trillion scale vector problem" requires indexing large datasets that don't fit in memory
• Vendors use various solutions to address the out-of-memory issue, including MemMap and disk-based storage
• Vamana is a new index optimized for solid-state disk retrievals using the Disk ANN algorithm
• Implementing HNSW on disk can reduce performance significantly
• Disk ANN is considered a standard approach but requires custom implementation for each database language
• Lance DD is a young database vendor that only supports on-disk indexes and has innovated its underlying storage layer.
• Performance of open-source vector databases
• Trade-offs between on-disk and in-memory storage
• Comparison of Quadrant, VV8, and LanceDB database architectures
• Future trend towards on-disk indexing as a standard
• Options for vector databases in cloud, edge, and embedded environments
• Embedded vs client-server architecture debate
• Comparison of Pinecone, DuckDB, and LanceDB solutions
• Infrastructure-related hurdles of cloud-based solutions
• Advancements in embedded databases and vector databases
• Competition between database technologies to offer business value at scale
• Emerging applications of vector databases, including search solutions and retrieval-augmented generation
• Intersection of graph databases and vector databases for knowledge graphs and connected data
• Potential for vector databases to enable scalable, reliable search engines and information retrieval solutions
• Vector databases and their potential for factual knowledge retrieval
• Challenges with conventional graph algorithms and languages in querying complex data
• The power of natural language querying interfaces enabled by LNMs (Language Models) on top of vector databases
• Enhanced retrieval and generation capabilities through the integration of tools like Langchain or Lava Index
• Strategic combination of technologies to achieve effective solutions