• Introduction to NestJS framework
• Comparison with Express.js and its lack of structure
• Dependency injection and its benefits
• Reuse of services between REST, GraphQL, and microservices
• Architecture and layered approach in NestJS (controllers, services, entities, DTOs)
• Transport-agnostic design allowing for easy switching between protocols
• Dependency injection and module structure
• Providers (controllers and services) and how they are used to inject dependencies
• Encapsulation of business logic in services and exposing it through controllers or resolvers
• TypeORM and other ORM solutions, including their usage and potential drawbacks
• Data transfer objects (DTOs) and their role in decoupling data exposure from persistence
• GraphQL support and setting up resolvers for queries and mutations
• Code-first vs schema-first approach in NestJS
• Using resolvers to expose methods in GraphQL API
• Automatic generation of schema and DTOs from metadata
• Benefits of using GraphQL for documentation and explorability
• Use of tools like GraphQL Code Generator to generate types on the frontend
• Introduction to Nestjs-query project, which simplifies CRUD and GraphQL operations
• Abstracting database operations and operators
• Cursor-based pagination and continuous pagination
• Standardizing CRUD endpoints with "input" terminology
• DTO (Data Transfer Object) creation and decoration for filtering, authorizing, and relating data
• Automatic generation of schema, resolvers, and services from DTOs and entities
• Decoupling GraphQL layer from backend persistence through adaptors and query service interface
• Assemblers: translation layer between DTO (Data Transfer Object) and entity, used for tasks like converting snake case to camel case
• Pagination strategies: cursor-based, offset-based, and disabling pagination entirely
• Code-first approach vs. schema-first: library uses code-first by default, with auto-generated schema
• Relay support for cursor-based pagination
• Automatic generation of page info, edges, and nodes in responses
• Query options decorator to specify paging strategy
• Support for multiple paging strategies, including offset and cursor, for relations
• Nestjs-query provides basic functionality for GraphQL queries and allows users to focus on exposing their data without having to write custom resolvers.
• The library doesn't replace existing functionality but rather builds upon it, allowing users to drop out of the provided features at any time.
• Users can create custom query endpoints alongside the provided features.
• Nestjs-query is part of a larger ecosystem that includes a friendly and supportive community, with many contributors from around the world.
• Building tools for developers is considered a more enjoyable experience than traditional client work, as it allows users to help other engineers without being present.
• Developing developer tools requires thinking about how they can be used and manipulated by others, including edge cases and error handling.
• Doug Martin discusses his experience with breaking open-source tools and ensuring test coverage.
• He talks about his open-source project FastCSV and how it was adopted by the community.
• The conversation shifts to Doug's transition from JavaScript to TypeScript, which he credits with improving code safety and making it easier to maintain old projects.
• Nick Nisi shares a similar experience of being spoiled by TypeScript and struggling to work on non-TypeScript projects.
• The two discuss their past reactions to new technologies, including TypeScript, React, and CoffeeScript, and how they learned to be more open-minded and willing to try new things.
• Doug invites listeners to contribute to his project NestJS or Nestjs-query.
• Introduction to conversation with Doug about NestJS, Nestjs-query, and related technologies
• Discussion of TypeScript integration with NestJS
• Explanation of GraphQL in NestJS context
• Comparison or mention of JavaScript (specifically HorseJS)