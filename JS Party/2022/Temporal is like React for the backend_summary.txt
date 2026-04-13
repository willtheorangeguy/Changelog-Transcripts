• Introduction to JS Party panel with Ali Spittel and Shawn Wang (Swyx)
• Swyx's background in finance and his transition to programming
• Swyx's career progression from frontend development to backend and leadership roles
• The concept of "learning in public" and its benefits for career advancement
• Temporal as a workflow engine for long-running processes in cloud services
• The concept of "serverless" is being stretched beyond its original meaning as a technology to describe a business model that focuses on scalable, pay-as-you-go infrastructure.
• Serverless databases and stateless services are becoming increasingly popular, allowing developers to focus on application logic without worrying about underlying infrastructure.
• Workflow engines like Temporal can help simplify complex stateful workflows by handling consistency, declarative rendering, and other complexities.
• The idea of a "single stateful service" that orchestrates multiple stateless services is being explored as a way to simplify cloud architecture.
• Serverless functions can be orchestrated by workflow engines, allowing for more flexible and scalable application development.
• Temporal is being pitched as a framework that can handle complex workflows and orchestration
• Traditional workflow engines are inflexible and require learning a proprietary language
• Temporal aims to provide a general-purpose programming language for writing software
• The goal is to enable maintainable and flexible systems, allowing for versioning and testing
• Complex systems with many edge cases require careful handling of retries, cancelations, and task distribution
• Shawn Wang draws an analogy between Temporal and React, aiming to bring componentization and predictability to the backend
• The current state of backend development is compared to the "spaghetti code" era of frontend development
• Temporal as an orchestrator centralizes retries, state management, and ties together requests for a reliable end-to-end user experience.
• The system allows for customizable behavior at every point of activity call with a well-designed philosophy for thinking about retries and timeouts.
• Temporal enables the creation of atomic backend components without worrying about infrastructure provisioning, allowing developers to focus on input and output.
• The system supports four first-party SDKs: Go, Java, PHP, and TypeScript, with more planned, using standard software engineering tools and best practices.
• Deterministic behavior is ensured through event sourcing and storing state transitions for reliable recovery from crashes.
• Testing involves writing unit tests with standard tooling and time skipping for long-running tasks, as well as integration testing with a test suite that mocks out APIs.
• Versioning and migration are handled through the ability to replay the entire history of running workflows on new code, allowing for smooth updates and rollouts.
• Temporal is a workflow engine analogous to React Suspense for the backend
• It organizes code into workflows (pure functions) and activities (side effects)
• Workflows suspend to activities, which handle data and side effects before returning control to the workflow
• Temporal was inspired by AWS Simple Workflow Service and is now an open-source project with a commercial cloud offering
• The company has advisors from companies like HashiCorp and Netflix, and has seen adoption in companies like Airbnb and Stripe
• Shawn Wang's role at Temporal is Head of Developer Experience, which involves designing a holistic developer experience across the product's lifecycle
• This includes internal developer experience, as exemplified by Netflix's approach to developer productivity tools
• Three buckets of software development lifecycle: internal infrastructure, developer tools, and external developer experience
• Improving productivity by 1% can justify hiring an internal developer experience person for every 50 engineers
• External developer experience includes product design, API design, first-party media channels, community engagement, and third-party content creation
• Strategies for growing a third-party ecosystem include super-user programs, influencer marketing, and career development opportunities
• Importance of nurturing relationships with users to create self-sustaining communities
• Role of friction logs in prioritizing developer experience improvements
• Discussion of the Kubernetes Empathy Sessions as an example of empathy-driven community building
• The importance of testing products with users who have not been involved in their development
• The value of "dogfooding" a product by using it internally and experiencing its pain points firsthand
• The potential drawbacks of not paying for one's own product, including missing out on the customer experience and difficulties in communicating with support teams
• The significance of money and billing as part of the developer experience
• A discussion about a vendor changing their pricing model unexpectedly, highlighting the challenges of managing costs and tech choices
• Temporal library's stage and progress
• Moment.js vs Date-FNS, and the benefits of built-in date functionality in JavaScript
• Availability of new features in embedded environments due to low system memory requirements
• Naming collisions with existing libraries or functions
• Developer experience and teaching others about new technologies