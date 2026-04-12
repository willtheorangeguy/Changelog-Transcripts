• Discussion of a survey on Go usage and dependency management
• Ed Muller's role in creating the survey and his observations on the responses so far (2,400+)
• Comparison and ranking of various Go dependency managers (Godep, Govendor, GB, Glide)
• Historical context for Godep's dominance in dependency management
• The challenges of solving the problem of vendor directories and metadata standards
• The Go Team's approach to dependency management and their desire for community input and solutions
• The Go community is frustrated with the lack of a standardized solution for dependency management and repeatable builds.
• Some newer programming languages (e.g. Nim, Rust, Crystal) have built-in solutions to these problems that are considered more effective than what Go has to offer.
• The Go Team's stance on this issue is that it's not their responsibility to solve it, but rather the community's.
• Ed Muller suggests that instead of creating new tools for dependency management, people should read existing codebases, submit PRs, and fix problems.
• Some of the issues that still need to be figured out include actual upgrade and version management of dependencies, specifying constraints on versions for libraries, and implementing semantic versioning.
• Semantic versioning issues in Go libraries and lack of adoption
• Difficulty in tracking changes to dependencies due to missing or inconsistent version tags
• Social contract of semantic versioning vs. technical implementation
• Importance of tools for checking API compatibility and detecting breaking changes
• Comparison with other languages that have addressed dependency management from the start
• Go's support on Heroku, including formal support for Go applications and documentation in dev center
• Growth of Go adoption on Heroku, particularly among API service developers
• Heroku customers are increasingly using Go in conjunction with other languages
• Large portions of the Heroku platform have been rewritten in Go, including Git server, log router, private spaces, API work, and system metrics
• Ed Muller estimates that 60-40% of the rewritten code is new development vs. rewriting existing code
• Doozer, a distributed coordination system written in Go, was used by Adobe and Bit.ly among others but is no longer widely used
• The Paxos implementation in Doozer was done by Blake Mizerany and Keith Rarick
• Discussion about a legacy Go project from 2011-2012 and its idiomatic code
• Heroku CLI tool is now 98% Node, with some remaining Go and Ruby code being phased out
• Damian's contributions to the Go community, including answering questions on Reddit and GoTime FM
• SourceGraph Editor plugin for Vim/Sublime/Atom, which provides real-time code analysis and examples
• Discussion about SourceGraph company and its open-source projects
• Cross-platform GUI type approaches in Go
• Gob project for writing a full web browser in Go
• CEF (Chrome Embedded Framework) as an alternative
• Shiny library used by Gob for UI components
• Gogs self-hosted Git service and its documentation
• Heroku's open source Go projects
• go get button Chrome extension for easy package management
• Pachyderm project for data science with Go
• Discussion about a tool that allows data pipelines to be piped through containers
• Mention of Visual Studio Code as an editor for Go development with praise for its features and tight integration with Delve debugger
• Shoutout to Luke Hoban and the Microsoft team for creating the Visual Studio Code plugin
• Comparison between Vim Go and Visual Studio Code, noting that VS Code is "significantly prettier"
• Mention of Go Doc Tool (also known as Pythia) which jumps to code source definition
• Discussion about Apache Kafka as a distributed message queue and publish-subscribe system
• Heroku's support for the Go world and their contributions to open-source projects
• Upcoming events, including the Women Who Go first birthday party in San Francisco and the next episode of GoTime FM with Jessie Frazelle and Beyang Liu
• Discussion of the podcast format and interaction with listeners
• Expression of gratitude to guest speaker Ed Muller for appearing on the show 
• Wrap-up and goodbyes from all participants