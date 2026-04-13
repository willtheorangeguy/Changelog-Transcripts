• Century's goals for full application health through error monitoring and tracing
• Importance of logically tying together various sources of telemetry data
• Use of a "trace ID" to connect disparate data points related to user actions
• Advantages of having a rich, structured data model with interconnected spans and logs
• Potential impact on system design and team dynamics
• Justin and Autumn discuss their new job announcements
• Autumn starts as product manager for Azure Linux at Microsoft
• Gerhard returns to the show, discussing his previous work with Changelog and starting Ship It podcast
• Reasons behind starting Ship It podcast include experience with infrastructure work and creating a community around it
• The podcast ShipIt is being discontinued by the Changelog network at the end of December 2024
• The decision to stop the podcast was made due to the Changelog network's desire to focus on their main podcast and trim down their extra podcasts
• Autumn and the current host plan to continue with some form of the podcast, at least for a little while
• The hosts discuss their passion for the podcast and its focus on infrastructure and technology.
• They mention the variety of topics covered, from 3D printer software to space-related projects.
• The hosts plan to continue the podcast in some form after the current year-end episodes are completed.
• They will make a formal announcement about the podcast's future direction and availability.
• A new feed may be added for listeners who want to continue following the podcast.
• The speaker reflects on the similarities between new technology and old infrastructure
• The importance of preserving and learning from past solutions, rather than discarding them
• The people met through their journey into tech have been a key part of its appeal
• The impact and money that can be made in the tech industry are significant
• The sense of community and shared passion for technology is what keeps the speaker engaged
• The importance of learning from mistakes and embracing ambiguity in work
• Psychological safety as a key contributor to good performance teams
• The value of being given freedom to make mistakes and learn from them
• The privilege of having been given benefit of the doubt in one's career
• The fallacy that senior people automatically know what they're doing
• The speaker is proud of their podcast's approach to discussing technology and its people aspect
• They believe that a safe environment and diversity are crucial in making good tech
• They want to use their privilege to influence positive change and help people from different backgrounds get started in tech
• Gerhard joins the conversation, explaining that he never really left Changelog, as they continued working on infrastructure improvements and taking it to the next level
• Reshuffling priorities in the past
• Transitioning from a large enterprise to a startup
• Working on RabbitMQ at VMware for 6-7 years
• Importance of kernel differences in distributed systems
• Real-world applications affected by kernel issues (e.g. banks, GPS trackers)
• Unexpected use cases and conversations about tech being used incorrectly
• The speaker reminisces about their past experiences, including working at VMware and Pivotal.
• They mention transitioning from a small startup (Cloud Credo) to a larger company (Pivotal) and the changes that came with it.
• The speaker talks about Docker and being fascinated by its capabilities.
• They introduce Dagger, a product they co-founded, which aims to simplify complex workflows and automate tasks in CI/CD pipelines.
• Bazel is mentioned as being in the world of heavyweight enterprise
• Dagger takes scripts and YAML, allowing them to be captured in code
• Automation can be written in various languages (e.g. Python, Go, TypeScript)
• Dagger allows for packaging automation in modules that can be distributed and assembled just-in-time
• Integration with CI/CD is simplified by calling functions from the right module
• Context assumptions are minimized with Dagger, which requires specifying a container image to run
• Dagger can run on various platforms, including Jenkins.
• The speaker discusses their experience with Dagger, a tool for managing Continuous Integration and Continuous Deployment (CI/CD) pipelines.
• They mention that they can run their pipeline locally or in Jenkins without needing Dagger.
• The speaker expresses interest in Dagger's potential to simplify CI/CD processes by allowing teams to focus on writing code rather than managing infrastructure.
• They highlight the traditional approach of having DevOps teams create and maintain Jenkins files, which can be time-consuming and prone to errors.
• The speaker notes that Dagger requires application teams to own their CI/CD pipeline, which can lead to more efficient and scalable processes when the team is familiar with the codebase.
• They conclude that Dagger makes sense for teams who write their own code and manage their own CI/CD pipelines.
• The benefits of using Dagger, including its ability to force different teams and companies to come together as code.
• The concept of writing company-specific code for automation, rather than relying on external scripts or tools.
• How Dagger allows for self-documenting code that can be consumed by users without requiring extensive knowledge of the underlying software.
• The idea of an "API to consuming code" that enables easy access to resources and artifacts.
• The speaker discusses using Dagger to manage and share infrastructure as code.
• Dagger modules are powerful and allow users to focus on their specific needs without needing to know the underlying details.
• The speaker highlights how Dagger modules can simplify the process of building a CI/CD pipeline and managing DevOps workflows.
• The modules provide a way to skip extra files and configurations, allowing teams to learn infrastructure management in a more straightforward way using Dagger.
• The speaker discusses the Dagger project and its capabilities in automating tasks
• There are multiple implementations of a Go module that can automate tasks such as testing, building, and linting
• The module can be run locally or in CI with the same commands
• Dagger has features such as caching and sending telemetry traces
• The speaker mentions that while other tools have similar capabilities, Dagger's comprehensive approach makes it special
• Code literacy is a barrier for many people who may not be comfortable writing automation code.
• The challenges of YAML for non-experts due to its differences from other programming languages
• The difficulty of transitioning from high-level code writing to infrastructure management and DevOps
• The need for more education on scripting, version control, and CICD in tech industry programs
• The potential of the topic being discussed as a barrier for people entering the field of DevOps and CICD
• The importance of making DevOps and CICD accessible to a wider audience
• Difficulty in maintaining complex software systems
• Lack of resources for understanding underlying technologies (e.g. JVM, caching, testing)
• Need for standardized tools and processes to manage software development
• Importance of having a team member or resource that can provide context and expertise
• Frustration with complex files (e.g. YAML, Jenkins) that are not user-friendly
• Frustration with trying to solve issues in code and NPM modules
• Difficulty understanding what is expected of a certain tool or system
• Encapsulation of complex systems within a holistic container
• Troubles with running and introspecting the execution of tools like Make and Dagger
• Value of automation and infrastructure tools, but difficulties with complexity and old documentation
• Discussion of Dagger, a drop-in replacement for other tools
• Explanation of modules as a way to package code and share it with others
• Open telemetry: capturing what happens inside a Dagger call and sending information to Dagger cloud for visualization
• Shell: an interactive environment to discover and work with automation
• Dagger Cloud: a platform for visualizing and analyzing automation processes
• Automation challenges and limitations
• Importance of understanding automation for maintenance and scaling
• Experience-based approach to automation, considering what would be done if starting from scratch
• Caching and storing operations in a remote cache at scale
• Distributed caching challenges, including race conditions and pruning
• Balancing recomputation vs. cached results, especially with large datasets
• Relying on containerization for caching, similar to Docker's approach
• Compartmentalizing code to understand dependencies and avoid cache invalidation issues
• The "magic" of the cloud and its benefits for developers
• Understanding how clouds work, such as AWS and GCP's abstractions like Lambda
• Building features for users by exposing low-level abstractions, such as Fly's Machines concept
• Exposing Linux kernel features through a minimal abstraction on top of generally available features
• GraphQL API as the common interface for all SDKs
• SDKs as GraphQL clients that expose operations and resources in language-specific ways
• Ability to mix and match modules written in different languages (e.g., Go, Python)
• Common API layer enables sharing of code between teams writing in multiple languages
• Enabling dev teams to use their preferred language and frameworks for development
• Restructuring of enterprises and lean operations
• Comparison between traditional on-premises infrastructure and cloud services
• Trade-offs between different technical approaches (e.g. DBAs vs data architects)
• Importance of documentation before automation
• Avoiding unnecessary changes to existing infrastructure (e.g. rewriting Makefiles in Dagger)
• Discussion on the importance of documentation and knowledge sharing in automation
• Incentivizing documentation and its benefits, such as lasting impact and maintainability
• Critique of the current approach to automation, which prioritizes technical skill over other aspects of being a good engineer
• Comparison to containers, which revolutionized applications and could have a similar impact on scripts and automation
• Ideal end goal: making automation easier for everyone to understand and use, with better tools and documentation
• Shared experiences of the pain points in consuming and building software, such as downloading packages and checking dependencies
• Containers not meeting expectations for application packaging and sharing
• Concerns about ambition being too big, resulting in unrealistic expectations and wasted resources
• Competition and market dominance leading to focus on dominant players rather than practical solutions
• Reliability and efficiency of containerized workflows, particularly at scale
• Costs and efficiency of using cloud services vs. local machines for development and testing
• The concept of "on-prem" (running servers on-site) vs cloud computing is evolving, with many companies building their own private clouds without true on-prem infrastructure.
• The speaker argues that even when companies claim to be running on-prem, they are often using a mix of colocation services and bare metal instances, which is not truly different from the cloud.
• Dagger is introduced as a tool that allows for portability and encapsulation of jobs, making it easier to run them anywhere without maintenance costs.
• The speaker highlights the benefits of dagger's portability, including cost savings and flexibility in choosing where to run workloads.
• The conversation touches on the importance of observability and monitoring in hybrid cloud environments and the need for tools that enable lift-and-shift capabilities.
• Importance of portability in development and CI/CD pipelines
• Challenges of scaling infrastructure and "lifting and shifting" legacy systems
• Benefits of using cloud computing, including scalability and on-demand capacity
• Need for well-rounded developers who can work with multiple technologies and architectures
• Role of WebAssembly (WASM) and WASI runtimes in changing the way we use containers
• Value of learning from failures and sharing experiences to become more well-rounded and responsible professionals
• Blue Sky vs other social media platforms
• Democratization of the internet and decentralized data ownership
• Blue Sky's ease of use and self-owned federation model
• Scaling and infrastructure discussion with Blue Sky team
• Personal storage and PDS (Personal Data Stores) integration
• Kubernetes and containerization discussion
• Future plans for the podcast and community engagement
• Promotion of the Changelog newsletter and its benefits
• Mention of Fly.io as a partner with over 3 million app launches
• Introduction of Breakmaster Cylinder as their beat freak in residence