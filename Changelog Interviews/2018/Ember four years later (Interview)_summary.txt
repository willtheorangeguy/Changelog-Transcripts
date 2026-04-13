• Chad Hietala's background and how he became an Ember core team member
• LinkedIn's involvement with Ember and its support of the framework
• The role of Tom and Yehuda Katz in Ember's development and standardization process
• Ember's evolution and innovations, including the CLI and Glimmer
• The framework's focus on sustainability and long-term development
• The standardization process and Ember's APIs, including ES6 decorators and computer properties
• The roadmap for Ember 3.0 and its potential to bring native JavaScript syntax to Ember's object model
• The Ember framework was ahead of its time in implementing APIs for web development, and its concepts have been standardized in newer browsers like IE10.
• The release cycle of Ember, with regular updates and a path for future releases, has been a successful model for other projects to follow.
• The Ember project has a status board that outlines current efforts, progress, and relevant resources for the community.
• The governance and decision-making process of the Ember project involves a consensus-driven team, without a single leader, and includes contributions from stakeholders with diverse viewpoints.
• Funding for the project comes from various sources, including employers, sponsorship, and personal contributions from team members.
• RFC process for proposing changes to the EmberJS project
• How to start an RFC and required parts of the document
• Importance of teaching and documentation in the RFC process
• Ember's RFC repo and template for proposing changes
• Iteration and improvement of the RFC process over time
• Comparison to other projects, such as React and Rust
• New features and innovations in the latest Ember release
• Modernization of the underlying rendering engine
• The original HTMLBars system was replaced due to performance issues and React's influence on Ember's development path.
• The first version of Glimmer was developed to address similar semantics to React, using a "set" function to update the UI.
• The introduction of angle bracket components in Glimmer 2 aimed to be a lighter weight version, but ultimately led to a reevaluation of the rendering engine's architecture.
• Glimmer 2 rearchitected the rendering engine, treating templates as pure functions and modeling the templating language as a functional programming language.
• The Glimmer rendering engine compiles templates into a JSON structure, which is then interpreted at runtime.
• This approach resulted in a 5x reduction in compiled template size in the LinkedIn application.
• The team then transitioned to compiling templates into a bytecode set, which is executed by a virtual machine.
• A later project explored precomputing the binary code at build time, requiring a bridging technology to resolve component invocations at runtime.
• The current approach compiles templates into an array buffer, aiming to reduce the costs of parsing and compiling JavaScript.
• Glimmer.js is a lightweight component library that is similar to React, but with a focus on being a view layer and not a full framework like Ember.
• Glimmer.js is used as a proving ground for new ideas and experiments that can later be integrated into Ember.
• The rendering engine and templating language used by Glimmer.js are the same as those used by Ember, allowing for seamless integration between the two.
• The goal is to have a single, consistent API for building applications, whether it's using Glimmer.js or Ember.
• Glimmer.js can be used as a standalone library, allowing developers to use its components in any application, regardless of the underlying framework or stack.
• The project is exploring ways to reduce the dependency weight of Ember by implementing tree shaking, which eliminates unnecessary code from the final bundle.
• Tree shaking vs static linking
• Subfonting/subsetting of web fonts
• Ember's ability to support tree shaking
• Evergreen browsers and their impact on development
• Modularity and the importance of scaling up and down in web development
• Comparison of Ember with other frameworks (Vue, jQuery)
• Ember's font subsetting process and performance optimization
• Future development plans for Ember, including adopting ES6 classes and improving performance
• The importance of server-side rendering and dynamic applications in web development
• The "stability without stagnation" approach of Ember, which balances stability with adaptability to new technologies and best practices
• Common use cases for Ember, such as building long-lived applications with multiple developers
• Performance improvements and addressing common issues with Ember
• The hype cycle in JavaScript and how Ember's stability and consistency make it a more attractive choice for developers
• Gratitude for the time spent on the podcast