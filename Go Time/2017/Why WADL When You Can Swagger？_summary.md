• Ivan Portacarero introduces himself and his background in software engineering
• He discusses his experience working with various languages including C#, Ruby, Scala, and Go
• He shares his work on IronRuby and how it led to him contributing to the Scala web framework
• He explains why he switched from Scala to Go due to issues with the language and community
• He expresses his positive experience with Go and its ability to support team development
• The origin of Swagger (now OpenAPI) and its name
• Common problems with APIs, including documenting inputs/outputs and evolving over time
• Solution: creating a machine-readable API specification to formalize expectations and facilitate client generation
• Features of Swagger, including:
  • Generating clients for APIs
  • Creating UI documentation that lives with code
  • Allowing for contract-first development and server generation
  • Marketplaces for accessing other companies' exposed APIs
• Benefits of using Swagger, including:
  • No longer needing to download client SDKs
  • Ability to quickly test and play with API requests through the Swagger UI
• Documentation comments for API routes and models
• Using Swagger to generate JSON documentation files
• Serving the Swagger UI using the binary or a hosted URL
• Publishing the Swagger JSON file on GitHub or other platforms
• Leveraging online tools, such as petstore.swagger.io, to view the UI
• Integration of Swagger with APIs and hosting requirements
• Kubernetes benefits for developers and infrastructure experts
• Challenges of scaling with Kubernetes in smaller businesses
• Importance of expertise in Linux and kernel facilities for effective use of Kubernetes
• Concerns about latency and performance in distributed systems, particularly with Istio
• Emergence of new projects like Istio, Envoy, and service meshes to solve distributed system problems
• Unsolved problems in distributed systems and service meshes
• Latency, points of failure, and debugging issues with version two and three implementations
• Difficulty in choosing between different solutions (e.g., Istio, Envoy) due to rapid innovation and potential for future replacement
• Need to balance adoption of new technologies with existing infrastructure and libraries (e.g., GoKit)
• Potential difficulties in maintaining and updating distributed systems
• Author's personal interests in decentralized databases and other unsolved problems
• Improving gossip algorithms in distributed systems
• Study of failure behavior in gossip-based membership systems (e.g. Cassandra, ACA)
• Research on improving the stability and performance of these systems under various conditions
• Development of a decentralized computing system using GoRapid
• Submission of a paper to ACM SIGCOM on decentralized computing
• Zookeeper usage: who uses it, Cassandra doesn't require it, Kafka does
• Operational cost and overhead of Zookeeper
• PKS (Pivotal Container Service) explained: implementation of Kubernetes for distribution on VMware
• PKS joint effort between Pivotal and VMware, with some involvement from Google
• PKS does not require Cloud Foundry, can be used next to it or standalone
• Separation between hardware and workloads
• Use of Bosch lifecycle manager for applications and infrastructure monitoring
• Automated restarting of processes and recreation of VMs in case of failure
• Management of unattended version of Kubernetes
• Integration with VMware's existing tools, including NSX-T overlay network
• Comparison to other solutions such as Flannel and Calico
• NSX-T management plane translates policies into rules for Kubernetes
• NSX-T has a centralized management plane for container interfaces, which Kubernetes takes advantage of
• Integration between NSX-T and Kubernetes allows for security features to be applied at the network level
• Kubo is an open-source tool that encapsulates source code, metadata, and monitoring information in a single package
• Releases is a system that stores source code, metadata, and monitoring information for rebuilding releases from scratch
• PKS (formerly Pivotal Container Service) makes it easy to set up Kubo in an environment with a UI and management tools.
• Implementing Active Directory and RBAC in a project called PKS
• PKS is a closed-source application
• The team hopes to release the project by December
• There's an exciting new project called Factory, which seems like a Sidekick successor but written in Go and supporting both Go and Ruby natively
• The speaker is excited about playing with Factory and its potential for open source companies
• Sidekick Pro model mentioned as a slick service
• Transition from Ruby to Go
• Updates on minor patch releases for Go (192 and 185)
• Bug fixes for issues with Go Get on non-Git repositories
• Release of Go Bot version 1.7.0 with OpenCV3 support
• Additional drone and robot implementations using Go
• Discussion of a project called Authouse, which is an open-source user authentication system for Go
• Comparison to existing authentication solutions such as Authboss and Ruby's device and other libraries
• Interest in exploring Authouse further due to its potential to simplify authentication in Go apps
• Reflection on the growth and maturation of the Go language and ecosystem
• Discussion about Authboss, a project that wasn't production-ready and had many broken things
• Comparison of Authboss's 1.0 version to the speaker's expectations
• Common issue in open source projects: vision vs reality
• Excitement for GRV, with some participants having already tried it
• Discussion of TIG, a CLI Git client
• Description of grv as a command line UI for Git
• Features of grv, including visual display of remote branches, commits, and tags
• Installation process and requirements (CMake, libgit2)
• Enthusiasm for using grv to manage Git repositories from the terminal
• Discussion about using Linux and its GUI tools
• Comparison of GRV with other tools (e.g., git-dash)
• Review of DEP 0.3.2 release and its features (import support for GPT and GB, bug fixes)
• Suggestion to play with DEP 0.3.2 for auto-import functionality from GVT or GB
• Recommendation of a blog post about version management by Shane/Sam Boyer
• Blog post name discussion
• Dependency management problems and appreciation for those who solve them
• Go Tracer tool introduction and its purpose
• Go Tracer's lack of documentation and explanation
• Go Tracer's features, including instrumentation and performance metrics capture
• Discussion on better tools being visual and interactive
• Performance issues with CPU time being taken up by one function
• Mention of a video to watch for performance optimization
• Bill Kennedy's blog post explaining channels and their usage in software development
• Discussion of understanding channels and how they work
• Free Software Friday segment is about to start
• Explanation of the OSS maintainer segment on the show
• Shoutouts to Francesc Campoy for his work in the Go community
• Discussion of Francesc's podcast, blog posts, tooling, and documentation
• Praise for Francesc's effort and dedication to the Go community
• Mention of a specific repository for Go tools created by Francesc
• Shoutouts to Bill Kennedy for a blog post on channels in Go
• Discussion of Carlicia asking if anyone else wanted to be mentioned.
• The guest talks about another person's tweets and online activities
• They mention GoNum, a library for numerical computations in Go
• The guest is excited about the potential of Python with NumPy in scientific regions
• The growth of the Go programming language and its community is discussed
• Shoutouts are given to Ivan for being on the show and to listeners
• Mention of Twitter handle @gotimefm
• Call to action to submit issues or suggestions on GitHub
• End of episode and reminder to tune in live next Thursday
• Discussion of holiday season and suggestion to "steal their phone" as a gift idea
• Promotion of changelog.com/live for live show streaming and community engagement
• The Breakmaster Cylinder is mentioned
• It is described as mysterious
• Mention of a previous episode or show
• Closing remarks and thanks to listeners