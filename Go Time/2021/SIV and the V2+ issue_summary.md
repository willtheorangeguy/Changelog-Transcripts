• Semantic import versioning (SIV) allows multiple major versions of a module to be used in a single project
• SIV denotes the major version of a module in its import path
• The concept is based on taking the major version out of the time dimension and moving it to the identity axis, making each major version a distinct "module"
• V0 and V1 versions have special significance due to their lifecycle assertion, which affects how Go Modules work and why the issue is referred to as the "V2+" problem
• The "V2+" problem refers specifically to issues with importing modules using semantic import versioning in Go projects, particularly when dealing with V2 or later versions
• SemVer (Semantic Versioning) and its application in Go Modules
• The reluctance of Go Module authors to make it easy for developers to release new major versions
• The assumption that releasing a V2 version is rare, and that a module should be stable by V1
• The strict definition of "stability" in Go Modules and how it differs from other languages/ecosystems
• The historical aspect of Go Module naming conventions (e.g. V0/V1 vs explicit versioning)
• The assumption that without a V suffix, a module is either V0 or V1
• The impact on newer developers who may not expect the jarring nature of Go Module's versioning system
• Go Modules' assumption that a major version bump is rare and only necessary for large teams
• Reluctance among developers to release V1 modules due to the burden of updating dependent codebases
• The cost of migrating to a new module version can be disproportionate to the actual change made, causing user experience problems
• Semver's definition of breaking changes as requiring a major version bump, even if only one file needs to be changed
• Criticism that semver's concept of breaking changes is too rigid and doesn't account for additive changes that may still require updates
• Suggestions that Go Modules' emphasis on semver has led to the proliferation of V0-only modules to avoid user experience problems
• Discussion of potential tooling solutions, such as deprecation mechanisms and better import handling, but acknowledging their current absence
• Discrepancy between semver assumptions and real-world application in Go Modules
• Automatic import path versioning not supported by Go Modules
• Proposal to improve import path versioning rejected by Go Modules authors
• Discussion on deprecation methods and their limitations
• Exceptional use cases for non-semver versioning schemes (calendar-based)
• Potential for package management system issues with commit hashes instead of semvers
• Problems with unsolvable dependency graphs in large codebases
• Go Modules' design assumption that package management systems must solve these problems
• Peter Bourgon's experience with large companies where this issue rarely occurs except at Google and in Kubernetes ecosystem
• Ubiquitous packages in the Go ecosystem causing version incompatibilities
• Kris Brandow's concerns about overloading semver to mean security indicators, advocating for more nuance in tooling and identification of security vulnerabilities
• Discussion on retract directive and its limitations
• The Go ecosystem's reliance on strong dependency management has created significant overhead for maintainers of libraries.
• Go Modules prioritizes the needs of consumers over those of maintainers, leading to burnout and discouraging people from maintaining libraries.
• The V0 proliferation in the ecosystem is causing problems for consumers, including breaking changes and introduced bugs.
• There's a lack of propagation of exclude statements down to the consumer, making it difficult for them to be aware of potential risks in their dependency tree.
• Some maintainers have resorted to renaming their projects or changing import paths instead of using versioning (e.g., V1, V2) to avoid dealing with breaking changes.
• The reliance on vanity domains can create single points of failure and ecosystem impacts if they go down.
• When key individuals in the ecosystem pass away, there's a risk that their domains and projects may be abandoned or become unreliable.
• The discussion focuses on the issues with Go Modules, specifically regarding documentation and usability.
• Kris Brandow criticizes the initial implementation of Modules, stating that technical solutions were prioritized over human-centered ones.
• Peter Bourgon agrees, arguing that package management is a social problem rather than a purely technical one.
• Tim Heckman highlights the complexity of Modules documentation, which can be overwhelming for new users.
• The conversation turns to recommending resources for learning about Go Modules, with Jon Calhoun and others expressing frustration with the current state of documentation.
• Peter Bourgon jokingly suggests that users start by reading academic papers on the topic or getting intoxicated at a liquor store before attempting to learn about Modules.
• Criticism of Go Modules for being too complex and exposing low-level details that are difficult to understand
• Concerns about the introduction of new commands and semantics that conflict with established meanings and usage patterns
• Discussion of the importance of package management systems respecting human intuition and not redefining established concepts
• Comparison between language features (such as error handling) and package management system design, highlighting the need for inclusivity and consideration of diverse use cases
• Warnings about the potential for a "monopoly" in package management systems leading to overstepping boundaries and neglecting certain user needs
• Emphasis on the social aspects of technical decisions, including issues related to inclusion and diversity in the Go community.
• Need for a shift in approach to feedback and criticism within the community
• Importance of accommodating different risk tolerances and workflows
• Difficulty in reconciling differing philosophies and ideas within the community
• Possibility of diverging or forking the project due to irreconcilable differences
• Potential benefits of in-person discussions and collaboration
• Impact of remote communication on community dynamics and decision-making
• The drawbacks and limitations of committee-based decision-making
• The benefits of having a small, cohesive team in decision-making
• The importance of psychological safety and team cohesion in large groups
• The risks of creating factions or opposing views in larger groups
• The potential for benevolent dictatorship to scale poorly
• The trade-offs between input, control, and responsibility in collaborative environments
• Misconceptions about Go being written for non-genius programmers
• The tendency of large groups to average down to the lowest common denominator
• The benefits of small teams (2-3 people) in design and decision-making
• The importance of having a Benevolent Dictator For Life (BDFL) or leader with clear vision and authority
• Debate on committee structures vs. single-leader approach
• Code as a liability and the goal to minimize it