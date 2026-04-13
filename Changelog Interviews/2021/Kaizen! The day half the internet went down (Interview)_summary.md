• Kaizen: the concept of continuous self-improvement and improvement of processes
• Reflection and improvement of the Changelog setup and show
• Importance of regular retrospectives and feedback loops
• Fastly CDN outage and its impact on the Changelog's infrastructure
• Switching to a Linode host and removing Fastly from the picture
• Experience with 99.96% uptime after the outage and cutover
• Discussion of the importance of being prepared for and responding to outages
• Miscommunication about downtime and Jerod's day off
• Discussion of recent downtime incident with Fastly and its impact on analytics
• Importance of redundancy and reliability in infrastructure and services
• Potential solutions for improving redundancy and reliability, including using multiple CDNs and cloud providers
• Trade-offs between cost, complexity, and benefits of implementing redundancy and reliability measures
• Technical challenges and limitations of implementing redundancy and reliability, including issues with stats and analytics.
• Discussing the limitations of using Cloudflare and the potential benefits of multi-CDN
• Managing incidents and creating a way to document and share lessons learned from them
• Dealing with a current incident involving a missing DNS token and the resulting certificate renewal issues
• Implementing an activity log for services with multiple users to track important actions and prevent similar incidents
• Deletion of an access token without clear activity log
• Discussion of the need for consensus or multiple approvals for sensitive actions
• Proposals for managing incidents, including tracking and communicating historical events
• Examination of the DNSimple platform and potential improvements, such as automated token management
• Exploration of incident management strategies and the role of proactive monitoring
• Discussion of the benefits of instant management and shared knowledge among team members
• Incident management and awareness
• Runbooks: codified steps for specific tasks and incidents
• Automation vs. manual processes
• Incident management platforms (e.g. FireHydrant, Incident.io)
• Retroactive creation of runbooks after incidents occur
• Importance of documentation and knowledge sharing within teams
• Discussing the importance of testing backup and restoration systems
• Exploring the trade-offs between pursuing high uptime and other priorities
• Mentioning the value of curiosity and experimentation in software development
• Discussing specific improvements to be made to the Changelog setup, including:
  • Incident management
  • Integrating Fastly logging with Grafana Cloud
  • Setting up Service Level Objectives (SLOs) for uptime and request failure rates
• Noting the limitations and potential drawbacks of integrating Fastly logging, including the need to set up a proxy server to handle log authentication and potential DDOS issues
• Mentioning alternative solutions, such as Honeycomb, that support direct integration with Fastly logging.
• Integrating Honeycomb with existing tools and workflows
• Discussing the benefits of using Honeycomb, including its ability to derive insights from complex systems
• Analyzing the current deployment pipeline and identifying areas for improvement
• Examining the impact of caching, dependencies, and cache invalidation on deployment times
• Exploring the idea of creating a "smarter" pipeline that can adapt to different types of changes
• Discussing the challenges of implementing such a pipeline, including the potential for complexity and brittleness
• Mentioning the goal of reducing deployment times to 15 minutes or less
• Discussing complexity of software development and the need to prioritize and simplify
• Investigating and optimizing the 15-minute delay in a specific process
• Considering a managed PostgreSQL database instead of hosting it internally
• Moving media assets to an S3 object store instead of local disk
• Addressing technical debt related to the assets uploader library in Elixir (Arc)
• Importance of regularly discussing and prioritizing improvements to software quality and system efficiency
• The app becomes effectively stateless, allowing for more flexibility and scalability.
• The chaptering feature for mp3 files is discussed, with the goal of adding it to the platform to enhance user experience.
• The lack of an ID3v2 library in Elixir is a major hurdle in implementing chaptering.
• FFmpeg is used to add ID3 tags, but it overwrites local ID3 tags, making local chaptering difficult.
• A possible solution is to pre-process mp3 files locally, adding chapters before uploading.
• The feature of allowing clients to skip to specific topics is desirable, similar to YouTube video segments.
• The ability to drag and drop files to automatically upload to S3 is also mentioned as a desirable feature.
• Proposal to improve areas of discussion from previous episode
• Plan to revisit discussion in 10 episodes
• Reference to "kaizen" (continuous improvement philosophy)