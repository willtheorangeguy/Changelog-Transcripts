• Introduction to the show topic: Foundations of Go performance
• Purpose of the show: To provide guidance from zero to hero in Go programming, specifically focusing on tooling, idioms, and writing efficient Go programs
• Initial steps to identify a performance issue: Ruling out network or disk issues, understanding what the code is doing
• Importance of profiling and understanding background skills such as Linux and kernel experience
• Question to ask first: "Is Go the problem?"
• Discussion of Go's design principles and philosophy: Simple, efficient, garbage-collected language
• Importance of considering the performance profile of compiled static languages like Go compared to dynamic languages like Ruby or Python
• Identifying performance bottlenecks and constraints
• Characterizing problems: repeating, non-repeating, specific requests or users
• Expectations from a performance standpoint: CPU allocation, memory allocation, resource usage
• Understanding the environment's behavior: orchestration tooling, Docker, Kubernetes, process killing due to exceeding allocated resources
• Profiling as a solution for identifying performance issues
• Mechanical sympathy: understanding how computers work and using that knowledge to optimize code
• Unpredictable workloads vs. predictable data sets: different approaches to writing code
• Go's profiling tools (pprof) for understanding goroutines and optimizing performance
• Optimizing Go applications for performance
• Common sources of latency and slowness (API calls, file system connections)
• Importance of understanding how Go handles I/O operations (e.g. IO reader/writer interface)
• Pprof tool for profiling and optimizing code performance
• Identifying bottleneck functions and opportunities for concurrency
• Using CPU profiling, memory profiling, and tracing to inform optimization decisions
• Using pprof tool to identify performance bottlenecks in Go applications
• Importance of benchmarking in optimization, as a last step after identifying issues with pprof
• Writing benchmark tests to measure function execution time and memory allocation
• Benchmarking involves running code multiple times to get an average performance measurement
• Setting up realistic test conditions is crucial for effective benchmarking
• Avoiding common pitfalls such as underestimating the impact of cache size on performance
• Iterating on small changes, measuring their impact, and repeating the process to optimize performance
• Caching and memory optimization in Go
• Understanding the stack and heap in Go
• Lifetime of data and garbage collection
• How garbage collection works in Go
• Factors affecting the cost of garbage collection (number of pointers, speed of generating new garbage)
• Phases of garbage collection: mark and sweep
• Garbage collection in Go and its impact on performance
• When to use pointers vs value types
• Best practices for allocation in Go (defaulting to slices unless necessary)
• Importance of understanding how Go works under the hood
• Use of pprof and benchmarking to optimize performance
• Strategies for minimizing garbage collection pauses (pre-allocating data structures, etc.)
• Benefits of pre-allocating memory for slices and maps
• Importance of writing efficient Go code through practices such as making it elegant before optimizing
• Best practices for using pointers and avoiding unnecessary memory allocation
• Value of using linters to catch common errors and prevent memory problems
• Strategies for optimization, including reusing compiled regular expressions and templates, and minimizing work
• Criticisms of Python as a language for data engineering
• Discussion of the benefits and use cases of "irate" data smoothing
• Apple's open-source project, Pickle (pkl), and its potential advantages over JSON and YAML
• Comparison between Pickle (pkl) and CUE programming language
• Johnny Boursiquot plans to research Pickle (pkl) further and potentially discuss it with the CUE contributors