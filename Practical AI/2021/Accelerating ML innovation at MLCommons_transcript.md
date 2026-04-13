[0.00 --> 5.74]  This is, I think, about 30 or 40x bigger than anything that's publicly available today.
[5.86 --> 13.24]  And I think the key thing is, for speech-to-text models, you need about 10,000 hours to actually produce something that's functional.
[13.24 --> 24.02]  Now, I don't claim that this will give you a truly production-worthy model, but I think it can really lower the bar for a lot of people, and it's very exciting to me.
[26.00 --> 28.60]  Bandwidth for ChangeLog is provided by Fastly.
[28.60 --> 30.80]  Learn more at Fastly.com.
[31.04 --> 33.32]  Our feature flags are powered by LaunchDarkly.
[33.60 --> 35.40]  Check them out at LaunchDarkly.com.
[35.64 --> 37.50]  And we're hosted on Leno cloud servers.
[37.88 --> 41.42]  Get $100 in hosting credit at Leno.com slash ChangeLog.
[42.04 --> 51.92]  Hey, friends, this episode of Practical AI is brought to you by Kodish, a podcast from the team at Heroku that explores code, technology, tools, tips, and developer life.
[51.92 --> 57.18]  There's tons of great conversations on the Kodish podcast, so I would encourage you to check it out and subscribe.
[57.18 --> 60.66]  But in particular, I wanted to bring to your attention two episodes.
[60.98 --> 67.48]  Episode 98 and 99, where Julien Duque explores the ethical and technical sides of deep fakes.
[67.80 --> 76.50]  The rise of manipulated pictures and videos and other forms of computer-generated media are able to cause uncertainty and doubt in what we see and hear online.
[76.50 --> 80.66]  And so how are we able to use these tools for good, if at all?
[80.96 --> 81.70]  Here's a sneak peek.
[81.90 --> 89.12]  Let's say we want to do a deep fake of my voice and we train the model and we have enough data and everything.
[90.20 --> 95.34]  This will be also able to imitate my accent, for example.
[95.34 --> 102.88]  Like how I pronounce English and the strong pieces of my accent or is not there yet.
[103.18 --> 104.12]  It really depends.
[104.24 --> 109.92]  If there would be a person with similar accent on the input, then it would be fine.
[110.00 --> 111.30]  But it's kind of cheating.
[111.80 --> 116.82]  You can think it's cheating because we're reusing accent of a different person that's similar to your accent.
[116.82 --> 130.96]  But if it would be like an American native speaker or a person with a British accent or whatever other accent, then it will kind of be a mixture on the output.
[131.70 --> 135.06]  So we're not there yet in terms of converting accents.
[135.82 --> 144.52]  It's a little bit more difficult than we initially anticipated because when we started the company, we thought we'll kind of solve it in a year or something.
[144.52 --> 149.02]  But then it turned out, oh, no, we're here for much longer.
[150.44 --> 151.56]  Check these episodes out.
[151.72 --> 158.30]  Links are in the show notes to both episodes or head to heroku.com slash podcasts to listen and subscribe.
[158.92 --> 163.18]  Again, check the show notes for links or go to heroku.com slash podcasts.
[174.52 --> 184.08]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[184.54 --> 188.48]  This is where conversations around AI, machine learning, and data science happen.
[188.92 --> 193.52]  Join the community and Slack with us around various topics of the show at change.com slash community.
[193.72 --> 194.84]  And follow us on Twitter.
[194.98 --> 196.54]  We're at Practical AI FM.
[196.54 --> 206.36]  Welcome to another episode of Practical AI.
[206.80 --> 208.74]  This is Daniel Whitenack.
[208.90 --> 218.10]  I am a data scientist with SIL International, and I'm joined as always by my co-host, Chris Benson from Lockheed Martin.
[218.24 --> 219.04]  How are you doing, Chris?
[219.32 --> 220.50]  I am doing very well.
[220.62 --> 221.34]  Happy New Year.
[221.50 --> 222.26]  How are you doing today?
[222.70 --> 223.84]  Happy New Year.
[224.06 --> 225.08]  Doing well.
[225.08 --> 226.64]  Got some snow on the ground.
[226.78 --> 229.62]  It definitely looks like winter up here in the Midwest.
[229.96 --> 233.14]  And yeah, it was a good New Year.
[233.34 --> 236.78]  Helped my wife with a few things with her business over the holiday.
[237.12 --> 242.52]  And also, I ripped apart our bathroom in an attempt to remodel it.
[243.18 --> 245.92]  And I am mostly...
[245.92 --> 248.48]  So I'm on the rebuilding part of that.
[248.48 --> 256.54]  So it still has momentum, but it's not done yet to my wife's disappointment entering the new year.
[256.84 --> 257.64]  But it will be done.
[257.78 --> 258.26]  I'm committed.
[258.70 --> 259.42]  It sounds good.
[259.68 --> 259.96]  Yeah.
[260.12 --> 266.02]  As we kind of get back in the swing of things, today was my first day back into work after a little vacation time.
[266.02 --> 266.78]  Yeah, same here for me.
[266.78 --> 272.82]  So I'm trying to readjust my whole brain into actually having to be productive, which is a scary thing.
[272.98 --> 275.68]  It's absolute chaos coming back, right?
[276.18 --> 276.66]  It is.
[276.78 --> 277.80]  But I took advantage.
[277.90 --> 278.70]  I'll tell you real quick.
[278.76 --> 279.98]  I took advantage of the holidays.
[280.14 --> 281.64]  I've started flying lessons.
[282.32 --> 282.98]  No way.
[283.24 --> 283.62]  Yeah.
[283.62 --> 284.50]  That's super cool.
[284.50 --> 289.54]  And over the holidays, I got in about a dozen flight hours, getting close to solos.
[289.68 --> 290.68]  I'm sharing that with our audience.
[290.90 --> 293.72]  Now, if I don't finish this thing, everyone's going to hammer me.
[294.14 --> 296.46]  But hopefully, I'll eventually...
[296.46 --> 302.70]  Well, you'll be able to fly from Georgia up here to where I'm at, and we can do some in-person recording for the podcast.
[302.70 --> 303.08]  There we go. Perfect.
[303.40 --> 303.62]  Yeah.
[303.76 --> 304.08]  Exactly.
[304.10 --> 306.02]  You just come every Monday.
[306.46 --> 307.84]  But I think you scare me.
[307.84 --> 314.82]  Because, I mean, I'm in the sunny south where it's just a frigid 55 degrees Fahrenheit right now.
[314.92 --> 316.02]  You're all bundled up, too.
[316.18 --> 319.14]  You got your jacket hoodie on.
[319.32 --> 320.86]  I'm afraid to go north now.
[322.56 --> 324.04]  Well, with that...
[324.04 --> 325.08]  Make that transition, Daniel.
[325.08 --> 325.70]  Go for it.
[325.70 --> 329.58]  Yeah, we'll switch to something completely different, which I'm really excited about, actually.
[329.94 --> 335.40]  So there's a couple of things that got me really interested in this when we got connected with this group.
[335.40 --> 338.42]  One is that this is a sort of...
[338.42 --> 339.34]  It's a new thing.
[339.72 --> 344.92]  It's a non-profit thing, which is related to my world because I work for a non-profit.
[345.18 --> 355.70]  But there's a crossover with some of the things I'm working on because they're working with speech data and are releasing some data for speech-to-text and other things.
[355.70 --> 364.72]  But I'm really excited today because we are joined by David Cantor, who is the executive director at ML Commons.
[364.72 --> 365.64]  Welcome, David.
[366.06 --> 368.16]  Happy New Year, and it's a pleasure to be here.
[368.64 --> 369.00]  Yeah.
[369.18 --> 370.88]  Happy New Year to you as well.
[370.98 --> 374.86]  It's great to have you with us as our first official recording of the new year.
[375.04 --> 375.74]  First victim.
[376.10 --> 376.50]  Yeah.
[376.76 --> 377.06]  Sorry.
[377.28 --> 377.92]  It's not really.
[378.04 --> 378.54]  Just joking.
[379.58 --> 382.94]  No, it's actually great to be here, although it is kind of amusing.
[383.04 --> 388.12]  So I'm in San Francisco, and I think the weather is kind of very similar to that in Georgia.
[388.12 --> 400.98]  But, you know, I know we're the two wearing coats, and the gentleman surrounded by snow is like, no, I've got eating, full-blown t-shirt, like looking relaxed, like might even have sandals on.
[401.08 --> 401.48]  I don't know.
[402.04 --> 402.28]  Yeah.
[402.46 --> 403.38]  Well, yeah.
[403.40 --> 406.14]  I mean, with Zoom, you don't even know if I have pants on.
[406.50 --> 409.12]  But we'll leave that.
[409.12 --> 409.74]  We'll leave that.
[410.30 --> 412.20]  Maybe just assume there.
[412.30 --> 413.28]  He had to go there again.
[413.28 --> 415.34]  I'm interpolating you with pants on.
[415.44 --> 415.72]  Okay.
[415.72 --> 416.32]  That's good.
[416.54 --> 416.90]  That's good.
[416.94 --> 418.54]  That's probably a good interpolation.
[419.16 --> 427.94]  Anyway, would you just tell us a little bit about yourself, what you've done in the past, and how you ended up doing what you're doing now with ML Commons?
[428.42 --> 429.32]  Yeah, absolutely.
[429.32 --> 439.20]  So, you know, actually, I'd say in some ways my background in ML dates back to when I was in university at the University of Chicago, where I did math and economics.
[439.20 --> 445.84]  And, you know, a lot of econometric analysis is actually very similar to some forms of machine learning.
[446.06 --> 451.04]  But from there, I was very heavily involved in sort of computer architecture, microprocessor design.
[451.16 --> 452.84]  I had a startup for a few years.
[453.38 --> 466.90]  And then sort of when I shut that down, I ended up getting into a lot of consulting and ended up falling in with the predecessor to ML Commons, which was a collaborative benchmarking effort called ML Perf.
[466.90 --> 477.54]  And, you know, in a lot of ways, ML Perf brought together the community of machine learning and then sort of system architecture, computer engineering, and so forth.
[478.02 --> 492.20]  And then, you know, as you mentioned, we formed ML Commons, which is a nonprofit, a global engineering consortium to bring everyone together around our overall goals.
[492.20 --> 499.32]  And so, you know, I very much come from the technical side, again, on sort of the performance aspects.
[499.54 --> 509.48]  But over the last two to three years, I've really, really leveled up my understanding of machine learning quite considerably, both through my consulting and, you know, now my day job.
[510.06 --> 512.24]  Yeah. And ML Perf, I remember.
[512.48 --> 514.64]  So when did that come about?
[514.68 --> 516.78]  Because that's been around for some time, right?
[517.20 --> 518.70]  I remember seeing things about it.
[518.70 --> 524.10]  I want to say 2017 or 2018.
[524.82 --> 525.42]  Gotcha. Yeah.
[525.54 --> 531.16]  So actually, it's interesting that ML Perf was a sort of predecessor of ML Commons.
[531.38 --> 537.24]  And now ML Commons is sort of, it's like the parent organization is the way to put it of ML Perf.
[537.30 --> 540.58]  Was it the first, you know, thing inside the association?
[540.98 --> 541.30]  Yeah.
[541.62 --> 543.88]  It was the Linux inside the Linux Foundation?
[544.30 --> 546.10]  That is a very good way to put it.
[546.10 --> 555.66]  Yeah. And I mean, in many respects, you know what, the Genesis story is that, you know, our DNA is very much like a startup.
[555.78 --> 562.46]  And everything kind of started off very informal handshake agreements, do things with consensus and move very fast.
[562.46 --> 567.14]  But one of the things we agreed on is, you know, that will only work for so long.
[567.58 --> 579.96]  But we wanted to, you know, ultimately put this in the hands of, you know, an industry organization that was, you know, owned by none beholden to all, so to speak.
[579.96 --> 583.00]  And so ML Commons is that container.
[583.34 --> 588.76]  And but the other thing is, you know, we knew that this was one leg of the tripod, right?
[588.78 --> 592.08]  And that we had other projects that we wanted to get done.
[592.56 --> 597.90]  And so, you know, it was very much the camel's nose under the tent, so to speak.
[598.44 --> 599.36]  Yeah. Good metaphor.
[599.80 --> 600.00]  Yeah.
[600.88 --> 602.20]  That's actually a new one on me.
[602.32 --> 604.26]  I'm going to have to start using that one.
[604.26 --> 604.82]  Yeah.
[605.28 --> 621.58]  So before we go too far, just for those who have not heard of ML Perf, since we're kind of leading into the story with that, can you give a brief outline of what ML Perf was, and then kind of go on to talk about what the container is of ML Commons and how it's structured?
[622.02 --> 625.04]  And then maybe we'll get into some of the other things as well.
[625.52 --> 625.94]  Sure.
[625.94 --> 635.06]  So ML Perf is a set of performance benchmarks to measure how fast you can train a neural network or do inference.
[635.88 --> 642.42]  And, you know, there's a very long history of this sort of benchmarking in computer systems.
[642.42 --> 649.34]  And so in a lot of ways, like the effort was, you know, sort of spiritually influenced by those prior efforts.
[650.18 --> 660.62]  You know, organizations like SPAC and TPC that help to, you know, sort of bring together industry and academics and kind of give folks a common set of benchmarks.
[660.62 --> 672.24]  And what we really noticed early on is, you know, there's so much excitement around machine learning, around AI, but, you know, it was almost like the UN without their translation devices.
[672.24 --> 677.94]  And people would be talking about performance in ways that were very much not apples to apples.
[677.94 --> 688.86]  And so the sort of the goal of the benchmarking side of things is to both provide a common set of metrics for what constitutes progress, right?
[688.90 --> 691.42]  A benchmark in some sense is a barometer on progress.
[691.60 --> 693.98]  And, you know, does it always point true north?
[694.22 --> 695.34]  You know, not exactly.
[695.48 --> 698.20]  But if it's off by five or six degrees, it's fine.
[698.26 --> 699.68]  You're still heading in the right direction.
[699.68 --> 719.02]  But it's also about giving everyone a common language for where you are, in fact, heading, whether it's sales and marketing or engineering or academic research or even folks in the government and sort of clarifying the field and, you know, providing a map and a barometer in some sense.
[719.02 --> 725.76]  Yeah, it seems kind of interesting to me to think a lot about this side of benchmarking.
[725.76 --> 740.04]  So I think where a lot of people, if you were to talk to a lot of like AI practitioners or ML practitioners and talk to them about like performance or leaderboards or something like that, they probably immediately think of like, oh, some list of models.
[740.60 --> 750.62]  And they got like this accuracy on ImageNet or they got this blue score on this machine translation task or something like that.
[750.62 --> 759.66]  And it's really a measure of the output of the model, not of its performance on hardware.
[760.22 --> 766.92]  And actually, you kind of see as these leaderboards have been released, people put more and more effort in.
[767.04 --> 779.72]  And actually, the models at the very top might be very poorly performant on a lot of or maybe even like some lowly people like me might not be able to run them on any hardware that we own.
[779.72 --> 798.32]  So how has, you know, your conversations with people over time around ML perf and actual like performance on hardware overlapped or come into conflict with those other sort of conversations around like, oh, how accurate can we be and that sort of thing?
[798.32 --> 806.82]  Yeah, no, I mean, I think that's a very, very on point observation, right, which is that, you know, what you've described is what I think of as accuracy, right?
[806.86 --> 810.32]  And that's a very, you know, common set of benchmarks.
[810.32 --> 825.48]  And, you know, I think one of the actual sort of core motivations behind what we do is that there is actually a very foundational paper by one of our founders when he was at Baidu, Greg Deimos.
[825.48 --> 839.58]  And sort of the rough outline of the paper is that accuracy for ML follows a relatively simple equation, which is you get a lot of compute and a lot of data together.
[839.98 --> 844.92]  And as you crank those up, you will increase your accuracy, right?
[844.92 --> 853.98]  And you've seen these papers from OpenAI and other people talking about, oh, our need for compute is, you know, doubling every six months or something like that.
[854.18 --> 861.00]  And so, you know, I think the good thing is that there are absolutely folks who are very cognizant about the importance of this.
[861.20 --> 870.22]  But it's also true that there's, you know, a large number of people for whom, you know, the performance is sort of a level below them, right?
[870.22 --> 885.42]  And, you know, this goes back to, I think, sort of the goals of our organization, which is that when I look at machine learning today, it makes me think of what aeronautics was probably like around the turn of the 20th century, right?
[885.70 --> 887.08]  You're speaking my language now.
[887.40 --> 887.66]  Yeah.
[887.78 --> 897.04]  You know, you had dozens of people working on planes from the Wright brothers to the folks in France who I can't remember their name, but it's all sort of custom and hand done.
[897.04 --> 905.74]  And, but then you look at where we are today when you hop in a 787 and that is, you know, the process to make it, the output, just totally different.
[905.96 --> 916.72]  And to pivot to sort of the second part of your question about, you know, ML Commons, you know, our goal is advancing innovation in machine learning to drive the whole industry forward.
[916.72 --> 929.82]  And so I, when I think about where we are today, there are a lot of digitally native companies that have tremendous AI capabilities, but then you look at how do we reach the rest of the world?
[930.28 --> 933.04]  How do we reach analog companies?
[933.44 --> 941.36]  You know, like someone like Goodyear, for example, or Macy's, you know, as opposed to Amazon, where I think of digitally native shopping.
[941.36 --> 946.60]  And so, you know, in order for that to happen, it can't be these handcrafted things.
[946.72 --> 950.04]  So you need a lot of standard components.
[950.16 --> 952.02]  And, you know, we have the beginnings of that.
[952.12 --> 956.16]  We have things like TensorFlow and PyTorch to help us along the way.
[956.30 --> 961.34]  But, you know, there's a well-proven recipe for industry growth.
[961.34 --> 970.86]  And so ML Commons is really built to address sort of three key things that we see there, right?
[970.88 --> 975.32]  And one are these performance benchmarks and generally speaking metrics, right?
[975.40 --> 986.16]  And, you know, if you think about the Industrial Revolution, you know, you want to make a precision airplane, you know, if you confuse your meters with inches, you end up with things like crashing the Mars Lanter, right?
[986.94 --> 989.08]  So, you know, we've got to get the measurement down.
[989.08 --> 991.76]  Then we need our sort of raw materials.
[992.38 --> 1001.70]  And, you know, you've had folks on the show before, like our colleagues at Mozilla and Unsplash, or you referenced ImageNet, right?
[1001.74 --> 1007.54]  And this is the raw ingredient to AI and ML, right, which is data sets.
[1007.72 --> 1012.68]  And, in fact, you know, I think in there, we're very much influenced by ImageNet, right?
[1012.68 --> 1018.94]  And they provided the resource that catalyzed this latest sort of revolution in machine learning, right?
[1019.08 --> 1023.52]  So AlexNet and convolutional nets beat humans at image classification.
[1023.94 --> 1027.86]  And sort of the rest is, you know, an adventure we're living out.
[1028.02 --> 1033.06]  And then sort of the third pillar of ML Commons is what I call best practices, right?
[1033.10 --> 1036.26]  Which is, you know, how do we ensure model portability?
[1036.26 --> 1039.76]  How do we get from where we are today?
[1039.84 --> 1047.20]  Which is, you know, if you look at BERT, right, which is just, you know, profoundly changed how everyone thinks about NLP.
[1048.04 --> 1049.08]  It was a paper.
[1049.46 --> 1050.74]  And maybe you got some code.
[1050.74 --> 1064.32]  But it would take you probably a month to go from paper and code that works at Google on their internal infrastructure to, I could run this on the compute resources that I might have at Lockheed Martin.
[1064.32 --> 1080.42]  And so if we can shorten that time down to a day or hours to allow reproducibility of these models, to allow portability, that would be a tremendous boon to the whole industry.
[1080.42 --> 1098.16]  So it's sort of those are, I think, the three things that we see really driving the industry forward and helping to bring the benefits of machine learning, whether it's, you know, translation, speech recognition, you know, self-driving cars, medical diagnostics to the whole world.
[1110.42 --> 1116.94]  Have you heard about Knowable?
[1117.18 --> 1124.70]  It is an awesome new platform for learning from the world's best minds, anytime, anywhere, at your own pace, through audio.
[1125.24 --> 1134.50]  Learn about the performance benefits of a plant-based lifestyle from NBA all-star Chris Paul, or how to launch a startup from Reddit co-founder Alexis Ohanian.
[1134.90 --> 1138.16]  There's even a 10-lesson course from astronaut Scott Kelly.
[1138.60 --> 1139.32]  Here's a sneak peek.
[1140.42 --> 1144.96]  We learned a lot up there, but what can you learn from a life in space?
[1145.68 --> 1147.16]  The answers might surprise you.
[1147.88 --> 1152.26]  In this Knowable course, I want to share some of the things I've learned that you might not expect.
[1153.42 --> 1158.34]  Lessons about leadership on a dark night on an aircraft carrier in the middle of a churning sea.
[1159.32 --> 1164.42]  Lessons about the fear you feel with 7 million pounds of thrust exploding underneath you.
[1165.60 --> 1169.70]  And most of all, there's an idea out there that astronauts are always perfect.
[1169.70 --> 1172.10]  Failure is not an option, right?
[1172.86 --> 1178.04]  That's why I want to take you through some of my life experiences to show you how that's just not true.
[1178.96 --> 1187.64]  I believe everyday, regular, human failure, if we handle it right, can be one of our greatest opportunities to learn, grow, and succeed.
[1187.64 --> 1191.36]  Knowable is accessible on your phone and on the web.
[1191.36 --> 1196.20]  And each audio course is broken out into individual lessons, usually around 15 minutes long.
[1196.20 --> 1201.16]  As a Changelog listener, you can get an annual membership to Knowable for 20% off.
[1201.54 --> 1205.10]  Get unlimited access to every Knowable audio course right now.
[1205.34 --> 1212.60]  Just download the Knowable app or visit knowable.fyi and use code CHANGELOG for that 20% discount.
[1212.98 --> 1215.68]  We put a link in your show notes for easy clickings.
[1215.88 --> 1220.58]  Check out Knowable today and start learning from hundreds of top experts from around the world.
[1220.58 --> 1223.84]  Once again, that's knowable.fyi, code CHANGELOG.
[1234.72 --> 1240.80]  So, David, I'm pretty curious about, I guess, the structure and origins of ML Commons
[1240.80 --> 1246.12]  in the sense that I'm kind of reading about this really exciting group of people that's joined together
[1246.12 --> 1253.54]  to help form ML Commons with initial founding board, including representatives from people like Alibaba
[1253.54 --> 1255.68]  and Facebook AI and Google Intel.
[1255.80 --> 1262.14]  But then you've got people involved, researchers from academia and even, you know, startups.
[1262.78 --> 1269.12]  So could you kind of describe a little bit of the origin story, I guess, of how this organization
[1269.12 --> 1271.88]  came to be and, you know, what was it like?
[1271.92 --> 1278.74]  Was it like these, you know, people from all of these different companies on a Zoom call
[1278.74 --> 1283.06]  and just saying, hey, this thing needs to exist, you know, remember that MLPerf thing?
[1283.26 --> 1285.86]  Maybe we need to, like, create this other thing.
[1285.96 --> 1293.10]  Or has it been sort of forming and, you know, is it rooted in kind of deeper things like MLPerf
[1293.10 --> 1293.82]  and that sort of thing?
[1293.82 --> 1300.88]  Yeah, so it really was, I think, you know, one of the things you tapped into is, you know,
[1300.96 --> 1303.86]  bringing people together and forming a really dynamic community.
[1304.90 --> 1308.46]  And, you know, MLPerf, you know, really grew organically.
[1308.46 --> 1312.72]  And it did start, and I'd say, you know, of our founders, Peter Mattson from Google,
[1312.84 --> 1316.92]  who's the president and probably talked to him almost every day, even when we're on vacation,
[1317.44 --> 1319.40]  you know, really kind of dreamed it up.
[1319.40 --> 1325.08]  And we got started with probably an equal mix of academics and industry folks like,
[1325.40 --> 1328.00]  you know, the folks you mentioned, NVIDIA, et cetera.
[1328.72 --> 1333.58]  And that was sort of the, you know, I think we had 70 or 80 companies with representatives
[1333.58 --> 1334.94]  involved in MLPerf.
[1335.44 --> 1342.22]  And, you know, sort of at the tail, the start of last year, we kind of got started on forming
[1342.22 --> 1345.42]  a nonprofit that would become ML Commons.
[1345.42 --> 1350.10]  And then actually in December is when we sort of formally launched.
[1350.34 --> 1354.14]  And so, you know, a lot of these companies, a lot of these researchers, you know, became
[1354.14 --> 1355.24]  sort of official members.
[1355.92 --> 1358.06]  And, you know, that is what got us started.
[1358.20 --> 1363.74]  But I think it was the excitement around the benchmarks and just having industry standard
[1363.74 --> 1368.36]  benchmarks and establishing a reputation for, you know, we're doing things that are fair
[1368.36 --> 1369.30]  to everyone, right?
[1369.54 --> 1373.14]  Startups, you know, respective of what country they're in and useful.
[1373.14 --> 1378.24]  And seeing that, yeah, this is a community that people can trust and work with.
[1378.74 --> 1382.60]  So as you talk about the community, one of the things I'm wondering is there are these
[1382.60 --> 1386.02]  other communities like, you know, Google has built a community around TensorFlow.
[1386.72 --> 1391.32]  NVIDIA has built a community around their hardware platform and the software that supports
[1391.32 --> 1391.58]  it.
[1391.78 --> 1393.34]  There's the PyTorch community.
[1393.34 --> 1399.46]  And as you've built out the ML Commons community, how do you go about, you know, interfacing with
[1399.46 --> 1403.44]  those other communities and the ecosystems that those communities have built?
[1403.50 --> 1409.38]  Because you essentially have multiple ecosystems that are all trying to work together for that
[1409.38 --> 1410.14]  total solution.
[1410.28 --> 1412.12]  So how does that look from your perspective?
[1413.00 --> 1413.16]  Yeah.
[1413.24 --> 1419.16]  So actually, I mean, one of the things that we're, you know, very blessed by is that, you
[1419.16 --> 1424.04]  know, a lot of the folks who are pioneering key pieces of infrastructure in ML are members.
[1424.44 --> 1429.64]  So, you know, TensorFlow and PyTorch, you know, we have representatives from Facebook and from
[1429.64 --> 1429.90]  Google.
[1430.14 --> 1434.54]  So, you know, when we run into something or have a question, you know, sometimes we're
[1434.54 --> 1437.10]  lucky enough to get the right people there in the call to start with.
[1437.28 --> 1440.32]  But, you know, it's pre-COVID days, a tap of the shoulder away.
[1440.50 --> 1445.30]  And, you know, now probably an instant message or Slack or Facebook message away.
[1445.30 --> 1448.58]  So I think that has actually been a tremendous strength of ours.
[1448.80 --> 1453.64]  But, you know, a lot of these communities are, you know, almost orthogonal to what we
[1453.64 --> 1453.78]  do.
[1453.86 --> 1457.12]  I mean, like, you know, our benchmarks, for example, are full system, right?
[1457.12 --> 1463.30]  So it incorporates software, systems, cloud, hardware, you know, compilers, sort of everything.
[1463.90 --> 1468.78]  But, you know, we do very much, you know, we're a global and open standard, right?
[1468.78 --> 1473.28]  And in some sense, you really have to be as a benchmarking organization because there's this
[1473.28 --> 1477.06]  intrinsic judging quality to it, right?
[1477.32 --> 1482.32]  And, you know, just as it's in the judicial system in the United States, right, you know,
[1482.38 --> 1487.56]  the judging organization, so to speak, must be above reproach, must be open and equal to
[1487.56 --> 1488.44]  all, right?
[1488.48 --> 1489.92]  And that is very much our goal.
[1490.06 --> 1493.42]  So, you know, it's not that they're members per se, but, you know, we want to work with
[1493.42 --> 1494.26]  everyone, right?
[1494.32 --> 1495.96]  We're all fellow travelers.
[1496.44 --> 1497.18]  Good way to put it.
[1497.22 --> 1498.44]  I like that a lot.
[1498.86 --> 1501.40]  So we've talked a lot about MLPerf.
[1501.40 --> 1505.38]  Maybe we could dive into a couple of these other pillars that you mentioned.
[1505.78 --> 1507.28]  You mentioned data sets.
[1507.54 --> 1509.54]  I'm looking at your website now.
[1509.66 --> 1515.06]  You talk about data sets and models publicly available and can form the foundation of new
[1515.06 --> 1515.68]  capabilities.
[1516.42 --> 1522.02]  And specifically, I see you mentioned the speech data set, the world's largest public speech
[1522.02 --> 1525.90]  to text data set, which is maybe your first foray into this.
[1525.90 --> 1531.66]  So could you maybe describe your vision in the longer term for this data sets component
[1531.66 --> 1535.90]  of ML Commons and then how you got started with this speech data set?
[1536.20 --> 1536.80]  Yeah, absolutely.
[1537.08 --> 1541.56]  So I think, you know, you've sort of hit the nail on the head, which is that, you know,
[1541.56 --> 1548.80]  we want to be providing and drive the industry forward with these data sets.
[1548.92 --> 1553.20]  You know, I think of our speech project as image net for speech in shorthand, right?
[1553.20 --> 1555.86]  That's sort of like the 30-second pitch to someone in ML.
[1556.56 --> 1562.98]  And, you know, as I look out, there's a lot of other areas that could use this sort of
[1562.98 --> 1563.72]  public data set.
[1563.78 --> 1568.24]  Now, my colleague, Vijay Reddy, who's a professor at Harvard, he did a study with his graduate
[1568.24 --> 1568.56]  students.
[1568.60 --> 1573.88]  And one of the things he found is that even at companies that have huge amounts of internal
[1573.88 --> 1579.02]  data, like, you know, a Google or an Alibaba, most of their research studies are done with
[1579.02 --> 1584.88]  public data sets because that gives you a level playing field to assess accuracy, right?
[1585.50 --> 1587.60]  And you get reproducibility and all of these things.
[1587.90 --> 1594.34]  But we want to push forward with data sets in all these different areas because that will
[1594.34 --> 1598.86]  ultimately democratize access to this technology and thereby benefit everyone.
[1599.00 --> 1600.96]  So that's sort of the vision.
[1601.54 --> 1605.14]  And as you say, right, the people's speech is our first data set.
[1605.14 --> 1611.24]  And right now, we actually, late last year, sort of started sampling it to partners.
[1611.40 --> 1613.48]  So to our members that have speech teams.
[1613.84 --> 1617.40]  And, you know, if there's anyone out there with a speech team that's interested, you know,
[1617.50 --> 1620.96]  this is, I think it's about 10 years worth of audio.
[1621.32 --> 1622.08]  I'm raising my hand.
[1622.16 --> 1625.86]  No one can see that on Zoom, but I'll have to follow up afterwards.
[1625.86 --> 1626.72]  No, absolutely.
[1626.86 --> 1627.88]  We should totally talk.
[1628.92 --> 1630.24]  You know, and it's big.
[1630.30 --> 1631.54]  It's 10 terabytes of data.
[1631.54 --> 1635.76]  And actually, one of the pieces of feedback we got was, for many people, it's actually
[1635.76 --> 1636.50]  a little too big.
[1636.58 --> 1640.28]  So we need to, you know, slice it down into smaller chunks so that, you know, individuals
[1640.28 --> 1642.64]  can play with it or, you know, a university.
[1643.12 --> 1650.72]  But we're getting it out to field test because, again, the hypothesis here is this is, I think,
[1650.76 --> 1655.60]  about 30 or 40x bigger than anything that's publicly available today.
[1655.60 --> 1662.34]  And I think the key thing is, for speech-to-text models, you need about 10,000 hours to actually
[1662.34 --> 1663.58]  produce something that's functional.
[1663.98 --> 1670.06]  Now, I don't claim that this will give you a truly production-worthy model, but I think
[1670.06 --> 1673.00]  it can really lower the bar for a lot of people.
[1673.10 --> 1674.46]  And it's very exciting to me.
[1674.92 --> 1679.42]  You know, there's two folks in my life who actually really benefit from speech technology.
[1679.72 --> 1685.14]  You know, one is my mother, who she had a stroke a few years back and has difficulty reading.
[1685.60 --> 1689.66]  But she uses speech-to-text in her phone all the time.
[1690.32 --> 1692.62]  And so, you know, that's great.
[1692.72 --> 1693.58]  She speaks English.
[1694.18 --> 1697.16]  And both English and Mandarin have very robust systems.
[1697.36 --> 1701.92]  But it doesn't take long before you get to other very commonly spoken languages, like
[1701.92 --> 1705.10]  Portuguese, where there's really almost no public data.
[1705.18 --> 1707.70]  But that's a language that's spoken by 300 million people.
[1708.32 --> 1715.14]  You know, so if we can help push those frontiers out, you know, I would love to be able to extend
[1715.14 --> 1720.60]  and play a role in extending speech technology to sort of, you know, the next several billion
[1720.60 --> 1723.14]  people, you know, this decade.
[1723.90 --> 1725.24]  So I'm kind of interested.
[1725.44 --> 1729.38]  I know, as I was kind of indicating while you were talking, I'm very interested in this
[1729.38 --> 1732.80]  because we have our own speech projects going on in our organization.
[1732.80 --> 1740.48]  And we're, you know, as our organization's mission is to extend, you know, benefits of
[1740.48 --> 1744.08]  these types of technologies and other things to local language communities.
[1744.08 --> 1745.20]  I'm super interested.
[1745.80 --> 1750.60]  But I know from experience, this is a lot of work putting these data sets together.
[1750.60 --> 1760.54]  So how does a sort of collaborative nonprofit, which is sort of, I imagine, kind of amorphous
[1760.54 --> 1766.70]  and changing a lot, you know, how do you like put the right pieces in place to make sure
[1766.70 --> 1769.56]  that this can be accomplished at this scale?
[1770.08 --> 1770.28]  Yeah.
[1770.46 --> 1774.30]  Well, so the good news is we are more official than three raccoons in a trench coat.
[1774.42 --> 1774.96]  Good, good.
[1775.08 --> 1775.86]  I like that.
[1776.00 --> 1777.00]  I like that's a good one.
[1777.00 --> 1780.96]  Yeah, I don't know if you guys have seen BoJack Horseman, but there's a great character,
[1781.26 --> 1786.20]  Vincent Adultman, who is a take on that, who is literally three children inside a trench
[1786.20 --> 1789.50]  coat, who goes to work and does a business.
[1789.90 --> 1791.46]  You know, that's sort of my prototype.
[1791.62 --> 1792.18]  Yeah, yeah.
[1792.56 --> 1797.52]  And I know, like, for example, our nonprofit, there's a lot of like, you form a lot of
[1797.52 --> 1798.00]  partnerships.
[1798.22 --> 1802.92]  And at some point, it's like, you know, it gets a little bit hard of like, where does
[1802.92 --> 1808.34]  like this entity end and this one start in terms of like what they're doing?
[1808.34 --> 1812.36]  And like, these people are with this organization, but they're working on that.
[1812.36 --> 1818.06]  Like, you know, maybe there's people in Facebook or Google, but they're working with and on ML
[1818.06 --> 1820.20]  Commons projects.
[1820.46 --> 1821.66]  You know, how does that play out?
[1821.70 --> 1826.04]  And how do you staff up to, you know, do this data set work?
[1826.66 --> 1826.86]  Yeah.
[1826.96 --> 1831.44]  So I think, you know, that kind of dives into, you know, some of what our organization
[1831.44 --> 1832.36]  provides, right?
[1832.40 --> 1836.88]  Which is, so we do have a budget and we do use some of that for staff, you know, hire
[1836.88 --> 1838.60]  consultants and folks to help us out.
[1838.76 --> 1843.88]  We have a core of like very dedicated folks who are, you know, incredibly interested and
[1843.88 --> 1844.78]  focused on speech.
[1844.78 --> 1849.68]  And, you know, a lot of those folks have kind of gravitated towards us, you know, and
[1849.68 --> 1852.14]  collaborating with others is absolutely part of this.
[1852.14 --> 1858.34]  But I do see some of the benefits that we have is that, you know, through the community
[1858.34 --> 1861.98]  that is ML Commons, we have access to tremendous, you know, compute resources, right?
[1862.04 --> 1868.16]  So, you know, if we want to start training a model on this 87,000 hours of speech, which
[1868.16 --> 1874.00]  we do, you know, we can go to some of the world's top cloud providers and, you know, work
[1874.00 --> 1878.70]  with them to take advantage of the resources that they have and collaborate together.
[1878.70 --> 1884.16]  But, you know, it is true that as a volunteer project, one of the biggest challenges is,
[1884.38 --> 1885.28]  you know, sort of turnover.
[1885.62 --> 1887.36]  And this is true in graduate schools as well.
[1887.40 --> 1891.58]  And actually, this is one of the things that I think is sort of a lesson from ImageNet
[1891.58 --> 1896.54]  that, you know, we're trying to build on and improve, which is the ImageNet folks did something
[1896.54 --> 1898.14]  amazing on a very tight budget.
[1898.54 --> 1900.20]  And we want to reproduce that.
[1900.42 --> 1905.74]  But we also think that sort of the techniques that go into these, building these data sets
[1905.74 --> 1911.84]  are durable and that by putting a lot of this expertise within an organization, we can drive
[1911.84 --> 1914.36]  down the cost over time, right?
[1914.66 --> 1919.40]  Because there's all sorts of tricks of the trade that, you know, are very much embodied
[1919.40 --> 1921.64]  in people and may not get written down.
[1921.74 --> 1925.30]  And so when you have people, you know, rotating in and out, you kind of lose that.
[1925.50 --> 1929.74]  But by having an organization behind that where it's all written down and, you know, we have
[1929.74 --> 1934.84]  some continuity, you know, folks like myself and other leads, you know, I think there is a
[1934.84 --> 1941.10]  great opportunity to really build up, you know, momentum that is beyond a single project.
[1947.40 --> 1952.70]  ChangeLog++ is the best way for you to directly support practical AI.
[1953.22 --> 1958.94]  Join today and unlock access to a private feed that makes the ads disappear, gets you closer
[1958.94 --> 1963.60]  to the metal and help sustain our production of practical AI into the future.
[1963.60 --> 1970.36]  Simply follow the ChangeLog++ link in your show notes or point your favorite web browser
[1970.36 --> 1972.68]  to ChangeLog.com slash plus plus.
[1973.00 --> 1976.86]  Once again, that's ChangeLog.com slash plus plus.
[1978.16 --> 1980.62]  ChangeLog++ is better.
[1993.60 --> 2002.32]  So David, I'm kind of curious.
[2002.32 --> 2008.52]  I know that one of the pillars that you have that is around best practices is called ML-Cube.
[2008.72 --> 2013.06]  I'm wondering if you could start us off by describing what that is, what its conventions
[2013.06 --> 2016.68]  are and such and kind of give us a quick intro to that.
[2016.68 --> 2019.58]  Yeah, so that is a great question.
[2019.98 --> 2027.56]  ML-Cube is really, I think of it as a set of conventions around ML models.
[2028.06 --> 2033.26]  And it's sort of, it's distinct from containerization, right?
[2033.34 --> 2037.48]  You know, obviously many folks are going to be familiar with Docker and so forth.
[2037.48 --> 2045.04]  But, you know, you can't take a Docker from inside Google containing BERT and expect that
[2045.04 --> 2052.36]  to run out of the box on AWS or, you know, systems that don't allow for containerization,
[2052.48 --> 2052.64]  right?
[2052.68 --> 2058.20]  So some of the organizations that we work with are supercomputer sites and some of those
[2058.20 --> 2062.08]  are classified supercomputers or portions of their infrastructure classified.
[2062.20 --> 2064.94]  And they have all sorts of rules about what can and cannot work.
[2065.10 --> 2065.80]  They do indeed.
[2065.80 --> 2066.62]  Yeah, right.
[2066.82 --> 2069.96]  I'm sure this is like, you know, every day for you, right?
[2070.48 --> 2077.52]  So how can we get a set of conventions in the way that will help you move models around
[2077.52 --> 2081.86]  transparently so you can pick it up from one set of infrastructure to another and just,
[2082.22 --> 2083.66]  you know, be up and running?
[2083.80 --> 2087.34]  And, you know, it might not give you the best performance, but it will actually run and
[2087.34 --> 2088.48]  allow you to reproduce things.
[2088.54 --> 2091.26]  And so that's kind of the goal of ML-Cube.
[2091.32 --> 2095.48]  And we're getting, you know, we're always very interested in volunteers, folks to use it.
[2095.80 --> 2101.56]  Because ultimately what I would love to see is, you know, a lot of these very common models
[2101.56 --> 2108.68]  that people use as references, whether it's ResNet or BERT, to be packaged up in ML-Cube.
[2109.08 --> 2114.40]  And so that, you know, you can trust that when you grab something from the model zoo, you know,
[2114.40 --> 2116.16]  it's just going to run wherever you are.
[2116.24 --> 2121.68]  And, you know, you don't have to fight tooth and nail with whatever the underlying infrastructure
[2121.68 --> 2122.24]  is.
[2122.30 --> 2125.76]  And I think that would just make everyone's life, you know, a lot easier.
[2125.76 --> 2127.56]  Yeah, I definitely agree.
[2127.74 --> 2134.44]  Speaking after some interesting experiences, even this last week, trying to get a number
[2134.44 --> 2137.88]  of random models to run locally.
[2138.60 --> 2139.26]  It's difficult.
[2139.54 --> 2145.70]  And people are eager because they see these, like, really awesome things coming out in research
[2145.70 --> 2146.20]  papers.
[2146.20 --> 2148.98]  And, oh, this happened in Google or this happened in OpenAI.
[2149.50 --> 2152.90]  And it seemed, you know, almost instantly it's up on GitHub.
[2153.24 --> 2159.58]  But then, like, actually running it and doing something useful with it is a whole nother game.
[2159.58 --> 2166.82]  So in terms of, like, let's say I'm an AI practitioner and, you know, you mentioned sort of model zoo
[2166.82 --> 2170.64]  and sort of portable models.
[2170.82 --> 2178.46]  What are you envisioning with ML-Cube my workflow would be if I was either contributing some model
[2178.46 --> 2182.64]  to ML-Cube or some method and also on the other side?
[2182.82 --> 2186.80]  So, you know, being a consumer of that and integrating it into my own work.
[2187.32 --> 2188.94]  Yeah, no, I mean, that is a perfect question.
[2188.94 --> 2193.06]  Actually, this is one of the things that, you know, it makes me very glad that we had
[2193.06 --> 2197.84]  certain deliverables in our launch, which was the ML-Cube team put together a great tutorial
[2197.84 --> 2200.96]  on how to publish a model and package it up with ML-Cube.
[2201.64 --> 2204.44]  And so I think we have a couple of examples up already.
[2204.78 --> 2209.64]  And, like, I would, you know, the beautiful future I'd love to see is where, you know,
[2210.26 --> 2214.36]  it's so low friction that everyone who's publishing research papers does it, right?
[2214.36 --> 2218.96]  And then, you know, the interaction with ML-Perf is, you know, we have a bunch of models that
[2218.96 --> 2220.10]  we use to measure performance.
[2220.42 --> 2223.50]  And those run on, like, a huge variety of hardware.
[2223.70 --> 2227.50]  So this is something that is in our own interest as well, right?
[2227.56 --> 2230.90]  And seeing cloud providers, you know, package things up.
[2231.02 --> 2235.88]  So seeing more people package things up would be great, in part because I think a lot of what
[2235.88 --> 2242.38]  this does is creates huge convenience on the consumer side, as you point out, right?
[2242.44 --> 2248.76]  So that, you know, you can grab things and just get them up and running a lot more quickly.
[2248.76 --> 2254.32]  Now, I think especially for research and experimentation, this is tremendously powerful.
[2254.80 --> 2257.88]  Because, you know, if you're doing things in production, you're going to really, really
[2257.88 --> 2259.28]  need to crank out optimizations.
[2259.46 --> 2264.52]  But I think even in production, this is actually potentially very powerful if you think about,
[2264.52 --> 2270.06]  you know, sort of a scenario where you have a model that you sort of centrally developed,
[2270.20 --> 2274.86]  but then you need to, like, maybe tailor a little bit for hundreds of different sites,
[2275.16 --> 2276.18]  right?
[2276.24 --> 2279.92]  And so this could be a convenient form to pass that model around in.
[2280.00 --> 2284.36]  And so, you know, we have some tutorials on how to, you know, the sort of Hello World
[2284.36 --> 2284.84]  equivalent.
[2285.40 --> 2290.52]  And I think we might have one with MNIST and then one with some other sort of more classic
[2290.52 --> 2292.90]  ML stuff, potentially BERT.
[2292.90 --> 2297.32]  I'd have to check my notes to see for, you know, here's how you publish and then here's
[2297.32 --> 2298.06]  how you consume.
[2298.50 --> 2304.50]  But again, it's really about how do we remove all of these sources of friction from the folks
[2304.50 --> 2307.16]  who are going to drive the industry forward and cutting edge research.
[2307.56 --> 2311.88]  Does most of that happen inside the working groups that you have or are there working groups
[2311.88 --> 2312.62]  for some things?
[2312.74 --> 2318.26]  And then you, you know, how do you divide out the productivity of what's coming out of the
[2318.26 --> 2319.44]  whole process end to end?
[2319.44 --> 2322.14]  Yeah, no, I mean, you, you, you totally nailed it.
[2322.26 --> 2327.48]  We, you know, DNA wise, I think we're, we have a lot in common with open source organizations,
[2327.48 --> 2331.16]  like, you know, in terms of principles, like by default, everything is open.
[2331.32 --> 2331.84]  It's on GitHub.
[2332.36 --> 2336.60]  You know, we have working group meetings, you know, usually once a week.
[2336.60 --> 2343.24]  And then we used to have, I mean, when we started, it was monthly physical meetings in the Bay
[2343.24 --> 2345.50]  Area and then quarterly.
[2345.90 --> 2349.66]  And I think one of the things that I'm very much looking forward to is, you know, we are
[2349.66 --> 2350.96]  an international organization.
[2351.24 --> 2355.50]  And one of my goals for 2020 was to start having some sort of regular meetings in Europe
[2355.50 --> 2356.16]  and in Asia.
[2356.16 --> 2360.36]  And obviously that, that that's on the agenda for the second half of this year.
[2361.08 --> 2363.40]  Some unexpected things came up along the way.
[2363.40 --> 2366.48]  Yeah, no idea.
[2368.00 --> 2372.74]  Hopefully this is not too, too bold of a question, but I think people might find it interesting
[2372.74 --> 2377.36]  because they see certain organizations like Chris mentioned, you know, Linux Foundation
[2377.36 --> 2380.40]  or maybe a cloud native or whatever it is.
[2380.82 --> 2383.54]  So you mentioned you had a budget, you had staff.
[2383.54 --> 2390.06]  Do the companies that are sort of subscribing and contributing and are part of the organization,
[2390.06 --> 2392.92]  are they contributing financially to make it happen?
[2393.08 --> 2395.46]  Is that how it happens, you know, practically?
[2396.30 --> 2397.80]  It's exactly like NPR.
[2397.96 --> 2399.46]  We have some fantastic mugs.
[2400.14 --> 2401.10]  Yeah, I bet so.
[2401.32 --> 2402.78]  Although it's actually jackets.
[2402.94 --> 2407.36]  You can't see it because this is a podcast, but I am wearing one with the ML Perflo.
[2407.60 --> 2407.96]  Oh, yeah.
[2408.04 --> 2408.64]  I see there.
[2408.66 --> 2411.46]  Chris and I can vouch for the style.
[2411.46 --> 2413.76]  Yeah, right.
[2413.76 --> 2418.48]  So the membership is open to individuals and academics, and that is free.
[2419.08 --> 2422.12]  But for companies, it is a paid membership.
[2422.56 --> 2426.70]  Now, you know, I think when we started out, actually one of the questions we asked ourselves
[2426.70 --> 2429.16]  was, do we really need to create another organization?
[2429.90 --> 2434.24]  And one of the things that we actually, we clearly came to the conclusion of yes.
[2434.24 --> 2441.10]  And I think the motivator behind that is that we are, there are a lot of engineering organizations
[2441.10 --> 2445.74]  that exist, you know, Linux Foundation, Open Compute, but none of them are actually focused
[2445.74 --> 2446.20]  on AI.
[2446.60 --> 2451.44]  And then there are a lot of AI organizations, you know, like the Partnership on AI and so
[2451.44 --> 2456.78]  forth, but none of them are actually focused on collective engineering, right?
[2456.78 --> 2462.42]  And so that's kind of the sweet spot that we want to focus on and do.
[2462.54 --> 2467.80]  And, you know, you have marketing focused organizations, and we'll leave that to them.
[2468.04 --> 2469.94]  You have policy focused organizations.
[2469.94 --> 2474.12]  And again, that's a very complicated area.
[2474.40 --> 2476.70]  And we really want to focus on building things.
[2476.76 --> 2478.04]  That's kind of what's in our DNA.
[2478.40 --> 2479.66]  I have a quick follow up to that.
[2479.66 --> 2485.34]  Over time and across many episodes, Daniel and I have chit-chatted around the fact that
[2485.34 --> 2492.62]  as AI really matures, and it's really along the longer path merging with software development
[2492.62 --> 2497.42]  as there's a set of tools that are becoming available, and they're becoming easier over
[2497.42 --> 2499.70]  time and standardized over time.
[2500.14 --> 2503.40]  So how do you see your future with these?
[2503.74 --> 2509.02]  Obviously, you're kind of in your sweet spot, but your sweet spot as it merges over time closer
[2509.02 --> 2511.82]  to other sweet spots that other organizations are filling.
[2512.30 --> 2517.26]  How does that change the nature of where you all are operating, not just your own organization,
[2517.54 --> 2519.10]  but the others that you're working with?
[2519.14 --> 2522.10]  Do you have any sense of that, you know, five years out, 10 years out?
[2522.58 --> 2523.76]  Ooh, that's a really good question.
[2523.76 --> 2525.32]  Or did I just throw a complete random?
[2525.66 --> 2526.60]  No, no, no, no, no.
[2526.96 --> 2533.70]  So I think, you know, realistically, the benchmarking and the metrics, you know, probably stay the
[2533.70 --> 2533.92]  same.
[2533.94 --> 2535.46]  And that value is very independent.
[2535.46 --> 2540.06]  I think that, again, the dataset creation is very unique to ML, right?
[2540.26 --> 2543.62]  Because there's a lot of things where when it comes to benchmarking and other stuff, you
[2543.62 --> 2545.66]  can fake the dataset, and that's commonly done.
[2545.86 --> 2550.30]  But like, you know, by definition, that does not work in ML, right?
[2550.38 --> 2555.64]  And so I only see the need for building datasets growing over time as ML pervades more and more
[2555.64 --> 2556.28]  things, right?
[2556.40 --> 2557.84]  That's a totally fair answer, yeah.
[2557.84 --> 2562.36]  And on the best practices, you know, I mean, in some sense, like, let's take this to the
[2562.36 --> 2563.28]  limit, right?
[2563.80 --> 2570.28]  Maybe one day, you know, ML will be as pedestrian as Excel is.
[2570.90 --> 2577.54]  And at that point, you know, the best practices will, you know, will have done its job.
[2577.64 --> 2581.68]  I mean, but, you know, it'll be decades before we ever get there, right?
[2581.78 --> 2581.98]  Yeah.
[2581.98 --> 2587.56]  And also, I think, to the extent that I think of best practices, I think of it as how do
[2587.56 --> 2588.54]  we remove frictions?
[2589.42 --> 2592.00]  There will always be new things popping up, right?
[2592.08 --> 2598.52]  Today, you know, model portability is probably, and interoperability is probably number one,
[2598.58 --> 2599.66]  as we've said.
[2599.80 --> 2604.34]  But, you know, I think there's a very long list, and as we go along, we'll find more
[2604.34 --> 2607.00]  friction that we want to help remove.
[2607.00 --> 2611.90]  Until we get to the saying, right, you know, the demo that is truly indistinguishable from
[2611.90 --> 2612.68]  magic, right?
[2613.62 --> 2621.34]  So how do you, with this sort of very collaborative group and so many parties involved, do you
[2621.34 --> 2626.18]  know sort of right now, like I'm just thinking of data sets, how do you choose what's the
[2626.18 --> 2630.80]  next data set, you know, that you're going to focus on and what area it is and that sort
[2630.80 --> 2631.18]  of thing?
[2631.18 --> 2635.72]  Is that driven out of sort of feedback from the community?
[2635.72 --> 2640.94]  Or is there a kind of roadmap from the board or like a combination of the two?
[2641.08 --> 2642.04]  How's that work?
[2642.64 --> 2643.66]  No, that's a very good question.
[2643.74 --> 2647.98]  So I think it is very much driven by, you know, sort of the member community and the
[2647.98 --> 2653.62]  board and right, and that is, you know, one of the keys to any effort like this is, you
[2653.62 --> 2657.64]  know, we don't really want to be taking money away from our member companies, but we obviously
[2657.64 --> 2661.24]  have to keep the lights on and do, you know, there's a lot of functions that we are providing.
[2661.24 --> 2665.94]  And so, but part of the value of being a member is helping to drive that forward.
[2666.06 --> 2670.92]  And so there are, you know, other things that we've identified as being sort of opportunities,
[2671.26 --> 2673.26]  you know, in terms of data sets.
[2673.62 --> 2676.72]  And that is sort of a board decision.
[2677.10 --> 2681.54]  But, you know, the way the board works is, you know, this is not like a Roman emperor,
[2681.74 --> 2682.04]  right?
[2682.08 --> 2684.54]  This is actually genuinely community driven.
[2684.66 --> 2685.68]  We listen to our members.
[2685.68 --> 2689.00]  And then, you know, there's also a bit of vision involved, right?
[2689.20 --> 2693.26]  And that, you know, vision is not you just listen to everyone and do what they say.
[2693.32 --> 2696.86]  It's, you know, you have to start with an end in mind, right?
[2697.14 --> 2701.90]  And, you know, by nature, a community will, you know, generally pull you to where their
[2701.90 --> 2702.82]  focus is.
[2702.88 --> 2706.18]  But, you know, one of the, some of the things that we happen to think are very important
[2706.18 --> 2709.30]  are things like AI and medicine, right?
[2709.30 --> 2715.98]  You know, that's clearly huge potential for impact on the whole world, you know, self-driving
[2715.98 --> 2718.02]  vehicles, you know, another one, right?
[2718.10 --> 2721.34]  Tens of thousands of people are killed or injured in automobile accidents.
[2721.34 --> 2726.22]  And if we could cut that down by an order of magnitude, that would just be, you know,
[2726.26 --> 2727.66]  a huge benefit to society.
[2727.80 --> 2732.42]  So, you know, it's kind of a combination and there's a bit of art to it because it does
[2732.42 --> 2734.24]  draw on sort of all three of those things, right?
[2734.70 --> 2739.28]  Broader community interest, what the board thinks, and then a bit of vision in terms of
[2739.30 --> 2744.32]  where researchers and academics and folks really, really, really on the cutting edge
[2744.32 --> 2745.86]  think there is opportunity.
[2746.50 --> 2750.74]  So you've actually just totally transitioned me into my next question because you were
[2750.74 --> 2751.86]  starting to get into vision.
[2752.40 --> 2756.92]  And so as we wind up here, I'd really be interested, you mentioned AI and medicine,
[2757.06 --> 2761.98]  you mentioned self-driving, but you personally, as you were helming the organization, you're
[2761.98 --> 2766.82]  creating all these relationships, you're engaged in the technology that's driving this forward
[2766.82 --> 2767.48]  in the algorithms.
[2768.22 --> 2771.02]  Just clean slate any kind of answer you want.
[2771.36 --> 2776.04]  What is your vision for where things are going over the next five years or longer, 10 years,
[2776.38 --> 2777.90]  whatever you feel comfortable with?
[2778.04 --> 2782.74]  You know, what's the thing that when you are going to bed at night and laying down and before
[2782.74 --> 2787.26]  you fall asleep is kind of getting you excited and thinking about at some point we're going
[2787.26 --> 2787.74]  to hit that?
[2787.74 --> 2796.74]  I mean, honestly, it's just really empowering new innovations that are going to benefit everyone
[2796.74 --> 2799.06]  built on ML and AI, right?
[2799.14 --> 2802.10]  And I think the speech to text is a great example, right?
[2802.10 --> 2807.32]  I can see, you know, a lot of our data is in English initially, but, you know, step two
[2807.32 --> 2813.36]  is how do we go from English to a dozen or a hundred or a thousand other languages, a thousand
[2813.36 --> 2814.70]  if we're being very bold, right?
[2814.70 --> 2818.82]  You know, and you can start thinking about how you might leverage transfer learning to
[2818.82 --> 2823.82]  get from a speech to text system that has a solid command of English to other languages,
[2824.06 --> 2824.58]  right?
[2824.70 --> 2829.18]  But, you know, again, medicine, my father's a physician, he's retired now, but, you know,
[2829.20 --> 2832.80]  I just see huge amounts of potential there.
[2833.28 --> 2839.80]  And, you know, will we necessarily be building the pioneering innovations, things like BERT that
[2839.80 --> 2841.44]  really do drive the whole industry forward?
[2841.52 --> 2843.86]  No, but we're going to be filling out the gaps around that.
[2843.86 --> 2849.74]  And so I think just knowing that our data sets are going to help catalyze things going
[2849.74 --> 2853.00]  forward, that we're going to make everything more efficient, like those are the things that
[2853.00 --> 2855.12]  are really exciting to me.
[2855.28 --> 2858.18]  And it's a tide that lifts all ships, right?
[2858.44 --> 2865.16]  You know, the name of the game is how do we build a better world in a bigger role for
[2865.16 --> 2865.42]  AI?
[2865.50 --> 2870.44]  Because ultimately then all of our members benefit and everyone across the world, right?
[2870.44 --> 2873.88]  So I think those are the things that really excite me.
[2873.96 --> 2877.84]  And, you know, five years from now, you know, maybe there are other pillars to our organization
[2877.84 --> 2878.96]  that kind of come up.
[2879.02 --> 2883.58]  And one of the things that we like having is we have a sort of a research group that allows
[2883.58 --> 2887.74]  for sort of more rapid development of these ideas so that, you know, things like the data
[2887.74 --> 2892.04]  sets we can sort of quickly iterate on until we figure out that, hey, okay, yeah, this is
[2892.04 --> 2892.68]  a good idea.
[2892.76 --> 2893.58]  This is mature now.
[2893.58 --> 2895.22]  Let's go push some real weight behind it.
[2895.22 --> 2897.62]  Or, you know, that idea wasn't quite ready.
[2897.82 --> 2901.36]  And, you know, there's a lot of ideas that, you know, are great, but it might not be the
[2901.36 --> 2902.12]  right time for them.
[2902.22 --> 2907.34]  So I think just, you know, the three things we've charted should really keep us good for
[2907.34 --> 2911.98]  the next five years, maybe even longer, but just the impact and then maybe some other
[2911.98 --> 2913.34]  new ideas as they come along.
[2913.64 --> 2915.00]  So that's for me, I think.
[2915.52 --> 2915.66]  Yeah.
[2915.66 --> 2922.52]  I think that's a very inspiring and good way to start out 2021, thinking about some
[2922.52 --> 2928.84]  of those ways in which AI can benefit those who it's not benefiting now.
[2929.02 --> 2933.08]  And as well, all of us who are in the industry can benefit as well.
[2933.18 --> 2938.18]  So I really appreciate your perspective on that and excited about the things that ML Commons
[2938.18 --> 2938.76]  is doing.
[2938.76 --> 2944.40]  And we will definitely link to a bunch of different things in our show notes, including
[2944.40 --> 2949.58]  ML Cube and the People's Speech Dataset and ML Perf and ML Commons in general.
[2949.80 --> 2952.30]  So definitely make sure and check those out.
[2952.64 --> 2956.06]  Check out what they're doing and get involved if you're able to.
[2956.44 --> 2957.82]  But thank you so much, David.
[2957.86 --> 2962.86]  I really appreciate you joining us today and recording with us at the very start of 2021.
[2963.62 --> 2964.50]  Yeah, it's been my pleasure.
[2964.62 --> 2967.00]  No, I thank you for taking the time to talk with me.
[2967.00 --> 2972.70]  And it's great, especially to connect to folks who are genuinely interested both on
[2972.70 --> 2977.60]  an intellectual level and on a sort of day-to-day level on the tasks and the mission that we're
[2977.60 --> 2978.38]  engaged in.
[2978.48 --> 2981.76]  I mean, yeah, there's a lot of exciting things going on in AI and ML.
[2982.28 --> 2987.20]  So maybe we can have a separate section where I get to ask you the questions and your thoughts
[2987.20 --> 2987.54]  on that.
[2987.86 --> 2988.74]  That sounds great.
[2988.88 --> 2990.54]  We'll definitely have to have a follow-up.
[2990.68 --> 2995.76]  I mean, with ML Commons being so embedded across the whole industry, I'm sure we'll be crossing
[2995.76 --> 2997.92]  paths and hope we can have another conversation.
[2998.38 --> 2998.76]  Absolutely.
[2999.40 --> 2999.86]  Thank you.
[2999.98 --> 3000.48]  Happy New Year.
[3001.14 --> 3003.66]  Happy New Year to you as well and everyone listening.
[3007.58 --> 3009.78]  Thank you for listening to Practical AI.
[3010.46 --> 3014.12]  If this is your first time, make sure you subscribe so you don't miss a thing.
[3014.12 --> 3021.48]  Head to practicalai.fm to subscribe or find us in Apple Podcasts, Spotify, or wherever you
[3021.48 --> 3022.30]  listen to podcasts.
[3023.16 --> 3027.24]  And if you get value from the show, please do share it with a friend or a colleague.
[3027.42 --> 3028.80]  We appreciate you spreading the word.
[3029.68 --> 3032.54]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[3033.04 --> 3036.64]  It's produced by Jared Santo, and our music is provided by Breakmaster Cylinder.
[3037.18 --> 3039.34]  We are brought to you by some awesome sponsors.
[3039.84 --> 3042.36]  Shout out to Fastly, Linode, and LaunchDarkly.
[3042.36 --> 3044.18]  That is our show.
[3044.70 --> 3049.22]  On the next episode, Daniel and Chris are joined by two fascinating folks from Area Bell to
[3049.22 --> 3053.42]  talk about, get this, their AI-enabled electronic nose.
[3053.90 --> 3056.26]  Stay tuned for that one coming at you next week.
