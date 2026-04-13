• Elixir Conf Europe recap
• Community growth and maturity
• Adoption of Elixir and Phoenix in industry
• Phoenix Presence and future features
• Personal experiences with Elixir and Phoenix
• Building a CMS with Elixir and Phoenix
• The speaker's experience with the Sinatra app and how it influenced their opinion on Phoenix
• The integration of Phoenix with Elm, a functional programming language, and the potential for a Phoenix-Elm library
• The benefits of using Phoenix, including its simplicity and the absence of bug reports for its HTML library
• The use of Brunch, a build tool, in Phoenix and the potential for confusion between Phoenix and Brunch issues
• The features of Ecto 2, including the separation of Ecto.Schema from Ecto.Model and the shift away from the active record pattern
• The old approach to modeling domain logic with callbacks and models is being phased out in favor of a more modular and composable approach.
• Ecto 2 is designed as a tool, not a framework for modeling the domain, allowing developers to think about their application as a collection of data sources.
• The concept of schemas has been redefined in Ecto 2 to focus on data transformation and validation, rather than modeling the database.
• The new approach emphasizes the use of small, reusable functions and modules to handle different data sources and operations.
• The introduction of Ecto 2's repository, changeset, and query components aims to simplify data manipulation and composition.
• The repository is responsible for managing database connections and transactions, the changeset handles data validation and transformation, and the query is used to slice and filter data.
• Ecto's main entities: Query, Changeset, Repository, and data structures
• Why Ecto doesn't perform lazy loading or automatic pre-loading of associations
• Pre-loading as a barrier to encourage developers to think about data upfront and load it explicitly
• Improvements to pre-loading in Ecto 2, including parallel loading of pre-loaded associations
• Ecto's goal to promote pure views and separate data transformation from side effects
• Automatic caching and other potential features based on pre-loads and data dependencies
• Concrete example of pre-loading in a CMS for podcasts and episodes
• Changesets in Ecto and their benefits for validation and constraints
• Parallel pre-loads in Ecto 2 for improved performance
• DB connection optimizations for better query performance
• Ability to insert data into the database without creating a changeset
• Ecto 2's feature for building a deep data tree and inserting it into the database
• Concurrent tests in Ecto 2, allowing tests to run concurrently even when talking to the database
• Integration of acceptance testing tools with concurrent tasks in Elixir
• Phoenix 1.2 and its Presence feature, which allows for real-time tracking of user connections
• Performance optimizations in Phoenix, including a WhatsApp-like scale of 2 million connections per server
• Challenges and nuances in implementing Presence, including treating users as unique even across multiple devices and dealing with distributed state in a cluster
• Presence feature in Phoenix 1.2 to track active users
• CRDT (Conflict-Free Replicated Data Type) used for consistency and fault tolerance
• Avoidance of single point of failure and remote synchronization
• Example of ORSWOT (observed-removed set without tombstones) CRDT used in Presence
• Eventually consistent list of presences with automatic recovery from network issues or server failures
• Simple API for generating Presence module and handling syncing state with server and client
• Presence object on client handles syncing state and resolving conflicts
• Optional callbacks for detecting specific cases, such as multiple devices or logout from all devices
• Goal of applying cutting-edge CS research into practice in Phoenix
• CRDTs not widely used in day-to-day applications, but solving a simple use case with a powerful research concept
• Phoenix Presence is a distributed system that allows for efficient and fault-tolerant tracking of online users
• The system uses CRDTs (Conflict-free Replicated Data Types) to maintain a consistent view of online users across multiple nodes
• Chris McCord notes that implementing CRDTs is challenging, but Phoenix Presence has been successful in production
• The system has accidentally solved the problem of service discovery, allowing for efficient lookup and routing of services
• The next step is to build an API specifically for services, enabling features such as process placement, load balancing, and automatic sharding
• The goal is to leverage the distributed runtime and primitives of the Elixir language to build a more robust and scalable system
• José Valim emphasizes the benefits of using a distributed system that can communicate efficiently, eliminating the need for complex infrastructure pieces and serialization formats like JSON.
• Simplifying service discovery and management in distributed systems
• Using a platform to handle service registration and management, eliminating the need for proxies and load balancers
• Parallelizing the design of the Presence system to enable communication between multiple services in a cluster
• Discussing the benefits of a simplified service discovery approach, including reduced complexity and improved scalability
• Exploring the integration of HTTP2 support in the Phoenix stack, including the use of Cowboy and Chatterbox libraries
• Discussing the deployment story for Phoenix applications, including the use of exrm and the need for additional tools to simplify deployment processes
• Addressing questions on running Phoenix behind a proxy, HTTP2 support, and deployment strategies
• Deployment issues with Phoenix, specifically the need for a tool that simplifies deployment and reduces the number of steps involved
• Discussion of existing tools, including Relisa, edeliver, and a bash script approach, to improve deployment
• Build tool situation in Phoenix, with Brunch being the default but others like Webpack available as alternatives
• Reasons for choosing Brunch, including its simplicity and speed, and the ability to easily swap out for other tools
• Decision to integrate with the JavaScript ecosystem rather than creating an Elixir asset pipeline
• npm install issues on Windows
• Phoenix 1.2 release candidate, Presence feature, and distributed applications
• Left-pad dependency and its impact on Phoenix
• Dockyard's support for open source and Chris McCord's role
• José's work on Plataformatec and its influence on Phoenix
• Chris McCord's keynote on CRDTs at ElixirConf Europe