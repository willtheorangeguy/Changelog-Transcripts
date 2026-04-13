[0.00 → 8.64] Welcome to Practical AI.
[9.20 → 15.96] If you work in artificial intelligence, aspire to, or are curious how AI-related technologies
[15.96 → 18.78] are changing the world, this is the show for you.
[19.20 → 24.36] Thank you to our partners at Vastly for shipping all of our pods superfast to wherever you
[24.36 → 24.66] listen.
[24.92 → 26.76] Check them out at Fastly.com.
[26.76 → 32.02] And to our friends at Fly, deploy your app servers and database close to your users.
[32.44 → 33.70] No ops required.
[34.04 → 36.08] Learn more at fly.io.
[42.16 → 45.22] Welcome to another episode of Practical AI.
[45.54 → 47.18] This is Daniel Whiten ack.
[47.30 → 53.32] I'm a data scientist with SIL International, and I'm joined as always by my co-host, Chris
[53.32 → 56.16] Benson, who's a tech strategist at Lockheed Martin.
[56.16 → 57.40] How are you doing, Chris?
[57.72 → 58.78] Doing well, Daniel.
[58.84 → 59.40] How are you today?
[59.88 → 60.90] I'm doing great.
[61.52 → 64.92] Chris, have you ever been called a grandmaster in anything?
[65.56 → 69.38] No, but I really wish I had because it's a freaking cool name, man.
[69.56 → 69.98] Our title.
[70.34 → 72.70] Weren't you like a street fighter or something?
[72.90 → 74.92] You were like a black belt or something?
[75.16 → 76.22] Oh, don't go that.
[76.70 → 79.58] Something like that 30 years ago.
[79.94 → 82.12] But yeah, once when I was a kid.
[82.12 → 82.72] But you know what?
[82.72 → 86.18] I was never a grandmaster at anything.
[86.72 → 88.60] I was just trying not to get pummelled.
[88.72 → 88.82] Yeah.
[88.82 → 91.34] I was just trying not to hit the mat, and that's it.
[91.70 → 91.96] Okay.
[92.12 → 98.74] Well, today we have with us an actual grandmaster, a Kaggle grandmaster, Christoph Hinkle, who's
[98.74 → 105.28] a senior deep learning data scientist at NVIDIA and a Kaggle grandmaster multiple times.
[105.28 → 106.42] Triple grandmaster, by the way.
[106.62 → 106.90] Yeah.
[107.10 → 109.14] In multiple of the different categories.
[109.98 → 111.26] So welcome, Christoph.
[111.30 → 112.28] It's great to have you here.
[112.62 → 113.22] Welcome, Daniel.
[113.46 → 114.12] Welcome, Chris.
[114.38 → 115.50] Very happy to be here.
[115.56 → 115.82] Awesome.
[116.06 → 116.38] Yeah.
[116.38 → 122.66] Well, for those that aren't familiar with this concept of Kaggle grandmaster, could you
[122.66 → 126.20] kind of give us the briefing on what exactly that means?
[126.36 → 131.42] And in the context of also Kaggle, what generally, I think a lot of people are familiar with that.
[131.50 → 135.38] But just in case, what is Kaggle, and what does it mean to be a Kaggle grandmaster?
[136.06 → 136.24] Yeah.
[136.36 → 137.60] So what is Kaggle?
[138.28 → 142.58] Kaggle, I would say, is like a platform for machine learning in general.
[142.58 → 148.70] It started off as a platform for hosting machine learning competitions.
[149.56 → 150.94] That's how it became popular.
[151.66 → 158.94] But in like the recent years, it also expanded for like being a platform for discussions,
[159.52 → 161.68] being a platform for sharing notebooks.
[162.46 → 164.90] They're hosting millions of data sets.
[165.40 → 171.52] So they're trying to become really like the go-to community for every topic around data science.
[171.52 → 174.34] And it's free to register for everyone.
[174.86 → 182.06] And they also provide some free resources where you can run code and try different stuff on competitions.
[182.72 → 189.82] And on this platform, they introduce different tiers in order to gamify a little bit.
[189.86 → 193.56] So to incentivize users to post content or to participate.
[194.66 → 199.48] So there are four different areas in which you can reach like different levels.
[199.48 → 203.36] So there are like competitions, which is like the most famous one.
[203.96 → 209.68] But there's also notebooks where you just progress by sharing notebooks with others.
[210.48 → 213.32] And the progression is based on upvotes on your notebooks.
[213.82 → 217.06] Then there are discussions, which work in the same format.
[217.24 → 220.94] So you post an answer to a question, or you post an interesting topic.
[221.32 → 226.94] You can also post just memes and generate upvotes in this way.
[226.94 → 229.70] And then there's data sets.
[230.16 → 235.16] So you can also post an interesting data set or a data set you think might be helpful for others.
[235.66 → 237.48] And then people can upload your data set.
[237.60 → 238.64] And by this, you progress.
[239.56 → 242.80] And you basically progress by earning medals.
[242.94 → 246.40] They're like bronze, silver and gold medals in each of the four areas.
[246.40 → 251.14] And then with these medals, you can reach like different tiers.
[251.62 → 254.82] So you start with as a novice, I think.
[255.08 → 256.48] Then you're a contributor expert.
[257.12 → 258.38] Then at some point you're a master.
[259.04 → 261.40] And like the very last stage is a grandmaster.
[262.50 → 265.02] And to put that into perspective.
[265.02 → 273.10] So from the 10 million users that are registered on Kaggle, there are 280 competition grandmasters.
[273.30 → 279.58] So it's really like the elite of the elite, the top-notch people in their area, I would say.
[280.06 → 283.30] So I have to ask because, you know, we were talking about it.
[283.46 → 286.34] Which of the three categories are you a grandmaster in?
[286.52 → 288.78] And what's the fourth one that you're not?
[288.86 → 291.66] And of course, I'm going to ask you, when are you going to become a grandmaster in the fourth one?
[291.66 → 294.36] So I'm a grandmaster in competitions.
[294.92 → 296.30] And that's the most difficult one.
[296.42 → 296.74] Indeed.
[297.98 → 300.08] Then I'm a grandmaster in notebooks.
[300.48 → 302.66] Because I shared some high-value notebooks.
[303.24 → 305.30] And then I'm also a grandmaster in discussions.
[305.30 → 306.86] Because I like to discuss stuff.
[307.12 → 308.24] That's also why I'm here.
[308.56 → 312.62] But I'm not so fond of curating data sets and uploading data sets.
[312.82 → 313.50] I can't blame you.
[314.48 → 316.96] That's why I'm only a beginner at the data set.
[317.16 → 319.10] That would be the one I would choose first.
[319.76 → 320.84] See, that's Daniel.
[320.84 → 323.92] Daniel loves to do data grudging and stuff.
[324.14 → 325.38] It's sick.
[325.46 → 326.20] That's terrible.
[326.90 → 327.82] So I understand.
[328.10 → 331.92] I give you a pass on not being a grandmaster in the fourth one there.
[332.54 → 335.08] What got you into Kaggle in the first place?
[335.22 → 338.88] And what was the journey like towards where you're at now?
[339.10 → 343.08] Some people might just be jumping in on Kaggle and trying things.
[343.18 → 345.80] And they have a vision of how far this could go.
[345.94 → 348.32] But what was the journey actually like for you?
[348.32 → 354.42] I think it's quite interesting because my journey began right in the last months of my PhD.
[354.98 → 356.52] So I did a PhD in mathematics.
[357.02 → 363.86] And in the last few months, so after I sent out everything and I just was waiting for my defence,
[364.30 → 366.06] there was suddenly some free time.
[366.52 → 367.64] And also free weekends.
[367.84 → 369.80] I wasn't used to it during the PhD.
[369.80 → 374.66] And I was also always curious about the AI topic.
[374.92 → 377.04] So back then, it was like five, six years ago.
[377.68 → 383.80] It was not so hyped as now, but it was like a niche area, what are neural networks and so on.
[383.80 → 392.88] And so I was just curious about that, watched some YouTube videos, started a Coursera course on like what are neural networks and so on.
[392.88 → 401.24] And due to that, I quite quickly found out about Kaggle and then just started with my first competition right away.
[401.68 → 405.00] And since then, I'm booked in the system.
[405.24 → 406.16] And how long has that been?
[406.56 → 407.88] Six years now, I think.
[408.46 → 416.62] And during those six years, also my professional life progressed more and more towards machine learning and deep learning and data science.
[416.62 → 422.30] So six years ago, when I joined Kaggle, I was working as a risk analytics consultant.
[422.82 → 424.76] So I had nothing to do with machine learning.
[424.92 → 426.50] I had nothing to do with data science.
[426.72 → 429.10] I programmed a bit on risk models.
[429.32 → 432.58] So I had some background in like R programming or MATLAB.
[432.92 → 434.76] But I never used Python before.
[435.24 → 440.64] And then due to Kaggle, also my professional career shifted towards machine learning and deep learning.
[441.00 → 446.14] Until right now, I'm working as a deep learning data scientist at NVIDIA.
[446.14 → 449.18] Which is like one of the top-notch companies in this area.
[449.44 → 453.32] Yeah, that's like the gold standard of jobs in the AI world right there.
[453.32 → 464.56] So do you feel like the experiences on Kaggle and your success there, in what ways did that kind of contribute to your own sort of career advancement?
[464.80 → 471.08] And also like your understanding of what you wanted to do as your career advanced?
[471.42 → 474.02] Yeah, it really had like a lot of impact.
[474.02 → 479.46] So step by step, I moved into the position I'm right now.
[479.76 → 483.96] So when I started, I was doing Kaggle like before and after work a bit.
[484.42 → 489.48] Not too much, like half an hour after work, half an hour before work and on weekends.
[490.42 → 491.68] And then I made some.
[491.90 → 496.10] And of course, I did horribly on my first competitions because I had no clue of anything.
[496.64 → 499.48] But the nice thing is that you really progress step by step.
[499.48 → 501.64] So in the first competition, you do horribly.
[502.08 → 505.00] In the next one, you do badly, but not horribly.
[505.92 → 511.02] And then you progress more and more until you become better and better.
[511.50 → 518.74] I quite quickly realized that a lot more fun in like machine learning and deep learning than on risk consultant.
[519.02 → 521.86] Just because you can be more creative, I would say.
[521.86 → 524.90] I moved within the consultancy company.
[525.34 → 527.86] I was lucky that they also had like a data science team.
[527.98 → 530.12] So I moved to the data science team there.
[530.38 → 538.04] And I had my first synergy effect between Kaggle competitions and what I learned there and what I was using in projects.
[538.20 → 541.26] So I could use my skills in the projects.
[541.26 → 544.90] And I could also use skills I gained in the projects in Kaggle competitions.
[544.90 → 548.86] But that was five, six years ago.
[549.40 → 559.00] There wasn't much deep learning in the industry, especially in the insurance industry, where the focus was in my consultants company.
[559.68 → 562.20] So I was not challenged enough.
[563.06 → 565.30] But I wanted to do more and more in this field.
[565.36 → 567.28] And also my skill set grew more and more.
[567.28 → 577.78] So I decided to quit this job and found my own deep learning consultancy just to have like even more synergy between projects and between Kaggle.
[578.28 → 581.22] Tell us a little bit about what that was like in those days.
[581.22 → 592.82] Because as we've grown up with deep learning over the last few years, I would guess that at least in the beginning, it was a little bit challenging to land, you know, engagements maybe.
[593.06 → 595.10] Or was it or did you have them from the start?
[595.10 → 602.68] Because I know for me, early in that phase, about the time Daniel and I started the podcast, people were like, deep what?
[603.18 → 610.18] So did you have any challenges in those early days that have obviously evaporated as the world has taken this on?
[610.62 → 611.06] Certainly.
[611.68 → 613.46] Not only in terms of projects.
[613.80 → 624.16] So people, especially the decision makers, I would say, they are really cautious about the let's say, possibilities you can do with deep learning.
[624.16 → 628.82] Especially like five, six years ago, there weren't any resources around.
[629.32 → 633.90] So I talked with customers about what amazing things you can do with like deep learning.
[634.12 → 637.18] And then they didn't have a single GPU they had access to.
[637.92 → 643.52] So that's like really like two worlds clashing against each other.
[643.52 → 648.10] So there were a lot of interesting and challenging problems around that.
[648.10 → 658.48] But as soon as they basically gave me a chance and I could do some prototype and can really show what you can do, then it was easy to convince them.
[658.68 → 664.76] But to get to this point, especially as like a young startup, a young consultancy startup, that was quite difficult.
[664.76 → 668.78] So I definitely want to get into many things later on.
[668.86 → 677.02] But I'm also thinking about these people out there that are maybe, you know, inspired by your journey and wanting to get involved in Kaggle and other things.
[677.02 → 684.52] I'm wondering if you can like to share a little bit about, because while you and Chris were talking about perceptions around deep learning that have shifted.
[684.72 → 694.24] Also during that time, like the tooling around deep learning has shifted and like the accessibility of maybe like thinking about four years ago,
[694.24 → 700.98] if I was to train a deep learning model for a Kaggle competition versus like being able to do that now,
[701.20 → 709.00] how have you seen that shift over that time period in terms of this sort of ability for people to,
[709.60 → 712.54] I guess people use the word democratize or whatever,
[713.06 → 718.04] the ability for people to hop in and do something advanced like that very quickly?
[718.72 → 721.02] There are like two aspects, I would say.
[721.02 → 723.76] One is like software wise and framework wise.
[724.24 → 726.82] There have been a lot of progress there.
[727.10 → 736.04] So when I started, it was still like TensorFlow 0.something, which was working, but it's really like no programming.
[736.70 → 741.16] So there was nothing like an RNN layer or a transformer layer or so.
[741.26 → 742.92] You need to code everything from scratch.
[743.64 → 746.66] But it also helps a lot for understanding the things.
[746.66 → 758.28] So I think nowadays people don't really understand the granular aspects of deep learning because you just do something like model. Fit, and you don't have any clue what's happening behind the curtain.
[758.28 → 764.22] So certainly it's easier nowadays to train a model just by this higher frameworks.
[764.22 → 766.90] Just calling by name.
[766.90 → 770.36] There's not only stuff like Keras, High Dodge Lightning.
[770.70 → 776.50] There's like a lot of different frameworks you can use, which are really high level and accessible for beginners.
[776.50 → 780.70] And there's also a lot of training material for these frameworks.
[781.08 → 782.26] So a lot of tutorials.
[782.94 → 787.38] So it's really easy to train a simple model for a simple task.
[787.38 → 797.74] But also in terms of resources, I think they are more beginner-friendly because on Kaggle, for example, five years ago, they didn't give you any resources.
[798.30 → 799.78] There was no Google Cola.
[800.30 → 803.90] So you basically have to have your own GPU at home.
[804.02 → 808.98] You need to build your own desktop machine or something, or you spend your own money on cloud resources.
[809.44 → 816.14] But now for beginners, you can get access to Cola, which gives you a free notebook to experiment.
[816.14 → 818.40] You get some free resources, some Kaggle.
[818.74 → 821.24] There's a lot of student credits and student programs.
[821.78 → 826.58] So it's really easy to start your data science journey, I would say.
[826.74 → 831.78] And there's also a lot of more material online where you can really teach yourself, I would say.
[846.14 → 853.56] Hello, friends.
[854.02 → 857.22] This is Jared here to tell you about Changelog++.
[857.86 → 865.40] Over the years, many of our most diehard listeners have asked us for ways they can support our work here at Changelog.
[865.54 → 868.12] We didn't have an answer for them for a long time.
[868.48 → 875.22] But finally, we created Changelog++, a membership you can join to directly support our work.
[875.22 → 886.42] As a thank you, we save you some time with an ad-free feed, sprinkle in bonuses like extended episodes, and give you first access to the new stuff we dream up.
[886.94 → 890.28] Learn all about it at changelog.com slash plus.
[890.54 → 893.84] You'll also find the link in your chapter data and show notes.
[894.46 → 897.50] Once again, that's changelog.com slash plus.
[897.70 → 898.32] Check it out.
[898.70 → 899.70] We'd love to have you with us.
[899.70 → 917.44] So, Christoph, as you were kind of leading in, talking about your entry into the world of deep learning and your career shift to accommodate that,
[917.72 → 922.42] and you're talking about kind of learning from Kaggle competitions and engaging in that,
[922.42 → 926.88] and then it was increasingly applicable in your professional life.
[926.98 → 929.82] Can you talk a little bit about how that happens?
[930.00 → 937.52] Like, when you're thinking about a Kaggle competition, and you're now working in a job in this field, how do the two relate?
[937.66 → 944.94] How are Kaggle competitions relevant to solving real business problems in a real job and getting that synergy?
[945.12 → 945.86] What is that like?
[945.94 → 947.52] What is the connection between the two like?
[947.52 → 951.68] I would say there are a lot of synergy aspects.
[952.58 → 961.68] So, doing a Kaggle competition is really very similar to doing a project at work, which is about performing a first prototype.
[962.66 → 968.78] So, in a Kaggle competition, you get like a problem which you are not familiar with, often from a different domain.
[968.78 → 982.14] Can be from biology, can be from astrophysics, can be from chemistry, can be Bengali language, sign language, just so many different problems that you have no clue about when you start.
[982.78 → 991.18] And then you finally have like three months' time to find like the best possible solution and also compete with other data scientists.
[991.18 → 996.04] So, like this prototype project characters, very similar.
[996.54 → 998.48] So, you have like these three months' time window.
[999.22 → 1001.56] Then you have a collaborative part.
[1002.26 → 1004.16] So, in Kaggle, you can also form teams.
[1004.34 → 1013.24] So, you can participate in competitions in a team, which is very similar to working in a team in your job with all the ups and downs, I would say.
[1013.24 → 1017.62] So, you're working in a team under pressure often.
[1017.94 → 1023.72] So, Kaggle competitions can create quite some pressure, more pressure than you might feel in your day-to-day job.
[1025.18 → 1029.86] So, you also get used to working efficiently with others.
[1029.98 → 1036.26] So, in terms of coding, in terms of reading their code, in terms of structuring the project.
[1036.26 → 1040.52] So, really like all aspects of project management are also important.
[1041.64 → 1047.30] And also things like optimizing runtime and optimizing code structure.
[1047.82 → 1049.98] You wouldn't think that it's quite important.
[1050.60 → 1054.02] But I think it's quite important also for Kaggle competitions.
[1054.78 → 1059.52] Because recently, they run the competitions on a restricted hardware.
[1059.52 → 1066.44] So, you just submit your code, and they will run your code on their infrastructure using their Kaggle notebooks.
[1066.82 → 1071.46] So, you need to have your code in a way that it's kind of production style.
[1071.58 → 1073.20] That's also what you would do in a project.
[1073.44 → 1075.72] So, you would develop ideas and so on and so forth.
[1075.78 → 1079.02] But at the end, you want to productize your code.
[1079.42 → 1083.94] And you need to think about all these ML Ops problems as well.
[1084.48 → 1086.84] And you also train those skills in Kaggle competitions.
[1086.84 → 1091.12] So, I really like parallels between the two worlds.
[1091.56 → 1098.00] That said, I must say that two things are really different between Kaggle and the real world project.
[1098.44 → 1100.12] First thing is data acquisition.
[1100.70 → 1103.36] That's like a very big topic in the real world.
[1103.56 → 1107.94] It's no topic, well, no topic, but a very minor topic on the Kaggle competition.
[1108.52 → 1110.32] You already add your training data.
[1110.32 → 1117.06] Of course, you sometimes can expand your training data by looking for more data online.
[1117.52 → 1120.94] But in general, you already have like a fixed training set you can work with.
[1121.50 → 1129.16] Whereas in the outside world or in the real world, that could be like the main problem just to require some data.
[1129.16 → 1134.00] And the second thing is definition of the metric.
[1134.42 → 1137.66] So, in Kaggle, people are like evaluated based on some metric.
[1138.30 → 1141.58] And this metric is predefined before the competition starts.
[1142.00 → 1149.84] Whereas in the real world, that can be a discussion which takes for ages between like data scientists, the business,
[1150.32 → 1156.18] and just creating a metric that is representative of the business problem can take a lot of time.
[1156.24 → 1158.52] And you don't have these issues and discussions on Kaggle.
[1158.52 → 1164.52] I'm curious, as you were describing that, I have an idea that came to mind.
[1164.98 → 1174.30] So, recognizing the limitation of you already have data provided and recognizing the fact that the metric is well-defined on a Kaggle team.
[1174.50 → 1178.24] And both of those are kind of optimal situations compared to the business world.
[1178.24 → 1187.96] But from the perspective of an organization out in the world, any organization that is keenly interested in data science and stuff,
[1188.30 → 1193.70] would forming Kaggle teams or participating in Kaggle teams be a good recruitment tool?
[1193.70 → 1199.30] Because if you can find people that are performing well on teams in that capacity,
[1199.70 → 1202.78] it doesn't check every box, you know, for what the business world is doing.
[1202.86 → 1207.62] But it kind of gives you a sense maybe of this might be someone who could fit in with us.
[1207.74 → 1212.90] We're going to throw the messiness of data sets and the messiness of metrics on top of that.
[1212.90 → 1215.04] But what do you think of that idea?
[1215.16 → 1221.04] Is that something that people might be thinking about in terms of trying to build data science teams for their organizations?
[1221.74 → 1222.22] Certainly.
[1222.60 → 1225.76] I think that that would be a great idea if people do this.
[1225.90 → 1230.06] And some companies already use Kaggle as a hiring tool.
[1230.70 → 1235.12] So, in order to run a competition, those competitions are sponsored by someone.
[1235.12 → 1242.20] And there are sometimes companies who sponsor a competition, but also tell the participants that they are hiring.
[1243.12 → 1247.90] And that if you are finishing like in the top spot, you can apply for a position there.
[1248.12 → 1253.44] So, getting a position is kind of part of the winning prize sometimes.
[1253.90 → 1259.30] So, they already see that Kaggle is very good for finding good candidates.
[1259.30 → 1267.08] But, as you said, you could also, and Kaggle nowadays even offers the concept of a community competition,
[1267.78 → 1271.42] where you host a competition by yourself without any Kaggle interference.
[1271.62 → 1278.24] And you could do this as kind of assessment centre for filtering potential hires,
[1278.40 → 1283.04] or see how they interact on a problem, or see how they work together.
[1283.74 → 1286.84] There are also, so normally Kaggle competitions are like three months or so,
[1286.84 → 1292.90] but there are some formats, for example, Kaggle days, which is like conference type of thing.
[1293.06 → 1298.22] They host like this conference-specific competitions, and they just go like one afternoon.
[1298.88 → 1303.96] And people get like a simple data set, and they have one afternoon to get like a good solution.
[1304.66 → 1309.88] And they could definitely see how this would benefit an assessment centre, for example.
[1309.88 → 1315.84] Because they really see like the whole range of skills people can bring to your company.
[1315.84 → 1325.24] I have to ask, of the sort of competitions and the notebooks that you've contributed to Kaggle,
[1325.64 → 1330.36] maybe the discussions too, what are some highlights for you, like of all the things that you've done,
[1330.48 → 1336.64] what are some highlights of the things maybe either you're most proud of, or that you would like to highlight?
[1337.24 → 1342.18] And what I'm most proud of certainly are the Google Landmark competitions.
[1342.18 → 1348.68] So there's a competition, which was hosted three times yearly by Google.
[1349.24 → 1353.08] And this is about classifying popular landmarks.
[1353.46 → 1356.40] So you have a data set of 5 million images.
[1356.86 → 1358.38] So it's really like large scale.
[1358.78 → 1363.10] And in this 5 million images, you have 80,000 classes.
[1363.54 → 1365.30] So 80,000 different landmarks.
[1365.42 → 1367.58] And you need to classify between those landmarks.
[1367.58 → 1373.84] And the difficulty especially there is that for some landmarks, you only have one or two images,
[1374.44 → 1378.16] which makes it quite complex to classify.
[1378.86 → 1386.32] And another complexity is because some landmarks are quite like looking differently from different angles.
[1386.50 → 1388.56] You can think of a museum, for example.
[1388.82 → 1391.02] People take a picture outside the museum.
[1391.02 → 1393.76] People take pictures within the museum.
[1394.22 → 1397.46] And you still would classify it as the same landmark, for example.
[1398.38 → 1400.02] So the competition is quite tricky.
[1400.46 → 1403.92] And I was able to win it three times.
[1404.46 → 1407.16] And two times of that without a team.
[1407.30 → 1407.98] So just solo.
[1408.34 → 1411.86] And that's something that's even harder in doing Kaggle competitions.
[1412.12 → 1414.84] So without participating within a team, but soloing,
[1414.84 → 1419.18] that brings a lot of additional, let's say, mental stress.
[1419.76 → 1424.48] Because you don't have a team you can talk about your problem with.
[1424.50 → 1430.78] You're just like isolated, working on a problem for three months with like high pressure and so on and so forth.
[1431.08 → 1435.88] So that brings another level of like mental component to the game.
[1436.42 → 1443.82] So I was quite proud that I could win two of those or win three competitions and two of those without any team.
[1443.82 → 1443.86] Great.
[1444.28 → 1446.32] So I'd like to follow up on that.
[1446.42 → 1452.66] What is your talking to people out there that might be, you know, either already participating in Kaggle,
[1452.86 → 1456.74] you know, not at the level that you're at or thinking about jumping in.
[1457.18 → 1463.30] What are some of the attributes that you and I want you to take a moment and harp a little bit on yourself.
[1463.30 → 1467.66] I'm asking you to and say, what are you bringing to the competitions?
[1467.66 → 1473.66] Do you think that really has given you an edge in getting to that grandmaster level?
[1473.82 → 1476.30] And being so competitive at that level.
[1476.48 → 1484.38] Do you have anything that you can offer people that are kind of maybe a little bit intimidated by it or trying to think, how can I level up a little bit?
[1484.50 → 1485.12] What would you say?
[1485.92 → 1500.86] I mean, I definitely have some analytical thinking just from my study of mathematics, because the whole study is there to basically learn how to think efficiently, how to solve problems efficiently.
[1500.86 → 1503.26] So that definitely helps.
[1504.16 → 1511.84] And coming from natural sciences in the broader sense, also a sense of solid experimentation is very important.
[1511.84 → 1522.30] So really having like a clean workbench, so to say, logging your experiments, following up on ideas and so on.
[1522.40 → 1531.04] So this really like thinking like a researcher in natural sciences and following your experiments like in a clean and reproducible way.
[1531.14 → 1532.58] That's also quite important.
[1532.58 → 1540.02] But I think what really pushed me to the top level is the curiosity of different domains.
[1541.06 → 1550.96] So even like top people, they tend to, let's say in quotation marks, lean back and do what they're good at and not expand and learn further.
[1550.96 → 1557.54] But I would say one more edge I get is that I really try a lot of different ideas.
[1558.18 → 1564.26] And at the end, in different areas, I try to explore like very different competitions, very different domains.
[1564.26 → 1571.34] And at the end, every now, and then I can leverage from something that you would think has nothing to do with the other.
[1571.90 → 1575.38] But you still can leverage some ideas and apply some concepts.
[1575.62 → 1587.84] So, for example, you can transfer knowledge from audio classification to biology or to astrophysics or from NLP to computer vision and vice versa.
[1587.84 → 1592.44] So there's a lot of synergy people wouldn't think about.
[1592.64 → 1598.92] And therefore, it's quite helpful to explore as different domains as possible.
[1599.54 → 1605.58] You alluded to this a little bit in what you were saying about used to with Kaggle competitions.
[1605.58 → 1611.50] Maybe you had to build your own machine with a GPU in it to sort of operate in that.
[1611.62 → 1613.74] Now there are good resources with GPUs.
[1613.74 → 1625.14] But I'm wondering, from your perspective, both as a competitor and a grandmaster, but also as a really senior data scientist at NVIDIA,
[1625.64 → 1633.00] how do you view kind of GPU acceleration as kind of important and playing a role in Kaggle competitions?
[1633.26 → 1637.16] Probably most people think about it in terms of training a model.
[1637.16 → 1647.08] But, you know, how do you think about that more holistically in terms of like the accelerated process that's key to performing well in competitions?
[1647.56 → 1655.64] So certainly, GPU-based programming or like calculation is like the bread and butter of training any model nowadays.
[1655.64 → 1668.40] But also, especially NVIDIA, they're looking more and more into moving other parts of your data science pipeline onto the GPU just to make it faster.
[1669.16 → 1676.68] And especially for Kaggle competitions, the speed of which you can run your stuff and try ideas is very important.
[1676.68 → 1686.36] So when a lot of people like on the top level compete against each other, one of the edges you get is when you can do more experiments than the others,
[1686.74 → 1689.50] which are just bound by, of course, your ideas.
[1689.76 → 1695.70] But most of the time, I'm not running out of ideas, but I'm running out of time in the competition.
[1695.70 → 1710.24] And so as long as I can run more experiments than other people can do because I have a more efficient pipeline, or I can run more parts of my pipeline efficiently using GPUs, that gives me an edge.
[1711.16 → 1715.18] And some examples of this are like data pre-processing.
[1715.22 → 1716.66] Or let's start even one step ahead.
[1717.32 → 1719.38] The first step is just data loading.
[1719.84 → 1723.22] Just loading your data frame for doing anything.
[1723.22 → 1725.84] Can be GPU accelerated.
[1726.28 → 1728.28] And that is just like 100x faster.
[1728.94 → 1734.82] So every time you're working on the problem, you get a 100x speed up just in the step of loading your data.
[1735.26 → 1737.78] And that's what Rapids, for example, are all about.
[1738.06 → 1750.54] So Rapids is like an NVIDIA tool stack, which is all about accelerating those parts, which are not like training the model, but are like what is normally handled with Pandas, for example.
[1750.54 → 1755.76] So they have a part which is called QDF, which is basically Pandas on GPU.
[1756.38 → 1760.74] They have something which is QML, which is basically SK Learn on GPU.
[1761.46 → 1766.80] So things like clustering, all this stuff you can do on GPU nowadays.
[1767.32 → 1770.68] Other examples are, for example, NVIDIA DALI.
[1770.68 → 1775.66] That's a tool especially for image processing, but I also support audio and video.
[1776.38 → 1780.10] But an example there would be decoding of JPEGs.
[1780.50 → 1792.04] So people wouldn't think about that, but something like having a JPEG on your disk and just loading the JPEG involves some decoding step, which basically decodes the JPEG format.
[1792.04 → 1804.18] And this can already be done using GPUs and can be accelerated by GPUs and also gives you a significant speed-up during your training, during anything which uses the images.
[1804.52 → 1809.02] So there are a lot of different steps in your pipeline that you can accelerate.
[1809.66 → 1813.36] And that's what all accelerated data science is about.
[1813.36 → 1825.20] So NVIDIA tries to move the complete pipeline from loading the data to saving conclusions, results, all end-to-end on GPUs.
[1825.32 → 1826.48] Yeah, that's fascinating.
[1826.76 → 1837.72] And I'm guessing that some of the things that you're talking about, like loading images or loading data frames or manipulating data frames, maybe doing certain operations, doing clustering.
[1837.72 → 1850.66] I don't know that this is the case, but I would guess like those things pretty consistently show up across competitions too, or in the real world, you could think about them as showing up across many different business problems.
[1850.66 → 1863.08] So like you were talking about your pipeline of processing, which I think is a really, wondering if you can dig into that a little bit, not a specific pipeline, but how you think about like solving a problem.
[1863.08 → 1868.96] Because most people might come to a Kaggle competition or a real world problem and say, okay, here's my data.
[1869.16 → 1874.34] I have my main step is this sort of like training of the model and maybe evaluation.
[1874.34 → 1875.84] Like how good is my model?
[1876.30 → 1876.90] Retrain it.
[1877.00 → 1877.72] How good is it?
[1877.86 → 1878.34] Retrain it.
[1878.34 → 1884.46] How do you think about the data sort of pipeline around, you know, like you're talking about running experiments.
[1884.46 → 1887.76] What is that sort of like data pipeline look like in your mind?
[1887.80 → 1900.42] And what are some of those reusable components or things you find yourself doing over and over again that are accelerated, that you found accelerated ways to do those things using GPU tooling like Rapids or this DALI?
[1900.70 → 1906.00] It really depends on from project to project, I would say, where it's applicable or not.
[1906.00 → 1916.80] So I would say that Rapids, for example, is even more applicable to the real world because there you might have way larger data frames, for example.
[1916.80 → 1929.58] So if you're like a bigger company, you have like user data, or you have client data or whatever, because the Kaggle competitions often are like packed into little problems that people can work on.
[1929.58 → 1936.78] And not like this company size, large scale data sets with like millions of users or thousands of users.
[1936.78 → 1941.74] And things like Rapids especially shine in like this large scale data sets.
[1942.34 → 1945.70] For me, my pipeline is, I would say, modular.
[1946.10 → 1949.84] So and that developed through the years coming from the competitions.
[1949.84 → 1955.40] So of course, I try to reuse as much as possible just to be efficient.
[1956.12 → 1962.48] So I have a really modular setup where I have one part which is just the model training.
[1962.76 → 1966.46] One part which is about the storage of my data.
[1967.30 → 1973.02] One part which is about logging the experiments and tracking results and visualizing results.
[1973.44 → 1978.00] One part which is about the framework setup, so to say.
[1978.00 → 1991.78] So I use Docker with a specific PyTorch image to have like always the same environment and also can replicate my experiments and also can use the exact same environment of different machines.
[1991.78 → 1996.92] So in the cloud or locally, that's all things I learned during the years.
[1997.60 → 2003.06] So it's a little bit complicated to explain the whole pipeline now on the podcast.
[2003.06 → 2009.44] I actually gave like a one-hour presentation two weeks ago just about this topic.
[2009.82 → 2014.12] So it's pretty difficult to condense into a few sentences.
[2014.56 → 2016.68] It's hard without a diagram for sure.
[2016.82 → 2020.86] But it's fascinating to me like the things you're talking about that you've made modular.
[2020.86 → 2032.10] I think are things people operating in a real world data science environment eventually need to make into sort of like components that work within their team.
[2032.36 → 2032.52] Right.
[2032.94 → 2042.88] Like, you know, my team, like we love using, for example, Streamlet to do like some data manipulation, visualization, interactive stuff on the other end.
[2042.88 → 2044.00] And we have a lot of those.
[2044.36 → 2046.58] We reuse a lot of those components.
[2047.20 → 2053.24] And, you know, we have like certain models that we multilingual models that we train over and over.
[2053.24 → 2057.74] So we've got, you know, modules around that and then like pre-processing and other things.
[2057.74 → 2073.12] So I think these are it's interesting how much what you're talking about overlaps with, I think, the efficiencies you gain over time as a data science team operates together, and they learn how to make their own processes more efficient.
[2074.00 → 2076.44] So I think that that's that's fascinating.
[2076.44 → 2083.04] So I have played around with Rapids a few times, and it is really cool.
[2083.18 → 2086.86] And I'm just looking at the latest stats here on Rapids website.
[2086.98 → 2100.80] And it's talking about performance on 300 million rows by two column data frame with like the highest speed up being for like group by operations like 80 times faster than not using Rapids.
[2100.80 → 2106.26] So like I don't know, you know, how long, you know, that saves you.
[2106.36 → 2117.26] But also like you're talking about if you are doing experiments over and over, and you want to rapidly do experiments, even if that saves you, let's say it's something smallish like in minutes, right?
[2117.26 → 2123.64] A couple of minutes, like you're able to do things much faster and automate things like your automation goes faster.
[2123.74 → 2126.72] You can learn things much faster and reduce that cycle time.
[2126.72 → 2135.70] Although I'm I'm also assuming for many people for their data, it might be more than a more than a minute's long speed up potentially on some of those operations.
[2136.00 → 2140.12] So, yeah, I don't know when you're when you're helping people.
[2140.12 → 2144.78] And you mentioned the discussion groups and the notebooks that you've worked on Kaggle.
[2144.78 → 2159.10] Is this something where you've seen like light bulbs come on for people when they like saying like, oh, I'm trying this group by operation or something on this data, and it's taking me like 15 minutes every time I run through this.
[2159.10 → 2163.52] Is that something you've been able to bring in those discussions and notebooks and such on Kaggle?
[2164.46 → 2165.08] Yeah, certainly.
[2165.08 → 2168.42] So like loading data frames is a good example.
[2169.18 → 2174.92] So 80 times sounds not that much, I think, but it's like one minute or two hours.
[2175.34 → 2181.32] That's like the scale you're talking about, like loading your data frame in two hours or loading it in one minute.
[2181.58 → 2184.00] That's like an ATX speed up difference.
[2184.00 → 2193.10] And especially in Kaggle, those discussions get a lot of traction because on your inference, you actually have like a time limit of like nine hours.
[2193.10 → 2198.10] So people try to get as much stuff into their submissions as possible.
[2198.92 → 2205.44] So loading data frames, manipulating data frames, loading images, all the stuff.
[2205.44 → 2215.02] If you can speed it up, the people will be very, very gratefully adept whatever you give them to speed up their stuff.
[2215.64 → 2217.44] And that's only the inference side.
[2217.92 → 2226.96] So that's even more true for training because as you said, my day to day is like doing a lot of experiments and those speed-ups accumulate.
[2226.96 → 2234.86] So the very first thing I ever do in a competition, like the first two weeks or so, I just optimize my workflow.
[2235.64 → 2245.12] So I optimize all the runtime, optimize how I load my things, accelerate all the pre-processing, post-processing, whatever I have in my pipeline.
[2245.36 → 2255.28] So I can then leverage the remaining time from like the most perfect setup or the most perfect code because then I can just run more and more experiments.
[2255.28 → 2277.40] So I'm curious because as you have been talking about optimizing and being able to do all of these iterations on your experiments, there are people out there, including myself, that are thinking whether they are wanting to jump into a Kaggle competition, they're psyched up because they've been listening to how you've kind of mastered this process.
[2277.40 → 2284.88] Or they're working for a company, and they are trying to get their own systems better and better.
[2285.18 → 2287.86] And, you know, early teams really struggle with that.
[2288.36 → 2297.64] And so either way, with you talking about what you've done and Daniel was jumping in and talking about the work they're done, there are people that want to be there with you.
[2297.72 → 2299.30] You know, they want to at least get on that path.
[2299.30 → 2311.12] Do you have some concrete recommendations on somebody who's at the beginning of that, and they're like, OK, I'm doing data science, but my God, it's taking me a long time to get through each iteration.
[2311.12 → 2316.22] And I'm listening to this grandmaster just cranking out productivity so fast.
[2316.22 → 2327.20] What are a couple of specific things that you would say, go do this and that and that, recognizing that they'll find their own path forward and they'll make their own adjustments.
[2327.36 → 2329.50] But how do they get on that path to begin with?
[2330.22 → 2337.06] The first thing, and I told this several times, is just to start your very first Kaggle competition.
[2337.28 → 2345.62] So you go to Kaggle.com, you look through the ongoing competitions, which is like 15 to 20 ongoing competitions.
[2345.62 → 2349.44] It just shows any topic you find interesting.
[2349.94 → 2352.00] You don't need to be an expert in this topic.
[2352.16 → 2355.24] You don't need to even know about the domain or something.
[2355.80 → 2358.42] But just starting is like the first step.
[2359.00 → 2373.18] And as soon as you start, just by the sheer amount of knowledge which is shared within the forums and the notebooks, you will see that you learn very, very efficiently how to improve your code, how to improve your skill set.
[2373.18 → 2378.74] And you get like immediate feedback on the leaderboard, for example, or on discussions.
[2379.08 → 2382.56] If you add like a comment, and it doesn't make sense, then people will tell you.
[2382.84 → 2385.36] If it doesn't make sense, people will also tell you a thank-you.
[2386.32 → 2392.90] So the leaderboard is very like an objective way and seeing your performance and seeing your progression.
[2392.90 → 2397.38] So that's the very first advice I would give someone.
[2397.92 → 2400.94] Try to find an interesting competition and just start.
[2401.20 → 2402.70] There's basically nothing to lose.
[2402.80 → 2404.24] You just can gain knowledge.
[2404.62 → 2411.00] As said, you will perform poorly on your very first competition, no matter where you come from.
[2411.50 → 2413.24] But just starting is like the first step.
[2413.24 → 2422.80] And as you start, I think the best advice is that you start simple, as simple as possible and just try to progress from that.
[2422.80 → 2436.10] You start with a very simple model with a subset of the data or with like images which are downsampled to a low resolution just to find like an efficient pipeline and to work on your code.
[2436.10 → 2444.74] Because all this is like an investment for the future and all this gives you an easier setup to work on and to improve on.
[2445.36 → 2446.82] Yeah, perfect advice.
[2447.00 → 2463.08] I think that part you talked about, about like spending a couple of weeks optimizing the sort of inputs, outputs and those portions of your pipeline so that you can really put a lot of your focus on fast iterations on the model or that middle bit.
[2463.08 → 2465.64] I think that's really, perfect advice.
[2466.10 → 2469.00] This has been a really fascinating competition.
[2469.40 → 2472.28] I have a long way to go to be a grandmaster, that's for sure.
[2472.74 → 2486.16] But as we wrap up here, this discussion about accelerated data science and the Kaggle competitions, what are you excited about sort of looking to the future?
[2486.26 → 2490.32] You mentioned that you're curious about all of these sorts of different domains.
[2490.54 → 2492.18] You've worked on a lot of different problems.
[2492.18 → 2508.58] What really excites you right now as you look towards the future in terms of things that you want to try or just in general things that you're excited about in terms of the tooling or the community around what you're involved with?
[2508.58 → 2517.26] I would say in the short term, I'm definitely excited about or interested in how AI will support my work.
[2517.26 → 2524.28] So something like GitHub Copilot or other natural language models, which helped me code.
[2524.28 → 2535.38] I haven't tried them much, but I think that in the near future or the short term, those tools will support our everyday life in some way.
[2535.38 → 2542.52] But I'm even more excited in the long term prospects, like what will happen in 10 years and 20 years.
[2543.02 → 2544.56] And that's really exciting.
[2544.70 → 2557.38] Because if you think back like 10 or 20 years in terms of AI and what systems could do and where we are right now, and you extrapolate that into the future, that will be very exciting and amazing.
[2557.62 → 2559.72] That will be what will happen then.
[2559.72 → 2562.70] Yeah, yeah, I think that's a great way to wrap things up.
[2562.88 → 2565.28] Thank you so much for joining us, Christoph.
[2565.34 → 2572.48] Really looking forward to following your progression and the things that you work on in the future and the great things that continue to come out of NVIDIA.
[2572.72 → 2575.96] So thank you for your work, and thank you for taking time to join us.
[2576.32 → 2577.18] Thank you for having me.
[2577.18 → 2588.66] Thank you for listening to Practical AI.
[2589.16 → 2592.98] Your next step is to subscribe now, if you haven't already.
[2593.42 → 2599.46] And if you're a longtime listener of the show, help us reach more people by sharing Practical AI with your friends and colleagues.
[2599.92 → 2604.84] Thanks once again to Vastly and Fly for partnering with us to bring you all Change Talk podcasts.
[2604.84 → 2609.22] Check out what they're up to at Fastly.com and Fly.io.
[2609.62 → 2614.94] And to our Beat Freakin' residents, Break master Cylinder, for continuously cranking out the best beats in the biz.
[2615.22 → 2616.12] That's all for now.
[2616.38 → 2617.54] We'll talk to you again next time.
