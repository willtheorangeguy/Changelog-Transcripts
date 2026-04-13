[0.00 → 8.66] Welcome to Practical AI.
[9.16 → 19.54] If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.24 → 24.92] Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 → 32.36] Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.78 → 35.44] So you can launch your app near your users.
[35.84 → 37.84] Learn more at Fly.io.
[42.72 → 50.12] Hey friends, do you remember the day that ChatGPT launched?
[50.12 → 53.24] I do. Well, not the exact day, but the time frame.
[53.24 → 57.16] It felt like the LLM was this magical tool out of the box.
[57.66 → 61.12] However, the more you use it, the more you realize that's just not the case.
[61.58 → 64.38] And as AI developers yourself, you know.
[64.78 → 68.84] The technology is brilliant, but it's prone to issues like hallucination.
[69.14 → 70.88] And that's not good, but there's still hope.
[71.26 → 76.78] Feed the LLM reliable current data, ground it in the right data and context.
[77.02 → 81.12] Then it can meet the right connections and give the right answers.
[81.12 → 88.28] The team at Neo4j has been exploring how to get results by pairing LLMs with knowledge graphs and vector search.
[88.78 → 95.12] And to hear all about this, check out the podcast episode about LLMs and knowledge graphs at graphstuff.fm.
[95.12 → 99.90] They share their tips on retrieval methods, prompt engineering, and more.
[100.20 → 100.88] Do not miss it.
[101.12 → 102.90] You'll also find a link in the show notes.
[103.40 → 105.92] Again, graphstuff.fm.
[106.12 → 111.94] That's G-R-A-P-H stuff, S-T-U-F-F dot F-M.
[111.94 → 131.30] Welcome to another fully connected episode of the Practical AI podcast.
[131.72 → 140.24] In these fully connected episodes, Chris and I keep you connected to a bunch of different things that are happening in the AI community.
[140.24 → 146.86] And try to plug you in with some learning resources to help you level up your machine learning game.
[147.10 → 148.28] I'm Daniel Whiten ack.
[148.42 → 153.14] I'm founder and CEO at Prediction Guard, where we're safeguarding private AI models.
[153.36 → 160.20] I'm joined as always by my co-host, Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[160.52 → 161.18] How are you doing, Chris?
[161.42 → 162.36] Doing great, Daniel.
[162.56 → 164.20] So many things happening in the news.
[164.20 → 169.58] And just was looking forward to a chance for us to finally, we've hit specific topics a lot lately.
[169.58 → 173.88] And I'm hoping we have a chance to jump in and just talk about all the stuff.
[174.56 → 179.36] How's your mind at these days in relation to AI?
[179.76 → 183.16] We haven't done a sort of general check-in on.
[183.74 → 186.66] Both of us are probably, I think, know each other well enough.
[186.66 → 193.18] Probably we're both fairly hopeful about things, looking forward and seeing many good things.
[193.44 → 199.50] But yeah, generally, how has this year looked for you in relation to how you thought it might look?
[199.62 → 207.82] And or in your own work with this technology, how's your view of how the technology is shaping up changed or stayed the same?
[207.82 → 212.48] In the large, I think some of the things that we have kind of predicted are happening.
[212.82 → 216.08] A lot of the developments are somewhat predictable.
[216.34 → 221.24] Like if you do something with imagery, you'll probably get there with video and things like that.
[221.28 → 224.16] And we talked about, we made some predictions last year about that.
[224.44 → 230.32] And I think those types of things are playing out more or less in a broad scale, kind of how we would have expected.
[230.58 → 232.10] Would you agree with that in general?
[232.42 → 232.86] Yeah, yeah.
[232.88 → 236.28] I would say definitely multimodality wise.
[236.28 → 238.20] Yes, we talked about that a lot.
[238.20 → 249.20] What about, I guess, both of us either are at or have interacted with friends of ours or colleagues at a variety of enterprise organizations.
[249.58 → 260.60] What do you think is the reality on the ground in terms of adoption of AI versus what's all in the news and the hype and that sort of thing?
[260.60 → 273.48] In terms of the practicalities and actual adoption rate of generative AI versus kind of the things that we've always had with us, the machine learning, the data science types of projects.
[273.48 → 275.40] Yeah, I think it's interesting.
[275.40 → 281.06] There's a lot of reality checking happening this year, especially in the last few months.
[282.02 → 287.88] Everyone's been hit with so much Gen AI marketing and just all the hype and everything with it.
[288.10 → 291.38] But we're also expected to get things done at work.
[291.38 → 299.48] And so trying to finally get past the hype and get stuff, which requires a lot of hard decisions to make.
[299.72 → 308.40] And so, you know, companies kind of going, well, do I, you know, I'm looking at the cost of one of the big providers, you know, with OpenAI being kind of the leader in those.
[308.48 → 310.50] And do I want to pay for that for everything?
[310.60 → 312.30] And thus, do I also want to send my data out?
[312.30 → 317.56] How can we do things with smaller models or other large language models that are open source?
[317.74 → 334.86] And across multiple companies, as I'm watching people make these choices, and we're having conversations about it offline and stuff, there's an agony associated with trying to navigate correctly and not end up in a bad position for your organization and stuff like that.
[334.86 → 335.30] Yeah.
[335.46 → 343.28] And so I'm seeing a lot of, well, we're going to use some open source for this, and we're going to use some API calls to commercial stuff for that.
[343.56 → 346.84] And we're going to use some smaller models over here.
[347.24 → 349.34] And how are we going to put them all together?
[349.60 → 353.32] And we've talked about these issues across a bunch of different conversations.
[353.32 → 355.98] Even the last guest we had, we had this conversation.
[356.38 → 360.90] But I think people are really challenged with making it all work.
[361.12 → 364.82] As I talk to people at different companies, I don't necessarily see everyone doing it.
[365.28 → 365.74] The same.
[365.94 → 372.64] There's enough variability to where we haven't arrived at the world of best practices yet, in my view.
[372.64 → 373.28] Yeah.
[373.78 → 383.74] One of the things that you highlighted is the sort of multimodel future people kind of spreading out their workloads across multiple model providers and open models.
[383.94 → 388.38] I think that's something that seems to be only increasing and will continue.
[388.38 → 393.68] You know, with all of this emphasis on large language models, generative AI.
[393.68 → 406.92] Have you got a sense from data scientists that you're interacting with or others that, you know, the actual day-to-day of data science teams is shifting?
[406.92 → 416.20] Or they're still just training their support vector machines and whatever time series forecasting and whatever those things might be?
[416.20 → 425.50] I think the thing, you know, to that point, there's shifting, but there's also the field has exploded out in the number of positions to support.
[425.76 → 437.94] And, you know, way back when I was young, which was, you know, back when the dinosaurs were roaming the earth, you had like software developers and they kind of had to do everything, you know, which is very reminiscent of how AI has been in previous years.
[437.94 → 444.88] And in the last couple of years, we've seen, you know, an explosion of, we first saw machine learning engineers, you know, beyond data science.
[444.88 → 452.82] And then you kept adding each title and position and there are, now there's UX people in AI concerns.
[452.82 → 463.30] And it feels very much like software exploded from the 1980s when I was a kid into young adulthood for me in the 90s and 2000s.
[463.36 → 467.30] And now, you know, we're seeing that same, it's very similar to me.
[467.30 → 470.58] I look at it and I go, I bit, you know, déjà vu for me.
[471.24 → 475.12] So it's a maturing of the industry and people are starting to figure it out.
[475.46 → 482.02] I think there's a recognition finally outside the marketing and hype machine, which goes hard and constant always.
[482.22 → 489.28] I think for the worker bees like me, there's a realization that it's part of software.
[489.46 → 491.96] And we've talked about this for a long time that that needed to happen.
[491.96 → 498.14] And so a little bit less hype and more about what can the models do and how do I combine them and what sizes.
[498.82 → 503.38] And it's putting the jigsaw puzzle together of what makes value for a particular organization.
[503.78 → 510.90] And that's been interesting for me to be part of that in my own organization and help us navigate through the morass.
[510.90 → 513.46] And every other organization I'm talking to is doing the same.
[513.98 → 514.40] So, yeah.
[514.88 → 515.06] Yeah.
[515.16 → 519.10] I was just sort of curious about boots on the ground.
[519.72 → 522.60] What's changing day to day for data scientists?
[522.86 → 529.42] It seems like one of the things that you're indicating is it's more that roles and teams are expanding.
[529.80 → 530.22] They are.
[530.22 → 530.74] Yeah.
[530.74 → 530.78] Yeah.
[530.78 → 543.78] Versus the data science teams that have existed sort of cease to exist in their form, you know, creating scikit-learn models and start moving over to Gen AI, which is probably not the case.
[543.86 → 551.06] I was just looking at Google trends of terms, which is always a fun thing to look at.
[551.06 → 561.28] And I was looking at Gen AI versus scikit-learn and there's sort of a, you know, scikit-learn still quite impressive search.
[561.42 → 568.32] But you can see this surge of interest kind of in the data science hype period, at least as far as I can tell.
[568.50 → 573.48] But then there's also been a surge since kind of 2022 and on.
[573.60 → 575.42] And, you know, that's gone down a little bit.
[575.42 → 581.96] So I don't know how much you can draw from that, but the data science team still lives as far as I can tell.
[582.36 → 595.42] I don't think it's going to die because people are also, to your point, they're also realizing the limitations and constraints of Gen AI and what types of things it doesn't do well.
[595.42 → 603.16] And so people are, I think, a bit smarter about it in 2024 versus 2023 and definitely 2022.
[603.58 → 616.60] It seems like the wisdom is finally kind of spreading out and people will kind of go, instead of just saying Gen AI is going to solve everything, they're recognizing it for what it is and the capabilities it has.
[616.60 → 630.64] And they're starting to say, this is a good use case for it, but we need to pair it maybe with a reinforcement learning model, you know, and they're starting to remember, oh, yeah, there's all these other capabilities, which we were quite enamoured with until Gen AI came along.
[630.74 → 633.66] And they're still perfect technologies to use.
[633.66 → 645.94] And so trying to start recognizing what and what shouldn't be an AI at all and combining those together in unique value propositions for their organizations is the thing I'm seeing.
[645.94 → 663.62] One other point that I've noticed also for the first time this year is that companies like the software side and the AI side are finally really coming together operationally instead of being very stuck apart, which is one of the problems we've talked about on the show many times.
[663.62 → 670.24] And I'm seeing like agile methodologies play out that had been on the software side for years in these organizations.
[670.48 → 682.22] And they're now including the AI and data science teams and how they're like if they're, you know, I'm just making up one of the like if they're using safe or scrum or whatever they're using, they're starting to account for that.
[682.42 → 684.72] And it feels more real life to me.
[684.72 → 693.48] It feels like, oh, we're finally getting to a point of maturity and recognizing that all the pieces need to come to play, or we need to be efficient in how we do that.
[693.62 → 698.00] So that's been my kind of enterprise observation of the last few months.
[698.66 → 698.78] Yeah.
[699.02 → 716.40] And I don't know, again, Google search trends only give you so much, but it seems like the main trend with data science as a function, at least according to searching, just sort of keeps going up pretty steadily, even though there's a switching of technologies.
[716.40 → 718.20] It would be nice, though.
[718.28 → 724.98] I know that we talked quite a while back in a number of episodes about being a full stack data scientist.
[725.28 → 730.72] And I know recently we had some of that discussion around full stack AI agent development.
[730.96 → 743.90] But that sort of idea that there would be more integration of that software side into data science teams and vice versa is something that maybe this is a push that's kind of materializing some of that.
[743.90 → 745.18] But, you know, it's interesting.
[745.36 → 749.38] The term full stack is so loaded in terms of how people perceive it.
[749.58 → 752.64] And it's a bigger thing if you're in a very small organization.
[752.64 → 764.02] And what it means there is, thank goodness I've got somebody who can handle all these things that we have gaps on because we don't have enough resource to go buy somebody in all these different areas.
[764.02 → 768.58] And so it's more meaningful in a smaller midsize organization based on the nature of the organization.
[768.96 → 783.30] You're going to see it a lot more job specific and role specific in the enterprise, which in my view is a good thing because you don't want to just put full stack this full stack into everyone because in a large enough organization that doesn't help with your efficiencies and stuff.
[783.58 → 786.00] But team wise, there could be more integration.
[786.38 → 786.86] There could be.
[786.86 → 788.52] And I think integration is really important.
[788.52 → 794.84] And so I think this is the first year when I have a little sense of actually seeing that out in the workplace.
[816.86 → 846.84] I think this is a good thing.
[846.84 → 854.76] Plum's declarative node based editor enables you to build quickly while empowering non-technical roles to iterate on what you've done without breaking it.
[855.14 → 865.28] You can build advanced AI features, get structured output every time, transform data and leverage validated JSON schema to create reliable, high quality structured output.
[865.80 → 867.40] So Plum is built for builders.
[867.84 → 873.22] Early stage product teams are using Plum to go from idea to validation in record time.
[873.22 → 876.22] To get started, go to useplum.com.
[876.96 → 880.82] That's Plum with a B as in plumber to request access today.
[881.18 → 885.30] That's U-S-E-P-L-U-M-B.com.
[885.48 → 887.42] Again, useplum.com.
[903.22 → 910.50] Well, Chris, we have got to Apple intelligence.
[911.04 → 911.34] Yes.
[911.34 → 917.34] This last cycle that we went through, you know, everybody's got their AI play now.
[917.42 → 922.24] And I guess, of course, Apple had been in AI in one way or another.
[922.24 → 924.24] So it's not like they were totally absent.
[925.04 → 928.26] But we got the announcement about Apple intelligence.
[928.80 → 930.24] So what do you think?
[930.30 → 931.20] First impressions?
[931.70 → 932.18] Excited?
[933.08 → 933.56] Confused?
[933.80 → 934.42] A mix?
[934.70 → 935.38] What's your impression?
[935.68 → 940.64] I'm always skeptical about everything when it comes out because of the hype machine, as you know.
[940.88 → 944.34] But as an Apple user, I'm looking forward to it.
[944.38 → 945.52] I want to see what they do.
[945.52 → 953.64] I buy a certain degree into the Apple ecosystem, but I also am not 100% invested in every way, the way some folks are.
[953.80 → 956.90] I use Google as well and various things.
[957.14 → 958.74] So they were very slow.
[958.90 → 973.16] Apple's received a lot of criticism the last couple of years because, you know, once upon a time, having been perceived as the Steve Jonahesque, you know, leader of we're the ones that bring you completely new ideas that are going to change your world,
[973.16 → 979.10] like the iPhone when it was released originally, they have definitely not been fulfilling that role.
[979.50 → 980.10] They've been slow.
[980.42 → 991.10] Having said that, having thrown the criticism out first, they have certainly, I would say the announcement seems differentiated in that Apple is kind of putting it out.
[991.32 → 1002.54] They're a product-focused company, and they've made these AI announcements that clearly position AI as a feature and not the product itself, which a lot of the other, you know, big companies are, you know,
[1002.54 → 1005.36] it's almost AI is the product that they're trying to do.
[1005.42 → 1014.80] And so with the announcements at WWDC 2024, which is their developer conference every year, often called Dub Dub by insiders there,
[1015.12 → 1021.34] they are talking about AI in the context of the devices and of the tasking that their users are doing.
[1021.50 → 1022.68] And so I actually like that.
[1022.86 → 1031.86] I like, as you know, you and I both get absolutely inundated with reach out from startups and companies always promoting and hyping their AI product.
[1031.86 → 1039.54] And at least to see Apple talking about it being feature enhancement rather than the thing itself is good.
[1039.94 → 1041.70] It's a little bit of fresh air on that one.
[1042.34 → 1049.64] Yeah, I think that there's like when you have a little button that summarize or rewrite or whatever that button is,
[1049.64 → 1057.04] that's very much how I like the sort of first wave of pre-Chat GPT AI features.
[1057.36 → 1063.40] A lot of them that came out where, yeah, you just see the suggested text, or you'd see something that makes sense.
[1063.56 → 1071.30] And UX wise, that's probably, like you say, very fitting with Apple and their approach to things.
[1071.30 → 1083.58] I know that there was definitely some shade thrown by some, including Elon Musk about the reliance on open AI in Apple intelligence.
[1083.78 → 1084.90] Did you see any of that?
[1085.28 → 1086.76] That's Elon Musk being Elon Musk.
[1087.10 → 1093.12] I think part of it is just a gambit for the spotlight at any moment, inserting himself into any spotlight.
[1093.34 → 1094.58] I won't go into the Elon.
[1094.64 → 1097.94] If you're listening, Elon, you can come on our show and steal the spotlight.
[1097.94 → 1104.26] You're welcome, although it might be an interesting conversation there.
[1104.52 → 1106.96] Yeah, he's the same age I am, more or less.
[1107.34 → 1111.98] And so, yeah, I always kind of go, I'm just trying to imagine when he does some of the things.
[1112.24 → 1116.10] But anyway, back to the Apple bit without derailing on that one.
[1116.62 → 1125.62] Elon came out with the specific criticism of, okay, you're going to send everything off to the GPT API.
[1125.62 → 1128.74] And that's a huge privacy breach and stuff like that.
[1128.78 → 1140.60] But Apple had already clearly in the announcement said every user on a per-use basis will be given the option of, do you want, Siri will say, do you want to send this off to GPT for an answer?
[1140.76 → 1145.76] And the user on a per-use basis can say, yes, I want to do that or no, I don't.
[1146.12 → 1148.52] And they were very explicit about that up front.
[1148.52 → 1153.68] So I'm like, Elon, if you're going to use an iPhone or an iPad, just say no.
[1154.02 → 1157.82] Just say no and stop because that way you still have control.
[1157.88 → 1159.26] And that seems like a reasonable thing.
[1159.48 → 1163.82] I use the OpenAI app all the time on my iPhone.
[1164.38 → 1166.88] And it's one of those things that's open all the time.
[1167.02 → 1169.02] And that is good enough for many cases.
[1169.02 → 1178.68] But there are times when I would certainly like to integrate that capability into my other activities on the iPhone in a more integrated way.
[1178.90 → 1180.48] And this gives me that opportunity.
[1180.74 → 1183.80] So Elon was saying, only have the OpenAI app.
[1183.94 → 1187.12] And as a user myself, I say, no, give me the option.
[1187.38 → 1189.54] Sometimes I'm just going to have the OpenAI app there.
[1189.68 → 1192.26] But other times, let me integrate it with my other activities.
[1192.88 → 1195.04] Apple's going to give me the choice on whether I want to do it.
[1195.22 → 1196.14] I'm happy with that.
[1196.14 → 1197.10] All good.
[1197.36 → 1199.88] So he's not speaking for me in that capacity.
[1200.38 → 1200.48] Yeah.
[1200.80 → 1213.22] It might be interesting to talk just for a second about whether it's Elon or, you know, there's certainly in a less public or Memling way.
[1213.36 → 1222.98] A lot of people out there that do have concerns about this sort of closed model providers and some people that are still blocked by using these.
[1222.98 → 1227.64] I'm wondering, from your perspective, I have a few of my own thoughts.
[1227.64 → 1233.12] But like from a practitioner's perspective, just to kind of make it practical as we are on practical AI.
[1234.08 → 1254.58] What are this sort of tradeoffs, I guess, as you see it now with closed model providers or kind of using open models or some version of hosted open models in kind of the enterprise or development scenario versus kind of your personal device?
[1254.58 → 1259.72] Certainly, there's a direct to consumer type of angle to what we've discussed so far.
[1259.72 → 1272.22] But in terms of the practitioner themselves, we've touched on this occasionally, but I think it's probably good to continue touching on it occasionally because things are changing over time and changing very rapidly.
[1272.60 → 1273.32] So, yeah.
[1273.32 → 1275.46] From your perspective, do you have any thoughts on that?
[1275.46 → 1276.02] Sure.
[1276.24 → 1284.52] I think that is an issue that every large organization is navigating because you have a certain amount of funding to support your operations.
[1284.52 → 1291.82] And almost everybody has some, you know, tie in to one or more of the large commercial APIs.
[1292.24 → 1295.28] And it's a different context from a personal user.
[1295.28 → 1302.76] Like I talked about, you know, I'm paying my open AI monthly fee and I use that all the time for a variety of different tasks.
[1302.76 → 1305.32] But in the enterprise, it's a bit different.
[1305.54 → 1314.50] There may be that capability, but I'm also seeing enterprises that are really concerned about their data going out, about their information going out.
[1314.86 → 1317.54] If it's not their own, it's their customers that they have.
[1317.54 → 1332.60] By using a public API that you're paying for where that data goes outside your control, there is a huge concern and risk not only about the immediate privacy concerns, but also about the liability and the legal concerns around that.
[1332.60 → 1341.10] Because most organizations have a mixture of their own and other, you know, other organizations, a bunch of partnership agreements in large companies.
[1341.32 → 1354.58] Maybe you're okay with your data going out, but of the 50 partners that you have, it might be that 36 of them aren't too keen about their data that they have an agreement with you holding goes out as part of your data to a third party.
[1354.58 → 1360.80] So that makes it pretty challenging to use third party APIs in a manner that everyone is comfortable with.
[1360.90 → 1364.94] So I'm really seeing a lot of open source models being internally hosted.
[1365.20 → 1372.38] There is still a lag because Google, OpenAI, Anthropic, they keep pushing the boundaries on what they're offering.
[1372.98 → 1382.18] And the open source community is not typically, you know, all the way to the it's not just the model, but the services built around the model that makes it easy to use.
[1382.18 → 1387.10] So you have to kind of recreate that or use existing open source capabilities that are out there.
[1387.16 → 1388.58] And that requires effort.
[1388.86 → 1392.18] And there is funding and money spent on a good bit of money spent on that.
[1392.28 → 1408.18] But I would say that of the ring of people that I hang out with across multiple companies, that I'm seeing more of the internal hosting of models with the effort of trying to stay on top of current releases and monitor that as being the more widespread way.
[1408.18 → 1418.28] And there's a recognition that those models may not give you quite as good of an answer if it's a very expansive thing you're prompting on as a GPT model would.
[1418.84 → 1420.62] But that's okay in a lot of cases.
[1420.72 → 1421.48] It can get you through.
[1421.62 → 1430.30] And if you have multiple models to choose from and combine, then you can usually be very productive without kind of violating all those concerns that I enumerated.
[1430.30 → 1431.74] So it's both.
[1431.92 → 1436.30] But for me, I'm seeing more people turn in where now I run in a national security world.
[1437.32 → 1443.34] And so we might be a little bit more conservative about that across the various defence companies and stuff like that.
[1443.34 → 1447.78] And so acknowledging that there's a bit of a, you know, an array of possibilities there.
[1447.78 → 1448.26] Yeah.
[1448.26 → 1448.58] Yeah.
[1448.76 → 1463.74] One of the things that maybe has shifted a little bit in my mind since the last time I've been considering this question, and we've talked is I would say there's all the sort of privacy, data misuse, data leaving your network.
[1463.74 → 1467.02] All of that, I think, is a big piece of it.
[1467.22 → 1473.84] There's been kind of a developing mindset that I've kind of picked up on, which is slightly different.
[1473.84 → 1484.40] And I started to pick this up from, I've mentioned this a couple of times because it's been helpful for me, A16Z's recent surveying and reports.
[1485.00 → 1494.68] But the fact that, yes, there's a privacy element, but a lot of times organizations are using open models because of the control element.
[1494.96 → 1500.32] And it took me a while to, I think, fully parse through the implications of that.
[1500.32 → 1513.88] And I think some of what it gets down to is when you're connecting to one of these closed systems and there's hosted open models in a variety of places you could get.
[1514.02 → 1521.82] So when I say hosted closed system, I mean, like you literally don't know what's happening behind that API or how the model is called and that sort of thing.
[1521.82 → 1535.36] Those are productized AI systems, which means that they're making opinionated choices about how to improve the performance of that product surrounding the model.
[1535.78 → 1535.88] Right.
[1536.20 → 1536.46] Yes.
[1536.60 → 1539.46] And that actually can be an amazing thing.
[1539.66 → 1539.86] Right.
[1539.94 → 1543.06] Like open AI functionality is spectacular.
[1543.06 → 1549.94] Like without doubt, these other systems, anthropic, others, really spectacular functionality.
[1550.50 → 1563.06] But there's this element of it where they've made some opinionated choices for you about how to process the data that you're putting into that system before and after it hits the model.
[1563.06 → 1564.64] And so there's a lot more going in.
[1564.76 → 1576.42] And I think you see this come out very much in, for example, the stuff that happened with Gemini, where you put in your prompt to generate an image of American founding fathers.
[1577.14 → 1586.32] And there's clearly, you know, however that worked, a modification of your prompt or extra instructions to bias that output to look a certain way.
[1586.72 → 1586.84] Sure.
[1586.92 → 1588.48] If you're interested, go look it up.
[1588.56 → 1589.98] There are lots of interesting pictures.
[1589.98 → 1593.56] And to be fair, they've rectified that situation as far as I know.
[1594.02 → 1597.82] But when you have that sort of decision made, you don't have full control.
[1598.04 → 1608.72] Like it's not just your prompt going into the model and you kind of choosing how to govern or bias that or process user inputs or do your prompt emulating.
[1609.28 → 1618.74] And so it can be perfect, but it can be sort of frustrating at that level where you get like 80 to 90 percent of the way towards what you want.
[1618.74 → 1632.30] And then for some reason, you just can't figure out why you can't like to get that last bit, or you can't figure out why you're like this error is happening or there's latency types of fluctuations or whatever those things might be.
[1632.40 → 1633.90] It could be bias in the output.
[1634.40 → 1639.58] So I think that that like opinionated product ties thing, like it's both a good and a bad.
[1639.58 → 1643.96] And depending on your scenario, that may actually be what you need.
[1644.10 → 1644.20] Right.
[1644.26 → 1646.08] Like I'm not going to worry about these things.
[1646.30 → 1651.78] I trust the way that sort of these things are being handled internally in a system like this.
[1651.80 → 1654.28] And I'm guessing that will be fine for many people.
[1654.28 → 1661.96] But then there's people that want to build kind of these competitive AI features into what they're creating as a company.
[1662.52 → 1672.32] And they want full control to figure out like, you know, to build those in exactly the way they want to make sure that they can test those in exactly the way they want and to have that control element.
[1672.46 → 1677.60] I think that's way more crystallized in my mind than it was previously.
[1678.08 → 1680.28] I think that's a fantastic insight right there.
[1680.28 → 1690.62] And I think most people miss that because with the hype machine going, we have a habit of talking about the models themselves all the time and, you know, kind of as product.
[1690.76 → 1697.96] And therefore, there's so much that these companies that are putting out these as a service are doing.
[1698.06 → 1700.48] There are so many humans involved that you never see.
[1700.66 → 1707.86] And yes, that can really make it much better in some ways because they're kind of shortcutting what the model may not be able to do on its own.
[1707.86 → 1712.04] They are shortcutting and greasing the skids to make you get what you want.
[1712.10 → 1716.72] But at the same time, anytime there's a human involved, you're going to have the bias as well.
[1717.08 → 1722.58] And they're trying to make it safe and controlled and not have some sort of thing that ends up in the news in a very negative way.
[1723.14 → 1725.18] And that puts constraints around it.
[1725.56 → 1726.54] It just is what you knew.
[1726.66 → 1734.74] So, yeah, I think it's really key that we look at it as not only a model, but model plus the surrounding services, whether you're building them or whether someone's building them for you.
[1737.86 → 1738.86] So, yeah.
[1749.86 → 1750.90] What's up, friends?
[1751.08 → 1752.20] I love Back blaze.
[1752.30 → 1753.80] I'm happy to have them as a sponsor.
[1754.28 → 1758.40] Back blaze makes backing up and accessing your data astonishingly easy.
[1758.86 → 1761.16] This is a service I personally use.
[1761.24 → 1764.22] Go to Backblaze.com slash practical AI.
[1764.22 → 1770.58] You get unlimited cloud backups for Macs, PCs, businesses for just $99 a year.
[1770.92 → 1781.42] You can easily protect business data through a centrally managed admin, protect all the data on your machines automatically, easily deploy across multiple workstations with various deployment options.
[1781.90 → 1790.22] You can add on enterprise control, including granular access permissions, advanced single sign-on, group management controls, and compliance support.
[1790.22 → 1796.22] They even offer multiple restore options, including rapid recovery in the event of data loss or ransomware.
[1797.12 → 1797.58] That sucks.
[1797.96 → 1803.76] You can access your backed up data from anywhere in the world using their web app or their iOS or Android app.
[1804.00 → 1805.74] You can even restore by mail.
[1806.04 → 1809.34] They'll give you a hard drive with all your data shipped to your door.
[1809.34 → 1814.46] You buy a hard drive restore, send the hard drive back within 30 days, and get a full refund.
[1814.84 → 1817.38] Get one year file retention and version history.
[1817.84 → 1822.26] Over 55 billion with a B files restored for customers so far.
[1822.60 → 1827.88] Visit backblaze.com slash practically I so they know where you came from and continue to support the show.
[1827.88 → 1841.28] This is a service obviously recommended by me, but also by New York Times, Inc. Magazine, Mac world, PC world, Life Wire, Wired, Tom's Guide, 9to5Mac, and just so many more.
[1841.78 → 1848.86] You receive a fully featured or no risk trial at backblaze.com slash practical AI.
[1849.38 → 1850.88] Again, they're supporting the show.
[1851.20 → 1854.92] Go there, play with it, start protecting yourself from potential bad times.
[1854.92 → 1855.88] Start today.
[1857.88 → 1875.04] All right, Chris.
[1875.18 → 1885.22] Well, a lot of times in these fully connected episodes, we do try to kind of bring some learning element to the forefront as people are exploring these topics.
[1885.22 → 1893.90] One of the ones that has been coming up a lot for me, which we've talked a lot about on the show is RAG or retrieval augmented generation.
[1894.70 → 1908.90] But we've only sort of talked about it at a surface level and at the sort of naive RAG level, which might misrepresent sort of some of what people are doing with this approach under the hood.
[1908.90 → 1912.22] And this would like generally kind of be framed.
[1912.54 → 1917.20] I think if you search advanced RAG, you'll find a bunch of articles.
[1917.72 → 1928.68] And really what's happening is there's a naive approach to this RAG type of workflow, which can get you to some really amazing results really quickly.
[1928.68 → 1939.52] But then when you have to kind of fine tune, improve that system, load in more data, use documents that are closely related one to another, various types of documents.
[1939.52 → 1947.74] There's a lot to dig into in terms of fine-tuning that system and fine-tuning both how the retrieval and the generation works.
[1948.16 → 1958.42] And there's a whole variety of sort of workflows that have been developed by the community that can help you improve your RAG setup.
[1958.42 → 1963.60] So that's kind of one of the things that I wanted to bring up here and maybe talk through a couple of those.
[1963.72 → 1967.24] I know our friend Demetrius, we talked to him.
[1967.28 → 1970.10] He's got some opinions about RAG versus fine-tuning.
[1970.26 → 1971.30] That's one thing you'll hear.
[1971.82 → 1976.18] But yeah, I would love to dig into that if it sounds interesting to you.
[1976.54 → 1976.82] Absolutely.
[1977.30 → 1982.52] And I think you're the right person to do this, given that you're diving into this stuff all the time.
[1982.52 → 1991.44] Yeah, well, certainly this is RAG pipelines are probably the first thing that people are building with generative AI.
[1991.88 → 1994.78] And the idea is not too complicated.
[1994.96 → 2004.04] The idea is, let's say I have a bunch of documents that contain information relevant to questions or queries that I might have.
[2004.04 → 2020.80] Instead of just asking an LLM to give me an answer or to do something, which would rely on the probabilities of that model in generating its own text and the data that it was trained on, you could get any sorts of answers out of that LLM.
[2020.80 → 2034.92] Rather than just relying on that, I'm going to inject on the fly some of that external data that I have into the prompt to help answer the question or the query, something like that.
[2035.00 → 2038.24] So we do this all the time with ChatGPT and other systems, right?
[2038.30 → 2042.50] When I say, summarize this email for me, and then I paste in an email.
[2043.26 → 2049.64] That's how I'm injecting data into the prompt to the model right at the time that I need it to run.
[2049.64 → 2052.42] So there's no fine-tuning of the model here.
[2052.52 → 2057.54] It's just a strategic insertion of data when I'm prompting the model.
[2057.98 → 2070.30] And often this happens in like, oh, I have a bunch of developer documentation or onboarding materials for my company or a wiki or a bunch of webinars or a bunch of podcasts or whatever.
[2070.30 → 2073.46] And I want to answer questions out of that material.
[2073.46 → 2080.50] So if you're interested in the model, then these can be loaded into a vector database, which allows you to do the retrieval part.
[2080.70 → 2085.56] So to find the relevant chunk of information that's required to answer the question.
[2085.68 → 2094.70] And then you take that relevant chunk, insert it into a prompt, and then respond or let the LLM generate based on that given context.
[2094.70 → 2101.24] So that's sort of the naive RAG approach where you sort of have a user query.
[2101.48 → 2109.68] You find a single chunk of information in some repository of information, insert it into the prompt as context, and hopefully get an answer.
[2109.96 → 2116.76] Which it is naive, but it surprisingly works amazingly well in many cases, right?
[2116.76 → 2117.78] It does.
[2118.14 → 2123.66] It's interesting as we get in from kind of the naive to the advanced ideas in it.
[2123.78 → 2126.94] And you also just mentioned for a second fine-tuning along the way.
[2127.16 → 2128.74] It is definitely the first step.
[2128.84 → 2132.84] I think it's easy to implement in general for people, which is why it's the first step.
[2133.04 → 2140.96] But I also think before you go on, I think a lot of organizations are getting stuck on naive RAG and just kind of stopping there.
[2141.08 → 2141.36] Yes.
[2141.46 → 2142.80] And I've noticed that.
[2143.04 → 2143.60] So keep going.
[2143.80 → 2144.28] Yeah, yeah.
[2144.28 → 2145.64] I think you're totally right.
[2145.64 → 2153.84] And I think this is why I wanted to bring up this topic because some will hit, and they'll get like sort of OK performance out of their RAG system.
[2154.08 → 2159.98] But then they don't realize that there are more options to improve that system.
[2160.32 → 2162.86] Yeah, I've seen a lot of people thinking it solves it.
[2163.00 → 2163.16] Yeah.
[2163.32 → 2169.40] Like all we need is an LLM, and then we're just going to give it the data for RAG that we're going to inject into it, and we're done.
[2169.40 → 2174.12] And that I'm hoping we can break some of that perspective over the next few minutes.
[2174.12 → 2174.72] Yeah.
[2174.80 → 2185.48] And the question would be like, well, OK, if you're getting some good answers and some not good answers, for example, what do you do to improve your RAG system?
[2185.48 → 2191.84] And that's where there is a whole variety of things to explore.
[2191.84 → 2197.02] And like I say, if you're really interested in this, I'd recommend searching for advanced RAG.
[2197.12 → 2202.12] I'd recommend looking at the Llama Index blog, the Lanced blog.
[2202.34 → 2206.90] There's a lot of perfect content out there to help you parse through this.
[2206.90 → 2212.92] But let me kind of inspire with a few snippets of things that you could keep in mind.
[2213.66 → 2218.70] So the first, I think, is around context enrichment.
[2219.42 → 2228.68] This is a very simple thing that you can do where let's say you have 100 documents, and you split them up into little chunks, which you embed in the vector database.
[2228.68 → 2233.50] And you search against those little chunks to find the relevant thing that might help you answer the question.
[2233.50 → 2240.88] Well, depending on how you chunked up that information, it might not give you all the context you need to answer.
[2241.18 → 2242.90] It might be in like the previous chunk.
[2243.00 → 2244.42] It might be in the next one.
[2244.52 → 2247.88] It might be in the one that you found, or it might be in a combination.
[2247.88 → 2254.48] And so this sort of idea of context enrichment might be that you just find that chunk that's relevant.
[2254.48 → 2261.58] And then instead of inserting just that chunk, insert that chunk plus the one before it and the one after it, for example.
[2261.58 → 2262.90] Just expand it a little bit.
[2263.00 → 2264.00] Enrich it a little bit.
[2264.56 → 2275.32] Another sort of common thing is maybe you want to pull the three most relevant chunks rather than the one most relevant and add more context there.
[2275.32 → 2279.70] So there's more that you can add in more than just a single chunk.
[2279.90 → 2292.60] The other sort of related methodology here before we get into maybe the more fancy stuff is actually doing a two-level search over your data.
[2292.60 → 2296.84] So if you think about it, let's say that I have, again, 100 documents.
[2297.76 → 2302.24] And, you know, there might be similar content across those documents.
[2302.24 → 2305.82] They might overlap in certain cases, but they're different documents.
[2306.08 → 2325.90] Well, if you take and summarize with an LLM each of those documents or pages of those documents, and then you also chunk it up into smaller chunks that you eventually want to use for your RAG, you could first search on the summary, which would kind of point you to the right document that's going to answer your question.
[2325.90 → 2333.54] And then do a second phase of retrieval within that document itself to pull out the relevant section, right?
[2333.66 → 2338.68] This helps you kind of hone in on the right document that you're using.
[2338.80 → 2346.16] So those are two fairly easy to implement in terms of how you set up your vector database and how you do your querying.
[2346.32 → 2348.08] But they can provide a boost.
[2348.18 → 2349.74] Now, there's more complicated things.
[2349.80 → 2351.52] We can get to those in a second.
[2351.76 → 2353.16] But do those make sense?
[2353.38 → 2354.22] It does make sense.
[2354.22 → 2354.58] Yes, yes.
[2355.24 → 2356.10] I'm just curious.
[2356.22 → 2357.08] Two-second question.
[2357.72 → 2370.52] When people are going, you know, in your first case there, where they're just going for the answer and not adding the surrounding chunks, do you think that's kind of bias from traditional database operations where you find the answer and that's it?
[2370.78 → 2372.42] Or is that in my space?
[2372.46 → 2376.50] I was just wondering, as you were saying that, why people might be limiting themselves in that way.
[2376.64 → 2378.44] Yeah, I think it's a perception problem.
[2378.44 → 2382.26] It's just like there's so many examples out there of getting started with RAG.
[2382.56 → 2386.58] And that's all you kind of see unless your kind of really dig in.
[2387.16 → 2389.06] So maybe it's just a perception issue.
[2389.22 → 2396.80] It is also like maybe that sort of holdover from how you would retrieve things from in a traditional database sense.
[2396.94 → 2397.16] Gotcha.
[2397.16 → 2399.06] Those might both factor in.
[2399.56 → 2406.58] There's another kind of hybrid or two-level type of search that happens.
[2406.58 → 2418.94] And this is implemented in several different vector databases, even natively now because it can be quite useful, is actually doing two levels of searching.
[2419.24 → 2429.78] But the first, which is a traditional full text search or keyword search, and then a vector comparison rather than just relying on the vector comparison.
[2429.78 → 2437.36] So you kind of hone in on the full text kind of keywords first and then do a vector comparison.
[2438.12 → 2446.14] And you could even ensemble these in various ways and use one for re-ranking or ordering versus the other one.
[2446.30 → 2448.48] There's a variety of ways to implement this.
[2448.62 → 2456.28] But this would be kind of generally categorized as hybrid ways of searching, I think is most frequently termed.
[2456.28 → 2461.80] So there's the context enrichment, there's the hierarchical search or index retrieval.
[2461.94 → 2463.92] That's the kind of summary then chunk.
[2464.20 → 2470.86] And then there's like the hybrid search, which would be actually using two different search methodologies.
[2470.86 → 2476.56] And notice all of this has to do with the retrieval part for the most part that we're talking about here.
[2476.68 → 2483.10] Not mostly the LLM side, although you could use an LLM to generate the summaries for the hierarchical approach.
[2483.10 → 2490.72] So it's interesting that those TF-IDF, keyword searching, full text search sort of things is coming up again.
[2491.18 → 2499.08] So back to our original way we started this episode, the data science pieces still survive in many ways.
[2499.30 → 2501.06] It's still, yeah, it's still relevant there.
[2501.22 → 2502.54] And I don't think that's changing.
[2502.92 → 2503.10] Yeah.
[2503.32 → 2511.04] The last two that I'll highlight, one that comes up a lot that people will use is a method called re-ranking.
[2511.04 → 2515.38] So there's actually models out there known as cross encoders.
[2515.96 → 2523.82] And what happens is you might do a first level vector search to get a smaller number of candidate documents.
[2524.18 → 2533.28] And then use maybe a more expensive model-based approach to actually re-score the candidates that you pulled and re-order them.
[2533.68 → 2535.04] Hence the name re-ranking.
[2535.36 → 2539.30] Re-order them or filter them to the most relevant document.
[2539.30 → 2541.12] So that's kind of the re-ranking approach.
[2541.58 → 2546.54] There are a couple of fascinating ones where you use an LLM in the loop.
[2546.88 → 2548.60] One of those called Hide.
[2548.98 → 2551.56] Lanced has a good blog post about this.
[2552.00 → 2558.72] Uses LLMs to generate sort of hypothetical documents that should answer this question.
[2558.72 → 2564.54] And then you kind of use those hypothetical documents in the retrieval.
[2564.78 → 2567.30] There's people that do also query transformation.
[2567.30 → 2569.36] So they actually take the query in.
[2569.58 → 2582.60] This kind of fits our previous discussion about modifying a prompt, except now maybe you're in control of it, where you take that prompt in, and you actually regenerate the query such that it's more favourable to the retrieval task.
[2582.60 → 2594.50] That was a lot, and I know it was quick, but I think it might be good for people to hear that and just kind of see that there's a much wider picture of these advanced rag techniques.
[2594.62 → 2597.52] And I didn't even get a chance to sort of get through all of them.
[2597.62 → 2599.10] People are exploring a lot of things.
[2599.10 → 2607.28] But that, I think, paints a much more rich picture of what can happen in these rag pipelines versus just that naive approach.
[2607.72 → 2609.60] Thank you very much for kind of bringing this to attention.
[2609.78 → 2618.14] I think it would be well advised for people to recognize they're kind of getting to first base with the typical rag approach.
[2618.52 → 2621.76] And that's working for them in some cases quite well.
[2622.38 → 2626.94] But these tools are out there now where it's not so hard to then go on and move past that.
[2626.94 → 2628.82] But I'm seeing a lot of people get stuck there.
[2628.82 → 2635.80] So thank you for kind of covering that territory and giving people an opportunity, if they're not familiar with it, to maybe dive into this.
[2636.16 → 2636.78] Yeah, definitely.
[2637.32 → 2644.20] Well, it's been a fun one, Chris, to bring back some data science discussions into our podcast.
[2644.68 → 2649.56] And, yeah, excited to see what's coming over the next couple of weeks that we can catch up on soon.
[2649.90 → 2650.28] Absolutely.
[2650.64 → 2651.36] Talk to you later, Daniel.
[2658.82 → 2659.78] All right.
[2660.08 → 2662.58] That is Practical AI for this week.
[2663.38 → 2664.40] Subscribe now.
[2664.60 → 2669.56] If you haven't already, head to practicalai.fm for all the ways.
[2669.98 → 2675.96] And join our free Slack team where you can hang out with Daniel, Chris, and the entire Changelog community.
[2676.56 → 2681.18] Sign up today at practicalai.fm slash community.
[2681.18 → 2688.72] Thanks again to our partners at fly.io, to our beat freaking residents, Break master Cylinder, and to you for listening.
[2689.08 → 2690.84] We appreciate you spending time with us.
[2691.20 → 2692.38] That's all for now.
[2692.62 → 2694.30] We'll talk to you again next time.
[2694.30 → 2710.80] Anyhow ETAs
