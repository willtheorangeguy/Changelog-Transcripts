• Definition and characteristics of static site generators (SSGs)
• Comparison between SSGs and CMS systems
• Evolution of SSGs from simple content generation to more dynamic websites
• Relationship between SSGs and JAMstack technology
• Advantages of using SSGs, including faster page loading times and reduced server requirements
• Disadvantages of using static site generators (SSGs) include reduced flexibility for dynamic user interactions and limitations on handling frequent database updates.
• Criteria to consider when deciding whether to use an SSG: how frequently content changes, user flexibility needs, and who will be accessing and updating the content.
• Tools are available to enable more flexible CMS capabilities with static sites, but additional complexity is introduced.
• SSGs may not be suitable for projects requiring multiple roles, users with different technical expertise, or frequent updates from non-technical contributors.
• Introducing a separate editing interface can help address some of these limitations.
• Next.js is a tool for creating websites with server-side rendering
• Next.js allows for both static site generation and dynamic server-side rendering
• It has a flexible developer experience for building complex applications or simple static sites
• However, setting up TypeScript support can be challenging
• Next.js can be used to build interactive applications like nteract/play, but also static sites like nteract.io
• Other front-end frameworks like Nuxt (inspired by Next.js) offer similar features and flexibility
• Jekyll is a static site generator from the Ruby ecosystem that is mature and has a strong plugin ecosystem
• Jekyll is easy to get started with, but requires installation of Ruby and other dependencies.
• Discussion of Jekyll limitations and potential replacement with 11ty
• Introduction of 11ty as a JavaScript-based alternative to Jekyll
• Comparison of Jekyll and 11ty features and functionality
• Mention of Panini as another simple, JavaScript-based SSG option
• Discussion of Panini's pros and cons, including its flexibility and ability to generate HTML emails
• Brief overview of Gatsby, including its popularity and potential use cases
• Example case study of using Gatsby to build a fast e-commerce site
• Predictions for the future of static site generators (SSGs) 
• Combining SSGs with API-based functionality
• E-commerce applications moving to SSGs and API-based systems
• Need for more user-friendly SSGs that don't require technical knowledge
• Decoupling content from codebase in SSGs
• Bridging the gap between dynamic and static site generation
• Improving documentation tools, particularly for API documentation
• JAMstack approach: decomposing traditional back-end into APIs, allowing static site generators to create initial view and skeleton, with dynamic content fetched from API
• Stripe and other third-party APIs used as substitutes for server-side functionality in JAMstack applications
• Advantages of JAMstack: better performance, security, and developer experience
• Challenges to hacking a static site generator, such as Nginx or S3 buckets serving the site
• White hat challenge issued by Kevin Ball to listeners to hack his site and receive bug bounty