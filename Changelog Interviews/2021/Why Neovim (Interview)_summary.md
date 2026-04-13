• History of Neovim and its creation
• Reason for Neovim's existence, specifically asynchronous job support
• Similarities and differences between Neovim and Vim
• Backwards-compatibility and shared codebase
• TJ DeVries' explanation of the project's branching point and evolution
• Nick Nisi's experience with Neovim and its advantages over Vim
• Jerod Santo's experience with Neovim and its similarity to Vim
• Development of Vim and Neovim's async capabilities and their differences
• Debate on whether Neovim's development spurred Vim's improvement or if it was simply a natural progression
• API and implementation differences between Vim and Neovim, particularly with async jobs and floating windows
• Efforts to create shared code and plugins to ease development for both Vim and Neovim
• Trend of shared codebases and patch porting between Vim and Neovim
• Discussion of Vimscript and its limitations compared to other scripting languages like Lua
• Emacs has its own programming language, Emacs Lisp, which is designed to be a programming language and allows users to rewrite parts of the editor.
• Vim was designed as a text editor and its configuration language, Vimscript, was added later and is considered a mess.
• Neovim chose Lua as its configuration language due to its embedability, size, portability, and stability.
• Lua is designed for embedding in other languages and provides a safe and easy way to script and extend applications.
• Neovim's use of Lua has made it more accessible and exciting for users, including those with previous experience with the language.
• The Lua configuration in Neovim is optional and users can still use Vimscript to configure the editor.
• Users can choose to convert their Vimscript configuration to Lua, which can result in a more powerful and elegant configuration.
• Discussion of writing configuration files in Vimscript versus Lua
• Comparison of Vimscript and Lua for scripting editor features
• Benefits and drawbacks of using Lua for configuration
• Portability and translation of configurations between Vimscript and Lua
• Future of Vim and Neovim configuration and plugin development
• Implications of Neovim-exclusive plugins on the Vim community
• Efforts to keep Vim and Neovim configuration and plugin development aligned
• LuaJIT installation and native C module linking for faster sorting
• Coexistence and compatibility of Neovim and Vim
• Frustration with community behavior regarding Neovim's fork of Vim
• Release of Neovim 0.5 with significant updates, including LSP and tree-sitter
• Language Server Protocol (LSP) explanation and its benefits
• LSP's purpose and functionality in communicating language smarts between editors and servers
• LSP (Language Server Protocol) is a standard way for language tools and editor tool makers to interact with each other.
• The protocol allows for customizability and flexibility in how language tools and editors interact.
• LSP can be used with various programming languages, including Go, Python, and TypeScript.
• Neovim's LSP client is written in Lua and is designed to be an interface between the editor and the language server.
• The language server can be a separate executable or a binary on the machine, and can communicate with Neovim over STDIN/STDOUT or TCP.
• To add support for a new language, a developer would need to provide their own LSP or plug in an existing one, rather than modifying Neovim's code.
• Tree-sitter is a separate technology that deals with a single file and its syntax, whereas LSP operates on a project-wide level.
• Tree-sitter is built into Neovim, and can be used for things like syntax highlighting and code completion.
• Tree-sitter is a library for writing error-recovering incremental parsers, useful for text editors
• Tree-sitter is incremental, meaning it doesn't reparse the entire file on every keystroke
• Tree-sitter allows for syntax highlighting and other features, but its most exciting aspect is its ability to handle multiple languages and parse them incrementally
• Tree-sitter is a separate project from Neovim, but is embedded inside it
• Neovim tree-sitter is a plugin that makes it easier to use tree-sitter in Neovim
• Tree-sitter is driving innovation in Neovim plugins, enabling features beyond just syntax highlighting
• Examples of tree-sitter's capabilities include detecting the current language and updating comment strings accordingly
• Tree-sitter queries can be used to highlight specific code blocks as if they were written in a different language
• LuaSnip plugin can run Lua code to generate text snippets
• Telescope is a fuzzy finder written in Lua that is highly customizable and extensible
• Telescope is not yet as fast as fzf for very large searches, but is nearing completion of a performance-boosting PR
• Using both fzf and Telescope may be a good approach for different use cases
• Neovim's UI consistency and user experience
• Telescope's beautiful UI and consistency with Neovim's theme
• Enthusiasm around Neovim's 0.5 release and its capabilities
• Community engagement and involvement with Neovim
• Joining the Neovim chat (on Element, Matrix, Gitter, or IRC) to ask questions and get involved
• Contributing to Neovim through issues and PRs, and getting help from the community
• Appreciation for user feedback and support for open-source software maintainers