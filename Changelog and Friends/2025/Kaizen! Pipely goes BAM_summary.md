• Pager Duty and its complexities
• On-call and incident management
• Wearable devices and notifications (Apple Watch)
• Apple Maps integration and navigation
• Mobile gaming and distractions while driving
• The hosts discuss a listener's desire to put a PlayStation console in their car dashboard and the impracticality of doing so due to skipping issues.
• Gerhard Lazu mentions that this will be his 1-1-1 episode, a rare occurrence, and jokes about it being a long time until he reaches a "round" number again.
• The hosts discuss their goal of reaching 100 episodes of Kaizen and the possibility of the show continuing for a long time, potentially even outliving the hosts.
• Adam Stacoviak mentions that he has appeared on nearly all episodes of the Changelog and can look up his episode count on the Changelog website.
• The hosts discuss their episode counts, with Jerod Santo having appeared on over 900 episodes and Gerhard Lazu estimating that it will take around 75 more episodes to reach 1000.
• The hosts joke about the possibility of Jerod Santo reaching 1000 episodes in the current year.
• The hosts discuss a hack on the News podcast that has given Jerod Santo a large number of episodes.
• The hosts discuss a recent outage of the Changelog website and the steps they took to resolve the issue.
• Fly.io outage caused by a far upstream network failure
• Outage occurred on February 16th, half of a Sunday, and lasted for 4 hours
• 97.40% of requests were still served during the outage
• The website was affected, but most visitors may not have noticed due to caching and CDN
• The app was specifically affected, but MP3s and other static assets were still accessible
• The team did not have a redundant application instance in a different region to mitigate the failure
• Discussion about distributing the database and adding free replicas to improve redundancy
• Next tasks mentioned include:
  • Linkifying chapters in Zulip and new episode messages
  • Reviewing the implementation of a recent feature
