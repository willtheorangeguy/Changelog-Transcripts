• Editors used in Go development
• Ramya Rao's involvement with VS Code and Go support
• Changes in project management and contributor base
• Gopls integration inside of VS Code
• Brief introduction to Gopls and its benefits
• History and development process of the Go plugin for VS Code
• Discussion of the Go language support system and its limitations
• Introduction of the Language Server Protocol (LSP) as a solution for language support in editors
• Explanation of how the LSP works, including providing navigation requests, completions, error diagnostics, etc.
• History of attempts to create a language server for Go, including Sourcegraph's initial effort and Google's eventual involvement
• Discussion of the benefits of having a single, universal language server (Gopls) that can be integrated with multiple editors
• Comparison of the old approach (editor-specific plugins) with the new approach using a language server
• Implications of having a common layer underneath all editors for language support
• Editor interactions and behaviors vary between different editors.
• Developers often think differently when using different editors (e.g., Vim users think in macros, while VS Code users think in multi-select).
• Peer pressure plays a role in choosing an editor, with developers wanting to fit in with their team or community.
• New features and updates can make it difficult for developers to keep up with the latest changes in an editor.
• Extensions and plugins can greatly extend the functionality of an editor, but writing them requires knowledge of JavaScript.
• Improving extension authoring guides for VS Code
• Lowering the barrier for developers to create extensions for VS Code
• Using JavaScript as a middle person to extend VS Code functionality
• Writing extensions in languages other than JavaScript (e.g. Go)
• Common keyboard shortcuts used by developers (e.g. Ctrl+Shift+O, Ctrl+B)
• Customizing VS Code key bindings and using extensions for key binding migration
• Key bindings for VS Code
• Using terminal in VS Code with Vim
• Customizing key bindings to improve productivity
• Using extensions to modify default behavior (e.g. font size)
• Navigating file history using Ctrl+Minus
• Go-specific features, such as "go to definition"
• Using hover-over documentation for symbols
• Consistency of language features across different languages
• Common API for language servers to provide editor features such as go-to-definition, hover, completion, and references
• Multiselect feature in editors like VC Code and its usefulness for tasks such as selecting all occurrences of a symbol or text
• Editor navigation shortcuts and their importance for developer productivity and competency
• Mastering keyboard shortcuts is not necessary for being a skilled developer
• Knowing some shortcuts can give a small edge in speed and productivity
• Syntax highlighting and color-coding can be useful in certain situations
• Personal preference plays a role in whether to use colors or not
• Not knowing basic skills (e.g. saving a file) can be more significant than not knowing shortcuts
• Plans for the Go support in VS Code, specifically focusing on debugging and language server improvements
• Current priorities: stabilizing the language server and getting feedback from users to improve it
• Ways for developers to get involved and help with improving the extension, including trying out the language server and reporting issues
• How to enable the language server in VS Code (through a setting)
• Future plans for debugging and refactoring features once the language server is stable