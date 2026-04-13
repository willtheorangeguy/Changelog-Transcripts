• Definition of serverless: where developers don't have to worry about provisioning servers
• Comparison to "functions as a service": functions are part of serverless, but there's more to it than just functions
• Relationship to microservices: serverless is a way to deploy microservices and can enable nanoservices that scale independently
• Introduction to nanoservices: individual components within a microservice can be scaled separately in a serverless environment
• Evolution from monolithic applications to microservices to serverless: each step allowing for greater scalability and independence
• Differences between traditional microservices and serverless architecture
• Functionality and organization in serverless platforms (AWS Lambda, Google Cloud Functions, etc.)
• Standardization efforts for events in serverless functions
• Value proposition of serverless compared to traditional microservices and splitting them down further
• Technical scaling vs team scaling in serverless environments
• Traditional development and operations separation can lead to slow deployment times
• Serverless computing allows for rapid application deployment and autoscaling
• Benefits include reduced operational costs, improved scalability, and increased developer productivity
• However, serverless computing has its limits, including function execution time limits and arbitrary resource constraints
• Local development with serverless frameworks is possible but can be complex due to dependencies on cloud services
• Cost savings are significant compared to traditional infrastructure management, but come at the cost of vendor lock-in and arbitrary resource limitations
• Limitations of serverless computing and when it's not suitable
• Running functions locally: challenges and workarounds (e.g. mocking, local versions of dependent services)
• Node.js version compatibility issues with Lambda and other cloud providers
• Advantages of serverless architecture, including ability to use multiple languages within a single microservice
• Benefits of splitting functions into small units for easier maintenance and replacement
• Managing large codebases and identifying unused code
• Organization methods for serverless functions, including separate Git repositories for each microservice
• Challenges with managing multiple microservices, including complexity and shared codebases
• The concept of "cold starts" and the benefits of consolidating routes into single Lambda functions
• Abstraction tools that allow developers to write code as if it were a single entity while still separating services behind the scenes
• Challenges of shared code in microservices architecture
• Versioning and managing shared libraries in serverless applications
• Reusing code within individual microservices
• Architecture patterns for implementing serverless applications
• The strangler pattern for migrating pieces of an application at a time
• Building new applications with serverless vs. traditional methods
• Limitations of serverless technology, especially for long-running tasks
• New developments in serverless frameworks and cloud-agnostic options
• Using serverless functions to manipulate and cache content in CDNs
• Discussion on the limitations of serverless technology when it comes to performance and latency
• Benefits of pushing application logic out to the edge, including reduced latency and increased efficiency
• Caching capabilities at the edge and how they can improve performance
• Use of AWS services such as Lambda and API Gateway for serverless architecture
• Authentication and security considerations in serverless environments
• New advancements in serverless observability, including tools from companies like Dashbird, Epsagon, and Thundra
• Funding trends in the serverless space with recent investments in PureSec and Serverless
• AWS Lambda updates: 15-minute execution times and upcoming announcements at AWS Reinvent
• Ease of getting started with serverless using the Serverless framework
• Comparison of cloud platform providers (AWS, Azure, Google Cloud Functions, IBM OpenWhisk)
• Importance of standardization across different serverless platforms