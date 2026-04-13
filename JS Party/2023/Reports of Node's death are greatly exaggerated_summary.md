• Node.js governance structure
• Introduction to Matteo Collina (Node.js TSC vice chair) and James Snell (Node.js contributor)
• Overview of Node.js contributors and their role
• Background on Chris Hiller's early morning recording session
• Introduction to the topic: Node versus Bun, Node versus Deno comparisons
• Context setting for understanding Node's technical structure and governance
• Governance structure prevents a single company from taking over Node.js
• Contributions to Node.js are driven by individual contributors, not a centralized roadmap
• History of corporate involvement in Node.js has led to careful consideration of governance
• Drama surrounding Bun's launch was manufactured on social media, not within the projects themselves
• Multiple JavaScript runtimes and engines exist, each with different trade-offs and priorities
• Nodes' decisions are based on trade-offs and use cases, rather than competition with other projects.
• Twitter drama and controversy surrounding Bun and its comparison to Node.js
• Importance of understanding the differences between new technologies and established ones
• Challenges of maintaining backward compatibility in a rapidly evolving technology landscape
• Comparison and criticism of Bun's 1.0 announcement and marketing claims
• Discussion of the Node.js project's complexity, scale, and stability guarantees
• Performance vs correctness in software development
• Node.js's approach to prioritizing stability and observability over performance
• Challenges of balancing observability and tracing capabilities with no overhead
• Comparison between Bun and Node.js on performance and standards compliance
• The impact of cloud computing companies' business models on the investment in performance
• Node.js's ability to handle concurrent requests has been misunderstood by some who claim it's inefficient
• AWS Lambda's cost model is criticized for charging even when CPU is idle, with a limit on concurrent requests per account (256 by default)
• At scale, serverless computing can be costly and may not always provide the best performance or observability
• Performance optimization should consider the company's velocity and ability to ship features rather than just reducing costs
• Investing in performance may not be worthwhile for early-stage startups or companies with simple web apps, but can pay off for those at high scale with compute-intensive workloads
• Discussion of performance benchmarking for Deno, Bun, and Node.js
• Criticism of current benchmarking practices and lack of apples-to-apples comparisons
• Analysis of specific cases where certain features or defaults may be contributing to performance differences
• Concerns about the readiness of Bun for production use due to issues with test frameworks and dependencies
• Comparison of Deno and Bun's install performance, including the role of safety checks and trade-offs between security and speed
• Node projects' default behavior and assumptions about dependency chains
• Pnpm options to get same behavior as Bun
• Balancing performance vs security in product decisions
• Backward compatibility challenges in Node and other projects
• Hidden boundary layers between public and private APIs in Node
• Monkey-patching and modifying internal C++ layer in Node
• Challenges of making massive performance improvements without breaking ecosystem
• The glob module in Node had issues when switching from an old algorithm to a new one in libuv, causing it to break for some users.
• Breaking Node would not be catastrophic like a "shutdown of the internet", but rather similar to the transition from Python 2 to Python 3, where older versions will eventually stop receiving security patches and updates.
• This would leave behind a large number of projects that won't work on newer versions of Node due to outdated dependencies.
• The use of Zig as a target language for contributors is being discussed, with some considering it an improvement over C++ but also having its own set of issues.
• Commercial open source projects like Deno and Bun have different goals and strategies compared to community-driven open source projects like Node.
• Node maintainership is largely volunteer-based, with only a few companies paying employees to work on Node full-time
• Contributing to Node requires commitment and patience due to its size and complexity
• There are three categories of contributors: paid full-time, paid part-time (but not specifically for Node), or unpaid but interested in contributing
• The website Node TODO is recommended as a starting point for new contributors
• Open JS Foundation hosts contributor days and provides travel funds to help maintainers collaborate
• Amal Hussein has announced her interest in joining the marketing committee at Open JS Foundation to advocate for Node and help with community building
• Matteo Collina has offered to assign unit tests to Amal Hussein if she is interested in writing them
• Discussing the importance of Node.js during Hacktober
• Concerns about corporate ownership and acquisition of projects
• Incentives for venture-backed companies to prioritize commercial interests over community needs
• Challenges for runtime competitors like Deno and Bun due to VC funding and potential conflicts between community and commercial goals
• Balancing community and commercial interests in open source projects
• Discussion about Node.js and its evolution
• Mention of past criticism and resistance to adding new features to the runtime
• Announcement of WebSocket support in Node.js, coming in version 21
• Details on the implementation and testing process for WebSocket in Undici
• Comparison between Bun and Deno's community engagement and marketing strategies
• Caution about prioritizing commercial interest over community voice
• Comparison of Deno and Bun compatibility layers
• Criticism of Deno's marketing claims and lack of performance with its compatibility layer
• Discussion on the importance of consistency in APIs across different runtimes
• Analysis of the impact of splintering in usage (e.g., multiple JavaScript environments) on the community
• Overview of Node.js performance enhancements and iteration challenges due to scope and lifetime of the project