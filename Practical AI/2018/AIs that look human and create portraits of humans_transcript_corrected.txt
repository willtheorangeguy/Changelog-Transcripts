[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com, and we're hosted
[11.42 → 17.36] on Linde servers. Head to linode.com slash Changelog. This episode is brought to you by
[17.36 → 23.72] DigitalOcean. They now have CPU optimized droplets with dedicated hyper threads from best in class
[23.72 → 29.18] Intel CPUs for all your machine learning and batch processing needs. You can easily spin up
[29.18 → 34.74] their one-click machine learning and AI application image. This gives you immediate access to Python 3,
[35.20 → 42.68] R, Jupyter Notebook, TensorFlow, Sci kit, and PyTorch. Use our special link to get a $100 credit for
[42.68 → 51.28] DigitalOcean and try it today for free. Head to do.co slash Changelog. Once again, do.co slash Changelog.
[59.18 → 68.60] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[69.02 → 74.52] productive, and accessible to everyone. This is where conversations around AI, machine learning,
[74.56 → 78.66] and data science happen. Join the community and snag with us around various topics of the show
[78.66 → 84.48] at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[89.18 → 95.22] Welcome to Practical AI. This is Chris Benson, and with me is Daniel White nick. How's it going today,
[95.30 → 99.72] Daniel? It's going great. How about with you, Chris? Doing pretty good. Looking forward to going
[99.72 → 104.10] through all these cool news stories we have today. What have you been up to lately? Yeah, I've been
[104.10 → 109.32] doing a lot of learning myself. I've been doing a lot of learning about graph structure data. I'll
[109.32 → 115.08] actually mention a couple of things related to that later in the episode, but also been working a
[115.08 → 119.72] little bit and learning a little bit about Vega data visualization library. I think I mentioned
[119.72 → 126.28] in a previous episode. Yeah, you did. I've had a desire for a long time to learn D3, but I have no
[126.28 → 134.50] experience at all with JavaScript. But Vega is this cool data visualization library that actually,
[134.68 → 140.46] I think it uses D3 under the hood, but essentially the interface for the data visualization creator
[140.46 → 146.48] is JSON, which I am perfectly fine with. So that was a lot more approachable for me. And yet you can
[146.48 → 152.70] still get these really cool, interactive, appealing data visualizations out of it. So I've been kind of
[152.70 → 157.16] tailoring some of my graph data into that world. And that's been a lot of fun. What about you?
[157.62 → 164.18] Well, technically, I've had my TensorFlow tutorials tab open a lot this week, and I've been doing some of
[164.18 → 169.08] the tutorials that I hadn't gotten around to that I've been meaning to for a while, procrastinated on.
[169.08 → 175.40] But I'm also getting ready to go to Nashville this weekend, Vanderbilt University, there the
[175.40 → 180.96] women in computing group sponsors the Emerge conference, and where they talk about emerging
[180.96 → 186.28] technologies, they're talking about AI. And I am really looking forward to going up there and
[186.28 → 192.82] talking about AI and actually talking a little bit about the world that that my daughter Athena is
[192.82 → 196.72] going to grow up in. And so that is, I'm really excited about that.
[196.72 → 203.22] Yeah, that's awesome. That sounds like a great opportunity. I would tell you to get some
[203.22 → 208.92] Martin's barbecue. But as you and I are both, both don't eat meat, that's probably not going to do any
[208.92 → 214.32] good. But yeah, yep. Yeah. Yeah. Barbecue doesn't work for at least for me for a vegan.
[214.50 → 220.64] Yeah, yeah. For for for us both. But I'm sure you'll find some other interesting things.
[220.64 → 227.64] I will find suitable rabbit food to eat. Let's go ahead and get into some news and updates here.
[228.26 → 233.16] Again, for those new listeners, we do this kind of news and updates show to highlight some of the
[233.16 → 240.10] things that have come across our radar in the AI world. The first of those for me was this article,
[240.40 → 245.86] which I'm sure is also information is published about it elsewhere. But where I saw it was on NPR.
[245.86 → 252.76] And they have this article entitled AI produced portrait will go up for auction at Christie's.
[253.28 → 259.44] And so essentially what this is, is there's an art collective that call themselves obvious.
[259.84 → 265.36] They say that they make paintings using artificial intelligence. They've they've kind of
[265.36 → 270.72] been doing a series of these. And they have a picture of the painting, it kind of looks like a
[270.72 → 276.84] kind of rough person in kind of maybe an older kind of old masters sort of style,
[276.84 → 281.98] kind of looks like a clergyman or something like that. And then in the bottom right-hand corner of
[281.98 → 287.88] the painting, there's this math formula. So that's probably maybe one indication that it's not quite
[287.88 → 293.60] a normal picture. But anyway, there's this painting, and it's going up for auction. And like I say,
[293.64 → 298.76] they've already sold one of these, but this one is estimated to sell for around seven to 10 grand.
[298.76 → 303.76] So seven to $10,000. And yeah, I think this is pretty interesting. What do you think,
[303.84 → 305.48] Chris? Would you hang this in your house?
[305.82 → 310.78] You know, I probably would. Now I will say that I know nothing about art. I never took art history.
[311.28 → 316.66] And so I'm just coming at it as your everyday guy looking at it. If I like it, I'll certainly hang it
[316.66 → 321.92] up. But you know, it really is. I find this fascinating. But in that, it's similar to some of the
[321.92 → 327.40] other things that we've seen lately about art and different creative pursuits being, you know,
[327.40 → 334.14] attempted in the world of AI. And a recent thing that I had heard was, and I can't remember exactly
[334.14 → 338.52] where I heard it, but it was about AI produced music being compared where they were kind of
[338.52 → 343.68] recreating classical music that, you know, the great masters had produced, and they would let
[343.68 → 349.86] people listen to it. And they would either kind of bias them as the AI was maybe the created by the
[349.86 → 354.08] human master or vice versa. And they were switching that up with different groups. And they found that
[354.08 → 359.86] people tended to follow their biases, oftentimes thinking that humans would always be better than
[359.86 → 363.92] AI. But if they kind of switched them behind the scenes on them, they would stick with their biases,
[363.92 → 367.22] even if they were listening to the other one. So I hope that made sense.
[367.48 → 368.26] But yeah, it's interesting.
[368.54 → 374.88] It really made me start to believe that I think that there will be types of creativity that AI does
[374.88 → 380.08] very well at. And you know what, if it can create beautiful art like this, I would certainly hang it
[380.08 → 384.54] in my house, especially if it is less expensive than buying at the art gallery.
[384.96 → 390.36] Yeah. And I mean, I think this is something not totally new in the sense that we've had,
[390.40 → 397.64] you know, computer and machine generated music and other things in the past. And a lot of that,
[397.74 → 402.74] you know, is digital signal processing and other things that have been utilized to create new types
[402.74 → 407.80] of sounds and soundscapes. And people seem all right with that. I think that this is kind of
[407.80 → 412.80] new for people in the sense that, you know, this art collective, I don't know what you would call
[412.80 → 417.38] the people in this case, if they're artists, I guess they're artists, the artists that created
[417.38 → 424.68] this AI that created the painting, they really wanted to give the AI a lot of free rein in terms
[424.68 → 430.22] of what it generated and kind of take themselves out of the picture, I guess. And it seems like they
[430.22 → 435.18] do give a little bit of technical explanation. It's not a technical article. Maybe there is another
[435.18 → 441.34] technical one somewhere that our listeners could point us to, but they do say that they fed in
[441.34 → 447.00] to the system, a data set of 15,000 portraits painted between the 14th century to the 20th century.
[447.36 → 452.78] The generator makes a new image based on the set. Then the discriminator tries to spot differences with
[452.78 → 458.72] the human made image and the one created by the generator. So there's definitely kind of a feedback
[458.72 → 465.64] thing going on here with these models. And so there does seem to be a lot of interesting tech behind
[465.64 → 471.42] it. And obviously it is creating something of value, whether people want to say it's a value or
[471.42 → 478.58] not, because people are assigning it a value, right? Seven to $10,000. So yeah, it's fascinating.
[479.16 → 484.10] Yeah. And just for listeners who may not have picked up on it, you were referring to generative
[484.10 → 488.66] adversarial networks, which are also known as GANs, when you were mentioning generators and
[488.66 → 493.04] discriminators. And they seem to be, that architecture seems to be really leading the way
[493.04 → 499.08] in creative efforts here. Yeah, definitely. And hopefully we can have a show that talks about that
[499.08 → 504.64] sometime, but that would be a great episode. Yeah, it would be. I would be interested to kind of hear
[504.64 → 509.82] the makeup of this team. Obviously they have very technical people on the team because this is not
[509.82 → 514.84] something that is, you know, I imagine that they teach in art school, right? So I would be really
[514.84 → 519.64] interested to see, hear the makeup of their team, if they have kind of a combination of artists and
[519.64 → 526.34] data scientists or AI people. I'm not sure. I would be interested to hear that and hear how that kind of
[526.34 → 534.30] maps to teams we see emerging in industry in general. Yeah. I think this kind of AI created art is
[534.30 → 539.72] going to become very, very common in the days ahead. So it'll probably become perfectly normal for us
[539.72 → 545.70] in the not so distant future. Yeah. And speaking of AI generated faces, or maybe not generated faces,
[545.70 → 551.24] but faces and AI, you ran across something we were just discussing before the show that was
[551.24 → 557.84] pretty interesting, maybe more on the little bit disturbing or alarming side. But tell us a little
[557.84 → 561.90] bit about that. I'm actually going to lead with my last point and say, this is another thing that I
[561.90 → 566.70] think is going to become extremely common in the days ahead. And that is, there is a company called
[566.70 → 574.24] Magic Leap, who has a personal assistant that is very much like Apple Siri or Amazon Alexa.
[574.58 → 581.52] It's kind of grounded in AI and augmented reality. And they have named theirs Micah. And apparently,
[581.78 → 589.02] Micah looks and acts human. And she can give you the and when I say she, if you look at the pictures
[589.02 → 594.40] that they have here, it is a woman. And if you interact with her, you can either do voice only,
[594.40 → 600.20] or apparently they have a pair of augmented reality glasses called Magic Leap One. And if you put those
[600.20 → 606.52] on, then you can actually see her in front of you, and you can interact with her. And apparently people,
[606.80 → 610.60] they note in the article that people that are reacting, that are interacting with her in this
[610.60 → 615.52] augmented reality will oftentimes, like if she leans in, they'll kind of lean back from a personal
[615.52 → 621.74] space standpoint and, and truly act as though they are dealing with a human being beside them. So very
[621.74 → 627.60] interesting and a bit creepy, maybe for us. I'm, I'm betting that my six-year-old daughter won't
[627.60 → 631.94] find it so creepy as she gets older, because I think they'll be ubiquitous. I think she'll grow up
[631.94 → 634.26] not knowing a world without them all over the place.
[634.64 → 640.94] Yeah. And I think it's kind of one of those things, and I'm not a UI UX type person, although I do value
[640.94 → 645.96] design, but I know that there's this kind of principle and I forget, I think it even has a name where
[645.96 → 652.88] if you try to make something look human and you kind of slightly are off, then it's kind of,
[652.88 → 659.02] it comes off super creepy and weird. Whereas if you just created something that was really like
[659.02 → 664.82] avatar-like and obviously not human, but kind of mimicking human, then that could actually come
[664.82 → 669.32] off, you know, a little bit better in the, in the user experience. So it's interesting to see people
[669.32 → 674.54] going both of those directions. I don't know which will kind of win out. I don't know. Furthermore, I don't know
[674.54 → 680.06] that I want, I want to be interacting with a lot of Micah's in the future, but like you say,
[680.12 → 682.52] maybe that's something that will just become commonplace.
[682.96 → 688.62] So as we are approaching Halloween, as this episode comes out, I'm going to challenge our
[688.62 → 694.14] listeners to either get a picture of Micah or any other, you know, human-like personal assistant out
[694.14 → 700.54] there and put in our Slack channel, your version of the avatar for Halloween. In other words, make your
[700.54 → 707.02] change. Let's, let's create a meme for the next week. Sounds, sounds good. So moving on to kind of
[707.02 → 713.22] a set of things that I have been running across. And really, I think I've been exposed to some of
[713.22 → 719.44] these things because as I mentioned in my personal work with the nonprofit SIL International, I've been
[719.44 → 724.92] doing a lot of work with graph structured data, specifically in the language space. So language
[724.92 → 730.24] families and populations, how they're related, what countries they're in, what resources are
[730.24 → 734.86] available in those countries, who's writing those resources, where they're coming from, what countries
[734.86 → 740.52] they're coming from. And so this kind of graph, very dense information that's represented in a graph
[740.52 → 747.66] structure. And obviously, as I've been going through that various ways that we could apply AI and machine
[747.66 → 752.80] learning have popped up. And I've been interested to see over the past couple of weeks, a bunch of
[752.80 → 757.96] articles from people that I didn't know were really working in graph data and machine learning pop
[757.96 → 764.68] up. And one of those is this article, which I actually saw on LinkedIn, but it's from Helena,
[764.88 → 772.16] Helena, uh, do sorry, uh, mispronouncing the name from Elsevier, which is the company that at least one
[772.16 → 778.64] company that has journal articles and a bunch of other tech in academia. And she wrote this kind of
[778.64 → 785.70] summary spawning out of the or stemming from the international semantic web conference in Monterey,
[785.76 → 792.58] California. And her kind of view on the state of things is that people are really interested in graph
[792.58 → 799.42] structured data and people are using machine learning on graph structured data. And she provides
[799.42 → 804.86] a lot of great links to things that people are doing, including helping people find relevant
[804.86 → 811.96] healthcare information and health data in knowledge graphs. There's also ones that are using graph
[811.96 → 818.30] structured data to find effective drugs for incurable diseases. There's people, uh, using
[818.30 → 825.84] graphs to kind of analyze documents and, and, and find related things of course, and, uh, and find
[825.84 → 831.58] groupings within social networks and all of that stuff that maybe is more obvious to us. But then she also
[831.58 → 837.80] gives some references to people that are doing deep learning and machine learning on graph structures.
[838.34 → 845.20] And another thing that I saw is related to that was this semantic scholar project from the Allen
[845.20 → 852.02] Institute for AI, where they're really using graph structured data and AI to help people to guide them
[852.02 → 858.64] to relevant academic works and scientific works, because it's really hard to find that as you're
[858.64 → 863.52] searching through all these different papers from all sorts of journals. So that's really cool to see.
[863.62 → 869.44] They provide a bunch of tooling around that. And then even from deep mine. So deep mine came out
[869.44 → 876.44] and open source this graph nets library. So it's on GitHub at deep mine slash graph underscore nets.
[876.74 → 885.00] And this is a library for using TensorFlow on graph structured data. So, uh, to be clear, this is not,
[885.00 → 890.10] I mean, there's still a computational graph within TensorFlow in many cases, but this is actually
[890.10 → 896.46] doing using TensorFlow models on graph structured data. So a graph is your input, a graph is your,
[896.52 → 901.42] your output, and they have open sources, but there's also some really cool things to play with.
[901.56 → 908.10] There are some collaborator notebooks where they can show you how to kind of figure out and learn the
[908.10 → 913.64] fastest or shortest path between things in a graph, like in a social network or a graph of,
[913.64 → 919.20] of health resources or whatever it is. And so I would recommend taking a look at that. And in general,
[919.20 → 923.90] take a look at some, you know, of the stuff going on with graph structured data. I think there's a
[923.90 → 925.84] lot of interesting work going on.
[925.84 → 930.78] Yeah. You know, it's, it's interesting. You just pointed out that this is to apply own graphs versus
[930.78 → 936.68] we tend to think of, we think of graph data a lot, but we tend to think of it as being part of,
[936.80 → 941.60] of the framework or the model, uh, the architecture that we're in. So as you were talking,
[941.60 → 945.50] it made me realize that I actually have a lot to learn on that. So I'm definitely going to
[945.50 → 949.18] dig into these links after the episode and try to ramp up on it myself.
[949.38 → 950.12] Awesome. Yeah.
[950.54 → 957.72] So I ran across an article this past week from MIT, and it was actually in, uh, on news.mit.edu.
[957.98 → 964.76] And they have announced that they are now going to build the new Stephen A. Schwartzman
[964.76 → 969.64] College of Computing. And, uh, you may on initial, just hearing that you may say, okay, well,
[969.64 → 974.00] that's what MIT does. They do computing, but this is a little bit of a different approach
[974.00 → 979.36] to setting up a new college. They received a $350 million foundational gift from Mr.
[979.36 → 984.78] Schwartzman, who happens to be the chairman and CEO of Blackstone. And then on top of that,
[984.84 → 989.80] they have what amounts to a $1 billion commitment. And what they're trying to do here with this new
[989.80 → 998.46] college of computing is to build an, uh, an interdisciplinary school around AI and the various, uh, fields
[998.46 → 1004.64] that it touches on to try to kind of drive things into where we're seeing the future go as, as we're
[1004.64 → 1010.10] living it right now. The AI world has really revolutionized education in that space. And,
[1010.16 → 1015.20] and some of the things that MIT notes is that they want to, uh, reorient. And I'm reading from the
[1015.20 → 1020.48] article when I say this reorient MIT to bring the power of computing and AI to all fields of study at
[1020.48 → 1025.98] MIT, allow the future of computing and AI to be shaped by the insights from all disciplines.
[1025.98 → 1031.80] They have 50 new faculty positions to support it. It's going to give, uh, there's a shared structure,
[1031.80 → 1036.96] uh, with other schools that they're doing. And they're really looking at trying to produce students
[1036.96 → 1042.10] that can operate in this interdisciplinary approach. And I think that's fantastic personally,
[1042.10 → 1047.24] because in my own experience, AI touches on other fields almost every time you use it. It's,
[1047.30 → 1052.44] it's never a standalone thing by itself. It always intersects other areas that you're using it on.
[1052.44 → 1053.32] What'd you think, Daniel?
[1053.58 → 1058.24] I mean, I think this is great. I think that coming from, you know, I've, I've always,
[1058.40 → 1063.88] I'm glad that I came from an academic and a physics perspective and I really enjoyed physics. I'm,
[1064.00 → 1070.02] I'm really glad that I spent my time in that world, but kind of what I tell people when I talk to them
[1070.02 → 1074.60] about academia and different disciplines and different departments within academia is that,
[1074.60 → 1079.78] you know, physics is kind of almost in a, in a lull in the sense that there hasn't been
[1079.78 → 1086.54] really like crazy paradigm shifting stuff going on for, for a little while. And so it's maybe not
[1086.54 → 1091.82] receiving, you know, quite as much funding or having as much enthusiasm in terms of grad students
[1091.82 → 1096.70] going into physics and all of that stuff. But on the other hand, computer science, especially with AI,
[1096.70 → 1102.44] and then also in some ways biology are really seeing this surge of enthusiasm. And I think this
[1102.44 → 1107.66] is one of the evidences of this. I mean, 50 new faculty members is, is crazy. And I mean,
[1107.66 → 1112.46] one of the things that I'm hoping they do talk about education here. I'm hoping that along with
[1112.46 → 1117.80] some of the stuff that MIT has already released, that they're able to release some of these resources,
[1117.80 → 1125.52] whether it be lectures or tools or documentation or other things to the community at large. And so that
[1125.52 → 1131.30] we might be able to benefit from, from this work as well. Because I know I love schooling. I love learning.
[1131.30 → 1137.80] I kind of like to go back and maybe go back to MIT and get this degree, but I imagine that probably
[1137.80 → 1141.72] where I'll intersect with it is with whatever resources they release to the community.
[1142.22 → 1147.34] Yeah. You know, I really envy the students that are just going into college or graduate school
[1147.34 → 1154.80] this moment in time, because just in the last three years, education around computing and AI and
[1154.80 → 1160.28] related fields has changed so dramatically and really taken off that if you came out of school five years
[1160.28 → 1165.76] ago, the curriculum that you went through is, is already changed since then. And so the rest of us
[1165.76 → 1170.66] that are, you know, past school at this point are having to continue to, to learn and catch up and do
[1170.66 → 1175.32] that. So I almost wish I could transport myself back to the beginning of college right now and just
[1175.32 → 1180.00] experience this because it's, it's hard for me to imagine a better way to spend the time.
[1180.34 → 1187.28] Yeah, definitely. And speaking of spending our time and community stuff in our last news and updates
[1187.28 → 1193.00] show, I mentioned a few conferences and CFPs that were open. And I want to continue to do that. I
[1193.00 → 1198.22] really encourage our listeners and encourage myself to make the effort to get out into the community,
[1198.22 → 1206.00] to meet in real life and have discussions with your AI community, learn from, you know, some of the
[1206.00 → 1210.74] people that are working in the space, hear some great talks. And the conference that I wanted to
[1210.74 → 1218.04] mention this time around is CSV conference or CSV cone version four, which is going to be May 8th
[1218.04 → 1224.80] through 9th, 2019 and in Portland, Oregon. And this is a conference that actually I was aware of last
[1224.80 → 1230.14] year, but I think I had a conflict with some other events. So I wasn't able to go, but it's one that I'm
[1230.14 → 1235.06] definitely interested in attending this following year, and they have their CFP. It looks like it's open.
[1235.06 → 1240.74] You can submit a talk, and it looks like just a really great fun conference. They even have a
[1240.74 → 1247.74] mascot, the comma llama, which seems, seems pretty exciting. That is cool. So if you're a fan of data
[1247.74 → 1253.90] or llamas, this is the conference for you, but yeah, it's not only about CSVs, and maybe you're thinking
[1253.90 → 1259.28] of spreadsheets or something, but I think there it's a nonprofit community conference, which is really
[1259.28 → 1265.98] great. And there are a lot of diverse topics. They're talking about data sharing and data analysis from
[1265.98 → 1270.96] science, journalism, government, and open source. And I think it would be a really great conference
[1270.96 → 1277.26] to go to, to get exposed to a lot of different ways that data analysis and AI is being used across
[1277.26 → 1282.36] industry, how data is being shared, all of the all the subtleties that go along with that. So
[1282.36 → 1287.44] yeah, I'm excited. I'm going to, I'm going to try to submit a talk, and hopefully I can,
[1287.44 → 1291.32] can make it there. That sounds good. I think I'll do the same. And you brought up a good point
[1291.32 → 1295.54] a moment ago, and that is just, you know, getting involved in your community to take a second and
[1295.54 → 1303.26] share an experience I had back in late 2016. I was deeply interested in this space and I happened to
[1303.26 → 1307.54] be in Atlanta and I thought I looked around at different meetups and different groups and no
[1307.54 → 1312.40] one was really tackling what I was interested in directly in these meetups. And I thought, well,
[1312.42 → 1316.04] I'm going to start a deep learning meetup. I have no idea if anybody will ever show up,
[1316.04 → 1319.38] but you know, I'll go ahead and give it a shot. And if it doesn't work out, it doesn't work out.
[1319.70 → 1324.74] It has been hugely successful. And that's just one case at the AI world, deep learning, machine
[1324.74 → 1330.56] learning, data science world. There are so many people, you don't have to have a PhD in these
[1330.56 → 1335.72] fields to be able to enjoy it. And so I would encourage anyone do what I did. You might be
[1335.72 → 1341.20] surprised at how many people will come out. We, I was shocked that we would have 60 to 120 people
[1341.20 → 1345.90] show up in person at any event. It was almost overwhelming. And I wasn't sure anybody would
[1345.90 → 1350.74] show up when I started. So wherever you happen to be, I would encourage you to go out and either
[1350.74 → 1355.30] start a meetup or some similar group and get to know the people in your area or your region
[1355.30 → 1359.20] that are interested in this, and you can help each other get along. So thank you, Daniel,
[1359.28 → 1361.04] very much for bringing up that suggestion.
[1361.54 → 1365.32] Definitely. Yeah. I totally agree with everything, everything you just mentioned.
[1365.32 → 1372.20] So I will dive into the last article before we go into learning resources. Periodically,
[1372.34 → 1377.78] we will talk about the world of medicine being impacted by AI. It's come up in several episodes
[1377.78 → 1384.50] prior. And Physics World had an article called Deep Learning Algorithm Identifies Dense Tissue
[1384.50 → 1391.12] in Mammograms. And so the Massachusetts Institute of Technology, MIT, and Massachusetts General Hospital
[1391.12 → 1396.58] developed a deep learning algorithm working together that assesses breast density and mammograms.
[1396.64 → 1403.70] And it does so very, very reliably. And this provides a tremendous tool for mammographies,
[1403.90 → 1408.00] if I'm saying that right, you know, doctors in this field to be able to use to help save lives.
[1408.34 → 1412.96] Apparently, and I wasn't aware of this specifically before I read the article, but dense breast tissue
[1412.96 → 1417.98] apparently masks cancers on mammograms, the common mammograms that people are getting every day these
[1417.98 → 1422.74] days. It makes the screening more difficult. And apparently that it can be an independent risk
[1422.74 → 1428.66] factor for breast cancer, the presence of it. And so in this case, the researchers trained and tested
[1428.66 → 1436.10] the algorithm on a data set that was 58,000 digital screenings that were mammograms. And so they divided
[1436.10 → 1443.14] that up into 41,000 for training and 8,600 for testing. And then during the training, the algorithm was
[1443.14 → 1449.38] given random mammograms to analyze. And in doing so, it was able to predict the most likely density
[1449.38 → 1455.44] category, which enables these doctors to save lives. And I just, it inspired me. I come from a family
[1455.44 → 1461.22] full of women. I'm the only boy. Furthermore, I have four sisters and I have a daughter as well, and my wife and my
[1461.22 → 1467.66] mother. And I see the impact of these things in their daily life. And so I was truly inspired by what
[1467.66 → 1472.10] what's happening in this field and the fact that these doctors are getting better and better tools every day.
[1472.10 → 1476.28] Yeah, this is awesome. And one of the things I was just reading through part of this while you were
[1476.28 → 1482.54] while you were talking is there's a quote in the article that says, then when radiologists view a
[1482.54 → 1487.94] scan at their workstations, they can see the models assigned rating, which they can accept or reject. And I
[1487.94 → 1493.80] think one of the big things that that is emphasized here, which I'm really glad to see is that this is really
[1493.80 → 1499.80] an AI augmentation of something the radiologists are doing. It's helping them actually do their job better. And it
[1499.80 → 1504.92] seems like the radiologists are very accepting of that they want to do their job faster, they want to
[1504.92 → 1509.46] make better predictions, because obviously, they care about their patients. And there's a lot of
[1509.46 → 1516.66] pressure on them as well. So this is really an welcome AI augmentation. It's not a article saying,
[1516.66 → 1522.76] you know, we're going to replace all radiologists with this sort of this sort of modelling, right? It's
[1522.76 → 1530.54] it's an augmentation that is actually very welcome, and makes things faster and cheaper and easier and better. So I
[1530.54 → 1533.52] think that's, that's a really important point to mention.
[1534.06 → 1540.54] Yeah, it's AI for good. And I think it shows the fact that it doesn't have to be an either or proposition. It's not
[1540.54 → 1547.46] humans versus the AI, like so many people are always putting out there, it's humans plus AI, make a much greater
[1547.46 → 1554.06] capability. And so I love seeing these examples of AI for good that can truly have a massive impact
[1554.06 → 1560.22] through our society. Awesome. Well, let's turn now to learning resources like we do in each of these
[1560.22 → 1566.16] news and updates shows, we provide some learning resources, I was just talking to a student the
[1566.16 → 1572.56] other day. And I think that there is a kind of stereotype that us working in AI, where we've got all
[1572.56 → 1578.24] the knowledge built up in our brains, and we're never having to consult the internet for things. But
[1578.24 → 1585.00] I always have, you know, Stack Overflow open in a tab, and my Slack channels open in a tab and forums and
[1585.00 → 1590.70] GitHub issues and all of those things. So, you know, we all need to constantly be learning from one another.
[1590.70 → 1595.88] And we want to share some of those resources with you. So one of the ones that actually came up this
[1595.88 → 1601.76] week, I'm teaching a corporate workshop. And one of the students in that workshop, we were going through
[1601.76 → 1608.52] learning rate, regularization rate, regularization, and some of these maybe concepts that can be hard,
[1608.60 → 1614.06] also in terms of just the jargon that you have to build up. And one of the students, they found the
[1614.06 → 1620.46] neural network playground at playground.tensorflow.org, and was saying that it was really helpful for them
[1620.46 → 1626.04] as they were thinking about these different, the different components that go into defining your
[1626.04 → 1630.82] model and the training process, number of epics, number of hidden layers, regularization,
[1630.82 → 1636.06] and regularization rate. And I agree, I think that this neural network playground, it's been around
[1636.06 → 1641.56] for a while, actually, I remember it. I used it. Yeah, I remember. Yeah, it's been around for quite
[1641.56 → 1646.14] a while. But I agree. I think it's, I mean, it is kind of interesting in the visualization, it's a
[1646.14 → 1650.92] really nice looking visualization. But I think even more so as you're learning a lot of this jargon,
[1650.98 → 1655.62] it can really help you firm up what is regularization rate and learning rate? Are they,
[1655.96 → 1660.54] how are they different? Why is there these two rates? You know, what does one do? What does the other one do?
[1660.54 → 1665.72] Those sorts of questions, I think, can be answered really nicely in this visual way. And you can
[1665.72 → 1671.40] modify things and update them. It's all interactive. And so definitely a really, perfect resource.
[1671.86 → 1676.58] Yeah, I mean, speaking for myself, I am a visual learner. And I remember when this came out,
[1676.86 → 1681.88] it's a fantastic tool. I'm playing with it right now. As we're talking, it graphically shows you as
[1681.88 → 1687.32] you've changed those different things, what that means to your architecture and what that output is.
[1687.32 → 1693.94] And it was one of the things that helped me grok how things would come out if I chose Tan H or Rely,
[1694.08 → 1699.04] for instance, because it will do it instantly for you there. So it's just a great way of if you've read
[1699.04 → 1703.42] up on something, and then you can go play with the idea and see it right there. So highly recommend it.
[1703.46 → 1704.22] It certainly helped me.
[1704.58 → 1709.74] Yeah. And the other one I wanted to mention just here quickly is actually coming from Lindsay Gulag,
[1709.92 → 1714.74] who was our guest in episode 17. So our last show. And of course,
[1714.74 → 1720.80] she did an amazing job at explaining bias in AI and how to fight that. And she mentioned this
[1720.80 → 1727.88] toolkit called the it's from IBM, it's called the AI Fairness 360 Open Source Toolkit.
[1728.04 → 1728.76] I remember.
[1729.04 → 1734.28] Yep. And I went ahead and took a look at that after the episode. And I was kind of pleasantly
[1734.28 → 1739.90] surprised in the sense that this isn't just like an open source toolkit that you go to a repo and look
[1739.90 → 1746.72] at it. They have a whole page full of demos, full of videos, papers, there are tutorials and example
[1746.72 → 1753.24] notebooks to help you kind of understand where bias creeps into the models. And also, you know,
[1753.52 → 1759.42] fairness metrics and state-of-the-art techniques and algorithms to help you mitigate bias in your
[1759.42 → 1764.74] algorithm so you can actually create more fair and better models. And so I would highly recommend
[1764.74 → 1769.86] taking a look at this resource, watching some of the videos. And I think it's a great place as you
[1769.86 → 1775.26] enter into a new project, really a good thing to revisit and think about, okay, what can I,
[1775.68 → 1780.58] what fairness metrics or what bias mitigation can I apply in this new project?
[1780.92 → 1785.62] It looks really great here. I had not looked at it prior to you bring it up. It was on my to-do list,
[1785.72 → 1791.40] but there are dozens of different topics to explore on this page. And so I'm looking forward to,
[1791.40 → 1795.42] to, I'm going to leave this tab open. Like I have dozens of tabs open. I'm going to leave this
[1795.42 → 1800.38] one open for after the show and go exploring. Awesome. What learning resources do you have,
[1800.44 → 1804.08] have for us this week, Chris? Well, I wanted to start off with one,
[1804.16 → 1809.78] and it wasn't one that I was typically thinking of as a learning resource, but I found myself,
[1809.78 → 1816.14] it's a medium site as in medium.com, the publishing platform that is called Towards Data Science.
[1816.40 → 1820.44] And it has different topics like data science, machine learning, programming, and visualization.
[1820.44 → 1827.94] And I find myself reading different topical posts on this site all the time and have for quite a
[1827.94 → 1833.06] while. Yeah. And I actually had a few tabs open this week from some of the articles I was looking
[1833.06 → 1837.26] through. And it occurred to me that this was a this was a learning resource for me personally.
[1837.26 → 1843.10] It's often where there'll be a particular topic that they, they will get covered in a post. And I may
[1843.10 → 1848.82] not have a lot of experience or exposure to that topic prior to reading. It's a starting point. It's a
[1848.82 → 1853.80] launching point for me to say, this is something I want to go learn more about, and then I'll go find
[1853.80 → 1858.58] other resources on it. But it's just an easy read. You can do it anywhere. You can pull up your medium
[1858.58 → 1863.86] app in your car. Well, maybe not in the car. I was thinking when you're stopped, but hopefully,
[1864.20 → 1868.62] yeah, don't, don't go reading medium while you're driving folks. I'm sorry I said that.
[1868.62 → 1875.00] So, but yeah, it's a great place, and it's, it's fun to read. And so I recommend Towards Data Science.
[1875.30 → 1880.96] I believe it's .com at the end of that. And then the other thing is I often get asked, you know,
[1880.96 → 1884.80] running the deep learning meetup and things like that, how reinforcement learning fits in and what
[1884.80 → 1889.90] exactly is it, and how is it related to deep learning? And there was a Forbes article that
[1889.90 → 1895.38] went around all the different feeds this week. I have a bunch of feeds in the AI space that I
[1895.38 → 1901.00] read from. And it came up in, in several of them and it's called artificial intelligence.
[1901.48 → 1904.86] What's the difference between deep learning and reinforcement learning? So this is a
[1905.18 → 1910.86] it's in Forbes, it's a non-technical explanation. That's very accessible where the, the writer kind
[1910.86 → 1915.66] of, he introduces the topic and kind of set, he starts off with what is deep learning? And he offers
[1915.66 → 1921.00] a few paragraphs on what that is. And then he goes into what is reinforcement learning and kind of
[1921.00 → 1925.24] gives that. And then he covers the difference between deep learning and reinforcement
[1925.24 → 1931.22] learning and finishes up by talking about how you may use deep learning as a component in your
[1931.22 → 1935.78] reinforcement learning. But it's a quick read. You can, you can probably do it in two minutes,
[1935.80 → 1940.34] I'm guessing, but it might give you a start. And if you're one of those people who are trying to figure
[1940.34 → 1945.28] out how these different, you know, these different things fit together, it's another good starting
[1945.28 → 1949.62] point, particularly for the non-technical folks in the crowd. So I recommend it.
[1949.62 → 1956.02] Awesome. Yeah. Um, I think that just the, the article's title in and of itself gives kind of
[1956.02 → 1961.62] tells that there is a misconception between, you know, that reinforcement learning and deep learning,
[1961.62 → 1968.42] uh, are necessarily different things or mutually exclusive, or how do they fit into one another?
[1968.42 → 1974.34] And I think that, um, that's really great to clarify. I would also recommend, we had a great
[1974.34 → 1980.30] discussion with, uh, Won Marimba, one of the co-founders of OpenAI and he, um, let us know,
[1980.64 → 1985.94] he gave us a great introduction to reinforcement learning and robots and, and, um, how they're
[1985.94 → 1990.98] using it in robotics. And that was episode 14, you know, included in the show notes and everything,
[1990.98 → 1994.48] but that's another great resource for, uh, reinforcement learning.
[1994.86 → 1999.68] He is a brilliant person. And I personally learned a lot from that episode. I was very impressed that you
[1999.68 → 2004.08] got him onto the show. He was a fantastic guest. And, uh, one of those that I keep going back and
[2004.08 → 2005.12] listening to over and over again.
[2005.20 → 2011.24] For sure. Thanks, Chris. I really enjoyed, uh, digging into these things. I also have a bunch
[2011.24 → 2015.14] of tabs open that I'm going to do some reading afterwards and look up a few of these things
[2015.14 → 2020.00] that you mentioned. And until next time, we'll, uh, try to keep my learning up, and then we'll,
[2020.10 → 2021.56] uh, we'll talk to you next week.
[2021.82 → 2026.82] Sounds good. If anyone happens to be, uh, in Nashville this Saturday, then I'm looking forward
[2026.82 → 2030.96] to seeing you at the Emerge conference and I will talk to you later on, Daniel. Take care.
[2031.12 → 2031.34] Bye-bye.
[2031.50 → 2031.80] Bye-bye.
[2034.08 → 2038.78] All right. Thank you for tuning into this episode of practical AI. If you enjoyed this
[2038.78 → 2043.30] show, do us a favour, go on iTunes and give us a rating, go in your podcast app and favourite it.
[2043.42 → 2046.88] If you are on Twitter or a social network, share a link with a friend, whatever you got to do,
[2047.10 → 2050.72] share the show with a friend. If you enjoyed it and bandwidth for change log is provided
[2050.72 → 2055.30] by fast learn more at fastly.com, and we catch our errors before our users do here at
[2055.30 → 2060.24] change log because of roll bar, check them out at robot.com slash change log. And we're hosted
[2060.24 → 2065.32] on Linde cloud servers at a leno.com slash change log. Check them out. Support this show.
[2065.46 → 2070.84] This episode is hosted by Daniel Whiten ack and Chris Benson. Editing is done by Tim Smith.
[2071.08 → 2076.18] The music is by break master cylinder, and you can find more shows just like this at change
[2076.18 → 2081.00] law.com. When you go there, pop in your email address, get our weekly email, keeping you up to
[2081.00 → 2086.56] date with the news and podcasts for developers in your inbox every single week. Thanks for tuning in.
[2086.72 → 2087.50] We'll see you next week.
