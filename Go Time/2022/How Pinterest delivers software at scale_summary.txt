• Nishant Roy's background and role as Engineering Manager at Pinterest
• Scaling challenges and processes at Pinterest
• Evolution of engineering processes from pre-IPO to post-IPO
• Importance of compliance and blocking reviews in a public company
• Pipeline stages for integration and delivery, including unit tests, integration tests, staging environment, and automated process
• Criteria for change review: significant impact on top-line metrics or major changes
• Lightweight process for smaller bug fixes and quick changes
• Implementing CI/CD system for continuous deployment
• Development of a robust canary analysis process to reduce outages and improve reliability
• Introduction of pre-submit integration testing framework to ensure changes don't cause significant issues
• Evolution of automated canary analysis from manual on-caller intervention to automated pause of deploys
• Addition of metrics from product teams and machine learning teams to the monitoring system
• Development of a production-simulated testing environment using Kafka logs to replicate production traffic.
• The speaker discusses how pre-submit tests in large companies can work well at scale, but may not be effective in smaller businesses due to limited sample size.
• Pre-submit tests are seen as a good approach for large companies with high volume and scale, but unit tests are still necessary for early-stage development.
• Pinterest uses an OpenTSDB backend for general observability and an internal tool called Statsboard for visualizing time-series metrics and defining alerts.
• The company has a custom solution for pre-submit tests that involves exposing metrics through an HTTP endpoint using the expvar library from the Go standard library.
• Pinterest's infrastructure is primarily based on Python, Java, and C++, but the ads team uses Go heavily for online serving due to low latency and high developer velocity requirements.
• The speaker discusses the challenges of tuning garbage collection in large-scale companies and notes that the Go team has recently added new features to improve this process.
• Discussion on the benefits of taking time to analyze GC (garbage collection) impact on services
• Comparison of Go's early days to its current state in terms of performance optimization
• Importance of tooling for understanding system usage and bottlenecks
• Need for official guides and tutorials on using performance tools like pprof and flame graphs
• Balancing premature optimization with the need for future-proofing and scalability
• Challenges of legacy systems and refactoring due to hypergrowth or changing product offerings
• Discussion on the eternal quest for balance between velocity, incidents, and system complexity
• Examples of modularity and config-driven systems to improve velocity and reduce system complexity
• Existing services were not optimized for performance and scalability at Pinterest's early stages
• Investment in better tooling and infrastructure has made it easier to optimize for performance and scalability
• At some point, there was a lack of centralized framework for ad-serving infra, leading to divergence in code quality, test coverage, and implementation logic among teams
• Standardization efforts are underway to standardize frameworks and tools across ads product teams
• Recording and communicating infrastructure decisions within teams and broader teams is done through standardized documentation templates, Production Readiness forums, email aliases, and detailed analysis documents
• Junior developers can learn by getting involved in incidents, observing discussions, and reading up on system documentation
• The value of knowledge gained from system owners or experts through their discussions and hypothesizing about system faults.
• The benefits of observing recurring issues and using past solutions as a guide for current problems.
• Onboarding process for new team members, including assigning an onboarding mentor and bi-weekly team meetings to share questions and suggestions.
• Nishant's unpopular opinion that working with non-typed languages can be challenging at large scales.
• Discussion of the trade-offs between typed and non-typed languages, with Jon Calhoun and Johnny Boursiquot sharing their perspectives.
• The importance of considering trade-offs in technology decisions
• The impact of ego on technology decision-making
• The role of experience and context in evaluating language complexity
• The challenges of switching languages as a company grows
• The lack of data to support definitive conclusions about language choice for different stages of company growth
• Personal anecdotes and humor regarding the snow outside