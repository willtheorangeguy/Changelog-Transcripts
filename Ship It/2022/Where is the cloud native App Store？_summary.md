• Conversation with Alexis Richardson, co-founder and CEO of WeaveWorks
• Discussing going fully remote and what a great team looks like
• GitOps: continuous deployment for cloud-native applications
• The missing app store for cloud-native apps
• Registry fragmentation and lack of curation in OperatorHub and Helm registries
• MongoDB Atlas as a multi-cloud application data platform
• Changes at WeaveWorks, including going fully distributed and moving to Oxford
• Update on GitOps definition and adoption
• GitOps definition and evolution
• Comparison to other technologies (DevOps, infrastructure as code, CICD)
• Potential for GitOps to make operations accessible to developers
• App store for enterprise: concept and current state
• Examples of existing platforms and marketplaces (Helm chart repositories, Amazon marketplace, Red Hat operator hub)
• The speaker draws an analogy between the shift from traditional to cloud native technology and past technological shifts, such as the rise of the web and the iPhone.
• The speaker believes that cloud native has yet to achieve its "iPhone moment", where it becomes obvious how life was better with the new technology.
• The App Store is mentioned as a parallel to Helm, but the speaker argues that there's more to cloud native than just installing apps.
• Interactions between components, security, compliance, and observability are mentioned as key aspects of cloud native that are often overlooked.
• Kubernetes is discussed as a platform where users can create identical environments, but in reality, each environment may diverge due to differences in configuration or usage.
• Enterprise IT challenges and cruft accumulation
• Comparison of consumer vs. enterprise technology mindset
• Examples of outdated IT thinking, such as OpenStack POCs still running years later
• Benefits of thinking like a consumer with regards to Kubernetes fleets
• Challenges of upgrading large numbers of clusters and potential benefits of simply replacing them
• Critique of treating Kubernetes as a private cloud technology and concerns about multi-tenancy
• Signs of maturity in software development teams include thinking about disposable technology and focusing on small pieces of the problem.
• Current issue resolution tools, such as Raygun's alerting feature, help identify errors quickly but may not prevent problems from arising due to migration issues.
• GitOps can help with migrations by capturing the entire definition and starting from a baseline, but a good GitOps solution for data is still lacking.
• Data storage technologies like ZFS have potential for solving data history management, but it's not yet easy enough for widespread adoption.
• GitOps has improved tooling in recent years, but more work needs to be done to make it simple and user-friendly.
• Introduction to the GitOps CLI and its benefits
• Explanation of how GitOps automates deployment and management
• Discussion of the scalability and security features of pull-based mechanisms
• Use cases for edge computing and managing thousands of identical clusters
• Future potential for cloud-native apps with always-connected infrastructure
• Use of KeylessH instead of Flux or Argo for updating Kubernetes cluster
• Importance of not running latest in production and instead using a CI/CD system that doesn't have keys to production
• Benefits of pull-based deployments for multiple Kubernetes clusters
• Need for integrating policy and compliance into the GitOps model for trusted delivery and supply chain management
• How the GitOps model fits with the CI-CD pipeline, including immutability firewalls and DMZs
• Variations on the GitOps pattern, including push and pull approaches, and staging involved in deployment
• Difference between traditional CI/CD and GitOps
• How a CI pipeline interacts with a canary deployment using Flagger and Prometheus
• Write-back mechanism in GitOps tools for communication between the cluster and the CI/CD pipeline
• GitOps maturity model, including scaled GitOps, Enterprise GitOps, prerequisites, and core GitOps
• Continuous reconciliation based on a plan in a shared mutual store, version-controlled
• Comparison to Chef and Puppet methodology with improved ease of use and applicability up the stack
• GitOps maturity model discussed as a framework for implementing and scaling GitOps
• Enterprise app store concept mentioned as a desirable goal for managing complex enterprise applications
• GitOpsCon North America talk and GitOps Days 2021 conference discussed, highlighting real-world use cases and industry adoption
• Companies such as Amazon, Microsoft Azure, VMware, Red Hat, and Mesosphere (now D2IQ) using GitOps in production with Flux or Argo
• Next six months expected to bring growth of edge computing and increased adoption of GitOps for retail stores and other industries
• The US Air Force uses Kubernetes and Flux to manage containers in fighter jets.
• GitOps has been successfully implemented by the Air Force in their Platform 1 software platform for secure management of containers in real assets.
• Ricardo from CERN discussed how GitOps helped manage an extraordinarily large and heterogeneous infrastructure at GitOps Days.
• A customer rolled out 5G using GitOps and will have a press release next week about it.
• GitOps is being used in various big-scale projects, including the Air Force's use case, and is expected to be more widely adopted.
• The future of GitOps includes deployment pipelines, policy integration, and secure DevOps practices.
• The concept of "fleets and platforms" will become important for scaling in the future.
• Introductions to sponsors: Fastly, LaunchDarkly, Lenover
• Thanks to Breakmaster Cylinder for music
• Recap of current week's content
• Announcement of new team and role
• Reflection on resilient teams and importance of sharing knowledge and shipping quickly