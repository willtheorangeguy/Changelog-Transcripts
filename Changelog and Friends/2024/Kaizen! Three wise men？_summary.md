• The hosts discuss the joy of missing out and their weekly talk show format
• Jasmine Casis from Sentry discusses the adoption of session replay, a feature that helps developers troubleshoot user interface errors
• Sentry is releasing a new edition of session replay for mobile devices
• The hosts announce that Sentry is offering a $100 discount on their team plan
• Gerhard discusses his "kaizen" episodes, which are presentations on the host's own productivity and workflow
• The hosts announce that they will be shifting their focus to making their podcast the best developer podcast experience in 2025
• Some shows, including Go Time and JS Party, will be discontinued or repurposed as part of this shift.
• cpu.fm is a new vision for the podcast universe, with a focus on supporting shows and creators in a more direct and personal way
• The current model has reached its capacity and can no longer support new shows or ideas
• The decision to create cpu.fm was made after considering various options, including scaling the business or staying at capacity
• cpu.fm will allow creators to produce their own shows independently, with the company's support and resources
• The change is bittersweet, with some shows being spun off or discontinued, but the goal is to create more and better developer podcasts in the long run
• The company's founders are excited about the future and the potential for new life and growth in the podcast universe.
• Imposter syndrome and the grass is greener on the other side
• The concept of the "Joy of Missing Out" (JOMO) and its application to remote work
• The importance of leaving space in one's schedule to focus on important tasks and personal projects
• The concept of kaizen (continuous improvement) and its application to productivity and work
• The limitations of a small team and the benefits of expanding to a larger team and new opportunities
• The importance of staying true to one's goals and desires, and finding room to breathe and experiment in one's work.
• The hosts discuss a "catalyst point" in their journey, marking the beginning of something amazing.
• The hosts mention that nothing is changing about Kaizen, but it will become more explicit and possibly better with more development time.
• The hosts tease a surprise announcement, which involves presents from Gerhard.
• Jared discusses his desire to upgrade his MacBook to a new Mac, specifically the M4 model, but is hesitant due to his current Mac's high specs.
• The hosts mention that some listeners have tried the "just contribute" feature, but it's not clear if it was successful.
• The speaker presented a talk about taking their home lab into production
• The talk was recorded and edited by the speaker, and is available on YouTube
• The home lab, a Latte Panda Sigma, is comparable in size to an iPhone and is highly powerful
• The device can run Kubernetes, has 16 cores, DDR5, and can serve 300 billion requests per month
• The speaker showcased the device's ability to do video transcoding with Intel's Iris Xe graphics
• The speaker demonstrated Jellyfin, a media server, running on the home lab and serving a video
• The speaker discussed their content creation process, including editing and publishing videos on makeitwork.tv
• The speaker mentioned their appreciation for video editing and the challenges that come with it
• The speaker discussed a pull request that enabled team members to use a prod db dump, and praised the ease of use of a CLI utility they created.
• Discussion of a tool (possibly called "gear hard") that automates complex tasks and makes them easier to manage.
• Comparison of using containers (with tools like Docker) versus virtual machines (VMs) in development environments.
• Mention of a company (Coder.com) and its cloud development environment, which uses VMs instead of containers.
• Explanation of the limitations of using containers and the benefits of using VMs in certain situations.
• Discussion of the technical details and trade-offs between using containers and VMs.
• Introduction of a new tool or approach to simplify complex development tasks.
• Enabling team members to run dev with a Neon DB branch
• Creating a new command to automate the process of creating a new branch on Neon and configuring the app
• Syncing data between branches
• Improving the process of developing against a production branch
• Migrating to Zulip from Slack for team communication
• Tracking and following conversations in Zulip
• Zulip's threaded conversations for teams and its differences from Slack
• Difficulty creating new topics in Zulip and the importance of having a place to discuss
• Wish to have a single non-threaded space in Zulip like a main channel
• Long-lived threads and their benefits in keeping conversations active
• Compartmentalization of conversations in Zulip, such as in podcast episodes
• Comparison of Zulip and Slack in handling asynchronous conversations
• Mobile app issues and UI problems in Zulip
• Criticism of Zulip's URLs and deep linking functionality
• Current use of both Zulip and Slack, with plans to finalize Zulip adoption
• Discussion of blue-green deployment and eventual shutdown of Slack
• Plans to move from Slack to Zulip for team communication
• Concerns about Slack's free plan and its limitations
• Ideas for improving Zulip to better support communities and compete with Slack
• Discussion of Zulip's potential and its open-source features
• Personal anecdotes about using Zulip and its features
• Adding clickable links to chapters in Zulip for easy navigation
• Challenges with integrating chapters in video format, including potential issues with timestamps and linking to YouTube
• Deciding between having one identical artifact on both platforms or creating separate content for each
• Catering to different audience expectations on YouTube, such as shorter, punchier content
• Creating separate content for audio and video formats, focusing on the listener for audio and the watcher for video
• Three types of content catering to different audiences: the listener, the watcher, and the nerd
• Improvements to the platform, including notification deployment in Zulip
• Ease of use with the Zulip API and token-based authentication
• Integrating Zulip into the app
• Using GitHub Actions to automate tasks
• Pull requests and topic-driven development
• Capturing context and conversation in code
• GitHub actions vs. writing own API client
• Deploying code and announcing changes
• Namespace runners and cost considerations
• GitHub Actions runner with caching
• Nice UI for build insights
• Sponsorship discussion
• Zelib auth integration improvement
• Eight Sleep pod for ultra, a sleep technology product
• Wix Studio, a web platform for developers
• Pipe Dream, a future world where users can run their own CDN with Varnish config deployed on fly.io machines
• The discussion revolves around using the Hurl tool to test HTTP endpoints.
• Hurl is used to write tests and assertions about HTTP requests, with a focus on testing caching behavior.
• The tool is text-based, easy to use, and has a simple DSL.
• The discussion also touches on the concept of integration testing and how it differs from testing configuration.
• The team is exploring how to use Hurl for development, specifically for TDD (Test-Driven Development) of changes to the Varnish configuration.
• The team is considering spinning up Varnish and Origin locally for development, and weighing the pros and cons of different approaches.
• Testing the pipe dream config with local changes to ensure they affect the system as intended
• Using VCR (video cassette recorder) as a metaphor for recording and replaying HTTP requests
• Introduction of Dagger for programmatic container creation and service connection
• Discussion of domain name options for a new CDN, including pipely.tech and pipely.li
• Reference to the story of the Three Wise Men and the birth of a new CDN
• Conversation about a name for a CDN (content delivery network)
• Discussion of the idea of a "Rebel Alliance" for the CDN
• Mention of a conversation with Kurt Mackie, co-founder and CEO of Fly.io
• Reference to a "pipe dream" idea for the CDN
• Discussion of the importance of a good name and domain for the CDN
• Excitement and positivity about the potential of the CDN project
• Mention of challenges in building a CDN, including cache misses and the interests of existing CDN providers
• Decision to make room for the CDN project and explore its potential
• The potential of smaller, more focused CDNs that don't offer as much as larger ones
• The concept of "Pipe Dream" and its potential to improve various things
• The idea that the success of Pipe Dream isn't about profit or VC funding, but about doing the right thing
• The importance of testing and iterating on the product, with a focus on usability and scalability
• The need to send logs to honeycomb and s3, with a discussion of potential alternatives (r2, minio)
• Discussion of implementing purge functionality across app instances
• Challenges of implementing purge across all app instances
• Using Fly.io machines and DNS to discover and purge instances
• Using Oban and VCL config to implement purge and edge redirects
• Timeframe for implementation: weeks of work, spread over a long period
• Discussion of the pipely project and its potential
• Review of progress since January and assessment of feasibility
• Challenges around TLS termination and proxying requests
• Introduction of Vector.dev as a tool for sending logs and metrics
• Discussion of building blocks and clear direction for implementation
• Team discussion and agreement on moving forward with the project
• Celebrating the team's success and relationships
• Announcing the birth of a new CDN, pipely.tech
• Recap of the kaizen process and looking forward to the next steps
• Emulator is shipping to the public before the end of the year
• 7th Annual State of the Log Spectacular episode is upcoming
• Voicemail submissions for State of the Log Spectacular are due soon
• Appreciation for listeners and show partners
• Mention of coding and meeting deadlines
• End of the show and encouragement to stop listening and work on tasks