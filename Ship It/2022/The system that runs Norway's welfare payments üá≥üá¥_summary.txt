• NAIS.io is an application infrastructure service built on Kubernetes used by Norway's welfare payments system
• Audun Fauchald Strand and Truls Jørgensen are principal engineers behind the platform at NAV
• The platform has increased deployment frequency from a few times a week to hundreds per day
• NAV is transitioning from legacy systems to NAIS, but not doing "lift and shift" to cloud infrastructure
• The organization values modernization of applications over just moving to new infrastructure
• NAIS has enabled teams to handle deployments themselves without manual testing periods
• Deployment frequency is now 1,500 releases per week with an average of one deployment per application per week
• The platform's unified approach to development and architecture has driven consistency across the organization.
• The speaker mentions the platform's architecture is surprisingly unified and not as diverse as expected.
• Data from 2009 shows the number of deployments has changed over time.
• Kubernetes was chosen for its open-source nature and ease of use, making it easy to move applications between platforms.
• Alternatives to Kubernetes are limited and may require more cloud dependence.
• The NAIS platform includes components such as Grafana, InfluxDB, Linkerd, Unleash, Kollide, and OSquery.
• Grafana is the speaker's favorite tool in the NAIS platform for real-time monitoring and troubleshooting.
• A separate data platform called Nada (NAV Data) was created to give teams ownership of their own data.
• Securing Kubernetes clusters is a top priority, with Kyverno being used as an example of a security solution.
• Security principles vs usability in development
• Zero trust architecture with service mesh
• Securing data at rest (e.g. PostgreSQL)
• eBPF-based solutions for security and visibility (e.g. Cilium)
• Migration from Istio to Linkerd and its challenges
• Benefits of using Kubernetes and its extensibility
• Kubernetes hosted services and automation
• Career history and experience in tech industry
• Discussion of programming languages and preferences (Java vs Kotlin)
• Impacts of COVID-19 on NAIS platform for welfare systems in Norway
• Challenges of transitioning to remote work during pandemic
• Developing a system to handle furloughed workers' benefits within a tight deadline
• Building the system using pair programming, user testing, and gradual rollout with Unleash
• Technical details of the system, including use of Kotlin, Postgres database, Kafka, and Bash scripts
• Implementing a payment system for Norway in one week
• Using a platform ( likely GCP) to deliver results quickly and securely
• Number of developers and teams involved (20 people, 10 developers, 100 teams)
• Scalability and resources used by the platform (50 nodes, 800 virtual CPUs, 1.6 terabytes of memory)
• Kubernetes cluster configuration and management
• Upgrades and maintenance of the cluster
• Comparison with on-premises setup and previous experiences with other cloud vendors
• Use of open source components and APIs in GCP
• Importance of using proven, stable, and open-source technologies for long-term stability and reliability
• Migration strategies for legacy systems, including rewriting code or translating COBOL to Java
• Challenges in finding people with expertise in old technologies like COBOL
• Comparing mainframe systems to modern cloud platforms like Kubernetes
• Importance of understanding the domain and having teams work on problems that can live as long as they need to be solved
• Working on a project to visualize application configuration in NAIS and improve supply chain security using SLSA model
• Exploring ways to make NAIS a platform for other organizations, not just NAV
• NAV's inspiration from gov.uk's open sourcing principles
• Adoption of open source code at NAV, except for certain sensitive areas
• Limited public interaction with NAV's open source code, mostly due to its niche application
• Attracting developers who value openness in software development
• Importance of treating internal developers as users when creating an application platform
• Value of writing good documentation and making it publicly available