• The founders of Transistor.fm discuss their journey and how they started the company
• Jon Buda shares his experience working on podcast hosting platforms in 2013 and again at Cards Against Humanity, which led to the creation of Transistor.fm with Justin in 2018
• Jason Pearl joins the team as the first non-Jon engineer after being approached by Jon and Mike, and discusses how he was recruited and why he chose to join the company
• The team now consists of four members: Justin, Jon, Jason, and Helen, who handles customer support from England
• They also discuss their podcast "Build Your SaaS" and how it started as a way to document their process of starting a company together
• Launch of a new feature for Transistor.fm
• 150+ signups and positive response on Product Hunt
• Infrastructure upgrades leading up to launch, including:
	+ Upgrading Elastic Beanstalk from an older version
	+ Switching from Amazon Linux 1 to Amazon Linux 2
	+ Updating Caddy web server from v1 to v2
	+ Upgrading Rails from 6.1 to 7 and Ruby from 2.6 to 3
• Single app architecture
• Reasons for choosing single app over microservices
• Experience with Ruby on Rails and its limitations (background workers)
• Background workers and queuing systems in Rails
• History of background worker implementations in Rails (delayed job, sidekiq)
• Redis and its introduction
• Switching from Mailgun to SendGrid due to issues with API and SMTP server
• Problems with Backblaze B2 service, including slow uploads and storage pod issues
• Previous issue with Caddy certificate renewal through Elastic Beanstalk load balancer
• Comparison of monolith vs. distributed architecture and its impact on operations
• Importance of keeping things simple in ops, without a dedicated platform team
• Monitoring and notification systems, including Sentry, Crisp, Amazon, CloudFlare
• CDN setup and usage (Cloudflare, Backblaze, Bandwidth Initiative)
• Current limitations of the current setup (dependencies on Rails app, potential issues with caching)
• Potential solutions to increase resilience (moving audio files to Cloudflare, using Cloudflare Workers)
• Comparison of traffic served through Cloudflare between different podcasts (750 terabytes vs 45 gigabytes)
• Discussion of alternative CDNs and their pricing
• Overview of available Cloudflare features and potential uses for Transistor.fm
• Improving deployment process with merge deploy to production
• Splitting large Sidekiq jobs into smaller, concurrent ones
• Improving import process for podcasts by making it asynchronous
• Implementing rate limiting for certain services
• Considering moving podcast analytics and audio serving to Cloudflare Enterprise
• Developing a standalone application in Go (Receiver CLI) for building themes locally
• Reducing code change deployment time from 15 minutes or more to near-real-time
• Speeding up specs in testing
• RSpec and its DSL
• Rails boot times improvements
• FFmpeg usage and potential replacement with Elixir library
• Continuous improvement (Kaizen) and infrastructure updates at Changelog
• Transistor.fm features, including YouTube integration and podcast tagging
• Discussion about YouTube Premium and its podcast features
• Plans for team members to meet in person for the first time at an upcoming event in Montreal
• Comparison of remote work experiences during COVID-19 pandemic
• Discussion about the company's culture and lack of drama
• Discussion about backup strategies, including a conversation about Backblaze and AWS S3 storage
• Importance of simplicity in infrastructure and keeping it easy to maintain
• Value of hiring people that get along with each other
• Benefits of growing slowly and not expanding too quickly
• Calm and relaxed approach to work, prioritizing quality of life
• Avoiding complex technologies like Kubernetes and focusing on proven systems