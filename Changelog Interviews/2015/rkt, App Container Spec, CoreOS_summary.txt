• Introduction to Alex Pulvey, CEO of Core OS, and the conversation about their company and products
• Discussion of Core OS and their open-source operating system
• Overview of Core OS' history, starting in 2013 with their first release
• Explanation of Core OS' mission and goals, including a focus on containers, distributed systems, and security
• Description of Core OS' business model, using open-source components and commercial products to drive sustainability
• Mention of Core OS' open-source projects on GitHub and their commitment to open-source development
• Introduction to Rocket, Core OS' new open-source product for containerization
• Discussion of Rocket as a competitor to Docker
• Types of software built by the company: open source components and commercial products
• Company's philosophy on containerization and creation of Rocket
• Background on Core West and why it was built as an alternative to Docker
• Core West's focus on security, specifically making updates easy to manage
• Concept of automatic server updates and its potential benefits (security, reliability, performance)
• Core OS is different from existing server OS due to its containerized approach
• Packaging and deploying applications is a key challenge in updating a server
• Core OS uses containers to manage dependencies and isolation between applications
• Docker was integrated into Core OS from its first release and has been a key component in enabling automatic updates
• The goal of Core OS is to manage the underlying infrastructure for users, freeing them from worrying about OS updates
• The platform provides a centralized patching and deployment system for users who opt into the service
• For users who do not use the commercial update service, Core OS provides a package manager (Docker) to manage updates
• Core OS has made its updates available for free as a community service, and commercial products are used to sustain the effort
• Docker was initially used as a package manager and was a key component in building the Core OS system
• The platform has also developed a tool called etcd, a distributed key-value store, to enable sharing of configuration across servers and to make it easier to build distributed platforms.
• etcd's GitHub page and its maturity as an open-source project
• Docker's evolution from a tool to a platform and its divergence from the original containerization philosophy
• The reasons behind the creation of Rocket, a new tool for containerization, and its specifications
• The announcement and reception of Rocket, including the subsequent press frenzy and controversy
• The team's internal reaction to the launch of Rocket and the handling of external pressure and criticism
• The lack of an open standard for containerization was a major issue
• CoreOS decided to build their own solution, Rocket, instead of contributing to Docker
• Rocket aims to provide a more secure, composable, and Unix-like containerization solution
• CoreOS has invested in Rocket and it's coming along nicely
• The goal is to create a shared standard for containerization between Rocket and Docker
• Containers will be more widely adopted when there's a clear, open standard in place
• Multiple implementations of a standard exist and it's beneficial for everyone
• CoreOS is guiding the direction of containerization, but also wants to create a better Docker
• The focus is on creating a better containerization solution, not just duplicating Docker
• Docker and Rocket are compared and contrasted
• The interviewee sees Rocket as a container runtime, like the original concept of Docker, while Docker is a more comprehensive platform
• The interviewee believes that Rocket and Docker serve different purposes and are not redundant efforts
• The interviewee discusses the benefits of competition in the marketplace, citing Firefox and Chrome as an example
• The interviewee highlights security concerns with Docker's architecture and the need to refactor it to separate individual applications
• The interviewee notes that rewriting Docker's architecture would be necessary to address these security concerns.
• Discussion of Docker's security issues and the decision to refactor it into individual components
• Comparison of Docker to Chrome and Firefox, and the idea of making it more composable and interoperable
• Rocket's creation from scratch instead of forking Docker, due to differences in architecture and goals
• Docker's change of business model from Docker Cloud to a new model, and its impact on the containerization ecosystem
• Core OS's business model and approach to monetization through free updates and community services
• App Container specification, a community-driven effort to standardize containerization
• Review of the App Container specification, its components, and ownership.
• Runtime environment consistency and portability
• Container state and arguments (environment variables, config drive, metadata service)
• Identity for containers (signed version of data posted to metadata service)
• Image format, runtime, and image discovery specification
• Docker's tightly integrated hub and image discovery/download process
• Open source and interoperability with Rocket and Go programming language
• App container specification progress and involvement opportunities
• Rocket and CoreOS product transition and support for Docker
• Motivation for Rocket and containers is to treat them like a package manager, with always-up-to-date packages
• Desire to deliver updates quickly to Docker platform users, not just package managers
• CoreOS can run anywhere, including Amazon, Digital Ocean, Google, and on-prem
• Root file system is bit-for-bit identical, ensuring security and portability
• Quay plays a role in the future of CoreOS and app container standards
• Enterprise-ready on-prem Docker registry is available from Docker
• Features of Quay will support app container and Docker standards
• CoreOS will power development and bug fixing across the spectrum
• Open source and core OS development
• Security and auto-updating of OS
• App container standard and interoperability
• Need for third-party implementations of app container spec
• Contribution opportunities for listeners, including system programming and distributed database work
• App container spec available on GitHub as appc
• Core OS CEO discusses what they would be doing if they weren't working at Core OS.
• Desire to work more directly on products and technology.
• Enjoyment of outdoor activities, such as windsurfing and white water rafting.
• Mention of inflatable kayaks for river crossings.
• Appreciation for being part of Core OS team and having control over projects.
• Acknowledgement of sponsors, including Rackspace and CodeShip.