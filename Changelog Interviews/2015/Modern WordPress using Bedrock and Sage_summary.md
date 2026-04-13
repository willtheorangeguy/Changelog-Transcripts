• The hosts discuss WordPress and its capabilities
• The guests, Ben Word and Scott Walkenshaw, are from Roots, the organization that created Bedrock and Sage
• Roots is a modern WordPress stack that aims to simplify WordPress development
• The hosts and guests discuss their love for WordPress, despite some criticism from others
• The guests introduce themselves and their involvement with Roots, including Ben's role as the creator and lead developer
• The origins of Roots and its evolution over the years, including the development of Bedrock and Sage
• The hosts and guests share a personal anecdote about how they met, through their shared passion for Call of Duty gaming
• The guests discuss their early experiences with WordPress, starting from around 2003-2004
• Discussion of the evolution of Roots, a WordPress theme, into Sage
• Sage's transformation from a bloated tool to a lean and minimalistic theme
• The renaming of Roots to Sage, and the confusion that followed
• Sage's features and functionality, including its use of a theme wrapper and gulp
• Bedrock, a WordPress stack that provides better structure and organization
• Bedrock's history and purpose, including its spin-off from Roots and its borrowed concept from WordPress core team members
• Bedrock gives a better folder structure and uses Composer for dependencies
• Bedrock's folder structure keeps WordPress's default folder structure, which is difficult to manage for large projects
• Bedrock has a top-level "web" folder, a "config" folder, and a "vendor" folder for Composer dependencies
• Composer dependencies include WordPress core and plugins, as well as PHP packages like Mustache
• Bedrock's design is geared towards large, long-running projects with multiple team members, not small personal blogs or quick sites
• Embedding the Whole Mustache library in a theme and committing it to the source code repository
• Using Composer to handle dependencies and manage library versions
• Organizing a WordPress site's structure using a Bedrock-style folder structure
• Creating a standard WordPress folder structure, but with some modifications (e.g. renaming "wp-content" to "app")
• Dealing with WordPress' hardcoded expectations and constants for folder locations
• Ensuring compatibility with plugins and themes, and updating them to use WordPress' built-in functions instead of hard-coded paths
• Coordinating with plugin and theme authors to update their code and follow the Bedrock structure.
• Authors of WordPress plugins may be unaware of best practices for loading plugins, leading to issues.
• Bedrock is designed for advanced WordPress developers, particularly those who use composer for dependency management.
• Bedrock is not suitable for beginners or those who do not use composer, as it can be difficult to set up on shared hosting.
• The deployment process in Bedrock involves running composer install to get the latest dependencies and packages.
• Bedrock is designed for teams and professionals, rather than individual freelancers or bloggers.
• The tool provides a more structured and professional approach to WordPress development, with features like dependency management.
• Methods for deploying WordPress sites, including Ansible and Capistrano
• Bedrock project structure and its benefits
• Top Tile network and its approach to freelancing and collaboration
• Deployments, including the use of Composer, rsync, and FTP
• Differences in deployment approaches for various levels of WordPress developers
• Personal experiences with WordPress deployment, including use of gulp and rake tasks
• Discussion of finding a better way to deploy WordPress sites for individuals and small teams
• Bedrock and its deployment workflow
• History of deployment in Bedrock (Capistrano)
• Capistrano and its configuration in Bedrock
• Ansible and its integration with Bedrock
• Vagrant and its use with Bedrock
• Creating development virtual machines with Vagrant and Ansible
• Automated deployment with Ansible playbooks
• Promoting parity between development, staging, and production environments
• Reducing complexity and mismatch between local and production environments
• Best practices from other communities, such as Ruby on Rails and DevOps
• Using Ansible for configuration and automation
• VVV (vagrant, vhost, vhost root) project and its similarities to Bedrock
• Importance of having a consistent and controllable local environment
• Introduction to Sage and the Roots organization's projects and initiatives
• Discussion of integrating Bedrock and Ansible projects for easy development VM creation
• Plans to add automation for creating Digital Ocean droplets
• Launch of a new example project on GitHub to demonstrate integration of Bedrock, Ansible, and Sage
• Collaboration with Digital Ocean on automated deployment
• Encouragement for WordPress developers to use Bedrock for its benefits
• Introduction of Sage, a theme based on HTML5, Bootstrap, and Gulp, and its workflow
• Explanation of Sage's Gulp file and its features, including browser sync and third-party asset management
• Sage is a WordPress theme framework that uses a base wrapper file (base.php) to centralize common markup and include individual template files.
• The wrapper encourages separation of application logic from templates and reduces code duplication.
• Sage is not for everyone, and the developers recommend it for client work, personal projects, or building applications, but not for widespread theme distribution or sale.
• The wrapper changes the way template files are structured, but does not alter the WordPress template hierarchy.
• Sage was designed to help developers learn new tools and best practices, but its implementation is not suitable for all types of themes, including those submitted to the WordPress theme repository.
• Sage is a WordPress theme targeted towards developers who understand CSS and JS
• Sage is not for beginners and is best suited for teams or individuals who want to modernize and manage their WordPress site efficiently
• The Roots organization is working on improving the WordPress ecosystem with tools like Bedrock and Sage
• The Roots team is contributing to WordPress and trying to make it more efficient and streamlined for developers
• The organization is taking a pragmatic approach, recognizing that WordPress is a widely used platform and trying to improve upon it rather than creating an alternative
• The team is working on making WordPress more efficient and easier to manage, particularly for teams and large organizations
• Contributing to WordPress is seen as broken and the team is trying to improve upon it
• The ultimate goal is to make WordPress a more pleasant and efficient platform for developers to work with.
• WordPress powers 23% of the web
• Difficulty in contributing to WordPress core due to outdated processes
• Current source control system is Subversion, whereas most projects use GitHub
• Contribution process is complex and involves generating patch files
• WordPress has a large number of open issues on its Track project, with some issues remaining unresolved for 4-7 years
• The community is discussing moving WordPress to GitHub for a more modern and accessible contribution process
• WordPress hosting its own GitLab-like platform
• Ease of contribution and issue management for WordPress
• Move to a pull request-based workflow for WordPress
• Challenging aspects of contributing to WordPress
• Root and Sage (Bedrock) initiatives and call to action for community involvement
• Bedrock Ansible project development and feedback requests
• Digital Ocean sponsorship and upcoming episode with Sarah Allen