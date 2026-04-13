[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.04] And unlike standard droplets, which use shared virtual CPU threads,
[29.04 → 32.88] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.42 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.18 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 → 88.54] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[106.84 → 109.04] Hey, welcome to the Practical AI podcast.
[109.96 → 114.12] This is going to be another fully connected episode where Daniel and I keep you fully connected
[114.12 → 116.30] with everything that's happening in the AI community.
[116.68 → 119.16] We're going to take some time to discuss the latest AI news,
[119.30 → 123.16] and we're going to dig into some learning resources to help you level up on your machine learning game.
[123.16 → 124.76] My name is Chris Benson.
[124.98 → 126.42] I'm one of the co-hosts.
[126.58 → 131.88] I am a chief strategist for artificial intelligence, high performance computing, and AI ethics at Lockheed Martin.
[132.16 → 137.50] And with me is my co-host, Daniel Whiten ack, who is a data scientist with SIL International.
[137.66 → 138.52] How's it going today, Daniel?
[138.98 → 140.12] It's going great.
[140.34 → 141.38] How about with you, Chris?
[141.72 → 142.70] Going very well.
[142.70 → 149.10] As we are recording this, I just got back from the Lifeworks Tech Conference in Boston.
[149.42 → 152.32] Had a good time there, gave a talk, and it went well.
[152.48 → 153.68] So I'm a happy camper.
[154.16 → 154.44] Awesome.
[154.82 → 155.00] Yeah.
[155.22 → 158.08] Well, things are looking up here as well.
[158.18 → 164.34] Over the past month or so, it seems like my internet at home kind of has gradually been degrading,
[164.34 → 172.10] and I haven't been able to figure out why I've updated my computer and done all the restarts of everything,
[172.28 → 177.32] checked all the things, but had the technician out today.
[177.42 → 186.22] It turns out that squirrels were eating the cables coming into my house, so producing obvious degradation.
[186.42 → 186.72] Absolutely.
[186.72 → 191.52] So I'm happy that that's actually figured out, and I have good internet again.
[191.60 → 192.18] There you go.
[192.18 → 195.58] So humane removal of squirrels to be considered here.
[195.94 → 200.88] Or reconfiguring the cable positioning to make it a little bit harder.
[201.18 → 201.66] Or that.
[201.78 → 202.56] Either one will work.
[202.66 → 202.82] Yeah.
[203.00 → 203.28] Okay.
[203.58 → 213.98] So we actually have a really, really timely topic right now because we are having conversations about this constantly.
[214.64 → 219.74] So today we wanted to talk about deep fakes, and we're kind of going to cover an overview with it.
[219.74 → 225.12] And so much is happening in the news right now regarding deep fakes.
[225.28 → 228.32] We'll tell everyone what they are and such as that.
[228.46 → 235.30] But everywhere I go, whether I was in Boston or we had this past week, we had our monthly Atlanta Deep Learning Meetup.
[235.50 → 236.80] The topic came up there.
[236.92 → 240.42] It's just kind of coming up everywhere, and it's coming up in the news on a daily basis.
[240.42 → 243.90] So we're going to delve into this topic and see what we find.
[243.90 → 244.38] Yeah.
[244.50 → 254.92] And actually, even just this morning, the policy director from OpenAI was testifying before the House Intelligence Committee here in the U.S.
[255.32 → 263.76] The topic of that was the national security challenge of artificial intelligence, manipulated media, and deep fakes.
[263.76 → 277.56] So, you know, this is reaching the highest levels of government and certainly something that people ask about a lot and something that we – I think it's time that we spend time talking about it on the podcast.
[277.84 → 279.40] So I'm glad you brought up the idea.
[279.86 → 279.96] Yeah.
[280.04 → 284.70] I actually – I saw your tweet about that was going on and tuned in.
[284.70 → 301.76] I was too late to catch the beginning of the show of the testimony, but I saw at least the full second half, and it was fascinating, and it was interesting to see how startled the members of the Intelligence Committee were receiving this information.
[301.94 → 312.02] I think they already had some insight into it, but it was – one of the reps whose name I don't have at the top of my head noted that it was very scary stuff.
[312.02 → 316.90] And so the potential of how it can be used nefariously, and we'll certainly get into that today.
[317.02 → 328.26] So we're going to kind of talk about what deep fakes are and then get into kind of how they can be used, how they have been used, what can be done to prevent bad actors, that such thing.
[328.42 → 334.02] And I'll certainly – I took notes and will refer to some of the congressional testimony in this episode.
[334.48 → 334.72] Awesome.
[334.92 → 335.78] I appreciate that.
[335.86 → 335.98] Yeah.
[336.04 → 339.08] And I guess this episode will be kind of a downer.
[339.08 → 340.54] Sorry, folks.
[340.54 → 342.04] Sorry in advance.
[342.26 → 349.50] We'll try to at least keep it's interesting, even if we are talking about sort of quote-unquote dangerous things.
[349.98 → 357.66] And, you know, try to, you know, bring some of our thoughts into it, but try to give you a kind of good overview of the topic.
[357.84 → 363.40] So maybe one good way to start is just by defining what a deep fake is.
[363.40 → 372.22] So in my understanding, a deep fake, the deep part really refers to like deep learning models.
[372.22 → 375.24] Now, we talk a lot about deep learning on this podcast.
[375.24 → 380.96] So if you want to know more about that, there are certainly a lot of links throughout the podcast about deep learning.
[381.50 → 390.90] But now I guess the question is for deep fakes, if we're talking about deep learning models faking something, so generating fakes of something.
[391.62 → 391.70] Yeah.
[391.72 → 393.28] What are we talking about?
[393.28 → 395.78] So what are deep fakes faking, Chris?
[395.78 → 404.04] So deep fakes are where you, and I'll get to a specific example, but that's where you are using deep learning technology.
[404.22 → 412.28] And we'll talk about the specifics in a moment to change, to either create or change videos that may be out there.
[412.28 → 413.60] It could also be audio.
[414.16 → 428.78] It can be any kind of media that people will watch to take in information, whatever that might be, and change those so that what you are seeing and hearing is not actually what really happened with the original unchanged video.
[429.36 → 432.76] And so it opens the door for all types of manipulation.
[433.20 → 433.30] Yep.
[433.38 → 434.66] And so that's a start.
[434.78 → 436.50] It's a broad, very broad definition.
[436.50 → 437.14] Yeah.
[437.38 → 449.70] So some of our regular listeners might remember that I think our last Fully Connected episode, we kind of did an overview of various advanced sort of methodologies in the AI world.
[449.82 → 451.02] One of those was GANs.
[451.48 → 466.04] And in that episode, we talked about how GANs, or generative adversarial networks, are one of the things they can do is generate art, or generate images, or generate videos, or change styling, or these other sorts of things.
[466.04 → 473.22] So this is one sort of methodology that's applied, a deep learning methodology that's applied to generate certain things.
[473.54 → 481.76] Like you were saying, Chris, I think the thing that people probably think of right away when they think of deep fakes, if they've seen some of these things, is the video thing.
[481.76 → 487.08] So there's been some funny ones or satirical ones as well.
[487.26 → 496.66] So I was just watching one before the episode where kind of Joker's face was applied to these different videos.
[497.22 → 503.24] There have been ones with President Obama's face where he's dancing and other things.
[503.24 → 514.96] So it's kind of like, you know, the Joker or President Obama didn't actually act in those videos, but their face is in those videos doing certain things when they didn't.
[515.42 → 519.06] So I think that that's probably what comes to mind.
[519.30 → 522.72] There's, of course, like you said, this is an only video.
[523.32 → 529.70] So we talked even in the last Fully Connected episode about generating kind of fake people.
[529.70 → 531.80] So pictures of fake people.
[532.22 → 541.74] But in this case, probably the deep fake part of it would be faking someone's face with an emotion or an expression or a scene that they were never in.
[541.92 → 545.52] Or faking someone's voice saying something that they never said.
[545.62 → 547.38] Or maybe it's both of those things together.
[547.52 → 552.48] Faking someone's voice and in a video saying something they never said.
[552.60 → 555.64] So replicating someone's voice and mouth movements.
[555.64 → 561.96] But then it also goes beyond kind of the video and imagery into text as well.
[562.06 → 577.96] Of course, there was a lot of focus on OpenAI's GPT-2 model recently this spring, which was capable of producing some like really realistic sort of news kind of articles or text on certain subjects and that sort of thing.
[577.96 → 589.02] So generating text in a certain style or based on a certain subject or something like that is also something that should be considered as we're kind of talking through this.
[589.30 → 589.64] Absolutely.
[590.04 → 601.24] And there have been – it's been in the media so much recently because there have been several notable things that I imagine most or all of our listeners are already somewhat familiar with.
[601.24 → 617.94] There was recently a video of the Speaker of the House of Representatives in the U.S. Congress, Nancy Pelosi, where she – in the video she was speaking, and they made her appear kind of – I think the most common references were drunk and slurred speech and such as that.
[618.38 → 625.06] And that was that one thing where it changed the characterization of her having that conversation.
[625.70 → 626.84] And that's a big part of it.
[626.84 → 628.78] It's not just changing the words.
[628.86 → 631.08] You can change how people appear to you.
[631.74 → 634.44] And a lot of people believe that video.
[634.44 → 640.18] They were like, oh, there's this video of Nancy Pelosi drunk on stage or whatever talking.
[640.48 → 641.88] And so that was one.
[641.96 → 645.10] And there was a bit of an uproar and Facebook refused to take it down.
[645.34 → 656.44] So earlier this week there was a video posted on Facebook and other places of Mark Zuckerberg, the CEO of Facebook, saying things that he never said where they took a –
[656.44 → 661.68] I think it was a 2017 talk of his and changed what he was saying.
[661.96 → 670.34] And so I think it was a – I think that was intended somewhat as a look, I told you so, Facebook, you should have taken down the Pelosi video.
[670.72 → 672.20] And so how does it feel?
[672.20 → 674.58] So those are certainly big.
[674.66 → 684.76] And I know in my day job working at Lockheed Martin's, you know, focusing on national security issues, this is certainly something that we talk about because there are all sorts of uses here.
[684.80 → 690.02] And we'll get into some of those potential use cases, you know, in the world as we go here.
[690.02 → 695.68] Now, some of you are probably thinking, well, this kind of has already been around for a while.
[695.90 → 713.04] So Hollywood and movie studios have been doing sort of CGI and video tricks and movie tricks for quite some time that might kind of put someone in a scene that they were, you know, standing on a mountain where they weren't really.
[713.30 → 716.58] Or maybe it's like superimposing a face.
[716.58 → 720.96] I'm thinking of the Star Wars example with Princess Leia.
[721.54 → 724.32] So there's certainly something that's not new.
[724.48 → 733.04] I think what is new is kind of traditionally or always in the past, these sorts of techniques were pretty much restricted to experts.
[733.04 → 739.48] So it required a lot of effort, required a lot of time and money to kind of pull off these things convincingly.
[739.48 → 766.08] Now, with these deep learning networks that have kind of these large encoding layers and decoding layers, you can have a training data set where you have a bunch of images with, you know, one person's face and output, you know, with the other face or from, you know, with a certain pose or representation of a body.
[766.08 → 770.02] And then output with someone in that pose or whatever it is.
[770.02 → 778.46] If you have the right training data, now it's just a matter of applying models that are existing to that training data.
[778.46 → 785.82] And it really doesn't require a lot of expertise beyond maybe some hours of compute time on AWS or something like that.
[785.82 → 788.48] And in some cases, you can even get pre-trained models.
[788.72 → 798.20] So like in terms of kind of generating these new looking faces, you know, corresponding to a certain facial expression or something like that.
[798.26 → 804.76] So in this case, maybe the input is a facial expression or something and the output is someone, you know, in that facial expression.
[804.76 → 813.10] You know, that may only take a few images to fine tune on if you've already got a very good pre-trained model.
[813.24 → 823.34] So it's not even like you have to have a bunch of images of someone to be able to fake them in a certain in a certain position or with a certain facial expression or in a certain scene.
[823.48 → 831.72] So I think the big difference now or what's been the development recently is kind of the ease with which you're able to do these sorts of things.
[831.72 → 844.80] That's true. And there 's's a whole host of software programs that have come out that are basically kind of dubbing down the process so that you don't have to have a lot of deep learning training.
[845.32 → 853.36] In some cases, you can just install the applications on your system, and they come with, you know, there's some for Mac and Windows and things like that.
[853.36 → 861.52] Some of the really well-known ones that people talk about or there was kind of the original what was called the fake app program, an open source version of that.
[861.72 → 879.52] Followed called Deep Face Lab, which I've seen referenced quite a lot, although that has recently closed down because the primary maintainer has moved on, though that person is encouraging other people to use the source and move on and do things with it if they choose.
[879.52 → 884.98] There 's's face swap. There's my face. I'm sorry, my fake app, which is on Bitbucket.
[884.98 → 889.40] And so there 's's, and I think you're going to see more and more of these coming about.
[889.66 → 892.22] And in addition to that, obviously, you can use the standard tools.
[892.36 → 897.02] You can use Keras and TensorFlow to do the same things with the data as you just alluded to.
[897.02 → 910.58] So it's I think that the key takeaway there is that, you know, when it was a Hollywood thing, it was a highly skilled thing that required, you know, special software, things that you would find in a movie studio, but not everywhere.
[910.58 → 915.86] And that's changed. It's now something that any computer savvy person can handle.
[916.34 → 922.10] And so I think that's that's what's changed as we hit 2019 is that it's now been democratized.
[927.02 → 938.28] The Data Engineering Podcast is a weekly deep dive on modern data management with the engineers and entrepreneurs who are shaping the industry.
[938.28 → 946.88] Go behind the scenes on the tools, techniques and difficulties of data engineering so you can learn and keep up with the knowledge to make you and your business successful.
[947.44 → 954.74] Can you give a bit of an outline about the motivation for choosing Jupyter Notebooks in particular as the core interface for your data teams?
[954.74 → 961.20] Yeah. And actually, when I first joined Netflix, it was sort of tossed at me, and I was definitely like, are we crazy?
[961.44 → 963.10] And the answer was like, we might be a little crazy.
[963.60 → 969.92] Go to dataengineeringpodcast.com to listen, subscribe and share it with your friends and colleagues.
[969.92 → 989.66] All right, Chris. So let's maybe get to the more, I don't know, important or depressing or however you want to put it.
[989.66 → 1010.46] Part of the part of the part of the part of the part of the part of the part of the part of the story is, you know, in some ways, it's kind of cool that this technology exists in the sense that, you know, technology wise and kind of intellectually, this is kind of interesting that these techniques can do this with, you know, with such little data or with such realism.
[1010.46 → 1016.38] And when you just think about it from that point of view, you know, technology wise, it's pretty interesting.
[1016.96 → 1022.04] But what makes this sort of technology? Why is there so much hype around it?
[1022.18 → 1026.52] Why are these sorts of methods that produce these deep fakes?
[1026.68 → 1030.80] Why are they so dangerous? What's your perspective on that?
[1030.80 → 1035.24] Well, I think there 's's a number of reasons that we can kind of work our way through.
[1035.78 → 1043.68] You know, I guess you can start off with the fact that since the data is so available, you can get videos from so many places now.
[1044.04 → 1050.10] And with people using their smartphones to take video and, you know, post it out on social media and stuff.
[1050.34 → 1056.66] It's not, you know, historically, deep fakes have really centred on things like celebrities.
[1056.66 → 1063.42] And, you know, they would put a celebrity's face on, you know, a pornographic video or take a politician.
[1064.12 → 1073.44] I saw something on one of the software on one of the deep fake software sites where they were superimposing Nicolas Cage's face on Donald Trump.
[1073.54 → 1079.72] And you could kind of clearly see it was it appeared to be Trump talking, but the facial expressions were clearly Nicolas Cage's.
[1080.08 → 1085.02] And those were, you know, kind of goofy so long as that was as far as you were taking it.
[1085.02 → 1087.22] And they could be a little bit fun meme like.
[1087.84 → 1094.28] But I think that obviously opens the same door for people who are out to cause harm to others.
[1094.28 → 1096.26] And that could be at a lot of different levels.
[1096.26 → 1103.04] It could be as personal as harassing a bad actor, harassing someone they know.
[1103.04 → 1112.40] You know if they'm just making something up, broke up with the girlfriend, and they had video of their girlfriend talking, and they could take that and, you know, take some other bad footage,
[1112.40 → 1115.20] whatever you want to do and put that out there to humiliate them.
[1115.24 → 1118.10] And I think there have been some instances of that.
[1118.74 → 1123.26] I think you had mentioned that there was one that The Washington Post had reported.
[1123.44 → 1124.56] I know when we were talking beforehand.
[1125.10 → 1125.28] Yeah.
[1125.28 → 1139.76] So there's kind of this I mean, one of the first ways I think this had surfaced and people have used it in this sort of harassing way is kind of the pornographic use, like you had said before, where, you know,
[1139.76 → 1147.04] maybe before there were certain people that tried this with celebrities, at least kind of leading up until very recently.
[1147.04 → 1157.88] Now, I think it's its very real that, you know, if someone had this sort of video of someone they knew, you know, that in their circle of friends or acquaintances,
[1157.88 → 1164.28] they could harass them in this way by making, you know, explicit content with that person's face.
[1164.28 → 1176.28] And, you know, it looks so real that if they kind of propagate that, then kind of the harm is done before, you know, it may come out or may never come out that that that was a fake.
[1176.94 → 1185.46] So it's its definitely a concern in terms of how this could affect, you know, real people's lives.
[1185.46 → 1195.52] You know, it's funny, just as an as when you said that about, you know, whether people after the fact would learn that that was addressed in the congressional hearing today.
[1195.62 → 1209.42] It was noted that when one of these videos goes out and goes viral, even if it's widely reported that the video was a fake after the fact, it is tends not to hit as many people.
[1209.42 → 1214.72] And so you inevitably have changed the landscape by the initial post.
[1214.90 → 1218.94] And then, you know, the quote fix afterwards doesn't actually completely fix it.
[1219.10 → 1231.94] And they noted that psychologically, that even if people know it was a fake that they saw, that psychologically, they still kind of hold on to some of that bias that was introduced through the fake.
[1231.94 → 1249.06] So even if I, you know, even if I found out that the picture of President Trump and Nicolas Cage was, in fact, a deep fake, as it was, in theory, there's the potential for that to influence me in some way, depending on what the video author was shooting for.
[1249.16 → 1251.72] So it's an it's an interesting side effect.
[1251.72 → 1277.70] Yeah. And part of the hype, maybe that's been generated recently and part of the momentum to discuss these things, I think, has been that shift from, you know, people's thoughts of before thinking that, well, yes, whether it was satirical, like a joke sort of thing, or whether it was actually harassment and humiliation, like in terms of the pornography type of stuff, you know, that was maybe restricted to celebrities.
[1277.70 → 1282.18] And people are thinking, oh, well, those people put themselves out in public, there's a lot of video of them.
[1282.52 → 1291.96] So they're kind of, you know, asking for this sort of thing, which is kind of sad anyway, because no one should have to be subjected to that if they don't want it.
[1291.96 → 1302.40] But now it's like you think about any video you see, whether it's a video of someone, you know, on Facebook or, you know, someone that's not a high profile celebrity.
[1302.40 → 1314.62] Now that there's this potential that even those videos are faked in some way or another to influence you, or at least there's the potential of that happening, which is kind of a shock when you think about it.
[1314.62 → 1324.42] Yeah, it really is. I mean, it's there's such a widespread application from a very personal level, as we were talking about a moment ago, you know, all the way to large societal concerns.
[1324.42 → 1332.50] And it is a technology that is kind of fluid enough in its application to where you can scope it however you want.
[1332.82 → 1341.82] And you're seeing everything from that level all the way up to nation states using it, you know, to influence others, which we'll talk about in just a moment.
[1341.82 → 1355.36] But I think one of the things that I think is certainly contributing to it being used this way and in such a successful frame is the fact that when your political environment is what we all know it to be.
[1355.96 → 1360.00] And we are we're very polarized, we're very tribe oriented.
[1360.00 → 1383.50] And we recognize that, you know, there are messages that are supporting each of those viewpoints that by itself, before you get to deep fakes already kind of introduces in a lot of people's minds, the potential for conspiracy theories and and and thinking about others in ways that may not be entirely realistic anyway, regardless of which side you're on.
[1383.50 → 1392.54] And so when you throw in the nefarious intent that deep fakes can lend themselves to, that just exacerbates the situation.
[1392.80 → 1402.84] So we really have created not only here in the United States, but in places around the world, an environment where we're very susceptible to this technology being used against us now.
[1403.26 → 1410.52] And it's certainly something that if we are is we are to navigate safely through this, we're going to have to we're going to have to figure out ways of coping.
[1410.52 → 1414.42] And we'll address some of those in the congressional hearing address some of that.
[1414.48 → 1415.48] We'll talk about that in a few minutes.
[1415.48 → 1432.38] Yeah, it is interesting that even the so just the fact that these deep fake videos exist, it creates kind of an excuse, an extra kind of excuse for people that don't want to face the truth or want to create conspiracy theories.
[1432.38 → 1435.28] So this has already been seen around the world.
[1435.28 → 1443.26] You know, I was reading in the there's a great Washington Post article that I'll link in our show notes, but it was talking about in Malaysia.
[1443.26 → 1451.28] There's a kind of viral video clip of a man confessing to certain things with a local cabinet minister.
[1451.28 → 1458.28] And that's kind of, you know, that questionable stuff is being kind of thrown into, oh, well, that's just a deep fake.
[1458.28 → 1479.06] And the similar things in Africa, even, you know, videos of leaders who have actually contributed to those videos have contributed and the controversy over those have has contributed to, you know, coup attempts and other things where it wasn't even I guess we don't I don't know if it's known in those cases.
[1479.06 → 1487.88] But even just the questioning of those videos, if they're a deep fake created enough uncertainty that it actually created political and military turmoil.
[1488.28 → 1496.56] Yeah. And those aren't the only places that was actually an example very similar to your African when in the testimony before Congress today about that.
[1496.56 → 1507.88] And so just to go ahead and get to that, there was it was a statement that was prepared for the permanent select committee on intelligence within the U.S. House of Representatives.
[1508.16 → 1513.76] And the person testifying was Clint Watts of the Foreign Policy Research Institute.
[1513.76 → 1523.52] I'm sorry, Institute. And the title of the brief was the National Security Challenges of Artificial Intelligence, Manipulated Media and Deep Fakes.
[1523.52 → 1531.14] And I read through the document that was submitted initially that kind of represented their viewpoint in addition to hearing some of the testimony.
[1531.72 → 1536.12] And it wasn't actually at the top, but there was a paragraph that jumped out and it's very short.
[1536.12 → 1540.54] And I'm going to read that really quick because I think it really kind of gets right down to it.
[1540.54 → 1546.22] It was deep fake proliferation represents two clear dangers over the long term.
[1546.42 → 1553.50] Deliberate development of false synthetic media will target U.S. officials, institutions and democratic processes with an enduring,
[1553.52 → 1566.28] goal of subverting democracy and demoralizing the American constituency in the near and short term circulation of deep fakes may incite physical mobilizations under false pretenses,
[1566.28 → 1573.16] which you can think of as troops, initiate public safety crises and spark the outbreak of violence.
[1573.16 → 1583.34] The recent spate of false conspiracies proliferating via WhatsApp in India offer a relevant example of how bogus messages and media can fuel violence.
[1583.52 → 1590.20] The spread of deep fake capabilities will likely only increase the frequency and intensity of such violent outbreaks.
[1590.36 → 1591.78] Now, that was one paragraph.
[1592.08 → 1594.38] And that's a scary paragraph when you think about it.
[1594.44 → 1594.88] It is.
[1595.06 → 1597.08] You know, that was just one out of the entire thing.
[1597.08 → 1600.50] And he goes on, and they do make recommendations, which will hit in a few minutes.
[1601.10 → 1605.50] But, you know, if that doesn't give you pause when talking about this, I'm not sure what would.
[1605.84 → 1626.02] Another one that I saw in that Washington Post article, which I thought was really great, was a quote from, or I don't know if it was a quote as a paraphrase from Rachel Thomas, who's the one of the co-founders at Fast.ai, which we all love for many reasons, including the educational piece and the practical packaging and everything.
[1626.02 → 1627.78] So shout out to Fast.ai.
[1627.78 → 1639.96] But she kind of said that disinformation campaign using deep fake videos probably would catch fire because of the reward structure of the modern web.
[1639.96 → 1650.70] So I think what she's getting at there is basically the shock factor of a deep fake video is really what drives the reach of that video.
[1651.08 → 1656.20] And so these videos are kind of set up to be shocking in many cases.
[1656.20 → 1667.22] And so just that by itself lends to this kind of going viral, reaching bigger audiences versus kind of maybe more mundane, but true videos.
[1667.22 → 1669.92] Right. So it's it is a concern.
[1669.92 → 1677.58] And, you know, I know that we've already talked about kind of just the idea of these videos existing as dangerous.
[1677.58 → 1685.96] But also, I mean, they are already being used by malicious actors, like you were saying, in various places around the world.
[1686.36 → 1693.38] And I think, you know, the Russia piece also fit into the hearings that were this morning.
[1693.38 → 1693.70] Right.
[1694.02 → 1694.58] They did.
[1694.58 → 1695.78] So they addressed.
[1695.96 → 1699.56] And so I know that in politics, some people may disagree.
[1699.56 → 1707.72] But, you know, the American FBI has stated explicitly that Russia interfered with the election of in 2016.
[1707.72 → 1714.86] And so taking that as a basis of fact for this, it was also noted in that same testimony.
[1715.52 → 1724.56] Moving forward, I'd estimate Russia as an enduring purveyor of disinformation is and will continue to pursue the acquisition of synthetic media capability.
[1724.56 → 1728.10] And employ the outputs against its adversaries around the world.
[1728.40 → 1731.68] And basically, that's I think that's representative.
[1731.68 → 1732.74] This is me speaking out.
[1732.82 → 1738.08] That's representative of the fact that it's a weapon of information warfare at this point.
[1738.24 → 1740.94] Deep fakes that it can be used in that way.
[1741.36 → 1742.22] And that does.
[1742.32 → 1744.00] And it's not necessarily just Russia.
[1744.00 → 1754.54] It can be many, many, you know, nations that can they can try to influence and sway other countries, other parts of society with that.
[1754.66 → 1758.74] And so these are the types of things that it's not just you and I talking about it.
[1758.78 → 1761.20] It's not just the AI community or the general population.
[1761.20 → 1766.40] It's certainly something that the defence industry and the military at large are having to consider.
[1766.74 → 1768.18] It's still relatively new.
[1768.18 → 1773.44] And it's something that really all countries are going to have to contend with going forward.
[1773.64 → 1773.80] Yep.
[1773.90 → 1784.46] So I guess maybe one last thing here when we're moving on from the dangers and maybe a quick point here that I know that you posed on our LinkedIn page.
[1784.46 → 1788.90] So if you aren't aware, our podcast has a couple of ways for you to engage with us.
[1789.08 → 1795.30] We'd love for you to engage on our Slack channel, which you can join if you go to changelog.com slash community.
[1795.30 → 1796.98] We also have a LinkedIn page.
[1797.04 → 1810.12] I think it was posed on the LinkedIn page if there were any beneficial uses of deep fakes or good use cases for using this sort of technology to create fake something's.
[1810.78 → 1814.04] So we would love to hear from you if you have those ideas.
[1814.04 → 1815.66] But I know a couple came up.
[1816.04 → 1817.42] What did you see there, Chris?
[1817.68 → 1821.18] So I know that, and I hope I don't mess up his name.
[1821.74 → 1823.24] Konstantin Vetrov.
[1823.24 → 1826.52] I'm sorry, Konstantin, about mispronouncing there.
[1827.24 → 1828.70] He is in Atlanta.
[1828.76 → 1831.36] He's part of the Atlanta deep learning meetup community as well.
[1831.62 → 1837.00] But he is a senior solution architect with NVIDIA and, you know, really savvy guy about this.
[1837.08 → 1839.74] But he did point out one of the things.
[1839.84 → 1844.04] He talked about kind of what you said earlier about, you know, the technology itself is agnostic.
[1844.18 → 1845.32] It's not a bad technology.
[1845.52 → 1847.64] It's a set of tools that can be used.
[1847.64 → 1853.80] And we've talked about some of the joking things and obviously can be used for bad as we've been addressing as well.
[1853.80 → 1860.42] But he pointed out that, you know, the forensic, you know, we can learn a lot when we do have bad actors doing that.
[1860.54 → 1865.14] The forensic evidence that we can then analyze and understand how people are doing that is beneficial.
[1865.48 → 1872.84] And so he's kind of saying there's something where you can take something good after something bad has happened and improve.
[1872.84 → 1879.74] And then he finishes up, he says, and also deep fakes who create a whole new genre of TV comedy.
[1879.96 → 1881.14] And there's that to be said, certainly.
[1881.62 → 1888.70] So maybe there's some pretty fun things that could be done lighthearted, which I know isn't the tone we've set here.
[1889.08 → 1892.78] But it'll be interesting to see how people use these technologies going forward.
[1892.84 → 1893.24] It's here.
[1893.54 → 1895.60] You know, everyone's going to have access to it at large.
[1895.74 → 1901.16] And so I would certainly love to see that optimism express itself in people's creativity.
[1901.16 → 1901.52] Yeah.
[1901.60 → 1922.06] And one thing that, you know, is useful like this in terms of the kind of entertainment industry, there's obvious use cases where studios, movie studios have people's permission to create sort of these computer generated things like, you know, maybe someone can't dance a certain way or something.
[1922.06 → 1930.70] But that needs to be in a movie, and they get that person's permission to kind of make that video of them dancing or whatever, whatever the situation is.
[1930.78 → 1935.22] I think there are, you know, legitimate uses of that within entertainment.
[1935.22 → 1945.86] But also in addition to governments kind of weaponizing this sort of technology or malicious actors kind of using it against, you know, their enemies.
[1945.86 → 1962.42] I think there are probably uses of this technology that could be beneficial in kind of the opposite way in terms of bringing humanitarian or help to people in the developing world as well, where the political situation is hard.
[1962.42 → 1974.18] I know that, you know, getting educational material to people in certain areas is really tough to certain language minorities as well, especially if those language minorities are also religious minorities.
[1974.18 → 1985.96] And so, you know, sometimes like in my mind, I'm aware of, you know, translators who might translate like educational material or something for those people, they probably don't want to have themselves on a video.
[1986.46 → 1993.96] So if that video was kind of created as an avatar or something like that, then, you know, a lot of that could be useful as well.
[1994.08 → 1998.54] So I think that putting all the weight on the bad uses is not completely fair.
[1998.54 → 2004.76] Although I think putting a lot of the focus there is warranted because this is a very serious topic.
[2004.96 → 2005.60] I agree with you.
[2005.72 → 2010.92] I'm really hoping to see some great use cases come forward where it's not just the doom and gloom thing going forward.
[2011.08 → 2019.36] So I'll tell you what, if anybody wants to put in my face, which is out there on a dancing video or something, my seven-year-old daughter would love that.
[2019.36 → 2024.84] So I'm hoping somebody will post something like that on Slack or in their LinkedIn community or something.
[2028.54 → 2033.40] Well, hello there, listeners of Practically I.
[2033.50 → 2033.98] How are you?
[2034.04 → 2035.34] This is Adam Stachowiak.
[2035.46 → 2039.10] If you haven't heard yet, we're launching a new show called Brain Science.
[2039.36 → 2041.44] It's a podcast for the curious.
[2041.54 → 2042.24] Are you curious?
[2042.50 → 2052.78] Because if so, we're exploring the inner workings of the human brain to understand things like behaviour change, habit formation, mental health, and what it means to be human.
[2053.26 → 2055.08] It's brain science applied.
[2055.08 → 2061.68] Not just how does the brain work, but how do we apply what we know about the brain that can transform our lives.
[2062.00 → 2066.54] Learn more about the show and subscribe at changelog.com slash brain science.
[2066.74 → 2071.82] Until then, here's a preview of episode one where we talk about the fundamentals of being human.
[2072.28 → 2075.00] We're also all designed to be in relationship.
[2075.00 → 2081.74] We are fundamentally hardwired to have social groups and this sense of attachment.
[2082.64 → 2094.42] And because I'm sort of a geek when it comes to research, what researchers have found is that attachment, which that's what we label how we relate and connect with others.
[2094.42 → 2103.60] Attachment is 100% learned, which means our genetics don't actually contribute to how we learn to stay in proximity with other people.
[2103.98 → 2111.50] And with that, that we all develop ways to manage the threat of the loss of a relationship.
[2112.02 → 2116.94] But nobody gets to opt out of going, I need to be in relationship with others.
[2116.94 → 2125.92] It's almost like we need to have that echo from another human being to let us know that we're there, or we're alive or just some sort of feedback loop.
[2125.98 → 2127.34] I'm not really sure how to describe that.
[2127.90 → 2130.82] Well, it really is this sense of being with, right?
[2130.86 → 2136.84] Like I can't fight battles on my friend's behalf or on my kid's behalf, right?
[2136.84 → 2146.80] But the simple fact that I know of what's going on makes a difference because I would contend its sort of like I help them hold that weight emotionally.
[2147.70 → 2150.02] And so that actually leads me into the third thing.
[2150.10 → 2157.14] And the third thing that I would say in regard to the fundamentals of being human is that we all struggle.
[2157.38 → 2158.22] Oh, yes.
[2158.76 → 2159.28] Right?
[2159.80 → 2160.44] Big time.
[2160.44 → 2166.42] And that, you know, we don't always get to pick the way in which we struggle, but we all struggle.
[2167.56 → 2171.88] Well, if you like what you hear, you should go to changelog.com slash brain science.
[2171.96 → 2174.54] The show is not out yet, so don't get too excited.
[2174.54 → 2179.56] But you can subscribe and be notified as soon as the show launches.
[2180.12 → 2183.14] Once again, changelog.com slash brain science.
[2190.44 → 2200.24] All right.
[2200.36 → 2203.62] So we've talked about, you know, what deep fakes are.
[2203.62 → 2209.42] We've talked about the dangers they pose and also maybe some benefits that they can offer.
[2209.42 → 2222.52] But maybe now let's kind of move to talking about how people are thinking about protecting themselves or other people or societies against deep fakes or the disinformation that they can spread.
[2222.52 → 2236.46] So I know one of those approaches that I've seen in the community to protect against deep fakes is kind of a strategy that OpenAI has taken with their GPT-2 model.
[2236.46 → 2240.70] So we have a podcast episode about that model and the technical details of it.
[2240.76 → 2244.84] If you're interested, definitely take a listen to that episode.
[2244.84 → 2263.56] But the thing that they saw with GPT-2 was that it is capable of generating this sort of very realistic text and very long form text, which obviously they saw as an opportunity to create fake news articles or fake content for social media and that sort of thing.
[2263.98 → 2265.94] And so they saw the danger with this.
[2265.94 → 2278.50] And the approach that they took to kind of prevent that was they just released the code for the model, not the full pre-trained model itself.
[2278.62 → 2280.90] They released kind of a limited version of the model.
[2281.38 → 2285.82] And they didn't release the full data set that they used to train that model.
[2285.82 → 2303.96] So their hope, I think, was basically to try and slow down the malicious use of that model and kind of give researchers time to develop kind of detection methods or methods that would help in some other way fight fake news.
[2304.12 → 2307.76] And now that they know that GPT-2 is out there.
[2307.90 → 2309.66] So it's an interesting approach.
[2309.90 → 2311.78] I don't know if you have any thoughts on that, Chris.
[2311.78 → 2313.14] I don't know if it did.
[2313.72 → 2326.90] I guess my question would be how much good did that approach do, given I know just recently I saw that a student who had access to certain compute resources, to TPUs.
[2327.02 → 2329.16] I forget if you use the cloud or what.
[2329.54 → 2333.28] But he had access to some compute resources, which are not that uncommon.
[2333.28 → 2335.60] And I think other people could get access to those.
[2335.60 → 2342.42] So he was a student, and he was able to use that code and reproduce the full GPT-2 model.
[2343.12 → 2346.66] And that kind of was less than four months.
[2346.66 → 2352.64] So three to four months after OpenAI released the code and the paper and all of that.
[2352.80 → 2361.74] So it's not that much time between when they released the kind of partial release and when the full thing was public and the student released that.
[2361.74 → 2366.66] So the question is, I don't know that three or four months really buys us much.
[2366.82 → 2371.16] But that's not to say that it wasn't a good approach or OpenAI didn't try.
[2371.36 → 2372.86] But I just wonder if that's enough.
[2373.22 → 2374.88] Yeah, it's a tough thing.
[2374.98 → 2388.30] I know when we did our GPT-2 episode shortly after its initial release there, and we talked about this in that episode and kind of debated that approach from OpenAI in terms of this release.
[2388.30 → 2395.26] And we contrasted that against kind of the norm in open source of kind of throw it out there and let the world dig in and see what your stuff is.
[2395.58 → 2404.96] And one of the things that we considered at the time was maybe this gave us a little bit of bumper, even though it wasn't purely in the spirit of open source in that way.
[2404.96 → 2418.32] And I think in the time, one of the things I said then was I thought probably a couple of things that it was probably good to give us a little bit of time just to absorb and realize the new world that we're in with that kind of release.
[2418.58 → 2422.96] And I also said that really it would happen anyway.
[2423.24 → 2428.56] You know, now that people knew what was possible, it would be recreated sooner rather than later.
[2428.68 → 2430.48] And this student has done just that.
[2430.48 → 2433.76] They came in and did exactly what I was predicting.
[2433.90 → 2435.78] And the reason is there's a lot of smart people in the world.
[2435.94 → 2440.90] And just because one team does something and doesn't release it doesn't mean everyone else now knows it's possible.
[2441.48 → 2444.92] And so you put smart people in the problem, and they know there's a solution then.
[2445.02 → 2445.90] And so they're going to get it.
[2446.10 → 2454.38] And I think as I've had a little bit of time to analyze this, I think OpenAI's approach was the responsible way to do it at this point.
[2454.46 → 2455.36] It wasn't too long.
[2455.36 → 2467.76] I mean, we saw that it's gotten out there anyway, but it gave us time to absorb what they had achieved, what was possible with that achievement, and how we might think about malicious uses of it, which we started doing immediately.
[2468.24 → 2470.54] And then this kid came out and released this, the student.
[2470.72 → 2477.66] And so I think for significant impacting technology releases, this might be the way forward, at least in my opinion.
[2477.66 → 2493.96] Yeah, given that the time period, so there may be a delay, hopefully organizations kind of approach things responsibly and give people notice when something like this is coming out and own up to the implications of it and kind of expose those.
[2494.52 → 2500.12] But even then, like you say, the full technology is going to be available and people are going to reproduce it.
[2500.26 → 2506.52] So in light of that, there's definitely people out there that are focusing on detecting fakes.
[2506.52 → 2515.60] So they're focusing on actual AI methods that would be able to detect or discriminate fake versus non-fake.
[2515.76 → 2520.40] So if you just go, so I really like the website paperswithcode.com.
[2520.54 → 2523.30] If you haven't seen that, you should definitely check it out.
[2523.72 → 2532.90] But if you just search for, I just search for fake and detection, and then a bunch of papers come up, kind of recent papers on this topic.
[2532.90 → 2542.92] And I would say that this kind of detecting fake deep fakes or fake news or fake images, fake videos, however they phrase it in their papers.
[2543.08 → 2550.02] There are definitely some approaches out there that seem promising, but there's definitely a no one size fits all solution.
[2550.02 → 2554.94] So there's no, you know, this is how we're going to protect ourselves against deep fakes things.
[2555.36 → 2563.06] There are some solutions out there for the on the video side, there's, there's people looking at kind of the way people blink in videos, actually.
[2563.28 → 2566.02] And apparently that's hard to replicate in a fake.
[2566.02 → 2573.76] There's also kind of a person's kind of facial fingerprint and also like per frame inconsistencies in videos.
[2574.04 → 2581.32] So there's people looking at those sorts of things to be able to tell like these, these artifacts that would give away a deep fake.
[2581.54 → 2594.42] On the text side, there's people that are analyzing kind of the persuasive structure of news articles or arguments and the stances that those articles take to kind of figure out if they're fake or not.
[2594.42 → 2597.62] So there's a whole variety of things that people are trying.
[2597.78 → 2600.30] And I certainly have only just mentioned a few.
[2600.42 → 2601.80] There's a bunch out there.
[2602.14 → 2604.58] We'll link some of those in our show notes.
[2604.72 → 2614.00] But I think probably the best thing if you're interested in those sorts of techniques is to, to search some, some site like papers with code and, and look at what people are doing.
[2614.26 → 2623.98] One of the things that, that I was struck by in reading that Washington Post article was, was a quote by a computer science professor at Berkeley.
[2623.98 → 2625.94] And Dr. Farid.
[2626.38 → 2628.98] And he said, we are outgunned.
[2629.10 → 2636.30] And the reason why he said that is the number of people working on video synthesis, as opposed to the detector side is a hundred to one.
[2636.36 → 2645.52] In other words, there's a hundred people working on interesting deep fake technology and only one of the one corresponding person working on detecting deep fakes.
[2645.52 → 2654.68] And that's probably also due to kind of, in my opinion, the incentives that are built into the academic system when, and you know, the, the AI community.
[2654.68 → 2664.52] Whereas if you come out with a, a deep fake technology or some video technology for generating videos, you're going to get a lot more attention than if you come out with a really great detection thing.
[2664.52 → 2665.16] Right.
[2665.84 → 2666.44] That's true.
[2666.60 → 2675.24] Um, so, so I think the moral of that story is, you know, if you're out there, and you're wanting to work on something around this, maybe consider working on the, the detection problem.
[2675.36 → 2677.54] We really, we really need people working on that.
[2677.64 → 2677.82] Yeah.
[2677.82 → 2684.70] You know, not only having to do with deep fakes, but having to do with things like poison data and other safety issues.
[2684.70 → 2685.88] We actually had an episode.
[2685.98 → 2693.14] I was wanting to call out to our listeners, uh, episode number 33 was called staving off disaster through AI safety research.
[2693.22 → 2698.60] Um, and that was one when I was, uh, attending, uh, applied machine learning days in Switzerland.
[2698.60 → 2705.74] And I know you organized the, the AI for good track for that conference that I met with, uh, and I'm, I'm, I'm going to try to get his name, right.
[2705.74 → 2708.30] Uh, L Made L Hamid.
[2708.40 → 2710.22] And I apologize if I just screwed that up.
[2710.22 → 2719.96] Because I know he listens to the podcast, and it was a fascinating conversation that we had that was recorded and put out where he kind of talked about different approaches to that.
[2719.96 → 2732.18] And he basically made that same point is that the number of bad actors, uh, nefarious actors out there far, far outweighs the number of people that are trying to be pro safety in this space.
[2732.18 → 2733.56] Uh, he is one of those people.
[2733.56 → 2737.66] So there's the kind of release of models side of things.
[2737.66 → 2740.32] There's the detection of deep fakes.
[2740.50 → 2748.86] Uh, there's probably a third category here, which really is assuming that deep fakes are going to exist.
[2749.12 → 2752.22] Um, that we're not going to be able to detect them all.
[2752.32 → 2754.80] So some are going to get through our best detection mechanisms.
[2754.80 → 2762.32] We should be able to, uh, criminally prosecute people that are generating these things in a malicious manner.
[2762.32 → 2764.92] That's what, that's the stance that some people are taking.
[2764.92 → 2768.00] So there's been bills introduced in the United States.
[2768.08 → 2774.62] I'm sure there's, there are other governments wrestling with this, but this is kind of probably what we're most familiar with is here in the U S.
[2774.62 → 2786.84] Like, uh, um, Senator from, from Nebraska, uh, you know, other, other lawmakers from Virginia and California are considering legislation around these things, even at a state level.
[2786.84 → 2795.06] So the New York state assembly has introduced bills to kind of push back against, uh, against this sort of technology.
[2795.06 → 2798.44] So I guess, um, that's another approach that people are taking.
[2798.44 → 2802.76] I think there's still a lot of really, you know, interesting open questions there.
[2803.04 → 2804.90] Like how, how is this enforced?
[2805.08 → 2816.40] How, how would we enforce this while still kind of allowing, you know, legitimate entertainment, uh, companies or companies that are maybe doing legitimate, uh, work in these areas.
[2816.40 → 2818.80] And, you know, helpful things in these areas.
[2818.96 → 2825.78] Um, how do we allow those people to operate and, and yet, you know, prevent this malicious usage of the technology.
[2826.12 → 2829.10] Um, so there's a lot of interesting, interesting questions there.
[2829.14 → 2833.52] You know, where do we draw the line of deep fake and not and malicious and not.
[2833.52 → 2841.94] And, um, you know, there's a whole range of things from, you know, jokes and satire to the really harmful bad stuff, quote unquote.
[2841.94 → 2843.60] So where, where do we draw the line?
[2843.66 → 2845.34] There's, there are a lot of open questions there.
[2845.34 → 2845.82] Yeah.
[2846.06 → 2858.00] When I was watching the, uh, the intelligence committee hearing that we've been alluding to in this episode, uh, this morning, that was a big issue because a great deal of this involves, you know, first amendment rights.
[2858.00 → 2870.18] Uh, and, and for those who are not, uh, us citizens, uh, the first amendment, uh, of our bill of rights, which is part of our constitution is the amendment that allows for free speech and free expression in the United States.
[2870.18 → 2876.60] And so that was, there was quite a bit of kind of legal oriented back and forth, much of, and I'm not a lawyer.
[2876.60 → 2878.26] So much of that went over my head.
[2878.74 → 2887.58] Um, and so, you know, I don't, I won't speak to that directly, but they really were talking about how do you handle this without violating first amendment protections.
[2887.58 → 2904.72] So some good news is that this morning in the, uh, house intelligence committee hearing that we've been talking about over, uh, the course of this episode, uh, they, they did in fact make some recommendations on how to contend with, uh, deep fake issues.
[2904.72 → 2908.90] And, uh, there were six explicit points that were called out.
[2908.90 → 2916.80] And I thought I'd just kind of not cover all the verbiage on each one, but just kind of the first sentence or so of each one, uh, which kind of gives you the sense of it.
[2916.80 → 2926.70] The first was Congress should implement legislation prohibiting us officials, elected representatives and agencies from creating and distributing false and manipulated content.
[2926.88 → 2934.56] Um, and as an addendum to that, they mentioned that the U S governments, you know, whatever kinds of statements they make should always be the truth.
[2934.72 → 2938.18] The official government statements and policy should always be based in truth.
[2938.32 → 2944.52] The second thing was that policymakers should work jointly with social media companies to develop standards for content accountability.
[2944.92 → 2955.84] The third was that the U S government should partner with the private sector to implement digital verification signatures, uh, designating the date, time, and physical origination of content.
[2956.30 → 2964.16] Uh, the fourth one was that social media companies should enhance their labelling of synthetic content across platforms and work as an industry.
[2964.16 → 2969.42] To codify how, uh, and when manipulated or fake content should be appropriately marked.
[2969.72 → 2981.38] The fifth was that the U S government from a national security perspective should maintain intelligence on adversaries capable of deploying deep fake content or the proxies that they employ to conduct such disinformation.
[2981.90 → 2991.36] And the final one they noted was public awareness of deep fakes and its signatures will be greatly assisted in tamping down the attempts to subvert U S democracy and incite violence.
[2991.36 → 2992.36] So those were good.
[2992.36 → 2992.64] So those were good.
[2992.74 → 3009.04] And, and I think the, uh, the intelligence committee heard that there, there was some debate about the legal issues, uh, regarding first amendment, uh, concerns, but it was good, you know, to see them wrapping up with potential ways forward to mitigate the dangers that we've been talking about on this episode.
[3009.04 → 3039.02] Um, I see a couple of things in there.
[3039.02 → 3040.30] You know, exactly.
[3040.68 → 3043.38] So there's, there's competing interests here always, right?
[3043.42 → 3043.78] Of course.
[3043.90 → 3047.18] Um, so, uh, so it'll be interesting to see how that pans out.
[3047.28 → 3054.18] Um, the other thing is, um, you know, main maintaining intelligence on, on adversaries capable of deploying deep fake content.
[3054.18 → 3055.90] I think that includes me.
[3056.02 → 3060.40] I don't want to give myself away, but you know, I'm capable of deploying it.
[3060.76 → 3062.86] I guess I'm not an adversary of the U S government.
[3062.86 → 3064.92] At least I don't consider myself to be so.
[3064.92 → 3067.78] Um, but, uh, it is interesting to me.
[3067.90 → 3074.64] I mean, that that's like everyone who knows how to like clone a repo on GitHub and run that code.
[3074.74 → 3075.22] I don't know.
[3075.60 → 3080.90] Um, I guess probably what they're getting at is, is, uh, government entities and other things.
[3081.02 → 3081.70] That's what I think.
[3081.76 → 3085.00] But it seems like there's a there's a huge range of things.
[3085.00 → 3091.88] Uh, I guess I don't want the government maintaining intelligence on me since I'm capable of deploying those technologies, I guess is what I'm saying.
[3091.88 → 3092.26] Yeah.
[3092.36 → 3101.96] I think the intent of the recommendation was, was really, uh, from the perspective of the United States, uh, foreign adversaries is what that was looking at.
[3102.06 → 3102.46] Makes sense.
[3102.54 → 3105.30] That was certainly an impression I came away from listening to the testimony.
[3105.58 → 3105.80] Yep.
[3105.80 → 3115.12] So I guess, uh, maybe one way we could wrap up this discussion is to kind of give you some good learning resources and links on this subject.
[3115.40 → 3120.18] Uh, not so much on to learn how to make, uh, deep fakes.
[3120.18 → 3134.18] Cause you probably also don't want to have, uh, uh, the U S government maintaining intelligence on you, but, uh, but maybe just kind of learning about deep fakes, the state of the art and also, uh, you know, detection methods and other things.
[3134.18 → 3148.94] I think one, one good link, if you, if you just go back one fully connected episode to when we're talking about GANS and, uh, reinforcement learning and transfer, certainly GANS and transfer learning come into play in, in this discussion in a, in a big way.
[3149.16 → 3154.50] Um, there's also a good over that good overview article that I mentioned from the Washington Post that we'll link.
[3154.60 → 3159.70] That's not really technical, but does provide a good amount of links in it as well.
[3159.70 → 3166.20] And then there were a couple of, uh, workshops that I found, um, actually right now ICML is going on.
[3166.36 → 3180.18] Um, there's a, uh, workshop there, uh, that I'm assuming we'll post kind of, uh, papers and maybe some results and discussions about, uh, synthetic realities, deep learning for detecting audiovisual fakes.
[3180.18 → 3187.44] Uh, there's also a workshop that happened at applied machine learning days this year, um, about fake news detection.
[3187.44 → 3196.98] And we'll link that there's actually a GitHub repo, um, that kind of goes through a tutorial and some ideas and slides about, uh, fake news detection.
[3196.98 → 3203.84] So I think those would be good starting places, but, um, yeah, I appreciated the discussion today, Chris.
[3203.84 → 3207.34] I think, um, it was good to talk through some of these things.
[3207.34 → 3211.48] It was difficult in many ways. Um, I like to be generally positive.
[3211.48 → 3215.40] I hope that comes through in the podcast, but I think we both do, actually.
[3215.52 → 3216.66] It's pretty heavy topic.
[3216.78 → 3223.72] Yeah. I think we have a responsibility, uh, to our listeners and in general, just to be able to fairly represent things.
[3223.72 → 3227.48] And, uh, obviously a lot of the things that we talk about are just exciting and fun.
[3227.50 → 3230.22] And I think, uh, I hope that we come off that way to our listeners.
[3230.50 → 3235.88] Uh, but there's occasionally some scary stuff in this field and I think it's our responsibility to represent that as well.
[3235.88 → 3246.50] So I hope our listeners, uh, feel a little bit more, uh, attuned to this topic and, uh, sorry for the downer of an episode and, uh, appreciate very much everybody sticking in with us through this.
[3246.66 → 3248.08] Um, it was, it was a good talk, Daniel.
[3248.28 → 3249.88] Yep. Definitely. We'll talk to you next time, Chris.
[3249.96 → 3251.12] Talk to you next time. Thanks a lot.
[3251.12 → 3266.58] All right. Thank you for tuning into this episode of practical AI. If you enjoyed this show, do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it. If you are on Twitter or social network, share a link with a friend, whatever you got to do, share the show with a friend.
[3266.58 → 3280.62] If you enjoyed it and bandwidth for change log is provided by fast learn more at facet.com. And we catch our errors before our users do here at change law because of roll bar. Check them out at robot.com slash change log. And we're hosted on Linde cloud servers.
[3280.62 → 3304.50] Head to leno.com slash change log. Check them out. Support this show. This episode is hosted by Daniel Whiten ack and Chris Benson. The music is by break master cylinder, and you can find more shows just like this at change law.com. When you go there, pop in your email address, get our weekly email, keeping you up to date with the news and podcasts for developers in your inbox every single week. Thanks for tuning in. We'll see you next week.
[3310.62 → 3312.62] Bye.
