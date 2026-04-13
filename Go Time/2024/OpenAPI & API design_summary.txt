• Definition and purpose of OpenAPI
• OpenAPI specification for documenting APIs, making it machine-parsable and machine-generatable
• OAPI CodeGen library for generating Go code from OpenAPI specifications
• Benefits of using OAPI CodeGen, including idiomatic Go code generation and reduced overhead in CI pipelines
• Best practices for working with generated code, including not modifying the generated code directly
• Configuration options and customization capabilities for generated code
• Common complaints about the project, including difficulties replicating complex aspects of OpenAPI.
• OpenAPI (OAPI) CodeGen allows developers to generate code from OpenAPI specifications
• OAPI CodeGen can handle complex types and schemas, but this also means it must fit within Go's type system
• The tool generates models and types for requests and responses, as well as full clients and server boilerplate
• It enables "readme-driven development" where the API is specified before generating code
• OAPI CodeGen can be used to reduce boilerplate code when writing services or communicating between services
• Developers can generate their own OpenAPI specification to interact with third-party APIs without waiting for a client library to be provided
• Managing API versions and changes
• Using OpenAPI specs to generate clients and manage versioning
• Server-driven media type contract negotiation vs using version in URL path
• Incremental vs major versioning in the path
• Balancing breaking changes with backwards compatibility
• Supporting multiple versions of an API over time
• Challenges of maintaining a public API
• Version numbers in APIs: Kris and Johnny discuss their dislike for version numbers in APIs, with Kris arguing that they can lead to unnecessary complexity and instability.
• HTML and TLS example: Kris uses examples from HTML and TLS to illustrate how older versions of these technologies are still compatible today, implying that APIs could also follow a similar approach.
• Shift towards forward/backward compatibility: Kris suggests that the industry should focus on creating APIs that are forward and backward compatible, rather than relying on version numbers.
• Alternative approaches: Johnny questions whether there is a better alternative to versioning, while Kris proposes using automatic upgrade paths and providing shims or implementation layers to facilitate smooth transitions between versions.
• Open Rewrite project: Jamie introduces the Open Rewrite project, which explores alternative ways of handling API changes.
• Problems with upgrading and migrating between versions of APIs
• Use of versioning allowing for "lazy" thinking in API development
• Need for documentation and information about how APIs work, not just their specification
• Temporal nature of specifications and variants of implementation
• Liability and risks of relying on unversioned or changing APIs
• Illusion of promise provided by version numbers
• Importance of extracting concrete promises from companies rather than relying on version numbers
• Discussion on versioning and specification in APIs
• Importance of written contracts or agreements for API usage
• OpenAPI as a contract that outlines expected behavior
• Challenges faced by open-source maintainers, including lack of financial support
• Initiatives to make OAPI CodeGen more sustainable, such as GitHub Sponsors and company contributions
• Time-consuming nature of maintaining an open-source project, including reviewing code and triaging issues.
• Challenges of maintaining open source projects
• Issue tracking and management for large projects
• Financial support for open source maintainers
• Models for sustainable open source development (e.g. Ben Johnson's model)
• Need for infrastructure and project management to triage issues
• Potential solution: a larger entity providing funding and resources for smaller projects
• Big foundations may not be effective in solving open-source project issues
• The value of non-code contributions (e.g., community management, documentation) is often overlooked in open-source communities
• Companies and projects struggle to support maintainers and contributors financially
• Foundational governance models can introduce politics and complexity, making it difficult for small projects to navigate them
• A focus on welcoming and valuing diverse types of contributions (not just code writing) is needed to revitalize the open-source ecosystem
• Using a spatula to eat ice cream and the benefits of using flexible utensils
• Jamie Tanna discusses various types of spatulas he uses for eating ice cream
• Johnny Boursiquot teases Jamie about his ice cream eating methods
• Discussion of Changelog++ and its benefits, including ad-free content and extra conversation
• Introduction to a "secret part" of the show where Johnny will discuss something with Plus Plus subscribers