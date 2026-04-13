• Switching assets to S3, AWS
• Reasons for initial delay (inexperience with Elixir, desire to keep it simple)
• Prioritization of tasks as a developer with multiple roles
• Contextual decision-making and trade-offs
• Limitations of keeping files local (single application instance limitation)
• Live migration process without downtime or significant disruptions
• Kubernetes storage drivers and complexities
• Deploying Changelog to multiple platforms
• Challenges with FFmpeg and ID3 tagging in Elixir
• Debugging and problem-solving process for Jerod Santo
• Solution: moving code outside of Waffle library and using own module
• Reflection on Kaizen (continuous improvement) process
• Reviewing past episodes for accuracy and accountability
• Migrating to a new Kubernetes cluster with Crossplane and testing S3 integration
• Addressing issues with elevated 404 responses for favicon.ico and MP3 files
• Investigating increased misses for MP3 files due to lack of origin shielding on Fastly
• Considering alternative CDNs, such as CloudFlare R2, for simplification of setup and configuration
• Discussion of performance metrics after switching to S3 for static assets
• Analysis of 99th percentile latency and potential causes
• Mention of Steve Schwartz's suggestion to reduce image file sizes to improve latency
• Explanation of why some large files (e.g. 18MB GIFs) are being served and considered for optimization
• Investigation into PostgreSQL query performance as a potential bottleneck
• Review of various content types' 99th percentile latencies and comparison to pre-S3 values
• Gerhard discusses his behind-the-scenes experience with Honeycomb, a tool for observability and debugging
• Adam Stacoviak suggests creating a 20-minute YouTube session where Gerhard explores Honeycomb and shares his experience with the audience
• Gerhard mentions that he recorded Merry Shipmas videos but never had time to edit or publish them
• The team discusses future plans to release these videos and explore other tools, including Crossplane, Dagger, and Frederick
• Gerhard explains the challenges of moving their database from a single stateful set on Kubernetes to a multi-platform environment
• The team discusses potential solutions, including Fly, CockroachDB, and hosted PostgreSQL offerings
• The importance of sharing information as a valuable resource
• Comparison shopping for cloud providers, with Fly being considered a solid player
• Why the podcast platform and news syndication platform needs to explore multi-platform deployment (e.g. LKE, Fly) for learnings and sharings
• The desire to improve through continuous improvement (Kaizen)
• A recent S3 cost spike and the effort to mitigate it using shielding and other means
• A discussion about change log.com/++ and how listeners can support the show by sharing it with friends or subscribing
• Discussion on Fly.io and its potential for Elixir/Phoenix users
• Exploring multiple CDNs/Kubernetes setups for increased resilience
• Importance of redundancy in infrastructure setup
• Sharing learnings from exploratory efforts rather than offering advice
• Listener feedback on the podcast's content and focus
• Desire to hear from users who have implemented solutions rather than company representatives.
• Addressing listener feedback about biased coverage of certain products and teams
• Importance of covering end-user stories and experiences in addition to product showcases
• Explanation of how the podcast's no pay-to-play policy affects sponsored content
• Discussion of the importance of transparency and trust with listeners regarding sponsored content
• Invitation for listeners to suggest potential guests or topics for future episodes
• Experimenting with different formats and topics for podcast shows
• Importance of telling stories about people and their experiences in the industry
• Dagger project and its goal to improve CI/CD systems by introducing a new container-based approach
• Gerhard Lazu's commitment to shipping code and his involvement with the Dagger team
• Solomon Hykes' return to the scene with a new project and his involvement with Dagger
• Discussion of Gerhard's excitement and passion about his work
• Dagger and its applications, including Changelog and deployment of Phoenix/Elixir apps
• Introduction of CUE (a language for defining infrastructure as code) and BuildKit
• History of Deliver and connection to current projects (10 years in the making)
• Connection between Steve Jobs' quote and Gerhard's experiences
• The concept of Kaizen (continuous improvement) and community engagement
• Discussion of vanity URLs for the Ship It podcast