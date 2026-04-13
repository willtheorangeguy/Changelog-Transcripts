• Changelog sponsorship and acknowledgments
• Introduction to JS Party podcast
• Guest introduction: Zach Leatherman, web developer at Filament Group and organizer of Nebraska JavaScript Conference
• Discussion topics for the week:
  • Fonts: current state of font loading, easiest ways to improve font loading behavior
  • Upcoming Nebraska JavaScript Conference
• Icon fonts can cause issues with fallback text showing while loading
• Private use area in Unicode can lead to unexpected emoji display
• There is no good font display descriptor value for icon fonts
• Web fonts can cause invisible text and fallback text issues during loading
• Browsers hide text using a web font for up to 3 seconds while it loads
• Fallback text may be displayed if the web font doesn't load within 3 seconds
• Multiple fonts interacting can lead to race conditions and partially visible text
• Web fonts have unique problems not seen with other resources on the web
• The default behavior for text loading in Chromium Edge is changing to three-second invisible text
• The ability to load partial fonts and combine them on the client (incremental transfer) is being standardized and will help with variable font sizes
• Font loading via JavaScript, specifically through the CSS font loading API, offers more control over font loading and reduces jank
• Preloading assets via preload or HTTP2 push can be used in conjunction with other methods to improve performance
• Preloading fonts can improve performance, but excessive preloading can delay first render
• There are different font formats (WAF, TTF, Open Type), with WAF being a container format that adds compression
• WAF 2 offers better compression than its predecessor and is becoming the standard
• Subsetting allows for customized font files to be created by including only necessary characters
• Tools like Glyph Hanger can programmatically subset fonts and create optimized files
• Glyph hanger can reduce font file sizes and improve rendering speed, but has limitations with dynamic content
• Glyph hanger uses puppeteer to spider JavaScript content, but still has some limitations
• The tool can be used in static HTML builds, but may not scale well for large sites or complex applications
• Font loading is discussed as a topic, including tools and techniques for improving performance
• Talks by Zach on font loading are mentioned, including one on improving WordPress theme default web font loading and another on "The Scoville Scale of Font Loading Opinions"
• Tech companies like Twitch, Stripe, and Adobe use Algolia for search functionality
• Interviewer mentions that their own site uses Algolia to power search
• Plug to check out algolia.com or the show notes for more information on using Algolia
• Discussion of Eleventy, a static site generator written in JavaScript
• Eleventy's simplicity and ease of use, making it accessible to those with little coding background
• Planned feature: plugin system to support multiple templating languages
• Eleventy is a command line tool for transforming templates into HTML
• It can utilize any template language that outputs a string
• It can be used with JavaScript templates and has similar functionality to other tools like Jekyll, but without the Ruby dependency
• Eleventy produces static files, such as HTML files, which are ideal for deployment on websites
• It is lightweight and easy to use, making it a good choice for developers who want to avoid complex dependencies
• It allows users to mix and match different templating languages together
• Eleventy can be used with GitHub Pages, but requires a CI approach or the use of GitHub Actions or Netlify
• Eleventy is a static site generator used by web.dev and V8.dev
• It was developed as an alternative to JavaScript frameworks with runtime dependencies
• The creator wanted a tool that outputs only what is put into it, without unnecessary dependencies
• Eleventy occupies the space between traditional static site generators and JavaScript frameworks
• It started as a project to showcase web fonts and web font loading, but has since taken on a life of its own
• The creator is heavily invested in Eleventy and appreciates the open source community's support and contributions
• Maintenance and development are done primarily by the creator with occasional help from others
• Encouraging community feedback and contribution to the project
• Importance of ease of use and intuitive design in project success
• Open Collective sponsorship and comparison with GitHub sponsorships
• Gauge test automation tool promotion
• Panelists' discussion on projects or tools they are excited about (specifically Vue and Svelte)
• The speaker is excited to explore Svelte and its syntax
• The release of Svelte 3 and Richard Harris' "accidental" talk on reactivity are mentioned
• Reactivity in frameworks, making them work like Excel spreadsheets, is discussed as a goal
• Learning Spanish and the challenges of grammar rules being different from English
• The process of learning a language takes one out of their programming mindset and assumptions
• Language learning as an exercise in learning about oneself and dealing with frustration
• The speaker is also learning Spanish alongside their almost three-year-old
• Learning and questioning preconceived notions by being in new situations, such as having children learn from scratch
• Observations on human babies' helplessness compared to other mammals
• The importance of considering a "beginner's mindset" when designing software or tools
• Excitement about various technology developments, including Eleventy and NeoVim 0.4
• Discussion of the speaker's excitement about various topics, including the HBO show Chernobyl and nuclear reactors
• IndieWeb concept and importance of owning one's own content on the web
• Svelte framework and potential crossover with Eleventy
• Serverless and Netlify movements and their impact on independent websites
• The Jamstack and its fascination for the speaker
• Book "Weapons of Math Destruction" and its relevance to algorithms controlling lives
• Discussing the static site generator Eleventy
• Migrating domains for political reasons
• Integration of Dojo with Eleventy
• Dojo static site generators
• Build time rendering in Dojo
• Elixir templates not working on Netlify
• Static site generation with Elixir and Hex dependency system
• Arlang language
• Using only Node-based technologies for projects
• Django as a REST API and templating engine
• Jam stack, amp stack, and Madge (markup-first) approaches to web development
• Discussion of AMP (Accelerated Mobile Pages) framework
• Criticism and "amp hatred" expressed by some individuals
• Overlap between anti-AMP people and JSConf EU attendees
• Clarification that speaking out against the AMP carousel is distinct from being opposed to the AMP framework
• Technical explanation of the AMP framework and its JavaScript implementation
• Concerns about lack of progress addressing user feedback on AMP issues
• Metaphor comparing AMP critics to lobbyists or protesters
• Personal anecdotes about encountering conspiracy theorists in everyday life, including a driver who showed banners against circumcision
• Discussion of engaging with such individuals for entertainment value rather than argumentation
• Concerns about algorithms promoting extreme ideas
• The danger of inadvertently spreading misinformation
• The challenges of discussing sensitive topics online without giving them attention
• Responsibility and caution when speaking or joking about controversial subjects
• Discussion of platform responsibilities and the potential for accidental spokesperson status