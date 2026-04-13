• Telemetry is the collection and storage of data from remote sensors or machines, used for monitoring performance, scalability, and security
• Common use cases include identifying bottlenecks, troubleshooting issues, and improving application performance
• Best practice is to implement telemetry early in the development process, even if it's not immediately useful
• It's essential to collect relevant metrics and gauge information from the start to make it easier to track down problems later on
• Small or medium-sized projects can benefit from implementing telemetry at the design stage to avoid costly mistakes later on
• Key considerations include determining what data to collect, how to collect it, and ensuring holistic thinking about project success factors such as availability, debuggability, and scalability.
• Efficient telemetry collection vs. paralysis
• Prioritizing important metrics for different teams and stakeholders
• Iterative approach to implementing telemetry in medium-sized projects
• Importance of storing as much data as possible and looking for anomalies
• Initial metrics to track: server, network, and application performance
• Responsibilities for caring for telemetry data (DevOps team or cross-functional)
• Strategies for dealing with alerts and SLOs (Service Level Objectives)
• The challenges of collecting telemetry data from large-scale systems and devices.
• The state of the telemetry landscape, including various open-source projects such as OpenTelemetry, OpenTracing, and OpenCensus, and the difficulty in establishing standards.
• The need for a standard way to collect and display telemetry data, especially in pre-packaged software and cloud platforms.
• The concept of observability and how telemetry plays a part in it, with concerns around debugging complex systems and issues that are difficult to solve.
• The trade-offs between custom solutions and standardized tools, such as Prometheus and Grafana.
• Observability is about being able to see through the complexity of a system and understand what's happening, even when faced with issues like cloud service errors or destroyed Kubernetes pods.
• It involves asking questions that are not easily answered by traditional metrics, but rather requires utilizing collected data in new ways.
• Dave Blakey notes that observability is not just about collecting more data, but about being able to see the system as a whole and identify potential problems before they occur.
• He also emphasizes the importance of simplicity in observability tools and APIs, making it easy for developers to collect and emit telemetry data without affecting performance.
• The conversation then shifts to Go, with Blakey stating that it makes collecting telemetry data "very easy" and doesn't pose any significant challenges compared to other languages.
• Jaana Dogan notes that while Go has good support for telemetry, a more accessible way of exporting metrics would be beneficial, especially for developers who may not consider telemetry until later in the development process.
• The conversation concludes with discussion on how to make telemetry collection and usage easier, including creating well-documented source code examples or packages that demonstrate best practices.
• expvar package's limitations and potential deprecation
• Push vs Pull model for metric data collection
• Advantages of pushing metrics over pulling
• Flexibility of push model in globally scalable monitoring stacks
• Use of UDP fire and forget for telemetry collection
• Company's use of multiple tools (Datadog) despite having a product that collects and exposes data
• Observability solutions not being a one-size-fits-all solution
• Importance of vendor-agnostic telemetry and data export
• Challenges with multiple stakeholders having different requirements for data
• Collection of telemetry data by ADC (Application Delivery Controller) platforms
• Focus on anomaly detection and predictive profiling rather than hard-coded thresholds
• Need to balance alert generation to avoid noise and ensure importance is conveyed
• Difficulty in weeding out false positives and finding a suitable threshold for alerts
• Anomaly detection challenges in timed events or sudden traffic spikes
• Balancing act between anomaly detection and alerting systems
• Importance of telemetry in DevOps teams and traditional teams
• Correlations and root cause analysis for issue resolution
• Difficulty in diagnosing bottlenecks and performance issues at scale
• Art vs. science approach to anomaly detection and data exploration
• Sources of problems: internal sources (developer changes) vs. external sources (traffic spikes, brute force attempts)
• Predicting system failures due to burst in traffic or unexpected events
• Page load times and telemetry data
• Choosing a programming language for startups and small companies
• The importance of hiring talent with experience in the chosen language
• Balance between using trendy languages and older, well-known languages
• Deployment strategies and the limitations of containerization and cloud-native solutions
• The industry is oversaturated with solutions and features, making it difficult for new products to stand out.
• Cloud-neutral approaches are becoming more popular as customers want to avoid proprietary cloud solutions.
• Orchestration and scaling have become easier, but telemetry remains a challenging problem that many companies are trying to solve.
• Having some form of telemetry is considered necessary for production-readiness.