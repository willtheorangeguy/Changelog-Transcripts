• Internet outage at Jerod Santo's house
• Discussion of alternative plans due to internet outage
• Gerhard Lazu's presentation on Pipely, including multimedia content
• Review of the Changelog site's responsiveness on different versions
• Analysis of performance issues, including image loading delays
• Initial request to website causes slowness
• Using CDN reduces slowness, but still issues with cache misses
• Cache hits are low, around 18% of requests are served from cache
• Problem started in October 2023, cache hits decreased 7X
• Testing Pipedream.changelog.com to see if it makes a difference
• Issues with background color delay on Pipedream newsletter side
• Comparison of Changelog.com and Pipedream.changelog.com performance and content loading
• Discussion of CDN and cache setup, including TTL and origin configuration
• Analysis of HTTP requests and cache headers on Pipedream.changelog.com
• Evaluation of fly.io and CDN instance distribution across the world
• Review of application rollout and potential issues with data synchronization
• Low download stats for a recent episode, suspected to be a system bug or misconfigured CDN.
• Incorrect URLs posted to podcast clients and Slack/Zulip due to a URL mismatch.
• Background jobs not updating correctly, causing delayed or missing updates to feeds.
• Experimental instance consuming production jobs and posting incorrect links.
• Discussing and confirming changes to mitigate current issues
• Examining the use of Fly Radar, a new terminal utility, to monitor Pipely instances
• Investigating the CDN and its performance, including instance deployment and updates
• Identifying and discussing various regions and locations associated with the CDN
• Exploring the Fly Radar tool, its features, and its potential uses
• Reviewing log data and requests to the Changelog instance
• Discussing the performance and functionality of the CDN
• Discussing the most requested URL on the Pipedream backend
• Identifying the assets endpoint as the culprit, serving a podcast original image 10,000 times per day
• Testing the new CDN instance on Fly with Gerhard running commands in the terminal
• Benchmarking the current CDN (Fastly) and the new CDN instance (Fly) to compare performance
• Scaling up the Fly instance to multiple servers to increase bandwidth
• Testing the scaled instance and seeing a significant increase in bandwidth
• Instances on Fly don't seem to be getting more bandwidth despite provisioning for it
• The Bunny changelog platform is being throttled, preventing benchmarking
• Pipedream's performance is bottlenecked by CPU, not network, when run locally
• The Varnish Test Case (VTC) tool is being explored for testing VCL configurations
• Benchmarking shows that Pipedream can handle high traffic and transfer large amounts of data
• The discussion mentions that Fly's network capacity is a bottleneck, and a faster network would allow Pipedream to saturate it.
• VTC (Varnish Testing and Configuration) allows for low-level control of Varnish requests and responses for rapid experimentation and prototyping.
• The tool enables isolated testing of Varnish configuration, allowing for the creation of a minimal set of VCL code.
• Pipely has acceptance tests for its CDN, using Hurl to run real requests and check endpoint behavior.
• The tests can simulate various scenarios, such as delays and staleness, to ensure the CDN behaves as expected.
• Testing the CDN locally allows for faster test completion and better control over variables.
• Pipely's CDN can be tested against the existing production configuration, identifying areas for improvement.
• The acceptance tests have revealed differences in behavior between the existing and new CDNs, allowing for targeted improvements.
• Difficulty in testing and verifying the efficacy of different CDNs
• Vendor lock-in and the fear of the unknown when considering a change
• Importance of understanding the components and interactions of complex systems
• Progressive rollout and gradual transition to a new system
• Designing systems for failure and ease of rollback
• Maintaining multiple systems in parallel to ensure a smooth transition
• Ensuring data consistency and integrity during a transition period
• Differences in data due to configuration in Varnish vs Fastly
• Reconciling differences between Varnish and Fastly, specifically in data logging and storage
• Enterprise Varnish vs Open Source Varnish, and their differences
• Integration of custom components to mimic Fastly's Varnish Enterprise features
• Dagger and Dagger Cloud for local testing and telemetry
• Acceptance testing of the system, including real-time analysis of requests to Varnish
• Overview of the process tree and memory usage of the Pipely system
• Benchmarking and testing of TLS Exterminator and other components
• Acceptance tests run locally in 1 minute and 26 seconds
• Memory headroom: configuring Varnish to use the right amount of memory to serve requests quickly
• Forwarding logs: setting up Vector to consume Varnish logs and deliver them to Honeycomb and S3
• Edge Redirects: writing more VCL config, straightforward but with some differences from Fastly
• Content Purge: integrating with Fly to orchestrate purging across all instances
• Next steps: finalize content purge and send logs to Honeycomb and S3
• Caching strategies for static assets and dynamic content
• Implementing content purging for cache invalidation
• Classification of assets for caching (e.g. A, B, C buckets)
• Behavior of CDNs for refreshing and serving stale content
• Log forwarding for monitoring and analytics (Honeycomb and S3)
• Edge redirects and implementing content purgeability
• Discussing the importance of GeoIP information in logs
• Integrating MaxMind database for IP information
• Setting a goal to complete the CDN project by the next Kaizen
• Considering the "tip of the iceberg" concept and the idea of bottlenecks
• Reviewing progress and lessons learned from the project
• Planning for the next Kaizen (20) and its expected completion of the CDN project
• Discussing the benefits of the CDN project, including improved availability and reduced redirects
• Reflecting on the project's journey and timeline, which started around October 2023
• Planning to delay the next Kaizen by a couple of months
• Completing the current project and achieving the "90% Done" goal
• Ideas for a launch party for Kaizen 20 in Denver
• Invitation for listeners to attend the launch party
• Plans for celebrating the completion of the project