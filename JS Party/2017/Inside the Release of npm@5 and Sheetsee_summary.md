• Introduction and host introduction
• Background and motivation for npm@5 release
• Cache rewrite performance improvement (5x speed increase)
• Additional performance updates and improvements
• Usability improvements in npm@5, including default save functionality
• Symlink feature and its benefits for monorepo development
• Future plans and ongoing work on improving monorepo support
• Optimizing default behavior in npm
• Introducing new configuration options (--prefer-offline, --prefer-online)
• Planning for a "low-mem" mode to reduce memory usage
• Breaking down npm into smaller, reusable components
• Avoiding dependency hell and maintaining flat installs
• Providing building blocks for custom package managers
• npm 5 supports all sources, including Git, with new semver support
• npm 5 includes building and installing Git dependencies as step dependencies
• npm 5's registry and package lock differ from yarn in terms of performance and lockfile management
• npm 5 guarantees exact directory structure for installed modules, unlike yarn which only stores relationships between modules
• concerns about post-install scripts still exist, but can be mitigated by using ignore scripts or running code in a sandboxed environment
• there is ongoing work to prevent automated self-publishing worms and mitigate other security risks
• npm@5 issues with breaking changes
• Revisiting ecosystem concerns about scripts in package-lock.json and npm-shrinkwrap
• Known issues with npm@5 and plans for release
• Breakdown of changes in npm@5, including save by default and lockfile changes
• Shrinkwrap usage and compatibility with npm@5
• Introducing Sheetsee library for visualizing data from Google Spreadsheets
• Use cases for Sheetsee, such as static websites and internationalization
• Using spreadsheets as a settings page to generate websites
• Utilizing Google Sheets features, such as GPS coordinates in addresses
• Connection of Sheetsee to Tabletop.js for data retrieval and JSON generation
• Handling scalability and potential server issues with Sheetsee
• Integration with Glitch.com for easy server setup and backup
• Possibility of syncing data locally using Pouch or service workers
• Error handling in Tabletop, particularly dealing with failed Google Spreadsheet connections
• JavaScript tooling often involves complex compile chains
• Alex Sexton reminisced about building his first website at age 10 using members.aol.com and encountered difficulties with database concepts
• He struggled to find information on retrieving data from a central repository without knowing the term "database"
• Rachel White presented her pick of the week: Chaosbot, an experimental GitHub project that updates its own code through democratic voting
• Mikeal Rogers is fascinated by Chaosbot's concept and has been following its development
• Alex Sexton mentioned his favorite project on GitHub: Babili, a beta ES6 minifier for shipping modern JavaScript code to browsers
• The speakers discuss their current projects and experiences with WebRTC and Node.js.
• pkg, a new tool from Zeit, is introduced as a way to turn Node projects into single executable files.
• A Medieval Fantasy City Generator tool is mentioned and shared in the live chat.
• The speakers also mention their enthusiasm for using ES6 features in WebRTC experiments.