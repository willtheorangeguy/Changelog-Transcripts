• Introduction to guests from the Angular Signals team
• Backgrounds of Alex Rickabaugh and Pavel Kozlowski on joining the Angular team and working on Signals
• Discussion of Angular's evolution over time, including its transition from a focus on browser consistency to developer experience and velocity
• The design review process that led to the creation of Angular Signals
• Angular's reactivity story was built around Zone.js, but it had limitations and wasn't viable for long-term use.
• The team looked for an alternative foundation for reactivity, considering new browser features and scalability issues with the current model.
• Signals emerged as a potential solution that met the necessary requirements.
• The team drew from 10 years of user data, bug reports, and feedback to understand how users were using Angular and identify areas for improvement.
• This data showed a disconnection between the framework's original design assumptions and actual user behavior, leading the team to create Signals as a more intuitive and flexible solution.
• Angular has a large user base with thousands of applications using its code, providing valuable insights into common problems.
• The team considered various approaches before choosing functional reactive programming and self-adjusting computations as the basis for the new framework.
• Signals were chosen due to their maturity and widespread adoption in other frameworks, such as Solid, Vue, and Preact.
• The team wanted a small, composable set of concepts with a notification mechanism that notifies the framework when data changes.
• The decision was made to move away from dirty checking and towards reactivity, which provides more information about what changed and who is interested in it.
• Dirty checking involves guessing which parts of the UI have changed, whereas reactivity provides explicit notifications of data changes.
• Discussion on the limitations of abstraction in performance-critical applications
• Pavel Kozlowski explains caching and defense mechanisms in React
• Alex Rickabaugh describes Signals as a variable with a special feature: broadcasting notifications when its value changes
• Two mental models are presented for understanding how Signals work: one is a simple box that can be read and written, the other is building a graph at runtime to propagate change notifications
• Discussion on the benefits of using a graph data structure for Signals, including scalability and performance efficiency
• The trade-offs of using Signals include the overhead of building and updating the graph
• Comparison with dirty checking: Signals provide more precise updates and better optimization opportunities
• Migration path from Zone.js to Signals is discussed, with options for gradual adoption and compatibility with existing applications
• Signal Components and their limitations
• Balancing gradual improvement vs breaking changes for new features
• Importance of incremental change in large-scale applications
• Relationship between Signals and observables (RxJS)
• Challenges of managing change and transitioning users to new concepts
• Need for clear benefits and obvious value to drive adoption
• Signals vs RxJS: distinction between values that can change over time (Signals) and notifications of events happening at a specific point in time (RxJS observables)
• Observables are event streams, while signals represent the current state
• Subscribing to observables creates side effects, whereas with signals, there is no consequence
• RxJS has been used extensively in Angular but can be overkill for simple applications and creates complexity
• Signals provide a simpler alternative for managing reactivity in applications
• Community engagement and feedback process for large-scale changes
• RFC (Request for Comments) process for soliciting community feedback
• Importance of being approachable and human in interacting with the community
• Recognizing the emotional impact of working on applications and frameworks
• Signals feature roadmap, including upcoming features and future plans
• Zoneless experience and how it will work in applications, testing, and server-side rendering
• Angular team working on Signals, a new way of working with the framework
• Signals will enable signal-based components with a set of rules for data flow
• Core framework work is currently in progress, with plans to update internal packages like Forms next
• Partnership with state management libraries (e.g. NgRx) to integrate Signals into existing offerings
• Dev tooling for Signals is being developed, including the ability to set breakpoints and visualize data flow
• Signals will be incremental, allowing applications to migrate from current approaches