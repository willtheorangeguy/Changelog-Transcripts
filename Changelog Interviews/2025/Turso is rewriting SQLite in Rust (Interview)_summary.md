• Glauber Costa and his team are rewriting SQLite in Rust with new twists and ideas, called Limbo
• SQLite is considered the most widely-deployed database in the world, and is public domain, but not open source in the classical sense
• The maintainers of SQLite do not take contributions from the public, and it's not designed for community-driven development
• LibSQL was a previous effort to create a modified version of SQLite that addressed some of its limitations, but ultimately decided to fork it instead of rewriting it
• The team decided to rewrite SQLite in Rust as Limbo, instead of continuing with the fork, after reconsidering the options
• The unique public domain-ness and closed contribution policy of SQLite
• Challenges of working with SQLite, particularly with large-scale changes
• The decision to fork SQLite and create a new database, Limbo
• Glauber Costa's clarification that the decision to fork was not a criticism of SQLite, but rather a choice to create a different project
• The goal of replacing SQLite with Limbo
• The history of LibSQL and its failure to replace SQLite, but its success as a business
• The decision to rewrite Limbo and create a new, more modern database
• The reaction to the new Limbo and the realization that it may not be enough to replace SQLite
• The original SQLite fork, LibSQL, failed to gain traction and differentiate itself from the original SQLite.
• The Limbo project, a new rewrite of SQLite, was announced and received an overwhelming positive response from the community, with 8,000 GitHub stars in a week.
• The rewrite allowed the team to start with a clean slate and implement new ideas and features, whereas a fork would have been limited by the original codebase.
• Deterministic simulation testing, a technique used by the TigerBeetle database, was adopted by the Limbo project to improve testing and debugging.
• The combination of deterministic simulation testing and partnering with Antithesis to simulate complex system interactions has greatly improved the testing and debugging capabilities of the Limbo project.
• The goal of the Limbo project is to eventually replace SQLite as the go-to database solution.
• Deterministic simulation testing (DST) is a complex and time-consuming process that requires rewriting code to ensure determinism
• Antithesis is a tool used in conjunction with DST to provide integration testing capabilities
• DST is not easily boltable upon existing codebases and requires a significant rewrite
• Limbo's goal is to be compatible with SQLite, with a focus on language, API, and file format compatibility
• Limbo aims to provide fully asynchronous IO, which requires a different approach than SQLite
• The simulator is used to generate random queries and test the system's behavior in a deterministic way
• The team is testing bytecode compatibility with SQLite to ensure that the query plan is the same
• The process of rewriting SQLite with DST is likened to unit testing, with the goal of gaining trust and confidence in the new system
• SQLite limitations for complex queries and serverless environments
• Limbo's async design and its benefits for complex queries and serverless environments
• Turso Cloud and its features, including serverless SQLite on the cloud, partial storage, and browser support
• The original intention to rewrite SQLite and the project's technical decisions
• The unexpected success of the project and its implications for the company's strategy
• Discussion of Limbo's unexpected success and subsequent decision to go all-in on the project
• Reasons behind the contributions of two key engineers, including their desire for a more ambitious project and a seat at the table
• Plans to replace the client-side part of LibSQL with Limbo and eventually rename Limbo to Turso
• Ongoing development work, including replication, schema changes, write throughput, and analytical workloads
• Timeline for completing these tasks, with a rough estimate of 9 months to a year
• SQLite fork project timeline: 9-12 months
• Project goals: make a stable and production-ready SQLite fork, called Limbo
• Turso business changes: simplifying the platform, discontinuing certain features, and focusing on Limbo
• Turso Cloud will remain a separate entity, offering serverless managed SQLite databases and other features
• Consolidation of Turso and LibSQL brands into a single Turso brand
• Limbo will replace SQLite as the default database in Turso Cloud and other products
• Renaming client offering to Turso, with no change in open source strategy
• Managing relationships between Turso, Turso Cloud, and third-party contributors
• Separating server code from client code to maintain independence and avoid conflicts of interest
• Open-sourcing client-side library and Turso, while keeping server-side code closed-source
• Defining success metrics, including reaching 1 billion databases
• Current state of the project, with some read functionality available
• Future plans, including a new server implementation with deterministic simulation testing, and a focus on scalability and multi-tenancy
• Turso Cloud to remain closed-source, with LibSQL as an open-source alternative for running databases
• Open-sourcing Turso, the embedded database, to encourage community contribution and adoption
• Implementing a database hosting model
• Company's financial runway (15-20 months without additional funding)
• Plans for future growth and scalability
• Schedule for a follow-up conversation (January 22nd, 2026)