• Play With Go was created as an open-source project to showcase specific use cases of the Go programming language
• Marcos Nils worked with Paul Jolly to develop Play With Go, building on his experience with Play With Docker
• The idea for Play With Go came from a need in the Go community to demonstrate tooling and module management concepts
• Play With Go has received positive feedback and has been used by many people, but development activity has slowed down recently
• Marcos Nils started Play With Docker after attending an event where he saw a need for a simpler way to showcase Docker use cases
• The idea for Play With Docker came from attending the Docker Contributors Summit and seeing attendees struggling with complex tasks during Jérôme Petazzoni's training
• Play With Docker was initially developed as a minimal proof-of-concept and eventually grew into a more comprehensive tool
• The concept of platform engineering and its goals, with Marcos defining it as making developers' lives easier
• Comparison between platform engineering and DevOps, with discussions on who owns platform engineering and how it fits into existing teams
• The difference between platform engineering and DevOps, with Marcos stating that they are not mutually exclusive but rather complementary
• Challenges in implementing platform engineering, including the need for a framework where everyone can contribute to building faster, more secure software
• The importance of understanding users' pain points and iterating on solutions in platform engineering
• DevOps teams often overlap with other teams, such as SREs, due to unclear metrics and goals.
• Platforms can help frame and connect different teams' goals, but do not solve underlying issues.
• The concept of platforms has been around for a long time, even before eight years ago.
• A company's context and infrastructure can greatly impact the success or failure of a platform.
• Principles such as autonomy, golden paths, and health checks have remained relatively consistent over time despite changes in technology.
• The basics of platform development, including scripts and workflows, have also stayed similar despite advancements in technology.
• One potential area for improvement is reducing the complexity and overhead of building and managing platforms.
• Challenges of building distributed systems and managed services
• Trying to replicate cloud services in-house (e.g. BQ as SQS alternative)
• Scaling issues and need for redoing work
• Risks of adopting new technologies before they are mature (e.g. Node.js 0.4)
• Importance of simplicity when designing complex systems
• Difficulty of building stateful services and distributed systems
• Examples of production data-related problems (e.g. RabbitMQ, queuing)
• Consequences of system downtime (e.g. payroll issues, customer impact)
• Building a distributed caching system with Redis compatibility
• Memory leak issue in caching library used
• Experience bootstrapping a startup with little knowledge of cloud and distributed systems
• Development of early platforms for AI engineers
• Use of Docker, AWS, and Amazon services for orchestration and deployment
• Simplification of workflow for developers through minimal descriptors (Docker files)
• Early stages of platform engineering, influenced by companies like Heroku and the CNCF
• Stateful data problem and management in cloud-based platforms
• Development of a service to handle model state in AI applications
• Last platform mentioned: Wildlife Studios, a gaming company with experience in mobile game development
• Context is crucial when building a platform for software engineers
• Developers were already exposed to Kubernetes and had a workflow in place
• A new VP introduced an idea to build a centralized UI and control plane like in their previous company, but it didn't fit the current organization and workflows
• The team adopted Backstage, a developer portal that was designed for a specific type of organization, which led to a complex and resource-intensive project
• It's better to start small and iterate on existing workflows rather than introducing an out-of-the-shelf platform or building a new one from scratch
• Big bang rewrites are considered a bad idea due to unknown risks and potential for introducing new problems.
• Incremental changes and data-driven decision making are preferred over large-scale platform implementations.
• Centralized visualization and communication platforms can simplify development and augment team collaboration.
• Starting with smaller, more manageable projects and building on existing infrastructure is suggested instead of starting from scratch.
• Serverless and containerization options are being considered, but serverless has limitations due to unresolved issues such as persistent database management.
• Discussing serverless computing and its potential disruption of traditional app development
• Comparison of Kubernetes to other platforms, with doubts about its suitability for serverless workloads
• Preview of upcoming trends and technologies in 2023, including WASM and serverless adoption
• Desire for more human connection and community sharing in the tech industry
• Personal reflection on past year's events and future collaborations