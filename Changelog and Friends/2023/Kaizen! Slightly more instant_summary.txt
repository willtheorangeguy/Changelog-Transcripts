• Discussion of Gerhard's return to Kaizen and Jerod's perceived lack of accomplishments
• Adam's defense of Jerod's co-hosting skills and the testing of a neural search engine on Changelog News transcripts
• The neural search engine's limitations and Duarte's progress in improving it
• Adam's opinions on the meaning of Kaizen and the limitations of the search engine in capturing its nuances
• The use of human feedback to improve the search engine's responses
• Gerhard's suggestion to discuss the things that were not done or procrastinated on during the Kaizen period
• Discussion of caching solutions, including using static-generated feeds and object storage as a cache.
• Exploring alternatives to caching, such as using Phoenix's Pub/Sub feature for clustering.
• Introduction to Elixir releases, which package code and dependencies for self-contained updates.
• Discussion of clustering and the complexities it introduces, including updating instances and handling network unreliability.
• Rethinking the need for clustering, given the current setup and CDN in front of the application.
• Update on Fly and the shift in application architecture, including moving away from a geolocated application.
• Two instances of an app server setup
• Clustering and scalability with Fastly and Fly
• Distributed proxy with Fly and its effect on caching
• Database placement and latency considerations
• Switching to R2 for storage and its cost benefits
• Debugging issues with Fastly and S3 caching
• The conversation begins with the hosts reminiscing about the company's relationship with Fastly, which started in 2016 and involved storing assets on S3.
• The hosts discuss how they moved to S3 from Linode and later from Fly, and how they had to switch to caching to improve performance and reduce latency.
• The conversation shifts to the importance of continuous improvement and identifying inefficiencies in systems, even at small scales.
• The hosts discuss how they were able to identify and fix issues with their billing and caching, and how they were able to improve their SLO (Service Level Objective) to 96%.
• The conversation includes a discussion of how to expire podcast feeds in Fastly using the Purge API and how to use Curl to purge endpoints.
• The hosts discuss the benefits of using Cloudflare R2 for caching and the improvements it brought to their system.
• Difficulty in purging Fastly cache
• Ability to purge individual URLs in Fastly cache
• Potential for abuse and DDoS attacks through cache purging
• Enablement of HTTP/3 in Fastly
• Benefits of HTTP/3 (20-30% speed improvement)
• Enablement of Brotli compression in Fastly
• Confusion about measuring Brotli compression benefits
• Enablement of edge-redirect for RSS feed
• Other low-hanging fruit improvements in Fastly
• Enabling WebSockets in Fastly to improve web app performance
• Debugging issues with WebSockets configuration and code
• Implementing a workaround (hack) to bypass configuration UI issue
• Containerizing and deploying Changelog Nightly using Dagger
• Upcoming changes to Changelog Nightly and Daggerize feature
• Team collaboration and communication on debugging and development
• Personal anecdotes and humor regarding debugging and development experiences
• Discussion of the Changelog Nightly app and its migration to a new server and setup
• Mention of Digital Ocean and Linode and the app's transition from 2015
• Explanation of the new setup, including Cloudflare Pages, Wrangler, and Dagger pipeline
• Discussion of using NGINX and Super-chronic for running cron tasks
• Reference to using Foreman for process management
• Mention of the remaining task of integrating 1Password service account
• Attempt to set up the app locally using Dagger CLI and Docker
• Discussion of the Nightly CLI and its features
• Demonstration of the CLI's functionality using Go code
• Explanation of how the Nightly CLI works and its advantages
• Mention of Dagger engines and their use in production
• Discussion of caching and performance optimization in the Nightly CLI
• Demonstration of running tests and building the project using the CLI
• dagger shell experimental features
• local image building with --debug
• GitHub DB storage (SQLite) and relocation to a persistent volume
• dotenv and BigQuery secret file handling
• embedding secrets in container image or using 1Password service account key
• 1Password integration for secret storage and access
• Discussing the origin of the term "OP" in relation to 1Password
• Exploring the functionality of Passbolt, an open-source password manager
• Comparing Passbolt's features with 1Password, particularly in terms of access control and encryption
• Discussing the importance of having two password managers for redundancy
• Examining potential solutions to issues with 1Password, such as creating separate vaults for different contexts
• Discussion of 1Password's vault visibility and searching functionality
• Comparison of 1Password's features to the hosts' own use of Changelog.com
• Desire to improve 1Password's continuous improvement (kaizen) and user engagement
• Planning for Changelog Nightly, including server setup and asset delivery
• Discussion of buffer scripts and potential removal
• Integration of Sentry for monitoring cron failures
• Mention of a potential $30.70 refund and plans to treat themselves to drinks
• KubeCon event details: November 6th-9th in Chicago
• Excitement and nervousness about finally meeting in person after 7 years
• Recording plans at Marriott Marquis and main show
• Expectations for the large conference: lots of people, energy, and activities
• Challenges of navigating the conference: need to pace yourself, prioritize conversations, and plan ahead
• Plans to connect with attendees: reach out via Twitter, Slack, email, or comments on the website
• Promotions of upcoming guests: Frederic from Polar Signals, Solomon, and Eric from BuildKit
• Phone number discussion
• KubeCon plans and meetup
• Kaizen T-shirt shipping issues
• Digital Ocean switch and Nightly shipping
• Plans for next Kaizen episode
• Personal jokes and humorous exchanges
• Discussion about potential new projects and prioritizing tasks
• Mention of upcoming KubeCon event in November
• Invitation to record an episode or meet in person at KubeCon
• Joking about seeing "every body" at KubeCon