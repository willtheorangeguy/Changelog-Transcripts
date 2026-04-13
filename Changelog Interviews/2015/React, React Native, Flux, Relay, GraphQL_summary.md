• React team from Facebook discusses the recent open-sourcing of React Native
• Guests Christopher Chadeau and Spencer Aaron share their experiences with React and React Native
• Christopher introduced to React by Jordan, who showed him a prototype a year before it was open-sourced
• Spencer came from a background managing the Facebook News Feed team and was drawn to React Native's fast reload capabilities
• React is a library for building user interfaces in JavaScript, not a framework
• React's core feature is its ability to re-render the entire app on every update, reducing complexity and bugs
• Guest discuss the excitement around React and React Native, particularly among developers
• CodeShip's Parallel CI feature is mentioned as a tool for deploying faster and reducing build times
• Discussion of the benefits of React, including its ability to render any tree and its abstract nature
• The history of React and its development within Facebook
• The impact of React on the company's product, including the rebuilding of a complex web application
• The benefits of React, including predictability, efficiency, and the ability to make confident changes
• The role of designers in working with React, including the ability to make design changes easily
• The myth that designers cannot code and the importance of making React accessible to designers
• Explanation of JSX, a syntax extension for JavaScript that allows for HTML-like syntax in React components
• Discussion of escaping and rendering of certain elements on a website
• Introduction of PHP objects to render elements and creation of custom tags and components
• Porting of Facebook app to JavaScript and React
• Explanation of JSX and its optional nature
• Discussion of React's compatibility with other toolkits and languages
• Adoption of React at Facebook and its initial implementation
• Explanation of React Native and its ability to render to native platforms
• Mention of a sponsor, Top Towel, and their relationship with the speaker and the podcast
• React Native's goal is to get the best of both native and web development
• The project was started due to performance limitations of web development
• Native UI components are well-designed and high-quality, allowing for reuse and consistency across platforms
• The project aims to have a unified development experience, with a single set of tools and codebase for multiple platforms
• Consistency across platforms allows for easier developer transition and collaboration between platforms
• React Native uses native rendering, sending DOM operations from JavaScript to Objective C for rendering on native platforms
• The speaker discusses the benefits of using a shared codebase for different platforms, such as Android, iOS, and web, with React Native.
• Shared codebase allows for faster development and reduced fragmentation of knowledge among engineers.
• React Native's plugin system allows for arbitrary native code to be implemented, enabling access to native features and APIs.
• The speaker highlights the importance of communication and collaboration among engineers across different platforms.
• They also discuss the challenges of platform-specific verticals and the need for a unified approach to development.
• React Native is now open-sourced
• The initial announcement was made at React Conf in January, but it wasn't open-sourced until March 26th
• The project was not initially ready for open-sourcing, so a month was spent cleaning and preparing it
• Attendees of React Conf in January had private access to the GitHub repo
• Open-sourcing was done to allow people to try and use React Native, rather than just hearing about it
• The goal is for users to be unable to detect the difference between React Native and native apps
• Facebook has committed to only launching open-source projects that they believe are useful for internal use cases and the community
• Paper, a Facebook product, uses a different open-sourced library called Async Display Kit
• React Native's layout calculation is done on a background thread to prevent blocking the UI thread
• Async Display Kit's open-source library is an inspiration for React Native's optimizations
• React Native has a "flex box style" layout paradigm that allows for complex layout calculations to be done in the background
• The library is modular and designed to support multiple platforms, including Windows 10
• Non-blocking aspects, such as garbage collection, are a key consideration for frame rate and animation smoothness
• React Native uses a serializable asynchronous bridge between the native runtime and JavaScript engine to prevent blocking
• Potential future optimizations include multi-threaded JavaScript architectures and garbage prediction
• Concurrent garbage collection in JavaScript core has not been a problem, despite initial concerns
• Digital Ocean is a cloud hosting provider for developers, with inexpensive pricing and fast servers
• The hosts discussed their use of Flux, a data management architecture, and its benefits for handling updates and reducing code complexity
• Flux is a way of organizing data, not a specific tool, and is used in conjunction with React for web and mobile applications
• Flux has a centralized dispatcher and stores data in JavaScript objects, with actions being sent as JSON payloads
• The hosts also discussed Graph QL, a query language for APIs, and its use in managing complex data structures
• The hosts briefly mentioned Relay, a framework that appears to be a spiritual successor to Flux, and its similarity to Flux in handling actions and data fetching.
• The speaker discusses the similarities between Relay and other architectures, but highlights the challenges of keeping client and server code in sync.
• Relay enables clients to specify exactly what data they need, allowing for efficient data fetching and reducing the "overfetching" problem.
• The speaker explains how Relay works with GraphQL to enable clients to request specific data from the server, rather than receiving unnecessary data.
• Relay also helps with data management, including combining data fetching for multiple components and handling updates.
• The speaker discusses the benefits of GraphQL, including its hierarchical structure and ability to reduce the "n+1 query problem".
• The speaker mentions that GraphQL was first implemented by the engineers working on the iOS app, and has since been adopted by other iOS and Android apps.
• The speaker explains that the main reason they didn't discuss GraphQL earlier was because it requires changes to the backend, but now that it's being integrated with Relay, the benefits are significant enough to encourage others to adopt it.
• Open sourcing language specification for grammar and custom implementations
• Plans to release node modules for integrating with databases (MySQL, Postgres, MongoDB)
• GraphQL and Relay announcement created hype, leading to increased focus on open sourcing
• Specification for GraphQL will be shared, allowing multiple implementations
• Flux and GraphQL compared, with a goal of creating an ecosystem around the latter
• Work is underway to smooth out "warts" in the GraphQL implementation before releasing the full spec