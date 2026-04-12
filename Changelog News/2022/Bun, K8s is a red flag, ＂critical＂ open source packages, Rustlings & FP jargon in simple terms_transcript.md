[0.00 --> 12.18]  Hello friends, I'm Jared, and this is Changelog News for the week of Monday, July 11th, 2022.
[12.78 --> 17.74]  Just one note before we get started, I was pleasantly surprised to hear that y'all enjoy
[17.74 --> 22.22]  the little pop culture soundbites I've been sprinkling in, but it can be frustrating when
[22.22 --> 28.34]  you miss a reference. So, from now on, I'll name and link to each soundbite's source material in
[28.34 --> 37.10]  the transcript. Okay, now to the news. Probably the biggest piece of software to drop into our laps
[37.10 --> 42.32]  of late is Jared Sumner's fast, all-in-one JavaScript runtime, Bun.
[45.56 --> 51.18]  You can do side bends or sit-ups, but please don't lose that native bundler, transpiler,
[51.18 --> 57.98]  task runner, and built-in NPM client. Bun is here to compete with Node and Dino and is designed to be
[57.98 --> 64.96]  a drop-in replacement for your current JS and TS apps. The goal of Bun is to run most of the world's
[64.96 --> 70.28]  JavaScript outside of browsers, which is ambitious to say the least, but it has early testers and
[70.28 --> 76.30]  users confessing to its impressive speed. Focus. Speed. I am speed.
[77.12 --> 78.68]  Jeremy Brown writes,
[78.68 --> 85.80]  Kubernetes is a red flag that signals premature optimization, which is kind of weird because he's
[85.80 --> 91.72]  spent much of his life advocating for and selling a distribution of Kubernetes and consulting services
[91.72 --> 98.68]  around it. Now, he didn't write this post merely to pick on Kates. Do people say Kates? K-8-S.
[99.18 --> 103.40]  Kubernetes. He's not picking just on Kubernetes. He says he's, quote,
[103.40 --> 109.58]  directing this post at every possible bit of premature optimization engineers make in the
[109.58 --> 114.32]  course of building software, end quote. The overwhelming sentiment can be summed up in these
[114.32 --> 120.34]  two points. One, your organization needs engineers to create an impact on the mission, and two,
[120.60 --> 127.90]  try to do more with less. Over the weekend, Armin Ronicher blogged a blog called Congratulations,
[127.90 --> 133.76]  we now have opinions on your open source contributions. But I think he's being sarcastic
[133.76 --> 137.28]  about that congratulations bit. He's not too excited about this.
[137.40 --> 140.98]  You keep using that word. I don't think it means what you think it means.
[141.14 --> 145.66]  This post is in response to a change made in Python's PyPy package manager.
[146.06 --> 152.22]  They are beginning to require two-factor auth for, quote, critical packages. About this and his
[152.22 --> 158.32]  newly deemed critical package, Armin says, quote, once packages are within a certain level of
[158.32 --> 163.88]  adoption compared to the global downloads, they are considered critical. Currently, if you maintain
[163.88 --> 169.82]  a critical package, you need to enroll a multi-factor authenticator. It appears that the hypothetical
[169.82 --> 176.42]  consequence of not enrolling into 2FA is not being able to release new versions. My visceral reaction
[176.42 --> 182.00]  to this email was not positive, end quote. I think we can all agree that increasing supply chain
[182.00 --> 186.92]  security is a noble goal for every package ecosystem. And on paper, it makes sense for
[186.92 --> 191.82]  this requirement to not affect every package maintainer, at least not at first. But I can
[191.82 --> 196.82]  still see how it rubs people the wrong way. Again, Armin says, quote, when I create an open source
[196.82 --> 201.94]  project, I do not choose to create a critical package. It becomes that by adoption over time.
[202.26 --> 207.48]  Right now, the consequence of being a critical package is quite mild. You only need to enable 2FA.
[207.48 --> 213.44]  But a line has been drawn now, and I'm not sure why it wouldn't be in the index's best interest to put
[213.44 --> 220.00]  further restrictions in place, end quote. We can file this one under open source. It's complicated.
[220.64 --> 228.98]  Next up, Rustlings. Small exercises to get you used to reading and writing Rust code. This repo that's
[228.98 --> 234.68]  maintained by the Rust team has made changelog news in the past, but Daniel Thompson of Towery, yes, that's how you
[234.68 --> 240.42]  pronounce it. Towery. Recommended it on the changelog, so we linked it up again. Here's a clip of Daniel
[240.42 --> 243.32]  telling us how Towery is like a gateway to Rust.
[243.50 --> 249.96]  Because you don't need to write Rust from the beginning, it lowers the barrier to entry because
[249.96 --> 256.44]  you can say you have now built a Rust-based application. And just being able to say this is
[256.44 --> 262.10]  kind of one of those visualization techniques of getting better at things, is understanding that,
[262.10 --> 269.36]  yes, you are capable of doing it. And the fact is, people get interested by it. Like, over the three
[269.36 --> 276.82]  years we've been working on this project, a couple people have very visibly improved in their Rust.
[277.04 --> 282.24]  At the beginning, they're like, this is hard. Everything is hard if you've never done it before.
[282.24 --> 289.24]  And having Towery as a gateway to understanding, well, okay, I need a compiler. Why do I need a
[289.24 --> 294.98]  compiler? Well, having a compiler is good because it makes my app small. Great. So you get that out
[294.98 --> 301.18]  of the way. And then you discover that, oh, maybe there's this special custom feature that you want
[301.18 --> 305.64]  to make. And you follow the instructions and you write a couple lines of Rust. And the compiler's like,
[305.68 --> 309.06]  oh, you did it wrong. And you're like, oh, okay, what did I do? Oh, that's what I did wrong. And
[309.06 --> 312.06]  you figure it out. And suddenly you've written a couple lines of Rust.
[312.74 --> 318.26]  Last one for today, jargon from the functional programming world in simple terms.
[318.72 --> 324.30]  FP provides many advantages. And I can say that in my career, as I learned and applied functional
[324.30 --> 330.36]  principles to my code, even in OOP languages like Ruby and JavaScript, my software became easier to
[330.36 --> 336.94]  reason about, less error prone, and more maintainable. Unfortunately, all that FP jargon can be a real
[336.94 --> 341.74]  sticking point. It can make you feel like a baby boomer trying to communicate with Gen Z.
[342.14 --> 346.18]  Hey, you trying to flex on me, Kerr? Pull up in a suit? I'm not trying to buy car insurance, bruh.
[346.32 --> 348.46]  Okay, laugh and say, I'm dead.
[349.60 --> 349.94]  What?
[350.00 --> 351.02]  It's Gen Z, remember?
[351.24 --> 352.82]  Ha! I'm dead.
[353.18 --> 360.12]  If arity, currying, idempotent, monoid, monad, or applicable functors have you cappin',
[360.12 --> 361.40]  say you cappin'.
[361.40 --> 362.56]  You cappin'.
[362.56 --> 367.24]  Check out this glossary, which includes definitions and example code.
[367.92 --> 372.96]  That is the news for now. We'll be back in your ears on Friday with that Towery episode.
[373.36 --> 377.62]  It's a deep one clocking in at almost an hour and 40 before mastering.
[377.98 --> 379.88]  Stay tuned for that. We'll talk to you then.
[379.88 --> 386.36]  Game on!
