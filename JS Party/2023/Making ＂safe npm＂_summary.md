• Introduction to a new project called Changelog, a podcast and newsletter combo
• Discussion of npm (Node Package Manager) safety concerns and vulnerabilities
• Announcement of a CLI tool called "Socket Safe NPM" or "NPM Safe"
• Explanation of how the tool works as a wrapper around npm to detect potential risks and alert users before installing packages
• Mention of Socket's threat detection tools and analysis of npm package safety
• Discussion of the importance of protecting developer machines from malware and arbitrary code execution
• Developer community reaction to CVEs is not to focus on them, as they can be overwhelming
• Current security tools alert developers to potential vulnerabilities after installation, but before it's too late
• New tool aims to step in before installation and alert about new scripts or changes in existing ones
• Tool will only alert when there are actual changes to scripts or dependencies
• Developers have different appetites for alerts, ranging from "leave me alone" to wanting every minor issue notified
• Security tooling focused on supply chain attacks and malware
• Importance of context in security tools to avoid false positives and noise
• Balancing security alerts with developer productivity and user experience
• Differentiating socket from other security tools that prioritize scaring or blocking developers
• The goal of socket is to educate developers about potential issues rather than overwhelm them
• Development of a wrapper program for npm
• First attempt to match npm's interface was scrapped due to maintenance issues
• Second attempt used dry run mode, but did not provide enough information for a good user experience
• Third iteration used arborist library to replace part of npm and provide full dry run functionality
• Discussion of difficulties in mocking and patching es modules compared to common js
• Description of how the wrapper program works with arborist to provide detailed package version information during dry runs
• Virtual file systems are hard to implement without getting into edge cases
• A wrapper is being used to intercept and override library functions for security reasons
• The wrapper causes performance issues, but analysis is done remotely on the company's servers
• There is a risk of malware being downloaded if the wrapper doesn't catch it first
• npm and Socket APIs are relied upon by end users, potentially creating two points of failure
• The project is not open-source yet due to instability and lack of standardization
• Discussion of how socket security works with npm and npx
• Introducing a new business that offers coaching services for non-technical problems
• Explanation of how to make npm safe using the command line interface
• Considering support for yarn and pnpm, including potential difficulties with integration
• Comparison of package management in different ecosystems, with a focus on JavaScript
• npm's behavior of installing two versions of a dependency when both are required by different dependencies
• Package manager conflicts and how they handle multiple versions of a package
• Arborist library for version resolution and ideal tree building
• Monkey patching npm on Linux systems using custom arborist code
• Shipping shims to alias npm commands and changing behavior at runtime
• Windows support and the need to disable certain features due to bugs
• Support for Windows is not programmatically safe, but WSL (Windows Subsystem for Linux) is supported.
• Bundling npm with an app can intercept the system's npm, as long as it's installed in the path.
• Npm's bin directory is considered deprecated and should not be relied upon.
• Remaining implementation details to be addressed include handling edge cases around installations from Git repositories and adding more configuration options.
• Feature requests include a VS Code plugin that highlights issues with Socket.
• Discussion of upcoming episodes on the JS Party podcast
• Review of recent episodes and after-show content for Plus Plus members
• Debate between yarn and npm, with a discussion of their relative merits and drawbacks
• Mention of new package managers (dino) and other alternatives to node
• Reflections on the role of competition in driving innovation and improvement in the JavaScript ecosystem
• Warts in current language make switching to something new appealing
• Inertia from existing systems is a significant barrier to adoption
• Dino has specific requirements that may limit its adoption (greenfield projects, tutorials, security system)
• Bun takes a more compelling approach by building on top of Node and TypeScript integration
• Adoptability is key for successful language changes, with superset or API-compatible approaches easier to adopt than starting from scratch