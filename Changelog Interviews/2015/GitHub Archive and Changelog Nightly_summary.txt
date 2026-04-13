• Introduction of Ilya Grigorik, internet plumber at Google, and his background
• Mention of Ilya's previous appearance on the show (episode 55, 2011) and changes in the industry since then
• Discussion of HTTP2 and its replacement of Speedy as a standard
• Introduction of Jared Santo on the call
• Ilya's project, GitHub Archive, and its connection to Google's BigQuery project
• Ilya's current role and team at Google, focusing on making the internet faster
• Google's team structure and collaboration with various companies
• Ilya's background and experience, including VimGolf, GitHub Archive, PostRank, and Ruby Hero award
• PostRank's purpose and tools for social advertising measurement and ROI analysis
• Ilya's transition to web performance work and building HTTP servers
• Current work and involvement in HTTP2 protocol development, including the Ruby gem and contributions from the Tokyo community
• The speaker discusses their GitHub Archive project
• The project started as a personal itch to follow interesting open source projects and stay on top of new releases and issues
• The speaker used to follow many projects and people on GitHub, but the stream became overwhelming as more projects and people joined
• The speaker wrote a Ruby crawler to collect and log hourly archives of data from the GitHub API
• The data was stored in cloud storage, initially S3 and then Google Cloud Storage
• The speaker used BigQuery to process and analyze the data, and to make the data public and queryable by others
• The speaker wrote a simple Ruby script to query BigQuery daily and send two reports: top 10 open source repos and top 10 by number of stars received
• The speaker's newsletter, which started as a solution to their own problem, has 1,000 subscribers and an average open rate of 40%.
• The newsletter was based on the GitHub Archive BigQuery, which was used to provide fast and flexible querying of GitHub data.
• BigQuery was used to solve a narrow problem, but it ended up opening up to anyone to run arbitrary queries.
• The speaker mentions the GitHub data challenge, where participants use the GitHub Archive to build interesting visualizations or insights.
• The challenge has been running for three years, and the speaker mentions some examples of winning projects, including the open source report card.
• GitHub Archive provides a snapshot of all public GitHub activity
• There are two ways to interact with the data: downloading raw archives or using the BigQuery interface
• The BigQuery interface allows for writing SQL queries to process the data
• GitHub Archive leverages BigQuery under the hood, so data is always up to date
• TopTal is a platform for freelance software developers to find high-quality, long-term work
• The platform provides benefits such as compensation based on worth, travel opportunities, and access to software, hardware, and support
• GitHub has a visualization tool for comparing programming languages
• JavaScript is currently the most popular language on GitHub
• Discussion of using GitHub Archive data set for big data analysis
• Importance of making data analysis cheap and easy for collaboration and iteration
• Benefits of using BigQuery or similar tools for fast and easy question-asking and data processing
• Comparison of processing time between BigQuery and local desktop systems
• Overview of BigQuery and its public counterpart, Dremel, used for analyzing large data sets
• The speaker praises the GitHub Archive for showing a "plumber's attitude" towards data work
• The Archive started as a simple solution to a specific problem, but eventually became a valuable tool for many
• The speaker notes that having to do more work upfront can be worth it in the long run, as it allows for more flexibility and use of the data
• The GitHub Archive has required maintenance, but it has also made the ecosystem more fruitful
• The API changes over time have presented some difficulties, but the speaker notes that it's a BigQuery-specific gotcha
• The speaker discusses the importance of defining the data schema upfront, but being able to create new datasets with different schemas later on.
• The speaker had issues with GitHub's data format changes causing problems with data import and querying.
• BigQuery's ability to import JSON payloads solved the issue, allowing the speaker to revisit their implementation.
• The speaker switched to a new model where a subset of columns is fixed, and the rest is stored as a JSON blob.
• This new model requires more work from users writing queries to access the JSON data.
• The speaker no longer has issues with data format changes since they can simply import the JSON data into BigQuery.
• The user didn't explicitly turn off a system or update a query.
• The data schema has changed, with data being logged into a new table.
• The user realized that they had been logging data into the same table for over three years.
• The user exceeded a free quota for data storage, prompting a change to a new model.
• The new model separates daily and monthly data into separate tables.
• The user didn't rewrite the original system, opting instead to use GitHub's trending repositories email.
• The user finds the GitHub email less valuable than their original implementation, but still useful.
• Discussion of an email system that stopped working
• Realization that someone else should run the project, focusing on infrastructure
• Introduction of a new email system called Change Log Nightly, replacing GitHub Archive
• Collaboration between the speaker and Ilya to transfer the email list and ensure continuity
• Announcement of the new email system and its availability on changelaw.com/nightly
• Discussing the shared design work with Ilya
• Ilya's background and role as a designer
• Visualizing data in a different way for the email part of the project
• Implementing a night theme for the email to be more visually appealing at night
• Shipping the updated email to users and excitement about its release
• Growth of a mailing list to over 1,000 subscribers
• Comparison of automated and curated email formats (nightly update vs. weekly changelog)
• Discussion of the original mailing list's lack of promotion and unexpected growth
• Idea for creating thematic lists within the mailing list
• Exploring the potential for more interesting data analysis and experiments using stored data in BigQuery and GitHubarchive
• Plan to serve the open source community through various means, including shipping emails, podcasts, and blog posts
• Intend to open source the Nightly repo, allowing for community contribution and participation
• Discuss the benefits of open sourcing the repo, including increased community involvement and the ability to contribute to the project
• Share thoughts on the initial takeover of Nightly, with a focus on the potential for improved email content and community collaboration
• Express enthusiasm for the opportunity to work together with the community on future projects
• Mention of GitHub Archive source code and availability on GitHub
• Discussion of the future of GitHub Archive, considering it "mostly finished"
• Plans to revisit data importation into BigQuery to ensure consistency
• Acknowledgment of support from the BigQuery team for hosting data
• Discussion of data storage and GitHub Archive data
• Use of GitHub Archive data in research and academic projects
• Interest from GitHub in collaborating with the academic community
• Potential use cases for GitHub Archive data
• Existing research and publications using GitHub Archive data
• Discussion of exposing additional data sets via BigQuery
• Upcoming availability of additional data through GitHub Archive
• Details of how data will be made available still being worked out
• A word from the sponsor, CodeSchool, and their offerings
• CodeSchool's approach to learning and expanding skills
• Availability of free and paid courses, including introductory classes and coding challenges
• Discussion about CodeSchool.com
• Future of GitHub Archive
• Ways the community can help with GitHub Archive
• Importance of playing with data and getting hooked
• Options for working with data (raw archives, JSON, BigQuery)
• Request for help with re-importing old data
• Discussion of the importance of guidelines for contributors to step in and help with issues
• Project owners' responsibility to provide guidance for contributors
• Desire to create a guide or "rails" for contributors to follow
• Mention of hacking on BigQuery and breaking up large tables
• Ilya offering to provide help with making that process happen
• Discussion of the difficulty of finding time for contributions and the idea of a "yak shave" t-shirt
• Question about open-source projects currently on the radar
• Chrome and chromium explained
• Differences between Chrome and Chromium browsers
• Time spent working on Chrome/Chromium development
• HTTP2 adoption and compatibility issues
• Plans for implementing HTTP2 on servers
• Search for HTTP2 compatible servers and resources
• HTTP2 status page and implementations
• Need for contributions and testing of HTTP2 servers
• Compatibility with other browsers
• Book on high performance browser networking
• Online availability of the book
• HTTP2 and XHR improvements
• Server set events and related topics
• Discussing the rapid pace of technology changes and the need for frequent updates
• Mention of HTTP2 as a new technology that will be covered in future episodes
• Plans to create a book or resource on HTTP2
• Future plans to revisit the topic of HTTP2 and answer questions
• Discussion of working together on keeping emails current and exploring new frontiers
• Mention of githubarchive.org and the changelog nightly service
• Shipping arrangements
• Central Time Zone reference
• Changelog membership and listener support
• Personal background and transition to full-time role
• Acknowledgement of supporting members
• List of supporting members mentioned
• The speaker has a difficult time pronouncing non-English names and words, including "Penna Goddess" and "Charles Hicks".
• The changelog.com team has gained support and sponsorship from various individuals and companies, including Ilya and the sponsors mentioned.
• The team is going full-time and encourages listeners to consider supporting them through membership.