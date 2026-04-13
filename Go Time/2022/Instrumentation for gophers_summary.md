• Instrumentation in Go code and its purpose
• Definition of instrumentation as generating signals to monitor application behavior
• Types of instrumentation: manual (adding statements) and automatic (eBPF solutions)
• Benefits of instrumentation, including health monitoring and metrics for distributed systems
• Examples of instrumentation use cases, such as tracking running tasks and tolerating some downtime
• History of Prometheus and its origins in instrumenting code for metrics
• The Go instrumentation library's surprise popularity
• Importance of instrumentation in software development
• Different layers of observability (development, operations, business)
• Challenges of building a solid instrumentation library (efficiency, API scope, dependencies)
• Risks of improper or excessive instrumentation (increased compute power costs)
• Optimizing for performance should be done after an initial working version is created
• Popular libraries and features need to consider the cost of their usage, especially in terms of metrics and cardinality
• The Go runtime metrics package introduced new challenges, such as increased metric count and potential costs
• Balancing feature additions with backward compatibility and user needs can be a complex task
• Changing code in popular packages requires careful consideration of breaking existing users
• Adding new features to an interface or library often results in cruft and weird coding patterns
• Importance of readability and maintainability in code
• Trade-offs between performance and readability
• Stability of APIs and their impact on community
• Instrumentation libraries and their complexity
• Designing APIs with optimization in mind vs. functional correctness
• Use cases for micro-benchmarks to optimize code
• Challenges of using multiple instrumentation tools and frameworks
• Guidance for developers choosing the right tool for observability
• Importance of considering organizational frameworks and existing infrastructure when selecting an instrumentation library
• Implementing metric instrumentation can be simplified using libraries that abstract common metrics.
• Exemplars provide information to show example situations that triggered metric increments or observations.
• Deciding which exemplars to include is a complex task, especially with sampling strategies like tail sampling.
• Sampling rates should be adjusted based on system understanding and volume/cost considerations.
• Tail sampling involves saving trace spans after the request has completed.
• Importance of monitoring in SRE
• Introducing SRE concepts at universities and early in careers
• Criticism of the term "observability" and its overuse/misuse
• Monitoring vs. observability: is one a subset of the other?
• Use of marketing terms vs. technical accuracy in industry jargon
• Discussion of the importance of embracing simplicity in programming
• Unpopular opinion that Go is the best foundation for every software, including embedded systems and machine learning
• Criticism of creating new languages from scratch when existing ones like Go can be refined
• Debate over the trade-offs between garbage collection, memory ownership, and other language features