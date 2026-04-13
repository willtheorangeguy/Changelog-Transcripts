• Introduction to JS Party and Changelog
• Sponsorship announcements (Fastly, Rollbar)
• Micro front ends: discussion on the concept, its history, and the guest expert's experience with it
• Guest introduction: Michael Gears, author of "Micro Front Ends in Action"
• Career background and introduction to micro front ends for Michael Gears
• Explanation of verticalization and its implementation in an e-commerce project by Michael Gears' company
• The concept of micro front ends was initially developed in 2014 and refined over time.
• Micro front ends involve multiple teams working on different aspects of a frontend, delivering their piece of the frontend to be assembled together.
• Team structure is crucial in micro front end architecture, with cross-functional teams being more effective than one large team or monolithic codebase.
• The trade-offs of micro front ends are similar to those of microservices: operational complexity and developer simplicity vs. organizational alignment.
• Micro front ends introduce redundancy, which can be mitigated by planning integration points and managing code size and load on the browser.
• Microservices changed where problems occur in software architecture
• Integration contracts and APIs are crucial in microservices
• Micro frontends introduce new fault lines and require clear connections between teams and components
• Cross-functional team splits can be beneficial, especially for e-commerce sites with multiple customer journeys
• Boundaries between teams should be based on user needs and tasks, rather than technology or skill sets
• Classical pages and routes can serve as indicators for team boundaries, but may not always be perfect
• Server-side and client-side solutions for integrating multiple micro-frontends
• Meta-routing frameworks (e.g. SingleSPA) for navigating between micro-frontends
• Server-side includes (SSI) for assembling UI fragments from different teams
• Web components for client-side composition of UI fragments
• Impact on deployment, including autonomy and testing
• Operational complexity of managing independent web servers and integration layers
• Discussing runtime vs build-time stitching in micro frontends
• Exploring the feasibility of pre-compiling micro frontends like Jamstack or Gatsby
• Integrating server-side includes (SSI) for micro frontend stitching
• Limitations and trade-offs of independent deployment in micro frontends
• Premature optimization debate: is independent deployment necessary?
• Microservices adoption patterns, comparing to monoliths
• Current adoption of micro frontends in various companies (IKEA, Zalando, Spotify, etc.)
• New failure modes in micro frontend architecture (coordination problems, cascading timeouts)
• Emerging approaches and systems addressing these failure modes
• Designing self-contained systems with minimal reliance on central data stores
• Replication between systems for redundancy and fail-safe design
• Microservices architecture as an outcome of microfinance implementation
• Debate over whether microfinance is synonymous with microservices and UIs
• Use cases for microfrontends without a tight coupling to microservices
• Techniques for optimizing frontend data queries and reducing cascading requests
• Trade-offs between flexibility, performance, and data model complexity in large applications
• Mitigating megabytes of JavaScript being loaded into browsers
• Strategies for reducing framework load and improving performance
• Use of smaller libraries and runtime-less frameworks like Svelte
• Code splitting and delivery of necessary components per team
• Inter-micro front-end communication methods (PubSub, custom events)
• Best practices for decoupling micro-frontends
• Event-driven architecture and event bus style approach
• Code sharing between teams and business logic shared between teams
• Best practices for micro frontends and code reusability
• Organizational structure and communication challenges in large-scale development
• Importance of proper documentation, versioning, and API design
• Trade-offs between team autonomy and organizational overheads
• Discussion of shared libraries and design systems
• Importance of design systems in building larger applications with consistent user experiences
• Micro Frontends and the need for a unified design system to avoid disjointed experiences
• The book "Micro Frontends in Action" and its availability through Manning's early access program
• Giveaway of free ebooks and discount code for 40% off Manning's entire catalog
• Episode discussion on Micro Frontends in Action
• Giveaway of a free ebook copy for commenting on the episode
• Show notes link to the episode discussion
• Acknowledgments to guest Michael Gears and co-host K-Ball
• Music credits
• Sponsor acknowledgments (Fastly, Linode, Rollbar)
• Closing remarks