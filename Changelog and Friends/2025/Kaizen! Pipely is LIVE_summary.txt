• The origins of Kaizen, a concept of continuous improvement, began as a podcast segment on Ship It episodes, where the hosts discussed improvements made to the Changelog platform.
• The conversation evolved over time, with the hosts discussing improvements and sharing their experiences with others, including the development of Pipely, an open-source project.
• The hosts reflect on the journey of Pipely, from initial doubts and discussions to the current milestone, where they are nearing completion of their goal.
• The Kaizen concept is emphasized as a collaborative effort, where the hosts work together to improve their platform and share their experiences with others.
• The hosts are excited to share their progress and plans for the future, including a presentation on Pipely and Kaizen 20, where they will discuss their accomplishments and answer questions from the audience.
• The group has met in person for the first time, marking a significant milestone in their 10-year journey
• The Changelog and Friends community has grown and evolved over the years, with many contributors and friends involved
• The group uses open-source technologies, including Varnish Cache, to build and maintain their platform
• There have been some challenges and setbacks along the way, including high S3 costs and inefficient use of resources
• The group has learned from their mistakes and is now using more cost-effective solutions, such as R2
• The Kaizen series of episodes has been a key part of the community's growth and development, providing a space for discussion and improvement.
• Discussing mistakes and learning from them
• Addressing a low cache hit ratio on the production CDN
• Mentioning the issue of slow loading times and its impact on the user experience
• Talking about the development of a new CDN and its potential benefits
• Discussing the challenges of distributing the application across multiple locations
• Mentioning the importance of having a good platform for hosting the application
• Referencing a "big thing" that will be revealed later
• Discussing the goal of keeping the application fast and reliable
• Application crash due to memory issues
• Architecture of Pipely explained, including Varnish instances and backends
• Discussion of feed generation and distribution for podcast indexes
• Problem of fine-tuning Varnish memory allocation configuration
• Live coding session to adjust Varnish memory limit to 66% of total memory
• Deployment of updated code to production using Git tags and commits
• Deploying Kaizen 20 changes to production
• Discussion of deployment pipeline and timing
• Review of the blue/green deployment process
• Examination of instance performance and request traffic
• Comparison of deployment times with other teams and technologies
• Discussion of potential issues with instance performance and request traffic
• Discussion of load average and endpoints being served
• Launch of Pipedream application and routing traffic to test its handling
• Review of live traffic and user requests, including Chicago and Frankfurt as top request locations
• Acknowledgement of the team launching Pipedream on Thursday with only 20% of requests going through the new instance
• Gerhard's emphasis on rolling out changes in a way that appears seamless to users
• Discussion of Varnish Configuration Language (VCL) and its complexity
• Mention of James and Matt's contributions to the project, including their objective perspectives and diligent approach to documentation
• Idea to simplify VCL by using includes and removing unnecessary lines, aiming for a 20-line VCL
• Discussion of Varnish and VCL configuration
• Counting lines of code in VCL
• SSL termination with Go code
• Nabil's solution to terminate SSL for Varnish
• Dagger usage for remote engine and testing
• Using Dagger to run containers and achieve reproducibility
• Varnish caching to RAM only (no disk)
• Varnish optimization: discussion of potential improvements to Varnish performance on Fly instances
• Memory allocation issue: Varnish's inability to use available RAM, leading to crashes
• Autoscaling: exploring options for handling increased load on Fly instances, including adding RAM or new instances
• Region-specific performance: analysis of performance differences between Fly instances in various regions
• Monitoring and optimization: using tools like Honeycomb to monitor instance performance and identify areas for improvement
• Investigating URLs from Chicago and San Jose, California
• Identifying a user who uploaded a URL 9,500 times, suspected of being a stalker
• Finding another user, Kball, who was involved in the upload
• Suspecting someone is hotlinking the website and attempting to determine the source of requests
• Filtering and examining San Jose URLs and finding that a popular episode of Pocket Casts was being requested
• Shifting all traffic to a new server, Pipe Dream
• Discussing a process of switching to a new service (Pipe Dream)
• Mentioning the process of deleting existing DNS settings
• Talking about the potential for traffic spikes and crashes
• Referencing the transition from Fastly to a new service
• Monitoring the performance of the new service using real-time dashboards
• Discussing the cache hit ratio and its impact on performance
• Noting the temporary spike in traffic and requests
• Discussion of a significant improvement in website traffic with a 99.1% hit rate
• Explanation of how the improvement was achieved through changes to DNS and caching
• Mention of the role of Pipely and fly.io in the changes
• Gratitude and thank-yous to various individuals who helped with the process, including Dan Moore, Kendall Miller, and Jason, the editor.