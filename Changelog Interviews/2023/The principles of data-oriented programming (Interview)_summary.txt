• Data-oriented programming as a concept and its lack of understanding and recognition
• Yehonathan's experience with writing a book on Clojure and his failure to interest readers
• Data-oriented programming as a set of principles that make it easy to manipulate data in programs
• Comparison of data-oriented programming to object-oriented and functional programming paradigms
• Key principles of data-oriented programming: treating data as a first-class citizen, separating data and code, using generic data structures, and using immutable data structures
• Differences between data-oriented programming and functional programming, particularly in the use of strongly-typed data structures versus generic data structures
• Separating code from data
• Representing data with generic data structures (maps and lists)
• Treating data as immutable
• Separating the schema from the data representation
• Benefits of separating code from data (preventing complexity, enabling code reuse)
• Problem with object-oriented programming (data and code are wrapped together, making it hard to reuse code)
• Benefits of using generic data structures (dynamic access, ease of renaming fields)
• Drawbacks of static typing (limiting dynamic access, requiring multiple structs for different representations)
• Discussing the trade-offs between static and dynamic typing
• Concerns about losing tooling, inference, and refactoring abilities with dynamic typing
• Flexibility and simplicity of data structures in dynamic typing
• Importance of runtime validation in dynamically-typed systems
• Using JSON schema for data validation and error handling in APIs
• Comparison of static and dynamic typing for data validation and error handling
• Declarative data validation using JSON schema is more flexible and expressive than static typing
• JSON schema can be used to generate Swagger JSON and is a perfect match for Swagger
• The main challenge is to get developers to adopt the discipline of writing schemas for their endpoints
• JSON schema can be used to generate test data and perform generative testing
• Using database schema as the schema is not typical, but there are tools that can translate SQL schema to JSON schema
• GraphQL is too rigid and adds too much complexity to business problems, making JSON schema a more appealing alternative.
• Union types for input data are not currently supported, but may be added in the future
• Data immutability is a paradigm shift that can be challenging for developers to adopt
• Structural sharing is a technique used by Git to achieve immutability without performance hits
• Data-oriented programming separates code from data and uses generic data structures, leading to benefits such as reduced bugs and easier data manipulation
• Adopting data-oriented programming can lead to a more enjoyable development experience and increased productivity
• A common schema language for expressing data schemas is still an unsolved problem.
• Ballerina language, designed for APIs and cloud, has a flexible type system that combines static and dynamic typing
• The language allows for optional type declarations and dynamic typing for certain data structures
• The flexible type system enables developers to switch between static and dynamic typing as needed
• Dynamic typing has its benefits, but also has tooling limitations
• Tooling is improving, but still has a long way to go
• Data-oriented programming is a style that combines the benefits of static and dynamic typing
• Yehonathan's book "Data-oriented programming" explores this style and its applications
• JavaScript and TypeScript are also suitable for data-oriented programming due to their flexible typing systems
• Introduction of Yehonathan Sharvit