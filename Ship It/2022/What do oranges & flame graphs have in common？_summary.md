• Introduction to Frederik Brancic and Polar Signals
• Overview of FrostDB (formerly ArcticDB) for observability and eBPF-generated data
• Discussion of Fastly and MongoDB Atlas as sponsors
• Recap of previous episode with Parka and Erlang Perf Maps
• Updates on Polar Signals team growth and new features in software
• Discussion of Kemal Akhoyun's blog posts on symbolizing stack traces
• Position independent executables support
• ELF (Executable and Linkable Format) walkthrough
• JIT (Just-In-Time) compilation and Node example
• Importance of understanding low-level details for performance improvement
• eBPF (Extended Berkeley Packet Filter) capabilities
• Parka project mission to bundle community information into one resource
• CPU profiling for various languages, including Ruby and Python
• Erlang support and whole system profiling goals
• Parka's ease of use compared to other profiling tools like PPROF and GDB
• Importance of continuous profiling for high-performance environments
• Multiple benefits of parka, including making profiling easy and providing performance data over time
• Open-source nature of parka and its usability with Kubernetes
• New website parka.dev designed by PixelPoint and the team's enthusiasm for understanding and promoting parka
• Collaboration between two entities led to the creation of a website and influenced the design of Parka.
• The speaker noticed improvements in flame graphs after an update but found them difficult to understand.
• Easter eggs were discussed, with the speaker appreciating their inclusion in websites as a way to have fun.
• Fire Hydrant was mentioned as a reliability platform for developers, offering incident management tools and automation capabilities.
• Parka was used by the speaker's team, with a demo cluster set up at demo.parka.dev that profiles itself and its agent.
• The importance of dogfooding (using one's own product) was emphasized, with Parka being an open-source project.
• Next.js company and their use of Parka.dev website
• PolarSignals Cloud is built on Next.js and uses Parka for profiling
• Demo shows internal project, not Parka functionality
• Continuous delivery pipeline improved with Matthias' recent fixes (6 minutes from PR to dry run)
• Relationship between PolarSignals Cloud and Parka
• CI/CD setup using GitHub Actions and caching implementation
• Issues with Docker layer caching and switching to go caching instead
• Build kit caching integration with GitHub Actions cache can be slower
• Building statically linked Go binaries through GitHub Actions
• Loading the Go mod cache from previous runs and saving it if changes occur
• Continuous integration and deployment (CI/CD) pipeline with automated testing and deployment in under 6 minutes
• Preview environment for testing pull requests on production data
• Rollback mechanism for identifying and reverting unexpected changes to production
• Pira tool for managing Service Level Objectives (SLOs) and tracking error budgets
• Pira allows efficient management of error budgets and generation of Prometheus alerts
• The speaker is discussing a conversation with Matthias about Pira's capabilities and its potential for long-term use
• The orange farm visit during Polar Signals' offsite event before KubeCon EU was mentioned as a unique team-building experience
• The group learned how to eat oranges correctly, including which part of the fruit to bite into first
• The conversation turns to remote work and the shift towards it becoming the new norm
• The benefits and drawbacks of startups
• Building a healthy team and company culture through in-person time and activities
• Observability solutions for cloud-native teams, including issues with Prometheus
• Chronosphere as an observability platform
• ArcticDB: a new columnar database written in Go, used by PARCA
• ArcticDB's semi-flexible schema allows for dynamic columns, useful for label-style data.
• Polar Signals' philosophy is based on giving users flexibility in labeling infrastructure, inspired by Prometheus.
• ArcticDB handles high cardinality use cases better than Prometheus due to its design.
• The cost of storing data with high cardinality is addressed differently in ArcticDB compared to Prometheus.
• In ArcticDB, storage costs are per row, rather than per series, reducing the impact of high cardinality.
• Differences between Prometheus and Parca (ArcticDB) regarding cardinality and labels
• Excessive storage and memory usage in Prometheus due to unique combinations of labels
• How Parca avoids this issue, resulting in lower costs for storing labeled metrics
• Possibilities opened up by being able to store samples or profiles with arbitrary labels
• Ability to attach trace IDs to stack traces and retrieve related profiling data
• Potential misuse of ArcticDB if used for storing events with arbitrary labels
• Discussing using ArcticDB for storing distributed tracing data or log data
• Exploring the possibility of replacing Prometheus TSDB with ArcticDB to solve cardinality issues
• Comparing performance characteristics between ArcticDB and Prometheus TSDB
• Highlighting that ArcticDB is optimized for events/tagged data, whereas Prometheus is designed for metrics
• Describing a use case where high cardinality data needs to be searched by label-based system
• Arctic DB is embedded and has implications for clustering processes
• The speaker is aware of the importance of open-sourcing Arctic DB but prioritizes making money with Polar Signals Cloud
• Open-sourcing Arctic DB may happen in the future, potentially to the open source community
• There are shoutouts given to individuals who have contributed to Arctic DB
• Experience of a person mentioned
• Collaboration on Arctic DB
• Tyler's involvement in building a new database
• Mechanisms for isolation and consistency
• InfluxDB and its similarity to the project
• Paul Dix, Andrew Lam, and their work on InfluxDB
• The speaker mentions InfluxDB's next-generation columnar database, Iox
• InfluxDB is building on top of Apache Arrow and Parquet
• The speaker praises the generosity of InfluxDB in sharing their experience
• The importance of great teams, products, and open-source projects is discussed
• Examples are given of how people come together to create something amazing
• A conversation about Ashill, an incredible engineer who worked on the Parquet Go library
• Discussion of collaboration between the speaker and Ashill on the library
• Mention of the library's performance and APIs being thoughtfully designed
• Shout out to Ashill for his work on the library
• Introduction to Polar Signals Cloud, a hosted service similar to SAS models
• Explanation of the benefits of continuous profiling using Polar Signals Cloud
• Polar Signals Cloud is a product that allows automatic profiling of entire infrastructure with minimal setup required
• The product involves deploying the parka agent on a Kubernetes cluster, which then connects to Polar Signals Cloud for profiling
• The feature is still in beta and not yet generally available, but interested parties can sign up on the company's website for further information
• The speaker appreciates the simplicity of using the product and compares it favorably to other setup experiences with tools like Prometheus and Grafana
• The product has undergone development and refinement over time, with the speaker expressing enthusiasm for its evolution.
• The speaker has been following the company's progress and is impressed by their achievements, including shipping Arctic DB.
• The company has grown from a small team to a product to a company, and it's been exciting to watch them succeed.
• The key takeaway for the audience should be about people, Arctic DB, and the company's mission for the year.
• The company plans to make the polar signals cloud generally available and accessible to anyone who wants to use it.
• They want to ensure that the data collected by the product is trusted and reliable before making it widely available.
• After general availability, they plan to explore building things on top of continuous profiling, including exciting applications for the collected data.
• Checking in on company growth every 6 months
• Importance of community and leveraging one's network
• Power of sharing your network with others
• Limitations of time, attention, and mind share
• Gratitude for connections made through podcasting
• Takeaways from the first year of the podcast
• Blog posts
• Slides
• Seeking input on ideas for content creation