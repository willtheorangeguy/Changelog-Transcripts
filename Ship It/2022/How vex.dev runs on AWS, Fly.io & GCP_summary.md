• Jason's startup Vex requires multi-cloud infrastructure due to scalability and reliability needs for video and audio streaming.
• Traditional cloud providers have limitations in scale, making it difficult to handle large audiences without latency or downtime.
• Load-balancing between cloud providers is implemented for resiliency, but a seamless failover mechanism is still being developed.
• The startup's initial focus was on building a scalable and reliable infrastructure, rather than starting with a minimum viable product (MVP).
• Simulating hundreds of thousands of simultaneous connections required testing frameworks and creative solutions to manage resource costs.
• The largest test conducted to date involved 500,000 users receiving video and audio from presenters, with constant connections lasting several minutes.
• Scaling to 500,000 simultaneous connections requires significant resources (15,000 CPUs for load testing and 1,600 CPUs for media servers)
• Google Cloud was used as the infrastructure provider and required quota system adjustments and multiple region scaling
• The platform is designed for interactive events, such as virtual conferences, trade shows, and online auctions, which require low latency and real-time communication
• WebRTC is critical for achieving low latency (under 200 milliseconds) compared to HLS (5-22 seconds)
• Bandwidth requirements are significant, with gigabits per second of traffic expected for large events, and high-resolution streams contributing to increased costs.
• Bandwidth costs for global streaming are significantly high due to latency and distance
• CDNs can help reduce latency, but may not be effective in all cases
• CPU costs are relatively low compared to bandwidth costs (95-99% ratio)
• Choosing a cloud provider is influenced by bandwidth cost considerations
• Efficient transmission of data is crucial for large-scale streaming applications
• Using WebRTC protocol and smart compression techniques can help reduce bandwidth usage
• Running own bare metal hosts can provide cleaner control over the network and lower costs
• Hybrid approach combining on-premise infrastructure with cloud providers offers flexibility and scalability
• Data privacy considerations, such as GDPR compliance, are important for companies handling sensitive information
• Concerns about data privacy when using online meeting platforms
• Discussion on the challenges of developing cross-platform video conferencing solutions
• Jason Carter's vision for Vex as a platform that provides building blocks for others to create their own applications
• Importance of providing easy-to-use tools and components for developers to integrate into their applications
• Overview of Vex's tech stack, including Elixir, Phoenix, LiveView, and Janus for media servers
• Combining Elixir and Phoenix for scalability and performance
• Evaluating Golang for high-performance tasks and potential replacement with Rust
• WebAssembly exploration for browser-based deployment of media servers and other applications
• Discussion of Rust's advantages over Go and Erlang, particularly in computationally-intensive tasks
• Jason Carter's background and interests, including technology, music, and e-biking
• Jason Carter discusses his background as a self-taught engineer and founder of Geometer, an incubator/venture studio working on WebRTC.
• He explains why he's attracted to complicated problems and learning new things, citing his experience with streaming games and video tools.
• The conversation turns to DevOps, with Carter recounting how he learned about Kubernetes through a project at Mavenlink, a startup where he worked before joining Geometer.
• Carter shares his approach to learning new technologies, emphasizing the importance of finding fun in the process and being willing to take on challenges.
• Gerhard Lazu asks Carter about Fly.io, which Carter uses in conjunction with Kubernetes for certain projects; Carter explains that they needed lower-level access to build machine images and set up firewall rules.
• Discussion of Fly.io as a platform for deploying apps and handling regionality
• Use cases for Fly.io in the company's infrastructure (e.g. load testing, media server workloads)
• Plans for exploring Fly.io's Machine API for booting machines quickly
• Comparison with container and VMs, noting that Fly.io's use of Firecracker micro VMs is "crazy quick"
• Upcoming plans for Vex.dev, including launching private alpha and expanding the platform to handle high-scale workloads
• Future development focus on stability, performance, monitoring, and scalability
• Team composition, with two co-founders (Jason Carter and Sam Pearson) and a small team of engineers from Geometer
• Plans to hire frontend developers and WebRTC experts as customers are secured
• Potential partnership with Geometer and its consulting arm
• Importance of attitude and approach in building a startup: curiosity, learning, teamwork, and joy
• Launching the Vex product and gathering feedback from users
• Adapting to changing customer needs and finding innovative solutions