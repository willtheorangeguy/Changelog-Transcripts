• Introduction to Graph databases
• History of Neo4j (19 years old)
• Challenges with traditional relational and NoSQL databases for storing graphs
• Benefits of using a Graph database for data modeling and querying
• Overview of Dgraph as an open-source, distributed Graph database written in Go
• Discussion of index-free adjacency and its role in efficient graph storage and querying
• Key-value storage structure vs traditional databases
• Partitioning data by predicate for improved scalability and performance
• Use of Badger, an open-source key-value store, with a log-structured merge tree (LSM) implementation
• Graph database applications beyond social networks, including knowledge graphs, geographic graphs, and dataset integration
• Advantages of graph databases over traditional databases for complex queries and dataset integration
• Indexes in graph databases are not always necessary for traversing relationships
• A schema may still be required to find initial nodes or handle specific queries
• Dgraph allows for a schema-less approach during development, but recommends locking the schema in production
• A type system can be added on top of a graph database for optional schema enforcement
• Rebuilding indexes after changing the schema is possible, but may take some time and temporarily limit mutations
• Having a schema or type system in place can help prevent data inconsistencies and errors in production.
• Data modeling should be straightforward and natural
• Graph databases can handle flexible schema with ease
• Relational databases require more forethought in data structure and indexing
• Migrating data between different structures is easier in graph databases
• Development advantages come from being able to adapt and migrate the data
• Switching between dev mode and prod mode involves creating a schema from seed data and then locking it down.
• Dgraph's serving mode has three options: standard, strict, and read-only
• Dgraph is designed to be distributed and fault-tolerant with multiple replicas of data
• Data replication occurs across groups, with each group having its own replicas and leaders
• GraphQL can be used as a layer on top of existing databases, but presents challenges like caching and the N+1 problem
• Dgraph's GraphQL implementation is adapted from GraphQL+- to make it more database-friendly
• Current analysis tools for Dgraph are limited, but a query planner is in development and OpenCensus is available
• Distributed traces as a knowledge tool
• Benefits of having control over system architecture and data storage
• Use cases for graph databases vs. relational/ document databases
• Challenges of managing relations in relational databases
• Strategies for integrating graph databases with existing systems
• Data storage format and structure within Dgraph
• The ZW (zero write-ahead log) folder contains configuration data for the database cluster
• Badger, the key-value store, requires SSDs for optimal performance but can work with other storage solutions
• A diskless mode is being developed to store data in memory instead of on disk
• Ristretto is a caching mechanism being integrated into Badger and Dgraph to improve performance
• Writing a cache in Go is challenging due to complexities in memory management and object sizing
• Discussion about ristretto and its relation to coffee
• Comparison between RAM capacity and scientific approaches to computing needs
• Introduction of Dgraph.io and Francesc Campoy's work
• Announcement of FOSDEM conference in Belgium (February 1st-2nd) and call for proposals