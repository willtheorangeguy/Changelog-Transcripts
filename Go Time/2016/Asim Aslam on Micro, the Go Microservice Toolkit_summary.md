• Introduction to Asim Aslam and his background
• Overview of the Micro framework and its design decisions
• Financial sustainability plan for the project and Asim's full-time work on it
• Adoption and usage of Micro by companies (numbers and scale)
• Philosophical discussion on the delineation point between a microservice and something larger
• Designing and building microservices platforms
• Microservices size and complexity: 1,000-2,000 lines of code
• Measuring complexity based on mental model creation time
• Comparing modular vs. monolithic architectures in microservices
• Collaborative development of microservices in an open-source setting
• Scaling and distributing microservices to achieve shared goals
• Automation, self-healing, and fault-tolerance in distributed systems
• Designing a framework for interacting with microservices through multiple interfaces (CLI, API, bot)
• Micro is a toolkit for building managed microservices with Go
• It uses the Go Micro library as its core, which provides fundamentals for communication, message passing, and request serving
• The toolkit has an outer layer that includes a CLI, API, web UI, and sidecar for interacting with the HTTP interface
• Asim Aslam built Micro to address the lack of tools for writing microservices in Go
• Micro aims to simplify the process of building microservices by handling lower-level details
• Go kit is another library for building distributed systems, which offers a standard library approach
• The two libraries have different design goals and philosophies: Micro focuses on simplicity and ease of use, while Go kit provides more comprehensive abstractions
• Micro's pluggable architecture allows users to easily swap out components such as messaging brokers or service discovery mechanisms
• Importance of supporting different tools while maintaining a unified way of building software
• Microservices architecture with interchangeable plugins for flexibility
• Reusability of individual packages in unrelated projects
• Getting started with Go Micro, including resources and tutorials
• Serverless computing concept and its benefits
• Challenges and limitations of serverless approach at scale
• Event-driven programming and serverless architecture
• Shift in thinking for building systems from traditional synchronous models
• Serverless frameworks such as AWS Lambda, Google Functions, IBM OpenWhisk, and serverless.com
• Use cases for serverless applications: rapid prototyping, frontend and API development, data analytics
• Available products for driving serverless application development: serverless.com, Apex, OpenWhisk
• Go 1.7 Beta release features, including SSA compiler, subtests, and performance improvements
• CoreOS and Torus
• Distributed storage system for containers
• Hacker News comments on CoreOS' new project
• [Discfg] - a distributed serverless configuration tool
• Asim's Micro project and its potential
• Open source projects that the panel is thankful for:
  • CoreOS (Brian)
  • State Management for Go (Carlisia)
  • Postfix (Asim)
  • VLC (Erik)