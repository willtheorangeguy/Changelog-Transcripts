• Common use cases of Go include back-end systems, queueing technologies, databases, high throughput networked applications and services
• Uncommon uses of Go include running user interfaces using native rendering through web browsers, using JavaScript in Go (e.g. GopherJS, Vecty)
• WebAssembly has potential to be cool in the future and projects like GopherJS have helped pave the way for it
• Developers are experimenting with new ways to use Go, including generating JavaScript from Go, which can be seen as a fun thought experiment or a way to push boundaries of what's possible
• Challenges of creating production-grade graphical user interfaces (GUIs) in Go
• Cross-platform GUI development: possibility and feasibility
• Trade-offs between cross-platform consistency and system-specific functionality
• Fyne project goals and design choices for a standard user interface across platforms
• System-by-system integration challenges, particularly with dialogs and file saving capabilities
• Differences in operating system consistency and how to handle them
• Benefits and challenges of using build tags and platform-specific code in cross-platform development
• Importance of consistent APIs for developers working on cross-platform projects
• Fyne's approach to providing a consistent API across mobile and desktop platforms
• Performance benefits of using Go for GUI development, particularly compared to JavaScript-based solutions
• Challenges of accessing low-level OS-specific APIs from higher-level languages like Go
• Complexity under the hood due to multiple languages and platforms
• Use of C bindings and CGO to interact with system libraries (e.g. OpenGL)
• Difficulty accessing platform-specific APIs on mobile devices
• Importance of designing an API for end-users rather than developers
• Different approaches to graphics programming (low-level vs high-level abstraction)
• Challenges in rendering graphical user interfaces across platforms
• Difficulty of creating game engines for Go and cross-platform development
• Limited visibility into usage patterns and feedback from the community
• Trade-offs between consistency and flexibility in API design
• Design decisions and considerations behind the project's architecture and features
• Lessons learned and potential changes to the design process with hindsight
• Roadmap for development of GUI toolkit Fyne
• Balancing feature development with ensuring API consistency across platforms
• Data binding system design process and its impact on the project timeline
• Writing a book on GUI application development in Go and its advantages
• Comparison of Go's suitability for GUI development compared to other languages (e.g. JavaScript)
• Overview of various GUI toolkits in Go, including Fyne, andlabs UI, and others
• Development of cross-platform GUI libraries for Go
• Comparison between Fyne, Shiny, Qt, Wails, Walk, and other tools
• Discussion on the trade-offs between opinionated vs. flexible toolkits
• Use cases for GUI development in Go, including command-line to graphical interfaces
• State of modern cloud-based technologies and their integration with native apps
• Suggestions for getting started with GUI development in Go
• The Fyne project allows users to quickly build graphical applications in Go.
• A gentle learning curve is important for new developers, but also need to consider preconceptions about GUI frameworks.
• Non-traditional avenues of adoption are expected as many new developers join the Go community.
• Quality and a well-engineered approach should take priority over speed of development.
• The size of the team affects what can be gotten away with in terms of code quality.
• Abrupt deprecation of APIs without a realistic migration strategy
• Importance of considering team size and code review when designing projects
• Value of pretending the internet is reviewing your code to keep yourself honest
• Unpredictability and potential criticism from online communities, even with perfect code