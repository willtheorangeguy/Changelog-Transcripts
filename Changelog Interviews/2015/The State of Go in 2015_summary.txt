• Introduction to episode 148 of The Change Log podcast
• Andrew Duran, a Go programming language developer at Google, joins the show
• Discussion of the state of Go in 2015
• Introduction of a new feature called Parallel CI by Codeship
• Benefits of Parallel CI, including faster tests and deployment
• Promotion of Codeship's free plan and a 20% discount for listeners
• Background on Google Sydney and its role in the development of Google Maps
• Andrew Duran's experience working on the Go team at Google
• Early days of the Go programming language and its release in 2009
• The Change Log podcast's third episode, which covered Go early on
• Audio quality improvement over time
• Nostalgia for early podcasting days
• Discussion of starting a new podcast
• Interviewing people in the Go community
• Mention of a past episode and a past talk at FOSDEM
• Description of FOSDEM conference and its dev rooms
• Curation of dev rooms and their shift in emphasis
• Go dev room organization and its community-driven nature
• FOSDEM's spirit of the open source community
• Linking to FOSDEM dev room talks in the weekly email
• Recording and release schedule for the podcast
• Lightning talks at conferences, allowing attendees to share small projects
• Comparison of Go's concurrency features to Erlang and Elixir's concurrency model
• Go's concurrency model is based on the use of goroutines and channels, but is not baked into the language
• Erlang and Elixir have a built-in framework for managing concurrent processes and passing messages between them
• Go's imperative programming model and process-based execution model are distinct from Erlang and Elixir's concurrency features
• The choice of language for concurrent applications depends on the specific needs and requirements of the project.
• The choices a programmer makes when building an application, including language selection
• Reasons why someone might choose Go over other languages
• Go's "developer joy" and how it gets out of the way and lets programmers write simple code
• The benefits of keeping the tool chain and language in a programmer's head, and how this relates to Go's design philosophy
• The c2go tool chain conversion and how it relates to Go's ability to keep things small and simple
• The challenges and benefits of converting from C to Go
• The original Go compiler was written in C by Ken Thompson
• The codebase was not easily accessible due to Ken's unique coding style
• The decision was made to convert the toolchain to Go to make it more accessible and maintainable
• Russ Cox wrote a program to convert the C sources to Go
• The resulting Go compiler is currently slower than the C version due to inefficiencies in Go
• Work is being done to tidy up the Go code and make it more idiomatic
• Issues arose due to differences in coding style and language features between C and Go
• Discussion of Russ's overhaul of the Go compiler
• Need for the compiler to be more accessible to more people
• Concurrent garbage collector being developed for Go 1.5
• Differences between the concurrent collector and the existing garbage collector in Go 1.4
• Benefits of the concurrent collector, including predictable pause times and improved performance for interactive applications
• Plans for HTTP2 server support, likely in Go 1.6 rather than 1.5
• Active development of HTTP2 server support in a separate repo
• HTTP2 support in Chrome and Firefox
• Brad Fitzpatrick's HTTP2 implementation on GitHub
• HTTP2 adoption and benefits, especially on high-latency connections
• HTTP2 demo site and comparison with HTTP
• State of mobile development with Go: current limitations and future plans for Android and iOS support
• Go mobile toolkit and toolchain for easier mobile development
• Transition to get from Google Code
• Digital Ocean cloud hosting provider
• Complexity of toolkits for Android and iOS development
• Google Code's shutdown and automated migration tool to GitHub
• Pros and cons of transitioning to get
• Google's reasons for shutting down Google Code
• Switching from Google Code to GitHub for hosting open source projects
• The importance of a well-supported code review system for large teams
• The choice to use Git over Mercurial due to Google's support for Git
• The role of Garrett in the code review process and its advantages over GitHub's pull request system
• The inefficiencies in GitHub's code review process for large teams and projects
• Discussion of using Garrett for code review vs GitHub's pull request process
• Importance of Contributor License Agreements (CLAs) and electronic signature
• Use of Google bot to check CLAs for pull requests on GitHub
• Preference for a GitHub workflow that integrates CLAs and reduces confusion
• Suggestion to surface contributing files on GitHub more prominently
• Frustration with contributors sending pull requests when not accepted
• Discussion of clarifying disclaimers on GitHub regarding pull requests
• Open source software development and GitHub's role in it
• Dependence on large organizations and the importance of self-reliance in open source
• Git vs. GitHub, and the misconception that GitHub equals open source
• Go 1.5 release and its support for new architectures (PowerPC 64 and ARM 64)
• Potential uses and applications of Go on various platforms, including mobile devices and servers
• Introduction to Go Mode and Google Compute Engine
• Existing builder infrastructure limitations and maintenance issues
• New builder infrastructure using Compute Engine and Go Mode
• Deterministic build environment and parallel build capabilities
• Speculative builds and tri-bot testing
• Go Mode tool for developers to test changes on various architectures
• Future plans for Go, including improvements to the language and ecosystem
• Go Kit project for building a standard for building Go applications
• Go Kit is a toolkit for building distributed systems in Go, aiming to provide a set of recommendations and libraries for a well-integrated developer experience.
• The goal of Go Kit is to address the challenges of building distributed systems in Go, particularly for medium-sized companies (the "modern enterprise").
• Go Kit's project is led by Peter Bourgon, and the community is actively working on developing the project and its ecosystem.
• Contributing to the Go project involves solving problems that matter to you and sharing your solutions, which can include learning Go, contributing code, or supporting the community.
• The current needs in the Go community include contributions to Go Kit, as well as other areas such as API stability policies and package management.
• Sigourney, an audio synthesizer project, is being neglected due to lack of time and space
• The speaker wants to learn about digital signal processing and create a portable audio synthesizer
• Sigourney is similar to Max MSP or Pure Data, but uses a physical modular synthesizer with patch cables
• The speaker thinks the project is similar to Kievl (a digital audio workstation) and mentions the electronic music making industry
• The speaker discusses their interests in audio hardware and software, and would work on Sigourney if they had the time and space
• The speaker recommends the Beats, Rye, and Types podcast, and discusses their own potential podcast idea
• The speaker mentions their screencasts with Brad Fitzpatrick, called Hacking with Andrew and Brad