• Origin of the name "Jeefy"
• Jeffrey Sica's role at the CNCF (Head of Projects)
• Project adoption process at the CNCF (sandbox, incubation, graduated)
• Efforts to automate project access to cloud resources
• Long-term goals and services provided by the CNCF
• Definition of cloud-native is evolving and includes distributed computing in a repeatable way
• CNCF accepting additional projects to flesh out the definition of cloud-native
• Kubernetes is a popular project, but its dominance doesn't mean it's the only answer
• CNCF's mission is to enable open-source projects, not to dictate which projects are used
• CNCF wants to support multiple projects, not just those within the organization
• Having all projects in one foundation might not be healthy for the ecosystem
• Being part of the CNCF can give a project "weight" and clout
• The CNCF's Technical Oversight Committee (TOC) decides which projects are "cloud-native" and worthy of the CNCF's brand equity
• The TOC filters out non-cloud-native projects, acting as a gatekeeper for the CNCF ecosystem
• Jeffrey Sica expresses concern that this creates an unhealthy ecosystem where projects that don't fit the CNCF mold are discouraged from participating
• Sica shares his personal experience contributing to Kubernetes and becoming a Sig UI Chair, and how he enjoys his role at the Linux Foundation CNCF
• Sica explains that he likes his job because it has a real impact on people's lives and allows him to make the world a better place
• The conversation also touches on the concept of the "endowment effect" and a social experiment involving shopping carts in a grocery store parking lot
• Comparison of bagging groceries to the role of the CNCF in open source
• Discussion of the benefits of the CNCF in facilitating collaboration and standardization among vendors
• Hypothetical scenario of a world without the CNCF and the potential for proprietary, vendor-locked solutions
• Story of Jeffrey Sica's experience working at Heroku and the early days of cloud hosting
• Discussion of the Kubernetes API and CLI, including the role of SIGs (Special Interest Groups)
• Humorous discussion of the various pronunciations of "Kubernetes"
• Kubernetes complexity and the tendency to "bike-shed" the kubectl tool
• Pronunciation and history of the kubectl tool
• Importance of the kubectl CLI and its development team, SIG
• Challenges of maintaining a high-demand project like kubectl, including saying no to feature requests
• Number of flags in kubectl (estimated to be in the hundreds)
• Use of Go as the language for the kubectl CLI
• Comparison of Bash and Go for scripting
• Contribution to the kubectl project, including the role of the SIG team and outside contributors
• Challenges of maintaining a large and complex codebase like kubectl
• Importance of reviewer contributions and code reviews for the project's success
• Kubernetes uses JSON internally, not YAML
• Maintaining marshaling between JSON, YAML, and Go structs is a significant challenge
• The project has a forked version of the Go YAML project and struggles with managing multiple versions
• The team has difficulty with mentorship, onboarding, and maintaining a steady stream of contributors
• Maintainer burnout is a significant issue, with the team feeling "crispy" from repeat mentoring
• The project has extensive documentation, but it's often overwhelming for new contributors
• Long-term contributor planning is a challenge, with no clear term of service or process for planning succession
• Growing contributors into maintainers through a process of involvement and contribution
• Factors that bring users back to the Kubernetes CLI multiple times, such as vested interest, curiosity, or employer requirements
• The challenge of filtering and allocating time to contributors with different goals and motivations
• Considering a parallel rewrite of the CLI alongside the existing version, rather than a complete overhaul
• The difficulty of introducing major changes to the project, such as versioning and LTS, due to compatibility and skew matrix concerns
• The possibility of releasing parallel versions of the CLI, allowing for easier development, contribution, and documentation
• The challenges of the KEP process and the difficulty of getting significant changes, such as a complete rewrite, approved
• Limiting developer access to production servers
• Using GitOps tooling to automate changes and reduce manual effort
• Cost and management of large-scale open-source projects
• Maintainer hacks and strategies for efficient issue triage
• Importance of knowledge transfer and community involvement in open-source projects
• Dapr's evolution from twice a week to once a month meetings
• Kubernetes meetings and SIG CLI folder
• Yaron Schneider's introduction of Dapr, an open source project incubating at CNCF
• Dapr's purpose: to simplify distributed systems challenges for developers
• Dapr's features: security, reliability, state management, Pub/Sub, and config management
• Dapr's architecture: sidecar architecture, APIs, and client libraries for various languages
• Dapr's component model: plugging in components for state stores, Pub/Sub, and secret stores
• Dapr's pluggable components and maturity levels: alpha, beta, and stable components
• Dapr was open sourced in October 2019 and has since gained significant traction with major companies adopting it
• Yaron Schneider and his co-founder left Microsoft in January 2020 to start Diagrid, a company that builds on Dapr
• Dapr was donated to the CNCF and has a steering committee with members from Microsoft, Alibaba, Intel, and Diagrid
• Diagrid offers a managed version of Dapr, which solves the operational complexity of running Dapr on Kubernetes
• The company's vision is to create a distributed systems API platform that can be used across various compute platforms, including serverless and edge computing
• Managing Dapr in a small Kubernetes cluster is manageable, but becomes more complex as the cluster size increases
• The CNCF (Cloud Native Computing Foundation) provides vendor neutrality and attracts new contributors to open source projects
• Donating Dapr to the CNCF allowed it to gain new contributors and users, and has benefited Diagrid's commercialization efforts
• The Apache 2 license allows for commercialization and enables others to create competing managed services
• Dapr is a polyglot framework with equivalents in individual programming languages, such as Spring for Java and Micro for Go
• The polyglot style of Dapr may have drawbacks, such as increased complexity, but is beneficial for most use cases
• Dapr may not be suitable for applications requiring microseconds of latency due to its abstraction layer and potential performance impact.
• Dapr may not be the best fit for applications with specific feature requirements from cloud services like Kafka, AWS, or DynamoDB.
• Dapr is an abstraction layer that adds features not found on top of cloud services in many cases.
• The project has huge plans for future development, including adding new APIs such as:
  • Workflows (as code programming model)
  • Cryptography APIs
  • Blob streaming APIs
  • Document store APIs
  • SQL APIs
• The project aims to expand its API offerings from 8 to 12 in the next year.