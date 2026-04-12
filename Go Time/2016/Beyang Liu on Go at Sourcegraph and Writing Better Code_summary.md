• Beyang Liu introduces himself as a representative of Sourcegraph, a programming assistant built on top of a global graph of code
• Sourcegraph's features include live-tweeting at GopherCon (although they may not be doing it this year)
• Recent releases from Sourcegraph include new editor integrations and native tools that provide information one keystroke away while coding
• Beyang explains the concept behind Sourcegraph, which is to treat code as a graph of nodes and edges, allowing for better understanding and analysis of code
• The SourceLib library is discussed, which enables language-independent parsing and static analysis of code
• Listeners discuss their interest in using SourceLib for personal projects and potential use cases
• Connecting local code to a global graph of open-source code
• Real-time analysis of semantic changes in code as it's being typed
• Architecture and scalability for editor plugins
• Data storage using Postgres and Google Object Store
• Indexing code data through crawling dependencies
• Comparison with BigQuery dataset for searching over code
• Treating code as highly structured data for querying and pattern recognition
• Future features for team collaboration, such as attaching discussion messages to specific pieces of code
• On-premise installations of Sourcegraph for larger customers
• Sourcegraph's application stack is primarily written in Go
• Benefits of using Go include its solid tooling and lack of surprises when building a web application
• Go enables metaprogramming through tools like go generate, leading to increased productivity
• GopherCon has grown along with the Go community, with varying degrees of success and experimentation each year
• The Go landscape is changing, with more companies outside of tech using Go for distributed systems and business logic
• GE's "digital company" campaign reflects a broader trend where non-tech companies increasingly rely on software
• Tooling around Go is considered robust compared to other language ecosystems
• Building tooling ecosystems and programming assistants for organizations with limited software development expertise
• Tool sponsorships: Equinox.io (package and distribute Go applications) and ngrok (secure tunneling)
• Alan Shreve's open-source contributions, including a tool to strip boilerplate from Go code
• Day-to-day tools used by the speakers, including Vim Go, gometalinter, ffjson, SQL C, Delve debugger, and Goa for generating APIs and code
• Importance of dependency management tools and potential interest in popular but underutilized tools
• Sourcegraph use and other tools
• Gen-mocks tool for generating mock structs
• Go Tooling and Garbage Collector improvements
• Twitch blog post on garbage collector latency
• GopherCon talks and presentations
• Kubernetes 1.3 release and cluster federation
• etcd 3.0 release and scalability
• Traefik.io load balancer 2.0 release
• Glide 0.11 release and new features
• Code analysis on Go projects
• Desirable statistics for code repositories (e.g. function call frequency, external dependencies)
• Effects of importing packages on project size and complexity
• Call to action for users to suggest additional statistics or features
• #FreeSoftwareFriday discussion and shoutouts to open-source projects and maintainers
• Shoutouts to specific projects (GoKit, The Silver Searcher) for their contributions to the Go ecosystem
• Discussion of Matt's unannounced work
• Encouragement to tweet at Matt to release his work publicly
• Thanks and appreciation for listeners and sponsors
• Upcoming events: GopherCon, live streaming on Twitch
• Promotion of GoTime.fm newsletter and social media channels