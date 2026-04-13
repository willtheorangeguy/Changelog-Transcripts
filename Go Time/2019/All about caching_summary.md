• Caching basics: definition, purpose, and benefits
• Types of caching: in-memory vs network-based (e.g. Redis)
• Advantages of in-memory caching: speed, RAM availability, cheaper storage options
• Limitations of caching: can't replace database functionality, scalability issues with cache management
• Cache consistency across multiple systems: challenges and solutions
• Use cases for caching libraries: in-host caching vs caching servers (e.g. Redis)
• Interaction between caching and database design: SQL vs NoSQL databases, graph databases
• Least Recently Used (LRU) caching strategy
• Limitations of LRU caching at scale, especially with high concurrency
• Cache capacity management: determining what to keep and what to evict
• Consequences of poor cache implementation on performance
• Designing a general-purpose cache library for concurrent systems
• Challenges in balancing trade-offs between different metrics (e.g. hit ratio, latency)
• Overview of ristretto, a caching system developed for Dgraph, and its design goals
• Influence of caffeine cache on ristretto's development and implementation
• TinyLFU admission policy in ristretto, allowing items to be cached based on access counters and eviction policy
• Freshness mechanism in TinyLFU, halving access counters periodically to give new items a chance to get cached
• Customization options for users of ristretto cache library, including configuring number of counters and lossy buffers
• Scalability and concurrency features of ristretto cache, designed to prevent deterioration in hit ratios even under high contention.
• Using Sync.Pool to build a buffer system similar to Stripe, with options for buffering up to 64 gets before applying internal locking
• Comparing the throughput of Sync.Pool to naive channel implementations, showing significant improvement in performance
• Discussing the limitations of Go's thread-local storage and how Sync.Pool provides a workaround
• Mentioning that Ristretto uses various "hacks" or optimizations to increase performance
• Talking about the importance of code readability and maintainability, with Dgraph prioritizing user feedback over refactoring or features
• Sharing experiences and stories of learning from successes and failures in cache optimization and design
• Explaining how Ristretto avoids contention on caches by spreading keys across shards using Sync.Pool
• Discussing the use of Go's internal MemHash function for faster hashing and its applications in caching
• Considering scenarios where pre-populating a cache with expected future traffic is beneficial, but also noting that Ristretto can handle this naturally
• Mentioning the concept of hit ratios as a metric for evaluating cache performance
• Bélády's theoretical optimum and its application in cache implementation
• Ristretto's cache algorithm, including its admission policy and eviction process
• Use of TinyLFU counters to estimate key values and optimize cache performance
• Sampling mechanism for finding eviction candidates with minimal value
• Trade-off between code complexity and performance, aiming for "good enough" solutions rather than optimal ones
• Potential server implementation of ristretto, including network considerations
• Future development plans, contingent on community demand and interest.
• Designing a cache for scalability and performance
• Ristretto's goals and purpose in the Go ecosystem
• When to use caching: prioritizing system design over introducing a cache
• Trade-offs of using caching: correctness issues, contention, and potential errors
• Testing and validation: multi-level testing, Jepsen tests, and correctness verification
• Reproducibility and usefulness of complex system tests
• Black box testing and its limitations in identifying issues
• Distributed tracing as a tool for identifying problems
• Importance of instrumentation in debugging complex systems
• Challenges in taking test results and turning them into actionable fixes
• Example use case: using OpenCensus tracing to track down issues with Jepsen tests