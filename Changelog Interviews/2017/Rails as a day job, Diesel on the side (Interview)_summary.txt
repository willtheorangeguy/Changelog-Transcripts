• Sean Griffin presents a changelog for Diesel, a Rust ORM and query builder
• Sean shares his background with Rails and how he implemented the Attributes API in ActiveRecord
• He discusses his role as a maintainer of ActiveRecord and the challenges that come with it
• Sean explains how he transitioned to working on Rails full-time at Shopify
• He reveals that his motivation for making the switch was to maintain a better work-life balance due to his inability to disconnect from work
• Open source is more than just code, it's a community, documentation, and research
• Sean Griffin petitioned the community for a full-time open source position for 6 months while at ThoughtBot
• Griffin's LinkedIn bio from the time listed open source contributions as his priority, with a humorous request for recruiters to leave him alone
• Griffin's role at Shopify involves focusing on Rails, with a large part of his time spent on issue triage and reviewing pull requests
• Moving forward with Rails involves maintaining stability and making incremental improvements, rather than pushing the boundaries of new technology
• Griffin is working on specific improvements to ActiveRecord, including changes to how Dirty behaves in after_save callbacks
• Discussion of upgrading to new versions of Rails and removing outdated hacks
• Introduction of Active Storage, a new feature in Rails 5.2 for cloud storage
• Background on the development of Active Storage and its benefits
• Sean Griffin's departure from ThoughtBot and his desire for a full-time open-source role
• ThoughtBot's contributions to Rails and open-source projects, including Paperclip
• The benefits of having a full-time staffer working on infrastructure and maintenance
• Discussion of the importance of funding and sustainability for open-source projects
• Roles like Sean Griffin's, which combine corporate job and open source contribution, can bring value to companies by providing availability for pairing, code review, and answering questions.
• Sean Griffin's role is structured to focus on open source, allowing him to contribute to Shopify's Rails maintenance and provide expertise to the development team.
• The role can be seen as a "back-office" function, providing infrastructure support to the "front-office" developers who work on new features and products.
• To grow more people in open source roles, companies can offer 20-25% time for open source contributions and give employees flexibility to spend that time in whatever chunks make sense for the project.
• Companies can also consider implementing programs like Shopify's "quarter-long open source immersion" where employees work on open source full-time for a quarter.
• Sean Griffin's role and happiness with his current job
• Business vs. technical problems and his preference for the latter
• His decision to build a Rust ORM called Diesel
• His interest in Rust and its type system, which led him to create Diesel
• His experience porting a C++ project to Rust and discovering its benefits
• The Rust type system and its unique features compared to Haskell and other languages
• Infinite size problem in Rust when implementing singly linked lists
• Sean Griffin's revelation to use a tangible example, such as a list of strings or numbers, to explain the concept
• Haskell's implications in the example and its community's reaction
• Classifying Rust as a systems language and its limitations
• Go and Rust's reclassification from systems languages to general-purpose languages
• Swift's clear ambition and presentation as a general-purpose language
• Rust's appeal to C++ developers and the broader audience
• Sean Griffin's experience building Diesel, a Rust ORM, and its current status
• Discussion of Diesel's structure and need for breaking changes before 1.0
• Sean Griffin's experience with Rust and Diesel's origins
• Diesel's features and how they were influenced by Griffin's experience with ActiveRecord
• Griffin's vision for Diesel as a memory-safe and type-safe ORM
• The evolution of Diesel's design, including the abandonment of certain original features
• Representing SQL queries in Rust for improved error messages
• Comparison of Diesel's query builder to ActiveRecord's, highlighting differences and similarities
• Support for arbitrary SQL expressions in Diesel's query builder
• Goal of reaching 95% of ANSI SQL standard in Diesel
• Limitations of Diesel's error checking, such as insert validation
• Differences in type mapping between Rust and SQL, including examples
• Design of Diesel's API, including separate structs for queries and inserts
• Influence of ActiveRecord on Diesel's design and implementation
• Potential future changes to Rails query builder inspired by Diesel
• Examples of lessons learned and design decisions in Diesel that may be applied to Rails
• Potential integration of Diesel's Postgres driver into Rails
• Binary representation of timestamps in Postgres
• Performance comparison of typecasting vs string parsing in Ruby
• Diesel's influence on Rails through binary type support and bind parameter handling
• Plans for future development, including a possible Rust web framework and a Ruby wrapper for Diesel's lib/pq feature