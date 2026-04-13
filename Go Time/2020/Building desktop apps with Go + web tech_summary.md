• Introduction to Wails project for building desktop apps in Go
• Lea Anthony's background: coming from Node world, wanting to build visual things with Go
• Birth of Wails: combining web frontend tech (JS, HTML) with backend Go app
• Wails features: CLI tool, templates for Vue, React, Angular, and vanilla JS
• How Wails works: serving static assets, compiling down to disk directory
• Bundling assets into binary for shipping
• Pros and cons of using Wails
• Target audience for Wails: people who want power of Go with low-level stuff, USB, etc.
• Porting Wally firmware flasher application to Wails
• IPC mechanism allows for hidden communication between frontend and backend using function calls
• Go functions or struct methods are bound to JavaScript endpoints, receiving parameters and sending results back
• Type conversions and JSON messaging used for data transfer
• Limitations of Wails include complexity on native UI perspective, limited access to browser features, and potential issues with library compatibility
• Benefits of Wails include cross-platform support, ability to build one frontend for multiple architectures (Windows, macOS), and slimline resource usage
• Integrating TravisCI for continuous integration and build management
• Using GoReleaser for automating releases and uploading to GitHub
• Accessing file system operations in Wails apps
• Unified events system for communication between frontend and backend
• Debugger tooling, including creating a headless version of the backend code and setting up a web server
• Comparison of WebView limitations vs. native tools like Chrome DevTools
• Discussion of using Go library's JSON state in a frontend application for live updates
• Impact of WebAssembly on allowing languages to compile to JavaScript and run anywhere
• Comparison of Wails project with Electron, including differences in approach and resources used
• Limitations of browsers and web views, such as cross-origin resource sharing
• Discussion of keeping business logic and state in the Go side versus frontend for a more efficient and scalable application
• Wails is a tool for building desktop applications using web technologies (JavaScript, CSS, HTML) and Go.
• The Wails build process produces two types of output: a packaged desktop application with an icon, and a terminal-only app for development.
• Assets can be embedded in the Go binary, eliminating the need to package them separately.
• The Wails build command replicates some of the behavior of Packer, but also performs additional tasks such as compiling frontend assets and creating directories.
• Embedding assets is a common problem in Go, and there are several proposals for solving it, including the embed proposal.
• Wails could potentially adopt future solutions to this problem, making its internal workings transparent to users.
• Lea Anthony shares her unpopular opinion that it's sometimes okay to mix Go and JavaScript code.
• Jon Calhoun suggests that people love frameworks like Rails until they encounter issues or limitations.
• Mat Ryer discusses the trade-offs of using tools and frameworks, such as optimizing for read or write, and how Wails aims to be agnostic and flexible.
• Lea Anthony clarifies that Wails is a build tool rather than a framework, due to its lack of opinions and strict rules.
• The hosts discuss the origins and name of Wails, including its accidental association with the country Wales and its logo inspired by the Welsh flag.
• Creation of Elvish language and its development
• J.R.R. Tolkien's writing of Lord of the Rings as a way to make the language relevant
• Wails: a tool for building desktop apps with Go and web-based technologies
• Combination of Go code with documentation or teaching materials
• Potential for package management in Wails, allowing composition of applications from different components