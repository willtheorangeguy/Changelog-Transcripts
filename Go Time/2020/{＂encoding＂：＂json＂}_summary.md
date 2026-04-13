• Bugs in standard JSON decoding process
• Discussion of JSON (JavaScript Object Notation) and its uses
• Explanation of JSON's generic data representation for cross-language compatibility
• Introduction to guest Daniel Marty, a prolific Go contributor
• Overview of the Go Time podcast episode topics, including a murder mystery related to a sneaky bug
• Discussion about the structure and types in JSON
• Comparison of JSON with XML, citing ease of use and human-readability of JSON
• Rise of HTML, JavaScript, CSS, and JSON on the web
• JSON's simplicity and tighter structure compared to XML
• Potential "gotchas" when working with JSON, specifically regarding data types in Go.
• Default behavior of JSON is to treat time as a string
• Custom code often used to handle specific time formats
• No built-in timestamp type in JSON, treated as strings
• Numbers in JSON default to float64 type
• Go has map string interface for unmarshalling JSON data
• Handling numbers can be tricky due to loss of precision
• Design considerations for JSON: stricter typing vs arbitrary precision numbers
• Encoding JSON package is co-maintained by the speaker
• Memory usage on laptop has been rising and may crash soon
• Co-maintenance of encoding JSON package involves fixing bugs and optimizations
• The package has active maintainers (Ross, Joe, Brad)
• Stress in maintaining a widely used package like JSON
• Team's internal tooling development and maintenance is discussed
• DoorDash's engineering director discusses their experience with Retool, a platform for building internal tools.
• Retool helped DoorDash quickly build tools, empower local operators, and reduce dependency on engineering.
• Before using Retool, DoorDash was bogged down by manual data entry, missed handoffs, and long turnaround times.
• With Retool, DoorDash cut engineering time to build tools by a factor of 10x and eliminated error-prone manual processes.
• A developer discusses the challenges of maintaining the encoding JSON package, citing stress from its large user base and Go compatibility guarantee.
• Discussing the importance of backwards compatibility in software development, specifically with Go and its JSON package.
• Explaining how JSON's flexibility and lack of schema can make maintenance and feature requests challenging.
• Describing the constant stream of feature requests, optimizations, and bug fixes caused by previous changes in software.
• The encoding JSON package has decent unit tests
• Importance of unit tests in ensuring backward compatibility
• Challenges in achieving 100% code coverage, including edge cases and panics
• Discussion on whether 100% code coverage is necessary or desirable in this specific package
• Unusual behavior of the API when passing a pointer to unmarshal JSON data
• The JSON package expects a pointer to a structure that can store decoded data
• If the passed structure is empty, the package will make assumptions about the data format
• If specific field types are defined in the struct, the package will follow those definitions
• Annotating fields with JSON annotations is not necessary if the field names match the output JSON names
• Preference for using standard library over third-party packages
• Trade-offs between performance and ease of use
• Discussion of Dave Cheney's experimentation with JSON parsing
• Importance of considering trade-offs when choosing between different approaches
• Mixed opinions on the value of third-party re-implementations
• Consideration of specific use cases where high performance is necessary
• Discussion of code generation for JSON decoding
• Trade-offs between generated code size and performance
• Use of the "unsafe" package for direct binary manipulation
• Security concerns with using the "unsafe" package
• Comparison to other packages, including easyJSON and a drop-in replacement with similar API
• JSON's dynamic nature and how it can be used for passing around objects between tools
• Using the `unsafe` package vs using reflection in the standard library to handle dynamic data
• A specific use case where JSON was used to pass objects between command line tools
• The difference between using the `marshal`/`unmarshal` functions and using a decoder/encoder with an IO reader
• The speaker discusses the inefficiency of loading an entire JSON file into memory
• They mention a gripe with the current API, which buffers and decodes the entire JSON value at once
• The encoding JSON package prioritizes correctness over efficiency, leading to tokenizing input for error detection
• An alternative approach is mentioned, where a JSON implementation only unmarshals specific key paths instead of the entire document
• This alternative approach is faster but less versatile than decoding the entire JSON value
• The speaker discusses the JSON iterator library and its usefulness in certain scenarios
• Two main use cases mentioned: getting a single field or value from a large JSON, and not knowing what the data looks like upfront
• The "json.rawmessage" package is discussed as a way to delay parsing chunks of JSON data
• The benefits and limitations of using "json.rawmessage" are weighed against other methods
• A named slice of byte called "raw message" is introduced, which implements Marshaling and Unmarshaling JSON data
• Changelog offering a membership with a 40% discount for early adopters
• GoTime podcast and its ad-free experience
• Bug in the program using too much memory when recording audio
• Go 1.0 compatibility promise and its limitations on updates to JSON package
• Potential future changes to the JSON package
• JSON.number type and its implementation
• Handling big numbers in JSON
• Inconsistent behavior of JSON.number when input is a string containing digits
• Difficulty in determining whether changes would break existing code
• Challenge of balancing compatibility with legacy code and adhering to documented behavior
• Limited visibility into how users interact with the JSON package, making it hard to gauge potential impact of changes
• Discussion of JSON encoding and potential issues with current implementation
• Maintainer's concerns about adding complexity to existing packages
• Proposal to add new methods to the JSON package instead of creating a new API
• Identification of bugs, including one affecting most codebases due to incorrect decoding of HTTP request bodies
• The nature of streaming and buffering data, specifically with JSON objects
• Potential issues with large JSON objects and memory usage
• Alternative binary formats for efficiency in transport and storage
• Cases where JSON may not be the best choice due to its human-readable format being less efficient for machine-to-machine communication
• Problem with decoding JSON data in a stream
• Issue with only one object being decoded from the body, ignoring multiple objects separated by new lines
• Importance of considering human readability of JSON data and not using it just for the sake of using it
• Criteria for deciding when to use or not use JSON
• Difficulty decoding JSON in certain edge cases
• API design flaws leading to misuse
• Edge case of sending multiple lines of JSON at once
• Complexity and potential for bugs in handling nested arrays in JSON
• Importance of proper error checking and handling in APIs
• Difficulty of maintaining packages for human consumption
• Choosing between plain text and binary formats
• Considerations for efficiency, space usage, and machine communication
• Comparison with gRPC vs JSON APIs debate
• Discussing the approach to gRPC services
• Using plain text by default and considering binary or JSON support only when necessary
• Adding a REST gateway on top of gRPC for client flexibility
• Yagni principle, where "you ain't gonna need it" means not adding unnecessary features
• Exploring HTTP requests and JSON bodies in the browser for debugging purposes
• The limitations of JSON, particularly in defining a data model
• The potential of JSON schema to address these limitations
• Comparison with other schema languages such as protobuf and gRPC
• Trade-off between simplicity and proper data modeling
• Use case-driven approach for certain types of projects
• Backwards compatibility features of JSON
• Discussion on the complexity of adding new IDs to existing formats
• Mention of a trade-off between maintaining old code and making changes for efficiency
• Examination of current implementation efficiencies and potential improvements
• Analysis of JSON decoding process and allocation reduction possibilities
• Comparison of performance improvements in previous versions of Go (110 vs 113)
• Critique of exaggerated claims of encoding speed improvements by other packages
• Discussion of a tokenizer that doesn't build data structures as it parses, but instead tokenizes values such as JSON objects
• Need to determine if the tokenizer describes its internal data structure or builds an intermediate data structure
• Suggested approach is to build a tree-like data structure similar to a syntax tree for parsing languages like Go
• The JSON package checks for valid closing tokens
• Preventing partial decodes by decoding only once
• Efficient design: keeping a tree instead of bytes
• Allocating objects can be costly in terms of performance
• Simple API with one entry point vs. doing extra work for correctness
• Discussion about a decoder's ability to reuse objects
• Importance of understanding idiomatic Go code and best practices
• Criticism of the encoding/json package for containing optimizations that can increase complexity and ugliness
• Opinions on whether encoding JSON is fast enough, with one speaker arguing it often is but acknowledging exceptions
• Discussion about the potential benefits of a new format for data storage and whether it's worth switching from JSON
• Argument that those who need to deal with large amounts of data typically choose faster formats
• Comment on how some people may not be aware of benchmarking tools and may overestimate the slowness of JSON encoding
• Technical discussion about a bug in recording software, including the use of memory and UI rendering
• Metaphorical comparison of the software behavior to the Heisenberg principle and Schrödinger's cat
• Technical issue with up to 30% memory usage
• Issue remained after minimizing window and restarting the system
• User experienced stress and anxiety due to the technical issue
• Issue resolved, but caused significant frustration and relief upon resolution
• Request for further debugging assistance from Daniel