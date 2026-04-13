• JSON (JavaScript Object Notation) explained as a way to represent data and its use across various languages
• Origins of JSON's popularity due to the rise of modern web technologies like HTML, CSS, and JavaScript
• Comparison between JSON and XML, with JSON being simpler and more human-readable
• Gotchas when working with JSON in Go, including handling timestamps and numbers as strings or floats
• Discussion of the encoding/json package and its limitations in representing numbers
• Daniel Martí is co-maintaining the encoding/json package in Go for 3-4 years
• The package has nearly 100 contributors and is used by many developers
• Maintaining the package can be stressful due to the high number of users and the responsibility to ensure backwards-compatibility
• The Go 1 compatibility guarantee requires that changes do not break existing code, making it a challenging balance to maintain
• Daniel Martí discusses various use cases for the JSON package, including decoding fields depending on other fields and streaming large objects
• He also talks about the importance of unit tests in ensuring backwards-compatibility and the challenges of achieving 100% code coverage
• Discussion around using the standard library's json package vs third-party packages with focus on performance and trade-offs
• Examination of a specific third-party JSON decoder that uses unsafe directly, which has security implications
• Comparison of marshal/unmarshal functions versus decoder/streaming approach
• Discussion of potential pitfalls in the encoding/json package's design, specifically its emphasis on correctness over speed
• JSON decoding and parsing
• json-iterator package for efficient key path searching
• encoding/json limitations due to compatibility promise
• Potential breaking changes in a future version of Go
• Designing a new API, including thoughts on the current issues with the existing one
• The role of the json.RawMessage type
• The issue with the JSON decoder in Go is a bug where it only decodes one object at a time, ignoring subsequent objects if they are separated by new lines.
• This can cause problems when dealing with APIs that send multiple JSON objects separated by new lines.
• Daniel Martí suggests adding a check to handle this case and provide an error or use all the data.
• The discussion leads to a broader question about when to choose between using JSON, plain text formats, and binary formats for data transmission and storage.
• Criteria for deciding against using JSON include situations where efficiency of transport and storage is important, such as in streams of data or ingesting large amounts of information.
• Debate between using plain text (JSON/YAML) vs binary formats for data exchange
• Importance of considering developer-friendliness when choosing a format
• Use case-driven approach to selecting a format, with both JSON and schema languages having their own advantages and disadvantages
• Discussion of backwards-compatibility and the trade-offs involved in choosing between simplicity and robustness
• Performance improvements in decoding JSON, including a 30% to 50% speedup between Go 1.10 and 1.13
• Potential for further performance optimizations, including rewriting the tokenizer
• The JSON package in Go performs double validation to prevent partial decodes.
• The design of the decoder and unmarshal functions is discussed, with some arguing that it's overly cautious about correctness.
• The age and evolution of the encoding/json package are acknowledged as potentially outdated.
• Daniel Martí makes an "unpopular opinion" that encoding/json is fast enough for most use cases, despite its potential to be optimized further.
• Discussion of a bug or issue that caused stress
• Minimizing the window seemed to resolve the issue
• Mention of checking memory usage and worrying about the program crashing
• Relief and amusement at resolving the issue
• Invitation for Daniel Martí to return and debug other issues