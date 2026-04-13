[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.84 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[25.82 --> 28.32]  Thanks to our partners at Fly.io.
[28.70 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.38]  Learn how at Fly.io.
[44.32 --> 48.18]  Welcome to another episode of the Practical AI podcast.
[48.64 --> 50.46]  This is Daniel Whitenack.
[50.46 --> 56.46]  I am CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who
[56.46 --> 59.70]  is a principal AI research engineer at Lockheed Martin.
[60.34 --> 61.04]  How are you doing, Chris?
[61.22 --> 62.08]  Doing very well.
[62.12 --> 63.00]  How's it going today, Daniel?
[63.46 --> 65.34]  It's going great.
[65.50 --> 71.82]  Yeah, it's been a fun, productive week in the AI world over here at Prediction Guard, so
[71.82 --> 72.78]  no complaints.
[73.38 --> 77.64]  But this is a really, I'm excited about this episode because it's one I've been wanting
[77.64 --> 80.50]  to make happen for quite a while.
[81.32 --> 90.72]  Today, we'll be talking about both AI hardware and software with DJ Singh, who is a staff machine
[90.72 --> 92.28]  learning engineer at Grok.
[92.40 --> 93.40]  How are you doing, DJ?
[94.20 --> 94.82]  Hey, Daniel.
[94.92 --> 95.94]  Thanks for having me.
[96.28 --> 97.48]  It's been going well.
[97.68 --> 97.82]  Yeah.
[98.36 --> 98.66]  Yeah.
[98.80 --> 99.20]  Good.
[99.38 --> 99.76]  Good.
[100.18 --> 100.38]  Yeah.
[100.46 --> 106.30]  And I guess we should specify for our audience, this is Grok as in G-R-O-Q.
[106.30 --> 111.94]  I imagine maybe some people get confused these days with that.
[112.10 --> 117.62]  But yeah, this is one that I've been really excited about, DJ, because I've been observing
[117.62 --> 122.42]  what Grok has been doing for some time and, of course, innovating in a lot of different
[122.42 --> 126.38]  ways, like I mentioned on the hardware side and on the software side.
[126.38 --> 133.82]  So could you maybe just set the stage for us a little bit in terms of the overall ecosystem
[133.82 --> 140.48]  as you see it in terms of kind of what may be a bloated term of like AI accelerator or
[140.48 --> 146.02]  hardware and also the software that goes along with that and kind of where Grok fits into
[146.02 --> 147.00]  that ecosystem?
[147.86 --> 147.94]  Right.
[148.32 --> 152.66]  So I think I'll first start and just quickly brief about Grok.
[152.66 --> 157.58]  So Grok is, of course, a company which provides fast AI inference solutions.
[157.98 --> 164.32]  So whether it's text, image, or audio, we are delivering AI responses at blistering speeds
[164.32 --> 168.08]  and order of magnitude more than traditional providers, right?
[168.68 --> 171.00]  Now, you spoke of AI accelerators.
[171.84 --> 177.08]  And traditionally, training and inference has been done on GPUs.
[177.08 --> 184.04]  But I think in the last few years, we've seen all sorts of AI accelerators come in play.
[184.10 --> 190.46]  So there are those more mobile device oriented ones that phone companies like Samsung and
[190.46 --> 192.24]  Apple come up with, right?
[192.50 --> 199.16]  And then there are more stuff happening on the server side, part of which is what Grok is
[199.16 --> 201.50]  also leading towards.
[202.26 --> 202.88]  Yeah, that's great.
[202.88 --> 207.70]  And on the server or hardware side, am I correct?
[207.88 --> 213.40]  Is sort of Grok does have their own sort of hardware that they've developed over time.
[213.62 --> 214.60]  Is that right?
[214.84 --> 217.76]  What's kind of been the progression of that and a current state?
[218.24 --> 218.72]  Absolutely.
[219.02 --> 222.86]  So Grok developed this technology, which we call as Grok LPU.
[222.86 --> 229.84]  It's essentially a software and hardware platform, which comes together to deliver that breakthrough
[229.84 --> 233.22]  performance of low latency and high throughput.
[234.42 --> 239.16]  But how Grok got into it was first to develop that software.
[239.70 --> 245.06]  So we developed the software compiler first before moving on to the hardware side.
[245.60 --> 250.62]  Kind of a shift in how traditional development was being done previously.
[250.62 --> 254.94]  And did that, I mean, that does seem very unique to me.
[255.26 --> 261.60]  So what was the, I guess, the motivation or the thought process behind taking maybe that
[261.60 --> 265.42]  non-standard approach kind of compiler first, then hardware?
[265.90 --> 266.78]  Yeah, no, absolutely.
[267.10 --> 272.82]  So traditionally, as I mentioned, development is done and that a new accelerator is developed.
[272.82 --> 278.30]  So if somebody makes the hardware first and then the software has to deal with the inefficiencies
[278.30 --> 279.56]  of the hardware.
[280.30 --> 287.18]  Whereas when Grok decided, and this company is founded by Jonathan Ross, our CEO, who was
[287.18 --> 293.22]  a co-founder of Google's TPU program, the Tensor Processing Unit program.
[293.94 --> 299.74]  And based on his learnings from there, one of the key decisions was let's develop the software
[299.74 --> 301.20]  software first, right?
[301.20 --> 309.38]  So we have developed the software compiler, which helps to convert these AI models into
[309.38 --> 313.08]  this code which runs on the Grok LPU.
[313.72 --> 321.86]  But specifically, the compiler is responsible for scheduling each and every operation of that
[321.86 --> 322.56]  AI model.
[322.56 --> 328.44]  So you can think of it like an AI model in terms of compute is made up of like additions and
[328.44 --> 329.36]  multiplications.
[330.32 --> 337.40]  And it kind of, the software compiler, it decides where and when to schedule something.
[337.94 --> 343.98]  And that goes into our, you know, various design principles, one of which, of course, I mentioned
[343.98 --> 346.50]  is to be software first, right?
[347.04 --> 351.68]  Now, you might ask, why do we do this, right?
[351.68 --> 361.08]  So one key consideration is that not only does the software have to deal with hardware inefficiencies,
[361.28 --> 361.44]  right?
[361.78 --> 368.40]  But there are other aspects of the hardware which can add on delays, whereas Grok prefers
[368.40 --> 371.54]  to have a deterministic system in place.
[372.16 --> 376.56]  So determinism, I would say, is like deterministic compute and networking.
[376.56 --> 382.22]  So kind of have an understanding of where and when to schedule an operation.
[383.06 --> 386.98]  So to understand this, we can consider an analogy.
[387.94 --> 392.68]  Now, imagine a car driving around along the road with several stop signs.
[393.42 --> 398.46]  Stopping at every sign is essential for safety, but it does add some delays, right?
[398.46 --> 405.44]  Now, what if the world was perfectly scheduled and we knew where to start the car and drive
[405.44 --> 409.70]  at maximum speeds so that there are no collisions, right?
[410.20 --> 414.54]  So there would be no need for these stop signs, no delays as such.
[414.80 --> 419.90]  And it also makes a more efficient use of the road since you can then have more cars and
[419.90 --> 423.60]  everybody's like going at maximum or near maximum speeds.
[423.60 --> 432.26]  So to reflect this analogy and back to the hardware space, Grok chose to remove components which
[432.26 --> 433.42]  can add delays.
[433.94 --> 440.58]  So it could be, let's say, network switches or other even algorithmic delays, some sort of
[440.58 --> 443.50]  algorithms which control packet switching.
[443.76 --> 447.98]  These all things add non-determinism into the system.
[447.98 --> 452.50]  I did want to, maybe some of our listeners out there, like you've been talking about this
[452.50 --> 459.04]  compiler level, which, you know, I think of a compiler similar to what you said as, hey,
[459.06 --> 466.10]  I'm writing some higher level software code that's compiled to these instructions that run
[466.10 --> 473.08]  under the hood on the actual hardware components doing, as you said, additions or whatever those
[473.08 --> 475.44]  sorts of numerical operations are.
[475.44 --> 481.84]  But people might sort of be confused also in terms of the software stack.
[482.00 --> 488.06]  They may be familiar with something like CUDA, which helps, you know, have drivers to run on
[488.06 --> 490.22]  certain hardware like NVIDIA GPUs.
[490.32 --> 496.90]  Or I know, you know, we've worked a little bit with Intel Gaudi processors and there's driver
[496.90 --> 502.24]  package Synapse, which is similar in that sort of way, helps translate kind of your higher
[502.24 --> 506.40]  level code to run on these hardware components.
[506.40 --> 512.42]  Could you help us kind of map out that software stack, like where this compiler fits in?
[512.80 --> 519.08]  And are there other components like these drivers that would have a parallel in the Grok world?
[519.08 --> 519.72]  Yeah.
[519.96 --> 528.76]  So traditionally, as you've mentioned, like on, let's say, NVIDIA ecosystem, there are like tons of engineers
[528.76 --> 537.18]  who go and create these kernels, which are invoked when you have some sort of model operations.
[537.18 --> 544.90]  So there would be maybe even thousands of engineers in the company who would work towards developing
[544.90 --> 548.62]  this very specialized kernels to go and execute things.
[549.34 --> 557.98]  However, due to the structure of the GPU itself architecturally, this is not the best philosophy
[557.98 --> 559.24]  for design.
[559.24 --> 563.24]  You know, I'm sure the audience is familiar with GPUs.
[563.46 --> 567.84]  I remember playing games on them growing up and editing videos.
[568.58 --> 573.22]  And these grew up to be more powerful in the recent decades.
[573.90 --> 580.48]  But, you know, GPUs started in the 90s and the design hasn't changed all that much.
[580.84 --> 587.48]  They've had an addition of high bandwidth memory and other hardware components to it.
[587.48 --> 594.60]  But all of it essentially is still the original design, you know, originating from the original design.
[594.98 --> 598.88]  It does make the system to be, again, less deterministic.
[599.10 --> 602.26]  So that goes back to the compiler system here.
[602.40 --> 606.18]  And let's talk about the NVIDIA GPU kernels here, right?
[606.76 --> 611.86]  So they have to deal with the different hierarchies of memories as an example.
[611.86 --> 619.24]  So for those of the listeners who are familiar with the different memory systems in a computer
[619.24 --> 620.20]  system, right?
[620.26 --> 626.92]  You might be familiar with like an L1 cache, which has like an access time of like one nanosecond.
[627.64 --> 634.06]  But you then have these bigger memories, which are high bandwidth memories, which are like
[634.06 --> 635.86]  closer to 50 to 100 nanosecond.
[635.86 --> 643.42]  And for a task to be processed performantly, data needs to be fetched from between these
[643.42 --> 646.68]  different memories onto the compute, which is there.
[647.20 --> 650.42]  And that transfer of data adds in more delays.
[651.34 --> 654.02]  And since this is a conservative system, right?
[654.10 --> 658.56]  So let's say you have two operations and one depends on the other.
[658.72 --> 661.64]  It's waiting on that operation to complete.
[661.64 --> 664.06]  So it adds on further delays, you know?
[664.14 --> 666.86]  So one operation is stuck on waiting on the data.
[667.38 --> 671.14]  The other operation is stuck on the second operation, right?
[671.46 --> 676.26]  So that kinds of just incrementally adds more and more delays into this.
[676.68 --> 683.42]  So that's an example of how the traditional, I guess, compiler or the traditional kernel-based
[683.42 --> 686.26]  system doesn't scale as well.
[686.26 --> 694.02]  What Grok chooses to do, of course, is not have any kernels whatsoever, but have a compiler
[694.02 --> 696.46]  which controls this at a fine-grained level.
[697.24 --> 700.92]  So a typical system will have multiple chips, right?
[701.30 --> 708.12]  So AI, you know, I'm sure people are familiar with models like LAMA 70 billion, right?
[708.48 --> 715.48]  And these models tend to be split across multiple GPUs and even on multiple Grok chips, right?
[715.48 --> 722.50]  And this compiler kind of controls how this model is precisely split across these different
[722.50 --> 728.78]  chips and how it's executed and to get the best performance out of it down to the level
[728.78 --> 732.42]  of the chipset and the networking.
[733.08 --> 737.52]  So as I mentioned before, we've removed a lot of the hardware which adds delay.
[737.52 --> 745.34]  And this sort of scheduling is done by Grok's compiler alongside with some assistance from,
[745.46 --> 747.14]  of course, the firmware which is there.
[747.80 --> 749.32]  And I appreciate that.
[749.52 --> 755.26]  As we talk, I'm trying to get a good sense of kind of how the whole stack looks as you're
[755.26 --> 756.40]  starting to dive into it.
[756.42 --> 761.82]  And you've talked a bit about the kind of the compiler versus having a kernel kind of at
[761.82 --> 764.28]  the model layer there.
[764.94 --> 771.50]  But with you guys covering both the hardware and the software, is Grok, would you say Grok
[771.50 --> 775.72]  is, I try to understand kind of that whole business model that you're approaching it with,
[776.20 --> 780.94]  is it more of an integrator that's full stack all the way from the hardware up through the
[780.94 --> 783.04]  OS and into the model layers?
[783.04 --> 788.80]  Or like from an integration layer, are you, do you think you're, are you writing most of
[788.80 --> 791.46]  the software stack that's touching the hardware?
[791.64 --> 796.36]  Like how do you, how do you choose whether to, to go pick that?
[796.44 --> 799.20]  And I'm just pulling things out of there, not attributing to you, but going and picking
[799.20 --> 804.84]  Linux and picking CUDA and picking this and picking that versus what you're writing to
[804.84 --> 806.24]  create your own full stack.
[806.32 --> 810.50]  How do you, I'm trying to get a sense of kind of how that's distributed those decisions
[810.50 --> 812.24]  from a design standpoint.
[812.24 --> 814.80]  Yeah, no, that's a great question.
[815.50 --> 818.68]  So all the way from our starting stack, right?
[818.74 --> 820.24]  So let's start at the top.
[820.72 --> 828.48]  So most folks end up and think about using AI models in production, would end up using some
[828.48 --> 829.22]  sort of API.
[830.10 --> 837.24]  So we, our cloud organization designed a REST compatible API, it's compatible with OpenAI
[837.24 --> 842.56]  spec, which is there, which makes it very easy for developers to really integrate with it.
[843.20 --> 848.00]  And then that ties into all the way into our rest of our stack.
[848.42 --> 853.88]  And to answer your question directly, yes, most of the stack has been custom written.
[853.88 --> 861.90]  We are, of course, using some Linux-based primitives, which are there underneath our system.
[862.32 --> 870.80]  And there are, of course, some components such as for the compiler, there is this MLIR system,
[871.32 --> 872.64]  which is being used.
[872.64 --> 876.02]  MLIR is like a compiler term.
[876.20 --> 881.20]  I don't want to go super deep into it, but it's like a multi-level intermediate representation,
[881.20 --> 885.48]  which kind of helps to transform things in between.
[885.48 --> 893.02]  So overall, I would say this entire design pattern has been thought through from scratch.
[893.40 --> 898.46]  And it's taken the company a couple of iterations to get to that point.
[907.08 --> 913.32]  Well, friends, I am here with a new friend of mine, Scott Dietzen, CEO of Augment Code.
[913.56 --> 914.52]  I'm excited about this.
[914.52 --> 919.50]  Augment taps into your team's collective knowledge, your code base, your documentation, your dependencies.
[919.94 --> 924.02]  It is the most context-aware developer AI, so you won't just code faster.
[924.10 --> 925.26]  You also build smarter.
[925.52 --> 927.02]  It's an ask me anything for your code.
[927.12 --> 928.54]  It's your deep thinking buddy.
[928.76 --> 930.44]  It's your stay-in-flow antidote.
[930.64 --> 934.44]  Okay, Scott, so for the foreseeable future, AI-assisted is here to stay.
[934.44 --> 938.70]  It's just a matter of getting the AI to be a better assistant.
[939.28 --> 943.22]  And in particular, I want help on the thinking part, not necessarily the coding part.
[943.22 --> 948.58]  Can you speak to the thinking problem versus the coding problem and the potential false dichotomy there?
[948.58 --> 950.32]  A couple of different points to make.
[950.54 --> 956.74]  You know, AIs have gotten good at making incremental changes, at least when they understand customer software.
[957.08 --> 963.32]  So first, and the biggest limitation that these AIs have today, they really don't understand anything about your code base.
[963.32 --> 967.36]  If you take GitHub Copilot, for example, it's like a fresh college graduate.
[967.50 --> 972.16]  Understands some programming languages and algorithms, but doesn't understand what you're trying to do.
[972.44 --> 980.16]  And as a result of that, something like two-thirds of the community on average drops off of the product, especially the expert developers.
[980.60 --> 981.40]  Augment is different.
[981.68 --> 987.26]  We use retrieval augmented generation to deeply mine the knowledge that's inherent inside your code base.
[987.26 --> 1001.00]  So we are a copilot that is an expert and that can help you navigate the code base, help you find issues and fix them and resolve them over time much more quickly than you can trying to tutor up a novice on your software.
[1001.54 --> 1003.84]  So you're often compared to GitHub Copilot.
[1004.00 --> 1006.32]  I got to imagine that you have a hot take.
[1006.72 --> 1008.48]  What's your hot take on GitHub Copilot?
[1008.84 --> 1010.96]  I think it was a great 1.0 product.
[1010.96 --> 1014.88]  And I think they've done a huge service in promoting AI.
[1015.32 --> 1016.78]  But I think the game has changed.
[1017.12 --> 1025.38]  We have moved from AIs that are new college graduates to, in effect, AIs that are now among the best developers in your code base.
[1025.60 --> 1030.38]  And that difference is a profound one for software engineering in particular.
[1030.64 --> 1036.74]  You know, if you're writing a new application from scratch, you want a web page that'll play tic-tac-toe, piece of cake to crank that out.
[1036.74 --> 1044.22]  But if you're looking at, you know, a tens of millions of line code base, like many of our customers, Lemonade is one of them.
[1044.40 --> 1046.18]  I mean, 10 million line monorepo.
[1046.46 --> 1058.12]  As they move engineers inside and around that code base and hire new engineers, just the workload on senior developers to mentor people into areas of the code base they're not familiar with is hugely painful.
[1058.12 --> 1071.22]  An AI that knows the answer and is available 7x24, you don't have to interrupt anybody and can help coach you through whatever you're trying to work on, is hugely empowering to an engineer working in unfamiliar code.
[1071.60 --> 1072.02]  Very cool.
[1072.10 --> 1082.40]  Well, friends, Augment Code is developer AI that uses deep understanding of your large code base and how you build software to deliver personalized code suggestions and insights.
[1082.40 --> 1086.64]  A good next step is to go to augmentcode.com.
[1086.72 --> 1090.88]  That's A-U-G-M-E-N-T-C-O-D-E.com.
[1091.16 --> 1097.52]  Request a free trial, contact sales, or if you're an open source project, Augment is free to you to use.
[1097.90 --> 1100.38]  Learn more at augmentcode.com.
[1100.44 --> 1104.76]  That's A-U-G-M-E-N-T-C-O-D-E.com.
[1105.26 --> 1106.64]  Augmentcode.com.
[1106.64 --> 1107.08]  Thank you.
[1112.40 --> 1126.60]  So, DJ, you mentioned that a lot of the focus around, you know, really that design from the hardware layer up through those software layers and digging into all of those was to achieve fast inference.
[1126.60 --> 1141.68]  Could you tell us a little bit about the kinds of models that you've run on Grok and just some, you know, some highlights in terms of when you say fast performance, what does that mean in practice?
[1141.68 --> 1147.72]  Now, I've seen some pretty impressive numbers on your website, so I won't steal your thunder.
[1148.38 --> 1156.92]  But, yeah, just talk a little bit about kind of what is achievable with what kinds of models on the Grok platform.
[1157.42 --> 1157.64]  Yeah.
[1157.92 --> 1162.78]  So, first of all, you know, I share some numbers, but we are just getting started.
[1163.06 --> 1165.84]  So, these numbers are only going to get better with time.
[1165.84 --> 1175.84]  But, like, let's say, let's take Lama 370 billion as an example, tends to be one of those industry standards for comparing performance.
[1176.54 --> 1186.58]  So, we've had numbers all the way from, like, 300 tokens per second to, like, multiple thousands tokens per second, depending on those use cases.
[1186.58 --> 1187.50]  Right.
[1187.66 --> 1194.54]  And, yeah, we've had some smaller models which go up to several thousand tokens per second.
[1195.20 --> 1203.64]  We've had one of our speech-to-text models called Whisper, which is, again, an open AI model running on Grok.
[1204.02 --> 1212.40]  And this model, I think we've gotten around 200x as the speed-up factor as they discuss it in the audio world.
[1212.40 --> 1212.96]  Yeah.
[1213.14 --> 1222.04]  And maybe talk a little bit about, and maybe for those out there that aren't, they're trying to process these thousands of tokens per second, what does that imply?
[1222.40 --> 1234.26]  I would say, you know, if you're using a chat interface, for example, and something is responding at thousands of tokens a second, it's, you know, potentially a wall of text.
[1234.26 --> 1239.76]  It's sort of almost all at once, as far as our human eyes see it.
[1240.02 --> 1243.46]  Could you talk a little bit about the implications of that?
[1243.54 --> 1248.72]  So, I mentioned the chat interface, which certainly some people are using chat interfaces, right?
[1248.78 --> 1260.32]  But at the enterprise level, for true enterprise AI use cases, why is fast inference for these kinds of models, why is that important?
[1260.32 --> 1269.36]  Because, like, in a chat interface, I can only read so much text so fast, right, with my own human mind as it comes back to me.
[1269.82 --> 1282.36]  Could you give us some, you know, and I certainly, you know, have my own thoughts on this, but I'm wondering if you could think about why does that speed matter in enterprise use cases?
[1282.36 --> 1290.16]  And why does it matter to push that maybe, you know, further than, you know, our own speed of reading, for example?
[1290.76 --> 1291.80]  No, great question.
[1292.44 --> 1305.00]  So, I think if you were to start with what Google studies from a decade ago, right, people's perception or, like, search results is, like, if it takes longer, then I think it's about 200 milliseconds or so.
[1305.00 --> 1313.92]  So, somebody, like, lose interest, you know, so speed is critical, whether it's for the enterprise or everyday people, right?
[1313.92 --> 1319.50]  I mean, we've demonstrated this several times, and you can try out for yourself.
[1319.68 --> 1331.14]  You can have, like, let's say you open ChatGPT with something like O1, or you have Grok on the side with one of our reasoning models, and you can try comparing them side by side.
[1331.14 --> 1346.44]  So, what becomes more critical, as I'm coming to, is that we, like, everybody thinks of speed as being, yes, it's important for real-time applications, but then there is the aspect of accuracy, right?
[1346.84 --> 1356.66]  So, if you could reason for longer, for, let's say, in the case of our reasoning models, so we've had, like, DeepSeek R1, for example, right?
[1356.66 --> 1367.66]  And these models, they generate a lot of tokens, and if you can reason for longer, you can get higher quality results as a consequence of this.
[1368.36 --> 1381.30]  So, while not making the system too slow for the user, right, so whether, again, it's enterprise or it's for everyday users, speed can translate to quality as well.
[1381.30 --> 1392.54]  So, to extend that just a little bit, if you are, and we've kind of been talking, you know, directly about inference speed and stuff like that, more from the practitioner standpoint,
[1393.14 --> 1405.26]  if you're maybe, you know, a business manager or a business owner out there, and you're looking at Grok, and you're kind of comparing it against kind of more traditional inference options that are already out there,
[1405.26 --> 1411.46]  when you're talking in terms of speed and, for instance, being able to have the time to do the research and stuff,
[1411.46 --> 1418.36]  what are some of the use cases from a business standpoint where they need to go,
[1418.80 --> 1426.62]  it's time for us to reassess kind of the more traditional routes that we've taken on inference and look at Grok for these solutions?
[1427.16 --> 1430.26]  Could you talk a little bit about what some of those business cases would be?
[1430.26 --> 1435.82]  Yeah, I mean, if you care about accuracy, speed, or cost, you should consider Grok.
[1436.44 --> 1447.76]  So, not only are we fast, the Grok LPU architecture allows us to give really low cost, or I would say our costs per token are really low,
[1448.34 --> 1451.80]  and we pass on those savings to all of our customers.
[1451.80 --> 1458.20]  So, if you are concerned about any of these cases, and you want to work with different modalities,
[1458.80 --> 1465.32]  if you care about image, text, or audio, if you care about RAG, if you care about reasoning, we are there for you.
[1465.68 --> 1471.54]  Yeah, and just to tie into that as well, some people might be listening to this and thinking in their mind,
[1471.54 --> 1476.66]  oh, Grok has this whole platform that they've designed, hardware and software.
[1477.24 --> 1480.64]  I don't have a data center.
[1481.12 --> 1485.72]  It's going to be expensive for me to spin up racks of these things.
[1486.12 --> 1491.80]  Could you talk a little bit about, I mean, I think, I could be mistaken, so please correct me.
[1491.80 --> 1494.02]  I think that is something that can happen.
[1494.18 --> 1501.80]  I mean, there are physical systems that people can access and use and potentially bring into their infrastructure.
[1502.08 --> 1511.44]  But I know also I see a login, I see API, as you mentioned, REST API in your previous answer about the developer experience.
[1511.64 --> 1520.08]  So, maybe just talk through some of those access patterns and also how you as a company have thought about which of those you provide.
[1520.08 --> 1530.98]  Because certainly there are advantages on the hardware side of maybe a fixed cost, but then there's the burden to support that.
[1531.10 --> 1537.88]  So, just talk us through a little bit about the strategy that you all have taken because you are deploying this whole platform.
[1538.48 --> 1544.96]  How have you thought about providing that to users in what sort of access patterns, I guess?
[1545.52 --> 1546.00]  Right.
[1546.00 --> 1553.92]  So, I'd say to start with, one can go to our website, grog.com, and just experience the speed themselves.
[1554.22 --> 1555.76]  It's a chat interface.
[1556.54 --> 1560.72]  And then it's trivial to sign up for our account over there.
[1561.16 --> 1566.00]  And on a free tier, we offer like tons of tokens over there for free.
[1566.18 --> 1569.88]  You can sign up and get access to our APIs.
[1569.88 --> 1582.38]  So, once you get access to our APIs, and let's say you've already been using an existing API, let's say you're using OpenAI, it's pretty easy for you to switch to a grog.
[1582.88 --> 1586.00]  And it's maybe a single or two-line change.
[1586.36 --> 1588.04]  And just try it out for yourself.
[1588.04 --> 1595.26]  We firmly believe in letting people experience the magic themselves, other than us talking about it.
[1595.60 --> 1597.62]  I think just actions speak louder.
[1597.98 --> 1598.84]  So, yeah.
[1599.24 --> 1608.12]  For, of course, our deep enterprise customers, we, of course, do offer other services on that side.
[1608.12 --> 1614.94]  So, you're talking about single tenant, and then there's, of course, multi-tenant-based architectures over there.
[1615.08 --> 1620.30]  So, we do offer dedicated instances where there's a real need for that.
[1620.76 --> 1622.28]  And we do manage that.
[1622.40 --> 1629.12]  So, now grog kind of deploys its own data centers, and we offer those all over an API.
[1629.52 --> 1633.88]  So, it's very easy for our customers to go and sign up and use them.
[1633.88 --> 1643.88]  You could, I'm going to ask you if you would, if you could kind of talk a little bit about it, just because as folks are listening and stuff, and they will go try that out after that.
[1643.92 --> 1647.96]  And I know that we'll have links in the show notes to the site so that they can do that.
[1648.12 --> 1658.82]  But could you talk a little bit about, and you could pick your example, but, you know, kind of, you mentioned, like, the OpenAI, you know, and something that they've probably had, you know, had experience with.
[1658.82 --> 1663.88]  And, you know, it's one of those things that kind of everybody has at least touched at some point out there.
[1664.16 --> 1666.68]  And you're providing a better experience here.
[1666.86 --> 1673.72]  And could you talk a little bit about what that is when you talk about go experience this yourself, and you're going to see how amazing it is.
[1673.72 --> 1687.32]  Could you talk through what you've seen your customers experience in that way, just so that listeners will kind of get a sense or maybe a preview of what they should experience having messed around with OpenAI for a while.
[1687.50 --> 1691.30]  And now they're going over to Brock, and they're doing that, and they're going, whoa, this is amazing.
[1691.64 --> 1693.62]  What is that amazing that you're expecting them to see?
[1693.62 --> 1706.92]  Well, first of all, people are just amazed by the speed that they get, like the speed of the output that comes up, you know, whether it's text or audio, you just get the output right away, right there.
[1707.38 --> 1709.10]  It's really, really fast.
[1709.28 --> 1715.20]  And it's, I think, really makes people think of new ways of doing things.
[1715.20 --> 1723.24]  So, you know, one example from our developer community, and, you know, our developer community has grown to over a million developers now.
[1723.96 --> 1739.50]  So, one recent example from a hackathon was that somebody developed this snowboarding navigation system based on Grok, taking images and kind of trying to guide people while snowboarding.
[1739.50 --> 1744.68]  And my mind was blown by these creative geniuses out there.
[1745.20 --> 1746.00]  Just amazing.
[1746.58 --> 1751.04]  So, all sorts of new applications out there enabled by the speed.
[1752.00 --> 1757.34]  Well, DJ, I do want to follow up on some of what you had talked about there on the developer community.
[1757.64 --> 1760.44]  So, could you maybe clarify one thing for me?
[1760.44 --> 1774.64]  So, there's the Grok systems that you have deployed and models that you have deployed in those systems, which it sounds like if I'm interpreting things right, people can just use, I'm assuming,
[1774.64 --> 1784.26]  your programming language clients or REST API to access that API and build off of those models that are in that environment.
[1784.44 --> 1792.68]  So, in that case, it's sort of accessing models, maybe in a, like you say, in a similar way to they would access open AI models and that sort of thing.
[1792.68 --> 1803.74]  Is there another side of the developer community that is saying, hey, well, we're actually, we have our own custom models, whatever those might be.
[1804.14 --> 1805.88]  What is the process?
[1805.88 --> 1812.42]  I guess my question is, what is the process of getting a model supported on Grok?
[1812.46 --> 1819.76]  You've talked about mainly kind of the Gen AI level models of, you know, LLM or vision or transcription.
[1819.76 --> 1844.64]  How wide is the support for models in terms of, hey, if I have this model, you know, I'm thinking in my mind, you know, manufacturing scenario, if I have a model that's a very specific model that needs to run at extremely fast speeds to like classify the quality of products coming off of a manufacturing line.
[1844.64 --> 1850.92]  Right. But it's a custom model. And I say, OK, I, you know, Grok has the fastest inference.
[1851.30 --> 1865.26]  What is the kind of what should I expect in terms of kind of model support as of now in terms of architectures and then your vision for that in the future and also how maybe people could contribute there if there is an opportunity?
[1865.86 --> 1871.90]  Yeah, I think right now one can just reach out to our sales team and we can figure it out.
[1871.90 --> 1881.58]  So based on the workload and the size of the model and things like that, we could we could figure out what's the best path going forward.
[1881.94 --> 1891.34]  Now, going to the future, we have some very exciting developments, but I don't want to spoil that right now since it's still a work in progress.
[1891.34 --> 1895.38]  So I guess we'll disclose that whenever we can.
[1895.38 --> 1906.30]  And maybe kind of along with that, I know we have, you know, even my team, we've tried out running models on a variety of kind of GPU alternatives.
[1906.90 --> 1911.52]  Sometimes what happens there is, you know, the latest model comes out on the market.
[1911.52 --> 1919.04]  Right. And it's maybe, you know, supported in certain driver ecosystems very quickly.
[1919.04 --> 1930.46]  And then maybe on some of these alternates, there's a there needs to be a kind of longer pathway for support in kind of custom software stacks that aren't, you know, aren't GPU based.
[1930.66 --> 1932.74]  How do you all navigate that right now?
[1932.80 --> 1938.66]  I know, you know, of course, our team is is small and it's hard for us to navigate that.
[1938.66 --> 1942.36]  And maybe you have people thinking about those things every day.
[1942.54 --> 1959.68]  But yeah, how do you how do you navigate that challenge as an engineering team to support all of these different models as they're as they're coming out, given that you have a different a completely different software stack than, you know, others are working with in the ecosystem?
[1960.56 --> 1966.42]  Yeah, if you think about it, we don't have to write kernels per model level, you know.
[1966.42 --> 1979.50]  So when a new model comes out, generally on the GPU world and even other custom accelerators, typically people spend a lot of time writing more optimal versions of it.
[1979.72 --> 1983.92]  So you might hear about new CUDA kernels being launched.
[1984.06 --> 1988.92]  Let's say, you know, after the original attention, there was the flash attention one.
[1989.18 --> 1994.36]  So that's like more optimal way of running some of these models on the GPU.
[1994.36 --> 1998.48]  But we don't have to do this at a per model level.
[1998.94 --> 2009.02]  What ends up happening is as we enhance our compiler over time, all these enhancements just reflect on to all of the models that we end up supporting.
[2010.02 --> 2016.36]  And the process to support different models on Grok is kind of similar.
[2016.36 --> 2023.38]  We end up spending some time removing vendor specific hard codings, right?
[2023.44 --> 2027.26]  So there tends to be a lot of GPU specific code, which we end up removing.
[2028.16 --> 2034.58]  And then we kind of run a compiler to translate this into, you know, finally to the Grok hardware.
[2034.58 --> 2041.66]  But there are a lot of knobs we tweak and turn to give you the best possible performance of that.
[2042.30 --> 2049.26]  And as the compiler improves with time, we just end up passing on these improvements to all the models right away.
[2049.78 --> 2053.86]  So our effort per model is not as high, you know.
[2053.86 --> 2074.04]  So just to clarify on that point, these models would kind of roll out, you would kind of build into the compiler kind of less vendor specific thing or, you know, more general functionality over time, which would expand your ability to support certain types of operations.
[2074.04 --> 2079.04]  But you wouldn't necessarily be able to say, hey, I've got this random model.
[2079.20 --> 2085.44]  I created my, you know, some research team created their own architecture, right, of this crazy thing.
[2085.64 --> 2092.60]  It may take some effort to kind of map that into the Grok software stack.
[2092.72 --> 2098.78]  But maybe if I'm hearing right, sort of less burden over time as the ecosystem develops.
[2098.96 --> 2101.06]  Is that the right way to interpret that?
[2101.06 --> 2102.26]  Partially, yes.
[2102.72 --> 2112.14]  But I would add that if you think about what the Grok system is at the heart of it, right, it's matrix multiplication and vector matrix multiplications.
[2112.40 --> 2116.32]  And that's what most machine learning models are there, right?
[2116.68 --> 2127.70]  Yes, when we have a generational shift like transformers, one might want to go and look at what's the new model type and how well does it map to our hardware.
[2127.70 --> 2132.12]  We might want to have some strategies to address some of that, right?
[2132.54 --> 2139.06]  But fundamentally, models haven't changed all that much after the transformers have been introduced.
[2139.70 --> 2145.56]  Now, you know, you kind of hear about diffusion models, even in the text world most recently.
[2145.56 --> 2160.60]  But as long as these fundamentals don't change frequently, I think our core belief of just supporting this wide ecosystem of models continues to live sturdy.
[2160.60 --> 2169.78]  If you look at other A-accelerators, some of them have gone and hard-coded, let's say, to the transformer architecture itself.
[2170.62 --> 2174.56]  And their bet is that super specialization is the way to go.
[2175.06 --> 2179.78]  But our belief is that we would like to support a more wider scale of models.
[2179.78 --> 2204.16]  And that's pretty much what our compiler system would do to kind of map between this high-level, let's say, PyTorch model into the Grok platform, converting it to, let's say, an intermediate layer where the compiler could work independently of what model it is.
[2204.16 --> 2211.18]  So there's no hard coupling, let's say, to a particular model or to even an architecture type.
[2211.38 --> 2213.44]  It's very low coupling.
[2214.88 --> 2216.08]  I'm curious.
[2216.34 --> 2224.92]  I've been really kind of spinning on the speed of what you're talking about in terms of inference and some of the capabilities that your stack offers.
[2224.92 --> 2235.76]  As in general, as the model ecosystem has been developing into the second half of last year and into this year, raging into this year, kind of agentic AI.
[2236.48 --> 2239.98]  And then that's kind of evolving into physical AI.
[2240.38 --> 2252.64]  And so you're dealing with robotics and autonomy and things like that that you're supporting to where we're expecting an explosion of devices out there in the world that these systems are supporting.
[2252.64 --> 2267.94]  What is your strategy forward and approach for thinking about kind of physical AI that we're evolving into where you have agents that are interacting with physical devices that are interacting with us in the real world?
[2268.46 --> 2271.58]  So it's not all in the data center, but the data center is supporting that.
[2272.34 --> 2276.72]  How does that fit into your overall view forward?
[2277.46 --> 2281.60]  Yeah, I think the AI industry revolves very rapidly.
[2281.60 --> 2289.24]  Like personally, I don't think there can be any long term strategy which will not need adjustments based on developments.
[2290.20 --> 2304.10]  But our belief is still that I think edge based deployments, you know, and calling things over APIs will be the preferred interface going forward for a long time.
[2304.10 --> 2312.92]  Right. So sure, your let's say mobile chip might be able to perform some basic level tasks over there.
[2313.02 --> 2322.40]  But if you need like really high accuracy, high quality model inference, doing this over an API, I think would get you there.
[2322.40 --> 2329.22]  So compared to the model size, which you can actually deploy on a mobile phone.
[2329.66 --> 2331.88]  So this is an example for like an edge device.
[2331.88 --> 2333.70]  I have one question for you.
[2333.70 --> 2354.52]  Just as an engineer that has been working on at the kind of forefront of this inference technology, what has been some of the challenges that I guess you faced as you really dug into these problems, maybe that were unexpected or maybe they were expected for you?
[2354.52 --> 2364.04]  What would have been some of the biggest challenges and maybe some learnings that looking back on your time working on this system you can share with the audience?
[2364.62 --> 2365.88]  Yeah, no, great question.
[2366.78 --> 2373.44]  As I said, I think the industry moves really fast and sometimes there are these shifts, right?
[2373.44 --> 2381.20]  So we saw this shift to large language models and that's when the company itself kind of pivoted to focus on this.
[2381.20 --> 2391.18]  So Meta releasing Lama and the Lama 2 series of models was really what got our company to focus on this side and really push on this, right?
[2391.76 --> 2395.34]  So similarly, I think we are a startup.
[2395.52 --> 2400.14]  We are always pushing on all fronts, always trying to improve on things.
[2400.14 --> 2411.30]  So whenever there's some new architectural change, we look to see how we could best adapt our system for that to get to maximize throughput, right?
[2411.74 --> 2422.78]  So sometimes there are these kind of changes and, you know, this is something which actually excites me about Grok and working at such a talent-tense company.
[2422.78 --> 2435.62]  My colleagues really come up with really great, exciting new ways of doing things to really push the bar on some of these things.
[2436.38 --> 2444.04]  So maybe it's like could be a mixture of experts or reasoning models whenever something new comes up, right?
[2444.04 --> 2449.84]  Like I think that's getting the maximum performance out of that is something we care about.
[2450.26 --> 2451.30]  We deeply care about.
[2451.64 --> 2455.28]  And yeah, I think that's been one of the key areas.
[2455.92 --> 2456.14]  Awesome.
[2456.42 --> 2462.90]  Well, as we kind of get close to an endpoint here, this has been fascinating.
[2462.90 --> 2473.00]  I'm wondering, DJ, if you could just close this out by sharing some of the things that you think about personally, kind of going into this next year.
[2473.04 --> 2475.08]  As you mentioned, things are moving so fast.
[2475.22 --> 2476.52]  There are shifts that are happening.
[2477.22 --> 2484.48]  What are some of the things that are most exciting for you as you kind of head into this next year of development and work?
[2484.48 --> 2496.16]  So as a developer and like amateur data scientist, I would say that for me, the push on the coding side of the AI world has been very exciting.
[2496.88 --> 2504.32]  It helps me kind of think about how can I have more impact, whether it's at Grok or in the world in general.
[2504.68 --> 2514.18]  So the push of AI on the coding side, reasoning models, multiple modalities, and the fusion of all of this, right?
[2514.48 --> 2518.70]  I think that's what I really want to look forward to for the next couple of years.
[2519.28 --> 2521.76]  There's, of course, the robotics bit, which we touched upon.
[2522.34 --> 2526.22]  But that I feel is probably a couple of years down the line.
[2526.80 --> 2527.00]  Awesome.
[2527.56 --> 2530.52]  Well, thank you, DJ, for representing Grok.
[2530.52 --> 2538.78]  And congratulations on what you and the team have achieved, which is really amazing and monumental work.
[2538.96 --> 2540.28]  So great work.
[2540.40 --> 2541.06]  Keep it going.
[2541.06 --> 2546.92]  We'll be excited to follow the story and hope to get an update again on the podcast sometime soon.
[2547.14 --> 2547.50]  Thanks.
[2547.76 --> 2548.72]  Sounds great, guys.
[2548.82 --> 2549.66]  Thanks for having me.
[2556.66 --> 2557.64]  All right.
[2557.86 --> 2559.74]  That is our show for this week.
[2559.74 --> 2566.06]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[2566.42 --> 2568.52]  There you'll find 29 reasons.
[2568.74 --> 2572.10]  Yes, 29 reasons why you should subscribe.
[2572.58 --> 2573.96]  I'll tell you reason number 17.
[2574.54 --> 2577.30]  You might actually start looking forward to Mondays.
[2577.46 --> 2580.16]  Sounds like somebody's got a case of the Mondays.
[2580.56 --> 2585.12]  28 more reasons are waiting for you at changelog.com slash news.
[2585.12 --> 2591.02]  Thanks again to our partners at Fly.io to Breakmaster Cylinder for the Beats and to you for listening.
[2591.46 --> 2592.54]  That is all for now.
[2592.74 --> 2594.08]  But we'll talk to you again next time.
[2594.08 --> 2595.08]  Bye.
[2595.08 --> 2596.08]  Bye.
[2596.08 --> 2596.58]  Bye.
[2596.58 --> 2597.08]  Bye.
[2597.08 --> 2597.14]  Bye.
[2597.14 --> 2597.20]  Bye.
[2597.20 --> 2598.14]  Bye.
[2598.14 --> 2598.20]  Bye.
[2598.20 --> 2599.14]  Bye.
[2599.14 --> 2599.20]  Bye.
[2599.20 --> 2599.26]  Bye.
[2599.26 --> 2599.30]  Bye.
[2599.30 --> 2599.36]  Bye.
[2599.36 --> 2599.40]  Bye.
[2599.40 --> 2599.44]  Bye.
[2599.44 --> 2601.30]  Bye.
[2601.30 --> 2601.36]  Bye.
[2601.36 --> 2603.30]  Bye.
[2603.30 --> 2603.36]  Bye.
[2603.36 --> 2603.44]  Bye.
[2603.44 --> 2603.46]  Bye.
[2603.46 --> 2603.48]  Bye.
