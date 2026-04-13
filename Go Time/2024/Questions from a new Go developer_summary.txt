• New Go developer experience
• Duarte Carmo's background and experience with programming languages
• How Duarte discovered Go as a middle ground between Python and Rust
• Discussion on the benefits of using Go as a language
• Duarte's past experiences with Advent of Code in Rust and building a website
• Binary vs script: the preference for creating binaries rather than scripts
• Go's simplicity and readability
• Error handling in Go
• The language's design to guide developers towards professional-looking code
• Dialects of Python and differences between Rust, Go, and other languages
• The importance of explicit error handling and treatment in Go
• Error handling in Go programming language
• Returning errors versus raising panics
• Importance of handling errors locally vs. passing them up the call stack
• Using fmt.Errorf() with context for error wrapping
• Creating custom error types with additional context
• Properly scoping variables to limit their availability
• Error checking and scoping of return values
• Dockerization vs. shipping binaries for deployment
• Tooling and operational context for deployment (e.g. container orchestration, Kubernetes)
• Managing updates for deployed binaries
• Building different executables for various platforms using Go's build process
• Packaging and dependency management in Go compared to other languages (e.g. Python)
• The history and necessity of package management in Go, including the introduction of the module system.
 • Benefits of using a GitHub base domain name for packages, such as namespace organization and ease of installation.
 • Importance of consistency in package structure and naming conventions.
 • Discussion of how to organize projects, specifically how to handle dependencies and create a reproducible build environment.
 • Lack of consensus on a standard approach to structuring Go projects.
• Creating a CMD folder at the root of the project to organize executables
• Avoiding unnecessary hierarchy and premature structure in Go projects
• Using package declarations at the top of each file, with folders acting as organizational tools for developers rather than Go itself
• Discussing the benefits of simplicity in Go programming, including avoiding unnecessary complexity and boilerplate code
• Debating the use of ORMs (Object-Relational Mappers) in Go projects, with some arguing that they are not necessary due to the language's simplicity and others advocating for their use in certain situations.
• The importance of ORMs (Object-Relational Mappers) for database access and management
• Trade-offs between using ORMs and writing raw SQL queries
• Benefits of learning SQL regardless of programming language or framework
• Use cases where ORMs are beneficial, such as team velocity and CRUD operations
• Alternatives to ORMs, such as lightweight packages like sqlc or sqlx
• Discussion of SQLite and its popularity among developers, including Go community members
• Personal experiences with using Litestream for backing up SQLite databases
• Go's concurrency model uses goroutines and channels for communication
• Wait groups are used to manage a fixed number of concurrent tasks
• Channels can be used as an alternative to wait groups, but add overhead
• Mutexes and atomic packages are used for mutual exclusion and thread-safe operations
• Errgroup is a package that allows for waiting on multiple goroutines with error handling
• Prioritization is key in managing time effectively
• Saying "I don't have time" can be a sign of poor prioritization or having too many commitments
• It's essential to drop non-essential tasks if they interfere with more important ones
• Mutexes can slow down high-throughput situations and may not always be the best choice
• Go has multiple concurrency tools (channels, mutexes, wait groups) and choosing the right one depends on the specific use case
• Discussion with guest Duarte Carmo about guidance in Go
• Invitation for listeners to come on the show and discuss Go-related topics
• Thank yous and closing of the episode