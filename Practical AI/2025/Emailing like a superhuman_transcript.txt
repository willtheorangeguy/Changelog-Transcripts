[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.46 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[26.32 --> 28.36]  Thanks to our partners at Fly.io.
[28.36 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.38]  Learn how at Fly.io.
[44.56 --> 48.60]  Welcome to another episode of the Practical AI podcast.
[49.16 --> 50.78]  This is Daniel Whitenak.
[50.88 --> 57.16]  I am CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who
[57.16 --> 60.84]  is a Principal AI Research Engineer at Lockheed Martin.
[61.14 --> 61.78]  How are you doing, Chris?
[61.90 --> 62.92]  Doing very well.
[63.00 --> 67.18]  Looking forward to talking some fun stuff on this beautiful spring day.
[67.96 --> 69.20]  Yes, yes.
[69.30 --> 76.04]  Well, I've always hoped that AI could make me a superhuman.
[76.04 --> 84.92]  I'm so really excited to hear about maybe something in that realm today from Loic Ossie, who is
[84.92 --> 86.70]  head of engineering at Superhuman.
[86.90 --> 87.60]  How are you doing, Loic?
[87.98 --> 88.78]  I'm doing great.
[88.92 --> 90.98]  I'm super excited to chat with you guys.
[91.20 --> 95.42]  And I would say with a pretty humbling, I would say, set of guests in the past.
[95.60 --> 99.84]  So I'm super happy to have this opportunity and discuss in length.
[99.84 --> 101.48]  Yeah, that's awesome.
[101.62 --> 108.44]  Well, I know this is kind of interesting because I know Superhuman, I think, is one of maybe
[108.44 --> 116.48]  this sort of first really integrated AI first kind of engineering tools that I remember seeing.
[117.06 --> 121.12]  And of course, the AI space has advanced a lot in that time.
[121.12 --> 129.06]  Maybe could you give us a little bit of a kind of state of AI in email or productivity more
[129.06 --> 130.38]  broadly, if you want to think about that.
[130.46 --> 133.68]  But really, I mean, obviously, we're going to talk a lot about email and messaging.
[134.44 --> 139.76]  So could you give us a little bit of a sense of what that landscape looks like right now
[139.76 --> 141.72]  and kind of how Superhuman fits into that?
[141.92 --> 142.36]  Yeah, totally.
[142.62 --> 146.20]  And it's incredible, like the time that we're living right now.
[146.20 --> 152.70]  Of course, like everyone has been shocked, like when we had like the first version of
[152.70 --> 160.36]  those LLMs, like doing some crazy, crazy stuff and like analyzing text, summarizing and doing
[160.36 --> 162.48]  like all sorts of magic.
[163.04 --> 166.76]  And of course, email, I mean, is all text-based for the most part.
[167.38 --> 174.40]  And so it was like a really nice testbed, like to try out, like all the cool stuff that you
[174.40 --> 174.96]  can do.
[174.96 --> 182.16]  And interestingly, that's also like helped like this category, like the email client to
[182.16 --> 184.28]  thrive, like for quite some time.
[185.12 --> 189.96]  Superhuman was almost the only one supercharging Gmail and Outlook.
[190.08 --> 195.46]  We were the only one on the space making like people faster going through their emails and
[195.46 --> 195.84]  all of that.
[196.14 --> 201.00]  And with the rise of LLM and agents and everything, now there's a bunch of people are like, oh,
[201.00 --> 206.76]  damn, this is like a great, great, great environment to play around and to make like things better.
[207.42 --> 208.88]  And right now, this is what we see.
[209.28 --> 215.24]  We see like a bunch of, I would say, other like tools trying to do stuff with LLM and to
[215.24 --> 219.88]  create like a better experience for email.
[219.88 --> 227.08]  And this is indeed like an interesting time for us because this is the proof that that category
[227.08 --> 231.64]  needs to exist, was existing before, but we are the only ones there.
[231.84 --> 235.94]  And now like more and more people are getting there showing that there's deep interest in it.
[235.94 --> 241.74]  And, and it's challenging and it's like a super interesting and it will probably talk about
[241.74 --> 246.20]  it, but it will also like help us understand what makes like a good product.
[246.20 --> 251.18]  And is like just the LLM and AI sufficient or like, do you, do you need some sort of like
[251.18 --> 253.14]  a secret sauce on top of it?
[253.20 --> 255.46]  And I'm happy to discuss about it.
[255.72 --> 261.46]  As you, I'm kind of curious following up on, on what Daniel was saying with, you know, with
[261.46 --> 268.26]  you guys being so early into the space and, and obviously we're, you know, the, not only
[268.26 --> 273.20]  LLMs, but just AI in general has been going at light speed, you know, increasing steadily
[273.20 --> 274.36]  over that time period.
[274.74 --> 279.60]  How is that, how is the, the space change for you guys from being kind of the early only
[279.60 --> 286.70]  player, you know, into, into the space where there's others, you know, it's becoming, you
[286.70 --> 290.58]  know, somewhat congested across, not just the space you're in, but just like everything.
[290.58 --> 295.94]  How has that changed the world for you guys in terms of, of staying differentiated and
[295.94 --> 296.38]  all that?
[296.94 --> 297.10]  Yeah.
[297.28 --> 301.52]  So, so it's very interesting because like there's multi-dimensions that we can talk about.
[301.62 --> 307.90]  Like the, the, the first one is this is like the, the, the raise of those AI features and
[307.90 --> 313.44]  capabilities are bringing like a new set of features that you can implement that you couldn't
[313.44 --> 314.08]  do in the past.
[314.18 --> 320.26]  In the past AI was mostly classification, like adding labels and, and stuff like this.
[320.26 --> 324.60]  And that was kind of like the limit of what AI could do really for everything that is
[324.60 --> 325.62]  text-based.
[325.86 --> 329.88]  So typical classifiers, typical models like this.
[330.52 --> 333.92]  And more and more now you can do like some intelligent stuff.
[333.92 --> 341.62]  So we moved from a place where we were making things faster for our users compared to Outlook,
[341.78 --> 342.48]  compared to Gmail.
[342.48 --> 342.56]  Gmail.
[343.90 --> 351.70]  But now there's like more that we can do so we can make things smarter, which is probably
[351.70 --> 355.70]  like a paradigm shift in terms of like the value that we're creating for our users.
[356.52 --> 360.82]  The other dimension is like, this is raising the expectations for, I would say, the different
[360.82 --> 361.22]  users.
[362.14 --> 365.66]  Like for a long time, they were like, damn, this is so fast.
[365.66 --> 369.06]  And I'm winning like four hours a week to go through my emails.
[369.28 --> 371.96]  But like everyone is used to chat with GPT.
[372.18 --> 374.10]  Everyone is used to perplexity.
[374.24 --> 379.30]  Everyone is like crafting images or like even movies with Sora and all of that.
[379.60 --> 384.52]  So like the level of awareness and the level of understanding of what the technology can
[384.52 --> 387.10]  do is raised dramatically.
[387.60 --> 392.30]  So for our users, the level of expectations like, hey, superhuman, I expect this now.
[393.02 --> 393.86]  I expect this now.
[393.86 --> 399.20]  The other dimension is like from an engineering standpoint and like a building standpoint,
[399.50 --> 401.32]  our tool set is totally different.
[401.84 --> 403.26]  Like the tools have changed.
[403.58 --> 409.06]  And engineers that were working like in some ways three years ago, even two years ago, even
[409.06 --> 414.54]  six months ago, like right now, the tool set and like your flow and like all your setup
[414.54 --> 417.74]  to work has dramatically changed.
[417.74 --> 426.42]  And maybe like the last dimension that I think is like really tricky to apprehend is the perceived
[426.42 --> 426.86]  quality.
[427.76 --> 433.98]  So superhuman was seen and built on the kind of like the one single dimension that was
[433.98 --> 435.38]  like it's highly qualitative.
[436.38 --> 439.72]  We were in charge of the quality because we master everything.
[439.72 --> 442.64]  So you can be like have like a zero bug policy.
[442.86 --> 446.28]  You can take the time to deliver the value, but it needs to be perfect.
[447.08 --> 452.86]  And now with LLMs, a bunch of the perceived quality depends on your prompt.
[453.40 --> 460.08]  So you have users that are prompting with different skills or different level of skills and the outcome
[460.08 --> 464.24]  of that prompt may be perceived as low quality.
[464.24 --> 466.62]  But that's something that is really hard to control.
[467.10 --> 471.02]  And it's creating like something that is like sort of like mind blowing from an engineering
[471.02 --> 471.52]  standpoint.
[472.08 --> 477.30]  I mean, we've all been working in tech and the craft, the bugs and everything.
[477.44 --> 479.28]  There are some processes to limit the number of bugs.
[479.62 --> 481.72]  But now quality is not only bugs.
[482.46 --> 486.20]  Like it's also like this perceived quality based on the user.
[486.60 --> 490.42]  And that's an interesting thing to do, interesting thing to tackle.
[490.42 --> 498.02]  And I'm curious as you kind of mentioned the fact that with some of the prompts and having
[498.02 --> 502.30]  different users, you know, skill level and stuff like that, could you talk a little bit
[502.30 --> 506.04]  about kind of how you tackle?
[506.30 --> 511.50]  This is one of those interesting things from my standpoint to hear about where there's all
[511.50 --> 516.94]  these little gotchas in this world that a typical person isn't going to ever have thought
[516.94 --> 517.90]  about going ahead of time.
[517.90 --> 523.86]  And so as one of those things where prompting itself is fairly diverse in terms of the skill
[523.86 --> 527.80]  set, can you talk a little bit about like, how do you deal with that when you're trying
[527.80 --> 532.44]  to put together a product and focusing on the quality issues and stuff like that?
[532.62 --> 536.36]  Because I'll be honest with you, that would not have occurred to me to have to think about
[536.36 --> 537.80]  addressing that kind of issue.
[537.88 --> 539.04]  Can you talk a little bit about that?
[539.32 --> 544.82]  You know, it's I will tell you like about one specific feature that we released in Q1.
[544.82 --> 547.34]  So we have those auto labels.
[547.78 --> 552.94]  So automatic labels that will basically flag your emails.
[553.28 --> 557.32]  And based on the label, you can decide to skip your inbox altogether.
[557.72 --> 564.38]  Typical stuff like random pitches from a company that want to get in touch with you to sell their
[564.38 --> 564.70]  product.
[565.36 --> 569.16]  I receive like probably like 30 of them every day.
[569.16 --> 573.58]  Do I want to take a look at those like 30 and answer like all of that?
[573.74 --> 574.36]  Probably not.
[575.22 --> 575.86]  Probably not.
[576.08 --> 579.36]  So I'd love them to basically like be skipped altogether.
[579.58 --> 585.62]  So for those, we build classifiers that do not rely on user prompts so that we control
[585.62 --> 589.78]  the quality, precision, recall, like the typical stuff.
[589.78 --> 596.30]  But we also allow our users to create and craft their own labels.
[597.00 --> 603.80]  Let's say like you want to have like, oh, I want all my podcast invitation to have the
[603.80 --> 604.48]  same label.
[604.70 --> 609.64]  But like you cannot just have like a deterministic rule to say because I don't know all the podcast
[609.64 --> 611.54]  like people and everything.
[611.66 --> 616.58]  So you cannot just do like the filter like Gmail would do where you say like if then,
[616.64 --> 617.02]  then this.
[617.02 --> 623.06]  So you have to prompt it and you have to basically allow the user to craft a prompt that will
[623.06 --> 624.36]  surface all of those.
[625.44 --> 630.18]  But then that prompt is tricky because like if you have someone that is just like putting
[630.18 --> 636.92]  just a one-liner, you start having like some issues because the precision and recall based
[636.92 --> 639.44]  on the one-line prompt is not great.
[639.44 --> 644.52]  And we know like as you, I would say, I guess your audience have been working with like
[644.52 --> 647.22]  chat GPT or like prompts in general.
[647.78 --> 651.70]  The more structured and extensive they are, the better the result.
[652.28 --> 656.82]  And there's a bunch of hallucinations that can happen if you are like just one-liner because
[656.82 --> 659.94]  lack of context and lack of all of that.
[659.94 --> 667.44]  So of course, you do like some like system prompt to basically surround this user prompt to try
[667.44 --> 671.20]  to avoid like too much issues.
[671.72 --> 675.14]  But there's also like a part of education that you need to have.
[675.20 --> 679.34]  And we're working on this now, which is like, huh, your prompt seems interesting, but like
[679.34 --> 681.26]  probably you want to structure it that way.
[681.26 --> 685.20]  So there's some stuff like this that we will be working on.
[685.46 --> 691.46]  Also sharing prompts, like libraries of prompts is something that we're thinking about more and
[691.46 --> 695.66]  more because not everyone is able to craft a nice prompt.
[695.74 --> 700.70]  And maybe someone in your team will have done like a prompt that you would really use happily
[700.70 --> 702.34]  if you get access to it.
[702.76 --> 705.94]  So it's sort of like, I mean, it's very product centric.
[706.02 --> 707.56]  So it's not AI centric.
[707.56 --> 709.74]  And you need to work around this new problem.
[710.46 --> 714.86]  And I wish we'd have a civil bullet and like the answer to that problem.
[715.06 --> 718.02]  But I think we are like learning as we walk.
[719.16 --> 720.36]  But it's super interesting.
[720.76 --> 725.94]  I'm wondering, like, I'm always intrigued by, I read a book by Richard Hamming.
[726.06 --> 732.46]  And one of the things that he talks about is how if you rethink a process that was very human
[732.46 --> 738.08]  and manual before, often the way that you would make that an augmented or machine driven process
[738.08 --> 742.76]  is very different from what the original human process would look like.
[742.84 --> 748.44]  And I think in the email client, we all sort of expect a certain process, a look and feel
[748.44 --> 750.82]  to the email client that's developed over time.
[751.34 --> 759.46]  What have you found in terms of like presenting an email client to a user that is drastically different?
[759.46 --> 761.82]  What sort of needs to be preserved?
[762.12 --> 764.94]  What's kind of up for grabs in that experience?
[765.52 --> 767.50]  What should stretch the user?
[767.82 --> 769.22]  What needs to be preserved?
[770.28 --> 771.72]  You know, how do you think about that?
[772.38 --> 773.80]  That's really interesting.
[774.06 --> 779.02]  That's a really interesting point because we are at that moment where the user interaction
[779.02 --> 783.52]  with the computer, with the system is like dramatically changing.
[783.52 --> 788.22]  Like, people don't expect to click in different windows anymore.
[788.92 --> 790.56]  Like, the expectation is different.
[790.72 --> 796.32]  Like, ChatEPT or the other, like, clones, like, from, like, different providers.
[796.80 --> 799.18]  You basically have a chat box and you ask everything there.
[799.26 --> 803.12]  Like, even if you're working on a document, you ask on the chat box and, like, oh, modify
[803.12 --> 806.20]  my document and rewrite my exact summary.
[806.56 --> 809.46]  Oh, make my tone a bit more like X and Y and Z.
[809.46 --> 814.36]  You don't expect to have, like, a button like Word would have, like, Microsoft Word back
[814.36 --> 814.88]  in the days.
[815.40 --> 819.48]  So, and we are only at the beginning of this shift.
[819.76 --> 824.88]  So, I think that, and it's kind of like coming back to, like, competition and all of that.
[825.00 --> 829.48]  The barrier to entry to, like, pretty much any SaaS application or, like, even a consumer
[829.48 --> 835.24]  application is very low now because it's very easy to, at least to build a POC.
[835.62 --> 836.72]  At least to build a POC.
[836.72 --> 840.62]  I wouldn't go, like, further than that.
[841.12 --> 845.40]  And what will make the difference is the product test and how you want to understand your users
[845.40 --> 847.22]  and how you understand their user interaction.
[847.78 --> 854.72]  And this is where, like, I feel pretty proud to work at Superhuman because our CEO is a
[854.72 --> 857.90]  freak in terms of, like, user interaction and vision.
[858.32 --> 863.16]  And he's already thinking about that and, like, how the future of interaction will be.
[863.16 --> 866.14]  And it will change.
[866.56 --> 867.34]  It will be different.
[867.78 --> 869.06]  So, like, what will stay?
[869.42 --> 872.74]  What will be slightly different?
[873.06 --> 881.00]  I'm pretty sure that the conversational aspect would be a strong paradigm.
[881.68 --> 883.28]  Like, right now, you don't talk.
[883.28 --> 888.24]  Whether it is, like, through your keyboard or through a mic, you don't really talk to your
[888.24 --> 888.54]  system.
[888.68 --> 889.98]  You don't talk to the application.
[890.66 --> 894.42]  Maybe you start talking with ChatGPT because they have this nice voice interaction.
[894.94 --> 900.78]  Maybe you use Whisperflow or, like, this type of tools to basically write your email or, like,
[900.84 --> 903.22]  write in Slack and your messages.
[903.22 --> 909.86]  But you're not exactly commanding the device to do things as you talk just yet.
[910.04 --> 911.76]  But more and more people are doing so.
[912.14 --> 917.88]  Like, I probably talk to my computer now more than I type, interestingly.
[918.88 --> 920.20]  So, there's a change.
[920.70 --> 924.82]  And everything that we've done in the past was mostly click and click and click.
[924.82 --> 932.68]  Superhuman started with, like, the common key and keyboard-centric access to things for
[932.68 --> 936.90]  people that wanted really productivity because, like, switching, like, with a mouse is, like,
[937.44 --> 938.48]  it's pretty slow.
[938.72 --> 942.16]  And now, more and more people are starting to engage with the voice.
[942.52 --> 946.86]  So, all of that will change the way you think, the way you surface the data, the way you interact
[946.86 --> 949.10]  with the data, the way you bring the focus.
[949.68 --> 953.52]  So, this is an interesting, I would say, area.
[953.52 --> 953.60]  Yeah.
[953.80 --> 959.76]  One thing that I do believe will stay, though, to your point, Daniel, and I would talk about
[959.76 --> 964.32]  email especially, the concept of inbox, like, the concept of having, like, some sort of,
[964.36 --> 968.62]  like, a timeline of things that you need to go through and get rid of the stuff that are
[968.62 --> 973.48]  top of mind, some sort of, like, a task list to some extent will stay.
[973.98 --> 980.90]  Now, how it will be surfaced, how you will go through it will dramatically change over time.
[980.90 --> 982.74]  And we're already, like, seeing this.
[983.52 --> 999.36]  Okay, friends.
[999.48 --> 1002.90]  Build the future of multi-agent software with Agency.
[1003.18 --> 1005.10]  A-G-N-T-C-Y.
[1005.58 --> 1010.82]  The Agency is an open source collective building the internet of agents.
[1010.82 --> 1016.20]  It is a collaboration layer where AI agents can discover, connect, and work across frameworks.
[1016.66 --> 1021.98]  For developers, this means standardized agent discovery tools, seamless protocols for inter-agent
[1021.98 --> 1028.54]  communication, and modular components to compose and scale multi-agent workflows.
[1029.18 --> 1036.18]  Join Crew AI, Langchain, Lambda Index, Browser Base, Cisco, and dozens more.
[1036.18 --> 1041.06]  The Agency is dropping code, specs, and services.
[1041.48 --> 1043.14]  No strings attached.
[1043.56 --> 1048.26]  You can now build with other engineers who care about high-quality multi-agent software.
[1048.78 --> 1051.76]  Visit agency.org and add your support.
[1052.12 --> 1055.88]  That's A-G-N-T-C-Y dot org.
[1055.88 --> 1068.52]  So, as we were kind of going into the break, we were talking about kind of, you know, the notion of rethinks of that.
[1068.52 --> 1084.80]  And I'm kind of curious, as you're thinking about not only like the rethinks, but you're also having to respond to the evolution of the technology itself that's available for your teams to implement stuff.
[1084.80 --> 1090.94]  And one of the things that we've seen over time is kind of, you know, it's not this smooth increase.
[1091.06 --> 1100.56]  You may have evolutionary increase in the model capabilities for a bit, but you also have these jumps that'll occur along the way.
[1100.56 --> 1116.14]  And with your product teams, as you're looking at, like, what the future of your products are going to be, and you hit these moments where it kind of goes from, you know, predictable improvement in the models and you make these jumps.
[1116.66 --> 1130.36]  How does that affect the product development cycle that you have internally when you're saying, are those moments, you know, as we were talking about rethinks, do you have moments where you kind of go, maybe it's time for kind of a deliberate rethink because something just happened?
[1130.36 --> 1134.48]  In terms of the technology capability that we weren't expecting last week.
[1135.04 --> 1136.02]  And we're going to do that.
[1136.12 --> 1140.06]  How do you guys handle this kind of an industry being in it for that?
[1140.48 --> 1141.40]  No, it's interesting.
[1141.68 --> 1149.96]  And so, Daniel, you were mentioning a book, but one book that comes to mind as you're asking this question is Zone to Win by Joe Fremur.
[1150.38 --> 1153.60]  And it talks about like continuous innovation and like disruptive innovation.
[1154.16 --> 1156.06]  And this is probably what we're talking about.
[1156.06 --> 1162.62]  Like we continuously innovate and we continuously add more features and new stuff into the product.
[1162.62 --> 1174.10]  And sometimes you have this opportunity to provide something that is disruptive, whether it is like the underlying technology that is disruptive or because you have like some sort of a wow moment.
[1174.10 --> 1182.52]  And you have like someone, I would say with a vision that is like, this is the duration to take and we need to either pivot or we need to do something like drastically different.
[1182.90 --> 1191.22]  What we've seen, especially with AI, is like the rate of those disruptive innovation is mind blowing.
[1191.22 --> 1203.56]  I would say before AI to some extent, like the technical innovation where maybe once a year, once every two years, like you have something that is like brand new and like, holy shit, I need to use this.
[1203.70 --> 1204.44]  And pardon my French.
[1204.96 --> 1214.30]  But what is interesting with like LLMs, like every two weeks or three weeks, if you're not on Twitter, you're not on Hacker News, like you can miss like the new big stuff.
[1214.30 --> 1222.54]  Like LLM, like multimodals, reasoning, MCPs, like that came in six months.
[1223.18 --> 1228.90]  And all of that is coming with like a new set of capabilities that you can decide to implement in your product.
[1229.34 --> 1233.50]  So to come back on your question, what is the impact on the product development?
[1233.76 --> 1234.70]  How do you handle this?
[1236.00 --> 1240.26]  One, you better be agile, meaning like the true agile.
[1240.26 --> 1245.82]  So you better be able to stop what you do and say, wow, focus.
[1246.10 --> 1248.40]  We need to sit down for a moment because this is coming.
[1248.56 --> 1249.60]  What do we do about it?
[1250.20 --> 1259.86]  And you need to have like, and that's why I love like small companies to some extent, because it's very easy to have like everyone, listen, there's this new thing.
[1260.12 --> 1261.32]  We need to do something about it.
[1261.68 --> 1263.14]  Let's change the roadmap right now.
[1263.14 --> 1275.32]  When you're in a bigger company, it's way harder to do it because you have your yearly planning that is like coming into quarterly planning and you have all those OKRs that you need to report on and everything.
[1275.60 --> 1282.70]  So like you need basically like almost a six month business plan to explain why you want to pivot and do something else, which is obviously not the case.
[1282.70 --> 1297.36]  Where you're a company that is of a small size, superhuman engineering and product and design is probably like, I don't know, I don't have the strict number, but like 40, 40, 60, maybe 50.
[1298.04 --> 1299.10]  But that's about it.
[1299.36 --> 1302.48]  That's the size where you can be like super agile.
[1302.66 --> 1307.84]  You can stop everyone doing something because something is coming up and we need to focus on it.
[1308.24 --> 1309.30]  Of course, we can do better.
[1309.30 --> 1314.40]  If my engineers are listening to this podcast, they would say, look, maybe you're like caricaturing a bit.
[1314.86 --> 1316.68]  So probably I'm caricaturing a bit.
[1316.70 --> 1317.90]  And of course they are, right?
[1318.10 --> 1318.36]  I mean.
[1318.42 --> 1319.26]  And of course they're right.
[1319.32 --> 1320.62]  Of course they're listening to it.
[1321.08 --> 1322.68]  And of course they're listening to it.
[1323.08 --> 1323.18]  No.
[1323.34 --> 1329.36]  So it's having this understanding that everything is changing right now.
[1329.76 --> 1334.50]  So you need to reassess your priorities like almost every two weeks, almost every two weeks.
[1335.28 --> 1336.10]  MCP is coming.
[1336.58 --> 1338.56]  People are standardizing on it right now.
[1338.56 --> 1340.00]  What do we do with it?
[1340.42 --> 1341.14]  What do we do with it?
[1341.38 --> 1343.16]  Should we invest like crazy?
[1343.60 --> 1345.20]  Should we stop everything that we're doing?
[1345.76 --> 1349.80]  Should we, I would say, do we still believe in the vision and it's providing more value?
[1349.98 --> 1352.12]  You need to make those decisions every two weeks.
[1352.54 --> 1354.26]  So, or like almost every week.
[1354.50 --> 1364.14]  So being close to, I would say, a close-knit team that is talking like basically on a daily basis to make sure that you're making the right decision is key.
[1364.14 --> 1364.98]  It's key.
[1365.12 --> 1369.02]  And by the way, just for listeners, you may have heard MCP in there.
[1369.02 --> 1372.84]  If we did an episode explaining what MCP is.
[1372.84 --> 1378.28]  So anyone who's not familiar with it, you should jump back a few episodes and hear that out.
[1378.44 --> 1380.18]  It'll give you some context around that.
[1380.64 --> 1380.78]  Yeah.
[1381.06 --> 1381.32]  Thanks.
[1381.38 --> 1381.80]  Thanks, Chris.
[1381.88 --> 1384.06]  And I'm sorry if I use, I would say, some jargons.
[1385.42 --> 1386.10]  Jargon's fine.
[1386.10 --> 1388.84]  We always try to jump in and point people to it.
[1389.50 --> 1390.34]  This is perfect.
[1390.62 --> 1391.24]  This is perfect.
[1391.48 --> 1403.04]  And I think kind of looking forward, one of the things that I'm really curious about is we've kind of tackled some of the bigger issues of AI and email.
[1403.04 --> 1420.16]  But I'm kind of curious, you know, if we dive down into specific functionality at Superhuman, you know, what, how do you see kind of the most, maybe the most useful AI email functions that you're currently either kind of releasing or kind of thinking about forward?
[1420.38 --> 1425.60]  You know, how do you, when you get kind of granular on the product, how are you starting to think about that now?
[1425.60 --> 1435.46]  The, I would just like, like the feature that all our users are basically talking about because they just love it is a feature called auto draft.
[1435.66 --> 1438.34]  You receive an email as part of a thread.
[1438.76 --> 1445.96]  Someone is asking you some questions and, or you send an email basically saying like, hey, can we meet next week or whatever?
[1446.34 --> 1448.26]  And after two days, you don't have an answer.
[1448.44 --> 1452.02]  You usually want to bump that into their inbox and everything.
[1452.02 --> 1456.94]  We build this feature where we create those drafts for you ready to be sent.
[1457.98 --> 1461.96]  It's, it's not mind blowing in terms of like usage of LLMs.
[1462.06 --> 1465.82]  Like you provide the context, you use the tone of like you're with that person and everything.
[1466.14 --> 1471.38]  And you craft a draft that could sound like a good way to reply to it.
[1471.60 --> 1474.34]  And the results are just mind blowing.
[1474.34 --> 1481.38]  Like the users find it like so addictive because it's relatively accurate and they win a lot of time.
[1481.38 --> 1483.48]  Like it's just about like winning time.
[1483.74 --> 1490.38]  Our users are mostly CEOs, CXOs on the sales side as well.
[1490.48 --> 1492.10]  Some consultancy firm.
[1492.48 --> 1496.18]  They leave like basically day in and day out like in their emails.
[1496.18 --> 1505.08]  So every 10 seconds that you can make them win in their day is a huge win for them given like the amount of emails that they have.
[1505.48 --> 1511.70]  So this is like one of those features that is super effective, even if it sounds simple.
[1511.70 --> 1527.04]  So like even with what you're just describing there, you know, creating an auto draft per email, you know, maybe an LLM call doing classifications, auto labeling, maybe other calls.
[1527.04 --> 1536.04]  I don't know how many, you know, calls or chains of LLM calls are happening per email, but that could potentially be a lot.
[1536.36 --> 1538.58]  And if you do that for one email, that's fine.
[1538.80 --> 1541.04]  You do that for all my emails, that's more.
[1541.16 --> 1548.18]  If you do that for all emails of thousands or hundreds of thousands of people, that's a lot of Gen AI workload.
[1548.18 --> 1566.18]  How does Superhuman, as more of a AI application company, think about that in terms of optimizing infrastructure or AI, Gen AI use, consumption, you know, hosting your own models, fine tuning your own models, using smaller models?
[1566.74 --> 1568.50]  How do you think through some of that?
[1568.98 --> 1570.64]  So this is a great question.
[1570.76 --> 1576.72]  And this is a real challenge to some extent, if not a problem sometimes.
[1576.72 --> 1587.82]  Indeed, I guess like my engineers are like very much into like the finance, like they understand like the cost of inference, the cost of the input, the cost of the output.
[1588.16 --> 1591.58]  They understand the difference between the different models.
[1592.24 --> 1601.74]  So we had to put some sort of like high level principles to keep moving fast so that they know, I would say, how to default and only like escalate if they have some questions.
[1601.74 --> 1602.74]  I will give you some examples.
[1603.36 --> 1607.58]  But if it's a new feature, we don't know if it will be working or whatever.
[1608.02 --> 1609.38]  So still testing.
[1610.20 --> 1611.72]  We want it to be great.
[1611.92 --> 1613.74]  So we take the most expensive model.
[1614.12 --> 1616.10]  It's working and we have traction.
[1617.04 --> 1617.44]  Great.
[1617.72 --> 1618.98]  Good problem to have.
[1618.98 --> 1622.96]  And now this is the moment where you start thinking about like optimizing the cost.
[1623.44 --> 1627.50]  And maybe you will switch to like a cheaper model, maybe more fine tuned.
[1628.04 --> 1631.88]  Maybe you would switch to like a different type of model altogether.
[1632.44 --> 1635.34]  So, for example, like the classification that we discussed.
[1636.20 --> 1644.18]  LLMs are OK with classifications, but you can have way cheaper for the same quality with like a better type of models.
[1644.76 --> 1647.72]  And inference cost is like a fraction of it, a fraction.
[1647.72 --> 1652.26]  So long story short, this is the way we provide the value to our end users.
[1652.54 --> 1654.64]  We try with the best working.
[1655.22 --> 1657.70]  We do optimization after the fact.
[1658.08 --> 1658.88]  Does that answer your question?
[1659.14 --> 1669.12]  But this is like more generally, I think this is like always like the right approach is like don't care about the cost right now if it's not becoming a problem.
[1669.46 --> 1672.48]  Because you always want to provide like the best experience.
[1672.48 --> 1676.12]  And if you don't have traction, too bad.
[1676.20 --> 1682.20]  Because the risk, if you try to start small because you're afraid of the cost, you will use like a cheaper model.
[1682.72 --> 1684.88]  And the feedback from the users would be meh.
[1685.50 --> 1687.42]  And they won't use your feature.
[1687.70 --> 1693.42]  And then you don't know if it's because the feature is, I would say, not well targeted or if it's because of the model.
[1693.42 --> 1698.38]  So targeting the best, you have like better answers and better insights.
[1698.38 --> 1703.08]  That was a really interesting answer from my standpoint.
[1703.80 --> 1713.28]  You explicitly kind of called out as you're getting to the feature and going ahead and going with the best, the most expensive thing.
[1713.40 --> 1717.62]  And then pulling it back to what the efficiency will be.
[1717.62 --> 1729.12]  And once again, one of the things that we often call out on the show is kind of the fact of kind of software engineering being applied and, you know, kind of the analogies on that on the AI side.
[1729.32 --> 1734.30]  So I just I really wanted to kind of call that out because I thought that was a great insight that you made there.
[1734.30 --> 1735.34]  And it has impact.
[1735.58 --> 1750.20]  So I'm sorry to cut you off, Chris, but like it has like a significant impact on the way you build your application because you want to be able to switch models to switch like the heuristic associated with the output that you want to have.
[1750.20 --> 1762.48]  So you have to invest some time to have like a way to do this switch relatively easily, potentially do A-B testing with different population to measure like the difference of perception.
[1762.66 --> 1770.46]  Because, again, there's not everything is like black or white, like there's like nuances of gray now in terms of perceived quality.
[1770.72 --> 1777.86]  So you you need to have like more of a statistical approach in terms of understanding the impact of like one model versus the others.
[1777.86 --> 1785.50]  And of course, we have internal evals and all of that to do our own testing in terms of with like our golden data set.
[1785.86 --> 1791.44]  But the reality is we have like a diverse set of customers and everyone is different.
[1791.56 --> 1796.12]  So we need to have like a broader perspective than just relying on our own data set.
[1796.44 --> 1806.02]  Yeah, Loic, I appreciate you getting into the technical side of things a bit and talking through some of those optimizations and how you think about them.
[1806.02 --> 1810.78]  Obviously, you're leading the technical efforts with Superhuman.
[1811.02 --> 1817.46]  And I'm wondering if you have any sort of hard lessons learned from doing AI engineering over time.
[1817.56 --> 1820.16]  We have a lot of practitioners that listen in.
[1820.66 --> 1825.12]  Any kind of general principles or lessons learned that you'd want to impart?
[1825.66 --> 1826.50]  That's a good question.
[1826.50 --> 1833.48]  Maybe one thing that I've learned is to like as a CTO, I need to discuss with the rest of my leadership team.
[1833.78 --> 1837.12]  And we talk about the success of features and everything.
[1837.38 --> 1842.32]  And the typical way to talk about like quality is typically in terms of like number of bugs and everything.
[1843.32 --> 1849.90]  Now, and I was at touch on it early on, but the perceived quality depends now.
[1850.00 --> 1853.38]  Like we're in a world with way more subtleties with LLMs.
[1853.38 --> 1864.22]  So setting the right expectation, basically explaining that the way the feature can be built and sometimes failing because the feedback is not great might not be because it's not well implemented.
[1864.68 --> 1866.62]  But maybe there's, I would say, more to it.
[1866.70 --> 1868.08]  Maybe there's a part of the perception.
[1868.34 --> 1870.72]  Maybe there's too much latitude that is offered to the end user.
[1871.24 --> 1873.88]  Maybe there's some work on the prompt side.
[1873.88 --> 1882.40]  So that's something that hit me in the beginning where the perception of the feature was like, oh, this is terrible work.
[1882.56 --> 1883.40]  Like it's not working.
[1883.54 --> 1884.30]  People are complaining.
[1884.70 --> 1885.50]  Guys, what have you done?
[1886.04 --> 1888.08]  And the work was done properly.
[1888.24 --> 1889.92]  It was like well implemented and everything.
[1890.44 --> 1898.96]  But the perceived quality of such, I would say, some of those features can be completely different based on like those new aspects.
[1898.96 --> 1910.02]  So maybe like my lesson learned was to is now to just like be very explicit when you basically launch a new feature about the risk of that perceived quality.
[1910.02 --> 1917.56]  And like the source of the mistakes being a bit less on the engineering side and maybe a bit more on the user.
[1918.02 --> 1926.50]  And there's a lot of work to be done to control that in terms of like user education, in product education.
[1927.16 --> 1937.54]  So putting a bit more effort on like the product led growth, typical aspect of the business that will have like a tremendous impact on the success of the feature.
[1937.54 --> 1939.36]  So that's probably one.
[1939.82 --> 1944.32]  The second one is, and it's interesting because I see it every day.
[1944.64 --> 1947.28]  We are moving up market, right?
[1947.64 --> 1951.12]  We have a lot of startups that are moving up market.
[1951.32 --> 1957.56]  So you start having like your companies that are like part of the Fortune 500 and they want to use your product.
[1958.30 --> 1962.00]  And I come from a world where moving to enterprise is pretty heavy.
[1962.26 --> 1963.40]  You need a lot of features.
[1963.58 --> 1965.04]  You need to have like a lot of compliance.
[1965.04 --> 1976.46]  You need to have like basically a lot of things that are not directly improving your product, but improving the confidence of those companies that you are the right partner to work on those for them.
[1977.42 --> 1979.08]  There's a shift now.
[1979.36 --> 1993.70]  There's clearly a shift in those Fortune 500 and by extension, all the enterprise market where, especially with AI, the risk associated with lesser compliance or you're a small company.
[1993.70 --> 1994.94]  Should we trust you?
[1995.50 --> 2001.22]  Is completely counterbalanced by the risk of missing out.
[2001.34 --> 2004.18]  Like the cost, the opportunity cost is too big.
[2004.26 --> 2014.38]  And now we see definitely push from CXOs on their security teams for those AI tools and productivity tools.
[2014.38 --> 2017.32]  Basically saying, hey guys, you need to make it work.
[2017.82 --> 2024.76]  You need to make it work because it's improving so much the efficiency of the C level and by extension of the rest of the company.
[2025.60 --> 2026.20]  You know what?
[2026.26 --> 2028.24]  We're probably ready to make the risk, to take the risk.
[2028.24 --> 2041.90]  Even if it's like a series A, series B, series C company and it's not like fully established maybe or like maybe the, yes, they are processing our emails, which is like a core data set of our business and we need to be like straight about it.
[2041.90 --> 2043.76]  Like maybe they're more okay.
[2044.02 --> 2045.48]  Of course, we need to do the work.
[2045.62 --> 2049.26]  You need to be like, you need to prove that you're the right partner.
[2049.26 --> 2053.32]  But the first approach is changing and the dynamic is changing.
[2053.84 --> 2066.66]  So it's basically a bias to let's make it work compared to two years before where it was probably prove us that you are a reliable partner and then we'll see if we do this POC.
[2067.00 --> 2068.56]  It's completely the reverse right now.
[2069.12 --> 2074.36]  So, yeah, that's an interesting dynamic that is useful in the way to build a product right now.
[2074.70 --> 2075.66]  I'm curious.
[2075.66 --> 2083.40]  And, you know, we get to talk about all these really cool things happening in the AI space and how they're affecting products and services.
[2084.12 --> 2087.10]  And, you know, LLMs can do so much now.
[2087.30 --> 2092.92]  And, you know, we're kind of moving into the agentic age, you know, of AI and that's increasing.
[2093.42 --> 2098.00]  But, you know, there's still a human being in the workflow.
[2098.00 --> 2110.42]  And kind of what are the critical factors that the human is still bringing into the workflow as opposed to all this amazing technology that we're able to utilize on that?
[2110.68 --> 2118.88]  How do you see the human in the workflow going forward, given the fact that you have so much capability from technology playing all around them?
[2118.88 --> 2120.44]  That's an interesting question.
[2120.80 --> 2122.68]  And I guess the answer is almost in the question.
[2122.84 --> 2126.16]  Like, it's like the human part that is hard to replicate.
[2126.86 --> 2133.82]  And so, I mean, creativity, ability to define, like to detect patterns and stuff.
[2134.02 --> 2141.04]  Like, so I think that the rise of LLMs is helping us get rid of everything that is mundane.
[2141.04 --> 2145.80]  Like, I spent, like, I was, I used to, I will give you one example.
[2146.46 --> 2149.94]  I do a lot of interviews because I hire, like, engineers.
[2150.48 --> 2157.12]  And as part of every interview process, you used to write up, like, a debrief for the team to consume.
[2157.50 --> 2161.24]  And so, and writing a debrief, like a thoughtful debrief, like, takes time.
[2161.66 --> 2162.10]  It takes time.
[2162.18 --> 2170.18]  Like, I was, like, probably spending, like, between 20 and 30 minutes after each interview to basically put, like, the pros, the cons, like, a question mark.
[2170.18 --> 2171.98]  Like, area to dive in.
[2172.98 --> 2180.36]  Now, we are pretty much all using, like, meeting minutes that are, like, using the transcript, formatting that the way you want.
[2180.64 --> 2185.34]  And you just have to add your quick thoughts here and there and on the line like that.
[2185.56 --> 2189.28]  So now, like, from 20 to 30 minutes, this is taking me three minutes.
[2189.60 --> 2193.26]  And boom, this is uploaded in the whatever ATS, like, tools, like, from HR.
[2193.80 --> 2194.66]  That's an example.
[2195.42 --> 2196.60]  Meeting minutes with my people.
[2196.82 --> 2197.80]  Like, I have one-to-ones.
[2197.80 --> 2200.80]  I do one-to-one, like, meetings with my people.
[2201.08 --> 2203.68]  I want to keep track of everything that we said.
[2203.80 --> 2204.76]  I used to take notes.
[2205.48 --> 2208.34]  I'm still, to some extent, taking some notes.
[2208.72 --> 2213.74]  But, like, the transcript itself is so good now that I don't have to take notes of everything.
[2214.04 --> 2219.30]  So I just, like, put notes of, like, the two key highlights that I want to keep somewhat private.
[2219.68 --> 2220.72]  The rest is already shared.
[2220.72 --> 2228.36]  And now it's building, like, a database for me, like, of information on my desktop that I can query any time to find information.
[2228.86 --> 2233.46]  So this is replacing all the mundane work that I was doing.
[2233.46 --> 2237.06]  And I can just focus on, like, brain power to some extent.
[2237.28 --> 2239.10]  And that's definitely changing.
[2239.38 --> 2240.90]  So same for my engineers.
[2240.90 --> 2250.26]  My engineers, they've lived, like, I would say, padding shift to padding shift and, like, changing the way they build software over time.
[2250.66 --> 2254.32]  They keep increasing their velocity because of those, like, new tools.
[2254.78 --> 2258.00]  They have also to think differently.
[2258.18 --> 2260.62]  But, like, it's still stupid to some extent.
[2260.98 --> 2264.60]  Like, all these toolings, like, it's basically an intern.
[2265.56 --> 2266.44]  It's an intern.
[2266.44 --> 2267.56]  So you need to review.
[2268.16 --> 2279.80]  You need to spend the time, like, reviewing what has been output, what's the output of, like, your new ID, being cursor, being C-line, being whatever, like, those tools.
[2279.98 --> 2286.06]  You need to review everything because sometimes it will make, like, some crazy mistakes that, like, a regular engineer won't do.
[2286.38 --> 2294.80]  But I think that it's saving a ton of time for our engineers that they can just focus on the core of their job, which is, like, understanding the user.
[2294.80 --> 2299.36]  Understanding what needs to happen and what is the smartest way to get it happen.
[2300.28 --> 2302.88]  LLMs are just a nice helper to go faster.
[2303.18 --> 2305.90]  But so far, it's about it.
[2306.20 --> 2307.32]  But it's changing every day.
[2307.58 --> 2308.50]  It's changing every day.
[2309.20 --> 2316.46]  Yeah, Loic, you mentioned kind of coding and vibe coding, you know, comes to mind.
[2316.46 --> 2324.14]  And I almost wonder, you know, there's going to be a new reality for email with all of these AI features coming in.
[2324.14 --> 2330.74]  And I know when I'm using vibe coding tools, I have to sort of learn a new way of working.
[2330.88 --> 2339.64]  And there's different types of mental loads that I have to manage, like a lot of context switching, you know, guiding the model in different ways.
[2339.64 --> 2342.74]  It's a different kind of mental load, a different kind of skill.
[2342.74 --> 2366.54]  Do you see a similar thing developing in terms of, you know, my interaction with email and, you know, learning a kind of different way of working through those things, you know, in good ways, but also in challenging ways to sort of retool my mind or retrain my mind of how to work in this kind of vibe emailing way?
[2366.54 --> 2370.36]  No, no, this is a good question.
[2370.84 --> 2375.60]  And we're talking about like the user interaction and how this is evolving.
[2375.98 --> 2381.44]  And our work is to make that transition, if there's any transition, like the smoothest possible.
[2381.64 --> 2388.84]  We need to take the user where they are to bring them where they will be eventually with this vibe emailing, if that even mean a thing.
[2389.08 --> 2395.76]  I'm not sure what would be behind it, but clearly there's a change that we are facing.
[2395.76 --> 2410.26]  And interestingly, I was talking lately, but right now startups, I would say, startup typically over index on seniority for engineers, because you need people to be able to manage the noise, manage the shit.
[2410.40 --> 2411.08]  Like it's always changing.
[2411.18 --> 2414.44]  Like you need people with like a tough skin to be able to manage that.
[2414.44 --> 2419.94]  That said, and we see it, it's harder right now for like a new grads to get into this market.
[2421.10 --> 2425.30]  So, but they have like one asset that makes them probably different.
[2425.72 --> 2427.18]  It's the brain plasticity.
[2427.62 --> 2435.48]  The new grads of this year, like for the last three years, they've seen so many different technologies coming like every six months.
[2435.64 --> 2437.74]  They had to read that, they had to relearn.
[2437.74 --> 2444.52]  So their brain is used to this mental shift like every six months, like, oh damn, this is the new way to code.
[2444.70 --> 2446.54]  Oh damn, this is the new, new way to code.
[2447.02 --> 2452.32]  Like in my days, like the biggest shift was moving from SVN to Git.
[2452.96 --> 2454.04]  That was about it.
[2454.12 --> 2461.50]  Or like you have a new framework or you have like a new language, but like it's same old, same old, like different flavor of the same thing.
[2461.50 --> 2469.26]  So I do think that the people that aren't like just born with it, we were born with internet.
[2469.42 --> 2474.66]  They are born with LLMs and with AI and they have this brain plasticity.
[2474.82 --> 2482.02]  And I think this will be like probably the challenge for like practitioners, like engineers globally is how to adapt to that.
[2482.04 --> 2486.70]  Because I'm 45, I'm not sure that my brain plasticity is still there.
[2486.70 --> 2491.46]  So I need to keep up, I need to still try new stuff and everything and challenge myself every day.
[2491.94 --> 2500.80]  Compared to even like five years ago where like I was just like tuning my own ways and like making it like slightly better over time.
[2501.12 --> 2505.12]  Like this is a paradigm shift and if I don't take the wagon, I'm probably last.
[2505.64 --> 2506.74]  And same applies for engineers.
[2507.10 --> 2509.04]  So it's definitely an interesting time.
[2509.40 --> 2510.54]  Definitely an interesting time.
[2510.54 --> 2520.20]  I got to say, if you hadn't dated yourself intentionally revealing your name, I was going to say the SVN to GitSwitch would have done that for you.
[2520.52 --> 2525.64]  I don't think anyone out there under 30 is going to know what SVN is anyway.
[2527.12 --> 2528.40]  Yeah, I'm sorry.
[2528.48 --> 2529.14]  I'm sorry for that.
[2529.24 --> 2531.12]  It's kind of like my gray hair that we're talking.
[2531.60 --> 2535.90]  No, I'm just definitely a brain plasticity is on my mind as well.
[2536.46 --> 2537.80]  I'm older than you are even.
[2537.80 --> 2546.96]  So I'm curious, you know, as we wind up here, you know, there's so much ground is getting covered right now.
[2547.02 --> 2556.54]  And, you know, you've talked about like, you know, the evolution of the product and, you know, new technologies, you know, kind of slamming into your current plans and having to adjust and stuff.
[2556.54 --> 2576.48]  But if you kind of take a step back or, you know, kind of done for the day and you're kind of thinking about the future and you're thinking on a little bit longer time frame than kind of what we've been talking about, kind of, you know, where can, you know, email and messaging and stuff, where can it go with these technologies in a little bit longer time frame?
[2576.48 --> 2582.54]  When you kind of get into, you know, kind of just letting your mind wander and kind of kind of dreaming what could be.
[2583.48 --> 2588.10]  What are your thoughts around the future around that, you know, in the large?
[2588.36 --> 2593.62]  What should we be thinking about that's not necessarily going to be science fiction going forward?
[2593.74 --> 2597.60]  But, you know, day to day life, given where things are kind of generally headed?
[2597.60 --> 2600.42]  No, this is a, I wish I knew.
[2600.78 --> 2601.34]  I wish I knew.
[2601.42 --> 2611.78]  But like, if I have to do like a bit of science fiction, like clearly I see the communication globally, communication between people is so fragmented, so fragmented.
[2612.16 --> 2613.82]  Like with my family, I use WhatsApp.
[2614.52 --> 2618.26]  At work, I use, with my partners and all of that, we use emails.
[2619.24 --> 2620.76]  Internally, we use Slack.
[2620.76 --> 2628.26]  But we also like discuss in like Google Docs, threads, like in comments and all of that.
[2628.78 --> 2643.00]  So communication is so spread out and so in different places that it's really hard to make sure that you have everything that belongs to the same topic into the sort of like unified inbox.
[2643.00 --> 2653.16]  So if I have to guess where we would be like in, I don't know, I would say 10 years, but like maybe with like AI, it would be like in six months.
[2654.02 --> 2665.40]  I would say that there's probably a need of a unified and central way to communicate for you, which is your preferred interface, regardless of where this will land.
[2665.40 --> 2670.36]  And doing so like in a way that brings focus.
[2670.72 --> 2680.84]  When I want to work on a specific partnership with like in AI, with like all those like big providers and everything, I want to focus only on this.
[2680.94 --> 2688.58]  But I don't care if like the information is in my email, is in Google Doc, is in Notion, is in WhatsApp or whatever.
[2688.74 --> 2692.52]  I want this to be consolidated so that I know everything that is happening in one place.
[2692.52 --> 2696.06]  So I think there would be like a lot of work around this.
[2696.34 --> 2703.36]  The other aspect that is really interesting is where LLM sits, what is the entry point?
[2704.04 --> 2711.64]  We see ChatGPT being like one entry point, but like all the tools have like an embedded ChatGPT equivalent.
[2711.64 --> 2725.70]  So whether you use like Confluence, Notion, whether you use like Salesforce, whether you use like any kind of B2B application, have their like own specific ChatBot.
[2726.06 --> 2734.82]  And then you have like actors like Glean, for example, and some others that try to like unify everything.
[2735.16 --> 2736.12]  Where is this going?
[2736.12 --> 2739.30]  And so that's something that I'm really curious about.
[2739.74 --> 2749.78]  Do we want to be where people work or do you want to have like some sort of like a unified experience regardless of the vertical people are working in?
[2750.90 --> 2751.76]  I'm curious.
[2752.04 --> 2753.80]  Like I have more questions than answer.
[2754.48 --> 2755.84]  What's for sure it will evolve.
[2755.84 --> 2762.34]  And that's I do believe like superhuman is doing that in a nice way and people tend to love it.
[2762.76 --> 2770.38]  So building on that experience and that empathy with users, I believe will be like well placed for that race, basically.
[2770.92 --> 2772.32]  But interesting race.
[2772.70 --> 2774.12]  I appreciate the insights.
[2774.12 --> 2786.96]  And thank you so much for coming on the show today and kind of sharing and not only where superhumans at, but kind of, you know, how you're how you're tackling the challenges and thinking about the future.
[2787.12 --> 2788.50]  A lot of insight there.
[2788.62 --> 2789.52]  I really appreciate it.
[2789.80 --> 2790.22]  Thanks, Chris.
[2790.40 --> 2792.44]  I appreciate the time with you and Daniel.
[2799.44 --> 2800.42]  All right.
[2800.70 --> 2802.52]  That is our show for this week.
[2802.52 --> 2808.82]  If you haven't checked out our changelog newsletter, head to changelog.com slash news.
[2809.02 --> 2811.30]  There you'll find 29 reasons.
[2811.52 --> 2814.88]  Yes, 29 reasons why you should subscribe.
[2815.36 --> 2816.72]  I'll tell you reason number 17.
[2817.30 --> 2820.08]  You might actually start looking forward to Mondays.
[2820.24 --> 2822.94]  Sounds like somebody's got a case of the Mondays.
[2823.34 --> 2827.88]  28 more reasons are waiting for you at changelog.com slash news.
[2828.06 --> 2830.64]  Thanks again to our partners at fly.io.
[2830.64 --> 2833.80]  To Breakmaster Cylinder for the beats and to you for listening.
[2834.22 --> 2835.32]  That is all for now.
[2835.50 --> 2836.88]  But we'll talk to you again next time.
