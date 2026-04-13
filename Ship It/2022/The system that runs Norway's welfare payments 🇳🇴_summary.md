• nace.io: an application infrastructure service built on Kubernetes
• Application platform increases shipping rate from few times a week to hundreds of times per day
• Runs Norway's welfare payments, handling billions of dollars in transactions annually
• Code Insights: a feature that tracks versions of languages and packages
• Replaces manual tracking methods with single-line source graph search and templates
• The speaker works at NAV, a governmental agency in Norway, as a principal engineer.
• They mention their colleague Truls Jørgensen and describe themselves and him as "Waldorf and Stadler" from The Muppet Show, who constantly complain about everything.
• NAV has undergone significant changes in the past five years, including a shift from fully outsourced to insourced development and hiring own developers.
• The agency is currently using NICE, an open-source platform built in 2017, which serves as a branding exercise and technology platform to attract developers.
• NAV faces challenges with GDPR and balancing technologist and lawyer perspectives on using cloud technology while protecting user privacy.
• The speaker notes that running everything in-house is not an option and that modernizing applications is necessary for making better services.
• Deployments were previously done manually and at nighttime, with big releases coordinated every few months
• With NICE's help, teams could handle deployment processes independently without needing to coordinate with others
• Current deployments are 1,500 per week for 1,300-1,400 applications, with most employees working on a smaller subset of apps
• Microservices architecture leads to varying app activity levels and some apps change frequently while others rarely do
• The platform has tight entry conditions, requiring stateless Docker containers, log collection, metrics, and alerts
• The unified architecture has led to consistent development practices and limited external services available
• Data shows a significant increase in deployments over the years, with 13 years of data available for analysis
• Kubernetes was chosen due to its open-source nature, allowing for better distinction between applications and platforms
• Open source projects and Kubernetes adoption
• Comparison of Mesos universe and Kubernetes
• Cloud vendors offering Kubernetes as a service
• Alternatives to Kubernetes, including serverless architecture
• Nase.io components, such as Grafana, InfluxDB, Linkerd
• Unleash feature toggle system and its integration with NICE device
• Collide and OS Query tools for laptop management and connectivity
• Favorite tool: Grafana for monitoring and insight into production applications
• Discussing ownership of applications and data on a platform
• Introducing NavData (also known as Nada) as a platform where teams own their data
• Mention of Kaverno, a tool used for securing Kubernetes clusters
• Importance of usability in security features and avoiding impossible-to-adhere-to principles
• Explanation of service mesh and zero trust principles for application security
• Introduction to Raygun, a software performance monitoring tool
• Discussion on measuring progress towards goals in software development
• Data collection and outliers
• Securing stateful data persisted at rest (Postgres, flat files)
• Using managed GCP services for Postgres
• eBPF and service mesh (Cilium) for system call visibility and security
• Migration from Istio to Linkerd and the benefits of Kubernetes' extensible API
• Discussion on the ease of switching between different solutions due to open-source nature
• The platform is now available hosted and managed, reducing the need for manual updates and maintenance.
• Documentation and resources are available at docs.nace.io, including step-by-step guides, YAML examples, and best practices for Kubernetes.
• The speaker has been in tech for 20 years and has experience with Java, but currently prefers Kotlin for its fun and stability.
• They would choose a cloud vendor's abstractions over traditional serverless solutions to make it easier for small companies.
• COVID-19 presented challenges to the platform, including adapting to remote work and ensuring continuity of operations.
• The challenges of remote work and team communication during the pandemic
• Furloughed workers in Norway and the need to process large numbers of benefit applications quickly
• Developing an alternative system to handle furloughed worker benefits, including creating a law and implementing a new system
• Using PERF programming and other technologies to build the system in a short timeframe
• Implementing the system using Unleash for gradual rollout and testing
• The system's performance and payment of 1 billion Norwegian kroner within a week of going live
• Discussion about currency exchange rates in Norway
• Overview of a system built and deployed by the speaker's team in just one week
• Importance of security and using hardened components to avoid mistakes
• Project involved around 20 people, including developers and lawyers
• Current development team size and structure at NAV (around 700 product developers)
• Use of GitHub for collaboration (800 seats) and organization into teams and product areas
• Discussion of cluster configuration and separation
• Comparison of managing one large cluster versus multiple smaller ones
• Experience with Kubernetes upgrades and downtime mitigation
• Benefits of using a managed service (GCP) for application modernization and easier operations
• Considerations for choosing cloud vendors (AWS, Azure, GCP)
• Evaluation of GCP's hosted Kubernetes offering compared to other providers
• Desire for more open-source component options within GCP
• The importance of using proven and tested software in a stable environment
• The difficulty of finding personnel with COBOL expertise due to the age of many programmers
• The potential for learning COBOL to become lucrative as systems running on COBOL approach obsolescence
• The strategy of rewriting or migrating older services rather than simply upgrading infrastructure
• Using technology such as code translation and Kubernetes to modernize mainframe-based systems
• Developing an application configuration tool in YAML format to manage access and permissions
• Creating visualizations of application interactions
• Exploring the importance of addressing unrequested ideas that can become game changers
• Integrating security frameworks with modern software development practices
• Supply chain security, including the Salsa model and Log4Shell incident
• Developing a platform for other government agencies in Norway
• Inspiration from UK's AlphaGov and Go.uk platforms
• Open sourcing code, following principles inspired by Go.uk's open sourcing approach
• Open source unemployment benefit systems and their code being open to the public
• Attracting a certain type of developer through coding openly
• Application platforms being valuable in big organizations
• Treating internal developers as users and making an application platform like a product
• Importance of documentation, with NACE.io's docs being highlighted as excellent
• Connecting with like-minded developers via changelog.com/community
• Appreciation for Fastly's low-latency worldwide service
• Availability of blazing-fast MP3s for listeners
• Discussion of Firecracker VMs and WireGuard integration
• Upcoming topic: developer experience infrastructure with Kenneth Orchenberg