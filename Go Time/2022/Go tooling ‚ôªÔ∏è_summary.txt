• Introduction to Go Time episode on tooling
• Jaana Dogan's return to the show after traveling for work and her upcoming new role at an undisclosed company
• Johnny Boursiquot's recent start in a new job and his experiences with the "honeymoon period"
• Discussion of the benefits and features of `go fmt` (the Go format tool)
• Etymology and pronunciation of `fmt` and "golang"
• Consistency in coding style with go fmt
• Importance of creating community culture around tooling from the start
• Benefits of early decisions on testing and prioritizing essential software engineering practices
• Differences between Golint (style errors) and Govet (lint is more about suspicious patterns)
• Value of using linter and vet tools together as part of a toolchain, including plugins and extensions in editors like VS Code and Vim.
• Benefits of using tools such as go fmt, go vet, and gometalinter (now called golangci-lint) for code quality and debugging
• Importance of running tests quickly and frequently, especially with unit tests
• Value of live feedback from the code during development, including linter messages and test results
• Advantages of using continuous integration (CI) tools to run these checks on remote servers and ensure code quality
• Fast and useful Go tools, such as go fmt, go vet, and gometalinter, that integrate well with IDEs
• Use of the race detector in go test to catch potential deadlocks and concurrency issues
• Importance of writing tests that cover concrete cases for the race detector to be effective
• Go build and run commands
• Race detector option with -race flag
• Comparison between make command and go build/run
• Go get tool for installing packages
• Module tools vs. GOPATH world
• Cross-compilation using GOOS and GOARCH flags
• Benefits of simplicity and transparency in package management
• Cross-compilation in Go and how it works
• Build tags for conditional compilation
• Intermediate assembly language used by compilers
• goimports tool for formatting code and resolving imports
• JSON-to-GO service for generating Go structures from JSON
• Go Report Card website for evaluating code quality
• GoDoc for viewing documentation and static analysis tools like Staticcheck
• Generating implementations of interfaces using a tool that takes the interface and creates a concrete implementation
• Using AST (Abstract Syntax Tree) tools from the standard library for code generation
• Performance tools and benchmarking support in Go, including pprof and go test
• Importance of benchmarking in understanding performance and making informed optimization decisions
• Risks of premature optimization and focusing on solving problems first before optimizing code
• Continuous profiling in production to identify hot paths and optimize performance
• Using pprof tools for low-overhead profiling without impacting critical paths
• Importance of identifying hot paths before optimizing code
• Difficulty with continuous profiling due to lack of built-in features in Go
• Idea of creating a tool or library for automatic continuous profiling reporting