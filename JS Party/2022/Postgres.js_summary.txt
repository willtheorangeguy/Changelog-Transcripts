• Relational databases vs document databases (Mongo), key-value stores, or Firebase
• Rasmus's personal experience with MongoDB and his eventual switch to PostgreSQL
• The resurgence of interest in relational databases like Postgres
• The development and design of Postgres.js library by Rasmus Porsager
• Rasmus Porsager started using PostgreSQL in 2016-2017 due to the lack of foundational libraries at the time.
• He used pg-promise as his initial introduction to PostgreSQL libraries in Node.js, but found it lacking and created a wrapper for tagged template literals.
• He discovered the PostgreSQL wire protocol and its simplicity, which led him to create Postgres.js.
• Key features of Postgres.js include pipelining and prepared statements, which significantly improve performance compared to other libraries.
• Benchmarks show that Postgres.js is 2-2.5x faster than the old PG library, but Rasmus wants to conduct more thorough benchmarking with real-world applications and network latency.
• The library uses async/await syntax throughout and was motivated by the shift towards this era in Node.js development.
• A real-world example of Postgres.js's performance improvement is seen in a digital signage company where Rasmus works, which reduced server requirements from 8-core to 2-core.
• Tagged template functions and their use in Postgres.js
• SQL injection protection through tagged templates
• Lazy evaluation and performance gains
• Schema generation and migration tools
• Comparison of relational databases (Postgres) vs NoSQL databases (Mongo)
• Use of a separate library (Postgres Shift) for schema migrations
• Discussion about using Postgres Shift for schema migrations
• Considerations for expanding the functionality of Postgres.js to include basic migration support
• Use cases and potential limitations of using Postgres.js to execute arbitrary SQL statements
• Potential implementation of a more robust ORM system within Postgres.js
• The concept of HashQL as an alternative to ORMs, allowing direct database querying from JavaScript
• API design principles, specifically the uniform access principle, where results are returned in a consistent format regardless of their size
• Postgres.js library features and benefits
• .describe query feature for TypeScript automated type inference
• Maintenance plans and intentions for the project
• Adoption of alternative database systems like FaunaDB and Cockroach
• Sustainability plan for maintaining open source projects
• History and naming of the Postgres package on npm
• Porting a JavaScript library from Node.js to Deno
• Postgres.js: a lightweight PostgreSQL client library written in vanilla JavaScript
• TypeScript support and community contributions
• Enhancing PostgreSQL's usability through Postgres.js
• Advanced features, such as JSON support, logical replication, and real-time subscriptions
• Plans for future development and user feedback