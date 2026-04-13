• Definition of serverless technology: a marketing term for cloud services where infrastructure is managed by providers
• Serverless features: event-driven work, pay-as-you-go model, automatic scaling and no need to worry about underlying infrastructure
• Use cases for serverless: small microservices, cron replacements, simple image processing (e.g. uploading images to S3)
• Drawbacks of serverless: not suitable for maintaining state or long-term state on the app tier
• The importance of a "glue layer" in serverless architecture, where services actively communicate with each other
• Cloud providers' need for serverless protocols to interact with users and provide execution environments
• Treating serverless functions as stateless web services, where instances are spun up/down dynamically
• Asynchronous event-driven architecture using queues and serverless functions
• Costing model misconceptions: just because you're not paying for idle resources, it doesn't mean you can go "haywire" with small functions
• Importance of considering concurrency primitives (e.g. goroutines) in serverless functions to optimize cost and performance
• Portability of serverless functions across different cloud providers
• Limitations and trade-offs of using abstraction models for portability
• Cost-benefit analysis of creating cloud-agnostic code versus importing third-party libraries
• Difficulty in achieving true multi-cloud functionality, especially with orchestration and configuration aspects
• Importance of separating business logic from cloud-specific APIs and implementation details
• Serverless environment requires adjustments in code for optimal performance
• Cold start issues and deferring setup for handlers are common considerations
• Using sync.Once package can help manage global state and reduce bugs
• Global state should be avoided, especially with serverless architecture
• Testing on local machine is recommended before deployment to avoid serverless-specific complexities
• Cleanup and unsetting global state are still important even in a serverless environment
• Security implications of instance reuse must be considered when developing serverless applications
• Integration-level testing: when and how to test serverless applications
• Development strategy for serverless apps: emulating environments vs running in test accounts
• Importance of logging and observability in serverless environments
• Orchestration of multiple functions in serverless applications: best practices and tools (e.g. Step Functions)
• Environmental cost of serverless computing vs traditional approaches
• Discussion on AWS serverless computing usage and optimization
• Challenges in debugging serverless applications due to lack of centralized logging and visibility
• Importance of distributed tracing in navigating complex systems and identifying problem areas
• Need for standardization in instrumentation and correlation logging across cloud providers
• Status of distributed tracing as a developing tool with increasing consensus on standards
• Discussion on the benefits of serverless technology for Go developers
• Comparison with traditional development approaches and the need for a different mindset
• Importance of learning serverless as it enables efficient glue work and stitching without infrastructure management
• Productivity gains from using opinionated, limited environments that delegate work to cloud providers
• Learning serverless as a means to improve understanding of distributed systems and non-serverless systems
• Addressing concerns such as statelessness, sticky sessions, and concurrency models in serverless development
• Discussion on the limitations and challenges of serverless technology, including massive parallelism and its impact on database connections.
• Serverless discussion
• Return of Jaana to the show
• Interview with Stevenson Jean-Pierre
• Behind-the-scenes work by Jon Calhoun
• Upcoming show ideas and participation in Slack channel