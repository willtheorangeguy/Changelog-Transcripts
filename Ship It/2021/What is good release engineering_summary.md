• Release engineering importance for open source projects
• Relationship between developers and end users of open source software
• Core infrastructure components (RabbitMQ) and their reliance on stable releases
• Comparison of release engineering in RabbitMQ and FreeBSD operating system
• Examples of release engineering gone wrong (security bugs, breaking changes, delayed shipping)
• Consequences of poor release engineering (lost trust, reluctance to upgrade)
• Importance of user confidence in software releases
• Vicious cycle of developers struggling with updates leading to decreased user adoption
• Relationship between end-user happiness and release engineering
• Comparison of RabbitMQ and FreeBSD as core infrastructure components
• Discussion of specific use cases where one or the other is more critical
• Overview of the FreeBSD release engineering process, including a fixed interval between major releases and flexible planning
• The FreeBSD development process involves a detailed calendar for planning and communication
• The community can plan and test new versions in advance, with Netflix being one example
• The release engineering timeline depends on whether it's a minor or major release
• Minor releases typically take weeks to months, while major releases take 2-3 months or more
• Major releases do not follow semantic versioning, but aim for compatibility between releases
• Contributors can find tasks in the Bugzilla bug tracker and solve problems they encounter with FreeBSD to contribute
• The community can participate by submitting patches through GitHub pull requests, mailing lists, or Bugzilla
• Release engineering in FreeBSD
• Calendar-based release cycles for major and minor releases
• Communication and organization improvements through fixed intervals and advance announcements
• Other open-source projects (Darktable, Mesa library) that implement similar release engineering strategies
• Balance between shipping stable software and incorporating new features/drivers
• Difficulty of testing complex graphics drivers and finding the right balance in shipping updates
• Use of Erlang for web development and its benefits
• Hot code reloading feature of Erlang and its challenges
• RabbitMQ not using hot code reloading due to complexity
• Packaging and configuration management issues with Erlang-based systems
• Challenges of packaging and distributing complex distributed stateful systems like RabbitMQ
• Benefits of containerization and Kubernetes in managing such systems
• Challenges with databases in containerized environments
• Limitations of RabbitMQ's current functionality compared to traditional systems
• Discussion of implementing hot code reloading in RabbitMQ
• Potential benefits and feasibility of implementing hot code reloading only for bug fixes
• Release engineering practices and experiences shared by users of open-source projects