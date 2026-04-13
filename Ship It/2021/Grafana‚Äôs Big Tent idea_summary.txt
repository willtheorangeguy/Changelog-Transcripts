• Launch of Tempo, a tracing system from Grafana Labs
• Loki 2.0 with improved query language and pipeline operator for filtering logs
• Collaboration between Grafana Labs and Prometheus team on LogQL design
• Development of exemplars in Prometheus and Grafana to link metrics and traces
• Prediction of observability future in KubeCon 2019 keynote and subsequent development
• Launch of GEM (Grafana Enterprise Metrics) and growth of Grafana Labs to over 400 employees
• Impact of global pandemic on Grafana Labs, which was set up as remote-first organization
• Unified alerting system in Grafana, combining features from Prometheus and Grafana alerting systems
• Launch of generous free tier for Grafana Cloud
• The speaker discusses how Cortex is a horizontally-scalable, multi-tenant version of Prometheus that allows for free provisioning and reduced costs.
• Cortex's architecture has been replicated in Loki and Tempo, providing consistency across offerings and reducing operational burden.
• The speaker's background as a software engineer and his involvement in the creation of Cortex are discussed.
• Grafana Cloud is mentioned as having a time-series database called Metrictank, which was later replaced with Cortex-style architecture.
• Acunu Analytics' contribution to Cassandra through virtual nodes is highlighted as an example of innovation in distributed systems.
• The connection between Graphite and Prometheus/Cortex is noted, with similarities between the scaling challenges faced by these projects.
• Definition of observability discussed
• Critique of traditional "three pillars" definition of observability (metrics, logs, traces)
• Importance of curiosity and interest in understanding system behavior for observability
• Discussion of Grafana Labs' approach to observability as a big tent philosophy that supports multiple solutions and techniques
• Tom Wilkie's preference for defining observability as helping engineers understand their applications and infrastructure through various tools and data sources
• Example of using Grafana to solve a specific problem (slow requests) in a monolithic application
• Discussion on Phoenix app architecture, including its monolithic structure and request flow
• Troubleshooting slow requests using Grafana ecosystem tools, specifically CloudWatch exporter and Prometheus
• Integrating Fastly logs with Grafana Cloud/Loki, including validation issues and proxy requirements
• Instrumenting the system for metrics and logs, including CDN, load balancer, Ingress NGINX, and application code
• Using Loki to extract metrics from logs and create dashboards
• Applying Tom's "RED" method (request rate, error rate, request duration) to instrument applications
• Creating a top-to-bottom dashboard layout for system performance analysis
• Mixins as a packaging format for Grafana dashboards and Prometheus alerts
• Overview of popular mixins, including Cortex, Kubernetes, and Etcd
• Use of mixins to simplify dashboard management and reduce cognitive load
• Jsonnet language used to express alerts and dashboards in mixin format
• Mixin tooling and ecosystem (e.g. mix tool, Grizzly, Tanker)
• Monorepo approach with single repo for config management across multiple Kubernetes clusters
• Use of Jsonnet for managing all aspects of deployment, including Kubernetes jobs and configuration
• Vision of end-to-end integration through a single language and tooling (Jsonnet)
• Kubernetes integration with Docker monitoring
• Using Grafana Agent for metric and log collection
• Difficulty in integrating dashboards with PromEx library
• Template-based dashboard approach with data source templating
• Building dashboards as code using Jsonnet or Grafonnet
• GitOps-style approach to managing dashboards with tools like Grizzly
• Collaboration on a YouTube stream to explore building dashboards as code
• Discussion of using Grafana Cloud and Grafana Agent for metrics and logs
• Overview of Tempo as a tracing component and its integration with Grafana Cloud
• Challenges of implementing tracing, including high barrier to entry and lack of incremental rewards
• Importance of traces in understanding performance issues and identifying slow requests
• Explanation of OpenTelemetry as a cross-functional project simplifying telemetry data collection
• Discussion of auto-instrumentation for languages such as Java, Python, and Go
• Problems with distributed tracing, including holes in instrumentation and black blind spots
• Need for entire stack to be instrumented to get full value from tracing
• Future possibilities for improved tracing capabilities through OpenTelemetry and W3C Trace Context
• Instrumenting spans for distributed tracing
• Determining the optimal places to instrument spans in a complex system (e.g. Ingress NGINX, Kubernetes)
• Effort vs reward trade-off in getting complete traces from every service
• Using OpenTelemetry to get vendor-neutral and open-source support for span instrumentation
• Integrating with Grafana dashboards and tools for version control and iteration
• Big tent philosophy approach to observability tooling (supporting multiple systems and vendors)
• Integration of systems in new ways
• Supporting multiple query languages within a single database (e.g. Tempo)
• OpenTelemetry's vendor-neutral approach
• Conversation discussion and exchange of interest between Tom and Gerhard