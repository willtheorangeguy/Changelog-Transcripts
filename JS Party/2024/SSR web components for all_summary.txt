• Enhance is a new framework from Brian Leroux and his team that allows server-side rendering (SSR) of Web Components
• Web Components have limitations, such as being client-side JavaScript-centric and requiring a lot of code to be sent to the browser
• Enhance addresses these issues by inverting the rendering process, allowing templates to be defined using plain JavaScript on the server side
• The framework allows for better performance and debugging, and provides a more even match between what is written and what is run
• Enhance Wasm (Wasm-ify) takes this concept further by compiling JavaScript into WebAssembly (WASM), allowing it to be executed in any WASM-compatible runtime on the server side
• This opens up new use cases for server-side rendering, such as being able to render components from different backend runtimes like Java or Python.
• Benefits of a technique that allows server-rendering with a design system
• Design systems and their challenges in large companies with multiple stacks
• Web Components and their potential for sharing components across different technologies
• Extism project and its ease of use for running JavaScript modules in various languages
• Shared validation logic and its benefits for reusing code across different properties
• Demo of a Rails application using the technique, with discussion on its simplicity and nostalgic feel
• The speakers discuss the challenges of implementing server-side rendering for Web Components
• They mention a project where they created example apps/integrations for various frameworks (WordPress, Rails, Flask, etc.)
• Brian Leroux explains that the goal is to provide examples that show integration points between Enhance and different frameworks
• Jerod Santo asks about the steps involved in setting up server-side rendering with Go, and Brian provides information on the Enhance-SSR-GO repo
• The speakers discuss the benefits of running Enhance inside WebAssembly (Wasm) and how it can provide better performance
• They also talk about the challenges of server-rendering web components due to the need to mock browser events and explain their approach using an immediate render pattern
• JavaScript's unreliability in client-side rendering
• Visibility into failures with server-rendered HTML Web Components
• Comparison to transpiling techniques and native HTML implementation
• Dev tools awareness and handling of Web Components
• Shadow DOM as an opt-in rather than default
• Definition of HTML Web Components: components that don't require client JavaScript to render and often use the light DOM instead of Shadow DOM
• Advantages of HTML Web Components: faster, more portable, and predictable rendering
• Difficulty in achieving consensus among developers for Web Components
• Ergonomics of Web Components being considered outdated or "long in the tooth"
• Challenges with using Shadow DOM for complex forms due to API limitations
• Need for a more straightforward approach to building forms using Web Components
• Concept of progressive enhancement and graceful degradation in Web development
• Discussion on platformizing Web Components and creating native primitives
• Benefits of declarative programming using CSS and its rapid evolution
• Exploration of design systems and formalizing them within the browser
• Discussing the need to create a reusable design system for web development
• Concerns about standardization leading to homogenized websites and losing creativity
• Introducing Begin and Enhance, two projects from startup Begin
• Explaining how Begin is a serverless hosting platform with an open-source core and local development environment
• Discussing the role of Enhance as a modern frontend framework for building cloud-native applications using Web Components and WebAssembly
• Encouraging community involvement and contributions to Enhance and related projects like Extism
• Web Components hype cycle
• Productivity plateau with WebAssembly adoption
• Java community's slow Wasm adoption
• Innovator's dilemma and incumbent resistance to new technologies
• Potential for WebAssembly to be useful despite initial skepticism
• JS Party coverage of Brian Leroux's work with Extism