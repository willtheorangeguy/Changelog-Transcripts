• Go was designed with concurrency in mind
• Goroutines and channels are key language primitives for concurrency
• Concurrency is not necessary or suitable for every problem
• Channels allow safe communication between goroutines
• The "go" keyword starts a new goroutine
• Main program is itself a goroutine that can wait on other goroutines
• Separation of concurrency and parallelism in Go makes it easy to use
• Select statements are powerful for concurrent programming
• Concurrency can be easily migrated from synchronous code
• Context in Go programming
• Boilerplate code for context handling
• Improving select block functionality for automated context handling
• Goroutine shutdown and cleanup mechanisms
• Communication between goroutines using WaitGroup, channels, and other means
• Limited control over underlying OS threads and scheduling in Go
• Fine-grained optimizations using pinning to specific processors or cores
• Go's sync.Pool is lossy and used by Ristretto authors due to lack of thread-local storage
• Some companies are misusing underlying thread-local storage for execution tracing and instrumentation
• sync.Once utility ensures a function is only called once, useful in concurrent contexts
• sync.Map is often misused as a thread-safe hashmap, but it's actually designed to reduce cache contention
• A mutex should be used with regular maps to protect against concurrent access
• Defer statements are now faster and can be safely used to lock and unlock mutexes
• Defer statement in Go for handling file and resource cleanup
• Readability benefits of using defer over explicit closing
• Exceptions to using defer (e.g., large functions, performance-critical code)
• Concurrency in Go, specifically the select statement
• How select works and its benefits in concurrency
• Importance of default case in select statements
• Blocking vs. non-blocking behavior with empty selects
• Using buffered channels for signal passing
• Using empty structs as signals for zero allocation mechanisms
• Benefits of using an empty struct over booleans or other types for signaling
• Concurrency in libraries: hiding concurrency internally vs. letting users orchestrate it
• Asynchronous APIs and the preference for synchronous ones
• Labeling concurrent operations in Go documentation
• Importance of keeping concurrent code local and nearby, avoiding scattering concurrent operations throughout a program
• Concurrency vs parallelism
• init function pitfalls
• Need for precise control over goroutine distribution
• Use of Unix package to lock threads to specific processors
• Workarounds for lack of fine-grained concurrency control
• Using buffered channels as a semaphore substitute
• Use of channels is more expressive than mutexes
• `time.After` function returns a channel that sends time after a duration, allowing for timeouts in select blocks
• Example of using `time.After` for testing and user updates while waiting for tasks to finish
• Roberto Clapis has had bad experiences with the Go `time` package, recommending caution when using it
• Discussion on the complexity of the `time` package and ticker functionality