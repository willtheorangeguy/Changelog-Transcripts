• Influx Data's new cloud dedicated service allows for single-tenant instances of the database
• The service runs on K3S, with each tenant having its own Kubernetes cluster and instance of InfluxDB v3
• Lili Cosic discusses her experience joining Influx and learning about their architecture and technology stack
• She highlights the benefits of using InfluxDB v3, including high cardinality support and customizability
• The discussion touches on the switch from Go to Rust as part of the database's rewrite, and its advantages in terms of performance and efficiency
• Lili Cosic's background with Rust programming and troubleshooting Containerd issues
• Comparison between Prometheus and Influx as time-series databases
• Key differences between the two:
  • Prometheus is more specialized for specific time-series metrics format
  • Influx is more general-purpose and flexible
  • Prometheus has a write-ahead log, while Influx does not
• Use cases for each database:
  • Prometheus: primarily for measuring data at regular intervals, suitable for alerting and rule evaluation
  • Influx: suited for long-term storage of metrics and can handle large volumes of data efficiently
• Immutable nature of Prometheus data and its implications for auditing and deletion
• Experience with the TICC stack (Telegraph, Influx, Chronograph, Graphite, Capacitor) and its integration into Influx V2
• Puppet infrastructure issues caused by excessive database connections
• MongoDB security concerns due to default password-less setup
• Specialized databases vs general-purpose ones like Postgres
• The importance of expert help and support for databases
• Experience with Prometheus, OpenShift, and Kubernetes operators
• Acquisitions in the industry, including Red Hat's sale to IBM and CoreOS's impact on OpenShift
• Kubernetes operators and custom resource definitions (CRDs)
• History of CRDs and their shift from third-party resources
• Origin of the term "operator" and its misuse by some companies
• Discussion of databases, including CockroachDB and TigerBeetle
• Lili Cosic's career path and her experiences at various companies, including Red Hat and HashiCorp
• Open source challenges in management and responsibility
• Comparison between Red Hat and HashiCorp approaches to open source development
• Difficulty of integrating open source projects into a business framework
• Balancing company stakeholders with open source maintainers' needs
• Managing people who want to build on top of open source projects vs. those who just use them
• Strategies for growing a career in complex spaces like databases and infrastructure without burning out
• The challenges of open source development, including the lack of boundaries and expectation of immediate response
• The impact of corporate funding on open source projects and the influence it has on decision-making
• The shift towards more restrictive licensing in open source, allowing companies to protect their investments
• The role of foundations, such as the CNCF and Linux Foundation, in governing open source projects and creating a neutral ground for collaboration
• The politics involved in open source development, including pay-to-play models and the influence of large corporations on project direction
• The importance of community involvement and welcoming culture in successful open source projects
• Discussion of social media presence (Lili Cosic on Twitter as @lilicosic)
• Lili Cosic discusses her career and work with Influx
• Guest leaves the show