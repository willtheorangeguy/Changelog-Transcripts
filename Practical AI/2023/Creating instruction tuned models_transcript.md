[0.00 --> 8.64]  Welcome to Practical AI.
[9.20 --> 15.96]  If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 --> 18.78]  are changing the world, this is the show for you.
[19.20 --> 24.36]  Thank you to our partners at Fastly for shipping all of our pods super fast to wherever you
[24.36 --> 24.66]  listen.
[24.92 --> 26.76]  Check them out at Fastly.com.
[26.76 --> 32.02]  And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 --> 33.70]  No ops required.
[34.02 --> 36.08]  Learn more at fly.io.
[42.46 --> 44.44]  Hello, this is Daniel Whitenack.
[44.54 --> 50.74]  I am here on site at ODSC East in Boston, the Open Data Science Conference.
[50.74 --> 57.66]  And I am super excited because I get to sit down with Erin McHale Staples, who's a developer
[57.66 --> 60.14]  community advocate at Label Studio.
[60.66 --> 63.08]  And yeah, what do you think of the conference so far, Erin?
[63.28 --> 67.18]  It's been, first off, super fan of kind of what you've been doing and a lot of anybody
[67.18 --> 71.88]  who's creating stuff out there in this space, especially with the current like zeitgeist
[71.88 --> 75.14]  and explosion of interest in AI and machine learning.
[75.24 --> 75.72]  It's a little crazy.
[75.96 --> 76.64]  It's a little wild.
[76.64 --> 77.76]  It's a little wild.
[78.04 --> 82.10]  I, you know, I would be lying if I'm not, wouldn't be saying I'm newer to the field myself,
[82.10 --> 84.68]  but it's been something I've been very fascinated about.
[85.18 --> 89.76]  But all that being said, this conference is really cool to see just the breadth of, first
[89.76 --> 90.48]  off, people here.
[90.56 --> 95.38]  There are people who are very new to the industry, people who came to just learn more for their
[95.38 --> 96.10]  first time.
[96.10 --> 99.44]  But there are people who had been practicing for years and years, and this is their third
[99.44 --> 101.00]  or fourth time at ODSC.
[101.78 --> 107.16]  And I'm also really interested about the number of people concerned about data integrity here.
[107.64 --> 107.76]  Yeah.
[108.14 --> 113.08]  Lots of like interpretability, integrity, reliability type talks.
[113.20 --> 113.34]  Yeah.
[113.42 --> 114.28]  Lots of reliability.
[114.60 --> 116.70]  The other one is like also on missing data.
[116.70 --> 121.12]  And like, how do we approach these problems, especially with the rise of foundational models
[121.12 --> 121.90]  and generative AI?
[121.90 --> 126.34]  Like, how does that impact it for the long, which is crucial conversations, I think, to
[126.34 --> 126.58]  have.
[127.10 --> 127.86]  Yeah, definitely.
[128.36 --> 133.28]  And what sorts of different players in the space are you seeing at this conference, both
[133.28 --> 141.02]  in terms of like open source or like different kind of targets, like ML ops platforms, that
[141.02 --> 141.46]  sort of thing?
[141.52 --> 142.60]  How do you see that developing?
[143.48 --> 146.56]  First off, I'm personally a huge fan of open source.
[146.74 --> 151.88]  It's not only how I learned to code in the first place, but just a big believer in the
[151.88 --> 152.40]  ecosystem.
[152.68 --> 154.16]  I'm a huge believer in open data.
[154.52 --> 156.16]  I'm a participant in open data week.
[156.24 --> 157.36]  So I think all of these things are like.
[157.66 --> 159.70]  And you're wearing a pie lady shirt, which is awesome.
[159.86 --> 159.98]  Yeah.
[160.22 --> 161.34]  I'm a member of pie ladies.
[162.48 --> 165.92]  So again, super important, I think, to have all these things in the ecosystem.
[165.92 --> 170.88]  But one of the things I think that stands out is there's so many new innovations that
[170.88 --> 175.32]  like if you're starting a tech stack from ground zero, it's really fun to see all the
[175.32 --> 176.48]  different players in the game.
[176.48 --> 181.84]  So selfishly, working at Label Studio, one of the best things about being in the space
[181.84 --> 185.58]  right now is we're a cool platform because we can integrate with so many different data
[185.58 --> 191.48]  types that it means that I always get to play with almost every other tool or workshop or
[191.48 --> 193.94]  players in the ecosystem, which is selfishly fun.
[194.12 --> 197.34]  It means I get to have more things to integrate with or build.
[197.34 --> 202.12]  And as always, we're huge friends of what the Pachyderm team is always doing.
[202.92 --> 204.24]  Work very closely with them.
[204.38 --> 205.14]  We work very closely.
[205.70 --> 208.34]  We've got a lot of friends and fans, the DVC crew.
[208.76 --> 213.36]  They're not here at this conference round, but did get to work with them at PyCon, which
[213.36 --> 215.64]  was really amazing to see kind of the work that they're coming out with.
[216.28 --> 218.68]  The Condor crew is always fun to see around.
[219.08 --> 219.90]  So that's always exciting.
[220.72 --> 220.88]  Cool.
[221.10 --> 221.30]  Yeah.
[221.42 --> 221.62]  Yeah.
[221.62 --> 223.72]  There's so many awesome things going on.
[223.72 --> 229.52]  And I've seen maybe three or four open source packages that I don't know if I've been ignoring
[229.52 --> 230.48]  or I haven't heard about.
[230.64 --> 233.68]  So that's one of the fun things about coming to these things.
[234.38 --> 240.66]  I know also you gave a recent talk at PyData Berlin about reinforcement learning from human
[240.66 --> 242.26]  feedback, I believe was the topic.
[242.64 --> 249.84]  Could you tell us a little bit about the general pitch or angle on that talk, which is definitely
[249.84 --> 255.28]  like a key topic these days with all the instruction tune models that are coming out and all of
[255.28 --> 255.48]  that.
[255.64 --> 259.04]  So what was your kind of angle in terms of what you're thinking about there?
[259.36 --> 259.58]  Yeah.
[259.68 --> 264.42]  So I think one of the cool things is it was a talk that Nikolai and I gave and Nikolai
[264.42 --> 266.82]  is the CTO and one of the co-founders of Label Studio.
[267.70 --> 273.60]  And what we did at Berlin is we really made sure to expand on this idea that like, yes,
[273.60 --> 277.30]  these generative models, these larger models are kind of becoming the norm.
[277.30 --> 281.18]  I think we met yesterday, I was talking to someone who was like, I got interested in
[281.18 --> 283.50]  AI because I made a thousand things with MidJourney.
[283.56 --> 284.06]  I'm like, cool.
[284.28 --> 289.04]  And I'm very fascinated by, and I'm a believer, like, I don't care how you got into it, but
[289.04 --> 292.66]  just the curiosity to show up to a conference and learn more is very fascinating.
[293.14 --> 298.14]  But explaining to someone how it works and then also explaining the best practices behind
[298.14 --> 299.04]  it is really important.
[299.52 --> 301.12]  Personally, I have a journalism background.
[301.26 --> 302.36]  I have a liberal arts background.
[302.36 --> 307.66]  And I think it's really important that we incorporate the humanities in technology for
[307.66 --> 308.18]  the long run.
[308.90 --> 312.90]  And so when it comes to reinforcement learning, all of these large generative models, they
[312.90 --> 317.32]  can all be made just a little bit better with the human signal that we can provide.
[318.12 --> 322.58]  And we can say a lot of things like, you know, get into prompt engineering, which is another
[322.58 --> 323.32]  whole other topic.
[323.32 --> 328.50]  But it will never be as good as like if you can retrain your own data set with subject matter
[328.50 --> 333.62]  experts or to a specific use case or condition that you're trying to output that data towards.
[334.22 --> 334.32]  Yeah.
[334.46 --> 339.74]  And I think one of the things that's been on my mind recently is like this topic, reinforcement
[339.74 --> 343.90]  learning from human feedback, especially with what's gone on with chat GPT and all, sometimes
[343.90 --> 348.62]  it feels like out of reach for like day-to-day data scientists.
[348.62 --> 354.12]  Like how do I, like I could leverage this model, but what is the tooling around reinforcement
[354.12 --> 355.56]  learning from human feedback?
[355.56 --> 362.32]  Like how could I use that framework or use tooling around that to like impact my own models
[362.32 --> 363.12]  or my own life?
[363.18 --> 369.52]  Like how could I connect my domain experts input and their preferences into a system that I'm
[369.52 --> 369.92]  designing?
[370.04 --> 370.84]  Do you have any thoughts there?
[371.18 --> 371.36]  Yeah.
[371.46 --> 375.44]  So one of the examples I love to point to is actually Bloomberg did this and they probably
[375.44 --> 376.70]  did this early April now.
[377.20 --> 381.78]  And they took the financial data that they had and Bloomberg from all the way back from like,
[381.92 --> 384.66]  you know, many of us know about it, Bloomberg from Bloomberg News, but that was actually the
[384.66 --> 387.12]  financial terminal that was used for stock trading.
[387.12 --> 391.06]  But they have these, I mean, mass amounts of financial data.
[391.20 --> 393.04]  And how do they stack on top of it?
[393.04 --> 399.20]  Like how do they get and access that data even faster and kind of train it to the best use
[399.20 --> 399.88]  case that we have?
[399.98 --> 402.34]  Like currently our larger models can't do that.
[402.60 --> 404.24]  They're not experts in financial data.
[404.24 --> 405.98]  They're not combing just financial data.
[406.52 --> 411.08]  But what Bloomberg did is they took and they retrained and they built the things.
[411.20 --> 414.32]  I probably fangirled over, sorry, if you're on the Bloomberg team and I fangirled over you
[414.32 --> 415.98]  at PyCon because I definitely was.
[416.28 --> 418.72]  I was like, I was like, this is the coolest thing ever.
[418.80 --> 419.60]  I use this as an example.
[419.74 --> 421.54]  Also, I like learn machine learning off of your repo.
[421.64 --> 421.74]  Okay.
[421.74 --> 421.94]  Thanks.
[421.98 --> 422.08]  Bye.
[422.08 --> 423.60]  But we do have a model.
[424.02 --> 427.82]  If you want to learn and see reinforcement learning in action, there is an open source
[427.82 --> 428.18]  repo.
[428.80 --> 435.14]  It is built by myself, Nikolai and Jimmy Whitaker, who is, we have as a data scientist in residence
[435.14 --> 439.38]  at Label Studio and Hartex, but also is at Pachyderm as well.
[439.84 --> 440.88]  But all of that is built.
[440.98 --> 441.40]  It's open.
[441.48 --> 442.18]  You can play around with it.
[442.24 --> 443.94]  It's based off of GPT-2 right now.
[444.08 --> 446.60]  So you can go have some fun and get your hands dirty.
[446.98 --> 449.68]  And it's all runnable within a Google CoLab notebook.
[450.04 --> 450.80]  That's awesome.
[450.80 --> 451.16]  Yeah.
[451.36 --> 456.40]  What is, so you mentioned it being run in a Google CoLab notebook, which I think is awesome.
[456.52 --> 461.10]  And using also a bit of a smaller model to start with.
[461.26 --> 467.32]  And we've seen a lot of kind of directions towards smaller open models that are accessible
[467.32 --> 471.32]  to data scientists with like LAMA and other things like that.
[471.70 --> 475.52]  How do you see that trajectory going?
[475.52 --> 481.56]  And how will that impact sort of like day-to-day practitioners in terms of what they're able
[481.56 --> 483.50]  to do with this sort of technology?
[484.08 --> 488.38]  I think the biggest thing, and I'm actually going to zoom out to answer this, is the biggest
[488.38 --> 489.52]  thing we need to think about is context.
[489.62 --> 493.48]  Like what are you using model to solve or AI to solve or ML to solve?
[493.52 --> 497.20]  And the more that I've been diving into these conferences and the ecosystem, especially at
[497.20 --> 500.06]  a conference where it's a blended conference, where you have folks that are not necessarily
[500.06 --> 504.26]  deep in the field or ML practitioner or they're like new to ML, it is so easy.
[504.34 --> 505.92]  And there's a meme I always point to that.
[505.98 --> 508.28]  It's like, oh, it's, you know, we're an AI back.
[508.36 --> 508.68]  So-and-so.
[508.72 --> 510.74]  And it's like, JK, we're just an AI.
[510.98 --> 514.44]  We're just, you know, calling the API and put a nice, pretty shiny front end on it,
[514.44 --> 520.76]  which is no shade to anybody who is putting a front end on a GPT API.
[520.76 --> 523.02]  Like there is no shade at all to that.
[523.56 --> 527.42]  But it's like, think about what you need a model for in the first place or what you
[527.42 --> 528.54]  want to use machine learning.
[528.62 --> 530.16]  Like that context is so important.
[531.00 --> 535.14]  I'm currently playing around with a naked and afraid data set just to like play around.
[535.26 --> 536.92]  There's an open source data set out there that is-
[536.92 --> 537.88]  Oh, that's awesome.
[538.26 --> 538.96]  Like videos?
[539.20 --> 543.70]  Like, no, it's context from the TV show of how many days they survived.
[543.90 --> 548.76]  Oh, so literally, yeah, like statistics about like, and features of the different survival
[548.76 --> 549.38]  situations.
[549.38 --> 555.66]  Yeah, it's like, it's like country, their name, gender, and then how many days they made
[555.66 --> 555.88]  it.
[556.06 --> 556.20]  Yeah.
[556.34 --> 557.06]  And like climate.
[557.68 --> 557.90]  Yeah.
[558.56 --> 562.58]  Based on that, like, yeah, that's so intriguing.
[562.74 --> 563.68]  I watch, I watch a lot.
[563.88 --> 568.92]  So confession, I watch also the Alone show, which is like another survival show.
[568.92 --> 570.88]  This is like, I'm a huge fan.
[571.80 --> 572.64]  Terrible junkie.
[572.80 --> 574.88]  I, that is how I do stress is reality TV.
[575.08 --> 579.36]  But so I always wonder, I have this conversation with my wife around like, could I do this
[579.36 --> 584.90]  and maybe with a model trained off of, off of your survival data set?
[584.98 --> 588.16]  I could like say, I'm from here and this is my background.
[588.48 --> 589.42]  Could I survive?
[589.64 --> 589.80]  Yeah.
[589.80 --> 590.08]  I don't know.
[590.30 --> 592.08]  And I can't take credit for the original data set.
[592.38 --> 595.98]  It is someone who I've made friends with in my reality TV subreddit.
[595.98 --> 599.98]  So if you need to know where I spend my time, but he runs a SQL database.
[600.14 --> 601.48]  It is actually very good.
[601.66 --> 603.00]  He's very awesome updating it.
[603.06 --> 603.70]  It's available on Reddit.
[603.82 --> 605.84]  I can share it with you and you can post it in the links.
[606.56 --> 609.32]  But I'm just kind of playing around with the data set for fun.
[609.42 --> 613.72]  But in this context, like I'm playing around building demos and just having some fun, teaching
[613.72 --> 614.80]  myself some new skills.
[614.80 --> 617.22]  I don't need a large foundational model for that.
[617.72 --> 621.04]  And I think going back to like your original question of like, well, all these models are
[621.04 --> 622.08]  getting smaller, more accessible.
[622.20 --> 622.98]  We can run it in a notebook.
[623.42 --> 627.44]  We don't need the high powered computer models, everything single times.
[627.44 --> 631.02]  And if we stop and think about the context of the problem that we're trying to solve,
[631.56 --> 635.08]  it can give us a lot of answers and it can save us time, energy and computing power.
[635.28 --> 638.82]  And I think that's why I get really excited about being on the data labeling side.
[638.94 --> 640.30]  Again, I have a background in humanities.
[640.60 --> 641.72]  I'm a self-taught programmer.
[641.72 --> 645.32]  But I think I don't want to be like, we need more people like me in data science, but we
[645.32 --> 648.48]  need more of the humanities in data science because we're missing the context.
[649.06 --> 654.00]  Yeah, we recently had a guest on the show that was talking about like the intersection
[654.00 --> 661.36]  of art history and computer science and how computer scientists who are analyzing and doing
[661.36 --> 667.42]  computer vision could actually learn a lot from like what we know about like art and like
[667.42 --> 673.54]  how scenes are composed or how art has changed over time and how the features that they're
[673.54 --> 676.18]  actually engineering are connected to some of those things.
[676.62 --> 680.78]  So yeah, I think that there's a lot of different areas where this could apply and domain experts
[680.78 --> 681.74]  are so important.
[682.20 --> 688.18]  And I assume that with all of this like reinforcement from human reinforcement learning from human
[688.18 --> 689.38]  feedback, I always mess it up.
[690.20 --> 691.02]  I've been it's okay.
[691.06 --> 691.90]  I've been doing the same thing.
[691.96 --> 694.22]  It's like R L H F.
[694.22 --> 694.70]  I get it.
[694.70 --> 699.76]  Yeah, especially since you're from the label studio side, do you have any could you give
[699.76 --> 706.98]  like a general picture or workflow for people of like, hey, I maybe want to take one of these
[706.98 --> 714.58]  models GPT to llama MPT now whatever the one is, but I also want to gather some domain expert
[714.58 --> 721.62]  feedback and eventually get to some type of like instruction or fine tuned model off of that.
[721.62 --> 727.36]  Like, could you just give a general picture for like what that looks in today's world?
[727.76 --> 728.00]  Yeah.
[728.24 --> 730.98]  Um, and we'll try this is like always, I feel like this is a better when you have a whiteboard
[730.98 --> 732.30]  and a diagram and some arrows.
[732.60 --> 733.18]  Oh, for sure.
[733.30 --> 734.10]  Yes, it's hard.
[734.20 --> 735.06]  I'll do a quick walkthrough.
[735.16 --> 738.16]  So first off, you'll create a sort of prompt.
[738.24 --> 742.42]  So typically these models work with a prompt and then you're given a large language model
[742.42 --> 743.56]  and then you start to train it.
[743.88 --> 748.00]  Usually what happens when you're training these models is you get a set of two outputs.
[748.00 --> 753.96]  And so in this case we can use, um, what is a possums because we're possum fans at label
[753.96 --> 754.26]  studio.
[754.44 --> 755.18]  I feel like that's natural.
[755.74 --> 761.32]  Um, and you can be like an opossum is a marsupial creature or a possum is a great character for
[761.32 --> 761.66]  memes.
[762.06 --> 766.32]  Technically both of those are correct, but depending on context and this is where that
[766.32 --> 767.64]  human signal side comes in.
[767.94 --> 770.44]  One answer is more correct than the other.
[770.44 --> 776.84]  So if we were training, let's say a possum meme bot thing or a meme bot generator, let's
[776.84 --> 777.48]  go that direction.
[777.58 --> 778.34]  We'll have some fun with it.
[778.64 --> 781.00]  We would take the latter answer of this.
[781.14 --> 783.28]  A possum is a great animal to make memes.
[784.40 --> 785.64]  And that would be the better answer.
[785.76 --> 789.36]  If we were going for what type of animal are we doing like a, maybe a biology assignment
[789.36 --> 791.70]  homework probably would pick the marsupial one.
[791.78 --> 796.38]  But this gives insight of like the details that you give your annotation team can really
[796.38 --> 797.74]  directly influence the model.
[798.08 --> 799.14]  That's the labeling side.
[799.14 --> 804.40]  When we move this on, all of this is put through kind of this results from human feedback.
[804.58 --> 805.42]  Your answers are ranked.
[805.52 --> 806.64]  I did a binary situation.
[806.74 --> 810.02]  So just two options, but you can have a multitude of options that you put in.
[810.20 --> 811.04]  It is all weighted.
[811.56 --> 816.56]  It is then looped back around when you wish that we had the whiteboard to a reward or a
[816.56 --> 817.36]  preference model.
[817.72 --> 821.70]  And this reward or the preference model kind of tells you like, Hey, I probably want to
[821.70 --> 823.82]  go for answers that look like this.
[823.82 --> 831.32]  Now computers don't speak memes or marsupial or biology textbooks, but they do know patterns
[831.32 --> 833.54]  and trends, which is like what they pick up on.
[833.66 --> 838.56]  So based on that context clues that we give them, this preference model will start to preference
[838.56 --> 839.58]  those type of answers.
[840.32 --> 845.26]  Now it's really important that these reward preference models also hold in place kind of
[845.26 --> 850.20]  the original things that we had that it knows, like how is language structured or other things
[850.20 --> 851.82]  from our original model that we enjoyed.
[851.92 --> 854.40]  Like we liked, like language is always structured like this.
[854.52 --> 855.50]  Here's a proper noun.
[855.64 --> 859.64]  We like to capitalize the first letter of the sentences, things that are important, but
[859.64 --> 863.66]  like we kind of overthink sometimes when talking about generative language models, at least.
[864.20 --> 867.34]  After that, we want to make sure that we're not just gaming a system.
[867.84 --> 870.00]  Models are, again, I don't think models are sentient.
[870.12 --> 873.58]  They're kind of just like math numbers or they're just trying to game a system.
[873.58 --> 876.86]  They're playing like, I always compare it to like, you're trying to like, it's money
[876.86 --> 877.64]  ball, essentially.
[878.02 --> 879.16]  I'm a baseball fan here.
[879.36 --> 880.32]  So it's money ball.
[880.40 --> 884.78]  You're, you're statsing out the system and they, in order so that they're just not giving
[884.78 --> 888.94]  you what you want to hear every time, you'll have to calculate an error rule in there.
[889.04 --> 893.36]  So put an error metric or an update rule and it basically says, all right, we're going
[893.36 --> 894.90]  to almost like dunk you down a little bit.
[894.98 --> 898.58]  So you're not too perfect and that'll prevent unwanted model drift.
[898.90 --> 902.80]  Then once you've done that a few times, you'll combine that with a copy of your original
[902.80 --> 904.24]  model that you had.
[904.44 --> 907.88]  Again, you're kind of doing that checks and balances, making sure it doesn't run away.
[908.64 --> 913.66]  After that, you will have a tuned language model and then rinse, wash, repeat until you've
[913.66 --> 915.04]  got that model right where you want it.
[915.46 --> 918.82]  Set it off to production and then talk to your friends that the other parts of your MLOps
[918.82 --> 919.40]  ecosystem.
[919.94 --> 920.30]  Yes.
[920.50 --> 921.56]  And it'll come in handy.
[921.68 --> 922.00]  Awesome.
[922.00 --> 922.28]  Yeah.
[922.50 --> 927.88]  And I hope that we can link some of your slides from that talk in our show notes.
[927.88 --> 928.24]  Of course.
[928.24 --> 932.04]  They're awesome, including emojis and the full deal, which helps.
[932.60 --> 934.78]  So make sure and check out the show notes.
[935.28 --> 939.02]  The link to the slides will be in there so you can take a look at these figures while
[939.02 --> 940.16]  you're listening to the show.
[940.52 --> 945.06]  One follow-up question on this, we're talking about gathering this feedback data.
[945.72 --> 950.08]  People can think about, okay, in the context of my company or where I'm working, I'm going
[950.08 --> 952.60]  to gather some of this data, tune a model.
[952.60 --> 960.62]  But what is your perspective on the open data ecosystem and what would you encourage people
[960.62 --> 966.64]  to think about in terms of data that they could make openly available to help others
[966.64 --> 972.16]  who are also trying to do this or the other way around, people that are searching for maybe
[972.16 --> 973.18]  a place to start?
[973.32 --> 979.46]  What does the open data ecosystem look like right now and how important is that as this
[979.46 --> 980.64]  sort of field advances?
[980.64 --> 981.16]  Yeah.
[981.54 --> 984.52]  First off, this is you've got me on my other favorite soapbox of the moment.
[984.68 --> 988.76]  And this goes back to my days when I was a journalism student working in journalism.
[989.64 --> 993.08]  But open data is one of my favorite topics to geek out on.
[993.84 --> 997.58]  Basically, it was something that really came actually as part of the Obama administration.
[997.78 --> 1003.08]  He actually established federal funding for a lot of our public and civic data as a part
[1003.08 --> 1004.90]  of government accountability and transparency.
[1005.64 --> 1009.58]  So there was actual federal grants that went out to make a lot of our civic data public.
[1009.58 --> 1011.52]  So there's a really cool example.
[1011.76 --> 1016.14]  I believe it's the city of Philadelphia that actually built a SimCity-like game off of their
[1016.14 --> 1017.12]  public data.
[1017.22 --> 1017.88]  It's so cool.
[1017.94 --> 1018.88]  It was like a grant given.
[1019.30 --> 1020.04]  Super fascinating.
[1020.42 --> 1021.86]  I'll link it to you and give it.
[1021.98 --> 1025.16]  It'll be in the plethora of show notes on all of that.
[1025.30 --> 1030.80]  But open data is just open, freely accessible, freely used data that is made available to the
[1030.80 --> 1031.02]  public.
[1031.40 --> 1032.12]  Love open data.
[1032.12 --> 1033.62]  I'm a participant in open data week.
[1033.88 --> 1038.36]  But when it's been federally funded, it's not always the best thing to be federally funded.
[1038.48 --> 1040.18]  And we all know how government grants go.
[1040.32 --> 1043.40]  And if you aren't aware how government grants go, they're very niche-specific and they run
[1043.40 --> 1043.68]  out.
[1044.28 --> 1045.96]  And they're not always maintained.
[1046.06 --> 1048.02]  And it's not always the cool, sexy job that we have.
[1048.18 --> 1051.64]  So they're always not the best maintained or context applicant.
[1051.64 --> 1056.32]  What a lot of these early machine learning models did and what a lot of machine learning
[1056.32 --> 1061.00]  models did is these open data sets have given opportunities for people like myself to even
[1061.00 --> 1062.66]  learn how to do data science.
[1062.78 --> 1065.08]  I learned Python in open data week.
[1065.44 --> 1069.04]  I remember going back and like, let's get the traffic data in New York City.
[1069.72 --> 1073.78]  And it's like basic, you know, using curl and like getting things started for the first
[1073.78 --> 1075.04]  like, can you query an API?
[1075.38 --> 1079.58]  Like, they're not the most organized data sets out there.
[1079.68 --> 1080.64]  They're not the most clean.
[1080.64 --> 1082.98]  Sometimes you get some really messy garbage data.
[1083.72 --> 1086.00]  You know, the 2020 census is actually a great example.
[1086.08 --> 1088.22]  I was speaking to someone yesterday at the conference about this.
[1088.86 --> 1091.34]  The 2020 census was the first time that we were able to do it digitally.
[1091.90 --> 1096.00]  Well, she gave the example of like, you know, hey, I started the census on my phone.
[1096.20 --> 1097.44]  Oh, no, the pot boiled over.
[1098.06 --> 1100.22]  Oops, I accidentally counted myself twice in the census.
[1100.72 --> 1102.32]  Or I didn't fill out my address.
[1102.58 --> 1106.50]  Or now I've got two people or a person who lives at this address or a typo.
[1107.18 --> 1107.38]  Crap.
[1107.70 --> 1109.12]  Now that's a very messy data set.
[1109.12 --> 1110.60]  So open data can be a problem.
[1110.98 --> 1113.14]  Let's go to like the practical application of this.
[1113.46 --> 1117.90]  If you are working in open data, or you are interested in getting more involved in open
[1117.90 --> 1122.20]  data, one of my favorite sources is like, if you're publishing a story, making tutorials,
[1122.36 --> 1125.54]  making content, put your data out there and put how you processed it.
[1125.94 --> 1129.18]  And it's not just like one thing to put like your data out there, but also how you processed
[1129.18 --> 1129.48]  it.
[1129.48 --> 1133.76]  In journalism, you have this phrase, how you frame the story is how the story or is how
[1133.76 --> 1134.64]  you tell the story.
[1135.94 --> 1141.44]  Leaving out details, context, or even how you came across the source can influence how the
[1141.44 --> 1142.22]  story comes across.
[1142.22 --> 1143.18]  Yeah, for sure.
[1143.18 --> 1148.20]  And that's, we see it especially evident in data-driven journalism and solutions journalism,
[1148.20 --> 1150.02]  which is interesting.
[1150.02 --> 1153.20]  And like, it's also can be really damaging to trust and reputation.
[1153.20 --> 1155.30]  But I think ML runs the same risk right now.
[1155.30 --> 1158.58]  If we're not transparent of here's how I prepared the data set.
[1159.04 --> 1160.74]  Here's how I trained an annotator.
[1160.74 --> 1162.84]  Or here's the tools that I used.
[1162.84 --> 1164.78]  Or here's how I obtained the data in the first place.
[1164.78 --> 1170.80]  Yeah, and like you were saying, the certain things like how you give instructions to a
[1170.80 --> 1176.12]  data annotator or how you set up your prompt, that has such an influence on the downstream
[1176.12 --> 1177.48]  performance of these things.
[1177.58 --> 1182.72]  But it's very frequently, I've definitely found like the instructions you give data annotators
[1182.72 --> 1188.48]  is something very often left out of the story of how people tell like what they did, right?
[1188.54 --> 1191.72]  It's like, oh, we gathered this data with these labels.
[1192.30 --> 1192.62]  Okay.
[1192.62 --> 1198.38]  Well, I can imagine like my own set of instructions for getting those labels, but it could result
[1198.38 --> 1204.50]  in a totally different thing that's happening, like all sorts of biases and other things
[1204.50 --> 1205.38]  that go into that.
[1205.70 --> 1208.10]  So, I mean, well, I have a perfect case example of this.
[1208.50 --> 1212.62]  In January, we met many of the team members at Hartex and Label Studio met up.
[1213.18 --> 1218.18]  Basically, we got our entire, you know, customer success and sales team and, you know, the community
[1218.18 --> 1222.60]  side of things and a bunch of our support engineers to all sit together and like,
[1222.60 --> 1224.64]  we had a data labeling competition for fun at the end.
[1224.78 --> 1229.00]  And I had just finished like, how did you get started with data labeling and like best practices?
[1229.10 --> 1230.26]  And I was like, easy.
[1230.68 --> 1232.14]  Like, I'm going to kick all of your butts.
[1232.22 --> 1237.22]  Like, I was totally going in like hot shit and everything and like thinking, well, I sped through.
[1237.40 --> 1238.20]  I was like, whatever.
[1238.70 --> 1238.98]  Next.
[1239.24 --> 1239.46]  Great.
[1239.64 --> 1239.86]  Done.
[1239.86 --> 1242.90]  And I like sped through because I was like, speed was a metric, but also accuracy.
[1243.28 --> 1245.08]  Well, I sped through this thing because I was like, whatever.
[1245.20 --> 1245.92]  I'm going to ace this.
[1246.04 --> 1247.12]  I know the keyboard shortcuts.
[1247.68 --> 1249.18]  Like my systems are set up.
[1249.94 --> 1251.68]  I had the lowest accuracy score, everybody.
[1251.80 --> 1253.76]  My data was all, I was like, you failed there.
[1253.80 --> 1257.88]  And it was like, I was like, man, I'm going to go embarrass myself right now after all that
[1257.88 --> 1258.74]  crap I just talked.
[1259.80 --> 1260.08]  Yeah.
[1260.24 --> 1260.54]  Yeah.
[1260.54 --> 1263.54]  I think that's the other thing.
[1263.90 --> 1268.42]  Like, I don't know if you have any encouragement here, but like data scientists out there who
[1268.42 --> 1272.38]  have not like actively participated in like the data labeling process.
[1272.60 --> 1277.38]  I think, yeah, that's like such a learning experience because like it gives you perspective,
[1277.38 --> 1282.48]  even if in the future, like you're not part of one of those processes, it gives you good
[1282.48 --> 1283.56]  questions to ask.
[1284.26 --> 1288.92]  If like, oh, someone gives you this data set that was labeled, you should probably ask a
[1288.92 --> 1291.60]  few follow-up questions about like, how did that go?
[1291.76 --> 1292.84]  What did you do there?
[1293.16 --> 1296.76]  Well, in academic research, you actually have to disclose things like, did you pay your
[1296.76 --> 1299.68]  annotators or how did you prepare the annotators when you're doing research?
[1299.68 --> 1304.24]  Because that can put so much of a bias on a model that is built off of that data.
[1304.60 --> 1308.94]  And that academic, like you can't get peer-reviewed studies done without disclosing that information.
[1308.94 --> 1310.46]  It's part of data ethics now.
[1311.08 --> 1314.92]  And one of the biggest things, and we don't talk about it enough, is how do you pay your
[1314.92 --> 1317.36]  annotators or do you outsource your annotators?
[1317.36 --> 1319.52]  Which isn't saying that's a bad thing to do.
[1319.60 --> 1323.22]  But again, we have to remember that so many of these models, and I see it, like I think
[1323.22 --> 1327.30]  a lot of it times, it actually is probably, I'm going to guess here, I don't know, but
[1327.30 --> 1331.74]  I would be even wondering if these smaller models that are generated because they're generated
[1331.74 --> 1337.44]  at home or people dorking around on their computer, they might even have more bias because
[1337.44 --> 1338.74]  we're not trading an annotator.
[1338.88 --> 1342.48]  Like I know when I'm goofing around with my naked and afraid data set, I'm not annotating.
[1342.48 --> 1348.26]  Like I'm playing some 30 second goofing around stuff and watching YouTube videos, just seeing
[1348.26 --> 1348.82]  what's out there.
[1349.04 --> 1351.42]  I'm not doing the work, which is a problem.
[1352.16 --> 1352.28]  Yeah.
[1352.46 --> 1355.86]  I guess kind of bringing things full circle a little bit.
[1355.92 --> 1361.14]  Like we started talking about like some of these like players and MO ops and sort of the
[1361.14 --> 1362.68]  ops around this process.
[1362.92 --> 1366.66]  We talked about human feedback, reinforcement learning.
[1366.66 --> 1368.30]  We talked about open data.
[1368.98 --> 1375.08]  What excites you about like the trends that we're seeing and what impact they could have
[1375.08 --> 1377.52]  on our industry moving forward?
[1377.98 --> 1382.80]  Maybe that's related to like people that weren't able to like participate in this process before,
[1382.92 --> 1386.80]  the tooling's better so they can, or maybe it's something totally different like around
[1386.80 --> 1389.56]  like tasks or other things that you see like in the future.
[1389.72 --> 1394.78]  Like what are you personally excited about like looking forward as you bring this stuff together?
[1394.78 --> 1398.06]  Well, first off, I've been really impressed with like what the Hugging Face team is doing.
[1398.14 --> 1399.12]  I noticed the Hugging Face shirt.
[1399.54 --> 1401.34]  The Hugging Face spaces have been amazing.
[1401.56 --> 1405.34]  We do have a label studio, a Hugging Face space, but the ability to get up and going in
[1405.34 --> 1407.02]  the browser has been super awesome.
[1407.30 --> 1411.68]  And there is a talk I went to at PyData Berlin that's running Streamlite.
[1411.78 --> 1415.52]  So they're running entirely Python based models right in the browser and tools.
[1415.66 --> 1419.76]  I think there's a, it's binders, I believe is another tool that's doing another, again,
[1419.76 --> 1424.68]  very similar to notebook processing all in the browser, makes it more accessible than ever before.
[1425.58 --> 1430.96]  And it's just really exciting, especially as like, I love that we have more people interested
[1430.96 --> 1436.00]  in this industry, but it's also not only the interest, but the tools to do it correctly
[1436.00 --> 1436.90]  and ethically.
[1437.26 --> 1441.20]  And again, jumping on my soapbox here, this is why the open data is so important.
[1441.20 --> 1446.50]  So putting when we can, putting our sources, our references, building in the public, building
[1446.50 --> 1450.76]  an open source and making kind of a almost, I don't want to say a paper trail, but like a
[1450.76 --> 1454.56]  show your work sort of process is really important for the future.
[1454.78 --> 1455.26]  Yeah.
[1455.50 --> 1455.84]  Awesome.
[1455.96 --> 1456.42]  That's great.
[1456.84 --> 1461.62]  And as we kind of close out here, where can people find you online?
[1461.66 --> 1467.52]  And also tell us a little bit about your own podcast, which sounds awesome and like includes
[1467.52 --> 1468.10]  pickles.
[1468.50 --> 1468.80]  Yeah.
[1468.80 --> 1476.96]  So I am available online at Aaron McHale on all the platforms or Aaron.bio has a link
[1476.96 --> 1478.00]  to everything that I'm at.
[1478.08 --> 1480.52]  You can also chase me down at label studio.
[1480.68 --> 1487.02]  So it's label studio, but the last.io is like a things join the community, come hang out
[1487.02 --> 1487.44]  with me there.
[1487.52 --> 1490.60]  We have an open coming upcoming town hall and getting into more workshops.
[1490.60 --> 1492.70]  Um, so very excited about that.
[1492.90 --> 1495.86]  I also run the dev relish podcast.
[1496.00 --> 1500.08]  So it's everything about dev rel and ish.
[1500.38 --> 1503.06]  Also, you know, naturally, um, some people made sourdough bread.
[1503.12 --> 1504.24]  I got into fermentation.
[1504.90 --> 1510.42]  We got a fun pickle fact and cool pickle logos because you got to relish the developer moments.
[1510.68 --> 1511.82]  Well, I open source.
[1512.28 --> 1512.44]  Yeah.
[1513.40 --> 1516.58]  I, this was definitely not a sour experience.
[1516.78 --> 1518.20]  I've, I've relished it very much.
[1518.20 --> 1520.54]  Uh, thank you so much for joining, uh, Aaron.
[1520.64 --> 1524.72]  It's been a great pleasure to talk to you and looking forward to, uh, following up with
[1524.72 --> 1526.52]  all the cool community stuff you got going on.
[1526.74 --> 1530.10]  Again, people check out the show notes and, uh, thank you so much.
[1530.24 --> 1531.12]  Thank you so much.
[1531.16 --> 1534.32]  This was a, quite a big deal that we had going on here.
[1534.86 --> 1535.46]  Good one.
[1535.62 --> 1535.90]  Good one.
[1545.28 --> 1547.88]  Thank you for listening to practical AI.
[1548.20 --> 1552.00]  Your next step is to subscribe now, if you haven't already.
[1552.42 --> 1557.08]  And if you're a longtime listener of the show, help us reach more people by sharing practical
[1557.08 --> 1558.48]  AI with your friends and colleagues.
[1558.92 --> 1563.84]  Thanks once again to Fastly and Fly for partnering with us to bring you all Change Talk podcasts.
[1564.42 --> 1568.22]  Check out what they're up to at Fastly.com and Fly.io.
[1568.62 --> 1573.22]  And to our Beat Freakin' Residence Breakmaster Cylinder for continuously cranking out the best
[1573.22 --> 1573.94]  beats in the biz.
[1574.22 --> 1575.12]  That's all for now.
[1575.42 --> 1576.54]  We'll talk to you again next time.
[1578.20 --> 1580.20]  Okay.
[1580.30 --> 1592.58]  Bye.
