• Execution tracer limitations and myths
• Improvements made to execution tracing in Go 1.21 and 1.22 (low overhead tracing)
• History of execution traces in Go, from Go 1.5 introduction
• Usage and benefits of execution traces (unique view into goroutine behavior)
• Challenges with using execution traces due to high overheads and scaling issues
• Traces are now scalable with the introduction of a new format in Go 1.22
• The current Go tool trace doesn't take advantage of this scalability yet
• Flight recording is introduced as a solution for tracing, keeping recent trace information and allowing for targeted tracing
• Tracing can be used to capture bad behavior and specific issues in an application
• An experimental API has been released for parsing traces and doing custom analysis
• Best practices are emerging around using flight recording and tracing, such as starting it at the point of interest and dumping the trace when a problem occurs
• The new features are still experimental and feedback is being sought to inform their development.
• The Go execution tracer can be difficult to understand due to its perspective from a Go scheduler rather than a developer
• Goroutines are not always continuously running and switching between CPU cores at various timescales (microseconds to nanoseconds)
• The traditional view of the execution trace is useful, but may not be approachable for new users
• The Go Trace UI tool provides a different user experience by showing goroutines in a timeline with stack traces
• Use cases for the execution tracer include proving and disproving theories about latency issues and understanding garbage collector behavior
• Execution traces can help identify throughput problems that are not just latency issues
• Goroutine view with filtering to show only relevant goroutines related to a request
• Throughput issues with low CPU utilization and large backlogs in queues, where execution tracing helps identify gaps and patterns in scheduling
• Bottlenecks in goroutine pools due to incorrect sizing, identified through execution traces showing contention on send operations and starvation on receive
• Patterns of garbage collection cycles causing disturbances in application performance, visible only in execution traces
• Importance of looking for gaps and patterns in execution traces rather than individual events
• System call behavior and tracking in execution traces
• Frame pointer unwinding for faster stack tracing
• Optimizations made to the execution tracer, including showing system call durations and treating cgo calls like sys calls
• Discussion of performance issues related to system calls and cgo
• Upcoming talk by Felix Geisendörfer on making frame traces faster
• Training data for a language model (LLM) and potential benefits
• AI performance in understanding and interpreting data analysis graphs
• Discussion of the future of AI development and its potential applications
• Unpopular opinions on tech-related topics, including:
  • Deprecating parts of the Go runtime package
  • The rise of LinkedIn as a platform for tech conversations
  • Music listening preferences when working from home