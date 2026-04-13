• Definition and basics of event-driven architecture
• Misconceptions about event-driven systems and the need to dig deeper into definitions
• Event-driven style of architecture as modeling real-world events and asynchronous behavior
• Relationship between microservices and event-driven systems, including organizing mutations of data and complexity
• Specific examples of using sagas and choreography with events in a microservice architecture
• Decoupling services for improved runtime efficiency and reduced latency
• Orchestration vs Choreography: differences in coupling, safety, testability, and explicit process representation
• Event-driven architecture principles and trade-offs (e.g., concurrency issues, load management)
• Comparison of orchestration-based systems with a centralized orchestrator and choreography-based systems without a central controller
• Example implementations of choreography-based systems (e.g., database tables for service communication) vs orchestration-based systems (e.g., request-based services)
• Evaluation criteria for choosing between event-driven architecture and other approaches, including consideration of trade-offs and system requirements
• Synchronous vs asynchronous systems
• Event-driven architecture using events, commands, and replies
• Choreography-based systems use event messages for coordination
• Orchestration-based sagas use command/reply messages for communication
• Commands are requests to do something, whereas events represent something that has happened
• Business capability boundaries define how services communicate with each other
• Contexts and interconnections between them
• Designing systems with loosely-coupled parts for scalability and maintainability
• Orchestration vs choreography trade-offs
• Events as a way to decouple services and allow extension without modification
• Applying the open/closed principle through event-driven architecture
• Implementing systems with orchestration, choreography, or a combination of both
• Evaluating existing cloud vendor tools for event handling
• Importance of atomicity when updating databases and sending messages
• Transaction outbox pattern for ensuring consistency and data integrity
• Use of open-source platforms (e.g. NServiceBus, MassTransit) to implement saga patterns and ensure data integrity
• Orchestration frameworks (e.g. Eventuate, Temporal) for more complex workflows
• Idempotent consumer pattern to handle duplicate message delivery
• Designing systems with abstraction layers to decouple messaging technologies from application logic
• Trade-offs in choosing a messaging technology (e.g. latency, throughput, scalability)
• Flexibility and potential need for change as business needs evolve
• Importance of change management in system evolution
• Strategies for upgrading complex systems incrementally
• Event-driven architecture and its trade-offs
• Design patterns and thinking critically about problem-solving approaches
• Unpopular opinions on food, including the superiority of burritos over lobster and the simplicity of coffee ingredients.
• Coffee and food preferences
• Criticism of overly technical solutions to complex problems
• Importance of considering people and organizational issues in software development
• Concerns about the focus on developer platforms and technology over human-centered problem-solving
• The need for more effort to be put into interpersonal communication and collaboration in the workplace