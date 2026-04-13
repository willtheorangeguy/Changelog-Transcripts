• Simey de Klerk's background as an actuary by day and hobby coder by night
• How he got into coding through work with Microsoft Excel and VBA
• His use of podcasts, including The Changelog family, to learn web development in JavaScript
• His experience contributing code to The Changelog's transcripts
• The overlap between actuarial science and data science
• The role of actuaries in calculating risk for insurance purposes
• Similarities between actuarial work and data science, including probabilistically-modeled calculations and machine learning applications
• Discussion about a satirical comedy skit on LinkedIn that highlights the PTSD people experience from the pandemic.
• Actuaries with coding skills can be highly effective and productive in their work by automating repetitive tasks.
• The hosts discuss their own experiences with automation, abstracting, and coding, and how they apply these skills to improve workflows.
• A GitHub issue about auto-improving episode transcripts was opened but sat dormant until a listener, Simey de Klerk, found it during Hacktoberfest and decided to work on the project.
• The conversation touches on the value of learning from online resources, such as Changelog's show on Hacktoberfest.
• Markdown format for transcripts
• Alexandru's transcription process and unintelligible words
• Hacktoberfest history and contributions to the transcripts repo
• Simey de Klerk's experience with contributing to the repo
• GitHub Actions and auto-formatting script development
• Feature implementation details and standardized formatting rules
• linter for text formatting inconsistencies
• timestamp removal from transcripts
• GitHub Actions workflow for automating changes
• implementing auto-commit vs pull request approach
• overcoming issues with commit triggers in GitHub Actions
• learning about Git and GitHub interactions
• finding a solution to impersonate existing users via email address
• Testing a GitHub Action without affecting the main repository
• Functional programming and explicit side effects
• Iterating on code changes using unit tests and functional design
• Refactoring and adding new rules to a formatter using regular expressions
• Implementing test-driven development (TDD) style for iterating on rule sets
• Running the script locally against a local clone of the repo for easy testing
• Discussion around regular expressions (regex) and their complexity
• Importance of readability over cleverness in code design
• Potential improvements to the regex approach, including using a linter framework or combining multiple regex into one
• Adding more cases to the regex, such as handling brand names like GitHub and GitLab
• Issue with batch updates on the Phoenix app side, where some changes may not be reflected immediately
• Proposal for running a cron job to catch any missed updates
• Plan to write a mixed task that loops over episodes with transcripts and checks for new updates
• Problems with regular expression matching URLs
• Limitations of current regular expression and potential edge cases (e.g. opensource.com)
• Fixing the bug by adding test case for opensource.com and modifying regular expression
• Consideration of linking to referenced URLs in transcripts
• Discussion of Changelog Bot updates and standardized formatting
• Humorous mention of blaming Logbot for issues
• Discussing the link between GitHub and their app for syncing show notes
• Identifying broken links in show notes using a script
• Considering how to handle thousands of issues created from dead links (e.g. creating one issue per episode, updating existing issues)
• Evaluating the importance of fixing dead links versus deleting them altogether
• Examining the value of preserving old show notes with potentially broken links for new listeners and potential future reference
• Noting that internet content is ephemeral and can be lost over time (e.g. 4 out of 5 links in episode #200 were no longer active after 6 years)
• Hacktoberfest contributions may be challenging due to low-quality show notes submissions
• Show notes issues include broken links, outdated information, and difficulty in assessing relevance
• Automation of show note maintenance could improve the process
• The team discusses potential solutions for broken links, including labeling them as "broken" or using the Wayback Machine
• Simey de Klerk shares his experience contributing to the project, and the team discusses the value of making it easier for others to contribute
• The conversation touches on the desire to create an online dev setup that can be easily deployed with minimal technical expertise required
• Discussing potential collaboration with GitHub on a project
• Availability of GitHub Codespaces for Changelog.com's infrastructure
• Challenges in contributing to Changelog.com due to unclear vision and dev setup issues
• Possibility of rewriting Changelog.com's codebase in a more mainstream language like Rust or Go
• Jerod Santo's plans to create an API and command line tool for Changelog.com, potentially using Go instead of Elixir
• Development of a web server for the survey game using Go
• Use of sound effects in the web UI, specifically in the Jeopardy game
• Creation of a Family Feud style game show format with a UI and scoring system
• Open-sourcing of the Go-based web server on Changelog's account
• Discussion of learning Go again for future projects, including the Changelog command line tool
• Feedback from Mat Ryer on Jerod Santo's code
• New feature added to the website: subscription notification for transcript publication
• Changelog Bot to be used to format the transcript