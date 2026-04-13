• What are migrations
• Why schema migrations are necessary
• Tooling for managing migrations (e.g. Golang Migrate, Dbmate, Pressly Goose)
• How these tools work behind the scenes (e.g. using metadata or schema history tables to track applied migrations)
• Issues with manually changing or undoing migrations
• Handling out-of-order migrations
• Pros and cons of using timestamp-based versus sequential versioning for database migrations
• Risks of out-of-order migrations and potential issues with tooling and troubleshooting
• Benefits of sequential numbering, including easier rollback and reduced risk of errors
• Approaches to handling migration failures, including running entire migrations in transactions or using locking mechanisms
• Types of migrations that cannot be truthfully undone, such as deleting tables or columns, data manipulation changes, and certain types of alters.
• Decoupling migration steps from application code
• Benefits of having a separate process for migrations, including zero downtime deployment
• Common mistakes in setting up migrations, such as running migrations within the same binary and not ensuring forwards and backwards compatibility
• Importance of tooling in managing migrations, including Goose and Golang Migrate
• Building custom migration tools, with Mike Fridman suggesting it's a good learning experience to create one on your own
• Approaches to deploying migrations to production, including ad-hoc, semi-manual, and continuous deployment environments
• Challenges of running multiple instances of an application and the need for tooling that can handle concurrent migrations.
• Pitfalls of automated migration mechanism
• Using singleton process for migration deployment
• GitHub Actions for CI/CD pipeline and migration deployment
• Testing migrations in continuous environment
• Techniques for testing up and down migrations
• Decoupling production database from development environment
• Checking final schema against desired schema
• Comparing schema between staging/production and Git repository
• Importance of maintaining a consistent database schema across all environments
• Need for developers to carefully consider their changes before implementing them
• Benefits of having backups and disaster recovery documentation in place
• Danger of premature use of new features, such as Go generics
• Criticism of the Go logger struct design
• Discussion on the need for a logging interface in Go and potential implications of its adoption
• Debate about whether an interface is necessary or if third-party libraries would adapt to work with standard HTTP handlers
• Introduction of the "any" alias in Go 1.18, which maps to the empty interface, and concerns about potential confusion and fragmentation in codebases