• Debugging Go and common challenges
• Importance of logging in Go applications
• Unpredictability in debugging and addressing it with tools and techniques
• Panics vs exceptions in Go and how to handle them
• Differences between debugging locally and in the cloud
• Using print statements vs debuggers for debugging
• Cloud debugging challenges: difficulty in attaching debuggers, limitations of logs, and pain of adding print statements
• Traditional debugging techniques don't work well in cloud environments due to proxies, timeouts, and process termination
• Rookout's live debugger provides a breakpoint-like experience without attaching a traditional debugger
• Snapshots are collected asynchronously, allowing for offline analysis and navigation between different snapshots
• Good practices for easier debugging: logging (not too much or too little), focusing on error conditions while writing code, and prioritizing logs for error states over happy flow
• Importance of error logs in debugging
• Value of providing context in error messages
• Role of metrics in monitoring software performance
• Difficulty of using metrics without understanding their context and application-specific characteristics
• Difference between using metrics for debugging versus prioritizing performance issues
• Challenges of debugging in production environments, including lack of direct access to user environments and reliance on logs and metrics
• Reproducing bugs in a staging environment vs production
• Limitations of traditional debugging methods and monitoring tools
• Considerations for debugging in production, including security, privacy regulations, and performance/availability impact
• The importance of log levels in debugging, particularly in large-scale systems with high traffic
• Potential drawbacks to relying on log levels alone, including gaming the system by adjusting verbosity levels based on recent needs rather than long-term importance.
• Importance of careful logging practices as systems scale
• Approaches to debugging, including reproducing issues and examining code
• Criticism of OpenTelemetry, citing complexity and limited benefits over structured logging
• Preference for simple solutions in observability and software engineering
• Advocacy for using the standard library's testing package, citing simplicity and effectiveness
• Discussion of the testing package in Go and its limitations
• Comparison of testing package with traditional testing methods
• Use cases for the testing package and its potential applications
• Unpopular opinion on status updates in project management (via email or tracking system)
• Alternative approaches to requesting status updates from team members
• Importance of clear communication and focused questions in project management
• Comparison of status update messages to debug logs or info-level messages