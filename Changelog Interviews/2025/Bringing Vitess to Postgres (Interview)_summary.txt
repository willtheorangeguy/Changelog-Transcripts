• Sugu Sougoumarane's three-year sabbatical and decision to return to work
• Reasons for taking sabbatical: burnout and completing a 12-year project on Vitess
• History of Vitess and its purpose: a database scaling solution to address YouTube's scalability issues
• Sugu's role at PlanetScale and his relationship with co-founder Sam Lambert
• Sam Lambert's role at PlanetScale and his impact on the company
• Industry changes and the continued importance of databases and infrastructure
• Development of Vitess as a database connection pooler that evolved into a fully sharded solution
• Vitess' adoption by companies such as Flipkart, HubSpot, and Slack
• Plans to port Vitess to PostgreSQL, including initial discussions and false starts
• The challenges of sharding, including the lack of practical implementations and the need to reinvent the concept from the ground up
• The technical difficulties of sharding, including understanding SQL, query complexity, and relational algebra
• The process of inventing a solution to shard a database, including a breakthrough moment after months of intense thinking
• Sharding is difficult because it requires a different way of thinking about query execution and optimization
• The speaker's "a-ha" moment came when they realized that the application was already computing keyspace IDs and that the system could do it instead
• The system can support full SQL language with the use of relational algebra and route primitives
• Keyspace ID can be computed using various methods, including hashing user IDs
• The speaker's team initially used a random assignment method for keyspace ID, but later transitioned to a unique ID system
• Vitess supports various sharding schemes, including range-based, hash-based, and lookup-based, and allows users to choose the scheme they want to use.
• Illustra was a commercialization of Postgres that introduced pluggable indexes, inspiring the concept of externally defined indexes.
• Vitess is being ported to Postgres, with the goal of maintaining a Postgres-native solution.
• The Vitess team is leaving behind legacy and poorly implemented components, but bringing over high availability components to improve Postgres' HA story.
• The team is struggling to determine how to port Go-based plugins to Postgres, which could compromise the native Postgres goal.
• The team aims to reuse as much knowledge and code from Vitess as possible, considering the significant time and effort invested in its development.
• Discussion about coming out of retirement to work on Supabase
• Explanation of why Sugu chose to start Supabase with a existing company rather than as a startup
• Importance of open source and adoption in project success
• Timeline and goals for Supabase's MVP and future development
• Debate about using Go to write Postgres extensions and potential alternatives
• Exploring options for linking to Cgo and translating AI for use in Vitess
• Considering a new approach to development, potentially leaving Go and using C directly
• Addressing technical challenges and trade-offs, including flexibility and approachability
• Building a new team for the Multigres project, including hiring high-caliber engineers and contributors
• Planning for implementation and deployment of Multigres, including a Kubernetes operator and potential use in Supabase
• Discussing the importance of testing and validation, particularly at scale, in order to ensure that the system works as intended.
• Implementing a rigorous testing policy to ensure code reliability and confidence in the product
• Considering porting or copying test suites from Vitess to speed up development
• Determining the licensing for the project, with a plan to use Apache
• Debating whether to create a new project or fork Vitess, with a goal of allowing the project to evolve independently
• Addressing the need for high availability and consensus in database systems, and the importance of storage being integrated with the database
• Planning to cover high availability and consensus in upcoming blog posts
• Supabase's need for a scalable solution for Postgres
• The limitations of existing solutions like Neon and Aurora
• Sugu Sougoumarane's goal of creating a sharded solution for Postgres
• The absence of a solution like Vitess for Postgres
• Sugu's decision to come out of retirement to work on Multigres
• The potential impact on Postgres and the Postgres community