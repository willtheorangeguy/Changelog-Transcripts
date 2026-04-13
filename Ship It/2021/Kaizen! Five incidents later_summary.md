• Discussing the second Kaizen series, 2.5 months after episode 10
• Reviewing an incident involving DNSimple tokens and Cert Manager
• Using Incident.io for incident management and tracking
• Integrating Incident.io with Slack for easier access to past incidents
• Sharing knowledge and distributing incident information between team members
• Discussion of incident management and how the team uses an incident platform
• Explanation of how /inc command creates an incident in Slack
• Story about Oban, a background job processing library for Elixir, and its integration with the codebase
• Review of PR#378, which improved the use of Oban and reduced dependencies
• Discussion of the importance of testing system reliability and documentation of incidents
• Deployment process insufficiency led to a pod being put into service even though it was unhealthy
• The unhealthy pod caused the origin server to return 503 responses, resulting in a degraded experience for some users
• The incident affected only logged-in users who tried to access certain endpoints or pages
• The company took steps to improve redirects at the edge and reduce health check frequency after the incident
• The team implemented HTTPS everywhere and removed www redirects in favor of apex domain redirects
• Technical difficulties with www redirects
• Fastly configuration issues causing Safari redirect problems
• Testing in production and scripting requests to hit endpoints
• DNSimple findings and experimentation gone wrong
• Debugging as a detective who is also the murderer ( referencing a quote by Filipe Fortes)
• Discussion of extra domains used for testing
• Ping Pong domain reference to Erlang and infrastructure management
• Gerhard Lazu discusses his connection to Switzerland and the domain "lazu.ch"
• The discussion shifts to ClickOps and the importance of version control and GitOps for Fastly configuration
• Gerhard shares his experience with experimenting with Fastly and finding it difficult due to its ClickOps nature
• The conversation turns to recent incidents on Upbound Cloud, including Linode networking issues and LKE unavailability
• Gerhard discusses the reliability of backups and restores during networking issues, particularly with CockroachDB and Fly PostgreSQL
• Discussing network downtime and reliability
• Using Fly to run multiple instances of an app in different regions
• Limitations of local storage (block storage) vs S3-compatible APIs
• Planning for multi-region deployments
• Switching from Arc to Waffle for file uploads
• Errors in Sentry related to Erlang 24 upgrade
• Discussion of Erlang version upgrades and potential improvements
• Twitter Auth issues and consideration to remove or fix feature
• Ecto.Query.CastError errors, specifically related to podcast unsubscription route
• Analysis of error data in Getsentry and discussion of its features
• Proposal for handling robot-generated unsubscribe requests
• The team is having trouble receiving emails for new issues with Sentry
• Ownership rules in Sentry may be a solution to automatically assign new issues to the right people
• Weekday vs weekend error patterns are being discussed, with an interesting anomaly of high errors on weekends instead of weekdays
• Plans for episode 30, including exploring alternatives to their current infrastructure setup (Fly.io and Elixir)
• Integrating Honeycomb is mentioned as a priority, with Jerod Santo suggesting testing its integration and reporting back
• NGINX performance metrics discussed, including 90th and 95th percentile times
• Long tail requests taking over a minute to service
• Importance of reliability and robustness in software, particularly for Changelog app
• Goal of continuous improvement (Kaizen) for infrastructure and business progress
• Upcoming T-shirt design featuring Japanese characters representing Kaizen