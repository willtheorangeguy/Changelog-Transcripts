[0.00 → 5.46] Hey, what's up everyone? Adam Stachowiak here, editor-in-chief of Changelog. We're doing something a little different today.
[5.70 → 8.04] I want to introduce you to a podcast called Command Line Heroes.
[8.54 → 12.20] It's an original podcast from our friends at Red Hat, hosted by Serrano Bark.
[12.58 → 17.44] It's about the people who transform technology from the command line up. It's an awesome show. I'm a subscriber.
[17.94 → 23.52] So when our friends at Red Hat mentioned they were looking for unique ways to promote Season 3, which launched last week,
[23.76 → 28.74] I said, hey, let us rebroadcast Episode 1 in our podcast feed. And needless to say, they love the idea.
[28.74 → 33.18] We're just huge fans of Serrano and the team behind this podcast, and we wanted to share it with you.
[33.50 → 38.82] So learn more and subscribe at redhat.com slash command line heroes, or check the channels for a link.
[44.52 → 52.14] On the morning of July 12th, 2018, members of the Python community all around the globe woke up,
[52.66 → 55.72] grabbed a cup of coffee, and popped open their laptops.
[55.72 → 61.98] Then, one by one, they discovered a message from their benevolent dictator.
[63.08 → 68.68] Guido Van Possum, the man who invented Python, one of the world's greatest programming languages,
[69.38 → 73.42] maybe the greatest programming language, had written to them all.
[73.90 → 77.58] So imagine all those Python fans reading these words.
[77.58 → 81.32] I don't ever want to have to fight so hard and find that so many people despise my decisions.
[81.56 → 83.74] I would like to remove myself entirely from their decision process.
[83.90 → 87.72] I'm giving myself a permanent vacation from being benevolent dictator for life.
[89.20 → 91.04] And you will all be on your own.
[91.48 → 93.96] I am not going to appoint a successor.
[94.52 → 97.28] So what are you going to do? Create a democracy? Anarchy?
[97.28 → 107.22] With that simple but earth-shattering note, Guido Van Possum, the man that the Python community had been following for decades,
[108.00 → 109.88] well, he basically just bowed out.
[110.42 → 116.94] His message was titled, Transfer of Power, and it would change the landscape of the Python language forever.
[116.94 → 126.60] But more than that, it called into question how all our programming languages were going to evolve and thrive in the future.
[127.12 → 132.54] Were languages supposed to be run by one benevolent dictator, giving them shape and coherence?
[132.98 → 137.82] Or, in our open-source world, were languages actually more like spoken languages,
[138.36 → 143.08] things that grow and react according to the behaviour of a bunch of different speakers?
[143.08 → 150.66] The Python community, the fastest-growing community of any language out there, was about to find out.
[154.68 → 162.10] I'm Saran Titlark, and this is Season 3 of Command Line Heroes, an original podcast from Red Hat.
[163.88 → 168.98] Last season on Command Line Heroes, we explored a huge stretch of territory,
[169.38 → 172.84] from gaming, to the art of the fail, to serverless development.
[173.08 → 178.50] We even ended up tracking one of NASA's rovers across the surface of Mars.
[179.12 → 183.34] But there was one episode that seemed to really capture everyone's imagination.
[184.00 → 185.62] The story of Grace Hopper.
[186.24 → 191.16] Her work on compilers led to the first high-level programming language, COBOL.
[192.02 → 198.42] We realized afterward that Grace Hopper's story was just one of so many stories of languages
[198.42 → 201.10] shaping the world of development and ops.
[201.10 → 205.56] New programming languages allow us to bridge humans and machines.
[206.14 → 209.14] They open gateways toward amazing new possibilities.
[210.10 → 213.76] So, Season 3 is all about those languages.
[214.40 → 215.30] We're talking JavaScript.
[215.66 → 216.46] We're talking BASIC.
[216.86 → 217.78] GO, Perl.
[217.90 → 219.50] And yes, we're talking Python.
[220.24 → 222.20] Python is where our journey begins.
[222.20 → 229.90] Because by following the tale of Python, we learn a crucial truth about the future of all our programming languages.
[234.16 → 242.40] So, after Python's benevolent dictator abandoned his throne, the Python community was, yeah, a bit lost.
[243.10 → 246.28] How do you organize things after a dictator steps down?
[246.28 → 251.24] Somebody suggested they can model their structure after the Presbyterian church.
[251.88 → 253.12] That idea didn't stick.
[253.94 → 259.20] To understand how Python did reorganize and what it means for the future of languages in general,
[259.52 → 263.22] we have to go back to the origin of the Python tale.
[263.22 → 269.34] Well, I'm writing all this code in C, and it's getting kind of tedious.
[269.90 → 274.42] That's the man himself, Guido van Possum, Python's benevolent dictator.
[275.18 → 280.60] Van Possum had worked for years at Amsterdam's famous Centrum Vicente and Informatics,
[280.94 → 284.32] where he helped develop the ABC programming language.
[284.88 → 291.34] Here, he's describing the moment he was working in C and saw a need for a brand-new language.
[291.34 → 297.58] It still felt like there were lots of bugs and sort of it just was slow-going.
[297.98 → 302.68] And I was thinking, hmm, if we had an ABC implementation here,
[302.78 → 306.04] I would just write that whole login program in 15 minutes
[306.04 → 310.46] and then I would move on to the account management program or something
[310.46 → 312.88] and see it takes me a week each.
[312.88 → 324.28] I somehow started thinking about coming up with a way to use some of ABC's features in the Amoeba environment.
[325.64 → 329.70] Here's something we discovered in studying the history of programming languages.
[330.28 → 331.94] There's no such thing as brand new.
[332.52 → 337.04] They all borrow from old languages in order to cobble together solutions.
[337.96 → 340.28] Languages morph, they evolve, they branch.
[340.28 → 344.00] When Van Possum was getting frustrated with the possibilities out there,
[344.24 → 349.24] he imagined a language that could bridge the gap between C and shell programming.
[350.16 → 354.56] C was often overkilled, but at the same time, shell scripts felt too cumbersome.
[355.28 → 360.02] There was a sweet spot between the two, and that was the spot that Python filled.
[360.70 → 363.58] When Van Possum first released Python in 1991,
[364.22 → 367.22] it was a revelation for sysadmins especially.
[367.22 → 372.78] Here was a full-featured scripting language, unlike anything that had come before.
[374.10 → 377.64] The first time that I used Python, I absolutely fell in love with it.
[377.90 → 383.20] That's Emily Morehouse, one of five women currently working as a core developer on Python.
[383.56 → 388.82] I think seeing such a stark difference between a first language like C++
[388.82 → 395.02] and then moving into something like Python, you are really able to see the elegance of the language
[395.02 → 397.06] and the language design itself.
[397.58 → 403.76] You're not necessarily having to deal with any of the hairy implementation details of memory management.
[404.58 → 409.78] And it was such a great way to build things so much faster
[409.78 → 415.62] and build things for a much wider variety of applications.
[417.02 → 420.80] Key to Python's attractiveness was its extensibility.
[421.44 → 425.12] A language like ABC, for example, is monolithic in design.
[425.68 → 429.88] There's no way for a real community to help define how the language will work.
[429.88 → 435.58] By contrast, Van Possum wanted Python to be open and extensible from the beginning.
[435.58 → 445.46] When approaching software design, you often will have to take either existing software or other software systems
[445.46 → 447.80] and kind of get them all to work together.
[448.38 → 456.64] And one of the very true values of how you can design software is making sure that it's extensible.
[457.02 → 462.68] It sounds like a no-brainer, but not every language has achieved the level of extensibility
[462.68 → 465.00] that Python had right from the start.
[465.58 → 469.70] And the truth is, if a language doesn't have extensibility baked into it,
[469.98 → 474.44] there's a good chance it'll end up collapsing under its own weight as it grows.
[475.52 → 479.44] Python has been designed in a very interesting way
[479.44 → 484.30] that allows it to be kind of extensible at its core.
[485.04 → 490.30] You can actually, like, patch different pieces of the system at runtime.
[490.30 → 497.48] So if you want to switch out how modules are imported, or you want to switch out your string type or your integer types,
[498.54 → 501.88] Python allows you to do all of these things fairly easily.
[502.58 → 510.50] At the heart of Python's extensibility is something called C extensions or C modules.
[510.50 → 518.30] And so Python has actually been designed to give you an entry point to other languages.
[519.02 → 527.28] And essentially, if you can, you can write a C extension or a C module that can then bridge to,
[527.48 → 528.94] I mean, hundreds of other languages.
[528.94 → 532.86] You can kind of hack Python.
[533.34 → 533.78] Python.
[533.78 → 539.20] It's all about the user's ability to adapt a language to their own means.
[539.90 → 542.54] So Python, as Guido Van Possum envisioned it,
[542.86 → 546.06] was never going to be limited to one dictator's vision.
[546.82 → 550.32] His transfer of power memo was a long time coming.
[551.18 → 554.06] Van Possum understood the power of community influence,
[554.50 → 557.24] the power of bringing everyone under a big tent.
[557.78 → 562.16] Yes, he ended up getting called a dictator, but it was a benevolent dictator.
[562.16 → 570.08] I think one of the reasons why Python has become such a diverse community is because of Guido.
[570.52 → 579.62] Python has female core developers now because Guido wanted that change to be made and made it happen himself.
[580.80 → 586.64] Naomi Seder, the chair of the Python Software Foundation, once gave a keynote where she said,
[587.02 → 590.06] Python, come for the language and stay for the community.
[590.06 → 594.22] And that may be Guido Van Possum's greatest legacy.
[594.92 → 598.42] Not just Python, but the Python community he made room for.
[599.00 → 605.26] He made Python seriously extensible, but it was, in a way, socially extensible too.
[605.80 → 608.14] It always had room for human additions.
[608.14 → 621.08] You have so many different applications of Python that your community is then, by definition and kind of by construct, very diverse.
[621.72 → 627.50] And so it's really, really broadened the community reach.
[627.50 → 634.94] Emily Morehouse is a core Python developer and director of engineering at Cuddle soft.
[637.88 → 642.46] Once Python hatched, it started to grow like nothing before.
[643.00 → 647.98] I'm looking at a stack overflow chart that shows the amount of chatter they get on each language.
[648.36 → 650.42] And Python's line is rocketing.
[650.42 → 655.98] In 2018, more people did Google searches for Python than for Kim Kardashian.
[656.78 → 663.96] All that excitement has it jostling for the title of most used language against options like Java, C, and C++.
[665.12 → 667.34] So what's with all that love anyway?
[668.04 → 673.74] To find out, I caught up with developer Michael Kennedy, who lives at the centre of the Python zeitgeist.
[674.24 → 678.46] Michael hosts not one, but two podcasts devoted to Python.
[678.46 → 681.54] Talk Python to me and Python Bytes.
[682.10 → 684.28] We'll throw some links in the show notes so you can check them out.
[685.48 → 689.24] Michael and I got chatting about how Python really hit its stride.
[690.18 → 699.36] If you look at the analytics and the surveys and stuff like that, it really seems to be that 2012 is a strong inflection point.
[699.36 → 711.20] And the most significant thing that happened around 2012 is the data science community switched away from things like R and some other stuff to really focus on Python.
[711.66 → 716.20] And ever since that's happened, there's been even more momentum there, more machine learning libraries.
[716.20 → 721.40] A lot of the popular machine learning libraries, for example, are Python first, and then they'll consider other languages.
[721.84 → 726.80] Yeah, that's kind of been my understanding, too, is when I think about Python, I know it can be used for web development.
[726.94 → 729.96] I know a lot of people who still use it to build web apps.
[730.08 → 734.88] But I feel like the heart of it nowadays is more in the data science part of things.
[735.00 → 737.04] What do you think led to that happening?
[737.04 → 743.26] Why did the data science community leave things, or I can't say leave, but moved away from things like R?
[743.30 → 743.98] Right, exactly.
[744.12 → 745.04] Yeah, where did that come from?
[745.10 → 748.04] So I think there are two things at play in that transition.
[748.46 → 759.06] One of those things certainly has to do with Python being a real, in quotes, real programming language in the sense that you can build simple things.
[759.06 → 766.96] You can build graphs and data analysis tools and whatnot, but you can also build Instagram and YouTube and all these others.
[768.10 → 771.32] Whereas things like R, quite literally, those are written on Python.
[771.82 → 781.26] So there are other languages they were using, like R at the time was a sort of scientific statistics type programming language that did data science-y stuff.
[781.26 → 787.28] But if you wanted to go build a web app to show off your results, well, what are you going to use, Node or Python?
[787.68 → 789.58] You couldn't stick with it, right?
[789.74 → 790.42] Yeah, that's a good point.
[790.54 → 795.68] So Python has this really nice ability that, well, basically it's a real programming language, right?
[796.12 → 797.16] So that's number one.
[797.58 → 805.40] Number two is Python is pretty unique in this, what I call, it's a full spectrum language.
[805.40 → 813.94] And what I mean by full spectrum is I can be a biologist or astrophysicist or something, and I want to explore a little bit of data.
[814.02 → 817.44] I want to load up a CSV file and run some commands and get a picture.
[818.16 → 824.72] I don't need to understand classes, static methods, static main void, compilation, linking.
[824.86 → 829.08] You know, you don't have to go through all the stuff that like some programming languages do just to get started.
[829.22 → 832.10] You can do just a couple of lines of code, like type a command and it runs.
[832.10 → 835.62] And yet you can build things like Instagram and so on.
[835.74 → 846.40] Like it can grow into this absolutely professional system that you can use, but you're not forced to understand all these deep abstractions that are meant for large applications right away.
[846.52 → 847.96] You can like to adopt them as you need it.
[848.04 → 848.74] Does that make sense?
[848.88 → 850.10] Yeah, yeah, that makes a lot of sense.
[850.54 → 853.08] So we talked about that inflection point around 2012.
[853.88 → 861.54] And, you know, when I was looking and doing some research about Python, Python is actually one of the world's most Googled, Google searched coding languages.
[861.54 → 861.98] Wow.
[862.38 → 865.70] Do you feel like it's really picking up and growing at this point?
[866.22 → 868.52] I do think it's picking up and that it's growing.
[869.36 → 875.54] There's, you know, in those last number of years we talked about, there's certainly more enterprise groups that are using Python.
[876.28 → 879.00] It used to be, you know, .NET, Java, maybe some C, right?
[879.04 → 879.70] That was the answer.
[879.88 → 882.24] And now Python is starting to make its way in.
[882.30 → 886.14] And I think it's kind of getting sideloaded into those environments somewhat.
[886.26 → 888.90] And by that, I mean like the data science folks, right?
[888.90 → 888.94] Right.
[889.18 → 894.46] It's like, well, obviously we're going to use JupyterLab and all the cool notebook stuff.
[894.68 → 895.98] And, right, that's Python.
[896.38 → 900.50] Data science doesn't have such a legacy code base story, right?
[900.56 → 909.42] Like if I'm going to start a new project where we're exploring some ad campaign or some science results, like that doesn't have a huge dependency on old stuff.
[909.52 → 911.58] Like models and data expire.
[911.58 → 916.14] So it's easier for the data science world to kind of switch technologies or stay more current.
[916.42 → 917.58] That's a good point.
[917.78 → 918.16] Yeah, thanks.
[918.34 → 918.68] Yeah.
[918.86 → 921.82] And it sounds like it's not going to stop growing anytime soon.
[921.84 → 926.32] It sounds like it's going to keep growing, and the momentum is still, you know, still going to carry it forward.
[926.70 → 930.34] What do you think is going to influence that growth the most moving forward?
[931.14 → 933.70] I feel like it's this ball kind of rolling downhill.
[933.70 → 938.86] So we have all the libraries and packages you can use with Python.
[939.52 → 943.70] You know, it's a ridiculous number that we have now, right?
[943.74 → 945.76] Like a year or two ago it was 100,000.
[945.82 → 949.28] Now it's 170,000 packages or projects.
[949.44 → 953.00] You can just, you know, in a couple lines of code, oh, I'd like to do machine learning.
[953.42 → 962.44] Someone at the conference showed us an example of here's how we're going to train a machine learning system to be given a bunch of faces of people.
[963.30 → 965.00] Choose what type of eye they have.
[965.06 → 965.90] Do they have round eyes?
[965.96 → 966.68] Do they have oval eyes?
[966.74 → 967.20] Things like that.
[967.26 → 969.40] Apparently this drives like the kind of makeup you have or something.
[969.60 → 969.92] Oh, wow.
[970.06 → 976.38] This woman did a great presentation, and she said, and here's the code to train this model and then to ask it questions.
[976.38 → 979.30] And it was like 15 lines of code from beginning to end.
[979.30 → 983.12] And you have, here's your thing that tells you, you know, given a picture of what your eyes are like.
[983.20 → 983.66] Oh, my goodness.
[983.68 → 991.42] The momentum of those types of things, like these little, like super powerful things you can just bring in through these packages is ridiculous.
[991.88 → 992.66] That's so cool.
[992.74 → 993.44] Isn't that crazy?
[995.56 → 997.96] Okay, let's pause that conversation for a sec.
[998.20 → 1000.08] We're going to hear more from Michael later on.
[1000.62 → 1003.08] But I want to go back and underline something.
[1003.42 → 1008.16] It's what makes all those amazing Python qualities possible in the first place.
[1008.16 → 1010.16] The Python community.
[1010.88 → 1016.36] A defining part of Python's success is that huge, responsive community.
[1019.44 → 1026.04] At the same time, as we saw with Van Possum's departure, the size of that community could be overwhelming.
[1026.68 → 1031.78] I mean, imagine having to carry the hang ups of an entire language around with you.
[1031.78 → 1039.18] In a way, attracting such a massive community made the idea of a single dictator for life just untenable.
[1040.84 → 1046.94] Van Possum wasn't necessarily prepared for how huge a response his language was going to receive.
[1046.94 → 1060.32] But, almost organically, community members pulled together Python's mailing list, its newsgroup, its website, and eventually, the process for discussing language changes via Peps.
[1060.70 → 1063.82] That stands for Python Enhancement Proposals.
[1063.82 → 1070.30] So, despite the dictator title, Van Possum was building a language that you could really talk back to.
[1070.74 → 1073.12] A language that users could help build.
[1073.88 → 1084.12] I'm betting that, despite his frustration at that moment of departure, Van Possum knew that a dynamic community would give more to his language than it could ever take away.
[1084.64 → 1085.68] My name is Diane Mueller.
[1086.38 → 1090.88] Diane's the Director of Community Development at Red Hat for the cloud platform.
[1090.88 → 1097.82] Over the past 30 years, she's witnessed a powerful evolution in the strength of open-source communities.
[1098.44 → 1101.30] And she's been impressed by Python's community in particular.
[1101.64 → 1112.50] The Python community has done amazing—they brought in the concept of codes of conduct for conferences, diversity, scholarships, all of that sort of stuff.
[1112.50 → 1121.98] By bringing in the different voices and the different perspectives, we get a better and more innovative project that will live on longer and hopefully work better for more people.
[1122.74 → 1131.24] Even the mistakes they made, they handled openly and transparently and through collaboration with the community.
[1131.24 → 1147.14] After seeing that sort of spirit wither away into a bro culture from Silicon Valley and startups, Python felt like coming back home to the roots of where I got started and the community that had been around back in the day.
[1147.84 → 1150.94] So, it was pretty inspiring and pretty awesome.
[1150.94 → 1159.16] Inspiring largely because Python redefined what it means to be part of the community in the first place.
[1159.74 → 1165.22] I mentioned that Guido Van Possum started championing women in the community, even as he stepped down.
[1165.78 → 1169.16] But he also helped widen the tent in a more general way.
[1170.16 → 1173.46] Individuals bring a lot more to the table than just code contributions.
[1173.46 → 1180.08] Mostly community managers and project leads focus on trying to get people to contribute to their project.
[1180.62 → 1192.36] And in the Python community, people were really highly encouraging you to work on documentation, to help run the conferences, to help promote diversity.
[1192.62 → 1197.28] There were all sorts of other things you could do to be part of the Python community.
[1197.28 → 1212.88] So, that idea that contribution isn't just about code, it's about participation, it's about learning and education, and it's about a lot about documentation was the way into communities for a lot of people.
[1213.52 → 1216.24] Of course, we've still got a ways to go.
[1216.44 → 1219.08] The meritocracy is still very technically focused.
[1219.08 → 1232.32] No one's going to doubt that, but I think you also see the belief in that community management and community managers were skilled parts of a community, as opposed to just the person we hired to create our events for us.
[1233.62 → 1241.04] For Diane, Van Possum's decision to officially abdicate his dictator role is part of a global shift.
[1241.54 → 1245.44] It's moving away from older, monolithic kinds of language building.
[1245.44 → 1248.64] So, I think we might have moved on from that model.
[1250.36 → 1255.52] Though every once in a while I hear someone say, yeah, I'm the benevolent dictator for life of this project.
[1255.60 → 1257.22] And I'm like, yeah, I don't think so.
[1260.02 → 1263.74] Diane Mueller is the director of community development at Red Hat.
[1267.38 → 1272.16] By the time Guido Van Possum sent that jaw-dropping transfer of power memo,
[1272.16 → 1275.82] the Python community was a powerhouse unto itself.
[1276.46 → 1280.48] It's common for projects to adopt new governance models as they grow.
[1281.10 → 1286.58] And in many ways, as we've seen, these folks were ready to take charge of their own language.
[1287.26 → 1290.84] But I still want to know, how exactly did that pan out?
[1291.38 → 1293.62] What happened after Van Possum stepped away?
[1294.14 → 1298.32] Let's go back to our conversation with Michael Kennedy to get some answers.
[1298.32 → 1303.38] Back and kind of away from Python, how has the community been doing without him?
[1304.38 → 1310.44] Well, the community has been okay, but we've been in, at the highest level of kind of stasis.
[1311.24 → 1318.00] The runtime and the language just basically had to go into like a coma.
[1318.20 → 1322.24] There were proposals for interesting things, and they were sometimes complicated,
[1322.86 → 1324.02] but sometimes really simple.
[1324.02 → 1327.76] Like, hey, wouldn't it be great if we could ship Python yearly instead of every 18 months,
[1327.84 → 1331.60] so it's a little more predictable, tie it around the yearly conference, things like that.
[1331.94 → 1336.00] Like, that couldn't be decided because there was no way to make decisions after he stepped down.
[1336.22 → 1338.40] He basically said, I'm going to go on vacation.
[1339.16 → 1340.12] This is up to you guys.
[1340.24 → 1341.98] You have to figure out how to keep running this.
[1342.40 → 1345.70] I'm not even going to tell you how to decide how to keep running it.
[1345.76 → 1347.48] Like, this is your problem now.
[1348.74 → 1349.88] That sounds dramatic.
[1350.52 → 1351.30] But check this out.
[1351.30 → 1354.04] Remember those Python enhancement proposals?
[1354.72 → 1357.10] The Peps that allow the community to give feedback?
[1357.88 → 1359.92] Well, Peps to the rescue.
[1360.58 → 1365.82] There was a series of them trying to determine new governance models for the Python community.
[1366.18 → 1371.74] Well, the big news is they've decided on one of those called the Steering Council,
[1371.92 → 1373.12] which is like five people.
[1373.24 → 1374.54] I believe they all have equal votes.
[1375.34 → 1378.30] And they've recently elected those five.
[1378.30 → 1381.72] So instead of it being on one person's shoulders, it's on all of them.
[1381.78 → 1387.78] And one thing that I think is really nice is that we have Guido Von Possum as one of those members.
[1387.78 → 1388.78] So he stepped away.
[1388.86 → 1394.86] He said, I cannot be the single source of, you know, all the pressure of people wanting changes and feedback.
[1395.50 → 1398.38] But he didn't completely run away from the language.
[1398.50 → 1400.64] He's still a core developer, and he's on the Steering Council.
[1400.64 → 1405.82] So he still has some say, but he doesn't have to take it, like, on entirely, which is pretty cool.
[1406.88 → 1409.04] I'm wondering how that works out in reality.
[1409.04 → 1414.94] Because I feel like if I'm on the Steering Council, and I'm sitting next to, you know, the creator of the language,
[1415.52 → 1417.48] I'd probably tend to agree with whatever he says.
[1417.68 → 1418.12] Right, exactly.
[1418.28 → 1421.20] Like, all things being equal, like, ties go to Guido.
[1422.32 → 1423.28] Yeah, exactly.
[1423.28 → 1424.72] You know, I don't know.
[1424.74 → 1432.36] I do know some of the people on the Steering Council, and they've been constant contributors and developers,
[1432.80 → 1437.72] maybe even at a code level more so than Guido for, like, 15 years.
[1438.18 → 1442.22] So they're also pretty deeply involved and pretty opinionated.
[1442.58 → 1443.20] And invested.
[1443.62 → 1445.02] Yeah, yeah, certainly invested.
[1445.12 → 1447.10] So I feel like it's going to be okay.
[1447.10 → 1453.34] And also, I feel like Guido's probably like, I still want to be involved, but, you know,
[1453.38 → 1458.50] he's probably done trying to impose his will on people because that'll just put him right back into the same thing.
[1458.52 → 1461.66] I think he's probably going to take a more relaxed position.
[1462.00 → 1462.26] Okay.
[1462.56 → 1467.94] But I'm wondering, do you feel like this model of having a benevolent dictator for life,
[1467.94 → 1474.74] is that model almost required at the beginning of a language in order to get it up and running,
[1474.84 → 1478.14] in order for it to be radical and have these breakthrough advances?
[1478.82 → 1479.22] I do.
[1479.50 → 1483.74] I think stuff mostly designed by committee is not super.
[1484.20 → 1484.42] Yeah.
[1484.74 → 1490.02] You know, so, like, in the early days, so many decisions about, you know, how does the language work?
[1490.10 → 1491.10] Does it use semicolons?
[1491.22 → 1492.02] Does it do this?
[1492.12 → 1492.62] Does it do that?
[1492.68 → 1493.08] What's the main?
[1493.40 → 1497.24] Like, all that stuff is really hard to committee decide, right?
[1497.24 → 1500.28] But, you know, Python is over 25 years old now.
[1500.48 → 1504.24] It's got so many people involved in it.
[1504.44 → 1507.42] I think now that this is a pretty good model.
[1507.86 → 1510.94] They also debated whether there should just be a replacement BDFL.
[1511.18 → 1513.76] Like, who do we elect now to be our king?
[1513.92 → 1514.50] Yeah, yeah.
[1514.58 → 1515.98] They decided against that, though.
[1516.38 → 1516.64] Okay.
[1517.20 → 1524.22] So, if that BDFL position is so important, I'm wondering how long does a community need one?
[1524.22 → 1527.48] You know, it sounds like Guido kind of decided on his own, hey, this is too much.
[1527.58 → 1529.38] This is not sustainable anymore.
[1529.48 → 1530.30] I'm not doing this anymore.
[1530.54 → 1539.54] But if it wasn't his decision, I'm wondering, is there an optimal time when that person should step down, and we should move to something a little bit more democratic?
[1539.54 → 1542.08] Yeah, there has to be, right?
[1542.22 → 1544.08] I think that there probably is.
[1544.54 → 1555.68] It's hard for one person to still be completely connected with the pulse of the community and technology and the new trends, you know, like, let's say 40 years out, right?
[1555.70 → 1556.82] That would be super difficult.
[1556.96 → 1559.00] So, there's got to be, like, this switchover.
[1559.00 → 1569.24] I don't really know where it is, but I feel like it's got to be after you have other people doing more work than the BDFL is doing, you know, right?
[1569.30 → 1572.00] Like, more core contributors and developers.
[1572.24 → 1578.06] And you're just like, well, I was on vacation and look at all these new things that happened, and it survived or something to that effect.
[1578.32 → 1578.50] Yeah.
[1578.62 → 1580.84] It's almost like the community will tell you when it's ready.
[1581.04 → 1581.28] Right.
[1581.36 → 1581.72] Exactly.
[1581.72 → 1590.80] The Python community is still taking on a life of its own.
[1591.28 → 1593.32] So, that's where we'll leave them for now.
[1594.12 → 1599.16] Michael Kennedy is the host of two podcasts that'll keep on tracking their progression in the meantime.
[1599.98 → 1603.24] You can check out Talk Python to Me and Python Bites.
[1605.92 → 1611.54] Have you ever heard the story of Solon, the guy known as the lawgiver of ancient Athens?
[1611.72 → 1612.70] Pretty cool guy.
[1613.30 → 1620.28] After Solon established a constitution for Athenian democracy, he went off into a state of voluntary exile.
[1620.94 → 1625.66] That's because he knew there was a danger he'd become a tyrant if he stayed in power.
[1626.68 → 1634.46] I guess Guido van Possum is a latter-day Solon, giving us decades of standard practice, which is a bit like a constitution.
[1634.46 → 1642.72] Here's a guy who set up a brilliant programming language, a language where an open source community could really make it their own.
[1643.28 → 1648.72] And then, he also gave them that transfer of power moment, where he told them,
[1649.12 → 1649.86] You're on your own.
[1650.28 → 1651.90] I'm no longer your dictator.
[1651.90 → 1659.32] He made sure that it had to be the community, not himself, that carried the Python mantle forward.
[1659.62 → 1667.78] In a way, Guido van Possum's transfer of power memo is a manifesto for all programming languages in an open source world.
[1667.78 → 1675.06] Because as any language grows its community, it ends up taking on challenges that only the community can solve.
[1675.06 → 1683.98] In Season 3 of Command Line Heroes, we're doing a deep dive into the world of programming languages.
[1684.72 → 1689.40] Languages gain influence because they solve a new problem in some powerful new way.
[1689.98 → 1697.56] And for the rest of this season, we're uncovering the superpowers baked into JavaScript, Perl, COBOL, Go, and so much more.
[1698.74 → 1704.60] Next episode, we'll learn the story of BASIC and what it teaches us about everybody's first language.
[1705.06 → 1714.38] If you want to dive deeper into Python or anything else you heard on this episode, head over to redhat.com slash command line heroes.
[1714.94 → 1717.28] Until then, I'm Saran ya Barak.
[1717.84 → 1718.94] Keep on coding.
