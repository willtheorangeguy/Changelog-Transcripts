• The Skyhook team worked together in 2019 on a serverless project and have since been out of touch.
• The COVID-19 pandemic had a significant impact on Skyhook as a travel website business, but also presented an opportunity to rethink their product and improve it.
• Skyhook is a website that allows users to book adventure trips with local guides, providing a unique and authentic experience.
• The team decided to move towards serverless technology, initially using AWS Lambda functions backed by an RDS database (Aurora).
• They later realized the limitations of this approach and began exploring other options, including DynamoDB and splitting their services into separate databases.
• The team eventually moved to a more modular architecture with each service having its own DynamoDB database.
• Switch from REST API to GraphQL/AppSync
• Implementation of a microservices-based architecture with serverless functions
• Improved reliability and reduced bugs in the system
• Reduced deploy times from 20 minutes to 3 minutes
• Increased testing and faster feedback cycles
• Addition of feature flags for rapid feature deployment and customer testing
• Using AWS AppSync for synchronous communication between microservices
• Utilizing AWS Event Bridge for asynchronous communication between services
• Implementing Next.js with Vercel for server-side rendering and caching of static pages
• Serving the application through a custom deployment environment using GitHub Actions and Vercel's zero-config option
• Achieving fast latency (10ms) in internal service interactions, but potentially improving it
• Exposing API services to individual microservices for data querying
• Using standardized JSON objects with schemas for event bus messages
• Discussion of Vercel vs Netlify for zero-config deployment
• Benefits of using Vercel with Next.js as the parent company
• Managing environments, including multiple PR-specific URLs and data migration
• GitHub Actions setup for automated testing and deployments
• Single repository approach for microservices, including benefits and challenges
• Automated testing and linting on code changes, including integration tests
• Configuration and setup of services using Hygen tool for CDK and AWS
• Storage of configuration in the repository next to usage
• Changes to infrastructure deployment using AWS CDK
• Avoidance of CloudFormation due to complexity and yaml issues
• Development experience improvements, including environment portability and data management
• Challenges with payments provider during pandemic, including disabled refunds and changed regulations
• Discussing potential solutions for improving development experience and overcoming current challenges
• The importance of customer experience and managing risks in third-party services, particularly with payment providers
• A case study on a travel company's experience with a payment provider that suddenly prevented automatic refunds across their API
• How the company resolved the issue by convincing their provider to re-enable automatic refunds for them
• An alternative solution using tools like Spreedly to hook in with multiple payment providers
• A second incident where a system issue was solved with an unorthodox approach involving event streams and Lambda functions
• The importance of prioritizing customers' needs over shipping code or adding new features
• A discussion on the feature "hosts sign-up" that improved the process for hosts to get signed up, resulting in a 5-fold increase in host sign-ups
• Development of a user-friendly cancellation feature on the Skyhook marketplace
• Utilization of third-party tooling (e.g. Algolia) to implement features such as search functionality and improve development speed
• Adoption of serverless tools (e.g. AWS Lambda) for faster code deployment and improved customer experience
• Use of Drip for email marketing services due to its e-commerce specialization