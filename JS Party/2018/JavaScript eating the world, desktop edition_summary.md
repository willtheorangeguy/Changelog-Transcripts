• What Electron is and its purpose
• Development environment for Electron apps (similar to developing web apps)
• How Slack's app works with Electron (loading the web app inside the desktop app)
• Electron-specific tooling and libraries (improving development experience)
• Application architecture in Electron (main process vs render process, security considerations)
• Electron security concerns and sandboxing limitations
• Brave browser's experience with forking Electron and making changes to its security model
• Trade-offs between convenience and security in Electron development
• Proposed improvements to Electron's security by default, including disabling Node integration and improving permission handling
• Comparison of Electron's architecture to browser extensions and the evolution of architectures in extensions
• Best practices for keeping Node code out of the renderer process and using messaging instead
• Operating system design flaws from the 1970s lead to issues with app sandboxing and user trust
• Electron's pros include ease of use, good dev tools, and "batteries included" functionality
• Many web developers are familiar with JavaScript and its ecosystem, making it a popular choice for cross-platform apps
• Electron allows a wider range of developers to create desktop applications they wouldn't otherwise be able to
• The framework has had a significant uptake, with over 20% of developers reporting use in various industries
• Electron's memory usage as a trade-off for functionality
• Compositor team's efforts to reduce memory usage vs. speed trade-offs
• RAM's increasing availability in modern computers
• Concerns about targeting users with limited resources (e.g., low-end hardware)
• Optimizations for improving startup time and CPU performance in Electron apps
• Lazy loading of modules to improve startup time
• Electron Link and mksnapshot tools for pre-loading JavaScript code
• Electron core team and community growth, now around 15 people strong
• Four companies (GitHub, Microsoft, Atlassian, Slack) working on Electron full-time
• Broader ecosystem of tooling and libraries around Electron
• Community-driven contributions to improve Electron's features and usability
• Maintaining Electron as an open-source project can be demotivating due to negative comments from some users
• Being paid for maintaining the project makes a big difference in managing stress and negativity
• Working with developers from diverse backgrounds and companies is enjoyable and helps personal and technical growth
• The Electron community prioritizes inclusivity, diversity, and code of conduct
• New contributors can start by joining the Slack instance for maintainers or attending office hours
• Improving communication on project priorities, tasks, and contributors is an area for improvement
• Upcoming roadmap includes updates to Node core and collaboration with the Node community
• The Electron team holds a bi-annual summit to align on goals, discuss concerns, and foster team relationships.
• Keeping Electron up-to-date with the latest Chrome version
• Challenges of maintaining compatibility with rapidly changing Chrome APIs
• Efforts to improve velocity and correctness in staying current with Chrome
• Plans to switch to Chromium's build system (GN)
• Upstreaming patches from Electron to Chromium and Node.js
• Introducing modularity to enable parallel development and maintenance
• Relationship between Electron, the web platform, and progressive web apps