• Bandwidth for Changelog is provided by Fastly
• Sponsor: Rollbar
• Importance of catching errors before users do
• Benefits of using Rollbar for error resolution and debugging
• Approaches to debugging JavaScript applications
• Use of dev tools, including console tab, debugging with breakpoints, and stepping through code
• Approaches to identifying the source of a bug (Suze: starting high level and digging deeper; Jared: blaming others before looking inward)
• Identifying the root cause of bugs vs symptoms
• Importance of isolation and identification in debugging
• Using tracing tools and debugger to diagnose issues
• Challenges with complex codebases and JavaScript's build tools
• Techniques for isolating bugs and setting up traces
• Using console statements, debugger, and logging to aid debugging
• Tips for speeding up the debugging process
• Utilizing dev tools tricks and features like storing temporary variables
• ES6 syntax allowing objects to be created with variable names as keys
• Destructuring feature and its opposite, where a key is the value
• Console.table functionality for displaying data in a tabular format
• Creating custom logging displays in Chrome Dev Tools
• Plotting coordinates or geographic locations in the console using plot or graph features
• Styling console output with CSS-like syntax for better readability
• Development tools for logging and debugging in Node.js
• Using a debug module to create styled and contextual logs
• Lightweight solutions for teams working together on development
• Importance of tracing specific issues in libraries vs applications
• Large teams often leaving log statements in code due to recurring problems
• Dev tools and tricks, including black boxing, and build process optimization
• Blackboxing scripts in dev tools to exclude library code from stack traces
• Using dollar sign zero ($0) to refer to the currently focused element in the elements panel
• Using dollar sign underscore (_ ) in the console to pull up the last return statement
• Dragging and dropping elements in the elements panel to reorder the DOM
• Generating a screenshot of a single element using command/ctrl shift P and selecting "Capture node screenshot"
• The speaker discusses using Chrome DevTools to take screenshots of specific page elements and storing them.
• Conditional breakpoints are mentioned as a useful feature for adding logging to pages without having to stop JavaScript execution.
• DOM breakpoints are discussed, allowing users to pause on modifications to specific elements or their children.
• Mutation observers can be used to emulate this functionality but Chrome DevTools provides an easier solution.
• The speaker also mentions using the console's "get event listeners" method to view and inspect event listeners attached to page elements.
• The job search platform Hired is discussed, with features such as companies sending offers with salary and equity upfront, and the ability to accept or reject offers online.
• The spread operator in JavaScript is explained, including its use to expand an array into another one and uniqueify arrays by combining it with sets.
• The bang bang operator (!!) is mentioned as a way to convert falsie values (such as null, undefined, empty string) into Boolean false.
• JavaScript binary literals
• Easy Off Bam cleaner ad reference to the "bang bang" song
• Discussion of hexadecimal vs binary notation in programming
• Explanation of binary literals in JavaScript, including examples and use cases
• Personal anecdote about learning about binary literals too late for a steganography project
• The speaker's nostalgia for cryptography and steganography from their childhood.
• Using the bitwise operator (~) to shift index values in arrays.
• ES 2015 APIs for handling array operations, such as find() and findIndex().
• Array destructuring with regular expressions to capture and assign variables.
• Using destructuring to improve code readability and accessibility.
• The conversation centers around potential issues with real-time feedback in console executions.
• Discussing the nuances of commas in code for variables, specifically their use to indicate omission.
• Mentioning the benefit of using const and its implications on variable scope.
• Touching on the topic of clean Git history, referencing an article from changelog.com/GitLab.
• Exploring the importance of meaningful history and understanding change flow in projects.
• Discussing personal opinions on the value of clean Git history and its benefits when working with teams.
• Importance of descriptive and succinct Git commit messages
• Usefulness of clean commit history in debugging and finding bugs
• Value of high-quality commit messages for future reference and maintenance
• Dangers of poorly written comments or misleading commit messages
• Benefits of avoiding merge commits and keeping the branching history clean
• Need to balance complexity with clarity when structuring commit history
• The importance of presenting code history accurately versus manipulating it for cleanliness
• The trade-off between rewriting history and preserving the original commit order
• Keeping attribution when working on teams and avoiding squashing others' commits
• Situations where rebasing and merging are acceptable or necessary, such as solo work or long-running feature branches
• Common pitfalls to avoid in code history management, including losing merge commit context and creating convoluted histories
• Conflicts with rebase in Git
• Solving merge conflicts on a live stream
• Rewriting history in Git and force pushing
• Risks and implications of force pushing in collaborative environments
• Setting up GitHub to prevent accidental force pushes
• Amending commits and force pushing with flags (-force-with-lease)
• GitHub's feature for merging pull requests directly from the UI
• Benefits of using GitHub's merge features (e.g., fast forward merge, squash and merge) over command line options
• The importance of communication when working on shared repositories