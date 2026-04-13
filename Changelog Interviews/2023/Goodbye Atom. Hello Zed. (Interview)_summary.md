• GitHub officially ending support for Atom text editor
• Discussion of Nathan Sobo's work on Atom at GitHub and its legacy
• Evolution of Changelog.fm's tone and style over the years
• Mention of a new Apple TV+ movie about Tetris and Henk Rogers
• Adam Stacoviak's interview with Henk Rogers in 2010 about the history of Tetris
• History of Atom and its impact on the development of Electron and VS Code
• Discussion of the creation of Zed, a new project from the same team that worked on Atom
• Nathan Sobo discusses his experience with Zed, a new social code editor, and how it's a second attempt at creating a tool that facilitates effective communication about code among developers.
• The mission of Zed is to build a well-crafted, lightweight, fast, and extensible tool that enables developers to collaborate on code.
• Nathan Sobo reflects on his previous experience with Atom, a code editor that he helped create, and how he learned from its limitations and challenges.
• He discusses how he and Antonio started working on a new project called Xray, which eventually became Zed, and how they learned Rust and built the editor from scratch.
• Nathan Sobo shares how he got "batted around" by different political winds inside GitHub and eventually left the company, but continued working on Zed in his spare time.
• Atom's mission and goals
• GitHub acquisition and its impact on Atom
• Why VS Code won and Atom lost in the market
• Electron and its limitations
• Mistakes made by Atom's team, including unclear leadership and technical decisions
• The importance of a clear business model and leadership structure
• Switching from JavaScript to a more performant language (Rust)
• Prioritizing performance and core experience over extensibility
• The strategy of Zed (Atom's successor), focusing on core experience and extensibility later
• The speaker discusses their performance requirements for a coding project, ranking extensibility, collaboration, and performance in that order.
• The speaker inquires about the connection between the Xray project and the Zed project, learning that there is a small amount of shared code.
• The speaker explains that they attempted to use Electron for rendering, but abandoned it due to performance issues.
• The speaker describes their development of a 2D rendering GPU thing and the creation of their own UI library, GPUI.
• The speaker explains the principles behind GPUI, including data flow, ownership, and event handling.
• GPUI is a system for modeling bi-directional data relationships between views and models in an app, allowing for efficient updates and rendering of UI elements.
• The system involves a tree of elements, where any view update triggers a full re-render of the window, rather than relying on diffing and mutation like React.
• GPUI is designed to be cross-platform, with platform-specific pieces isolated into small interfaces for easy porting.
• Zed, a code editor, is being developed on top of GPUI, with the goal of creating a native business model for the code editor space.
• Nathan Sobo, the founder of Zed, aims to create a business model that generates value and allows the company to capture enough of that value to continue innovating.
• Sobo believes that the code editor space needs a new business model, one that goes beyond license-based models and corporate patronage.
• Zed's development is motivated by Sobo's personal goal of creating the perfect code editor, rather than competing directly with existing editors like VS Code.
• Motivations for building Zed, a tool for communication and collaboration around code, rather than a quick route to riches
• The goal of creating a tool that facilitates real-time interaction around code, similar to Figma or Google Docs
• The current state of code editors, with limitations in communication and collaboration
• The innovation opportunity in tightly integrating code editing with real-time collaboration and conversation
• The competitive insertion of Zed in the code editor space
• The business model, which aims to fund the development of Zed through team subscriptions and open-source the editor itself
• The challenges of competing with established code editors like VS Code
• Discussion of the inspiration for the name "Zed" as an homage to the Unix editor "Ed"
• Concerns about shadowing the existing "Ed" editor and finding a similar name
• Introduction of the concept of open core, where some parts of the system will be proprietary while others are open source
• Discussion of the benefits of open core for hiring and community engagement
• Mention of the influence of Warp on the development of Zed and the importance of transparency and user control
• Business model and sustainability of open-source products
• Importance of open-source for long-term viability and community adoption
• Benefits of having a core team stewarding a product with community involvement
• Planned business model for Zed, potentially including subscription-based licensing
• Long-term vision for Zed as a platform for open-source collaboration and development
• Competition with GitHub and VS Code, with a focus on creating a new kind of open-source experience
• Changing editor tooling and what makes developers switch
• Product direction and business model based on developer needs
• Key enablers for a product, including performance, clean design, and team collaboration
• Defining "team" in the context of a multiplayer code editor and its implications
• Future features, including AI integration and animations inspired by video games
• Discussion of adding fun, non-essential features to Zed editor
• Examples of "cool" features in other software (e.g. Tesla's ability to dance, Cybertruck's bulletproof feature)
• Value of a "hacker spirit" in software development, prioritizing fun and creativity
• Expectations for users trying Zed for the first time, including a solid experience with Rust and TypeScript, and good performance and language server integration.
• Feedback and community engagement for Zed
• The importance of fast tooling and performance
• The conjoined triangles of success (L, W, and O) and the importance of identifying a clear mission
• Nathan's perspective on the success of Atom, viewing it as an incomplete success
• Zed's goals and competition, including Sublime Text and VS Code
• The need for extensibility and a large community of users
• The discussion revolves around the challenges of building a code editor with a balance of extensibility and core features.
• Nathan Sobo discusses the limitations of Atom, which focused too much on extensibility and not enough on core features.
• The importance of having a solid core before adding extensibility is emphasized.
• The panel discusses the potential competition with existing code editors like VS Code, Atom, and Sublime Text.
• Zed.dev, the new code editor, is introduced, with its focus on high performance, multiplayer, and extensibility.
• The panel expresses their support and enthusiasm for Zed.dev and encourages listeners to try it out.