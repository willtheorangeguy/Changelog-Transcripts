• Python vs Ruby
• Django framework and batteries included
• Postgres as a database with batteries included
• Features of Postgres
• Changelog podcast and sponsors (Fastly, Rollbar, Linode)
• Interview with Craig Kirstens, a Postgres aficionado
• Craig's involvement with the Postgres project and his love for the database
• Working with people, particularly at startups and companies like TruViso and Heroku
• Early experiences with complex events processing and transforming Postgres into a streaming database
• Sharing knowledge through blogging, including the importance of getting content out quickly and imperfectly
• Interacting with app developers, including troubleshooting and providing solutions to common problems
• Speaking to developers rather than being a DBA
• The challenge of directing people to online resources, such as blog posts, rather than providing immediate answers
• The growth and decline of TruViso and the speaker's move to Heroku
• The speaker discusses the origins and history of Postgres and its roots in the Ingress database from UC Berkeley.
• The speaker notes that many databases, including Sybase and SQL Server, have the same root as Postgres.
• The speaker shares their personal experience with Postgres, starting with Heroku, where they helped build Heroku Postgres, and now working at Crunchy, building and running their cloud service based on Postgres.
• The speaker recalls the shift from MySQL to Postgres as the preferred database for Rails developers, and attributes this shift in part to Heroku's influence.
• The speaker discusses the evolution of Postgres, including its growing user-friendliness and the addition of features such as JSON support.
• The speaker notes that Postgres gained mainstream recognition, including a standing ovation at an Amazon conference, and speculates about why Postgres is so beloved among developers.
• The speaker switched to PostgreSQL from MySQL due to its reputation for being safe and reliable.
• The ease of switching to PostgreSQL in Rails environments was a factor in the speaker's decision.
• Postgres's focus on being safe and reliable was its core value, rather than adding new features.
• MySQL has had issues with data loss and corruption, which was a concern for the speaker.
• The speaker appreciates the reliability of PostgreSQL and values trustworthiness in a database.
• The speaker distinguishes between areas of their application where they can experiment with new features and areas where reliability is paramount.
• The speaker recounts their positive experience with PostgreSQL and contrasts it with the potential consequences of data loss.
• Origins of Postgres and its evolution from Ingres
• History of Postgres development at UC Berkeley
• Community-driven development and stewardship of Postgres
• Notable contributors to Postgres, including Tom Lane and others
• Open-source development process and governance structure
• Unique aspects of Postgres' community-led development and management
• Comparison of Postgres to other open-source projects, such as Linux
• Entity set up to maintain copyrights and licensing for Postgres
• Core team acts as a steering body with 5 members, no more than 2 from any one company
• Distributed development with multiple companies involved
• Commitment-based development with contributors reviewing patches
• Postgres released with a major release once a year
• Reviewing patches is key to building credibility and contributing to the project
• Postgres C code is well-structured and well-defined, allowing for active development and maintenance
• Technical debt is managed through refactoring and good architecture
• Contributors earn a commit bit and must stay active to maintain it
• Self-accountability among contributors ensures code quality.
• Postgres stability and data consistency
• NoSQL trend and relational databases being "thrown under the bus"
• JSON feature in Postgres and its addition 8 years ago
• Debate around SQL, NoSQL, and schemaless databases
• JSONB data type and its binary representation
• Feature flags as an example of using JSONB in Postgres
• JSON vs JSONB: when to use each
• Indexing and querying requirements
• Use cases for JSON: logging, API logs, preserving whitespace
• JSONB advantages: indexing all keys and columns, faster querying
• Heuristics for choosing between JSON and JSONB
• Relational vs NoSQL databases and schema design
• Using JSONB for optional extra fields and settings
• Flexibility of Postgres for adding new columns to tables without migration
• Use of lightweight tables on objects for storing nested data
• Limitations of NoSQL databases for analytics and querying complex data
• Importance of relational algebra and calculus for understanding SQL power
• Postgres features such as JSON, JSONB, and indexing
• Advantages of Postgres indexing, including GIN indexes for JSON data
• Use of array data type in Postgres for efficient storage and querying of multi-value columns
• GIN and GIST indexes in PostgreSQL
• Overlap of values between rows and indexing for full text search
• Geospatial indexing with GIST and SPGIST
• Clustering of phone numbers and zip codes for indexing
• Index types in PostgreSQL, including B-tree, GIN, and GIST
• Contributions from the PostgreSQL community, including the "Russian" group
• PostGIS as a separate module or extension in PostgreSQL
• Upgrade cycle of Postgres vs. PostGIS
• Challenges of maintaining PostGIS
• Extension of Postgres, with own community and development path
• Full-text search in Postgres and its capabilities
• Notify, a pubsub system within Postgres for queueing and background jobs
• Postgres is a stable and reliable workhorse database with regular feature updates.
• Postgres 13 is a recent release that exemplifies the trend of incremental updates rather than flashy new features.
• Extensions in Postgres allow for low-level hooks and customizations, including new data types and functions.
• Extensions can be written in various languages, including SQL, C, and others.
• The Postgres community is utilizing extensions to create new features and functionality, which can later be incorporated into the Core database.
• Examples of extensions include PostGIS and HStore.
• Extensions have the potential to greatly expand the capabilities of Postgres.
• Postgres extensions for sharding and distribution
• PostGIS and other spatial extensions
• pgcron for cron functionality within the database
• Procedural languages such as plv8 and plpython
• Data types such as hstore and JSON
• Madlib for analytics and data science functionality within Postgres
• PLPython: a Python module for Postgres
• Using PLPython to write a recommendation engine in 20 lines of Python
• Integrating Python code directly into the database
• Rethinking the "gospel" of never putting logic in the database
• PLV8 and JavaScript support in Postgres
• Comparison of writing SQL vs. writing Python or JavaScript
• Creating and executing functions in Postgres using Python
• Packaging functions with extensions (e.g. Madlib)
• Writing and deploying custom extensions in Postgres
• Practical example of using PLPython to write a Python script in a Postgres function
• Using PSQL from the command line and editor integration
• Backslash timing shows how long a time query took to run
• Customizing PSQL editor settings can improve productivity
• Displaying null character values as emojis can help identify nulls
• Postgres extensions for time series and sharded data management
• Integrating JavaScript and other tools with databases
• Zombo DB synchronizes Postgres data with Elasticsearch for full-text search
• Developers can expect more innovative extensions and integrations in the future
• Elasticsearch integration with Postgres for full-text search
• Pluggable storage engines in Postgres, allowing for different storage engines
• Zheap backend, a new storage backend that aims to improve vacuum performance and space usage
• ZedStore, a Columnar storage engine that stores data by columns, useful for time series data
• Discussion of various trade-offs and limitations of each new feature and storage engine
• The advantages of using Postgres for non-traditional workloads, such as data warehousing
• The concept of pluggable storage and its potential to expand what Postgres can do
• The evolution of Postgres-based products, such as Amazon Redshift
• The importance of extensions and pluggable storage for future development
• Resources for learning and staying up-to-date with new Postgres features, including Postgres Weekly and Planet Postgres
• The importance of learning about Postgres internals and basics
• Recommended mailing lists and communities for Postgres:
  - PG-SQL hackers mailing list
  - PG-SQL users mailing list
  - Postgres team community Slack
  - PostgresQL IRC
• Resources for debugging slow queries and troubleshooting issues
• The existence of blogs and other online resources, but some being redundant
• Links to mentioned resources to be included in show notes