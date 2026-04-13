• Introduction of guest Filippo Valsorda from CloudFlare
• Discussion of hellogopher project to simplify Go development for non-Go developers
• Problems with GOPATH: confusion around cloning repositories, contributing code
• Success story of using hellogopher at CloudFlare to streamline development process
• Guests' experiences with setting up Go environments and vendoring
• Discussion on the limitations of the new default GOPATH feature in Go 1.8
• Custom GOPATH setup and compatibility with existing tools
• Vending tool agnosticism and compatible vendor management
• Whoami SSH server demo, using public keys to gather user information
• Discussion of potential information leakage via SSH authentication
• Filippo Valsorda's work on TLS 1.3 implementation in Go and its deployment on CloudFlare sites
• CloudFlare uses a mix of NGINX and Go for reverse proxying, but the Go stack can take over connections with TLS 1.3 enabled.
• The crypto/tls package in Go is considered to have a better security track record than OpenSSL, but it's less battle-tested and may be slower or more CPU-intensive.
• TLS 1.3 offers improved robustness by removing unnecessary features and one less round trip for connection establishment compared to TLS 1.2.
• Filippo Valsorda works on the Crypto team at CloudFlare and has given talks about Go, cgo, and TLS 1.3, including a talk at 33c3 and blog posts on Gopher Academy Advent list.
• Discussion of Go binaries being reproducible
• Introduction of a side project by Filippo Valsorda on binary transparency and reproducibility
• Explanation of CT (Certificate Transparency) and its application to build servers
• Mention of Debian's struggle with reproducible builds
• Details on the importance of latency profiling in Go
• Discussion of latency vs throughput optimization in Go garbage collection
• Plans for Filippo Valsorda to present on latency profiling at GopherCon India
• Discussion about Filippo Valsorda's keynote at GoLab and its recording
• Introduction of new project Gopherize and its features
• Request for a GoTime logo T-shirt design
• Explanation of the codebase behind Gopherize and its connection to Google's Turkey Doodle
• Mention of chromedp, a tool that uses the Chrome debugging protocol to steer browsers
• Discussion about Camlistore content-addressed storage
• Introduction of pre-alpha dep tool and GPS library
• Plans to have Sam Boyer on the show to discuss the dep tool and its features
• Makefiles and GNU make
• PHONY declarations in makefiles
• Using PHONY to manage dependencies
• Gopher avatars and online culture
• Out Of The Loop Subreddit
• Kubernetes plugin called Mate
• Sourcegraph code navigation tool in general availability for Go language
• Sourcegraph features for clicking to definitions in open-source code
• Play With Docker: a project allowing embedded Docker terminals in the browser
• #FreeSoftwareFriday: shoutouts to open-source projects and maintainers making life easier, including:
  • Ponzu CMS and Buffalo website combination
  • Static Check by Dominik Honnef
  • ZIM by Matt Hamilton
• Discussion of Zsh shell and its features compared to Bash
• Release announcements for Go 1.7.5 and Go 1.8rc3
• Preview of upcoming changes in Go 1.9 and discussion of Go 2.0 proposals
• Mention of a possible JVM backend for Go
• Brief history of the Go cross-compiler and gccgo
• Embarrassing moments from past GopherCon events