• Tom Pansino and Gunnar Holwerda share real-world stories from OpenSesame's experience with tooling and organization.
• The company started with a single team but grew to 7 teams as it scaled, necessitating changes in governance and control.
• They implemented the "Bootstrap" project for lightweight governance and control of various system components.
• The primary driver for organizing themselves better was to increase efficiency, reduce duplicated effort, and make sense of complex systems.
• Splitting engineers into areas of competency was not the intention; rather, it was about reducing cognitive load and allowing teams to focus on their stream-aligned work.
• Four fundamental types of teams: platform team and value stream team
• Platform team: provides building blocks for other teams to work on top of, reduces cognitive load and access control complexity
• Value stream team: focuses on delivering specific business value or revenue stream
• Bounded contexts: reduce cognitive load by isolating complex systems and making them more manageable
• Domains: product domains owned and cared for by individual teams
• Team API: providing a simple interface to interact with complex systems, hiding underlying complexity
• Example of platform team in action: delivering pre-configured cloud resources (e.g. VPC, subnets) to reduce networking complexity
• Initial rollout issues with AWS infrastructure led to health checks being implemented
• Complexity of infrastructure management was addressed through Terraform configuration
• The process involves a repository, configuration file, and modules that provision resources such as Amazon accounts, New Relic, and API keys
• GitHub Actions run the Terraform apply to deliver the infrastructure
• Quality assurance is achieved through running a Terraform plan in the cloud, analyzing the output, and testing in a staging environment before deploying to production
• Chaos engineering as a method for exploring system failures
• Discussion of a specific incident where staging deploy passed but production failed due to a parity issue
• The importance of staging environments in ensuring scale testing and detecting potential issues before they reach production
• Terraform's benefits in automating infrastructure management and minimizing large cleanups
• Migration strategies for domains and resources from legacy systems to the new platform, including enabling work and office hours for internal customers
• The success of office hours in facilitating communication between teams and providing hands-on training and learning opportunities.
• Importance of communication in implementing new systems or changes
• Role of Office Hours in facilitating collaboration and knowledge sharing among teams
• Inverse Conway Manoeuvre: structuring teams to reflect desired system structure
• Siloing of knowledge within individual teams and the need for experts to provide guidance
• Relationship building between platform teams and other teams for effective collaboration
• Avoiding "architect" mindset in providing suggestions versus imposing solutions
• Managing imposter syndrome in team members who may feel uncertain about their approaches
• Capturing knowledge and communication in a written form (e.g. Confluence) to facilitate asynchronous learning and collaboration
• Micro retrospectives: short review sessions after conversations with customers or stakeholders to reflect on what went well and what didn't
• Improving customer communication: reducing unnecessary conversations and documentation by sending teams to work together on shared projects
• Value stream optimization: using data to inform decisions and reduce time-to-delivery for customers
• Developer experience: improving local development environments, creating reusable pipelines, and standardizing tooling to make it easier for developers to get code into production
• Production environment: not prescriptive, but rather providing recommendations and guidance to teams who know the domain best to design solutions that meet their needs
• Dev stage prod flow structure using AWS accounts
• GitHub Actions workflow for deployment and testing
• Legacy components requiring manual verification
• Benefits of reducing stages and checkpoints in CI/CD pipelines
• Importance of observability and pushing changes to production quickly
• Tradeoffs between speed and testing, and the need for a balance between them
• Using Terraform for infrastructure provisioning and management
• Importance of team buy-in and collaboration on pipeline design
• Importance of getting people comfortable with change
• Role of legacy systems in slowing down deployment workflows
• Need to build trust and confidence among teams for faster deployments
• Benefits of measuring progress and feedback loops
• Importance of questioning and challenging established processes
• The "gorilla story" analogy: how humans can create and perpetuate unnecessary complexities through learned behavior.
• Resistance to change due to institutional knowledge and fear of deviating from established processes
• Importance of understanding why certain practices are in place, rather than just following tradition
• The need for clear documentation and explanation of organizational policies and best practices
• Avoiding a "black-and-white" approach to process, and instead focusing on continuous improvement and learning from failures