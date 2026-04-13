• Introduction to the Changelog podcast and its hosts
• Michael Papis, maintainer of RVM, joins the show
• Background on Michael's experience with RVM and his transition to its maintainer
• Discussion of Michael's early contributions to RVM and his eventual full-time work on the project
• Mention of the Pledge on RVM's homepage and its role in supporting Michael's work
• Funding of an open-source project through contributions from a community
• Creation of a new format for specifying ruby versions, called "ruby version"
• Discussion of the past drama between RVM (Ruby Version Manager) and RBM (Ruby Build Manager)
• Comparison of different methods for specifying ruby versions, including gem files, ruby version files, and rvmrc files
• Proposal for a new format, called "versions.conf", for specifying multiple settings and dependencies in one file
• RVM (Ruby Version Manager) allows specifying versions for dependencies and plans to introduce support for switching almost everything (e.g. virtualenv for Python, nvm for Node.js)
• RVM 2.0 will merge functionality from multiple tools into one, allowing users to switch environments with a single tool
• Managing the influx of tickets and requests from users is a challenge, and the developer relies on contributions and reviews to help
• The developer has a plan for RVM 2.0 to switch from shell scripting to writing in Ruby, which will simplify code quality and reduce the need for manual reviews
• The project has grown to over 20,000 lines of shell code, making it difficult to manage and ensure code quality
• The developer relies on a few contributors to help with reviews and code quality, but still spends a significant amount of time on these tasks
• rvm installs ruby and switching to a dependency (ruby 1.3) is planned
• proposed solution for getting rvm onto a machine without installing it
• alternative options for installing ruby: binary rubies and jruby
• rvm2 plans: remote execution, installing ruby on a remote machine without local rvm installation
• rvm2 plans: using shell scripting or non-ruby code to download binary ruby and bootstrap other rubies
• discussion about the initial binary ruby and its treatment after installation
• plans for rvm2: managing everything, not just ruby versions, and integrating with chruby
• future plans for rvm2: integrating with other version managers, including python and javascript
• basic requirements for rvm2: getting ruby and javascript binaries available for faster application development
• integration with ruby gems: automating dependency installation and metadata usage
• RVM2 is being developed as a mix of RVM and SM framework, with a potential name change
• The name RVM will not be changed to RVM2, as it is a well-known brand
• The focus is on maintaining compatibility with RVM1
• The release manager for RVM at Engine Yard is being supported by the company to ensure RVM works properly
• Engine Yard needs RVM to function properly for their clients to deploy applications
• The release manager's role at Engine Yard is mostly focused on RVM, with some occasional support questions and a small project to integrate RVM with a client.
• Working on RVM while being full-time employed by Engine Yard
• Feedback from Engine Yard's deploy and support teams on RVM development
• Challenges of balancing work and personal life with RVM's 24/7 support needs
• Integration of RubyGems and Bundler into RVM
• Impact of RVM's stability and functionality on users and the community
• Discussion of RVM (Ruby Version Manager) and its upcoming version 2.0
• Automatic loading of binaries and its relation to pure RubyGems
• Implementation of autolibs in RVM1 due to RubyGems SSL change
• Planned features for RVM2, including integration with RubyGems
• RVM1 feature freeze and the desire for a Christmas release of RVM2
• Call to action for the community to help with issue handling and documentation
• Information on where to find RVM documentation and how to get involved
• Michael Papis's mention of his programming hero, Wayne Seagreen
• Availability: Host is available 16 hours a day, 7 days a week on various channels for ruby and rvm related questions
• Sponsor: App Sketchbook is a sponsor, and listeners can save 5 bucks using a specific code
• Host thanks guests: Michael for joining, Jared for co-hosting, and Andrew for setting up the conversation despite not feeling well
• Upcoming conversation: Update on rvm with Michael