• Linkerd details from KubeCon North America 2021
• PARCA: a new continuous system profiling tool using eBPF
• TalosOS and KubeSpan perspective with Andrew Reinhardt
• New beginnings with RawCode (David Flanagan) after a busy two months
• Partners mentioned: Fastly, LaunchDarkly, Linode, Fly
• Linkerd 2.11 release and new features, including policy control for microsegmentation
• Introduction of two new CRDs in Linkerd 2.11
• Expressing policy using annotations and CRDs for traffic control
• Flexibility in cluster configuration from open to locked-down settings
• Limited customization via UI, focusing on read-only functionality
• Security concerns driving development of policy features and microsegmentation
• Securing traffic within a Kubernetes cluster as a major theme in Linkerd's evolution
• Development of a new theme in Linkerd
• Importance of user value and adoption
• Challenges in tackling complex problems
• MTLS and Kubernetes blog post by the speaker
• Linkerd 2.11 installation methods
• Maintaining legacy installation methods for simplicity
• Importance of repeatable deployments in production environments
• Recommended practices for installing Linkerd in production
• Operator concept for automating installations and upgrades
• Upgrade process from Linkerd version 2.10 to 2.11
• Breaking changes in multi-cluster mechanics
• Additive features in Linkerd 2.11
• Policy and MTLS implementation
• Certificate rotation for cluster-level issuer certificate
• Dependencies on Kubernetes versions and cert manager
• Production runbook for Linkerd available on buoyant.io
• TLS certificates and clock skew issues
• Importance of human interaction in open-source communities
• Linkerd project and its impact on users
• Benefits of sharing experiences and use cases with the community
• Advice for virtual conference attendees to make the most out of it
• The contrast between in-person and virtual conference experiences
• The speaker's virtual booth at KubeCon is set up with fun and interesting content, including a run book and other Linkerd-related materials.
• There will be a raffle for Linkerd swag, including hats and shirts.
• The speaker is excited about two talks: one from Elkjof, the largest retailer in the Nordics, on how they use Linkerd and Kubernetes to replatform their company, and another from Intain Australia on how they 10x'd their throughput using Linkerd.
• The speaker will be meeting with people who have worked on Linkerd for a long time but has never met in person before.
• There are no specific plans or announcements mentioned for the next six months.
• Planning for releases 2.12 and 2.13
• Boynt Cloud: a SaaS complement to Linkerd with free tier and features like metrics hosting, topology maps, and traffic breakdowns
• Linkerd future plans: policy focus and mesh expansion to run proxies outside of Kubernetes
• Polar Signals: founded by the speaker after leaving CoreOS/Red Hat, focusing on continuous profiling in observability
• The speaker wants to explore the concept of continuous profiling before discussing it with others.
• Continuous profiling has been around since the 1960s and was initially expensive and hard to do in production.
• Sampling profiling allows for continuous monitoring without high overhead, making it accessible to hyperscalers.
• eBPF (extended Berkeley Packet Filter) technology enables low-overhead data capture and exportation to user space.
• Kubernetes has unified the observability space by standardizing terms like "pod" and "container".
• The combination of eBPF with Kubernetes allows for automatic discovery and analysis of CPU time consumption across containers and infrastructure.
• eBPF and its role in presenting system information
• Continuous profiling and the need for education in this space
• Parka's open-source goals, including democratizing continuous profiling and reducing infrastructure costs
• The backstory behind Parka's development, including a proof of concept with Conprof and Google's paper on cost optimization
• The ease of use and UI improvements in Parka
• Dogfooding as a key factor in the development and improvement of Parka
• Parka is performance-sensitive software with a specifically designed storage and query engine for continuous profiling.
• The team uses Parka to optimize itself, creating a vicious cycle of improvement.
• eBPF (Extended BPF) is evolving into a production-ready state, with many people exploring its applications.
• The speaker is excited about the potential of eBPF and mentions specific talks at KubeCon related to it.
• Travel restrictions prevent some attendees from attending in person, but they can still participate virtually or catch up on recordings later.
• Advice for those who couldn't attend includes finding local virtual meetups, watching recordings, and trying to be part of the community as much as possible.
• The next KubeCon EU is expected to have improved circumstances for attendance due to COVID cases decreasing.
• In the next six months, Parka will likely release more features based on community feedback, rather than a set plan.
• Discussion of the benefits of community involvement in open source projects
• The role of the CNCF and its successful approach due to community thinking
• Congratulations on a well-designed hiring page that serves as an example for others
• Update on Cozy, including rewriting the networking stack of Talos using Cozy concepts
• Launch of Koops Band, an automated wire guard product
• Options for running Talos: laptop, bare metal, cloud
• Easy way to start with Talos is to spin up a Kubernetes cluster on your laptop using the CLI command "Talos CTL cluster create"
• Bare metal setup can be done by using an ISO or Cozy, but requires networking configuration
• Pixie booting and Sedaro product can streamline the process, but may not be necessary for beginners
• Cloud setup involves uploading an image and turning it on with correct user data
• Talos aims to provide a consistent experience across different environments, allowing users to describe their application and how it should run using declarative YAML.
• Discussion of Talos and its benefits
• Comparison to Debian and Ubuntu
• Minimalism of Talos (50 megabytes, no package manager)
• Removal of unnecessary features (SSH, Bash) for Kubernetes focus
• Security emphasis in Talos (reproducible supply chain, read-only file system)
• Ephemeral nature of Talos
• Importance of hardening the experience and eliminating node-level management
• The speaker discusses Talos's use of Musil instead of GLibC for C libraries
• Performance issues are reported when running Musil outside of GLibC
• The speaker attributes this to the limited scope of Musil in their environment
• They mention using Go and a new init system, contributing to Musil's performance
• Kubernetes containers use GLibC, reducing the role of Musil in the ecosystem
• The speaker recalls issues with Alpine-based container images and Ubuntu ones
• They discuss running the latest LTS kernel version (5.10.62)
• The team considers releasing LTS-style versions of Talos with pinned Linux kernel versions
• A new product called KubeSpan is announced, which bridges bare metal clusters with cloud instances using Talos's API-driven stack
• The discussion centers around KubeSpan, a technology that allows users to securely scale Kubernetes clusters across different networks and locations.
• WireGuard is used as the underlying networking protocol to establish secure connections between nodes.
• The technology enables users to maintain a consistent network experience regardless of location, including remote or edge computing scenarios.
• KubeSpan makes it seamless to expand or contract clusters as needed, without disrupting the cluster's operation.
• There are some limitations and considerations to be aware of, such as needing at least one direction of communication between nodes.
• The technology has potential applications in various use cases, including on-premises data centers, cloud environments, and edge computing scenarios.
• Meeting in person at KubeCon
• Virtual attendance options (booths, Slack, catch-up videos)
• Prioritizing sessions and topics of interest
• Balancing technical and management roles
• Exploring new technologies and tools (Talos OS, Sdero, Cubespan)
• Raygun will provide daily performance summaries for websites
• KubeCon is being discussed, specifically the speaker's experience attending remotely due to travel ban
• The speaker has had a significant change in personal life, having a new baby and changing jobs from Equinix Metal to Pulumi
• Remote participation methods are being discussed, including joining sessions on Slack, Discord, Twitter, and watching recorded talks later
• Discussing a KubeCon experience with multiple sessions running at the same time
• Comparing in-person vs virtual attendance and consumption of talks
• Mentioning community member Noel Georgie's ability to watch four or five talks simultaneously
• Sharing personal preference for single-tasking during events
• Revealing involvement as chair of the operations track and selecting talks for KubeCon
• Discussing popular sessions on GitOps, infrastructure as code, and specific tools like Argo, Terraform, Crossplane, and Pulumi
• GitOps tools comparison: Flux vs Argo
• GitOps tool consolidation attempt by original creators of Argo and Flux
• Challenges with custom resources in Argo
• Ease of use and simplicity of Flux
• Benefits of using Flux for agnostic YAML generation
• Announced GitHub Summit and KubeCon events
• Continuous integration and delivery
• Infrastructure as code
• Pulumi's platform for deploying applications
• Comparison between Terraform, HCL, and Pulumi
• Dagger and its use of Q language
• Programming languages for defining resource graphs (Go, TypeScript, etc.)
• Encapsulation of knowledge through programming languages
• Pulumi vs Crossplane: comparison of their approaches
• XRDs (compositions) in Crossplane for combining resources
• Providers in Crossplane interacting with IASs
• Dagger and Q: data language, block-based, and query APIs
• Dagger's ability to move beyond infrastructure provisioning
• Boundary as a continuous delivery component for applications
• Constraints of Crossplane still being defined by YAML
• Continuous reconciliation in Crossplane vs Pulumi
• Control over actual reconciliation in Crossplane vs client-side in Pulumi
• Dagger making infrastructure provisioning easy with minimal boilerplate
• Comparison to Pulumi and CDK from Amazon for similar approaches
• CDK having advantages over YAML alternatives
• Similarities between Pulumi and CDK for TypeScript support
• Benefits of using TypeScript for infrastructure as code due to its strict typing and ecosystem
• Differences in experience between using Go versus TypeScript with Pulumi
• Convenience factors of the TypeScript ecosystem compared to Go
• Inventing tools that were half-working and often caused more pain than they solved
• Switching from vendor-managed repositories to GoMod
• Difficulty in choosing between multiple GitOps tools and CNI options
• Raw Code Live's transition to use-case specific content instead of just introductory material
• Importance of having breadth of knowledge about available tools, but also needing to apply them in real-world scenarios
• Onboarding process and its importance for a smooth job transition
• Acceleration and lack of time to appreciate the present
• Future plans for Clustered, Raw Code Live, and Pulumi
• Alignment of personal interests with new role at Pulumi
• Wrap-up and thank yous from host and guests
• Promotion of changelog.com podcasts and community