• Keeping Node Core small and modular
• Limiting features added to Core to prevent breakage and promote stability
• Encouraging more modules and less in-Core functionality
• Addressing issues with pre-packaged dependencies and the inability to choose specific module versions
• Considering removing certain libraries from Node Core, such as URL and Promises
• Discussing solutions for handling dependencies and breaking changes when removing or changing libraries
• Adding a WHATWG compliant URL parser to Node's internals for consistency
• Vendoring in third-party modules instead of duplicating functionality
• Deprecation and removal of Node's built-in URL library
• Using npm-installed versions of libraries for userland code instead of built-in ones
• Punycode module being deprecated and possibly removed due to low usage
• Concerns about breaking changes if removing or deprecating the URL library
• Criteria for determining what should be in Node Core vs userland modules
• Deprecating and removing outdated or obsolete modules
• HTTP/2 module, including potential performance benefits and implementation challenges
• Pre-built binaries for Node ecosystem to facilitate easier installation of native dependencies
• URL library deprecation and replacement with a better version
• Websocket APIs and their relationship to Node Core vs userland modules
• Node HTTP API and its complexity
• Tradeoffs between performance, implementation ease, and maintenance costs
• HTTP/2 protocol implementation and its implications for Node
• Streams module: design issues, user problems, and alternative solutions
• Soft deprecation approach for deprecated modules (e.g. Streams)
• Potential movement of streaming capabilities to libuv
• Maintenance and documentation strategies for Node Core
• Changing the API to force correct usage of Streams
• Potential breaking changes causing issues in dependent modules
• Documentation updates as a solution
• Educational process (blog post, etc.) to inform users about the change
• Plans to eventually remove Streams from Node Core
• Readable Streams documentation improvement