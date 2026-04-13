• Introduction to a "best of" style clips show covering the summer months
• Panel discussion on working with databases in episode 132, The Trouble with Databases
• Discussion of trade-offs between NoSQL and SQL databases for different use cases
• Importance of understanding how data is stored at a lower layer
• Common practice of using multiple databases in a system for different purposes (e.g. relational, warehousing, search)
• Trade-offs in distributed systems and the CAP theorem (Consistency, Availability, Partition Tolerance)
• Tolerance tradeoffs in distributed systems: consistency vs. availability
• CAP theorem limitations
• Relational databases (CP) vs. NoSQL databases (AP)
• Spanner's approach to achieving high availability and partition tolerance
• Importance of understanding underlying technologies in software development
• Personal anecdotes about learning from mistakes and over-planning/over-optimizing
• Trade-offs between abstraction and understanding underlying protocols
• Understanding HTTP RFC and basic headers for writing more direct code
• Open-source projects as showcases of perfected code, but not representative of initial development stages
• Choosing technology based on team experience and minimizing learning curves
• Innovation tokens and the cost of being productive with unfamiliar technologies
• Stealing ideas from open source to solve problems effectively
• Scalability and control in microservices architecture
• Managing a wide tech stack as a small company grows
• Postgres is mentioned as a stable, mature solution with over 20 years of history and widespread use among thousands of companies worldwide.
• The importance of using well-tested and established technologies for long-term data storage is emphasized.
• A Go developer's perspective on working with databases, including the use of connection pooling in the standard library.
• A discussion about avoiding Object-Relational Mappers (ORMs) and instead learning to write SQL queries directly.
• A mention of a humorous XKCD comic illustrating the concept of SQL injection.
• Learning the Go programming language through online resources and communities
• Using platforms like Exercism for learning and mentorship
• Benefits of receiving iterative feedback from mentors during the learning process
• Importance of understanding concepts like garbage collection and reviewing best practices across languages and architecture patterns
• The value of having a support community while learning a new skill or language
• Retool as a platform for building internal tooling with reduced time, effort, and maintenance required
• Testing frameworks in Go, specifically the use of Testify and BDD (Behavior-Driven Development)
• The challenges of testing code with multiple variants and the benefits of string-based text names
• Property-based testing, including its similarities to fuzzing and how it can find edge cases
• Generics in Go, including the latest draft proposal and the decision to simplify contract types to interface types
• The development of a translation tool and type checker for generics
• The timeline for moving from a draft proposal to a formal proposal in the language
• Concerns about allowing too much flexibility in generics
• Need for a best practices guide to help developers use generics effectively
• Importance of experimentation and gathering feedback from the community
• Potential impact on build speed and need for compiler changes
• Comparison to garbage collection, which was initially met with skepticism but is now widely accepted
• Discussion of JSON's popularity and widespread adoption in modern languages
• The speaker discusses the trade-offs of using third-party JSON re-implementations in Go, including performance benefits but also increased binary size.
• A bug in the standard library's JSON decoder is mentioned, where it can lead to incorrect behavior when decoding large JSON objects.
• The speaker and others discuss the challenges of defining roles such as SRE (Site Reliability Engineer), systems engineering, and DevOps due to varying definitions across organizations and over time.
• The chicken and egg problem of needing experience to get a job, but also needing a job to gain experience
• The difficulty of learning certain skills on one's own, especially for large-scale jobs
• The potential benefits of hiring inexperienced people into a field, as they can bring fresh perspectives and identify core friction points more effectively than experienced individuals
• A discussion about the Go programming language's context package, including ways to reduce latency in requests
• An explanation of how the `context.Background()` function works, including its differences from `context.TODO()`
• The use of `context.TODO()` as a way to indicate that a function needs to be updated to accept a context, rather than returning an empty context.
• Pixie is a magical API that provides instant debug data without code changes or manual UIs, living inside Kubernetes.
• Pixie can capture metrics, traces, logs, and events like a decentralized Splunk.
• The team behind Pixie aims to bring it to market for broad use by the end of 2020.
• Links to the beta and Slack community are available in the show notes.
• Unpopular opinions expressed include:
  • Most new technologies are not necessary
  • Docker and Kubernetes can be overused
  • Small teams are more effective than large ones
  • REST APIs cause more confusion than problems they solve
  • Pair programming is unpopular despite its benefits
• Importance of documentation in contributing to a project's success
• The need for balanced identifier naming (short vs long)
• Critique of overly long variable names and excessive commenting
• Caution against proposing language changes without considering potential drawbacks
• Defense of the performance of encoding JSON, with consideration of trade-offs
• Concerns about premature adoption of Protocol Buffers (protobuf) and its complexities
• Critique of protobuf's verbosity and generated artifacts in Go programming language
• Discussion on the benefits and potential use cases for generics in Go
• Mention of a past episode on Encoding JSON and a discussion on JSON injection attacks
• Upcoming guests
• End of current broadcast
• Appreciation for listeners
• Return from commercial break