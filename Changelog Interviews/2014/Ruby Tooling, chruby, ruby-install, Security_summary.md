• Introduction to Postmodern and his background in security research and development
• Discussion of the pronunciation of "chroot" and "ch ruby"
• Overview of Postmodern's projects, including ch ruby, ruby install, and ronin
• Explanation of ch ruby and its purpose (managing multiple ruby versions on a system)
• Mention of other ruby version managers, such as rvm, rbm, and chruby
• Discussion of Postmodern's experience with rvm and his decision to create ch ruby
• Problems with RVM
• Criticism of RVM's bash scripts and platform-specific issues
• RVM's installation limitations and the need for global rubies
• Research into alternative Ruby switchers, including rbm
• Comparison and evaluation of rbm and other Ruby switchers
• Decision to create a new Ruby switcher with specific requirements
• Issues with rbm's implementation and syntax
• Ruby switchers and custom gem directories
• RVM limitations and annoyances (patch-level specific gem directories, etc.)
• Designing a new ruby switcher (ChRuby) to address RVM's issues
• Comparison to RVM and other ruby environment managers (rbm, etc.)
• Plans for ChRuby's future development and features
• Discussion of rvm2's scope and goals (integrating with package managers, etc.)
• Sponsor announcement for Code Chip, a hosted continuous deployment service
• Discussion of Ruby Build and its use for installing Rubies
• Creation and design of Chruby, a tool for switching between Rubies
• Critique of Ruby Build's design and behavior
• Introduction to Ruby Install and its similarities to Ruby Build
• Comparison of Chruby with other tools like RVM and Ruby Install
• Discussion of package managers and dynamic linking in Ruby
• Design goals and principles of Chruby for multi-system and multi-package manager support
• The project's maintainer discusses the project's longevity and regular releases.
• ChRuby is mentioned as a comparison to other Ruby switchers, with a small codebase (90 lines) and low maintenance needs.
• The maintainer discusses the importance of keeping the project small and simple, aiming for a 100-line core.
• The role of auto-switching and its implementation in a separate file is mentioned.
• The maintainer shares their experience with testing and unit testing shell scripts, and how it helps catch bugs and improve the project.
• The conversation touches on the complexities and edge cases of shell scripting, including implementation differences between shells.
• The importance of using unit tests and pull requests to collaborate and discuss implementation details is emphasized.
• Test and rewrite of the 1819.10-1823.54 test
• Importance of style and safety in shell scripting
• Contributing to open-source projects, including ch ruby
• Maintaining a low profile and avoiding cult of personality
• Giving credits to contributors and acknowledging the role of casual contributors
• Development of a generic make file for shell scripts
• Importance of small fixes and contributions in open-source projects
• The speaker's experience with releasing code and the importance of being meticulous
• Ronin, a project created to make security research easier with Ruby, and its features
• The evolution of the Ruby community and tools, including the transition from Ruby Forge to Ruby Gems
• The challenges of keeping up with rapid changes in the Ruby community and the need to simplify and streamline processes
• Development challenges with Ruby and related tools (e.g. rvm, rbm, bundler)
• Creator's dissatisfaction with current gem set approaches (e.g. rvm, bundler)
• Introduction of ch gems as a gem set replacement tool
• ch gems' approach of explicit project entry and isolation
• Conflicts between ch gems and ch ruby due to differences in initialization and shell management
• Sponsorship by New Relic for application analytics and performance monitoring
• Discussion of chruby and its functionality for managing multiple Ruby versions and gems
• Criticism of chruby and its implementation
• Alternative methods for managing gems and Ruby versions, such as rvm and bundler
• Lack of a definitive guide or write-up on using chruby
• User-written blog posts and experiences with chruby
• Benefits of using chruby, including isolation and environment variables
• Migrating gemset projects to using bundler and sharing gems
• Alternative ways to manage gem dependencies, such as directly editing path and gem home variables
• Discussion of a hypothetical tool to push and pop directories on the gem path and set gem home accordingly
• Confusion and reinvention of gem sets, and the difficulty of solving the problem
• Comparison of bundler's default behavior with other package managers, such as npm and cabal
• Advantages of cabal's package management, including its sandboxing and plain text specification
• Discussion of using gemspec YAML files and hiding metadata from the gemspec
• Comparison of dependency tracking systems between bundler, cabal, and npm
• Use of npm's --save flag to install packages locally
• The speaker has been learning JavaScript and has experience with both Ruby and JavaScript development.
• The speaker notes that Ruby development is often unnecessarily complex due to the use of package managers and configuration management tools.
• The speaker suggests that in many cases, a single package manager (e.g. apt-get) is sufficient and can provide many benefits, including automatic updates and security patches.
• The speaker criticizes the use of Ruby switchers (e.g. rvm) in production environments, citing added complexity and security risks.
• The speaker proposes a "call to arms" for the open source community to rethink the use of complex package managers and configuration management tools in favor of simpler, more straightforward solutions.
• The speaker would like to write a blog post or create an open source project to promote this idea.
• The speaker mentions several potential open source projects they would like to contribute to or hack on, including security exploitation tools.
• The importance of refactoring and cleaning up technical debt in codebases
• Padrino, a framework built on top of Sinatra, and its potential for more contributors and improvement
• Ruby Object Mapper (ROM) project, its features, and the need for more contributors to simplify the code
• Mruby, an embeddable language with a unique build system, and its potential for use in various projects
• Programmer influences, including Dan Cubb, Piotr Solnick, and Marcus Schiemann, and their thought-provoking discussions on design and principles.
• Discussion of getting the guest on the show
• Appreciation for the guest's work in open source
• Encouragement to continue working on open source projects
• Expression of gratitude for being on the show
• Farewell and closing remarks