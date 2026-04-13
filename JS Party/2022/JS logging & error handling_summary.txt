• Introduction to the guests and their background
• Definition of logging: Bret Comnes and Mikola Lysenko describe logging as a way to present errors in context, with examples including console logs, stack traces, and structured logs
• Types of logging: simple statements printed out to the console, sending logs somewhere else, providing different log levels for filtering, command line output
• Challenges of concurrent processes and multiple services running at the same time
• Aspect-oriented programming (AOP) as a way to handle cross-cutting concerns like logging
• Incidental complexity in logging and its impact on code maintainability
• Interoperability issues with logging systems and their dependencies
• Limitations of current JavaScript logging solutions (e.g., Debug)
• Client-side logging vulnerabilities and lack of validation
• Best practices for CLI app feedback and user interaction
• Standard output (STDOUT) vs standard error (STDERR) for logging and progress bars
• Philosophy of CLI design: Unix-style vs interactive user interface
• Importance of considering Windows compatibility when designing open-source tools
• Evolution of CLI style over the past 5-10 years, from Unix philosophy to more interactive designs
• Differentiating between CLI logging and backend service logging
• The group discussed the issue of dealing with multiple output streams from development tools
• Tools like Next and TypeScript can produce a "giant, unreadable stream" of logs that are hard to manage
• Some suggested using Tmux or creating custom log viewers in Electron to handle this problem
• Others discussed the potential for innovation in developing a better solution for handling output streams
• The group also touched on the topic of structured logging and its use in certain situations, but generally agreed that simple logging is preferable to complicated systems like Log4j
• Current tools used for logging include Debug, with some additional structured logging for specific events or analytics
• Differences between logging with Debug and structured logging approaches
• Overview of structured logging using Pino and its benefits
• Discussion of metrics collection for performance measurement
• Use cases for full session recording tools (e.g. Datadog's Real User Monitoring)
• Error handling in JavaScript, including exceptions and stack tracing
• Review of modern error handling features and their usage
• Exceptions in JavaScript can make static analysis difficult due to their unpredictable behavior.
• V8, the engine that runs Node.js, has performance issues when dealing with exceptions, making them slower than non-exceptional code.
• Some developers choose not to use exceptions for performance reasons and instead return errors from functions.
• Abort signals are a way to handle exceptions in promises by signaling cancellation from the top of the call stack down.
• Abort signals have two parts: an abort signal and an abort controller, which can be used to stop long-running tasks or cancel promises.
• Abort signals should be used in every promise to allow for canceling and cleanup.
• Abort signals can be used with promises, async/await, and other concurrency control methods.
• Using abort signals allows for handling exceptions and Ctrl+C signals correctly.
• Semaphores are a useful tool for concurrency control and work well with abort signals.
• Abortable synchronization primitives (such as semaphores) are necessary to prevent deadlocks and dangling promises.
• Semaphores for concurrency control
• Abort controllers for canceling promises and avoiding resource leaks
• Adding context to abort signals with reason field (Node 18+)
• Error constructors with optional cause field for adding context to errors
• Performance considerations when using try-catch blocks
• CLI apps should not throw stack traces by default
• Stack traces are often confusing to users and may be unnecessary in many cases
• Debug mode or verbose logging can provide a better solution for developers who need detailed error information
• Libraries should opt-in for log output, rather than announcing themselves by default
• The market may prioritize convenience over optimal engineering practices