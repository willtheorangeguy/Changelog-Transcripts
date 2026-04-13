• Clever started using Go in 2014 after experiencing pains with CoffeeScript and Node.js
• Initial success with Go was due to a rate limiter called Sphinx, which was easy to implement and manage
• Clever's first projects in Go were relatively small and isolated, allowing them to test the language without significant risk
• The team used a "bet on a small project" approach to introduce Go into their stack
• Early experiences with Go led to increased enthusiasm for the language, particularly due to its ease of development and collaboration
• Clever's data extract workers were another early success story in Go, allowing them to improve their data ingestion logic and abstraction
• The team was testing various aspects of Go, including its type system, testing framework, and benefits of having strong typing
• Comparison of Go and Node/JavaScript development experiences
• Discussion of testing in Go vs. Node/Ruby/Rails
• Advantages of using Go's standard library for testing and HTTP services
• Challenges of developing web apps in Go, including complexity and toolchain issues
• Current architecture at Clever: mix of Node/TS on frontend, Go microservices on backend
• Split between business logic and UI needs; desire to move all business logic to Go
• Managing multiple repositories and deployments
• Consistency across services through standardized tools and processes (e.g. Swagger OpenAPI, Wag)
• Microservice architecture and average service size
• Performance considerations for core services
• Team ownership and responsibilities for microservices
• Customizing open-source tools to meet specific needs
• Customizing workflow tools for team efficiency
• Edge case features and the value of simplicity in tooling
• Comparison of Swagger and OpenAPI generator usage
• Microservices architecture with separate data layers
• Automation and CLI tools for DynamoDB instance management
• Go-based CLI development and binary packaging benefits
• Go's binary sharing and infrastructure team experience
• go.mod and dependency tool transition experiences
• MicroPlane tool for automating changes across multiple repos
• Challenges in managing hundreds of repositories, including updating dependencies and build processes
• Automating deployment and management of microservices, including safe shipping and consistent alerts
• Custom deployment process using a Slack bot and state machine
• Using AWS Step Functions for state machine runtime and maintaining a smaller surface area.
• Challenges of evolving underlying systems when using complex technologies that are difficult to change.
• Local development process, including running individual microservices locally and pointing to shared staging environments.
• Need for internet connection during development to interact with web services.
• Isolated testing approach, where individual services are tested separately before end-to-end tests in QA environments.
• Unpopular opinion on Go channels, considering them not worth the complexity and difficulty in explaining concurrency.
• Limitations of using channels in Go web services
• Use of errgroup library as a simpler alternative to channels
• Re-evaluating the "use the right tool for the job" advice and its limitations
• Value of settling on a set of tools that work well for repetitive tasks
• Trade-offs between introducing new languages or tools versus investing in existing ones
• Importance of considering ecosystem, tooling, and experience when selecting databases or other technologies
• Critique of "use the right tool for the job" advice as being too vague and unactionable