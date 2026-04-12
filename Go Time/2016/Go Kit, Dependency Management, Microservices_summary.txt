• Peter Bourgon's background and experience with Go
• Early attempts at using concurrency in Go, including failed projects and lessons learned
• Soundcloud's use of Go for internal infrastructure and applications
• Common mistakes made by beginners in Go, including overuse of channels and misunderstanding interfaces
• The importance of understanding the subtleties of Go language features, such as interfaces and goroutines
• The difficulty of rewriting or erasing bad code once it is open-sourced
• Discussion of how to approach learning and understanding Go, including the value of the language spec and seeking out explanations from experts.
• The importance of experience and "battle scars" in understanding complex concepts, such as the Memory Model.
• The challenges of teaching newcomers about the language without them experiencing the problems firsthand.
• Peter Bourgon's approach to teaching Go through a service-oriented lens, highlighting its strengths and best features.
• Microservices and their benefits, including reduced complexity and easier maintenance.
• Peter Bourgon's experience with microservices at Soundcloud and his advocacy for using Go in this area.
• The ideal size of a codebase is one that can be held in your head as a mental model, and microservices can help with this.
• Microservices enable organizational harmony, improve shipping velocity, and reduce communication overhead.
• However, there are risks to taking it too far, such as creating technical problems and duplicated services.
• An "elegant monolith" architecture can be a viable alternative, especially for small teams or projects.
• Package boundaries in Go can make it easier to contain code within a single repository.
• Monorepos can be beneficial, but also have their drawbacks, and there's no one-size-fits-all solution.
• Dependency management issues in Go
• The "hope-driven development" approach to dependency management
• The problem of nested vendoring and vendor directories
• The proliferation of 13 different standards for managing dependencies
• Peter Bourgon's proposal to form a committee to pick a standard solution
• The current state of the community's efforts to address dependency management issues
• Creation of a new dependency management tool for Go
• Current state: prototype implementation underway by core committee
• Goal: create a single standard for dependency management in Go ecosystem
• Timeline: aim to have a usable prototype by end of year, with potential integration into Go tool in 1.9 timeframe
• Challenges: competing standards and usability issues introduced by multiple tools
• The benefits of a restrictive approach to package management in Go
• Discussion around complex requirements and use cases for Go's package manager
• Influence from other languages' package managers and idioms
• Aliases in Go's package manager and potential drawbacks
• Peter Bourgon's project, Go Kit, and its purpose in addressing microservice architecture challenges in Go
• The speakers discuss Go Kit's usage and adoption rate, mentioning that many companies use it but don't publicly disclose it.
• They mention Go Kit's channel on Gopher Slack has over 1,000 members, which is a significant percentage of the total community.
• The conversation turns to measuring involvement in communities and estimating user numbers, with one speaker citing an "80/20" rule where 80% of users are not visible in public communities.
• Peter Bourgon compares Go Kit to Go Micro, describing them as having different approaches to solving microservices problems: Go Kit is more conciliatory and focused on software architecture, while Go Micro is more opinionated.
• The speakers discuss the benefits of Go Kit's modular design, which allows organizations to adopt its principles gradually.
• Discussion of distributed tracing and logging in Go Kit
• Trade-offs between adopting multiple features at once vs starting small
• Comparison of Go Kit with other frameworks like Go Micro
• Interoperability of Go Kit components with self-written code and other tools
• New tool gops for debugging Go processes, including its limitations
• Upcoming GothamGo event in New York City
• Go Team's new font for Go code
• Discussion on the usability and readability of the new font
• Reluctance to change editors or environments despite technological advancements
• Peter Bourgon's question about a Prometheus-like solution for log management
• Distributed log storage and querying
• Comparison of Elasticsearch with other solutions (Logstash, FluentD)
• Discussion on metrics vs logs and their different use cases
• Scalability challenges in logging at large scale
• Differentiating between debug logging and audit logging
• Mention of structured vs unstructured logging
• Introduction to #FreeSoftwareFriday segment
• Discussion of alternative search tools to grep
• Mention of ack and The Platinum Searcher as viable alternatives
• Shared experience of panelists discovering The Platinum Searcher but not installing it yet
• Closing statements and thank yous from the hosts