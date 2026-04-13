• Definition of serverless Postgres
• Benefits of serverless Postgres, including consumption-based pricing and right-sizing of resources
• Adoption of serverless Postgres, including challenges and reasons for slower adoption in the database world
• Categories of users adopting serverless Postgres, including indie developers, software developers, and professional organizations
• Comparison of serverless Postgres offerings, including Neon, Planet Scale, and Aurora
• Factors contributing to the growth of serverless Postgres, including friction and costs
• Reducing friction and cost for developers to experiment and explore new technologies
• Introducing features that give developers "permission to mess up", such as branching and Time Machine
• Discussing the challenges of merging database changes and the importance of understanding data and schema changes
• Exploring the concept of "scaling to zero" in databases and the difficulties of achieving it
• Describing the approach to achieving cost-efficient database scaling through separating storage and compute, and using a multi-tenant and distributed storage system
• Discussing the use of micro VMs for compute and caching, and the ability to scale them to zero and preserve state
• Developing technology for live migrations of VMs, including cache and CPU adjustments, with Cloud Hypervisor
• Using Amazon S3 for cold data storage, and integrating with S3 through LSM Tree data structure
• Evaluating and planning to expand to other public cloud providers, such as Fly and Google Cloud
• Managing data storage economics, including separating compute and storage, and storing data in S3 in a compressed form
• Developing and implementing a serverless Postgres architecture, with a focus on developer experience and separation of compute and storage
• Discussing the infrastructure and team aspects of building and maintaining a complex system like Postgres
• Addressing the importance of confidence in architecture and the need for continuous testing and improvement.
• Changes made to Postgres for separation of storage and compute in the cloud
• Five patches submitted to Postgres upstream for acceptance
• Neon's open-source storage project, under Apache 2.0 license, separate from Postgres
• Potential for Neon's storage project to be integrated with Postgres in the future
• System architecture: patches for Postgres, Neon extension, and Kubernetes for multi-compute setup
• Scalability and storage efficiency features in Neon's storage project
• Algorithm for automatically removing older data from cache based on usage patterns
• AI applications in database management, including auto-tuning and generative AI
• Decoupling compute and storage
• Geographic distribution and the challenges of managing a globally distributed database
• Solutions for replicating data across regions, including read-after-write issues and the use of proxies to mitigate them
• Comparison of different paradigms for managing globally distributed databases, including multi-master replication and distributed consensus algorithms
• Fine-tuning and data distribution in Neon's database architecture
• Alternative approaches to data distribution, such as row-based versus page-based
• Partitioning and region assignment in distributed databases
• The trade-off between elegance and pragmatism in database design
• Developer experience and user experience in database design
• Serverless, branching, and time machine features in Neon's database
• Developer experience best practices, including CLI, API, and documentation
• Instant provisioning and cold starts in database development
• Instantly shareable environments and application previews in database development
• Team collaboration and CI/CD pipelines
• Developer experience (DevEx) and its importance
• Communicating DevEx to end-users through transparency and feedback loops
• Roadmap and transparency: making the roadmap public and accessible
• Company progress and timeline: 18 months working on the product, 36 people on the team, and expecting first dollar in Q1 2023
• Business model and revenue generation: usage-based consumption and volatility impact on revenue
• Consumption-based pricing aligns value with customer consumption
• Subscription-based pricing can lead to overcharging and wasted resources
• Companies like Snowflake and Twilio have adopted consumption-based models
• Video streaming services, such as Netflix, are examples of unnecessary subscriptions
• Aligning pricing with customer value increases simplicity and trust
• Consumption-based pricing reduces risk for customers and makes sales easier
• Postgres is a growing market share in the database market, particularly in the cloud
• The cloud market is dominated by hyperscalers, but Postgres is gaining ground
• MongoDB's license issues and reliance on Postgres hinder its growth.
• Postgres cloud service market size and potential
• Goal of creating the best Postgres cloud service
• Company's roadmap and future plans
• Engineering and product teams, including job openings
• Auto-scaling, integrations, and live VM migrations
• Generative AI features for automatic index suggestions and schema changes
• Plans for removing invite gates and implementing pricing and billing
• Generous free tier for developers and hobbyists
• Concerns about abuse and potential solutions using AI and machine learning
• Fly.io vs. actual VMs
• Importance of long-term optimization and scaling
• Trade-offs between free tier, user adoption, and revenue expectations
• Partnership with Hasura for seamless onboarding
• Workarounds for accessing Neon without an invite (tweeting for an invite, Hasura integration)
• Plans for resource-based billing, regions, and branching features
• Excitement for Neon's future growth and potential