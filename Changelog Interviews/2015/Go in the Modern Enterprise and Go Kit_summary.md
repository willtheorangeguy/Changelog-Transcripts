• Peter Begon's background and experience in software engineering, including work in telecom, distributed systems, and container networking
• Overview of Peter's current work at Weaveworks on software-defined networking for containers
• Discussion of the differences between embedded software development and distributed systems development
• Peter's shift in focus from optimizing performance to building correct systems quickly, especially in the face of failure
• Introduction to Go Kit, a toolkit for microservices, and its connection to Peter's talk at FOSDAM in London
• The speaker was approached to give a talk at a Go conference and reflected on the state of the Go community and his own experiences with Go at SoundCloud.
• SoundCloud had to choose a few supported languages as they grew, and Go was initially considered but ultimately not chosen for all projects.
• The speaker realized that Go was missing a collection of higher-order idioms and tools to make it more attractive to organizations as a long-term choice.
• This realization led to the creation of Go Kit, a framework designed to give confidence to organizations choosing Go for their application layer and business logic.
• Go Kit's goal is to be a good neighbor to existing infrastructure and allow organizations to slide into using Go where it makes sense.
• The speaker's goal is to make Go a viable option for developers who want to use it, and to lower barriers to adoption for those who are unfamiliar with the language.
• The speaker notes that Go has only been around for about 5-6 years, which is a relatively short time in software development, and that it's still a young language.
• The speaker is designing Go Kit for companies that have chosen to adopt a microservices architecture, which they believe should only be done by companies of a certain size (at least 100 engineers).
• Go Kit is intended to help companies that have adopted microservices architecture to simplify their development and deployment process.
• The speaker distinguishes between containers (which solve technical problems) and microservices (which solve organizational problems).
• The speaker notes that microservices architecture makes sense for companies with at least 100 engineers, and that Go Kit is designed to shine in this context.
• The speaker mentions that there are other options, including monolith and SOA, and suggests breaking down the different options for developers.
• Monolith vs Microservices: trade-offs and evolution of architecture
• Characteristics of monolith and microservices, including deployment and scaling
• Challenges of microservices, including complexity and frictional costs
• Evolution of architecture as teams grow, from monolith to microservices
• Gokit: a collection of tools for building well-behaved microservices in Go
• Importance of proper logging, telemetry, and life cycle management in microservices
• Simplifying distributed systems theory and messaging patterns with Gokit
• Choosing an RPC messaging pattern for Gokit
• Go Kit is a collection of libraries for building scalable and robust microservices in Go
• It provides a set of idioms like circuit breakers and rate limiters to help services play nicely together
• The goal is to give a positive story and bright future to organizations using Go for the first time or expanding its use
• Go Kit is compared to other similar libraries from companies like Twitter (Finagle) and Netflix (Ribbon)
• The project is open-source and relies on the community for development and contributions
• The goal is to attract more contributors and developers to the project to further its success and adoption in the Go ecosystem.
• Chris Hines' contributions to the GoKit log package
• Collaboration with Thomas Sanart on endpoint API design
• Help from Roger Pepe with the rate limiter
• Digital Ocean sponsorship and promotion
• Peter's upcoming talk at Gopher Con on GoKit
• Gopher Con event and its significance
• Discussion of GoKit components and their statuses
• Introduction to the package endpoint concept and its purpose
• RPC messaging pattern and method signature in GoKit
• Context and its role in GoKit architecture
• Google's value-add package for microservices
• Context and threading information across stack boundaries and services
• Package endpoint, metrics, and logging packages
• Circuit breaker and load balancer for rate limiting
• Tracing and client patterns for service discovery
• Microservices logging standards and structured logging
• Metrics and instrumentation for application performance
• Graphite and statsd-like metrics package in gokit
• Histograms, gauges, and counters for metric collection
• Common interface for metrics, with adapters for popular packages (e.g. Prometheus)
• Circuit breakers for preventing cascading failures in microservices
• Load balancers for distributing traffic across multiple instances of a service
• Service discovery for translating service names to sets of instances
• Value-add components for microservices, including rate limiting and rate limiting
• Load balancer package
• Rate limiting, its differences and applications
• Distributed tracing framework, including Zipkin, Dapper, and App Dash
• Client patterns and tracing implementation in gokit
• Support for other distributed tracing systems, including Source Graph and H Trace
• Comparison to Kubernetes and Borg
• Client patterns for exposing services on different transports (e.g. HTTP, JSON, Thrift, GRPC)
• Service discovery for finding services to talk to
• Go Kit's goal of writing implementation once and exposing on multiple transports simultaneously
• Client package for creating clients with same semantics as service implementation
• Ad service as an example implementation of Go Kit's features and APIs
• API stability and documentation, with current state being pre-alpha and subject to change
• Go Kit's API stability policy
• Importance of API stability in software development
• The concept of vendoring in Go Kit
• Creating reproducible builds and enforcing API stability policies
• The Go 1.5 release and its impact on Go Kit
• The potential creation of a working group for Go Kit enthusiasts
• Top Towel's network of freelance software developers and its benefits
• Gophers.slack.com as a community and online forum for discussing Go-related topics
• Invitation and link to join the Go Kit community on Slack
• Gopher Con conference schedule, including hack day and workshop events
• Hack day experience and its focus on collaboration and code development
• Gopher Con community and networking opportunities
• Go Kit Birds of a Feather (BoF) meeting possibility
• Changelog Films and documentation of Go-related conferences and events
• Getting involved with Go Kit development and contributing to its growth
• Discussing the Go ecosystem and the need for contributions to the Go kit
• Mentioning the importance of user stories and use cases in shaping the Go kit
• Introducing the Go kit Slack community and encouraging users to participate
• Talking about the concept of "heroes" in one's career, referring to mentors and role models
• Discussing the importance of mentorship and the need for more mentorship in the Go community
• Mentioning the Digital Ocean partnership and the company's involvement with the Go kit
• Discussing the adoption of the Go kit by organizations and the potential for feedback-driven development
• Thanking the guest, Peter, for joining the show and discussing the Go kit
• Discussing the show's history and previous guests, including Rob Pike and Andrew
• Peter Bergon's upcoming project mentioned as something "very cool" that the Go community should know about
• Plans to discuss Prometheus on the show in the future
• Peter Bergon's contact information (GitHub, Twitter)