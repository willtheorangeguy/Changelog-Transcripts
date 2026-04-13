[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com, and we're hosted
[11.42 → 17.36] on Linde servers. Head to linode.com slash changelog. This episode is brought to you by
[17.36 → 23.72] DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 → 29.18] Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 → 34.74] their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 → 42.68] R, Jupyter Notebook, TensorFlow, Sci kit, and PyTorch. Use our special link to get a $100 credit for
[42.68 → 51.30] DigitalOcean and try it today for free. Head to do.co slash changelog. Once again, do.co slash changelog.
[59.18 → 68.60] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 → 74.52] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 → 78.66] and data science happen. Join the community and snag with us around various topics of the show
[78.66 → 84.48] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 → 92.96] Well, hello, Chris. How's it going today? Doing really well. How are you today, Daniel?
[93.38 → 100.48] I'm doing good. I know in one of our previous news and updates show, we started kind of going down
[100.48 → 107.20] the rabbit hole of AI and art. And I'm really excited today because we have Brett Taylor here with us
[107.20 → 115.88] from Mozilla. And he's really working at the intersection of AI and media. And so I'm really
[115.88 → 120.04] excited to have you here, Brett. Welcome. Thanks. Nice to be here. Hi, Chris. Hi, Daniel.
[120.42 → 126.30] Hi. Yeah. So Brett, why don't you give us a little bit of a background of how you got involved in AI
[126.30 → 129.92] and media and Mozilla? Just give us a little bit of background about yourself.
[130.40 → 136.64] Sure. I'm a documentary filmmaker is usually how I describe the work that I do. But actually,
[136.98 → 142.98] scratch that. I would call myself a documentarian. I'm kind of, you know, platform-agnostic to be
[142.98 → 151.18] nerdy. So I make documentary. I like it. Yeah. I make creative nonfiction work on the internet
[151.18 → 160.10] about the internet using the internet. So kind of a three-part trifecta there. So I've made
[160.10 → 166.10] some feature documentaries. One of them was about remix cultures called Rip, A Remix Manifesto.
[166.10 → 174.86] And that was, you know, kind of in the early aughts, you know, around 06, 07, 08, we were sort of seeing
[174.86 → 182.10] the internet become a place where kind of emerging folk culture of people taking media and
[182.10 → 187.38] remixing it, downloading it to their computer. And that whole process was really creating a lot of
[187.38 → 194.64] anxiety in traditional legacy media, but also pointing kind of a way towards a more participatory
[194.64 → 201.16] culture of the internet. So I made a documentary about that sort of period of time. And, you know,
[201.18 → 206.26] it was a really hopeful time for those of us who, you know, were involved in the internet's early
[206.26 → 213.12] days. It kind of felt like this really democratic moment where anybody who wanted to participate in
[213.12 → 219.96] the surrounding culture was suddenly able to do that much more easily and to be able to find a
[219.96 → 222.24] good kind of global audience all around the world.
[222.44 → 227.10] The internet was going to democratize everything and solve all our problems.
[227.26 → 230.34] It, wasn't it? It was like, it was just, well, didn't you do that?
[230.92 → 238.68] Well, and Nazis, you know, that's what, so yes, the internet did do this, but then we sort of saw
[238.68 → 250.18] a few cracks in the utopian kind of landscape. And around 2013, I started thinking about, you know,
[250.24 → 257.90] the ways in which the business model of the internet was leading to an increasing amount of
[257.90 → 265.36] collection of personal data about people that use the internet and sort of this creeping surveillance
[265.36 → 272.92] capitalism sort of model that was beginning to emerge as the sort of de facto, especially since
[272.92 → 278.00] in that earlier moment that I described in the internet's evolution, it was like, oh, wow. And
[278.00 → 283.34] here's another great platform, Facebook. It's going to encourage us to share everything and
[283.34 → 285.76] connect all the people.
[285.76 → 285.94] Boy, did it.
[286.12 → 290.66] It really did. They were really, perfect at encouraging us to share things. And so
[290.66 → 298.72] at that time, I had started to work at Mozilla and had created with a lot of amazing community
[298.72 → 304.86] members, a system called Popcorn.js, which was essentially a way to synchronize a piece of
[304.86 → 311.50] media, like a video or an audio file with web events. So you could say, you know, at this time,
[311.86 → 319.72] make the web page do this or pull in this piece of data or fire this JavaScript command. And I thought,
[319.72 → 325.16] what would it be like to make a documentary about online privacy that would play like a movie,
[325.16 → 331.28] but it included your data? And so that was the inspiration behind Do Not Track, which turned
[331.28 → 335.56] into quite a large documentary series that was produced with the National Film Board of Canada,
[336.12 → 341.30] several partners in France. And it did really well. That kind of played around the world. It was
[341.30 → 346.00] received a Peabody Award, which is sort of a recognition of media.
[346.00 → 346.64] Congrats.
[347.16 → 354.08] Yeah, thank you. It was fun. That year was David Letterman and the folks behind Mr. Robot and,
[354.16 → 360.30] you know, just some amazing media. And it was kind of cool to see documentary work about the
[360.30 → 366.00] internet sort of in the mix of important social issues. And so...
[366.00 → 372.28] It probably also illustrates people's genuine, like, interest and concern over the topic as well,
[372.28 → 372.84] I would imagine.
[373.20 → 377.50] And I also just wanted to note that I find it ironic that as we record this today,
[377.54 → 379.74] it happens to be election day in America.
[379.90 → 380.18] Yeah.
[380.28 → 383.56] And a lot of these issues are very top of mind as we're going through that.
[384.06 → 388.54] Yeah, that was definitely not the case when we started to make Do Not Track. But over the course
[388.54 → 394.22] of making the series, you know, it became much more relevant. Like, for instance, we had one of the
[394.22 → 398.64] episodes, the third episode was about... It was sort of like, if you look at it now, it's kind of naive.
[398.64 → 402.82] It's like, what could you know about somebody from their Facebook profile? And we're like,
[403.06 → 411.54] we found this, you know, sort of niche study by researchers at Cambridge University who feel that
[411.54 → 418.22] they're able to predict your personality based on your likes on Facebook. And that was the AI
[418.22 → 424.24] researcher, Mikhail Kolinsky, who did, who basically created this model where you could correlate
[424.24 → 430.90] person's likes on Facebook to a really high degree with their psychological profile. So it was a
[430.90 → 436.56] vetted and peer reviewed study where I think what they did was, you know, took interviews with people's
[436.56 → 442.38] family members and their friends and psychologists and sort of plotted you on what's called the ocean
[442.38 → 450.60] model, which stands for openness, conscientiousness, extroversion, I want to say agreeableness,
[450.60 → 458.08] and neuroticism. So that's your ocean model. So you exist somewhere in an axis of all of those points.
[458.48 → 463.56] And so what Kolinsky was able to do was correlate, like say, the one that we always used was,
[463.88 → 470.76] there's apparently like, if you like the dark night, that correlated really highly with a low score
[470.76 → 478.68] in extroversion, for example. And so basically, they took large group of likes on Facebook,
[478.68 → 485.22] and then did these interviews with folks and sort of said, like, here it is, I could, I could log in
[485.22 → 491.24] with my Facebook ID, and it would look at all my likes, and then say, like, here it is, you're,
[491.30 → 497.16] you're this open, or you're this neurotic, the nuts thing is, like, is pretty accurate. And so anyway,
[497.16 → 503.58] we use that, that became an API called apply magic sauce. And we use that in the Do Not Track documentary
[503.58 → 509.86] to sort of, you know, use people's personal data to sort of show how these emerging, you know, this,
[510.12 → 516.00] this is AI really, was starting to, to work. Now, then what happened after the film came out,
[516.00 → 521.32] or probably while we were making it, was this startup called Cambridge Analytica,
[521.74 → 528.98] requested the licensing of that API, they were denied by the University of Cambridge. And then they were like,
[528.98 → 534.12] well, we're just gonna basically copy their approach. And out of spite, we'll call our company,
[534.62 → 540.24] Cambridge Analytica, and the rest is history. Seems like some of us are familiar with that,
[540.48 → 546.58] that the rest of that story. Yeah, the rest of the story is poor. It's interesting, he actually has
[546.58 → 552.84] another very controversial paper, I don't know if you've seen it, but attempts to guess a sexual
[552.84 → 560.50] orientation based on a Facebook profile photo. So he, I've seen this. Yeah, he tends to create these
[560.50 → 568.58] like highly controversial, sort of mind bomb sort of studies that kind of illustrate some of the
[568.58 → 575.14] bleeding edge dragons of these emergent, like machine learning or AI systems.
[575.14 → 581.82] So is that kind of where, I mean, I know that kind of up, you know, recently in your profile,
[582.04 → 588.40] you're kind of heading up these creative media awards for Mozilla was kind of all of that
[588.40 → 591.92] you've mentioned that was kind of in the mix leading up to Cambridge Analytica and all of those
[591.92 → 596.04] things. Is that part of the driver for that work and how you got involved in that or?
[596.34 → 600.82] And also, could you take a second and just kind of describe Mozilla for anyone in our audience who
[600.82 → 604.92] isn't familiar with it? They may know Firefox, but just kind of give a quick intro as you answer.
[605.14 → 607.40] Yeah, you guys got to keep me on track too, because I can.
[608.40 → 610.88] All good stuff. This is good, man.
[611.16 → 616.30] This could be a long answer, but I'll keep it short. Yeah. So most people are familiar with
[616.30 → 626.46] Firefox, but Firefox is one aspect of the mission of the Mozilla Foundation, which is a project basically
[626.46 → 633.82] to keep the internet open and accessible public resource for all of humanity. So we're guided by a
[633.82 → 638.94] manifesto, which I would encourage anybody to check out online. Yeah. And it really comes out of the
[638.94 → 645.16] recognition that the Firefox project and the open source code is a useful instrument in the market
[645.16 → 651.16] to make sure that there is some web browser and sort of user agent that exists in the world that
[651.16 → 655.22] is independent and is not one of the... Corporate driven.
[655.22 → 664.42] Yeah, exactly. And however, we don't disparage the commercial interest on the internet, and we value
[664.42 → 669.80] independence at the same time. So Firefox is one thing that Mozilla does, but the Mozilla Foundation
[669.80 → 678.70] that I work with also does various interventions to ensure what we call internet health. So we see like
[678.70 → 684.70] the internet as an ecosystem and for that ecosystem to be healthy, we need to kind of tend it. You know,
[684.74 → 689.88] it's like, imagine that the internet was like the ocean. Well, if you want the ocean to continue to
[689.88 → 693.84] be healthy, you got to make sure people aren't polluting it or somebody hasn't overfished it or,
[694.42 → 701.04] you know, and so sometimes that requires work. And so for us, that work is giving out grants and awards
[701.04 → 707.56] to sort of promising approaches to internet health. We also have a really robust fellows program.
[707.56 → 714.50] So we support like sort of leaders in this effort to keep the internet healthy. So that could be
[714.50 → 719.62] like a policy person, like a lawyer, or it could be a technologist, or it could be an activist, or
[719.62 → 723.84] in my case, it's media makers who are trying to explain this stuff to the public.
[724.24 → 729.30] So that sounds incredibly dynamic as a mission for Mozilla because I mean, as this is evolving so
[729.30 → 734.12] quickly, then I guess it has to really keep track of new developments that are coming out.
[734.12 → 740.10] Obviously AI, as we're talking about that, how is Mozilla involved in AI? How does it use it
[740.10 → 744.30] internally? And where is it taking that? How is it choosing to participate?
[744.84 → 752.16] At Mozilla, we kind of recognize that these emergent AI systems are just becoming part of our computing
[752.16 → 756.50] environment. Like what's the quote? It's like when you're fundraising, it's AI, when you're hiring,
[756.68 → 760.94] it's machine learning. And when you're implementing, it's linear regression.
[760.94 → 767.96] I think this will say, so the have some of the, you know, best minds in engineering that think
[767.96 → 773.66] about the sort of technical infrastructure of the internet. And just a lot of the elements of
[773.66 → 780.12] this computing environment now feature some of these computing principles, you know, so trying to
[780.12 → 786.38] look at large patterns, trying to build systems that evolve over time, that's just kind of part of
[786.38 → 794.02] the way that you make software these days. And so we want those systems to have the same kind of
[794.02 → 801.12] values that we expect and push for in other aspects of the internet. We want it to be transparent. So
[801.12 → 808.72] you understand how it works. We don't want more data collected about you than is necessary. We want,
[808.72 → 815.40] you know, other engineers to be able to see the code so that they can confirm that there isn't
[815.40 → 824.94] bias in those systems. We want the internet to be built by as wide a cross-section of society as
[824.94 → 830.62] possible. So by that, I mean, it isn't just engineers in Silicon Valley who are creating these systems.
[830.62 → 837.10] They are consulting with civil society. They are consulting with, you know, potentially the groups that are
[837.10 → 842.92] evaluated by these, by these systems. So it's a really, that's a complicated answer to kind of
[842.92 → 849.20] big question is like, what does Mozilla think about AI is like, we think that it needs to serve humanity.
[849.20 → 856.14] And we think that it needs to be open and free and healthy. Okay, sign me up. I'm ready.
[856.68 → 861.50] Yeah, that's a good answer. I'm wondering if like, and maybe this is a more personal question
[861.50 → 868.64] as well. But, you know, in terms of like the current trajectory of AI, you know, as a community,
[868.64 → 875.04] as, you know, practitioners, as researchers, do you see the community, you know, embracing those
[875.04 → 880.66] sorts of values? Or do you see it, you know, kind of steering, steering in another direction that's
[880.66 → 886.30] maybe concerning to you? I think there's some really positive signs that, you know, that let's call it the
[886.30 → 893.26] computer science community is realizing that, you know, you need to think about the social
[893.26 → 899.40] implications of what you build. And that's why Mozilla is making efforts to support that. So we
[899.40 → 906.44] just launched a program to support promising approaches to ethics in computer science education,
[906.44 → 911.18] for instance. You know, if you look at what's come out of Google a lot lately, you know, there's some
[911.18 → 917.76] promising signs from both like employees and management that they recognize that there needs
[917.76 → 924.52] to be some really like bright lines that separate where artificial intelligence technology should not
[924.52 → 930.58] be monetized. Or, you know, like the examples of, you know, not wanting to have their technology used
[930.58 → 936.36] in military contracts, for example, or, you know, you're seeing a lot of employees of Amazon,
[936.36 → 943.64] for instance, not want those facial recognition technologies used in immigration or other really
[943.64 → 949.24] sensitive areas where you need a lot of public oversight and transparency and how those systems are
[949.24 → 956.66] built. I think that's happening. What maybe concerns me is the sort of speed at which all this is, is
[956.66 → 964.38] changing, and kind of feeling of that there's sort of a manifest destiny in the way that these
[964.38 → 968.54] technologies are built. So it's like, oh, yeah, any place where we could collect data, let's just
[968.54 → 975.70] collect it. And then we'll assume that there will be a use for that, that machine learning algorithm
[975.70 → 982.38] yet to be invented will solve. I think you sort of see that a little bit in the maybe what's promised
[982.38 → 992.18] to governments or cities about how, you know, they can save money or make difficult decisions at scale
[992.18 → 996.86] using machine learning or artificial intelligence. I don't know if you guys are familiar with this
[996.86 → 1004.74] report that ProPublica did on the US justice system, where some states were using machine
[1004.74 → 1009.24] learning systems to predict people's probability of recompense.
[1009.72 → 1011.80] I am familiar with it. I've read up on it.
[1012.06 → 1018.24] Yeah. And so that's like an area where it's like, you know, maybe we should just let the humans continue
[1018.24 → 1025.52] to make these decisions because it's very difficult to sort of see where exactly bias can occur because
[1025.52 → 1034.30] these algorithms are so complex. And it's so difficult to give them data that isn't collected
[1034.30 → 1041.04] in a manner that doesn't reinforce an existing bias of the past. So that's a real concern about,
[1041.16 → 1046.82] you know, these automated decision-making systems is oftentimes they just reinforce previous
[1046.82 → 1052.48] inequalities or, you know, frankly, like racist systems that have evolved.
[1053.34 → 1057.44] Yeah. In that report, you mentioned, if I recall, there was an inappropriate bias
[1057.44 → 1062.96] against African-Americans as a result of that. Correct me if I'm wrong, but I think that's what
[1062.96 → 1063.82] the result was.
[1064.04 → 1068.42] If anybody's interested, you can just look up ProPublica. The report is called Machine Bias.
[1068.42 → 1076.96] And it basically took two people that were eligible for bail. And the system basically
[1076.96 → 1083.86] predicts whether one person is going to re-offend or not. And it, two people with a very, with similar
[1083.86 → 1091.60] crimes, an African-American woman and a Caucasian man. And while the man actually had much more serious
[1091.60 → 1099.22] previous offences, the African-American woman was denied her bail because she was assessed to be
[1099.22 → 1104.64] a higher risk than the man. So now why is that? And is that because African-Americans in the United
[1104.64 → 1111.32] States are incarcerated at a higher level than Caucasian people? That's true. Does that mean that
[1111.32 → 1117.60] that woman, that specific woman is more likely to re-offend than that man? No, it does not. But the
[1117.60 → 1124.66] system assess them this way because it's looking at this history in the United States that unfortunately
[1124.66 → 1130.30] incarcerates black people at a much higher level than it does white people. And so then what happened
[1130.30 → 1137.86] in this case is the man got bail and he re-offended, and she didn't get bail, was, you know, left in jail
[1137.86 → 1143.76] for a longer period of time. And so that's just sort of like doubling down on some of the problems that
[1143.76 → 1149.48] we, that we see in these systems. So in this case, it's kind of like reinforcing problems of the past.
[1149.98 → 1156.60] Yeah. And we, we recently had a talk with Lindsay Gulag who works in, in hiring, and we were talking
[1156.60 → 1161.70] about some of the biases there as well. And, and some of these things come up very subtly, you know,
[1161.70 → 1167.44] she was talking about just the fact, you know, that you have fewer women applicants, for example,
[1167.44 → 1174.80] in software engineering positions. And so thus you have less data, you know, if only one woman applies
[1174.80 → 1180.20] for the position in software engineering and the AI for whatever reason determines that that wasn't a
[1180.20 → 1185.80] good candidate, then it can generalize to all women applying in software engineering. Right. And so these
[1185.80 → 1191.46] things come up and, and they have, they hit, have a huge impact on people's real lives. And I know that
[1191.46 → 1195.64] we're going to talk here in a second about some of the awards that Mozilla has given out recently,
[1195.64 → 1202.84] but I know that those are focused around AI's impact on society. Are these the types of impacts on society
[1202.84 → 1209.80] that you're, that you're imagining in terms of maybe a biased AI, you know, giving certain people a privilege
[1209.80 → 1216.42] or, or whatever it is, or in general, how do you kind of see the biggest impacts of AI that AI is having now
[1216.42 → 1218.28] and maybe in the, in the near future?
[1218.94 → 1225.22] Yeah, that's exactly right. This is basically the way that we framed it as projects that use this kind of media
[1225.22 → 1231.74] advocacy to highlight some of these unintended consequences of, of artificial intelligence and,
[1231.74 → 1238.06] and places where we want to be thoughtful about how we apply it. So we're, we're awarding media
[1238.06 → 1243.92] makers who are kind of exploring these topics in a way that, you know, lay people can understand that
[1243.92 → 1248.84] unlike the three of us don't think about this stuff obsessively every day. It's like for the first time,
[1249.06 → 1253.58] you know, like when you talk to people about AI, I'm sure you both get this all the time. You were like,
[1253.58 → 1258.76] to talk to somebody at a Christmas party, they'd be like, Oh, you mean like Terminator? And like,
[1258.80 → 1262.96] you know, like, you're like, you know, like problems in the future with AI, I mean, like that
[1262.96 → 1269.88] the robots are coming for all of us. And they're not. Well, maybe. And there is some real stuff
[1269.88 → 1276.42] happening right now in the world that we want to be thoughtful of. And that actually can be either
[1276.42 → 1282.48] course corrected or, you know, with intention and thoughtful design and like, the proper application
[1282.48 → 1286.82] of ethics can maybe turn out all right. We don't have to worry about a future, you know, robot invasion.
[1287.12 → 1292.40] So it's these questions of bias, but it's also, you know, I mean, I could talk about some of them.
[1292.54 → 1298.14] There's one that I'm really excited about. It's called Stealing Your Feelings by a really fun and
[1298.14 → 1304.02] funny engineer slash comedian, which is a fun mix that you don't really get. It's a perfect combo.
[1304.02 → 1310.00] I know, right? So Noah has created this project that looks at facial recognition systems,
[1310.38 → 1317.50] and specifically patents that Snapchat has recently filed to be able to do facial recognition on like
[1317.50 → 1326.18] groups of people. So what he's going to do is use the webcam of your computer to in real time,
[1326.36 → 1330.98] analyze what your face is doing while you're watching the film so that he can, you know,
[1330.98 → 1335.92] either shock you or make you laugh or make you surprised or make you angry. And the film can
[1335.92 → 1341.86] react to your emotions while you're watching it. And that sort of is the perfect example of what we
[1341.86 → 1347.58] want to do because an audience that watches it, it's not like you're just telling them that cameras
[1347.58 → 1351.86] can, you know, detect their feelings. You're showing them like their feelings will be detected in real
[1351.86 → 1355.88] time and that will change the movie. So that's one, you know, and it's like, it's not, that's not
[1355.88 → 1359.24] necessarily biased, but it's a it's an issue and would be remiss.
[1359.24 → 1359.80] A little bit creepy.
[1360.18 → 1360.74] A little bit creepy.
[1360.92 → 1363.14] Good use of masking tape on your laptop.
[1363.78 → 1368.34] Exactly. Might, might lead to, you know, duct tape flying off the shelves.
[1369.44 → 1378.30] There's a fun one called A Week with Wanda that basically simulates an AI that tries to be helpful
[1378.30 → 1384.76] in your life, but goes off the rails and starts to suggest things to you that you may or may not want.
[1384.76 → 1390.76] This one's going to be kind of all done with, it's like an episodic serialized email exchange with
[1390.76 → 1396.70] you. So the AI might one week be like, oh, I noticed that, you know, you wanted to spend more
[1396.70 → 1401.04] time with quality friends. So I went ahead and deleted like half of your Facebook friends because
[1401.04 → 1406.80] you don't talk to them anymore. So the idea of like that, this AI is being like a little bit too keen
[1406.80 → 1413.04] and too helpful. There's one called Survival of the Best Fit, which does address a lot of these,
[1413.12 → 1420.46] the issues that you were mentioning, Daniel, about biases in workplace hiring. So they want to like
[1420.46 → 1427.00] show that by simulating a job application process. Another one that I'm like super excited about,
[1427.06 → 1433.22] it's called the Training Commission, which is a it's basically like a work of creative fiction.
[1433.22 → 1441.58] Stay with me here. It's a speculative fiction from the future that is looking, that is, takes place
[1441.58 → 1449.38] when a truth and reconciliation committee is struck to see what happened with an artificial intelligence
[1449.38 → 1457.16] that basically something cataclysmic happened in, in society. So this AI, we don't exactly know what
[1457.16 → 1465.84] happened. The AI either, I don't know, did it, did it, did it assume that it needed to fix some part
[1465.84 → 1470.92] of the way that humanity was structured? Did it, what exactly happened? So we have to piece together
[1470.92 → 1477.12] what happened in this story by the events that are told to us about this truth and reconciliation
[1477.12 → 1481.72] condition. I'm, I'm murdering this one. Ingrid is going to be really sad to hear my explanation.
[1481.72 → 1487.06] And then there's, there's another great one that looks called, what do you see that exam,
[1487.18 → 1493.70] that examines the difference between what an image recognition system sees and what a human sees. So
[1493.70 → 1498.98] it uses a lot of these like edge cases of where AI systems can't understand, like when people,
[1499.28 → 1504.58] when it shows a picture of somebody wearing a mask, for example, this one mate me or eat me is going
[1504.58 → 1510.94] to be all about bias and dating apps. And it's basically like a game where you swipe right or left
[1510.94 → 1516.94] to choose which monster you want to date. And then it'll sort of show in that process,
[1517.00 → 1523.60] how quickly bias and reinforcement can lead to discrimination within this sort of dating systems.
[1524.40 → 1530.68] So Brett, I'm thoroughly interested and intrigued by all these projects that, that you just mentioned.
[1530.84 → 1537.12] I kind of have like a general question about all of these, given that, you know, Chris and I are kind
[1537.12 → 1541.88] of like AI practitioners, I guess you would call us. I'm really interested to hear your perspective
[1541.88 → 1548.74] on why you think that in this effort to explain kind of like how AI works and expose like some of
[1548.74 → 1554.46] these things like bias and other things, why it's so important to involve creative people, maybe,
[1554.72 → 1558.78] you know, artists, and like you were mentioning, comedians, filmmakers, writers,
[1559.06 → 1563.44] why it's essential that we kind of involve those people in helping us tell that story.
[1563.44 → 1571.18] I think it's really important to involve creative people because often their job is to give a
[1571.18 → 1577.18] language to things that we don't know how to talk about yet. You know, like, if you think about,
[1577.72 → 1584.24] again, if you think about your friends that aren't obsessing over these topics, when they sort of
[1584.24 → 1590.70] encounter something that we might call machine learning or artificial intelligence, where it's sort of a
[1590.70 → 1600.12] decision that they might call it creepy. They don't really know, they don't have like the contours of where,
[1600.78 → 1607.34] of how they should feel about these systems and where they might affect them. So, it's kind of like one of the
[1607.34 → 1616.58] roles of creative people is to sort of map out that landscape and also to actually map it out emotionally.
[1616.58 → 1623.96] Would this be kind of in the idea of design thinking in terms of applying that methodology to this creatively?
[1624.32 → 1626.50] That's a good way of thinking about it. You mean like...
[1626.50 → 1632.50] Kind of going and analyzing, you know, what you're trying to get to almost from scratch and then figuring
[1632.50 → 1634.98] out how this fits in. Is that where you're going with it?
[1635.16 → 1641.16] Yeah. So, it's interesting. We try to think about the impact that these projects will have with their
[1641.16 → 1646.96] intended audience, and we work with the people that we award in this way to really get them thinking
[1646.96 → 1654.42] about that. Who is this for? What change do you want to see in that person? So, you might just say,
[1654.50 → 1659.24] it's like, oh, it's for... Like, we talked to Noah about this, and he was like, oh, it's for millennials
[1659.24 → 1666.02] and I want them to feel angry. It's like, okay. So, that's going to shape how you create that work.
[1666.02 → 1671.02] You know, the platforms that it goes out onto, the sort of references that would be included in it,
[1671.24 → 1677.48] the tone, the length, all of that. And so, it's important for creative people to be leading the
[1677.48 → 1683.64] charge in that because that's their job and their work is to create a reaction in people. And so,
[1683.70 → 1691.48] we kind of need that in this sort of early days of kind of creating a multidisciplinary approach to
[1691.48 → 1697.10] responsibly building these AI systems because we need to know what people think about AI in their
[1697.10 → 1703.62] lives and what people think about machine learning. And especially if we know some of the right policy
[1703.62 → 1708.66] interventions and some of the right design questions that needed to be asked, we need to
[1708.66 → 1714.32] quickly help the public catch-up to where people at the leading edge of this stuff have been thinking.
[1714.32 → 1719.26] So, if you think about like all the, you know, the questions of bias, there are likes really concrete
[1719.26 → 1725.20] proposals of how you can design these systems, but they're not going to, they're not going to get
[1725.20 → 1729.30] traction if the public doesn't understand them or understand the urgency to them.
[1729.72 → 1735.38] So, where does that take you? So, if you, if you start getting a handle on public perception
[1735.38 → 1740.64] of these technologies and how they're affecting their lives, what do you as an artist go do with that?
[1740.64 → 1743.98] How do you take that new information and do something productive with it?
[1743.98 → 1749.94] I think it's, you know, it's not necessarily about, let me see how I want to dig into that one.
[1750.50 → 1755.64] I think this work is the most effective when the makers really understand the change they want to
[1755.64 → 1761.82] see in a, in a member of the audience. So, if you, you know, you're going back to that example of Noah,
[1761.92 → 1770.76] if you feel like you want to anger this person, then what's, what can you expect that that person
[1770.76 → 1775.98] would be willing to do once you've achieved that emotion? Is it like, oh, you want them to delete
[1775.98 → 1780.82] Snapchat or you want them to write to their member of Congress, or you want them to share it with a
[1780.82 → 1787.60] friend, or you want them to, you know, complete a quick survey. If you're able to incite the curiosity
[1787.60 → 1793.60] or the emotion that you intend, you sort of have a little bit of a window where you can get people
[1793.60 → 1794.30] to do things.
[1794.30 → 1799.58] So, if they have, at this point, a sense of awareness and some perception of that,
[1799.82 → 1804.10] that, that AI is involved, you know, going back to Noah's project where, you know, the camera's
[1804.10 → 1810.30] being used to do emotion detection based on, on facial reactions, is that, does the awareness
[1810.30 → 1814.88] itself, in other words, if you are the viewer of that show, and you're, you're looking at your
[1814.88 → 1820.32] laptop or TV with a camera on it, does that awareness change the reality that you're in? In other words,
[1820.32 → 1825.84] if I'm a viewer and I don't know that AI is being used in this and the, the movie is reacting,
[1825.84 → 1831.28] how is that different from if I'm a savvy person regarding AI? And I know that's happening with the
[1831.28 → 1835.44] camera that's looking at me right now, and I'm still experiencing, how does that change the reality
[1835.44 → 1837.42] that the, that the person is engaged in?
[1837.80 → 1843.38] Do you mean like, how is it different if they just are told that versus if they like to feel it in their
[1843.38 → 1849.36] bones? That, because we've kind of debated, uh, the, the idea of the public being aware of,
[1849.36 → 1855.30] you know, in quote, kind of how AI works and why is that important? And what, what is the meaning
[1855.30 → 1861.60] of our life when you have, uh, an educated person in the audience, and they're aware of their experience
[1861.60 → 1866.16] being shaped by AI versus someone that's not, where does it matter or does it not matter at all?
[1866.42 → 1871.90] So I think it matters. It's interesting. I was just in London at the Mozilla festival and inside the
[1871.90 → 1879.20] tube, there was all these ads for programs that would teach young people how to code. And the way that
[1879.20 → 1885.26] they were trying to get kids to do this was like presenting it as magic. It was like,
[1885.30 → 1890.62] you have this magic wand and if you know the spells, you can cast them, and you can, you know,
[1890.62 → 1895.08] make the world whatever you want. And I think that's a terrible approach because it's not magic.
[1895.08 → 1902.10] It's actually humans that make really specific and concrete decisions that lead to really specific
[1902.10 → 1907.28] outcomes. So to answer your question, I think that what the opportunity that we have to show people
[1907.28 → 1911.48] how these systems are built is to realize that like, none of this stuff is a foregone conclusion.
[1911.48 → 1918.90] If we don't like the way that these systems make us feel, or we don't like the effects that they have
[1918.90 → 1923.62] on some of the more vulnerable member members of society, there's an opportunity to change that.
[1923.62 → 1929.50] And when you see how it is working with your data or with, you know, an algorithm that's kind of like
[1929.50 → 1934.82] presented to you, and you see like, Oh, I get it. It takes these three things and compares them and then
[1934.82 → 1940.06] says, Oh, okay. These two are alike. And this one isn't alike. And you can sort of see how that can
[1940.06 → 1946.16] lead to things like confirmation bias, or, you know, you can see the system. Then you're, you're,
[1946.16 → 1951.30] you're much more likely to sort of say like, Oh, this can be changed. This, we just, these people
[1951.30 → 1955.96] are just doing it wrong. Or, you know, like in the same way that like, if you're building a bridge,
[1955.96 → 1960.86] this is how you build it. And so that it won't fall down. And so we need to, you know, add those
[1960.86 → 1965.64] principles to the ways in which you design these AI systems that like, Oh, yeah, you, you can't use
[1965.64 → 1972.34] data like that, because it's because it's clearly biased, or you just give people the clear
[1972.34 → 1978.68] understanding that none of this is to be taken for granted, it all up for design.
[1978.98 → 1984.22] Yeah, I am really glad you brought that up. Because frequently, I have this moment when I am teaching
[1984.22 → 1989.68] like corporate workshops to people that haven't done machine learning or AI before. There's this moment,
[1989.68 → 1995.12] and I, and I literally, I see it in their eyes, where it's almost like a disappointment, because
[1995.12 → 1999.94] they think that they were going to like, learn something magical and level up and be wizards.
[2000.28 → 2004.78] But they really just find out that, you know, machine learning and AI, it's, it's actually
[2004.78 → 2011.48] kind of set of well-defined functions that you execute in code. And it's really just kind of
[2011.48 → 2018.06] a way of combining those in a certain process. And it's not like, you know, you sprinkle fairy dust
[2018.06 → 2023.58] over your computer, and then the magical AI comes about. So I'm really glad that you brought
[2023.58 → 2028.32] that up. I think it's an important thing, even for technical people to realize that this isn't,
[2028.32 → 2033.38] this isn't kind of a magical thing that is outside our control. But it really is,
[2033.56 → 2037.72] it does have design behind it. You know, Daniel, I think you're totally misleading your workshops,
[2037.72 → 2041.94] though, because you walk into the classroom with the wizard's hat and the robes on and everything.
[2042.32 → 2044.74] I'm just saying, I think you're setting it. I think you're setting them up.
[2044.74 → 2048.82] Yeah, well, Brett is wanting creative people to be involved. So I do my part.
[2049.38 → 2054.22] So I was wondering, you know, from that perspective, maybe Brett, you know, there's this group of
[2054.22 → 2060.42] like practitioners like Chris and I, there's kind of researchers, and then there's maybe artists or
[2060.42 → 2067.02] designers or filmmakers or whatever it is that can help tell this story. How best do you think or what
[2067.02 → 2073.98] opportunities are there for like practitioners like us or other people to maybe lend a hand in telling
[2073.98 → 2078.66] this story along with creators or designers? Because I'm imagining like these projects that
[2078.66 → 2083.52] you're funding, maybe the lead person is like a filmmaker or whoever it is. But like you were
[2083.52 → 2088.96] talking about with the feeling recognition thing, there is a technical element to that, you know,
[2088.96 → 2095.40] has to be built and figured out. So how can we as practitioners kind of engage with creative
[2095.40 → 2097.38] people to tell these stories?
[2097.38 → 2106.04] So actually, all of these projects do incorporate some type of AI within the actual creative approach.
[2106.04 → 2114.00] So they all actually have to have a real algorithm that does the sort of creative piece within it. So
[2114.00 → 2118.74] almost all of these, these folks that we're supporting are kind of these hybrid folks that are
[2118.74 → 2125.04] creative people and have a an ability to, you know, tinker in engineering. Having said that,
[2125.04 → 2131.88] it's like, there's one that's really fun project is called do not draw a penis. And this is basically
[2131.88 → 2140.02] a comment on the sort of algorithmic censorship process that you see in systems like YouTube or
[2140.02 → 2146.92] other kind of user generated content systems, because all those systems are now applying machine
[2146.92 → 2152.28] learning to ensure that nothing bad happens on, on these platforms. They also, right?
[2152.28 → 2154.60] Like nudity detection and certain things.
[2154.60 → 2160.40] Yes. They also, it has to be noted, employ thousands of people, unfortunately, to have to
[2160.40 → 2166.52] look at a lot of those images and so that we don't have to. And they also employ some of these systems.
[2167.04 → 2174.08] Now, this particular project is basically, it presents you with a blank canvas, invites you to draw
[2174.08 → 2179.18] whatever you want. And knowing the internet, some people are going to draw, guess what? Penises.
[2179.18 → 2186.38] And so the program will basically say, like detect that and tell them like, hey, you know,
[2186.42 → 2190.44] you shouldn't be drawing that. This is, this is a safe for work project and kind of like turn their
[2190.44 → 2198.80] penis into a flower or, you know, a tree. That project uses sort of object recognition libraries,
[2199.14 → 2206.34] projects like Google Quick draw. But of course, there is no penis detection within that, that system.
[2206.34 → 2213.18] So they've had to create their own huge library of, you guessed it, thousands and thousands of
[2213.18 → 2219.52] crudely drawn penises collected from the wide reaches of the internet. So my point here is,
[2219.56 → 2226.34] and I have one, is that a lot of these projects use existing libraries and existing approaches.
[2226.34 → 2233.38] So the more of that stuff that can be open source, the more creative people can be,
[2233.46 → 2239.56] they can sort of innovate on the content layer, if you will, of the project, rather than having to like,
[2240.18 → 2245.78] create entire, the entire stack of artificial intelligence systems that are needed.
[2246.18 → 2250.62] That is a tool that would make a big impact right now in my family's life. I have, I have a first
[2250.62 → 2254.60] grader. And they're at that stage, we're very active about going in the classroom and participating.
[2254.60 → 2260.42] And they're all at that stage where penises or anything else you can think of, farts, you know,
[2260.42 → 2264.88] are, are funny and cool. And they're trying to figure that out in the world. And a tool like that
[2264.88 → 2267.76] would, would actually be a delightful thing at this moment in my life.
[2267.86 → 2272.94] Oh yeah. I have a kid in grade two. And it's like, you just give him a blank sheet of paper and he
[2272.94 → 2279.36] draws the poop emoji on everything. It's like, dude, enough with the poop emoji. But so, you know,
[2279.36 → 2284.88] but like, imagine an AI system that, you know, and each time he tried to draw the poop emoji is like,
[2285.04 → 2289.66] you're not allowed to do that. I don't think we want to live in that future either, where like his
[2289.66 → 2296.74] pen is embedded with like a naughtiness filter that when it like goes onto any blank sheet of paper,
[2297.24 → 2301.28] it sort of censors what he's saying. So, but that's kind of the reality.
[2301.28 → 2301.94] That's a good point.
[2301.94 → 2307.74] Some of these systems are building, you know, if we, if we assume and agree that the future
[2307.74 → 2313.04] creative palette of our children is going to be the internet, we really want to make sure that it's,
[2313.16 → 2317.78] that, you know, we're not preventing them from expressing themselves.
[2318.08 → 2318.82] That's a great point.
[2319.04 → 2326.90] I don't want to see penises over everything. And I, you know, don't want to live in a world where,
[2326.90 → 2333.06] you know, like certain combinations of lines cannot exist on a blank canvas. Tough stuff.
[2333.16 → 2335.30] We're going to solve it from Villa. You heard it here first.
[2337.12 → 2342.50] Awesome. Awesome. I, and I think like going back to one thing that was mixed into that whole
[2342.50 → 2347.72] conversation was you mentioned open source. And I think one of the things that I got out of that was
[2347.72 → 2355.06] one of the ways that maybe we as AI practitioners can kind of help tell these stories and help,
[2355.06 → 2361.04] you know, make more transparent how AI works is actually to, to put our work out there in an
[2361.04 → 2368.36] in an open way and to, you know, create, you know, tools and documentation and pre-trained models and
[2368.36 → 2373.64] those sorts of things and put them out in the open. So creative people can use them and try to
[2373.64 → 2377.98] understand what they're doing and what they're capable of and that sort of thing. Would you agree?
[2378.50 → 2382.96] Yeah, absolutely. All this creative exploration that we sponsor at Mozilla. I mean,
[2382.96 → 2387.36] we encourage people to release their stuff under open licenses and in fact, sometimes require it,
[2387.36 → 2393.20] but it's so true that like, you can just get so much further if you can A, see what other people
[2393.20 → 2398.84] have done in, in this realm and then B like, Oh, there's a library for this exact thing that I want
[2398.84 → 2403.48] to do. And you just go and get it. Yeah, absolutely. Totally agree with you. That's just,
[2403.70 → 2408.74] that's a thing that the community can really help with. And then, you know, like there are other ways of
[2408.74 → 2415.16] like peer review or, you know, you know, just, just participating in systems like GitHub when
[2415.16 → 2420.92] people have questions or pull requests or stuff like that, just be active and know that you could
[2420.92 → 2426.90] never anticipate that somebody is going to build like a facial recognition movie out of a library
[2426.90 → 2432.90] that you make. But sometimes those kinds of weird uses that they didn't need to ask you for permission
[2432.90 → 2438.56] for are some of the most delightful and unexpected things that can happen on the internet. So do more
[2438.56 → 2443.54] of that. Yeah. I think one kind of interesting piece of this that I'm kind of curious to see is as
[2443.54 → 2448.50] more creative people utilize a lot of the open stuff that's out there, I think that they're actually
[2448.50 → 2453.38] going to be able to kind of help us probe some of these implications in ways that like the
[2453.38 → 2458.16] practitioners haven't even thought of. And I'm thinking of like the chatbot that Microsoft released
[2458.16 → 2463.46] that, you know, turned into a Nazi and however many days or whatever it is, sometimes the
[2463.46 → 2469.00] practitioners, the researchers, since the cycle between research and releasing, you know, like
[2469.00 → 2475.60] model code and all of that on GitHub is so quick now. I think having people probe those questions and
[2475.60 → 2481.06] think about the implications is also important, you know, for the other side. So it's important for us
[2481.06 → 2486.22] to release things into open so that creative people can use it. But it's also important for us to look at
[2486.22 → 2490.64] what the creative people are doing with what we're releasing, because it can help us, you know,
[2490.64 → 2495.26] shed some light on the implications of what we're actually doing. I agree.
[2496.44 → 2502.70] So where can we find out more about the projects that Mozilla is funding through this program?
[2502.70 → 2509.14] I think that just we tend to help support these projects at the release. So if you're following us on
[2509.14 → 2516.08] Twitter, that's probably one of the easiest ways. We have a nice blog post up about the awardees.
[2516.22 → 2521.60] And that folks could probably find fairly easy. And we're anticipating that these will all be
[2521.60 → 2527.12] released sometime over the course of the next year. Everything is meant to be done by June,
[2527.12 → 2530.80] but they'll all have different release dates depending on the complexity of their project.
[2531.00 → 2536.44] So I think just keep in touch with Mozilla. We do have a mailing list as well that we tend to
[2536.44 → 2542.40] send the stuff out on if folks are not subscribed to too many mailing lists. But I think the best way for
[2542.40 → 2548.94] people to keep in track with interest with these projects is just to follow us on Twitter at Mozilla.
[2549.44 → 2553.40] We also have a mailing list if people are interested. And there's a blog post that should
[2553.40 → 2559.06] give links to the creators of the project. But poke around and see what else these folks have made if
[2559.06 → 2563.10] you're interested in this type of work. This has been a really cool conversation for us, I think,
[2563.16 → 2569.18] in terms of the intersection of creativity and different forms of art and communication as opposed to AI.
[2569.18 → 2573.98] We got into where we talk about ethics a lot, but I think we need to have even more conversations
[2573.98 → 2580.70] about the larger world, people outside just AI in the traditional sense doing this. So thank you so much.
[2581.20 → 2583.06] Yeah, it was a pleasure. Thank you to both of you.
[2585.86 → 2590.74] All right. Thank you for tuning into this episode of Practical AI. If you enjoyed this show, do us a favour.
[2590.86 → 2596.20] Go on iTunes, give us a rating. Go in your podcast app and favourite it. If you are on Twitter or social network,
[2596.20 → 2599.64] share a link with a friend, whatever you got to do, share the show with a friend if you enjoyed it.
[2599.94 → 2605.28] And bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. And we catch our errors
[2605.28 → 2609.48] before our users do here at Changelog because of Rollbar. Check them out at rollbar.com slash
[2609.48 → 2615.18] Changelog. And we're hosted on Linde cloud servers. Head to linode.com slash Changelog. Check
[2615.18 → 2621.14] them out. Support this show. This episode is hosted by Daniel Whiten ack and Chris Benson. Editing is done by
[2621.14 → 2626.86] Tim Smith. The music is by Break master Cylinder. And you can find more shows just like this at
[2626.86 → 2632.24] changelog.com. When you go there, pop in your email address, get our weekly email, keeping you up to date
[2632.24 → 2637.64] with the news and podcasts for developers in your inbox every single week. Thanks for tuning in.
[2637.64 → 2638.60] We'll see you next week.
