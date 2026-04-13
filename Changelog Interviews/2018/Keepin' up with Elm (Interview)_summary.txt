• Elm is a programming language for building web apps that compiles to JavaScript
• Elm provides enough tools to build an entire web app, eliminating the need for frameworks
• Richard Feldman's company, NoRedInk, uses Elm for 250,000 lines of code and has had mostly success with it
• Elm 0.19 includes a new compiler flag that optimizes code and prevents runtime exceptions
• The company hired Evan to work on Elm full-time, and he has complete autonomy to take Elm in any direction
• NoRedInk is a remote-friendly company that is hiring, and they prioritize supporting open source projects like Elm
• Elm's adoption has increased, with a notable shift from individual hobbyists to teams using Elm at work.
• The language has seen significant growth in Europe, particularly in London and Oslo.
• Elm's focus on community and technical merits has led to a substantial hiring benefit for companies that adopt it.
• Elm developers are in high demand, making it easier for companies to hire high-quality Elm developers compared to JavaScript developers.
• The language's niche status has created a "bigger fish in a smaller pond" effect, where companies that adopt Elm can attract top talent.
• Mainstream languages vs niche languages
• Correlation between hobby and professional programming
• Advantage of dedicating time to programming as a hobby
• Elm's impact on the programming world
• Elm architecture and its influence on other languages
• Elm 0.19 features, including compiler speed and bundle size reduction
• Asset size reduction and its significance in web app performance
• Elm implementation achieves smallest bundle size compared to React, Angular, and Ember
• Elm's function-level dead code elimination eliminates unused code and dependencies
• Elm's separate package ecosystem and transitive dependency management contribute to smaller bundle size
• Measuring bundle size and code contributions from different sources is challenging due to Elm's ecosystem
• Elm's compilation process and optimization flags enable further code reduction and minimization
• Function-level dead code elimination in Elm
• Impact on code-splitting and lazy loading
• Bottlenecks in performance optimization
• Benefits of Elm's ecosystem-wide dead code elimination
• Comparison of Elm's package ecosystem to npm
• JavaScript interop and Elm's guarantees
• Function-level dead code elimination in JavaScript using the Google Clojure compiler
• Discussion on the limitations of using JavaScript with function-level dead code elimination and the potential benefits of other ecosystems like ClojureScript and Elm.
• The JavaScript ecosystem's potential to adopt a similar approach, but requiring specific constraints and ergonomics.
• Elm's current focus on the browser and its potential future on the server, with WebAssembly as a possible compilation target.
• The potential benefits of Elm compiling to WebAssembly, including lower overhead, improved concurrency, and better performance.
• The challenges of creating a good experience for Elm on the server, including design and implementation work to build an ecosystem.
• The importance of considering WebAssembly as a compilation target for Elm, and the potential for it to enable running Elm on the server.
• Designing a replacement for popular frameworks like Rails, Sinatra, and Express that meets ergonomic standards
• Challenges of compiling to JavaScript and interacting with Node, and potential benefits of compiling to WebAssembly
• Importance of concurrency primitives and supervision trees in language design
• Goal of creating a credible alternative for building front-end applications, and extending that goal to server-side development
• Comparison of the complexity of front-end and back-end development ecosystems
• Common reasons for not adopting Elm, including team buy-in, learning curve, and aesthetic preferences
• Specific challenges of Elm's JSON decoders and its need for robust data validation and translation
• Elm prioritizes type checking and guarantees over assumptions, whereas JavaScript relies on user assumptions
• Elm's JSON decoding process involves validating against a schema, which can be cumbersome but results in a more reliable system
• A single source of truth for the schema, such as protocol buffers, can help maintain data consistency and reduce boilerplate code
• The single source of truth approach also enables code generation and can improve reliability by breaking the build if the client and server get out of sync
• Recommended resources for learning Elm include the official guide, Richard Feldman's book "Elm in Action", and a course on Front-end Masters