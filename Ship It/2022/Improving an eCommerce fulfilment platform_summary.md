• Alex Sims shares his experience with implementing Kaizen principles at James & James, a 4PL business.
• He discusses his initial challenges with legacy tech and adjusting to the company's development approach.
• The team was using a waterfall method for releasing software every two weeks, but this didn't scale well with the growth of the company and remote work during the pandemic.
• They hired an agile consultant and began shipping multiple changes daily or weekly, which increased their build confidence and reduced testing time.
• Alex talks about his experience with managing high traffic periods like Black Friday and implementing alert systems to handle queues.
• He highlights the transition from releasing every two weeks to more frequent releases and the challenges that came with it.
• Migrating from a single server to multiple servers
• Implementing Ansible for provisioning users on servers
• Dockerizing applications to allow developers to work locally
• Improving system stability during peak periods and the pandemic
• Rewriting critical business logic in PHP using Lumen, including implementing new algorithms and unit tests
• The team had a system that was not fully operational and tested a new API to improve performance
• A canary release was used to test the new API with a small portion of users before rolling it out to all users
• The new API improved performance by 10x, reducing bottlenecks in warehouses where operators could no longer capture due to mutual exclusivity
• As time passed, the team blurred the boundaries between services and started writing more code for the Lumen application, creating a new monolith
• This created technical debt and made it difficult to upgrade applications in the future
• The team introduced Kafka to improve data processing and allow multiple applications to consume and reason with movement data
• Automated testing was implemented using Robot to write automated test packs for legacy applications
• Confidence in changes is gained through continuous integration, unit tests, manual smoke testing, and monitoring tools such as Datadog
• The team tracks performance issues, deployment failures, and slow responses in production
• Importance of documentation in IT
• Automation vs. manual processes
• Choosing between different tools and frameworks (e.g. Kubernetes, Docker)
• Benefits and drawbacks of adopting new technologies
• Collaboration and communication among team members in decision-making
• Balancing short-term needs with long-term goals and vision
• Emphasizing enjoyment and well-being in work environment
• Concerns about adding extra complexity to the tech stack
• Importance of thorough documentation for maintaining system knowledge
• Caution against chasing popular technologies without justification
• Using the right tool for the job, even if it's not your primary language
• Considerations for moving from legacy systems to more sustainable ones
• Potential benefits and drawbacks of open-sourcing code
• Discussion of serverless architecture and its potential applications
• Resilient system design and fault tolerance
• Deploying security patches and handling potential data loss
• System downtime and preparedness for failure
• Deployment pipeline and continuous integration/continuous deployment (CI/CD)
• Use of Jenkins, GitHub, AWS Lambda, and other tools in the development process
• Migration from Rackspace to AWS
• Discussion of starting a blog and sharing content with the show
• Explanation of the process of merging into main in a legacy application
• Benefits of deploying small changes frequently to catch defects early
• Plans for future improvements, including using Docker in production
• Idea for a pipeline that automatically sets up a preview environment for each pull request
• Implementing a messaging layer in legacy database
• Achieving operational cost savings
• Using new functionality to build on existing data
• Importance of team support and buy-in
• Future plans and upcoming milestones