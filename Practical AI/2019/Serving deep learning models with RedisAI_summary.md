• Changelog sponsors: Fastly, Rollbar, Linode, DigitalOcean
• Practical AI podcast introduction and community invite
• Conversation about weather in Boston and Atlanta
• Introduction of Redis AI project with guest Peter Cayo from Redis Labs
• Background on Peter's career path to becoming a senior product manager at Redis Labs
• Introduction of a graph database example using Neo4j and its use in a bridge scenario
• Transition from Neo4j to Redis and experience with the company
• Explanation of Redis as an in-memory key-value store and NoSQL database
• Discussion on the difference between traditional databases and NoSQL databases
• Overview of various NoSQL database models, including graph databases, key-value stores, search databases, time series databases, and others
• Key-value stores and Redis' ability to store values other than strings
• List data type in Redis and its capabilities
• Set data type in Redis, including intersection and union operations
• Commands available for working with lists and sets
• Typical uses of Redis, including session caching and caching
• Redis as a queue or message broker, including streams data type and consumer groups
• Redis is open-source and released under the DSD license
• Modules within Redis have a Redis source available license with restrictions on creating database as a service
• Enterprise version of Redis is closed-source and includes enterprise features for scaling and database management
• Modules allow developers to create custom data types, structures, and commands
• Redis is not just a cache, but also effectively a database with tunable durability
• Data lives in memory first, then can be persisted
• Redis modules provide various features and client libraries for data structures and databases
• Popular Redis modules include:
  • Redis Search (inverted index)
  • Redis Graph (graph capabilities)
• Differences between graph native technologies and graph technology on top of other databases
• Advantages and disadvantages of each approach
• Graph logic and its application in the project
• Comparison of relational databases (O(log N) complexity) vs Redis graph database (O(1) time complexity)
• Features of Redis, including:
	+ Redis Bloom (probabilistic data structures)
	+ Redis JSON (JSON document splitting into a tree for atomic operations)
	+ Redis Time Series (time series capabilities)
	+ Potential features of Redis AI and Redis Gears
• Discussion on the importance of downsampled data in IoT applications
• The speaker discusses the concept of a multi-model database and how Redis Gears allows users to execute certain codes based on specific events.
• The speaker explains that multiple modules in a database do not necessarily make it a multi-model database, but rather the ability to run scripts and integrate different components does.
• The speaker introduces Redis AI and mentions that it is what they want to discuss further in their conversation.
• The background of Redis AI is discussed, including how the team was motivated to create it due to user requests for integrating AI models with Redis.
• Development of Redis AI module
• Need for data locality and DevOps part of publishing models
• Benefits of using Redis, including high availability, durability, and scalability
• Advantages of integrating models with Redis, such as getting "goodies" like database capabilities for free
• Importance of data locality in model deployment
• The model takes in two tensors: the latest message received by the chatbot and an intermediate state of the conversation.
• The model produces an output, which is a response, and a new intermediate state that serves as a new history of the conversation.
• Keeping the data close to the model is recommended to avoid latency caused by fetching large amounts of data from another database or host.
• Redis AI allows data structures to be created within Redis next to the model for faster inference and classification.
• There are three data structures inside Redis AI: tensors, scripts, and models.
• Integrating tensors into Redis for storage and use in AI applications
• Using Redis AI with modules such as scikit-learn and Spark
• Deploying models into Redis and running inference using client libraries
• Storing data structures like tensors, graphs/models, and scripts in Redis
• Executing scripts on stored data to perform tasks or answer questions
• Data preprocessing and combination using different data structures
• Inference with a model using graph data structure
• Post-processing and storing results in tensor data structure
• Combining multiple commands and models into a single call to Redis
• Pipeline-like execution of commands using Redis AI
• Using Redis as a knowledge base for text search, reading comprehension, and other tasks
• Vectorization and transformation of text data into tensors
• Mention of hosting knowledge graph in Redis graph
• Using Redis graph as a living database to evolve over time
• Routing logic between scripts, graphs, and tensors
• Renaming "graph" to "model inside Redis" for clarity
• Explanation of using Redis AI with PyTorch, TensorFlow, and Onyx Runtime as backends
• Discussion of Onyx Runtime's role in strategy around modules and its definition
• Combination of Redis ML and Onyx Runtime for machine learning
• Onyx provides an intermediate format between various frameworks (e.g., PyTorch, TensorFlow)
• Use cases include transforming models from one framework to another or uploading them into backends
• Backends are agnostic to model commands, allowing easy switching between different backends
• Client libraries can work with the same API regardless of backend changes
• Steps for implementing a knowledge graph or knowledge base article entries in Redis include:
  - Converting scikit-learn vectors to Onyx format
  - Creating and vectorizing articles with TF-IDF vectorizer
  - Saving vectorized articles back into Redis
• Python client for Redis AI
• Converting between different models using a conversion toolkit
• Using Onyx runtime to publish models inside Redis AI from within Python code
• Versioning and shipping models for DevOps
• Typical use cases for Redis AI, including transaction classification and fraud detection
• Data locality and scalability offered by Redis
• Familiarity with Redis among software engineers vs. data scientists and AI professionals
• Software engineers using Redis can potentially "bolt on" AI functionality to existing applications
• Positioning Redis AI as a general-purpose model serving framework, competing with TensorFlow Serving and others
• Collaboration between Redis Labs and TensorWork on Redis AI development
• Tooling and versioning systems for data, such as Hangar, being developed in conjunction with Redis AI
• Potential personas using Redis AI: data scientists, DevOps people, data engineers, and software engineers familiar with Redis.
• Development roadmap for Redis AI and its potential applications
• Future directions for the tooling and higher-level applications that might sit on top of Redis
• Connecting Redis Gears module to Redis AI for more efficient data processing
• Batching and performance statistics tools for model optimization
• Integration with existing ecosystem, such as Prometheus and Grafana, for monitoring and visualization
• Versioning models for tracking multiple versions or conducting A/B testing
• Contributing to the development of Redis AI and its tooling
• Quick start with Redis.io using Docker containers preloaded with backends
• Contributing to Redis.io through a Google group
• Feedback and issues on Redis.io GitHub project
• Link sharing for resources mentioned during the episode
• Show notes and further information available at changelog.com
• Community support and links to social media channels