[0.00 --> 14.68]  What up nerds? I'm Jared and this is Changelog News for the week of Monday, May 19th, 2025.
[15.68 --> 21.44]  I may sound a little different than usual because I'm in a hotel in Seattle and I'm shipping this
[21.44 --> 26.78]  out a little later than usual because Adam and I spent the morning attending the Microsoft
[26.78 --> 35.40]  Build 2025 keynote where Satya Nadella and company mentioned AI agents 187 times. Yes, I counted.
[35.82 --> 42.62]  That excludes mentions of Copilot, MCP, or Models, which would have ballooned the count even more
[42.62 --> 49.40]  because I'm only a man, not a machine. The good news, there was at least one cool non-agentic
[49.40 --> 55.94]  announcement. Okay, let's get into the news. Windows subsystem for Linux is open source.
[55.94 --> 62.64]  The announcement that WSL is now finally open source garnered perhaps the biggest applause break
[62.64 --> 68.76]  of the entire build keynote. Turns out opening the source of a beloved developer tool slash platform
[68.76 --> 75.30]  at a developer conference is an easy win. From the announcement post, quote, WSL could never have been
[75.30 --> 81.86]  what it is today without its community. Even without access to WSL's source code, people have been able
[81.86 --> 88.48]  to make major contributions that led to what WSL is now. This is why we are incredibly excited to
[88.48 --> 94.56]  open source WSL today. We've seen how much the community has contributed to WSL without access
[94.56 --> 101.00]  to the source code, and we can't wait to see how WSL will evolve now that the community can make direct
[101.00 --> 107.50]  code contributions to the project. End quote. Windows subsystem for Linux is one of the coolest things
[107.50 --> 112.20]  Microsoft has built this decade, and having it out there in the open makes it even cooler.
[113.20 --> 119.58]  Hypertyping. Paolo Scanferla describes an inherent tradeoff in TypeScript's type system.
[120.02 --> 126.40]  Stricter types are safer, but often more complex. He calls this phenomenon hypertyping, which is,
[126.40 --> 132.72]  quote, where libraries, in pursuit of perfect type safety, end up with overly complex types that are
[132.72 --> 138.84]  hard to understand, produce cryptic errors, and paradoxically even lead to unsafe workarounds.
[139.22 --> 145.10]  End quote. Paolo argues that simpler types, or even type generation, often lead to a more practical
[145.10 --> 151.20]  and enjoyable developer experience, despite being less perfect. Turns out, perfect really is the enemy
[151.20 --> 158.50]  of good, even in TypeScript. I'm going back to using my brain. Alberto Fortin is taking a step back from
[158.50 --> 166.28]  heavy LLM use while coding. Why? Quote, one morning, I decided to actually inspect closely what's all this
[166.28 --> 170.92]  code that Cursor has been writing. It's not like I was blindly prompting without looking at the end
[170.92 --> 176.92]  result, but I was optimizing for speed, and I hadn't actually sat down just to review the code. I was just
[176.92 --> 184.04]  building, building, building. So, I do a coding review session, and the horror ensues. End quote. I won't list
[184.04 --> 189.72]  all the horrors here. You can probably guess what they are. Here's Alberto's experience after stepping
[189.72 --> 195.60]  back. Quote, since I've taken a step back, debugging has become easier. Maybe I'm not as fast, but I
[195.60 --> 200.48]  don't have this weird feeling of, I kind of wrote this code, but I actually have no idea what's in it.
[200.76 --> 207.46]  I'm still using LLMs, but for dumber things, like rename all occurrences of this parameter, or here's
[207.46 --> 214.44]  some pseudocode. Give me the Go equivalent. It's now time for sponsored news. Everything you need to
[214.44 --> 220.80]  know about Vibe Coding. Vibe Coding, love it or hate it, is here to stay. Everyone has an opinion
[220.80 --> 227.12]  about it, and Retool's Kenan Coppenhaver does a good job explaining the trend's potential and risks
[227.12 --> 232.86]  with developers in mind. Quote, where Vibe Coding enables non-engineers to create without learning to
[232.86 --> 238.92]  code. Experienced engineers are freed up to focus on advanced problem solving and relieved of
[238.92 --> 244.40]  undifferentiated heavy lifting, such as changing the entire app's color scheme, rebuilding a data
[244.40 --> 250.64]  table for the 100th time, or implementing a known algorithm in a new language. Think of the flow state
[250.64 --> 256.26]  you could achieve or the creativity you could harness if you could just remove these kinds of tasks from
[256.26 --> 262.84]  your project. End quote. The reality, as we both know, isn't so straightforward. Kenan goes on to
[262.84 --> 267.74]  lay out the security concerns, the team-wide inconsistencies, and the tech debt that Vibe
[267.74 --> 272.96]  Coding can produce. Thanks to Kenan for the great write-up, and to Retool for sponsoring Changelog
[272.96 --> 280.60]  News. Check them out at retool.com. Coding without a laptop. Did you know you can run a full desktop
[280.60 --> 286.06]  Linux environment on your phone? Not some clunky virtual machine and not an outright OS replacement
[286.06 --> 292.46]  like Ubuntu Touch or Postmarket OS. Just native ARM64 binaries running inside a little cheroot
[292.46 --> 299.80]  container on Android. Pretty cool. The pseudonymous hacker who blogs at holdtherobot.com had a two-week
[299.80 --> 304.30]  trip coming up where they needed to work, and they got obsessed with the idea of leaving their laptop
[304.30 --> 310.56]  at home and just using their phone. So, they added a folding keyboard and some AR glasses. The whole
[310.56 --> 316.96]  setup cost $636. And here's four reasons why they still like the idea after trying it on for a bit.
[316.96 --> 323.00]  One, it really does fit into your pockets. No bag, nothing to carry. Two, I can use it outdoors in
[323.00 --> 328.62]  bright sunlight. I wrote most of this blog post sitting at a picnic table in a park. Screen glare
[328.62 --> 335.46]  and brightness is not an issue. Three, I can fit into tight spaces. This setup was infinitely more
[335.46 --> 341.02]  comfortable than a laptop when on a plane. Some coffee shops also have narrow bars that are too small
[341.02 --> 347.86]  for a laptop, but not for this. And four, the phone has a cellular connection, so I'm not tied to Wi-Fi.
[348.26 --> 352.78]  That said, there are plenty of pain points too. Check the link in the newsletter for the full story.
[353.32 --> 360.18]  Microsoft wants this to be the HTML of the agentic web. The most interesting segment of today's build
[360.18 --> 366.60]  keynote in my eyes was when CTO Kevin Scott took the stage to discuss the open agentic web and
[366.60 --> 372.18]  Microsoft's commitment to it. He emphasized the importance of protocols and Microsoft's support
[372.18 --> 380.98]  of MCP. Then he compared MCP to HTTP and said, we need an HTML equivalent to sit on top. That's when
[380.98 --> 388.10]  he introduced NLWeb as Microsoft's attempt at defining the HTML of the agentic web. Quote,
[388.36 --> 395.72]  NLWeb is a collection of open protocols and associated open source tools. Its main focus is establishing
[395.72 --> 402.38]  a foundational layer for the AI web, much like HTML revolutionized document sharing. To make this
[402.38 --> 408.90]  vision reality, NLWeb provides practical implementation code, not as the definitive solution,
[409.26 --> 416.20]  but as proof of concept demonstrations showing one possible approach. End quote. This is early days and
[416.20 --> 422.32]  things are moving fast. Sounds like a great time to get involved. That's the news for now, but go and
[422.32 --> 428.68]  subscribe to the ChangeLog newsletter for the full scoop of links worth clicking on, such as a leap year
[428.68 --> 437.24]  check in three instructions, cat slash Etsy slash iter.conf, and an online museum of internet artifacts.
[437.70 --> 445.76]  Get in on the newsletter at changelog.com slash news. Have yourself a great week. Like, subscribe,
[445.76 --> 451.46]  and leave us a five-star review if you dig the show, and I'll talk to you again real soon.
