• Homebrew's 1.0 release and changes, including moving from /usr/local to /usr/local/Homebrew
• Autoupdate feature for a cleaner /usr/local
• 6,000 unique contributors to Homebrew
• Linuxbrew, a fork of Homebrew
• Sponsorships from Rollbar, Toptal, and Linode
• Mike McQuaid's background and involvement with Homebrew, starting from his college days and work on Gentoo and KDE
• Mike's transition from using Linux to Mac, and how it led to his work on MacPorts and eventually Homebrew
• The interviewees discuss their early experiences with Macs and open source software, with Mike McQuaid on Leopard and Jerod Santo on Ubuntu.
• Mike McQuaid's transition to lead maintainer of Homebrew and the shift from a democratic to a meritocratic governance model.
• The impact of Max's departure from Homebrew and the transition to a more structured leadership model.
• The split of Homebrew into two repositories (Homebrew/brew and Homebrew/core) and its effects on contributor patterns.
• The current structure of Homebrew, with a lead maintainer (Mike McQuaid) and a group of core maintainers, and the role of meritocracy in decision-making.
• The need to separate the package manager from the packages in Homebrew
• Splitting the Homebrew repository into separate repositories
• Analytics introduced in March to track usage and inform future design
• Separating package definitions to support cross-platform and old platforms
• Prioritizing support and options based on user data from analytics
• Impact on GitHub's use of Homebrew and employing Mike McQuaid
• Introduction of Homebrew 1.0 release with new features and highlights
• Limitations of watchers and stars for maintainers
• Importance of metrics tracking for decision-making
• Homebrew's use of Google Analytics for metrics tracking
• Controversy over opt-out analytics and concerns about data collection
• Effects of controversy on open source maintainers and the community
• Benefits of transparency in metrics tracking and potential for an open dashboard
• Statistics on Homebrew user activity and popular packages
• Discussing user experience with Homebrew and the importance of focusing on speed
• Auto-updating features in Homebrew, including checking for updates in the background and running updates during the installation process
• Efforts to optimize the auto-update process, including moving the update code from Ruby to Bash and improving the performance of git fetch operations
• Design decisions regarding auto-updating, including the separation between update and upgrade commands and the decision not to auto-run upgrades
• Comparison of Homebrew's auto-update process to other software, including Firefox and its large download size
• Conflicting goals of package managers: balancing what users want and what they need
• Running Homebrew as root: a bad idea due to security risks and lack of privilege dropping
• Sandbox implementation to prevent arbitrary file modifications
• Default location of Homebrew repository changed from usr/local to usr/local/Homebrew
• Benefits of moving repository include easier maintenance and reduced clutter in usr/local
• usr/local/cellar directory used for storing binaries and symlinking to usr/local
• Permission issues with usr/local ownership reset by Apple's OSX installers and other tools
• Solution to create root level directories in usr/local and allow users to take ownership
• Homebrew's importance to developers and the complexity of its ecosystem
• Mike McQuaid's experience working on Homebrew leading up to its 1.0 release
• Homebrew terminology (tap, cask, brew, formula/formulae)
• Taps as third-party repositories for formulae or Homebrew extension commands
• Shift in perspective on taps, from being an afterthought to a central part of the Homebrew ecosystem
• Cask, a package manager for Mac applications, and its integration with Homebrew
• Unification of Homebrew and Homebrew Cask, including de-vendoring code and sharing maintainers and testing
• Brew Bundle: a tool for creating and managing lists of Homebrew packages, Cask packages, and Taps
• Standardizing software installations with Brew files
• Thoughtbot Laptop project and Strap project: custom system bootstrap scripts
• Package File/Dependencies: a proposed format for declaring project dependencies across package managers
• Keg: the directory where Homebrew installs packages
• Cellar: the directory where Homebrew stores packages
• Pints: a non-existent concept in Homebrew
• Glossary: a proposed resource for explaining Homebrew terminology
• Changes to terminology in Homebrew
• Debate over the need to simplify or rename certain concepts
• The value of maintaining a unique personality and theme in the project
• The redesign of the Homebrew website and its focus on playfulness and fun
• The community's British English preference and its origins
• The importance of having a legal entity to own and manage project assets, provided by the Software Freedom Conservancy
• The benefits of the Conservancy's nonprofit status and tax-deductible donations
• The challenge of managing recurring revenue and donations for the project
• Community outreach and fundraising challenges
• Homebrew's Discourse site for community communication and support
• Relationship between Homebrew and Linux Brew
• Invitation for community members to get involved and help with Homebrew
• Importance of welcoming and inclusive community practices
• The role of leadership in setting a positive community tone
• Discussion of Mike McQuaid's subscription to the email newsletter
• Mention of Homebrew's 1.0 announcement
• Light-hearted joking about pressure to meet Mike's expectations
• Encouragement to listeners to subscribe to the email newsletter