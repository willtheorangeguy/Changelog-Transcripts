• What Kafka is and how it works as a publish-subscribe system for messaging
• Use cases for Kafka, including moving data from point A to point B, observability and security-related workloads, and custom applications
• Why Kafka is considered a polarizing technology, including its difficulty to run and high cost of running in the cloud
• Specific cost breakdowns for running open source Kafka in AWS, including minimum costs for replication and storage
• Comparison of running Kafka in a public cloud versus on-premises, including the challenges and differences in cost
• Polarization around Kafka's developer programming model
• Challenges with running Kafka, including scaling up/down and managing cluster rebalancing
• Cost concerns and egress fees in cloud environments
• Comparison to WarpStream and its designed architecture
• Practical challenges with improving a large open source project like Kafka
• Trade-offs between different system architectures and environments
• History of Kafka's design and its original purpose at LinkedIn
• Capacity planning for EC2 instances and on-demand rates
• Why Amazon charges higher rates for EC2 instances compared to buying a server off the internet
• The concept of "worst case scenario users" and how it affects cost planning
• The story of how Ryan Worl and Richard met and started working together, including their time at Datadog
• The development of Husky, a system that replaced Datadog's legacy system for observability data
• The similarities and differences between Husky and Kafka, including the use of object storage
• The importance of understanding object storage characteristics, including latency and oversubscription
• Designing systems to work with object storage, including thinking of it as a "very large, oversubscribed array of spinning disks" and retrying requests speculatively
• The challenges of using tiered storage and trying to match the characteristics of object storage with faster storage options.
• Cost savings with object storage for infrequently accessed data
• Limitations of open-source tiered storage in Kafka
• Decoupling ownership of partitions from brokers in WarpStream
• Stateless agents in WarpStream for scalable data access
• Comparison of broker architecture in open-source Kafka and WarpStream
• Trade-offs between latency and durability in WarpStream
• Applications where high real-time performance is critical (e.g. credit card fraud detection)
• Analytical applications (e.g. moving application logs) are more tolerant of latency and can benefit from WarpStream's cost-effectiveness
• WarpStream's object storage-based architecture enables cost savings for high-volume workloads
• Latency is a key consideration, with writes at 500ms (P99) and end-to-end latency at 1-1.5 seconds (P99)
• Alternative to open-source Kafka, WarpStream offers features like agent groups for flexible cluster deployment and reduced security risks
• Hosting flexibility is provided through S3-compatible interfaces and support for various object storage solutions
• R2 could provide additional savings for users running compute in specific providers with free peering
• WarpStream's demo (a curl-based install script) aims to provide a painless and hacker-friendly way to try out the product
• The WarpStream demo is designed to show the product's capabilities in a simple and easy-to-understand way, but it has limitations.
• The Playground mode allows users to start a cluster for local development without the need for extensive setup or cost.
• The product's compatibility with Kafka is crucial for its success, as it allows users to integrate with existing open-source tools and avoid rewriting their applications.
• WarpStream has achieved significant success with large use cases in production, processing multiple gigabytes of traffic per second.
• The company is finding success with large open-source users who feel that the open-source product is too challenging to run and are facing budget pressure.
• Greenfield projects with high data volume are not ideal for WarpStream, but existing initiatives within companies are successfully adopting the product for cost reasons
• WarpStream is a commercial product that is not open source, despite being compatible with Kafka
• The company's decision not to release WarpStream as open source is due to concerns about being able to invest in the product without being tied to an open-source model
• Commercial open-source companies often face challenges such as competition, patent enforcement, and pressure from investors, which can lead to "re-licensing" and negative brand reputation
• The founders of successful commercial open-source companies have advised against starting a new company as a commercial open-source entity due to the current market challenges
• Challenges of going upmarket and competing with open source projects
• Limitations of exerting pricing pressure on enterprise customers for open source products
• Difficulty in monetizing open source projects through support contracts
• Benefits of providing a valuable product to compete with open source alternatives
• Challenges of bootstrapping and maintaining equity with a small team
• Rationale for raising venture capital to accelerate growth and hiring
• Market size and potential for multiple players in the Kafka market
• Concerns about competitors copying and open-sourcing existing products
• Importance of having a safety net (e.g. funding) for founders and employees
• Challenges of selling to enterprise buyers without VC funding
• Trade-offs between VC funding and commercial open source business models
• Raising VC funding as a means to increase chances of success and bigger outcomes
• Balancing act between VC investors' interests and founders' goals
• Potential risks of being copied by hyperscalers (e.g. Amazon) if offering an open-source product
• Difficulty of competing with established players in the market
• Announcement of a new product or feature similar to WarpStream's direct-to-S3 approach
• Pricing and cost-effectiveness of WarpStream compared to competitors (Kafka)
• Importance of support and response time for enterprise customers
• Cost savings of using WarpStream over Kafka for large workloads
• Comparison of costs for different retention periods and scalability
• Trade-offs between cost and developer experience, operational burden, and ease of use.
• Key benefits of WarpStream highlighted as value proposition
• Cost savings emphasized as primary promise
• Other benefits seen as icing on the cake
• Discussion of WarpStream's commercial open source approach
• Importance of seeking input and learning from others in decision-making
• Recap of the conversation and thanks to Ryan Worl