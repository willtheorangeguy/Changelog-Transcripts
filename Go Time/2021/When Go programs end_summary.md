• What happens when a Go program ends and its main function returns
• How goroutines are handled at program exit
• Behavior of deferred statements at program exit
• Handling of open files and file handles at program exit
• Exit codes and their meaning
• Automatic cleanup by the operating system, including memory reclamation and file handle closure
• Signal handling in Go and its complexity
• Graceful shutdown mechanisms, including the os/signal package and NotifyContext helper
• Signals (e.g. SIGINT, SIGABRT) and their use with Ctrl+C and kill
• Hard exit using os.Exit and its limitations
• Closing of STDIN, STDOUT, and STDERR streams
• Exit codes in Go and how they work
• Proper use of os.Exit() and its implications
• Panics and their effect on program execution and cleanup
• Goroutine exit and defer functions
• Resource management and cleanup when exiting a program or goroutine
• Using curl to test server behavior under various conditions
• Deferred functions are not run when os.Exit is called
• It can be inconsistent or even problematic to run defers for the goroutine that called os.Exit
• os.Exit terminates all goroutines and resources in a program
• A "graceful shutdown" strategy may not always be necessary, but building it into a program can be a good practice for designing resilient systems
• Sub-processes do not get terminated when their parent process exits, unless specific workarounds are taken (such as using CommandContext and context cancellation)
• Discussion on the behavior of os.Exit in Go
• Sub-processes and their cleanup when using os.exec.Command or os.exec.CommandContext
• Comparison with C++'s main function return type for exit codes
• Use of sentinel error types and run functions to manage exit codes
• Importance of graceful shutdown for server processes, file operations, and cleanup
• Practice of implementing graceful shutdown as a habit in programming
• Strategies for handling interrupts and shutdowns in programs
• 12-factor application design and its benefits for consistent behavior
• Importance of being a "good citizen" in the operating system during shutdowns
• Role of garbage collection in Go and potential trade-offs between CPU and memory usage
• Potential alternatives to copying or generational garbage collectors in Go
• Discussing the usefulness of garbage collection in programming and potential performance gains from disabling it
• Mention of Plan 9 C compiler allocating memory without freeing it, leading to performance improvements
• Sharing of a strategy where short-running functions can be written with minimal concern for garbage collection
• Joking about the Terminator's reliance on cloud services and hypothetical implementation with Raspberry Pi and Kubernetes
• Discussion about Robocop and the testing of surround sound systems with R-rated movies