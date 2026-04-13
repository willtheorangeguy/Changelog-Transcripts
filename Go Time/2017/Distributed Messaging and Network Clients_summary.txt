• Wally Quevedo introduction and background
• Overview of NATS project and its use cases
• Purpose behind NATS in Cloud Foundry control plane
• Resilience of NATS and why it's hard to crash
• Transition from Ruby to Go implementation of NATS
• Reasons for choosing Go, including performance and concurrency benefits
• NATS is a high-performance messaging system that can be used for pub-sub, request-response, and RPC patterns
• NATS has a "fire-and-forget" model, where messages are not persisted if clients are offline when they're received
• NATS Streaming provides persistence and message redelivery capabilities, similar to Apache Kafka
• The cost of durability in NATS Streaming is lower performance compared to regular NATS
• NATS is highly flexible and can be used as a transport layer for microservices with libraries like Go Micro
• There are numerous client implementations for various programming languages, including JavaScript, C#, Python, and more
• Apcera uses NATS heavily in their own infrastructure, particularly in the control plane and service discovery.
• NATS as a messaging system for low-latency communications
• Benefits of using NATS (simple deployment, lower collective overhead)
• Alternatives to NATS and when it's a good choice to use it
• Performance improvements with new Go releases and NATS
• Wally Quevedo's upcoming talk at GopherCon on Writing Network Clients In Go
• Apcera's community-oriented culture and involvement in the Go community
• Issue with MacOS 10.12.4 update breaking cgo-enabled binaries in Go
• Call for proposals for Golang UK conference
• GopherCon workshops announced
• Go ERD tool for generating Entity Relationship Diagrams
• Vim-Go 1.12 released
• Emacs vs Vim discussion, including Wally Quevedo's use of Emacs and Domink Honnef's Go-mode
• Discussion of NATS project, its evolution, and Wally Quevedo's involvement
• Mention of a blog post by Nate Finch on his experience with Canonical and 500,000 lines of Go code
• The speakers discuss how Go and its ecosystem have evolved over the past four years
• They reminisce about the early days of Go when vendoring was not a concern and there were no external packages
• Brian Ketelsen talks about his daughter's slime-making hobby and compares it to Oobleck
• The discussion turns to #FreeSoftwareFriday, where they promote open-source projects, including Brian's work on Go Micro for microservices
• They also discuss the increasing adoption of gRPC in communication protocols, including its use in Etcd and Kubernetes
• The speakers briefly touch on NATS' plaintext protocol and their editors' preferences (VS Code vs Vim)
• Carlisia has issues with Vim plugins not functioning correctly
• Brian suggests trying different Vim plugins to resolve the issue
• Wally recommends a Go utility called GHR for releasing NATS artifacts
• Erik gives a shoutout to Kubernetes maintainers for their work on recent releases
• The group discusses KubeCon in Berlin and related projects