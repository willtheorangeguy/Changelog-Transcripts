• Discussion on Tom's past appearance on the podcast (Changelog episode 375) and how much has changed since then
• Introduction to new tools and features: Loki, Tempo, and Grafana Agent with Prometheus and Grafana Cloud
• Explanation of Cortex architecture and its role in offering a generous free tier for Grafana Cloud
• Discussion on Tom's previous appearance at KubeCon 2019 North America and how the industry has evolved since then
• Overview of new features and updates: Tempo, Loki 2.0 with improved query language, and linking metrics and logs with traces
• Discussion of the impact of the global pandemic on Grafana Labs
• Mention of the scalability and remote-first nature of Grafana Labs
• Reference to a keynote speech on observability and its vision for the future
• Description of the development and benefits of Loki, a Grafana project
• Discussion of Grafana Cloud and its hosted managed service features
• Explanation of unified alerting in Grafana and its combination of Prometheus system features
• Mention of the importance of cloud architecture and multi-tenancy in offering a free tier
• Description of the horizontally scalable, multi-tenant version of Cortex
• Discussion about the cost-saving statistical multiplexing techniques used in Loki and Tempo
• Consistency across offerings due to shared architecture and techniques
• Background of VP of product explaining their coding expertise
• Experience with open-source codebases, including Zen hypervisor project and Prometheus/Cortex development
• Mention of Grafana Cloud features, including Metric Tank and future plans for Graphite V5
• Connection between Acuna Analytics (former company) and GoSquared (previous startup)
• Discussion about past experiences with analytics and monitoring systems (GoSquared, MongoDB, Cassandra, Graphite)
• Comparison of scalability and limitations of various systems (Graphite, Prometheus, Cortex)
• Mention of Acuna's contribution to the Cassandra project (virtual nodes technique)
• Connection between Cassandra/Graphite and modern systems (Cortex, Loki, Tempo)
• Reflection on the evolution of analytics and monitoring technology
• Debate about the definition of observability and its relationship to metrics, logs, and traces
• Discussion of the importance of curiosity and understanding system behavior for observability
• Grafana Labs avoids one-size-fits-all solutions and instead supports multiple tools and combinations to help users get the best results
• The goal is to bring together different teams' tools into a single place with a unified experience
• The ideal tool helps users access data and test hypotheses, rather than providing automation or root cause analysis
• Situationally-appropriate tool selection depends on the problem and available tools
• The speaker mentions a colleague named Manu who was previously involved with the Phoenix app and is now at a cryptocurrency company.
• The speaker explains that the Phoenix app is monolithic, meaning it's not broken down into microservices, and has a specific architecture involving a CDN, load balancer, Ingress Nginx, and a database.
• The speaker discusses the importance of instrumenting the system to collect metrics and troubleshoot slow requests.
• The speaker mentions using Prometheus and exporters to collect metrics from various components of the system.
• The speaker explores integrating Fastly logs with Grafana Cloud but notes that there is no native integration and that a proxy would be required to forward logs.
• The speaker discusses how Loki in Grafana Cloud can process log data into usable metrics, such as request rates, error rates, and latencies.
• Deploying Promptail as a daemon set and sending logs to Loki
• Instrumenting application code with Prometheus client library
• Collecting metrics from database (e.g. MySQL) using exporter
• Organizing dashboards in a consistent format (e.g. request rates, error rates, latency)
• Using mixin packaging format for distributing dashboards and alerts
• Referencing Cortex or Kubernetes mixins as examples
• Challenges in using JSON for changelogs due to version differences between languages (e.g. Go, Python, JavaScript)
• Introduction of mixins as an advanced feature for packaging and redistributing software components
• Advantages of JSON it bundler tools (MixTool, Grizzly, Tanker) for managing complex configurations
• Use of a single repository for config management in Grafana Cloud with Kubernetes clusters
• Managing Kubernetes jobs using JSON it
• Discussion of the vision for delivering dashboards, alerts, and applications as a single package
• Criticism that this approach is too hard to use and may not be suitable for most people
• Introduction of a more opinionated and integrated version of JSON it in Grafana Cloud
• Simplification of configuration through the Grafana agent and its integration with various exporters.
• JSON it bundler
• Grafana agent vs Prometheus operator
• Challenges with dashboard integration in Grafana
• Best practices for building dashboards:
  • Templating data sources and job/instance labels
  • Using templates to dynamically discover jobs/metrics
  • Adding info metrics to software
  • Building dashboards as code using libraries (Grafana, Grafana Builder, Grafana Lib)
  • Version controlling dashboards from the start
  • Implementing GitOps style approach with tools like Grizzly
• Discussing the use of Grafana with a JSON definition of a dashboard
• Implementing dev deploy cycle on a laptop for developing dashboards and uploading them to Grafana
• Version controlling source code instead of JSON files for reviewability and collaboration
• The 80/20 rule for Grafana usage, where 80% is easy-to-use editing and 20% is advanced SRE/DevOps approach
• Pair programming an hour-long YouTube stream to capture the advanced approach
• Discussing VS Code Sharing and Rufana Cloud/Rufana Agent integration
• Importance of capturing and sharing the advanced approach for others to learn from it
• Barriers to entry for tracing vs logs
• Challenges in the tracing space due to high investment and instrumentation requirements
• Benefits of tracing, particularly in performance challenges
• Open Telemetry and its tracing stack
• Auto-instrumentation in various languages (e.g. Java, Python)
• Distributed tracing and blind spots in instrumented stacks
• Tracing in load balancers and CDNs (e.g. AWS ELBs, Fastly)
• Distributed tracing and spans in software applications
• Instrumenting Elixir server and client for better understanding of request flow
• Challenges in getting complete traces from all services and the effort-reward trade-off
• Focusing on key hops in the application stack (e.g. Ingress Nginx, Kubernetes service, application)
• Potential limitations of adding spans to certain layers (e.g. load balancer, TCP level)
• Using OpenTelemetry for vendor-neutral tracing standards and potential for adding spans to open-source projects
• Creating Grafana dashboards for visualization of request flow and exploring different tools and version control systems
• Iterating on solving specific observability problems
• Long-term value of integrating tempo and other tools
• Ecosystem maturity and changing tooling landscape
• Big tent philosophy in observability and data sources
• Grafana Labs' mission to support multiple tooling choices
• Origin of the term "big tent" and its application in Grafana