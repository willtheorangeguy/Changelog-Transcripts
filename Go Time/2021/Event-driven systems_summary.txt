• Event-driven systems basics
• Daniel Selans' background and experience with event-driven systems
• Batch.sh startup and data pipeline company
• Steve High's experience with event-driven systems and NTWRK company
• Definition and explanation of event-driven system concepts (asynchronous messaging, state change, message bus)
• Example of event-driven system architecture in action (user signing up and paying for a plan)
• Benefits of event-driven architecture include improved performance and scalability
• It allows for asynchronous batching of messages, reducing IO boundaries and improving throughput
• Event-driven systems force discipline in communication across the stack and make it easier to create a common lexicon of types
• They provide a solid foundation for future growth and can help avoid decoupling complex monoliths later on
• However, event-driven systems can be complex and may not be suitable for all startups or use cases
• The choice between synchronous and event-driven architectures depends on specific goals, such as high throughput and scalability requirements
• Event buses (message brokers) are a key component of event-driven tech, allowing for centralized messaging and queuing of events
• Eventual consistency problems arise from allowing writes to be processed asynchronously
• Idempotency is key: services should handle duplicate events without causing issues
• Exactly-once delivery is unreliable and often impossible; focus on idempotency instead
• Techniques for idempotency include using timestamps, event IDs, or service-specific caches
• Event-driven systems naturally provide audit logging and event history due to the event source of truth
• Developer experience improves with event-driven systems as they simplify tasks like seeding a developer database
• Replay functionality for events
• Event-driven architecture vs event sourcing
• Use cases for replaying events in testing
• Best practices for designing and updating events
• Using protobuf as a message envelope for event design
• Avoiding JSON and using strict schemas for conflict-free development
• Discussing the benefits of using Protocol Buffers (protobuf) for data serialization, including its ability to work with complex schemas and provide a unified format
• Comparing protobuf with JSON, highlighting the limitations of JSON in representing complex data structures
• Exploring the integration of protobuf with other tools, such as Qlang, which provides additional constraints and validation features
• Discussing the benefits of using Go for event-driven systems, including its concurrency primitives and simplicity
• Highlighting the quality of Go libraries for event buses and message buses
• Recommending a setup for building an event-driven system in production, including Kafka for high-throughput messaging and RabbitMQ for interservice communication
• Providing guidance on getting started with event-driven development in Go, including using RabbitMQ and protobuf for simplicity
• Etcd as a caching layer and its benefits
• Importance of understanding low-level communication protocols (e.g. wire protocol) when working with message buses like MQTT
• Risks of relying on complex message buses like RabbitMQ without thoroughly learning their features and limitations
• Potential drawbacks of continuous deployment, including breaking systems at critical times
• Value of manual, controlled deployment processes and ownership of deployments by developers
• Ownership and responsibility in development and deployment
• Automating everything vs manual oversight
• GitHub's deploy process and verification system
• Error handling in Go (reusing the variable name "err")
• Naked braces syntax in Go for increased readability
• Organic idioms in error handling (e.g., using the word "err")
• Difficulty in refactoring code to return specific error types
• Type switches and unwrapping interfaces as potential code smells
• Limitations of reusing error variables due to different error types
• Alternatives to error.is, such as returning rich error objects or using bitmasks
• Higher-level error libraries often being created after the fact and not meeting expectations
• Challenges in justifying spending time on improving error handling
• Importance of properly handling conflicts and errors in software development.
• Inconsistent error handling in codebases leads to difficulties in debugging and observability
• Importance of checking all errors, including those that may be rare or edge cases
• Consistency in propagating errors throughout a system is crucial for good observability
• Handling errors with detailed information vs. generic messages affects user experience
• Selective security thinking can lead to inconsistent security practices
• Password reset forms and other interactive systems can frustrate users if they don't provide clear, detailed error messages