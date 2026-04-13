[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.46 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[26.32 --> 28.36]  Thanks to our partners at Fly.io.
[28.36 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.38]  Learn how at Fly.io.
[44.54 --> 48.40]  Welcome to another episode of the Practical AI podcast.
[48.98 --> 50.50]  This is Daniel Whitenack.
[50.60 --> 56.24]  I'm CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who
[56.24 --> 59.72]  is a Principal AI Research Engineer at Lockheed Martin.
[60.28 --> 60.96]  How are you doing, Chris?
[61.28 --> 62.40]  Doing great, Daniel.
[62.44 --> 63.12]  How's it going today?
[63.56 --> 64.66]  It's going great.
[64.76 --> 70.70]  I was just commenting before we hopped on about I'm feeling the emotional boost of seeing the
[70.70 --> 73.90]  sun again after a long Midwest winter.
[73.90 --> 82.30]  So I'm feeling good today and excited to chat about all things AI and code assistant and
[82.30 --> 89.04]  development and all of those things because we have with us Kyle Daigle, who is COO at
[89.04 --> 89.38]  GitHub.
[89.64 --> 90.26]  Welcome, Kyle.
[90.82 --> 91.48]  Thank you so much.
[91.60 --> 92.48]  It's so great to be here.
[92.86 --> 93.12]  Yeah.
[93.22 --> 93.44]  Yeah.
[93.44 --> 95.56]  It's awesome to have you on.
[95.56 --> 102.92]  Just even in your comments about how you like to think about the practical side of AI, this
[102.92 --> 104.18]  is your place.
[104.40 --> 106.46]  So I already feel a kindred spirit.
[106.68 --> 108.18]  I feel very much at home already.
[109.36 --> 109.56]  Yeah.
[109.84 --> 110.04]  Yeah.
[110.36 --> 115.78]  Well, speaking of which, I mean, you're, of course, you know, really kind of at the center
[115.78 --> 121.24]  of a lot of what's going on in terms of code assistance with GitHub Copilot, of course,
[121.36 --> 124.70]  but you're also, I'm sure, seeing a ton of things out there.
[124.70 --> 130.46]  I'm wondering if you could just kind of take a 10,000 foot view and kind of for those that
[130.46 --> 136.64]  maybe aren't following all of the things happening with AI code assistance and development,
[137.34 --> 143.52]  what's kind of like as of now sitting in, what is it, March of 2025, if you're listening
[143.52 --> 151.62]  to this, what's kind of the state of AI code assistance and how people are kind of generally
[151.62 --> 153.84]  using those right now?
[153.84 --> 154.32]  Yeah.
[154.32 --> 154.72]  Yeah.
[154.86 --> 161.42]  I mean, it's so interesting to see how far I feel like we've come in such a short period
[161.42 --> 162.08]  of time, right?
[162.10 --> 167.78]  It was only a couple of years ago when ChatGPT came out, GitHub Copilot came out.
[167.90 --> 173.36]  And back then, the novelty was sort of like, it wasn't going to disappoint you, right?
[173.48 --> 178.88]  For GitHub Copilot, you know, you would type some lines and it would respond with, you know,
[178.88 --> 182.08]  a line, two lines, a method, et cetera, it was going to complete your code.
[182.08 --> 186.40]  Very similar to, you know, I'm going to ask instead of Google a question, I'm going to
[186.40 --> 189.00]  ask ChatGPT and I can keep asking a question.
[189.00 --> 197.38]  I think what really, you know, locked in this enormous transformation then was finding a
[197.38 --> 203.80]  user experience that was simple, straightforward and didn't need much explanation, right?
[203.80 --> 209.24]  Like I'm a dev, I'm writing code and it's just working there versus, you know, needing
[209.24 --> 213.40]  to figure out how to use a tool, figure out how it works in my workflow and kind of go through
[213.40 --> 214.48]  hours of onboarding.
[215.14 --> 217.74]  Fast forward a couple of years, right?
[217.78 --> 224.06]  Not only have the models materially gotten so much better, but we've found more and more
[224.06 --> 232.00]  ways to kind of have that similar joyful expected user experience with code assistance.
[232.00 --> 236.82]  So it's not just really about writing the code in some ways, right?
[236.92 --> 239.88]  It's not about that at all right now.
[239.88 --> 244.90]  I think that's at the bleeding edge of what we're experiencing with code assistance where
[244.90 --> 250.66]  it's much, much, much more about sitting down with a couple of dev friends and saying,
[250.82 --> 256.46]  hey, I have this idea for an app, but instead of pitching it to your friends, now you're pitching
[256.46 --> 263.08]  it to your IDE and that code assistant is going to jump in and help you get that next step done.
[263.22 --> 269.40]  So when I look back over this wave and how it went from sort of, you know, cool, but in
[269.40 --> 273.70]  retrospect, right, a little bit simplistic behavior of, wow, it really knows what I want
[273.70 --> 278.92]  to write next into like the next level of what it's always been like to be a developer,
[278.92 --> 282.94]  which is I have this idea and now I have to explain it to someone else.
[282.94 --> 291.32]  We keep finding ways to augment, improve and speed up what a dev does kind of every single
[291.32 --> 291.68]  day.
[291.68 --> 299.08]  And we're at a point now where I think we're seriously starting to blur the edges of like,
[299.20 --> 300.54]  what is a developer?
[301.46 --> 305.36]  I don't think we're there all the way to be very clear, but I think, you know, a year
[305.36 --> 308.28]  ago we were talking about that and it was like, sure.
[308.52 --> 314.56]  And now it's getting closer and closer to say, you know, well, what is that distinct, that
[314.56 --> 315.42]  distinct need?
[315.42 --> 319.48]  And that's only really been in a year and then, you know, about two and a half, three
[319.48 --> 322.98]  years from the start of the start of this journey.
[323.20 --> 328.08]  And so I think the code assistant category has always been so interesting to me because
[328.08 --> 331.80]  it doesn't, it's kind of matching how we work.
[331.96 --> 336.24]  You know, it's finding ways to augment and improve how we work, not trying to teach us
[336.24 --> 338.58]  totally to do something completely different.
[338.58 --> 344.72]  Which I think when we zoom maybe from 10,000 feet to 40,000 feet and we look at AI, the
[344.72 --> 348.24]  best tools are the ones that are just helping us do work we're already doing.
[348.52 --> 353.90]  The tools that aren't the best or having more difficulty finding traction, in my opinion,
[354.38 --> 360.00]  tend to have to make the human contort to get the most power out of the AI tool.
[360.44 --> 364.28]  And so because we're devs, we're just kind of iterating in what we know.
[364.28 --> 368.44]  Uh, and that's been the power of, you know, code assistants and the growth of them, you
[368.44 --> 369.94]  know, over the last year or so, I think.
[370.50 --> 371.36]  I'm curious.
[371.54 --> 376.48]  I mean, that's a, it's a great point you're making there and about the, the changing developer
[376.48 --> 379.46]  experience and changing so incredibly rapidly.
[379.46 --> 384.40]  I mean, you know, month by month, there are changes in what it means to be a developer
[384.40 --> 384.72]  now.
[385.00 --> 388.90]  And so I know, you know, and I'm sure I'm speaking for a lot of people.
[388.90 --> 394.84]  I like, I keep reinventing kind of parts of my own workflow, uh, as I'm doing stuff because
[394.84 --> 398.92]  new tools become available and what I am doing or not doing is changing constantly.
[399.78 --> 404.94]  It's kind of a, it's, it's both amazingly wonderful, you know, given where, where we've
[404.94 --> 405.72]  been over the years.
[406.02 --> 407.82]  Uh, but it's also quite tumultuous.
[407.88 --> 412.54]  And, and, and when we stop and if I stop and kind of lean back a little bit and have a
[412.54 --> 416.16]  cup of coffee and think about it, I'm kind of going maybe a little bit scary in the future
[416.16 --> 417.86]  about how good it's getting and where that's going.
[417.86 --> 422.26]  What, what are your thoughts on, you know, since you've talked about the developer experience
[422.26 --> 427.42]  explicitly and, and the user experience of code assistance and that they are going, they
[427.42 --> 428.70]  are rapidly going so far ahead.
[429.24 --> 433.44]  What, what kind of, of, of thoughts, and I don't even go out a long way.
[433.52 --> 438.24]  I'm just talking about in the next few months in the short term, like where, how, how can
[438.24 --> 444.60]  we be thinking about, um, adjusting ourselves to an ever evolving state right now as we're,
[444.74 --> 447.74]  as we're trying to think about that, even before we get into the specifics of the tools
[447.74 --> 448.24]  themselves?
[448.72 --> 448.86]  Yeah.
[448.96 --> 449.12]  Yeah.
[449.16 --> 455.70]  I mean, you know, I think, uh, what we've seen at GitHub by a rolling out these tools
[455.70 --> 459.22]  is like, we'll talk to customers or I'll just talk to devs or open source maintainers, et
[459.22 --> 459.50]  cetera.
[459.78 --> 462.58]  And they can kind of fall on this continuum, right?
[462.60 --> 465.14]  This continuum of, I absolutely love every AI tool.
[465.14 --> 468.10]  I'm going to use every single one and I'm going to try every single one.
[468.58 --> 471.76]  And then you have the folks who are like, I'm never touching these things ever.
[471.86 --> 472.36]  They're terrible.
[472.36 --> 473.52]  And they're going to destroy software.
[473.52 --> 475.78]  And then there's all the folks in the middle.
[476.18 --> 480.72]  And so I think the thing that I tend to tell folks is like, you know, just like in our
[480.72 --> 485.40]  careers, we've all had a moment where a new piece of technology comes in.
[485.50 --> 491.50]  And I feel like for some reason it's in at least 50% developers minds of like, oh, well,
[491.50 --> 493.94]  that's just a silly thing or that's just a toy or whatever.
[493.94 --> 499.34]  So I'll just say for myself personally, Rubyist by nature, JavaScript took over and I'm like,
[499.38 --> 501.94]  oh, JavaScript, Ruby's, you know, blah, blah, blah.
[502.32 --> 507.04]  And so like over time you grow and you realize, oh, well, I should really understand that and
[507.04 --> 507.70]  try it out.
[507.74 --> 514.06]  And it may not become my new go-to tool, but I, it would not help me or honestly, like
[514.06 --> 517.52]  the industry or my peers for me just to be like, ah, I'm never going to touch JavaScript.
[517.88 --> 522.40]  So I think that experimentation that you were talking about, Chris, is the important thing.
[522.40 --> 528.90]  I see a lot of devs like try out a new tool or try out a new feature or a new library or
[528.90 --> 533.92]  a new model and then drop back to whatever their floor is, whatever the thing they're
[533.92 --> 536.76]  most comfortable with, the model they know, et cetera, et cetera.
[536.96 --> 543.38]  And I think that is the minimum because the change is going to happen just like it's always
[543.38 --> 548.64]  happened between serverless languages, databases, you pick it, right?
[548.64 --> 555.74]  And if you just don't experiment, my fear personally would be that you do kind of start to get left
[555.74 --> 562.06]  behind because you don't know how to reach out to the new tool that is actually excellent
[562.06 --> 563.04]  and actually helpful.
[563.04 --> 568.62]  And you're kind of stuck behind the eight ball learning something that you could have been
[568.62 --> 570.26]  learning as you go.
[570.26 --> 576.32]  I will say like, you know, in the next few months, even not even just kind of like now,
[576.32 --> 586.42]  I do expect way more kind of AI functionality to come outside the editor because if you're
[586.42 --> 590.76]  developing software as part of a team or as part of a company, not as a solo dev or a
[590.76 --> 596.86]  smaller startup, but a bigger group, we all know like writing code is an important part
[596.86 --> 599.48]  of the job, but it's not all of your day, right?
[599.52 --> 604.08]  You're reviewing code, you're building out a decision records or architecture diagrams,
[604.08 --> 606.18]  or you're debating how to roll this out.
[606.24 --> 609.06]  You're operating a live site, so on and so forth.
[609.20 --> 615.98]  I think as AI comes into those spaces to fill in the gaps more and more, again, like you're
[615.98 --> 621.02]  going to want to have those skills from, you know, figuring out the right way to word things
[621.02 --> 625.24]  when the AI can't just figure it out or the LLM can't just figure it out on its own.
[625.24 --> 631.30]  Or again, like every developer know how the system is working inherently so you can best
[631.30 --> 632.94]  benefit from it.
[632.98 --> 637.66]  So as long as you're kind of trying these things out, even if you drop back to your baseline,
[637.90 --> 640.60]  I think you get set up for more productivity.
[640.60 --> 645.24]  And I think just kind of like more joy when the AI can take more of those mundane tasks
[645.24 --> 646.52]  away from you.
[646.62 --> 650.24]  Again, like I think over the next couple of months, not even the next year.
[650.24 --> 655.76]  What do you think are the, for those devs, you know, some that have jumped right in,
[655.82 --> 657.00]  they figured out their workflow.
[657.20 --> 660.40]  Maybe there's devs out there that are experimenting with the tools.
[661.02 --> 666.10]  What do you think are those new kind of, you know, everyone's kind of got their muscle memory
[666.10 --> 669.68]  of how they develop, you know, the things that they like to use.
[669.82 --> 678.46]  What are kind of the new muscles that need to be developed for kind of AI-assisted coding?
[678.46 --> 682.78]  Like the most important ones that you've seen over very many use cases?
[683.36 --> 683.48]  Yeah.
[683.60 --> 687.52]  I mean, I think there's kind of two major ones.
[688.40 --> 694.20]  Every developer has, like you said, you know, come up with the kind of practices and principles
[694.20 --> 695.52]  for you personally, right?
[695.86 --> 699.50]  We've all worked in systems that have linters and CI and everything that like stops you from
[699.50 --> 700.14]  making mistakes.
[700.30 --> 705.06]  But there's just also a bunch of things that I like to work in this order.
[705.16 --> 707.74]  It helps my brain process what's going on.
[707.74 --> 708.36]  You know what I mean?
[708.72 --> 715.56]  And so I think on a tactical level, stating those rules, those prompt instructions, whatever,
[715.84 --> 720.40]  you know, depending on which tool you're using for this, there's a different name for it.
[720.62 --> 726.98]  But I do think that that's something just the act of sitting down and writing out, well,
[726.98 --> 728.62]  how do I work on this project?
[728.66 --> 731.94]  Even if you work as a part of a company, you know, how do I care about it?
[731.94 --> 737.12]  I always want to define a schema for the backend API before I implement the front end.
[737.28 --> 740.04]  And then I go back to the backend or whatever the thing is for you.
[740.26 --> 746.56]  It's writing that down and then letting the tool use that, I think is a dual benefit, which
[746.56 --> 748.26]  kind of gets me to my second point.
[748.26 --> 755.74]  The big skill that everyone is, I think, trying to work out is it used to be called like prompt
[755.74 --> 756.22]  engineering.
[756.22 --> 759.46]  And I honestly think it's just describing a problem.
[760.16 --> 766.36]  We use so much shorthand and sort of we skip over the details, like the hilarious meme of,
[766.44 --> 769.30]  you know, what the product manager said, what the engineer did, what the designer did.
[769.30 --> 772.76]  But that is exactly what we have to do with these tools every day.
[772.76 --> 777.60]  We go build an app that X, Y, Z's and suddenly it comes back and it makes no sense.
[777.72 --> 780.52]  And you go, oh, this stupid thing doesn't work, you know?
[780.58 --> 782.78]  And yes, sometimes it just doesn't work.
[782.82 --> 787.44]  But realistically sitting down and saying, well, what are the must do's of this app?
[787.54 --> 789.54]  You know, how do I want it to work?
[789.64 --> 791.10]  What do I want the flow to be?
[791.18 --> 796.94]  Whatever those things are, being able to clearly communicate, particularly in a written form
[796.94 --> 800.62]  is like crucial in this new era.
[800.78 --> 805.98]  And I think it's been a skill that in some ways we've kind of let fall down.
[806.16 --> 811.84]  Like, you know, when I think back to the era in which I was a much more active dev, you know,
[812.10 --> 817.20]  I think there was just so much written communication, whether that be blog posts or GitHub's always
[817.20 --> 817.74]  been remote.
[817.86 --> 822.02]  And so for us, it was usually like a GitHub issue or campfire back in the good old days,
[822.12 --> 825.56]  Slack these days, just writing down what you mean.
[825.56 --> 830.22]  And that's a skill to bring to saying what I want this app to do.
[830.30 --> 834.26]  And I think that's why when you're on Twitter or X or wherever, and you're looking at, you
[834.26 --> 836.66]  know, wow, how did this example get one shot?
[836.82 --> 838.72]  It's like ask for the instruction.
[839.36 --> 843.84]  That instruction was certainly not build a game, a multiplayer game that allows me to
[843.84 --> 844.56]  fly airplanes.
[844.92 --> 846.06]  Like that was not it.
[846.16 --> 847.32]  You know, it was much more.
[847.32 --> 852.96]  But with all the practice that came from describing problems socially, describing problems for your
[852.96 --> 855.64]  LLM, being able to do that regularly.
[855.92 --> 860.40]  And I really think it's mainly describing problems as the models have gotten so much
[860.40 --> 860.68]  better.
[860.78 --> 864.88]  There's a little less like, how do I make it work for each model than there used to be?
[865.02 --> 870.32]  That's a skill that's going to serve you both in those tools and with your colleagues,
[870.32 --> 876.54]  with your manager, with your open source friends and maintainers, just cohesively, if you can do it
[876.54 --> 876.94]  really well.
[876.94 --> 878.26]  I'm curious to that.
[878.34 --> 884.72]  Do you think as just as a two second follow up that for developers, kind of that that describing
[884.72 --> 889.88]  a problem skill that you've that you've been addressing, along with kind of the communication
[889.88 --> 891.70]  skills that support that?
[891.90 --> 895.06]  Should we think of that as developer skills now?
[895.14 --> 898.90]  And, you know, maybe that is a muscle that we have that we should start exercising as well.
[899.10 --> 899.92]  Yeah, I think it was.
[900.02 --> 905.20]  I think it's something that we like the best teams, the best companies have considered that.
[905.20 --> 911.08]  And I think we've kind of let a little bit of the like 10x developer meme take over and
[911.08 --> 913.70]  make communication not be as big of a deal.
[913.90 --> 920.42]  There's no major application site or app that serves hundreds of millions of people or tens
[920.42 --> 921.42]  of millions of people.
[921.44 --> 926.80]  We're being able to communicate what's happening or what the problems are isn't core to the
[926.80 --> 927.98]  job of being a developer.
[927.98 --> 935.04]  And if we just play out over time, you know, if AI and LLMs are going to continue to write
[935.04 --> 941.42]  more and more and more and more of the code, even if it never hits, you know, all of the
[941.42 --> 945.80]  code, whatever that ultimately means, all that's left is collaboration.
[946.02 --> 951.60]  All that's left is collaborating with your peers, with LLMs, with agents, with designers,
[951.80 --> 954.42]  with your boss, with your client, whatever that is.
[954.42 --> 959.74]  And so suddenly the fact that you can write an app incredibly well, succinctly, well factored
[959.74 --> 961.80]  and tested, whatever, that's great.
[961.94 --> 963.78]  That's a great skill too.
[963.98 --> 967.60]  But the human factor will be, I can look at you in the eye.
[967.72 --> 972.86]  I can read what you're writing, intuit what you're saying, what you're looking for, and
[972.86 --> 977.64]  describe that in such a way that I can, you know, benefit from all of these tools.
[977.64 --> 983.96]  It's going to be incredibly necessary as those, you know, more rote or highly automated tasks
[983.96 --> 986.32]  can be done by, you know, AI tools.
[986.32 --> 1007.30]  Well, friends, today's ever-changing AI landscape means your data demands more than the narrow
[1007.30 --> 1011.56]  applications and single model solutions that most companies offer.
[1011.56 --> 1018.76]  Domo's AI and data products platform is a more robust, all-in-one solution for your data.
[1019.20 --> 1023.98]  It's not just ambitious, it's practical and adaptable.
[1024.12 --> 1027.68]  So your business can meet those new challenges with ease.
[1028.12 --> 1034.04]  With Domo, you and your team can channel AI and data into innovative uses that deliver measurable
[1034.04 --> 1034.72]  impact.
[1035.26 --> 1040.38]  And their all-in-one platform brings you trustworthy AI results without having to overhaul your entire
[1040.38 --> 1046.90]  data infrastructure, secure AI agents that connect, prepare, and automate your workflows,
[1047.34 --> 1052.90]  helping you and your team to gain insights, receive alerts, and act with ease through guided
[1052.90 --> 1058.00]  apps tailored to your role, and the flexibility to choose which AI models you want to use.
[1058.48 --> 1059.80]  Domo goes beyond productivity.
[1060.30 --> 1065.54]  It's designed to transform your processes, helping you make smarter and faster decisions that drive
[1065.54 --> 1073.76]  real growth, all powered by Domo's trust, flexibility, and their years of expertise in data and AI
[1073.76 --> 1074.28]  innovation.
[1074.80 --> 1075.62]  Data is hard.
[1076.02 --> 1077.50]  Domo is easy.
[1077.88 --> 1081.46]  Make smarter decisions and unlock your data's full potential with Domo.
[1081.94 --> 1086.34]  Learn more today at ai.domo.com.
[1086.34 --> 1090.18]  Again, that's ai.domo.com.
[1094.98 --> 1102.02]  Well, Kyle, one of the things that I was thinking about the other day was there's a sort of generation
[1102.02 --> 1108.46]  of developers that are growing up sort of not having any other experience than having this
[1108.46 --> 1116.72]  sort of AI-assisted experience, both on the kind of like educational debugging IDE side,
[1116.88 --> 1123.72]  but also, of course, using, you know, interesting tools, whether it be kind of vibe coding tools
[1123.72 --> 1125.12]  or other things.
[1125.34 --> 1130.68]  I was listening to the A16Z podcast and they did like a, I think it was them.
[1130.94 --> 1131.44]  I forget where.
[1131.44 --> 1138.76]  It was like somewhere they mentioned a survey of the latest cohort of Y Combinator, that cohort
[1138.76 --> 1143.36]  of companies, and they were saying like 95% of the code is AI generated.
[1144.00 --> 1152.08]  What kind of impacts are on your mind in terms of like this generation of coders that are really
[1152.08 --> 1154.60]  like this is what coding is to them?
[1154.60 --> 1161.56]  What does that mean for kind of both organizations that are hiring kind of developers out of that
[1161.56 --> 1168.60]  environment, but also, you know, new opportunities that maybe like people, people that wouldn't
[1168.60 --> 1175.72]  have maybe broken into developing cool projects or that sort of thing now have have opportunity
[1175.72 --> 1176.10]  for?
[1176.10 --> 1176.74]  Yeah.
[1176.74 --> 1176.90]  Yeah.
[1177.06 --> 1188.00]  I mean, you know, I look back on how I personally got started coding and it was because I wanted
[1188.00 --> 1193.26]  to build a video game and I feel like that's not very unique, but it's one of those things
[1193.26 --> 1195.58]  where like I enjoyed playing video games, but it's still cool.
[1196.00 --> 1196.44]  Exactly.
[1196.60 --> 1198.30]  And I wanted to go build a video game.
[1198.30 --> 1205.20]  So back in the day I went to, I probably Barnes and Noble and bought, uh, you know, the red
[1205.20 --> 1206.44]  C plus plus book.
[1206.50 --> 1208.98]  Cause you had to learn C plus plus if you wanted to write a video game.
[1209.04 --> 1213.44]  And that thing was, I don't know, 650 pages, probably, you know, that was an enormous book.
[1213.60 --> 1221.42]  And so that is a huge immediate barrier to entry to like learning because you're like, the reason
[1221.42 --> 1223.84]  I came here was to solve a problem.
[1223.84 --> 1231.70]  And if I just do 650 pages of how C plus plus works, I'll eventually get to build a text-based
[1231.70 --> 1232.28]  video game.
[1232.32 --> 1232.72]  Probably.
[1232.96 --> 1233.58]  You know what I mean?
[1234.00 --> 1239.54]  And at GitHub with like our teams and GitHub education, uh, I get to work with them and
[1239.54 --> 1245.10]  the team there on, well, how do we approach learning in this era in a way where like we
[1245.10 --> 1248.92]  can bring that problem up front, which is essentially what vibe coding is, right?
[1248.94 --> 1250.08]  I want something in the world.
[1250.20 --> 1251.62]  I want to go build it.
[1251.62 --> 1258.92]  I think the piece that is necessary to continue to learn is that problem solving piece.
[1259.06 --> 1264.52]  And I just want to make it accessible to you so you can bring a problem, something you want
[1264.52 --> 1270.50]  to go learn, but in the process of getting you to your destination, we can just expose
[1270.50 --> 1276.84]  you to the ideas around why this application works this way or why there's two files, one
[1276.84 --> 1279.54]  for the front end and one for the backend or whatever.
[1279.54 --> 1285.90]  So you're kind of learning as you go, but still focused on ultimately, you know, solving
[1285.90 --> 1288.36]  that problem that you're going after.
[1288.52 --> 1293.70]  So I don't think it's a bad thing that, you know, uh, these startups or folks online or
[1293.70 --> 1297.16]  even me on the weekend, I'm writing an app that is just for me.
[1297.16 --> 1299.20]  It's going to have a user of one in perpetuity.
[1299.20 --> 1301.78]  I just want it to get written.
[1301.78 --> 1308.34]  You know, I want it to just work, but if we can help folks learn as they go, I think we'll
[1308.34 --> 1314.82]  actually create more, you know, crafts people in a way similar to like, I always describe,
[1314.82 --> 1317.56]  you know, changing out a light switch in my house.
[1317.56 --> 1322.64]  Like if you own a home, we've all probably replaced a plug or a switch, but there's no
[1322.64 --> 1325.40]  way we're going to go into the circuit breakers on our own.
[1325.40 --> 1326.74]  We'll probably fry ourselves.
[1326.74 --> 1330.42]  And so we call in an electrician to come do that, but I'm not an electrician.
[1330.48 --> 1332.22]  I just know how to go change the light switches.
[1332.22 --> 1335.34]  And that's what I need in order to solve my problems.
[1335.62 --> 1339.84]  That's what I think learning coding and the AI era is going to be is that you can continue
[1339.84 --> 1343.52]  to start from this place of, well, I just want something and that's fine.
[1343.56 --> 1344.28]  I think that's great.
[1344.28 --> 1345.98]  And it makes the idea more accessible.
[1346.30 --> 1351.00]  I want to be able to get you to that, you know, journey person stage of, oh, okay.
[1351.00 --> 1351.88]  I know how this works.
[1351.88 --> 1354.36]  I understand variables, new technology came out.
[1354.44 --> 1356.16]  Oh, I want to try to play with that, et cetera.
[1356.70 --> 1362.80]  But it's possible that at some scale and speed, we're still going to rely on, you know, professional
[1362.80 --> 1367.78]  software developers in perpetuity running these apps, building these apps, kind of, et cetera.
[1368.16 --> 1372.68]  The real thing that's interesting to me about that stat I was talking to some teammates about
[1372.68 --> 1378.84]  is I really think there's a huge opportunity in operating the apps.
[1378.84 --> 1384.38]  And I'm a little dumbfounded that that hasn't been something that's been tackled yet.
[1385.38 --> 1390.66]  I mean, at GitHub, right, we kind of focus on like, you've got to production and like,
[1390.76 --> 1391.30]  okay, great.
[1391.34 --> 1396.86]  And then you use Century and PlanetScale and whatever, Azure and so on and so forth to run
[1396.86 --> 1397.04]  it.
[1397.40 --> 1403.64]  But I really think that in all of our probable life experiences as developers, the thing that
[1403.64 --> 1406.58]  bothers you is you get paged, you get an email, there's an error thing.
[1406.58 --> 1407.92]  And you're like, crap, what is this thing?
[1408.48 --> 1413.48]  That is another place that I feel like as Vibe Coding continues, once you run an app and
[1413.48 --> 1417.66]  you have thousands or tens of thousands or hundreds of thousands of users, I'm not on
[1417.66 --> 1420.80]  team like, oh, well, that's when you got to bring in the serious people.
[1420.90 --> 1422.22]  No, rewrite it the right way.
[1422.44 --> 1427.20]  I really think there's still space to just, okay, well, an error came in.
[1427.74 --> 1429.00]  The AI saw what it was.
[1429.04 --> 1430.14]  It resolved it.
[1430.18 --> 1430.88]  It wrote a test.
[1430.96 --> 1431.72]  The test passed.
[1431.78 --> 1433.88]  It deployed it to Canary or to a small version.
[1433.88 --> 1436.58]  And you just get a text message that's like, we fixed it.
[1436.92 --> 1442.12]  That I feel like is the next step of this era of writing, learning how to code, writing
[1442.12 --> 1448.30]  and deploying these apps versus deploying them and going, uh-oh, now I need a real pro to
[1448.30 --> 1449.12]  come in and help me out.
[1449.52 --> 1450.76]  That makes so much sense.
[1451.10 --> 1455.54]  And are you actually seeing anyone out there, kind of early people doing some of this?
[1455.54 --> 1461.20]  Is this in the wild more than just, you know, because we tend to think of AI in terms of
[1461.20 --> 1464.94]  writing the code, operating the app makes perfect sense.
[1465.28 --> 1465.76]  Who's doing it?
[1465.76 --> 1470.68]  I think the issue here is it will require us all to work together.
[1470.68 --> 1478.62]  So, I mean, when I joined GitHub, uh, oh my God, like nearly 12 years ago now, like I joined
[1478.62 --> 1483.72]  to work in the ecosystem on APIs and web hooks and how you connect everything with GitHub.
[1483.94 --> 1486.38]  And I really, that's where my passion lies.
[1486.38 --> 1491.10]  It's in, you know, the hub part, you know, of like, how do we get everything connected?
[1491.10 --> 1498.28]  And so, as I look at, you know, how quickly the industry's gotten so excited about, um,
[1498.48 --> 1506.50]  MCP and being able to connect tools together, I'm really hoping this hype wave drives into
[1506.50 --> 1512.92]  something valuable, which will be if I can bring the context of my error tracker, my database,
[1513.52 --> 1519.74]  my two cloud services, my email provider, et cetera, et cetera, all together, then I believe
[1519.74 --> 1525.06]  it becomes possible for tools to work together to solve these problems.
[1525.60 --> 1530.96]  Unfortunately, right now, each tool is attempting to solve the problem that it can see.
[1531.22 --> 1534.00]  And I do not think that's terribly valuable, right?
[1534.00 --> 1538.98]  As an end consumer, I don't want to use three AI tools to solve an error in production.
[1539.54 --> 1545.02]  I want one, you know, I want one tool to do that, or I at least want them in some future
[1545.02 --> 1548.98]  magical state where agents all actually work together and blah, blah, blah.
[1548.98 --> 1554.06]  Uh, then, you know, eventually that could also happen, but I have yet to see a tool that
[1554.06 --> 1560.20]  is kind of tackling this, I think because of the like interdependency problem that, uh,
[1560.32 --> 1567.46]  uh, a tool like that would have in this current, you know, very quick moving, uh, AI tooling
[1567.46 --> 1567.82]  state.
[1568.38 --> 1568.94]  Yeah.
[1569.14 --> 1569.34]  Yeah.
[1569.34 --> 1575.18]  I think it's, it's somewhat connected to like my concern around the ease at which all of this
[1575.18 --> 1576.94]  can get built is great.
[1576.94 --> 1580.56]  The burden on the debugging side, right.
[1580.56 --> 1586.82]  Is, is potentially, potentially kind of growing and sort of, you have all this stuff and then
[1586.82 --> 1593.02]  I guess it's more around, yeah, more around decision support in terms of, of like making
[1593.02 --> 1598.42]  good decisions based on like these overwhelming pieces of, of information because you built just
[1598.42 --> 1603.98]  so much stuff and you might not have kind of visibility and intuition around that.
[1603.98 --> 1611.92]  Um, what, what is your thought kind of, cause as more code is AI generated there, there's
[1611.92 --> 1619.96]  potentially not a good intuition even on how things are interconnected or like, Oh, this
[1619.96 --> 1621.26]  function exists, right?
[1621.28 --> 1624.08]  I didn't know that this function existed, right?
[1624.08 --> 1625.88]  I've never heard this function name.
[1626.00 --> 1627.72]  I have no context there.
[1628.36 --> 1635.26]  So, you know, what's needed from a tool standpoint to really get the proper context around that
[1635.26 --> 1641.46]  kind of decision support or whatever you want to call it for, for the developers in, in the
[1641.46 --> 1642.50]  tools that they're working in.
[1642.76 --> 1649.76]  I think, you know, for most of a modern, uh, uh, you know, history of software development,
[1649.76 --> 1654.82]  I feel like most folks are working in a relatively like highly high, uh, level language, right?
[1654.82 --> 1659.24]  A lot of abstraction ultimately, most of us aren't working in C or even lower than that.
[1659.84 --> 1667.24]  I think that in order to help us understand our code bases or our multiple code bases and
[1667.24 --> 1668.54]  multiple systems, right?
[1668.56 --> 1674.48]  Like at GitHub, I, there's no world in which as a developer who works on, uh, you know,
[1674.48 --> 1680.86]  web hooks, I'm going to understand how Git, uh, systems is ultimately going to work for
[1680.86 --> 1681.04]  me.
[1681.56 --> 1689.20]  Um, and so for me, I think the piece that I'm trying to figure out is how can we get more
[1689.20 --> 1695.26]  kind of, uh, that higher level abstraction of how the code base is working available to
[1695.26 --> 1695.52]  me.
[1695.52 --> 1701.30]  And it probably needs to be in a way that as a human, I can like understand how that works
[1701.30 --> 1709.40]  more so than, you know, this class, this file, this, whatever, I don't really need to understand
[1709.40 --> 1709.58]  that.
[1709.66 --> 1714.62]  I need to know that the web hook system is having an issue or this other piece isn't
[1714.62 --> 1718.10]  working, or there's a bug over here where we process images.
[1718.48 --> 1723.36]  And then I can kind of click down and dive in and dive in a little bit more because usually
[1723.36 --> 1729.24]  when you have a bug, even if you do understand the system, your goal is to figure out what to
[1729.24 --> 1732.20]  ignore, you know, like you're like, okay, well, it's not any of this stuff.
[1732.28 --> 1733.30]  It's gotta be over here.
[1733.64 --> 1740.30]  Uh, and I do think that similar to, you know, humans being good at describing a problem ultimately
[1740.30 --> 1742.60]  to, uh, the LLM.
[1742.70 --> 1749.42]  I think the LLM has to help us abstract up to a level where I would draw on a whiteboard,
[1749.42 --> 1755.00]  you know, and then let me double click in and understand more deeply what's ultimately
[1755.00 --> 1755.54]  going on.
[1756.06 --> 1756.18]  Yeah.
[1756.42 --> 1756.62]  Yeah.
[1756.70 --> 1758.46]  That, that's a, that's a great point.
[1758.46 --> 1765.74]  It reminds me of like the sort of peak microservices days and, you know, everything, everything
[1765.74 --> 1768.02]  expanded into it.
[1768.12 --> 1772.38]  You know, we're, I was at a small company at the time and I don't know how many microservices
[1772.38 --> 1775.14]  we had and, you know, we had alerting set up, right.
[1775.26 --> 1779.98]  But then the alert would go off and, you know, everything was dependent on everything else.
[1779.98 --> 1781.78]  So all the alerts would go off.
[1781.88 --> 1784.70]  It was either none of the alerts go off or all of the alerts go off.
[1784.70 --> 1786.62]  And then you're like, well, I give up.
[1786.62 --> 1789.04]  I like, where do I even hop in here?
[1789.58 --> 1789.74]  Yeah.
[1789.88 --> 1794.48]  It seems like a, seems like a big, uh, big opportunity.
[1794.48 --> 1800.84]  Um, I guess in terms of the, you know, and I want to talk about, uh, co-pilot, um, specifically
[1800.84 --> 1806.38]  here in a second, but just in terms of the IDE specifically and at a more general level,
[1806.38 --> 1814.08]  um, how do you see kind of the, the IDE, you know, obviously people are trying various
[1814.08 --> 1819.78]  things with, um, what, both what co-pilot's doing and cursor and windsurf and all of these
[1819.78 --> 1821.80]  things, all hands and all of that.
[1822.34 --> 1826.44]  How do you see that interface morphing over time?
[1826.44 --> 1832.78]  Do you, do you see that kind of still kind of being recognizable in a year and a half
[1832.78 --> 1839.32]  or two years or, or being something kind of completely foreign maybe to, to certain people?
[1840.12 --> 1848.20]  I'm hoping that, you know, in the next, honestly, six months that a startup just because of the
[1848.20 --> 1855.32]  nature of how these things move, you know, can kind of show us a future state that is in
[1855.32 --> 1857.30]  some ways backwards compatible.
[1857.64 --> 1860.36]  So what I mean by that is like, GitHub has had workspace.
[1860.68 --> 1861.72]  We kind of demoed Spark.
[1861.88 --> 1868.98]  All of these are kind of the code is stepping into the background, uh, to show me the prompts,
[1869.10 --> 1873.10]  the thinking, and like a preview of what ultimately is being built.
[1873.46 --> 1878.48]  But right now in IDEs, all the ones you've mentioned, and generally all of them that aren't
[1878.48 --> 1883.40]  the sort of like idea to app tools, like lovable, bold, v0, et cetera.
[1883.40 --> 1887.24]  They all are still staying code forward.
[1887.40 --> 1890.94]  And I think it's necessary, you know, in order to attract an audience right now.
[1891.30 --> 1895.34]  Otherwise that kind of, you get pushed aside as like a, it's a fun toy.
[1895.54 --> 1898.02]  It's not really a tool that I'm going to use as a professional dev.
[1898.34 --> 1904.72]  I do think in the future though, I'm working with the app or the, you know, the web app,
[1904.80 --> 1906.92]  the actual, you know, iOS app or whatever.
[1907.32 --> 1911.18]  Every time I'm writing code, like I'm writing code, I'm writing a test, and then I'm going to
[1911.18 --> 1912.42]  go and touch the app.
[1912.66 --> 1916.70]  That last step is usually where I figure out if I'm right or not.
[1916.78 --> 1921.90]  And when something's wrong, why do I have to keep bouncing back and forth between the result,
[1922.04 --> 1924.92]  the thing I'm trying to actually build in code?
[1925.12 --> 1927.74]  And so there's a couple of tools out there now, right?
[1927.78 --> 1929.66]  That are kind of showing me the preview.
[1929.66 --> 1936.14]  And as I adapt that, like the code is changing and it gets to the most, like maybe not the
[1936.14 --> 1940.94]  most, but one of the most interesting problems to me in this AI era, which is like the magic
[1940.94 --> 1941.92]  mirror problem.
[1942.12 --> 1949.26]  How do I continuously change a representation and have the code or the text or the readme
[1949.26 --> 1952.82]  or the spec match what I'm doing in the representation?
[1953.28 --> 1955.72]  So yes, moving pixels is pretty easy, right?
[1955.72 --> 1958.02]  I'm going to go, oh, I changed this position or whatever.
[1958.22 --> 1962.10]  But what if I ask it to do something completely different, right?
[1962.28 --> 1965.08]  How do I make sure that the code always matches that?
[1965.38 --> 1968.82]  And I think there's a couple of really interesting like attempts at that.
[1968.92 --> 1976.44]  But if and when models, tech, specs, et cetera, get better there, then I think IDEs will broadly
[1976.44 --> 1981.10]  be, you know, the prompts, the preview, the thinking.
[1981.10 --> 1986.52]  So I can kind of correct and adapt and then probably some way for me to, you know, click
[1986.52 --> 1991.76]  on a part of the app and not go make it blue, which is the demo where that we all see, but
[1991.76 --> 1993.70]  instead be, well, no, no, no.
[1993.74 --> 1999.12]  I want this to be like a dynamic view that shows me this whole other, you know, basically
[1999.12 --> 2001.56]  another control or another view, another app or whatever.
[2001.74 --> 2003.80]  And it'll code it right there and show it to me.
[2004.10 --> 2008.78]  Then I think we'll be even faster than we think we are kind of like right now, because
[2008.78 --> 2011.90]  instead we're going and manipulating by a prompting, you know, it'll listen to turn.
[2011.98 --> 2014.58]  Okay, well, I'm going to convince you AI to go do this thing.
[2015.22 --> 2019.86]  But it feels like we're still a couple of clicks away because there's some actual hard
[2019.86 --> 2026.86]  problems to solve to let you go back and forth very, very easily because most companies
[2026.86 --> 2031.84]  are still like working in code ultimately by a CI build systems deploy, et cetera.
[2031.84 --> 2036.04]  So we want to make sure that everything matches up in the code base, not just in the app
[2036.04 --> 2039.08]  or the visual representation of what we're trying to build.
[2040.26 --> 2043.88]  So, you know, as we've been talking about code assistance and where things are going
[2043.88 --> 2048.04]  and stuff, I want to get more specific for a moment because we got you here.
[2048.32 --> 2048.52]  Sure.
[2048.74 --> 2056.36]  Talk a bit about GitHub Copilot specifically and kind of maybe as a starting point on this,
[2056.86 --> 2062.14]  kind of talk a little bit about, you know, what the current state of GitHub Copilot is,
[2062.14 --> 2069.72]  kind of how the user experience is now and as a starting, you know, toward what tomorrow
[2069.72 --> 2077.14]  and the day after is going to look like and how you see that affecting, you know, IDEs,
[2077.42 --> 2083.90]  adoption of the technology, the whole thing going forward and kind of start a path into the future
[2083.90 --> 2086.32]  from here on that particular item.
[2086.84 --> 2087.54]  Yeah, yeah, for sure.
[2087.54 --> 2096.12]  I mean, you know, I feel like most folks are familiar with Copilot 1.0, we'll call it, right?
[2096.22 --> 2099.72]  Like everyone's like, okay, so it does code completions and cool.
[2100.14 --> 2106.70]  And, you know, in the last six months or so, we went from the, yeah, it does code completions
[2106.70 --> 2113.56]  to, you know, now you can choose to use a variety of models usually within a day, if not the same
[2113.56 --> 2115.56]  day of them coming out.
[2115.56 --> 2118.40]  There's chat, you know, the ability to ask these questions.
[2118.76 --> 2123.74]  Now there's agent mode available in VS Code Insiders, which allows you to have that experience
[2123.74 --> 2129.36]  of describing a problem, watching it do the work, asking it to do something else, working
[2129.36 --> 2135.24]  across multiple files, the context of your entire repository, not just the file that's open
[2135.24 --> 2141.36]  and make these sort of much broader, you know, changes to your application in the IDE still.
[2141.36 --> 2147.96]  As part of sort of the overall Copilot family, we continue to do these explorations like Workspace
[2147.96 --> 2151.20]  and Spark, where we're sort of going like we were just talking about.
[2151.74 --> 2159.36]  What does it mean for me to plan out what I want to build and then let Copilot as an agent
[2159.36 --> 2165.68]  go and figure out all the steps that need to be taken across multiple files, multiple repos
[2165.68 --> 2167.40]  to ultimately kind of build that app.
[2167.46 --> 2173.72]  So the goal, instead of just saying, give me some lines of code or give me a whole, you know, method
[2173.72 --> 2178.10]  is now starting with, well, what problem are you trying to solve?
[2178.38 --> 2184.14]  You know, most of our devs are working in, you know, major open source projects or big companies
[2184.14 --> 2185.86]  or they're starting to learn, etc.
[2185.86 --> 2191.54]  And so we want to be able to let folks come from a problem that could be a prompt in chat.
[2191.66 --> 2193.12]  That could be a GitHub issue.
[2193.44 --> 2196.84]  That could be a pull request that's already open and you think that there's a piece of
[2196.84 --> 2197.48]  it that's missing.
[2197.82 --> 2203.50]  We want you to be able to just state what you're looking for, you know, and then let kind of
[2203.50 --> 2205.62]  Copilot take it from there.
[2205.62 --> 2211.20]  So we kind of shared a little bit of a, you know, a preview of that path forward where,
[2211.34 --> 2215.88]  you know, we've all gotten bugs and we put them in our issue tracker and it's like not
[2215.88 --> 2216.34]  interesting.
[2216.48 --> 2222.24]  It's going to take a fair bit of time to solve, you know, or to resolve and kind of reposing
[2222.24 --> 2227.42]  the question, like, why not just assign that to Copilot and let them work just like a dev
[2227.42 --> 2231.82]  would work, you know, trying it out, running the test, the test failed, commenting what they
[2231.82 --> 2235.96]  think they got wrong, continuing to go and then asking for a human review.
[2237.02 --> 2241.38]  That's something that, you know, again, we're trying to model it after that experience of
[2241.38 --> 2246.72]  anyone on your team versus treating it like this magical tool that's, you know, always
[2246.72 --> 2250.66]  going to get something perfectly right instead, just like you would explain with another dev
[2250.66 --> 2250.96]  friend.
[2251.20 --> 2255.86]  You can go in and help Copilot understand or just go, yep, that's totally right.
[2256.14 --> 2259.80]  Just change these two things and Copilot will do it and ultimately deploy.
[2259.80 --> 2264.48]  So when we're sort of looking at the code creation process, which generally happens in
[2264.48 --> 2267.28]  IDEs, I think that's a big part of it.
[2267.78 --> 2274.66]  The part that's in some ways like more exciting for me as a dev is all the other pieces of
[2274.66 --> 2275.36]  being a dev.
[2275.44 --> 2281.08]  Like I kind of said, you know, like when I'm writing or when I'm reviewing code, I'm a human
[2281.08 --> 2281.44]  being.
[2281.48 --> 2286.58]  And so I may not remember the exact like method signature of something, but this doesn't seem
[2286.58 --> 2287.72]  like the best way.
[2287.92 --> 2293.22]  And so to be able to work with Copilot in those moments or to let Copilot kind of just
[2293.22 --> 2297.12]  tell me, yo, Kyle, this isn't quite right based on what, you know, how I know you work.
[2297.22 --> 2302.98]  And so it can show it to me and just let me accept the change or in actions and CI, why
[2302.98 --> 2309.74]  not let it fix the failures that come through or let me define my actions workflow just by
[2309.74 --> 2313.30]  talking to AI versus having to go and build it myself.
[2313.30 --> 2319.60]  And so, you know, the real kind of magic I think of Copilot over the next year is how
[2319.60 --> 2326.12]  can we find moments both in creating code, but also in reviewing it, building it, testing
[2326.12 --> 2331.96]  it, deploying it and let Copilot probably in a much more agent fashion, you know, having
[2331.96 --> 2336.92]  a multitude of Copilot agents that can work together and use the context, not just of your
[2336.92 --> 2342.48]  code, all the code in your organization, but also the tools that you also use.
[2342.48 --> 2349.00]  If Copilot can reach out and get the information from them using MCP or a Copilot extension, then
[2349.00 --> 2353.82]  suddenly it can take over the tasks that you probably didn't want to do in the first place,
[2353.82 --> 2358.00]  to be honest, you know, less so those sort of interesting novel on building my business
[2358.00 --> 2359.34]  around this tasks.
[2359.86 --> 2361.38]  It'll help you do all those things.
[2361.64 --> 2366.50]  But at the very least, let's let it take away the kind of rote pain work that I think,
[2366.50 --> 2369.94]  you know, every dev kind of has in their backlog, but it's been sitting there for the last,
[2370.06 --> 2374.22]  you know, two years, three years or however long it's artisanal now.
[2374.76 --> 2380.44]  And so Copilot's, you know, really, really trying to allow you to just go from problem
[2380.44 --> 2386.22]  to app or, you know, problem to fix via these new experiences in the IDE and VS Code in particular,
[2386.44 --> 2392.40]  but also now in more IDEs like we announced, you know, Xcode now has chat.
[2392.40 --> 2394.90]  A bunch of other editors also continue to have chat.
[2395.02 --> 2398.40]  So if you're in those environments, you can still use, you know, the power of Copilot.
[2398.64 --> 2404.38]  And then in GitHub.com, you'll see all those new experiences coming in, like code review,
[2404.78 --> 2410.92]  being able to use an agent to, you know, build an actual solution for you from an issue
[2410.92 --> 2417.40]  and kind of fix the other, you know, 80% almost of dev time inside the SDLC process
[2417.40 --> 2421.42]  that they're working in versus only focusing on that editor workflow.
[2422.02 --> 2428.96]  How do you think, I realize this is probably a complex question, but I get it posed to me a lot.
[2429.78 --> 2435.30]  So I figure you're probably the best one to answer or at least have an opinion.
[2435.56 --> 2441.70]  But oftentimes I get a lot of questions around this side of, I mean, even in what you just described,
[2441.70 --> 2447.12]  kind of here's an issue, generate a fix, you know, agents that can do this,
[2447.38 --> 2452.70]  especially around like the open source community and code generation.
[2452.70 --> 2461.54]  How does this kind of influence, you know, licensing and kind of the ecosystem of open source over time from your perspective?
[2462.20 --> 2466.22]  Yeah, I mean, you know, with Copilot and what it's doing, ultimately,
[2466.22 --> 2472.56]  that code that is being generated, whether that be generated for, you know, your business or for an open source project,
[2472.56 --> 2480.36]  we have tools in Copilot that you can basically say, hey, if this matches any public code, don't give me a match.
[2480.36 --> 2486.94]  And then it won't, you know, it's not going to match anything from the public code base that it has access to.
[2487.46 --> 2492.58]  And so in general, for folks that are most worried about, you know, well, where's this code coming from?
[2492.58 --> 2498.50]  Is it using code and generating code that looks like other public repos that I don't want to match on?
[2498.70 --> 2501.08]  It can do that just by setting a setting.
[2501.26 --> 2507.08]  And for some of our sort of SKUs of Copilot, we require that to be on.
[2507.20 --> 2512.54]  You know, you have to have that on in order to sort of protect yourself if there's any concern around, yeah,
[2512.56 --> 2514.52]  where is this code coming from? What's the license, et cetera?
[2514.92 --> 2522.00]  I think as we continue to move forward more and more and as we're looking at all the tools, you know, out in the market,
[2522.00 --> 2531.64]  as developers, I think we can all kind of intuit that there's only so many novel ways to write the same exact thing.
[2531.82 --> 2538.22]  And so you'll sometimes hear, or I should say I'll sometimes hear, particularly from open source devs, you know, going like,
[2538.60 --> 2540.58]  oh, well, Copilot won't write this for me.
[2540.84 --> 2544.70]  You know, it's not going to get, why won't it give me the answer?
[2544.70 --> 2552.30]  And the answer is because that loop that you're trying to build is complex enough that it triggers us to look for a match.
[2552.86 --> 2560.00]  And because we have that blocking on, because, you know, you've turned it on or the business has, it won't give you a return.
[2560.34 --> 2569.36]  And so it really depends on the business's personal preference or the user's personal preference on whether they want that public matching to come back to you.
[2569.36 --> 2578.30]  But in general, especially as we get into agent mode and we get into, you know, the ability to kind of create close to an entire app, you know,
[2578.34 --> 2586.22]  or at least a very complex set of files, you know, Copilot's going to iterate and iterate and give you something that, again,
[2586.28 --> 2588.88]  doesn't match that public set if you have it turned off.
[2588.94 --> 2592.58]  But ultimately, you know, try to solve that problem for you.
[2592.58 --> 2600.64]  Every other tool has a different set of, you know, obligations like this or whether it's going to use the suggestions, etc.
[2601.00 --> 2609.52]  But I think at the end of the day now, our goal is really to make sure that everyone's empowered to use this tool.
[2609.62 --> 2616.82]  They can choose, you know, how they want to use it and what kind of responses and suggestions they want back.
[2616.82 --> 2623.58]  And that's why we give Copilot, you know, for free to students and maintainers of very popular open source projects.
[2623.58 --> 2629.40]  And we're trying to find more ways to just make sure everyone can have the tool if they want to use it.
[2629.46 --> 2633.40]  Now Copilot free, basically everyone can use at least a portion of Copilot.
[2634.94 --> 2642.98]  And then kind of let them decide for themselves what they're most comfortable with as we keep going down this, you know, AI future of coding.
[2642.98 --> 2651.64]  As we start to wind up here, we often will ask guests kind of, you know, what we refer to as the future question kind of going forward now.
[2651.74 --> 2654.10]  But we have covered so much ground.
[2654.40 --> 2656.24]  I'm going to ask you that.
[2656.38 --> 2672.46]  And I will say that as you look into the future and you're kind of, you know, we've covered everything from AI in terms of productivity with code to the developer experience to the GitHub Copilot product itself and a bunch of tangential stuff.
[2672.46 --> 2674.40]  You go wherever you want to go.
[2674.40 --> 2686.76]  Where do you think as you are kind of finishing up for the day and you get through the crush and you have a glass of wine or maybe you're getting in bed for the night and your brain's kind of spinning in open mode, you know, where you're being creative.
[2687.02 --> 2695.20]  Where does your brain go and where all this is going to go for us and what kinds of things might be next that we haven't already talked about?
[2695.36 --> 2699.40]  You know, what would you like to see aspirationally coming down the pike?
[2699.40 --> 2702.46]  Take us into your brain for this last question.
[2702.68 --> 2703.26]  Yeah, for sure.
[2703.44 --> 2709.82]  So, you know, if I were a good corporate citizen, I'd be pitching you on something from GitHub.
[2709.98 --> 2711.18]  But that's not the honest answer.
[2711.26 --> 2712.82]  And we're all developers in some way.
[2712.94 --> 2714.08]  And so the people will understand.
[2714.34 --> 2728.14]  I think true ambient AI that understands me and has access to my information and what I choose is the thing I'm most interested in coming right now.
[2728.14 --> 2731.30]  You know, I think we've seen the power of the LLM.
[2731.58 --> 2734.52]  And I don't think we've honestly tapped into the vast majority of it.
[2734.60 --> 2736.60]  We're still broadly speaking in chat models.
[2736.74 --> 2738.92]  And that's incredibly boring to me.
[2739.06 --> 2741.30]  You know, I get it and why it's that way.
[2741.30 --> 2750.34]  But like, I really think the next step is going to be more about if you have all of my emails, my calendar, all the things that I'm currently sharing.
[2750.34 --> 2752.10]  That could be my purchases on Amazon.
[2752.10 --> 2758.54]  That could be, you know, access to sort of my doorbell camera and you see what I'm wearing on the way out, etc.
[2758.54 --> 2764.44]  There's all these experiences where we go to Google and we go, what's the weather today?
[2764.44 --> 2768.94]  Or we ask our assistant, like, you know, a tool at the house or whatever.
[2769.18 --> 2775.30]  Or more complex, you know, like, when's the last time I, what was the last episode I listened to of Practical AI?
[2775.52 --> 2776.34]  And what was it about?
[2776.50 --> 2778.20]  Because I'm going into a podcast recording.
[2778.34 --> 2781.14]  And I want to remind them that Matt Collier is a friend of mine.
[2781.14 --> 2783.60]  And he did a great job with Sidekick and kind of so on and so forth.
[2783.60 --> 2794.54]  But that ambient AI or that ambient intelligence where we're not, like, invoking an assistant, it's just telling me what I need to know when I need to know it because it has all that data about me.
[2795.52 --> 2796.48]  Is I want it.
[2796.58 --> 2798.08]  I desperately, desperately want it.
[2798.14 --> 2801.90]  And I think there's a couple of, like, really interesting attempts at this.
[2801.90 --> 2812.00]  Like, there was Rewind AI that was a Mac app and they kind of pivoted into this Limitless tool, which is like a wearable plus all the apps that has the same idea.
[2812.00 --> 2816.94]  There's been a couple of, I won't, like, name them, but a memed versions of this thing.
[2816.96 --> 2818.90]  And that's not really kind of what I mean.
[2818.90 --> 2826.76]  I really mean the ability to finish my thought because you have all the context that I need.
[2826.86 --> 2833.50]  And I didn't have to set up 55 integrations or IFTT or Zapier to move all my data into a single place.
[2833.58 --> 2836.24]  So that way GPT-4-5 can answer it or whatever.
[2836.40 --> 2836.78]  You know what I mean?
[2837.08 --> 2839.06]  And I don't think we're that far off.
[2839.06 --> 2848.54]  I think that I find it incredibly interesting that, like, iOS and Apple Intelligence have been attempting to come up with what they're next up on.
[2848.72 --> 2858.70]  But I actually have some hope that they may solve this because they haven't shipped their solutions, you know, and they kind of publicly are talking about how it may take longer than they thought.
[2859.02 --> 2861.80]  The biggest gap to this isn't LLMs.
[2862.04 --> 2863.60]  It isn't connecting all the data.
[2863.74 --> 2864.56]  It's privacy.
[2864.56 --> 2871.64]  I don't want all of this data sitting in an arbitrary startup's cloud or wherever, you know, to do this.
[2871.92 --> 2879.36]  For as powerful as all of our laptops are, there's still limits, you know, about how much it can do and how much data it has and what the models it can run, etc.
[2879.36 --> 2895.48]  I think someone that can take all the information, do it in a way that I'm personally comfortable with from a privacy perspective, both for me and for anyone that is inherently, you know, like getting data sent from them into this tool, you know, like if I was recording my screen right now, for example.
[2895.48 --> 2909.80]  To be able to be able to have all that and actually help my day to day life in a real way, you know, and reminding me of what's coming up and helping me do those things without the personification of a hey Siri or hey Alexa situation, just text.
[2909.80 --> 2936.04]  That's what I sit up thinking about at night and how to crack the privacy nut, because I think that'll be required for us to do this in a way that is both really powerful, but also, I think, morally correct and, you know, safe for all of us to benefit from versus accidentally slipping into a even worse dystopia by letting all this information kind of, you know, get out into the wild in a way that we don't want.
[2936.04 --> 2937.92]  That's a great way to end it, Kyle.
[2938.16 --> 2942.10]  I also have hopes for similar things.
[2942.90 --> 2945.50]  We end on the same wavelength again.
[2945.74 --> 2947.06]  Really appreciate you joining.
[2947.26 --> 2948.00]  Thank you so much.
[2948.34 --> 2949.32]  Thank you so much for having me.
[2956.50 --> 2957.42]  All right.
[2957.66 --> 2959.52]  That is our show for this week.
[2959.52 --> 2965.84]  If you haven't checked out our ChangeLog newsletter, head to changelog.com slash news.
[2966.04 --> 2968.30]  There you'll find 29 reasons.
[2968.54 --> 2971.88]  Yes, 29 reasons why you should subscribe.
[2972.36 --> 2973.74]  I'll tell you reason number 17.
[2974.08 --> 2977.08]  You might actually start looking forward to Mondays.
[2977.24 --> 2979.94]  Sounds like somebody's got a case of the Mondays.
[2980.36 --> 2984.90]  28 more reasons are waiting for you at changelog.com slash news.
[2985.06 --> 2990.82]  Thanks again to our partners at fly.io to Breakmaster Cylinder for the beats and to you for listening.
[2991.02 --> 2993.86]  That is all for now, but we'll talk to you again next time.
[2996.04 --> 2999.52]  Join Liebна-
[3003.52 --> 3005.40]  Deadline, Subtitle for the paid while you're on the Facebook page.
[3005.50 --> 3006.08]  And yes, we'll see you again next time.
[3006.08 --> 3006.92]  They can leave you again next time.
[3006.92 --> 3008.82]  We'll see you today.
[3008.88 --> 3011.46]  You just keep it in line.
[3011.52 --> 3012.82]  It really makes a perfect account.
[3012.82 --> 3013.52]  I love you today.
[3013.52 --> 3014.24]  Got it in love.
[3014.24 --> 3014.74]  Well back to you now.
[3014.94 --> 3015.64]  We'll see you next time.
[3015.64 --> 3016.90]  Yes, and after you guys have fun to breakiras some of your teammates.
[3016.92 --> 3018.12]  We'll see you later.
[3018.12 --> 3018.66]  See you guys later.
[3018.80 --> 3020.00]  Bye-bye.
[3020.00 --> 3020.76]  Yeah.
[3021.00 --> 3021.24]  Bye.
[3021.24 --> 3021.98]  Bye.
[3022.48 --> 3023.06]  Bye.
[3023.30 --> 3024.24]  Bye.
