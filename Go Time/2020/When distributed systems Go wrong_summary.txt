• Distributed systems going wrong as a matter of when, not if
• Infrastructure monitoring at various levels (cluster, pods, deployments)
• Importance of understanding "what to care about" in monitoring
• SRE and SLA/SLO practices for prioritizing metrics and actions
• Focusing on the life cycle of data packets to inform monitoring needs
• Monitoring tools collect a wealth of information about system performance
• The goal is to focus on key metrics (SLA) rather than detailed infrastructure issues
• Different stakeholders require different levels of monitoring and context
• Data needs to be transformed into knowledge through analysis and contextualization
• Various approaches can be used, including collecting wide events, machine learning, or filters, depending on the specific needs and trade-offs
• Importance of understanding what users need versus what they want
• Need for data collection and analysis to inform decision-making, rather than just collecting all available data
• Importance of contextual dashboards for different user needs (e.g. debugging vs. monitoring)
• Blind spots in traditional monitoring approaches that focus on symptoms rather than root causes
• Separation between real-time monitoring and analytical workloads
• Monitoring as a sentry for detecting conditions that require investigation
• Importance of data collection and logging for root cause analysis
• Difficulty in correlating data from distributed systems
• Need for high-fidelity data to understand system state during outages
• Different levels of monitoring, with basic alerting being the foundation
• Observability as a related but distinct concept from monitoring
• Challenges in transitioning from reactive (rebooting servers) to proactive approaches
• Maturity level and cultural shift required to prioritize observability and root cause analysis
• Discussion around making systems observable and easy to monitor
• Trade-offs between rebooting servers vs. implementing more complex monitoring solutions
• Importance of business context and understanding return on investment for fixes
• Maturity levels in organizations and how they influence decisions around monitoring and troubleshooting
• Role of platform providers (e.g. cloud platforms) in making monitoring and troubleshooting easier and more accessible
• Examples of cludgy workarounds (e.g. rebooting servers) vs. implementing more robust solutions
• Shared responsibility model in cloud computing
• Visibility into cloud infrastructure and systems
• Observability of cloud platforms
• Data collection and storage in the cloud
• Responsibility for monitoring and troubleshooting bespoke solutions
• Surfacing the right data to the right people
• Providing queriable interfaces for data analysis
• Importance of regularly pruning unused dashboards and data to avoid overwhelming systems and teams
• Benefits of having top-level KPIs with drill-down capabilities for deeper analysis
• Separation between collecting data and analyzing it, allowing for flexibility in resource allocation and data retention
• Need for clear understanding of the difference between collection and analysis tools and processes
• The knowledge gained from data isn't always preemptive and may come after an incident
• Misunderstanding of system trade-offs can lead to issues with consistency and availability
• Chaos engineering can help understand how systems behave in the face of failures
• Open source projects can still lead to lock-in if one gets too deeply invested in a particular solution
• Logs are often over-relied upon for troubleshooting and debugging, when actually they're only useful at certain levels of detail
• Structured logging vs typical logs
• Benefits of structured logging in understanding system behavior and generating metrics
• Importance of reading error messages for debugging and troubleshooting
• Developers' tendency to resist reading error messages and instead rely on intuition or manual intervention
• SLAs (Service Level Agreements) and their importance in communicating expectations to customers
• The need for developers to understand and prioritize SLAs to ensure system reliability and user satisfaction