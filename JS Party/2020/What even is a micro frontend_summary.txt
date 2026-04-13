• Definition and background on micro frontends
• Michael Geers' experience with implementing micro frontends at neuland in 2014-2017
• Creation of the term "micro frontends" and the website microfrontends.org
• Explanation of micro frontend architecture as a team structure, not just code structure
• Comparison to microservices and trade-offs between developer simplicity, organizational alignment, and operational complexity
• Challenges of frontend architecture with multiple teams using different JavaScript frameworks
• Decoupling and integration points between micro frontends
• APIs as contracts between teams, and providing fallbacks for broken fragments
• Sweet spot for organizational/team size to adopt micro frontend architecture
• Cross-functional team splits, example e-commerce shop with two teams handling different stages of the checkout process
• Dividing boundaries along user's perspective and modes (e.g. routing, customer tasks)
• Integration types: server-side solutions (e.g. links between teams), client-side solutions (e.g. meta-routing frameworks)
• Composing micro frontends using techniques such as server-side includes or Web Components
• Techniques for server-side integration of micro frontends
• Comparison of various libraries and frameworks (Single-Spa, Tailor, Podium) for handling integrations
• Independent deployment and autonomy in updating user interfaces without coordinating with other teams
• Use of Edge Side Includes (ESI) or Server-Side Includes (SSI) to dynamically assemble and cache UI components at runtime
• Runtime stitching vs. build-time stitching and pre-compilation options (JAMstack, Gatsby)
• Coordination challenges and failure modes in micro frontend architectures
• Fallbacks and waiting for slow fragments during server-side integration
• Self-contained systems approach to minimize dependencies between teams' data stores
• Replication between systems for disaster recovery
• Micro frontends forcing adoption of microservices architecture
• Decoupling data and frontend workloads across multiple teams
• Using composition techniques like single-spa without microservices
• Managing data cascades and pre-processing layers in micro frontends
• Mitigating performance implications with shared frameworks and code splitting
• Runtimeless frameworks like Svelte as a solution to framework bloat
• Inter-micro-frontend communication using event systems and custom events
• Event bus style approach for sharing code between teams
• Avoiding shared libraries and promoting internal open source projects instead
• Design system as a crucial part of micro frontend architecture
• Importance of documentation and versioning in shared libraries
• Organizational structure and communication challenges with large teams
• Benefits of splitting large teams into smaller, isolated teams