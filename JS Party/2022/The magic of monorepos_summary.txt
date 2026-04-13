• Monorepos in JavaScript
• Juri Strumpflohner's background and experience in software engineering and dev tools
• NX (a tool for coordinating and scheduling tasks) explained as a build system framework that integrates with other tools like WebPack, ESBuild, and Gulp
• NX's role in managing multiple projects within a workspace and its ability to coordinate tasks across them
• Scaffolding and generators in NX, similar to Create React App and Yeoman, for setting up new projects or adding components to existing ones
• Definition of a monorepo as a multi-project repository with shared code and relationships between projects
• Origins of NX (Next.js) as a tool for monorepos in the JavaScript ecosystem
• Characteristics of monorepos, including:
  • Package-oriented monorepos for sharing code across packages
  • App-heavy repositories for large applications with multiple domains
• Benefits of using monorepos, such as improved overview and composition of projects
• Drawbacks of moving to a monorepo setup, including potential complexity and need for careful planning
• Monorepo advantages: code sharing, collaboration, easy experimentation
• Potential drawbacks of a monorepo: increased CI time if not properly toolled
• Shared code within a monorepo: benefits and challenges (dependency chains)
• Addressing tangled dependency chains with tooling (e.g. module boundary lint rule in NX)
• Importance of defining good code practices and creating custom lint rules to enforce them
• Classification and customization of lint rules for different project types
• Benefits of plugin-based approach in NX
• Linting rules and their application in monorepos
• NX project graph and its visualization
• Dependency management and optimization in monorepos
• Common pitfalls in using monorepos (tangled dependencies, speed issues)
• Tools for addressing common pitfalls (NX caching, dependency filtering)
• Comparison and optimization of caching systems
• Overview of monorepo tools such as Lerna, Yarn workspaces, Pnpm, and NX
• Discussion of the trade-offs between different monorepo approaches (e.g. Lerna vs. Yarn/npmm workspaces)
• Explanation of NX's plugin-based architecture and its benefits for companies with large monorepos
• Description of NX's automated migration and tooling upgrade process using "nx migrate" command
• Benefits of using NX for migrations, including easy upgrades to WebPack 5
• Power of NX plugins in automating tasks and providing a more restrictive but beneficial configuration experience
• Importance of maintenance and keeping software up-to-date, with NX's ability to make this process easier
• Lightweight setup and flexibility of NX, as well as its appeal for enterprise environments
• Ratchets and boundary rules that ensure quality and prevent backsliding
• Unsolved problems in the monorepo world being addressed by NX, including reducing configuration repetition and improving TypeScript integration.
• NX tool for parallelizing tasks and caching
• Community plugins available for Python integration
• API allows hooking in custom extensions and project graphs
• AST parsing capabilities available for Python
• Automated migration framework provides a shell for user customization