• Mislav Marohnić's background and experience maintaining the project "hub" and his work at GitHub
• History of the hub project: its creation by Chris Wanstrath as a short script to make Git interact with GitHub more smoothly
• Evolution of hub from a small tool to an official GitHub CLI, eventually becoming part of the company's organization
• Mislav Marohnić's experience transitioning from working on hub as a personal project to being employed at GitHub and maintaining hub professionally
• GitHub's hiring process and how Mislav Marohnić's prior work with GitHub founders and employees influenced his application and eventual hire
• Early version of hub was a Ruby script, intended to be easily copied to any system; its initial goal was to extend Git for use with GitHub
• Abstraction vs extension of Git's API
• Difficulty in maintaining large number of extensions and added functionality on top of Git
• Consideration of abstracting away 80-90% of GitHub users' usage to simplify the interface
• Examples of extensions: adding flags, transforming arguments, creating new commands (e.g. sync)
• Challenges of extending Git without breaking its core functionality
• Evolution of hub from Ruby to Go
• Issues with Ruby's performance and portability, leading to decision to rewrite in Go
• Transitioning hub from Ruby to Go
• Minimizing bugs and maintaining trust in the community during the transition
• Introducing Go to a team not familiar with it using CLI projects as an example
• The importance of hands-on experience with Go and seeing its successful implementation by colleagues
• Testing approach for the CLI, specifically using end-to-end testing through Cucumber and story-driven development
• The challenge of maintaining a test suite that covers both Ruby and Go versions
• Mislav Marohnić learned Go by working in an existing project's codebase
• He rewrote the hub tool in Go from scratch, motivated by preserving what worked well with the new language and its compiler
• The decision to rewrite was made after evaluating other options, but ultimately decided that starting fresh was the best approach due to technical feasibility and avoiding bug-prone code
• The new official CLI tool will eventually replace hub, and Mislav plans to continue supporting both projects until they are sunsetted
• The speaker discusses their reduced involvement in maintaining a CLI project due to other priorities.
• They plan to make updates before scaling back further, including authentication improvements and exposing new features.
• The topic of building CLIs in Go is discussed, with the speaker recommending not starting from scratch unless for learning purposes.
• Cobra library is mentioned as popular but with drawbacks, such as requiring backwards-compatibility maintenance.
• The importance of structuring a project to be flexible and easily maintainable over time is emphasized.
• Other libraries and tools are mentioned, including Testify, go-colorable, and go-isatty.
• The CLI codebase has many library dependencies
• The use of markdown rendering was impressive and utilized Blackfriday for parsing
• Specialized tools for terminal interaction are scattered and hard to discover
• Mislav Marohnić considers contributing to Go libraries as part of giving back to the community
• Handling errors and bugs in a CLI is challenging, especially without monitoring or crash reporting
• A microservice design could facilitate easier error reporting and debugging
• The trade-off between adding features like monitoring and user comfort was considered
• Mislav Marohnić expresses disappointment with Go's inability to handle GraphQL well
• GraphQL limitations and potential misuse in Go projects
• Difficulty in batching multiple queries or mutations in current Go libraries
• Over-fetching issue in REST APIs vs. benefits of GraphQL for selective field requests
• Current state of Go GraphQL client implementations as lacking or "suck"
• Potential growth of CLI usage with GraphQL APIs
• Concerns about Go's suitability for GraphQL and potential impact on its usefulness as a CLI language
• Git CLI discussion, mentioning primary interface to Git itself
• Difficulty in using Git due to its complex commands and concepts
• Need for a more approachable version control system that reflects how humans think about version control
• Importance of including graphical tools and abstractions to simplify the user experience
• Issue of Git being designed primarily for power users, making it difficult for average users to use effectively
• Proposal for two versions of Git: one for average users and another for advanced users with specific needs
• Challenges of using GitHub official CLI (gh) and its predecessor hub
• Writing gh in Go and potential benefits and challenges
• Importance of learning from contributors and discovering new tools and libraries
• Upcoming departure of guests from a podcast or show (Go Time)
• Positive experience and appreciation for the insight shared by guest Mislav Marohnić