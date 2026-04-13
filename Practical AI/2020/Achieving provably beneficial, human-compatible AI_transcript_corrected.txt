[0.00 → 4.82] I don't think deep learning evolves into AGI. So AGI, artificial general intelligence,
[5.14 → 10.44] is not going to be reached by just having bigger deep learning networks and more data.
[10.82 → 16.72] AGI and human intelligence require fundamental capabilities that are just not present in
[16.72 → 20.42] deep learning technology as we currently understand it. Deep learning systems don't
[20.42 → 26.14] know anything. They can't reason. They can't accumulate knowledge. Furthermore, they can't apply what
[26.14 → 30.44] they learned in one context to solve problems in another context, et cetera, et cetera. And these
[30.44 → 33.58] are just elementary things that humans do all the time.
[35.92 → 42.06] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[42.06 → 47.18] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted on Linde
[47.18 → 55.76] cloud servers. Head to linode.com slash Changelog. This episode is brought to you by Digital Ocean,
[55.76 → 60.92] Digital Ocean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[61.28 → 66.02] They have an intuitive control panel, predictable pricing, team accounts, worldwide availability
[66.02 → 73.82] with a 99.99 uptime SLA and 24 seven, 365 world-class support to back that up. Digital Ocean makes it
[73.82 → 79.98] easy to deploy, scale, store, secure, and monitor your cloud environments. Head to do.co slash
[79.98 → 84.60] Changelog to get started with a $100 credit. Again, do.co slash Changelog.
[85.76 → 99.68] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical,
[100.00 → 105.00] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[105.00 → 109.70] and data science happen. Join the community and Slack with us around various topics of the show
[109.70 → 114.94] at Changelog.com slash community and follow us on Twitter. We're at Practical AI FM. Okay,
[114.94 → 126.00] take it away, Chris. Welcome to another episode of the Practical AI podcast. My name is Chris Benson.
[126.20 → 131.02] I'm a principal AI strategist at Lockheed Martin. Normally, listeners would know that Daniel Whiten ack,
[131.08 → 136.94] my co-host, would be with me. He is unavailable today. He's out sick. And so I have the pleasure
[136.94 → 145.08] of introducing our guest today, who is a legend in the AI field. With me today is Stuart Russell,
[145.62 → 152.32] who is a professor of computer science at University of California, Berkeley, and holder of the Smith,
[152.32 → 155.02] is it Made chair, if I'm getting that correct?
[155.18 → 155.80] Smith Made.
[156.04 → 162.20] Made, I apologize. And also, if the name sounds familiar, he is the author of the standard book
[162.20 → 165.98] on artificial intelligence, which most practitioners in the field will be familiar with,
[166.36 → 172.18] as well as a recent book for a general audience, which is called Human Compatible,
[172.28 → 177.46] Artificial Intelligence and the Problem of Control. Stuart, thank you very much for coming on the show.
[177.58 → 178.02] Pleasure.
[178.32 → 183.24] I know I barely touched on it. I know you have been in this field for decades. If you could tell us
[183.24 → 186.74] just a little bit more about your background before we get fully launching.
[186.74 → 192.58] Yes. As you say, it's been quite a long time. I first started doing AI when I was in high school,
[192.72 → 197.62] because I got a programmable calculator, and I thought I could make it really intelligent.
[198.04 → 203.22] But it turned out that it only allowed 36 keystrokes in the program. So I didn't get very
[203.22 → 211.10] far with that attempt. And then I got to use a giant computer at Imperial College. So I wrote a chess
[211.10 → 216.72] program. That was my first serious AI program. I did my PhD at Stanford. I joined Berkeley,
[216.72 → 224.14] in 86. So it's 34 years teaching at Berkeley. And it's been a pretty interesting time. And it's,
[224.50 → 230.10] you know, most people would say now is maybe the most exciting time to be doing AI, because there's
[230.10 → 235.92] so much progress. We've been able to solve or nearly solve some of the major open problems of
[235.92 → 240.52] the field, you know, speech recognition, machine translation, certain parts of computer vision,
[240.64 → 245.30] so particularly recognizing objects and images, all of those things now work pretty well. So then
[245.30 → 251.24] we can roll out all those techniques into the real world and do cool things like driving cars and
[251.24 → 253.90] everything like that. So it's lots of fun. We're all very busy.
[254.68 → 259.76] So I guess, you know, given that you've seen so much of the evolution of this field over time,
[259.76 → 265.74] could you talk a little bit about what the field was like when you came into it and what technologies
[265.74 → 271.90] were prevalent? And tell us a bit about the evolution of the field over the years, all the way into the
[271.90 → 275.04] current, you know, what's certainly taken off these last few years.
[275.04 → 280.68] Sure. Yeah. So in the early years, so I guess I would say I started probably 1975.
[281.82 → 290.88] The focus was almost exclusively on problem-solving, game playing, planning, logical reasoning. So
[290.88 → 297.44] everything was deterministic. So we assume that we could give the computer perfect knowledge of the
[297.44 → 301.44] problem, a perfectly stated goal, and then it would come up with a guaranteed solution,
[301.44 → 307.14] whether it was proving a theorem or, you know, finding a checkmate or assault, you know, coming up with a
[307.14 → 314.24] plan to deliver a bunch of parcels to a bunch of recipients or whatever it might be. And in the 80s,
[314.24 → 322.20] we had the big expert system boom. So initially a logical rule-based system. So encoding expertise in
[322.20 → 328.20] logical rules. Sometimes we now call it business rules or business intelligence. That's a phrase that
[328.20 → 333.50] they use because the term expert system fell out of favour. But in the 80s, that was a really,
[333.50 → 340.16] you know, big, exciting, you know, hype bubble, just like today. Sure. And the beginnings of
[340.16 → 345.80] handling uncertainty because we wanted to make expert systems that did things like medical diagnosis,
[345.80 → 351.20] where there are no hard and fast rules. You have to take the evidence and combine it in,
[351.20 → 358.14] you know, to get some kind of soft prediction, you might say. But that technology largely failed
[358.14 → 364.06] in the real world. And complicated reasons for it, but I think basically it was not doing uncertain
[364.06 → 369.66] reasoning correctly. And so as you tried to build bigger systems for real problems, the whole thing
[369.66 → 375.46] would kind of fall apart. Every time you had a new rule, the other ones would start messing things up.
[375.46 → 380.40] And, you know, the interactions would cause wrong answers to come out. And companies very quickly
[380.40 → 387.38] stopped investing in this. And we had what we call the AI winter, where, you know, I think my AI course
[387.38 → 395.12] was down to about 25 students in 1990. It's up at about 900 right now. I imagine it is.
[395.98 → 400.22] And that's only because we're not, you know, the fire marshal won't let us have any more people in the
[400.22 → 405.24] class. It would probably be, you know, 12, 1500 if we let everyone in.
[405.46 → 411.18] So what happened next in AI actually was that rigorous probabilistic methods took over
[411.18 → 417.26] within the field, mainly from the work of Puerperal starting in the mid 80s. And then
[417.26 → 424.56] machine learning had a renaissance, reinforcement learning had a renaissance. And so from the late
[424.56 → 435.44] 80s until around 2011 or so, there was pretty solid technical research progress using probabilistic
[435.46 → 443.10] statistics, connections to operations research control theory became a very mathematical field.
[443.30 → 448.78] Some of the techniques worked pretty well, you know, so speech recognition became reasonably
[448.78 → 455.90] practical. And the first self-driving cars were operating long before the present day and
[455.90 → 461.06] doing so reasonably successfully. You know, there were big applications of planning, there were
[461.06 → 466.60] lots of diagnostic systems and so on. So it was relatively successful, but it wasn't really
[466.60 → 474.82] until deep learning happened around 2011, 2012, that it really hit the big time in terms of media coverage
[474.82 → 483.18] and excitement and so on. So it was deep learning that enabled us to, for example, beat the human
[483.18 → 488.90] world champion at Go, a combination of deep learning with reinforcement learning methods and
[488.90 → 495.24] game playing techniques that had been around for decades and decades. But deep learning was this
[495.24 → 501.58] extra ingredient that let the system somehow recognize patterns on the Go board that allowed
[501.58 → 506.28] it to be the human world champion. So now we're in a position where, you know, as I mentioned,
[506.44 → 512.34] thousands of students want to take AI courses. There are thousands of startup companies, all the big
[512.34 → 520.00] companies have major AI divisions and are using AI in hundreds of applications throughout their
[520.00 → 524.72] businesses. So it's fun, it's exciting. Maybe there's some hype going on too.
[525.64 → 530.92] There might be a little bit. So going through that, it really begs the question for me,
[531.12 → 536.18] and I'm going to throw a question at you, I imagine it will be like, but you're looking at all these
[536.18 → 541.76] different types of artificial intelligence, different things that are being labelled as artificial
[541.76 → 547.74] intelligence, you know, from the symbolic logic days, through expert systems, all the way up
[547.74 → 552.82] through today's deep learning and other associated technologies. And there are obviously vastly
[552.82 → 558.20] different underpinnings in terms of what they can do and how you arrive at them. How do you define
[558.20 → 563.68] artificial intelligence? What does the term mean to you as the person who has literally written the
[563.68 → 567.74] textbook on the subject? And how has that changed and evolved over those years?
[567.74 → 573.34] So it's a good question. I mean, all of the above, all the things you mentioned, this is all artificial
[573.34 → 580.80] intelligence because it's all in the service of creating machines that can act intelligently,
[581.04 → 586.20] which means really choosing actions that can be expected to achieve their objectives.
[586.86 → 592.48] You know if you're a self-driving car, the objective is to get to the airport safely, legally,
[592.48 → 599.62] comfortably. And so in order to do that, you need perception, but you also need symbolic planning
[599.62 → 607.30] to choose a route. You need parablastic forecasting to deal with traffic delays and maybe have a backup
[607.30 → 612.84] route just in case. And you need speech recognition in order to interface with the passenger, et cetera,
[612.90 → 616.14] et cetera. So, you know, if you want to build a system that's going to help a mathematician,
[617.14 → 621.40] you can't just throw a bunch of theorems and proofs into a deep learning system and say, here,
[621.40 → 625.78] you know, learn how to do math. You actually have to have symbolic reasoning capability,
[626.00 → 632.06] theorem proven, you know, which the underlying technology of that is symbolic logic and not
[632.06 → 638.72] statistical learning. So it all depends on what you want to do. The overriding model, which I think
[638.72 → 645.20] pervades not just AI, but a lot of other disciplines, control theory, operations research,
[645.20 → 652.00] economic statistics, they all have this model, which is that we specify an objective and then
[652.00 → 659.84] the machine finds some optimal solution or a way of achieving the objective, the best solution.
[660.22 → 666.04] And so actually what the book is about, the human compatible book is basically saying that model
[666.04 → 674.02] is really a terrible model. Now, unfortunately, the first three editions of my textbook actually kind
[674.02 → 680.26] of solidified that model and said, okay, here's how we understand, you know, here's how we pull
[680.26 → 685.28] everything in AI together into a single conceptual framework. And you can see all the different
[685.28 → 689.86] kinds of AI research. It's sort of different facets, different ways of looking at that same
[689.86 → 697.62] underlying conceptual framework. And the reason I think it's a terrible model is not a new thing,
[697.62 → 704.58] right? It's something we've known for thousands of years, which are we cannot specify our objectives
[704.58 → 709.86] completely incorrectly. And, you know, if you look at the legend of King Midas, he specifies his
[709.86 → 714.86] objective, I want everything I touch to turn to gold, you know, the gods, or you could say the AI system
[714.86 → 720.06] gives him the objective exactly as he specifies. And then of course, his food and his drink and his
[720.06 → 724.20] family will turn to gold and he dies. Misery, starvation.
[724.20 → 726.54] Unexpected consequences.
[727.08 → 731.08] Right. You know, that's the thing, right? It's always unanticipated consequences,
[731.98 → 737.10] accidental side effects, collateral damage, externalities is what the economists call it,
[737.22 → 743.16] but it's a pervasive problem. We've known about it for a long time. You know, that's why your third
[743.16 → 749.06] wish is always please undo the first two wishes because I've ruined everything. Right? So the human
[749.06 → 755.64] compatible book basically says, okay, we have to throw away that model because, you know, up to now,
[755.74 → 761.12] it hasn't been that bad because, you know, first, most of our AI systems were toys. They were
[761.12 → 763.80] in the lab. You know, we were doing demos.
[763.80 → 766.58] It wasn't out there in industry at the level it's at now.
[767.08 → 773.08] Until recently on a global scale, but now it is, right? So now, you know, you've got the content
[773.08 → 779.22] selection algorithms from all the different social media platforms and those algorithms are,
[779.46 → 786.70] they're machine learning algorithms, but they decide what billions of people spend hours every day
[786.70 → 794.56] reading and watching. Right? So in terms of their actual direct, in terms of like, you take the
[794.56 → 799.92] number of people times the amount of time, they are more powerful than anything that's ever existed
[799.92 → 807.92] in the history of the human race by far, by far. Right? I mean, you know, you think Stalin was powerful,
[808.24 → 813.38] but he got to speak to his people like, you know, maybe half an hour every month or something. Right?
[813.38 → 818.78] Yes. These algorithms are speaking to 50 times more people for hours every day.
[819.76 → 823.84] A largely oblivious audience for the most part that's acting on them.
[824.24 → 827.38] Yeah. So the audience doesn't know what the algorithms are doing or what they're trying to do.
[827.44 → 832.74] The algorithms are trying to maximize their objective, which is click through or engagement
[832.74 → 838.70] or something like that. And in the course of doing that, rather than just send you what's
[838.70 → 845.48] interesting, they actually modify you into someone who's more predictable from their point of view,
[845.48 → 848.70] because the more predictable you are, the more money they can make off you.
[849.50 → 856.08] And so whatever you start out as they change you and mould you into a predictable clicker.
[856.60 → 859.88] And so that's what they've done. And I think, you know, most people would say
[859.88 → 863.54] that the results have been pretty disastrous on the whole.
[863.54 → 868.04] So I want to ask you, there's a particular remark you make in the book that I want to ask you,
[868.08 → 873.12] and I think you're already kind of going down the path on this to some degree, but you say,
[873.26 → 878.72] we must plan for the possibility that machines will far exceed the human capacity for decision
[878.72 → 883.32] making in the real world. And I think that you've started to address some of the challenges.
[883.56 → 888.40] Could you give us a little bit more of a holistic perspective on what, I mean, that statement
[888.40 → 894.16] has a lot in it right there. Can you talk a little bit about what the implications of that is?
[895.02 → 900.60] So, yeah. So let's give an example, right? Suppose that a few years or decades down the line,
[901.24 → 907.42] you're, you know, the CEO of an IT company or your solar power company or whatever it might be,
[907.50 → 914.06] and you want your company to be more successful. So you engage an AI system, and you give it the objective
[914.06 → 920.86] of, let's say, you know, maximizing the profits or the revenues in my corporation. And because that
[920.86 → 930.34] system is far more capable than humans are, right, it devises plans that are more successful than
[930.34 → 938.10] all the competitors can be. And so that corporation in the interests of maximizing revenues
[938.10 → 945.24] gradually takes over larger and larger portions of the world economy, you know, and if it's not
[945.24 → 951.92] properly designed, right, if that was the objective, you know, wherever it was feasible, it might end up
[951.92 → 957.64] using slave labour, for example, in order to maximize profits, and so on and so forth, right? I mean,
[957.64 → 964.12] you can imagine all the ways that corporations have abused humanity in the past, and now we've got one
[964.12 → 968.96] that's much more capable than human beings are. You know, some people actually argue that this is
[968.96 → 978.28] already happening, not from AI, but from corporations that optimize profit at the expense of everything
[978.28 → 985.82] else. So, for example, at the expense of the climate, the fossil fuel industry has optimized its profits by
[985.82 → 993.96] sort of multi-decade misinformation strategy that's actually outwitted the human race, right?
[993.96 → 1000.48] And so even though the vast majority of experts and economists and scientists say, oh, you know,
[1000.56 → 1004.86] we need to have a carbon tax, we need to do this, we need to do that, we aren't doing any of it,
[1005.32 → 1011.74] right? We're just talking about it. And so effectively, the fossil fuel industry has defeated the human race
[1011.74 → 1020.38] by superior pursuit of a fixed objective. So it would get much worse than that when AI systems are able to
[1020.38 → 1026.34] invent and carry out these kinds of strategies. So that's even, you know, within the realm of things
[1026.34 → 1032.76] that we currently understand, right? That you could have corporate strategy, you could enslave people,
[1032.80 → 1035.88] you could do this, you could do that, but AI systems will come up with things we don't understand.
[1036.46 → 1036.58] Sure.
[1036.58 → 1045.14] And, you know, the whole human race could be collateral damage if we don't know how to control the systems that we
[1045.14 → 1052.50] create. And so far, there are no examples of a dumb species controlling a more intelligent species forever.
[1053.50 → 1060.06] I totally agree with that. So for my own employer, I'm actually the person leading on AI ethics. So AI ethics is a huge
[1060.06 → 1066.06] passion of mine. And obviously, you've raised some pretty big concerns there. And I'm taking a little bit of a tangent,
[1066.06 → 1073.08] I wasn't really expecting to go down this path. But I am curious how you envision the role of AI ethics
[1073.08 → 1079.60] in our society and the world at large, given everything that you just said. I mean, it clearly
[1079.60 → 1085.96] the potential for consequences that we did not envision that we did not plan on is fairly significant,
[1086.08 → 1089.08] especially as technology evolves. Do you have any thought?
[1089.42 → 1091.28] In a sense, I wish it wasn't called AI ethics.
[1091.58 → 1093.10] Okay, what should it be called?
[1093.32 → 1095.70] Well, so I mean, let's give you an analogy, right?
[1095.70 → 1101.70] So the nuclear engineers who make sure that nuclear power stations don't explode like Chernobyl,
[1102.22 → 1109.94] are they ethicists? Would you say that's a nuclear ethics issue? No, I mean, it's just common sense
[1109.94 → 1114.72] that you don't want your nuclear power station to explode. It's common sense that you want your AI
[1114.72 → 1116.56] systems to remain under human control.
[1116.56 → 1117.16] Sure.
[1117.56 → 1123.66] But at the moment, under the standard model, they won't remain under human control.
[1123.66 → 1128.78] And would you talk us through what that implies when you say it won't? And I'm going to set it up in
[1128.78 → 1135.10] this way and that recognizing, and it's funny how many people I talk to have different perspectives
[1135.10 → 1141.80] from what I think you're about to go. But given the evolution that we've seen over time and the
[1141.80 → 1146.30] rapid evolution we're seeing in deep learning and whatever follows coming up that potential for loss
[1146.30 → 1150.02] of human control, where does that come from? Why is it inevitable in your view?
[1150.02 → 1155.90] I don't want to say inevitable if we persist with AI within the standard model.
[1156.14 → 1156.42] Okay.
[1157.00 → 1163.68] Right? Where we fix an objective. Because when you fix an objective, you're basically telling the system
[1163.68 → 1170.38] whatever course of action optimizes that objective is the correct thing to do.
[1170.38 → 1182.34] And in particular, for example, anything that imperils the success of the objective has to be prevented.
[1182.86 → 1187.56] Well, what might imperil the success of the objective? Well, being switched off.
[1188.24 → 1188.36] Sure.
[1188.78 → 1194.06] So by giving a system a fixed objective, you've now given it an incentive to protect itself
[1194.06 → 1199.92] from any attempt to interfere with the objective, from any attempt to switch it off.
[1200.50 → 1205.32] So as a very typical argument I hear people make, if you kind of go back to like, you know,
[1205.36 → 1211.12] Asimov's three rules for robotics, you know, in the idea that you can just in a non-probabilistic
[1211.12 → 1215.80] way just definitively say, you know, you can't hurt people, that kind of thing, as an underlying
[1215.80 → 1221.48] thing, given the fact that you have this ever-increasing capability in the AI realm,
[1221.48 → 1227.72] would it be fair to say that's not a realistic perspective, that the intelligence that AI would
[1227.72 → 1230.62] fundamentally look to circumvent? Or how do you see that?
[1231.18 → 1237.82] Yeah. So Asimov's laws, as you say, don't take into account the probabilistic perspective. They
[1237.82 → 1242.68] don't allow for uncertainty. But of course, in the real world, there are always risks. So,
[1242.80 → 1246.08] you know, an Asimov self-driving car would simply stay in the garage.
[1246.62 → 1251.14] It would say, I'm sorry, you know, the first law does not allow me to leave the garage,
[1251.14 → 1255.94] because that would expose you to risk of injury or death. So, sorry, we're not going anywhere.
[1256.26 → 1257.74] I love that. That's very funny, actually.
[1258.44 → 1258.88] That's true.
[1259.30 → 1263.88] And if you were out for a walk, it would run around with an umbrella in case a photon from
[1263.88 → 1268.60] the sun, you know, landed on your skin and maybe initiated a little melanoma or something like,
[1268.70 → 1273.12] you know, there's a chance that could happen. So we have to protect it. So, you know, in any kind
[1273.12 → 1278.86] of real world situation, there are trade-offs. But one of the things that Asimov's laws do is they
[1278.86 → 1284.68] make a start on saying what it is that humans want, right? One of the things we don't want to
[1284.68 → 1290.80] be harmed. We don't want to be physically injured. And that's a start because, you know, for example,
[1290.80 → 1295.66] none of the self-driving cars that are out there right now know that people don't want to be
[1295.66 → 1297.10] injured. Understood.
[1297.10 → 1301.70] Right. They have built-in rules that say, well, if there's a pedestrian in front of you, and you're
[1301.70 → 1306.58] going forward, stop. Right. And if there's a if you're lucky, they have another rule that says if
[1306.58 → 1311.00] there's a pedestrian behind you, and you're going backwards, stop. Right. But they don't know why.
[1311.10 → 1315.98] They don't know that if you run into a person, you can injure or kill them. And they don't know
[1315.98 → 1320.28] that the person doesn't want to be injured or killed. And it's that lack of knowledge, actually,
[1320.34 → 1326.14] that makes them very brittle because when they get into situations they haven't been prepared for,
[1326.14 → 1331.72] they haven't the faintest idea what to do because they don't know which course of action is good and
[1331.72 → 1338.04] which is bad. So the solution that the book proposes actually is to say, look, it doesn't
[1338.04 → 1344.12] matter how much the human tells you that they want this, or they don't want that. There's always going
[1344.12 → 1356.12] to be residual uncertainty about other preferences the human may have. So if the human says, I'd like a
[1356.12 → 1363.64] life's mission, right? You know, the robot could say, well, you know, the coffee in this hotel is
[1363.64 → 1369.20] 15 bucks a cup. Are you sure you want a cup of coffee? Right. Because this machine is uncertain
[1369.20 → 1375.08] about your trade-off between coffee and money. Right. If you're miles from the nearest coffee,
[1375.30 → 1380.90] you know, the robot might not be sure. You know, do you want to wait two hours for this coffee? Is it
[1380.90 → 1387.22] okay if I like trundle off across the desert to the nearest Starbucks and come back two hours later
[1387.22 → 1391.42] or two weeks later with a cup of coffee? You know, so it would be reasonable again to ask
[1391.42 → 1396.90] permission. And, you know, if you give it a more important goal, like restoring carbon dioxide
[1396.90 → 1402.60] levels to pre-industrial concentrations, if that was the only objective, well, you know, one very
[1402.60 → 1406.90] straightforward solution is just to get rid of all the people. Understood. Because they are the ones who are
[1406.90 → 1411.34] producing the carbon dioxide. And then you might say, oh, well, I didn't mean that. All right. So
[1411.34 → 1419.08] wish number two, restore the carbon dioxide, but don't kill anybody. And then the system says, fine,
[1419.34 → 1426.40] fine, no problem. We'll just have a multi-decade social media campaign to convince people not to
[1426.40 → 1432.06] have children. And then the human race will gradually die out. And then carbon dioxide levels
[1432.06 → 1437.42] will be restored. And that's great. So what I'm really proposing in the book is actually
[1437.42 → 1443.24] throw away the standard model or only use a standard model in very restricted circumstances.
[1443.70 → 1453.44] But in general, have a new model where the objectives are in the human and the machine knows
[1453.44 → 1458.64] that it doesn't know what they are. Its job is to try to satisfy them, but it knows that it doesn't
[1458.64 → 1464.24] know what they are. And when you design things that way, and you actually solve that problem,
[1464.30 → 1471.34] so you can have an algorithm that for that problem specification decides what the machine
[1471.34 → 1478.92] is going to do, that algorithm produces behaviours that seem to be what we want, namely asking permission.
[1479.10 → 1484.04] Like, you know, is it okay if I turn the oceans into sulphuric acid in order to restore carbon
[1484.04 → 1490.54] dioxide levels? And you say, no, we like those little fishes. Don't burn the oceans into sulphuric acid.
[1491.06 → 1495.34] Right? So we will ask permission. You know, it'll even allow itself to be switched off. So rather
[1495.34 → 1503.04] than try to protect itself and take steps to prevent interference, it actually welcomes interference
[1503.04 → 1508.00] because interference by a human is a way of gaining information.
[1514.06 → 1518.52] What up nerds? I've got some pretty awesome news to share with you. Pluralsight is totally free
[1518.52 → 1523.74] for the entire month of April. I'm not kidding. Seriously, head to pluralsight.com slash change love
[1523.74 → 1528.76] and skill up while you stay at home. For the entire month of April, you'll get access to over 7,000
[1528.76 → 1533.78] courses from experts in software development, security, cloud, and data. There's never been
[1533.78 → 1539.54] a better time to skill up. Head to pluralsight.com slash change love. Again, pluralsight.com slash change love.
[1539.54 → 1562.26] So if you would take us a little bit farther into your, the new model that you're proposing to
[1562.26 → 1568.14] replace the standard model, and maybe along the way, one of the things I was wanting to ask as you were
[1568.14 → 1575.44] discussing that, is if you could do that also in the context of, as we're looking at AI in the deep
[1575.44 → 1581.80] learning context of today, anticipating wherever we may be going in the future, and with the idea
[1581.80 → 1587.74] that people talk about, about AGI, which is artificial general intelligence, which presumably
[1587.74 → 1595.20] would change the nature of what AI is, maybe, and maybe distinguish how your new proposal would work
[1595.20 → 1602.48] kind of in both worlds. I mean, if you were, even today, as we're looking at exceeding human capability
[1602.48 → 1609.38] by, if you have a complex set of tasks, even now we can take the models that we have and have many
[1609.38 → 1615.78] models, each one addressing kind of a narrow scope, and working together, and they can far outperform what
[1615.78 → 1622.18] humans could do in a similar complex task. And with the idea also of having AGI, where we have models that
[1622.18 → 1627.90] are, for lack of a better word, more capable, and themselves maybe eventually aware, I don't know,
[1628.38 → 1634.38] if you could kind of talk about what your proposal looks like in that evolving world, I'd love to know.
[1635.06 → 1640.64] Sure. So first, I should point out that I don't think deep learning evolves into AGI.
[1641.02 → 1641.30] Okay.
[1642.26 → 1647.98] Right? So AGI, artificial general intelligence, is not going to be reached by just having bigger
[1647.98 → 1656.20] deep learning networks and more data. AGI and human intelligence require fundamental capabilities
[1656.20 → 1660.96] that are just not present in deep learning technology as we currently understand it.
[1661.62 → 1670.22] So deep learning systems don't know anything. They can't reason. And they can't accumulate knowledge.
[1670.56 → 1675.32] They can't apply what they learned in one context to solve problems in another context,
[1675.32 → 1680.96] etc., etc., etc. Right? And these are just elementary things that humans do all the time.
[1681.62 → 1685.42] A bit of a stepping stone technology of the moment, in a sense? The deep learning?
[1685.48 → 1690.20] Well, I think deep learning is one of the pieces. But, you know, so is symbolic logic. So is
[1690.20 → 1696.94] parablastic reasoning. So is sequential decision-making techniques, planning, hierarchical reinforcement
[1696.94 → 1703.56] learning, parablastic programming, etc., etc. So there, you know, there are lots of pieces of the puzzle,
[1703.56 → 1709.34] some of which have been lying around for a long time. Deep learning is just the newest, shiniest one.
[1710.04 → 1714.68] So everyone's sort of, ooh, look, you know. But, you know, in the 80s, people were going,
[1714.78 → 1719.16] ooh, look, expert systems, you know. And similar claims are being made, right? That we just,
[1719.46 → 1724.80] you know if you just like scale up the number of rules by a factor of 500, you know, and you had
[1724.80 → 1730.30] like learned people, you know, making quantitative estimates, like, oh, yeah, we would need about
[1730.30 → 1737.92] 500,000 rules to manage a military campaign and stuff like this, like just complete drivel.
[1738.46 → 1744.34] Yeah. And there's a lot of drivel being talked now about deep learning. But okay, so within the
[1744.34 → 1749.62] context of just straightforward supervised learning, let's say for image classification.
[1749.62 → 1757.64] Okay. Right. So how does it work? Well, we have training data. And then we have deep learning,
[1757.80 → 1763.40] which is basically a giant unable circuit with billions of unable connection strengths,
[1763.98 → 1769.62] like little tiny volume controls. And we just tweak all those volume controls in this huge circuit
[1769.62 → 1775.12] until the thing that comes out the other end is the correct classification of an image. So in
[1775.12 → 1780.44] statistical learning, what you do is you, you're supposed to specify the loss function,
[1780.86 → 1787.80] which says if you classify an objective type A as an objective type B, so let's say you classic
[1787.80 → 1796.60] picture of a dog, and you classify as a cat. How bad is that? Right? So almost everybody in this business
[1796.60 → 1802.66] uses what we call a uniform loss function, which means that they say every error is equally bad,
[1802.66 → 1808.20] because that's how the competitions work. They penalize you for the number of errors you make,
[1808.30 → 1815.90] not how bad the errors are. Right? So, you know, for example, in ImageNet, there are two categories of
[1815.90 → 1820.40] dog one, well, there's a hundred and something categories, but two of them are the Norfolk Terrier
[1820.40 → 1825.42] and the Norwich Terrier. Right? And these are practically identical. In fact, they weren't even
[1825.42 → 1831.56] recognized as separate breeds of dog until 1960 something. You know, and there's like a slight difference in the
[1831.56 → 1836.42] shape of the ear. And it's like, okay, who cares? I'm sure the Norfolk Terriers are not going to be
[1836.42 → 1841.06] that upset if you call them Norwich Terriers. You know, Norwich is in Norfolk anyway.
[1841.40 → 1842.70] They'll lick your face either way.
[1843.26 → 1850.78] Right. So clearly that kind of error is relatively cheap. Whereas classifying a human as a gorilla,
[1851.34 → 1856.82] as Google found out, is really expensive, like in the billions of dollars of, you know,
[1856.82 → 1863.86] trashing your goodwill of your corporation and its global reputation for being fair and idealistic and
[1863.86 → 1868.04] all the rest of it. Right. You know, it was, yeah, I'm sure it was sort of an innocent error coming from
[1868.04 → 1873.38] just using a uniform loss function. Sure. And, but if they had thought about it, they would have said,
[1873.46 → 1879.06] oh, of course our loss function is not uniform. Oh, then what is it? Oh, I don't know. We haven't
[1879.06 → 1884.22] thought about it, and we're not sure. And in fact, you know, if you've got typically an ImageNet,
[1884.22 → 1889.12] there's like 20 something thousand different categories of object. So your loss function is
[1889.12 → 1895.10] a matrix with 400 and odd million entries. And do you know what they are? No, no one knows what
[1895.10 → 1901.52] they are. So you have an uncertain objective. You don't know what the objective is you're supposed
[1901.52 → 1907.56] to be optimizing. And when you formulate the problem that way, right, first, you'd have to say,
[1907.66 → 1914.16] okay, well, how do we specify a probability distribution over these 400 million entry matrices?
[1914.22 → 1920.30] These giant tables. And now I go to say, okay, what's the probability of each possible table
[1920.30 → 1927.36] of 400 million numbers? Well, that probability distribution is itself a massively complex object
[1927.36 → 1937.34] to specify. And no one has ever figured out even how to write it down, how to structure that
[1937.34 → 1942.82] probability distribution, because clearly it has lots of structure, right? The costs of misclassifying
[1942.82 → 1949.78] each breed of dog as a cat is probably about the same. I think all dogs are equally upset to be
[1949.78 → 1956.76] called cats. But if, you know, if you classify a bus as an insect, maybe that's a more embarrassing
[1956.76 → 1962.66] mistake to make and so on. So you can imagine that there's lots of structure in this matrix. And,
[1962.90 → 1968.80] you know, the structure partly reflects a taxonomic hierarchy of objects and how we arrange them
[1968.80 → 1975.52] into categories. So you could do a whole PhD thesis just on that part of the problem. And now there's
[1975.52 → 1980.40] also, well, what does the algorithm look like? Right? Well, if it doesn't know the loss function,
[1980.40 → 1987.02] and it has the opportunity to find out more, for example, by asking the user, you know, is it worse
[1987.02 → 1992.64] to call a cat a dog or to call an apple an orange? And sometimes the algorithm would say,
[1992.64 → 1997.88] yeah, I'm not going to classify that image. Right? That's too dangerous. So I'm just not going to
[1997.88 → 2002.44] make a guess as to what it is. So you immediately see that just the nature of supervised learning
[2002.44 → 2007.76] would change considerably. Yes. If you allow for uncertainty about the underlying objective.
[2008.28 → 2015.78] And then with AGI, we don't yet know exactly how to build AGI. I mean, there are a bunch of unsolved
[2015.78 → 2023.26] major conceptual problems that we have to figure out. But I think the basic answer is that if you
[2023.26 → 2030.60] formulate AGI within this new model, the key property of the new model is that the better the
[2030.60 → 2038.00] AI solves the problem, the better the outcome is for human beings. Because it means that the AI system
[2038.00 → 2044.14] does a better job of finding out what it is you want, and does a better job of achieving it.
[2044.14 → 2050.98] And so you were talking a moment ago about kind of applying control in the new model that you're
[2050.98 → 2055.98] proposing. As we move into AGI, would you pick that train of thought right up where you left it there?
[2056.44 → 2064.34] Yes. So with AGI, if we formulate it in the new model, the key property is that the smarter the AI,
[2064.34 → 2072.14] the better the outcome for humans. Because the AI system will be able to better interpret our behaviour
[2072.14 → 2077.72] as evidence of our underlying preferences. So this is the nature of information flow
[2077.72 → 2082.14] between the human and the machine about what the human objectives and preferences are,
[2082.44 → 2087.68] is that everything the human does reveals evidence for our underlying preferences.
[2088.38 → 2093.86] So the AI system observing us, observing our whole history, observing everything we've ever written,
[2093.86 → 2101.18] is able to infer from that something about what we want as individuals, as a species, and so on.
[2101.70 → 2106.42] And so the better the AI system, the better job it'll do of that, and the better it'll be able to
[2106.42 → 2107.42] achieve those objectives.
[2107.98 → 2111.28] When you say that, just to clarify, it sounds like you're going into unsupervised learning,
[2111.28 → 2115.60] where it just has kind of the wealth of human knowledge and what humans have done. Or are you
[2115.60 → 2121.56] strictly leaving it for, in this new approach, are you leaving it for the algorithm that you're
[2121.56 → 2128.16] training to figure that out? Are you specifying it as the practitioner? Do you see this as kind of,
[2128.42 → 2133.48] at some point, maybe leaving kind of today's deep learning behind and taking a different
[2133.48 → 2137.28] approach mathematically? How does that look going into the future if everyone adopts this?
[2138.00 → 2143.36] Well, yeah. So you often see this claim that there's supervised learning, unsupervised learning.
[2144.34 → 2149.96] And then, well, that, I mean, logically, if those were correct, then supervised and unsupervised,
[2149.96 → 2153.30] that constitutes a complete coverage of all learning, right?
[2153.34 → 2153.58] Right.
[2153.86 → 2157.20] You know, A and not A. But then they say, oh, and there's reinforcement learning as well.
[2157.24 → 2162.18] But actually, there's not. There are other kinds of learning, too. And this is related to something
[2162.18 → 2167.68] we call inverse reinforcement learning. And inverse reinforcement learning is basically,
[2168.10 → 2171.70] well, so let me first say what reinforcement learning is, right? Reinforcement learning is
[2171.70 → 2180.76] the human specifies the reward to the machine. And then the machine learns how to optimally
[2180.76 → 2187.46] produce reward, right? So the machine says, okay, this is, I'm going to give you one point when you
[2187.46 → 2191.14] win the game, and I'm going to give you zero when you lose. And then the machine learns to get one
[2191.14 → 2196.78] point more often than not. So inverse reinforcement learning is the other way around. The machine is
[2196.78 → 2202.94] observing, let's say, the human and trying to figure out what is the reward function that this human is
[2202.94 → 2213.20] optimizing, right? And we came up with it, actually, when I was collaborating with some biologists. And we
[2213.20 → 2220.02] were trying to figure out how could we apply reinforcement learning to understand animal locomotion. So, you
[2220.02 → 2226.38] know, cockroaches and flies and other, you know, creepy crawlies and so on. And it struck me that actually, we
[2226.38 → 2232.14] can't apply reinforcement learning to sort of simulate animal, you know, to create a simulated
[2232.14 → 2237.90] insect or whatever, because we don't know what the reward function is. Right. Right. So then I said,
[2237.94 → 2244.00] oh, well, why don't we watch them walking and figure out what reward function are they optimizing,
[2244.00 → 2249.36] you know, with their particular choice of how to loco mote, right? Because I mean, I don't know if you've
[2249.36 → 2255.14] ever seen the Monty Python silly walk sketch. Yes, I have. If your listeners may want to check that out on the
[2255.14 → 2260.82] web, right? So John Cleese demonstrates that there are many other ways you could walk besides the usual
[2260.82 → 2267.30] one, right? So we choose the usual way of walking, because it does something good for us, whether it's
[2267.30 → 2272.76] energy efficient or stable, you know, it avoids falling over, whatever it might be, it's optimizing
[2272.76 → 2278.08] something. And so the idea of inverse reinforcement learning is observed the behaviour and figure out what
[2278.08 → 2285.22] is being optimized by this behaviour. Okay. And so this, this approach, the new model is a sort of
[2285.22 → 2292.18] generalization of that idea, because it's generalized in the sense that the human is not just being
[2292.18 → 2297.90] passively observed, behave, you know, doing whatever human thing, but the human is sort of an active
[2297.90 → 2302.38] participant. For example, you know, if they, if the human solves their half of this problem,
[2302.38 → 2308.82] they will actively teach the robot about their preferences, right? Including saying things like,
[2308.94 → 2315.00] I would like a cup of coffee, right? That's conveying preference information to the robot. It's not
[2315.00 → 2321.28] an order. It's sort of just, you know, factual evidence about my state of mind, and the robot can
[2321.28 → 2328.88] interpret it as it wishes. So when you, when you solve this, this kind of problem, it's what the
[2328.88 → 2333.62] economists call a game, which just means a decision problem with more than one decision-making entity.
[2334.00 → 2337.70] So you can imagine one human and one machine, or lots of humans, lots of machines.
[2338.28 → 2344.60] So you can solve that problem mathematically. And then you just look at the behaviours that the
[2344.60 → 2349.86] machine and the human engage in when they solve this problem. And, you know, indeed the human teaches
[2349.86 → 2356.26] the machine and the machine does things, it asks permission, it allows itself to be switched off and so on.
[2356.26 → 2363.58] So you get very different behaviours than you do in, in the standard model of AI. And so I think I'm
[2363.58 → 2368.72] reasonably optimistic that in fact, it shouldn't matter how intelligent the AI system is, things will
[2368.72 → 2375.56] still go well. And in the old model, the more intelligent the machine, the worse the outcome for
[2375.56 → 2382.60] people, because the machine would find some way of messing with the world to achieve the objective
[2382.60 → 2386.30] that you said, and mess with the things you forgot to mention that you care about.
[2387.76 → 2393.18] So I'm kind of curious, as you take this, and you're looking, we've hit so many different areas.
[2393.28 → 2398.58] And so I'm, I'm trying to tie it together. You look into the future at this point, having come as far
[2398.58 → 2403.92] through this field as it's evolved and changed over the years. Where do you see it going, especially
[2403.92 → 2410.06] with control in mind? And, and, you know, as you've talked about how the current standard model
[2410.06 → 2416.06] can lead us awry, then if you are a practitioner, and you're out in industry, and you're trying to do
[2416.06 → 2423.72] the things that your organization wants you to do, how do you apply your new model? And as you look
[2423.72 → 2429.70] out, what do you think we're going to be doing in terms of what types of models, what is AI kind of
[2429.70 → 2434.94] evolving into if you're looking out five years or 10 years, and we're learning these lessons that
[2434.94 → 2440.04] you're teaching us in this capacity? What is the near mid and a little bit farther out look to you
[2440.04 → 2446.64] at this point? Interesting. So first, there's going to be a little bit of pushing and shoving,
[2447.08 → 2453.68] right? I would imagine. The AI community that's grown up with the standard model and learned it from
[2453.68 → 2460.54] the textbook is going to keep pushing ahead with their, you know, solving the technical problems
[2460.54 → 2465.82] that they're, that they're solving within the standard model. And, and they have to be dragged,
[2465.98 → 2470.84] kicking and screaming into this new way of doing things. So, so partly it means we, you know,
[2470.86 → 2474.70] are my research group, there are, you know, maybe a dozen other research groups around the world
[2474.70 → 2480.36] working in this new framework. Now we have to provide the technical solutions, right? We have to
[2480.36 → 2487.84] provide the new algorithms that behave according to the, the, the different principles. And I think
[2487.84 → 2494.32] we can do that. If we can do that in practical settings, whether it's, you know, recommendation
[2494.32 → 2500.48] systems, content selection for social media, intelligent personal assistance, then I think
[2500.48 → 2506.00] that will have a significant effect. People will say, oh, now I get it. In fact, no, they won't say,
[2506.00 → 2511.12] now I get it. They'll say, oh, I always thought that way. Of course. Right. So there were, you know,
[2511.16 → 2516.08] there won't be a sort of, you know, a moment of, of capitulation. There'll be a just a gradual
[2516.08 → 2521.28] realization that of course, this is what they've always thought. And it makes sense, right?
[2521.60 → 2526.50] It does make sense. Do you think that as they adopt this, as I'm thinking about what you're saying
[2526.50 → 2532.50] here, and, and you've already mentioned that the poorly named idea of AI ethics, you know,
[2532.50 → 2537.12] in terms of how do we prevent those, how does that come together? I mean, cause there's the
[2537.12 → 2541.94] algorithmic side, there's the new algorithms and, you know, where you are going out into the future
[2541.94 → 2546.06] and you're implementing inverse reinforcement learning and, and, and it's working for you
[2546.06 → 2553.82] technically. And you're also trying to say, we want to ensure that the outcomes are beneficial,
[2553.82 → 2559.02] uh, and certainly to the human involved. How does all that come together? Cause right now,
[2559.02 → 2563.96] you know, as I look at people, there are people that are doing kind of the, the outcome,
[2564.10 → 2568.66] the ethical concern there. There are people that are strictly algorithmically focused in terms of
[2568.66 → 2574.40] solving problems. And yet, if I'm understanding you correctly, you need to be able to, to fuse all
[2574.40 → 2579.34] these together. It sounds like so that that works. Yeah. Because I think the last thing you want,
[2579.34 → 2584.84] and you've probably experienced this yourself is that AI ethics, people leaning over the shoulder of
[2584.84 → 2589.26] the AI practitioners and wagging their finger and saying, no, no, you're a bad person, right?
[2589.46 → 2595.64] It doesn't work. So what we have to do actually is to get people to understand that this is just
[2595.64 → 2603.62] how you do AI, right? You know, when, when civil engineers design bridges, there's not a bunch of
[2603.62 → 2607.64] bridge designers and then a bunch of ethicists saying, oh, by the way, you have to make sure it
[2607.64 → 2613.54] doesn't fall over. Right. It's just, of course it, of course it's, it's not supposed to fall over.
[2613.60 → 2619.38] It wouldn't be a bridge if it just fell over. Right. You know, and similarly, you know, nuclear
[2619.38 → 2624.36] engineers who design nuclear power stations, there isn't, you know, another discipline of people who
[2624.36 → 2629.72] care about safety and then the nuclear engineers don't care about safety, and they just want to
[2629.72 → 2632.90] generate lots of energy, right? It doesn't work that way. If we want to generate energy, we can just
[2632.90 → 2638.38] set off lots of bombs and that's, that's cheap and cheerful, gets past all this red tape and all
[2638.38 → 2644.42] that crap. So, so I think there should be a strong incentive to just design systems this way because
[2644.42 → 2650.22] they won't fall down. Right. The, you know, the example I use in a lot of talks is that, you know,
[2650.22 → 2657.30] your domestic robot, if it's designed this way, won't cook the cat for dinner because there is,
[2657.30 → 2660.98] you know, because the fridge is empty because it would say, well, I mean, it might realize, yeah,
[2660.98 → 2667.96] cooking the cat for dinner solves the problem of lack of food, but I'm uncertain about perhaps the
[2667.96 → 2672.92] cat has sentimental value, and so I shouldn't cook it. Right. I should, I should ask permission before
[2672.92 → 2679.94] I cook it. Right. So you get better behaviour out of your AI systems. And so they'll be economically
[2679.94 → 2686.18] more valuable. They'll incur far less in the way of liability insurance and so on. So there's that.
[2686.18 → 2693.44] But I also think that we, at some point we'll need regulation because there will always be just
[2693.44 → 2700.66] as there is with malware, there's a tended, you know, temptation to just bypass safety and all
[2700.66 → 2709.38] the rest just in terms of immediate grasping. And so as AI systems become more and more capable and
[2709.38 → 2715.52] potentially powerful, they need to be regulated more and more strictly just as we do with nuclear power
[2715.52 → 2719.90] stations. Sure. And I would imagine that's not just at a national level, but there'll have to be a body
[2719.90 → 2724.72] of international law because you have different, you know, parts of the world, different countries
[2724.72 → 2727.82] have different values that they're bringing to play. And some are going to care more about these
[2727.82 → 2733.22] kinds of outcomes than others. I guess I wanted to finish up with, you know, you have all these
[2733.22 → 2739.08] students looking to you to, and they're coming in, and they are starting their careers out in this field.
[2739.08 → 2744.82] You have people like me who are a little bit older, and we are, we are trying to constantly retool and
[2744.82 → 2750.16] stay up with the field. And you've really, you've kind of shifted, you know, in this conversation that
[2750.16 → 2754.28] we've just had, you've really shifted how I'm looking at the future and the things that need.
[2754.72 → 2761.58] How does a practitioner or a student that's about to be a practitioner kind of tool themselves today
[2761.58 → 2766.72] beyond just the current state of deep learning? Because that's, you know, where all the focus is right now.
[2766.72 → 2771.88] It's all about, you know, TensorFlow or, you know, pick whatever tool you want to use. And we're,
[2772.14 → 2777.40] we're building neural networks or adjacent technologies. And that's where all the education
[2777.40 → 2782.20] is really focusing, you know, that's broadly available out there on the internet and by service
[2782.20 → 2787.72] providers and others. How should someone like myself or a student coming in the field be thinking
[2787.72 → 2793.28] about this? And how should we focus on educating ourselves for the future to align ourselves with this
[2793.28 → 2796.40] vision that you just set out? Obviously there's your book, there's Human Compatible.
[2796.72 → 2800.22] I don't know if it's out yet, the fourth edition to your textbook?
[2800.54 → 2805.30] Yeah. So the fourth edition is out next week. We finished it a few weeks ago, and I think it'll
[2805.30 → 2806.66] be in the stores in a week's time.
[2807.00 → 2809.32] Perfect timing as they hear this. I can go out and buy it.
[2809.62 → 2813.82] Yeah. So, you know, it's an unfortunate situation because we basically, we've put the technical
[2813.82 → 2819.34] content from Human Compatible into the new edition of the textbook. You know, so the first two chapters
[2819.34 → 2822.32] saying, okay, well, there's this old way of thinking about AI and now there's this new way,
[2822.32 → 2828.86] but we don't have all the chapters in the middle telling you how to do the new way. So we're going
[2828.86 → 2832.94] to tell you how to do the old way, but keep in mind that you really should be thinking about the
[2832.94 → 2834.80] new way. So that'll have to be the fifth edition.
[2835.18 → 2839.76] An awkward timing. Yeah. So the fifth edition will hopefully have more stuff, but the things to keep
[2839.76 → 2846.76] in mind are, first, is the objective that you're designing your system to optimize. And I think,
[2846.76 → 2851.36] you know, as I mentioned with the example of image classification and the, you know, classifying
[2851.36 → 2858.92] the person as a gorilla, most people are not even thinking about that. The objective there is typically
[2858.92 → 2864.48] implicit. You know, when you run TensorFlow, if you don't put in the loss function, then you're putting
[2864.48 → 2869.52] in a uniform loss function. And if you put in a uniform loss function, you're saying that classifying
[2869.52 → 2874.90] human and gorilla is just as bad as classifying one kind of terrier as another. Right. And that's not
[2874.90 → 2881.66] true. So don't do it. Right. The second thing to think about is what is the scope of action
[2881.66 → 2891.12] of your system? So if your system could learn any function that strings together actions that it
[2891.12 → 2898.60] carries out, you know, what is the sort of transitive closure? What's the full set of states that your
[2898.60 → 2904.88] system could take the world into when it runs in the real world? Right. And if, for example,
[2904.90 → 2911.64] you're just writing a Go program, you know, and it's only moving pieces on a simulated board,
[2911.66 → 2918.06] you know, within the memory of the computer and then displaying, it's relatively safe.
[2918.66 → 2924.48] All right. Because no matter what sequence of moves it does, it's still only changing what
[2924.48 → 2931.22] appears on the screen when someone's playing Go with it. Now, theoretically, it's not perfectly safe
[2931.22 → 2940.06] because, you know, just as we have learned the origins of our own universe and the physics of
[2940.06 → 2946.50] the world in which our bodies run, a sufficiently intelligent Go program could actually do the same
[2946.50 → 2952.96] thing and then figure out that there must be other entities outside its computer and try to
[2952.96 → 2958.44] communicate with them through the Go board and convince them to give it more CPU power or whatever.
[2958.44 → 2964.00] Right. So, so it's not hermetically sealed even then. But if your algorithm is in contact, direct
[2964.00 → 2971.76] contact with humans, right, then, you know, here's one good way to remember this. Hitler did it with words.
[2972.76 → 2978.90] Right. Hitler was not a thousand-foot tall giant robot with laser beam sweeping destruction everywhere.
[2979.10 → 2981.50] It was just a little guy who spoke.
[2981.50 → 2983.44] Yeah. That's a great point.
[2983.78 → 2989.38] And so if your AI system is in direct contact with humans, it has far more power than Hitler
[2989.38 → 2994.72] already because it can speak to billions of people all the time.
[2995.18 → 2998.42] That may be the most terrifying thing I've ever heard a person say right there.
[2998.70 → 3000.62] That's a perspective right there.
[3001.34 → 3006.64] Yeah. If you think, you know, what is the closure, right? What is the transitive closure of all possibles
[3006.64 → 3009.32] actions that system could do? There's really no limit to it.
[3009.58 → 3009.78] Yes.
[3009.82 → 3016.16] Right. It could affect the world in any way. So those kinds of systems, I think, should absolutely
[3016.16 → 3023.60] be carefully regulated. And I think, for example, we talked earlier about how social media algorithms
[3023.60 → 3030.36] work. I think you can distinguish between reinforcement learning algorithms in that context and supervised
[3030.36 → 3034.72] learning algorithms. So a supervised learning algorithm, roughly speaking, will learn what people
[3034.72 → 3040.00] want. Whereas a reinforcement learning app will learn to manipulate people to change what they want
[3040.00 → 3046.66] so that the algorithm can make more money off them. And so, you know, I really think that algorithms
[3046.66 → 3053.30] that are facing the public in that way need to be regulated, not in exactly the same way,
[3053.36 → 3059.36] but in some way analogous to the way we regulate pharmaceuticals. We don't just get to spit out,
[3059.46 → 3063.54] you know, new pharmaceuticals to billions of people whenever we feel like it.
[3063.54 → 3068.88] Right. They have to be carefully tested on, you know, on animals and then on, you know,
[3068.92 → 3075.26] control groups of humans. And because if it goes wrong, it's terrible. And the same as we've
[3075.26 → 3078.30] learned is true with, with these social media algorithms.
[3079.00 → 3084.78] Well, I just wanted to say thank you so much for coming on the show. This is truly been one of the
[3084.78 → 3090.28] most fascinating conversations I've ever had. I think at this point, I will be recommending that
[3090.28 → 3096.64] people read human compatible pretty much everywhere I go. Well, thank you. You point out the danger of
[3096.64 → 3101.70] as we grow here, if we don't start taking that into account. So thank you so much for coming on the
[3101.70 → 3105.82] show. You've really blown my mind. So I don't normally finish the show stuttering like this.
[3105.82 → 3109.12] So thank you very much. Thank you, Chris. It's nice talking to you.
[3109.12 → 3118.80] Thank you for listening to this episode of Practical AI. More like this at changelog.com
[3118.80 → 3124.94] slash practical AI. There you'll find our latest as well as lists of our most popular episodes and
[3124.94 → 3129.30] the ones we recommend. If this show has helped you on your AI journey, please leave us a five-star
[3129.30 → 3135.00] review on Apple Podcasts, part us on Spotify, star us on Overcast and tell a friend what they're
[3135.00 → 3139.74] missing out on. Practical AI is hosted by Daniel Whiten ack and Chris Benson. It's produced by me,
[3139.84 → 3143.10] Jared Santo. And our music is brought to you by the Beat Freak, Break master Cylinder.
[3143.60 → 3147.48] We have awesome sponsors. Please support them. They support us. Thanks again to Vastly,
[3147.76 → 3151.24] Linde, and Rollbar. That's all for now. We'll talk to you next time.
[3165.00 → 3166.00] Bye.
[3166.04 → 3168.98] Bye.
