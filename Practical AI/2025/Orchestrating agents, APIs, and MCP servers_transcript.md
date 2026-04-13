[0.00 --> 10.06]  Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 --> 11.46]  and accessible to all.
[11.46 --> 14.48]  If you like this show, you will love The Change Log.
[14.70 --> 19.52]  It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 --> 21.38]  talk show for your weekend enjoyment.
[21.84 --> 25.82]  Find us by searching for The Change Log wherever you get your podcasts.
[26.32 --> 28.36]  Thanks to our partners at Fly.io.
[28.36 --> 31.10]  Launch your AI apps in five minutes or less.
[31.40 --> 33.40]  Learn how at Fly.io.
[44.18 --> 48.24]  Well, welcome to another episode of the Practical AI podcast.
[48.74 --> 50.42]  This is Daniel Widenack.
[50.50 --> 52.62]  I'm CEO of Prediction Guard.
[52.62 --> 60.98]  And I'm really excited today to dig a little bit more into Gen AI orchestration, agents,
[61.22 --> 67.50]  coding assistance, all of those things with my guest, Pavel Veller, who is Chief Technologist
[67.50 --> 68.64]  at EPAM Systems.
[69.10 --> 69.92]  Welcome, Pavel.
[70.06 --> 70.78]  Great to have you here.
[71.10 --> 71.32]  Thank you.
[71.40 --> 71.76]  Hello, hello.
[72.32 --> 73.08]  Yeah, yeah.
[73.44 --> 75.46]  Well, I mean, there's a lot of topics.
[75.66 --> 80.86]  Even before we kicked off the show, we were chatting in the background about some really
[80.86 --> 81.88]  interesting things.
[81.98 --> 87.18]  I'm wondering if you could just kind of level set us of people may or may not have heard
[87.18 --> 88.10]  of EPAM.
[88.40 --> 94.26]  I think one of the things that I saw that you all were working on was this Gen AI orchestration
[94.26 --> 95.52]  platform dial.
[95.96 --> 100.66]  Maybe before we get into some of the specifics about that and other things that you're interested
[100.66 --> 105.52]  in, maybe just give us a background of what EPAM is.
[105.72 --> 110.74]  I know you mentioned even in our discussions that some of what you're doing right now maybe
[110.74 --> 114.16]  wouldn't have even been possible a couple of years ago.
[114.36 --> 115.80]  And so things are developing rapidly.
[116.06 --> 120.70]  Just level set the kind of background of this area where you're working.
[121.10 --> 121.18]  Sure.
[121.28 --> 121.62]  Yeah, yeah.
[121.62 --> 125.02]  So EPAM is a professional services organization.
[125.26 --> 125.76]  We're global.
[125.76 --> 131.54]  We're in 50 something countries, 50,000 people globally work with clients.
[131.70 --> 136.08]  We have been for, I think, 32 years to date.
[136.50 --> 139.24]  So we do a lot of different things, as you can imagine.
[139.48 --> 144.98]  And what I was mentioning about doing things that would not be possible is doing things
[144.98 --> 146.14]  with Gen AI today.
[146.40 --> 148.40]  We do a lot of work for our own clients.
[149.00 --> 152.78]  We also do work for ourselves, applying the same technology.
[152.78 --> 158.90]  Because EPAM historically as a company has been running on software that we ourselves built.
[159.16 --> 164.78]  The philosophy has always been that things that do not differentiate you, like an accounting
[164.78 --> 168.36]  software or like CRM, you would go and buy off the shelf.
[168.86 --> 175.18]  Things that differentiate you, how we actually work, how we operate, how we execute projects,
[175.34 --> 180.08]  how we hire people, how we create teams, how we deploy teams.
[180.08 --> 185.44]  All of that software has always been our own since as early as late 90s.
[186.14 --> 188.74]  And we keep iterating on that software for ourselves.
[188.96 --> 191.72]  And that software today is very much AI first.
[192.02 --> 197.34]  And a lot of things we do, we do with AI and really do because AI in its current form exists.
[198.08 --> 198.10]  Interesting.
[198.10 --> 198.50]  Yeah.
[198.64 --> 207.64]  And how I guess does, you know, I think when we initially kind of were prompted to reach
[207.64 --> 212.14]  out to you, part of it was around this orchestration platform.
[212.30 --> 217.20]  So talk a little bit maybe generally, not necessarily about the platform per se, although we'll get
[217.20 --> 221.02]  into that, but just Gen AI orchestration generally.
[221.28 --> 224.40]  So you talked about, you know, some of these things that are becoming possible.
[224.40 --> 227.48]  Where does orchestration fit in that?
[227.54 --> 229.24]  And what do you mean by orchestration?
[229.78 --> 231.50]  You probably think of dial.
[231.94 --> 233.22]  You can Google it.
[233.42 --> 237.12]  We do a lot of applied innovation in general as a company.
[237.20 --> 241.52]  And this is one of the good examples of applied innovation to AI.
[242.30 --> 248.52]  The best way to think of dial would be, you guys all know ChatGPT, right?
[248.62 --> 250.46]  ChatGPT isn't an LLM.
[250.46 --> 255.78]  It's an application that connects to an LLM and gives you certain functionalities.
[255.96 --> 258.68]  It can be as simple as just chatting and asking questions.
[258.68 --> 263.56]  It can be a little more complex, uploading documents and speaking to them, like talk to
[263.56 --> 264.16]  my documents.
[264.48 --> 269.60]  It can be even more complex when you start connecting your own tools to it, right?
[269.70 --> 275.64]  We see our clients not only do this, but also want something like this for their own business
[275.64 --> 276.14]  processes.
[277.02 --> 282.32]  And this orchestration engine becomes, how do I make it so that I don't have 20 different
[282.32 --> 286.12]  teams doing the same similar things over and over again in their own silos?
[286.64 --> 294.62]  How do I connect my teams and their EIs and their thoughts and results into a consolidated
[294.62 --> 295.64]  ecosystem?
[295.64 --> 302.42]  And it's likely because of Gen AI and because of what we can do with conversation and text
[302.42 --> 304.26]  becomes sort of conversation first.
[304.62 --> 309.50]  You can think of conversation first application mashups almost, right?
[309.52 --> 312.48]  Like you talk, express a problem.
[313.00 --> 314.76]  And what comes back is not just the answer.
[314.88 --> 317.42]  Maybe what comes back is UI elements.
[318.00 --> 322.16]  Buttons you can click, forms you can fill out, things you can do, as well as things that
[322.16 --> 324.34]  are done for you by agents automatically.
[324.34 --> 329.66]  So Dial, in that sense, is, well, by the way, it is open source.
[329.82 --> 332.60]  You guys can also go look, download and play with it.
[332.66 --> 340.64]  But it is a chat GPT-like conversational application that has many capabilities that go beyond.
[341.06 --> 342.18]  We have Dial apps.
[343.72 --> 345.94]  They predate MCP.
[346.62 --> 351.72]  But the idea is that you, so Dial itself has a contract, an API that you implement.
[351.72 --> 357.28]  You basically come back with a streaming API that can receive a user prompt.
[357.76 --> 358.72]  And whatever you do, you do.
[358.80 --> 362.00]  And you come back to Dial with not just text.
[362.34 --> 367.82]  It's a much more powerful payload with UI elements, interactive elements, and things that
[367.82 --> 371.24]  Dial will display for me, the user, to continue my interaction.
[371.74 --> 377.00]  And Dial becomes this sort of center mass of how your company can build, implement, integrate
[377.00 --> 381.18]  AI into this single point of entry.
[382.14 --> 388.62]  And then Dial goes, well, from day one, Dial was a load balancing model agnostic proxy.
[389.24 --> 389.28]  Right?
[389.36 --> 391.56]  So every model, every deployment has limits.
[391.98 --> 395.58]  You know, tokens per minute, tokens per day, whatever, requests per minute.
[395.58 --> 402.68]  You'll likely, if you're a large organization with large, different workflows, your AI appetite
[402.68 --> 405.56]  will go well beyond a single model deployment.
[406.14 --> 408.28]  You'd like to load balance across multiple.
[408.82 --> 414.08]  And then you'd like to try different models, ideally with the same API for you, the consumer.
[415.10 --> 416.52]  So Dial started like that.
[416.92 --> 420.94]  Started like load balancing, model agnostic proxy, single point of entry.
[421.48 --> 424.18]  We can log everything that is prompted in the organization.
[424.18 --> 429.48]  We can do analysis on that separately, because that's very helpful to know what kind of problems
[429.48 --> 430.84]  your teams are trying to solve.
[431.40 --> 435.98]  And then it evolved into this application hosting ecosystem.
[436.78 --> 440.90]  Now it's evolving clearly towards what MCP can bring in, because now you can connect a
[440.90 --> 443.42]  lot more things to it through MCP.
[444.34 --> 447.56]  So I think it's running at like 20-something clients by now.
[448.28 --> 449.60]  So just a couple of follow-up questions.
[449.60 --> 456.14]  It's been in the news a lot, but just so people understand, if maybe they haven't seen it,
[456.44 --> 463.70]  what are you referring to with MCP and kind of how that relates to some of this API interface
[463.70 --> 464.62]  that you're enabling?
[465.14 --> 466.48]  Well, the easiest is to Google it.
[466.64 --> 467.24]  You can Google it.
[467.28 --> 467.94]  You're going to find it.
[468.00 --> 468.70]  It's on Claude.
[470.00 --> 474.00]  Let me tell you how I think about this, because not what it actually...
[474.00 --> 474.44]  That's helpful.
[474.66 --> 474.80]  Yeah.
[474.80 --> 476.46]  Yeah, I think about it in a very simple term.
[476.64 --> 483.56]  So MCP allows to connect the existing software world to LLMs.
[484.12 --> 486.28]  In a way, think like...
[486.28 --> 491.04]  And I don't want to hype it too much, because it's not yet a global standard or anything.
[491.20 --> 492.82]  It's very early, early, early days.
[492.98 --> 494.30]  It's been months, right?
[495.16 --> 500.80]  But what, let's say, HTML and browsers and HTTP, they enabled to connect...
[501.26 --> 502.18]  Well, us.
[502.40 --> 504.40]  People to software all over the world.
[504.92 --> 508.20]  MCP does that, but for LLMs.
[508.76 --> 510.02]  So today, if I want...
[510.02 --> 518.42]  If I today want to be able to prompt my application that is in front of an LLM to do things with
[518.42 --> 522.88]  additional tools, let's say I wanted to be able to search file system based on what I
[522.88 --> 525.82]  prompted and find a file and something in that file, right?
[525.86 --> 528.76]  So my application needs to be able to do that.
[529.48 --> 530.58]  My option is what?
[530.58 --> 532.30]  I can write that function.
[532.30 --> 536.34]  I can then tell my LLM, hey, here's this function you can call if you want to.
[536.66 --> 537.00]  Call it.
[537.06 --> 538.42]  I'm going to call it for you.
[538.80 --> 539.08]  Great.
[539.14 --> 539.82]  That's one function.
[540.20 --> 541.58]  What if I need to do something else?
[541.60 --> 545.52]  I want to go talk to my CRM system and get something out of there.
[545.70 --> 546.90]  I'm going to write that function.
[546.90 --> 552.04]  If I'm going to write all the functions I can think of, it's going to take me years, probably
[552.04 --> 553.00]  hundreds of years.
[553.68 --> 559.06]  So instead, what I can do today, I can say, hey, my LLM application, can you talk a protocol?
[559.48 --> 561.10]  Because there's a protocol called MCP.
[561.10 --> 566.16]  I'm going to bring you MCP servers that other people have built for my CRM system, for my
[566.16 --> 567.74]  file system, for my CLI.
[568.26 --> 569.82]  There are MCP servers for everything.
[570.20 --> 575.80]  IntelliJ exposes itself as an MCP server to do things that IDE can do.
[576.12 --> 577.94]  Now you can orchestrate those things through LLM.
[577.94 --> 584.50]  So you connect all the MCP servers through an MCP client, this application in front of
[584.50 --> 587.92]  LLM, to LLM, expose the tools to LLM.
[588.18 --> 590.84]  LLM can now ask the client to call a tool.
[591.60 --> 594.50]  And through this MCP protocol, the client calls the server.
[594.64 --> 597.24]  The server does the function that has been written in that server.
[597.68 --> 599.10]  And boom, LLM gets results.
[599.72 --> 602.86]  So it's this connective tissue that did not exist three months ago.
[602.94 --> 604.66]  Three months ago, everybody was writing their own.
[604.66 --> 608.26]  And right now, everybody, as far as I can tell, writing MCP servers.
[608.68 --> 612.64]  And those who talk to LLMs, they consume MCP servers.
[613.42 --> 613.50]  Yeah.
[614.00 --> 621.28]  And maybe just give even, so I like the example that you gave of sort of searching file systems.
[621.46 --> 625.50]  What are, just to kind of expand people's understanding of some of the possibilities,
[625.70 --> 631.56]  what are some of the things that you've seen maybe implemented in Dial as things that are
[631.56 --> 634.32]  being orchestrated, you know, in general terms?
[634.32 --> 636.38]  What are kind of some of these things?
[636.76 --> 643.18]  Let me give you a higher level and much more sort of fruitful example.
[643.64 --> 643.72]  Okay.
[643.80 --> 643.96]  Yeah.
[644.44 --> 647.66]  We have our own agentic developer.
[647.96 --> 651.58]  It's called AI slash run code me.
[652.02 --> 655.92]  Because AI slash run has multiple different agentic systems.
[656.28 --> 658.86]  Code me is specifically coding oriented.
[658.86 --> 662.86]  We have others oriented at other parts of SDLC workflow.
[663.30 --> 668.18]  By the way, you guys can go to SWE bench and look at verified list.
[668.56 --> 672.32]  I believe code me as of now is, takes fifth.
[672.52 --> 677.74]  It's number five on the list of all the agents who compete for solving open source defects and stuff.
[677.74 --> 683.22]  So code me as an agentic system has many different assistants in it.
[683.72 --> 693.26]  Dial as a generic front door, as a chat GPT, would like to be able to run those assistants for you as you talk to dial.
[693.26 --> 702.44]  And until MCP, it really couldn't other than, hey, code me, implement an API for all of your assistants.
[702.64 --> 704.48]  Let me learn to call all of your APIs.
[705.04 --> 711.78]  Now the story is, hey, code me, give me an MCP server for you, which is what they have done.
[712.64 --> 722.46]  Dial as an MCP client can now connect to all of code me features, all the assistants, expose them as tools to an LLM.
[722.46 --> 724.50]  And orchestrate them for me.
[725.00 --> 726.72]  So I come into the chat.
[726.86 --> 737.54]  I ask for something that something includes reading a code base and making architecture sketches or proposals or evaluation, right?
[738.32 --> 745.32]  And LLM will ask code me assistants to go and read that code base because there is a feature in code me that does it.
[745.64 --> 752.22]  And Dial needs to only orchestrate, but doesn't need to rebuild or build from scratch.
[752.22 --> 752.84]  That's the idea.
[752.96 --> 754.54]  So this is the example.
[754.70 --> 754.80]  Yeah.
[755.40 --> 756.64]  Could you talk a little bit?
[757.12 --> 760.84]  I'm asking selfish questions because sometimes I get these asked of me.
[761.26 --> 764.06]  And I'm always curious how people answer this.
[764.14 --> 774.76]  So one of the questions that I get asked a lot in respect to this topic is, okay, I have, you know, tool or function or assistant one.
[774.76 --> 777.06]  And then I have assistant two.
[777.16 --> 779.42]  And then I kind of have a few, right?
[779.62 --> 784.68]  And it's fairly easy to route between them because they're very distinct, right?
[784.68 --> 794.54]  But now if you imagine, okay, well, now I could call one of a thousand assistants or functions or something or, you know, later on 10,000, right?
[794.54 --> 805.42]  How does the sort of scaling and routing kind of actually, how is that affected as you kind of expand the space of things that you can do?
[805.84 --> 814.48]  So that I think, and again, I can't know and I don't know, but I think that is still the secret sauce.
[814.48 --> 820.72]  In a way, that is still why there is all of this coding agents in SWE bench.
[820.92 --> 825.88]  All of them work with, let's say, Cloud Sonnet 3.5 or Cloud Sonnet 3.7 or GPT-40.
[826.88 --> 828.18]  LLM is the same.
[829.10 --> 831.40]  And yet results are clearly different.
[831.88 --> 833.82]  Some score 10 points higher than the other.
[834.56 --> 838.62]  You go to cursor, IDE cursor, you ask it something, it does something.
[839.04 --> 841.22]  You switch the mode to max.
[841.82 --> 843.16]  They've introduced very recently.
[843.16 --> 855.30]  Cursor on Sonnet 3.7 and now on Gemini 2.0, I think, they have a max mode, which is pay-per-use versus their normal monthly plans.
[855.64 --> 868.74]  Because max will do more iterations, will spend more tokens, will be more expensive, will likely run through more complex orchestrations of prompts and tools and whatnot to give you better results.
[868.74 --> 877.82]  So how you build the pyramid of choices for your LLM, how you, because yeah, you will not ask LLM, you will not give it a thousand tools.
[877.82 --> 886.04]  If you, if you as a human, look a thousand options and you lose yourself, you know, a hundred options in it, I, again, I don't know.
[886.26 --> 890.80]  I expect LLM to have the same sort of oops, overwhelmed effect.
[891.16 --> 892.94]  You don't want to give it a thousand tools.
[893.00 --> 893.80]  You want to give it groups.
[893.94 --> 896.00]  You want to say, hey, you know, pick a group.
[896.50 --> 900.76]  And then within that, so you want to do this basically like a pyramid, like a tree.
[900.76 --> 907.32]  But how you build it and how you prompt it and how you, how you do this, now that's still on you.
[907.58 --> 920.48]  This is the application that connects the MCPs, the tools that it itself has, the prompt that the user has given, the system instructions and building the, some of the chain of thought LLM can build.
[920.70 --> 922.64]  And this is going to be a very interesting balance.
[922.74 --> 924.54]  What do you ask LLM to build?
[924.54 --> 935.98]  How much of this sequencing of steps will be on you in your hands versus how much you're going to delegate to LLM and ask LLM to come up with a sequence of steps.
[937.00 --> 944.80]  And from what I, from what I've seen over the last year, you're better off delegating more to LLMs because they get better at it.
[944.80 --> 952.00]  So the more you control the sequence yourself, the less, the more sort of inflexible it becomes.
[952.62 --> 957.60]  You're better off delegating to LLM, but you don't expect it to just figure out from one prompt.
[958.24 --> 962.02]  Daniel, I can give you that example that I gave in the beginning, if you want, about the failure.
[962.78 --> 963.56]  Yeah, go for it.
[963.66 --> 964.76]  So I use AI.
[965.00 --> 967.16]  So I built with AI, right?
[967.20 --> 968.78]  But I also use AI as a developer.
[969.04 --> 972.14]  So I'm on cursor as my primary ID these days.
[972.14 --> 975.92]  I use the AI slash run code me that I mentioned.
[976.32 --> 980.70]  I play around with other things like as they come up, like cloud code and things.
[981.40 --> 983.70]  But I also record what I do.
[984.20 --> 998.06]  Little snippets, five, 10 minutes videos for my engineering audience at EPAM for the guys to just look what it is that I'm doing, learn from how I do it, try to think the same way, try to replicate, get on board with using AI.
[998.40 --> 999.86]  So I started out to do a task.
[999.86 --> 1006.72]  I wanted to record, I wanted to, on record, get a productivity increase with a timer.
[1007.12 --> 1012.90]  My plan was I'm going to estimate how long it's going to take me, announce, let's say two hours, do it with an agent.
[1013.36 --> 1016.80]  And I always pause my video when the agent is thinking because that's a boring step.
[1017.12 --> 1018.48]  But the timer is going to get ticking.
[1018.92 --> 1022.68]  And at the end, I'm going to arrive at, let's say, an hour, maybe 40 minutes out of two.
[1022.98 --> 1025.08]  Boom, that's the productivity gains.
[1025.08 --> 1028.22]  And 30 minutes in, I completely failed.
[1028.72 --> 1033.54]  I had to scrap everything that DLM and agents wrote for me and start from scratch.
[1033.64 --> 1036.22]  And my problem was I overprompted.
[1036.66 --> 1038.64]  I thought I knew what I wanted agent to do.
[1038.76 --> 1043.98]  There were three steps, like copy this, write this, refactor this, and you're done.
[1043.98 --> 1046.30]  And it did it.
[1046.42 --> 1048.30]  It iterated for 10 minutes.
[1048.54 --> 1052.22]  It was the CodeMe agentic developer that we have.
[1052.74 --> 1060.52]  When I scrapped it and started doing it myself, I did half of it, stopped, and realized that the other half was not needed.
[1060.90 --> 1062.32]  It was stupid of me to ask.
[1062.32 --> 1071.92]  So the correct approach would have been to iterate, do the first half, stop, rethink, and then decide what to do next.
[1072.16 --> 1075.44]  But the agent was given the instruction to go all the way.
[1075.70 --> 1077.38]  So it went all the way.
[1078.08 --> 1081.48]  And this is the other thing with thousand instructions, right?
[1081.48 --> 1091.84]  You don't want an agent to be asked to do something that you think you know, but you only really will know as you iterate through.
[1092.58 --> 1094.02]  In these cases as well.
[1094.54 --> 1103.62]  So I find your experience with balancing how you prompt it, how far the agent goes.
[1103.74 --> 1106.62]  All of this is intuition that you're kind of learning.
[1106.62 --> 1112.68]  One of the things that was interesting, we just had Kyle, the CEO of GitHub, on.
[1112.80 --> 1115.26]  And we were talking about agents and coding assistants.
[1115.94 --> 1122.60]  One of his thoughts was also around the orchestration after you have generated some code, right?
[1122.62 --> 1125.54]  It's one thing to create a project, create something new.
[1126.04 --> 1130.80]  But most of software development kind of happens past that point, right?
[1130.80 --> 1140.30]  And I'm curious, as someone who is really trialing these tools day in and day out, kind of as your daily driver and utilizing these things,
[1140.76 --> 1144.16]  I think that's on people's mind is, oh, cool.
[1144.30 --> 1156.54]  Like I can go into this tool, generate a new project that maybe whatever it is, you always see the demo of creating a new video game or whatever the thing is, right?
[1156.54 --> 1161.70]  But ultimately, I have a code base that is very massive, right?
[1162.02 --> 1163.80]  I'm maintaining it over time.
[1164.90 --> 1168.32]  Most of the work is more on that operational side.
[1168.92 --> 1173.24]  So in your experience with this set of tooling, what has been your learning?
[1173.56 --> 1174.70]  Any insights there?
[1174.84 --> 1178.00]  Any thoughts on kind of where that side of things is heading?
[1178.00 --> 1186.94]  Especially for, you know, you're dealing with, I'm sure, real world use cases with your customers who have large code bases, right?
[1187.22 --> 1189.30]  Well, that's great.
[1189.58 --> 1191.28]  I'm so glad that you asked.
[1191.56 --> 1194.22]  Because what I do is actually that latter aspect.
[1194.48 --> 1201.76]  I have a monorepo of like 20 different things in it that could have been separate repos of their own.
[1201.84 --> 1203.78]  So I have a large code base that I work with.
[1203.78 --> 1211.80]  And I actually saw our own developer agent occasionally choke because it attempts to read too much.
[1212.32 --> 1217.44]  And it just chokes on like tokens and limits and things that it can do per minute or per hour or something.
[1217.72 --> 1219.34]  So that's one thing.
[1219.44 --> 1224.94]  But what I find myself doing with cursor, for example, I actually pinpoint it very actively, very often.
[1225.20 --> 1227.20]  Because I wanted to work with these files.
[1227.62 --> 1230.90]  When it's something specific, I'll just point the files at it.
[1230.90 --> 1234.40]  And I'm going to ask, I'm going to prompt it in context of these three or four files.
[1234.76 --> 1236.70]  And that limits how much it's going to go out.
[1237.16 --> 1239.48]  But really, back to your question.
[1239.88 --> 1241.90]  To me, it's not about code bases that much.
[1241.94 --> 1242.96]  I don't think it's going to be...
[1242.96 --> 1247.14]  Well, maybe if I do something greenfield and funny, it's going to write it.
[1247.18 --> 1247.82]  I'm going to run it.
[1247.84 --> 1249.36]  And if it works, it's all I need.
[1249.58 --> 1250.36]  Like, it's correct.
[1250.46 --> 1250.92]  It works.
[1251.46 --> 1251.82]  Great.
[1252.78 --> 1254.90]  Today, and it's still a mental shift.
[1254.98 --> 1255.76]  It's still early.
[1255.76 --> 1263.12]  I'm still looking and thinking of the code base that I write with my agents as code base that will be supported by other people.
[1263.62 --> 1265.58]  Likely with agents, but people still.
[1266.48 --> 1270.46]  So correct by itself is not good enough.
[1271.06 --> 1274.02]  I want it to be aesthetically the same.
[1274.12 --> 1275.56]  I want it to follow the same patterns.
[1275.68 --> 1279.26]  I want it to make sense for my other developers who will come in after me.
[1279.60 --> 1283.86]  I want it to be as if it's the code that I have written, or at least more or less that I have written.
[1283.86 --> 1287.80]  And that slows me down a little bit, clearly, I'm sure.
[1288.34 --> 1291.20]  But the other thing is, I am the bottleneck.
[1291.70 --> 1300.76]  An agent will take minutes, small digit, like single digit minutes, if not less, to spit out whatever it spits out.
[1301.30 --> 1304.00]  And oftentimes in code bases, it's not a single file.
[1304.46 --> 1306.14]  It's edits in multiple places.
[1306.56 --> 1308.30]  Then I have to come in and read it.
[1308.54 --> 1309.16]  Here's the difference.
[1309.16 --> 1314.58]  When I write myself, my brain has a timeline.
[1314.90 --> 1320.30]  I was thinking as I was typing, as I was thinking, I know how I arrived at what I have arrived at.
[1320.88 --> 1322.50]  I may decide that it's bullshit.
[1322.82 --> 1324.22]  You know, scrap, we start over.
[1324.38 --> 1325.06]  That happens.
[1325.16 --> 1325.76]  We're all developers.
[1326.06 --> 1328.76]  But I know how I arrived at where I am.
[1329.14 --> 1334.38]  When I look at what agents produced for me, I have no idea how it arrived at where I am.
[1334.38 --> 1337.70]  I need to reverse engineer, like, why?
[1337.96 --> 1338.72]  What did it do?
[1338.88 --> 1339.54]  It takes time.
[1339.64 --> 1342.38]  I tried recording it, and I can't.
[1342.40 --> 1345.62]  Because I can't speak as I think at the same time.
[1346.28 --> 1346.34]  Yeah.
[1346.46 --> 1347.76]  This is the bottleneck, literally.
[1348.04 --> 1349.46]  So this is the bottleneck.
[1349.70 --> 1356.16]  The other thing is, when I was doing that video with a timer, I sort of, I expected certain outcomes.
[1356.16 --> 1359.58]  But I also knew that if it works, I'm going to say this at the end.
[1359.64 --> 1365.08]  I'm going to say, guys, look, it took me 20 minutes, let's say 30 minutes out of an hour.
[1365.32 --> 1366.60]  So it's 2x, right?
[1366.88 --> 1369.00]  Literally 2x productivity improvement.
[1369.10 --> 1369.90]  Amazing, isn't it?
[1370.76 --> 1371.70]  But here's the thing.
[1372.12 --> 1379.64]  Within the 30 minutes that I've spent, the percentage of time I spent critically thinking was much higher than normal.
[1380.20 --> 1384.58]  Percentage of time I spent doing boilerplate is much lower because the agents did this.
[1384.58 --> 1390.76]  I really critically thought about what to ask, how to prompt, and then analyzing what it did, thinking what to do next.
[1390.90 --> 1391.58]  Do I edit?
[1391.68 --> 1392.48]  Do I reprompt?
[1393.58 --> 1400.24]  Can I sustain the same higher percentage of critical thinking for the full day to get 2x in a day?
[1400.94 --> 1402.08]  Probably I can't.
[1402.80 --> 1410.06]  So what probably is going to happen, I'm going to get 2x, but I'm going to use the time in between as agents work to do something else.
[1410.06 --> 1415.06]  My day will likely get broken down into more smaller sections.
[1415.78 --> 1419.10]  My overall daily productivity is likely to increase.
[1419.64 --> 1421.78]  I'm likely to do more things in parallel.
[1422.20 --> 1423.22]  Maybe I'll do some research.
[1423.34 --> 1424.68]  Maybe I'll answer more emails, right?
[1425.16 --> 1429.50]  But it's going to be more chaotic, also likely more taxing.
[1430.06 --> 1431.94]  I don't think we've learned yet.
[1432.02 --> 1433.60]  I don't think we've had enough experience yet.
[1433.62 --> 1435.20]  I don't think many people talk about this yet.
[1435.26 --> 1436.12]  People talk about this.
[1436.12 --> 1437.40]  Oh my God, look what I've built with agents.
[1439.70 --> 1445.92]  I wonder how they're going to talk about how they've worked for like six months with agents.
[1446.70 --> 1453.98]  And how six months that they've done with agents is better than six months without and how they feel at the end of the day.
[1455.00 --> 1456.78]  And think about in the zone.
[1456.78 --> 1466.44]  We all, I hope, as engineers, like to be like, you know, disconnect all emails, whatever, get the music on, IDE in front of you, you're in it for like two hours.
[1467.06 --> 1468.72]  With agents, you just can't.
[1469.30 --> 1472.48]  You prompt an agent, it goes off doing something.
[1472.80 --> 1473.32]  What do you do?
[1473.98 --> 1474.16]  Yeah.
[1474.50 --> 1475.70]  Do you like pull up your phone?
[1475.98 --> 1479.98]  And then your productivity increases one way, your screen time increases the other way.
[1480.38 --> 1481.22]  It's not a good idea.
[1481.60 --> 1482.46]  What can you do?
[1482.46 --> 1485.94]  Like, what do you do in this minute and a half or three?
[1486.06 --> 1487.18]  And you don't know how long, right?
[1487.26 --> 1490.66]  Well, you can see the outcomes coming up, but the agents are still spinning.
[1490.80 --> 1491.38]  It's still spinning.
[1491.60 --> 1494.62]  Like, so I'm sorry, it's a long answer to a question.
[1495.10 --> 1495.22]  Yeah.
[1495.32 --> 1498.20]  But that's what I'm thinking about like constantly.
[1498.50 --> 1500.96]  And that's what I don't yet have answers for.
[1501.40 --> 1501.80]  Yeah.
[1501.84 --> 1507.92]  But I really hope to eventually through experiments and recording and thinking arrive at at least what it means for me.
[1508.18 --> 1510.40]  Because I cannot even tell you what it means for me yet.
[1510.40 --> 1510.70]  Yeah.
[1511.20 --> 1511.52]  Yeah.
[1511.58 --> 1526.88]  I mean, I experienced this yesterday too, because I'm preparing various things for investors, you know, updating some competitive analysis and that sort of thing.
[1526.88 --> 1536.06]  And, you know, I just, when you have whatever it is, I think it was 116 companies and I like, oh, I'm going to update all of these things for all of these companies.
[1536.06 --> 1540.18]  Like, you know, obviously I'm going to use an AI agent to do this.
[1540.22 --> 1542.60]  This is not something I want to do manually.
[1542.82 --> 1545.32]  I just put in all of these things and search websites.
[1545.32 --> 1546.60]  So I did that.
[1546.70 --> 1553.64]  But to your point, it was like, I could figure out how to do a piece of that and get it running.
[1554.12 --> 1559.84]  And then I see it running and I, you know, I realized that this will take however long it is, right?
[1559.92 --> 1563.40]  10 minutes or whatever the timeframe is.
[1563.40 --> 1571.48]  And then you context switch out of that to something else, which for me, I think was email or whatever.
[1571.56 --> 1572.66]  I'm like, oh, this is going to run.
[1572.74 --> 1577.20]  I'm going to go answer some emails or something like that, which in one way was productive.
[1577.20 --> 1579.44]  But then I had to context switch back.
[1579.54 --> 1579.78]  Yeah.
[1579.80 --> 1582.52]  Like, oh, why did I output all these things?
[1582.52 --> 1587.38]  Or, you know, it happened to be that I wasn't watching the output, right?
[1587.48 --> 1594.56]  And in one case, when I ran it, I was like, oh, well, I really should have had this output, this column or this field.
[1594.56 --> 1596.94]  But I didn't think of that before.
[1596.96 --> 1601.96]  And I wasn't looking because I turned away from the agent back to my email, right?
[1602.04 --> 1608.48]  So, yeah, I think this is a really interesting set of problems that is more of like a new...
[1608.48 --> 1612.26]  Yeah, it's a new way of working that hasn't been parsed out yet, right?
[1612.26 --> 1614.12]  And I tried not to do it.
[1614.24 --> 1615.56]  Like I tried, but then you sit idle.
[1616.06 --> 1617.24]  Like you literally sit idle.
[1617.38 --> 1619.24]  It's like, and it doesn't feel good.
[1619.32 --> 1621.94]  It feels like, oh my God, why am I not doing anything?
[1622.06 --> 1624.30]  Yeah, it's an interesting dynamic.
[1624.64 --> 1625.90]  That's for sure.
[1625.90 --> 1635.04]  And I've definitely seen people that show, you know, having multiple agents working on different projects at the same time.
[1635.22 --> 1642.16]  And that when I see someone with two screens and things like popping up all the place, I, you know, there's no way I could.
[1642.26 --> 1645.66]  In my brain sort of monitor all of that that's going on, right?
[1645.72 --> 1647.64]  It must be very taxing first.
[1647.74 --> 1654.36]  And second, half of those merge requests, pull requests from the agents will be, let's say, subpar.
[1654.74 --> 1655.14]  Yeah.
[1655.68 --> 1657.06]  Frustration and you will rise too.
[1657.12 --> 1659.40]  Like you would think, man, I would have done it already myself much better.
[1659.40 --> 1660.04]  Like what is this?
[1660.12 --> 1667.06]  Like emotionally, it is a very different way of working emotionally.
[1667.72 --> 1668.10]  Yes.
[1668.10 --> 1672.94]  And I really, I can't, well, I keep thinking.
[1673.14 --> 1673.86]  I can't forget.
[1674.06 --> 1676.42]  I advise people also to think.
[1676.74 --> 1678.52]  Not just think about productivity gains.
[1678.60 --> 1681.60]  Not just think about delegating to agents and enjoying the results.
[1681.60 --> 1689.24]  Think about how it changes the dynamic of your day and how you think about it afterwards, right?
[1689.66 --> 1689.80]  Yeah.
[1689.96 --> 1690.18]  Yeah.
[1690.18 --> 1690.82]  That's interesting.
[1691.20 --> 1694.18]  So I know we're circling kind of way back.
[1694.36 --> 1694.74]  Sure.
[1695.10 --> 1695.98]  Interesting discussion.
[1695.98 --> 1701.80]  But I do want to make sure people can kind of find some of what you're doing with Dial.
[1701.90 --> 1704.20]  You mentioned kind of the open source piece of this.
[1704.84 --> 1710.78]  What's sort of needed from the user perspective to kind of spin this up and start testing it?
[1710.88 --> 1716.90]  And for those that are out there that are interested in like trying some things with the project,
[1717.34 --> 1720.54]  what would you kind of tell them as a starting point?
[1720.54 --> 1725.26]  And like what the process is like to kind of get a system like this up and running?
[1725.26 --> 1730.40]  I actually not sure I can tell for Dial specifically.
[1731.36 --> 1734.16]  Nobody is running local Dial.
[1734.26 --> 1736.42]  It's not something you run locally.
[1736.92 --> 1737.04]  Gotcha.
[1737.18 --> 1743.64]  It's something that you run sort of centrally in organization of size can be different,
[1743.64 --> 1751.36]  but you expose it to your people through like a URL that they all can go to and use like
[1751.36 --> 1754.80]  sort of use AI through Dial and do things through Dial.
[1755.26 --> 1755.66]  Interesting.
[1755.86 --> 1761.68]  One of the apps we built as an example earlier, it was last year, was like talk to your data.
[1762.10 --> 1768.18]  But if you look at analytics like Snowflakes of the world, they all have something like this
[1768.18 --> 1771.14]  today, like semantic layer, which you work on.
[1771.14 --> 1776.98]  And then through semantic layer, through prompting and through some query conversions and connectors
[1776.98 --> 1782.68]  to data warehouses and data lakes, you get yourself a chat with your data, like analytical
[1782.68 --> 1784.62]  reports, graphs, tables.
[1785.28 --> 1786.14]  So we built that.
[1786.18 --> 1787.28]  That was built into Dial.
[1787.28 --> 1788.30]  So you go to Dial.
[1788.60 --> 1790.62]  And then again, imagine ChatGPT.
[1790.70 --> 1793.58]  Imagine ChatGPT that allows you to choose what model you talk to, right?
[1793.58 --> 1800.12]  Not just OpenAI models, but all the other models that exist, as well as applications.
[1801.00 --> 1803.72]  So go to this ChatGPT, which is now just Dial.
[1803.96 --> 1808.06]  You select this data heart AI, we call it, which is our talk to your data.
[1808.10 --> 1809.22]  And you start talking to it.
[1809.22 --> 1815.52]  And this is still your Dial experience, but you're really talking to an app that then
[1815.52 --> 1817.44]  talks to semantic layer.
[1818.16 --> 1823.36]  Then it builds queries based on your questions, runs them, gets data back, visualizes it in
[1823.36 --> 1827.66]  Dial, because Dial has all this visualizations capabilities to explain how it's not just text
[1827.66 --> 1828.34]  coming back.
[1829.08 --> 1830.82]  Builds your charts and you can interact with it.
[1831.40 --> 1833.26]  But again, you don't run Dial locally.
[1833.26 --> 1841.68]  If you want to explore what it is, I hope, I expect that if you go to, I think it's rail-epam.com.
[1842.66 --> 1843.76]  E-pam-rail.
[1844.12 --> 1844.24]  Yeah.
[1844.70 --> 1845.92]  E-pam-rail.com.
[1846.02 --> 1846.38]  Thank you.
[1846.82 --> 1848.32]  And you're going to read about what it is.
[1848.38 --> 1853.02]  And you're going to find all the links to hopefully documentation, how to, you know.
[1853.82 --> 1860.32]  But also most companies who we work with, they want more than just, hey, how do we install it?
[1860.32 --> 1864.48]  They want, and now we want to build with it.
[1865.54 --> 1868.90]  And that's where we come in with professional services.
[1869.30 --> 1876.70]  We can build them things for their Dial so that they can do the AI that matters to them
[1876.70 --> 1882.94]  in their context, with their data, with their workflows, with their restrictions on things
[1882.94 --> 1884.74]  they can and cannot do and yada, yada, yada.
[1884.74 --> 1885.46]  Yeah.
[1886.10 --> 1895.14]  And I'm wondering for this kind of, if you think about this zoo of underlying applications
[1895.14 --> 1900.92]  or assistance, I'm wondering, because you've obviously been working in this area for some
[1900.92 --> 1910.00]  time, do you have any insights or learning around kind of easy wins for, you know, underlying
[1910.00 --> 1916.24]  functions or agents that can be tied into this sort of orchestration layer or maybe like
[1916.24 --> 1917.76]  more challenging ones?
[1917.98 --> 1922.62]  Things that you've learned over time in developing and working with these things in terms of,
[1922.74 --> 1929.30]  you know, things that you could highlight as, you know, easy types of wins and things that,
[1929.56 --> 1934.24]  I mean, you mentioned the workflow stuff around some of what isn't yet kind of figured out,
[1934.24 --> 1939.54]  but more on the orchestration layer and the function calling, you know, what are some areas
[1939.54 --> 1944.62]  of challenge or things that might not be figured out yet that are, that you think are interesting
[1944.62 --> 1946.42]  to explore in the future?
[1946.86 --> 1947.76]  Let me think.
[1947.92 --> 1953.34]  So, because my first thought was to, so you're asking about connecting tools and functions
[1953.34 --> 1959.56]  to NLLM and which of the functions or what type of connectivity sort of is easier?
[1959.56 --> 1960.46]  Yeah, yeah.
[1960.50 --> 1964.90]  Is there anything that's out of scope or more of a challenge currently, or is it fair
[1964.90 --> 1971.06]  game for kind of, you know, I guess it's whatever you can build in that function in the assistant,
[1971.32 --> 1977.40]  but yeah, what limitations are there or challenges in that kind of mode of development of developing
[1977.40 --> 1979.44]  these underlying functions or tools?
[1979.72 --> 1979.94]  I see.
[1980.38 --> 1982.44]  So it's kind of a twofold answer.
[1982.84 --> 1989.18]  If you take the technicality aspect, like how do I build a tool that does X?
[1990.12 --> 1993.26]  The complexity is really in X.
[1993.94 --> 1998.28]  Like if you want to go and query a database, how hard is that?
[1998.44 --> 2000.12]  Well, not hard, right?
[2000.18 --> 2001.96]  I mean, connectivity to the database.
[2002.32 --> 2004.52]  If you have a query, you run it, you get results back.
[2004.62 --> 2011.40]  So it's not hard to do the technicality of querying a database, making it useful and making
[2011.40 --> 2018.00]  the result useful in context of users prompt and conversation is a lot more challenging.
[2018.00 --> 2021.10]  I had this, so I'm running a service.
[2021.32 --> 2025.40]  You can actually, it actually has a public webpage called api.epam.com.
[2025.86 --> 2026.46]  It's our own.
[2026.64 --> 2030.82]  So you will not really go past the front page, but you'll understand what it is.
[2030.82 --> 2035.46]  It's a collection of APIs that we built, my team has built that exposes a lot of data.
[2035.74 --> 2037.92]  Remember I said EPEAM runs on internal software.
[2038.70 --> 2043.76]  So all of those applications, they stream their data and their events out into a global
[2043.76 --> 2044.34]  data hub.
[2044.60 --> 2048.22]  Think big, big, big Kafka cluster, but that's Kafka.
[2048.22 --> 2050.52]  So you can read data out of it as a Kafka consumer.
[2051.08 --> 2056.06]  But if you want to have like more modern, you know, API search, lookup, this, that.
[2056.38 --> 2059.32]  So we have an API service, all of the data.
[2060.08 --> 2063.36]  And somebody came to me today and said, hey, have you heard of MCP?
[2063.46 --> 2064.62]  I'm like, yes, of course I have.
[2065.22 --> 2068.62]  Why don't you guys build MCP for api.epam.com?
[2068.62 --> 2071.78]  My answer is it is easy to build.
[2072.42 --> 2074.50]  api.epam.com speaks RSQL.
[2075.18 --> 2079.96]  I can build a server that will take your query, create RSQL.
[2080.46 --> 2083.90]  LLM will be able to do that easily, run it, give back the data.
[2084.30 --> 2088.28]  But I said, it's not going to be useful because this is single data set APIs.
[2089.02 --> 2090.82]  Your questions are likely analytical.
[2091.42 --> 2097.02]  You likely want to ask something that expects me to do summary by month, this, this, this,
[2097.02 --> 2100.74]  and give you like a, which like, that's a very different question.
[2100.94 --> 2104.68]  So you ask me about MCP to an API, easy to do.
[2105.18 --> 2109.58]  Make it useful for your actual use case, much harder to do.
[2110.00 --> 2115.00]  I likely need to do a lot more than just connectivity of tool to an LLM.
[2115.36 --> 2121.32]  I need to understand what you're asking, figure out the orchestration that is required,
[2121.50 --> 2123.36]  maybe custom apps, maybe something else.
[2123.36 --> 2130.00]  And then, and then you start hitting authentication, legacy apps, all the other roadblocks.
[2130.58 --> 2134.48]  And in a way, the talk to your data is an amazing prototype that we built.
[2134.58 --> 2135.88]  And I have a video about this.
[2135.88 --> 2144.80]  But we sort of stopped because we clearly sensed how steep the curve is to get it to like actual,
[2145.04 --> 2150.62]  because what we wanted to do, what we envisioned we could do was analytics democratized.
[2150.82 --> 2154.80]  So you don't have to go to analytical team, ask them to build your new Power BI report.
[2155.32 --> 2159.24]  And them spending a week doing so, you can just come into dial and say,
[2159.24 --> 2162.24]  Hey, you know, show me this, this, this, and this.
[2162.62 --> 2164.66]  And yes, we technically can do it.
[2164.92 --> 2169.34]  But to be able to do this for all kinds of questions you can ask about our data,
[2169.82 --> 2171.98]  that's a much harder thing to do.
[2172.68 --> 2172.94]  So yeah.
[2173.48 --> 2173.74]  Yeah.
[2174.00 --> 2179.52]  And it also, yeah, to your point, underlying systems might have limitations.
[2179.52 --> 2184.72]  I think in analytics related use cases that we've encountered with our customers,
[2185.78 --> 2188.62]  you know, often I'll just ask the question around,
[2189.50 --> 2194.94]  Hey, if you, if you gave this database schema or whatever it is to,
[2194.94 --> 2201.50]  you know, a reasonably educated, you know, college intern or whatever that is.
[2201.50 --> 2207.54]  And you ask, you know, what columns would be relevant to query based on this,
[2207.80 --> 2213.04]  you know, based on this natural language query, you know, you can pretty easily tease out.
[2213.30 --> 2215.02]  Well, I look at all these columns.
[2215.20 --> 2220.56]  I have field 157 and custom underscore new underscore field.
[2220.74 --> 2224.46]  You know, there's no way for, for just someone off yet, you know, to,
[2224.64 --> 2226.08]  to know anything about that.
[2226.08 --> 2228.88]  And so it's not really a limitation of what's possible
[2228.88 --> 2233.78]  in terms of the technicality, like you said, it's more of, you know,
[2234.24 --> 2238.78]  you're not always set up for success in terms of utility, like you mentioned.
[2239.28 --> 2241.80]  And for data, that's where semantic layer comes in.
[2241.92 --> 2248.42]  So if you have descriptions of your columns, of your tables with business meaning,
[2249.08 --> 2256.40]  then connecting that semantic layer with some data samples to LLM
[2256.40 --> 2261.34]  will allow it to write the query that you thought was impossible to write.
[2261.42 --> 2268.54]  Because it is impossible without the semantic layer sort of can explain the data that you have
[2268.54 --> 2273.98]  in business terms, in the language that the questions will be asked of your assistant.
[2274.60 --> 2278.46]  And that's what allows us, allows us to do this talk to your data analytics.
[2279.16 --> 2279.26]  Yeah.
[2279.26 --> 2283.90]  Well, I, I know that, um, we've talked about a lot of things.
[2283.90 --> 2291.02]  I think you, you are probably seeing a good number of use cases across your clients at EPAM
[2291.02 --> 2293.78]  and also your own experiments with dial and other things.
[2293.90 --> 2299.94]  I'm wondering as you, as you kind of lay, lay in bed at night or whenever you're thinking
[2299.94 --> 2304.64]  about the future of, of AI or, or maybe it's all the time, or maybe it's, maybe it's not,
[2304.64 --> 2310.62]  uh, at night, but, uh, yeah, as, as you kind of see what is to your point,
[2310.68 --> 2315.30]  just bringing it all the way back to the beginning, you see what is possible to do now,
[2315.30 --> 2320.66]  which even six months, a year ago, whatever it was, you know, as it was not possible,
[2320.88 --> 2328.78]  what kind of, uh, is most exciting for you or, uh, most interesting for you to see how it plays
[2328.78 --> 2334.62]  out in the next, you know, six to 12 months? What, what is kind of constantly on your mind of,
[2334.62 --> 2339.24]  where things are going? Sounds like, you know, the, how we work with these tools is one of those
[2339.24 --> 2344.60]  things. We already talked about that a little bit, but what else is, you know, exciting for you or,
[2344.60 --> 2349.22]  or, um, encouraging in terms of how you see these things developing?
[2349.80 --> 2356.06]  My answer may surprise you when I think about it. I don't, you know, think or anticipate
[2356.06 --> 2363.72]  any new greatness to come. I actually mostly worry. And I worry because I know that my thinking
[2363.72 --> 2371.52]  is linear. Like most of us, uh, even though looking back, we know that technology has been
[2371.52 --> 2378.40]  evolving rather exponentially, our ability to project into the future and think what's coming
[2378.40 --> 2386.36]  next is linear. So I am unlikely to properly anticipate and get ready for, and then expect,
[2386.36 --> 2393.60]  right. And wait for what's to come. I am sure to be surprised. And I guess as everybody else,
[2393.60 --> 2402.72]  I'll be doing my best to hold on to not fall off. So I worry seeing how the entry barriers rise.
[2403.02 --> 2409.40]  It's harder for more junior people to get in today. When I'm asked about skills, I recommend
[2409.40 --> 2416.84]  that people focus on as far as trying to be better prepared for the future. I always answered with
[2416.84 --> 2424.76]  the same things. I always say fundamentals and then critical system thinking and fundamentals.
[2425.18 --> 2431.70]  You can read about a lot, but you really master them when you work with them yourself, not when
[2431.70 --> 2438.52]  someone else works with them for you and not having them is likely going to constrain you from being able
[2438.52 --> 2444.80]  to properly curate and orchestrate all these powerful AI agents. And when they get so powerful
[2444.80 --> 2450.36]  that they don't need you to curate and orchestrate them, then what does it do to you as an engineer?
[2451.04 --> 2457.34]  And maybe that's not the right thinking, but this is what I think about at night, like you asked,
[2457.96 --> 2464.74]  when I think about AI and what's coming, I am excited as an engineer. I like using all of this.
[2464.74 --> 2470.44]  I just don't know how it's going to reshape the industry and how it's going to change my work,
[2470.44 --> 2472.24]  you know, in years to come.
[2473.34 --> 2479.36]  Yeah. Well, I think it's something even in talking through with you, kind of some of the work that
[2479.36 --> 2484.84]  you and I have been doing with agents and how that really has triggered a lot of questions
[2484.84 --> 2491.64]  in our own mind of what is the proper way of, of working around this. And I think there is going
[2491.64 --> 2497.44]  to be a, you know, that is a widespread issue that people are going to have to navigate. So yeah,
[2497.44 --> 2503.78]  I think it's, I think it's very valid and we'll, we will be interested to see how it develops and
[2503.78 --> 2510.04]  would love to have you back on the show to, to have your learnings again in, in six or 12 months of,
[2510.12 --> 2515.24]  of how it's shaking out, shaking out for you. Really appreciate you joining. It's been a great
[2515.24 --> 2517.44]  conversation. Thank you very much. It's been a pleasure.
[2521.64 --> 2530.84]  All right, that is our show for this week. If you haven't checked out our changelog newsletter,
[2530.84 --> 2539.40]  head to changelog.com slash news. There you'll find 29 reasons. Yes, 29 reasons why you should
[2539.40 --> 2545.16]  subscribe. I'll tell you reason number 17. You might actually start looking forward to Mondays.
[2545.32 --> 2548.04]  Sounds like somebody's got a case of the Mondays.
[2548.04 --> 2554.56]  28 more reasons are waiting for you at changelog.com slash news. Thanks again to our partners
[2554.56 --> 2560.42]  at fly.io to Breakmaster Cylinder for the beats and to you for listening. That is all for now,
[2560.42 --> 2562.00]  but we'll talk to you again next time.
