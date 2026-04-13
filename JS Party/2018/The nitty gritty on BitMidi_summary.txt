• Feross Aboukhadijeh is starting his master's degree in CS, which he put on hold several years ago
• He shares his history of working at Yahoo! and developing the WebTorrent project during a startup experience
• Feross discusses his Patreon experiment to explore open source funding solutions
• He reflects on the limitations of Patreon as a solution for open source sustainability and advocates for a higher goal of profitability rather than mere sustainability
• BitMidi, a project developed by Feross, is mentioned but not discussed in detail
• Patreon sustainability model for open source developers is flawed
• Celebrities in programming culture lead to unrealistic expectations and models
• Feross Aboukhadijeh is returning to college to finish his degree, stating he wanted to have fun and refresh his skills
• BitMidi web app was created to bring back midi files, which were a nostalgic part of early web development
• Browser vendors have locked down the audio element API to prevent auto-play abuse, breaking some websites that relied on this feature
• Discussion of the <bgsound> tag and its non-functionality in modern browsers
• Explanation of why midi playback is not supported in web browsers, due to operating systems removing built-in midi playback infrastructure
• Release strategy for BitMidi, a project that allows users to play midis on the web
• Promotion and self-promotion as important aspects of releasing software or projects, including sharing updates on social media and reaching out to mainstream coverage outlets
• Importance of being intentional about promoting one's work, rather than fearing being seen as self-promotional
• Pitching an idea to tech publications is challenging due to competition and timing.
• Developers should not be shy about promoting their own projects and themselves.
• The Web MIDI API allows for two-way communication between a web page and a MIDI device.
• MIDI files are collections of messages that control instruments, with no sound data included.
• Sound sets or instrument packs are required to play back MIDI files and produce sound.
• Differences in instrument libraries between MIDI file formats
• Using libTiMidity to play back MIDI files on a modern computer
• Compiling libTiMidity to WebAssembly for use on BitMidi.com
• Overcoming limitations of previous JavaScript MIDI players
• Emscripten and WebAssembly compilation process
• Creating a working MIDI player with small file size and fast loading times
• WebAssembly executable for TiMidity music player
• Web Audio API used to play sound in browser
• Emscripten build process exposes C functions to JavaScript
• Pointer translation between C and JavaScript using Emscripten library
• Wrapping up low-level details with a nice JavaScript API
• Porting large codebases to WebAssembly and dealing with file system limitations
• Using fake file systems and dynamic instrument loading in browsers
• BitMidi web app built with Preact, showcasing a high-quality example of Preact application
• Front-end development criticism: complexity, confusion, breakage, and slowness
• Building a minimalist web framework from scratch
• Importance of minimizing JavaScript size for mobile device performance
• Comparison of maximalist vs. minimalist web development approaches
• Challenges in implementing animations and page transitions
• Discussion on server-side database caching and site performance
• Potential for a follow-up video walk-through of the code
• Trade-offs made during development, including using Preact and Express
• Babel build optimization for minimum amount of processing and avoiding polyfills
• Goal of making JavaScript work in latest Edge, Chrome, Firefox, Safari, and mobile browsers
• Use of Lighthouse scores as main metric for measuring success
• Importance of considering parse time and gzip size limitations when optimizing bundle size
• Google's historical data tool for real-world user metrics on website performance
• Comparison of Preact with React, including smaller size and assumed use of DOM
• Discussion of opting out of ecosystem things, such as Preact Router and Redux.
• Discussion of tools for measuring website performance, including Chrome UX Report and Google Page Speed Insights
• Future plans for BitMidi, including implementing continuous playback and improving sound quality with FluidSynth
• Setting thresholds for feature implementation based on user numbers, with a goal of 10,000 monthly active users for certain features
• The importance of prioritizing user needs over personal enjoyment or interest in building a project
• Strategies for promoting a project and gathering feedback, including press outreach and user testing
• Discussion of building features based on personal wants rather than general user needs
• Personal anecdotes from Feross and Jerod about music they want to play continuously in BitMidi
• Importance of sharing unique and weird projects with others
• Encouragement for developers to build cool stuff that benefits themselves and share it with the community