• Introduction and overview of the episode
• Project introduction: ML pipeline for image processing and automated comparisons in healthcare use cases
• Guests introduced: Samantha Coyle and Anita Elizabeth Simon from Intel
• Focus on weight strategy for ML pipeline healthcare solution microservices
• Improvements made to an open source Go package as part of the project
• Guests' backgrounds and experience relevant to the project
• Biopharma-based healthcare solution with reusable architecture for various industries
• Image processing at the edge with additional complexities and considerations
• Utilizing EdgeX Foundry community for IoT device development and Go Microservices
• Distributed microservices based containerized solution for image capturing, transferring, and processing
• Use of Go programming language due to its popularity in building distributed microservices solutions
• Advantages of using Go include speed, concurrency, and scalability
• Decision to use containerized and microservice infrastructure for lightweight and scalable architecture
• Benefits of microservices architecture include loose coupling and ease of service addition/removal
• Overview of a project that required coordination between microservices on Windows and Linux machines
• Discussion of weight strategy for service dependencies in Go implementation (Go Rebo)
• Comparison of Go Rebo to Vishnubob Bash script and other alternatives
• Considering the Docker layer vs. Go application code layer for implementing wait logic
• Overview of using Docker Compose with entry points and potential issues with overriding commands
• Discussion of Docker as a solution for homogenous deployment
• Evaluation of "wait-for-it" package, inspired by Vishnabha bash script, for waiting on dependent services
• Comparison with other packages (net wait go) that were considered but had issues with licensing and maintenance
• Decision to use "wait-for-it" package due to its license and activity level
• Discussion of implementing the "wait-for-it" package in a Go project, including copying code into the project and adding minor modifications for idiomatic consumption
• Implementing the wait package and its dependencies
• Adding retry logic for when services are not available
• Interaction with core authors/maintainers on GitHub
• Contributing to the repo and opening a pull request
• Lessons learned from implementing the specific use case, including:
  • Importance of communicating with maintainers
  • Need to balance package responsibilities vs. user needs
  • Finding a "happy path" for users with different requirements
• A previous project's package was used for a new project, but the original author stopped maintaining it
• The team had to copy and paste code to make it work in the new project, highlighting a challenge with using open-source packages
• The team discussed challenges they faced in their big project, including one where a dependency stopped being maintained
• They talked about the importance of monitoring dependencies and having a plan for replacements if they're no longer maintained
• It was noted that sometimes it's not possible to find suitable replacements, requiring significant work to build something from scratch
• Complex software development may be more feasible with existing expertise and resources.
• Customer requirements should guide the decision on whether to develop a feature in-house or use external tools.
• Team expertise plays a crucial role in determining the feasibility of developing complex software features.
• Learning curve for Golang was found to be moderate, with some overlap between programming languages.
• The advantages of Golang include its open-source community support and better documentation.
• Every language has its own strengths and weaknesses, and developers should choose the best tool for their use case.
• Go is a suitable choice for microservices development.
• Software engineering involves continuous iteration and new versions
• Intel's business model focuses on selling hardware and chips, not software
• The project aims to build open-source sample projects for partners and solution integrators
• Support for the project will depend on customer demand
• The timeline for releasing the project is end of quarter
• Open source has more depth than initially meets the eye
• Microservices-based, containerized solutions are becoming increasingly important in IoT development
• Go (Golang) is a recommended language for developing microservices
• Discussing Christmas spirit as a year-round mindset
• Characteristics of Christmas spirit: robust, cozy, and warm like Santa Claus vs. cheeky elf energy
• Sam (or Santa) committing to giving everyone a gift every day
• Discussion on testing vs. graceful failure in software development
• Unpopular opinion that focusing on testing corner cases can be counterproductive
• Game start announced.