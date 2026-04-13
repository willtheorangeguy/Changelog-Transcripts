[0.00 --> 2.58]  As far as the first language goes, it doesn't really matter.
[2.58 --> 16.92]  If you're coming in from a data science point of view, what's the most important thing is when you see a data set that is quote unquote messy, can you like in your head write the general sequence of steps to make it clean again?
[17.16 --> 21.86]  I borrow all the terminology from the R world, which is like the concept of tidy data.
[21.86 --> 33.64]  And so if you can see a data set and know the steps on making it tidy, at that point, it really doesn't matter what language you use, because you can literally just look up like in the R world now in tidy verse, it's like pivot longer or wider.
[33.78 --> 36.80]  So you would just Google like pivot longer, wider tidy R.
[37.36 --> 40.78]  And then on the Python side, it will be like pivot longer, wider, like Python.
[41.08 --> 43.72]  One of those words will show up some search result.
[43.72 --> 53.78]  And I think that's probably the more important thing is just knowing the steps on processing data and then just treating programming as the thing to get you there.
[55.78 --> 58.50]  Bandwidth for Changelog is provided by Fastly.
[58.88 --> 60.76]  Learn more at Fastly.com.
[61.02 --> 64.08]  We move fast and fix things here at Changelog because of Rollbar.
[64.22 --> 65.90]  Check them out at Rollbar.com.
[66.14 --> 67.72]  And we're hosted on Linode cloud servers.
[68.68 --> 70.66]  Head to linode.com slash Changelog.
[70.66 --> 73.52]  This episode is brought to you by Digital Ocean.
[73.88 --> 74.52]  Droplets.
[74.92 --> 75.70]  Managed Kubernetes.
[76.06 --> 76.90]  Managed databases.
[77.42 --> 78.02]  Spaces.
[78.26 --> 79.16]  Object storage.
[79.44 --> 80.68]  Volume block storage.
[80.94 --> 84.42]  Advanced networking like virtual private clouds and cloud firewalls.
[84.62 --> 90.88]  Developer tooling like the robust API and CLI to make sure you can interact with your infrastructure the way you want to.
[91.28 --> 94.78]  Digital Ocean is designed for developers and built for businesses.
[94.78 --> 101.84]  Join over 150,000 businesses that develop, manage, and scale their applications with Digital Ocean.
[102.20 --> 105.64]  Head to do.co slash Changelog to get started with a $100 credit.
[105.98 --> 108.12]  Again, do.co slash Changelog.
[108.12 --> 133.76]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[133.76 --> 138.18]  This is where conversations around AI, machine learning, and data science happen.
[138.60 --> 143.20]  Join the community and Slack with us around various topics of the show at Changelog.com slash community.
[143.58 --> 144.54]  And follow us on Twitter.
[144.66 --> 146.26]  We're at Practical AI FM.
[152.92 --> 156.66]  Well, welcome to another episode of Practical AI.
[157.04 --> 158.80]  This is Daniel Whitenack.
[158.80 --> 171.20]  I am a data scientist with SIL International, and I'm joined, as always, by my co-host, Chris Benson, who is a principal emerging technology strategist at Lockheed Martin.
[171.56 --> 172.50]  How are you doing, Chris?
[172.78 --> 174.30]  I'm doing very well today, Daniel.
[174.34 --> 174.74]  How's it going?
[175.38 --> 176.94]  It's going great.
[177.18 --> 187.44]  Over the weekend on Saturday morning, my time, I gave a workshop at ODSC Europe, Open Data Science Conference Europe.
[187.44 --> 188.88]  And that was a good time.
[189.12 --> 191.78]  Virtual conferences are kind of fun because I get to connect.
[192.38 --> 194.64]  There were people joining from all over the world, kind of.
[194.76 --> 203.28]  So that was cool to get, you know, people joining into the workshop from sort of all over and get to discuss some fun things with them.
[203.40 --> 210.46]  We did some transfer learning and reinforcement learning and GANs with TensorFlow, which was fun.
[210.56 --> 214.80]  Transfer learning is very much the bedrock of a lot of, you know, industry work.
[215.08 --> 215.50]  Sure is.
[215.50 --> 222.98]  Reinforcement learning and GANs is like, for me, it's a really fun topic to play around with and have some fun with.
[223.04 --> 227.12]  It definitely has some practical application, but it's just kind of fun to get into.
[227.42 --> 228.80]  So that was a good time.
[228.88 --> 231.26]  It was a fun weekend in that sense.
[231.48 --> 232.10]  What about yourself?
[232.78 --> 235.30]  Well, over the weekend, just enjoying cooler weather.
[235.38 --> 236.04]  It's been nice.
[236.26 --> 239.94]  We're getting into, you know, about to get into the fall here, and that was pretty pleasant.
[239.94 --> 248.76]  Last week, I know that we may talk a little bit about public orientation, government type stuff potentially today in terms of conferences and stuff.
[248.92 --> 251.80]  And I was doing some work with the Air Force.
[251.90 --> 260.84]  It's amazing to see, you know, government, you know, following industry into advanced technologies, things that support AI, doing software development better.
[260.84 --> 264.50]  That was the last week for me, and it's just a pleasure.
[265.22 --> 266.12]  Yeah, yeah, cool.
[266.54 --> 269.66]  Yeah, it's definitely good to get some cooler weather, I'm sure, for you, too.
[269.68 --> 270.28]  I can't imagine.
[271.00 --> 272.56]  We've mentioned this before on the podcast.
[272.80 --> 273.38]  I just don't know.
[273.44 --> 274.88]  I don't know if I could survive Georgia.
[274.88 --> 280.52]  It's actually chilly outside right now.
[280.58 --> 281.04]  Yeah, it's awesome.
[281.46 --> 290.34]  It's amazing when you get through a Georgia summer, which is all very humid and hot, and you get to this first inkling of spring and everything.
[290.48 --> 291.64]  It's like, ah.
[292.12 --> 292.80]  Yeah, yeah.
[292.80 --> 308.84]  Yeah, well, as you mentioned in talking about sort of government and that vertical, which I know you're involved a lot in, recently got connected to the R conference, which I've spoken at before, the New York City version, which was a lot of fun.
[308.92 --> 312.02]  I think that was two or three years ago I was there.
[312.16 --> 316.52]  But now they do, of course, they're doing virtual conferences this year.
[316.52 --> 319.92]  I attended the one online recently.
[320.30 --> 323.12]  It was super high quality and a lot of fun.
[323.52 --> 324.94]  They had a great system for it.
[324.96 --> 328.28]  But they're doing several of these that are related to different verticals.
[328.36 --> 342.80]  There's going to be one coming up that is related to government and related sectors and what used to be the sort of DC conference but is now, of course, virtual and got connected to that.
[342.80 --> 349.56]  So we're actually going to, as the podcast, we're going to kind of do a media partnership with that conference, and that's going to be really cool.
[349.80 --> 360.64]  And as part of that, they helped arrange today for us to have a conversation with Daniel Chen, who's with us, who is a Lander Analytics data scientist.
[361.34 --> 367.36]  He's a PhD candidate as well at Virginia Tech and a former RStudio intern.
[367.76 --> 368.98]  So welcome, Daniel.
[369.08 --> 370.66]  It's great to have you on the show.
[371.24 --> 371.38]  Hi.
[371.68 --> 372.36]  Thanks for having me.
[372.36 --> 372.76]  Yeah.
[373.00 --> 377.56]  We're going to have to navigate this to Daniel situation.
[378.16 --> 379.92]  Chris, best of luck to you.
[380.02 --> 381.82]  If it makes it easier, you can call me Dan.
[382.56 --> 382.74]  Yeah.
[383.96 --> 388.28]  I may still respond to that accidentally, but we'll navigate this.
[388.36 --> 389.78]  I think we'll get through.
[390.08 --> 395.90]  I don't know about you guys, but it always bothered me when there's two people named the same.
[396.26 --> 399.74]  Sometimes people want to call that Daniel Squared or something.
[399.74 --> 405.34]  But that always really bothered me because it seems to me to be actually two Daniel, not Daniel Squared.
[405.50 --> 406.82]  Like there's two of them.
[407.26 --> 407.84]  That's two Daniel.
[407.92 --> 410.20]  It's not like I'm multiplied by Daniel Chen.
[410.20 --> 412.40]  You're not multiplied by yourself there.
[412.40 --> 413.28]  Right.
[413.28 --> 416.24]  I don't know if that's just my own peculiarity.
[417.92 --> 418.36]  No.
[418.48 --> 419.46]  My name's Chris.
[419.96 --> 422.10]  There were Chris's all over the place growing up.
[422.20 --> 423.50]  So I understand.
[423.76 --> 428.00]  You feel like you're melting into the background when there's like five Chris's in your class.
[428.40 --> 428.82]  I get it.
[428.82 --> 429.26]  Yeah.
[429.78 --> 443.12]  Well, on that note, Daniel, Daniel Chen, if you want to just let us know a little bit about yourself, about your background, how you got into doing what you're doing now, the path that you took to there.
[443.44 --> 444.94]  I'd love to hear a little bit about it.
[444.94 --> 445.38]  Yeah.
[446.38 --> 453.74]  So I grew up in New York City and I guess I've my dad is a software engineer.
[454.02 --> 460.52]  My parents, when they came to America, they both studied computer science in college.
[461.26 --> 469.58]  My mom doesn't do computer science related stuff anymore, but I've always had a computer at home since, you know, when I was a kid.
[469.58 --> 479.68]  So like back in the day, these were just like old company hand-me-downs and around high school, I went to one of the math and science high schools in New York City.
[480.14 --> 491.48]  And it was interesting because sophomore year, it was a requirement for all the sophomores to take one semester of computer science and one semester of technical drawing.
[492.00 --> 497.08]  And then the people who liked computer science at the time could take the AP class, et cetera, et cetera.
[497.08 --> 504.56]  But it was interesting the fact that like every single sophomore student in high school was exposed to programming some way, shape or form.
[504.88 --> 505.82]  Yeah, that's super interesting.
[506.44 --> 514.96]  Yeah, we actually, looking back on it, I have no idea how the instructors handled, like got all the material in because we covered in like one semester.
[515.20 --> 519.32]  We covered, we first went through NetLogo, which is like drawing turtles.
[519.32 --> 523.16]  And I made like a little blackjack game for that small project.
[523.44 --> 530.40]  Then we went through a scheme, which is like a Lisp language to talk about like lists and functions.
[530.40 --> 540.26]  And then like towards the end, we like got introduced to Python where it was like make your own prisoner dilemma kind of algorithm and we'll compete it in the class.
[540.40 --> 541.62]  And that was all in one semester.
[541.62 --> 548.88]  So like as an educator, like I start teaching data science now, I'm like always baffled when I think back, like how do they make that work?
[549.32 --> 555.14]  Because like there's no way like I wouldn't be able to teach all of that stuff even in like a semester.
[555.38 --> 556.90]  So that was super interesting.
[557.52 --> 557.66]  Yeah.
[557.80 --> 565.12]  Did it seem overwhelming at the time or did it just seem like new and like exciting stuff or different stuff?
[565.12 --> 565.56]  Yeah.
[566.20 --> 567.60]  So it was new and exciting.
[568.24 --> 574.18]  But as I started teaching more, I didn't realize it at the time.
[574.76 --> 578.66]  But yes, there's always at the because of it was a math and science high school.
[579.00 --> 582.08]  Like clearly there were people who have done this stuff before in the past.
[582.20 --> 582.34]  Right.
[582.68 --> 585.38]  And then there are the people who like have seen this for the first time.
[585.70 --> 589.64]  And so I was in a camp of like I've actually never programmed before.
[589.64 --> 594.26]  But then there's all these kids who like know the answer as the questions being written on the board.
[594.36 --> 597.36]  And I'm staring at a blank like piece of paper, like how do I do this?
[597.80 --> 604.64]  And so it was actually that was like one of the like I don't think I'm ever going to do this for a living moments.
[605.60 --> 605.72]  Yeah.
[605.78 --> 611.84]  It pushed you into that place rather than sort of further inspiration, at least at the time.
[612.40 --> 612.64]  Yeah.
[612.80 --> 617.36]  Well, like I've always been interested about like just tech and things.
[617.36 --> 619.56]  But yeah, programming definitely at the time.
[619.64 --> 623.10]  It seemed this is not for me kind of ordeal.
[624.30 --> 624.74]  Yeah.
[624.80 --> 628.42]  And then fast forward a little bit to my undergraduate years.
[628.90 --> 633.14]  I ended up getting a computer science minor just because I was like, you know what?
[633.16 --> 634.54]  I'm just going to go go do it.
[634.54 --> 636.90]  Like just learn how to program like formally.
[637.28 --> 642.72]  And that's when I realized like looking back, like the whole people who have seen it before versus not seen it before.
[642.72 --> 650.18]  Like my intro classes, they were relatively easy for me, even though it was like, for example, the one C++ class.
[650.24 --> 656.98]  I've never actually programmed in C++ before, but I didn't have to think about like, you know, print statement debugging.
[656.98 --> 660.62]  Like that's like not a brand new concept at the time.
[660.76 --> 661.12]  Right.
[661.12 --> 667.44]  Or, you know, if statements and loops are no longer something I need to struggle with because I've seen it before in the past.
[667.54 --> 670.00]  And then I actually felt bad for some of my students.
[670.00 --> 675.82]  I picked up my computer science minor like junior or senior year of my undergraduate career.
[675.82 --> 684.84]  And then I felt bad for like the freshmen coming in who were like, they've wanted computer science as like their degree, but they've like, but they've never seen it before.
[684.84 --> 686.92]  And like, they actually struggled really hard.
[687.58 --> 693.86]  So like, that's when I like had those, those feelings back in high school again.
[694.38 --> 695.52]  Gives you empathy, doesn't it?
[695.84 --> 696.10]  Yeah.
[696.24 --> 696.42]  Yeah.
[696.50 --> 696.70]  Yeah.
[696.70 --> 700.38]  That's when I actually started realizing like, hey, wait, I've actually seen this before.
[700.40 --> 701.52]  And that's why it's easy for me.
[701.52 --> 704.86]  So and in some way that like carried forward.
[704.86 --> 712.94]  So like after, after that, I got my master's in public health in epidemiology, which is somewhat relevant these days.
[713.76 --> 716.30]  And it was a two year program.
[716.78 --> 724.68]  And the second year I ended up taking a intro to data science class with some of my MPH friends.
[724.68 --> 726.82]  And that's where I met Jared.
[727.14 --> 728.96]  So that'll eventually tie in somehow.
[728.96 --> 742.20]  And so like, it was during that intro to data science class where I sort of really understood what like data science and like, what could you actually do?
[742.20 --> 745.78]  Like during the time when I was doing my master's, it was.
[745.78 --> 754.52]  We talked a lot about like linear regression, logistic regression, survival analysis, and all of the epi concepts associated with that.
[755.04 --> 764.34]  But it never like I never knew what like random forest was, or like clustering, and all of that stuff until I took the data science class.
[764.34 --> 772.28]  And that's when it was sort of like, oh, if you can just think of something, something already exists to make that happen in some way, shape or form.
[772.50 --> 781.08]  So it was really eye opening in that sense, that like, whatever you can imagine, you can probably make it happen in some.
[781.32 --> 782.76]  So that was great.
[782.76 --> 787.24]  And then from my MPH, I entered my current PhD program.
[787.76 --> 798.64]  Fast forward, like till today, since I started, I am now doing my dissertation topic on data science education in the medical and biomedical sciences.
[798.64 --> 820.12]  So do you think that those I mean, it sounds like that those experiences of, you know, in high school, when you were introduced to computer science, and then when you're introduced and kind of your vision was expanded to see all these different methods and the possibilities later in your education, do you think that like, pushed you to this specific interest in data science education?
[820.12 --> 829.14]  Or like, what is it you feel about data science education that like, I know, there's a lot of gaps out there, and a lot to be addressed.
[829.14 --> 838.28]  But how did your specific interest in that develop? And what are you kind of hoping to learn and contribute through what you're doing now and in your current PhD work?
[838.92 --> 849.82]  Yeah, so I guess like, in terms of like pivotal moments in my life, it would definitely be taking that data science class during my master's program.
[850.12 --> 868.62]  And part of it was Jared was a inspiring teacher, Jared care and Rachel, they taught the class and it was a very actually, it was a very difficult class. But like, if you struggle through it, there was so much that you learned from it.
[868.62 --> 876.18]  And also during that class, it was the first time I attended a software carpentry workshop.
[877.30 --> 889.48]  And so those two things put together sort of put me on the road where I am now. So during that software carpentry workshop, so a little background about software carpentry, which is now the carpentries, they are a nonprofit organization,
[889.48 --> 897.26]  focused on teaching scientists, the computing skills that they sort of never were learned, never taught.
[897.48 --> 916.26]  And so I attended that first workshop, I sort of knew a little bit of Python from like, undergrad and high school years, and had been sort of like, playing around and bash and get because for some weird reason, I decided to install Linux on a computer where no one, no one that I work with, uses Linux.
[916.26 --> 929.82]  And so the stuff that they taught during that workshop were like all of those pieces, it was a little bit of Python, some bash and some git. And I thought to myself, like, hey, like, I can actually do this, like not that much of a jump from what I currently know.
[930.46 --> 940.80]  So that's how I got into the education area. So like the following semester, I signed up to be a carpentries instructor. This was back in like 2014 or so.
[940.80 --> 956.66]  And that's where I met Greg Wilson, who was the instructor trainer at the time. He currently works at our studio. But that's sort of where I picked up all of the fundamental parts of like, teaching this stuff.
[956.66 --> 977.56]  Didn't know that like, this would actually turn into like, a career or like a dissertation topic. But that's sort of when I realized, or started thinking about like, what makes a good teacher, thinking about students, like how to convey topics in some coherent way for people who are new to this.
[977.56 --> 995.14]  And I did that for enough times, or over a large enough period of time, that I eventually wrote it all down into a book called pandas for everyone. And so that is my attempt of teaching Python from a data science perspective. Yeah, using Python.
[995.14 --> 1025.12]  Yeah, that's awesome. So you mentioned Jared a couple times. It's Jared Lander. He is very involved in the R world. So if you're listening, and you're here in the part of the R community, you probably know that name already. But he's also involved in the R conferences that I mentioned, like the one that's coming up later this fall, the podcast is involved with as well. And he actually was a previous guest on the podcast as well, all the way back on episode number seven, which seems like another age ago.
[1025.14 --> 1054.92]  It does. And you know, I don't know if, as part of that data science class with him, Daniel, if this was part of it, but I remember him just talking this really great, sort of giving a really great overview of the landscape of like machine learning or AI techniques, and like where certain things fit in, and like how to kind of orient yourself in terms of how, for example, deep learning fits into like the spectrum of other techniques. So that was very, very useful.
[1055.14 --> 1083.38]  So I got a question for you, Dan. And it's something that really caught me when you said it a few minutes ago, you were, you were referring to that first data science class when you were taking your master's as a pivotal moment for you. I'm kind of wondering, we have other students out there listening, and they're kind of trying to figure out where they want to go. What was it about that class that you found inspiring? You talked a little bit about the fact that if you'd get through it, and when you could, you know, it would help you. But what was it that really grabbed you about that?
[1083.38 --> 1087.06]  What was it that you found beautiful about data science at that particular moment?
[1087.56 --> 1110.88]  Yeah, so there's two parts to it. One was the people and then the actual and then second was the actual data science material. And so this was a class. So the people that you're interacting with are probably going to be more important than anything else. And what I've also learned, this doesn't apply to actual Jared's case.
[1110.88 --> 1133.06]  But one of the things I learned over the years, like, what makes a good teacher doesn't necessarily mean you have to master the material, like being a good teacher is different from knowing the material. But it was sort of like, the way the whole entire class was taught, Jared taught the technical lab component, and he was also a carpentry's instructor or at the time.
[1133.06 --> 1149.94]  And so it was sort of that style of actually live coding in the class to go through the lab material that was really good as a student to see because one, like, it just slows you down. Instead of flipping through slide decks, it literally will just slow you down.
[1149.94 --> 1166.70]  And you see the typo error process and stuff like that, which is a lot to take in when you're a student seeing it all for the first time. But I want to believe that subconsciously, it does really help a lot just seeing the error process.
[1166.70 --> 1188.46]  And then Kair Patel and Rachel Shutt, they taught like the general data science landscape portion of it. And that's where I learned about like, how does this apply to like everything else? Like there's so many techniques and methods outside of what I was learning, in my epidemiology classes, that I just didn't know existed.
[1188.46 --> 1203.24]  And so just learning about those methods and just understanding or not really understanding at the time, but just seeing how they what they are, how they work, just understanding the heuristics of how they function under the hood.
[1203.24 --> 1222.78]  I saw so much, it was eye opening for me just to see how this could just be applied in the health space. Granted, I was doing a master's. So like, a lot of the stuff that we were learning in the data science class, you know, I believe that if I were to do a PhD in epidemiology, I would have seen some of that stuff eventually.
[1222.78 --> 1251.60]  But it was more just like, I was doing a master's, there was so much new information about a field already coming in. And then you just threw in this analytics component. And it was just like, whoa, we can just do this for everything. So it was sort of like that eye opening moment for me, where it was just the teachers were great. So it kept me motivated. And then the material itself, I just was able to make so many more connections to what I was currently learning. And so that sort of just kept pushing me forward.
[1252.78 --> 1282.76]  Thank you.
[1282.78 --> 1312.76]  Thank you.
[1312.78 --> 1336.56]  Yeah, so I was really interested to hear that you kind of as you were going through that data science class, you saw kind of a new world open to you in terms of how these techniques could be applied specifically, like in the medical space or in epidemiology, like like you were talking about.
[1336.56 --> 1364.88]  Do you feel like that those communities now are aware of those methodologies and like data science and AI is really like taking a foothold in those industries? Or do you still kind of see it as like maybe a bit of an uncomfortable mixing right now and people like still learning where things are being applied? What do you think is like the kind of current state of those things? And how do you see it progressing forward?
[1364.88 --> 1379.82]  So it's definitely been more adopted in the medical space, especially with like deep learning stuff being so good at image recognition, like that's a prime case for, you know, looking at medical imaging.
[1379.82 --> 1383.82]  But it's tricky for other parts of medicine.
[1383.82 --> 1394.60]  Because a lot of what we learned in epidemiology courses and biostats courses is trying to do inference on our like data.
[1394.60 --> 1403.68]  And so epi as a field is one way you can think about it is it is the field of setting up all of your observational experiments.
[1403.96 --> 1409.26]  So when you do the stats, you have you're a little bit more comfortable with like what is actually like a cause and effect.
[1409.26 --> 1422.64]  And so if you take that part in mind, it gets a little tricky because there's so many machine learning methods that are really just black boxes that really don't give you like any sort of inference, it's really just made for a prediction.
[1422.64 --> 1431.28]  And so you have to be careful using these methods in a medical context if they are like these black box methods.
[1431.28 --> 1438.20]  Because if it predicts something wrong, it becomes harder to figure out why did the model predict this wrong?
[1438.44 --> 1442.36]  And usually at the other end of this is someone's life on the line.
[1442.70 --> 1444.22]  Yeah, the consequences are high.
[1444.22 --> 1452.04]  Yeah, so yes, there is a place for all of the, you know, AI, ML stuff in medicine.
[1452.04 --> 1460.80]  And you just have to be more careful when you're trying to put a model into production, I guess, than like, you know, your regular company, I guess.
[1460.96 --> 1471.54]  That's the other way to put it is it's at the end of the day, like in health, like the end of that model is going to affect someone's life versus, you know, some bottom line, I guess.
[1472.08 --> 1472.22]  Right.
[1472.22 --> 1493.00]  And I imagine that that that kind of ties into some of your feelings about, you know, good, good code practices and like the carpentry stuff that you were talking about as well in terms of understanding, like the implications of the code you're writing and how, how to test it and how to deal with, you know, debugging models and all of those things.
[1493.72 --> 1499.96]  Yeah, so that the next part question or problem is like, not everyone was as fortunate as me.
[1499.96 --> 1509.32]  Like I went into a public health program or a medically related program and then got thrown into data science and then went down that track.
[1509.32 --> 1529.24]  So a lot of people who are actually practitioners or physicians on the medical end, when they want to do like research, they typically are just doing research from, you know, like Excel sheets, because that's what they know, or that's what they went through school with doing.
[1529.24 --> 1540.30]  They weren't taught like all of the techniques and methods and skills from like computer science or data science or just programming in general.
[1540.30 --> 1552.60]  And so, yeah, that's sort of where the carpentry stuff comes in, where, you know, now it's our time to teach all of the researchers, like the skills that they haven't like actually formally learned.
[1552.60 --> 1561.82]  And they just went through their life, you know, patching stuff together because, you know, programming was the means to get their work done.
[1562.18 --> 1568.66]  And it was just, you know, they just had to program something or do some kind of analysis just to get the result that they needed.
[1568.96 --> 1572.36]  They just struggled with a tool because they never really had formal training.
[1572.36 --> 1579.26]  And so that's eventually how I came to my dissertation topic, which was I've been teaching for so long.
[1579.64 --> 1582.12]  You know, I read like education books, like for fun.
[1582.50 --> 1585.88]  And I've always had this interest in the medical space.
[1585.88 --> 1590.94]  So find an advisor who will let me mash those two things together.
[1590.94 --> 1593.82]  And I got super lucky at tech.
[1594.36 --> 1596.26]  So my current advisor is Anne Brown.
[1596.84 --> 1601.80]  And yeah, I got super lucky just getting to meet her through the Virginia Tech Library.
[1601.80 --> 1605.16]  So if you are a student, definitely go befriend a librarian.
[1606.04 --> 1613.50]  And, you know, because if you think about what the people in the libraries do, like they've been doing data science, like since libraries were a thing.
[1614.02 --> 1615.14]  That's a great point right there.
[1615.66 --> 1621.46]  So one thing I'm curious about is you have a lot of experience in both Python and R.
[1621.94 --> 1627.70]  You know, on the Python side, you wrote Pandas for everyone to share that learning.
[1627.70 --> 1632.88]  On the R side, you know, you're giving a talk at the R conference focusing on government and public sector.
[1633.46 --> 1639.30]  And I'm wondering, you know, those are two different tools within the data science toolkit, if you will.
[1639.44 --> 1640.98]  And how do you see those?
[1641.02 --> 1652.98]  At what point do you turn to R and say that's, you know, the particular problem I'm trying to solve right now lends itself better to R in your view versus when would you turn to Python?
[1652.98 --> 1658.88]  How do you, since you have them both and often those two communities, you know, people kind of do an either or.
[1659.08 --> 1663.76]  But, you know, for the benefit of someone who might want to consider both, how do you see that?
[1663.88 --> 1665.92]  Where is each one stronger for you personally?
[1666.54 --> 1666.64]  Yeah.
[1666.80 --> 1672.54]  So currently, like today, the way I pick the language is like, who am I working with?
[1672.54 --> 1677.06]  So if I'm working with my advisor, I'm probably working in Python.
[1677.32 --> 1681.04]  If I'm working with someone else who does R, I'll probably use R.
[1681.22 --> 1681.76]  That's today.
[1682.20 --> 1694.52]  If you're currently an R user and you go through my book, there was a tweet like a couple weeks ago that was actually like, this book is great if you're an R user because like I make so many references to R things in the Python book.
[1694.52 --> 1698.26]  It's not super explicit, but it's one of those like, if you know, you know, kind of moments.
[1698.26 --> 1708.30]  And what's actually like interesting these days or now, like it really doesn't matter which language, if it's your first language, it doesn't matter.
[1708.88 --> 1711.64]  Eventually, like you're going to end up learning both.
[1711.82 --> 1716.20]  Just it's I almost feel like it's the nature of just doing data science.
[1716.36 --> 1717.52]  It's the nature of programming.
[1717.72 --> 1718.70]  It's the nature of programming.
[1719.04 --> 1720.68]  Lots of languages for different things.
[1720.80 --> 1721.02]  Yeah.
[1721.28 --> 1721.50]  Yeah.
[1721.50 --> 1729.40]  And so as far as the first language goes, it doesn't really matter if you're coming in from a data science point of view.
[1729.40 --> 1733.26]  Like I always make the distinctions between like data science and computer science.
[1733.26 --> 1741.46]  But if you're coming from a data science point of view, what's the most important thing is when you see a data set that is quote unquote messy.
[1741.46 --> 1748.34]  Can you like in your head write the general sequence of steps to make it clean again?
[1748.54 --> 1754.08]  And I borrow all the terminology from the R world, which is like the concept of tidy data.
[1754.84 --> 1763.16]  And so if you can see a data set and know the steps on making it tidy, then at that point, it really doesn't matter what language you use.
[1763.16 --> 1768.42]  Because you can literally just look up like in the R world now in tidy verse, it's like pivot longer or wider.
[1768.56 --> 1771.58]  So you would just Google like pivot longer, wider tidy R.
[1772.14 --> 1775.62]  And then on the Python side, it will be like pivot longer, wider like Python.
[1775.92 --> 1777.66]  But in Python is melt and pivot.
[1777.86 --> 1781.44]  So one of those words will show up like some search result.
[1781.44 --> 1794.30]  And I think that's probably the more important thing is just like knowing the steps on processing data versus and then just treating programming as like the thing to get you there.
[1794.80 --> 1802.58]  Because if you struggle, if you're just starting off, you don't know the steps, you don't know like the terminology or how to clean data.
[1802.58 --> 1804.70]  And then you're also trying to learn a brand new language.
[1805.02 --> 1813.66]  So when something goes wrong, you don't know if it's like your, the sequence, like the overall sequence was wrong or was it like an actual like programming type of mistake?
[1814.30 --> 1819.56]  And that's, that's what you want to like separate as much as possible.
[1819.56 --> 1822.76]  So like just pick one, learn how to manipulate data.
[1822.76 --> 1827.38]  And once you're comfortable with that, it becomes super easy to transition to another language.
[1827.38 --> 1833.18]  Like when I did my data science course in my master's program, it was actually all done in R.
[1833.80 --> 1837.84]  It was actually all done pre-Tidyverse was like formalized as a thing.
[1838.42 --> 1844.20]  But I worked with processing data for like a good year or two.
[1844.82 --> 1849.96]  And then that's when I like sort of when I like actually understood what like tidying data meant.
[1850.46 --> 1853.24]  That transition into Python was super easy.
[1853.24 --> 1863.52]  And then that's sort of why like the ordering of the book that I put together or like there was a lot of stuff in the book that was sort of like this is I learned all this from my transition to R.
[1863.68 --> 1867.20]  And so that's why there's so many like random R things in the Python book.
[1867.66 --> 1868.46]  Yeah, that's awesome.
[1868.46 --> 1877.74]  And I, it sounds like we were talking a little bit before the show about kind of your, your personal data processing pipeline.
[1877.74 --> 1897.18]  Like when, when any of us kind of go into a project, somehow we have to set up a set of, you know, scripts, programs, folders, files, config, you know, data sources, whatever that is to, to define our project and the structure of like the pipeline that we're using.
[1897.18 --> 1900.82]  It sounded like that's something that you think about quite a bit.
[1901.04 --> 1907.98]  What, what is your, as you're kind of now also thinking about data science education a lot.
[1907.98 --> 1915.64]  What are your thoughts as far as when you're talking to students, when you're thinking about how to educate them around your project structure?
[1915.84 --> 1929.18]  What are some of the main things that, you know, really can benefit you as you set up a project, a new project, whether that be just something that's analytics or whether that be a machine learning project?
[1929.40 --> 1932.76]  What are some ways that you can help yourself down the line when you start out a project?
[1932.76 --> 1935.62]  Yeah, so I am in academia.
[1936.02 --> 1941.66]  So there's three papers that like sort of talk through this entire process.
[1941.94 --> 1947.78]  The first one that I read that sort of introduced me to all of this is by William Noble.
[1948.12 --> 1952.48]  And the title is called A Quick Guide to Organizing Computational Biology Projects.
[1952.48 --> 1962.84]  And that was probably the first time I've seen in academic writing, literally, how do you set up the folders in a project?
[1962.84 --> 1967.20]  So you have like an output or an output folder.
[1967.52 --> 1969.38]  You have like a scripts folder.
[1969.56 --> 1970.58]  You have a docs folder.
[1971.18 --> 1973.42]  You have a readme file in the top level.
[1974.90 --> 1976.00]  Stuff like that.
[1976.42 --> 1984.82]  And then the two other papers that sort of like expand on this from the Carpentries folks is there's a paper called Best Practices for Scientific Computing.
[1984.82 --> 1986.86]  That was written in 2014.
[1986.86 --> 1992.98]  And then in 2017, there was another one that said good enough practices for scientific computing.
[1993.16 --> 1997.78]  So you can see how like doing good or best practices is actually pretty difficult.
[1997.78 --> 2010.30]  But it really all does stem from one of the core pieces is really having a folder structure so that your scripts can find the data that you're working with.
[2010.30 --> 2028.96]  And it's focused around the idea of, yes, it works on my machine, but it needs to work on someone else's machine or another one of your machines or the cloud as well without having to, you know, change a whole bunch of like file paths.
[2028.96 --> 2039.96]  In an ideal world, it runs on your computer with like a command and it will run on another computer with the same exact command without you having to change anything.
[2040.30 --> 2047.76]  So that's sort of the overall like overview of what I focus a lot on.
[2047.94 --> 2054.30]  And then there's, you know, then there's like the super technical parts of like, yes, Git is a thing.
[2054.48 --> 2058.44]  Version control is a thing that you have to know when you're trying to collaborate.
[2058.72 --> 2060.76]  That's just sort of the nature of the beast.
[2061.08 --> 2064.18]  The good thing is the Carpentries has a Git lesson.
[2064.34 --> 2068.00]  So if you want to learn it on your own, it is written down somewhere.
[2068.00 --> 2084.60]  And I've, this past summer, put together a few workshops that are on the Carpentries like YouTube page on like the actual super like complicated collaboration aspects of using Git and GitHub.
[2085.34 --> 2096.54]  But yeah, so most of my stuff really does focus around, you know, project organization is the actual like cornerstone or centerpiece to managing like a project.
[2096.54 --> 2098.24]  Yeah, it's interesting.
[2098.56 --> 2103.48]  Like you talked about the one paper being like best practices and then they went to like good enough practices.
[2103.88 --> 2106.26]  That concept definitely resonates with me.
[2106.76 --> 2118.08]  I was wondering, because there is like software engineering sort of best practices in industry where like I think now, like if you're working on a project, you have a GitHub repo.
[2118.08 --> 2130.40]  So if it's not connected to some sort of CICD and you don't have some sort of portable way of deploying this thing, maybe with Docker or something like that, that's kind of like what people are doing a lot.
[2130.82 --> 2138.56]  But that's like a that's a lot of things for a like someone in academia or like a new data scientist to learn.
[2138.56 --> 2140.56]  It can be rather burdensome.
[2141.64 --> 2144.48]  So like, yeah, I guess daunting.
[2144.62 --> 2145.66]  Yeah, daunting is a good word.
[2145.66 --> 2155.48]  So like in terms of like people that are starting out as data scientists, do you think that's something like as they're embedded in an organization?
[2155.48 --> 2168.98]  Should should should they sort of strive for, you know, eventually kind of learning all of those software engineering best practices and like adding that to their workflow?
[2168.98 --> 2176.96]  Or do you think there is a sort of in between where, you know, the workflow of a data scientist is it is different, right?
[2176.98 --> 2179.34]  There's different data concerns and all of those things.
[2179.34 --> 2188.08]  So how much of a software engineer does a data scientist have to be, I guess, is that in in question that I'm that I'm going for?
[2188.96 --> 2189.08]  Yeah.
[2189.20 --> 2199.62]  So that's the other big dilemma is a lot of workflows from data science are actually like anti patterns from software engineering.
[2199.80 --> 2200.30]  Right.
[2200.82 --> 2206.64]  As a data scientist, we primarily work in like scripts that execute from top to bottom.
[2206.64 --> 2215.80]  Very rarely do we end up writing classes or things like like using those software engineering tools in a data science analysis.
[2216.22 --> 2217.54]  We will write functions.
[2217.68 --> 2218.08]  That's good.
[2218.32 --> 2227.24]  But we don't necessarily create packages like that is considered like maybe a best practice, but it's it's a lot more stuff.
[2227.66 --> 2229.60]  So like just writing a function is good enough.
[2229.60 --> 2238.20]  But then what happens when you have 50 functions like, yeah, there's this like tension between well, not tension, but there there is like the way you program things.
[2238.32 --> 2242.64]  And from a data science perspective is going to be different from software engineering.
[2242.64 --> 2244.16]  That's just going to happen.
[2245.22 --> 2252.52]  It's kind of interesting when you hear stories about data scientists working with the engineers and then like when their code bases need to mesh.
[2252.52 --> 2256.26]  And that becomes a different question and problem on its own.
[2256.48 --> 2266.66]  But from at least from what I'm working on now, which is the data science perspective, but it's like catered towards the biomedical sciences and those people.
[2266.66 --> 2286.48]  We even need to go like an even step further back from that from like we're thinking about best practices and that stuff, because these are the people who are so new to this field that if you talk about like Docker and CICD integrations, like those are like letters that they've never seen put together before in that order.
[2286.48 --> 2300.26]  And so so one of the I guess byproducts of my dissertation is this I guess you can call it a book slash lesson plan that's called DS for Biomed.
[2300.42 --> 2302.24]  So data science for the biomedical sciences.
[2303.06 --> 2313.14]  Literally, the first thing I talk about is like we're just going to talk about spreadsheets for now, like because it is probably something that they're most familiar with in terms of a data perspective.
[2313.14 --> 2316.18]  Spreadsheets are one way you can think about spreadsheets.
[2316.34 --> 2318.10]  It is a GUI for your data set.
[2318.64 --> 2322.00]  And so people like looking at things and being able to click on things.
[2322.62 --> 2331.98]  And so how do we go from spreadsheets to data science pipeline is sort of where I'm focusing more of my time these days.
[2332.74 --> 2339.26]  And so, yeah, like I just finished like the first like spreadsheet module so I can actually talk about this.
[2339.26 --> 2359.68]  And putting that part together, I sort of realized that like, yes, we can actually introduce like those tidy data concepts like in the spreadsheet section, which is like, you know, if you've ever loaded up like an Excel sheet, like first of all, when I'm as a data scientist, when I see an Excel sheet, I'm already preparing myself over like if I get a CSV file.
[2359.68 --> 2364.36]  And so like, why do I like, you know, cringe when I see an Excel file?
[2364.48 --> 2369.62]  Well, it's because like, you know, sometimes, you know, we have multiple tables like in the same sheet.
[2369.82 --> 2372.48]  And it's like from A to M is like one table.
[2372.48 --> 2375.32]  And from like P to Z is like another table.
[2375.48 --> 2377.26]  And you have to load those tables separately.
[2377.26 --> 2383.48]  Like those are like data issues that happen when you're loading in data into R or Python or whatever language.
[2383.48 --> 2387.82]  But from a lot of people who don't actually work with programming languages, that's great.
[2387.90 --> 2389.22]  They get to see everything at the same time.
[2389.32 --> 2397.32]  So it's sort of like identifying those bad habits and trying to show them why they're not conducive.
[2397.32 --> 2405.38]  If you want to load them into a programming language is sort of like that's where I'm at right now.
[2405.38 --> 2414.56]  And so it all also comes down to the whole mantra of you want to have empathy for the people who are learning this stuff.
[2414.90 --> 2422.52]  And, you know, if all they get away from like that first workshop is like structuring their spreadsheets better, I'll be okay with that.
[2422.64 --> 2423.50]  I'll be happy with that.
[2423.54 --> 2428.50]  So it's always about making like these small incremental improvements every time you start a new project.
[2428.50 --> 2433.04]  And that happens if you're like a full-blown data scientist as well.
[2433.04 --> 2443.64]  Like, yeah, maybe you have the whole project structure thing working for you and you can have your computer, you know, all your code work on whatever machine that your code base is deployed on.
[2443.90 --> 2452.76]  What would be the next step for you that might be trying to learn like one of the continuous integration services or like using Docker or something.
[2453.02 --> 2456.54]  So there's always something that you can do to improve like your workflow.
[2456.54 --> 2466.66]  And I guess like that that does take a lot of effort on like one's end because you do have to do a lot of like introspection of like what can be improved.
[2466.66 --> 2476.34]  And like I guess like the way I've always seen it for me, it was easier for me to do it because it's always like, oh, what is the best practice?
[2476.34 --> 2478.90]  And then I read about it and it's like that is way too complicated.
[2478.90 --> 2486.20]  And then like six months later, it's like that seems doable now because I've like learned all the other stuff in the middle that's like that gets me there.
[2486.34 --> 2491.36]  So there's different entry points towards like picking up practices from software engineering.
[2491.80 --> 2498.18]  But at the end of the day, like data science pipelines or workflows really don't mesh with software engineering stuff.
[2498.18 --> 2505.82]  Like in software engineering, your end product is probably like a library or like this big program thing versus like in data science.
[2505.82 --> 2509.20]  It's really like this pipeline of scripts that like create this model.
[2509.20 --> 2512.98]  And then this model gets handed off to like the software engineers to implement somewhere else.
[2513.32 --> 2516.24]  So like those things are just going to be different.
[2516.24 --> 2519.92]  And it makes sense that the best practices on both sides aren't going to be the same.
[2519.92 --> 2525.04]  But, you know, if you make incremental progress, you know, you'll eventually get to a good spot.
[2528.18 --> 2553.98]  So you're really thinking a lot about trying to get people working in these areas, bioinformatics and other related areas to think about using data science techniques.
[2553.98 --> 2576.46]  If you were to look into the future and let's say that you've accomplished your goals of getting these people to use these sorts of techniques in their workflows, what are some of the example things that you envision them being able to do with data science techniques that maybe they wouldn't have been able to do if they kind of followed the same workflows that they have been using for quite some time?
[2576.46 --> 2586.02]  So one of the main takeaways would be just working with multiple sources of data at the same time.
[2586.02 --> 2595.26]  We have a system where, you know, every local department, organization, government at the government level, etc.
[2595.58 --> 2602.84]  They're doing reports of case counts, for example, on a daily basis.
[2603.14 --> 2607.52]  And they don't necessarily all come in as like one.
[2607.74 --> 2610.24]  They're not all combined together for you.
[2610.24 --> 2615.22]  In this current pandemic, yes, you can find data sources that are doing the aggregation for you.
[2615.44 --> 2619.98]  Back in 2014, during the Ebola outbreak, that wasn't necessarily the case.
[2620.40 --> 2626.30]  We were getting daily reports from different countries as like PDF files, for example.
[2626.30 --> 2636.16]  And so being able to work with multiple data sources is going to be one of those like skills that are going to be super important.
[2636.16 --> 2641.70]  And how it all ties back into like why use a data science approach.
[2641.80 --> 2658.14]  And when I say that, like why use a programming language to do that kind of analysis over something like spreadsheets is that goes into like one of the most important things when you're working with data is like you always want to keep your raw data completely intact.
[2658.14 --> 2671.32]  And so this way, if there is an improvement or something in your actual data science code, in an ideal world, you just rerun your code over a new set of data and then you get your updated results right away.
[2671.32 --> 2679.46]  That's probably the most important idea that we have, even in like today's COVID world.
[2679.76 --> 2692.52]  That's sort of the reason why like you'll hear like recommendations changing over the past couple of months is because in the beginning we weren't, the data itself didn't show a conclusion.
[2692.52 --> 2700.70]  But as more data came in, if you were to rerun your analysis over and over again, over new courses of data, you might actually find a new outcome.
[2700.70 --> 2706.00]  And so like currently we are in real time living the scientific process.
[2706.60 --> 2714.48]  And part of that process is, you know, making sure that if you do have new data sources coming in, you can still rerun your analysis.
[2715.08 --> 2717.96]  And, you know, that part is reproducible.
[2718.48 --> 2722.64]  And then, you know, as more data comes in, your conclusions may change.
[2722.78 --> 2725.98]  So that's sort of how that all ties into current times.
[2725.98 --> 2731.56]  But it really is something that is like really just fundamental to data science as a whole.
[2731.82 --> 2742.28]  Since, you know, we're always querying data from the world and we want our pipeline to be there so that like as new data comes in, we can have an updated model at the other end.
[2742.28 --> 2744.10]  That makes perfect sense.
[2744.44 --> 2749.86]  So, you know, we talked a little bit a while ago about the fact that you're doing a talk at the R conference.
[2750.06 --> 2759.90]  And I was wondering if you could share a little bit about, you know, what you're talking about and what is your message to the R community and give us a little insight into that.
[2760.04 --> 2761.78]  We'd love to hear what's of interest to you.
[2761.78 --> 2772.86]  So my previous R conference talks have always been around the topic about like this data pipelining part of data science.
[2773.06 --> 2784.40]  So like, you know, I think the last talk I gave last year was, you know, something around like, I'm going to teach you how to make a make file so you can like make your reports.
[2784.84 --> 2785.24]  Super useful.
[2785.38 --> 2786.20]  Yeah, it is.
[2786.20 --> 2801.28]  So last year, so 2019, I was one of the interns at RStudio and I worked on a package called grade this, which is the auto grader system for R code.
[2801.66 --> 2806.18]  So it can, yes, tell you if like you're an instructor, like here's the correct answer.
[2806.18 --> 2810.32]  And then the student can type in some R code and compare the results.
[2810.32 --> 2812.22]  That's like the easier way you can grade code.
[2812.22 --> 2817.66]  The more complicated way you can grade code is like looking at the code itself.
[2818.56 --> 2822.60]  So like in more technical terms, it's looking at the abstract syntax tree.
[2823.18 --> 2829.46]  And so you're literally comparing like if the student put in, for example, log of three and your solution is log of two.
[2829.80 --> 2836.42]  You want a sentence that essentially says you put in three where the answer should have been two.
[2836.42 --> 2842.40]  So creating that sentence is a lot more complicated than it may or may not seem if you didn't think it was a hard problem.
[2842.90 --> 2851.16]  So during that process, I learned a lot about R's way of handling code expressions.
[2851.16 --> 2857.54]  And so this year I am trying to teach that to regular people.
[2857.54 --> 2875.46]  How that ties into the greater R ecosystem is if you've worked with tidyverse packages, you'll notice that you are allowed to pass in like column names without having them like quoted in strings.
[2875.46 --> 2887.02]  But they look like regular variable names, which is terrifying from like a Python user's perspective because lazy eval is not a thing in the Python world, but it's like there in the R world.
[2887.68 --> 2894.42]  So it's sort of trying to introduce those topics is sort of my goal for like the next series of talks.
[2894.90 --> 2895.84]  Why does this help?
[2895.84 --> 2908.40]  This is sort of the transition of if you want to write your own tidyverse compatible packages for your own work, this is sort of like what you need to know to make that happen.
[2908.40 --> 2920.02]  So, yes, the talk is more towards like the software engineering side of things, but it's one of those like, hey, if you want to have your own work plug into this whole ecosystem, like how would you go about doing it?
[2920.02 --> 2926.88]  And so this is my part of trying to make an incremental improvement for myself and like for the greater community.
[2926.88 --> 2940.98]  Do you think as you dug into like the underlying mechanics of how like R processes expressions, do you think that's influenced how you write your R in terms of like just your general programming?
[2940.98 --> 2950.40]  And like, has it made you more sympathetic in terms of like how you how you write your R with that kind of better underlying understanding?
[2951.52 --> 2963.18]  So as far as like, like regular day to day, like if you were to just tell me to run some type of analysis on a data set now, it doesn't affect that part of it.
[2963.18 --> 2969.12]  If anything, I have a lot more sympathy for the people who develop these packages.
[2969.52 --> 2978.52]  Like last year, I literally read the advanced art book like three times over and over again without understanding like what I was doing during my internship.
[2978.52 --> 2986.84]  And then like after seeing it and having it like mesh in my brain for like a year, like I'm reading it like again, rereading it again.
[2986.84 --> 2988.40]  And it like makes total sense now.
[2988.40 --> 2993.16]  So as far as like a day to day thing, it doesn't affect it that much.
[2993.36 --> 3012.16]  But when I am writing functions, and things that might need to end up like a collection of functions, if I start writing a collection of functions, whether they make it into a package or not, I am more mindful of certain things, mainly around like dependencies is what I'm really mindful about.
[3012.16 --> 3029.32]  One of the things that sort of surprised me last year was, you know, if I wanted to, you know, do like some kind of grep search for string, you know, in tidy first world, I would just instinctively like you something from like the string R package or something like that.
[3029.32 --> 3040.70]  But you don't need the entire string R dependency, which, if all you're doing is like a simple grep call, just use like the regular built in grep L, it's like fine.
[3040.88 --> 3049.20]  Like, I sort of realized that like, yes, there's like, when you are a package developer, all of the engineering like hurdles are now like your problem.
[3049.20 --> 3051.94]  Like your job is to make like the end users life easy.
[3052.46 --> 3055.30]  And then you deal with all of the engineering burden on your end.
[3055.66 --> 3058.26]  And so I definitely appreciate that a lot more.
[3058.66 --> 3068.68]  But like, as far as like my day to day, it's mainly just like, you know, just write more functions and like try to keep working on like the best practices and stuff like that.
[3068.74 --> 3075.96]  And then when I have a new student that I'm working with, that sort of like, grounds me back, like, okay, this is where I once was.
[3075.96 --> 3082.74]  And then so how do I get them to like some other point, the next like level in their life and programming?
[3083.10 --> 3087.54]  Like, how do I make that transition like, less violent for them?
[3088.94 --> 3094.34]  Yeah, no, I, I really appreciate what what you just said, actually, about dependencies.
[3094.80 --> 3104.86]  Like you can reduce, I don't know what the right word is, I guess your liability or your, your potential debugging issues in the future.
[3104.86 --> 3110.58]  If you only need for like, I've, I've done this sometimes where it's like, oh, I need to like a sigmoid function or something.
[3110.70 --> 3120.48]  Like, well, I could like, import any number of packages where I could call like, sigmoid parentheses, like, give my thing.
[3120.60 --> 3126.00]  But I could also just write that in a couple lines of code and just embed the function in my own code.
[3126.00 --> 3128.40]  So that, like, it's super clear what's going on.
[3128.46 --> 3129.96]  I don't have an external dependency.
[3129.96 --> 3135.46]  I think that's something that like is underrated a lot.
[3135.62 --> 3139.10]  So I really appreciate you bringing that point to the surface.
[3139.24 --> 3145.76]  And I'm super interested to hear like the other insights you have from your talk at the R conference.
[3145.76 --> 3147.62]  We'll definitely look forward to that.
[3147.90 --> 3157.00]  And we'll also link in our show notes to a bunch of the things you've mentioned, the carpentry courses, your book, the various packages you've mentioned, and all of that.
[3157.00 --> 3161.82]  We'll also link to Jared Lander's episode if people want to go back and listen to that.
[3162.38 --> 3164.28]  But yeah, we really appreciate you joining us.
[3164.36 --> 3172.86]  I think if I'm right, that people can find out more about the R conference at rstats.ai is the correct website.
[3173.62 --> 3175.74]  And we'll, of course, link to that as well.
[3176.36 --> 3179.60]  But yeah, it's been a huge pleasure to get to chat with you, Daniel.
[3179.78 --> 3184.04]  Looking forward to spending some more time together at the conference.
[3184.62 --> 3185.48]  Yeah, thanks for having me.
[3185.54 --> 3186.28]  It's been really fun.
[3186.28 --> 3196.72]  The R conference is where our enthusiasts and data scientists gather to explore, share, and inspire ideas.
[3196.72 --> 3199.94]  It's happening December 2nd through 4th.
[3200.04 --> 3201.68]  And we have a discount code for you.
[3201.84 --> 3205.24]  If you're interested, use code practicalai20.
[3205.46 --> 3210.04]  That's good for 20% off every ticket type, including the conference and all workshops.
[3210.46 --> 3214.00]  This episode was hosted by Daniel Whitenack with Chris Benson.
[3214.00 --> 3215.84]  Our special guest, Daniel Chen.
[3215.96 --> 3216.98]  Thanks for coming on the show, Daniel.
[3217.44 --> 3221.06]  Our music is produced by the one and only Breakmaster Cylinder.
[3221.28 --> 3223.24]  And we are brought to you by amazing sponsors.
[3223.86 --> 3227.10]  Thanks again to Fastly, Linode, and Rolbar for their continued support.
[3227.58 --> 3228.24]  That's all for now.
[3228.68 --> 3229.76]  We'll talk to you again next week.
[3229.76 --> 3231.18]  See you then.
[3231.18 --> 3231.70]  Bye-bye.
[3231.70 --> 3231.84]  Bye.
[3231.84 --> 3232.38]  Bye.
[3232.58 --> 3233.22]  Bye.
[3233.22 --> 3233.76]  Bye-bye.
[3233.96 --> 3234.48]  Bye.
[3234.66 --> 3235.24]  Bye.
[3235.92 --> 3237.32]  Bye-bye.
[3237.32 --> 3238.00]  Bye-bye.
[3241.90 --> 3248.40]  Bye-bye.
