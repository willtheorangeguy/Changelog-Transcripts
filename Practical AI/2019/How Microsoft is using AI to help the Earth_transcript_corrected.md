[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 → 23.00] on Linde servers. Head to linode.com slash Changelog. Welcome to Practical AI, a weekly
[23.00 → 27.90] podcast about making artificial intelligence practical, productive, and accessible to everyone.
[27.90 → 33.48] This is where conversations around AI, machine learning, and data science happen. Join the
[33.48 → 37.56] community and slack with us around various topics of the show at Changelog.com slash community.
[38.08 → 41.64] Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[46.36 → 51.64] Welcome to the Practical AI podcast. This is Chris Benson, your co-host, as well as the chief AI
[51.64 → 57.00] strategist at Lockheed Martin RMS APA Innovations. This week, you're going to hear one of a series
[57.00 → 62.20] of episodes recorded in late January 2019 at the Applied Machine Learning Days conference
[62.20 → 67.16] in Lausanne, Switzerland. My co-host, Daniel Whiten ack, was going to join me, but had to
[67.16 → 70.64] cancel for personal reasons shortly before the conference. Please forgive the noise of the
[70.64 → 74.78] conference in the background. I recorded right in the midst of the flurry of conference activities.
[75.26 → 80.18] Separately from the podcast, Daniel successfully managed the AI for Good track at Applied Machine
[80.18 → 84.84] Learning Days from America, and I was one of his speakers. Now, without further delay,
[84.84 → 93.28] I hope you enjoy the interview. I have Jennifer Marksman, who is principal engineer on the AI for
[93.28 → 97.98] Earth team at Microsoft with me today. Welcome to the show, Jennifer. Thank you for having me, Chris.
[98.10 → 104.02] So I was fascinated to learn that Microsoft had an AI for Earth team. I think that's super cool,
[104.14 → 108.06] and I would like to know more about it. Could you tell me a little bit about yourself
[108.06 → 113.34] and, you know, kind of how you got on the team and a bit about the team itself? Give us kind of broad
[113.34 → 118.88] intro to it? Absolutely. So I'm very excited about the AI for Earth team as well. I actually heard
[118.88 → 123.96] about it before I joined the team as one of the kind of new initiatives Microsoft was going forward
[123.96 → 130.22] with, and I wrote an essay to the hiring manager on why they needed to hire me because I was so excited
[130.22 → 136.04] to be a part of it. I love that. Oh, yeah. Oh, yeah. I went hardcore for this one. But here's the idea
[136.04 → 143.68] behind it. AI for Earth started by the guy who is now my manager, a dude by the name of Lucas Joppa.
[144.24 → 150.18] And Lucas is actually Microsoft's first chief environmental officer, which I did not even
[150.18 → 154.94] know that we had prior to taking this job, but apparently that is a thing. And what's really cool
[154.94 → 159.66] is Lucas worked for this guy, Eric Horowitz, for a very long time. And Eric Horowitz is, of course,
[159.70 → 164.48] a big name in the machine learning world. He's been at Microsoft Research for a long time.
[164.94 → 171.36] And Lucas's background was actually in biodiversity and conservation, and that's where he got his PhD.
[171.92 → 177.56] And so coming from that kind of environmentalist background and then working with, like, for Eric
[177.56 → 186.34] for a time really got him thinking all the time about the intersection between AI and these hard
[186.34 → 190.76] environmental issues. And when you think about the progress we've made with artificial intelligence
[190.76 → 196.20] just in the last 15 years, I mean, it's astronomical. It's so much like things that were...
[196.20 → 201.56] So I'll give away my age here a little bit. But when I finished grad school, I did my grad school in...
[201.56 → 206.86] Actually, my degree is in artificial intelligence, which gives you an idea of how long ago I did my
[206.86 → 213.10] thing, that that was still a degree then. Now that's way too broad a field to have as a degree.
[213.20 → 220.40] Now it's NLP or computer vision or whatever. But back in the day, this was maybe 16 years ago,
[220.44 → 228.56] at least, when I got my degree in AI. We've made such progress since then. With deep learning,
[228.56 → 233.00] just in the last, what, 10 years or so, we've been able to solve really hard problems like
[233.00 → 237.92] automatic machine translation and speech recognition and a lot of these other things.
[238.32 → 244.76] And so the idea was, since machine learning is having this exponential effect, could we apply
[244.76 → 251.04] it on hard things like climate change or like being able to conserve animals that are going extinct
[251.04 → 256.68] at a rate that's like thousands of times the natural rate currently? Or how to build or how to
[256.68 → 262.94] grow more food on land sustainably? So you're not burning out the land by doing...
[262.94 → 266.70] You can get the short-term benefits, but then it's not good for the land long-term.
[267.06 → 273.20] But to be able to increase the yield while still doing it sustainably and then provide
[273.20 → 278.28] clean water to people. So all of these really hard challenges, like what would happen if we applied
[278.28 → 280.68] machine learning to them? And that's what was keeping Lucas up at night.
[280.68 → 287.10] And so he wrote a white paper and that white paper became the basis of essentially the AI
[287.10 → 291.50] for Earth program. So at its heart or at the beginning, it is a grant program. So Microsoft
[291.50 → 299.26] publicly committed $50 million over a five-year timeframe. And that is money that is available
[299.26 → 306.52] as grant money to anyone who is doing machine learning or data science work in the areas of agriculture,
[306.52 → 313.04] water, climate change, and biodiversity. So any one of those four is fine. And it can be a startup,
[313.20 → 317.40] it can be a nonprofit, large corporations, independents, anyone at all is welcome to
[317.40 → 325.58] submit a grant. And we accept grants on a quarterly basis. I think the next deadline is in April 2019.
[326.28 → 333.42] And so folks are welcome to apply for a grant. And so that's kind of the one, the start of it. But
[333.42 → 338.02] our kind of aspirations are even grander than that. As you said in the intro, I am an engineer.
[338.02 → 343.96] So like I'm, I want to be building models. I want to be doing the fun data science work myself. And so
[343.96 → 349.90] we're actually doing a great combination of that. So there's, we partner very closely with Microsoft
[349.90 → 354.96] Research. So there's several Microsoft Research projects that we're funding and working very closely
[354.96 → 360.72] with. We're actually, our engineering team is kind of building some of our own APIs where we take
[360.72 → 367.12] models that may be useful to a number of people who are doing sustainability efforts and then exposing
[367.12 → 371.62] those models as APIs so that people could call them and utilize them. And then the third bucket of
[371.62 → 376.90] engineering work is in the area of our AI for Earth grant recipients. So being able to support them
[376.90 → 382.22] wherever they're at in their machine learning journey. So some folks that we work with are these
[382.22 → 386.88] brilliant environmentalists, but maybe they don't have as much of a machine learning background.
[386.88 → 392.16] And so they have these fantastic data sets. And so we help them get started with how they can apply machine
[392.16 → 397.20] learning techniques to that data. And then some people are, you know, PhDs in machine learning, academics
[397.20 → 402.78] and such. And those people, you know, may be just, you know, absolutely brilliant at machine learning,
[402.78 → 407.74] but maybe they would want to know how to use Azure, you know, to be able to scale out their work or, you know,
[407.74 → 414.02] get results faster or any of those things. Yeah. So my job, like I try to, I actually own the three E's
[414.02 → 420.54] for AI for Earth, um, engineering, evangelism and education. So I do work.
[420.54 → 424.76] That sounds like a fun job right there. It is. Oh, it is. So I'm just kind of trying to work across
[424.76 → 429.84] those. It's a it's a lot of, it's a lot of work, a lot of stuff, but I'm really, really exciting to be
[429.84 → 435.64] able to be a part of it. So that sounds super cool with it. So it sounds like you both, uh, you know,
[435.64 → 439.96] fund these other projects that are out there through the grants that you talked about, but you also
[439.96 → 444.96] mentioned that you have your own engineering team. So what is the, uh, what kinds of things would you,
[444.96 → 449.26] uh, focus on helping other people from a grant perspective? What kinds of things would your own
[449.26 → 455.20] engineering team and how do those interact? Yeah. Great question. So essentially, um, the grant
[455.20 → 460.16] proposers are whatever people submit. So those are not something that I have control over. It's whatever
[460.16 → 466.18] people want to submit. Um, we accept things that seem feasible, that seem like they're doable. Um,
[466.18 → 470.50] we want to make sure they have a data set that will, will actually work and something that seems
[470.50 → 475.26] like it's possible, but as long as it's a, um, a feasible, uh, a data set that would support what
[475.26 → 478.50] they're trying to do. And it seems feasible, and they seem like they have the knowledge and
[478.50 → 482.86] background that they could do it. It's, um, probably worth at least a small investment of,
[482.86 → 487.44] of Azure, give them at least some Azure credits to let them try it, that sort of thing. Uh, and then
[487.44 → 492.96] our own engineering team, what we're trying to focus on is, are there things that we could build
[492.96 → 499.68] that are, um, things that would work for a large variety of people, right? So almost trying to do
[499.68 → 503.60] like the way that I think about it personally, and this, this is kind of just Jennifer Marksman
[503.60 → 508.50] speaking, not an official AI for Earth thing, but for me, um, I try to think of what are things that
[508.50 → 514.32] would be useful to a variety of people, right? Um, because a lot of times the way a grant recipient
[514.32 → 521.78] should work, um, so, so let me take a quick tangent, quick tangent. So I, for a long time,
[521.78 → 526.26] there's a guy who actually does a lot of speaking now about AI in China, Kai FM Li, who has worked
[526.26 → 531.46] at Microsoft and Google and such. And so he's also a big, um, venture capitalist and funds a lot of
[531.46 → 536.20] startups. And one of his words of wisdom about startups is that you should, startups should never
[536.20 → 540.28] build a platform. They should build a product, right? They should solve one specific problem
[540.28 → 545.70] and solve it well, and then expand out to a platform, right? Okay. And so I think about the work
[545.70 → 552.50] that these nonprofits and academics and such are doing the exact same way. I think that they, a lot
[552.50 → 557.84] of times they are trying to solve such a specific problem. Like I need to be able to, um, predict how
[557.84 → 562.84] well, um, you know, flooding for this particular river in Africa and this one place in Africa. Uh, so
[562.84 → 569.66] it's a very specific problem and, um, and they shouldn't focus on the high back. They should solve the
[569.66 → 573.40] problem that they need to solve because if it's a nonprofit trying to solve a thing, like they need to focus
[573.40 → 579.30] on their mission, right? Um, and so what I think our team should be focused on is taking that step
[579.30 → 585.50] back and building real APIs. Like, okay, is there something, is there a way that we can then, um,
[585.76 → 591.24] build things that would work for a wide variety of people, um, kind of in the spirit of that,
[591.38 → 596.28] you know, rising water lifts all boats so that we can enable the entire sustainability community
[596.28 → 603.60] to do great work. So, um, we've started with two specific APIs that our engineering team has produced.
[603.76 → 609.28] One of them is, um, around land cover mapping. So we did, um, and essentially if you're not familiar
[609.28 → 615.08] with land cover mapping, what that means is that given some, um, aerial imagery as input. So, um, and
[615.08 → 620.04] typically like what we're using is a four band imagery. So it's the NADP imagery, if you're familiar
[620.04 → 625.84] with that, but it's essentially RGB. So natural colour as well as a near infrared channel. Okay. So those are the
[625.84 → 633.58] four bands and then take that as input and then be able to say, okay, what, um, what, uh, pixel by
[633.58 → 639.26] pixel level. And this is, we're actually doing it at one pixel, um, resolution. Uh, is this water or
[639.26 → 644.98] tree or barren? So essentially it's a road or a, you know, house, something you can't build on. Um,
[644.98 → 650.02] and we have this enumeration of different classes. And so pixel by pixel level, we can enumerate those
[650.02 → 655.14] things. And so that's great for use if you are, you know, disaster relief kind of work, trying to look at,
[655.14 → 659.52] um, or flood levels, like realizing, okay, where are the water lines now? You can use that. It's
[659.52 → 663.80] great for urban planning. It's great for a lot of different scenarios. So that's one great general
[663.80 → 669.00] purpose thing that we're trying, that we have a an API for that's available already. If people would
[669.00 → 675.50] like to email, I think it's AI for earth APIs at microsoft.com. I can give you a key. Otherwise,
[675.76 → 679.14] yeah, we can add that to the show notes as well later on. So we can check that and make sure that's
[679.14 → 682.96] good. That would be perfect. Thank you, Chris. Sure. And then another one we're working on is, um,
[682.96 → 688.86] uh, iNaturalist, if you're familiar with them, has released a large public data set.
[689.24 → 694.52] They do really amazing work, and we've partnered with them as, um, and, uh, given them some funding
[694.52 → 697.76] as well. And what they have, if you haven't downloaded it, oh my gosh, you should, because
[697.76 → 702.36] it's perfect. They have a really great, uh, mobile app that's available for iPhone and, um,
[702.76 → 709.08] and Android. And essentially what you can do is they have a classifier that allows people to,
[709.08 → 715.76] uh, you can take their app and then wherever you are, any animal, any plant or any fungi,
[715.76 → 720.50] you can actually take a picture and then record an observation of where that is in nature. So it's
[720.50 → 725.96] great. Then, um, biologists and such can use that data to get a good sense of the, you know,
[725.98 → 730.56] the ecological makeup of any given area. And it's just citizen scientists, everyday people like you
[730.56 → 735.02] and me who like might care about the environment, but are not necessarily a biologist, uh, can take
[735.02 → 739.68] pictures. And then, uh, that way scientists know that, okay, this particular species of plant is
[739.68 → 744.90] located here, and this animal was seen here. It's so cool. And so what's really nice is that they
[744.90 → 750.14] released this data set that and make it available for folks. So we actually trained a classifier
[750.14 → 758.34] that will distinguish between like, it's remarkably accurate for, um, plants and animals giving you the
[758.34 → 763.24] species. So given an image of something, here's the species, it will return the exact species name.
[763.24 → 768.64] And so you can do this across animals. You can do it with, um, uh, plants. And I believe, um,
[768.64 → 773.36] here at this conference, um, Grant Van Horn is actually speaking on iNaturalist. He did a lot
[773.36 → 776.26] of the machine learning work behind that. Okay. I can't wait to hear him speak that. Yeah. It's
[776.26 → 780.60] really cool. It's really amazing stuff. So, and so they're one of our grant recipients as well.
[780.94 → 785.58] Awesome. So a little follow-up question to that. Um, just, so how, how is it when you,
[785.70 → 788.64] normally when most people are thinking about Microsoft, they're thinking about technology,
[788.64 → 792.16] they're thinking about cloud, obviously thinking about windows and office and other,
[792.16 → 795.76] other things that Microsoft is doing. How did they get into this in particular? What was the
[795.76 → 800.32] motivation for the company to back this? Yeah. Great question. So as Microsoft's chief
[800.32 → 806.02] environmental officer, uh, Lucas owns, um, not only the AI for earth program, but he also owns our
[806.02 → 810.90] environmental sustainability, uh, work. And in terms of, um, environmental sustainability,
[810.90 → 816.04] like Microsoft has won numerous awards for that. We've been carbon-neutral since 2012. Um,
[816.42 → 821.72] we actually have different departments inside Microsoft pay a carbon tax, um, to offset usage and,
[821.72 → 825.54] and flights and stuff like that. Uh, we pay a carbon tax on that. Something that was not very
[825.54 → 829.96] popular when first introduced at the company, but has been great. But the way we look at it is
[829.96 → 835.58] even if Microsoft was absolutely perfect. So let's say our data centres were all completely like
[835.58 → 841.82] underwater data centres and, and everything was just fabulous. That's only so much. There's only so
[841.82 → 847.40] much impact. Microsoft as a company is having, you know, just in our own operations. So how could we
[847.40 → 853.64] scale out even more? And so AI for earth was really our answer to that question by dedicating
[853.64 → 861.32] this $50 million over five years, um, to people that enables everyone to be able to partake. And, and,
[861.32 → 869.66] and what's, what I, what I love about that is that we are asking oftentimes the people with the
[869.66 → 875.36] the least resources to solve the world's hardest problems, right? It's nonprofits. It is, um, these,
[875.36 → 880.28] these sustainability groups, it's academics who are, we're asking to solve these hard problems of
[880.28 → 885.16] like climate change and, you know, um, reducing, you know, the, the rate that these species are going
[885.16 → 891.36] to extinct and a lot of others, um, really, really hard challenges. And so this is a way that Microsoft
[891.36 → 897.00] can kind of dedicate what we're good at. Namely, we can provide machine learning knowledge. Um, and,
[897.08 → 901.94] and we do that through the, the education arm of the AI for earth program, um, as well as, um,
[901.94 → 906.56] our data centres. So at here's Azure, here's like all this, you know, infinite compute power with
[906.56 → 912.38] using the cloud. Great. You know, use this. And then that gives people both the knowledge
[912.38 → 917.64] and the access to cloud that they need to help them be successful, um, in their areas of expertise.
[917.78 → 921.80] So these folks who are grantees are tended to be good at the stuff that I'm not good at,
[922.02 → 926.48] which is the environmental end of it in that strong domain knowledge, um, in the areas of agriculture
[926.48 → 931.42] and water and such. So put those things together and you can do something really powerful.
[931.86 → 937.44] That sounds great. So, um, do me a favour and, and, in your mind, uh, think of maybe one of the
[937.48 → 943.30] your favourites that come through and take us through what it looks like from the point where
[943.30 → 948.92] they decide to apply and what, how you help them. What are the different, uh, both from, uh, the
[949.08 → 952.86] the what you might call, I don't know, the business side of it, and the machine learning
[952.86 → 957.54] side and just give us a picture because there may be people out there in nonprofits listening
[957.54 → 961.98] to this right now that suddenly jump at this opportunity and tell them what this project
[961.98 → 966.50] will look like when they engage you. Absolutely. Absolutely. Okay. So Chris, I'm going to have a
[966.50 → 970.74] really hard time choosing a favourite because I love, there are so many good stories. Like our grant
[970.74 → 975.22] recipients are doing such amazing things. Okay. So I'll try it. Let me tell you a few stories.
[975.44 → 980.22] Um, and then, and then we'll, uh, and then we'll kind of go back to the, you know, if you're a startup,
[980.22 → 983.00] how do we get started here? Or if you're a nonprofit, um, how would we get started?
[983.82 → 990.92] All right. So let me, let me do, um, one in particular that is a, um, a, uh, something
[990.92 → 994.68] that's kind of inside of Microsoft research and then one grant recipient. So let me do a Microsoft
[994.68 → 999.68] research one. Sounds good. Okay. So there is an amazing gentleman by the name of Ran veer Chandra,
[999.68 → 1006.72] who is, um, part of Microsoft research, fabulous guy, very, very smart. He got his, uh, start doing,
[1006.72 → 1013.30] um, networking and battery technology, which is kind of cool. And he, uh, essentially there is a
[1013.30 → 1020.60] very, very hard problem whereby the year 2050, um, it is predicted that we are, are the pace of
[1020.60 → 1025.34] the amount of food that we can grow is, is just not going to be sufficient in, in no way.
[1025.34 → 1026.64] I've actually heard that separately.
[1027.12 → 1032.82] This is, uh, I think it was, uh, spoken at the meeting of the United Nations in 2009. Uh, someone put
[1032.82 → 1037.04] forward something that it was, uh, we would need to essentially double our current rate of food
[1037.04 → 1039.96] production if we're going to be able to feed everyone with the world's growing population
[1039.96 → 1045.94] rate. And so like he started out like really trying to think about that problem. Like how could we
[1045.94 → 1050.58] solve that? Like what, what kind of things can we do? And so he hit on the idea of precision
[1050.58 → 1054.40] agriculture, and I wasn't familiar with this prior to joining the team. So let me explain it for the
[1054.40 → 1058.40] folks who, who aren't familiar. So the idea behind precision agriculture is instead of,
[1058.78 → 1062.62] for instance, like homogeneously watering a field where every part of the field gets
[1062.62 → 1066.80] the exact same amount of water, like we traditionally do with the large sprinklers and such, um,
[1067.18 → 1071.46] precision agriculture or precision irrigation, for example, is let's only water the parts that
[1071.46 → 1075.00] actually need water because if there's little dips in the field or things like that, water runs down.
[1075.38 → 1080.68] Some of the field may get more water than others. And so obviously that seems pretty easy to do,
[1080.72 → 1084.78] right? Because you know, there's, um, if anyone's been on, does any IOT work and has ever played with
[1084.78 → 1089.42] these things, you can go to adafruit.com or whatever and get little moisture sensors that you can put in
[1089.42 → 1094.84] the ground. So pretty, pretty easy to do. But, um, so I was talking with Ran veer, and I'm like,
[1094.86 → 1099.52] okay, this seems doable. And then he told me it actually worked out to about a thousand dollars
[1099.52 → 1104.14] a sensor to do this. And I was like, you must be kidding me here. Look at this website. It's much
[1104.14 → 1107.54] cheaper than that. So what was driving that cost up? Great question. So the actual sensor,
[1107.62 → 1112.22] of course, is only like tens of dollars. Um, my next guess was maybe power, right? But it turns out
[1112.22 → 1116.62] we use solar panels to drive in and power. And those little chips don't take that much. Um,
[1116.62 → 1121.80] anyway, a little, um, little, uh, board doesn't take that much power anyway. And a solar panel is
[1121.80 → 1126.26] like 50 to a hundred dollars us. So still nowhere in the neighbourhood of a thousand. Turns out where
[1126.26 → 1131.98] that thousand dollars is coming from is actually connectivity, getting data from the actual farm
[1131.98 → 1138.24] into the cloud. And so there are actually a couple different ways, uh, that we can handle that. Um,
[1138.32 → 1141.80] a lot of times when you think about it in this farm, if you have ever driven through a more, uh,
[1141.80 → 1145.96] rural area and your cell phone coverage kind of goes out, right? Um, there's the cell phone
[1145.96 → 1149.54] coverage tends to be not be quite as good cause there's not the population to support it.
[1149.82 → 1153.06] And then there's also, um, when you think about Third World countries and stuff like that,
[1153.06 → 1157.40] where the wireless access, um, may not be as good or Wi-Fi is good, but the problem with Wi-Fi
[1157.40 → 1162.42] is that it only stretches so far. Like I know when I'm going to get my kids from the bus stop across
[1162.42 → 1166.02] the street, I'm literally right across the street from my house and can't reach the home of Wi-Fi.
[1166.24 → 1170.24] You lose it. Right. So you, if you're dealing with like hundreds of acres of farmland,
[1170.24 → 1174.02] like Wi-Fi is just not, you have need to repeat a million repeaters. So it's just not feasible.
[1174.02 → 1178.18] So, um, there's actually two different ways we've solved this problem. One of them
[1178.18 → 1183.56] use machine learning and one of them uses cutting edge, uh, networking technology. So the first
[1183.56 → 1189.54] one using machine learning is you can actually reduce the number of sensors that you need by,
[1189.54 → 1195.96] um, by putting sensors in, in fewer places and then augmenting that with either drones flying
[1195.96 → 1201.86] overhead or other ways of collecting aerial imagery. And then, uh, you can feed a machine
[1201.86 → 1206.68] learning algorithm, both those aerial images, and the data from the sensors that you do have.
[1206.68 → 1211.66] And from that, be able to extrapolate the values of the entire field. So it uses essentially
[1211.66 → 1216.90] conceptually what the machine learning model is using is, um, visual smoothness as well as spatial
[1216.90 → 1221.24] smoothness. So the idea that two things that are close together are likely going to have similar
[1221.24 → 1228.98] values and then things that have similar colour. So think of if we, um, if we have a, uh, like an
[1228.98 → 1233.68] a patch of farmland that's darker because it's been freshly watered and another patch that's darker,
[1233.76 → 1238.10] those, you know, two, both dark patches might indicate that they have similar amounts of water
[1238.10 → 1242.14] applied to them. So that sort of thing. So that's, it makes me think of topographical maps,
[1242.28 → 1248.68] contours on them, maybe different colours. Yep. Yep. That also, yep. So, so having that information,
[1248.78 → 1252.02] feeding both of those in, we have a machine learning model that's based on Gaussian processes
[1252.02 → 1255.16] that can extrapolate and then give you essentially, here's how much water in the field.
[1255.16 → 1258.72] So that's, that's one example. The other part of it that's really cool, not as machine learning
[1258.72 → 1264.24] related is that, um, uh, he also brought in his, his old networking background to do, um,
[1264.60 → 1270.22] the concept of television white spaces. So this is really cool, Chris. So he's actually using it.
[1270.22 → 1273.76] And for the audience, she's leaning in, and she's so excited about this.
[1273.76 → 1280.52] I'm so excited. So this is the idea of using unused television channels to be able to send data
[1280.52 → 1284.34] packets over there, like your own internet. Okay. Sure. So think about it. So in a, uh,
[1284.34 → 1288.68] a television station can broadcast very, very far because it's, um, lower spectrum, right? So
[1288.68 → 1293.08] those frequencies are going to stretch further. And so you can actually use one television right
[1293.08 → 1298.50] spaces router, and it can, you know, stretch miles and miles and miles, right? Tens of miles. Right.
[1299.34 → 1302.60] So that's a really, really cool thing. And a lot of times when you get to these, um,
[1302.80 → 1306.68] either Third World countries or rural areas where we're setting these things up, um, there's a lot
[1306.68 → 1310.14] of unused television stations. So a lot of empty bandwidth there. So you do have to work with the
[1310.14 → 1313.24] local government. You can't just start broadcasting things on television stations, right? It is very
[1313.24 → 1319.08] regulated, but if you work with the government, you can actually, um, send data over these, uh,
[1319.08 → 1322.42] television channels. And so that's the other part of what they're doing. And that's also
[1322.42 → 1326.84] driving down the cost as well. That sounds great. It's such cool work. So it's, it's amazing stuff.
[1326.92 → 1330.74] So that that is called, um, farm beats is the name of the project. And I can provide a link to that in
[1330.74 → 1335.90] the show notes as well. Okay. And then let's talk about one of our grant recipients, our fabulous AI for
[1335.90 → 1340.82] earth grant recipients. So I love all of them, and they're all doing such cool work, but one in particular
[1340.82 → 1345.92] that would be fun to talk about is, um, in a company called wild me and their platform is something
[1345.92 → 1352.66] called wild book. And so the problem they're trying to solve is to be able to recognize individual
[1352.66 → 1358.92] animals. Um, so not just, you know, zebra, not a zebra, but rather this is Iggy, the zebra versus
[1358.92 → 1364.48] Zoe, the zebra, like zebra five, seven, one, five, you know, kind of thing. So, um, and this can be really,
[1364.58 → 1368.78] really helpful because when you think about it, there was actually a an amazing article in, well, not an
[1368.78 → 1373.98] amazing, a very sad article in National Geographic a while back where, um, some folks were actually
[1373.98 → 1381.44] trying to tag this rare, um, whale in the Pacific Northwest. And they actually botched the tagging
[1381.44 → 1385.44] job and ended up killing the animal, which was the exact opposite of what they wanted to accomplish
[1385.44 → 1389.80] by tagging it. Um, that it was such a rare animal. They wanted to track it and all that sort of thing.
[1390.18 → 1394.98] And so the idea is, can we use computer vision to do that instead? And that can lead to a whole,
[1394.98 → 1399.66] when you understand like the animal population that can drive so many benefits, you can estimate
[1399.66 → 1405.08] population densities, you can, um, uh, track migration patterns, all kinds of cool things.
[1405.08 → 1410.14] And so, so how, and, and let me, as you answer this, how are they going to use computer vision
[1410.14 → 1417.84] to accomplish this particular task? Great question. So they are taking, um, uh, images, um, and training
[1417.84 → 1423.14] essentially a wild book per animal. So when you think about it, uh, I don't know if you've ever heard
[1423.14 → 1427.50] this, but you know, humans have very individual fingerprints where each of us have a unique
[1427.50 → 1431.86] fingerprint. Well, with zebras, their stripe patterns all are unique. I've heard that as well.
[1431.88 → 1436.00] And then same thing with giraffes, actually the spot patterns on their neck, their long necks
[1436.00 → 1439.82] have uniqueness. And same thing. Really? I didn't know that. Yeah. That. And then like the shape of,
[1439.92 → 1447.06] uh, um, uh, an elephant's ear, um, the spot patterns on cats. So they've actually created a wild book
[1447.06 → 1453.94] for a lot of different large mammals, and they train it with this kind of, uh, data. And then,
[1453.94 → 1458.30] um, and then they're able to recognize individual animals. So it's a very, very cool process,
[1458.30 → 1464.72] but here's where the story goes from good to great. Okay. I'm waiting. They actually are then
[1464.72 → 1471.60] augmenting their data using social media. So the idea is let's say, so one of their, one of their wild
[1471.60 → 1478.08] books is, um, whale shark.org. That is the wild book for whale sharks. And, um, let's imagine that
[1478.08 → 1482.68] some, you know, random person goes on a whale watching trip, and they see whale sharks, and they're
[1482.68 → 1487.76] taking videos of them, and then they're posting them to YouTube. Well, wild book has an intelligent
[1487.76 → 1492.74] agent that wakes up every night at 10 PM, and it searches the internet, and it looks on these social
[1492.74 → 1497.32] media sites. And then it will find instances of people using just like natural language processing.
[1497.32 → 1502.48] It can find, or just regular search. You can find people who are, um, posting about whale sharks.
[1502.66 → 1507.50] Sure. And then they're, um, extracting frames from those videos and then running their object
[1507.50 → 1512.20] detector to find the whale shark in the object and then classifying those things and recognizing
[1512.20 → 1516.88] that individual animal. So they're finding both new whale sharks that way that researchers haven't
[1516.88 → 1521.54] been exposed to before. Isn't that great? Isn't that so much better than using Instagram to show your
[1521.54 → 1525.84] food? Yeah. Like what an innovative use of social media. I could be on a vacation with my family.
[1525.84 → 1531.20] We're on a boat. We see a whale shark. We take a picture. Furthermore, we, we tweet it. And then later on that
[1531.20 → 1535.94] evening it comes and not only is it able to detect it, but it's also able to know exactly which
[1535.94 → 1540.44] individual in the population we're looking at. Is that correct? That is correct. That is correct. And
[1540.44 → 1544.56] they actually give you a little comment, which is kind of cool. The agent will, it's looking not
[1544.56 → 1548.74] only for the animal, but it also wants to know the, the when and the where. So when did they see that
[1548.74 → 1553.58] and where did they see it? And so they're actually using some NLP actually on the, on the, like the YouTube
[1553.58 → 1558.80] page itself, for example, if it's posted, it said last month we saw this, and you get the post date
[1558.80 → 1562.58] there, and you can do some, their NLP is good enough to like to do the math and figure out, okay,
[1562.58 → 1567.06] it's approximately this time. And then where, and they'll again, try to extract that from the video.
[1567.18 → 1572.28] But if they can't, it will, this is all automated. It'll post a comment and say, oh, where did you see
[1572.28 → 1577.46] that? Or they'll take whatever information is missing, post the information and then get that data
[1577.46 → 1582.66] back. And then, and then they actually post a little comment saying, Hey, you know, your picture
[1582.68 → 1586.54] was able to help science and help us help this conservation effort. And then they'll point to
[1586.54 → 1592.30] the whale, the page of that particular whale that they've contributed images to, which is really,
[1592.42 → 1596.58] really nice. So YouTube is a great one. Cause that's, that all is public domain by default.
[1596.68 → 1601.00] Any public things are shared based on their licensing. So anything like that, where it's a public image,
[1601.00 → 1606.84] they can track those kinds of things and then be able to utilize that for data. But it's really cool.
[1606.84 → 1610.26] Cause then you can like go click on it and be like, oh, there's my whale shark that I saw.
[1610.42 → 1614.44] And they, they have some neat stuff where they allow people to nickname them. So you can like
[1614.44 → 1618.90] give your whale shark a name and stuff like that. And then you can see all images, other images that
[1618.90 → 1623.06] people have taken of them. There's like an adept a whale feature type thing. And then it actually
[1623.06 → 1627.20] shows, oh, and this is why they call it wild book. They call it like the Facebook for animals
[1627.20 → 1632.44] because it actually shows co-occurrence charts. So the social graph of this whale has been seen with
[1632.44 → 1637.22] these other whales. So you can see exactly kind of the, um, some of the, um, you know,
[1637.22 → 1641.08] parent child type relationships. So you get the whole graph of the relationships that their whales
[1641.08 → 1644.84] have with each other. Exactly. That's pretty amazing. So isn't that neat? And then you can
[1644.84 → 1650.08] actually see, um, using when or the where, sorry, information you can see, um, like migration
[1650.08 → 1654.94] patterns of individual whales. It's phenomenal stuff. It just, oh, it gets me so excited.
[1655.20 → 1661.30] So all this sounds incredibly fascinating. Um, I, I, I'm an outdoors person, so I'm particularly
[1661.30 → 1665.96] interested, uh, in, in covering this. And, uh, and frankly, this may be the first practical AI
[1665.96 → 1670.26] episode that my six-year-old daughter wants to listen to because she's really into animals and
[1670.26 → 1675.96] stuff. So, um, I, I suddenly have a hook for the family on this. So like if you are out there,
[1675.96 → 1682.24] uh, and you are interested in engaging you guys, um, I guess there's a lot. One of the big
[1682.24 → 1687.66] challenges obviously is data sets. Um, do you have any recommendations on where people can find
[1687.66 → 1691.02] data sets that will help him? Do you all have a repository? Are there good go-to
[1691.02 → 1692.34] sources that you recommend?
[1692.34 → 1698.44] That is an awesome question. 10 points to Gryffindor. So we are actually in the middle
[1698.44 → 1703.44] of that process right now. So currently we are collaborating with several other organizations
[1703.44 → 1709.50] and we established something. Um, if you go to HTTP colon whack, whack Lila dot science,
[1709.50 → 1715.58] um, that is a repository of camera trap data, which one of my esteemed colleagues, um, Dan Morris
[1715.58 → 1721.28] is very passionate about camera trap imagery. And so he started putting together this data
[1721.28 → 1727.72] set, um, on Lila dot science. And the, um, the Lila is actually a reference to the library
[1727.72 → 1734.38] of Alexandria, uh, which is kind of, kind of cool. So it is, um, that is available today.
[1734.38 → 1739.36] So you can go and I, there are, um, several data sets that contain lots and lots of different,
[1739.36 → 1744.60] uh, animals and imagery there. So that's one, um, one great start that we have right now.
[1744.68 → 1748.96] Okay. And then we're trying to do even more work. Um, I would love to be able to hope we're,
[1748.96 → 1754.10] we're currently, um, in the process of trying to host more and bigger and better data sets.
[1754.56 → 1759.72] So, uh, that is work in progress. So hopefully this time next year, I will have even more great
[1759.72 → 1765.60] data sets to share with you. But in the meantime, um, Kaggle is also a wonderful, uh, resource.
[1765.60 → 1770.18] It always is. Oh my God. I love Kaggle. Isn't it the best? It is. So Kaggle is another great
[1770.18 → 1773.88] resource for, um, they, they always have AI for good type challenges on there. I mean,
[1773.88 → 1779.18] currently right now there's some great earthquake predicting data that's there. There's an identity
[1779.18 → 1784.10] a whale type data, which is very similar to like the wild me work, um, is available right now.
[1784.18 → 1788.56] There's a data set on that. So there, there are so many cool sources for data sets, but we're trying
[1788.56 → 1792.58] to compile even more of that as part of our AI for earth mission as well. So we have a start,
[1792.66 → 1795.28] but we want to go even further with that. Gotcha. So
[1795.28 → 1801.56] um, what types of, uh, deep learning algorithms do you find that are the most common that you use
[1801.56 → 1806.46] with people? Are there areas in particular that are on the rise or that you're most interested in,
[1806.54 → 1812.28] you know whether they be CNNs or Gans or, or even if, if we move over, uh, into reinforcement
[1812.28 → 1815.62] learning and such, what, what are some of the things that you're seeing out there that are used?
[1815.62 → 1821.76] Great question. So in particular on the AI for earth space, a lot of the problems revolve around
[1821.76 → 1828.96] computer vision. Um, it's the idea, a lot of things, um, just seem to reflect, okay, given like this,
[1829.20 → 1833.70] um, data, maybe there are cameras in a farm or something, and we want to recognize, um,
[1834.04 → 1839.80] pests on leaves like that sort of thing is, is one example, or we're trying to recognize like an
[1839.84 → 1843.58] in camera trap. I should mention, I haven't defined camera trap. So what that means for those who aren't
[1843.58 → 1849.26] familiar is, um, mounted cameras that are usually enclosed in waterproof casing that may be mounted
[1849.26 → 1855.58] in trees or other remote places. Um, we've worked with the, um, snow leopards, for example. Uh, and
[1855.58 → 1861.30] those guys are so elusive. They're so quiet. They're so hard to, um, spot. There's one researcher
[1861.30 → 1868.10] that devoted his life to, um, snow leopard research, and he was up in the mountains, like living there
[1868.10 → 1874.24] in the area, only saw a snow leopard twice in 11 years. Really? It's insane. So you really need
[1874.24 → 1878.82] camera traps to be able to do that where they move in front. Exactly. They move. Exactly. Only the
[1878.82 → 1882.34] problem with camera trap, the thing that's historically challenging about camera trap data
[1882.34 → 1887.42] is that camera or animals don't line up nicely for their selfies, right? They don't, they're not in
[1887.42 → 1890.90] the middle. So you get somewhere, it's like an animal sniffing, and you'll get like a closeup of
[1890.90 → 1896.58] a nose that's kind of checking out the, the mounted camera itself, or you'll get them very far away. Or
[1896.58 → 1901.18] if it's at night, which is when a lot of animals are most active, you'll see like two eyes squinting out of
[1901.18 → 1904.94] the darkness, but it's hard to tell what they are. So there are all kinds of fun challenges with
[1904.94 → 1911.20] camera trap data. And so, um, that in particular is, is one, one thing, but that, that's very much
[1911.20 → 1915.80] a computer vision problem. So of course, computer vision, um, CNNs are a big, you know, convolutional
[1915.80 → 1920.48] neural nets are a good way to go there. So there's a lot of work, um, in, in object detection and
[1920.48 → 1926.46] computer vision, um, also with climate. So given satellite imagery, for example, spot the little swirl
[1926.46 → 1932.88] that means like a hurricane is going to form or something like that. Or, um, in the, um, you know,
[1932.90 → 1937.66] in the water space, there's like monitoring plastic flow into the oceans, which another group ocean
[1937.66 → 1944.90] cleanup is doing that we've worked with. And they have like mounted, uh, um, cameras on that flow on
[1944.90 → 1949.58] bridges. And then as water flows underneath, they're tracking plastic flow that going into the ocean.
[1949.58 → 1954.44] So, and being able to tell the difference between a water bottle and a fish can actually be, or pieces of
[1954.44 → 1958.18] plastic is actually harder than you think. Because they're both kind of clear or silverish in the
[1958.18 → 1962.62] water and that sort of thing. So it's just an interesting problem. As a side thing before you
[1962.62 → 1966.74] go into, do you actually have a project associated with that this time or is that there is. So the
[1966.74 → 1971.20] ocean cleanup has done a lot of great work with them, and they actually came to Microsoft for one of our
[1971.20 → 1976.70] hackathons and have partnered with some of the folks, uh, here as well, but they are doing amazing
[1976.70 → 1981.76] work in terms of tracking plastic flow into the ocean. And yeah, I mean, everyone is hearing in the
[1981.76 → 1986.88] news these days about the, the, the giant amount of plastics, particularly in the Pacific, uh, where
[1986.88 → 1990.42] that is, and you know, what, what are, what's being done to help that. So it's fascinating to
[1990.42 → 1994.72] hear about something. Ocean cleanup is a great organization doing exactly that. I love hearing
[1994.72 → 2000.28] about, uh, about how these technologies that we love so much are being used to solve these real
[2000.28 → 2007.36] world problems, uh, that we actually hear about in the news or watch TV on. So, um, I guess, uh,
[2007.36 → 2012.32] other than, uh, than CNNs, uh, is there much room for things like natural language processing or
[2012.32 → 2017.94] capsule nets or GANs or anything? Great question. So, um, I've seen, I'm actually would love a good
[2017.94 → 2023.96] RNN problem. So if anyone has any, please let us know. We have a few of them. There's one where people,
[2023.96 → 2031.14] um, some, one of our AI for earth grant recipients is doing some work, um, using like, uh, working
[2031.14 → 2037.32] through text to be able to find what makes a difference to people the most. So, um, for example,
[2037.36 → 2041.58] like, let's pretend there's all these like flyers or, uh, communications that go out to people,
[2041.58 → 2046.64] what actually inspires them to act to prevent climate change, that sort of thing. Um, and so
[2046.64 → 2051.92] they're doing some NLP work around that, trying to find the most motivating things, um, for people.
[2052.00 → 2056.54] So I know that's one particular project. Um, and there's a couple like chatbot type scenarios,
[2056.54 → 2062.00] but there's not as many RNN things as you would think. And then, um, GANs, I am just in love with,
[2062.00 → 2066.20] as I think everyone is. Yeah, they're, they're, they're the hotness right now. It keeps expanding.
[2066.20 → 2071.30] There's so many more use cases. Oh my gosh. Oh my gosh. Oh my gosh. Yes. So if anyone has a good
[2071.30 → 2075.20] GAN project, let me add it. Like, I'd love to see a little, a few more GAN projects here, but
[2075.20 → 2081.46] I don't think there's a few, there are a few GAN projects, but again, um, it's primarily dominated
[2081.46 → 2086.04] by, um, convolutional neural networks and, and, uh, computer vision problems. I will say on reinforcement
[2086.04 → 2091.62] learning, I think that is another huge area for AI for earth in particular, because if you can do
[2091.62 → 2096.76] things like modelling climate change, um, and then tweaking different variables to see, okay, running,
[2096.76 → 2101.42] you know, using reinforcement learning to run simulations and see, you know, as I toggle these
[2101.42 → 2105.88] different things and I try these different actions, what is going to make the most impact and help us
[2105.88 → 2111.08] fight climate change, um, the quickest. And so that's a great area for, for reinforcement learning
[2111.08 → 2115.68] as well. That's fantastic. You know, the, the thing that I love about all these stories you're telling me
[2115.68 → 2120.74] is that, um, you know, historically we've, we've kind of, we've gotten into data science and then
[2120.74 → 2125.70] we might, we might do environmental things, you know, on the weekend or, you know, as a hobby or,
[2125.70 → 2131.12] or donating our time to charity. Uh, but it's, it's for most people kind of separate activity.
[2131.12 → 2136.84] Right. I love the way your team has brought this together to where you can both have a career in
[2136.84 → 2142.32] this field and also do tremendous good for the world. Um, and, and, and I think that is, uh,
[2142.32 → 2147.52] as people realize that Microsoft is there supporting, uh, organizations and people that
[2147.52 → 2152.78] want to do this work, I think it's a fantastic whole new way of using, uh, artificial intelligence
[2152.78 → 2157.90] and machine learning technologies to do this. Absolutely. Absolutely. You had asked earlier
[2157.90 → 2162.38] about how people could get started. So if you go to, yes, if you go to the AI for Earth webpage,
[2162.64 → 2167.40] please come join us, come help us save the world. Cause, um, my background is in machine learning
[2167.40 → 2172.08] and AI, but, and so I'm, uh, there are some folks on the team who are stronger at the Earth side.
[2172.08 → 2175.34] Some people are stronger at the AI side. I'm definitely one of the AI people. And I'm just
[2175.34 → 2181.18] in awe of what people are doing. Um, these, these amazing environmentalists and conservationists
[2181.18 → 2187.42] who are working so hard on these, these huge problems that face our Earth. And so, um, if
[2187.42 → 2191.44] there's anything, you know, Microsoft can do to help, like I would love to support folks.
[2191.44 → 2197.68] So people are welcome to apply for grants. Um, um, again, we, we, uh, evaluate all the applications
[2197.68 → 2204.24] every quarter. So I think it's January, April, what is it? October. And I'm forgetting, but every,
[2204.32 → 2209.56] every four months we, we evaluate, uh, proposals and then, um, uh, give things out, um, or apply
[2209.56 → 2213.98] or award grants. We have a couple of different grant types. Um, one of them is just standard
[2213.98 → 2218.62] Azure compute hours. So just getting some cloud computing time. Um, we actually have a data
[2218.62 → 2223.44] labelling grant as well. Now where, um, if you have a great data set, but you need to pay someone
[2223.44 → 2227.12] to get it labelled. And sometimes it may be a specialist. It's not, you know, something that a
[2227.12 → 2231.60] Mechanical Turk type thing can, can solve because you need very specialized knowledge of climate,
[2231.72 → 2236.54] for example, to be able to read these satellite things to, to label it properly. And so we actually
[2236.54 → 2241.18] are providing funding for, for data labelling as well. So that before you even go on, that is
[2241.18 → 2246.50] fantastic because I know in real life at the companies that I have worked for, that has been one of the
[2246.50 → 2251.34] the biggest problems about getting a project off the ground is not only getting the data set, but then
[2251.34 → 2255.96] after you have it, getting it labelled in a useful way so you can use it. And, and at times that can
[2255.96 → 2261.60] slow down a project by weeks or months to get that done. So I love that. I completely am with you.
[2261.66 → 2265.12] You know, for, for those machine learning folks, I mean, we, everyone listening to this can probably
[2265.12 → 2269.62] relate. Like data is like, that's the hard part, right? The algorithms are the easy part. It's, uh,
[2269.86 → 2274.12] getting the data is and getting it in right format. All that stuff is usually 85% of the work. So,
[2274.12 → 2278.72] um, I completely agree. We're on the same page there. It's how can we help people if they're,
[2278.72 → 2282.66] if you kind of think of it as like a pipeline of, okay, we start with some data, and then we need
[2282.66 → 2286.54] to get to this stage and this stage, we're trying to find things to help at each stage of that pipeline.
[2287.04 → 2291.50] And so the data labelling grant is essentially, how do I get from just having some data to actually
[2291.50 → 2296.38] having data that is useful that a machine learning algorithm can consume or supervised machine
[2296.38 → 2302.00] learning algorithm, I should say. Um, yes. And then we provide education as well. Uh, we have some
[2302.00 → 2308.14] online resources that we've compiled for our grant recipients. Um, I hold office hours monthly so that
[2308.14 → 2313.62] people can just show up and ask questions. And then we also twice a year have an AI for Earth
[2313.62 → 2319.18] summit where we bring some of our grant recipients, um, to Redmond, Washington, where Microsoft's
[2319.18 → 2324.74] main campuses, and we give them, um, training. So it's like a day of training. There's networking
[2324.74 → 2329.86] opportunities, um, which is great because if someone is working on hard agricultural problems in
[2329.86 → 2334.50] India and someone else is doing it in North Carolina, great. Like we see people coming together
[2334.50 → 2338.62] and collaborating and sometimes sharing data sets and stuff for getting even better results.
[2339.12 → 2344.96] So it's really amazing to see the, the, you know, the power of what we can do collectively.
[2345.36 → 2349.20] I would love to be able to see that and actually talk to these people with this passion firsthand.
[2349.40 → 2351.14] Oh, you should maybe come do a podcast there.
[2351.28 → 2357.36] I may come do that. Be careful what you offer there. Um, so I guess, uh, I, you know, as had been
[2357.36 → 2362.32] mentioned before, we are at, uh, applied machine learning days in Switzerland at this conference.
[2362.32 → 2366.52] And you, in just a few minutes are about to go up and give your keynote. Uh, could you tell us
[2366.52 → 2370.28] quickly a little bit by the time this airs, it'll, it'll be past that, but could you tell us a little
[2370.28 → 2374.68] bit about what you're going to talk about? Yes. So, uh, what I'm going to do is I'm going to try to
[2374.68 → 2379.28] cover, um, kind of the basics of the AI for Earth program, basically not spend too much time on that,
[2379.34 → 2383.02] but just let people know that it's a resource that's out there. Cause the worst thing is when there's
[2383.02 → 2386.50] this free pot of money that people don't know about, right? So just spread awareness of the
[2386.50 → 2391.90] the grant program that it exists. And then I'm just going to tell, um, a couple of stories of AI for Earth
[2391.90 → 2397.00] grant recipients and what they've done. So we'll talk about wild me. We'll talk about farm beats,
[2397.00 → 2400.36] um, which we've already spoken. And then the final thing I'm going to talk about is, um,
[2400.36 → 2405.10] another project, project premonition, which also started with Microsoft research. This one is very
[2405.10 → 2413.36] cool as well. It's focused on how can we predict outbreaks of disease before they happen? So think
[2413.36 → 2418.18] about like Zika virus and West Nile and cow disease and some of these things that we've seen in recent
[2418.18 → 2423.20] years. So the idea here is, is there a way we could get out in front of that and be able to predict
[2423.20 → 2429.28] these things before they happen? And, um, the way this is so cool. So the principal researcher on this
[2429.28 → 2434.74] one is a guy by the name of Ethan Jackson. Okay. And the idea behind this one is what if we take
[2434.74 → 2439.64] advantage of little data collectors who are out in the environment already collecting random blood
[2439.64 → 2446.72] samples? And those are of course mosquitoes. Oh, yes. If you can collect, uh, data, basically mosquitoes,
[2446.72 → 2450.76] use them as data collectors. They're collecting all these random blood samples, and they bite humans,
[2450.86 → 2455.00] they bite animals. They, you know, they're collecting essentially discriminant. Exactly.
[2455.16 → 2459.98] And so they're getting a great random sampling of the environment, and I'm feeding off of these
[2459.98 → 2465.40] various hosts. And so what we do is we actually have, um, there's two kind of big contributions
[2465.40 → 2470.26] of this work. Number one is a smart mosquito trap that can selectively just trap mosquitoes. Other
[2470.26 → 2475.86] insects can, um, go in and go out of the trap. Like they'll head in, check out the lure and then fly away.
[2475.86 → 2479.88] And then there's little trap doors and they only close if it's a mosquito. And we can actually
[2479.88 → 2484.08] differentiate between species of mosquitoes as well. Because I did not know this prior to this work,
[2484.18 → 2488.62] but, um, it's actually like the Aedes aegypti, uh, species of mosquito is the one that's responsible
[2488.62 → 2494.12] for Zika. And then there's a different one. The Culex is responsible for, um, West Nile and all these
[2494.12 → 2498.38] other things. It's, it's fascinating. And so we can actually differentiate between those two species of
[2498.38 → 2504.12] mosquito, um, if we need to focus on one disease or the other, which is very cool. And 75%
[2504.12 → 2510.40] of these large diseases actually originate with animals and then come to us. And I know a lot of
[2510.40 → 2514.90] them have these cutesy names of like mad cow disease or avian flu or some of these other things,
[2514.90 → 2518.90] but there are a lot of them outside the ones with the cutesy names do actually start with animals
[2518.90 → 2522.54] and then spread to us. So if you can catch them while they're still at the animal stage, that's
[2522.54 → 2526.90] great. So the first thing is the smart mosquito trap, which uses machine learning to be able to
[2526.90 → 2530.24] differentiate mosquitoes from other insects. The second big contribution of this work
[2530.24 → 2535.66] is our metagenomics pipeline. And so what we've done there is now that we have those mosquitoes,
[2535.66 → 2540.68] we can actually take the blood meal they've consumed, reverse engineer it, and be able to tell
[2540.68 → 2545.64] what host animal it came from and what diseases they carry. And then from that, you can actually
[2545.64 → 2549.84] get a sense of what diseases are there and then recognize them before the outbreak happens.
[2550.02 → 2550.58] That's amazing.
[2550.88 → 2552.84] So cool. Such an amazing work.
[2553.02 → 2557.40] I am looking forward. I'm going to come watch your talk. I can't wait to see it. And, um,
[2557.40 → 2562.84] I wanted to, uh, finish up by saying, how can people listening, reach out to you or to the
[2562.84 → 2565.98] organization, um, and start that conversation with you?
[2566.56 → 2572.26] Great question. I am on Twitter. Uh, so you can find me at Jennifer Marksman on Twitter. Um,
[2572.26 → 2580.92] I have a blog as well, um, which is blogs.msdn.microsoft.com slash Jennifer. And then the AI for
[2580.92 → 2586.84] Earth team has a, um, has a great website and there's information about the grant program and such on
[2586.84 → 2591.70] there. So I, and some of our, um, amazing grantees is all available on the AI for Earth website,
[2591.70 → 2599.62] um, which is microsoft.com slash AI for Earth. And then you can also, um, contact us. I think
[2599.62 → 2604.80] there's another Twitter account, Microsoft underscore green, um, which deals not just with the AI for
[2604.80 → 2609.06] Earth, but other environmental, um, initiatives, um, around Microsoft.
[2609.58 → 2613.74] All right. Well, Jennifer, this has been a fantastic conversation. Thank you very much for taking some
[2613.74 → 2617.54] time out of your day. I know you're rushing around doing a lot of stuff. Um, but it was a
[2617.54 → 2624.40] fantastic conversation. Thank you so much. Thank you. All right. Thank you for tuning into this
[2624.40 → 2629.16] episode of practical AI. If you enjoyed this show, do us a favour, go on iTunes, give us a rating,
[2629.38 → 2633.86] go in your podcast app and favourite it. If you are on Twitter or social network, share a link with a
[2633.86 → 2637.48] friend, whatever you got to do, share the show with a friend. If you enjoyed it and bandwidth for
[2637.48 → 2642.98] change log is provided by fast learn more at fastly.com. And we catch our errors before our users do
[2642.98 → 2647.82] here at change law because of roll bar, check them out at robot.com slash change log. And we're
[2647.82 → 2653.30] hosted on Linde cloud servers at a leno.com slash change log. Check them out, support this show.
[2653.42 → 2658.80] This episode is hosted by Daniel Whiten ack and Chris Benson. Editing is done by Tim Smith.
[2658.80 → 2664.92] The music is by break master cylinder, and you can find more shows just like this at change law.com.
[2664.92 → 2669.48] When you go there, pop in your email address, get our weekly email, keeping you up to date with the
[2669.48 → 2675.20] news and podcasts for developers in your inbox every single week. Thanks for tuning in. We'll see you next
[2675.20 → 2675.46] week.
