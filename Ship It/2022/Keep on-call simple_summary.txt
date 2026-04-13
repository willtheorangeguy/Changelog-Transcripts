• The origin and pronunciation of the company name Amixr (Grafana OnCall)
• Why people need to be on-call for their teams' services
• Benefits of having a distributed team for on-call shifts
• Outsourcing on-call as an option for small companies
• Experiences of being on-call, including waking up in the middle of the night
• The ideal scenario where incidents are automatically fixed and humans don't need to be on-call
• Shared experiences of the speakers' best (and worst) on-call moments
• Incident management and learning from incidents
• Importance of sharing and documenting incident learnings to mitigate technical debt
• Worst on-call experiences, including making problems worse with code changes or sending notifications to all customers
• Dealing with unexpected behavior in production systems, such as auto-responding threads taking down servers
• Deleting production data accidentally, including deleting entire databases and dealing with migrations gone wrong
• Database management, including using hosted databases and duplicate clusters for synchronization
• Discussion of high availability and disaster recovery strategies using multiple cloud providers
• Use of MySQL 5.7 and Kubernetes for infrastructure management
• Explanation of Grafana OnCall's incident response management system
• Story of how the company created its own IRM tool due to dissatisfaction with existing solutions
• Experience of building a Slack application for on-call scheduling and management
• Discussion of a significant incident involving DigitalOcean's Kubernetes service going down, leading to creation of two fully functional clusters in different cloud providers
• Discussing running production on beta version of Grafana OnCall
• Current hosting setup (DigitalOcean as backup, not primary)
• Discussion of multi-cloud strategy and diversifying from Kubernetes
• Current Kubernetes setup (using basic components, no complex technologies)
• RabbitMQ usage (critical component for Amixr, managed internally due to complexity)
• Surprise reveal that Gerhard Lazu is a former core RabbitMQ engineer
• Grafana OnCall is part of Grafana Cloud
• Starting point for using Grafana OnCall is the Grafana Cloud interface
• Grafana OnCall is focused on notifications and incident management, not alerting or large-scale incident response
• Integration with existing Grafana setup and unified alerting system required
• Customizable on-call rotation and escalation policies available
• Can consume on-call schedules from external calendar systems like Google Calendar
• Mobile phone verification and SMS capabilities also available
• Ideal incident scenario: receiving notifications only when attention is needed, and having enough context to investigate.
• Automated alerts vs manual investigation: wanting to know the cause of an issue before investing time in investigation.
• Importance of context during incidents: knowing which part of the network or system is affected.
• Redundancy and failover: having multiple instances and providers to minimize downtime and allow for easy recovery.
• Incident management software: needing a tool that can provide detailed information about issues and help with incident response.
• Plans to read books during holiday season
• Most important takeaways for listeners from the conversation
  • Importance of building accessible and user-friendly tools for engineers
  • Unique opportunity for on-call engineers to create products that can change their lives
  • Incident management process should be tailored to individual needs
• Future prospects for Grafana on-call and its ecosystem in 2022