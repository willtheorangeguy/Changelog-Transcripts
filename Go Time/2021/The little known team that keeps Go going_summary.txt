• History of the Go Tools Working Group
• Creation of the group at GopherCon 2018 to address need for modernized tooling around modules
• Initial brainstorming session attended by multiple guests and focused on tools, workflows, and areas for improvement
• Goals of the group include standardizing and improving tooling, reducing fragmentation, and becoming a leader in tool development rather than following others
• Current mandate or charter is open-ended and emphasizes collaboration, feedback, and discussion among developers and users of Go tools
• Scope includes code analysis, compilers, editor plugins, language servers, and standard libraries, as well as broader topics like tooling for modules and language features
• The group has been used for testing, proofreading, and design discussions, with an open agenda and no registration requirements.
• The Tools Working Group was formed after GopherCon where the Go team demoed the package site
• The group has worked on various tools including the go command, package discovery site, and Gopls editor integrations
• Discussion and experimentation around the go command, such as changes to workspaces and replace directives, have been key topics in the working group
• The group is open to discussing any tool or idea, even if it's not officially part of the Go project
• Experimentation and experience reports are encouraged, with tools like Gohack being used as examples of how ideas were developed and improved through discussion in the group
• The group has facilitated collaboration between the Go team and external developers on issues like go install package at version
• Tools Working Group meetings occur approximately once per month
• Main topics discussed: command go, Gopls, package site, generics, and their interactions/impacts on each other
• The group has a super-open agenda and encourages discussion and participation from all members
• Current projects being worked on include multi-module workspaces, generics, and updating existing tools to support new features
• Package site (pkg.go.dev) is a discovery site for Go packages and modules that replaces GoDoc.org
• Gopls is an LSP (Language Server Protocol) implementation for Go, and its integration with package site is important
• Creation of moddoc by Marwan Sulaiman to address lack of observability and shared modules in Go Modules
• Importance of experimentation and showing people what can be achieved
• Deprecation of module versions and how they should be viewed
• Process for getting something developed as a tool, including proposals and acceptance
• Involvement of the Tooling Group and official process for bringing ideas to the group
• Ad-hoc approach to proposing new tools and integrating them into main systems
• Interaction between the Go Tools Working Group and the open source Go Tools Team at Google
• Importance of focused expert voice and listening to community input
• Buffering role in representing experiences and expertise from colleagues
• Growth of communication effectiveness within the group over time
• Increased importance of getting feedback from people with diverse perspectives
• The Go Tools Working Group has become an effective communication channel for gathering feedback and improving tooling.
• The group's focus on the developer experience has led to improvements in how tools work with Modules and Go Packages.
• Go Packages abstracts whether GOPATH or Modules are being used, making it easier for tools to use them.
• The go list command is a key part of Go Packages, allowing tools to load packages from disk, build them, and download dependencies as needed.
• The Tools Working Group has helped improve coordination between tool authors, leading to better adoption and integration of new tools and features.
• The group's focus on the developer experience has been essential in making working with Modules a more pleasant experience.
• The Tools Group's role in resolving issues with semantic info versioning (SIV) and other newer features of Modules.
• How the group helps by finding ways to improve user experience without changing core technology.
• The benefits of discussing complex issues on the Tools call, including nuance and constructive dissent.
• Importance of welcoming feedback and disagreement on the Tools call and Slack channel.
• The role of early feedback and proposal discussion in the Tools Group for success.
• Challenges in maintaining an open and inclusive conversation within the group.
• How the Tools calls serve as a good forum for discussing challenging topics.
• Dangers of fragmentation in software development tools
• Importance of standardizing workflows and artifact production
• Benefits of having a shared feature set across different editors and tools
• Participating in the Tools Working Group: meetings, calls, mailing list, Slack channel, and GitHub repository
• "Unpopular Opinions" segment on Go programming language and tooling
• Comparison between Gerrit and GitHub PRs for contribution and review workflows
• Importance of face-to-face interaction or video conferencing for effective communication and collaboration
• Perception that Go is becoming too complex due to its growing popularity and evolving ecosystem
• Discussion of Gerrit being unpopular
• Alternative tools to Go being considered better in some cases
• TinyGo's potential for frontend development with Go
• Use cases for Go in embedded systems and frontends
• Debate on writing frontends in Go, with differing opinions
• Update on new members joining the Tools channel