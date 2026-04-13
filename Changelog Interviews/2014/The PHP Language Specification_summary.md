• Discussion of the PHP spec and its importance for the PHP community
• Explanation of the PHP language's organic growth and its current state as a "fractal of bad design"
• Introduction of the PHP spec as a way to formalize the language and provide clear documentation
• Explanation of the need for a clear definition of proper PHP and its syntax
• Discussion of Facebook's HHVM technology and its relation to the PHP spec
• Announcement of the PHP spec's release and its implications for the PHP community
• The speaker mentions a project to improve the PHP language and make it more efficient
• HHVM (Hip-Hop Virtual Machine) is mentioned as a compiler that Facebook is working on to run PHP code
• The PHP code base is massive (10^7 lines of code) and changing to another language is not feasible
• Facebook chose Mercurial over Git for version control due to speed and developer efficiency concerns
• HHVM is a crucial project for Facebook to improve PHP performance and efficiency
• The project was a long-term effort (5 years) to implement a just-in-time virtual machine to run PHP code
• The speaker describes the project as a "crunch time" situation where they had to find a solution to run the site at high speeds.
• The process of transpiling PHP to C++ code led to a significant performance win
• The transpiler had problems, including long compile times and inconsistencies between dev and production environments
• The team switched to a virtual machine (VM) project to address these issues
• The VM project involved a team from Microsoft who worked on the CLR and had experience with just-in-time compilers
• The team chose to write the PHP specification in Markdown due to its native support on GitHub and ease of use
• The original specification was written in MS Word, but the team decided to stick with it until a new format could be implemented
• The PHP community has been receptive to Facebook's efforts to standardize the language through a published spec
• The spec was split from a monolithic Markdown file into chapters, which was initially suggested by the speaker
• The community's concern that Facebook was trying to impose its will on the language was alleviated
• The importance of a spec in a language with multiple implementations, such as PHP, was discussed
• The PHP language has undergone version cycles, with notable skips in version numbers (e.g., 5 to 7, skipping 6)
• The benefits of a spec include ensuring consistency and preventing accidental changes to the language
• The usefulness of a spec is also demonstrated through ongoing language revisions, such as the introduction of uniform variable syntax and abstract syntax trees
• CodeShip, a continuous deployment service, was mentioned as a sponsor
• Code Ship's features and benefits
• Backlash against Facebook's involvement in the PHP community
• Distrust of Facebook's intentions and its impact on PHP
• Licensing and ownership of the PHP specification
• Facebook's choice of the CC0 license for the PHP specification
• Comparison with other open-source licenses, such as GPL
• Discussion of the CC0 license and its implications for the PHP community
• Potential changes to the PHP spec based on feedback from developers
• Introduction of the Hack language and its relationship to PHP
• Comparison of Hack to PHP and its benefits
• Features of the Hack language, including scalar type hinting and parameterized type hinting
• Plans to publish a spec for the Hack language and its potential impact on the PHP community.
• Background on a developer workstation constantly watching for code updates
• Hack is a superset/subset of PHP, developed by Facebook, with 98% of code base converted
• Concerns about serving two masters (PHP and Hack) and maintaining PHP compatibility
• Hack's extra features are development-time focused, not runtime-focused
• Tens of thousands of tests run on every single diff to ensure PHP conformance
• Parallel effort between PHP and Hack, with some seeing it as a competitor, others as a complementary tool
• Hack is not meant to be a complete new language, but rather something that can live alongside PHP
• Discussion of the importance of the PHP specification and its contributors
• Mention of the book "Extending and Embedding PHP" and the author's contributions to the PHP community
• Discussion of PHP's design and its flaws, with the speaker calling it a "fractal of bad design"
• Explanation of the concept of an Abstract Syntax Tree (AST) and its potential to improve PHP's compilation and optimization
• Reference to HHVM and Facebook's approach to making Facebook fast
• Mention of other side conversations, including uniform variable syntax and the PHP internals list
• The speaker works at a non-profit called Pure Charity and used Top Towel to find Ruby and Rails developers
• They used to work on a library called LibSSH2 to enable SSH functionality in PHP
• The speaker enjoyed diving deep into the code and understanding how things work underneath
• They worked on the HHVM project and didn't need to look at low-level code, but would like to understand it
• The speaker has commits that likely won't be used again, but was fun to write
• They used the knowledge to speed up compile time and shortened a file from 100 seconds to 10 seconds
• The speaker doesn't consider anyone a "programming hero" but admires people on their team
• Mark Williams and Jordan DeLong's expertise and contributions to open source projects
• Concerns about the corporate takeover of open source and the loss of community-driven development
• The importance of true open source, as opposed to "corporate source"
• Encouragement to get involved in open source projects despite potential fears or doubts
• The value of documentation and the benefits of contributing to open source projects
• The contrast between corporate-driven and community-driven open source development
• Development of documentation and code tweaks for a project
• The importance of self-taught coding skills and open-source contribution
• The ease of getting involved in open-source projects with platforms like GitHub
• The benefits of open-source collaboration and community involvement
• The role of passion and generous contribution in open-source development
• Upcoming plans for the project and potential future collaborations