• A new feature allowing clickable links in comments was implemented
• The feature is useful for referencing external resources within conversations
• Adam Stacoviak initially claimed he had not clicked any of the links, but later admitted to clicking at least one
• Adam Stacoviak also made a joke about eating "crow" due to his initial claim
• The group discussed the quality and usefulness of the feature and its benefits for the community
• Adam Stacoviak shared a personal anecdote about being unaware of the term "Reese's" for a long time
• Discussion of a YouTube video podcast featuring Adam Stacoviak and Techno Tim
• Feedback from Gerhard Lazu on the value of video content, citing a specific episode that kept his attention
• Adam Stacoviak's recent build of a beefy AI homelab, including hardware specifications and configuration choices
• Discussion of network and PCIe lane configurations, and potential performance implications
• Adam Stacoviak's experience with buying a 3090 GPU on eBay and his subsequent setup and testing of the machine
• The discussion starts with a critique of Windows, citing its hostile nature towards developers and users.
• Adam Stacoviak shares his experience with Ubuntu Desktop, calling it the closest contender to a non-macOS operating system that's fun to play with.
• Gerhard Lazu recommends PopOS, an Ubuntu-based distribution, for its improved NVIDIA integration and tiling manager.
• The group discusses the challenges of using Linux, including difficulty with GPU support and Docker integration.
• Adam Stacoviak shares his struggles with SSH-ing into a Windows 11 machine, citing the need to install the OpenSSH server and dealing with username issues.
• The conversation also touches on WSL2, with Gerhard Lazu expressing mixed feelings about its integration and usability.
• The discussion concludes with a mention of alternative operating systems and distributions, including Mac and Nix OS.
• Discussion of Windows workstation vs Mac for editing machine
• Comparison of fan noise and temperature between Windows and Mac machines
• Exploration of building a Linux workstation and its benefits
• Consideration of having multiple machines for different tasks and having backups
• Discussion of launching video podcasts and the transition from audio-only podcasts
• Reflection on the response to video podcasts and the desire to maintain a balance between audio and video content
• Linux is mentioned as being cool and used in the Changelog podcast
• A lengthy comment on the embedded podcast is discussed, highlighting its thoughtfulness and relevance
• The conversation turns to YouTube and the benefits of having a video-first approach, including being able to capture a larger audience and provide a more humanistic component
• The hosts discuss various features and integrations with YouTube, including the Watch button and expanded play bar
• The conversation shifts to CPU.fm, a new project, and the hosts discuss infrastructure needs and technical plans, including a possible database and CDN
• The hosts discuss the technical stack for CPU.fm, including Ruby on Rails, and the possibility of using Fly for deployment
• Plans to rebuild Pipely on top of Ruby and Rails, and potentially open-sourcing it
• Jerod Santo's experience with Ruby and Rails after a long time, and his willingness to share his experience on the Changelog
• Pipely's CDN and how it relates to Fly.io
• Contributions to Pipely, including a contribution from Matt Johnson to make it easy to develop locally
• Another contribution from Nabil Suleiman to resolve the Varnish TLS issue using TLS Exterminator
• Discussion of the uniqueness of Jerod Santo's perspective as someone who has used both Elixir and Ruby/Rails, and the potential for interesting content on the Changelog
• Discussion about disabling HTTPS and keeping TLS on for security
• Explanation of why Varnish Cache doesn't have built-in SSL support
• Mention of Poul-Henning Kamp, a Danish developer who contributed to FreeBSD and Varnish, and is known for his transparency and open-source work
• Overview of Pipely, a tool that uses Dagger to create a specific environment and deploy containers
• Demonstration of using Just Debug to interactively debug a container and run tools like curl and tmux
• Example of using Just to start a Varnish instance and list backends
• Discussing a horizontal setup for a Changelog application
• Benchmarking the Changelog origin application in production
• Analyzing performance with 90 requests per second
• Benchmarking the CDN and finding it to be doing its job
• Testing Pipely deployed on Fly, which proxies to the origin
• Benchmarking Varnish directly, finding it to be quicker and able to serve 211,000 requests per second
• Comparing performance with current setup using Fastly, which can handle 10,000-11,000 requests per second
• Discussion of benchmarking CDN performance, with Gerhard Lazu testing Pipely's limits and comparing it to Fastly
• Throttling and protection measures implemented by Pipely to prevent abuse and DDoS attacks
• Possibility of authenticated benchmarking to bypass throttling and allow for more realistic testing
• Comparison of Pipely's performance to Fastly's, with Gerhard Lazu scaling up his machine to test it
• Fly's command-line interface and its ability to upgrade machines for better performance
• Gerhard Lazu's setup and environment, including a new camera and monitor, and a Grafana dashboard behind him
• Discussion of a large screen (Samsung S95D) and its capabilities
• Explanation of the BAM (Big Ass Monitor) and its use in monitoring Changelog infrastructure
• Demonstration of the screen's ability to display metrics and spikes in real-time
• Discussion of Pipely and its performance compared to the current CDN
• Mention of scaling issues with Pipely and the need for further configuration
• Discussion of the cost of the Samsung S95D screen and Gerhard's suggestion to shop around for a deal
• Personal conversations about birthdays and the screen's impressive features
• Upgrading to Performance 1x instances resulted in 10x the RAM, but scaling to 10 instances did not significantly improve bandwidth performance
• The team is considering whether 4,000 requests per second is sufficient for their needs
• Network bandwidth limits may be a bottleneck, and the team is researching how CDNs allocate bandwidth
• Throttling may be necessary to prevent DDoS attacks on the system
• The team is deciding whether to implement rudimentary throttling to protect against low-level DDoS attacks
• They are weighing the trade-offs between performance and cost, and considering the implications for their own usage of the system
• Caching limitations and costs
• Memory vs disk storage for hot and cold data
• Optimizing instance size and configuration for different regions
• Cache hit ratio and evictions
• NVMe disks speed
• Adding feeds backend and static assets
• Configuring Varnish for different backends
• Logs and sending logs to Honeycomb
• Integration with S3
• Purge across all application instances
• Benchmarking and replacing current CDN capabilities
• Configuration and resource requirements for Pipely
• Discussion of a new system (Pipely) being developed to replace Fastly
• Gerhard's home lab setup and homelab tour discussion
• Adam's interest in a homelab tour and Gerhard's plans to provide one
• Overview of Gerhard's M25 machine, a fully maxed out TrueNAS setup
• Discussion of storage and RAM needs for various systems, including TrueNAS and homelab setups
• Gerhard's experience with his wife gifting him a Samsung S95D TV as a reward for his work on Pipely
• Adam Stacoviak has a flood in the studio and is moving his home office into a home lab
• Adam is updating his network to 10-gigabit everywhere
• Discussion of setting up a true home lab and being close to equipment and projects
• Gerhard Lazu and Adam discuss a possible Zoom or FaceTime tour of Gerhard's home lab
• Discussion of Makeitwork.tv and the challenges of distributed podcasting, including screen recording quality
• Adam puts Gerhard on the spot about his CPU upgrade, and Gerhard expresses his continued interest in the project
• Clarity is necessary when considering the service
• Kaizen is a deep and complex process
• The show is wrapping up for the day
• Gerhard Lazu and Jerod Santo discuss "Kaizen"
• Adam Stacoviak joins in on the discussion