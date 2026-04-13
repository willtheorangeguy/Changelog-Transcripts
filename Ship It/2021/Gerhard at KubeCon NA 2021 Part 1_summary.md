• Overview of Linkerd 2.10 and new features in 2.11
• Introduction of policy control in Linkerd 2.11 for micro-segmentation and security
• Declaration of policy through annotations or CRDs (Custom Resource Definitions)
• Read-only UI in Linkerd, focusing on understanding system state rather than configuration
• Security theme in Linkerd development, including encryption and regulatory compliance
• Future plans for securing traffic in Kubernetes clusters
• Linkerd's ease of use for beginners
• Recommended production deployment practices (Helm, Terraform, etc.)
• Potential operator for automated upgrades and installations
• Linkerd's upgrade process from 2.10 to 2.11
• Supported Kubernetes versions and dependencies (cert manager)
• Importance of certificate rotation and clock skew considerations in production environments
• Linkerd community's transactional relationship with users
• Benefits of in-person interaction vs virtual conferences
• Importance of user gratitude and sharing success stories
• KubeCon event and talks featuring Linkerd users' experiences
• William Morgan's personal preferences and interests at KubeCon
• Upcoming releases and events for the Linkerd project
• Linkerd and Buoyant Cloud discussed as complementary technologies
• Expansion of mesh capabilities to non-Kubernetes environments
• Focus on policy and data plane improvements in Linkerd
• Introduction of Polar Signals, a company offering continuous profiling solution
• Discussion of continuous profiling, its history, and how it can be done cost-effectively in production using eBPF and Kubernetes
• Parca (a continuous profiling tool) is being opened up to the world at KubeCon
• The goal of Parca is to provide a way for developers to optimize their systems and reduce costs by identifying performance bottlenecks
• Continuous profiling is still a relatively new concept, and Parca aims to democratize it and educate the community about its benefits
• The tool uses eBPF (extended Berkeley Packet Filter) to collect data on system performance metrics such as CPU, memory, disk operations, and network operations
• Parca's UI has undergone significant improvements over a short period of time due in part to extensive dogfooding (using the software internally)
• The developers use Parca themselves to optimize their own tool, creating a self-reinforcing cycle of performance improvement
• Plans to productionize eBPF-related projects
• Advice for those who couldn't attend KubeCon in person or virtually
• Updates on Parca's development process and community involvement
• COSI (Cozy Operating System Initiative) progress and implementation in Talos
• Discussion of the future of operating systems, specifically with regards to API-driven interfaces and reduced reliance on SSH
• Talos installation methods and ease of use
• Creating a Kubernetes cluster with minimal setup and networking complexity
• Using COSI or PXE booting for bare metal installation
• Cloud deployment options and image upload requirements
• Consistency across environments, including laptops, cloud, and bare metal
• Minimalism and lack of unnecessary packages in Talos compared to other operating systems
• Security features, such as reproducible supply chain, read-only file system, and ephemeral storage
• Signing and tracing code commits from development to deployment for security and audit purposes
• Concerns about minimalist systems and security
• Use of musl instead of glibc and its performance implications
• Talos' use of musl and Go programming language
• Kubernetes and containerization with glibc
• Host and container configuration for musl and glibc
• Linux kernel version and LTS strategy
• KubeSpan announcement and on-demand cluster scaling
• Discussion of Andrew Rynhard joining an AWS Graviton instance to his laptop
• Andrew Rynhard's excitement about attending KubeCon in person and meeting his company colleagues
• Advice from Andrew Rynhard on how people who can't attend KubeCon in person should participate, including joining the CNCF Slack and watching catch-up videos
• David Flanagan's personal updates, including the arrival of his new baby boy Caleb and his job change to be a developer advocate for Pulumi
• Remote participation in KubeCon and managing multiple sessions
• Comparison of David Flanagan's and Gerhard Lazu's methods for participating in remote KubeCons
• Interacting with other attendees during virtual events
• Chairing the operations track at KubeCon, selecting talks, and being familiar with upcoming sessions
• GitOps tools Argo and Flux, their use cases, and benefits
• The failed attempt to consolidate both tools into a single "GitOps Toolkit" in 2019
• Interest in understanding the strengths and weaknesses of each tool and attending an upcoming GitOps summit
• Comparison between Flux and Argo for GitOps
• David Flanagan's new role at Pulumi and his interest in infrastructure as code and continuous integration/delivery
• Benefits of using Pulumi over TerraForm and HCL, including support for high-level programming languages
• Comparison with other tools such as Dagger (using CUE), Crossplane, and CUE Blocks
• Discussion of CUE language and its use cases, particularly in comparison to HCL and Pulumi
• Discussion of limitations and constraints in infrastructure as code tools
• Comparison of Dagger and Boundary for providing a single interface to infrastructure management
• Advantages of Crossplane for continuous reconciliation and control over execution
• Similarities between Pulumi, CDK from Amazon, and other tools for infrastructure as code
• Preference for TypeScript as a language for infrastructure as code due to its strict typing and flexibility
• Comparison of Go and TypeScript for use with Pulumi
• Discussion of challenges in managing dependencies in Go
• Changing format of Rawkode Live from high-level introductions to use case-specific content
• Focusing on real-world applications and solutions with specific tools
• Reducing decision fatigue by providing more practical examples and inspiration
• Exploring the cloud-native ecosystem and its many projects
• Importance of balance between breadth of knowledge and in-depth expertise