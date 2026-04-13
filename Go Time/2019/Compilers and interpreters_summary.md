• What is a compiler? (Thorsten Ball explains)
• The difference between compilers and interpreters
• Go's compilation process (Go code to binary)
• Machine language and how computers understand different languages
• The Monkey language (a programming language implemented in Thorsten Ball's book)
• Implementing an interpreter for the Monkey language
• Transferable skills: building an interpreter enables solving other problems
• Templating in Go
• Understanding parsing and programming languages
• Book by Thorsten Ball on parsing programming languages
• Reusing knowledge from book to implement new features
• PEGs (Parsed Expression Grammars) as high-level abstraction around parsers
• Common problems that can be solved with understanding of parsing, such as templating, configuration files, and regular expressions
• Writing one's own implementation of a parser or interpreter
• Using parsing to solve real-world problems like search queries in code
• Creativity and flexibility of developing a programming language
• Writing interpreters and compilers using a well-structured approach
• Error handling and reporting in string input processing
• Parsers and parser expression grammars (PEGs) for building parsers automatically
• The benefits of writing parsers, including their applicability to various file formats and tasks
• Using PEGs for code generation and parsing
• Writing PEG files to define grammar rules and custom behavior
• The limitations of using PEG (Parsing Expression Grammar) for parsing, including difficulties with following complex rules
• Auto-generated code from PEG can be large and difficult to understand
• Comparison between writing a parser manually and using a parser generator like Yacc or Bison
• Difficulty in understanding grammars like BNF and EBNF without prior experience with parsers
• The books "Interpreter" and "Compiler" by Thorsten Ball, including their structure and how they build on each other
• Discussion of the Monkey programming language and its fate at the end of the first book
• Technical authoring and metaphor comparisons
• Computer interpretation vs compilation of code
• Go language compiler and optimization trade-offs
• Super-compilers for optimal performance optimization
• Interpreters (e.g. REPLs) for languages like Bash or scripting languages
• Introduction to Lush, a new embeddable scripting language being developed by Mark Bates
• Lush is designed as a superset of Monkey and Plush, with a focus on compile-time code generation
• Discussion of the trade-offs between custom parsing and using a PEG (Parsing Expression Grammar) for code generation
• Comparison between compilation and transpilation, with the two terms being used somewhat interchangeably
• The process of writing Lush involves understanding parsers and the underlying patterns behind code generation
• Lush's focus on code generation allows for more flexibility and maintainability compared to custom parsing
• Outputting strings from an intermediate language
• Unused variables in intermediate languages (Lush and Monkey) vs. Go
• Compilation step and outputting Go code for unused variables
• Intermediate layer or data flow analysis to detect used variables
• Perfection being the enemy of progress when adding features
• Excitement of making progress and seeing intelligent behavior
• Experience with Plush and PEGs (Parser Expression Grammars)
• Bootstraping a system and building higher-level constructs
• Danger of creating self-compiling languages like Skynet
• Discussion on Plush templates and how they interact with the Go standard library
• Trade-offs and consequences of adding new features to a programming language
• Use cases for generics in templating and parsing
• Challenges of implementing generics and maintaining backward compatibility
• Importance of considering long-term implications of language design decisions
• Discussion of a past project involving a templating language and its parser
• Use of PEG (Parsing Expression Grammar) in formatting code
• Promotion of Thorsten Ball's books on interpreting and parsing text
• Brief discussion about Amazon.com, including its international presence
• Lighthearted banter among the hosts about grammar and language conventions