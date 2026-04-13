[0.00 --> 8.74]  Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 --> 13.64]  of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 --> 19.14]  Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 --> 23.54]  Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 --> 25.12]  buzz, you're in the right place.
[25.12 --> 29.84]  Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 --> 33.02]  drops, behind-the-scenes content, and AI insights.
[33.36 --> 35.88]  You can learn more at practicalai.fm.
[36.18 --> 37.50]  Now, on to the show.
[48.22 --> 51.80]  Welcome to another episode of the Practical AI Podcast.
[51.80 --> 53.58]  This is Daniel Leitnack.
[53.72 --> 59.64]  I am CEO at Prediction Guard, and I'm joined, as always, by my co-host, Chris Benson.
[59.84 --> 63.02]  Who is a Principal AI Research Engineer at Lockheed Martin.
[63.58 --> 64.30]  How are you doing, Chris?
[64.60 --> 66.98]  I'm doing just dandy today, Daniel.
[67.18 --> 68.66]  Getting ready as we record this.
[68.78 --> 71.60]  We're approaching Halloween, so I'm getting in the spirit.
[72.00 --> 73.40]  All sorts of sweet treats.
[73.68 --> 75.62]  Thank goodness the listeners can't see me.
[75.62 --> 84.20]  But yeah, I'm busy growing out my costume in this week beforehand, so I don't look so good.
[84.38 --> 86.04]  So yeah, glad this is audio only.
[86.12 --> 86.62]  Thank goodness.
[87.04 --> 88.30]  Well, you're in between.
[88.56 --> 91.42]  Yeah, you're getting ready for the festive season.
[91.74 --> 92.68]  That's okay.
[92.88 --> 93.18]  That's right.
[93.38 --> 96.86]  Not quite to no-shave November, I guess.
[97.70 --> 101.02]  But you could stretch it out through November.
[101.02 --> 103.78]  I'm starting to become the monster under the bed, maybe.
[104.40 --> 105.22]  There you go.
[105.62 --> 109.84]  Speaking of sweet treats, our guest today has me thinking about cake.
[110.32 --> 117.96]  Because a little while ago, we had Jared Zonereich, who is co-founder and CEO at Prompt Layer, join us.
[118.20 --> 124.70]  And of course, always reminded of their nice cake logo, which is making me hungry right now.
[124.84 --> 126.20]  I'm wanting some dinner.
[126.78 --> 128.50]  But welcome back to the show, Jared.
[128.56 --> 129.28]  It's great to have you.
[129.28 --> 130.10]  Thank you.
[130.20 --> 130.70]  Thank you.
[130.78 --> 132.66]  I'm excited to be back.
[132.86 --> 139.42]  And a fun note for you, I'll tell you, we're designing our booths to go to conferences now.
[139.46 --> 142.10]  And I think we're going to bring real cakes to the booths.
[142.10 --> 142.44]  That's awesome.
[142.60 --> 143.26]  You should.
[143.72 --> 144.16]  Definitely.
[144.48 --> 144.62]  Nice.
[144.68 --> 145.62]  Steer into it.
[146.26 --> 146.92]  Yeah, yeah.
[147.18 --> 149.28]  Just have those little...
[149.94 --> 156.44]  I see at the airport occasionally, they have those little vending machines where you can get cake out of the vending machine.
[156.44 --> 160.32]  And it's in a little plastic thing you pull open and eat while you're at the airport.
[160.32 --> 162.76]  So yeah, I think that's a great idea.
[163.42 --> 164.86]  But I'm just looking.
[165.22 --> 168.42]  We last talked to you March of 2024.
[168.82 --> 170.56]  So episode 261.
[170.90 --> 177.68]  Folks, go ahead and can loop back and hear from Jared when we had this initial discussion, which was great.
[177.68 --> 182.84]  At the time, Jared, everyone was, of course, talking about the...
[183.80 --> 190.94]  I think we were still in the days of everyone talking about kind of prompt engineers and prompting going crazy.
[191.20 --> 197.62]  Certainly, people are still talking about prompting, but maybe they've shifted in some ways focus.
[197.62 --> 204.92]  As you've been kind of at some of the center of discussions around prompting, how people are engaging with AI.
[205.10 --> 208.46]  From your perspective, what has the year been like?
[208.60 --> 215.76]  How have things kind of changed in people's perceptions of prompting AI systems?
[215.76 --> 219.38]  Or maybe even your own thoughts around prompting AI systems?
[219.80 --> 222.06]  And of course, we can get into agent stuff later.
[222.34 --> 223.66]  But yeah, any thoughts?
[223.66 --> 226.26]  Well, we're still called prompt layer.
[226.62 --> 228.00]  So we haven't changed that yet.
[228.12 --> 228.92]  I don't think we will.
[229.66 --> 234.60]  But yeah, so March 2024, a year, a year and a half almost ago.
[234.88 --> 235.96]  It's almost...
[235.96 --> 239.64]  It would be hard to even list all the big AI things that happened since then.
[239.82 --> 245.12]  I mean, the one that immediately comes to mind, though, is reasoning models.
[245.52 --> 248.76]  So reasoning models, I think OpenAI released 01.
[248.90 --> 252.60]  I think I saw a tweet that it was like a year from last week or something like that.
[252.60 --> 257.98]  And that was, I think, the first next generation of prompting.
[258.24 --> 262.82]  Meaning before, if you recall, probably our last talk, we talked about chain of thought.
[263.28 --> 266.52]  And now I guess the reasoning model does the chain of thought for you.
[266.60 --> 268.06]  And just the models have been getting better.
[268.64 --> 281.14]  But at the core, the core way to think about LLM applications as an input to an output or input to the LLM, meaning the prompt and the model and then the output, that's all the same.
[281.14 --> 283.36]  I think it's gotten much easier.
[283.50 --> 284.68]  The models have gotten much better.
[285.18 --> 286.64]  They're easier to steer.
[286.96 --> 293.90]  And some of the weirdness of how you persuade the model and yell at the model has changed, has gone away.
[294.04 --> 296.36]  And it's gotten a little bit more straightforward.
[296.72 --> 301.42]  But I think, yeah, I think prompting is still at the core of everything.
[301.42 --> 306.76]  And I will have to say the new word people love to say is context engineering, of course.
[307.10 --> 308.66]  And to me, they're the same.
[308.84 --> 314.24]  But I think the main reason people like this word context engineering is it's not just the prompt.
[314.42 --> 315.32]  It's not just the text.
[315.54 --> 318.20]  It's how much are you putting in the text?
[318.26 --> 319.12]  Are you putting too much?
[319.16 --> 320.38]  Is the model getting distracted?
[321.06 --> 322.36]  Are you using rag?
[322.40 --> 323.36]  Are you not using rag?
[323.40 --> 324.70]  Are you throwing in a blob?
[324.82 --> 326.68]  Are you using multiple models?
[326.68 --> 334.84]  And I think my high level one sentence of what's changed would be we have way more tools at our disposal now.
[335.08 --> 338.30]  And we have way more mixing and matching.
[339.06 --> 339.66]  Interesting.
[339.96 --> 340.12]  Yeah.
[340.12 --> 352.86]  And I guess that how would you distinguish or how might your thinking around kind of context engineering, you know, maybe that is a term that's coming up.
[353.40 --> 358.36]  What do you think is kind of just some jargon that's changing?
[358.36 --> 368.60]  And what do you think is kind of a more substantive part of what that means and maybe why people are shifting language if there is one?
[369.46 --> 369.60]  Right.
[369.60 --> 379.12]  I think the key around context engineering and the reason, well, we're a little financially invested in prompt engineering because we made hats that say prompt engineer on it.
[379.22 --> 381.78]  So maybe that's where my bias comes from.
[382.80 --> 384.00]  But maybe we'll make both hats.
[384.58 --> 387.50]  But I think context engineering really gets to this.
[388.18 --> 390.24]  Well, one context is much longer.
[390.38 --> 393.36]  So you can send so much more to a model than a year and a half ago.
[393.62 --> 396.60]  It's almost unlimited from a user perspective.
[396.60 --> 400.18]  And the question is, how do you send it?
[400.32 --> 403.30]  How do you make how do you squeeze the juice out of the model?
[403.72 --> 406.70]  Models, I like to think, get distracted like us humans do.
[406.82 --> 410.16]  So how do you not lead it down the wrong path?
[410.16 --> 422.38]  And the core difference, though, on how we build stuff is I think there's been much more because models have gotten better and because we can fit more in the context.
[422.38 --> 441.32]  We've moved from and we've seen this with our customers moved from complex DAGs or complex workflows where you say this prompt goes to this prompt and this prompt goes to that prompt to something a little more autonomous and a little more agentic and a little more of just a while loop with tool call.
[441.32 --> 443.36]  Everything is a while loop with tool calls now.
[443.64 --> 446.06]  But that's a whole different topic.
[446.28 --> 447.36]  But let me leave it at that.
[448.16 --> 448.88]  I'm curious.
[449.12 --> 458.36]  Just to kind of pick up on that point, though, I think I mean I'm guessing a lot of our listeners can really feel an association with what you're just talking about, about that evolution.
[458.36 --> 470.20]  I know that like in my own job, it's not a primary responsibility, but as an ancillary, I often get asked to talk to groups in our company about how to prompt and stuff.
[470.46 --> 477.24]  And some of the things we had put out internal videos like that I put out a year and a half ago that are completely obsolete.
[477.52 --> 483.54]  And so I'll come back to a group and I'll be like that whole thing I told you before, don't do it that way anymore.
[483.54 --> 491.72]  It's gotten a little bit more capable, a little bit more sophisticated, drop the the the structured framework a bit.
[492.08 --> 496.98]  I'm curious, you know, so I'm kind of backing out of what I told them a year and a half ago at this point.
[496.98 --> 500.66]  And I'm sure a year and a half from now, I'll be doing the same thing with what I'm doing today.
[500.66 --> 512.06]  So like how do you address when you're dealing with end users how to evolve with the capabilities that the model and the infrastructures are providing these days?
[512.06 --> 514.74]  Because it's really hard to track that fast, quite honestly.
[515.30 --> 520.34]  It takes me many hours a day of scrolling on Twitter to keep in touch with what's going on.
[520.84 --> 527.50]  I would say so I guess for context for everybody, we're a platform for building and testing LM applications.
[527.50 --> 539.18]  And people are using us to version their prompts, version their agents, evaluate them, log them and generally just build a AI system that's working.
[539.28 --> 543.14]  So we get asked this question all the time of like, how do we track it?
[543.18 --> 544.04]  What should we do today?
[544.56 --> 545.98]  And also we have the same problem.
[546.10 --> 551.08]  We we have YouTube videos or interviews where maybe I rewatch it.
[551.20 --> 552.88]  I'm like, oh, well, that's not true anymore.
[552.98 --> 554.06]  Now you could just use this.
[554.28 --> 556.00]  Thank goodness it's not just me.
[556.00 --> 557.72]  Yeah, I mean, it's everyone.
[557.90 --> 558.64]  It's open AI, too.
[558.74 --> 559.54]  It's anthropic, too.
[559.64 --> 560.08]  It's Gemini.
[560.64 --> 568.24]  I think I think the answer is to lock into the core truths of building LM systems.
[568.50 --> 571.10]  And how we look at it is it's a philosophy thing.
[571.58 --> 575.30]  It's I guess there's there's two there's two competing ideas here.
[575.36 --> 578.10]  And I'm curious also to hear your opinions on this.
[578.10 --> 587.42]  But there's the academic idea of how do you understand LLMs and how do you understand which the context and how it works.
[587.42 --> 595.64]  And then there's the tinker, the builder philosophy, which we push people towards, which is it's a black box.
[595.64 --> 596.86]  I don't need to understand it.
[596.96 --> 599.76]  I just need my input to match to what I want in the output.
[599.76 --> 608.46]  And I usually give a really annoying answer to teams who use us because we get on a lot of calls with our customers.
[608.58 --> 609.60]  We're not a consulting product.
[609.78 --> 612.66]  We're a software, but we love to help our customers and we like to share knowledge.
[612.66 --> 627.08]  So we get on a lot of these calls and almost always my answer to a specific question of should I use GPT-5 or should I use Sonnet-4-5 or should I use Gemini is that I don't know the answer.
[627.28 --> 628.70]  I don't think OpenAI knows the answer.
[629.06 --> 630.90]  I don't think Anthropic knows the answer.
[631.16 --> 640.06]  The only person who can know the answer is you for your own use case by building tests and checking and seeing what works.
[640.06 --> 642.42]  Basically, it's a black box.
[642.82 --> 645.06]  You just have to try it out and see if it works.
[645.28 --> 648.14]  And that's the only repeatable motion here.
[648.40 --> 649.84]  I know it's an annoying answer, though.
[650.64 --> 651.40]  No, it's good.
[651.80 --> 664.54]  And I think it's an answer that flows with the times because anything that you would say is going to be, you know, anything that any of us say today is obsolete tomorrow with the way this thing accelerates.
[664.94 --> 667.86]  So it's not as annoying as you might think.
[667.86 --> 674.24]  It's a framework for figuring out the answer instead of relying on us three.
[674.74 --> 678.22]  And it's how do you think about testing?
[678.34 --> 679.78]  Because testing them is really hard.
[680.22 --> 684.00]  And figuring out if your output is good and if the prompt works is really hard.
[684.14 --> 690.96]  So how do you build heuristics and how do you build evals and how do you even or how do you skip the eval?
[690.96 --> 697.40]  Like, just how do you how do you approach this is the interesting thing, at least to me.
[697.74 --> 697.84]  Yeah.
[697.92 --> 703.56]  And I think I agree with you, Jared, in terms of like the spectrum that you were talking about.
[703.72 --> 714.50]  The reality is a lot of people don't need to know what, you know, self-attention, you know, means, for example, to build cool AI automations.
[714.50 --> 727.08]  I think there is like on the flip side of that, I guess there would be this kind of like you need kind of enough of a mental model to understand kind of maybe the coverage of to your point.
[727.08 --> 741.84]  Like, I think this is partially why the testing is so hard, because sometimes it may not be clear to you like, oh, if I, for example, change the formatting of my prompt without changing any of the words, why would that change anything?
[741.84 --> 745.40]  And kind of these things around prompt sensitivity and other things.
[745.50 --> 745.62]  Right.
[745.62 --> 765.84]  So some of that, like some of that can be built up through tinkering, but maybe also comes even with this kind of mental model, maybe not so much of like what the models are, but I find sometimes like how they operate in generating output is often a trigger for people to know like, oh, well, now it makes sense.
[765.84 --> 774.40]  Maybe why kind of like things could go off the rails with, you know, high temperature or other other things like that.
[774.40 --> 788.18]  So, so, yeah, I don't know if you have any thoughts on that, but that that's kind of my thought is that there's like a different kind of mental model or intuition that you need less so the academic kind and more so like how how things operate.
[789.08 --> 791.06]  Yeah, a hundred percent agree.
[791.06 --> 800.00]  I think, I think the, I think you could have too much academic knowledge of how LMs work and that actually might hurt you in this because you try to understand what you're doing.
[800.66 --> 807.02]  Whereas a lot of these things are pretty hard to understand and maybe people don't, it's, it's in the neural net somewhere.
[807.32 --> 812.76]  But I think what you're referring to, I like to refer to it as an LLM idiom.
[812.96 --> 815.86]  So how do you, how do you understand the language of LMs?
[815.86 --> 822.26]  I think the example you gave was good about formatting, like JSON formatting has been a big topic people talk about.
[822.66 --> 827.06]  Can you just give JSON to the model instead of a prompt and how will that work?
[827.80 --> 840.48]  And I think it's a really illustrative example because giving, asking the model to return JSON or a structured format will work really well if you want to return precise numbers or precise values.
[840.48 --> 847.10]  But if you want to write a love note, it's probably not going to work as well because the model is now in I'm coding gear.
[847.54 --> 857.08]  It's like if you go into maybe, I like to, I always compare it kind of the, I don't think AI is human, but I think there's some things we can kind of use as metaphors.
[857.08 --> 863.66]  So it's like if you go into an engineering school and you just give someone a paper and say, write a love note, they're, they're thinking about code.
[863.74 --> 869.88]  They're not in the brain space of, of poetry as opposed to maybe they are good at it.
[869.94 --> 877.04]  Maybe they can do it, but you kind of have to step back and say, okay, this is what we're thinking about in the same way as if you're asking the model to output.
[877.04 --> 885.42]  So JSON and output a key and curly braces, it's probably not going to write as good creative language in one of those values.
[886.10 --> 900.78]  And I can't write academic proof for you on why this is true, but it, it is, it's a, it's like an idiom, it's intuition, it's a way to talk to the LM without using so many words, I think is where I'm kind of settling around.
[900.78 --> 907.54]  And you may have just identified why my last anniversary with my wife just went off the rails, you know, the JSON output for the love note.
[908.00 --> 910.54]  I thought I had it, but you know, clearly not.
[912.94 --> 927.08]  Yeah, it's a, you gotta, you gotta be careful with it, but it's really an important thing of, I mean, when we're talking as humans, we have idioms that we can say one word and you're going to think of a whole different thing.
[927.08 --> 936.98]  If I mentioned Beethoven, or if I mentioned Kanye West, you're, you're not, you're not thinking of just the person, you're thinking of everything surrounding them.
[937.20 --> 938.50]  And I think it's the same thing here.
[938.54 --> 941.08]  And it's the same, you're putting it in a probability space.
[942.22 --> 947.50]  And if you want to be in this part of the probability space, it's going to be a little bit more challenging.
[947.50 --> 971.72]  So Jared, I do want to dig into something that you said a little bit earlier, which is there has been this progression, maybe from static workflows or kind of prompt chaining where you have like a DAG, which people, if they're not familiar, like that's sort of a one directional graph of like this logic that the chain of calls to the AI system is going through.
[971.72 --> 976.34]  You kind of mentioned that shifting more to kind of a while loop with tool calls.
[976.66 --> 977.76]  So could you break that down?
[977.86 --> 989.06]  I mean, first of all, like maybe for those that aren't familiar, kind of what you might, what you mean by kind of tool calling and then like what, what this means to have a while loop of, of tool calls.
[989.48 --> 989.62]  Yeah.
[989.92 --> 995.02]  So maybe the best way to start is to like paint the evolution here.
[995.02 --> 1004.80]  So like you just mentioned DAGs, these one direction, these basically graphs that are just a bunch of nodes that say this node goes into this node, this node goes into this node.
[1005.22 --> 1011.52]  The reason we started with that is because models were a little unpredictable because of hallucinations.
[1011.52 --> 1018.18]  If you were at the beginning of this LLM craze, let's say two years ago, three years ago, maybe three years ago is too much.
[1018.28 --> 1018.84]  Maybe it didn't exist.
[1018.94 --> 1019.28]  No, yeah.
[1019.50 --> 1021.40]  Something like three years ago was chat GPT.
[1021.40 --> 1028.70]  If you're a United Airlines and you're making a customer support chat bot, you don't want to accidentally give people free flights.
[1029.40 --> 1035.70]  And to avoid doing that, the best way to do it would be to build these structured paths that LLM can go down.
[1035.82 --> 1040.20]  So the first question would decide what the user was asking.
[1040.30 --> 1043.68]  And if the user was asking for a refund, it would go to the refund prompt.
[1043.68 --> 1053.16]  And this is kind of how, let's call it prompt engineers, context engineers, agent engineers, whatever you want to call it, stopped LLMs from going off the rails.
[1054.20 --> 1059.22]  Now what's changed is two big, let's call it innovations.
[1059.42 --> 1066.24]  One, just models are better at following instructions and hallucinations really don't happen that much anymore.
[1066.24 --> 1072.08]  And the second thing is models have gotten much better at structured outputs.
[1072.50 --> 1077.80]  So before it was kind of hacky to get the model to return in a way that code can process it.
[1078.18 --> 1084.48]  Now tool calling, which I'll explain in a second, is baked into all the main models.
[1084.64 --> 1095.90]  So what tool calling is, is basically you're telling your prompt, you're giving the instructions to the prompt, but you're also telling the prompt it has access to a few different functions.
[1095.90 --> 1100.90]  So in the United Airlines example, maybe the functions are issue refund.
[1101.34 --> 1104.42]  Maybe there's another function of check user status.
[1104.56 --> 1108.24]  When you use chatgpd.com, it has access to search the web.
[1108.32 --> 1113.72]  It has access to like when you're generating an image, it's probably like a generate image type tool.
[1113.72 --> 1126.72]  So this way, as we've built more tool calls, a lot of the models have been built around tool calls and have gotten really good at interacting with them, interpreting their response, sending another message to them.
[1127.14 --> 1130.22]  And that's why you see so many more autonomous agents.
[1130.22 --> 1147.88]  Like if you look at Cloud Code, or you look at Codex, the reason coding agents are actually good now is because of this paradigm and because they've actually simplified everything and said, instead of this complex tag where we think through every single step, we're going to actually kind of give the model a little bit more free reign.
[1147.88 --> 1155.04]  Let the model run things, see if it works and actually fix it because models are turned out to be really good at fixing their own mistakes.
[1155.42 --> 1159.40]  And what that has unlocked is a lot more flexibility for the model.
[1159.40 --> 1168.16]  So now if you use Cloud Code, which is for Codex or any of these coding agents in the command line, they have only access.
[1168.40 --> 1172.88]  It's the we wrote a few blog posts on how it works behind the hood.
[1173.02 --> 1180.24]  But the simple way to explain it is it's one loop that says continue until the AI is done and then ask the user for input.
[1180.44 --> 1183.44]  So I'll say make my application work.
[1183.44 --> 1189.36]  And then now it'll start the loop and it has access to just right in the terminal, like a human.
[1189.54 --> 1191.26]  So it'll write something, it'll get the output.
[1191.88 --> 1197.38]  And then it'll decide, do I wait for a user response or do I want to run another tool call?
[1198.14 --> 1207.14]  And this simple loop is much easier to develop, much easier to debug, and kind of just the way everybody's gone.
[1207.14 --> 1213.66]  Of course it has disadvantages, but that's kind of the way I see it in terms of where we've gone.
[1214.02 --> 1229.44]  I'm curious, as we talk through this and, you know, as we've transitioned into the sygentic world, especially since we talked to you last time, you know, over the last year and a half, it's really, you know, come on strong, you know, versus where our conversation was back then when that was a very new thing.
[1229.44 --> 1237.54]  What kind of incumbencies does this whole new set of capabilities bring to the user when they're trying to think?
[1237.70 --> 1246.56]  You know, we've talked a little bit already in this conversation about kind of the evolution of prompting context and, you know, the rapidity of that.
[1247.12 --> 1256.20]  But, you know, as we move into the sygentic world, any thoughts around what the user's new responsibilities are to be effective in that?
[1256.20 --> 1260.16]  Yeah. The user as in the builder of an AI application?
[1260.66 --> 1270.34]  The user in this case as in the human who's listening to our podcast right now and is going to turn to their system at the end of the show and go, I'm going to go try that.
[1270.56 --> 1272.86]  Totally. Totally. So a little of both, maybe.
[1272.86 --> 1289.20]  I think if you're just a user on chatbd.com or you're using an AI application that's available, codex, cursor, whatever, it's capable of doing much more and working for a much longer time and staying on track more.
[1289.20 --> 1294.70]  And you kind of can have a it can do a better job.
[1295.16 --> 1298.38]  I know of figuring it out, let's call it.
[1298.38 --> 1312.28]  So if you if you want to do a general task or do an exploration because of this new concept that people are using to build AI applications, these AI agents are able to try something.
[1312.48 --> 1316.96]  If it doesn't work, try something else and do the exploration that humans would do.
[1317.12 --> 1319.38]  And we're really just trying to make them act more like a human.
[1319.38 --> 1326.48]  And the DAG way, the old way that we're talking about, where you have a bunch of nodes and you have a structured way, that's not how humans work.
[1326.72 --> 1333.86]  When you when you when you give an intern a task, you're not giving them the exact flow chart of how to solve it.
[1334.14 --> 1340.16]  You're telling them generally what tools they have at their disposal and they're going to keep working and using the tools and figure it out.
[1340.26 --> 1347.34]  Now, for the builder behind these applications, what it gives them is it makes it a little bit harder to test.
[1347.34 --> 1354.40]  It makes it a little bit harder to keep things on the rails, but it makes it much quicker to build something that succeeds.
[1354.58 --> 1359.86]  We built a agent using cloud code that updates our docs every day.
[1360.30 --> 1368.08]  It looks at all the code our team has written over the last 24 hours and decides if it should be in the docs and then updates it.
[1368.50 --> 1377.02]  Took me two hours to build because all I said was download these repos, read the commits and then check our docs and see if it should change.
[1377.34 --> 1381.02]  And then it gets to figure it out. Now, is this going to be good for a production system?
[1381.30 --> 1386.34]  Maybe it needs a little bit more work, but for something simple, it opens a lot of use cases.
[1387.24 --> 1398.88]  And what would you say, I guess, as you mentioned, you're focused on kind of a platform around kind of building, testing, versioning, improving AI workflows or agents.
[1398.88 --> 1404.12]  With these kind of while loop tool calling things, right?
[1404.34 --> 1418.04]  If you have kind of a variety of tools that could be called under the hood and you have kind of part of the complexity of the system, I guess, is in the tools that you can call.
[1418.04 --> 1436.44]  How does that influence, I guess, like the way that you should version or test these systems or does it even in the sense that you kind of now, whereas before it felt like there was kind of a single function that I'm calling into with a prompt, right?
[1436.44 --> 1440.02]  And that function produces output, which may or may not be useful.
[1440.64 --> 1448.08]  Here, you have kind of this recursive function that feeds into itself and could call any number of things.
[1448.28 --> 1453.76]  And so like when you look back, if you're just looking at the input and output, I guess is what I'm saying.
[1453.76 --> 1461.70]  Then any number of things could have gone wrong in that kind of recursive loop or in that while loop that you're talking about.
[1461.80 --> 1472.02]  So how does that, I guess, how does that influence kind of the prompts that you would version, how you iterate on those, how you test and improve the systems from your perspective?
[1472.56 --> 1473.54]  Totally. It makes it interesting.
[1473.54 --> 1486.00]  So at the end of the day, the tool calls that are being run, the functions are still those input output things that can be unit tested and that could be really thoroughly and rigorously tested.
[1486.38 --> 1488.02]  The hard part is this while loop.
[1488.20 --> 1494.00]  So I think the core master prompt, the one that runs the loop, that could be tested in a lot of ways.
[1494.16 --> 1496.00]  You can run sanity checks.
[1496.10 --> 1497.62]  You can test against old data.
[1497.70 --> 1498.98]  You could see how things changed.
[1498.98 --> 1512.00]  But what you're getting at is this really interesting problem that's kind of been created, which is how do you test a flexible agent where flexibility is kind of one of the keys to it, what makes it good?
[1512.42 --> 1517.42]  I think there's kind of the heuristic I've developed is something I want to call it.
[1517.44 --> 1519.86]  Maybe I'll write a blog post about it, like agent smell.
[1520.34 --> 1525.54]  So if you run an agent, what sanity checks can you see to see if it smells a little funky?
[1525.54 --> 1528.82]  Like is something, is it raising any red flags?
[1528.86 --> 1529.80]  And I'll give you some examples.
[1530.06 --> 1538.06]  So if I was building a agent to, let's say, to fix errors in my application.
[1538.32 --> 1548.70]  So like if I had a database error and I wanted to build an agent that would go and fix the code automatically, I would want, if I wanted to test this agent, what I would test for is how many tool calls is there?
[1548.92 --> 1550.70]  First, I just want to surface these statistics.
[1550.86 --> 1552.06]  How many tool calls is it running?
[1552.56 --> 1554.54]  How many times is it retrying the tool calls?
[1554.54 --> 1556.44]  How long does the agent take?
[1556.82 --> 1558.34]  And these are kind of surface level things.
[1558.46 --> 1563.08]  They're not end all be alls, but you first want to start simple.
[1563.18 --> 1571.72]  So you first want some sort of smell test where you can say, hey, this new version is behaving very differently than my old version.
[1571.80 --> 1573.70]  Maybe better, but maybe worse.
[1573.98 --> 1578.02]  And then that's when you go in and break down like a state by state test.
[1578.02 --> 1586.00]  So the most useful tests we see our users doing are individual states or full conversation simulation.
[1586.20 --> 1590.04]  So individual states would basically be saying, here's conversation history.
[1591.10 --> 1593.66]  Now run that to the tool and what's the next step?
[1593.74 --> 1595.84]  And we're just checking if the next step is the same.
[1595.84 --> 1597.98]  Of course, that's only one part of the picture.
[1598.18 --> 1601.58]  The other part of the picture is here's the initial instructions.
[1601.80 --> 1605.64]  Now simulate the whole conversation and see if the final output's correct.
[1605.96 --> 1608.08]  And then combine that with the smell.
[1608.24 --> 1610.14]  And it doesn't give you a full picture.
[1610.14 --> 1621.40]  But I think the core learning we've had, at least since the past year and a half, is that you don't need to have 100% coverage when you're evaluating these things.
[1621.58 --> 1626.42]  If anything, if you're trying to make a perfect test for your agents, you're probably never going to ship.
[1626.84 --> 1629.86]  And you're probably going to, it's just going to, you're never going to do it.
[1630.30 --> 1638.94]  The better thing is to make it good and have heuristics of figuring out when it's regressed before it does.
[1638.94 --> 1643.58]  So Jared, we talked through a little bit of this agentic stuff.
[1643.58 --> 1666.90]  And I know you set up some of the conversation where you as a company are enabling kind of non-technical users to kind of work on prompts, embed their domain knowledge, kind of have that kind of non-technical connection to the prompts under the hood, which are maybe embedded in various systems or tools and that sort of thing.
[1666.90 --> 1688.40]  I'm wondering about your perspective on, obviously, one of the things that's been talked about in recent months a lot is this kind of like 95% of AI pilots failing and that sort of thing, which we've talked about on the show, the report from MIT and gave some thoughts.
[1688.40 --> 1702.50]  But I'm wondering how you think that intersects with the way that the tools that people are using to manage their prompting their AI systems, maybe the rigor that needs to be there that's not.
[1703.02 --> 1712.08]  Or maybe like there's another side of this where kind of some of those engineering principles need to be brought into the picture.
[1712.08 --> 1718.40]  Yeah. What is your thought kind of from working with a lot of non-technical users on a platform like this?
[1718.88 --> 1733.18]  You know, what have you learned over time to be those kind of key pieces of making sure that those people coming to a problem don't end up just wasting a lot of their time working on something that doesn't actually get results?
[1733.18 --> 1741.60]  Right. So maybe 95% of AI pilots fail, but they're not using front layer.
[1741.74 --> 1742.22]  So that's why it's.
[1742.24 --> 1745.88]  Yeah, exactly. That was the setup for the question.
[1747.48 --> 1750.22]  0% of AI pilots in front layer fail.
[1750.48 --> 1754.80]  Yeah, exactly. Same with prediction guard. Yeah, exactly.
[1754.98 --> 1755.30]  Exactly.
[1755.50 --> 1756.34]  Exactly. Yeah.
[1756.34 --> 1764.88]  They're not using the right tools. I would say. So as a platform, how we look at it is prompt layer.
[1765.46 --> 1774.14]  We have a large diversity of teams ranging from super technical and all engineers to basically no engineers and everything in the middle.
[1775.76 --> 1784.22]  And what we are trying to do is build a rigorous process for building these applications and expose it to the people who know if the outputs are correct or not.
[1784.22 --> 1791.44]  So what I mean by this is rigor in terms of versioning and knowing which versions are working.
[1792.06 --> 1802.00]  Rigor in terms of being able to test, like we're just talking about testing agents, testing prompts, and also rigor in terms of logging and seeing what's happening in production, what's going on.
[1802.04 --> 1810.90]  Because you can only test so much in development in AI and you kind of need to expand the surface area of how people use your product.
[1810.90 --> 1825.22]  But the reason we focus a lot on getting these domain experts involved in the process is because we believe actually from a business perspective, that's how you win as an AI company.
[1825.46 --> 1830.36]  If you're building legal AI, you win by having a lawyer involved.
[1830.36 --> 1833.96]  The example I always give and I love going back to.
[1834.38 --> 1835.90]  So I come from a family of psychologists.
[1836.26 --> 1837.18]  It skipped me.
[1837.56 --> 1838.24]  I'm an engineer.
[1838.88 --> 1842.42]  But I have some familiarity with it.
[1842.68 --> 1844.76]  And if you want to go to see a shrink.
[1844.76 --> 1849.56]  But now you're just psychoanalyzing the language that's going into models.
[1849.76 --> 1852.28]  So I guess your family can be proud.
[1853.16 --> 1854.22]  I hope so.
[1854.56 --> 1854.78]  Yeah.
[1855.42 --> 1856.38]  I hope so.
[1856.52 --> 1857.40]  I'm working on it.
[1857.40 --> 1861.78]  But if you want to see a shrink, there's like six on the block, right?
[1861.82 --> 1862.68]  I live in New York City.
[1862.90 --> 1863.76]  There's a lot of them.
[1864.24 --> 1868.84]  And the assumption I'm making here is that there's no global maximum.
[1869.20 --> 1872.34]  There's no one correct answer to psychology.
[1872.94 --> 1874.40]  You know, you have different methods.
[1874.50 --> 1875.20]  You have CBT.
[1875.36 --> 1876.98]  You have ayahuasca retreats.
[1876.98 --> 1880.16]  You have a lot of different ways to treat people.
[1881.08 --> 1882.90]  And same with medical doctors.
[1883.14 --> 1884.72]  Same with education.
[1884.90 --> 1885.78]  Same with a lot of things.
[1885.78 --> 1892.60]  And what's the core differentiator between the different psychologists on the block that my office is on?
[1893.06 --> 1893.78]  The taste.
[1894.14 --> 1896.40]  And how they choose to practice their field.
[1896.64 --> 1898.52]  They're all going to the same education.
[1898.68 --> 1900.58]  Maybe some have a little bit more knowledge than others.
[1901.16 --> 1905.08]  But how they implement their product, let's say.
[1905.08 --> 1915.80]  And in the same way as if you're building an AI therapist, how you win as a business is the non-engineering taste that's been put into the AI product.
[1916.18 --> 1922.70]  And the way it's using the context that you provided and what you've told it to do.
[1922.70 --> 1932.58]  And going back to your question of how do you take that knowledge of needing the non-technical engineer.
[1932.58 --> 1936.38]  Or like we think an AI engineer should be non-technical.
[1937.70 --> 1941.24]  But how do you bring in those engineering principles so the pilot doesn't fail?
[1941.24 --> 1946.08]  And a lot of times we see engineering actually owns the product, the AI product.
[1946.18 --> 1951.64]  So we're usually talking to a VP of engineering or CTOs or something like that to get Promlayer installed.
[1952.28 --> 1955.34]  Because we're all engineers on our team.
[1955.44 --> 1956.62]  We're bringing in these principles.
[1956.78 --> 1964.70]  We think even if it's a non-technical expertise, you have to do it in an organized and systematic way.
[1964.70 --> 1974.58]  And that's why you see the skill of prompting, I almost think, is not quite the same Venn diagram as the skill of coding.
[1974.70 --> 1976.12]  Because it's really a skill of tinkering.
[1976.34 --> 1977.70]  And not all coders are tinkers.
[1978.24 --> 1981.46]  But not all writers are tinkers either.
[1981.62 --> 1987.40]  So there's some new type of algorithmic thinking that overlaps very highly.
[1988.00 --> 1988.20]  Yeah.
[1988.42 --> 1990.30]  It's almost like being a negotiator.
[1991.38 --> 1991.58]  Exactly.
[1991.58 --> 1998.04]  It is, but it also, you know, maybe you have organizations that are leaning one way or the other.
[1998.22 --> 2004.82]  You know, you've just kind of described that spectrum of skill and expertise that apply.
[2004.82 --> 2014.22]  And so possibly for whatever problem your organization is trying to solve, trying to find the right place on that spectrum to bring the right resources together.
[2014.22 --> 2021.80]  And that, like, even aside from what we're talking about here, that's an easy place for businesses to fall down anyway across.
[2021.94 --> 2028.18]  And so in a sense, it may not be that different from any other business problems that companies are trying to face.
[2028.64 --> 2029.18]  Yeah, totally.
[2029.18 --> 2035.48]  It's like, what can we learn from non-AI world to ship these things better?
[2035.84 --> 2042.80]  To us, the big thing that, the big mistake people make is they try to boil the whole ocean at the beginning.
[2043.06 --> 2044.26]  And they try to do too much.
[2044.26 --> 2050.74]  And really, you want to do the whole crawl, walk, run when you build these systems.
[2050.98 --> 2061.16]  And you want to maybe, instead of the pilot being, hey, we're going to add a billion dollars of revenue with our AI product, you want to say, all right, we're going to make a beta version.
[2061.32 --> 2062.70]  Maybe we'll only release it internally.
[2062.92 --> 2063.62]  Maybe we'll do this.
[2064.14 --> 2064.88]  Maybe it won't do everything.
[2064.94 --> 2066.94]  Maybe it won't be the while loop with all the tool calls.
[2067.04 --> 2068.42]  Maybe it'll just be one tool call.
[2068.42 --> 2072.22]  And that's also true with how you test these things and how you build them.
[2072.28 --> 2080.40]  So it's not just what the product does, but it's a lot of teams get stuck at trying to build tests because they try to build perfect tests.
[2080.74 --> 2084.34]  And like we were saying, it's hard and maybe even impossible.
[2085.14 --> 2088.04]  And there's a learning process, which that kind of implies.
[2088.36 --> 2098.08]  Crawl, walk, run is that it gives companies a chance to not crater too hard when they're first starting out as they're trying to get something done.
[2098.42 --> 2107.88]  Keep it small enough scope so that they can actually achieve something small but positive and learn from that and kind of build up toward what their true aspirations might be.
[2108.38 --> 2108.66]  Exactly.
[2108.88 --> 2110.02]  I mean, we're all learning.
[2110.32 --> 2110.46]  Yeah.
[2110.56 --> 2111.44]  And I don't know.
[2111.52 --> 2122.58]  When you said crawl, walk, run, Chris, it made me think like some of the problem might be that people don't understand what is crawling, what is walking, what is running.
[2122.76 --> 2125.02]  Like it all just looks like AI tasks.
[2125.02 --> 2129.74]  Like it's a big soup of things that you can sort of quote do with AI.
[2130.00 --> 2134.88]  And it's unclear, you know, how do I pick out the crawling tasks?
[2134.88 --> 2138.70]  Because I don't know which of them it is.
[2138.84 --> 2141.96]  I see that kind of paralysis a little bit.
[2142.16 --> 2150.30]  I don't know if you see that as well, Jared, or have any suggestions for like how people can think about, you know, picking apart.
[2150.30 --> 2161.28]  Because you mentioned like those domain experts who are coming into, you know, prompt layer and you're connecting those people with the business knowledge into prompt layer.
[2161.28 --> 2172.06]  You know, how is it that they come upon the knowledge to know what is a kind of crawl task or a feasible task to like start with and play around with?
[2172.16 --> 2173.04]  Any thoughts?
[2173.92 --> 2175.24]  Yeah, it's a good point.
[2175.36 --> 2183.16]  I think the most successful teams, AI teams I've seen work in collaboration between engineering and domain experts.
[2183.16 --> 2189.86]  So if you're just domain experts or you're just engineers, you can succeed and I've seen it succeed.
[2190.02 --> 2195.34]  But the most common way and what we recommend is it should be a joint effort.
[2195.86 --> 2201.54]  The engineers often know how to ship a product and how to do agile or iterative design.
[2201.76 --> 2205.52]  And the non-technical understand what makes it good.
[2205.84 --> 2207.02]  And you need both of these.
[2207.02 --> 2213.32]  I think how to break it down, it's almost the crawl task.
[2213.50 --> 2217.36]  It's almost you have to just step back and say, what is my heuristic here?
[2217.90 --> 2219.06]  Let's talk about testing.
[2219.28 --> 2223.12]  Just what's the crawl task in testing of our AI application?
[2224.32 --> 2228.76]  The hard examples are like something like summaries where there is no ground truth.
[2228.92 --> 2233.28]  So what is the crawl task of evaluating an AI note taker?
[2233.28 --> 2237.70]  Well, you kind of have to step back and say, as a human, what is a good summary?
[2237.88 --> 2238.86]  All right, what's the simplest thing?
[2238.94 --> 2241.92]  Maybe the simplest thing is just saying, is the summary in English?
[2242.28 --> 2246.58]  Maybe doing another element as judge where we say, does it use markdown?
[2246.70 --> 2249.80]  And then maybe another one that says, is it less than a page?
[2249.92 --> 2254.46]  And these are all obviously not end-all, be-all tests, but it's the crawl.
[2254.60 --> 2258.48]  And then once that's working, you can check for hallucinations.
[2258.62 --> 2260.50]  And then maybe you can check for a style.
[2260.50 --> 2263.46]  But it's very use case dependent.
[2263.80 --> 2266.42]  So it's hard to give a one-size-fits-all there.
[2267.06 --> 2271.12]  So I want to turn things as we're starting to get closer toward the end.
[2271.28 --> 2273.52]  And I want to ask kind of a fun question for you.
[2273.80 --> 2275.16]  I know you like Cloud Code.
[2275.64 --> 2280.12]  And so I wanted to ask some of the things that you're playing around with and what you're doing
[2280.12 --> 2282.04]  and what's got you excited on it.
[2282.52 --> 2282.70]  Yeah.
[2283.22 --> 2286.98]  And I will say, I like Cloud Code, but I also like Codex.
[2287.08 --> 2288.08]  I also like Cursor.
[2288.48 --> 2289.36]  I also like AMP.
[2289.36 --> 2292.68]  AMP is doing really cool stuff with the free coding agent too.
[2292.78 --> 2294.38]  So I switch between all of them.
[2294.64 --> 2299.18]  I think I give Cloud Code a lot of credit for being the first really useful coding agent
[2299.18 --> 2299.74]  that I've used.
[2300.18 --> 2300.84]  What am I doing?
[2301.30 --> 2302.72]  So a lot.
[2302.94 --> 2308.04]  We redid our whole engineering philosophy around these coding agents at Promlayer.
[2308.04 --> 2315.28]  Basically, the hard part about building a platform, as you guys likely know, is all these little things
[2315.28 --> 2317.48]  and the death by a thousand cuts.
[2317.66 --> 2324.02]  So we have to work on big features, but also the UX of like this button here doesn't have a loading state
[2324.02 --> 2329.24]  or this is not draggable here is how you could fail if you don't fix those.
[2329.24 --> 2330.82]  And that list piles on.
[2331.56 --> 2333.18]  So now we have a new rule in our company.
[2333.56 --> 2338.62]  If it takes less than two hours to do using Cloud Code or Codex or something, just do it.
[2338.70 --> 2339.44]  Don't ask anyone.
[2339.44 --> 2340.88]  Don't prioritize it.
[2341.40 --> 2343.24]  And it's helped a lot.
[2343.38 --> 2349.30]  Honestly, our customers have literally told us like, wow, you guys are shipping so much faster now.
[2349.30 --> 2355.78]  So I think everyone who says, oh, it actually makes you a slower coder is just full of it.
[2355.94 --> 2356.88]  You know, it's so good.
[2357.22 --> 2359.58]  And I use it for non-technical things too.
[2359.90 --> 2366.28]  If I want to go through a CSV, I'll tell you one thing I did recently that is pretty interesting
[2366.28 --> 2367.56]  and non-technical.
[2367.56 --> 2374.46]  I went to an event and I won't say which one because then people will be like, oh, that's why I'm getting spammed.
[2374.62 --> 2380.18]  But I went to an event and everyone was pretty interesting on the event.
[2380.50 --> 2384.46]  And I basically copied and pasted the list of users there.
[2385.30 --> 2387.18]  Actually, I gave the HTML to Cloud Code.
[2387.28 --> 2393.58]  I said, make it into a CSV of all the people there who click going and whatever social media you have.
[2393.58 --> 2399.14]  And then I put it into PromptLayer and I actually like added new columns.
[2399.28 --> 2402.64]  So I like did a batch of like find where they were, find their whatever.
[2402.80 --> 2404.38]  And then you could go back to Cloud.
[2404.48 --> 2408.34]  I went back to Cloud Code and did some data processing and saying like, who should I contact?
[2408.34 --> 2412.60]  And just doing like random tasks like that and batch prompting.
[2412.76 --> 2415.20]  Like I combine PromptLayer with it, of course.
[2415.40 --> 2421.20]  But random stuff, like sending emails, creating random UIs for like to understand a company.
[2421.72 --> 2422.84]  I use it for everything.
[2423.08 --> 2424.32]  I'm constantly on it.
[2424.46 --> 2426.84]  I constantly vibe code these days.
[2426.84 --> 2432.88]  And we sat down with everybody on our team and Cloud Coded with them just so they can see how good it is.
[2432.94 --> 2434.04]  Because a lot of people are skeptical.
[2434.78 --> 2436.48]  And it's great.
[2437.86 --> 2439.24]  That's great, Jared.
[2439.42 --> 2450.80]  I love the tie-in to even this sort of like combination of things that it's like when Anthropic released Quad Code,
[2450.80 --> 2457.62]  I don't know that they imagine all of these like trickle-down effects of like things in the way that people are combining it with other things.
[2457.74 --> 2460.18]  And like even the non-technical things that you mentioned.
[2460.66 --> 2462.64]  So it's really cool to see how that plays out.
[2463.08 --> 2469.46]  As you kind of look towards the future, as we get to the kind of wrapping up here,
[2469.74 --> 2475.44]  tell us a little bit about kind of what excites you kind of moving into this next year.
[2475.44 --> 2481.62]  And, you know, when we talk again in the next year and a half or whenever it is,
[2481.78 --> 2484.76]  what you're excited about during that period of time,
[2484.88 --> 2490.28]  like related to prompt layer and related to kind of things in general and how the ecosystem is evolving.
[2490.64 --> 2491.66]  I'm excited about a lot.
[2492.38 --> 2496.88]  The simplest one, because we're talking about it, these coding agents as a headless tool.
[2497.24 --> 2499.72]  So using them in your workflows to run things.
[2499.86 --> 2500.50]  That's exciting.
[2500.68 --> 2504.32]  I'm excited about especially non-technical uses of these things.
[2504.32 --> 2509.12]  I think you're going to, right now they're in a terminal and you're going to be using them for so much more.
[2509.42 --> 2514.46]  And then, cloud code aside, I'm very excited about the whole,
[2514.66 --> 2519.96]  how the space is evolving to a place where you have a lot of different tools at your disposal.
[2520.14 --> 2521.56]  Some models are really good at writing.
[2521.70 --> 2523.12]  Some models are really good at coding.
[2523.84 --> 2530.34]  And the consumer is just having more options than ever to building their product.
[2530.34 --> 2534.40]  I think we're not in a world of one model rules at all.
[2535.00 --> 2536.86]  There's a lot of ways to solve a problem.
[2537.00 --> 2541.02]  There's a lot of variability on how you build your product.
[2541.30 --> 2542.64]  And I think that's a good thing.
[2543.06 --> 2545.86]  I think I'm very, I think the future is great.
[2546.00 --> 2547.68]  I'm excited for AI to take over.
[2547.84 --> 2550.46]  I think I don't, I'm not worried about it at all.
[2550.46 --> 2554.32]  And yeah, I think, I think, and I'm honestly really excited.
[2554.32 --> 2558.00]  I know this is a little bit of a shill because this is what our company does.
[2558.06 --> 2564.58]  But I'm very excited about unlocking AI engineering for people who didn't study computer science.
[2564.80 --> 2573.54]  And I think this has been something people have talked about for so long of how do we democratize coding and get more people coding?
[2573.54 --> 2586.16]  And maybe people aren't going to be coding anymore, but the way to like people have expertise and now they're going to be able to build AI products around it and do AI engineering around it.
[2586.20 --> 2591.38]  And it's really, anybody's going to be able to distribute their work to almost infinite levels.
[2591.52 --> 2594.58]  So that's what keeps me up at night in a good way.
[2595.02 --> 2595.50]  That's awesome.
[2595.50 --> 2606.86]  And yeah, I would, I would definitely recommend, of course, we'll include links to PromptLayer in the show notes, but also as, as Jared mentioned, they have a, they have a great blog.
[2607.12 --> 2610.56]  You know, they've, they've released some, some excellent articles.
[2611.18 --> 2613.72]  They, they have great learning resources out there.
[2613.80 --> 2615.46]  So check out everything that they're doing.
[2615.82 --> 2622.76]  Really appreciate the way that you all are contributing to, to the ecosystem, Jared, and definitely keep up the good work.
[2622.76 --> 2627.16]  And we'll look forward to, to talking with you again next time you're on the show.
[2627.54 --> 2627.90]  Amazing.
[2628.00 --> 2628.26]  Amazing.
[2628.38 --> 2629.08]  Thanks for having me.
[2629.14 --> 2635.24]  And anyone can reach out on Twitter or on email or sign up for PromptLayer and get started for free.
[2635.34 --> 2637.40]  So excited to see what people build.
[2637.76 --> 2638.50]  Yeah, definitely.
[2638.90 --> 2639.24]  All right.
[2639.32 --> 2639.98]  Talk to you soon.
[2640.24 --> 2640.70]  Thank you.
[2647.70 --> 2648.40]  All right.
[2648.54 --> 2649.98]  That's our show for this week.
[2649.98 --> 2657.26]  If you haven't checked out our website, head to practicalai.fm and be sure to connect with us on LinkedIn, X, or Blue Sky.
[2657.54 --> 2663.24]  You'll see us posting insights related to the latest AI developments, and we would love for you to join the conversation.
[2663.74 --> 2667.50]  Thanks to our partner, Prediction Guard, for providing operational support for the show.
[2667.84 --> 2669.84]  Check them out at predictionguard.com.
[2670.24 --> 2673.88]  Also, thanks to Breakmaster Cylinder for the beats and to you for listening.
[2674.22 --> 2675.02]  That's all for now.
[2675.32 --> 2677.04]  But you'll hear from us again next week.
[2677.04 --> 2677.90]  Thank you.
[2677.90 --> 2680.64]  music
[2680.64 --> 2681.60]  music
[2681.60 --> 2681.62]  music
