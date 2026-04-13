• Introduction of guests Mat Ryer and David Hernandez
• Discussion on Go in production, spotlighting the Pace.dev app
• First steps in building the app: starting with a simple Go binary serving HTML
• Decision not to use a framework, opting instead for the standard library
• Choice of technology stack based on prior experience and familiarity
• Importance of knowing what you're getting into when choosing new technologies
• The speakers discuss the importance of not over-engineering and over-abstraction in code, citing the potential for unnecessary complexity and bloated code.
• They mention using "argument-driven development" to validate ideas and approaches before investing too much time or resources.
• The speakers highlight the value of copying and pasting code when it's simpler and more efficient than creating an abstraction.
• They discuss how a flat folder hierarchy can influence their approach to abstractions, making them think more concretely about specific concepts rather than abstracting away complexity.
• Mat Ryer shares examples from the frontend (waiters/spinners) and backend (permissions) of using repeated code instead of creating abstractions.
• Abstractions in software development can lead to unnecessary complexity
• The speaker's team has adopted a simple structure with all services in one folder, rather than creating separate packages or modules
• This approach is driven by a desire for simplicity and flexibility, rather than adhering to traditional packaging or modularity principles
• The Oto project is mentioned as an example of this approach, which allows for RPC-style communication between frontend and backend without the need for complex protocols like gRPC
• The team chose not to use gRPC due to limitations in their deployment environment and the complexity of implementing plugin tools
• Instead, they used interfaces to generate code for both frontend and backend, allowing for a simple and readable implementation that can be customized as needed
• Testing is done using a built-in Go tester and integration tests that use a generated client to hit real endpoints
• The team uses a tool to spin up a data store emulator and run tests locally, without containerization or continuous integration
• The team prefers local development over formalized testing processes due to their small size and rapid iteration cycle
• They do not have a release manager and deploy frequently, with a focus on good test coverage for confidence in deployment
• This approach may change if they were working on an open-source project with specific version dependencies
• Monolithic deployment of the system
• Trade-offs between simplicity and complexity at scale
• Continuous integration and testing strategies
• Speed and feedback loops for developers
• Balance of frontend and backend logic in application development
• Integration testing methods and approaches
• The current API is tightly bound to the frontend and returns all necessary data in one response
• The team uses Svelte as their frontend framework due to its compile-time build process and minimalistic approach
• The tech stack includes Firestore for the database, Pubsub for background tasks, and App Engine as the platform
• GraphQL is not used as it's not necessary given the tight binding between frontend and backend
• The Go client uses RPC (Remote Procedure Call) to interact with the API
• The architecture is simple and focused on serving a specific use case rather than being highly scalable or general-purpose
• Dealing with failures in asynchronous operations
• Designing systems to handle retriable errors and reporting non-retriable ones
• Idempotence and designing systems that can tolerate multiple attempts at the same operation without unintended consequences
• Eventual consistency models for data storage, particularly with non-relational databases
• Handling inconsistent or outdated data across multiple copies, including renaming tags or labels
• Balancing UX experience with technical trade-offs
• Designing applications for specific databases (relational vs. document stores)
• N+1 problem and database query optimization
• Working in tiny teams and its benefits
• Open and honest communication in rapid development environments
• Discussion of open-source development and the importance of trust and respect among team members
• The balance between honesty and politeness in communication, especially in online communities like open-source projects
• Sharing personal anecdotes about experiences with open-source development and teamwork
• Nostalgia for early internet search engines and browsing experiences