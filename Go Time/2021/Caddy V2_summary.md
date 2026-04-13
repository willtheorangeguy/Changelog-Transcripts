• Background information: Matt Holt created Caddy as an undergrad student at NYU to address his own frustrations with existing web server options.
• HTTPS feature: Caddy's early adoption of secure HTTPS, particularly with Let's Encrypt, was a key factor in its initial success and helped it "catch on" during the right time.
• Saturated market: Holt believes that today's web server landscape is too saturated, making it harder for new projects like Caddy to gain traction.
• ACME protocol: Caddy is compatible with multiple publicly-trusted certificate authorities implementing the ACME protocol, including Letsencrypt and ZeroSSL.
• Version upgrade: Holt explains that a major version bump from v1 to v2 was necessary due to changes in the Go language, internet landscape, and feedback from users.
• Design evolution of Caddy from version 1 to 2
• Challenges with version 1 and the decision to rewrite version 2
• Key features in version 2, including config API, module system, and JSON native config format
• Decision-making process for rewriting software versus adding new features
• Managing customer expectations during a major version transition
• Caddy 2 is a more complex tool than its predecessor, but still easy to use for simple tasks.
• The complexity is hidden from users when they use the Caddy file, and is converted to JSON behind the scenes.
• The tool has a "magic" mode that allows for simple configuration, but also provides access to advanced features through the JSON configuration.
• Users can choose between using the Caddy file or generating JSON directly, allowing for customization and flexibility.
• Writing software for continuous use without updates has presented challenges, particularly in terms of user responsibility to keep software up-to-date.
• The developer wishes that users would update their web servers more often, but acknowledges it's a complex issue with various factors at play.
• URL shorteners and auto-updating
• Enterprise customers and auto-update concerns
• Approaching auto-updates through package management (e.g., cron jobs)
• Documentation and accuracy, particularly with version 2 release
• Managing documentation for multiple versions and plugin compatibility
• Web server configuration and reference documentation
• JSON documentation and interactive features
• A Caddy plugin generates a JSON schema for the Caddy build.
• The v2 version of Caddy was a technical goal and unrelated to funding/sustainability efforts.
• Caddy experimented with shipping custom binaries from its website, licensed for non-commercial use unless paid for.
• Ardan Labs funded the development of Caddy 2 for the first ten months, allowing Matt Holt to drop commercial licensing binaries.
• Caddy is now purely an open source project, sustained by sponsorships on GitHub and other platforms.
• Sponsorships are a key aspect of making open source projects sustainable, with big companies often having easier access to funding through existing systems like GitHub or Amazon.
• Discussion on GitHub sponsorship pricing and its limitations for open-source projects
• Need for de-cheapification of sponsorships for professional companies using open-source software
• Value of sponsored companies receiving more attention from project maintainers
• Importance of sustainability in open-source projects, particularly for core infrastructure like Caddy
• Future plans for Caddy, including hosted management UI and leveraging remote management capabilities
• Unpopular opinion that request per second (RPS) metrics are no longer relevant for measuring web server performance
• Performance metrics for web servers are often unrealistic in production environments.
• Caddy performance is comparable to NGINX, but other factors like security and ease of use matter more.
• Measuring requests per second can be misleading, as real applications do more than just serve static content.
• Basic auth performance issues were fixed in Caddy 2 by changing the way passwords are configured.