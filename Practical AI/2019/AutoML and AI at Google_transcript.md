[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.02]  And unlike standard droplets, which use shared virtual CPU threads,
[29.02 --> 32.86]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.40 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 --> 45.20]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.20 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.76 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.28]  And now onto the show.
[106.66 --> 108.92]  Welcome to Practical AI.
[109.38 --> 113.28]  I'm Daniel Whitenack, a data scientist with SIL International.
[113.70 --> 120.24]  And I'm here with my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[120.68 --> 121.40]  How are you doing, Chris?
[121.72 --> 122.26]  Doing great.
[122.32 --> 122.98]  How's it going, Daniel?
[123.36 --> 124.78]  It's going really good.
[124.78 --> 130.58]  I spent some vacation time doing a little bit of backpacking in Minnesota.
[131.12 --> 137.04]  So just about the opposite from my day-to-day life sitting in front of my computer screen.
[137.18 --> 140.54]  So it was a really nice disconnected time.
[140.72 --> 143.24]  So happy to have that time.
[143.70 --> 145.88]  Do you have any good times over Labor Day?
[146.84 --> 148.76]  Yeah, I had a good time with the family over Labor Day.
[148.76 --> 153.68]  We went to a local lake in the Atlanta area and did a little kind of a beach thing, which was nice.
[154.08 --> 157.86]  And I, too, am looking forward to a couple of weeks of vacation coming up.
[157.96 --> 158.52]  I'll be in the UK.
[158.90 --> 161.76]  My wife is British, so we spend a lot of time over there.
[162.00 --> 166.34]  And other than that, lots and lots of business travel, conferences, things like that.
[166.90 --> 167.56]  Yeah, definitely.
[167.70 --> 169.22]  You're keeping busy for sure.
[169.80 --> 173.70]  Well, today we have Cheryl Chen on the show.
[174.44 --> 176.90]  She is an ML developer at Google.
[176.90 --> 180.10]  I met her recently over the summer.
[180.28 --> 186.62]  She's doing some really awesome things and has done some really quite a bit of different things while she's been at Google.
[186.88 --> 194.48]  But I'm really happy to have her on the show today to talk about some of the things that she's doing with Google Cloud and some other AI things.
[194.60 --> 195.22]  So welcome, Cheryl.
[195.64 --> 196.70]  Hey, nice to meet you.
[197.38 --> 197.72]  Yeah.
[197.72 --> 213.54]  Well, could you just give us maybe just a little bit of background about, you know, how you got into computers and eventually AI and programming and ended up at Google and doing machine learning and all of these things?
[214.42 --> 215.26]  Yeah, of course.
[215.26 --> 218.46]  So yeah, so currently I work at Google, like you said.
[218.46 --> 233.22]  And my primary area of focus is auto machine learning, which has been this up and coming practice in machine learning where you're basically given the label data.
[233.22 --> 242.38]  And at the end of it, you get, you know, predictive model without having to really do very much machine learning in the process.
[242.70 --> 253.44]  And what brought me here, I guess like that story starts with my first computer, which I would actually say was the Nintendo, which kind of dates me, I guess.
[253.44 --> 253.84]  Nice.
[254.20 --> 254.42]  Yeah.
[254.42 --> 255.78]  It's like the original Nintendo.
[255.92 --> 260.50]  The original Nintendo was like my first, you know, gateway into technology.
[260.50 --> 274.32]  And I just remember, I have a lot of memories of just playing, you know, hours upon hours of games and being captivated by these virtual worlds, these pixel, very pixelated virtual worlds.
[274.32 --> 290.46]  And, you know, just like not only was it just, you know, wondering how it was possible that we could have these, the input, output, all that feedback coming out of my TV, but, you know, thinking and dreaming of how I could make it better.
[291.20 --> 296.82]  And so naturally, you know, I just, I went to a high school that happened to have, you know, computer science.
[296.82 --> 299.66]  And I remember asking, you know, what is computer science?
[299.66 --> 308.22]  I, you know, was in a classroom eventually of like four or five students that, you know, happened to have a particular interest.
[308.38 --> 311.20]  It wasn't like a very widely popular subject area.
[311.40 --> 313.10]  Then, of course, naturally you go to college.
[313.38 --> 319.76]  And I think I'd forgotten that I loved video games at some point or like that that was kind of my motivator.
[320.32 --> 327.36]  And so at some point I think it was like I was, and I was late, late to playing this game, but Final Fantasy VII.
[327.52 --> 327.90]  Nice.
[327.90 --> 333.80]  Really got me back into thinking about these worlds and the stories that they told.
[333.96 --> 346.34]  So then I signed up for some summer research and I did a research project looking at like artificial intelligence and storytelling, which then led me to UC Santa Cruz, where I studied under Michael, Dr. Michael Matias.
[347.30 --> 352.98]  He was a leading expert in interactive intelligent dramas, he would call them.
[352.98 --> 369.90]  So there are like basically these, he created this game called Facade, which is this very lifelike, you know, reactive, natural language driven interaction or game with within this story of this couple that you would go visit them and talk to them.
[369.90 --> 376.14]  And at the time it was like, that was like 10 years ago, it was like state of the art, you know, there hadn't been anything like that before.
[376.14 --> 381.48]  And that really, really motivated me to go and pursue studies under him.
[381.58 --> 382.90]  So I went to do grad school there.
[383.30 --> 386.76]  And while I was in grad school, I thought I would be like an academic for the rest of my life.
[386.88 --> 387.98]  I wanted to be a professor.
[388.48 --> 390.58]  And in some ways I still do want to be a professor.
[390.58 --> 397.06]  But I was in Silicon Valley and I took an internship with Google because somebody asked me, like, why not?
[397.72 --> 400.00]  And it totally changed the way I saw the world.
[400.10 --> 402.16]  I thought of impact in a totally different way.
[402.98 --> 407.52]  And so I started, like you said, at Google I did a couple different roles.
[407.70 --> 419.80]  So I was at YouTube, working on YouTube search as a software engineer, really looking at search algorithms and the ways that like little changes here and there could impact how people use the product.
[419.80 --> 423.94]  Then I wanted to be more publicly engaged.
[424.16 --> 429.54]  So I was doing developer advocacy at Google Cloud, working with the machine learning and AI tools.
[429.68 --> 434.96]  And that's really kind of where, like, that was also around the time the ML boom was happening.
[435.14 --> 439.36]  One of the big, like, oh my gosh, you know, look at all this, look at all this progress.
[439.52 --> 445.26]  Look at all of the abilities that weren't possible before enabled with machine learning.
[445.50 --> 447.98]  And that was probably like 2016.
[448.32 --> 449.44]  Yeah, it was around 2016.
[449.80 --> 460.54]  And then I ended up doing a rotation with Google Brain, which is one of the premier groups working in AI today, working on Project Magento, which does music and machine learning creativity.
[461.50 --> 470.04]  And then as I'm, like, digging deeper into these products, that led me to AutoML, which I explained at the beginning.
[470.24 --> 476.52]  But yeah, that's basically my journey from video games to working in ML at Google.
[476.52 --> 478.26]  That's amazing.
[478.48 --> 489.98]  Yeah, I'm interested in, like, one of the things you said was, like, it kind of, you know, going to Google and experiencing that kind of reset your ideas about impact.
[490.48 --> 498.10]  Do you mean, like, in academia, you can have an impact because you can research new things and kind of release them into the world in some sense?
[498.10 --> 500.38]  Is that the kind of impact you're thinking of?
[500.42 --> 504.56]  Or how do you view impact these days in terms of, like, the AI work that Google's doing?
[505.18 --> 513.16]  Yeah, I mean, I think you're right in that, like, what we do in academia is that we write papers.
[513.58 --> 519.14]  And these papers hopefully are cited by future papers and that people receive them well.
[519.14 --> 523.18]  And it helps, you know, continue to advance the state of the art.
[523.78 --> 526.86]  And to me, that was, like, it was very romanticized in my mind.
[526.94 --> 535.86]  You know, like, when I went to undergrad, I thought, you know, this is where everyone's just, like, talking about ideas and challenging one another to do better.
[536.04 --> 538.60]  And, you know, I found that in grad school more so.
[539.00 --> 541.76]  But then it was kind of all I knew, right?
[541.76 --> 547.24]  It's like when you're looking up to your professors, you're like, oh, I'm going to become that someday.
[547.90 --> 555.54]  You think, in addition to all that, think about how you're going to be a teacher and how you're going to mentor people and how you're going to grow a group that way.
[556.00 --> 558.96]  And so, you know, I'm almost embarrassed to tell this story.
[559.50 --> 561.08]  But I honestly didn't know.
[561.30 --> 564.84]  Like, I didn't go into computer science thinking I'm going to be a software engineer.
[565.02 --> 568.32]  I'm going to, you know, like I wasn't influenced by the dot-com stuff.
[568.70 --> 570.32]  I really had no idea.
[570.32 --> 571.72]  I wanted to make video games.
[571.82 --> 574.44]  Like, I would call up Nintendo's hotline.
[574.56 --> 580.88]  Like, I think it's, like, 1-800, like, I had it, like, memorized, you know, like, 255-370-00.
[580.94 --> 581.94]  I don't even know if that's right.
[582.22 --> 583.32]  But it was something like that.
[583.32 --> 586.34]  And I would ask them, like, how do I make video games?
[586.42 --> 591.54]  That was how, like, detached I was to how kind of the non-academic world functioned.
[591.94 --> 600.22]  So when I went to Google, I was, you know, really excited because there was a whole new world that I didn't understand.
[600.32 --> 606.08]  And a whole lot about one of the questions they asked me was, you know, this is really embarrassing.
[606.62 --> 609.08]  How many users did I think YouTube had?
[609.40 --> 611.84]  And I was like, okay, you know, like, what's a big number?
[611.84 --> 617.80]  For me, you know, in research, like, having 100 users was like, that was like a lot of users.
[618.00 --> 618.88]  Like, too many users.
[618.88 --> 622.78]  I remember the statistician telling me, like, 100 users, that's, like, too much data.
[623.08 --> 624.98]  Like, you collected too much.
[625.18 --> 630.48]  Yeah, I don't think what I coded in grad school ever had 100 users for sure.
[630.68 --> 631.96]  Yeah, yeah, yeah.
[632.22 --> 639.00]  So the number I gave, and sometimes I'll even, like, multiply my guess by a factor of 10 because it's so embarrassing.
[639.40 --> 641.58]  I said, I was like, oh, like, 10,000.
[641.68 --> 642.78]  Like, I didn't even think about it.
[642.78 --> 647.72]  I said 10,000 and the manager, like, laughed and then said, never mind.
[648.40 --> 649.56]  And then moved on.
[650.26 --> 651.68]  There's at least 10,000.
[652.08 --> 652.32]  Yeah.
[652.46 --> 653.02]  That's a good story.
[653.28 --> 653.42]  Yeah.
[653.68 --> 656.66]  No, this was, and this was, like, just, that was, like, how new I was to it.
[656.70 --> 660.30]  That's how little I knew about, like, the product side of things.
[660.30 --> 661.70]  Like, the real world applications.
[662.18 --> 666.92]  Yeah, and sometimes when I tell the story, I'll say 100,000 because it's a little bit, like, okay, like, you know.
[666.92 --> 667.96]  So I can see that.
[668.04 --> 669.90]  But, yeah, no, I literally said 10,000.
[670.28 --> 689.48]  Yeah, so, like, the scale of the impact of YouTube and, like, anything you would integrate in YouTube, including, like, whatever it is, like, you know, whether it's AI related or not, is going to have an impact on a scale that's just totally outside or just totally different than what it is in academia, basically.
[689.94 --> 690.84]  Absolutely, yeah.
[690.84 --> 697.18]  So I got to, before I ask a question, I'm actually going to throw back all the way to the beginning when you were talking about your childhood in high school.
[697.70 --> 705.72]  And I think I might be slightly older than you because my first computer game was the original Atari system.
[705.80 --> 706.34]  Wow, yeah.
[706.42 --> 712.96]  And then when I learned how to, in high school, they were still teaching typing on typewriters.
[713.30 --> 714.32]  Oh, nice.
[714.56 --> 715.92]  That was just coming to an end there.
[715.98 --> 717.02]  I know, I know.
[717.02 --> 721.80]  And we didn't have a computer in the school at the time, so I'm slightly older than you, but just barely.
[722.64 --> 722.84]  Yeah.
[723.16 --> 724.38]  I work with a guy.
[724.56 --> 726.12]  I just think this is cool.
[726.18 --> 735.46]  I work with a guy who met his wife messaging back and forth on the, I think it was the University of Michigan, like, mainframe.
[735.84 --> 739.28]  So it was, like, there was only, like, there was no internet, right?
[739.28 --> 747.66]  So they, like, let students access, like, the University of Michigan mainframe, and they were, like, two of the students messaging on there.
[747.74 --> 750.54]  And they eventually, you know, talked and got married.
[750.64 --> 751.82]  I thought that was pretty great.
[752.40 --> 756.34]  That might be the only mainframe romance story I've ever heard about in my life.
[756.34 --> 768.46]  So, okay, so I want to actually get a little clarification because, you know, we are all always hearing about everything AI from Google, and there's all these different things.
[768.54 --> 772.66]  Google Brain, Magenta, TensorFlow, Google AI, Google Cloud, you name it.
[772.66 --> 781.18]  And so, like, how do these things, how do these different parts of Google that work in AI areas relate to each other?
[781.34 --> 783.04]  And, you know, are some of those the same?
[783.10 --> 785.28]  Is Google Brain and Google AI the same or not?
[785.36 --> 789.46]  And how does TensorFlow, you know, as a tool fit into that ecosystem?
[789.80 --> 795.44]  And, you know, can you kind of just give us a sense of where all these pieces of AI fit in at Google and how they relate?
[795.90 --> 796.08]  Yeah.
[796.58 --> 799.30]  I would say that that's a really good question.
[799.30 --> 803.54]  And I definitely have a pretty good insight having worked with a lot of these teams.
[804.32 --> 809.36]  So, like any big company, there's always, like, there's, like, the research side and there's the product side, right?
[809.42 --> 820.38]  And so when you're, if you're looking to work in technology and you want to be a research scientist, then, you know, you're looking at, like, being the leading expert in your area.
[820.50 --> 825.84]  So you're good at doing image recognition and you're, like, one of you have all these publications.
[825.84 --> 831.44]  If you're looking to be, like, on the product side, oftentimes they're looking for people who are, like, straight up builders.
[831.62 --> 834.82]  So engineers, they're looking at people who have business sense.
[834.92 --> 837.70]  They're looking at people who understand users, things like that.
[837.74 --> 840.26]  So they're, like, in some ways their objectives are very different.
[840.36 --> 846.12]  One is looking at being published at NeurIPS or iClear, these top machine learning conferences.
[846.12 --> 854.06]  And some are looking, and on the other side of things, you're looking at people who want to, you know, create a tool that has a lot of users.
[854.76 --> 860.12]  So at Google, you know, it's a big company, you know, like, close to 100,000 employees.
[860.96 --> 862.50]  It's in the ballpark, I think.
[862.64 --> 863.88]  And it's all over the world, right?
[863.92 --> 871.14]  And so a lot of these projects are really, like, it's really kind of an opportunity for people to see, you know, what really sticks.
[871.14 --> 873.24]  What's actually going to show traction?
[873.48 --> 887.84]  So you see a lot of, like, organic emergence of different applications of technology, whether it's VR, AR, whether it's, like, you know, home systems, like the Google Assistant, whether it is something like AI and ML.
[888.98 --> 890.24]  So, like, what is the landscape?
[890.24 --> 900.88]  So, like, I've heard people say, like, you don't want the outside-facing representation of what you do to look like your organizational chart.
[900.88 --> 912.86]  So you don't want the team structure to be directly reflecting of, like, what it is that you're providing for people in the, you know, the public to use and to see and to experience.
[913.28 --> 925.42]  I would say that the way that they're shaping that, and a lot of this is, like, I think, you know, just being good storytellers or being good marketers to kind of put the tools in places where people who need them will be able to get them the easiest.
[926.46 --> 928.54]  So we have, like, you know, Google Cloud, right?
[928.54 --> 932.18]  That's where they're moving towards providing business solutions.
[932.42 --> 936.62]  They're providing enterprise technologies, things like that.
[936.66 --> 937.92]  So things that will help your business.
[938.46 --> 940.66]  Then there's what we call Google AI.
[941.52 --> 946.32]  A lot of Google AI, like, within Google it's called research and machine intelligence.
[946.32 --> 963.50]  It's basically a lot of the, like, the less, like, looking at how many users we have, but more looking at, like, you know, is this, is the work that's coming out of here relevant to the state of the art or, like, advancing the state of the art?
[963.50 --> 970.38]  And so those are kind of two of the bigger, bigger organizations that we could dissect even further.
[970.54 --> 979.76]  But then outside of that, there's, like, one more group, which is, I would say, like, more of a collection of groups where you have, like, Google Assistant, you know, Google Photos.
[980.02 --> 988.20]  A lot of these Google products use machine learning and AI to create better features, to create better user experiences and things like that.
[988.20 --> 991.10]  So, like, so Google Cloud, I think, is pretty straightforward.
[991.24 --> 994.80]  If you go to the cloud website, you can kind of look at all the different offerings and things like that.
[995.12 --> 1003.58]  I think Google Cloud AI and, like, Google Research is probably where it's kind of like, okay, what, where does TensorFlow fit and where's the AI side of things?
[1003.68 --> 1010.06]  So I can kind of, I could talk about it from, I would say it was, like, it was Google I.O. 2017.
[1010.78 --> 1016.06]  And that was when we moved to being an AI-first company.
[1016.48 --> 1017.02]  Yep, I remember.
[1017.02 --> 1019.32]  Like, Sundar was, like, AI-first.
[1020.22 --> 1022.98]  I had just joined Google Brain at that time.
[1023.20 --> 1027.72]  And we were in a building that was, like, you know, there's the, you know, Google's based in Mountain View.
[1027.80 --> 1028.80]  We have the Googleplex.
[1028.92 --> 1039.60]  Like, it was in, like, you know, the main area, but not in the Googleplex, which is, like, a set of four, let's see, 40, 41, 42, 43, four buildings.
[1039.60 --> 1047.10]  And so Google, like, a lot of the, you know, Google Brain team, it was actually, like, across the street, right?
[1047.42 --> 1049.92]  So I joined Sundar announces.
[1050.38 --> 1052.06]  We're, like, AI-first.
[1052.36 --> 1055.30]  And all of a sudden, they're getting moved to the center of campus.
[1055.30 --> 1063.26]  And so I remember my desk was, like, maybe, like, 30 feet away from, like, Sundar's desk because of that move.
[1063.72 --> 1065.86]  And, like, of course, I never really saw Sundar.
[1065.94 --> 1067.88]  And there was, like, a wall that separated us.
[1067.98 --> 1070.02]  And you couldn't badge into that side of the building.
[1070.26 --> 1074.70]  So, like, I think we were – I'm just, like, looking at, like, the blueprints of the building.
[1074.82 --> 1077.12]  I was kind of like, oh, like, I'm, like, pretty close to this.
[1077.20 --> 1079.16]  We're probably breathing the same air or something.
[1079.16 --> 1081.58]  But I didn't get to see.
[1081.82 --> 1087.28]  Anyways, let's just kind of give you a sense of, like, topologically, like, how the feel of it is, right?
[1088.12 --> 1089.54]  So TensorFlow, right?
[1089.84 --> 1094.18]  TensorFlow is, like, basically is – it dwells.
[1094.24 --> 1094.76]  It lives.
[1094.88 --> 1099.32]  It's, like, being developed and improved within the Google Brain team.
[1099.32 --> 1108.82]  Google Brain team was, at the time, run by this superstar engineer, Jeff Dean, that, you know, he's a celebrity inside and outside of Google.
[1109.16 --> 1115.00]  I believe, like, you know, Andrew Ng and some other people also were responsible for starting this, like, you know, Google Brain effort.
[1115.76 --> 1124.86]  And when we became AI first, it kind of got moved into, you know, a more central location physically, but also as far as focus goes.
[1125.44 --> 1128.68]  So then brain isn't the only thing in cloud AI, though, right?
[1128.68 --> 1135.50]  Because we have groups like Machine Perception and Descartes, which, you know – do you guys know Ray Kurzweil?
[1135.92 --> 1136.74]  Yes, absolutely.
[1137.32 --> 1138.10]  Yeah, legend.
[1138.10 --> 1139.12]  Okay, absolutely.
[1139.40 --> 1139.78]  Yeah, okay.
[1139.88 --> 1142.22]  You guys would – so, like, Ray Kurzweil has a team, right?
[1142.24 --> 1145.10]  And that team isn't a part of Brain, but he's also doing incredible work.
[1145.20 --> 1150.52]  So one of my favorite works that came out of Ray Kurzweil's group is the talk to books.
[1150.76 --> 1158.32]  And so, you know, Ray Kurzweil has these, like, you know, amazing, fantastical, like, aspirations for technology.
[1158.32 --> 1162.62]  And so his thought is, like, you know, what if you needed to know something in a book?
[1162.66 --> 1167.66]  Like, what if you could just ask the book and say, hey, book, you know, tell me, you know, what's the meaning of life?
[1167.66 --> 1169.64]  And the book can just kind of spit out an answer.
[1170.18 --> 1177.34]  And so, like, that was the kind of – like, every research lead would, like, kind of bring in their own flavor.
[1177.34 --> 1184.26]  You know, ironically, that's kind of how the rest of us think about just Google search in a lot of ways, you know, is, hey, we're just going to go and find out what the answer is.
[1184.50 --> 1186.48]  So it's just funny to hear it coming out of your mouth there.
[1186.72 --> 1187.18]  No, totally.
[1187.40 --> 1192.80]  And it's like – and so, like, in a team like that, like, they're thinking, you know, what is the next evolution of search?
[1192.80 --> 1201.58]  Right now it's just – it's been kind of, like, this, like, keyword, like, pattern matching where you look for the exact pattern of characters that you've typed in.
[1201.92 --> 1209.38]  But what if there was more of, like, a semantic reasoning behind, you know, search and results that arise from those queries?
[1209.84 --> 1219.00]  So, like, when you talk to your Google Assistant, you have the ability to kind of – it's kind of trying to reason more about your intent behind what you're trying to look for.
[1219.00 --> 1224.32]  And so they've created this idea of, like, you know, rather than keyword search, what about, like, semantic search?
[1224.36 --> 1225.36]  And they created this game.
[1225.48 --> 1234.46]  It's called Semantris, where you have, like, a list of objects and then you're trying to, like, semantically match the meanings.
[1234.68 --> 1241.16]  And you can knock out different words if you can get, like, a direct match or there's, like, a, you know, one degree separation between meanings.
[1241.28 --> 1241.58]  Oh, cool.
[1241.58 --> 1246.74]  So anyways, anecdotally, that's, like, something that I found really, really delightful.
[1246.74 --> 1253.08]  But, okay, so then Google Brain, run by Jeff Dean.
[1253.54 --> 1260.14]  And Jeff Dean now, like, you know, JG was originally the man in charge for research.
[1260.36 --> 1267.54]  But he has left and Jeff Dean now is running RMI and doing a lot of the research leadership.
[1268.28 --> 1275.18]  Google Brain, though, at the time and now focuses really on, like, you know, how machine learning can make the world better.
[1275.18 --> 1278.20]  And so there's a huge, like, medical side of it, right?
[1278.26 --> 1283.14]  So there are a lot of people looking at, you know, medical advancements or medical use cases for machine learning.
[1283.62 --> 1292.48]  There's, you know, Project Magenta, which is under kind of the generative models group where they're looking at how we can generate not only just music and art but text.
[1292.48 --> 1301.88]  And one of the cool use cases of that is generating Wikipedia pages because you do have a large, well-curated data set from Wikipedia.
[1302.56 --> 1306.74]  And so how can you use that to generate text in intuitive ways?
[1307.18 --> 1308.80]  And, yeah, robotics is another group.
[1308.92 --> 1311.12]  So then there's all these different topics, use cases.
[1311.12 --> 1318.72]  And I think the reason why Cloud AI came about was that, as you can tell, it's kind of a lot of, there's a lot going on under the hood.
[1318.88 --> 1340.04]  And Cloud AI is kind of this landing spot, this portal where you can get the Cloud AI stuff, where you can get into, you know, what Magenta is doing, where you can see, you know, what kind of research is coming out of the group in a more, you know, more, like, user-facing side of things rather than, like, you know, if you're, like, Jeff Dean, like, overseeing kind of the research arms and limbs.
[1341.12 --> 1371.10]  Thank you.
[1371.28 --> 1371.62]  Thank you.
[1371.84 --> 1375.88]  Thank you.
[1379.68 --> 1381.38]  Thank you.
[1394.38 --> 1395.30]  Thank you.
[1396.52 --> 1399.86]  Thank you.
[1401.12 --> 1407.58]  So you mentioned AutoML a couple times or AutoMachine learning.
[1407.58 --> 1414.68]  And I think it would be great if we like jump into a little bit of detail on that, because it's definitely come up a few times on the show.
[1414.84 --> 1424.76]  But as we were kind of discussing prior to starting the recording, we haven't really, you know, talked about it in any in any sort of detail.
[1424.76 --> 1442.92]  So I'm wondering if you could just kind of describe AutoML, like generally how it's different than like how people are used to doing ML, maybe, because some people might think, you know, ML is kind of automated in some ways already in the sense that like, oh, I can get a CSV, right?
[1442.94 --> 1450.16]  And then I can like go use random forest from scikit-learn and like choose the column that's the labels, right?
[1450.16 --> 1453.92]  And it seems like it kind of just happens for me, right?
[1453.92 --> 1459.32]  So how is like, how is AutoML kind of different than than that?
[1459.42 --> 1463.98]  And maybe also like, why is it why is it needed in certain scenarios?
[1464.48 --> 1468.60]  Yeah, so I love like, you know, practical AI, right?
[1468.62 --> 1469.50]  Let's be practical.
[1469.68 --> 1473.18]  Let's think about how that would be great.
[1473.32 --> 1474.26]  Yeah, yeah.
[1474.56 --> 1474.96]  Perfect.
[1475.12 --> 1476.50]  Yeah, I want to be.
[1476.60 --> 1479.32]  Now let's take this down the practical route.
[1479.32 --> 1483.42]  So we have, we have machine learning, we have AI.
[1483.96 --> 1485.56]  How does that impact the world?
[1485.78 --> 1490.42]  Like, do you like, can, like, how, how does it affect the everyday person, right?
[1490.72 --> 1494.48]  So a lot of people in the US, they use smartphones.
[1494.70 --> 1503.70]  And so now they're able to, now they're able to, you know, if they're traveling abroad, they could take a picture of a menu and get that translated on the spot.
[1503.70 --> 1509.18]  Or they don't even have to take a picture, like, just within the computer screen, they can translate from like Spanish to English.
[1509.40 --> 1515.30]  And a lot of this, this image recognition or language understanding comes from advanced machine learning.
[1515.42 --> 1518.04]  So on the user side, there's already a lot of people using it.
[1518.34 --> 1532.50]  And what they found is that a lot of these tools are useful, like if you want to be able to use voice commands, you don't need to necessarily retrain, you know, like, I don't even know how much data they use.
[1532.50 --> 1545.16]  But like all the data that they require to kind of train that, that voice model, that voice speech to text model, they don't need to necessarily have to go through, like every, every company that needs that doesn't need to go through and do that again and again, right?
[1545.16 --> 1553.00]  So, so Google having worked on this technology and using it in its own products makes this available for people.
[1553.12 --> 1560.56]  So you can come in, you have an app that you want to build, you want to use like, you know, you want it to be voice activated.
[1560.56 --> 1566.58]  Or you want to be able to take images and figure out if they are kid-friendly images.
[1567.22 --> 1573.04]  Like there are these models that Google has pre-trained and that they work, and they, and Google is ensuring that these models work well.
[1573.54 --> 1583.04]  So without any data, with just the desire to have this feature, you can already plug and play certain products that Google have in machine learning, right?
[1583.04 --> 1591.92]  Anything with, a lot of stuff that requires, anything that requires vision or audio processing or natural language, I think these are very common use cases.
[1591.92 --> 1598.96]  And then on the other end of things, right, like you were mentioning, you could, you could set up your own Python environment.
[1599.10 --> 1601.04]  You could be, you could be coding in TensorFlow.
[1601.34 --> 1603.14]  You could train your own model.
[1603.32 --> 1605.64]  You can, you could feature engineer on your own.
[1605.72 --> 1607.30]  You can hyperparameter on your own.
[1607.44 --> 1613.76]  You can look at the models and the precision and recall and assess how good these models are doing.
[1613.76 --> 1615.52]  And then you can do it all over again.
[1615.68 --> 1624.22]  And as data, as, you know, maybe you have something running in production, you can kind of have all of that, you know, like all the control over every aspect of that.
[1624.44 --> 1625.46]  So that would be the other end.
[1625.54 --> 1629.32]  And of course, you know, enterprise cloud technologies, they provide the environments.
[1629.46 --> 1630.32]  You have Docker containers.
[1630.48 --> 1633.52]  You have virtual machines that can also satisfy that need.
[1634.04 --> 1640.34]  What AutoML does is it focuses on the middle piece or at least trying to figure out how you go from one end to the other.
[1640.34 --> 1648.06]  So on one end, you have pre-trained APIs where you have like basically no control over how that model is making decisions.
[1648.64 --> 1651.58]  And then you have like build it from scratch, like do it all yourself.
[1651.88 --> 1658.62]  For a lot of businesses, it's kind of hard to go sometimes from research directly to, you know, production.
[1659.34 --> 1667.12]  And so trying to find that middle point, you know, is what the, what people working in auto machine learning are trying to figure out.
[1667.12 --> 1669.58]  Like, like things like hyperparameter tuning, right?
[1669.58 --> 1672.86]  Are we tuning these weights around to kind of get a feel?
[1673.04 --> 1680.26]  And people before have said, you know, this is a highly intuitive thing where you kind of get a sense of, you know, whether this number should be bigger or lower.
[1680.82 --> 1685.02]  Auto machine learning, one of the aspects is like trying to figure out how to just simply do that.
[1685.36 --> 1691.02]  With the tools that we have now, like it could just be a matter of thinking, you know, why, why, you know,
[1691.02 --> 1703.58]  you might be able to figure out, you know, safe search or kid friendly images is something that, that pretty universal for the most part, but maybe not for every culture, right?
[1703.58 --> 1707.60]  You might want to label your own data as like, you know, this image isn't safe.
[1708.10 --> 1713.60]  You might want, you may, maybe like, it's not enough to know which pictures have cats in them.
[1713.64 --> 1715.80]  Like you can go to your Google photos right now and do that, right?
[1715.80 --> 1720.12]  You can go into your Google photos, type in cat pictures, get all the cat pictures.
[1720.22 --> 1726.04]  But what if you want to know what type of cat or what if you want to know like, you know, different colors of cats?
[1726.88 --> 1731.64]  The specificity that these pre-trained more general use cases may not provide.
[1731.78 --> 1740.82]  And so AutoML in the, in the most like general use case is basically giving you the opportunity to label your own data and then feed that in.
[1740.82 --> 1745.06]  So you're getting customization without having to build everything up from scratch.
[1745.72 --> 1745.82]  Yeah.
[1745.94 --> 1752.38]  So am I correct in saying that kind of AutoML encompasses what could be a lot of things?
[1752.56 --> 1757.12]  So there's also like all this other sort of jargon that's, that we're running across, right?
[1757.12 --> 1760.22]  Like meta learning, like learning to learn.
[1760.22 --> 1776.12]  And then there's like the transfer learning side of things, which is taking like, you know, pre-trained models and either fine tuning on, on additional small amount of data or maybe adding, adding layers to a network or something like that.
[1776.12 --> 1784.88]  So is AutoML kind of an encompassing term that encompasses a lot of those things or is it, or is it more specific or separate from those things?
[1785.34 --> 1785.54]  Yeah.
[1785.68 --> 1792.38]  As we, as we know in like AIM, ML, jargon is like, like often, it's very controversial sometimes.
[1792.76 --> 1793.78]  No, I would, I would say so.
[1793.82 --> 1801.22]  Like the people who I like, you know, learning to learn, like these are all groups that, that for which AutoML is the product.
[1801.22 --> 1808.40]  Like they draw upon the findings and, and the, the answer isn't like, how do we make machine learning better, which is a research question.
[1808.60 --> 1812.86]  What it's really doing is it's trying to figure out how do we deliver the best prediction model.
[1813.06 --> 1823.58]  And so maybe that prediction model is like heavily rules-based and they basically figured out in like two if statements, you can like figure out like the best prediction for a certain problem, right?
[1823.58 --> 1834.26]  I think, I think, I think AutoML, like the goal really is to make sure that you're providing the most accurate results given the data and the kind of outcomes that you're looking for.
[1834.50 --> 1834.98]  Yeah.
[1835.14 --> 1842.76]  So it's, it's kind of a general term that I guess could encompass many different things.
[1842.76 --> 1846.18]  So it could, like you were mentioning hyperparameters, right?
[1846.20 --> 1850.66]  Like there could be this sort of automated way of determining hyperparameters.
[1850.66 --> 1861.68]  Um, I know there's like maybe more complicated things like figuring out like the right types of, you know, uh, nodes or architecture of your neural network and that sort of thing.
[1861.74 --> 1863.68]  So I guess all of that would fit into AutoML.
[1863.90 --> 1866.04]  Would that be appropriate to say, I guess?
[1866.38 --> 1866.76]  Absolutely.
[1866.98 --> 1873.06]  Like, uh, one of my, there's this researcher on Google brain that, uh, works like who I'm friends with.
[1873.06 --> 1881.26]  And so we joke a lot and he's always like, we joke that he like uses up like so much of the, the, um, computing, uh, for the whole company.
[1881.26 --> 1882.68]  Like, you know, he like, right.
[1882.72 --> 1886.98]  There's like a leaderboard for like who uses the most computing for throughout all of Google.
[1887.40 --> 1891.44]  And one thing that I always joke about, I'm like, oh yeah, like how are those hyperparameters doing?
[1891.44 --> 1898.22]  Cause it's kind of a, like, we're kind of like minimalizing the kind of work that he's doing by joking about that.
[1898.28 --> 1906.74]  But I think it's, you know, hyperparameters tuning is just such a, like a fundamental, like something that people who get their introduction to ML like know about.
[1906.82 --> 1911.90]  And they know that this is this thing that's been highly, you know, human intuitive, intuited practice.
[1911.90 --> 1917.94]  And so it's kind of a, this go to, you know, how would you automate machine learning type deal?
[1918.48 --> 1929.94]  But yeah, but no, whenever I joke about it, he's just like, you know, it's not, I didn't, I don't mean to, I only do it in jest to minimize it a little bit, but no, it's, it's a very like common example to use.
[1930.06 --> 1932.16]  But yeah, like you said, it's like way more than that.
[1932.20 --> 1935.76]  It's the kind of, what kind of algorithm are you being, what kind of model are you training?
[1935.76 --> 1941.76]  What kind of approach are you, are you like, like even within like RNNs, there's already so many different ways of like,
[1941.90 --> 1945.28]  applying and using and deploying RNNs, things like that.
[1945.96 --> 1949.86]  And that, that almost takes right into what I was about to, I was kind of had at the top of my mind anyway.
[1949.86 --> 1957.80]  And that is how is AutoML being used in production and, and what makes it important for the future of AI and ML?
[1957.98 --> 1962.72]  So, you know, if people are using it in some way out in the real world, where is that going to lead for them?
[1962.88 --> 1963.92]  Where is that going to take them?
[1964.24 --> 1965.14]  No, that's a good question.
[1965.14 --> 1970.98]  I was actually talking to one of the gaming partners, so like a gaming company.
[1970.98 --> 1982.58]  And I was, it's interesting because on one hand you think, you know, AutoML's trying to take a lot of that in between the statistical work out of it, right?
[1982.66 --> 1994.46]  So I was talking to data science teams and I ultimately feel like AutoML's like purpose should really be able to, to be able to extend the data scientists' abilities and intuitions.
[1994.46 --> 2001.36]  It should be, it should be, it should give them a sense of like which features are, you know, the most relevant, things like that.
[2001.78 --> 2008.64]  And sometimes I feel like a lot of this, there's like ML engineers, there's data scientists, they, they, they work together and sometimes they're working separate.
[2008.64 --> 2017.86]  But I do think that like ultimately it's the data scientists that's kind of serving that AutoML role, especially for specifically structured data.
[2018.00 --> 2022.74]  So we're talking about tabular, you know, spreadsheet-like data.
[2023.22 --> 2028.68]  I feel like a lot of that work is, the human intuition has been coming from data scientists at large.
[2028.68 --> 2034.46]  And the question is, does AutoML meet the standard of the data scientists?
[2034.58 --> 2036.58]  Does it extend the capability of the data scientists?
[2036.68 --> 2044.60]  Does it give the data scientists who has been this expert, like stewarding this area, does it give the data scientists the ability to kind of do more?
[2044.76 --> 2049.84]  Or to get a better sense of like, you know, what direction should we go in in making these decisions?
[2049.84 --> 2070.44]  So yeah, so I think that when we talk about these problems, we think like, you know, if you're a gaming company and you're looking at use cases for whether a player is going to continue, like whether a player is kind of, you know, plateauing and really like the game is just not engaging anymore.
[2070.44 --> 2080.94]  And at what point that is, and you're trying to make a prediction that after these actions, this next thing's happening, how do you correct course so that you make something that is more satisfying to the user?
[2081.48 --> 2088.26]  Things like that, where like I think a data scientist would sit and kind of go through like, here are the signals and here are the signs.
[2088.60 --> 2096.52]  I think AutoML would be like an additional like tool to be able to help arrive at those conclusions in a more efficient way.
[2096.52 --> 2104.60]  So there is like, I guess, some level of expertise that's needed to use AutoML.
[2104.90 --> 2108.48]  Like I was looking at one of the, I'm not sure where I was seeing this.
[2108.54 --> 2113.58]  I think this is one of the examples when I was looking at AutoML on the Google Cloud site.
[2113.72 --> 2118.16]  But, you know, my life right now at least is all about AI and natural language.
[2118.50 --> 2125.66]  And I think I was seeing, you know, one of the examples or use cases they were talking about was like, oh, you have this machine translation model.
[2125.66 --> 2130.88]  Maybe that's, that's pre-trained for some language pair, like English to German or whatever.
[2131.48 --> 2137.62]  But really you need like some very specific types of vocabulary translated.
[2137.76 --> 2147.10]  Like maybe it's like legal vocabulary or maybe it's like some domain that's not covered well by the data that the model was trained on.
[2147.10 --> 2158.40]  So you need to kind of get that model, you know, fine tuned a bit to that, to that, you know, vocabulary that's, that's not sort of general vocabulary.
[2158.40 --> 2171.40]  So I'm, I'm assuming that still like, you know, to structure that data, to get it in like the language pairs that you needed in to kind of understand and evaluate if your model's like doing well.
[2171.40 --> 2185.30]  Well, even if you're not like setting all of the hyper parameters or you're not like, you know, you know, coding all of the neural network architecture, there's still like a level of expertise that's required to set up that, that experiment.
[2185.30 --> 2188.08]  Right. And be able to know if it's, it's working. Is that right?
[2188.08 --> 2208.38]  Um, so I would say that, uh, it really, we were talking about tabular data earlier, right? I can kind of walk through a little bit of like how that would look, but I would say to answer your question, um, that you really need to, uh, I think the expertise really comes in once the model is trained.
[2208.90 --> 2215.06]  Um, because from that you kind of, you need to have kind of a sense of whether the model is doing well enough for you.
[2215.06 --> 2220.60]  So every, for every, you know, in production, every, every feature, every use case is going to be different.
[2221.00 --> 2224.50]  And sometimes, you know, you know, if you're 99% accurate, that's good.
[2224.86 --> 2226.82]  So for some of them, that's not good enough. Right.
[2227.08 --> 2244.78]  But really, uh, I would say the expertise comes in with, um, with also once if say the model needs to be better, um, or say some change needs to be made to be able to understand like how to engineer or, or shape the data in a way that's going to give you a better outcome.
[2244.78 --> 2247.86]  So there's, there's like, there's basically, there's two different ends of it, right?
[2248.06 --> 2256.88]  You could just, uh, trial and error it and, you know, give it data, uh, run the prediction, uh, or train it and then run the predictions and then see how well it does.
[2256.96 --> 2261.70]  And if it's good enough from your sense, uh, I, I would say that that's kind of the bare minimum.
[2261.70 --> 2272.18]  Um, but I think, you know, to hold to kind of higher standards and to kind of, uh, oversee like, you know, what I said earlier, the state of the art, um, is doing.
[2272.26 --> 2284.68]  I, I do think it's important to have somebody with like data science or statistical understanding or machine learning understanding to be able to see whether, like to kind of just not let it run, run in the wild.
[2284.68 --> 2288.68]  And this is something that, um, that people talk about, you know, auto ML, this is like true democratization.
[2289.32 --> 2294.22]  Cause you're really just giving you, all you have to do is just have the label data, show it lots of examples.
[2294.22 --> 2295.74]  And then it's going to make the prediction.
[2295.74 --> 2306.68]  Um, I've talked to like, you know, the product, uh, manager, the product side of TensorFlow, you know, going back to the research side and what they would sometimes say is, you know, is that truly democratization?
[2306.68 --> 2315.54]  Because at the end of the day, you're, you're relying on Google cloud auto ML tables to make this decision and you're controlling these two ends.
[2315.54 --> 2320.74]  You get to decide what data goes in and you get to decide whether this prediction model goes into production.
[2320.74 --> 2333.78]  But like, you know, tense, like arguably TensorFlow, this open source tool for machine learning, uh, you actually have is like ultimately giving you the, like all the control and all the power.
[2333.86 --> 2335.38]  It's just the learning curve is much higher.
[2335.50 --> 2337.52]  So there, there's the cost benefit of that.
[2337.66 --> 2350.58]  But, uh, but yeah, I would say that I could teach, you know, a 13 year old how to use with no machine learning understanding somebody who's like, you know, understands how to point and click and load.
[2350.74 --> 2360.16]  In files, um, how to train their own model and give them kind of an intuition of what that evaluation, how that should evaluate and how to test that out.
[2360.54 --> 2363.80]  So one of the things I'm, I'm wondering, um, I'm pretty interested.
[2363.92 --> 2368.56]  I know in a few minutes, I'm going to ask you to kind of take us through kind of an example, if you would.
[2368.60 --> 2372.98]  But before we get to there, what are some of the disadvantages maybe for auto ML?
[2372.98 --> 2377.22]  Well, you know, things like would, would interpret, interpretability be one of those?
[2377.22 --> 2382.88]  And are there, are there certain kinds of domains for which it might not be the most suitable thing?
[2382.88 --> 2388.84]  And, you know, and I guess since I'm talking about, you know, what, what is it, you know, potentially not best suited for?
[2388.94 --> 2395.22]  What are some of the biggest research areas, the biggest open questions that you guys are taking auto ML into?
[2395.48 --> 2397.68]  You know, so what's it, what, what's it challenged on?
[2397.74 --> 2400.84]  And where do you, where do you see it going in the future in terms of applicability?
[2400.84 --> 2411.68]  Yeah. Yeah. I guess in the, in the spirit of AI, it's like throw out, I'll throw out more buzzwords, like humans in the loop and mixed initiative, co-creative systems.
[2412.00 --> 2412.78]  Differential privacy.
[2413.12 --> 2429.44]  Yeah. Um, so I like the, I think the question I get asked most when I'm, you know, showing, working with like data scientists or showing teams, uh, customers, uh, partners, um, people who want to, you know, people who are already or want to use machine learning.
[2429.44 --> 2442.82]  When I showed them these tools, you get kind of a range of questions. If somebody is like more on the data science machine learning side, they'll say things like, like, what if I want to be able to get in there and like make some changes?
[2442.82 --> 2453.06]  I mean, it gives you like this tool and it, and honestly, this tool change, it launched auto ML tables for tabular data launched in April of this year.
[2453.20 --> 2466.10]  So it's changed a lot already since then. It's not been that long. So it's constantly changing. But, um, but right now what, what is, what is available to you is you can, um, once the model is trained, you can call a REST API.
[2466.10 --> 2480.46]  REST API, you can, um, export the model as a TensorFlow package and download it onto your own machine and run it from there. There's things like that, that you can do. Right. But what we get asked often is like, well, can you give us more information?
[2480.46 --> 2496.86]  We want more analytics. We want more, uh, we want to see like really, you know, how well the features are doing in more detail. And that is like totally under the hood. You don't have access to that. You can't, um, you know, say if you wanted to, you couldn't really tune the hyperparameters in this case.
[2496.86 --> 2513.76]  It's really just giving you, uh, the end points of machine learning from training to, to, um, inference. Um, yeah. So, so I, I would say that that's probably one of the drawbacks is that you're ultimately not getting the amount of control that you would if you were building your own model from scratch.
[2513.76 --> 2541.30]  And that question of control or at least intuition, and you said interpretability and understanding why it's making these decisions. It's even more abstract. It's like, like the, it's almost like by design is trying to like reduce complexity by not showing you these things. But again, with like, you know, this concept of humans in the loop or understanding what kind of controls do we want as we, like, you know, the whole point of machine learning. And it's almost like seen in research as the more humans are involved, the more they're going to mess it up.
[2541.30 --> 2571.28]  Um, but like, like, as we, as we reintroduce, like, like working in like the team Magenta, right. It was focused on project Magenta was focused on creating generative tools, like extensions of humans. And so this concept of where does the human, where, what kind of control the human wants is very important. Um, the problem is, is that machine learning can get very complicated very quickly. So, uh, so either people are just overwhelmed with the, you know, with the burden of choice that they have and not really understanding how it all works together.
[2571.30 --> 2580.80]  Or it's like, we're kind of taking that away so that they can still make decisions without kind of taking for granted all the stuff that happens in between. That makes sense.
[2580.80 --> 2607.04]  Hey, guess what? Brain science is officially launched. Episode number one is on the feed right now. So head to changelaw.com slash brain science to listen, to subscribe, and to join us on this journey of exploring the human mind.
[2607.04 --> 2612.84]  Once again, changelaw.com slash brain science or search for brain science in your favorite podcast app.
[2612.84 --> 2642.82]  Okay. So let's say, um, so I've never used AutoML, um, other than just, uh, kind of browsing around the website and looking at some examples and that sort of thing.
[2642.82 --> 2664.28]  And in, in, in, in very general, uh, detail. So, um, I was wondering if you could kind of just walk, walk us through, like if I'm, if I'm going to go implement my, my first AutoML application or workflow, um, what are kind of the steps I, I go through at least with, you know, Google's AutoML tools?
[2664.28 --> 2665.28]  Yeah, yeah, yeah, yeah, yeah.
[2665.28 --> 2685.44]  Yeah, yeah, yeah. Of course. And yeah, you know, Google's not the only company that's offering these, these capabilities, but, um, but yeah, it definitely, it definitely starts with what you've been saying earlier about how, you know, you have certain language, like say you're a German doctor and you need something, you need a tool that recognizes that, that context.
[2685.44 --> 2700.36]  Or you're, you know, you know, searching for a cat and food pictures is general, but maybe you're a automotive manufacturer and you need to, you have all this label data of car parts that isn't going to show up in the more, you know, general use cases of the pre-trained models.
[2700.36 --> 2730.34]  So what you need to do is you need to, you have this data set and you know, this data set is good and accurate. Um, what you would do in this case, let's use like, uh, I've talked a lot about tabular data, right? So we're using like spreadsheet data. Spreadsheet is something that, you know, almost everybody uses today. But in this case, what feature we're looking to establish within like a spreadsheet is the ability to say, you know, select a column in a spreadsheet and say, given all these other columns,
[2730.34 --> 2758.76]  can you predict this, like what the value of this column is going to be? And so let's say it's like a, it's, it could be categorical, it could be numerical. Like the example that I've been using a lot is, um, there's, you know, one of the open data sets that we have is like a banking, a banking data set that shows different types of, uh, banking customers and what they like, you know, things from, you know, how often they deposit to like, you know, what their income is to what kind of jobs they have.
[2758.76 --> 2782.74]  And then trying to infer which banking customer is most likely to have a, um, to turn on direct deposit. So they're going to have their paychecks directly go to the bank. And so what you would do is you would find, first of all, you know, whether it's, we talked about CSV files. We've taught, uh, of course, this is Google. So you could have your data in BigQuery and you just give it the BigQuery ID.
[2782.74 --> 2804.92]  You go to AutoML tables and you would select, you would load in that, uh, that data set. So you would import it and, you know, given all the different, so it'll be labeled. It'll be either like, you know, categories or numbers or text. And from there you have, uh, the opportunity to kind of look at the different column names.
[2804.92 --> 2827.88]  From the column names, you can then, you know, like nullify or, um, select your features. Uh, in this case, they have things like age, education, balance, housing, loans, um, things like that. And from there, you look at each of the column types and you select one to be the target. In this case, we're going to select like direct deposit.
[2827.88 --> 2845.88]  So this is like a true false, like does this person use direct deposit? Do they not? Um, then there's other analytics you can look at, right? So it gives you an opportunity to see kind of the spread or whether there's any, um, features that, or any, um, columns that have missing values or invalid values, things like that, where you can kind of remove.
[2845.88 --> 2864.52]  And this is where a data scientist said that, you know, these kinds of tools actually are very useful because they often have data. They have like lines and lines and lines and lines of data for which like some of the data might not even be valid. So being able to detect that automatically would be very useful for them. Um, from that point on, you just, you would just then train the model.
[2864.52 --> 2894.06]  And the selection you'd make there is how long you feel like training for. So you could say, I want to train usually like one hour, honestly, like for maybe like, these are approximations and it changes case by case, but like, you know, an example, right? For this case, I would say for 4,000 lines of, of input, um, you could train for an hour and you'll get a decent result. You'll get like a, you know, 95% accuracy for predicting whether or not someone has direct deposit.
[2894.52 --> 2924.40]  Once it's trained, you select that threshold. If it finishes earlier. And of course it's going to detect things like overfitting, um, when it's like just kind of reaching diminishing returns. So it will terminate early as well. Um, if it needs to, but you get like at the end of that, you get like an evaluation. So you look at, um, you know, there's the recall, there's precision, there's, uh, looking at the true positive rates and the false positive rates. There's the accuracy. So in this case, this model that I, I'm just going to pull up on right now. Uh,
[2924.40 --> 2954.40]  this model has accuracy of 91%, um, which is, you know, pretty good. Um, again, case by case, it's like, what is your use case? What is your threshold in production? Uh, and it's going to differ. It also show you feature importance, um, how the labels are doing. And you can then, uh, basically what you could deploy it right then and there. You can just deploy it within AutoML. And then it's, you know, do, you can run online predictions, you can run batch predictions,
[2954.40 --> 2984.38]  like I said earlier, you know, export it. It'll be a TensorFlow package. You can run the model in a Docker container. You can take that Docker container. You can download it onto your local machine, or you can just, you know, not do any of that and just, uh, use REST API and be able to make predictions that way. And so that, that kind of gives you kind of the end to end, uh, you know, it's basically once you load it in and you click train and the training completes, you're basically ready to, uh,
[2984.40 --> 2990.70]  you know, you once you, and you have to deploy it as well, but you're ready for online predictions after those few steps.
[2991.20 --> 3014.38]  So, so just to clarify, to make sure, um, I know like Daniel and I have come, uh, come at things from, you know, more of a framework perspective and, and using, you know, TensorFlow or PyTorch or one of the other frameworks over time. In this case that you're talking about, you're really not doing that at all, right? Your AutoML is its own process and you're selecting, uh, the data from BigQuery or, or elsewhere, pulling it in and essentially,
[3014.40 --> 3024.34]  producing a product at the end in the form of a model that you can go use. Is that fair that it is a parallel path versus an integrated path with whatever framework you're using?
[3024.58 --> 3044.26]  Absolutely. Yeah. It's, you're loading the data, you click a button, it says train, and then an hour later you have this model, which you kind of look at the stats for it, and then you're online after it's deployed. So it's like a few clicks. I mean, getting the data is non-trivial, I would say.
[3044.26 --> 3073.62]  And then making sure that the model's actually performing the way you wanted to is also non-trivial. But yeah, it is like a few clicks away. And then you have what you would normally do if you had like, you know, you had like maybe even like a TensorFlow notebook, right? You would still have to kind of, you still had the ability to like, you know, choose the type of approach you want to use and then, um, you know, change the values around a little bit. But in this case, you don't really have that. You get to select the target, um, of which you want to be the, what you're predicting for.
[3073.62 --> 3074.74]  But that's about it.
[3074.74 --> 3104.72]  Yeah, I definitely see what you're saying about like the expertise that's needed. Because like, if you're, if you're looking at a screen, and you're getting first of all, like, you know, a package out or a Docker container out there, like you need to understand how to work with those things or like REST API. So there's like, engineering expertise there, of course. But even if you're presented with the screen, and it says like, Oh, here's precision and recall and these different things, like, you know, there's, there has to be a level of understanding of those things.
[3104.74 --> 3129.74]  To be able to understand, you know, if your model is really doing what you want it to do, like you said, it seems like there's like, if I think about a my AI workflow or machine learning workflow, there's, of course, always the data side of things, which is still going to be, in some cases hard, like you're saying here, because like, you know, the data quality is going to influence things.
[3129.74 --> 3145.86]  There's the training process, which, you know, if you do it manually might involve like you were saying hyper parameter tuning, like trying out a bunch of different architectures or models and that sort of thing, to where you get something that works, then you have to, you know, evaluate that and then put it into production.
[3145.86 --> 3156.12]  It seems like here there's, you know, like you're really greasing the wheels around that training process side of things where you don't have to think as much about the architecture, the specific model, the hyper parameters.
[3156.12 --> 3167.04]  And then you're also helping a bit in terms of like, you know, of course, like productionizing that in the sense of making a REST API available and that sort of thing.
[3167.04 --> 3177.90]  So you can spend a lot more time thinking about the data and the type of model that you want out rather than those sorts of architectures and other things.
[3178.64 --> 3179.74]  Yeah, that's totally it.
[3179.76 --> 3187.24]  That's the idea is to make that more accessible, to give people the opportunity to kind of use it at that level of abstraction.
[3187.24 --> 3199.88]  But like, I think I think in some point we're trying to look at like, you know, that full the full sense of like how much control and what kind of control we want to have in as we create these models as well.
[3200.50 --> 3206.74]  Cool. Yeah. So to kind of wrap up here, I think this has been great to I mean, I've learned a lot going through this.
[3206.74 --> 3210.30]  Me too. And definitely want to like try out some of these things.
[3210.30 --> 3229.42]  So I guess ending, you know, to kind of end up with some useful things is wondering if you could just kind of recommend like so thinking about someone that's maybe wanting to try out these sorts of AutoML techniques, what the kind of easiest way for them to try out those things are.
[3229.42 --> 3237.96]  Maybe there's tutorials or like, you know, notebooks or I don't know what the interface is to try those things.
[3237.96 --> 3252.34]  And then also if people are interested in kind of learning generally about like maybe the methods behind AutoML and like working on those, you know, like learning to learn things and hyper parameter, automated hyper parameter tuning.
[3252.34 --> 3256.12]  If there's any kind of specific places that that you could point them to.
[3256.12 --> 3266.26]  So, yeah, for people who want to know about like AutoML in general, I mean, the Google AI, the portal, they link to one of the groups.
[3266.26 --> 3273.80]  The researcher that one of the researchers that I hear a lot of working in this area is Kwok Le.
[3274.20 --> 3279.28]  He's a Google brain research scientist that has a team of people working in auto machine learning.
[3279.38 --> 3289.82]  So anything under him, any of his publications, I think would give you kind of an understanding of the state of the art within that area for people who want to try it out.
[3289.82 --> 3301.30]  So if you go to cloud.google.com slash AutoML, it'll kind of bring you to, you know, all things AutoML that is available as tools for people to use.
[3301.30 --> 3306.42]  It gives you kind of a list of the different applications or verticals.
[3307.08 --> 3311.30]  There's like, you know, site where you have AutoML vision, AutoML video intelligence.
[3311.54 --> 3313.72]  So this is, again, you're providing your own label data.
[3314.24 --> 3315.24]  There's language.
[3315.52 --> 3320.10]  So AutoML natural language, AutoML translation, and then structure data, which is what we talked about today.
[3320.24 --> 3321.08]  AutoML tables.
[3321.60 --> 3327.54]  There's a few like customer testimonies where you can see how it's being used and and a little bit of a description.
[3327.54 --> 3334.10]  And then you'll find if you go to structure data, there's a there's a there's a video narrated by me.
[3334.32 --> 3337.78]  I pulled together this video for explaining kind of the basics of it.
[3338.12 --> 3341.54]  But if you want to try it, there's a again, you would choose from those categories.
[3341.54 --> 3345.40]  And so if you choose, you know, AutoML tables, there'll be the opportunity.
[3345.56 --> 3348.08]  It'll kind of pull up the UI in the cloud console.
[3348.22 --> 3351.18]  So, of course, you'll have to have like a Google Cloud platform account.
[3351.18 --> 3357.96]  But you do get some you get you could train for free for up to a certain amount to kind of try it out for yourself.
[3357.96 --> 3360.40]  And then actually the cost isn't very much.
[3360.78 --> 3364.18]  I'm not on the sales side, so I actually don't know the exact numbers.
[3364.62 --> 3373.18]  But every time I've talked to like a solutions engineer and heard them quote, you know, it's like very low amounts of money once it actually once you actually want to get it going.
[3373.84 --> 3377.54]  But yeah, I do know that there's a free there's amount that you get to use for free.
[3377.54 --> 3382.16]  So if you just want to check it out, try it out yourself, it's pretty accessible.
[3382.60 --> 3393.06]  And and even if not that, if you want to even, you know, try some of the pre trained APIs like, you know, like you want to upload a cat picture and see if it knows your cat is a cat.
[3393.92 --> 3395.86]  You can just do that within the web.
[3395.98 --> 3402.48]  So if you just want to like see how well these pre trained ones work, they have like online demos like within the website as well.
[3403.18 --> 3405.18]  Awesome. Well, thanks for pointing those things out.
[3405.18 --> 3408.00]  We'll definitely share those in in the show links.
[3408.00 --> 3410.98]  So make sure and check out the show links.
[3411.34 --> 3420.20]  We'll we'll put those links there and you can try out AutoML and definitely consider joining our community somehow.
[3420.20 --> 3423.60]  So you can go to changelog.com slash community.
[3423.92 --> 3431.10]  And we have a Slack team where you can chat about AutoML and practical AI and all those things.
[3431.10 --> 3435.20]  We also are active on Twitter and LinkedIn.
[3435.60 --> 3436.92]  So make sure you engage with us.
[3437.00 --> 3442.76]  Tell us what you're using AutoML for or where you found it useful or what research you're interested in.
[3443.20 --> 3446.20]  But thank you so much, Cheryl, for for joining us.
[3446.46 --> 3447.86]  Really great conversation.
[3448.14 --> 3454.52]  It was really great to hear your story, hear about some of the things you're doing and the things Google is doing in AutoML.
[3454.68 --> 3455.82]  So thank you for taking time.
[3456.22 --> 3456.68]  Thanks a lot.
[3457.00 --> 3457.86]  Yeah, thank you.
[3457.86 --> 3460.68]  All right.
[3460.74 --> 3463.36]  Thank you for tuning into this episode of Practical AI.
[3463.64 --> 3465.08]  If you enjoyed the show, do us a favor.
[3465.20 --> 3465.78]  Go on iTunes.
[3465.90 --> 3466.60]  Give us a rating.
[3466.86 --> 3468.72]  Go in your podcast app and favorite it.
[3468.84 --> 3471.54]  If you are on Twitter or social network, share a link with a friend.
[3471.62 --> 3472.30]  Whatever you got to do.
[3472.50 --> 3473.98]  Share the show with a friend if you enjoyed it.
[3474.28 --> 3476.94]  And bandwidth for changelog is provided by Fastly.
[3477.06 --> 3478.48]  Learn more at fastly.com.
[3478.68 --> 3481.88]  And we catch our errors before our users do here at changelog because of Rollbar.
[3482.10 --> 3484.50]  Check them out at rollbar.com slash changelog.
[3484.50 --> 3487.32]  And we're hosted on Linode cloud servers.
[3487.66 --> 3489.28]  Head to linode.com slash changelog.
[3489.36 --> 3489.82]  Check them out.
[3489.90 --> 3490.74]  Support this show.
[3491.14 --> 3494.34]  This episode is hosted by Daniel Whitenack and Chris Benson.
[3494.78 --> 3496.84]  The music is by Breakmaster Cylinder.
[3497.26 --> 3500.66]  And you can find more shows just like this at changelog.com.
[3500.84 --> 3502.80]  When you go there, pop in your email address.
[3503.10 --> 3509.10]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[3509.52 --> 3510.26]  Thanks for tuning in.
[3510.44 --> 3511.16]  We'll see you next week.
[3511.16 --> 3512.44]  We'll see you next week.
[3513.06 --> 3513.08]  Thank you.
[3513.08 --> 3543.06]  Thank you.
