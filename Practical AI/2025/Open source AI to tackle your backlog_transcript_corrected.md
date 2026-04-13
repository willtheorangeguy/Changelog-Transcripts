[0.00 → 10.06] Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 → 11.46] and accessible to all.
[11.46 → 14.48] If you like this show, you will love The Change Log.
[14.70 → 19.52] It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 → 21.38] talk show for your weekend enjoyment.
[21.84 → 25.82] Find us by searching for The Change Log wherever you get your podcasts.
[26.32 → 28.36] Thanks to our partners at Fly.io.
[28.36 → 31.10] Launch your AI apps in five minutes or less.
[31.40 → 33.38] Learn how at Fly.io.
[44.12 → 47.62] Welcome to another episode of the Practical AI podcast.
[48.02 → 49.80] This is Daniel Whiten ack.
[49.90 → 55.68] I'm CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who
[55.68 → 58.74] is a Principal AI Research Engineer at Lockheed Martin.
[59.02 → 59.68] How are you doing, Chris?
[60.06 → 61.26] Doing well today, Daniel.
[61.30 → 61.70] How's it going?
[62.14 → 63.68] It's going great.
[63.76 → 71.92] On the road this week, talking about AI and security in various places, which is always
[71.92 → 73.30] fun.
[73.30 → 77.72] And often, you know, things come up in those sorts of talks.
[77.86 → 83.82] One of the things I've got a lot of questions about this week, actually, is the impact of
[83.82 → 90.96] AI on coding workflows and vibe coding and all of those sorts of things.
[91.14 → 97.00] And really happy to have with us some really amazing guests today to help us talk through
[97.00 → 101.48] some of those subjects and also share what they're doing both on tooling and models.
[101.48 → 106.80] We've got Robert Brennan, who is co-founder and CEO at All Hands AI.
[107.26 → 113.50] And then we have Graham Newbie, who is co-founder and chief scientist at All Hands AI and associate
[113.50 → 115.06] professor at Carnegie Mellon.
[115.28 → 115.96] How's it going, guys?
[116.24 → 116.78] It's going good.
[117.04 → 117.46] Very good.
[117.78 → 118.48] Thanks for having us.
[118.80 → 119.00] Yeah.
[119.06 → 119.78] Thanks for joining.
[120.18 → 125.10] Maybe one of you or both of you could kind of give your thoughts generally.
[125.10 → 130.78] Like I say, even this week at conferences, it seems like half of the questions that I'm
[130.78 → 135.74] getting are around how AI is impacting developer workflows.
[136.10 → 139.20] You know, how many people are really using vibe coding tools?
[139.46 → 145.12] If you're using vibe coding tools, you know, what impact is that having on code quality?
[145.20 → 146.54] All of these sorts of things.
[146.54 → 151.78] So I'm wondering, you know, from the perspective of, you know, All Hands and the work that you
[151.78 → 159.36] all are doing, what does the kind of environment around these code assistant vibe coding tools
[159.36 → 161.44] look like from your perspective right now?
[161.52 → 163.78] Kind of what does that ecosystem look like?
[164.12 → 168.16] And then maybe set All Hands in the context of that would be helpful.
[168.54 → 168.98] For sure.
[169.18 → 169.36] Yeah.
[169.36 → 174.08] So there's a huge variety of tooling out there right now for code generation.
[174.42 → 176.84] So it's a very hard space to navigate.
[177.46 → 179.56] There are two ways I like to bifurcate the space.
[179.92 → 185.10] One is on the one hand, you have a lot of tools that are really meant for like rapid prototyping.
[185.38 → 187.08] There's some really cool stuff happening there.
[187.20 → 191.00] Stuff like lovable, bolt.dev, v0.dev stuff.
[191.24 → 192.52] They tend to be very visual.
[193.16 → 196.66] You're getting like quick prototypes of games or websites, things like that.
[197.10 → 198.58] Some really fun stuff happening there.
[198.58 → 203.40] And it's stuff that's enabling like a whole new set of people to experiment with software development.
[203.56 → 208.18] People who, you know, maybe like designers or product managers don't really have coding experience,
[208.26 → 210.04] maybe have like very little coding experience.
[210.20 → 212.14] They can now build whole apps, which is super cool.
[212.78 → 216.36] And then on the other end of the spectrum, you have stuff that is much more oriented towards
[216.36 → 218.80] like senior developers who are shipping production code.
[218.92 → 223.04] They're working on a code base that's going to go and serve millions of users,
[223.48 → 225.92] where you have to be a little bit more careful about what's going on.
[225.92 → 229.14] And also some really cool stuff happening on that end of the spectrum.
[229.92 → 234.38] And then the other way I like to bifurcate this space is that you have some tools that are very tactical.
[234.64 → 240.98] So stuff like GitHub Copilot, where it's, you know, inside your IDE, you know, it's suggesting code,
[241.06 → 243.48] like exactly where your cursor is inside the code base.
[243.48 → 248.02] You're like you're zeroed in on a task and the AI is just like helping you move faster through that task.
[248.72 → 252.90] And then on the other end, you have these tools that are much more agentic, right?
[252.92 → 260.52] They're able to just take a quick human description of a problem and then go off and work for 5, 10, 15 minutes
[260.52 → 264.54] while you go get a cup of coffee or work on a different problem or catch up on email.
[265.04 → 267.52] And then it comes back to you later with the solution.
[268.22 → 271.24] And Open Handsets basically on the right end of both of those spectrums, right?
[271.24 → 276.72] We are really oriented towards senior engineers who are working on production-grade code bases.
[277.04 → 281.84] And we're really oriented towards those more agentic workflows where you're giving an agent something to work on
[281.84 → 285.08] and it can iterate forward on its own without you having to babysit it,
[285.12 → 290.48] without you having to be, you know, squinting at your computer screen trying to figure out, you know, where you should be editing.
[291.00 → 292.38] Yeah, that's super helpful.
[292.76 → 298.08] I'm wondering, this might be an interesting question, but I know, you know, Graham,
[298.08 → 307.14] we've run into each other in the past as related to human language-related work, you know, in another context.
[307.14 → 312.18] I'm wondering from your perspective as kind of chief scientist, but also a researcher,
[312.68 → 318.12] as you've dug into this all-hands project and work and product,
[318.12 → 327.44] what has been surprising in terms of challenges around this and maybe things that were surprising in terms of,
[327.44 → 330.62] you know, easier than what you might have thought.
[330.70 → 331.92] Any thoughts there?
[332.42 → 334.34] Yeah, it's a great question.
[334.82 → 339.18] Thinking back in hindsight, it's kind of sometimes hard to come up with surprising things
[339.18 → 342.30] because the things that were formerly surprising now seem kind of obvious.
[342.30 → 349.90] But one of the things that I actually wrote a blog post about before was right when the Open Hands project started out,
[350.54 → 358.90] we were kind of on this bandwagon of trying to create a big agentic framework that you could use with
[358.90 → 360.74] and define lots of different agents.
[360.94 → 365.50] Like you could have your debugging agent, you could have your software architect agent,
[365.72 → 368.58] you could have your browsing agent and all of these things like this.
[368.58 → 372.74] And we actually implemented a framework where you could have one agent delegate to another agent
[372.74 → 377.88] and then that agent would go off and do this task and things like this.
[378.40 → 386.10] One somewhat surprising thing is how ineffective this paradigm ended up being from two perspectives.
[386.76 → 390.76] So the first perspective is it didn't really,
[391.00 → 393.76] and this is specifically for the case of software engineering.
[394.08 → 395.94] There might be other cases where this would be useful.
[395.94 → 405.16] The first is in terms of effectiveness, we found that having a single agent that just has, you know,
[405.24 → 409.16] all the necessary context, it has the ability to write code,
[409.72 → 413.08] use a web browser to gather information and execute code,
[413.62 → 417.96] ends up being able to do a pretty large swath of tasks without a lot of, you know,
[418.36 → 422.38] kind of specific tooling and structuring around the problems.
[422.38 → 429.02] And then the other thing is building many, many different agents is kind of a relatively large maintenance burden
[429.02 → 431.28] if they're not very easy to define.
[432.10 → 438.40] So we've basically gone kind of full in on having like a single agent that can do many, many different things.
[438.94 → 444.40] But in order to do that, it has to have the ability to pull in, you know, whatever information it needs.
[444.40 → 453.50] So we have a framework called micro agents where basically you can pull in a new prompt or a new tool or something like that for a particular task.
[453.62 → 457.28] But the underlying overall agent is a single agent that can do many different things.
[458.12 → 458.98] Quick follow up on that.
[459.12 → 464.82] Just for listeners who aren't really familiar with agentic workflows and stuff,
[464.82 → 468.02] could you talk just a moment about what that means?
[468.28 → 473.88] You know if so, if you've been developing for a number of years in the more traditional workflows that we've all,
[474.04 → 479.92] you know, kind of all started out at, and now we're hitting this world of agentic possibilities,
[480.52 → 485.74] could you talk a little bit about what's different for the user from where they came from
[485.74 → 491.40] in kind of traditional development environments to what agentic development workflows are like?
[491.40 → 498.28] Yeah. So, you know, I think the sort of like step one of integrating AI into your development process was like Copilot, right?
[498.38 → 501.06] Where it's really just plugging into autocomplete, right?
[501.10 → 502.28] We're all familiar with autocomplete.
[502.40 → 503.48] We've been using it for decades.
[504.02 → 506.18] It just got a thousand times better all of a sudden.
[506.28 → 509.94] Instead of just completing a class name, now it's writing like, you know, several lines of code.
[510.10 → 513.44] So that was like a huge boost to my productivity when I adopted Copilot.
[513.56 → 514.42] I was like, yeah, this is amazing.
[514.98 → 518.98] And then I was still, you know, for bigger chunks of code, I was like going to ChatGPT, and I was like,
[518.98 → 523.08] hey, can you write a SQL statement that'll do X, Y, and Z or, you know, things like that.
[523.38 → 529.96] And often I found myself doing this workflow where I would ask ChatGPT or Claude to like to generate some code.
[530.20 → 537.18] I'd paste that into my IDE, run it, get an error message back, paste the error message back into Claude or ChatGPT.
[537.34 → 538.52] And I just do this loop.
[539.20 → 540.54] And at some point I was like, well, this is dumb.
[540.62 → 543.16] Like I'm just shuffling text between one half and another.
[543.16 → 553.50] And that was actually when I built my first like agent basically where I built a little CLI that would just do that loop with Anthropic in the background.
[554.74 → 557.32] And that's kind of like the core of what an agent is.
[557.48 → 566.80] It's doing a full loop where you basically give a problem to the agent and say, okay, I want to write a SQL statement that does X or I want to modify my app to add this new feature.
[566.80 → 578.58] The agent writes some code, it runs the code, it sees what happens, it gets some kind of output from the real world, whether that's like the output of a command or maybe, you know, the contents of a web page or the contents of a file.
[579.00 → 583.22] Puts that back into the LOM's context, and then it can take one step forward closer to its goal.
[583.88 → 593.16] And then, you know, you can, as you get kind of better and better and more accurate at taking one step closer to your goal, you can take on longer and longer range tasks.
[593.16 → 602.20] So I would say in the beginning agents were perfect for things that would take like 10 steps, you know, something really simple like implement a new test and then make sure it passes.
[602.90 → 606.84] And now they can implement, you know, things that take hundreds of steps, which is really cool.
[606.96 → 613.04] I mean, that's the changes that we've seen over the last, you know, six to 12 months is that they're able to take on these huge tasks.
[613.04 → 617.72] So I can say implement feature X, you know, front end, back end and add testing.
[618.08 → 628.00] And today's agents are able to just continue executing, stepping forward into that until it comes to a full PR where all the tests are passing, and it's just kind of packaged up and ready to go.
[629.16 → 636.88] Selfishly, maybe I'll pass on a question for I was sitting around with a number of people at the conference I'm at last night and there were some opinions.
[636.88 → 639.06] This gets to some of what you were just talking about.
[639.28 → 649.06] I mean, some of what you talked about at the beginning about this being geared towards more senior, maybe more senior developers working in existing code bases or something like that.
[649.06 → 668.60] But also what you were just talking about, about that kind of workflow, it was kind of the opinion around the group that I was with last night that, hey, a lot of a lot of these tools might be well suited to senior engineers because you can iterate like that and actually have a sort of smell test for what's going right and what's going wrong.
[668.60 → 677.42] But not really for, you know, less experienced developers or new developers who really don't have that ability.
[677.68 → 688.78] I'm curious to understand like your perspective on that and maybe who's sort of using this and who's using it successfully, I guess, is the question.
[688.94 → 690.58] And what does that persona look like?
[690.58 → 701.10] Yeah, I think it's important to realize that, like, you still need to keep all the same code quality controls in place that you did before the age of AI, if not more code quality controls.
[701.22 → 702.82] Right. You need everything needs to go through code review.
[703.08 → 706.46] You need somebody who's familiar with the code base to look at the changes that are happening.
[706.46 → 721.18] I would say one of the kind of failure patterns I see with the technology is a lot of times a junior engineer or someone who doesn't really know how to code, you know, vibe codes their way to like a pretty good MVP because these agents are especially good at like Greenfield stuff.
[721.24 → 724.36] Right. They can build a, you know, a to-do list app all day.
[724.36 → 732.20] And then as you layer on more features over the course of like weeks or months, the code base just starts to rot a bit.
[732.30 → 744.80] Like the agent adds a bunch of maybe like duplicates a whole function because it couldn't find the original function, or it just keeps expanding the single function so that it's like thousands of lines of code and has all these forking paths.
[744.80 → 754.28] If you don't have somebody looking at the changes that are being proposed and critiquing them and like telling the agent, hey, you know, you added this new function, but we have an existing function that does that.
[754.38 → 757.06] Or, you know, this function is getting too big. Please refactor it.
[757.32 → 766.44] If you're not looking over its shoulder and critiquing its work, the code base will just grow into this monster, and you'll have to throw it all away because it's just it's its beyond repair.
[766.44 → 777.10] Well, I do want to get into some of the kind of unique elements of all hands and, you know, the perspectives that you all are taking.
[777.32 → 789.62] One of the things, of course, that strikes me right away as I, you know, it's even, you know, top of the web page when you go there is your approach to do this kind of open source.
[789.62 → 794.62] So open source approach to this kind of tool for developers.
[794.92 → 807.60] I'm wondering, you know, both of you could speak to this, but maybe, Graham, you could start in terms of like, obviously, you've built various projects over time and done research and been plugged into the research community.
[807.60 → 822.52] Why, from your perspective, was it important that at least some portions of some key portions of what you're building here, open source and, you know, what you think that might mean for this kind of tools, including all hands moving forward?
[823.18 → 828.68] Yeah. So there are a number of reasons why we decided to do this open source.
[828.68 → 846.42] The first reason is, I think everybody in our, you know, community believes that this is going to be very transformative technology, and it may drastically change the way we do software development going forward.
[846.42 → 859.06] And we have two options. We have an option where software development is drastically changed for us by people, by other people, or there's the option where we do it ourselves together.
[860.14 → 871.32] And we believe in the latter approach. Basically, we believe that, you know, if this is going to have a big effect on software development, software developers should be able to be, you know, be able to participate in that.
[871.32 → 897.18] And that's kind of the ideological point of view. The other point of view is we also believe that from a research perspective, open source, especially from the point of view of like agent frameworks, not necessarily the underlying foundation models, but from the point of view of agent frameworks, open source is not ever really going to be behind the closed options.
[897.18 → 904.76] And the reason why is that academia and all of these people really love this topic. They really love working on it.
[904.98 → 917.90] If we have an open framework, and we can provide a platform, both from the point of view of like having a good code base, that's easy to experiment with and providing resources to people who want to, you know, do experimentation on these topics.
[917.90 → 926.88] Then, you know, the open source community together will be just as good as, you know, any company that is working on this in a closed manner.
[927.12 → 936.72] And so instead of reinventing the wheel, we can all invent it together and come up with something perfect that's good for developers, interesting for the academic community and other stuff like that.
[937.26 → 941.30] Could you talk a little bit about how you bring developers into this process?
[941.30 → 951.30] You know, as you since that's kind of foundational to how you're operating, could you talk a little bit about what you're looking for, how you bring people into your community and kind of ramp them up on that?
[951.92 → 953.74] Yeah. So it's kind of interesting.
[954.30 → 969.50] Our software is a little bit complex because there's necessary complexity in order to do things like make a very strong agent, give it all the tools it needs, allow it to run safely and things like this.
[969.50 → 978.62] So, you know, if people, one thing that we try to do is we try to, if people are interested, point them in the direction of issues they could start working on.
[979.00 → 986.72] We have a unique problem, which is a lot of the easy issues that would be good for developers to learn more about the code base are just solved by the agent.
[987.74 → 992.06] So we're still working through the best way to fix that.
[992.06 → 996.92] But, you know, especially front end stuff, you know, we have a new front end capability that we'd like to have.
[997.02 → 999.74] We've had a lot of people join successfully through that.
[999.90 → 1004.52] And then we've had longer term research projects where we collaborate together with, you know, people in universities.
[1004.94 → 1009.34] And we've been pretty successful at doing some interesting things there, I think.
[1009.34 → 1018.18] Cool. Yeah. I'm wondering, Robert, from the perspective of obviously, sometimes this is hard to do on an audio podcast.
[1018.18 → 1026.26] But if you could just give a sense, like I just logged into to all hands, you know, not that long ago online.
[1026.26 → 1028.18] So I see some visuals.
[1028.18 → 1030.48] But if you could maybe paint the picture.
[1030.64 → 1040.02] So there's like the open source side of things, which I'm assuming means people could maybe host all hands themselves, which might be interesting for some.
[1040.02 → 1043.28] But you also have kind of a hosted version of that.
[1043.50 → 1057.02] Could you just talk us through like those options, how kind of people can access this and, you know, what they'll see, how they integrate or how they connect their code into all hands to get started?
[1057.12 → 1058.52] That kind of getting started picture.
[1059.26 → 1060.42] Cool. Yeah. Yeah.
[1060.46 → 1063.20] So for the open source, everything runs inside of Docker.
[1063.36 → 1065.04] So that includes the application itself.
[1065.04 → 1072.46] You just run Docker run, and you'll see, you know, a web interface running at localhost 3000 and you can just drop in a prompt to the agent.
[1072.88 → 1079.18] You can also connect it to GitHub by generating a token inside your GitHub settings, plugging that into the UI.
[1079.68 → 1082.34] And then you can start to pull and push to your repositories.
[1082.84 → 1089.62] It's a little bit tricky running things locally because not only do we run the application in Docker, but when you start a new conversation with the agent,
[1089.62 → 1097.04] we want to make sure the agent's work is done in a nice sandbox way, so the agent gets its own Docker container to work inside.
[1097.48 → 1098.62] So there's a little bit of trickiness.
[1099.50 → 1103.78] We have to deal with a lot of like troubleshooting, you know, why isn't Docker behaving properly kind of stuff.
[1104.24 → 1107.20] So it's a little bit of a difficult application to run locally.
[1107.20 → 1113.04] So we actually created app.allhands.dev where you can use open hands in the cloud.
[1113.74 → 1120.72] This is a really just like, it's pretty much, you know, one for one in terms of the functionality with the open source.
[1121.26 → 1129.40] But there are a bunch of convenience features because, you know, A, we have this persistent server in the cloud and B, we can take care of all the infrastructure for running these sandboxes for the agent.
[1129.40 → 1139.40] So, you know, for instance, when you start up a conversation in the cloud, sandbox comes up within like one or two seconds rather than having to wait like 30 seconds or so for it to start up on your local machine.
[1140.06 → 1149.64] And we also can like to connect into GitHub a little bit more seamlessly because we can have an OAuth application where you just like one click log in and, you know, we can access everything.
[1149.64 → 1161.26] And then the cloud feature that I love more than anything is that if you can, if you leave a comment in like a, like a pull request, like say the tests are failing, you can just say add open hands, please fix the tests.
[1161.64 → 1170.04] And because we have this long live server in the cloud that can just kick off a conversation automatically and open hands will just commit back to your, to your pull request.
[1170.36 → 1175.40] Those are actually the interactions I love the most where I don't have to go into the open hands UI and like fiddle around.
[1175.40 → 1182.04] I just inside of GitHub or soon inside of Slack, I just, you know, summon the agent, and it just does the work for me.
[1182.20 → 1185.92] And I get to, you know, reap the fruits at the end there.
[1186.40 → 1187.98] My favourite is programming from my phone.
[1188.46 → 1191.80] So you log in, you log into the app and then just tell it what to do.
[1191.96 → 1193.44] I do that while I'm walking to work.
[1193.50 → 1195.70] And by the time I get to work, I have a pull request to review.
[1195.94 → 1199.80] So, you know, it opens up a lot of possibilities if you don't have to run it locally.
[1199.80 → 1200.34] Yeah, yeah.
[1200.34 → 1206.62] I could imagine also like just in the spur of the moment, like thinking of some great feature to add.
[1206.76 → 1208.60] And a lot of those things are lost, right?
[1208.66 → 1216.12] So if you have the ability to just, I know some people, or it's when they're running on a treadmill, or they're coming out of the shower or something,
[1216.12 → 1223.78] they can just like pop in and give a prompt and like have some work be done and then finish getting ready and get into work.
[1223.88 → 1224.70] I love that idea.
[1224.70 → 1225.64] Yeah, it's funny.
[1225.70 → 1230.80] I feel like I'm still getting a lot of coding done despite being the CEO of the company and being in meetings all the time.
[1230.86 → 1235.80] Because as I'm going into a meeting, I'll just like quickly be like, hey, do X, Y, Z, go into the meeting.
[1235.86 → 1238.46] And then once I'm done, it's just the codes that are waiting for me.
[1239.04 → 1239.52] It's funny.
[1239.58 → 1247.34] You guys are actually already leaping ahead and answering the question I was about to ask as I was thinking, Robert, on your first answer a moment ago.
[1247.34 → 1258.02] And that's really, you know, it's dramatically changing the workflow and the and, you know, not only the workflow, but, you know, how and where you're coding and stuff like that.
[1258.40 → 1260.46] As what I'm kind of curious.
[1260.56 → 1265.50] I mean, this is, you know, if you've been developing for a long time, this feels a little bit magical.
[1265.50 → 1285.26] And as you've had users come into this new workflow, what are the kind of the mindset shifts that are either challenges or maybe most welcome on the conversely that, you know, that get people productive and useful and recognizing the utility of this and benefiting from it?
[1285.30 → 1291.50] Because there's a little bit of a leap from kind of, you know, where they, where they grew up into the bold new world of this.
[1291.50 → 1295.62] What, what's that mind shift like and, and, and how do you get people through that?
[1296.22 → 1297.22] Yeah, it's a great question.
[1297.32 → 1304.58] It's, it's actually very similar to when I started managing folks for one, like you, you just have to get good at thinking like, oh no, I should delegate this.
[1304.74 → 1310.62] You have to like kind of have that switch flip and like your instinct is like fire up BS code and just like start working.
[1310.62 → 1319.28] And you have to, you have to have, like have that moment of like, oh no, like this is actually a good thing for the agent to work on or for my employee to work on.
[1319.28 → 1321.60] Uh, there's also like a little bit of a trust thing, right?
[1321.62 → 1324.66] Like when I first started managing folks, I wanted to micromanage them.
[1324.84 → 1327.30] I wanted to like to tell them exactly how to do everything.
[1327.82 → 1331.00] Uh, and it ended up being just more work for both of us and frustrating for them.
[1331.28 → 1337.48] Once I learned to like to trust my employees and know that like, they might not do it exactly like, like I would do it, but like, they're going to do a good job.
[1337.62 → 1342.78] They might need some coaching and some direction, but building, building that trust over time is, is really important.
[1342.78 → 1344.06] And it's the same thing with the agent.
[1344.36 → 1346.26] You know, the agent isn't always right.
[1346.32 → 1348.94] You do need to, you know, I like to say trust, but verify, right.
[1348.94 → 1361.30] You need to read its code and like, understand what it's trying to do and where it might've misunderstood something and maybe iterate a few times through, uh, either like a code review in GitHub or by just like chatting with it inside the application itself.
[1361.64 → 1370.18] But yeah, very, very similar to that management experience of like learning to kind of take your hands off the keyboard and, uh, be really clear with somebody else about communicating.
[1370.18 → 1373.80] These are the requirements and, uh, here's how you can improve and things like that.
[1373.80 → 1374.16] Yeah.
[1374.16 → 1374.44] Yeah.
[1374.72 → 1385.08] Graham, I, I have maybe a question that I also get a lot of times, you know, one is actually related to, you know, Chris just asked one question that I get a lot, which is the workflow related stuff.
[1385.08 → 1399.14] But the other question that I get a lot related to these types of tools is, Hey, I've seen people create a lot of cool demos with these sorts of tools, small projects that you can kind of like sort of regenerate if it doesn't work.
[1399.14 → 1406.20] But if I'm working in a large existing code base to, to the points that were brought up earlier, that's where most development happens.
[1406.20 → 1436.18] What are the technical pieces that have to be in place for you to have an agent work in a kind of larger code base or an existing project and actually have the context that's needed to, you know, needed to do things that fit, you know, have the context of the other things that exist in the code base, but also potentially the context of, you know, maybe it's a company, you know, style or, or other things like that.
[1436.22 → 1462.02] Yeah, it's a good question. For reference, the open hands agent is the largest committer to our code base. So we're definitely in our code base is rather large and complex. So I just checked now, and it had 209 commits over the past three months and the next closest contributor had 142. So it's doing pretty well. But there are a bunch of technical pieces that need to go together to make that work.
[1462.02 → 1478.96] The underlying language model is really important. And fortunately, a lot of the kind of core language model providers are focusing on this. We're also, you know, training language models ourselves. But the underlying language model needs to have a lot of abilities.
[1478.96 → 1500.36] One kind of boring but extremely important one is the ability to edit files. So about six months ago, this was a major problem for most language models. They were not able to successfully generate a diff between what the file used to, what a portion of the file used to look like and what the new portion of the file would look like.
[1500.36 → 1504.78] Or they would like to add an extra line or duplicate things or stuff like this.
[1504.78 → 1513.04] So this was a major problem. Claude is very good at this right now. A lot of the other language models are kind of catching up to be good at doing this.
[1513.04 → 1523.00] Another thing that's kind of like, especially a big problem for large code bases is identifying which files to be modifying.
[1523.96 → 1530.92] And this is somewhat less of a big problem than I originally thought it would be.
[1530.92 → 1535.92] Like, I was kind of imagining that this would be a really huge problem.
[1535.92 → 1543.94] But actually, language models are pretty good, even if you give them no tools to specifically like search a code base or something like that.
[1543.94 → 1552.32] They use finding, grew, and like all the other tools that a normal programmer might use and are able to kind of navigate their way around the code base.
[1552.32 → 1557.48] But I do think that like code search and other things like this can help this.
[1557.48 → 1567.82] And we have some preliminary results that demonstrate that it doesn't necessarily improve your resolution accuracy, but it definitely improves your speed of resolution.
[1568.46 → 1569.82] And so that's another thing.
[1570.34 → 1580.38] Being able to run tests and iterate on tests, being able to write appropriate tests that test whether a new piece of functionality or adding is actually working as expected or not.
[1580.38 → 1586.86] Being able to try, on the language model side, being able to try lots of different possibilities.
[1587.28 → 1596.94] So, for example, one big failure case of a lot of language models is they try the same thing over and over and over again and get in loops and never get out of that.
[1597.68 → 1606.40] And models like Claude are good at not doing this, whereas a lot of other models fall into this failure mode and don't do as well.
[1607.02 → 1608.18] So, the list kind of goes on.
[1608.18 → 1613.96] I could talk about this for much longer, but those are some of the kind of most important parts, I think.
[1614.80 → 1619.96] Well, Graham, you're already getting into this, which is another thing that I wanted to ask about.
[1620.30 → 1627.40] Maybe you could comment from your angle of the technical and research side.
[1627.40 → 1636.16] And Robert, I'd be curious on the kind of business product side about generally why you got into also building models.
[1636.92 → 1643.66] And for those that want to kind of take a look, there's some really great models that All Hands has released.
[1644.52 → 1647.46] It's just all dash hands on Hugging Face.
[1647.66 → 1651.24] And you can read a little bit more, and we can talk about the details here.
[1651.24 → 1657.18] But yeah, maybe first, just like, why was that a step that you all felt was important?
[1657.40 → 1662.08] And or kind of wanted to be part of your contribution to the space?
[1662.78 → 1665.46] Yeah, so there are two reasons.
[1666.06 → 1675.74] The first reason is, you know, we are an open source company and we kind of philosophically believe in, you know, open source and openness.
[1675.74 → 1684.20] And if you're relying on a closed API based model entirely, then, you know, you can never fully achieve that goal.
[1684.20 → 1696.38] Another thing is practically there are issues with customizability and cost for closed models.
[1696.72 → 1699.86] And the best closed models are somewhat expensive.
[1700.52 → 1708.84] They, you know, there's a non-trivial cost involved with using them to do agentic tasks, especially because you need to query them over and over and over again.
[1708.84 → 1725.96] And so having another option that's more cost-effective that we can either like just use as is or possibly switch over to that for easier portions of a task, but use a more expensive model for the less easy portions of the task is, you know, something that would be useful.
[1725.96 → 1727.86] And then customizability.
[1728.18 → 1743.30] We have a lot of our kind of enterprise customers or design partners asking for some variety of customizability, be it to their code base or to a programming language that they're interested in working with and other things like this.
[1743.30 → 1752.00] And if we don't have a model that we can fine tune, you know, we are limited in our scope of things that we can customize.
[1752.52 → 1756.58] So looking forward, that's something that we would like to do.
[1756.66 → 1758.22] And we're not we're not done yet.
[1758.32 → 1760.16] Like we just released V 0.1.
[1760.40 → 1764.36] So we'll definitely continue being interested in this in the future.
[1764.36 → 1765.16] Awesome.
[1765.36 → 1765.50] Yeah.
[1765.62 → 1780.92] From the guess from the product perspective, Robert, like in terms also of the hosted version that you're running, the one that people can can log into, are the models that you have you've you've built?
[1781.04 → 1786.98] Are those integrated to one degree or another in that kind of live product, or what's the kind of roadmap there?
[1787.66 → 1788.10] So, yeah.
[1788.10 → 1790.60] So right now it's all cloud 3.7 under the hood.
[1790.60 → 1795.44] One, there are some really cool ways where we can build where we can build our models into the process.
[1796.12 → 1809.48] One is if we can route certain parts of the agentic loop or certain queries to a cheaper model rather than putting everything through the most expensive model out there without sacrificing accuracy.
[1809.70 → 1812.98] That's that's really great for our users because we can pass those savings on to them.
[1813.24 → 1815.38] So that's that's one fascinating path.
[1815.38 → 1828.32] Another path that we have where we have a model that is specifically trained basically to recognize whether open hands is on the right track to solving a problem or if it's like going off the rails.
[1828.32 → 1828.58] Right.
[1828.58 → 1832.06] So we built this model specifically based on the data set that we've gathered.
[1832.36 → 1842.78] And that's a really cool product feature because on the one hand, like you can just recognize, like, did we achieve did we solve the task or did we not and like to report back to the user appropriately?
[1842.78 → 1849.20] We can stop the agent if it's like going off the rails, and we can say, hey, this is what's going wrong.
[1849.28 → 1851.52] Please reroute, you know, using this new strategy.
[1852.04 → 1856.02] We can also like launch several different trajectories towards solving a problem.
[1856.02 → 1861.84] And then, you know, maybe pick one out of the out of the three that we launched and say, OK, this one looks like it's going in the best direction.
[1862.40 → 1864.22] Keep following this one and kill the other two.
[1864.76 → 1871.76] So lots of really cool stuff we can do there by having a model that specifically knows kind of the inputs and outputs of what open hands is doing.
[1871.76 → 1881.38] Well, while you're talking about that, I'm wondering, could you talk a little bit, you know, with whether the models we've kind of talked about the, you know, the frameworks and stuff being open?
[1881.58 → 1886.92] Are you looking at models that you're creating being open or does that say as part of a proprietary offering?
[1887.02 → 1897.16] How are you envisioning that from, you know, in terms of what the models are, what they're addressing, whether they're larger or smaller models, what licenses apply, that kind of thing?
[1897.16 → 1901.28] Could you speak a little bit about your philosophy and strategy toward that?
[1901.76 → 1904.88] Yeah, I mean, so far it's its we're opening everything up. Right.
[1906.08 → 1913.34] We've we've taken the position that we basically want open hands to be as useful as possible to an individual developer running it on their workstation. Right.
[1913.34 → 1916.04] You know, we are a company. We do want to make money.
[1916.24 → 1922.62] And so we are building some closed source features specifically for like large teams who are using open hands together.
[1922.90 → 1930.02] But so far, we've taken the position that basically all the research we do and all the like know how for how the agents do as good a job as possible.
[1930.12 → 1933.48] It's like software tasks that should be open source that should be available to every developer.
[1933.48 → 1946.10] And it's stuff like collaboration features, things like multi tenant, things like auditing, compliance, stuff that like big enterprises need that your average developer working on an open source project doesn't need.
[1946.30 → 1951.60] That's what we're going to hold back and say, OK, this is closed source, and we're going to enable big enterprises to do this stuff.
[1951.60 → 1954.10] You know, the way the big enterprises like to do things.
[1954.60 → 1961.58] And one other follow up, just because I happen to work in an industry where security and privacy are really paramount.
[1961.98 → 1968.74] How are you thinking about like with, you know, with going instead of going off to one of the large foundation models via cloud?
[1968.86 → 1975.34] Often that runs into challenges for enterprises that have security concerns in particular.
[1975.34 → 1987.00] Any thoughts on or something that you can offer for when it needs to be, you know, all held close, closely held data that cannot go out onto a cloud connection, that kind of thing.
[1987.08 → 1990.02] What you're thinking about that either for present or for the future?
[1990.72 → 1992.42] Yeah. So we basically have three offerings.
[1992.42 → 1995.66] We've got the open source, which anybody can run and use for free.
[1995.66 → 2007.80] A lot of security conscious companies do start with the open source because everything they can hook it up to bedrock or, you know, a local model or, you know, basically they can plug into the existing models that the company has approved.
[2008.20 → 2017.78] We have the cloud offering, which all runs through Anthropic, all runs through our servers, which is a great convenience for a lot of people, but kind of scares off some companies that are very security conscious.
[2017.78 → 2024.30] But then we can also take basically all the infrastructure we've built for our cloud offering and ship it into somebody else's cloud.
[2024.42 → 2026.76] So you can run it all inside your AWS environment.
[2026.94 → 2028.10] You can connect it to bedrock.
[2028.58 → 2031.52] So it's basically all configured to stay within your walls.
[2031.52 → 2051.94] I'm wondering, kind of just thinking about like current functionality and, you know, what you know, Graham, you mentioned all of these commits from all hands in your own repo and some of those kind of easy, maybe first issues that the developers could solve.
[2052.00 → 2053.50] Maybe those are taken care of.
[2053.50 → 2057.80] But how do you see kind of the level of performance now?
[2058.06 → 2067.22] Like, how are you all measuring that and kind of red teaming that testing that over time and thinking about improving that over time?
[2067.34 → 2073.68] How do you even kind of consider something like that, given that there are so many different types of projects out there?
[2073.72 → 2075.74] Obviously, there are academic benchmarks.
[2075.74 → 2081.08] I think, you know, you have the SWE bench and those sorts of things.
[2081.30 → 2088.28] But as a product, as an offering, how do you how do you think and measure kind of that performance over time?
[2088.28 → 2091.44] And what right now is like performing very well?
[2091.44 → 2094.00] And maybe where are those areas of improvement?
[2094.46 → 2095.56] Yeah, it's a great question.
[2095.66 → 2096.88] There's a lot to that question.
[2097.16 → 2101.16] But just about how we are doing benchmarking.
[2101.16 → 2112.16] Up until recently, we were doing a lot on SWE bench, but we have a very large evaluation harness that actually already has 20 benchmarks incorporated into it by our academic partners.
[2113.08 → 2130.62] And one thing that we're thinking about doing going forward and are actually kind of in the process of doing is we have identified the common use cases, the ways that people typically use open hands and tried to identify, you know, benchmarks that reflect these use cases.
[2130.62 → 2134.30] And then do a more balanced benchmarking strategy across these.
[2135.18 → 2151.86] So we have some pretty exciting results about things like web navigation and web information gathering, which is really, really important for like if you want to function in an environment where you have lots of docs or learn about a new library or do data processing, data science related tasks.
[2152.68 → 2158.34] And then we're also doing things like making sure that you can fix broken commits.
[2158.34 → 2162.46] So you have like a pull request that has failing tests and merge conflicts.
[2162.60 → 2163.50] And can you merge that in?
[2163.56 → 2167.90] And this is something developers hate to do, but like need to do all the time.
[2168.06 → 2171.34] So this is something we're putting a lot of effort into making sure we're good at.
[2171.46 → 2176.62] And we have some good results about that we hope to release soon.
[2176.62 → 2187.00] And then other things like test generation, version updates, things like this, like the academic world is large.
[2187.22 → 2192.10] So it turns out there are benchmarks for almost all of these that have already been created by some institution somewhere in the world.
[2192.20 → 2198.06] And so very often we like talk to these institutions and say, hey, do you want to contribute this into our evaluation harness?
[2198.06 → 2203.08] And, you know, often the answer is yes, because, you know, they did their work for a reason.
[2203.18 → 2203.98] They want it to be used.
[2204.24 → 2212.36] So we're using that as a way to expand our kind of like vision of benchmarking to cover the actual use cases that the users are most interested in.
[2212.36 → 2223.16] Well, as we start to wrap up here, one of the things that we really like to do is to kind of get a sense of the future going forward.
[2223.32 → 2233.38] And with both of you here, I'd like to ask the same question of each of you and get each of your takes for a little bit of diversity on how you're seeing the thing.
[2233.38 → 2249.24] But as you've kind of introduced us into this kind of new way of thinking about development going forward and what's possible for old guys like me, it takes it's definitely changing how I think about development.
[2249.76 → 2252.60] And this is moving really, really fast right now.
[2252.68 → 2254.32] And, you know, it's accelerating.
[2254.32 → 2273.24] I'd love to understand how each of you sees the future both in the space itself in terms of, you know, changing the world in terms of developer workflows and your role in that process as an organization and as an open source community, how you see those going forward.
[2273.68 → 2278.92] I'll let you guys decide who wants to go at it first, but would love to hear each of your perspectives.
[2278.92 → 2285.60] Yeah, I think the thing that that's really exciting for me is the idea of bringing the next, you know, a billion developers into the fold.
[2286.36 → 2295.50] You know, when I first started learning to code, I felt like a wizard, like I could just all of a sudden make my computer do anything and I could build all sorts of different applications.
[2295.50 → 2297.52] And I was, you know, a baby engineer.
[2297.64 → 2299.02] I was building all sorts of nonsense.
[2299.48 → 2303.26] And I just I felt so powerful and so excited.
[2304.00 → 2306.12] And then that like that fades over time.
[2306.12 → 2308.86] And, you know, it becomes a job.
[2309.06 → 2312.78] And then I would say over the last year or two, I've got that excitement again.
[2312.82 → 2314.86] I feel like a wizard again.
[2314.96 → 2320.30] I can get so much done, you know, using large language models and using agents.
[2320.74 → 2334.08] And so I'm really excited to bring that feeling to like a whole new tranche of people who have maybe had ideas for software that they want for, you know, work clothes that they want for applications that they'd like to have and just haven't been able to like to bring them to life.
[2334.08 → 2337.42] And I think it's really exciting that they'll, they'll be able to do that.
[2337.64 → 2340.72] I think there are a lot of questions as to like how we enable them.
[2340.90 → 2346.26] Like, you know, my mom definitely has some really cool ideas, but she has no business like monitoring a production database.
[2346.26 → 2352.18] And so I think we're going to need to rethink like how infrastructure works and how we ship applications and things like that.
[2352.34 → 2356.58] I think there's a lot of thought that is going to need to go into that.
[2356.58 → 2359.64] And I'm really excited to see kind of what shakes out.
[2360.32 → 2365.10] Yeah, I love Robert's answer, but from a completely different angle.
[2365.64 → 2378.64] One of the things I have in my introductory slides to like a presentation I give about coding agents is looking at the Nobel Prize winners from last year in physics and chemistry.
[2378.64 → 2386.26] And the Nobel Prize winners in physics were people like Jeff Hinton and the ones in chemistry were people like Demi's Hussites.
[2387.16 → 2394.24] And, you know, these are obviously the top awards in areas other than computing.
[2394.24 → 2399.88] And I'm building agents to create software.
[2400.32 → 2405.64] But the reason why I'm building agents to create software is not because software is the end.
[2405.96 → 2409.10] It's because software is like a means to an end.
[2409.10 → 2423.34] And I think like AI has a huge possibility to increase, you know, the impact and the human condition and things like this.
[2423.34 → 2426.78] But I think the way it's going to do that is through software, basically.
[2426.78 → 2440.58] And so if we can make it very easy to effectively create software and make it very accessible to the people who want to use it, you know, we'll be able to make great strides forward.
[2440.86 → 2443.78] And so that's, you know, what I'm most excited about.
[2444.90 → 2447.82] Well, we're definitely excited to see what you all are doing.
[2447.82 → 2457.00] It's amazing work and really just encouraged to hear also your perspective on the project and the way in which you're building.
[2457.20 → 2461.52] I encourage all of our listeners to go and check out all dash hands dot dev.
[2461.86 → 2463.04] Check it out. Try it out.
[2463.42 → 2466.74] And yeah, thank you both for joining and taking time.
[2466.80 → 2467.30] It's been great.
[2467.70 → 2468.30] Thanks for having us.
[2468.64 → 2469.16] Thanks so much.
[2469.16 → 2477.20] All right.
[2477.48 → 2479.32] That is our show for this week.
[2479.44 → 2485.64] If you haven't checked out our change log newsletter, head to change log dot com slash news.
[2485.82 → 2488.10] There you'll find 29 reasons.
[2488.30 → 2491.68] Yes, 29 reasons why you should subscribe.
[2492.16 → 2493.50] I'll tell you reason number 17.
[2493.86 → 2496.86] You might actually start looking forward to Mondays.
[2496.86 → 2499.74] Sounds like somebody's got a case of the Mondays.
[2500.12 → 2504.68] 28 more reasons are waiting for you at change log dot com slash news.
[2505.04 → 2510.58] Thanks again to our partners at fly dot IO to break master cylinder for the beats and to you for listening.
[2511.02 → 2513.68] That is all for now, but we'll talk to you again next time.
