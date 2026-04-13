• Microservices vs Monoliths
• Working from home tips (turning off Slack notifications, having a nice workspace)
• Matt Heath's experience with breaking down large applications into smaller components
• Benefits and trade-offs of monolithic architecture
• Tom Wilkie's attempt to deploy passwords to neighbors' homes as a working from home tip
• Isolation in microservices can be beneficial for separating read and write paths
• Some organizations start with microservices at design time, while others introduce them after experiencing pain points
• Scalability and organization scalability are the main concerns that lead to considering microservices
• Microservices may not solve all problems, but rather move them elsewhere
• Monoliths can have advantages in terms of ease of development and deployment
• Monorepos can provide some benefits of monolithic architectures while still allowing for microservices
• Deployment flexibility and control
• Trade-offs between microservices and monoliths
• Simplifying deployment with a single binary or process
• Complexity of deploying multiple services on local machines
• Variability and scale of service-oriented systems (e.g. Monzo's 1,600+ services)
• Granularity and separation of concerns in service design
• Deployment strategy for microservices across multiple availability zones
• Use of protocol buffers for defining consistent APIs between services
• Importance of isolation and independence in microservice development
• Team ownership and responsibility for specific services or service groups
• Comparison of microservices to monoliths, including advantages and drawbacks
• Role of tooling and automation in mitigating deployment and testing challenges
• Challenges with release engineering in microservices environments
• Difficulty in debugging and troubleshooting complex distributed systems
• Importance of tooling and metrics for understanding system performance
• Trade-offs between complexity and efficiency in system design
• Use of proxy services and service mesh architecture for debugging and monitoring
• Benefits of being able to deploy specific tools or features live without affecting the entire system
• Microservices architecture complexity and the need for tracing
• Volume of moving parts and metrics in microservices
• Observability system requirements for incorporating metadata and dimensionality
• Rise of systems like Prometheus to support multi-dimensional data and rich integrations
• Comparison with monolithic architectures
• Automatically instrumenting RPC boundaries for instrumentation purposes
• Techniques for collecting execution trees and visualizing performance
• Discussing a clamp (as an aside) 
• Microservices and testing, with benefits to isolated service testing
• Difficulty in integration testing across microservice boundaries
• Unit testing vs. isolated service testing
• Challenges of mocking services and dealing with complexity
• Use of staging environments for load testing and production monitoring
• Continuous deployment and better tooling for more accurate testing
• Propagating environment variables for mirroring production/staging traffic
• Prototypes of new features running in staging environments for testing and isolation between teams
• Unpopular opinions discussion:
  • Tom Wilkie: Jsonnet is the future for config management, Helm is overrated
  • Matt Heath: Microservices can be unpopular due to complexity perception
  • Jaana Dogan: Working on a single service in a large organization is similar to working on a monolith
• The benefits of building internal tooling and microservices in a small company
• Thinking about future separation of components even when building monoliths
• Importance of building nice interfaces for potential external use
• Discussion of a previous 3D-printed clamp project
• Conversation about online presence and internet searches