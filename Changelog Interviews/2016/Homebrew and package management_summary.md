• Homebrew 1.0 release
• Changes in Homebrew, including no more user local and auto-updates
• History of Homebrew's growth, with 6,000 unique contributors
• Discussion of Linux Brew, a fork of Homebrew
• Interview with Mike McQuaid, maintainer of Homebrew
• Background and origin story of Mike McQuaid
• History of Homebrew, including a previous episode of The Change Log discussing Homebrew in 2010
• Overview of Homebrew's development and release process
• The speaker's experience with Linux desktop environments
• Google Summer of Code and the KDE project
• Transitioning from Linux to Mac
• Introduction to MacPorts and homebrew
• Maintaining homebrew as a key contributor
• The speaker's history with Macs and their preferences for OSX and TextMate
• Transition of leadership from Max to the current lead maintainer
• Role of the lead maintainer and the change from a democratic to a meritocratic governance model
• Implicit vs explicit power structures in open source projects
• The current lead maintainer's assumption of the role and the complaints that followed
• The contributors tab and its limitations in reflecting contributors' efforts beyond code contributions
• The use of contributor graphs to visualize contributions and involvement over time
• Split of Homebrew into two repositories: package manager and formulae
• Differences in contribution patterns between the two repositories
• Shift in focus to package manager with 1.0 release
• Transition from flat structure to lead position with Mike McQuaid
• Definition of roles: maintainers, contributors, and users
• New structure with lead position mainly for decision-making
• Gathering analytics and influence on product direction
• Relationship between GitHub and Homebrew with lead maintainer employment
• GitHub's involvement in Homebrew development and Google Summer of Code students
• The speaker discusses their workflow, stating they don't do Homebrew work during GitHub time, but instead do it in their free time.
• Daniel Reed, head of design at TopTow, talks about the benefits of using TopTow for designers, including the ability to switch up their lifestyle and work on multiple projects.
• Lee and Mike discuss the new Homebrew 1.0 release, including the separation of repositories and the introduction of analytics for tracking usage.
• The onus behind splitting the repositories was to separate the package manager from the packages, allowing for greater stability and the ability to update packages without breaking others.
• The new release includes features such as separate repos, a community site, and the move out of user local Homebrew.
• Discussing the package manager's rolling release approach and its impact on star count
• Mention of Linux Brew and separating package manager from package definitions for cross-platform support
• Introduction of analytics dashboard and its ability to track user counts, command usage, and package popularity
• Importance of analytics in informing future design and prioritizing support for different platforms and packages
• Comparison with hub stars and watchers as indicators, but not providing deep enough insights
• Use of analytics to track error counts and make decisions on maintenance and feature development
• Sending packages to the "boneyard" for maintenance and removal
• Importance of metrics tracking for making informed decisions in software development
• Debate over Homebrew's analytics being opt-out rather than opt-in
• Vocal minority criticizing the decision and sending personal emails to the maintainer
• Effect on open-source maintainers and the community, including driving people away and killing projects
• Discussion of the importance of diversity in open-source and the impact of abuse on underrepresented groups
• Sharing of statistics on Homebrew usage, including user numbers, package popularity, and version breakdown
• Proposal for an open dashboard for analytics data, and the feasibility of automating database dumps for improved transparency
• Use of tracking stats to determine the importance of work being done
• Ability to put tracking stats in papers to demonstrate the value of work
• Auto-updating feature and its performance
• Optimization of auto-update process, including moving from Ruby to bash and leveraging the GitHub API cache layer to speed up git fetch operations
• Impact of controlling both sides of the API on the development process
• Importance of speed in user experience, particularly when it comes to updating software
• Conflict between user desire for convenience and need for security updates
• Homebrew's approach to updating, including separation of update and upgrade commands
• Auto-updating mechanism, including background updates and optimization for no-op cases
• Trade-offs between user convenience and security, including potential for systems to be compromised if updates are not prioritized
• Homebrew's security risks when run as root
• Homebrew's sandbox feature and its limitations when run as root
• Decision to disable sandbox for root users due to security concerns
• Changes to default location of Homebrew repository from user local to user local/homebrew
• Reasoning behind keeping the default location of binary packages the same to avoid massive rebuild process
• New flexibility in moving repository files and not cluttering user local with unrelated files
• Homebrew's installer issues with OSX and permissions
• Solution: creating root level directories and user local, and having users change ownership
• Permission issues caused by Apple's OSX installers and other tools
• Homebrew's impact on developers and the community
• Terminology: taps, casks, brew, formulas, and formulae
• The process of tapping a third-party repository in Homebrew
• Homebrew formulae and taps
• Taps as a central concept in Homebrew, allowing for private repositories and easier maintenance
• Cask, a command for installing Mac applications, and its integration with Homebrew
• Efforts to unify Homebrew and Homebrew Cask, including de-vendoring code and moving package manager code into Homebrew
• The speaker discusses their use of Homebrew and its features, including cask and brew bundle.
• The speaker explains the benefits of brew bundle, which allows for the creation of a single file that lists installed packages and their versions.
• The speaker mentions the use of brew files in ThoughtBot's laptop project and their own project, Strap.
• The speaker discusses the potential for a standardized format for brew files that could be used across different package managers.
• The speaker references RVM's similar goals for a unified package manager.
• The speaker introduces the concept of "kegs" in Homebrew, which refers to the directory where installed packages are stored.
• Package managers and their file structure organization
• Homebrew's unique approach to package management, including separate prefixes for each package
• The benefits of Homebrew's approach, including side-by-side installation of conflicting packages
• The concept of "kegs" and "pints" in Homebrew, and their relation to package management
• The debate over renaming Homebrew terminology to make it more accessible to new users
• The suggestion of creating a glossary to define Homebrew terminology and its analogies
• The role of branding and theme in Homebrew's identity, including its use of beer-themed terminology
• Danielle's design changes, including new icons, aim to create a more playful and fun vibe for the project
• The project's use of British English and emphasis on being "difficult" is a nod to its Scottish and British roots
• Homebrew's decision to join the Software Freedom Conservancy provides a legal entity to own project assets and defend against lawsuits
• The conservancy's 501c3 status makes it easier to accept tax-deductible donations and accept recurring revenue
• The project's current lack of recurring monthly revenue is a challenge, but fundraising efforts are underway
• The project's low cost and open-source nature are benefits, but also raise questions about financial stability and sustainability.
• Financial limitations of Homebrew and the impact on its functionality
• Discussion of fundraising and potential future collaborations
• Importance of community outreach and growth
• Limitations of having no recurring revenue
• Introduction of the community discourse site and its benefits
• Clarification of the relationship between Homebrew and Linux Brew
• Plans for a unified package manager for OSX and Linux
• Invitation for community members to get involved with Homebrew
• Importance of being nice in the open source community
• Retaining and welcoming people from diverse backgrounds
• Leadership and behavior in the community
• Universal "mini-so" (being nice) as a guiding principle
• Email newsletter (Change Law Weekly) for open source news and updates
• Threats of sending nasty emails
• Promotion of subscribing to the show's email list
• Mention of the homebrews 1.0 announcement
• End of the show and farewell to listeners