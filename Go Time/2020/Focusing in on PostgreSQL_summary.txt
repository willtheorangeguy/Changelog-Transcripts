• Introduction to Postgres and its purposes
• History of Postgres (over 20 years old)
• Comparison with alternatives like SQLite
• Advantages of using Postgres in Go (good library support, stability, maturity, speed, ease of use)
• Wire interface of Postgres (different from other SQL databases)
• Postgres' influence on other databases that implement its wire format
• Experience of using Postgres as a programmer
• Relational databases (Postgres) require predefined table structures and schema
• SQL language is used to define tables and relationships between them
• In contrast, document stores allow for flexible data storage without predefined structure
• Indexes and optimization are key to performance in relational databases
• Denormalization can be used to improve performance in relational databases at massive scale
• Data replication across geographical nodes can become a problem with large datasets
• Creating a star schema in a relational database
• Performance considerations for transactional vs reporting data
• When to switch from relational databases (e.g. Postgres) to NoSQL or other technologies
• Importance of understanding domain and business problems before choosing technology
• Role of caching in addressing performance issues
• Starting with well-established, well-tested technologies like relational databases (e.g. Postgres)
• Over-reliance on hype and popular opinion when making technology choices
• SQL learning curve can be intimidating, but it offers great benefits and flexibility
• Migrations are essential for database schema changes, allowing easy upgrades and rollbacks
• Postgres supports migrations through SQL commands and libraries like golang-migrate
• Connection pooling in Go's standard library simplifies database interactions
• Care must be taken when applying migrations across multiple clients or servers
• Connection pooling between database and client in Go is handled by the standard library.
• Jackc/pgx driver for PostgreSQL offers a faster binary encoding interface.
• The main differences between lib/pq and jackc/pgx are their performance and type safety features.
• sqlx is a wrapper around the standard library's database package that simplifies working with databases.
• The standard library can interact poorly with some databases, such as Postgres, due to differences in syntax.
• Running tests against an in-memory SQLite database is easier than setting up a real PostgreSQL instance.
• Debate over testing databases with different versions of SQL
• Use of Docker to run tests against a Postgres database
• Automated Docker testing to create a temporary database for testing purposes
• Benefits of using the standard database/sql package instead of ORMs
• Discussion on performance issues caused by ORM usage and reliance on abstraction
• Importance of writing actual SQL queries for better control and understanding of database interactions
• ORMs (Object Relational Models) vs writing SQL directly
• Defining a database access layer to allow swapping between ORMs and raw SQL
• Avoiding scattering SQL queries throughout codebase
• Using UUIDs instead of auto-increment IDs
• Handling testing for migrations and performance issues in development environments
• Approaches to keeping test environment data up-to-date with production changes
• Replication and transformation of data between primary and secondary nodes
• Using a separate instance for testing and applying transformations to data before writing it to disk
• Testing migrations by migrating to a step, inserting data, and checking that the data was updated correctly
• The importance of testing in a production-like environment to avoid unexpected issues
• Criticism of importing packages with side effects, such as sql.register, due to potential bugs and difficulties in debugging
• Discussion about Go's init function being difficult to understand and use
• Criticism of the builder pattern in Go due to compatibility issues with static typing
• Unpopular opinion that Squirrel, a query builder library, is an exception to the rule against using the builder pattern
• Potential for rewriting Squirrel using functional options
• Use cases for lightweight abstractions over data stores to provide robustness and security
• Importance of protecting against SQL injection attacks through placeholder variables
• The dangers of SQL injection vulnerabilities
• A humorous anecdote about a principal who lost data due to a SQL injection attack
• Discussion of Postgres and its suitability as a database choice for Go developers
• A tangent conversation about the host's name (Johan/Johaan/Juwan) and how it changes in Sweden when someone is in trouble