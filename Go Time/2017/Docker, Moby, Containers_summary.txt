• Introduction of guests and sponsor
• Solomon Hykes' background and history with Docker/DotCloud
• Explanation of DotCloud's technology and pivot to open sourcing Docker
• Discussion of containers vs VMs and the confusion around Docker's abstraction
• The diversity of opinions within the Docker community
• Challenges in getting different groups (developers, operators, beginners) to participate in the same community
• The transition from a platform-as-a-service to an open-source project (DotCloud to Docker)
• Market size and competition in the platform-as-a-service market
• Customer demand for customization and flexibility
• The "Lego set" approach of containers (vs. monolithic platforms) and the success of Docker as an open-source containerization platform
• Docker's creator Solomon Hykes discusses why they chose Go as the language for Docker
• The team initially used Python, but switched to Go due to its ease of adoption and ability to compile to a binary
• Soloman cites reasons such as optimizing for contributions, avoiding tribal divisions in devops tooling, and wanting a language that was familiar to many people
• He also mentions the early days of Docker, where it wasn't an obvious choice and they weren't seeing "hype" around Go at the time
• The team's decision to use Go was met with some resistance, but Solomon successfully sold the idea to the team by explaining its benefits and potential for growth
• The development of Docker came out of operational experience with Linux containers.
• Early adoption of Docker faced pushback from "cranky ops" who were skeptical of new technologies.
• Solomon Hykes, a C systems engineer, chose Go for Docker due to its combination of compiled language and high-level syntax.
• Docker's early use of Go was seen as validation of the language, but it is no longer a unique selling point.
• The lack of external libraries and standard library support for Go were initial stumbling blocks in its adoption.
• Docker and LXC comparison
• Standard library vs external libraries use in software development
• Moby brand name and its relation to Docker
• Docker community size, diversity, and reaction to the Moby change
• Goals and implications of the Moby project for open source contributors and users
• Docker rebranding to Moby
• Concerns over lack of explanation for changes
• Solomon Hykes admits making tactical mistakes during transition
• Focus on two main groups: maintainers and mainstream users
• Middle population (non-active contributors, non-developers) not prepared for change
• Criticism from open source contributor community over company-driven vs community-driven approach
• Reference to Docker 1.12 announcement as an example of discrepancy between project and product behavior
• The Docker project was moved to a new repository (moby/moby) without changing its codebase, causing confusion among users and developers.
• The name change caused a "backfire" effect, leading to a temporary disruption in Docker's production shipment and numerous broken dependencies for some users.
• Solomon Hykes explains that the intention behind the move was to be more open and transparent with the community, but it ultimately backfired due to confusion over the name change and its implications.
• Moby is being positioned as a separate entity from Docker, allowing for further componentization of the platform and breaking up Docker's monolithic codebase into independent projects.
• The goal of Moby is to create a modular, open-source container platform where various components can be combined in different ways, promoting collaboration and innovation among developers.
• Solomon Hykes acknowledges that Docker has learned from its experiences at large scale and has made changes to address issues raised by the community over the years.
• Challenges of managing a large user base and extracting actionable feedback
• Need for modular architecture and partnering with others to build missing pieces
• Plans to simplify development by making tools more accessible and easier to use
• Switch from REST API to gRPC as the underlying RPC layer for low-level interfaces
• Roadmap for Docker/Moby API, prioritizing not breaking existing users and adopting new technologies like gRPC
• Encouraging open source contributions to Moby and addressing concerns about joining a new community
• Discussing the difficulty of making first-time open source contributions and efforts to make it easier
• Explaining the name "Moby" and its connection to Docker's mascot
• Mentioning resources for contributing to Docker, including documentation and events