• Qi Xiao developed a shell called Elvish in Go programming language
• Elvish has been in development for 11 years, with on and off contributions from Qi Xiao
• The project started as a personal experiment to create a more capable and interactive shell
• Qi Xiao uses Elvish as his default terminal shell, consuming his own "dog food"
• A shell is described as both a programming language and an execution environment
• It can be thought of as another terminal application, but with the unique ability to launch other applications
• The distinction between a shell and a terminal is discussed, with Qi Xiao explaining that a shell is more like a program in your environment, rather than just another application.
• The speakers discuss their transition from graphical user interfaces (GUIs) to command-line interfaces (CLI) and the benefits of using a CLI for tasks such as video processing.
• Qi Xiao explains why he chose Go as the programming language for his shell project Elvish, citing its modernity, expressiveness, and speed compared to other languages available at the time.
• The conversation touches on the evolution of Go's niche within the programming language landscape, from a systems programming language to a cloud-focused language.
• Qi Xiao discusses the role of Go in allowing Elvish to run on multiple platforms with a single binary, and how he had to write platform-dependent code for handling keyboard events in terminals.
• The speakers highlight the abstraction provided by Go's os/exec package, which simplifies launching external programs across different operating systems.
• Portable shell with platform-dependent features
• Elvish has real programming features and UI features out of the box
• Features include lists and maps that can be nested, lambdas, and functional programming
• Built-in file manager and command history search
• Rely on external commands for tasks like running Git
• Built-in commands geared towards programming tasks and designed to work with portability in mind
• Support for Windows in addition to Unix environments
• Development of Elvish programming language
• String manipulation and file handling features
• Comparison between Bash and Elvish scripting languages
• Use of Go's standard library and runtime features in Elvish development
• Garbage collection in Elvish and its relationship with the underlying Go runtime
• Decision-making process for choosing a programming language
• Importance of selecting the right tool (language) for the job
• Discussion on limitations of the Go programming language for library implementation
• Examples of Go's lack of true enums and tagged unions hindering clean API design
• Development status of Elvish, including new TUI framework and integration with main branch
• Future plans for Elvish to integrate shell and terminal into a single application
• Critique of relying on LLMs for command generation in Elvish
• Unpopular opinion on 100% code coverage as the minimum goal for testing, not an end goal
• Importance of end-to-end test coverage in code development
• Limitations of language models (LLMs) in large-scale legacy system maintenance and refactoring
• Need for human context and understanding in LLM-driven code changes
• Potential role of TDD in generating tests with the help of LLMs
• Trade-off between writing tests first or later, and the potential for LLMs to generate tests