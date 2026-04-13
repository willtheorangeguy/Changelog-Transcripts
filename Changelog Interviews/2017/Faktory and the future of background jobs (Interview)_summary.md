• Mike Perham is back on the show for the 4th time, discussing his new project Faktory and its differences from his previous work on Sidekiq
• Faktory is designed to be language-independent, unlike Sidekiq which is tied to Ruby
• Mike is building Faktory as an inverse to Sidekiq's architecture, allowing it to scale and be more versatile
• The goal is to create a background job framework that can benefit businesses regardless of the language they use
• Mike plans to hire additional staff if Faktory becomes successful and needs more support
• The discussion touches on the potential for commercial variants of Faktory and the desire to expand the business's customer base
• Faktory is a standalone daemon that allows for job operations, making it easier to implement workers in any language
• Faktory provides a web UI for tracking jobs, errors, and worker processes
• The simplicity of Faktory workers is a major selling point, making it easier for developers to implement
• Faktory's pricing model allows for low costs, making it more accessible to smaller shops
• The creator, Mike Perham, notes that Faktory's goal is to provide a pre-baked solution that solves a well-known problem, without the need for extensive operations management
• The "secret sauce" of Sidekiq is its comprehensive and singular package that includes features such as performance and a strong opinion on how to bake in features
• Faktory aims to replicate this by baking in features and providing a valuable solution that solves problems for developers
• The value of Faktory's web UI being built-in and simplified deployment and management
• Challenges of balancing simplicity and feature-richness in a single binary
• Removal of Redis as a dependency and its implications for data persistence
• Consideration of long-term support and production-grade quality in selecting a storage engine
• Evaluation of alternative storage engines, including RocksDB, BoltDB, and SQLite
• RocksDB's design is an LSM (log-structured merge tree) that offers faster writes than other databases
• Mike Perham built a load test to compare RocksDB and BoltDB, finding RocksDB to be 1,000 times faster for his use case
• The need for performance testing and due diligence in choosing a database or dependency
• The importance of abstraction and using multiple implementations for a system
• The benefits of using a widely adopted and maintained database like RocksDB, including its LSM design and active development
• The challenges of embedded databases, including data management and backup procedures
• The importance of testing and verifying performance in real-world use cases, rather than relying on assumptions or benchmarking alone
• Embedded storage subsystem in Faktory, using RocksDB
• Backup and restore mechanisms for Faktory
• Comparison of Faktory to Redis, and tradeoffs between the two
• Plans for a Faktory Pro product with additional features
• Potential for Faktory to be used as a SaaS
• Discussion of the success of Sidekiq and the application of a similar open source/open core model to other projects, including Inspeqtor
• Discussing the potential for a new open-source project, Faktory, to succeed where Sidekiq, another open-source project, failed to gain traction.
• Identifying successful models for sustaining open-source projects, including the "open core" model, where a company offers a free open-source version and a commercial version with additional features.
• Considering the possibility of Faktory adopting a similar model to Sidekiq's, but with a focus on providing a more robust and scalable solution.
• Discussing the potential for Faktory to become a polyglot solution, allowing users to use it with various programming languages, rather than being tied to Ruby like Sidekiq.
• Addressing concerns from users of Sidekiq, assuring them that Sidekiq will continue to be supported for the foreseeable future, but also highlighting the benefits of Faktory as a more future-proof solution.
• Faktory's value proposition is not just selling Ruby code, but providing conventions and opinions on a feature-rich background job system that can scale to multiple programming languages.
• The next release of Faktory will include job prioritization, allowing users to specify priority levels for jobs, and will be available in the next week.
• Faktory's open source community response has been strong, with over 100 pull requests in the last two weeks and several major features contributed.
• The project is planning to stabilize Faktory, evangelize its use, and get people using it in staging or production, and also recruit maintainers for worker libraries.
• Mike Perham is considering hiring people to maintain worker libraries and ensure they stay up to date with Faktory's latest changes.
• Faktory will be available as a Docker image and can be installed via Homebrew, with a tap available for the latter.
• Discussing installation and documentation for Faktory
• Using Gitter for real-time chat and community support
• Initial challenges with onboarding users and current progress
• Faktory's community growth and available resources
• Appreciation for Mike Perham's open-source success and contributions