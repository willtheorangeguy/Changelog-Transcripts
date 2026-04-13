• Travis Jeffery introduces himself and his background in programming
• Motivation for creating Jocko: to simplify Kafka setup and configuration, and eliminate dependencies on JVM and Zookeeper
• Explanation of what Kafka is and its use cases (message queue, commit log service)
• Discussion of the benefits of using Kafka as a system of record and data hub
• Examples of using Kafka in a streaming data workflow for analytics events
• Implementing a distributed system using Go, with workers reading from Kafka and producing output
• Designing a dependency graph management system for decoupling services
• Similarities to goroutines and channels in Go
• Using consumer groups to handle concurrent data processing
• Feature-complete implementation of the system, with remaining work on replication and consumer group support
• Performance comparison to Java, with potential limitations due to lack of zero-copy networking
• Simplification by removal of Zookeeper requirement in Kafka protocol
• Implementation of storage layer for Jocko, using Kafka's log-structured merge tree design
• Use of Raft consensus algorithm and Serf service discovery in Jocko implementation
• Google releases Shenzhen Go app for graphically designing concurrency and data flow in Go
• Discussion of Go-Call-Vis project for visualizing call graphs of Go programs
• Mention of Subgraph OS, an operating system using Go for memory safety
• Uber's Cherami library for queuing systems and its similarities to NSQ
• Comparison between Cherami and NSQ, including durability and ordering guarantees
• Introduction to Ponzu CMS, a content management system with API access
• Ebiten 2D game library for building old-school style games
• Influence of GoldenEye on their youth
• Discussion about Go Resolutions for 2017 and potential implications for future versions of the language (Go 2.0)
• Package management in Go, including frustrations with current tools and desire for improvement
• Use of vendoring tools in Go projects, specifically discussion of Go Vendor and godeps
• Discussion of an article that sparked anger in Brian Ketelsen
• Importance of addressing sexual harassment in the industry, with a potential future episode on the topic
• GopherCon conference and its Code of Conduct (COC)
• Incident at GopherCon where someone violated the COC
• Promotion of GopherCon's Call for Papers (CFP) and importance of submitting proposals early
• Discussion of the gops project by Google, a tool to list and diagnose Go processes
• Reminder that the CFP for GopherCon ends January 31st
• Submission guidelines for talks at GopherCon
• Qualifications for speakers and how to demonstrate expertise without revealing identity
• Benefits of submitting a talk, including mentorship and travel compensation
• Variety of presentation formats available, including tutorials and workshops
• #FreeSoftwareFriday segment featuring projects or software recommendations
• Discussion of specific open-source projects, such as oklog and OpenOCD
• Redis 4.0 release candidate is out
• Travis Jeffery discusses his experience with Redis and its uses
• Brian Ketelsen shares his use of goa/gorma for designing APIs first
• Discussion about using Go frameworks for web development vs standard library
• Buffalo framework is mentioned as a popular choice for Go web development
• Eric St. Martin mentions writing web applications without using a framework
• Discussion of a Docker-backed web terminal and issues with WebSocket upgrades
• Tradition at GopherCon of taking the first ticket purchaser out to dinner
• Request to discuss the standard logging interface in Go
• Proposal for a single interface for logging in Go, inspired by Java's Log4j
• Concerns about current logging packages in Go, including lack of log levels and structured logging
• Discussion of potential compiler changes to improve logging performance
• Show wrap-up and thank-yous to listeners
• Shoutouts to sponsors: StackImpact and Backtrace
• Recap of show participation: Travis, Carlisia, and Erik St. Martin 
• Promotion of GoTime.fm resources: Twitter handle, email newsletter, and GitHub ping for guest suggestions