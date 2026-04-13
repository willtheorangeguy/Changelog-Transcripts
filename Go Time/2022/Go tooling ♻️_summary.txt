• Discussion of a re-released episode of "Go Time" from 2019 about tooling
• Overview of the changes in the world since the original episode was released (COVID, social distancing, etc.)
• Promotion of Sourcegraph's new feature, Code Insights, for tracking code base metrics
• Introduction to the main topic of discussion: Go tooling and its uses in building, running, testing, formatting, and linting code
• Guest appearance by Jana Dogen, who is joining the show after a brief absence due to travel and a potential job change
• Johnny Borsico discusses his new job and the excitement and challenges that come with it
• GoTools are discussed, specifically GoFumpt (also known as GoFormat), which formats Go code into a uniform style
• The benefits of Go's uniform formatting include improved readability and reduced conflicts in pull requests
• Pronunciation of GoFumpt is clarified as "Go-Fumpt"
• Discussion about the naming conventions for Go, including using "Go" instead of "Golang", and the correct pronunciation of GoFormat as "Go-Funp" or "GoFund".
• Programmer preferences for styling in Go are subjective and varied.
• GoFund standardized formatting, reducing cognitive load when reviewing code.
• Its creator, Robert Grismer, doesn't agree with all of its rules but appreciates enforcement.
• Large companies struggle to implement style guidelines due to conflicting opinions.
• Having a canonical place like GoFund helps avoid debates on minor issues.
• Injecting tools like GoFund into an existing community can be challenging.
• Design decisions made early in the development process set precedents and pay dividends.
• Tooling in Go represents priorities, such as 80% of essential software engineering practices.
• GoLint and GoVet are mentioned for discussion.
• GoLint tool catches style errors and encourages best practices
• Code comments should be included for exported functions with capital letter names
• Lint rules are not enforced by the compiler but generate useful reports
• Beth and Lint differ in their approaches, with Lint focusing on style and Beth on suspicious behavior
• False positives can occur when using these tools, but they generally produce genuine reports
• Using linters like GoLint and Beth can improve code quality and make it more familiar to follow GoFund guidelines
• The difference between linting and vetting is not strictly defined, but linters focus on style and formatting issues.
• Tooling for Go development, including vet, lint, and format checking
• IDE integration, such as in VS Code, for seamless tool usage
• Importance of live feedback from code during development
• Running tests quickly and continuously while coding
• Local tool usage vs. CI/CD pipeline tools like CircleCI or Travis
• Benefits of becoming a Square solutions partner, including access to the entire Square platform and custom solutions for sellers
• Incentives and profit sharing, including a 25% SaaS revenue share and seller referrals
• Access to alpha APIs and new products
• Product, marketing, tech, and sales support
• Opportunity to get Square certified
• Use of GoTest tool for writing test codes in Go programs
• Race detector feature in GoTest for detecting potential deadlocks
• Importance of covering concrete cases in tests for effective use of the race detector
• The benefits of using Go Run for quick results and feedback
• Complications that can arise when relying solely on Go Run
• The importance of using Go Build or install instead of Go Run
• The use of the -race flag with Go Run to detect race conditions
• The trade-off between enabling the -race flag and potential slowdown in program execution
• The mixed results experienced by the speaker with large codebases and the -race flag
• The comparison of go get vs. module tools for package installation
• Difficulty in understanding GoGet and its simplicity
• Importance of being able to see code in a browser to understand what is being pulled down
• Comparison with NPM package installation and hidden dependencies
• Discussion on the value of simplicity and clarity in software development
• Mention of Go month and potential episode idea
• Use of GoGet for initial experience and distributing tools
• Discussion on cross compilation using go build and its benefits
• Experience with cross compiling on different platforms, including Docker
• The importance of intermediate assembly in compiler design
• Cross-compilation process and its benefits (faster development)
• How compilers generate machine code based on architecture
• Build tags and conditional compilation
• Using build tags for testing and including specific files depending on the target platform
• Limitations and complexities of multiple build rules and custom build tags
• Retool as a platform for building internal tools
• Community-created tools for Go development, such as Go Imports and JSON to Go service
• The Go report card website for evaluating code quality
• Godoc and its hosted service for viewing documentation
• Dominic Honneth's GoTools repo with static check tool
• Fixing Me, a GitHub integration that creates PRs with style rule changes
• Fix Me project: a tool similar to the Go report card, tightly integrated with GitHub
• Static analysis tools in Go
• Generating implementations of interfaces using a custom tool
• Performance tools in Go, including PPROF and benchmarking support
• Dynamic tools in Go for debugging and performance monitoring
• Benchmarking as a first-class citizen in certain languages creates a culture where benchmarking is prioritized.
• Effective benchmarking requires understanding of tooling and proper usage to avoid incorrect results.
• Benchmarks can be used for comparing performance of algorithms or HTTP requests, but may not provide meaningful information for complex tasks like HTTP.
• Premature optimization should be avoided, and instead, problems should be solved first, then optimized.
• Continuous profiling in production environments provides valuable data on hot calls and critical paths to inform optimization decisions.
• Optimization during development time can create fabricated problems and a culture of over-optimization.
• Profiling techniques for low overhead and continuous profiling in production environments
• Strategies for minimizing impact on critical paths, such as enabling profiling on one replica of a web server or limiting duration
• Importance of identifying hot paths and optimizing based on usage patterns
• Use of P-Prof tools for dynamic profiling and aggregation of data
• Potential for community-built tooling to support continuous integration and profiling
• Benefits of systematic optimization, including cost savings and improved performance
• GoLint became easier to satisfy
• The host made a contribution that allowed this
• The show ended with thanks and promotional announcements
• Upcoming episode featuring Ronna Steinberg discussing object-oriented programming in Go
• Partners acknowledged, including Fastly and BMC
• Call for audience engagement and recommendations