• Context matters in application design and influences trade-off decisions
• Global state is generally considered problematic due to issues with testability and reasoning
• Packages should store declarations (type definitions, functions) and only main should store state
• Injection of STDIN/STDOUT can be done through a main struct or other mechanisms for testing purposes
• Using io.Reader and io.Writer interfaces to handle input/output
• Returning errors from a main function and handling them at the top level
• Adapting error handling for specific use cases (e.g., HTTP responses)
• Discussing the potential removal of global state in Go
• Eliminating init functions as part of a possible major language change
• Approaches to avoid over-engineering code and instead focus on simplicity
• Importance of growing code organically, avoiding premature complexity
• The value of writing "code that's easy to delete, not easy to modify"
• The panel discusses how junior developers often try to anticipate and plan for every eventuality when building a complex application.
• They advise against premature abstraction and instead recommend starting with a simple structure and letting abstractions emerge from the program as it grows.
• Kat Zień emphasizes the importance of taking time to understand the problem and domain before designing a solution.
• Ben Johnson shares his experience of refactoring by starting with a flat structure and using GoDocs to identify related code.
• The panel discusses the trade-off between following established patterns and incorporating new learning into an existing system, with some advocating for consistency and others recommending adaptation based on context.
• Kat Zień suggests keeping microservices homogeneous to reduce maintenance and understandability issues.
• Microservices as a solution to organizational problems rather than technical ones
• Importance of team ownership and strict boundaries between microservices
• Scalability benefits at large scale (e.g. over 1,000 microservices)
• Single-responsibility principle for microservices
• Use of libraries and code generation to minimize friction when adding new services
• Consistent architecture across all microservices
• Ease of deployment and rolling out changes across the fleet
• Discussion on rolling out fixes and upgrades across multiple services
• Explanation of hexagonal architecture and its benefits in separating application code from framework and third-party code
• Comparison of strictness vs flexibility in implementing hexagonal architecture, including using marshaling packages to translate between data types
• Debate on the trade-off between performance and readability, with examples of where business logic should be placed (e.g. controllers, models)
• Performance optimization and profiling
• Context-dependent performance requirements (e.g. trade-offs between latency and complexity)
• Structuring applications for performance: breaking down sequential processes into asynchronous calls
• Prioritizing mission-critical paths vs. non-mission critical tasks
• Designing systems with concurrency in mind, but avoiding over-engineering
• Leaving micro-optimizations until the end and focusing on proper optimizations
• Coming out as a magician
• Writing code that is clear and easy to understand
• Concurrency in programming
• Domain-Driven Design (DDD) and its application
• Avoiding unnecessary complexity in software architecture
• The importance of flexibility and adaptability in software development
• Interfaces in Go and the concept of structural typing
• Dependency injection and interfaces
• Contextual use of dependency injection frameworks
• Premature abstraction and optimization
• Performance profiling and bottleneck identification
• Tooling for performance analysis and visualization
• Importance of simplicity and letting patterns emerge in architecture
• Twitter handles of the guests: @kasiazien, @benbjohnson, @peterbourgon (and @therock)
• Recap and closing remarks 
• Future appearance by the guests on the show