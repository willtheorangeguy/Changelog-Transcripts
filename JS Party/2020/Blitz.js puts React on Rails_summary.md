• Introduction to Blitz.js, a full-stack React framework inspired by Ruby on Rails
• Brandon Bayer's background as a software consultant and his experience building multiple React applications
• The concept of "Ruby on Rails for React" and how Blitz aims to bring similar features to the React ecosystem
• Comparison with other frameworks such as Meteor, Happy.js, and Redwood.js
• Discussion of the manifesto behind Blitz, including 7 core principles:
  • Full-stack and monolithic
  • API not required
  • Convention over configuration
  • Loose opinions
  • Easy to start, easy to scale
  • Stability
  • Community over code
• Blitz separates frontend and backend logic, allowing for static TypeScript and auto-completion without the need for GraphQL in the middle
• At build time, Blitz swaps out direct function imports with API calls, eliminating the need for GraphQL or manual serialization
• The automatically generated API is JSON-based and RPC-style, but can be accessed directly if needed
• Developers have full control over data sent over the wire, as it's simply a connection between the server and client function call
• Blitz handles serialization of objects, including regex, sets, and maps, so developers don't need to serialize manually
• Blitz allows specifying which fields to return in GraphQL queries
• Differentiated from Redwood by not requiring an API, but can be used as a standard API endpoint with token authentication
• Planning to add first-class support for React Native and mobile apps
• Fallback idea of auto-generated client library if native React Native support is not available
• Blitz has loose opinions, meaning it takes a less strong approach than Ruby on Rails and doesn't enforce its opinions strongly
• Supports TypeScript by default but allows JavaScript as an option
• Emphasizes stability, with the goal of having multiple release channels like Ember's stable, beta, and long-term support
• Predictable release cycle for Blitz
• "Community over code" foundational principle
• Community size and aspirations (30 people, 75 contributors)
• Compile step: compiling Blitz code into Next.js code
• Production use cases (a few websites using Blitz in production)
• Sponsorships (Brandon Bayer accepting sponsorships to fund Blitz full-time)
• Relationship with Next.js (Blitz built on top of Next, but adds new features and functionality)
• Code generation and scaffolding
• Compilation step (compiling Blitz code away into Next.js code)
• Serverless deployment options for Blitz
• Comparison of serverless vs traditional deployment methods
• Challenges with serverless implementation (queuing, background processing, cold-start issues)
• Database connection pooling and security considerations
• Potential for a platform to simplify serverless full-stack development
• Prioritization of features and plans for future development (authentication, recipes, plugins)
• Discussion of how Blitz's recipe system works, including virtual DOM diffing and composable components
• Plans for 1.0 release, including built-in auth, recipes, and plugins
• Future features, such as mobile React Native support
• Community involvement, including GitHub issues, Slack community, and contributing guide on the website