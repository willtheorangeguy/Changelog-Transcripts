• Protocol buffers are a language for writing schemas for data and a binary format for serializing data.
• They were created by Google to simplify and improve efficiency in programming, especially when dealing with APIs and multiple clients.
• A protocol buffer schema is similar to a Go struct but can be used across languages and formats (e.g. JSON) with a code generator.
• Using protocol buffers allows programmers to avoid error-prone tasks of rewriting data structures for each client language.
• Trade-offs include the need for a schema and potential compatibility issues, but especially in Go, these are considered minor compared to the benefits.
• Protocol buffers can be used as a schema language even when working with JSON.
• Comparison of Protocol Buffers to Swagger (OpenAPI) for data modeling
• Critique of JSON schema's verbosity and lack of native types
• Discussion of the trade-offs between static typing (Protocol Buffers) and dynamic typing (JSON)
• Comparison of Protocol Buffers to GraphQL
• Suitability of Protocol Buffers for exposing public APIs, particularly with gRPC
• Historical challenges with tools for working with Protocol Buffers
• The complexity of using protocol buffers (protobuf) outside of Google due to its low-level nature and dependencies on other stack components.
• Benefits of binary formats over text-based ones, including optimized parsing and smaller size.
• Comparison of protobuf with JSON, including the ability to parse JSON quickly through specialized techniques and compression.
• Discussion of the Go standard library's encoding mechanisms, including Gob, which is not widely used due to its caveats, such as instability across Go versions.
• Protobuf's advantages over Gob in terms of performance, stability, and cross-language support.
• Protocol buffers as a data format for efficient serialization
• Comparison of protocol buffers with JSON and REST APIs
• gRPC as an RPC runtime that works with protocol buffers
• Criticism of gRPC's complexity and verbosity
• Alternative runtimes such as dRPC and Twirp
• Discussion on why developers might choose to create their own solutions instead of using existing libraries like gRPC
• The discussion centers around gRPC, its origins, and its marketing aspect.
• gRPC is derived from Google's internal system called Stubby, which uses protobuf-flavored HTTP/2.
• The protocol is relatively simple and could be described in a few paragraphs.
• The group acknowledges that there are multiple implementations of gRPC, but only one widely-used Go implementation (gRPC-Go).
• The discussion touches on the idea that having different trade-offs and implementation choices can be beneficial for developers.
• Buf is working on improving protocol buffers tools, including writing its own protobuf compiler from scratch and a schema registry.
• gRPC is intimately connected with Protobuf and using one requires considering the other
• gRPC has strengths in certain areas, but weaknesses in others, such as interoperability with net HTTP
• Connect is a drop-in replacement for gRPC that is wire-compatible and works with net HTTP
• Connect aims to make gRPC feel more like a part of the Go ecosystem, rather than a separate entity
• Perf-wise, using Connect or gRPC is generally comparable to using net HTTP
• The approach of using statically-typed languages like Go, TypeScript, and Python for APIs is deliberate
• Even dynamically-typed languages can benefit from type information at boundaries
• Using gRPC or Connect may be more suitable for internal communications rather than user-facing APIs
• Developer mindset plays a role in choosing between gRPC/Connect and traditional approaches
• The benefits of using gRPC with a JSON format for external APIs
• Limitations of traditional gRPC (e.g., inability to communicate with web browsers)
• Connect protocol: an alternative to gRPC that supports multiple protocols, including a REST-like one
• Protocol buffers as a more suitable solution for external APIs due to their flexibility and ability to generate code
• Importance of being able to call APIs from web browsers and the limitations of traditional gRPC in this regard
• XML mentioned as an outdated technology and contrasted with modern solutions like protocol buffers
• Structured logging libraries (such as Zap) being proposed for standard library inclusion
• Akshay Shah's criticism of structured logging due to performance issues with JSON format
• Problems with JSON being re-parsed by multiple tools in the log pipeline
• Preference for binary formats like MessagePack over JSON
• Jon Calhoun and Johnny Boursiquot sharing their own experiences with logging and structuring code
• Importance of hands-on coding experience in learning programming
• The need for showing code and writing it as examples to illustrate concepts
• Code-alongs encouraged in training programs
• Launching a new Go course with Lincoln Learning, focusing on hands-on learning
• Comparison between theoretical understanding and practical implementation of programming concepts
• Generics in programming and their impact on coding experiences
• Designing a free course on common algorithms and data structures
• Teaching without generics initially to focus on core concepts
• Understanding the role of generics in implementation, particularly with Java's "t" syntax
• Evolution of Go as a language and its impact on understanding generics
• Use of generics in code generation for protocol buffers and gRPC