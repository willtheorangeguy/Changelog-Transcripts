• Brandon Mathis discusses Octopress 3.0, a major rewrite of the project
• Octopress 2.0 is no longer supported, and 3.0 is a significant improvement
• Brandon has been working on Octopress 3.0 for two years, learning new skills and refining the project
• He has poured energy into making Octopress a valuable tool for others, rather than writing about other topics
• Octopress 3.0 has not been widely announced or promoted due to Brandon's focus on other projects and personal life
• Open source projects often require more contributors or a single leader to maintain and improve the project
• Brandon is a friend of the Jackal team and has participated in their online conference, Jackal Conf
• Discussion of Tom's request to add specific features to the Octopress core
• Explanation of Octopress's tagline evolution and the mention of Hacker News
• Description of Octopress as a tool that allows the creator (Jackal) to "jump into a Ferrari" and showcase his skills
• Discussion of the history of Octopress and its name, including the possibility of it being a play on the word "WordPress"
• Explanation that the name "Octopress" was actually chosen because the creator likes octopuses and thought it was a cool name
• Mention of the creation of the Octopress logo and the process of designing it
• Discussion of the creator's experience with WordPress and how it led to the creation of Octopress
• Recounting of the creator's early days with GitHub, including their first day joining and the excitement around the platform
• Conversation about the dates of joining GitHub and the comparison of joining times between the creator and others.
• Discussion of a visit to Pivotal Labs and meeting with Tom Preston-Warner and Chris Wanstrath about GitHub
• History of GitHub and its early days
• Octopress 1.0 and its development, including learning from initial GitHub code
• The current state of Octopress 3.0 and its evolution
• Comparison of Octopress to other projects, including Daniel Stenberg's 17-year-old project Curl
• Brandon's side projects, including a personality profile test and an HSL color picker
• Discussion of the end of life for Compass and Chris Wanstrath's new project, Spectacles/Speckle
• The speaker is not actively contributing to the Compass team and has been busy with other projects.
• The speaker wrote a book with Chris and Natalie, and has also worked on Octopress.
• Octopress is a collection of tools to make working with Jekyll sites better and more fun.
• The speaker has been working on Octopress 3.0 for about two years, which is a complete rewrite.
• The speaker notes that Octopress 2.0 had some deficiencies, particularly with regard to plugin management.
• The speaker explains that Octopress 2.0 was a "repo that you fork or clone and then run some commands" but had problems with merge conflicts.
• The speaker acknowledges that they didn't know how to build gems, which contributed to the issues with Octopress 2.0.
• Issues with maintaining and updating Octopress due to its complexity and fragility
• Problems with merge conflicts and code management when publishing updates
• Need for a simpler deployment process, which is now facilitated by Ruby gems and bundler
• Difficulty in maintaining a command-line interface due to lack of Ruby skills
• Attracting novice developers who submitted issues without fully understanding the system
• Difficulty in separating concerns and making the system testable
• Challenges in breaking down the system into separate, reusable components
• Problems with the original Octopress deployment method using Git, including tracking of unnecessary files and difficulty with adding or removing parts of the system
• Octopress 3.0 is a rewrite and not just an update, with a new architecture that allows for easier adoption and customization
• 3.0 is shipped as an independent gem with its own tests and CLI, making it easier to use with any Jekyll blog
• Octopress 3.0 has a more modular design, with separate plugins and a main gem that provides CLI tools and templates
• The getting started process for 3.0 involves creating a new Jekyll site and installing the Octopress gem
• Octopress 3.0 provides tools for working with posts, pages, drafts, and deployment, including post and page templates and a CLI for generating new content
• The new design makes it easier to use Octopress with Jekyll, especially for developers who are new to Jekyll or don't know much about its file system-based architecture.
• Creating a new draft in Octopress
• Automating tasks such as metadata changes and date formatting
• Introducing the "octopress new draft" command
• Publishing and unpublishing posts using the "octopress publish" and "octopress unpublish" commands
• CLI system architecture and extensions using gems
• Deployment options, including Rake files and separate gems for deployment
• Comparing Octopress to Jekwa and Middleman
• The benefits of using Octopress for hackers and tinkerers
• Octopress has options for deploying and new page themes, but lacks a templating system for pages in version 2.0
• The speaker is rebuilding and expanding upon these features in Octopress, focusing on user interface and design
• Octopress now includes a debugger for Jekyll templates and a command-line tool for testing and debugging
• A testing framework called Clash has been developed for Jekyll, allowing for easier creation of plugins and frameworks
• Several plugins and themes have been developed for Jekyll, including Code Blocks, Ink, and Littlefoot
• The speaker's goal is to make Octopress a comprehensive platform for Jekyll developers, with a focus on user experience and design
• Jekyll is used for the speaker's personal and company websites.
• The speaker expresses frustration with making changes to their Jekyll sites and blames it on Jekyll.
• The speaker discusses the Web 2.0 show and how Skype grabbed a preview of a page with a suspicious title.
• The speaker shares a personal experience with hacking on their WordPress site and the need for a static site.
• The speaker mentions a GitHub show and warns against visiting the site due to malware concerns.
• The speaker discusses the Octopress org repository and notes that the Docker one is lacking, but is being worked on.
• The speaker discusses the benefits of using Docker for Octopress and Jekyll, including ease of use and management.
• The speaker mentions a CLI for Octopress and how it can enable GUI development and other features.
• The speaker highlights the Octopress inc system as a key feature for Jekyll theming and its potential to simplify plugin development.
• Octopress Inc is a plugin that combines stylesheets and JavaScript files into a single asset
• It allows for fingerprinted and compressed assets, as well as customizable compression settings
• Octopress Inc plugins are automatically combined into a single stylesheet or JavaScript file based on gem load order
• The Octopress asset pipeline adds local style sheets and assets to the asset pipeline
• Octopress Inc allows for configuration of individual plugins, with features such as command-line listing of installed plugins and assets
• Multi-language support is available through Octopress Multilingual
• A plugin scaffold can be generated to create a gem with a theme, including JavaScript and stylesheet files
• The roadmap to Octopress 3.0 is discussed, with six steps outlined in a release plan
• The current status of the release plan is that the Octopress to Octopress Org migration is the next step
• Octopress 3.0 will be the canonical version, while the other one is a vestigial repository for legacy purposes.
• The speaker needs to write and publish a migration guide for users.
• The new Octopress site will use a documentation system that collects information from gems and repositories.
• The speaker is working on a new default theme, which will be a major redesign.
• The new theme will have a lot of flexibility and will make it easy to add features like large image headers.
• The speaker is considering how to make the theme easy to edit and maintain.
• The speaker wants to set up a good pattern for theming in static sites, anticipating that people will fork and modify the theme.
• The new theme will be designed with learning and ease of use in mind.
• Desire to create a new theme, "Octopress Genesis", and have users easily fork and create their own versions
• Current state of the theme, including its documentation and potential for migration issues
• Challenge of writing a migration guide that accounts for various user modifications and customizations
• Plan to move the Octopress repository to a new, legacy branch for maintenance
• Desire to preserve links and user experience when transitioning to a new repository
• Discussion of how to handle migration from one repository to another, particularly when there are links pointing to the old repository.
• Challenges with GitHub and managing issues
• Benefits of the new system and collaboration with users
• Current development priorities, including releasing Octopress 3.0 and Octopress Inc
• Need for documentation and guides for new users
• Ways to help with the current release plan, including contributing to Octopress on GitHub and providing feedback on the migration process
• Encouragement for users to try the new system and provide feedback and support
• Discussion of migrating from Octopress to Octopress 3.0
• Steps to migrate, including removing old plugins and adding new gems
• Importance of understanding Jekyll and starting with a new Jekyll site
• Recommendation to try out Octopress CLI and new plugins
• Request for feedback and discussion on migration path
• Programming hero, Chris Coy, and his work on CSS tricks and Code Pin
• The origins of the name "Sassway.com" and its connection to the Ruby and Rails communities
• The Sass language and its benefits for writing CSS
• The creation of the Sass podcast (The Changelog) and its role in promoting Sass
• The evolution of the name "Sass Tricks" and its relationship to CSS Tricks
• The distinction between Jekyll and Octopress, and the reasons for maintaining the Octopress brand
• Upcoming show with guest Peter Burgoyne, author of "Go Kid" and expert on Go in the enterprise