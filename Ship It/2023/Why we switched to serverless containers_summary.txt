• The guest speaker Florian Forster and host Gerhard Lazu discuss a talk on switching from Kubernetes to serverless containers
• Reasons for switching include scalability limitations in Kubernetes and better cost profiles with serverless containers
• Serverless containers refer to running OCI images without managing underlying infrastructure, similar to AWS Fargate or Google Cloud Run
• Florian has been working with Kubernetes since its early days, around 2014-2015, and has a deep understanding of its complexities
• He compares Kubernetes to an "operating system" that requires too much management and abstraction for his company's needs
• The discussion touches on the concept of "serverless" and alternative terms such as container-as-a-service
• Florian is currently the CEO/CTO of Citadel, where he focuses on overall vision, business side, and easing operational stress
• Citadel's purpose and functionality
• Citadel's architecture and components (key cloaks, zero trust model)
• CPU requirements for hashing and token generation
• GPU usage and potential future integration
• Network requirements and latency optimization
• Workload patterns and traffic predictions
• Tech stack: Cloud Run, CockroachDB, Google CDN, Global Load Balancer, Cloud Armor, Datadog, Google Suite
• Company uses Google Cloud, CockroachDB, Datadog, TerraForm, GitHub Actions, and other tools for infrastructure provisioning and management.
• 80% of company employees know Git and use it for source control; Citadel software is built with GitOps principles in mind.
• The majority (80%) of the tooling used is for the cloud service, with the rest being for binary building.
• GitHub Actions, Docker files, and custom-built shell scripts are used for CI/CD pipeline management.
• Automated testing tools like Cypress and static analysis tools like Dependabot, CodeQL are used to ensure code quality and security.
• The company has 8 dedicated engineers working on Citadel's code and 20-25 external contributors across multiple projects.
• Poor documentation is a major pain point for the company; they plan to invest heavily in improving API documentation and user guides.
• A clear and well-structured documentation flow is essential for showcasing the value of the product to users.
• Challenges of self-hosting infrastructure
• Comparison of Cloud Run with Microsoft and AWS, including issues with HTTP support and documentation
• Requirements for end-to-end HTTP support and gRPC APIs
• Limitations of Cloud Run, including internal artifact registry and VPC connector
• Global deployment strategy for Citadel service with multiple regions and pop-ups
• Engineering decisions around scaling and region deployment
• Discussion of slow start times for Java-based applications
• Influence of container image sizes on startup latency
• Evaluation of Cloud Run and caching strategies
• Comparison of Google CDN with other CDNs (CloudFlare, Fastly)
• Pricing models and the decision to charge per usage rather than feature-locked tiers
• Evolution of Citadel Cloud service over 7 months, including changes in pricing, deployment strategy, and API design.
• The importance of providing a seamless experience and the effort required to maintain it
• Free hosted offerings vs running own infrastructure and maintenance responsibilities
• Citadel's cloud service as a hands-off solution for customers with special requirements
• Security considerations and data residency restrictions
• Importance of starting with turnkey services, then gradually moving to more customized solutions
• Lessons learned from past experiences: assuming things, not validating features, and maintaining codebases
• Refactoring code in an open source repository and deploying new features to production for observability
• Extending authentication APIs for developers to create custom login experiences and register pages
• Changing the login system from Go to Next.js for a more SDK-like approach
• Expanding the actions concept to allow more flexibility in customized JavaScript codes
• Reducing threat surface by limiting foreign code execution in Citadel
• Using machine learning and event sourcing concepts for data-driven security features
• Considering opening additional regions and expanding cloud footprint
• Developing an event API for change tracking and backpressure processing
• Experimenting with CPU profiles to reduce latency in cloud service
• Reviewing and potentially revising pricing, including offering free domains
• Authentication and authorization are complex topics that require thorough thinking and planning.
• Using a turnkey solution or framework can be safer than building one's own system from scratch.
• Password hashing algorithms should not return results quickly, indicating potential security issues.
• The OAuth threat framework is a complex resource (60 pages) for considering authentication threats.
• Building secure authentication systems requires ongoing maintenance, testing, and evaluation.