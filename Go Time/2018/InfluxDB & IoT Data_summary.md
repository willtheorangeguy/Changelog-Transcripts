• InfluxDB is an open-source time series database written in Go
• Founded by Paul Dix in 2012 as a monitoring platform, later opened up to be used as a general-purpose database for time series data
• The company has received funding from Y Combinator and raised several rounds of venture capital
• InfluxDB is being used in various applications, including IoT sensor data collection and display on Grafana
• The database's data model is well-suited for IoT use cases due to its ability to handle large amounts of time-stamped data with tags and field sets
• Go has been a good choice for building InfluxDB due to its simplicity, fast compile times, and performance
• Paul Dix has positive experience using Go and credits it with helping him build the database efficiently.
• Concerns about using Go as a language due to garbage collector issues with large heaps
• Potential solutions included hiding data from the heap or waiting for Go team improvements to GC
• The Go team's improvements to GC have been significant, making it a viable option for large-scale applications
• Dependencies and generics were identified as two major pain points in using Go
• Code generation was mentioned as a workaround for lack of generics
• Generics were discussed as potentially being added to the language, but with concerns about complexity and readability
• Go ecosystem and standard library
• Organizing project structure in Go
• Decomposable monolith architecture
• Code organization and packaging in Go
• Kubernetes and container orchestration
• InfluxDB's hosted solution changes
• Scaling issues with single-tenant architecture
• Cluster orchestration benefits (resource efficiency, cost control)
• Moving to multi-tenanted architecture with workload isolation
• Using Kubernetes primitives to decouple storage from compute and processing
• Implementing Kubernetes operators and Istio mixers for service management
• Exploring Envoy as a proxy and service mesh for container communication
• The importance of having experience with Go for certain roles at Chronograph
• How quickly someone can learn Go and become productive within a few days
• Differentiating between basic and advanced Go skills, such as performance optimization and profiling tools
• The benefits of hiring contributors from the open-source community
• Various projects and news, including:
  • Grumble: an automatic CLI and shell tool
  • OpenFaaS: implementing serverless on top of Kubernetes
  • Alibaba's Pouch: a fast and efficient container engine competing with Docker
  • OpenCensus: an open-source framework for metrics and distributed tracing
• Discussion of OpenCensus-Go and its relation to Stackdriver
• Comparison with opentracing and potential implementation differences
• Support for Prometheus exposition format, OpenZipkin, and Azure App Insights
• Go language topics including pointers and interfaces
• Introduction to Pixel, a 2D game library in Go
• Discussion of PocketCHIP, a tiny Linux computer
• Free Software Friday segment featuring the go-multierror package
• Discussion of LXRunOffline app for creating multiple WSL installations
• Overview of Windows Subsystem for Linux (WSL) and its limitations
• Paul Dix's shoutout to Wes McKinney's Apache Arrow project
• Efficiency benefits of using zero-copy methods in data processing
• Review of Wes McKinney's blog post on the motivations behind Apache Arrow
• Shoutouts to Hybrid Group projects: GoBot, Cylon.js, R2, and GoCV
• Recap of show and upcoming episode