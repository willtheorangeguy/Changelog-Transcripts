• Distributed messaging systems
• NATS (distributed messaging system written in Go)
• Challenges of building distributed messaging systems
• History and evolution of Pub/Sub technology
• Importance of messaging as a connecting technology for distributed systems
• Common pitfalls in using point-to-point communication instead of messaging systems
• History of messaging systems and NATS
• Derek Collison's background with Go and its impact on his choice of technology
• Fan-out approach and decoupling in architecture
• Role of messaging in modern, distributed architectures (nanoservices)
• Importance of addressing and discovery beyond IP addresses
• Pub/sub messaging patterns and abstraction
• Benefits of decoupling and avoiding assumptions about message usage
• The speaker discusses the evolution of system design, from traditional client-server architecture to modern microservices and messaging systems.
• They argue that traditional HTTP request-response architecture is not suitable for large-scale distributed systems.
• Messaging systems, such as NATS, are proposed as a more efficient and scalable solution.
• Key benefits of messaging systems include simplicity, flexibility, and low operational overhead.
• The speaker also highlights the cost savings (80% OpEx reduction) possible with messaging systems compared to traditional cloud-based solutions.
• He suggests that people get introduced to messaging systems by starting small and tackling common problems such as logging and anomaly detection.
• The discussion also touches on the complexity of scaling traditional request-response architectures.
• Load balancing as a starting point for NATS adoption
• Advantages of NATS beyond production environments, including design simplicity and lightweight architecture
• Impact on application design due to decoupling from message queues
• Addressing discovery and security in microservices environments
• Consistent identity authentication and authorization with NATS
• IoT applications as a key use case for NATS
• Centralized vs. decentralized communication systems in the context of remotes (e.g., IoT devices)
• Pattern recognition across various industries and technology backgrounds
• NATS as a generic abstraction for various problems
• IoT use cases and implementation
• Multi-tenancy in distributed systems
• Account isolation with secure sharing
• Flexible subject naming and token-based authorization
• Mixing and matching utility models (e.g., SaaS, on-premises) 
• Avoiding "or-conversation" (either cloud or on-premises) and achieving an "and-conversation"
• Creation of NATS 2.0 and its main differences from previous versions
• Security model in NATS 2.0, focusing on forward-looking security with no private keys or passwords
• Multi-tenancy capabilities in NATS 2.0, requiring changes to the codebase rather than a patch
• Global topology support in NATS 2.0 for handling lossy systems and varying network conditions
• Backward-compatibility of NATS 2.0 with previous versions, allowing existing configurations to work seamlessly
• Differences between NATS and other messaging technologies like SQS, RabbitMQ, and Kafka
• Business model for the company behind NATS, focusing on making it a viable business through various revenue streams
• NATS as a service with global network capabilities
• Recurring on-premise support and training for complex use cases
• Basic and premium services offered through NATS, including messaging, queuing, load balancing, circuit-breaking, self-healing, state storage, object storage, GraphQL services, and advanced analytics
• Software license revenue from companies requiring specialized features or running NATS in their own data centers
• Business model focused on recurring support as initial major revenue driver, with NGS and direct revenue increasing over time
• Challenges with transitioning from free to paid models in open-source software
• Difficulty finding a clear distinction between free and paid features in open-source software
• Importance of creating a value-added service over just providing a feature or functionality
• The open core model as a way to monetize open-source software
• Need for careful consideration of business models when building a company, rather than relying on assumptions about what users will pay for
• Most systems that appear distributed are not truly distributed
• Using HTTP to connect modern distributed systems can lead to complexity
• Sidecars and load balancers can make systems unnecessarily complicated
• Building a business around an open source project is challenging
• Understanding the psychology of consumers is key when building software
• Changing consumer behavior from expecting free products or services is difficult
• The guest, Derek Collison, shares a story about visiting a financial institution to resolve an issue with their software.
• He was presented with a suit and told to fly to New York for a meeting with the CEO.
• Upon arrival, he discovered that the issue wasn't with his company's software but rather a configuration problem with the Sun operating system.
• During the 12-14 hour wait for the CEO to arrive, Derek wrote a program to demonstrate the issue and ultimately resolved it by manipulating the OS to optimize performance.
• The guest concludes with a lesson learned: even if an issue isn't your fault, own up to it and be nice, as it could have been your problem.