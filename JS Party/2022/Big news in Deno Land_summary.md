• Ryan Dahl discusses the recent release of Deno 1.28, which includes an npm compatibility layer
• The layer allows users to import npm packages directly into their Deno projects without requiring manual installation
• This is achieved through a technical implementation that uses a proxy and Rust code to download and manage npm packages
• The goal is to make it easier for developers to use Deno by allowing them to leverage the vast library of npm packages
• The compatibility layer also includes security features, such as conditional access control, to mitigate risks associated with importing external packages
• Ryan Dahl explains that this decision was pragmatic, aiming to solve real-world problems and increase adoption of Deno
• Conditional access and permissions system for Deno
• Limitations of specifying access on a package-by-package basis in JavaScript
• Process-wide permissions and conditional access
• Future development: shadow realms and more granular control over access
• Compatibility with existing Node modules and JavaScript syntax
• Challenges of maintaining backwards compatibility
• Concept of "JavaScript containers" and Deno Deploy serverless system
• The Unix part of Deno Deploy is shrinking while the JavaScript business logic is growing
• Abstraction layers in cloud services are being raised with Deno Deploy providing only JavaScript, rather than packaging it inside a Unix container
• Cold start times for Deno Deploy are around 400-300 ms, with warm response times around 40 ms
• Deno Deploy is built on top of public cloud infrastructure (GCP and AWS regions)
• Other companies like Vercel and Cloudflare Workers are providing similar services to Deno Deploy
• Goals for Deno Deploy include reducing cold start times to under 100 ms worldwide within the next couple of years
• Winter CG: a community group aiming to standardize server-side JavaScript APIs
• Deno's goal to be the fastest JavaScript runtime and competition with other runtimes
• Critique of benchmark numbers and cherry-picking examples
• Discussion of complexity and maturity in large software projects, such as Node and Deno
• WebAssembly's potential role in serverless computing and edge computing
• Unique capabilities of Deno Deploy for rapid deployment and low-code development
• The analogy is drawn between ImageMagick and WASM, where JavaScript is to Bash as WASM is to Elf executable.
• Deno Deploy allows calling into WASM apps from JavaScript apps, and vice versa.
• Ryan Dahl sees the customer base for Deno Deploy as a mix of indie programmers and larger providers, empowering them to do things they couldn't before.
• Edge compute is becoming more prevalent, with Deno Deploy allowing complex scripting in JavaScript at the edge.
• There are open questions around state management and data stores for edge applications, including geo-replicated databases.
• CockroachDB, Spanner, and Dynamo DB are mentioned as off-the-shelf solutions for geo-replicated databases.
• Ryan Dahl mentions an R&D effort to create a first-party storage solution alongside other Deno features.
• Deno's growth and user adoption
• Persistence of building a programming platform
• Measuring success with weekly user numbers
• Node vs Deno and changing perceptions over time
• Future plans for expanded npm support in Deno
• Addressing deployment size concerns with npm dependencies
• ChatGPT integration and scraping data from websites