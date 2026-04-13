• Ilya Gregorik discusses his work at Shopify on securing e-commerce checkouts from sophisticated attacks
• David Hsu, founder and CEO of Retool, describes their ideal user: developers who focus on delivering value to the business, not those who are opinionated about specific tools
• Retool's goal is to become more well-known outside of Silicon Valley, where they have strong word-of-mouth recognition
• Ilya Gregorik returns to the show, discussing his work at Shopify, specifically on APIs, infrastructure, and checkout security
• The conversation turns to the compliance aspect of checkout security, which Ilya Gregorik was not expecting to work on
• Founding PostRank in 2011 and developing a better search algorithm by aggregating social signals
• Acquisition by Google and work on Google Analytics and infrastructure
• Work on Google Fi and the problem of objectively quantifying performance
• Leadership of the W3C Web Performance Working Group
• Joining Shopify and work on custom storefronts and APIs
• Development of Hydrogen, a remix-based stack for building custom experiences
• Work on API infrastructure and performance capabilities
• Exploration of technical infrastructure, including application stacks and checkouts
• Discussion of Core Web Vitals and its relevance to performance metrics
• Defining and measuring website performance metrics
• The importance of real-world measurements and aligning on common definitions
• The evolution of Web Vitals and its expansion to include interactivity metrics
• The role of Web Vitals in providing a shared definition of good website performance
• PCI (Payment Card Industry) security requirements and compliance
• The shift from PCI v3 to v4 and the use of iFrames to outsource payment processing
• Stripe elements and the PCI v3 standard
• PCI v3 limitations in protecting payment pages
• Skimming attacks and mage card attacks
• PCI v3 section 643 requirements for parent page security
• Inventory management of scripts on parent pages
• Content security policy and subresource integrity
• Challenges of implementing PCI v3 requirements for third-party scripts
• Difficulty in managing and inventorying third-party vendor scripts
• The speaker needs to understand the chain of dependencies and CSP policy for a specific project
• The speaker is unsure about how to obtain the hash of content from a partner and ensure integrity
• The speaker is working with Augment Code, an AI coding assistant for professional software engineers
• Augment Code helps companies like Lemonade and Webflow with complex code bases
• The speaker discusses the importance of context-aware AI in software development
• Augment Code is being used to improve software quality and liberate companies from tech debt and security gaps
• The speaker mentions Shopify's approach to providing stronger control and behavior over checkout experiences
• Shopify's hosted checkout experience provides a base UI that can be customized with apps and custom components
• Restricting third-party scripts in top-level page
• Introducing sandboxing to isolate third-party content
• Using remote DOM and web workers to provide extensibility
• Controlling data exposure and consent for third-party access
• Rebuilding APIs to accommodate web worker limitations
• Providing a bridge for safe and approved interactions between parent and isolator workers
• Balancing functionality and security in the sandbox environment
• Merchants are using a sandboxed primitive for checkout functionality
• Upgrading safety and reliability for checkout capabilities
• Providing guarantees for customizations and API changes
• Improving performance and security through sandbox execution
• PCI compliance through isolated context execution
• 99.9% of merchants are now using the new platform
• Rolling out the new platform required rebuilding capabilities and recreating APIs
• PCI v4 compliance does not guarantee complete prevention of skimming or attacks
• The issue of antivirus programs not being able to detect malicious code is discussed
• The concept of "watching the watchers" and the difficulty of detecting malicious activity
• The implementation of security measures, such as PCI compliance, to prevent attacks
• The idea that even with security measures in place, attacks are still possible but more difficult to execute
• The Shopify approach to security, including the use of remote DOM and sandboxing
• The development of the remote DOM library as an open-source project
• The potential for browser-based security measures, such as content security policy and SRI, to be improved
• The identification of gaps in browser-based security, including the inability to pass integrity hashes for module imports
• Upstreamed patches for SRI support in Chrome and Safari
• Implemented "require SRI for" capability in Chrome and Safari
• Allows for report-only mode to detect missing SRI attributes
• Enables reliable signal for identifying security issues
• Reporting endpoint for CSP violations can be a separate origin or a third-party service
• "Require SRI for" works similarly to CSP violations in terms of reporting
• Can be used to detect missing SRI attributes in script resources
• Implementing a Content Security Policy (CSP) to ensure the integrity of first-party content in a Shopify checkout
• Isolating third-party content in an iframe to prevent potential security breaches
• Using a sandbox and technology to deploy the same pattern of isolating third-party content in admin and checkout
• Discussing the benefits of isolating content, including better security assurances, performance, and upgrade ability
• Exploring the potential of using web workers as a more secure and isolated environment
• Highlighting the need for the industry to think through and standardize APIs for web workers to prevent reinventing the wheel
• Agent interactions in checkout and commerce
• Model Context Protocol (MCP) and its potential applications
• Human interaction in AI-driven checkout processes
• Security and compliance implications of agent-driven payments
• Future of checkout with agents driving meaningful portions of the experience
• Rapid advancements in AI and software engineering, changing the definition of software engineering
• Problem definition and the importance of clarifying intentions
• Rubber duck programming and collaboration in coding
• Securing e-commerce checkouts and the challenges involved
• E-commerce sales and the high stakes for security
• Sponsorship and upcoming projects (Retool, Augment Code, Fly.io and Changelog's album "After Party")