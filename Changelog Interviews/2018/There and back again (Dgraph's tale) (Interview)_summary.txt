• Dgraph is a graph database described as the world's most advanced
• Manish R Jain, co-founder of Dgraph, shares his background and experience in building distributed systems, including his work on the Knowledge Graph at Google
• Dgraph was built to address limitations of existing graph databases, including scalability and consistency issues
• The project started as an open-source effort in 2015 and has since raised $3 million in funding and grown a large open-source community
• Dgraph's architecture is designed for distributed systems and includes features such as synchronous replication and linearizable reads
• The company is now in a place where Dgraph is close to being used in production at a few big companies
• Dgraph is written in Go and uses gRPC for communication
• The project initially used RocksDB as an embedded key-value database, but later developed Badger, a custom database written in Go, to improve performance
• Graph databases are often used as a secondary data store, but may be necessary as a primary data store for companies with complex data relationships
• Traditional relational databases like MySQL and Postgres are sufficient for small to medium-sized companies, but can become limiting as companies grow and data relationships become more complex
• Graph databases are particularly useful for companies with large amounts of data that require recursive queries and complex relationships
• Dgraph has been successfully used to build complex data-driven applications, such as question-answering websites, by leveraging its query language and ability to retrieve complex data in a single operation.
• Recursive data fetches and graph databases
• Using GraphQL as a query language for graph databases
• Modifying the GraphQL spec to create a new query language, GraphQL+-
• Graph database use cases, including real-time recommendations, fraud detection, identity reconciliation, and data silo unification
• Graph databases as a single, unified database
• Artificial intelligence applications and Google's use of graph databases
• Simplifying data modeling with graph databases
• Power of graph databases in joining data points
• Traditional relational databases vs graph databases
• Limitations of graph databases, including flat data and time series data
• Deployment and maintenance of graph databases
• Distributed database system with sharding and replication for high availability
• Consensus algorithm (Raft) ensures data consistency and replication across replicas
• Linearizable reads ensure freshness of data, even in case of node crashes
• Trade-off between consistency (CP) and availability (AP) in the CAP Theorem
• Dgraph uses a permissive Apache license, allowing for adoption and feedback
• Discussion of open core and open source business models
• Importance of feedback over code contributions in open source projects
• Comparison of AGPL and GPL licenses, with AGPL being considered a viral license
• The GPL and AGPL licenses were discussed as solutions to the issue of companies using open-source software without contributing back
• The AGPL was seen as a fix for the GPL's "loophole" in dealing with server-side code
• The Commons Clause was introduced as a solution to prevent companies from using open-source software without contributing back
• The Commons Clause prohibits the sale of software that is substantially the same as the original code
• Google banned the Commons Clause, and other companies such as Facebook and Apple were also hesitant to use AGPL code
• The issue of balancing permissive licenses with protection against companies exploiting open-source software was discussed
• The decision was made to switch from AGPL to Apache license due to the Commons Clause being banned by Google
• The Cockroach license was mentioned as an alternative to the AGPL that adds an enterprise license on top of the Apache license
• Dgraph switched to Apache license and plans to build enterprise modules with source visibility.
• The Commons Clause is discussed, with Manish R Jain defending it as being in the spirit of open source.
• AGPL (GNU Affero General Public License) and SSPL (Server Side Public License) are mentioned as stricter licenses than the GPL.
• The conversation touches on the issue of large companies like Amazon being restricted by the Commons Clause from selling Redis and other codebases.
• The discussion concludes with a debate on the merits of the Commons Clause and the intentions behind its use.
• The challenges of building a database that others will base their tech stack on, and the importance of trust in the codebase.
• The tension between proprietary and open-source models, and the difficulties of selling proprietary software.
• The Commons Clause and its implications for open-source development, and the need for clearer terminology.
• The importance of sustainability in open-source projects, and the need for developers to be able to profit from their work.
• The three models of making money with open-source software: open core, support and training, and running the software as a service.
• Open source licensing and the potential for "leeching" off other projects without contributing back
• The Commons Clause and other licenses (such as GPL and AGPL) that aim to dissuade non-contributors from benefiting from open source projects
• The need for evolution and practical considerations in open source licensing, particularly for companies using open source software as a service
• The potential impact of MongoDB's SSPL license on the open source community and the need for a bigger dialogue around these issues
• The importance of finding a balance between open source ideals and practical considerations in running an open source company
• The need for meaningful change and a willingness to have difficult conversations in the open source community