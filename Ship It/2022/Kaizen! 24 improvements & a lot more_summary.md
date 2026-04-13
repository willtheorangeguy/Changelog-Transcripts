• Episode chapters feature in IDv3x Elixir library
• Jerod Santo has 24 improvements in this episode of Kaizen
• Discussion on the concept of continuous improvement and "Always Be Improving" (ABI)
• GitHub pull requests as a bottleneck to shipping code quickly
• Proposal for a different pull request behavior, where commits can be grouped together with metadata
• Discussion of the 24 improvements made in Kaizen
• Review of commit 19, which fixed an unexpected bug in Jerod's code
• Explanation of Scribe, a feature that improves the reading experience for Medium posts
• Integration of Open Podcast Prefix Project (OP3.dev)
• Cleanup and removal of unnecessary features, including the iTunes owner element to reduce spam
• Shout-out to Josep "Pep" for his pull request #415, which was merged after being open since May 2022
• Decision to send Pep a Kaizen T-shirt as a reward
• Discussion of Noah's two pull requests and consideration of sending him a Kaizen T-shirt as well
• Authentication issues prevent remote Docker engine from pushing images
• Fly/Docker setup solves local Docker for Mac slowness and disk space usage
• Using a shared Docker host on Fly to run CI and development environments
• Dagger-related improvements planned, but will be discussed later
• RSS feed support for specific topics added in pull request 430
• Consumers may not always be the listeners of content, but rather publishers or platforms
• Idea for a publishing bot to mirror topic feeds into different indexes and platforms
• Contributing guide created to make it easier for people to contribute to Kaizen development (Pull request 434)
• Discussing stock levels of Kaizen T-shirts available for sale on the store
• Reviewing Pull Request 431, which aims to move contributing information out of the readme file and into its own place in the repo
• Installing a Mac
• Pull requests and reviewing code
• Verified commits and DCO (Developer Certificate of Origin)
• Using 1Password for biometrically signing Git commits
• SSH key management and rotation
• Security best practices for SSH keys and passphrases
• Discussion of SSH key management with 1Password
• Comparison of creating SSH keys within 1Password vs. using external tools and importing the key
• Authentication methods: YubiKey OTP, UI Verify, and Google Authenticator
• Challenges with authentication token backup and restoration
• Pros and cons of cloud-based backups versus direct phone-to-phone transfer
• The importance of authenticating commits in GitHub and other applications for supply chain security
• Discussion on migrating to 1Password and its integration with infrastructure
• Concerns about relying on a cloud-based service and potential backup plan
• Proposal for open-ended discussions on GitHub before each episode of Kaizen
• Experimenting with using badges from shields.io to show the status of discussions
• Alternative methods, such as labels, could be used instead
• Mermaid flowcharts and interactive diagrams
• GitHub support for native Mermaid rendering
• Mermaid.live editor and its features (live preview, icons, etc.)
• Using Mermaid to document infrastructure setup
• Creating a PR with a diagram to capture changes over time
• Discussion of tools and technologies used (Fly, GitHub Actions, Sentry, DockerHub)
• Arrows that move and change in Dagger
• The ability to run CI/CD locally with Dagger version 0.3
• Support for multiple languages (Go, Node.js, TypeScript, CUE) with Dagger version 0.3
• Plan to add a pipeline written in Go using the Dagger Go SDK 0.4
• Comparison of Dagger to Docker and BuildKit
• Discussion of Dagger's transition from being built on top of BuildKit to its own engine
• Discussing the potential for reducing CUE and makefiles with Magefile in Go
• Reviewing progress on Kaizen episodes and considering listener feedback
• Planning future contributions to Changelog, including external contributors and infrastructure improvements
• Introducing low-hanging fruit issues for new contributors to work on
• Encouraging listeners to join the community through changelog.com/community or GitHub discussions
• Discussing a potential state of the 'log episode covering the Changelog's growth and development