• Introduction to the Changelog episode 0.6.9
• Discussion of Spree, a Ruby on Rails e-commerce platform, and its recent funding
• SpreeConf conference announcement for February 15th-16th in New York City
• Interview with Sean Schofield and Brian Quinn from the Spree Project
• Background on the Spree Project and its evolution
• Discussion of the move to Rails 3.1 and the asset pipeline
• Challenges and benefits of the asset pipeline in Spree
• Latest release of Spree (0.70.1) and its compliance with Rails 3.1.1
• Development performance penalty with combined assets
• Pre-compilation of assets as a solution
• Spree as a Rails engine and its customization capabilities
• Decorators as an additional layer for development
• Extensions and third-party plugins available for Spree
• Engines in Rails and their benefits
• Devise and other plugins used in Spree's architecture
• Consolidation of dependencies and migration to newer gems
• Simplifying Spree's architecture for easier migrations
• Spree Commerce's extension and integration with other libraries and frameworks
• Use of Active Merchant and Plugin a Week State Machine in Spree
• Customizability of Spree models
• Integration of Spree with other applications, including existing Rails applications
• Potential for Spree to be integrated with other e-commerce platforms, such as Refinery and Radiant
• Formation of Spree Commerce, the company behind Spree
• Funding of $1.5 million seed round led by True Ventures
• Public goods and documentation for open-source projects
• Upcoming SpreeConf conference in New York City (February 15-16)
• Conference content: training, talks, hackathon, and networking
• Speakers and attendees: Wyn, Bree Pettis (CEO of MakerBot), Scotch O'Con, and other notable Ruby community members
• Sticker Mule's success with Spree Commerce and their attendance at the conference
• Largest installation of Spree: Shoe Dazzle (rumored to be $100 million in sales)
• Kim Kardashian's Shoe Dazzle uses a customized version of Spree
• Second Life uses a highly customized version of Spree with a well-preserved data model
• Spree is suitable for both small and large businesses, with a range of sales from $2,000 to $700,000 per month
• A vibrant ecosystem of extensions and themes is developing around Spree, with 600+ repositories on GitHub
• Official extensions, such as Spree Social and Spree Active Shipping, are maintained and actively supported
• The Rails Dog Radio project is a sample store that uses Spree and its extensions to demonstrate its capabilities
• Theming is a relatively new feature in Spree, introduced in the 0.7.0 release
• The team is actively building out more team extensions (which are equivalent to themes) to expand Spree's capabilities
• Building an open-source version of Rails Dog Radio as a reference implementation of Spree
• Using the project as a way to showcase the capabilities of Spree
• Discussing the challenges of creating the project, including the time and resources required
• Mentioning the need for more themes, better curation of extensions, and updating outdated versions
• Addressing issues with the online store, including refunding fake purchases and providing admin views
• Introducing a new Heroku instance feature to allow users to create their own sandbox
• Discussing the use of real product data and SKUs in the project
• Mentioning plans to make the data set open-source
• Addressing technical flaws and future plans to improve the project
• DeFace is a generic Rails 3 library that solves a problem with Spree's views
• Customizing Spree views can be difficult due to a large number of views and the need for small changes
• DeFace allows targeting of specific elements in views using CSS selectors and substituting code or rendering partials
• DeFace hooks into ActionView and performs parsing and conversion of ERb files to XML for Nokogiri
• DeFace provides upgrade protection and warnings for changes in original HTML
• DeFace is not currently compatible with Haml, but may allow Haml as replacement markup in the future
• The speaker notes that views tend to be project-specific and not well-written, and that DeFace is useful for turning off the view layer in projects.
• DeFace's benefits for e-commerce store management
• Simplification of Spree's front-end views
• Semantic HTML implementation in Spree
• Hiring a community manager for Spree
• Community manager role and responsibilities
• Documentation and naming issues addressed by the new community manager
• Discussion of a software version update from 0.x to 1.0
• Explanation of the delayed version update due to ongoing development and changes
• Comparison of the software to Rails and Spree, and how they've converged
• Mention of past features and innovations being later adopted by Rails
• Discussion of the software's current state and readiness for a 1.0 release
• Introduction to an open-source radar section, where panelists discuss their current open-source projects
• Project similar to Spree is being developed with a large contributor base and active development
• Interest in using Rails Admin and creating a pluggable admin interface
• Barrier to integrating with other CMS platforms is authentication and authorization
• Need for a generic interface to plug in security mechanisms and integrate with various platforms
• Inspiration from Django's out-of-the-box features and desire to build on successful open source projects
• Learning from other open source projects, such as WordPress and Drupal, and their vibrant ecosystems
• Potential for a new open source project to be started to address admin interface needs
• Venture funding and its potential for improving documentation and community curation
• Upcoming conference and expectation for a talk
• Roadmap for Spree and request to keep stakeholders informed