[0.00 → 5.10] The biggest unsolved problem really in mapping for all levels of fidelity is change management.
[5.34 → 14.62] When things change, it's still really the old methods of map creation or map maintenance are just too slow or expensive for this to work, especially for machine first uses.
[14.62 → 23.34] So that's what our technology and our focus has been on, either for our own base maps or even for someone else's, some other mapping company's map.
[23.54 → 29.86] We can modularize our change management technology, which uses camera based crowdsourcing to do that really efficiently at scale.
[30.00 → 35.22] Big thanks to our partners, Linde, Vastly and Launch Darkly.
[35.44 → 40.16] We love Linde. They keep it fast and simple. Check them out at linode.com slash changelog.
[40.16 → 46.34] Our bandwidth is provided by Vastly. Learn more at Fastly.com and get your feature flags powered by Launch Darkly.
[46.62 → 48.34] Get a demo at LaunchDarkly.com.
[51.28 → 53.80] This episode is brought to you by our friends at O'Reilly.
[54.14 → 56.78] Many of you know O'Reilly for their animal tech books and their conferences,
[56.78 → 60.32] but you may not know they have an online learning platform as well.
[60.70 → 65.14] The platform has all their books, all their videos and all their conference talks.
[65.50 → 69.68] Plus, you can learn by doing with live online training courses and virtual conferences,
[70.18 → 76.26] certification practice exams and interactive sandboxes and scenarios to practice coding alongside what you're learning.
[76.26 → 85.92] They cover a ton of technology topics, machine learning, AI, programming languages, DevOps, data science, cloud, containers, security,
[86.42 → 90.20] and even soft skills like business management and presentation skills.
[90.32 → 92.10] You name it, it is all in there.
[92.42 → 95.68] If you need to keep your team or yourself up to speed on their tech skills,
[95.76 → 97.58] then check out O'Reilly's online learning platform.
[98.12 → 101.68] Learn more and keep your team skills sharp at O'Reilly.com slash changelog.
[101.68 → 104.08] Again, O'Reilly.com slash changelog.
[112.88 → 119.96] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[120.32 → 124.36] This is where conversations around AI, machine learning, and data science happen.
[124.74 → 129.42] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[129.42 → 132.50] And follow us on Twitter. We're at Practical AI FM.
[139.22 → 142.00] Welcome to another episode of Practical AI.
[142.34 → 143.96] This is Daniel Whiten ack.
[144.12 → 147.18] I am a data scientist with SIL International,
[147.52 → 150.18] and I'm joined as always by my co-host, Chris Benson,
[150.42 → 154.28] who is a principal emerging technology strategist at Lockheed Martin.
[154.60 → 155.46] How are you doing, Chris?
[155.74 → 157.66] I am doing very well. How's it going today, Daniel?
[157.98 → 158.86] It's going great.
[158.86 → 160.42] It's been a podcasting day.
[160.52 → 163.52] Actually, I don't know if you saw, but right before this one,
[163.60 → 167.66] I recorded with the changelog, who is our sort of sister podcast.
[168.02 → 173.38] The changelog podcast is all about software engineering and open source and other things.
[173.38 → 174.94] They've been going for a long time.
[175.10 → 181.60] And the creator of Elixir was on there talking about their new numerical Elixir library
[181.60 → 187.96] and Axon, which is a neural network library for Elixir, which is really cool.
[188.16 → 189.42] I really enjoyed the conversation.
[189.64 → 190.96] I don't know anything about Elixir.
[191.06 → 192.04] I don't know about you, Chris.
[192.04 → 198.56] I used to follow it a lot since I have not been doing as much focus strictly on programming language as I have it.
[198.56 → 200.08] But I know it's a really cool language.
[200.08 → 204.08] I know Jose, the creator, is a pretty talented person.
[204.30 → 205.06] Yeah, for sure.
[205.26 → 206.76] So I'm looking forward to it.
[206.96 → 211.20] Now that he's doing these data science libraries, I'll have to dive into it.
[211.22 → 213.56] So I'm going to listen to your episode and see what he has there.
[213.70 → 214.62] I'm excited about it.
[214.62 → 216.00] It's really cool and impressive.
[216.22 → 220.40] They released one week, they released the numerical library for Elixir.
[220.52 → 224.20] The next week, or seemingly, they released the neural network library.
[224.38 → 229.44] And then not long after, they released Notebooks, their own version of Notebooks.
[229.64 → 230.42] So it's pretty cool.
[230.70 → 230.86] Definitely.
[230.94 → 231.66] Watch out, Python.
[231.78 → 232.02] Watch out.
[232.02 → 234.36] Watch out, Python, because Elixir is right on your tail there.
[234.36 → 240.24] One of the features listed on their notebook library was sequential execution,
[240.24 → 245.92] which for anyone that works in Notebooks and struggles with state, that's pretty cool.
[246.26 → 248.38] Anyway, I was pretty excited to do that.
[248.46 → 252.80] And so I've already had a good conversation about all sorts of AI things today.
[252.80 → 261.20] But I'm really excited to hear more about some things related to autonomous driving and also mapping.
[261.64 → 267.18] I know we've talked about before, but I think talking about the specific mapping side of that
[267.18 → 269.22] and some of the data along with that,
[269.22 → 275.30] and also the human sort of machine interface that goes along that is fascinating.
[275.52 → 280.22] And that's what we're going to talk about today with RO Gupta, who is CEO of Camera.
[280.46 → 280.88] Welcome, RO.
[281.24 → 281.68] Hey, guys.
[281.72 → 282.30] Thanks for having me on.
[282.52 → 282.80] Yeah.
[283.32 → 287.64] Before we get into all that, could you just give us a little bit about yourself and your background?
[288.16 → 288.44] Sure.
[288.80 → 292.62] I co-founder, CEO of a company called Camera.
[292.86 → 294.42] We've been around for about six years.
[294.42 → 300.92] Before that, I was at a different startup in sort of the, you know, web 2.0 type phase of the Internet.
[301.58 → 305.60] And before that, I've also been with bigger companies like Disney.
[305.60 → 320.20] But really, my kind of academic grounding and what we do at Camera started back in the 90s when I was an undergraduate in an operations research program at Princeton and got exposed to the early forms of everything we do now.
[320.20 → 326.28] So I actually designed my first autonomous mobility system in 1998, I think.
[326.74 → 327.36] Very theoretical.
[328.26 → 335.48] You know, early forms of ML, computer vision, the non-deep learning kind of computer vision, the old school.
[336.02 → 340.72] Neural nets, everyone, you know, all the faculty thought they were gimmicks, but they just kind of had to tell us about them.
[340.92 → 341.66] Little did they know.
[341.90 → 342.10] Yeah.
[342.10 → 345.50] Well, it took about, yeah, 15 years for it to get real.
[345.78 → 353.44] A lot of people saw cool vision, but it definitely, at that time, I get what you're saying is it was a neat toy for sure.
[353.74 → 353.92] Yeah.
[354.16 → 356.92] So that's a little bit about my kind of background.
[357.08 → 361.80] And then I was, I mean, going back farther, born in India, moved to the U.S. when I was young.
[361.80 → 370.06] But as we can talk about, I think spending time in developing countries also definitely has influenced how we see infrastructure.
[370.52 → 375.64] Infrastructure is a hot word right now, but particularly roads and digitizing roads, which is what we do.
[375.92 → 382.54] I would love to hear about that, you know, at whatever point you want to dive into it and just kind of understanding what kind of perspective that gives you.
[382.54 → 382.82] Sure.
[382.96 → 395.08] As well as what you just mentioned in terms of, you know, getting started back in the last winter, you know, for AI, you know, before neural networks evolved back out into the field of deep learning as it is today.
[395.22 → 403.06] And having gotten into autonomy at that point, I'm pretty interested in how that's also shaped how you approach the deep learning side of it.
[403.06 → 403.38] Sure.
[403.38 → 411.94] Sure. I'll say this for me is a tool as opposed to sort of, you know, a means to an end as opposed to an end in terms of my career.
[412.38 → 413.34] It's fascinating.
[413.52 → 422.50] And as you noted, not only are we knee-deep in it in our current jobs, but was exposed to it at a pretty impressionable time, you know, in my development.
[422.50 → 433.26] But for me, actually, I think what has been kind of, you know, the hardwired into me in terms of from a very young age and again, growing up, you know, I was born in Kolkata.
[433.38 → 436.16] India, we used to call Kolkata, India when I was there.
[436.72 → 440.86] One of the densest, chaotic urban settings you can imagine.
[440.98 → 443.16] When you think, you know, I live in New York now.
[443.34 → 444.90] We think that's pretty dense and chaotic.
[445.06 → 447.22] It's nothing like a developing country's big city.
[447.30 → 447.44] Right.
[447.74 → 453.68] So I think when you grow up in an environment like that, I mean, I got to think subconsciously and well, not even subconsciously.
[453.72 → 462.30] I think even consciously, I realized this later in life when I was older and also spent some time in some developing countries like in Africa, for example, Mozambique with some NGO work I did.
[462.30 → 471.94] You really don't take infrastructure, specifically mobility infrastructure for granted, because it is such an at the forefront of everyday life.
[472.14 → 475.78] Like you have to take into account to get somewhere much more than you would.
[476.00 → 479.58] You know, like there are many cases where there isn't even a real drivable road, you know.
[479.58 → 483.54] So I think that probably had a big impact on me.
[483.62 → 496.10] And for me, when I say AI is a means to end, for me, the end has always, I think what's always been interesting to me is, you know, I see roads as sort of the circulatory system of the planet.
[496.34 → 497.48] You know, the IRL version.
[497.74 → 497.94] Right.
[497.94 → 505.30] It's just it is just how things move around, how the nutrients get to us, whether it's, you know, to our house from an Amazon delivery or whatever.
[505.58 → 509.74] And I've seen also when what happens when there are clots all over the place.
[509.74 → 510.28] It sucks.
[510.46 → 512.56] And it's its just bad for everything.
[512.56 → 520.94] And so I think I'm not going to pretend like when I was four years old, and I was, you know, moving from Calcutta to the United States, I all of a sudden had some epiphany.
[521.04 → 533.46] But I think like that hard-wiring got me very interested in the concept of like basically like packetizing, you know, roads, like the way, you know, that our digital lives are and the Internet is, you know.
[533.54 → 536.52] And so, so first, before you packetize, you got to digitize.
[536.68 → 540.48] And that's exactly what we in our industry and Camera is doing.
[540.48 → 541.86] So I'll kind of pause there.
[541.90 → 546.84] But I think I'd actually not really thought about it in that way until you just asked me that.
[546.98 → 549.82] But I mean, I sort of thought about it is just disparately like that.
[549.84 → 551.86] But I think I'm not going to stick with that answer.
[552.48 → 553.14] That's a good answer.
[553.22 → 554.02] It's an interesting answer.
[554.10 → 556.14] This is a little bit of a shrink session, actually.
[556.62 → 557.44] No, that's fine.
[557.56 → 558.44] I'm here.
[558.50 → 559.50] I'll send you my bill at the end.
[559.58 → 559.88] Yeah.
[561.64 → 566.84] I'm fascinated by the way you describe that and in your thought process around roads.
[566.84 → 574.42] I think when there is also as we maybe in kind of cities in the U.S.
[574.42 → 584.40] have a certain perception of roads and our expectations around how they operate, which is, of course, very different from like if you go to the developing world.
[584.40 → 594.02] I think also there's varying degrees of perceptions around maps and what we expect those to be and contain and all of those.
[594.50 → 608.90] So maybe you could just talk for a second about in terms of the autonomous driving world, what sorts of maps are involved in the development of autonomous driving technologies?
[608.90 → 621.42] Maybe some of those are different from the sort of maps that we might think of right away in terms of, hey, I look on my phone and here's a route from my house to the restaurant down this road and that sort of thing.
[621.68 → 622.12] Yeah, sure.
[622.34 → 630.10] I think it's probably good to abstract that a little bit initially and then kind of speak a little bit more specifically to maps, both for machines and humans.
[630.10 → 640.88] But for machines, for autonomy, you know, basically for the autonomous driving use case, which is the vertical that we really started focusing on when we came out of stealth a few years ago.
[641.18 → 642.80] We serve other use cases as well.
[642.92 → 646.06] But let's just start with that since this is an AI podcast.
[646.06 → 655.80] For those of your listeners who are, you know, Bayesian or Bayes theorem fans, it's really best to start off with, you know, that maps are priors, basically, right?
[655.92 → 666.18] And so that's what basically we're solving a, you know, we were talking about my past and when I was an undergrad in the 90s, you know, basically it's just statistics, you know, and probability.
[666.18 → 671.24] And then we had to invent more and more impressive terms for all this stuff, ML and deep learning, blah, blah, blah.
[671.24 → 676.70] But that's basically, you know, it all, I mean, I was taught Bayes theorem in the 90s and that's what maps are.
[676.78 → 679.06] It's priors for Bayesian reasoning.
[679.44 → 680.80] And that includes a robot car.
[681.14 → 685.28] And so a starting point is, okay, like what is the role of maps?
[685.40 → 688.38] It has more actual utility than that, actually.
[688.38 → 698.02] And many people feel like the role of it as a prior in the pure sense may actually probably won't ever go away totally, but may be less of the emphasis.
[698.02 → 704.22] And whereas more of the value of maps being in kind of the foresight value.
[704.42 → 709.38] So, you know, telling you what your sensors don't have line of sight into, but for planning purposes, right?
[709.38 → 723.18] But really much of the industry is still very reliant on maps and high-definition maps as priors for kind of the initial, you know, localization and perception decisions that the AI-based vehicle is making.
[723.72 → 726.56] And so that's really what it boils down to.
[726.56 → 731.08] You know, the question then is like, what really moves a needle in your map prior?
[731.36 → 737.82] And then there's a big optimization problem for that versus cost, speed of update.
[738.08 → 741.04] And then, of course, scalability is part of that big equation as well.
[741.28 → 745.70] That's kind of the initial premise of, you know, what everyone's working on.
[745.76 → 749.58] But it's also a bit of a moving target, which I can certainly talk about as well.
[749.58 → 754.42] So I'm curious, you mentioned a couple of times like high-definition maps.
[754.42 → 759.40] And I see that as sort of verbiage on your website and what you're working towards.
[759.74 → 772.84] So like when I think of high-definition, I mostly think of photos or videos that have a, you know, certain resolution or something like that, you know, when I'm watching Netflix or whatever it is.
[772.84 → 785.34] In terms of like the data that's needed for whether you're using this data for priors like you're talking about or maybe you're using it in other ways that people are developing.
[785.34 → 795.44] What is like high-definition mean in terms of the data, the map data that's used in autonomous driving and other related technologies?
[795.44 → 801.22] Is that like also images and video or is that high-definition in terms of information?
[801.50 → 803.66] Or could you kind of expand on that a little bit?
[803.92 → 813.00] And if I can add to that just a tiny bit, for those who don't have your experience, kind of differentiate what that is versus what the map that most people think about in their head is.
[813.00 → 815.06] Obviously, that's not enough.
[815.40 → 818.94] But maybe kind of how do you have to step forward to get to where you're at?
[819.44 → 819.60] Sure.
[820.14 → 825.22] You didn't come here to like plug our blog or anything, but we just happened to write a piece about this that's really relevant.
[825.48 → 828.52] So if anyone's curious, you can go to carmere.com and click on that.
[828.72 → 830.64] We will definitely include it in our show notes.
[830.64 → 831.34] We are curious.
[831.50 → 831.64] Yeah.
[831.72 → 832.46] Tell us about it.
[832.66 → 840.24] Well, it also has a very, very pretentious title, which is my fault, which it's the name of the title is The Mapping Singularity is Near.
[840.24 → 844.40] Naming is important, as we found out doing a podcast.
[844.92 → 850.24] If you look at statistics, it turns out that the name of the post is definitely important.
[851.34 → 854.82] I mean, content, of course, is what grabs people, but I totally get it.
[855.12 → 855.18] Yeah.
[855.30 → 863.14] Well, thankfully, the content has been received really well actually across our industry, even, quite frankly, people who've had to tell us that off the record.
[863.14 → 870.10] But anyway, the point of that, go read the post, but I think to answer your question, what the post is really helpful for is really defining these things.
[870.20 → 873.74] And the problem is these have been very nebulously defined, actually.
[873.90 → 877.14] High definition, I'm not sure who actually coined it.
[877.18 → 880.20] I don't know if it was like Nav tech or someone else.
[880.20 → 882.06] Maybe it was from the DARPA days.
[882.14 → 882.90] I'm not really sure.
[883.16 → 894.18] But it was just sort of this useful catch-all term for something higher definition than a normal map that humans have been using for research and navigation.
[894.88 → 896.66] Like a static image, essentially.
[896.80 → 897.46] Yeah, exactly.
[897.84 → 903.20] And really, even those maps only started to really become digitized in the 2000s, really.
[903.20 → 904.98] So it's still pretty recent.
[905.70 → 920.90] And so the difference is, they're actually, what we wrote in that post is the differences between what we call SD, so standard definition maps, that's the maps we've known forever, and high definition maps, HD maps, has felt pretty binary for the past five plus years.
[921.50 → 925.16] SD maps, typically for, they've been for human use.
[925.16 → 933.54] Typically, it's like researching, you know, I don't know, a restaurant or, you know, giving you some basic directions, but you're still the one driving or riding your bike or walking.
[934.24 → 939.04] And that's, again, that's for you, the human, to consume HD maps for the machine.
[939.36 → 948.22] And like I said before, with, you know, the primary need is in the form of priors with some other added benefits for, you know, localizing and path planning.
[948.22 → 954.72] And in terms to answer your question, in terms of like, what are some specific differences in the data?
[954.98 → 957.56] Again, the post has some nice sort of examples.
[957.56 → 961.76] Like we show you an intersection mapped in SD and then in HD.
[962.36 → 973.12] And to give you an example, that SD map for that intersection, I'm doing this off the top of my head, but, you know, I think there's only maybe like nine features that you need to represent that intersection, right?
[973.12 → 978.58] If you had it in just like a database, it would only be like, you know, this many lane lines, this many signs, et cetera.
[979.36 → 985.54] In the HD map, it's in nine features and maybe a few dozen attributes of those features, right, of each feature.
[985.94 → 989.88] The HD map, you're talking hundreds of features and thousands of attributes.
[989.88 → 1000.38] So like every turn line and every traffic signal, but not even just the traffic signal, you know, knowing about every bulb and the phasing and which lane of traffic each bulb controls, you know, like.
[1000.38 → 1005.56] So, so part of it is, you know, what we would call like feature and attribute granularity, right?
[1005.60 → 1007.90] So you're talking like a hundred X difference in that.
[1008.22 → 1010.64] Part of it is also in spatial accuracy.
[1010.94 → 1016.80] So, you know, an SD map, typically you're, you know, you can be off by tens of meters and that's very common.
[1018.32 → 1025.12] Whereas HD typically kind of the absolute accuracy bars have tended to be in the tens of centimetres.
[1025.32 → 1026.28] There's, there are a bunch of variants.
[1026.40 → 1029.70] Some people are in the lower end, some people are closer to meter, but definitely sub meter.
[1029.70 → 1030.62] And in the tens.
[1031.26 → 1033.06] So it's, it's both of those things.
[1033.48 → 1040.36] And ultimately the point of that post though, is we're actually seeing trends towards a convergence.
[1040.60 → 1044.66] We're actually already seeing it shift from a binary situation to a continuum.
[1045.04 → 1049.74] So as a company, we build high definition maps, you know, from the bottom up as we need to.
[1049.74 → 1065.66] And typically we do the full stack more for like the urban, you know, robot taxi mobilities and service type deployments where, you know, you have a more contained geography, but much higher granularity and accuracy requirements, you know, to the level I just mentioned.
[1065.66 → 1072.40] However, the biggest unsolved problem really in mapping for all levels of fidelity is change management.
[1072.62 → 1082.90] You know, when things change, it's still really, you know, the old methods of map creation or map maintenance are just too slow or expensive for this to work, especially for machine first uses.
[1082.90 → 1100.20] So that's what our technology and our focus has been on either for our own base maps or even for someone else's, you know, some other mapping companies map, you know, we can modularize our change management technology, which uses camera-based crowdsourcing to do that, you know, really efficiently at scale.
[1100.20 → 1117.84] And so for that change, what we call change as a service, that we actually do in a layer of fidelity internally called medium definition or MD for short, because that's a really useful state to keep data in and only upgrade it to HD quality when you need to.
[1118.00 → 1122.90] Otherwise, oftentimes it's overkill, and it's needless cost or time to do that across the board.
[1122.90 → 1136.52] But what we're seeing, this trend we're seeing is actually convergence where the AI is actually getting so good that it's not asking as much of the map of the HD map as it used to, even just a few years ago.
[1137.04 → 1146.06] You know, they're saying, you know what, actually for those features, even if I just know that it's in this block or at least in this hundred meter or 10-meter stretch, that's fine.
[1146.12 → 1148.38] You don't need it to be placed perfectly to 10 centimetres.
[1148.90 → 1152.84] But these other ones I do, you know, and so basically there's just a little, it's kind of,
[1152.90 → 1154.04] the lines are blurring.
[1154.04 → 1174.84] So the point is that this sort of some convergent layer in between the standard definition and high definition, the so-called medium definition is already where we're seeing the technological needs go to because the real-time perception and controls technology are getting good enough where they don't need as many crutches in the form of priors as they used to.
[1175.22 → 1179.10] However, definitely still need some and are still very reliant on them.
[1179.10 → 1184.68] And the other trade-off though is what they're saying is what we need this is in way more places.
[1184.84 → 1192.04] We don't, you know, just mapping, just, you know, a little urban area in Vegas or just the highway network isn't good enough.
[1192.16 → 1199.24] Like we need this to be way more ubiquitous, and we need you to update it way more frequently than like the old maps used to be.
[1199.24 → 1206.12] Like if you look at Google Street View, for example, you know, you are lucky if the last Street View image was within the last year.
[1206.28 → 1208.94] Sometimes it's three years ago, depending on where you live or even more.
[1209.54 → 1216.62] That's exactly the problem we're solving and kind of paying attention to how these goalposts are kind of moving towards this MD steady state that we think is emerging.
[1216.62 → 1230.20] This episode is brought to you by our friends at Rudder stack.
[1230.32 → 1234.92] And we're calling all data engineers to check out Rudder stack Cloud and start building smart customer data pipelines.
[1235.42 → 1238.34] Rudder stack is warehouse first, no more silos.
[1238.80 → 1242.14] Rudder stack builds your customer data lake on your data warehouse, not theirs.
[1242.14 → 1247.84] Enabling all functionality of a CDP with more security and retaining full ownership of your data.
[1248.18 → 1250.62] It's open source and API first.
[1250.92 → 1254.36] Rudder stack can be easily integrated into your existing development processes.
[1254.92 → 1257.68] And because they're open source, you can see all their code.
[1257.90 → 1260.32] So you don't have to worry about vendor lock in or black boxes.
[1260.86 → 1262.44] And best of all, they have transparent pricing.
[1262.64 → 1264.88] Stop paying your CDP a premium to store your data.
[1265.36 → 1270.24] Rudder stack is free up to 500,000 events and pricing scales transparently from there.
[1270.24 → 1272.68] Learn more and get started at Rudderstack.com.
[1272.96 → 1275.24] Again, Rudderstack.com.
[1275.38 → 1278.94] That's R-U-D-D-E-R-S-T-A-C-K.com.
[1292.52 → 1299.04] You had mentioned when you were starting out talking about how you viewed infrastructure, how you viewed roads.
[1299.04 → 1306.40] You were talking about this sort of perspective of also thinking about infrastructure in developing countries.
[1306.82 → 1316.22] Of course, a lot of the focus on navigation systems and technology has been focused on U.S. or European cities and that sort of thing.
[1316.22 → 1329.08] If we're able to start kind of bringing down the fidelity of what's required for navigation and even some advanced technology like autonomous driving, what does that mean for the developing world?
[1329.32 → 1332.54] Do you see that sort of change being impacted as well?
[1332.78 → 1333.20] Absolutely.
[1333.68 → 1334.06] Totally.
[1334.38 → 1334.62] Yeah.
[1334.76 → 1337.70] I mean, that's exactly my hope and our hope.
[1337.70 → 1351.96] I mean, that's why we've been really delighted actually to see that these trends may be, they really do appear to be emerging because that post was written on the backs of a lot of pattern recognition across the entire automotive and AV industry and maps industry.
[1352.52 → 1362.18] And a lot of big companies I can't really mention on the record, but everyone has been sort of, especially in the last, interestingly, I would say in the last like, what are we in?
[1362.18 → 1363.10] What was it?
[1363.12 → 1363.54] April now?
[1363.88 → 1367.68] So maybe in the last like eight, nine months, we really started to see that pick up.
[1367.78 → 1376.22] And by the way, I think some of that has been sort of almost a forced discussion given where Tesla's going with so much of this.
[1376.80 → 1380.56] You know, you could actually, you could kind of argue Tesla's already essentially using MD maps.
[1380.66 → 1382.92] They don't just, they don't like to call that, call them that.
[1382.92 → 1393.50] They kind of eschew using, you know, higher definition maps altogether, but they are using enhanced map data that a normal human map wouldn't have.
[1393.62 → 1400.42] It's just that they want to like be rid of it altogether and have a pure, like a super purist, you know, AI only approach.
[1400.42 → 1411.58] But I think the good thing about Tesla is it's really forced a lot of the old guard, so to speak, the incumbents to think about future reality sooner than they otherwise would have.
[1411.58 → 1415.00] And so I think MD is one example of that.
[1415.18 → 1417.00] And I think that it does get us excited.
[1417.14 → 1426.20] You know, a big kind of ethos of Camera is, you know, you'll look at like, if you look at our website and even one of our internal, you know, kind of inclusion groups.
[1426.46 → 1428.04] So we use the term for all a lot.
[1428.30 → 1432.36] One of our longtime partners, Toyota, you know, Mobility for All is their tagline.
[1432.36 → 1438.16] So that's always been very much the ethos of Camera is to sort of, you know, liberate and democratize.
[1438.24 → 1449.28] We always used to kind of use those terms in the early days of how do we liberate this data that, you know, is only some small handful of really large companies are able to collect and make it accessible to all.
[1449.28 → 1454.20] My hope is actually what we kind of saw with something like, you know, telecommunications, like, right.
[1454.28 → 1463.78] So like when I was in India as a kid, and then even, you know, when I'd come back, it was like a big deal and pain in the ass to make a call anywhere, really.
[1463.78 → 1471.14] And especially internationally, you know, you'd have to go to these little, like, these like government booths, like on the road, on the side of the road.
[1471.14 → 1475.86] And, you know, like, whatever, it was a pain and like not, it was not a connected country.
[1476.28 → 1485.50] And then mobile came along, and they didn't have to follow the same decades long mobile, you know, path that we had to in the US leapfrogged.
[1485.84 → 1488.50] Yeah, they skipped that whole step there.
[1488.72 → 1489.08] Exactly.
[1489.08 → 1497.34] So that's exactly what I'm hoping this, this and many other things could mean for developing countries getting access to this type of technology sooner.
[1497.70 → 1506.54] And what do you think, just to follow up on that, you mentioned crowdsourcing as well, as a big part of your sort of change management of maps.
[1506.54 → 1518.82] I'm thinking back to like, when I visited Russia, I visited Yandex, which is, so like, if you go to Russia, at least when I was there, maybe it's changed, I don't know, like, when you're navigating,
[1518.82 → 1524.30] on the streets, everybody uses these Yandex maps, which it's like, it looks amazing.
[1524.30 → 1526.38] It's like Google Maps is beautiful.
[1526.60 → 1538.84] But it's like, they were telling me, hey, you know, if you look at the fidelity that you get from, from Google, like they're not putting in the effort to map all of these roads in Siberia.
[1538.84 → 1538.96] Yeah.
[1539.30 → 1541.50] But we're going to put in the effort over here.
[1541.62 → 1544.80] And that's why people use it is because they have that fidelity.
[1545.16 → 1548.66] It's cool to see localized companies do those things.
[1548.66 → 1558.36] But it seems even more powerful if you put some power in the hands of users and people that are users of products to help crowdsource that data.
[1558.36 → 1562.02] What does that scenario look like to you as we move forward?
[1562.02 → 1564.46] Well, I think there are two thoughts I have on that.
[1564.56 → 1565.56] First off, I'm optimistic.
[1565.84 → 1581.54] Both of those thoughts, I'm optimistic on other countries, especially developing ones, kind of getting, you know, not being second class citizens when it comes to having their, you know, roads mapped and things like that at the same standards we see here.
[1581.54 → 1585.20] So first off, maps have been a huge money pit for a long time.
[1585.38 → 1592.74] And that there's a good reason Google had such a lead is because they were the only company who had that will.
[1593.06 → 1597.08] First off, that's a big part of it is just like the founder led will to do it.
[1597.12 → 1601.18] There's a whole story about how, you know, Larry and Sergey were convinced to do this.
[1601.28 → 1607.20] And of course, the just dry powder to go spend an inordinate amount of money on these maps around the world.
[1607.20 → 1616.86] And they're still, I mean, that's part of the reason we exist is because that's not tenable at a certain point, especially it's one thing to spend a huge amount on creating the map once around the world.
[1617.08 → 1622.10] But, you know, it's just simply even for Google, for any company, you can't keep doing that for maintenance.
[1622.76 → 1629.02] But the other thing that has been useful is, you know, in the early days, maps weren't really directly monetized.
[1629.02 → 1637.02] They were more just this like absolute killer app that like set Google so far apart from others in terms of using their other consumer products.
[1637.20 → 1639.80] You know whether it's search or Android or whatever.
[1640.60 → 1654.98] What does appear to be happening, if you kind of read into some of their investor statements and things like that, is they've been able to connect those dots much more closely of, you know, what they're spending on maps actually monetizes from their other products like search, for example.
[1654.98 → 1662.46] And I think there's some, I heard some stat that like 43% or something like that of Google search results now return a map.
[1662.46 → 1676.22] So that way I mentioned that because that's, there's much now, not just Google now, you know, anybody who has a business like that index, of course, the Google of Russia, they are much more able to justify financial investments in mapping assets.
[1676.22 → 1683.92] Because I think, you know, it's becoming clear, like, for example, for location based, you know, advertising, things like that, it's that connection is becoming clear.
[1684.54 → 1691.36] Second reason is to what you were, I think, hinting at Daniel, which is around the power of the consumer.
[1691.36 → 1702.90] And interestingly, in developing countries, especially in Asia, so, you know, there's an interesting Genesis story of for Career, where I was still at my previous startup in 2013.
[1703.62 → 1712.48] And randomly that year, I don't know if any of you guys will remember this, but there was like a bunch of viral videos of meteors of that year, then there was happened to be spotted in Russia.
[1712.48 → 1721.24] And these meteors happen very quickly. So even if you see it as a human, it's usually too quick to whip out your phone and fumble with it and, you know, get the camera going.
[1722.02 → 1727.86] And I learned that the only way they were captured is because some people were driving by with their dashcams on.
[1728.26 → 1731.28] And I was like, what's a dashcam? I'd never even heard of a dashcam back then.
[1731.28 → 1749.48] And what I realized is in certain countries like Russia, like China, like Korea, because of the additional risk of driving and also, you know, maybe the lack of maturity in some of the insurance industries, people felt like dashcams are actually very common there.
[1749.62 → 1754.28] And they have been for a while because of just personal security and being able to prove liability for that.
[1754.28 → 1761.80] And of course, that's right around the time when, you know, cameras being so cheap, connected, you know, IoT, all the other buzzwords.
[1762.14 → 1773.60] So and so I think that's also interesting because like, you know, these incredibly cheap connected cameras everywhere, you know, clipped to every moving thing is not just a rich country thing.
[1773.68 → 1781.64] In fact, if anything, as I told you, like we were seeing it in less developed countries even before the US because of that kind of that insurance need they had.
[1781.64 → 1790.50] So I don't think we mentioned this, but one of the ways that we do what we do at Camera is in addition to getting data from, you know, car, like car cameras.
[1790.60 → 1801.20] So, for example, you can see some of the public work we've done with Toyota where we've used data from, you know, Lexus production cameras or production grade cameras to do, you know, maps and change management.
[1801.64 → 1806.02] We have never wanted to rely solely on the automotive companies for our data.
[1806.02 → 1811.12] So we've also developed our own partnerships with commercial delivery fleets.
[1811.28 → 1823.54] These include one of the largest ones in the world, but also, you know, small and medium businesses who, you know, do pickups and drop-offs every day for storage or installing signs or whatever that might be.
[1823.54 → 1832.94] And they are using basically dash cams, you know, this sort of evolved versions of these dash cams that were first popped up in Asia years ago that we provide to them.
[1833.12 → 1841.18] But they have our technology running, you know, in the device, NLCV technology in the device that also then passes it off to the cloud at a certain point.
[1841.18 → 1850.18] That is crowdsourcing. But for us, we're actually using, we kind of coined this term pro sourcing because we focus on professional fleets as opposed to just any consumer.
[1850.84 → 1860.98] Because for us, it's more efficient. You know, these are delivery drivers who are on average are driving, you know, 10 to 100 times more mileage than just, you know, maybe you would, Chris, going from home to work and back.
[1860.98 → 1879.14] But what we're seeing is there's kind of an ecosystem forming as well on the telematics and dash cam side where there are a bunch of companies who sell these devices, and maybe they have access to some of the data, or maybe it's the delivery fleets themselves, some of these literally large logistics companies.
[1879.14 → 1883.70] They know they have, they're able to collect all this data, but they don't know what the heck to do with it.
[1884.22 → 1895.92] And that's where, you know, we can come in and structure fairly low grade raw data into very high grade, you know, up to high definition or medium definition, depending on the need data at scale.
[1895.92 → 1904.44] And having a mix of both consumers crowdsourcing for you and, you know, professional fleets crowdsourcing for your makes for a perfect portfolio of sources.
[1904.44 → 1917.80] One of the things that you said a little while ago, and it's been kind of tickling my thinking ever since you said it, and so is you mentioned earlier about kind of something that I've heard in other, you know, in other conversations and other venues as well.
[1917.80 → 1924.24] And I love your perspective on it. And that is, you kind of mentioned like the way that you guys are approaching it and the business bets that you're making.
[1924.24 → 1929.98] And then you have like Tesla and other people out there that are kind of doing a pure AI approach.
[1929.98 → 1935.54] And there's a legitimate conversation going on in the, you know, within autonomy about like how to approach that.
[1935.54 → 1939.04] And, you know, and I work for another company with interests in autonomy and stuff.
[1939.04 → 1945.76] And, you know, whether it's ourselves internally or other organizations, everyone's talking about the different approaches.
[1945.76 → 1949.68] And I'd love it if you could lay out what that conversation looks like.
[1949.68 → 1955.94] Clearly, you have a bias in that you have bet your company on a particular set of ways to do it.
[1956.24 → 1960.74] But, you know, obviously Tesla has, you know, that kind of that, you know, as you said, pure AI.
[1960.84 → 1969.90] Could you define what that would mean from their context and then maybe differentiate a little bit about the business bets that you're making and kind of lay the conversation out?
[1970.16 → 1970.22] Yeah.
[1970.26 → 1976.20] I'm not trying to pitch you against anyone, but just I'm trying to capture what the industry is talking about in that way.
[1976.20 → 1976.64] Totally.
[1976.88 → 1979.74] So I've seen a few different ways of framing this.
[1980.20 → 1987.36] Some people frame it as, you know, they use a dichotomy of like, you know, AI versus rules based, right?
[1987.40 → 1988.26] Or something like that.
[1988.50 → 1994.00] I also more recently saw it, which I kind of like as someone using sort of nature versus nurture.
[1994.40 → 1996.02] And maybe let's start with that.
[1996.10 → 1997.92] We were talking about priors before.
[1997.92 → 2006.20] And that's where I've seen it's actually the nature versus nurture dichotomy I saw because we're so we're connected.
[2006.32 → 2011.70] One of the several academic institutions that we have pretty close ties with is NYU here in New York.
[2011.86 → 2016.78] And when you use known for Jan Begun and his work, but also Gary Marcus.
[2017.10 → 2021.80] And in some ways they're, you know, sometimes friendly at odds with each other.
[2021.80 → 2026.08] And I've seen even them debate this concept of nature versus nurture for AI.
[2026.36 → 2033.34] And I might be kind of morphing it a little bit simplistically or off, you know, what they mean in their arguments.
[2033.34 → 2050.78] But for when it comes to what we think about is it's, you know, and what Elon's thinking about when he's saying what he's saying about Tesla's, you know, eschewing of things like maps is, can an AI get to where it needs to get purely on just learning and, you know, essentially nothing else?
[2050.78 → 2058.96] Or is there a need for there to be a certain, I think Gary Marcus uses the term innateness.
[2059.54 → 2066.26] Again, I'm kind of morphing it for this conversation a little bit, but like in our case, that might be analogous to sort of the use of priors.
[2066.92 → 2070.56] And so I think it kind of, a lot of these debates boils down to that.
[2070.68 → 2073.44] And actually, yeah, we kind of have a dog in the fight.
[2073.60 → 2076.46] Sure, we are a mapping company and that's used for priors.
[2076.46 → 2086.66] But actually, for me, I've always felt like what is actually going to solve the problem both now, but where can you future-proof yourself, including on the business side?
[2086.72 → 2099.80] It's really important to future-proof yourself so that, you know, if and when sort of certain trends materialize, you can sort of seamlessly ride that wave as opposed to completely flipping your, you know, your technical approach that you've taken.
[2099.80 → 2103.58] So like this SDHD to MD is a perfect example of that.
[2103.58 → 2114.44] Like right now, I don't care who you ask, especially for like really high levels of autonomy and also, you know, like where the driver truly is not in the loop and also in complicated environments.
[2114.80 → 2117.42] No one is able to do that without priors.
[2117.42 → 2128.60] And no one thinks that will be possible from, you know, a safety case, from regulatory and societal acceptance rate case for several years at least, if not more than that.
[2128.60 → 2132.06] But, you know, the but is that what if that changes?
[2132.24 → 2145.04] And the thing is, we always have to be humble because these things change in a very nonlinear way and our lizard brains are still really struggle with nonlinearity and predicting things because we just don't know where we are in those S curves, you know?
[2145.04 → 2151.94] So that's why I always kind of like we always sort of exercise humility there and kind of think about what if scenarios.
[2151.94 → 2158.44] And I think what if scenario of, you know, needing it, like allowing this AI to be more nurture than nature.
[2158.44 → 2170.38] Right. So just purely whatever you expose it to, it learns, and it just gets better, and it leads it needs less and less of what it was hardwired with from the beginning, I think would be a great thing.
[2170.38 → 2182.34] And for us, it would actually allow us to focus on higher level problems where you're switching from kind of, you know, certain problems on the lower rungs of the hierarchy.
[2182.34 → 2191.98] So actually another, again, I ended up coming in a blog to plug our blog, but another post we referred to in this last post was this thing we call the mapping hierarchy of needs.
[2191.98 → 2193.50] It's sort of a take on the Maslow thing. Right.
[2193.50 → 2206.66] But like over time, there's higher order problems that the data that we create still can are really important for us just that like it's stuff like, you know, user experience or compute efficiency or economics.
[2207.06 → 2212.72] Whereas the first order problem that everyone's really trying to get over the bar with is safety, you know?
[2212.84 → 2217.42] And so that's where, as I said, right now, everyone want really, really, really wants to use good priors for that.
[2217.42 → 2227.72] But, you know, in the steady state, you could totally envision maps being more used for things like comfort and monetization and, you know, things like that.
[2227.78 → 2237.78] I mean, if you think about aviation or other industries, you know, there's certain data sets that were much more critical for safety, but are really now much more for comfort.
[2237.84 → 2240.54] Like, let's say, for example, turbulence or something, you know, like weather data.
[2240.54 → 2249.20] Right. Like, you know, I'm old enough to remember when we did worry about poor taste jokes about like TWA and stuff about their safety.
[2249.42 → 2250.52] You and me both. Yeah.
[2250.88 → 2252.38] I'm about the same age, I think.
[2252.64 → 2253.30] Yeah, yeah, yeah.
[2253.32 → 2253.76] I agree.
[2254.08 → 2258.20] So remember, we actually used to think about that when booking a flight to somewhere.
[2258.60 → 2261.66] We never do because do they still use weather data?
[2261.80 → 2267.54] Yes. But you don't worry about it for like a turbulent, you don't worry about it for like crash safety.
[2267.54 → 2277.48] You worry about it more for like, you know, am I going to have a smooth ride and not spill my martini that I ordered, you know, with my Delta bucks, you know, I think you'll see a similar progression.
[2277.48 → 2286.40] And I think the use of, you know, the usefulness of the data that we inject into the AI will just it'll just change in nature, you know, and that's that's OK.
[2286.48 → 2286.98] That's a good thing.
[2297.54 → 2303.36] So change log plus is the best way for you to directly support practical AI.
[2303.90 → 2314.28] Join today and unlock access to a private feed that makes the ads disappear, gets you closer to the metal and help sustain our production of practical AI into the future.
[2314.28 → 2323.36] Simply follow the change log plus link in your show notes or point your favourite web browser to change log dot com slash plus.
[2323.54 → 2327.60] Once again, that's change log dot com slash plus.
[2328.74 → 2330.42] Change log plus.
[2330.70 → 2331.28] It's better.
[2331.28 → 2349.64] So we've talked a lot about kind of driverless and automation, autonomous driving.
[2349.64 → 2360.60] But one of the things that you talk about both on your website and in that blog post about HD and MD maps is consumer maps.
[2360.60 → 2381.64] And I thought it was interesting some of the things that you were talking about in terms of possibly us in the future seeing enhanced functionality in consumer maps that could be driven by MD maps where, you know, maybe in autonomous driving, we're able to use less fidelity.
[2381.64 → 2385.76] But we have this higher fidelity that's available for consumer maps.
[2385.76 → 2397.68] How do you see that evolving and maybe some of the AI capabilities that might be able to be built within consumer maps because of higher fidelity data that becomes available?
[2397.96 → 2401.82] Yeah, I mean, that's why, you know, we gave it this sort of high political title.
[2402.04 → 2404.44] The mapping singularity, you know, is near.
[2404.62 → 2407.36] I do think that like we're already seeing those trends.
[2407.36 → 2411.00] So, I mean, even if you look at, you know, like let's take Apple Maps.
[2411.12 → 2413.76] They were, you know, way behind Google for a long time.
[2413.76 → 2419.66] But if you, I don't know if you guys use Apple Maps, you know, I try to constantly sample all the major ones just to see what's going on.
[2419.90 → 2423.56] I bet your phone has so many map apps on it.
[2423.84 → 2426.06] You kind of have to try them all, right?
[2426.06 → 2431.18] I recently did a bit of a purge, a little bit of a cleanse, but it'll, you know, we'll get back up to where I was.
[2431.30 → 2440.00] But yeah, some like the natural language directions, for example, that you're seeing, you know, like, for example, from Apple Maps and I think others now as well.
[2440.00 → 2447.86] You know, that's a good example of like, it's kind of like giving us some superhuman machine-like qualities that we didn't use to have with normal maps for humans.
[2447.86 → 2457.94] So it's like, instead of just, you know, the next turn is a right-hand turn on the streets and, you know, maybe even giving you the amount of meters away it is.
[2457.94 → 2473.34] It's like, you know, being a lot more precise and allowing you, the human, to be, to almost feel a bit more like a machine, to feel more automated by saying, no, you know, hang a sharp turn at the McDonald's, you know, like being, like really like starting to get more granular.
[2473.34 → 2480.26] And like, just, let's just take a let's just sort of play that out where, let's just say like a package delivered today, right?
[2480.90 → 2502.88] So that driver, whether they're working for Amazon or for any other company, they might be using a standard off-the-shelf mapping, a navigation app, or they might be using something, you know, in certain cases like Amazon, they have, they're savvy enough to actually have their own, you know, routing and navigation capabilities on top of, you know, sort of consumer, general consumer maps.
[2502.88 → 2511.64] And so even today, that driver would greatly benefit from being guided by their maps app precisely to the right part of the curb.
[2512.08 → 2520.24] That's already pre-optimized for, first off, safety, like making sure it's not a dangerous part, you know, part of like, especially if it's a city or something to pull over.
[2520.94 → 2523.66] Proximity, obviously, to the doorstep or wherever they have to go.
[2524.02 → 2532.48] The probability of it being vacant, you know, you should hopefully, like, whether you have statistical data or other data from, say, the city,
[2532.48 → 2533.74] you should be able to incorporate that.
[2533.82 → 2542.02] There are a lot of things that could make that delivery dryer kind of superhuman as opposed to just letting them wing it, you know, which is what we've done for a long time.
[2542.40 → 2549.84] That's kind of what we're talking about, which is, you know, like, if you compare that to the inputs that an autonomous delivery vehicle would need,
[2550.26 → 2553.34] it's actually like in the MD future, it's not that different.
[2553.34 → 2554.98] You know, it's all those things I just mentioned.
[2555.14 → 2563.76] Plus, yes, you know, the robot's going to want more vector information on the map on where precisely to be able to, you know, pull into the curb space.
[2564.22 → 2569.94] And for the human, you don't really need that because, you know, they can handle that just fine, drive the steering, you know, doing the steering themselves.
[2569.94 → 2580.22] But that's where what we mean by that MD, you know, fidelity layer where, you know, humans are now being empowered to be sort of superhuman and act almost more like machines.
[2580.42 → 2595.88] And then machines are basically just being able to make more human-like decisions, you know, and just smoother, slicker decisions that a human, like a really experienced, attentive human would make in terms of pulling over, you know, in that drop-off space for that curb.
[2595.88 → 2600.76] That's an example. Yeah, as I said, we're seeing hints of that now, you know, it's like, it's pretty cool.
[2601.00 → 2614.84] I'm curious, as you're much closer connected to this industry, where you see the sort of trust levels of both companies and users of these technologies in terms of their capabilities?
[2614.84 → 2617.86] Because it's one thing to enable capabilities, right?
[2617.86 → 2630.30] It's a whole nother thing to ensure that humans' adoption is one thing, but also building trust and understanding how humans should and shouldn't operate with these technologies.
[2630.48 → 2640.10] I'm thinking back to, like, it's probably a meme in your industry, but that one Office episode where, like, the Garmin or whatever tells Michael Scott to, like, drive into the lake.
[2640.10 → 2643.66] And he, you know, trusts the Garmin and drives into the lake or whatever.
[2644.14 → 2650.96] And, of course, that's getting at the fact that, like, hey, at that time, like, people generally knew that there are a lot of flaws in this.
[2651.06 → 2653.24] Be careful what you think about it.
[2653.80 → 2662.34] So how do you view people's general trust in these sorts of mapping and navigation technologies?
[2662.34 → 2664.88] And how do you see that evolving as we move forward?
[2664.88 → 2665.32] Yeah.
[2665.68 → 2679.74] Well, I don't want to go off on a tangent, but there's actually also part of the origin story for Camera, believe it or not, was a Curb Your Enthusiasm episode, which I could talk to you about later, but kind of related to.
[2679.88 → 2680.66] Yeah, for sure.
[2680.82 → 2686.36] I'm sure that there are all sorts of, you know, memes posted around your office of various things.
[2686.52 → 2690.54] I'll tell you, it's specifically, though, season eight, episode eight is called Car Periscope.
[2690.64 → 2691.02] Look it up.
[2691.16 → 2691.88] But it's all right.
[2691.98 → 2693.22] We'll link it in the show notes.
[2693.22 → 2693.40] Yeah.
[2694.30 → 2697.38] Anyway, but to answer your question, yeah, it's a big, big deal.
[2697.42 → 2698.96] And that's why we're very involved.
[2699.08 → 2700.92] Like, the trust is the biggest deal, actually.
[2700.92 → 2711.00] And we try to get really involved in that, you know, for example, in shows like this and really, like, just educating and being super honest about where we are today, where we're going.
[2711.52 → 2718.12] We're on the board of the main kind of, I guess, educational body of the AV industry.
[2718.34 → 2721.80] It's called PAVE Partners for Automated Vehicle Education, I think.
[2721.80 → 2724.74] So, yeah, we're big believers in that.
[2725.14 → 2728.34] And, you know, look, I'm not actually a Tesla hater at all.
[2728.40 → 2735.52] In fact, I actually give them huge credit for whipping much of this industry into gear, including on the EV side.
[2735.52 → 2742.90] But we are very worried about, like, lasting impacts of trust with stuff like FSD, right?
[2742.96 → 2748.86] With this so-called full self-driving and, you know, seeing a lot of the incidents that are happening.
[2749.26 → 2758.00] And what's it going to take to set us back because of losing trust in, you know, for training their Tesla's neural net, right?
[2758.00 → 2766.36] And so I think the best way to trust is all the things we're doing, which is, you know, transparency and education.
[2766.54 → 2770.22] But ultimately, it's making the technology boring, right?
[2770.26 → 2775.68] Like, again, going back to aviation, the aviation is incredibly, amazingly safe.
[2775.68 → 2776.82] And it's boring.
[2777.02 → 2779.02] And no one thinks about those things really anymore.
[2779.82 → 2782.74] And I think, and it took time, you know, it didn't happen overnight.
[2783.28 → 2793.76] I don't think autonomous driving needs to, you know, like take as long to really industrialize at scale as aviation did from the Wright Brothers.
[2793.82 → 2795.24] I don't think it will take that long.
[2795.24 → 2805.76] But it's definitely taken longer than all the 2019, you know, 2020 predictions everyone was saying back at CES 2015 of when we're going to have robotaxis everywhere.
[2806.20 → 2809.78] You know, first off, it's, everyone knows by now, it's just, it's way harder than people thought.
[2809.88 → 2811.28] It's the classic 90-90 problem.
[2811.46 → 2816.40] You know, you're 90% of the way there, but then you realize the last 10% is actually 90% more.
[2816.40 → 2825.52] But I think the boring part is really key because when, you know, like, for example, Waymo 1, you know, they really have been the first to truly take the driver out in Phoenix.
[2826.40 → 2831.30] And, you know, not just them, but other AV companies we've worked with or know really well.
[2831.36 → 2832.42] They always say that same thing.
[2832.46 → 2838.32] And by the way, my smoothest AV ride has been when I forgot that autonomous mode was engaged.
[2838.74 → 2841.16] This particular one was in downtown Detroit.
[2841.16 → 2849.98] And I got out, and I told them, I am so impressed because in the other AV rides I'd done, I had been thinking about, I was remembering it.
[2850.08 → 2851.86] And I remember I kind of zoned out for a second.
[2852.54 → 2864.84] So that, whether you're thinking about level four, you know, like the mobility as a service model, or you're talking about kind of the more super cruised, you know, autopilot on a highway.
[2864.84 → 2875.74] Once, you know, the user really feels like it's, you know, they're at the comfort level where either the whole ride is such that it's kind of mundane, and they don't even have to think about the technology.
[2876.20 → 2886.80] Or in the case of human assistance, where it's more highway, you know, assists, like I guess it's kind of a Cadillac super cruise, where they're still confident that the system is perfect at bringing them back in the loop.
[2887.28 → 2888.38] That is what it's going to take.
[2888.48 → 2890.98] And the good thing is those are parallel tracks that are happening.
[2891.54 → 2893.46] They just need to play out in the right way.
[2893.46 → 2905.86] And the problem with boring using, you know, kind of Tesla approach, the thing people fear is it's really hard to square boring with, oh, but you still need to be in the loop.
[2906.20 → 2906.30] Yeah.
[2906.42 → 2907.64] Really, really hard to do that.
[2907.70 → 2908.54] That doesn't work very well.
[2908.74 → 2915.78] I think you've called out a truth there that goes beyond just this use case that we're talking about, that's technology in general.
[2915.78 → 2923.98] And that is that the, you know, boring, when things become boring, it is really that point where you see acceptance, you see people move on in their thinking.
[2924.52 → 2926.24] Sorry, Apple, but none of us think about our iPhones.
[2926.24 → 2928.14] And for Google, it's just there.
[2928.14 → 2933.22] And I agree with you that I think that's the secret is when people just don't care too much.
[2933.22 → 2937.12] It's just part of the fabric of their life, which kind of makes me think forward.
[2937.12 → 2944.24] While we have you here, if you could kind of finish up with telling us what you think we need going forward.
[2944.36 → 2950.34] Like if we abstract, and I'm using the term map loosely in this case so that it can be whatever you want it to be.
[2950.34 → 2959.20] But what kind of map needs to exist in the future to move us toward boring, to move us toward daily acceptance, to make life evolve in that way?
[2959.62 → 2960.70] Everyone's comfortable with it.
[2960.76 → 2964.32] And what needs to happen to get to that next level?
[2964.48 → 2970.18] What does that map, in quotes, look like for tomorrow that doesn't exist today?
[2970.18 → 2979.86] Yeah, the rule of thumb we always use and was given to me actually by, I believe it was someone who was associated with Google Maps in the very early days is 100x.
[2980.00 → 2984.26] 100x on ubiquity and 100x on sort of temporal density.
[2984.40 → 2985.24] So freshness.
[2985.62 → 2991.34] So that's always, you know, so basically like one order of magnitude isn't enough on either of those dimensions from where we've been.
[2991.34 → 3000.20] It's two orders of magnitude to get to this, you know, this like Shangri-La steady state that we've all been talking about during this podcast.
[3000.20 → 3012.68] You know, all the fidelity and cost and speed and humans in the loop, out of the loop, everything kind of ultimately is this massive optimization, you know, problem to get to that, that 100x.
[3012.92 → 3013.18] Awesome.
[3013.36 → 3014.30] That's a great perspective.
[3014.58 → 3017.18] And yeah, I really appreciate the work.
[3017.18 → 3027.16] You can tell that you and your team put a lot of work into that blog post that we've been referring to and sort of the clarity that it brings around some of these things.
[3027.28 → 3033.80] So I appreciate you being willing to put in time to that sort of communication because I think it is very helpful.
[3034.44 → 3039.52] So I encourage our listeners to check that out and to check out all the things that your team is doing.
[3040.06 → 3043.16] But yeah, thank you so much for taking time to chat with us today.
[3043.30 → 3044.12] It's been a pleasure.
[3044.42 → 3046.02] Yeah, thank you for having me.
[3046.02 → 3060.60] I mean, if I could just also plug, you know, for folks, like, especially in the communities like yours, whether it's for, you know, maybe working with us one day, or even just riffing on some of these things, or like the reason we put them out there is that we get really, you know, interesting feedback back.
[3060.66 → 3062.74] And oftentimes we'll publish like a follow-up.
[3062.88 → 3073.70] So please do, you know, come to carmera.com or hello at carmera.com or LinkedIn or Twitter, whatever, you know, let us know if you have thoughts on some of these topics.
[3073.70 → 3079.80] It's also, if you go to carmera.com join, you can sort of see some of the things that we, you know, tend to look for, for team members.
[3079.96 → 3082.82] I think one thing we didn't have time to cover, which is totally fine.
[3082.88 → 3085.30] We can, you know, we can save that for some time else.
[3085.30 → 3096.84] But what's kind of cool about what we do is we use AI to make AI, you know, like we use AI to power AI, you know, so everything we talked about in this episode was about the output, right?
[3096.92 → 3099.14] Of like the data we're injecting into AI.
[3099.48 → 3108.98] But for the other geeks who are interested, we basically like all the NLCV stuff we use to actually create that, those maps, that data is pretty cool stuff too.
[3109.18 → 3109.68] So check it out.
[3109.68 → 3111.54] Sounds like we're going to have you back for another episode.
[3112.74 → 3113.78] That might be my pleasure.
[3113.92 → 3114.02] Yeah.
[3114.48 → 3114.82] Yeah.
[3114.90 → 3115.08] Yeah.
[3115.08 → 3115.56] For sure.
[3115.62 → 3117.04] I definitely hope that happens.
[3117.18 → 3118.00] Thank you so much.
[3118.10 → 3120.94] And we'll put some links to those, those you mentioned in our show notes.
[3121.10 → 3122.34] Definitely check those out.
[3122.82 → 3123.00] Yeah.
[3123.04 → 3124.36] Thank you again for joining us.
[3124.36 → 3124.86] Thanks guys.
[3125.10 → 3125.32] Take care.
[3139.68 → 3143.48] We are also on the web at practicalai.fm.
[3143.74 → 3148.70] There you'll find recommended episodes, listener favourites, and a free signup to join the community.
[3149.32 → 3152.72] Practical AI is hosted by Chris Benson and Daniel Whiten ack.
[3152.90 → 3156.46] It's produced by Jared Santo with music by Break master Cylinder.
[3156.88 → 3160.06] Thanks again to our sponsors, Vastly, Linde, and Launch Darkly.
[3160.20 → 3161.02] That's our show.
[3161.44 → 3164.16] We hope you enjoyed it, and we'll talk to you again next week.
[3169.68 → 3171.68] Bye.
