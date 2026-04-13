• Discussion about upcoming podcast episode focusing on Git and Gitea
• Justin Garrison's personal anecdotes about drinking Dr Pepper and trying to lose weight
• Brief discussion about Rick Martin CDs with embedded rootkits in the early 2000s
• Topic shift to a white paper on record-breaking fasting by Angus, who fasted for 382 days without eating but with medical supervision
• Discussion of potential health risks associated with long-term fasting
• Discussion of Justin Garrison's fasting and Autumn Nash's taco cleanse diet
• Mention of a book on taco diets by Autumn Nash
• Comparison of the healthiness of tacos vs gluten-free diets
• Introduction of Matti Ranta as a guest on the show, discussing Gitea
• Explanation of Gitea as an open-source developer platform similar to GitHub
• Discussion of the scalability and infrastructure of hosting Gitea at scale
• Complexity and operational challenges with Kubernetes and Ceph
• Switching to single-server setup for simplicity and reduced complexity
• Importance of failover process and ensuring site availability
• Planning for scale and future needs, including using cloud-native technologies like EKS or GKE
• Infrastructure planning and scalability issues related to global latency
• Storage requirements for Git repositories, including the need for on-disk storage due to performance concerns
• Roadmap plans for improving repository storage and scaling
• Gitea is an open-source alternative to GitHub, with similar functionality
• Gitea prioritizes self-hosting and data sovereignty over users' code
• The project has received support from a corporate entity, which also provides bounties for maintainers
• Gitea's business model differs from GitHub's, as it encourages self-hosting rather than relying on the hosted version
• The conversation highlights the differences between Gitea and other popular Git platforms like GitHub and GitLab
• A key goal of Gitea is to give users control over their own infrastructure and data
• Git LFS limitations and differences with GitHub and GitLab
• Benefits and drawbacks of using Git LFS for storing large binary files
• Soft versus hard limits on repository sizes and storage
• Abuse of compute power, storage, and file hosting by some users
• Anti-abuse measures implemented in Gitea, including web hooks and automation
• Challenges of scaling a platform with 70,000 accounts compared to private instances
• LFS support was implemented to address ballooning repository sizes
• S3 was used to offload large files from disk
• Packages were added with support for various formats (e.g. Docker, Maven, npm)
• CI/CD system was implemented and leveraged experience from other projects
• Equinix Metal sponsored servers for testing software on ARM
• Gitea maintainers contributed to other open source projects (e.g. drone.io, xgo)
• GitHub Actions were made compatible with Gitea by implementing a connection between the server and runner
• Kubernetes and Ceph as storage backend proved to be complex for managing a simple website
• Switched to a single node instance for simplicity, allowing for vertical scaling
• Added complexity with features like package management, LFS, and HA, but still encourage users to "run it themselves"
• Utilized Terraform and autoscaling groups in cloud environments for easier management and scalability
• Dogfooding own project by hosting most of Gitea's infrastructure on the flagship site
• Challenges include migrating metadata from older systems with different mindsets
• Importance of community feedback and advice in designing and maintaining infrastructure
• Discussion of outdated car features and the price of cars
• Comparison of software pricing models (e.g. Adobe Photoshop vs Gitea)
• Artists' financial struggles with subscription-based services
• Introduction to Git and Git Extras, a package for extending Git functionality
• Examples of useful Git commands in Git Extras (e.g. git pr, git standup, git undo)
• Git Extras provides a collection of scripts for automating Git tasks
• git setup command initializes, adds, and commits files in a repository
• Open source contributors can add new commands or features to Git Extras
• Delete merged branches is an example feature that simplifies cleanup of Git repositories
• Aliases and automation tools can be used with Git Extras commands