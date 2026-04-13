• Yoni Goldberg's background and inspiration for creating Node Best Practices
• Challenges of server-side JavaScript, including unique cultural baggage and the need for conventions
• The "LegoLand" nature of Node.js, with developers often having to craft their own modules and infrastructure
• Key security challenges in Node.js, including maturity and single-threaded issues
• Overview of the best practices guide, focusing on project structure, error handling, style, etc.
• Discussion of coding style conventions, including semicolons vs. automatic semicolon insertion
• Discussion about writing code and avoiding flammable discussions
• Best practice: distinguishing between catastrophic errors and non-catastrophic errors
• Example of using process.exit for unknown errors, but later adjusting to a balanced approach
• Consideration of server-side apps vs command line apps and the importance of logging in production environments
• Importance of ops involvement in error handling through monitoring, logging, and proactive action
• Discussion about extending the built-in Error object and avoiding throwing arbitrary objects or long strings for error messages
• Error handling best practices for Node.js
• Importance of structuring error messages with identifiers and classifiers
• Comparison of error handling approaches (inheriting from base error object vs. creating separate classes)
• Functional vs. composition-based design for error handling
• Standardization of error logging and formatting
• N-tier architecture as a middle ground between over-structured and under-structured designs
• Layering code with N tiers, separating concerns into API, business logic, and data access layers
• Comparison of N-tier to MVC (Model-View-Controller) architecture
• The limitations and flaws of traditional MVC (Model-View-Controller) architecture
• The N-tiers approach as a solution to manage complexity and separate concerns
• Challenges with applying N-tiers to frontend JavaScript/TypeScript applications
• Importance of metrics over logging for monitoring and measuring application performance
• Benefits and best practices for using metrics, including documentation and tool support
• Platform-specific metrics vs business metrics
• Importance of understanding logging and monitoring costs
• Abstraction layer for logging to allow flexibility and switch between tools
• Separation of verbosity levels for logs (infrastructure-level vs. debug)
• Creating a dedicated method for metrics within the logger abstraction
• Using ASTs or similar to automate process changes and notifications for ops teams
• STDOUT vs STDERR best practices for logging
• Importance of not logging to files in production environments
• Distinguishing between STDOUT and STDERR in backend applications
• EventStream incident and supply chain attacks
• Need for a grace period before updating packages to avoid security breaches
• Dependabot and the importance of keeping code updated
• Unpublish package feature and its implications on the immutability of the npm registry
• Importance of being one major version behind for dependencies to avoid churn and interlocking issues
• Limiting and scrutinizing dependencies as a practical takeaway to prevent supply chain exploits
• Establishing a rubric or process for evaluating new dependencies, including considering dependency chains and maintaining code
• Addressing problematic input from users in first-party code, such as SQL injection and cross-site scripting
• Validation and escaping of user input
• Benefits of using OpenAPI Spec (Swagger) for schema validation
• Importance of structured APIs and data formats, such as GraphQL
• Challenges of escaping and sanitizing strings across different platforms
• Need for collaboration and collective knowledge in improving security
• Role of frameworks like NestJS in providing good defaults and making development more sustainable
• Faux-pas to watch out for in frontend code that can affect backends, including unvalidated user input
• Unpredictable user input can cause security issues and DDoS attacks on backend systems.
• The "backendless" pattern, where the frontend is the core and the backend is generic, poses security challenges due to increased flexibility and power for users.
• The use of GraphQL and single endpoints can lead to a larger surface area for potential attacks.
• Limiting the frontend's power requires tools and careful implementation to prevent security issues.
• Testing was mentioned as a topic that deserves its own episode or series.
• Discussion of releasing a full series on testing
• Sneaking in testing content into existing episodes
• Nick Nisi's use of TypeScript model
• Blender analogy (blending broccoli into chicken nuggets batter)