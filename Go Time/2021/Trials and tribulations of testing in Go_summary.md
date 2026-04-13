• Importance of testing
• Difficulty and challenges of writing tests
• Regret not having testing in place (e.g. financial transactions, production defects)
• Benefits of automated testing (e.g. regression testing, time-saving)
• Test-driven development (TDD) and its benefits (e.g. well-organized code, good design)
• Over-testing vs. under-testing and finding the right balance
• Putting yourself in the mind of the user through test code
• Testing as a design tool to ensure code intention and correctness
• Importance of writing tests before or concurrently with application code
• TDD (Test-Driven Development) approach for creating testable code
• Writing tests for existing code to ensure changes don't introduce new bugs
• Different approaches to testing, including bottom-up vs top-down design methods
• Writing tests in a way that follows the style and requirements of the specific project or type of software being developed
• The importance of separating serialization logic and storage components
• Eliminating dead code through testing
• Writing concise and compact services
• Context-dependent testing approaches for different programming tasks (e.g. Go package, service integration, UI)
• Testify: a Go testing library that provides single-line assertions and simplifies testing
• Criticisms of Testify's large API footprint and complexity
• Alternative approaches to testing in Go, including using the standard library or third-party packages like cmp
• Comparison and simplicity of testing libraries
• Transitioning from assertions to more direct tools for testing
• Differences in testing approaches between Go and other languages
• Overtesting and brittle tests
• Design process and role of testing in software development
• Importance of testing as part of the larger design process
• Tension between testing implementation details vs abstracting away for easier testing
• Use of mocks vs end-to-end testing for caching and external system interactions
• Difficulty in testing complex systems with many external dependencies
• Pros and cons of mocking: tying test code to implementation, versus using real dependencies
• Designing systems with built-in sandboxes or proxies to reduce need for mocking
• Balancing unit tests and integration/end-to-end tests for effective coverage
• The overuse of mocking and abstractions in Go code can lead to leaky abstractions, hyper-abstraction, and difficulty in understanding the code.
• Abstractions should be used sparingly and only when thoroughly thought through, with a focus on creating true abstractions that don't expose implementation details.
• Mocking is not inherently bad, but it's essential to consider the effort required to use mocking tools and whether they're worth it for the specific problem being solved.
• Only testing one thing in a unit test, rather than over-testing, can lead to more confidence in code quality without unnecessary complexity.
• End-to-end testing with SQL databases is challenging due to the difficulty of simulating failure scenarios with mock libraries like Sqlmock.
• The importance of testing for failure modes in systems
• Limitations of 100% code coverage and the potential risks of overemphasizing it
• Idempotency as a design principle to simplify error handling
• The value of trusting developers to write correct code, rather than relying solely on exhaustive testing
• Critique of test coverage metrics as a heuristic for determining code quality
• Design process and upfront design
• Nuances of design and semantic differences
• Importance of prototyping, testing, and iterative development
• Rewriting code as part of the design process
• Unpopular opinions on chocolate and candy preferences
• Conversation devolves into discussion about Easter treats and personal vices
• Discussion of personal sugar cravings and consumption
• Agile methodology and its perceived limitations
• Potential drawbacks of using Scrum and sprints in software development
• Need for more flexible approaches to project management
• Importance of trusting team members and avoiding rigid frameworks
• Kris Brandow's unpopular opinion on the need to move away from Agile