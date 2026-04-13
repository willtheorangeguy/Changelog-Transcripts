• Serverless computing explained
• Functions as a service (FaaS) discussed as part of serverless
• Difference between FaaS and microservices highlighted
• Nanoservices concept introduced in serverless context
• Comparison made between traditional monolithic applications and serverless architecture
• Jeremy Daly's experience with serverless as CTO of AlertMe.News mentioned
• Machine learning component requires more resources and can be scaled independently
• Nanoservices allow individual components to scale without affecting the entire microservice
• Microservices are composed of smaller "functions" that can be deployed individually in a serverless environment
• Functions within serverless environments, such as Lambda or Xur, can communicate with each other and other services
• The concept of nanoservices allows for more granular scaling and team organization
• Serverless computing breaks down the traditional notion of microservices and applications into smaller, independently scalable components.
• Communication with databases through APIs or API gateways
• Microservices architecture and separation of concerns between services
• Technical scaling and team ownership in serverless environments
• Differentiation between cloud providers (AWS, IBM, Google) and their implementation of serverless functions
• Standardization efforts for serverless events and function definition
• How serverless functions receive and respond to inputs from various sources (e.g. REST calls, message queues)
• Consistency across different cloud providers and services (Lambda, OpenWISC, Google Cloud Functions)
• Value proposition of serverless computing
• Comparison with microservices and traditional development methods
• Benefits of speed and ease of deployment with serverless
• Auto scaling and resource management in serverless environments
• Example use case: image processing component for startup
• Discussion of tools and frameworks for serverless development (AWS SAM, Claudia JS)
• The speaker discusses their experience with serverless computing and its benefits over traditional infrastructure management
• They compare the speed of launching a new virtual machine or server with Kubernetes/Docker/ECS/EKS vs serverless options like AWS Lambda
• Serverless reduces operational work (but doesn't eliminate it) and saves money on idle time and infrastructure costs
• The speaker highlights potential downsides, including local development difficulties due to lack of direct access to underlying resources
• They mention that tools are being developed to improve local development experience, but current solutions have limitations
• Limitations of serverless functions, such as time limits and memory constraints
• Cloud providers taking risk on idle time, reducing costs for users
• Need to run local versions of dependent services, such as databases
• Challenges in testing microservices with remote dependencies
• Version compatibility issues between cloud provider's Node.js version and the user's chosen version
• Importance of considering platform stability when using serverless functions
• Upgrades and versions of Node.js on Lambda
• Benefits of serverless architecture for diversifying technology use within microservices
• Ability to use multiple languages and frameworks within a single service or team
• Smaller code base and ease of maintenance with serverless architecture
• Management of code bases, including Git repository organization
• Organizing serverless functions and microservices in separate Git repositories
• Pros and cons of separating functions into smaller files vs. consolidating them
• Managing cold starts and performance issues with consolidated functions
• Potential solutions for abstraction, such as splitting code into multiple services behind the scenes
• Importance of documenting interfaces and events between microservices
• Concept of splitting a service into multiple functions
• Comparison with web frameworks like Express
• Introducing Lambda API, an open-source project for AWS and Lambda
• Separating business logic from routing in microservices architecture
• Code sharing between microservices, including database connection layers
• Managing versioning and updates in shared codebases
• Alternative corrections to queries using Algolia
• Using serverless technology in the broader ecosystem of product development
• Evaluating whether to re-architect an entire system for serverless or use it incrementally
• The Strangler pattern as a method for migrating pieces of an application at a time
• Building applications from scratch with serverless, including authentication and other considerations
• Using cloud-agnostic frameworks like Serverless Inc's V2 that allow for running functions in containers
• Focusing on the business logic and processing needs when building a new serverless application
• Discussing the future of serverless applications and CDNs
• Exploring Cloudflare workers and Lambda Edge for global distributed CDN functionality
• Pushing application logic out to the edge (CDN) to reduce latency
• Caching data on the edge for faster load times
• Limitations of executing code at the edge due to speed of light constraints
• API calls and edge servers
• AWS authentication and IAM roles for accessing Lambda functions
• Authentication and authorization through API gateway and policy documents
• Serverless observability platforms, including Dashbird, Epsilon, and Thundra
• Security aspects of serverless computing, including event injection and remote code execution attacks.
• Funding trends in serverless technology
• AWS Lambda's new 15-minute execution times and application view features
• Upcoming release of AWS Reinvent
• Serverless framework as a tool for getting started with serverless development
• Comparison of serverless providers (AWS, Azure, Google Cloud Functions)
• Importance of standardization and consolidation in serverless technology
• Resources for learning more about serverless development (serverless.com, serverless conf videos)
• Scheduled meeting for next week