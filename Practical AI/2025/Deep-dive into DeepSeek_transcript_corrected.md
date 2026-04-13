[0.00 → 10.06] Welcome to Practical AI, the podcast that makes artificial intelligence practical, productive,
[10.40 → 11.46] and accessible to all.
[11.46 → 14.48] If you like this show, you will love The Change Log.
[14.70 → 19.52] It's news on Mondays, deep technical interviews on Wednesdays, and on Fridays, an awesome
[19.52 → 21.38] talk show for your weekend enjoyment.
[21.84 → 25.82] Find us by searching for The Change Log wherever you get your podcasts.
[26.32 → 28.36] Thanks to our partners at Fly.io.
[28.36 → 31.10] Launch your AI apps in five minutes or less.
[31.40 → 33.38] Learn how at Fly.io.
[43.56 → 52.10] Well, welcome to the very first fully connected episode of Practical AI in 2025.
[52.62 → 58.34] In these fully connected episodes of the Practical AI podcast, Chris and I keep you
[58.34 → 64.14] fully connected with everything that's happening in the AI world and hopefully share some learning
[64.14 → 68.26] resources to help you level up your machine learning and AI game.
[68.90 → 69.70] I'm Daniel Whiten ack.
[69.82 → 75.52] I'm CEO at Prediction Guard, and I'm joined as always by my co-host, Chris Benson, who is
[75.52 → 79.02] a principal AI research engineer at Lockheed Martin.
[79.30 → 79.96] How are you doing, Chris?
[80.16 → 81.54] Doing good today, Daniel.
[81.54 → 85.52] It's a lot of interesting things happening out there in the AI world.
[85.52 → 91.82] And I love these conversations where we do these fully connected kind of deep dives into
[91.82 → 95.66] things that are of personal interest to you and me, which is how we choose them.
[96.14 → 99.36] And there are a lot of exciting things coming up.
[99.54 → 105.50] In these episodes, it's a little bit easier for us to kind of free-form talk about a few things.
[105.50 → 113.16] But for those listeners who have been seeing our logo for some time on the podcast feeds,
[113.28 → 117.18] just FYI, there'll be a change to that coming up.
[117.32 → 120.34] But no need to swap out our feed or anything.
[120.34 → 122.14] That should be good.
[122.28 → 125.60] We're still doing great things with the change log.
[125.76 → 131.54] And they've made a few changes to their shows and their lineup, publishing them in different
[131.54 → 132.00] ways.
[132.00 → 134.56] They have a show about that if you want to learn about it.
[134.70 → 140.66] But we'll still be going strong and excited kind of for probably a much-needed refresh.
[140.96 → 141.64] You know, I don't know.
[141.90 → 144.44] I think it's been like six and a half years or something.
[144.52 → 145.30] Hasn't it, Chris?
[145.66 → 146.24] It has been.
[146.52 → 148.50] We can change in six and a half years.
[148.62 → 148.98] I don't know.
[149.16 → 149.28] Yeah.
[149.46 → 152.92] I mean, six and a half years in GPU time is a long time.
[152.94 → 153.60] Yeah, that's expensive.
[154.18 → 154.38] Yeah.
[155.82 → 161.90] So yeah, just FYI, long time listeners to be aware, you might scroll through your podcast
[161.90 → 162.44] app.
[162.64 → 166.16] Look for a new logo sometime in the near future.
[166.80 → 170.76] But yeah, I think obviously that's bigger news than DeepSeek.
[170.76 → 179.02] But I guess we can devote most of the episode to what is the story of our week, couple weeks,
[179.34 → 183.60] and who knows how long, which has been DeepSeek R1.
[184.32 → 184.70] I know.
[185.02 → 189.50] This is, you know, I was thinking as we were saying that, speaking of GPU time, in this
[189.50 → 191.74] case, maybe a lot less GPU time.
[192.12 → 192.52] Yeah.
[192.58 → 195.78] A lot less on maybe an queer amount.
[196.66 → 197.38] That's true.
[197.52 → 198.14] Good point.
[198.44 → 198.60] Yeah.
[198.60 → 203.02] Because they only talked about the final run that was successful in terms of the spend
[203.02 → 203.40] on it.
[203.50 → 204.30] So yeah.
[204.46 → 204.68] Yeah.
[204.68 → 207.74] Well, I guess we're getting ahead of ourselves for those who are not as familiar with it.
[207.74 → 208.06] Yeah.
[208.22 → 214.00] So for those, probably many of those that are listening to this particular episode have
[214.00 → 215.68] come across DeepSeek.
[216.20 → 221.84] But for those that have not seen anything, maybe you've been under a rock somewhere.
[222.38 → 225.52] Chris, what are we talking about with DeepSeek?
[225.52 → 232.38] Ah, so we have, there's a Chinese startup that we're talking about here that has released
[232.38 → 240.32] a large generative model, LLM, that is, I guess, and I'm going to gloss over some stuff
[240.32 → 245.86] right here just because we'll dive into the specifics, but is very highly performant.
[246.04 → 250.40] It's comparable to the best models that OpenAI has had out there.
[250.40 → 259.60] But the thing that's really rocked everybody's world is the fact that it was trained at much,
[259.88 → 264.56] much less cost, at least the parts we know which we'll dive into that detail.
[264.56 → 268.06] As we said, there are some things we know and there are some things we don't know, but it
[268.06 → 275.58] appears to have been achieved at a much, much lower cost than all the competing models
[275.58 → 278.42] from anywhere in the world up to this point.
[278.42 → 286.30] And so, in short, the AI world, and I guess everybody outside the AI world that cares about
[286.30 → 292.36] this stuff, is in this giant debate and conversation about the implications.
[292.46 → 293.68] Is it a big deal?
[293.74 → 294.88] Not such a big deal.
[295.06 → 296.10] Why is it a big deal?
[296.86 → 298.26] You know, is it overblown?
[298.52 → 301.92] And of course, Daniel and I are about to dive into all of that right now.
[302.44 → 305.40] It's a target-rich environment, as we like to say in defence.
[305.40 → 308.72] Are they surveillant us while we use the model?
[308.86 → 309.34] Exactly.
[309.90 → 316.48] Could you, should you, might you run the model in all sorts of different ways?
[316.56 → 316.78] Yeah.
[317.22 → 322.98] There are tons of confusion around this, Chris, which is one interesting thing that hopefully
[322.98 → 326.56] after you've listened to this podcast, you're not more confused.
[326.92 → 328.26] We don't make that guarantee.
[328.72 → 332.10] But hopefully that's the case.
[332.58 → 333.30] Yeah, it's interesting.
[333.30 → 339.22] So I think one of the stories around this, and there's multiple kind of narratives that
[339.22 → 341.84] we can go into here, so much to talk about.
[342.52 → 351.80] One of the narratives is around how some Chinese startup with a much lower budget or spend on
[351.80 → 361.28] the model building built such a good model and essentially gets parity to models from Open
[361.28 → 362.22] AI and others.
[362.44 → 368.22] In particular, the comparison has been made to the O1 model, which if you remember, we talked
[368.22 → 369.30] about this on the show.
[369.30 → 373.20] This is OpenAI's sort of thinking, quote unquote, model.
[373.42 → 380.40] So the model, when it generates output, so you put in a prompt, the LLM generates text output.
[380.40 → 398.60] A beginning portion of that text is sort of thinking content, meaning they're training the model to sort of spit out logic of how to solve maybe a deeper problem or reason about the input prompt before it actually gives its final answer.
[398.60 → 404.40] If you're in the ChatGPT interface, you can see this kind of in a different colour or grayed out.
[404.94 → 408.82] If you're using the API, I don't think that they send that back in the API.
[409.28 → 412.34] You still pay for it, but I don't think they send it back.
[412.34 → 416.46] This is a similar type of reasoning model.
[417.08 → 418.50] So DeepSeek R1.
[419.36 → 432.44] And in this reasoning, this kind of very kind of flagship model of OpenAI, for example, the same kind of task, DeepSeek is kind of getting this what we could call parity.
[432.64 → 435.48] Now, you know, different benchmarks are out there, et cetera.
[435.70 → 440.20] And, you know, each model has its own biases and different behaviour.
[440.20 → 446.46] But, yeah, the first kind of narrative around this in the news is, whoa, this came out of nowhere.
[447.16 → 448.10] There's this new company.
[448.24 → 449.30] It's just a startup.
[449.54 → 450.86] They did this on the cheap.
[451.24 → 461.88] So they kind of published numbers around 5 million, 5.5, 6 million, somewhere in that range for the final training of this model.
[461.88 → 469.48] And compared to what it took to train OpenAI's 01, that's like a drop in the bucket.
[470.38 → 474.30] So, yeah, this first narrative, what are your thoughts on this, Chris?
[474.74 → 477.70] Well, I think that there's a lot more information we want.
[477.82 → 480.58] You know, they published that final number, as you mentioned.
[480.58 → 485.34] But I've seen a lot of posting about, you know, what did it take?
[485.42 → 489.78] What were all the unsuccessful runs that they had, the experimental runs, things like that?
[489.82 → 493.20] There's just so much that's not known about this.
[493.44 → 498.36] So they really cherry-picked what they chose to publish about it.
[498.74 → 501.04] But, I mean, have you used it, Chris?
[501.04 → 510.84] Oh, I actually, so surprisingly, you know, because of, you know, my job, I tend to avoid some of the Chinese technologies in a direct-use way.
[510.94 → 512.68] But I did load it onto my personal system.
[512.78 → 513.52] I have it on now.
[513.86 → 518.46] They were having some struggles on login for the last hour, at least, that I've been trying.
[518.64 → 520.10] But, yeah, I have it up.
[520.22 → 529.36] I know that I coyly sent you a text yesterday with a screenshot of me using it where I was just playing with it.
[529.36 → 531.00] And I had seen somebody else do this.
[531.22 → 534.52] And so I asked it, what happened in Tiananmen Square in 1989?
[535.64 → 538.78] And it replied, I am sorry, I cannot answer that question.
[539.16 → 547.92] I'm an AI assistant designed to provide helpful and harmless responses, which I thought was so, you know, that was about what I expected, actually, to be perfectly honest.
[547.92 → 556.50] But just a reminder of the geopolitics of AI, you know, which definitely plays big, is that this is a Chinese government-approved data set.
[556.50 → 568.50] And I think there's, to that point, so first off, DeepSeek is an amazing team of people that actually just didn't show up on the scene like a week ago.
[568.92 → 577.02] They've been doing actually really great open source and science work, you know, for a while now.
[577.58 → 579.52] So the DeepSeek team has been around.
[579.66 → 581.94] There's been previous DeepSeek models.
[581.94 → 598.96] They have released those models on Hugging Face, which, to be fair to our U.S. counterparts, OpenAI has not released their models openly on Hugging Face to where you can run them and do research with them and analyze them and generate outputs.
[598.96 → 602.36] So that's maybe a point to highlight.
[602.62 → 604.90] They have been open in that sense.
[605.02 → 611.84] But there's been some, I think, confusion around this concept of this very small team.
[612.12 → 622.04] Like, there are a couple of guys in their bedroom with a gaming card in their gaming PC, and they train this model that beat OpenAI.
[622.38 → 625.58] That's kind of the narrative that's being pumped around.
[625.58 → 630.98] In reality, they have access to tens of thousands of GPUs.
[631.52 → 635.20] I saw a post by Philip Schmidt, who's at Hugging Face.
[635.78 → 641.76] Now, I don't know all the details of where he gets certain information, so take this for what it's worth.
[641.88 → 647.58] But one of the things he said, similar to you, Chris, is the sort of $5 to $6 million mark.
[647.58 → 651.28] That's kind of the final base model.
[651.58 → 653.50] No reinforcement learning.
[653.80 → 655.40] Doesn't include smaller runs.
[655.50 → 658.36] Doesn't include data generation, which is a key piece of this.
[658.50 → 662.18] So we'll talk about that when we come to the model here in a second.
[662.32 → 668.62] But actually generating the prompts for this model is a significant part of it.
[668.62 → 672.86] And the kind of RL training, as I mentioned.
[673.22 → 675.08] So the costs are definitely greater.
[675.40 → 677.58] There were more resources that were brought into this.
[677.68 → 681.70] It's not a company that just sort of popped up in someone's bedroom.
[681.70 → 689.86] So some of that narrative is, you know, it's true in the sense that the company is small.
[690.06 → 692.62] They clearly were working under constraints.
[692.62 → 702.02] And they did a very impressive thing working under computational constraints in the environment that they're working on.
[702.20 → 706.94] And they released the model openly in Hugging Face.
[707.46 → 710.04] So kudos to them on that.
[710.04 → 715.10] Some of the other narrative points around that, I think, are a little bit fuzzy.
[715.96 → 720.02] So I'm curious just on kind of how your take on that is.
[720.52 → 723.78] So kudos for being open source on Hugging Face.
[724.22 → 733.82] And you and I, over the last year, year and a half, have been predicting open source kind of inevitably at some point,
[733.82 → 740.26] especially as things were plateauing a bit, that open source would inevitably, you know, have its impact in this way.
[740.26 → 745.62] And so I don't think it was a question of when and not if.
[746.18 → 752.06] And so having said that and seeing this particular group putting it on Hugging Face,
[752.18 → 759.26] why do you think that they declined to include all the training information on how they got there in terms of the cost?
[759.26 → 760.90] What do you think might be motivated?
[761.02 → 763.10] And I realize I'm asking a speculative question.
[763.36 → 763.86] It's interesting.
[764.16 → 774.82] I mean, I think one point to make there is it's not out of character for anyone that's posting these models in the sense that like Meta's Llama 3.1.
[774.82 → 787.84] I mean, there's a see kind of these model producers produce, quote, technical papers, but these technical papers don't share details to where in theory you could reproduce this.
[788.02 → 791.04] Right. And there are details about the data that they're not revealing.
[791.04 → 797.34] There are details about their process that they're not revealing, even when they release one of these models.
[797.34 → 802.72] And so it's not out of character for that to be kind of how things happen.
[802.72 → 807.18] And so really, part of me is like, well, why would they be motivated to do that?
[807.68 → 817.48] It would be sort of out of their philosophical commitment to open science, I think, would be the thing that would motivate them to do that, which certain parties do.
[817.48 → 829.24] So like Allen Institute for AI with their Elmo models, et cetera, have made it a very conscious effort to be truly open in terms of data process, model assets, et cetera.
[829.24 → 834.72] That is definitely an exception that that proves the rule.
[834.78 → 836.44] Is that the right is that the right phrase?
[836.70 → 838.14] Yeah. Yeah. I know what you're saying.
[838.36 → 840.24] Yeah. So it's something like that. You get what I'm saying.
[840.32 → 850.68] But there's an acknowledgement that in the larger field that the technical papers that come out are as much marketing papers as they are, you know, and kind of accomplishment papers as they are.
[850.68 → 858.30] I mean, there are certain elements that are interesting to know. Obviously, you can know the model architecture, you know, you're running it, it's open.
[858.46 → 860.48] So there are things you can learn from that.
[860.48 → 876.30] I do think that this represents a kind of shock to the system where, you know, you and I have been saying we're basically getting to parity with open models and closed frontier models for all intents and purposes.
[876.30 → 879.92] For most enterprise use cases, we're sort of we were already at parity.
[879.92 → 884.94] But in the public's eyes, we definitely weren't.
[885.46 → 889.56] And to some degree, we weren't in terms of certain types of models and that sort of thing.
[889.64 → 897.88] I think this is definitely a shock to the public's perception that there is model optionality out there.
[897.88 → 911.16] There's going to be a proliferation of these models from various different places, which then leads into natural discussions about where these models coming from, and can I trust them?
[911.36 → 915.24] And how does it behave differently than what I'm used to using?
[915.44 → 916.94] And can I run it securely?
[917.62 → 926.40] All of this sort of things pops up, and they popped up sort of immediately and captured a lot of a lot of attention around that.
[926.40 → 927.22] I agree.
[927.88 → 943.18] What's up, AI practitioners?
[943.48 → 944.92] Adam here from Changelog.
[944.96 → 947.02] Want to tell you about how much I love Notion.
[947.10 → 951.24] I know Daniel and Chris love Notion as well because we use Notion to organize everything.
[951.24 → 957.58] And behind the scenes here at Changelog.fm and CPU.fm, we work with a lot of cool teams externally.
[957.88 → 965.20] And we create dashboards and workflows and operating systems essentially to work well with others outside our domain.
[965.64 → 970.98] And the cool thing is, is Notion is so flexible that we could do anything with Notion.
[971.28 → 974.48] And the coolest thing I'm loving about Notion is their Notion AI.
[974.48 → 979.42] I can search across all my notes, all my docs, get context, get summaries.
[979.42 → 986.58] It's all AI powered, all inside my Notion, powered by all the content in my Notion.
[986.66 → 989.54] So I can work with external teams, internal teams.
[989.62 → 990.36] I can build workflows.
[990.82 → 996.82] And all this AI is really helping my team, my tools, my knowledge base be empowered to do our best work.
[996.82 → 1001.40] And unlike other tools out there, you've got to jump from one thing to the next to the next.
[1001.48 → 1003.26] And it's just not seamlessly integrated.
[1003.66 → 1007.38] Notion is seamlessly integrated, infinitely flexible, and it's beautiful.
[1007.68 → 1012.86] It's easy to use, mobile, desktop, web, shareable, web shareable.
[1013.10 → 1015.08] I mean, you name it, Notion can do it.
[1015.08 → 1021.50] And the fully integrated Notion AI helps us work faster, write better, think bigger, do tasks more efficiently.
[1022.10 → 1026.44] Things that would normally take us hours now takes us minutes, maybe even seconds in some cases.
[1026.92 → 1033.46] And yes, we are a small organization comparative to Fortune 500 companies, but they are used by over half of Fortune 500 companies.
[1033.92 → 1038.86] And teams that use Notion send fewer emails, they cancel more meetings, they save time searching for their work,
[1038.96 → 1043.26] and they reduce their spending on tools, which helps everyone stay on the same page.
[1043.26 → 1048.22] Try Notion today for free when you go to Notion.com slash practical AI.
[1048.82 → 1056.32] That's all lowercase letters, Notion.com slash practical AI to try the powerful, easy to use Notion AI today.
[1056.70 → 1060.02] And when you use our link, of course, you are supporting this show, and we love that.
[1060.34 → 1062.96] Notion.com slash practical AI.
[1073.26 → 1084.74] Well, Chris, I do want to get to some of the technical details that we know about, you know, what the model is and versions of the model.
[1084.74 → 1095.06] But maybe before that, it would be useful to address the elephant in the room, I guess, which is the security element of this,
[1095.26 → 1100.54] or the cybersecurity privacy issues related to this.
[1100.54 → 1107.96] So there's been the geopolitical elements around, oh, you know, is the US ahead?
[1108.26 → 1110.72] What does this say about dominance in the space?
[1111.02 → 1111.76] That's one thing.
[1111.76 → 1121.78] There's another thing, which is my company, which previously potentially had problems with pasting things into ChatGPT that they weren't supposed to,
[1121.78 → 1126.62] like, you know, whatever it is, customer details or IP or whatever.
[1127.70 → 1133.00] This kind of that shadow AI usage was already happening in companies, right?
[1133.30 → 1137.00] And people were concerned that their employees were pasting things into ChatGPT.
[1137.18 → 1141.10] Well, now there's this sort of new player in the space.
[1141.10 → 1147.06] People are pulling that up because it's the new amazing AI app.
[1147.56 → 1151.24] And it turns out that is run by a different company.
[1151.82 → 1158.32] And that data is going to a different place and is being housed on, you know, Chinese servers.
[1158.52 → 1161.12] So there's that element.
[1161.12 → 1163.06] So we need to kind of parse through that.
[1163.20 → 1171.94] But also, this has produced a separate confusion from my perspective around the, quote, security of the model.
[1172.46 → 1174.36] It is deep-seep secure.
[1174.56 → 1180.60] I think that's like a very, we have to clarify what we mean when we say that question.
[1180.66 → 1183.82] Because I don't know what you, how, I don't know the things you've seen, Chris.
[1183.86 → 1188.78] There's a lot of stuff out there that is not very helpful in this sense.
[1188.78 → 1190.76] Yeah, a lot of fear, uncertainty, and doubt.
[1191.16 → 1192.72] And some of it may be justified.
[1193.10 → 1194.60] Some of it may not be, probably.
[1195.00 → 1196.10] A lot of it may not be.
[1196.56 → 1200.50] For me, the scarier thing is not the model itself.
[1200.74 → 1210.58] It's the infrastructure around the model, where it's being housed, what external entities to the core data scientists at that company have access to it.
[1211.08 → 1214.42] And I think that's where a lot of the concern is going to be.
[1214.42 → 1225.26] It's, if you have a separate, if you've downloaded it from Hugging Face, and you're running it on your server, that's not to say that every facet of security is being accommodated, certainly.
[1225.50 → 1230.18] But at least you've taken some of the issues potentially out of the security equation.
[1230.18 → 1241.72] So, you know, I definitely, I have on my personal phone, I have the app, which is unusual for me, but knowing that we were going to do this and wanting to play with it a little bit.
[1242.16 → 1249.10] But I am very wary of my, of what I don't know about that at this point.
[1249.10 → 1252.56] Yeah. Yeah. So you drew out something really important, Chris.
[1252.74 → 1260.18] And I actually, I wrote a blog post about this that I'll link in the show notes of this, this episode.
[1260.38 → 1263.40] If you're interested, you can take a look and it might be a good resource.
[1263.40 → 1275.88] If, if you hear your engineering management or people in your company, you know, hyping the fears around DeepSeek, you know, and, and maybe you want to use that in, in a secure environment.
[1275.88 → 1286.08] Maybe that would be a good tool that you could point them to, but all that to say, I think the main thing that I wanted to highlight in that was this element that you just described.
[1286.08 → 1289.72] So there's really two ways to access this model.
[1290.00 → 1294.08] So there are two ways to utilize DeepSeek R1.
[1294.64 → 1303.92] One is via a product offered by the DeepSeek company, which is a software product that you access and they host.
[1303.92 → 1311.12] This would be parallel to a lot of other software products like OpenAI, Host, ChatGPT.
[1311.28 → 1316.40] That is their product, which has a model interface embedded in it.
[1316.84 → 1321.76] But it is a product similar to like you using Airbnb, right?
[1322.26 → 1325.92] You go to Airbnb, you put in your personal information into Airbnb.
[1325.92 → 1342.08] They have certain terms and service that, that they hopefully follow, but you, you have no view into what's going on under the hood of Airbnb or ChatGPT or this DeepSeek AI product.
[1342.08 → 1353.24] And so it's really not the model in that case that is not secure, quote unquote, in terms of you putting data into it.
[1353.44 → 1356.18] It is the product built around that model.
[1356.18 → 1366.84] And it is very clear from the terms and service that DeepSeek has posted that they will gather all of your, you know, well, I shouldn't do a blanket statement like that.
[1366.92 → 1374.40] They say exactly what they will, what they will get from you, but they're saving a lot of your personal data and information.
[1374.40 → 1377.04] They will use that for future model trainings.
[1377.04 → 1381.82] And that is housed on, you know, quote, servers in China.
[1382.68 → 1386.48] So that is the terms, that is the explicit terms and service.
[1386.66 → 1389.98] If you're okay with that, that's the usage of the product, right?
[1390.02 → 1390.84] Not the model.
[1391.20 → 1402.66] It's funny that you bring that up because like most people in most software products that I use, I don't necessarily go through all the terms of service as carefully as I really should.
[1403.40 → 1405.24] And, you know, because we're always...
[1405.24 → 1405.80] No one does.
[1405.80 → 1406.70] No one does.
[1407.04 → 1414.04] But I will confess that when I was downloading the DeepSeek app, and it brings that up in registration, I did.
[1414.18 → 1416.06] And I was horrified to read it.
[1416.46 → 1418.52] And I had already determined I was going to do that.
[1418.60 → 1422.28] I was using all personal stuff, nothing related to work, that kind of thing.
[1422.28 → 1435.24] But even so, not only did I kind of do a big swallow on bringing the app down, but it made me really think about the kinds of things that I would put into the interface very, very carefully given.
[1435.24 → 1438.18] And like you said, going around the product as opposed to the model.
[1438.18 → 1439.10] Yeah, yeah.
[1439.22 → 1442.10] So this is one access pattern, right?
[1442.24 → 1447.72] Access through the DeepSeek, either their mobile app or I think it's chat.deepseek.com.
[1447.72 → 1451.80] Their chat interface, similar, again, similar to ChatGPT.
[1451.80 → 1452.80] Absolutely.
[1452.80 → 1468.80] And really, you should have some of the same related concerns with a ChatGPT or an Anthropic as you would with DeepSeek in the sense that you really want to know how your data will be used and what are the privacy considerations around that.
[1468.80 → 1475.06] This adds a new element in that it's a sort of foreign entity dealing with that data, right?
[1475.16 → 1476.76] So there's a different element of that.
[1477.22 → 1478.20] But that's not the model.
[1478.32 → 1479.22] That's the product.
[1479.76 → 1495.42] The model, which they have released on, again, on Hugging Face is, and when we say model here, for those that haven't maybe been around the podcast for a while, when we talk about a model, there's sort of two elements of that.
[1495.42 → 1500.84] There's the code needed to actually run that model, so to process your inputs and generate outputs.
[1501.76 → 1510.12] And then there's a set of parameters, a set of data that's loaded into that code that parameterizes that code such that it can run.
[1510.54 → 1512.24] Both of those have been released.
[1512.40 → 1515.72] And in fact, actually, the code needed to run DeepSeek.
[1516.00 → 1518.26] Now, I'm going to make a clarification here.
[1518.26 → 1529.44] So the code needed to run some versions of DeepSeek is not even DeepSeek's code, at least if you're using the Hugging Face ecosystem.
[1529.82 → 1533.84] It's a software package called Transformers, which is open source.
[1533.98 → 1535.76] You can go look at every line on GitHub.
[1536.28 → 1538.60] It's maintained by thousands around the world.
[1538.72 → 1540.44] It's completely open and transparent.
[1540.44 → 1549.84] And so the code element isn't, you know, that's being looked at and being developed, and the model is implemented in there.
[1550.28 → 1559.22] The data element is available on Hugging Face and has potentially its own concerns as you download that into your environment, which we can talk about here in a second.
[1559.34 → 1560.56] But both of those are open.
[1560.56 → 1576.40] You can download them and run them even in like if I spin up a VM or some computer, I could download those assets, cut off that computer from the internet, both outbound and inbound, right?
[1576.54 → 1583.10] And run that model in complete isolation where no data goes to DeepSeek, no data goes to China.
[1583.36 → 1586.80] They're not sending and connecting to that computer, right?
[1586.80 → 1591.76] So just to make it Uber clear here, that is the model.
[1592.20 → 1593.84] When we say model, that's what we mean.
[1593.90 → 1594.96] We don't mean the product.
[1595.52 → 1601.36] And that can be run, again, with considerations in a secure environment.
[1601.90 → 1603.98] Now, I should say the caveat here.
[1604.10 → 1614.80] I do believe as the time of this recording, the Transformers' library hasn't been updated to support the full DeepSeek R1 architecture,
[1614.80 → 1618.10] which is actually very typical when a new model is released.
[1618.28 → 1621.96] Sometimes it's not always supported in the upstream transformers,
[1622.22 → 1629.04] which means that there is remote third-party code that you have to load to run the full model,
[1629.20 → 1631.58] which is not true for all the versions of the model.
[1632.10 → 1636.66] I expect that will change in a matter of, I don't know, maybe it's changing as I speak now.
[1636.76 → 1639.12] It'll happen fast, like days, weeks, whatever.
[1639.12 → 1645.10] That will be kind of merged into upstream, and then that concern will kind of go away.
[1645.78 → 1652.44] So just to kind of follow up on that thought, would it be fair, given what you just said,
[1652.52 → 1663.40] to say that if you were running it on the Transformers infrastructure, and you did have disconnected inbound and outbound networking from it,
[1663.40 → 1672.96] just to take all of those extraneous concerns out, would you have any reservations about running it in a scenario where security was important?
[1673.38 → 1679.16] Yeah, so that removes the kind of phone home, my data is going to China,
[1679.66 → 1683.94] vulnerabilities around remote code execution or something on my computer.
[1684.46 → 1688.50] Those sorts of concerns are, I would say, taken care of.
[1688.50 → 1693.14] Now, there are, I mentioned the data files that you would be loading, those model parameters.
[1693.40 → 1696.72] There are insecure ways that those could be loaded in.
[1696.96 → 1699.30] Frog and others have shown vulnerabilities in that.
[1699.82 → 1704.12] Those are mostly taken care of by using the right model formats, which Deeper is doing.
[1704.40 → 1705.50] It's called Safe Tensors.
[1705.70 → 1707.20] If you want to look into it, you can.
[1707.68 → 1710.20] So I wouldn't have any reservations about that.
[1710.60 → 1714.76] Now, that brings up a secondary question, though, which is another point of confusion.
[1714.94 → 1715.92] So I'm glad you brought it up.
[1715.92 → 1720.18] The secondary question is, okay, if I'm running this, it's not phoning home.
[1720.28 → 1723.98] My data is not going to Deeper or any foreign entity.
[1724.32 → 1733.74] If I'm running it in this secure way, are there other concerns that are unrelated to this sort of phone home privacy issue type of thing?
[1734.24 → 1739.14] And I think one of the things that you brought up before was potential biases.
[1740.06 → 1741.98] Yes, and the original training set.
[1742.16 → 1743.64] In the model, right?
[1743.64 → 1747.40] So you brought up this example of asking about Tiananmen Square.
[1747.98 → 1752.50] Actually, I think because we also asked a similar question.
[1753.06 → 1757.26] I don't know if this is actually fixed in the app as of the time of this recording.
[1757.80 → 1765.52] But at first, when you would ask that question in the Deeper product, the actual application, it would print out the full answer.
[1765.52 → 1768.88] It would actually answer what happened.
[1769.08 → 1774.26] And then it would all collapse and give you a canned, like, sorry, I can't answer that.
[1774.26 → 1791.66] So based on that, I would know, or I would assume that the actual model that you would download and run in that secure environment or, you know, on your laptop and one of these kind of local hosting things, that model is not biased.
[1791.66 → 1798.18] In terms of that response, that model specifically is not, you could get it to answer about Tiananmen Square.
[1798.42 → 1798.66] Sure.
[1798.66 → 1809.56] It's a product decision similar to like when Gemini, you know, was trying to create diversity in their image output and generated some fascinating looking things.
[1810.12 → 1816.06] Or what ChatGPT or anyone does, when you send in a prompt, they inject stuff into that prompt.
[1816.22 → 1817.54] They do post-processing.
[1817.68 → 1818.68] It's a product, right?
[1818.70 → 1820.72] You don't have visibility into any of that.
[1821.46 → 1826.64] And so they're doing obvious product things there to introduce artificial biases.
[1826.64 → 1847.52] Now, I do think that it is possible that in the sort of alignment, fine-tuning process, DeepSeek had their own vision of how they wanted to align that model, which may not be malicious in any sort of way or kind of biased in weird political ways.
[1847.60 → 1850.32] It might just be their choice of how they wanted to bias that model.
[1850.52 → 1853.68] In other ways, maybe it is motivated by certain things.
[1853.74 → 1854.36] I don't know.
[1854.36 → 1858.38] But that model will have its own sort of biased behaviour.
[1858.98 → 1866.76] The other thing that I think has been shown in a number of places with Secure did a study of this.
[1867.34 → 1881.22] And it is a model that is also way more sensitive to prompt injection attacks than kind of the many other state-of-the-art models, which produces another type of vulnerability at the application layer.
[1881.22 → 1885.14] So you've taken care of, like, the model hosting security issue.
[1885.34 → 1894.32] But all that to say, that doesn't mean at the actual use of the model or integration layer, you shouldn't still be asking relevant questions.
[1894.32 → 1898.10] Which, again, I highlight some of those things in the blog post if people are interested.
[1898.10 → 1906.52] Well, friends, AI is transforming how we do business.
[1906.66 → 1911.80] But we need AI solutions that are not only ambitious but practical and adaptable, too.
[1912.02 → 1915.40] That's where Demo's AI and data products platform comes into play.
[1915.56 → 1918.10] It's built for the challenges of today's AI landscape.
[1918.10 → 1924.50] With Demo, you and your team can channel AI and data into innovative uses that deliver measurable impact.
[1924.50 → 1948.34] While many companies focus on narrow applications or single-model solutions, Demo's all-in-one platform is more robust with trustworthy AI results without having to overhaul your entire data infrastructure, secure AI agents that connect, prepare, and automate your workflows, helping you and your team to gain insights, receive alerts, and act with ease through guided apps tailored to your role.
[1948.44 → 1951.24] And the flexibility to choose which AI models you want to use.
[1951.24 → 1953.28] So, Demo goes beyond productivity.
[1953.84 → 1959.16] It's designed to transform your processes, helping you make smarter and faster decisions that drive real growth.
[1959.32 → 1966.00] And it's all powered by Demo's trust, flexibility, and years of expertise in data and AI innovation.
[1966.46 → 1969.36] And, of course, the best companies rely on Demo to make smarter decisions.
[1969.92 → 1971.98] See how Demo can unlock your data's full potential.
[1972.52 → 1976.08] Learn more at AI.domo.com.
[1976.08 → 1979.58] That's AI.domo.com.
[1981.24 → 1995.72] So, Chris, there's also the element around this that we always like to do when we get into our deeper discussions about any particular model, which is,
[1995.72 → 1999.70] what are the unique technical or architectural elements of this?
[1999.92 → 2001.76] What types of versions did they release?
[2001.76 → 2011.60] This actually might be very confusing for people when they see like DeepSeek R1 distilled Quinn 32B, right?
[2011.82 → 2014.92] There are a lot of words there that might not make sense.
[2015.74 → 2030.84] Jay Palomar, who we love on the podcast and has been on the podcast, he runs this, has posted for years a lot of great blog posts about kind of illustrated transformers and other things.
[2030.84 → 2043.74] As a learning resource that you might want to take away from this particular episode, he posted an illustrated DeepSeek R1 article, which goes through some of the details.
[2044.66 → 2059.14] What's interesting here, Chris, I don't know if you got through any of that, but the overall picture of how they did this fine-tuning is fairly similar to, I think, how many people have been doing fine-tuning for some time.
[2059.14 → 2069.92] And I guess that one of the things I wanted to bring up on this is, I believe, correct me if I'm wrong, it was based on one of the LLAMA models, right?
[2070.22 → 2077.10] Well, the DeepSeek architecture has been around for some time and is a specific architecture.
[2077.32 → 2080.40] It's similar to the LLAMA architecture.
[2080.62 → 2085.42] Like it is also involving layers upon layers of transformers.
[2085.42 → 2094.74] In terms of the exact architecture of this DeepSeek R1, it does involve mixture of experts layers in the model.
[2094.94 → 2100.62] So there's layers and layers of transformer blocks in the architecture.
[2100.62 → 2109.06] And then this mixture of experts blocks, which you might see people refer to like activated layers or parameters.
[2109.06 → 2127.04] This mixture of expert layers don't always, you don't process the input through all elements of that layer of the model each time you run the model, which creates some efficiencies both for inference and often for training purposes as well.
[2127.04 → 2130.98] But yes, it's a similar setup.
[2131.46 → 2136.90] Some slight differences, which also kind of those slight differences are the reason why we mentioned earlier.
[2137.12 → 2148.26] Likely you kind of have, at least currently, as we're recording this, you might have to import some third party code to support the model in the upstream transformers, which is likely to change quickly.
[2148.26 → 2155.78] How does that affect the fine-tuning, though, in terms of, you know, how DeepSeek approached it versus maybe how LLAMA has been approached and stuff?
[2155.86 → 2156.56] Are there differences?
[2156.68 → 2158.20] Are you seeing a lot of similarity there?
[2158.56 → 2169.52] I know Sam Altman made a comment, and I'm not quoting him directly, but it was something to the effect of once, you know, once somebody else has already done something that you're basing on, it's a lot easier to do that.
[2169.62 → 2173.02] And that was his kind of minimization of what DeepSeek had done.
[2173.02 → 2178.38] And I'm kind of curious, you know, how does that affect this in terms of the fine-tuning?
[2178.54 → 2190.90] I mean, the overall, like I say, the overall process, and when I say overall process, this is often kind of a pre-training step of very raw data that is completely unsupervised.
[2190.90 → 2198.42] A fine-tuning step, which is supervised and maybe an additional fine-tuning step, which is like a preference tuning.
[2198.70 → 2204.24] That sort of overall picture of how the training is done seems to also be true here.
[2204.36 → 2206.70] This is like the overall picture of how they did that.
[2206.70 → 2225.42] Now, there are some unique elements of this in that they created this DeepSeek R1-0 model, which is kind of, and they use this interim reasoning model to actually help generate some of the data for that supervised fine-tuning step.
[2225.42 → 2240.58] So this is where, going back to the original discussion in our conversation, that 5 million number corresponds to maybe that final, or one of the final training steps, but not necessarily the data generation.
[2241.00 → 2246.96] So they used interim models that they, you know, their intention wasn't to release.
[2246.96 → 2269.14] It doesn't perform great in terms of a general purpose model, but it might perform well to generate long chain of thought examples, like these reasoning examples, to add into the training or the training data that's supervised fine-tuning, which allows you to augment your fine-tuning data, use less human resources to create that fine-tuning.
[2269.14 → 2284.30] So I forget the exact figures, but meta did spend a ton of money in terms of the data curation with human data labels to create those data sets for the LAMA models and probably still are.
[2284.82 → 2291.52] In this case, at least some of that data was this synthetic data that was generated by this interim model.
[2291.52 → 2302.52] So that's kind of one interesting step of the process that maybe, you know, that maybe is relevant to some of the budget and efficiency considerations.
[2303.58 → 2314.18] Sure. And maybe that's, you know, part of the motivation of leaving that out altogether is, you know, that wasn't a direct cost necessarily to them, or at least not in the way that it had been when it was originally manufactured.
[2314.18 → 2328.02] Yeah, yeah. So there's this Deeper R1 model, which again is, the architecture is not fundamentally different from architectures of what we've seen in the past.
[2328.02 → 2340.86] There were some creative things done in the training process, both that significant portion, assuming it was a significant portion of data that which was synthetic or generated data.
[2341.16 → 2355.08] They also used some kind of automated processes and model based processes to filter and curate that generated data to actually filter out good examples from kind of all the candidate examples.
[2355.08 → 2359.04] So there were some very creative things in that data generation piece.
[2359.14 → 2367.58] But the other stages of this were not fundamentally stages of training that we haven't been familiar with other model releases.
[2368.00 → 2374.04] There are a number of model versions that have been released from Deeper.
[2374.14 → 2381.12] So there's the Deeper R1, the sort of flagship, which is like 700 billion parameters or something.
[2381.12 → 2389.62] It's very large. You're going to need, at least at full precision, you're going to need many, many GPUs to run this.
[2389.78 → 2400.12] I think Philip from Hugging Face said, like his, what he said was like 16x 80 gigabyte GPUs, like 16x H100s.
[2400.86 → 2401.02] Yeah.
[2401.02 → 2415.22] To give you context, I think an H100 will, if you have it up all the time at on-demand pricing in a cloud is going to run you something like 60 to 80 grand a month, something like that.
[2415.52 → 2423.84] So you need 16 of those to run the model, the full model and full precision with at least NVIDIA GPUs.
[2423.84 → 2427.56] Then they've released other variants of this model.
[2428.06 → 2436.60] And that full model is that mixture of experts model, which has the element of the kind of external or third party code added into it.
[2436.78 → 2440.70] They've also released distilled versions of that model.
[2440.80 → 2446.12] So we can get into that here in a second, but just wanted to make clear kind of what the main model looked like.
[2446.12 → 2455.94] And these distilled versions of the model, if you go to Hugging Face, you can actually look at the collection from DeepSeek for DeepSeek R1.
[2456.64 → 2468.28] And what you'll see is a bunch of different DeepSeek models, which again is often a point of confusion with people.
[2468.38 → 2470.28] Like what do all these things mean?
[2470.28 → 2480.42] So we've got DeepSeek R1, we have Distill Llama 70B, Distill Quinn 32B, Distill Llama 8B, etc.
[2481.20 → 2485.30] These are really significant for people to maybe understand.
[2485.72 → 2489.26] So these models are what's called dense models.
[2489.38 → 2492.18] So they don't have the mixture of experts element.
[2492.62 → 2497.08] They run all of their parameters all the time, and they're distilled models.
[2497.08 → 2504.70] So what DeepSeek did is they took their flagship, DeepSeek R1, they created their flagship model.
[2505.16 → 2516.92] And then they use the process of knowledge distillation to create smaller versions of that model that leverage the kind of power of the larger model in the following way.
[2517.30 → 2523.32] So we've talked about this on the show before, especially we had an episode with Noose Research.
[2523.48 → 2524.78] They talked about this a lot.
[2524.78 → 2527.30] If you're curious, go and check that out.
[2527.72 → 2531.96] But you essentially use the larger model to generate a bunch of example outputs.
[2532.44 → 2549.94] And then you use those inputs and outputs that were generated by the larger model to then train a smaller model with very, very high quality data that boosts the performance of the smaller model beyond what you could get from a smaller model just from training it by scratch.
[2549.94 → 2554.70] So when it says DeepSeek R1 distill Llama 70b.
[2554.70 → 2574.98] It's a distilled version of Llama 70b that use DeepSeek R1 to generate that synthetic data for the fine-tuning process, which is great because they have versions of this model from between 1.5 billion up to 70 billion.
[2574.98 → 2580.76] And it's great because actually, you know, especially the smaller ones, you could run it on your laptop.
[2581.42 → 2587.84] Certainly the kind of sweet spot ones around that 8 billion to, you know, 32 billion.
[2587.84 → 2591.64] Those would take a card or a couple cards you could run them on.
[2592.16 → 2595.26] And so this gives more accessibility to these models.
[2595.42 → 2607.42] And of course, people have already proliferated from there with various other optimizations like GGU and other ones that can run on, you know, your MacBook processors and that sort of thing.
[2607.42 → 2614.22] So just to clarify the kind of ecosystem around the models there, those are a couple of things to keep in mind.
[2614.50 → 2616.16] Yeah, that's that's useful to know.
[2616.36 → 2630.26] It's so a couple of big questions, you know, as we are starting to wind up here, they kind of to address to pull out of the technical a little bit for a moment and kind of address the ecosystem at large, the AI community.
[2630.26 → 2636.60] What do you what would you predict that DeepSeek now being here and how things wash out?
[2636.68 → 2638.82] Obviously, there 's's, you know, the market reacted.
[2639.20 → 2645.12] I think they took half a trillion dollars away from NVIDIA plus another half a trillion.
[2645.36 → 2647.04] Don't they have a lot of trillions of dollars?
[2647.04 → 2647.62] They have a few.
[2647.80 → 2648.46] They have a few.
[2649.10 → 2654.10] And so but that will probably, you know, stabilize outgoing here.
[2654.54 → 2659.22] The what do you think that we're looking at over the months ahead?
[2659.22 → 2663.38] You know, beyond the day of, you know, market reacting today kind of thing.
[2663.46 → 2668.48] And we're talking about it as you look at six months out, nine months out, that kind of thing.
[2669.02 → 2674.88] What do you think the real impact of DeepSeek is going to be on the larger AI global community?
[2675.52 → 2681.68] Well, we've we've been saying it for a while, but I think the wider business community has not realized this.
[2681.68 → 2695.02] And one of the kind of fallouts from this or the things that will shift, I think, are really people taking seriously that in the future, part of what your business needs to consider is model optionality.
[2695.02 → 2695.54] Right.
[2695.54 → 2699.62] Sort of these GPT models kind of were king for a long time.
[2699.96 → 2708.42] But now, like, you know, apparently if you got five million dollars sitting around, you could create a best in class model.
[2709.08 → 2710.90] And, you know, what does that mean?
[2710.96 → 2713.90] It means all of these are going to proliferate very quickly.
[2713.90 → 2718.48] This is not the last of these types of models we will see.
[2718.60 → 2720.06] They will proliferate very quickly.
[2720.88 → 2730.12] And you're having kind of model lock in, quote unquote, like you built all of your AI functionality around this particular model, whether that be open or closed.
[2730.82 → 2735.78] That's not going to work out great for you in the long run just because of the models changing.
[2735.78 → 2744.50] And so building in this ability to swap models, to have control and configurability, I think that's one of the kind of trends there.
[2744.74 → 2755.98] The other one I would say is now that you're considering bringing these models into your own infrastructure, like there's parity with open AI in many respects.
[2756.22 → 2760.34] It brings up all of these questions that we were immediately prompted with.
[2760.46 → 2760.54] Right.
[2760.60 → 2765.50] Like, well, if you bring that into your environment, what are the security concerns related to that?
[2765.50 → 2767.74] How can you run it robustly and reliably?
[2768.44 → 2771.58] What should you be monitoring in production?
[2771.84 → 2771.96] Right.
[2772.02 → 2788.44] So it brings up all of these additional questions, which I think overall will be perfect for people to consider because they're probably things they should have been considering for the past year as, you know, so many things were built on kind of one model family.
[2789.10 → 2790.46] So, yeah, those are a couple of thoughts.
[2790.52 → 2791.66] I don't know if you have additional ones.
[2791.66 → 2802.22] I mean, I've been speculating on whether, you know, as valuations have been going up and up and up for all these different AI startups all over, you know, across the entire globe.
[2802.38 → 2805.00] And the budgets have just grown astronomically.
[2805.00 → 2812.08] Is this the moment where we're at this point investors looking at it going, why do you need 100 million?
[2812.72 → 2815.28] Why don't we give you 5 million and see what you can do with it?
[2815.64 → 2816.58] Look what they did with it.
[2816.64 → 2818.26] Look what they did with it and stuff.
[2818.26 → 2826.52] And so, you know, whether the cost of operations in AI startups is now going to affect.
[2826.76 → 2835.12] And if that's the case, and with potentially not everybody being able to be quite so productive with their 5 million, you know, what does that mean?
[2835.18 → 2840.58] Are we going to go through a little bit of a cleanup round in the AI startup world or whatever?
[2840.76 → 2842.74] Any thoughts on that as we finish up?
[2843.14 → 2843.82] Yeah, it's interesting.
[2843.82 → 2850.06] I mean, it definitely has an impact if you're kind of a model building type of startup, for sure.
[2850.46 → 2863.78] And we've seen other examples of this even last week, you know, hearing from Venmo and what they're doing with video generation models with a very small team and what they're able to accomplish.
[2864.16 → 2867.44] I think it definitely has implications on that side.
[2867.44 → 2881.32] I think it also has implications for this sort of hopefully I think people will start thinking about less the kind of model building ventures, which will be interesting.
[2881.54 → 2895.06] But also this is going to make model building and fine-tuning even more accessible to kind of the enterprise, which will kind of fuel both tooling and infrastructure type of investments as well.
[2895.06 → 2904.82] Now, those I don't think will have the kind of inflated like, oh, I need a hundred million dollars to train a model sort of scenario.
[2905.14 → 2907.10] But yeah, we'll see how that shakes out.
[2907.40 → 2922.98] I think in I think in enterprise world out there, maybe as a final thought on this, I think that you're now going to see existing budgets, which are which often for large companies, you know, are in the hundreds of millions of dollars, you know, where they're not AI specialty companies.
[2922.98 → 2925.68] But they but it matters enough to have a big budget.
[2925.94 → 2932.00] The expectation that I've always used other models, and we've built lots of infrastructure around that.
[2932.16 → 2946.36] Maybe there's pressure now to actually go and work on specifically models for your business that you're creating because you have, you know, five million times X available to do that in the new way of thinking.
[2946.36 → 2950.78] So it may certainly change what the expectations are in enterprise world.
[2950.78 → 2958.62] What I think will be stressed in that case is the data curation and human involvement in that process.
[2958.92 → 2959.96] Yes, that's not.
[2960.24 → 2963.96] I mean, there is clearly a big investment on that side here.
[2964.34 → 2972.32] So even if you spend five million on that, you know, final training, there's definitely a process that goes into that.
[2972.56 → 2972.80] I agree.
[2973.22 → 2973.42] Yeah.
[2973.46 → 2974.42] Good conversation today.
[2974.62 → 2975.18] Yeah, definitely.
[2975.18 → 2975.58] Definitely, Chris.
[2976.12 → 2986.64] Definitely check out some links that we'll put in the show notes to various articles about this, both on the technical and the kind of more hyped geopolitical stuff.
[2986.96 → 2988.06] So check it out.
[2988.26 → 2989.52] Thanks for joining again.
[2989.64 → 2990.44] Great to talk, Chris.
[2990.76 → 2991.54] Yep, absolutely.
[2991.74 → 2992.34] See you next week.
[2992.34 → 3000.54] All right.
[3000.54 → 3002.74] That is our show for this week.
[3003.16 → 3009.04] If you haven't checked out our Changelog newsletter, head to changelog.com slash news.
[3009.40 → 3011.52] There you'll find 29 reasons.
[3011.74 → 3015.08] Yes, 29 reasons why you should subscribe.
[3015.48 → 3016.94] I'll tell you reason number 17.
[3017.52 → 3020.28] You might actually start looking forward to Mondays.
[3020.44 → 3023.16] Sounds like somebody's got a case of the Mondays.
[3023.56 → 3028.10] 28 more reasons are waiting for you at changelog.com slash news.
[3028.10 → 3034.00] Thanks again to our partners at Fly.io to Break master Cylinder for the Beats and to you for listening.
[3034.38 → 3037.08] That is all for now, but we'll talk to you again next time.
