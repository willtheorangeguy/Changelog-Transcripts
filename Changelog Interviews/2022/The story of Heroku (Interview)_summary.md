• The hosts of the podcast, Jerod Santo and Adam Stacoviak, introduce Adam Wiggins and explain that they'll be discussing his work on Heroku and its history, as well as his current project, Muse.
• Adam Wiggins explains that he's made a rule for himself not to talk about his past work on Heroku, but feels that this conversation will be special and provide a new context for discussing his experiences.
• The hosts explain that they're interested in discussing Heroku's history and how it affected the industry, and Adam Wiggins shares that he's hesitant to revisit the past because it can feel stale and he doesn't feel like he has anything new to say.
• Adam Wiggins and the hosts discuss the early days of Heroku, including its relaunch in 2007-2008, and how it changed from an in-browser editor to a platform for deploying and managing applications.
• Adam Wiggins shares the story of how he and his co-founders, James Lindenbaum and Orion Henry, started Heroku, and how they were driven by a desire to make the development process more joyful and productive for themselves and their clients.
• Development of a Ruby debugger for the browser
• Idea to create a Ruby debugger in the browser, influenced by the author's experience in the video game industry
• Prototype of a debugger with multiple panes for code, stack trace, console, and application output
• Meeting the Ruby community at RailsConf 2007 and the opportunity to create a product for the community
• Decision to pivot and create a web editor, influenced by the concept of end-user programming
• Creation of an all-in-one runtime environment, including code editor, database, and deployment
• Realization that the original vision was too ambitious and the focus shifted to instant deployment and the web editor
• Discussion of the challenges of deploying Ruby applications in 2006-2007 and the idea of making deployment easier
• The speaker recalls the early days of Rails hosting and how they envisioned a more straightforward and easy deployment process.
• The current state of Rails hosting is still complex and requires manual configuration, despite advances in technology.
• The era of hosting in the early 2000s featured various players, including Engine Yard, Rackspace, and Slicehost.
• Adam Wiggins discusses the influence of Slicehost and the emergence of virtualization, which laid the groundwork for Heroku.
• The need for managed hosting and support was a significant problem for Ruby on Rails applications at the time.
• The confluence of technologies, including EC2, Git, and GitHub, created a fertile ground for Heroku to emerge and succeed.
• The timing of Heroku's launch was a key factor in its success, as it capitalized on the growing popularity of Ruby on Rails and the need for easier deployment and hosting solutions.
• The importance of making good content and its relation to serendipity in achieving viral success
• The creation of Heroku and its early development, including the pivot from a web editor to a platform
• The role of decentralized revision control, specifically Git, in the development of Heroku
• The serendipitous meeting with GitHub founders and the early adoption of their product
• The significance of the San Francisco Ruby community and its impact on the development of Heroku and other companies
• The lessons learned from participating in Y Combinator, including the feedback received on their initial pitch and the decision to pivot
• Recognizing product-market fit and understanding that users were enthusiastic but didn't stick with the product
• Raising a series A round of funding and the challenges that came with it, such as focusing on expansion rather than changing the product
• Identifying that the user base was split between citizen developers and more serious developers who were willing to pay
• Deciding to pivot the product to focus on the more serious developers
• The process of launching the new product and its positive reception
• Discussing the source code and infrastructure behind the original product, including the editor and deployment system
• The innovation and tech that went into creating the developer experience on Heroku, including routing mesh and using Erlang and Go
• The challenge of hooking into the operating system and understanding application developers' needs
• Composability and system-level technologies used in Heroku's infrastructure
• Use of Unix tools for process management and proxy configuration
• Dynamic routing mesh and rewriting of httpd.conf for Apache
• Development of a C module for NGINX for dynamic routing
• Writing of a custom load balancer
• Dynos (precursor to containers) and load balancing layer
• Heroku's style and branding, including Japanese influence and poetic app names
• The name "Heroku" was inspired by a combination of "heroic" and "haiku", reflecting the company's goal of creating a tool to help developers be heroic and make a significant impact.
• The name was influenced by Ruby's Japanese origins and the company's desire to bring a sense of elegance and beauty to the product.
• Adam Wiggins explains the meaning of the name and how it was developed, including the involvement of Yukihiro Matsumoto, the creator of Ruby.
• The company's style and perspective were key factors in its success, with a focus on creating a polished and intentional product.
• The sale of Heroku to Salesforce was announced in December 2010, and was a significant event in the company's history.
• The acquisition was a result of the company's success in the cloud space, as well as its sticky product and expanding user base.
• Adam Wiggins credits his colleagues James Lindenbaum and Byron Sebastian for their role in negotiating the deal, while he was focused on product development.
• Cloud companies and developer tools
• Acquisitions by Amazon, VMware, and Salesforce
• VMware deal and its potential implications for the company
• Series B funding and change in direction
• Regrets about selling Heroku to Salesforce
• The speaker's art-like approach to building companies and their desire to have a complete vision before moving on
• The decision to sell Heroku to Salesforce in 2010 and the initial concerns about it disrupting the company's vision and mission
• The positive effects of the acquisition on the company in the short term, including increased innovation and access to new markets
• The speaker's reflection on the acquisition's impact 10 years later, noting that while Heroku may not be as innovative as it once was, it is still a reliable and effective platform
• The discussion of the timing of the acquisition and whether it was premature, with the speaker noting that it was a high-risk decision that could have disrupted the company's vision and mission
• The speaker's personal perspective on the acquisition, noting that it allowed them to achieve their goals and move on to other projects, and that they are still proud of what Heroku has become
• The consideration of what could have happened if the company had delayed the acquisition by three to five years, potentially leading to a larger financial outcome but also increased risk and uncertainty
• Calculated risks and decision-making in startups and venture capital
• Salesforce acquisition of Heroku, and the pros and cons of the deal
• The emotional and existential challenges of considering an acquisition offer
• The impact of the acquisition on the company and its culture
• Reflections on the past and the current state of the platform, including recent changes and developments
• The importance of innovation and staying true to one's vision in the tech industry
• Heroku's decision to discontinue free dynos, upsetting long-time users who feel it goes against the platform's original vision of frictionless startup
• Adam Wiggins' emotional reaction to the change, recalling the importance of free dynos in allowing users to quickly prototype and test ideas
• Discussion of the challenges of managing free, open-ended runtimes, including abuse and spam issues
• Adam Wiggins' explanation that the decision was driven by the business need to manage resources and mitigate the impact of badly-behaved apps
• The idea that free compute resources can be abused and lead to problems for both users and the platform's management team
• Comparison to other platforms, such as GitHub Actions, suffering from similar issues
• Reflection on Heroku's original assumption that compute infrastructure would become cheaper over time, making it less valuable
• Discussion of the trade-offs between abstracting away infrastructure and worrying about compute costs, and the impact on user mindset and development approach
• Adam Wiggins' disconnection from modern development trends and tools
• Discussion of alternative platforms and services to Heroku
• Adam's current work in productivity software and product design
• His experience with Apple platforms and Swift
• Mention of Vercel, Fly, Render, and Netlify as successors to Heroku
• Adam's investment in and admiration for Netlify
• Discussion of his current business, Muse, and his transition to a different industry
• Adam's background at Heroku and his eventual exit
• His time off and decision to live in Germany
• His experience working at Salesforce and his eventual resignation
• His desire to "refill the creative well" and pursue a different path
• His decision to live abroad and work with startups in Berlin
• Adam Wiggins' decision to stay in Berlin after leaving Heroku was a result of his freedom to explore and the city's unique character
• He enjoyed working with various companies in Berlin and fell in love with the city's vibe, creative energy, and quality of life
• Remote work became a viable option, and Adam's research lab, Ink & Switch, started as an all-remote team in 2015
• The conversation will be continued in part two, discussing Adam's work with Muse, his podcast, product design, and team building