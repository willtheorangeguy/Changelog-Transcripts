• Battlesnake is a competitive programming game where developers build AI snakes to play against each other
• The game has various modes, including challenges and ranked play, with a strong focus on community and e-sports style competition
• Developers use web servers to program the game logic and interact with the game engine through an API
• Games are played in real-time, with a 500 millisecond timeout for responses to determine movement
• Top-tier competitors have optimized their setup by collocating their battlesnakes near the game engine to reduce latency
• The original version of a game had a 5-second timeout, which made it playable but not competitive.
• A robotic snake team cheated by using JavaScript to manipulate the board state, but still lost in competition.
• To prevent such cheating, variable timeouts were implemented, with default and custom options for different game modes.
• The game allows battlesnakes to be in multiple games at once, requiring developers to consider concurrency and response times.
• The introduction of health mechanics added a new layer of strategy, as players must balance growth and survival.
• The randomness of food placement on the board can be used to precompute potential next moves, but requires advanced AI techniques.
• Tofu was a dominant player in Battlesnake games, but their strategy was eventually discovered and exploited by a developer named Smallsco.
• AI and machine learning strategies are being used to compete in Battlesnake games, often targeting specific weaknesses in opponents' code.
• The community is focused on experimentation and exploration rather than pure competition, with many developers using the platform to learn new languages or technologies like TensorFlow or cloud platforms.
• Replit and other tools are providing easy entry points for beginners to get started with coding and building Battlesnakes.
• Large companies like AWS are getting involved in the community, running their own leagues and tournaments.
• Battlesnake is being used as a team-building activity and for showcasing developers' skills.
• Introducing concurrency through challenges
• Pros and cons of using game development for learning web backend development
• Solidifying reasoning and logic skills through gameplay
• Limitations in teaching code structure and team collaboration
• Potential for testing realm with tools such as unit testing and regression testing
• Community-built tools for test-driven development, including a board generator and desktop app
• Natural progression from simple to complex tasks in game development
• Go Starter Project and adding helper functions for distance calculations
• Game engine written in Go and its benefits (performance, concurrency)
• Open sourcing game logic and tools for debugging and understanding the game engine
• CLI tool for running games locally, written in Go
• Unique aspects of the game engine (web-based, web-request based) and why Go was chosen
• Comparison to other languages (e.g. Python) and their limitations
• Advantages of writing the game engine in Go for AI development and performance
• Plans to cross-compile the game engine to WebAssembly
• Fuzzing and early strategy approaches for AI development
• AIs in Battlesnake can recognize and adapt to their opponents' playing styles
• Tiered competition allows for gradual progression from Bronze to Elite, making the game more accessible
• Lower-tier players often employ stateless strategies focused on survival, while higher-tier players use look-ahead algorithms
• Even top-tier AIs can make "silly" mistakes that don't affect their overall performance
• An AI accidentally developed a strategy that actively avoided food and won games repeatedly
• Preconceived notions of good play vs actual game dynamics
• AI capabilities and limitations in games like Starcraft and Dota
• Accessibility of complex AI interactions through simplified games like Snake
• Non-programmer audience for AI-driven gameplay events and experiences
• Educational games that introduce programming concepts, such as Seven Billion Humans and Screeps
• Programmer interests in metrics like code length, speed, and latency
• Non-negotiable job offers
• Early-stage tech hiring
• Hiring bias and favoritism towards those who negotiate salary
• Unequal treatment of job candidates based on background, experience, or negotiation skills
• Benefits of non-negotiable job offers for building trust and fairness in the hiring process
• Challenges and limitations of implementing non-negotiable job offers, particularly in large organizations
• Salary transparency and non-negotiable salaries
• Concerns about companies using salary transparency as a way to underpay employees
• The importance of being upfront and honest about compensation expectations
• Using non-negotiable salaries to potentially take advantage of less confident candidates
• The role of experience and familiarity with a company's products or tools in the hiring process
• The benefits of open-source communities and collaboration for hiring and development opportunities
• Strategies for individual developers to increase their chances of getting hired, including using a company's developer-facing tools and researching the company before applying
• Battlesnake, a game where players control snakes, is discussed
• Brad Van Vugt joins to talk about the game and its upcoming summer competitive league
• Pre-registration for the league opened yesterday, with competitive play starting in June
• The website to check out the game is play.battlesnake.com