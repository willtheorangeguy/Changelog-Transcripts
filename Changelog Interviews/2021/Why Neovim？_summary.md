• Introduction to The Change Log podcast and its guest, TJ DeVries, a core maintainer of NeoVim
• Discussion of NeoVim, including its creation, differences from Vim, and features such as Lua configuration and plugins
• Introduction of the guest, Nick Neesey, and his experience with NeoVim
• Discussion of the process of switching to NeoVim from Vim and the benefits of doing so
• Mention of a previous episode on Vim and the popularity of NeoVim
• Introduction to Gitpod, a platform for automated dev environments, and its features and benefits
• Tiago Taruda created NeoVIM about 10 years ago as a way to add external job functionality to VIM
• Taruda's patches were initially rejected due to compatibility issues with Windows and other platforms
• NeoVIM was created as a separate project to allow for more experimental and forward-thinking development
• NeoVIM and VIM share a large codebase and many patches are ported from VIM to NeoVIM
• NeoVIM has some key differences, including:
  • Not shipping with a GUI by default
  • Implementing GUIs over RPC instead of tightly coupling it to a GUI application
  • Removing some plugins and features that are specific to VIM
  • Having a different set of default keybindings and commands
• Discussion of NeoVIM and VIM usability and performance
• Comparison of NeoVIM and VIM async job support and other features
• Bram's development approach and potential influence from NeoVIM
• Differences in APIs and implementation between NeoVIM and VIM
• Discussion of NeoVIM's use of lib UV and its event loop
• Discussion of implementation differences between Vim and NeoVim
• Portability of plugins and code between Vim and NeoVim
• Shared APIs and libraries between Vim and NeoVim
• Challenges and complexities of maintaining shared codebases
• Plans for creating a unified Lua API for floating windows
• Expectations for future code sharing and porting between Vim and NeoVim
• Retool's program for startups and its features
• Frustrations with VimScript and its limitations
• Contrast with Emacs Lisp and its relationship to the editor
• Introduction of Lua as the new scripting language for NeoVim
• Advantages of Lua, including performance, embeddability, and static language
• Comparison with JavaScript, which was considered but ultimately discarded
• Design principles of Lua and its purpose as an embedded scripting language
• NeoVim's architecture and its suitability for using Lua
• Performance benefits of using Lua in NeoVim, including speed and efficiency
• The conversation is about porting a Vim config to Lua in NeoVim
• The speaker, Nick, has experience with Vim script but not with Lua
• He initially found it difficult to use Lua but eventually converted his config to Lua and saw benefits
• The benefits include reduced lines of code and increased power
• TJ mentions that NeoVim is still missing some features to make configuration in Lua fully elegant
• Some parts of the config, like auto commands, still require VimScript
• TJ suggests that switching to init.lua is not necessary, but rather extending specific parts of the config with Lua is more beneficial
• Lua has advantages in ergonomics, such as using closures and passing functions around easily.
• Comparison of VimScript and Lua configuration options
• Advantages of using Lua in Vim configuration, including auto commands and object-oriented programming
• Challenges of translating VimScript to Lua and vice versa
• Project to transpile VimScript to Lua and maintain semantic consistency
• Potential for NeoVim to gain popularity over Vim due to its Lua support and plugins like Limelight
• Goal of keeping Vim and NeoVim "friendly" and compatible
• Discussion about the limitations of integrating TreeSitter into some editors
• Mention of NeoVim-only plugins and the potential for plugins to be exclusive to Vim or NeoVim
• Emphasis on the NeoVim team's goal of coexisting with the Vim community, not trying to replace it
• Discussion about the history and evolution of Vim and NeoVim, with a nod to Bram's contributions
• Lighthearted jokes about the "hostile takeover" and "long con" aspects of some open-source projects
• Shift to discussing the Square platform and opportunity for developers to build apps for sellers
• Introduction of Shannon Skipper, head of developer relations at Square, to discuss the opportunity for developers on the Square platform
• Development on the Square platform's seller trust
• Release of NeoVim 0.5 and its features
• History of Language Server Protocol (LSP) development in NeoVim
• Benefits and goals of LSP, including reducing M times N problems
• Explanation of how LSP works, including communication between editors and servers
• Comparison of VS Code and Vim development experiences, including use of LSP
• Origins and design of LSP by Microsoft
• LSP (Language Server Protocol) allows for communication between editor and language tools in a standardized way
• LSP can be used to customize editor functionality, such as going to definition
• LSP can be implemented in various ways, including as an external program or as a built-in binary
• Communication with LSP is typically done over standard input/output or TCP, with JSON used for request and response formatting
• NeoVim can spin up an LSP process and communicate with it through standard input/output
• LSP can be used to implement editor functionality in a modular and customizable way
• Example of using LSP to implement a custom "go to implementation" feature in NeoVim
• Discussion of how LSP can be used to create a standardized interface for language tool makers and editor tool makers to interact with each other
• LSP (Language Server Protocol) and its interaction with NeoVim
• Installing and configuring LSP servers for NeoVim
• Difference between LSP and TreeSitter
• TreeSitter's role in handling syntax trees and error recovery
• Comparison of LSP's project-wide scope vs TreeSitter's file-by-file scope
• TreeSitter is incremental, only parsing the necessary parts of a file, not re-parsing the entire file.
• TreeSitter generates a tree structure of the file, allowing for named nodes and ranges.
• This allows for better and more powerful syntax highlighting, especially for complicated file types.
• TreeSitter is a separate library that can be embedded in other editors, and is designed to be fast and performant.
• To use TreeSitter in NeoVim, a separate plugin is not required, but can be used to simplify configuration.
• However, an extra step is required to generate bindings, which can be done manually but is considered complicated.
• The conversation is about NeoVim and the TreeSitter plugin
• The speaker mentions that TreeSitter grammars should be included in NeoVim core for languages like C, Lua, and VimScript
• The plugin "nvimtscommentstring" is discussed, which automatically updates the comment string option based on the language detected by TreeSitter
• The plugin can handle languages embedded within each other, such as JavaScript and HTML, and can comment out code correctly in these cases
• Another example is given of using TreeSitter to highlight C code within Lua files
• A snippets plugin called Lua Snips is mentioned, which allows running Lua code to generate text as snippets are expanded
• The speaker wrote a Lua snippet that uses TreeSitter to query the return type of a function, making it easier to write code in languages like Golang
• Discussing the features and capabilities of TreeSitter
• Exploring the potential of snippets in editors
• Introducing Telescope, a fuzzy finder for NeoVim
• Describing Telescope's design and goals, including extensibility and configurability
• Comparing Telescope to FZF and discussing potential use cases
• Mentioning ongoing development and performance improvements for Telescope
• The speaker likes FZF but uses Telescope for daily use
• The speaker recommends using both FZF and Telescope for specific use cases
• The speaker prefers Telescope's UI and consistency
• The speaker notes that Telescope integrates well with other editor features
• The speaker discusses the excitement and enthusiasm around the NeoVim 0.5 release
• The speaker invites people to join the NeoVim community and contribute
• The speaker shares resources for getting involved with NeoVim, including a chat room on Element or Matrix
• Discussion of community engagement and welcoming open-source projects
• Sharing personal experience with contributing to NeoVim and receiving help from the community
• Tips for contributing to open-source projects, including commenting on issues and asking for help
• Importance of appreciating the people behind proprietary software
• Requesting guests and topics for future episodes of the ChangeLog
• Final words and shoutouts to the audience and Twitch channel
• The Galaxy brand move is to get the master feed at ChangeLog.com slash master
• All podcasts are available in a single feed
• Special thanks to partners Linode, Fastly, and LaunchDarkly
• Special thanks to Breakmaster Cylinder for music
• End of episode