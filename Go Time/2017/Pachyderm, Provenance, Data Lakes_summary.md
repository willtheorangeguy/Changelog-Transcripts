• Pachyderm: a modern data lake built on containers
• Version control for massive datasets
• Data provenance: tracking changes to data and analysis
• Applications in machine learning, particularly with EU's new regulations
• Customer use cases include General Fusion (fusion reactor) and financial institutions
• The system discussed is written entirely in Go and uses Docker containers.
• Pachyderm's architecture includes a daemon (Pachd) written in Go using gRPC, and a frontend command line interface tool (Pach Control).
• The motivation for choosing Go was due to the existing components being in Go and aligning with Google's internal use cases.
• Pachyderm handles data orchestration, while users handle data processing within containers.
• The system allows for complex pipelining of data sets and distribution across multiple containers.
• Discussion about potential episode where a guest is assigned a mission to try out the system and return to discuss their experience.
• Development of Pachyderm orchestration system in Go
• Benefits of using Go in Pachyderm, including batteries included standard libraries and goroutines for concurrency
• Scalability issues with large data sets (hundreds of gigabytes) and limitations of Docker containers
• Future plans to handle larger data sizes (multiple terabytes)
• Potential use cases for distributed file systems and discussion of existing projects like Minio and RADOS
• Collaboration between Pachyderm and other open source projects, including support from the Minio community
• Challenges of making money from open source software
• Importance of aligning incentives for developers
• Deploying open source products and navigating deployment costs
• Case study: Pachyderm's decision to deploy on Kubernetes
• Business models for open source projects (support contracts, hosted models)
• Communicating vision and attracting community engagement through charismatic leadership
• Role of project leaders in shaping the adoption curve
• Charismatic but controversial leaders and their impact on the open source community
• Discussion of Linus Torvalds and his role in creating a decentralized version control system (Git)
• Critique of GitHub for being closed-source, despite its contributions to the open source community
• Pros and cons of open source software, including the potential for centralization vs. decentralization
• Gitea and Pachyderm as examples of open source projects challenging the status quo on GitHub
• Vision for a decentralized data processing platform (Pachyderm) similar to GitHub's role in version control
• Wuzz: a terminal-based HTTP request tool
• Ozzo Validation: a Go validation package with separate rules and nested validation
• Melissa Data: a data cleansing and validation service criticized for being outdated and using C
• Dep: a dependency management tool in development to solve the Go dependency problem, with an article explaining its use and upcoming episode featuring Sam Boyer
• Discussion about the math behind dependency chain and graphs in a tool called GPS (packaging solver)
• Dependency management as a major problem in software development, with Go being no exception
• Comparison of different programming languages' approaches to dependency management, including Rust's Cargo and Java's IDEs
• Mention of the Gogland IDE from JetBrains as a high-quality, commercially-supported tool for Go developers
• Discussion about the importance of good IDEs in increasing language adoption in the enterprise
• Brief overview of other news and projects in the Go community, including Vim-go Debug and Jodosha's Delve integration
• Francesc's video about Go 1.8
• #FreeSoftwareFriday segment where the hosts give shoutouts to open-source projects that make their lives easier
	+ NATS from APCERA and Derek Collison
	+ HashiCorp, specifically Vault
	+ gRPC from Google
• Discussion of Pachyderm and its use of gRPC
• Erik's hypothetical recommendation for password cracking with Hashcat
• Show sponsors: Toptal and Backtrace
• Reminder to subscribe to GoTime FM and follow on social media
• Warning about using Pachyderm: don't flood your house with data lake
• Episode release in a week and anticipated memes/gif responses
• Official goodbye from hosts and guest