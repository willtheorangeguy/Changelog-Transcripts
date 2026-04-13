• GraphQL is a query language for APIs that allows for more flexibility and efficiency than traditional RESTful APIs
• It solves problems such as data overfetching and the N+1 query problem
• GraphQL has a lower entry barrier and provides better tooling than RESTful APIs
• Facebook and GitHub are examples of companies that have adopted GraphQL for their APIs
• GraphQL provides a schema that exposes the types and structure of the data, allowing for more efficient querying and reduced payload size
• GraphQL can be implemented in any language and is not limited to specific technologies like REST
• GraphQL schema is defined using the GraphQL SDL (schema definition language) and type definitions
• Type definitions provide free and up-to-date documentation and are the foundation for GraphQL schema
• GraphQL has a low learning curve and is easy to understand, but may require a new way of thinking for developers used to REST
• Drawbacks of GraphQL include:
	+ Potential for complex caching strategies due to unique API calls
	+ Not as well-established as REST standard, but gaining traction
	+ May be overkill for simple APIs or those already using REST
• GraphQL is transport-agnostic and can be used with various protocols, including HTTP, WebSockets, and binary transports.
• GraphQL mutations: writing data, updating data, equivalent to REST's PUT, POST, DELETE, PATCH
• Mutations are like remote function calls, with typed arguments
• Mutations can also perform queries while running, exposing a view into the graph
• Permission and authentication: not built into GraphQL, but can be implemented using various mechanisms (e.g. HTTP basic auth, session tokens)
• Graphcool's permission system allows field-based authorization rules
• Graphcool's permission system allows specifying authorization rules based on graph structure
• Comparison to Firebase and Parse: Graphcool uses open-source technologies and allows schema and data export for migration away from the service
• Concerns about service shutdown: Graphcool's openness and exportability mitigate this risk
• Graphcool's mission is to provide a better level of abstraction for building backends
• The company's "sunset policy" ensures that if Graphcool were to shut down, all its technology would be open-sourced
• Graphcool uses a mix of open-source and proprietary technologies, with the proprietary parts being the "glue" that connects the open-source components
• The company is considering fully open-sourcing its technology, but is concerned about the complexity of its codebase and the need for documentation and support
• Graphcool is currently focused on solving the problem of building backends with GraphQL, and is not yet ready to open-source its technology
• The company's goal is to provide a better abstraction for building backends, allowing developers to focus on business logic and user experience rather than the drudgery of mapping APIs to databases.
• Benefits of using services to simplify complex problems
• Lego building block analogy for GraphQL and serverless integration
• GraphQL typesystem and global type safety
• GraphQL Europe conference and community resources
• Future of GraphQL, including live queries and subscriptions
• GraphQL Subscriptions and Live Queries explained
• Excitement about serverless GraphQL back-end architecture
• Merging of GraphQL and serverless paradigms to reduce friction and enable developers
• Building a GraphQL API using the GraphQL SDL and existing infrastructure
• Implementing business logic in a scalable way using serverless infrastructure
• Using GraphQL clients such as Apollo and Relay for front-end development
• Encouraging developers to try out GraphQL and its clients for ease of implementation