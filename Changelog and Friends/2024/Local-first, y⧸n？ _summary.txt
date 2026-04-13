• Kurt Mackey explains how he approaches explaining Fly to developers, depending on their generation and experience.
• Kurt discusses the limitations of platforms like Heroku and Vercel, and how Fly aims to provide a no-limits platform for developers.
• The hosts welcome local first aficionados Johannes and James, who have previously discussed local first on the podcast.
• Johannes and James discuss their recent blog post (in progress) about the future of local first for all kinds of apps.
• The group debates the definition of "local first" and whether the term "web" should be included.
• Definition of local first software and its characteristics
• Martin Kleppman's simplified definition of local first software
• Challenges of building local first software in the browser
• The web as an anti-local first platform
• Local first as a spectrum and an aspiration, not a binary concept
• Examples of software that are already well on their way to being local first
• Reasons for aspiring to local first, including performance, simplicity, and data security
• The importance of a "local first" approach to app development, prioritizing simplicity and user experience.
• Limitations of local first, not suitable for all types of apps, particularly those requiring server-side data.
• Categories of apps where local first makes sense, including:
  • Note-taking apps
  • Personal finance apps
  • Small-scale collaboration tools
• Trade-offs of local first, including scalability and trust issues with larger teams or companies.
• Examples of successful local first apps, such as Obsidian and personal finance apps built with web tech.
• Using native SQLite vs. web-based solutions
• Distribution and deployment challenges with Electron and native apps
• WebAssembly and performance trade-offs
• Local data storage and query capabilities
• Complexity and overhead of distributed systems
• Note-taking and syncing use cases
• Trade-offs between performance, complexity, and customizability
• Discussion of the challenges of building a local-first application and its potential limitations
• Comparison of local-first architecture with a more traditional model that queries data from the server
• Proposal to rename "local-first" to "mostly local"
• Introduction to Timescale and its use of Postgres for various applications, including AI and IoT
• Discussion of the benefits of using Postgres for AI applications, including its extensibility and scalability
• Overview of Timescale's extensions to Postgres, including pg vector scale and pgai, for enhancing performance and enabling developers to build AI applications.
• The host is promoting a product called Eight Sleep, a high-tech mattress cover that uses AI to track sleep biometrics and make adjustments to improve sleep quality.
• The host shares their personal experience with the product, including its ability to boost REM sleep by 62%.
• The host is offering a discount code for Blind Friday, which will get users up to $600 off the product.
• The host also discusses their work on a project called Live Store, which is a successor to a previous project called Riffle.
• The host explains that Live Store is designed to make app state management more efficient and flexible, and that it is being developed in tandem with another project called Overtone.
• The host and James discuss the trade-offs of building a product, with the host taking a long-term approach that prioritizes design and technology over shipping quickly.
• The challenges of building local-first architecture, including handling account cancellations and data synchronization
• The inherent trade-offs and problems in local-first architecture, including the need for a fallback to the server
• The potential for local-first architecture to solve some problems but not others, such as the API problem
• The idea of rethinking the API-centric approach and instead focusing on synchronization mechanisms, using analogies from version control systems like Git
• The potential for apps to adopt a more declarative and Git-like mindset for synchronization, rather than using APIs in an imperative way
• The web has both positive and negative aspects, with capabilities catching up to native platforms but still lacking in certain areas.
• The concept of an origin private file system (OpFS) and its limitations, including accessibility and user control.
• The use of APIs to mount real file systems and folders from the user's hard drive, providing native-like capabilities.
• The benefits of embracing web capabilities, such as progress toward native app-like experiences.
• The challenges of building trust in web apps, including data loss and lack of control.
• The tension between building web apps that are connected-first and local-first, which may conflict with browser vendor goals.
• The importance of treating network connectivity as an optional thing when building web applications
• The challenges of building fully local-first web applications, including integration with services and data licensing
• The need for a hybrid approach that balances local caching with online connectivity
• The limitations of current web frameworks, such as Next.js, in supporting local-first development
• The importance of mindset and assumptions in web development, and how these can hold back technological progress
• Examples of successful local-first applications, such as Overtone, and their potential to inform best practices in web development
• Challenges of building an app with multiple external data sources
• Importance of tackling technical problems upfront rather than moving them under the rug
• Development of a module to reconstruct a history of changes to data
• Creation of Auth Kit by Work OS, a modular authentication platform for apps
• Features and benefits of Auth Kit, including ease of use, customization, and future-proofing of authentication systems
• Discussing the benefits of Offkit and Work OS, including its ability to handle large numbers of users and ease of use
• Challenges and trade-offs of building apps with a "mostly local" or "local first" architecture, including infrastructure and scalability issues
• Comparison to other apps, such as Notion, and their struggles with local-first architecture
• Pros and cons of using a local-first approach, including potential benefits for specific use cases and potential drawbacks for others
• Future prospects for local-first architecture and its increasing adoption and maturity.
• Local-first approach in app development
• Partial syncing of data
• Electric SQL, Power Sync, and Zero Sync as potential solutions
• Notion's complexity and engineering challenges
• Incremental approach to local-first development
• Balancing local-first and traditional development approaches
• Hybrid approaches for specific features or tasks
• Off-the-shelf local-first technologies and emerging solutions
• Incremental adoption and syncing for existing apps
• Challenges with relying on syncing libraries and tools
• Different approaches to syncing, including CRDTs and central authority
• Various tools and technologies for syncing, including yjs, auto merge, firebase, and jazz
• Academic research and the need for practical implementation
• Difficulty in building stable and trusted syncing products
• Examples of syncing challenges, including iCloud sync and Hyperlogical clocks
• The speaker discusses the potential for a future where local data and syncing are no longer necessary, citing the benefits of a multi-tenant approach and a scalable infrastructure.
• The speaker shares their own experience with a local web worker approach, but notes the complexity and mental tax it imposes.
• The concept of syncing and local data is mentioned as a complex problem that needs to be addressed, but the speaker suggests that it may be possible to simplify this process through the use of a multi-tenant approach.
• The speaker mentions a company called Terso, which is building out a scalable infrastructure for multi-tenant syncing.
• The speaker proposes the idea of hosting a web worker backend at the closest data center point to the user, which would reduce the network latency and make it more acceptable.
• The speaker suggests that this approach would allow for real-time analytics and updates, and would make it easier to manage a distributed network.
• Local-first vs server-first architecture
• React server components and their benefits
• Edge nodes and complex server interactions
• Light client apps and streaming live updates
• Boot-up times and optimizing for low latency
• Trade-offs between server-side and local-first approaches
• Challenges of building server-side applications on low connectivity
• The importance of addressing local-first problems in server-side development
• The challenges of building a fully offline-capable app
• The importance of embracing complexity when it comes to building local-first apps
• The fragility of global connectivity and the importance of considering trade-offs
• The future of local-first apps and the potential for them to become more mainstream
• Notion's efforts to build a local-first app and the potential implications for the industry
• The importance of community support and experimentation in building local-first apps
• Trade-offs and the importance of considering the needs of different users and use cases
• Discussing a potential feature at Notion and seeking an interview
• Requesting episode topics from listeners
• Thanking sponsors: Fly.io, Timescale, and Eight Sleep
• Promoting Eight Sleep's Black Friday sales and using a discount code
• Mentioning the team at Work OS