• Craig Kerstiens' involvement with Postgres started at a startup, Truviso, where they transformed Postgres into a streaming database
• He then moved to Heroku, where he helped establish Postgres as a preferred database for Rails developers
• Heroku's influence and the introduction of Heroku Postgres likely contributed to the shift from MySQL to Postgres among Rails developers
• Craig Kerstiens has contributed to the Postgres community through blogging, speaking, and teaching, but not through code contributions
• Postgres is considered a solid and sturdy database, with a long history and roots in Ingres, which has influenced many other databases
• The introduction of JSON support and other features has made Postgres more "sexy" and appealing to developers
• The speaker's experience switching from MySQL to Postgres due to data consistency problems and Postgres' reputation for reliability and consistency
• The differences between MySQL and Postgres, including MySQL's case-insensitive search and Postgres' focus on safety and reliability
• The evolution of Postgres from its Ingres roots and its development at UC Berkeley, with a focus on extensibility and community stewardship
• The community and development process of Postgres, including the work of Tom Lane and other major contributors
• The unique nature of Postgres as an open-source project, with no single entity owning the code or copyright
• The Postgres community is community-led, community-run, and community-managed, with a unique governance structure
• The core team is a steering body that oversees the project, with no single company in control
• Development is distributed across companies, with a focus on community involvement and participation
• Committers earn credibility through contributions, reviews, and patches, with a yearly commitment expected
• The project has a well-structured C codebase, allowing for efficient development and maintenance
• Postgres has added features like JSON support, XML data types, and has been able to keep pace with changing technology trends
• The project has a strong focus on community involvement, with a culture of accountability and self-regulation among contributors
• Postgres used JSON for validation, but later introduced JSONB for efficient storage and querying
• JSONB is a binary representation of compressed JSON, ideal for large datasets and frequent querying
• Regular JSON is useful for storing logs or API responses where exact format is preserved
• JSONB is typically preferred for development due to its indexing and querying capabilities
• JSON can be used for storing optional or extra fields, especially when data consistency is not critical
• NoSQL databases can be limiting for analytics and complex queries, whereas Postgres provides a robust foundation for these tasks
• Indexing in Postgres, including GIN, GiST, and BRIN indexes
• JSONB and indexing, including the use of GIN indexes for JSON data
• Array data type and its uses in Postgres
• PostGIS as an extension of Postgres, and its own maintenance and upgrade cycle
• The Postgres community and its contributions to new features and index types
• The concept of "extensions" in Postgres, and how they interact with the core database.
• Postgres has a range of indexes, some core and some extensions
• PostGIS is a huge extension for geospatial data
• Other extensions include full text search, pub/sub, and queue functionality
• Extensions can be written in SQL or C and can add new features to Postgres
• Extensions can be used for tasks like sharding, distributed databases, and screen scraping
• Postgres has a "batteries included" approach, with many features built-in
• The core community can pull in solid and reliable extensions into the core codebase
• There are over 250 extensions available for Postgres
• HStore and JSON data types in Postgres
• MADlib analytics package for Postgres
• PL/Python and PLV8 for executing Python code in Postgres
• Using Postgres as a database for data science and machine learning tasks
• Writing application logic in the database with Postgres
• Using PSQL with customizations and tips for productivity
• Integration of development environments with PSQL
• Building and testing SQL functions in PSQL
• Future extensions and features for Postgres, including time series and JavaScript integration
• ZomboDB for Postgres and Elasticsearch integration
• Pluggable storage in Postgres, including zheap and Zedstore
• VACUUM performance and new backend types for improved space savings and performance
• Postgres' capabilities in data warehousing and columnar storage
• Pluggable storage and extensions in Postgres
• Advantages and trade-offs of columnar storage vs. traditional transactional workloads
• Future of Postgres and its potential for growth and innovation
• Resources for learning Postgres, including Postgres Weekly, Planet Postgres, and community mailing lists and Slack channels