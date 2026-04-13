[0.00 --> 4.00]  cool things on Twitter, like cool, like little visualization blog posts to kind of play around
[4.00 --> 8.66]  with. I think there's a ton of good stuff out there that I kind of like playing around with.
[8.92 --> 13.72]  Transformers and NLP is an easy one. In visualizations, you see things like DeckGL
[13.72 --> 17.76]  that you can just make the coolest kind of visualization pieces around. There's a lot of
[17.76 --> 21.48]  cool stuff there. But I will tell you, part of it is, as I always tell people, they're getting
[21.48 --> 26.54]  into data science. Don't get suckered in by that. Most of the data science that's useful in an
[26.54 --> 30.20]  enterprise hasn't come out in the last three years. It's been around for much longer.
[30.52 --> 31.42]  That's a really good point.
[31.66 --> 37.14]  Don't get into reading the latest archive posts and trying to take those account because going
[37.14 --> 41.56]  back to those classic problems, those classic either Kaggle competitions or other projects,
[41.64 --> 45.58]  and learning those techniques is going to get you much further along than following the latest
[45.58 --> 46.00]  pieces.
[46.00 --> 49.34]  Don't start with GPT-3. It's your very first thing.
[49.34 --> 58.44]  Bandwidth for ChangeLog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[58.44 --> 62.98]  things here at ChangeLog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[62.98 --> 66.90]  on Linode cloud servers. Head to linode.com slash ChangeLog.
[69.72 --> 74.22]  Whether you're working on a personal project or managing enterprise infrastructure, you deserve
[74.22 --> 79.32]  simple, affordable, and accessible cloud computing solutions. So you can take your project,
[79.32 --> 85.30]  to the next level. Simplify your life with Linode's Linux VMs to develop, deploy, and scale your
[85.30 --> 91.48]  applications faster and easier. Get started on Linode today with $100 in free credit for our
[91.48 --> 96.86]  listeners. You can find all the details at linode.com slash ChangeLog. Or if you're not at your desk,
[97.04 --> 104.34]  just text ChangeLog to 474747 and get instant access to that hundred bucks. Linode has 11 global
[104.34 --> 111.14]  data centers and provides 24-7, 365 human support with no tiers or handoffs, regardless of your plan
[111.14 --> 116.56]  size. In addition to shared and dedicated compute instances, you can use that $100 credit on S3
[116.56 --> 123.22]  compatible object storage, manage Kubernetes, and more. Visit linode.com slash ChangeLog and click on
[123.22 --> 130.34]  the create free account button to get started. Or just text ChangeLog to 474747. Get started today on Linode.
[130.34 --> 144.58]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive,
[144.96 --> 149.14]  and accessible to everyone. This is where conversations around AI, machine learning,
[149.24 --> 153.84]  and data science happen. Join the community and Slack with us around various topics of the show
[153.84 --> 158.40]  at ChangeLog.com slash community and follow us on Twitter. We're at Practical AI FM.
[158.40 --> 170.28]  Welcome to another episode of the Practical AI podcast. I'm Chris Benson, a principal emerging
[170.28 --> 174.46]  technology strategist at Lockheed Martin. And with me, as always, is Daniel Whitenack,
[174.54 --> 178.56]  who's a data scientist with SIL International. Hey, how's it going today, Daniel?
[178.84 --> 186.80]  It's going really good. It's a beautiful day here in Indiana. And this weekend, I know in the last
[186.80 --> 192.90]  couple of times we've started out the podcast, I've had a few projects like, you know, tech projects,
[192.90 --> 197.36]  like the network at my wife's business and those things. You always got something going on.
[197.36 --> 202.90]  I always got some sort of tech. But this weekend was like, I was outside most of the weekend. So
[202.90 --> 210.72]  took a hike and then had a bonfire at my wife's family's place and birthday party. And so we were
[210.72 --> 216.50]  outside most of the most of the weekend, which was kind of nice, nice break from being in front of a
[216.50 --> 221.18]  screen. I'm so jealous because as we record this, we just came out of the weekend where Hurricane
[221.18 --> 227.70]  Delta came in off the Gulf. And so we have had torrential rains all weekend inside, not fun,
[228.22 --> 232.06]  that kind of stuff. Yeah, not good. So I'm looking forward to sunny weather coming up.
[232.06 --> 239.04]  Yeah, I also tried out this. There's an app called iNaturalist. And you like take pictures of
[239.04 --> 244.88]  like birds or plants or other things. And there's like a whole like crowdsource community on there
[244.88 --> 249.40]  that will help you like identify what you're looking at and that sort of thing. My wife and I,
[249.90 --> 255.36]  both in the spring and through the summer and fall, we like to go mushroom foraging. And I've tried
[255.36 --> 261.94]  like all sorts of different apps that try to identify. It seems like something that should be like,
[262.06 --> 267.58]  totally doable. But there's definitely a user risk in that as well. So talking about like a
[267.58 --> 271.42]  classification model and the risk associated with it, that's a pretty high one.
[272.28 --> 276.38]  Yeah, I was I was thinking that as you were saying that I was thinking if I was doing that,
[276.38 --> 282.80]  I would either end up dead, or I would end up with an inappropriate level of something I shouldn't
[282.80 --> 288.30]  have in my body. Definitely. So yeah, so it's cool to find this iNaturalist thing. It's like a citizen
[288.30 --> 295.80]  science sort of deal. And yeah, if you're interested in like, you know, plants and animals and, you know,
[296.04 --> 301.56]  fungi and that sort of thing, it was pretty cool to find that. So joking aside, I actually do have
[301.56 --> 306.76]  that app. Yeah, wonderful. I've been using it for a while. So I like it a whole lot. Yeah, for me,
[306.76 --> 311.26]  I'm just like, I'm hoping for good weather here. I'm excited. I got to tell you something tomorrow,
[311.26 --> 315.78]  by the time this comes out, it'll have just been in the past, but I believe a recording will be
[315.78 --> 321.90]  available. I'm giving the keynote at an IEEE conference tomorrow. Oh, cool. Congrats. Yeah,
[321.98 --> 327.40]  it's the Digital Avionics Systems Conference. And I will be doing artificial intelligence and
[327.40 --> 333.10]  autonomy state of the union, which is kind of ties where the entire science of autonomy and the
[333.10 --> 337.00]  sciences of artificial intelligence come together and where they intersect and where they don't.
[337.00 --> 340.64]  Cool. Can well, you know, do you know if the that will be posted online?
[340.64 --> 345.32]  I think it will. I'm going to check. And if so, I will certainly include it in the show notes.
[345.56 --> 352.20]  Cool. Yeah. Excited to listen. So we have a very exciting guest today based on reading some of the
[352.20 --> 359.20]  stuff online on Twitter that we've looked at. Today, we have Rajiv Shah, who is a data scientist at Data
[359.20 --> 364.62]  Robot. He's an AI researcher, and he's also a professor at the University of Illinois at Chicago.
[365.00 --> 367.98]  Welcome to the show, Raj. Thank you very much. Thank you for having me.
[367.98 --> 375.60]  So wondering if, before we dive in to our topic today, which is going to be all about
[375.60 --> 380.92]  leaking information from your training and data sets, if you could tell us a bit about your
[380.92 --> 386.94]  background and kind of how you got to this point. Like a lot of early folks kind of into data science,
[387.00 --> 392.60]  I probably have a long kind of meandering journey. But partly I started off as an engineering
[392.60 --> 398.80]  undergraduate, didn't want to do engineering, went off, studied law, ended up with a PhD in
[398.80 --> 404.52]  communications where I ended up kind of studying just that intersection between technology and people
[404.52 --> 409.84]  was just really interesting and solving a lot of interesting research questions. And I used kind of
[409.84 --> 415.68]  various methods, both qualitative and quantitative methods to kind of solve these problems. And, you know,
[415.68 --> 419.46]  this was at the time the internet was booming. So there was a lot of interesting questions around that.
[419.46 --> 425.40]  I did that for a while, kind of moved out of academia. I was a sysadmin for a number of years,
[425.46 --> 430.12]  so worked in IT. And then this data science thing came around. And I was like, hey, wait a minute,
[430.42 --> 435.50]  right? Like I have a little bit of a background in math. And my social science background had taught
[435.50 --> 441.12]  me like how to ask interesting research questions and kind of probe them. And then the nice thing is
[441.12 --> 445.52]  Andrew Ng made these wonderful courses. And I was able to kind of skill myself up on some of the newer
[445.52 --> 450.74]  algorithms and approaches that I hadn't learned. And so that was kind of my introduction to data
[450.74 --> 455.40]  science and landed my first data science job at State Farm and worked there for a couple of years,
[455.48 --> 459.78]  went over to Caterpillar, worked there as a data scientist, and now I'm over at DataRobot.
[460.30 --> 465.98]  So just out of curiosity, was that his original machine learning course by any chance?
[466.44 --> 469.10]  Well, yes, it was his original machine learning course. Yes.
[469.10 --> 475.24]  I did the same one. It was kind of the first big, major deep learning course that he put out there.
[475.34 --> 479.12]  And I think it started a lot of us down this path in a professional context.
[479.98 --> 482.70]  Yeah. I can't say I finished the course, but yeah.
[483.28 --> 486.36]  Understood. It was a hard course. I remember it kicked my rear.
[487.08 --> 489.14]  Yeah. No, he has a great knack for explaining things, right?
[489.40 --> 489.86]  He does.
[490.54 --> 493.06]  His side gig was starting Coursera. So you got to like that.
[493.06 --> 498.92]  Do you find that you're sort of like with that background thinking about people and technology,
[498.92 --> 506.00]  which is, it seems super relevant to AI specifically in terms of like, you know,
[506.00 --> 512.14]  I'm thinking there's a lot of interesting thought around, you know, augmenting humans with AI,
[512.14 --> 516.14]  but also systems like, you know, if we're talking about like active learning or something,
[516.14 --> 522.84]  which I think is extremely powerful where, you know, you are sort of having a human in the loop
[522.84 --> 529.72]  with these systems. Has that made you think maybe more about those or brought a fresh perspective on
[529.72 --> 533.56]  those as opposed to just, you know, kind of thinking about the tech side of it?
[534.18 --> 539.32]  Yeah. So it really helps me to like, remember how kind of socially grounded everything is.
[539.42 --> 543.82]  I think one of the valuable things of where you do a PhD and you collect your own data,
[543.82 --> 549.50]  you end up with kind of learning some skepticism towards kind of quantitative data because you
[549.50 --> 554.48]  realize like how it's collected, like what was the questions asked? Like how does that formed on
[554.48 --> 558.74]  the survey, right? You know, how did they handle the missings? All those different types of things
[558.74 --> 564.34]  that we often just accept when we're running algorithms. And so kind of having that understanding
[564.34 --> 569.06]  is really strong. The other pieces that's really kind of come around now in data sciences,
[569.48 --> 573.48]  I think there's a movement in data science away from just focusing on algorithms,
[573.48 --> 579.54]  but thinking about the entire value chain going from your raw data to how you finally use that
[579.54 --> 584.14]  model in a production setting, as well as the larger questions, like how does that interact
[584.14 --> 588.38]  with the rest of the organization? How does that interact with the rest of society where now,
[588.80 --> 593.60]  right? I mean, we see now at conferences where they're being asked to say, you know, yes,
[593.60 --> 598.14]  you can tell us about how you solve the problem, but we also want to know what are the larger
[598.14 --> 603.60]  social, political, economic impacts of your research and wanting researchers to be cognizant
[603.60 --> 603.92]  of that.
[603.92 --> 610.12]  Yeah. And of course that dips definitely into, you know, you mentioned a little bit of a background
[610.12 --> 616.68]  in laws as well. And of course that dips into like, you know, ethics and of course, governance and all
[616.68 --> 624.06]  of those things, which we're seeing a definite surge in. And I'm guessing that you have thoughts there
[624.06 --> 630.82]  with that background, but it's really interesting to hear your perspective coming from that background.
[630.82 --> 639.58]  And have you found very many sort of other people in data science coming from communications or from
[639.58 --> 648.16]  law? You know, I hear a lot coming from, you know, maybe engineering or science or, you know, math or
[648.16 --> 652.44]  physics or whatever it is. Are people surprised when they hear about your background?
[653.14 --> 656.44]  A little bit, but I think there's a few people about kind of coming in this way, right? I mean,
[656.62 --> 660.80]  you had Patrick Hall on kind of a couple of weeks ago, right? Talking about, you know,
[660.80 --> 665.10]  what are the implications that data scientists or their people that are owning the data science
[665.10 --> 671.22]  products need to think about within liabilities within an organization? So for me, it's kind of
[671.22 --> 676.92]  natural as data science expands, where now the decisions that we're making are really impacting
[676.92 --> 681.06]  organizations and society that, hey, there's a lot more people that are going to be involved
[681.06 --> 683.72]  and kind of giving scrutiny to what's going on.
[683.72 --> 690.14]  Yeah. Well, I'm curious, maybe kind of from that perspective, how did this topic, you know,
[690.20 --> 694.20]  Chris mentioned that we're going to be talking about this topic a little bit today about data
[694.20 --> 700.20]  leakage. How did this topic come to the forefront of your mind? How did it become something that you
[700.20 --> 701.12]  started thinking about?
[701.52 --> 708.14]  Yeah. I mean, so target leakage is a very common problem in data science. I think most data scientists
[708.14 --> 712.76]  who've been out there practicing for years, they know it, they're aware of it. They know that,
[713.06 --> 718.94]  and just to kind of level set for everybody, what target leakage is, is when you use information
[718.94 --> 724.66]  from the future when you're making a prediction. It's a very common problem that can occur. And
[724.66 --> 730.84]  so a simple way that it might occur is you're building an HR model. You want to predict what the
[730.84 --> 737.02]  salary is going to be for kind of your new computer, your CS hires. And you build a model,
[737.02 --> 742.54]  you take on all their background, and it spits out a number and says, this is what my the annual
[742.54 --> 748.44]  salary should be for this particular person. But now, what happens if when you're predicting annual
[748.44 --> 754.36]  salary, one of the variables you used was the monthly salary, because remember, you start off
[754.36 --> 760.14]  with historical data from the past. And especially in an enterprise setting, it's easy, you have lots of
[760.14 --> 764.44]  features and variables in the data sets, you grab them. And you might have something that's entirely
[764.44 --> 769.78]  related to your target, when you're building the model. So it's kind of leaking that future
[769.78 --> 774.78]  information into your model. The great thing is, is when you're building this, the model looks
[774.78 --> 779.70]  flawless, right? Often when you have target leakage, the performance of your model looks really good.
[780.38 --> 784.24]  And it's only when you actually put it into production, you realize, wait a minute, I don't
[784.24 --> 788.78]  have that monthly number, right? Like, it's always missing now. And your model all of a sudden doesn't
[788.78 --> 794.58]  look nearly as good as when you were training it. And so this is kind of the fundamental problem.
[794.58 --> 799.86]  And it happens in many particular ways, where essentially kind of your model cheats a little
[799.86 --> 803.40]  bit, and kind of gives you performance that's really misleading.
[804.20 --> 809.62]  Is this something that happened to you personally, as you were starting to get into data science,
[809.62 --> 815.04]  where you had some of these experiences, maybe where you had to answer for a production model
[815.04 --> 820.34]  that was having issues? So it didn't happen to me before, all the way at the level of a production,
[820.50 --> 826.84]  but I see it all the time. I mean, my kind of intuitive guess is like 75% of all data science
[826.84 --> 833.24]  models, at one point have some target leakage. Now, typically, right, as you're kind of building
[833.24 --> 837.50]  the models, hopefully you're debugging it and trying to understand how well the model's working,
[837.78 --> 843.22]  right, using your explainability and interpretability tools. And hopefully with that,
[843.22 --> 849.22]  and some domain expertise, right? This is where as a data scientist, you really have to understand
[849.22 --> 854.18]  what the data elements are in your model. If you don't, right, it's very easy to fall into target
[854.18 --> 861.04]  leakage. But with those, usually, right, most of the time, 99 out of 100 times, those errors are caught,
[861.18 --> 863.50]  hopefully before you finally get to production.
[864.46 --> 869.94]  So what was it? Because as we're all working in this space and stuff, you've really put some thought
[869.94 --> 874.86]  into this, and you've really noticed it, you've probably more than most have, what really oriented
[874.86 --> 880.56]  you on this particular issue? Because it's fascinating. But I'm not sure it's something
[880.56 --> 887.16]  many of us pay attention to very well up front. And so what kind of got you focused on this in
[887.16 --> 889.70]  particular, along this this line of thought?
[890.42 --> 894.66]  So I really like data science. And one of the things I like to do is often is,
[894.66 --> 899.72]  when I see other interesting projects that are out there, I like to rerun them and just try to
[899.72 --> 903.84]  understand, like, how did they solve this problem? What did they use? I mean, for me, I have a hands
[903.84 --> 908.62]  on learning style. And it's just much better to kind of be in the data and with the code, rather than
[908.62 --> 915.42]  just reading a page of formulas. And I remember years ago, Chicago was one of the leaders of open
[915.42 --> 922.86]  data. And they put forth a model for predicting kind of restaurant inspections. The idea was, we want to
[922.86 --> 927.58]  figure out and sign our inspectors to go to restaurants that likely were going to fail
[927.58 --> 932.48]  inspections versus ones that aren't, right? Inspectors are rare resources, we want to just
[932.48 --> 938.26]  allocate them efficiently. And I remember when I went through that model, they had a couple pieces
[938.26 --> 943.44]  of target leakage. One is they used weather. Weather is, if you're building a model that you're
[943.44 --> 947.38]  predicting way out in the future, often you don't actually have the actual weather, what's going to
[947.38 --> 951.90]  happen a month from now, for example, right? So that's a form of kind of target leakage that can happen.
[951.90 --> 958.42]  And they also had a more subtle thing where they were using the inspector ID information in their
[958.42 --> 965.04]  model. And the reason this was target leakage is because in the past, some inspectors often
[965.04 --> 970.76]  kind of were very easy inspectors, some were really harsh, I'll find everybody. But when they actually
[970.76 --> 974.80]  were going to deploy this model, they wouldn't know what inspector was likely to go to the restaurant.
[975.38 --> 979.38]  And so going through this process, I realized like, wait a minute, they made a mistake. And I talked to
[979.38 --> 983.20]  the folks in Chicago, and the actual model they implemented was a bit different than what they
[983.20 --> 988.86]  had shared publicly. But it kind of got me attuned to, you know, these types of problems happen if we
[988.86 --> 995.06]  kind of don't carefully scrutinize the data. And then just along the way, I see it routinely when
[995.06 --> 999.78]  I work with other customers, where they bring in their models, we walk through them, I'm like,
[999.84 --> 1003.88]  wait a minute, like, this variable is really good. Should this be in the model? And then somebody thinks
[1003.88 --> 1007.56]  about it, and they're like, oh, no, you know, you're right. Like, that shouldn't be in the model.
[1007.76 --> 1012.94]  That's leakage. You see it in Kaggle competitions, right? If you look at the history of Kaggle
[1012.94 --> 1017.16]  competitions, there's many Kaggle competitions where along the way, they discovered target
[1017.16 --> 1022.36]  leakage, and they're like, oh, we have to redo the competition. Or the competitors all use the target
[1022.36 --> 1028.48]  information and make these unrealistically good models as part of the competition. And then the one
[1028.48 --> 1034.48]  that really highlighted it to me was there was an article in Nature studying aftershocks. So kind
[1034.48 --> 1040.04]  of earthquakes, and you have aftershocks. And the great thing was the researchers put the data out
[1040.04 --> 1045.14]  there, they put their code out there. So I was able to kind of play around with it. And once I started
[1045.14 --> 1050.06]  looking at it, there's kind of some funny things that kind of made me a little concerned. One thing
[1050.06 --> 1054.82]  is, is whenever I see a paper, and I don't see a baseline model, that always concerns me, right? This is
[1054.82 --> 1061.50]  kind of for me, a data science best practice is, before we kind of jump into using fancy deep
[1061.50 --> 1066.20]  learning methods, like, what does a simple model do, right? We do this if we're working, whether
[1066.20 --> 1071.32]  we're doing a time series problem, or kind of, if an enterprise has a rule based system, right? Let's
[1071.32 --> 1076.80]  find out like, if we just do the bare minimum, like, what the starting point is. And then we can see,
[1077.44 --> 1082.30]  hey, now I'm going to apply this fancy data science methods and see how much of an increase I can get.
[1082.52 --> 1083.18]  Does that sound fair?
[1083.18 --> 1083.80]  It does.
[1084.22 --> 1088.24]  And so that was one issue that I kind of had with the paper. The other issue when I started looking
[1088.24 --> 1095.18]  at it was how they had organized and partitioned their data. So within data science, typically,
[1095.74 --> 1103.02]  there's an assumption often that the rows of our data are not related to each other. And so what
[1103.02 --> 1107.76]  happened in this case was some of those aftershock earthquakes actually happened near the same time
[1107.76 --> 1114.14]  near the same place. And so I made the assumption, well, if you treat them like they are related to
[1114.14 --> 1119.26]  each other, we can still solve the same problem, we can still use data science. But what we use is a
[1119.26 --> 1123.98]  different partitioning method. We organize the data differently when we're training the models,
[1124.48 --> 1128.34]  right? Typically, kind of the default you'll see is pretty much every blog post out there
[1128.34 --> 1133.38]  goes with random partitioning, right? All your rows of your data are the same, it doesn't matter
[1133.38 --> 1139.26]  where we put them. But the reality is, as often in a lot of problems, there's some relationships in
[1139.26 --> 1146.12]  your data. Maybe, for example, you have data and it's broken up by state. So you have a bunch of
[1146.12 --> 1151.20]  observations for Texas, and you have a bunch of observations for Florida. And what happens is,
[1151.26 --> 1155.92]  is there's some regional variations that if you know something about a little bit about Texas,
[1155.92 --> 1160.18]  you can probably make a pretty good assumption what the next person from Texas is going to do.
[1160.18 --> 1166.50]  And so what happens then is, when we randomly distribute this data, and we put some of Texas
[1166.50 --> 1172.30]  data in our test, kind of where we want to see if our data will generalize to, the model can very
[1172.30 --> 1178.08]  easily cheat. It can say, hey, this is what I know about Texas versus all the other characteristics that
[1178.08 --> 1184.38]  we really want the model to learn from. And there's an easy remedy. It's something called group partitioning,
[1184.42 --> 1189.12]  where we just make sure all the Texas information stays together in one partition when we train,
[1189.12 --> 1194.58]  all the Florida information stays together in one. It's a very simple thing to do. It takes a little
[1194.58 --> 1199.74]  bit of extra data science work to think about it and to kind of code it up. But then you can run it
[1199.74 --> 1205.46]  and see, hey, is there a big effect? Is there an effect of this state, you know, that is actually
[1205.46 --> 1210.92]  kind of leaking information as I'm solving it? Okay, I said a lot, I kind of want to make sure you guys
[1210.92 --> 1215.74]  are with me on this so far. Definitely. That was good. Thank you. You know, and that's what brought me
[1215.74 --> 1219.82]  back in this Aftershocks one is that's what I noticed is that there was some type of kind of
[1219.82 --> 1224.96]  leakage going on. And for me, the big issue isn't that there's leakage. I mean, like I said, it happens
[1224.96 --> 1230.42]  all the time. Most data science teams haven't. And I hopefully, I mean, most data science teams have
[1230.42 --> 1235.40]  confronted leakage. I think most of us who have experienced data science, it's not a big deal.
[1235.40 --> 1241.22]  It happens all the time, right? It's nothing to be embarrassed about. You fix it, you move on. And
[1241.22 --> 1246.06]  you've learned, right? Just another kind of data science battle scar that you have. And you've
[1246.06 --> 1250.50]  learned from that. But my concern in this one case was, you know, this got to an article that was
[1250.50 --> 1255.92]  published. When I brought up the issue, it wasn't like we were on the same data science team and
[1255.92 --> 1259.84]  we're like, oh, shoot, let me fix that. Let me rerun the results and see, is it going to make a
[1259.84 --> 1265.16]  difference or not? But there was quite a bit of pushback. And so for me, this brings up kind of the
[1265.16 --> 1270.26]  larger concern about as we welcome more people into using our data science tools and techniques,
[1270.26 --> 1275.78]  which I'm all for, right? I work for an auto ML company, right? The goal is to kind of make data
[1275.78 --> 1281.48]  science available to a much larger set of people. But how at the same time can we balance and make
[1281.48 --> 1286.96]  sure that folks kind of learn some of these fundamental concepts and best practices for
[1286.96 --> 1293.40]  how to do data science and solve these problems? So I'm curious, with this particular problem, it seems
[1293.40 --> 1302.48]  at least in some cases, like one of those things like you may not be able to like deduce or it may
[1302.48 --> 1307.68]  not be obvious to you up front when you're when you're first like creating a model and trying to
[1307.68 --> 1314.62]  solve a problem where you might be having data leakage. It's sort of like you see some weird behavior
[1314.62 --> 1320.74]  afterwards or you see like degradations in your production model or you see some maybe suspicious
[1320.74 --> 1326.80]  evaluation results and that might trigger you to kind of dig in deeper. And we can dig into those
[1326.80 --> 1331.60]  here in a second, like kind of detecting where you're leaking. But are there ways up front as you're
[1331.60 --> 1337.68]  getting into a problem that you could kind of set yourself up for success, you know, before you have
[1337.68 --> 1344.86]  to kind of retrospectively debug where you have leakage? No, absolutely. And I think part of it is just
[1344.86 --> 1350.02]  that good problem framing up front. Data scientists, I think, are getting much better about this. But
[1350.02 --> 1354.36]  thinking about what is the problem? What are you trying to solve? How are you going to implement
[1354.36 --> 1358.84]  this at the end of the day? Right? What is the data looking like? What are the production systems that
[1358.84 --> 1365.60]  are coming in? Right? So a common problem that often happens is data gets updated in databases all the
[1365.60 --> 1371.72]  time. And if you're not using kind of snapshots, your model could fail to that. You could fail because of
[1371.72 --> 1377.54]  that. So let me kind of explain that. So imagine you're doing a model on claims and you're using
[1377.54 --> 1383.54]  the text of the claims. Well, if the text of the claims is constantly being updated during the
[1383.54 --> 1388.66]  lifecycle of the claims from when it was taken to when the final process was, well, that information
[1388.66 --> 1393.34]  is changing over time. So hopefully you have that conversation when you're setting up the model
[1393.34 --> 1398.80]  and the project and being like, hey, is this data that I'm using at training time? Are the fields
[1398.80 --> 1404.62]  going to be the same as when I actually go and set up my production pipelines at the time of prediction?
[1405.40 --> 1409.84]  So I think a lot of this can be addressed by just thinking through and having the domain experts
[1409.84 --> 1414.16]  and knowing what the data looks like at the time of prediction. Does that help?
[1414.54 --> 1420.16]  Yeah, it does. I'm wondering, like, how do you connect this also? Like, is this connected to,
[1420.48 --> 1425.76]  like you were talking about partitioning your data? And, you know, there's a lot of talk when you first
[1425.76 --> 1431.78]  learn data science about training and tests and holdout sets and, like, cross-validation.
[1431.78 --> 1441.12]  And you talked about this sort of group partitioning. Is there one or is it sort of a case-by-case basis
[1441.12 --> 1446.96]  in terms of, like, every project you do, you should consider what unique partitioning is?
[1447.44 --> 1453.36]  A lot of data scientists sort of just use one-size-fits-all, basically. Like,
[1453.36 --> 1458.80]  cross-validation is easy because I can just write this, like, one-liner in my code and then,
[1458.88 --> 1465.00]  like, I'm set for not overfitting, right? So do you have any thoughts on that?
[1465.52 --> 1468.72]  And you might want to define a couple of those things along the way, by the way,
[1468.76 --> 1470.62]  for listeners who may not be familiar with everything.
[1471.48 --> 1475.58]  Yeah, no, so that's great. And it kind of gets to, right, are there some good best practices I
[1475.58 --> 1480.88]  could use for avoiding target leakage, right? And one of them is, what is my default partitioning
[1480.88 --> 1484.90]  scheme, right? When I get the data, right, we talked about the issues with the random.
[1485.50 --> 1490.86]  How can I do it? Well, I think kind of the general best practice for data science is to use
[1490.86 --> 1497.06]  a technique called nested cross-validation, where what you do is when you partition your data,
[1497.50 --> 1501.90]  you're making sure that you kind of break this up into, I don't know if I can
[1501.90 --> 1507.84]  sufficiently define nested cross-validation, into kind of different folds. But what we want to do is
[1507.84 --> 1512.64]  make sure there's different data that we're using for both the validation, as well as the
[1512.64 --> 1516.68]  hyperparameter tuning of the models. That's another subtle thing that can come into play.
[1517.20 --> 1522.80]  So this is where kind of, for folks that aren't new, I just have them set, right, nested cross-validation
[1522.80 --> 1527.54]  is the default. It's a pain in the butt to code up, but it's kind of gets you in the best place.
[1528.32 --> 1533.46]  But kind of like we said with the aftershocks, that's not 100% bulletproof. I mean, this is where
[1533.46 --> 1538.00]  you still want to have folks that understand a little bit about data science and have been burned
[1538.00 --> 1543.36]  and are just very skeptical. I think one of the takeaways is always to be skeptical of your model
[1543.36 --> 1549.34]  and its performance and think about what else could it be that's going wrong. Because otherwise,
[1549.42 --> 1551.82]  it's going to happen when you go to move it to production.
[1552.48 --> 1557.54]  Absolutely. And as you were talking about that, I was also thinking like, on the aside, you know,
[1557.54 --> 1562.44]  at least you have a lot of the control as you're busy doing the, you know, planning out the model and
[1562.44 --> 1568.30]  figuring out your training data and you can find those things and correct them. When you're dealing
[1568.30 --> 1572.16]  with the production environment or maybe planning at the stage for the production environment,
[1572.68 --> 1578.00]  how can you apply this line of thinking to that effectively, especially if maybe you don't have
[1578.00 --> 1582.92]  control of that, you know, exclusively? You may be working with, you know, infrastructure people,
[1583.18 --> 1588.58]  database people, all sorts of different ties. Even if you've recognized it for training,
[1588.58 --> 1592.60]  how do you get it out into the real world and accommodate these same issues?
[1593.26 --> 1599.28]  I've seen far too many models that data scientists have made that haven't accounted for all the
[1599.28 --> 1603.72]  production issues that end up just sitting on laptops that never actually get put into production.
[1604.04 --> 1609.38]  So even if it's a pain to deal with those IT folks on that and figuring out those pipelines,
[1609.52 --> 1615.16]  what data they have, getting snapshots of real production data, you got to do it. It's the only way to
[1615.16 --> 1620.42]  actually get your model in there. I realize, right, lots of data scientists would rather just sit on
[1620.42 --> 1626.00]  their laptop, be handed some data and just kind of plug away at it. But if your goal is to actually
[1626.00 --> 1631.64]  bring value to the organization, to get models implemented into production, like you got to have
[1631.64 --> 1637.42]  those conversations and figure that stuff out. And it's much better to do it earlier before you have,
[1637.62 --> 1642.36]  you know, you or your team spending time kind of looking at these models than doing it.
[1642.36 --> 1651.28]  So let's say that I've tried at least to, you know, use some reasonable partitioning scheme.
[1651.78 --> 1657.70]  I've tried to do the best that I could, but I put my model into production and I detect that there's
[1657.70 --> 1665.52]  something suspicious going on. How would you go about sort of retroactively looking into this
[1665.52 --> 1672.20]  issue of leakage? Like it could be other things, right? There could sort of be like model drift or
[1672.20 --> 1678.40]  something where like, you know, the state of your data was one way and then like, you know,
[1678.46 --> 1683.74]  something fundamentally changed about, you know, the data or the problem or the time period or
[1683.74 --> 1688.22]  whatever. And you've got some sort of drift of the performance, but it could also be some,
[1688.76 --> 1692.92]  you know, like this like leakage issue or something. So how do you kind of go about that when you have
[1692.92 --> 1695.12]  to do this more on the debugging side?
[1695.76 --> 1700.34]  So one thing is, I really like that you're talking about monitoring your models and thinking about the
[1700.34 --> 1704.92]  data drift and concept drift, because I think that's an important element, right? Those things
[1704.92 --> 1709.30]  could happen and it could be entirely separate from target leakage that could be affecting your
[1709.30 --> 1715.44]  model. So yes, who knows for kind of thinking and doing that. And then, yes, then we have to start
[1715.44 --> 1720.90]  kind of taking this apart and deciphering and seeing has the data changed from the time I trained
[1720.90 --> 1725.32]  the model to when it's in production? Is that's what's causing kind of this lack of performance
[1725.32 --> 1731.84]  or going back and looking at those features? So I have a longer talk that I have on target leakage
[1731.84 --> 1735.94]  that I did with a colleague of mine, Yuri, who's who's spoken at Open Data Science Conference.
[1736.54 --> 1742.04]  And he has a kind of different categories of target leakage. So like we've talked about data
[1742.04 --> 1747.64]  partitioning as one of them. We've talked a little bit about kind of that initial set of data is another
[1747.64 --> 1753.56]  source of leakage, thinking of that example of using that correlated feature or overwriting
[1753.56 --> 1760.54]  information is often another piece there. Another example of when that can happen is if you have,
[1760.60 --> 1765.92]  for example, image data, and it has some type of labels inside it, like using the explainability
[1765.92 --> 1770.30]  tools, interpretability tools, hopefully, then you can figure that out and go back and then fix that
[1770.30 --> 1777.04]  data for that. But two other places that it often happens is feature engineering, that this is one,
[1777.04 --> 1782.66]  it's a very subtle way. But when we kind of engineer and build those features that we're talking
[1782.66 --> 1788.68]  about decoding and deciphering, often people will make the mistake of doing it and creating this
[1788.68 --> 1794.70]  feature engineering on their entire data set, right? People will do EDA on the entire data set. And that
[1794.70 --> 1800.18]  allows you to learn the ins and outs of your entire training data sets. But that also subtly leaks
[1800.18 --> 1806.94]  information now because you don't have that holdout data set that's really kind of partitioned off from
[1806.94 --> 1811.34]  you where you haven't seen it from. And so that's a real subtle one that you won't be able to catch until
[1811.34 --> 1814.58]  you really think about how they actually did the feature engineering. And they're like, oh,
[1815.10 --> 1819.56]  shoot. Yeah. So yeah, I think that's a really important point that you bring up in something
[1819.56 --> 1825.34]  that really is not stressed at all. So like, I think if I'm getting what you're saying, like,
[1825.62 --> 1830.68]  let's say that you have a data set, you have a feature and you want to know like, oh, is this
[1830.68 --> 1837.12]  normally distributed? Do I have to apply some sort of power rule to this to make, you know, fit the
[1837.12 --> 1842.74]  assumptions of a model or like what? So you could do those things and look at nice histograms or plots
[1842.74 --> 1849.52]  on your entire data set, right? So like you get your whole like customer transaction data, you do that,
[1849.78 --> 1858.02]  but then you kind of partition off and you train your model on only part of that data. But the way in which
[1858.02 --> 1866.02]  you've created those models or the transformations you've done on those features is informed by data that you're
[1866.02 --> 1872.08]  not using in training. Exactly. Yeah. So I guess, I mean, one thing you can do, of course, is, you know,
[1872.08 --> 1879.08]  when you're preparing, you can adjust your exploratory data analysis methodologies. But yeah, I could see
[1879.08 --> 1885.02]  how that one would be a really hard one to catch because it also would require, I guess, like really
[1885.02 --> 1891.76]  good documentation around how you did that feature engineering initially, which I know maybe were
[1891.76 --> 1902.20]  at least myself, not always the best at documenting things the way I should. How does that fit into this and the
[1902.20 --> 1909.00]  teams you've worked on in terms of maybe not so much the data side of things, but the process side of things? What are
[1909.00 --> 1913.90]  some of your best practices around how you document your process on projects?
[1914.68 --> 1921.54]  Yeah, no, I mean, this is a very tough one to get because so I think one of the initial Twitter thread that we were kind of
[1921.54 --> 1926.96]  talking about a month or two ago that led to this podcast was a thread by kind of Jacob Schreiber that
[1926.96 --> 1932.84]  looked at a machine learning package in genomics that it was doing this exact same thing that was using
[1932.84 --> 1938.02]  all the training data to get the insights. And then later, yes, they used cross validation, but they'd
[1938.02 --> 1942.16]  already kind of been kind of corrupted because they'd already learned everything from the training data.
[1942.66 --> 1951.02]  So solving this problem is very tricky here because it relies on your data scientists being very aware of
[1951.02 --> 1957.64]  these issues and not doing it because I think right decoding it from somebody's code is a bit tricky
[1957.64 --> 1964.16]  to kind of go back and see how they engineered their code. Did they do the proper splits? And if we start
[1964.16 --> 1969.32]  thinking about things like time series where you start having lag features, it gets really tricky to be
[1969.32 --> 1975.44]  able to diagnose and look at somebody's. It's a hard one. Yeah, I don't have a very good answer for you on the
[1975.44 --> 1981.04]  best process for it because... Well, I have another way of going about it, which I kind of put you on
[1981.04 --> 1986.14]  the spot for a second and you can make it up because I literally was wondering if I'm trying to tie
[1986.14 --> 1990.12]  everything that we've covered together because there's a bit of complexity to it and I'm trying
[1990.12 --> 1996.36]  to make it easy to understand for my own selfish purposes so that as we get past the episode,
[1996.48 --> 2001.84]  I can start applying. Can you kind of think through a use case? And it can be fictional or it can draw from
[2001.84 --> 2006.66]  something that you've done, but kind of take us from the beginning to the end a little bit in your
[2006.66 --> 2010.94]  thinking and say, I'm doing this now and then I'm doing that. It can be anything. There's no wrong answer
[2010.94 --> 2017.52]  or it's whatever you want, but kind of sequentially take us through so that as we come out of that,
[2018.08 --> 2023.80]  myself and maybe other listeners that are interested can kind of go, okay, I get that. I can literally turn to
[2023.80 --> 2029.52]  my work after this podcast and go apply that. So I'm not sure I could do it quickly in 30 seconds. I will say
[2029.52 --> 2035.68]  we have built out a webinar that goes into detail on target leakage as well as there's an online course
[2035.68 --> 2042.48]  available that, so for me, this target leakage is really a fundamental concept that anybody new to
[2042.48 --> 2046.66]  machine learning really needs to kind of go through and learn all these different types of areas.
[2046.98 --> 2051.54]  So I've spent some time kind of actually taking all these different pieces together and building a
[2051.54 --> 2056.32]  little course with example problems for people to kind of go through and that way it kind of triggers.
[2056.32 --> 2061.22]  So that way, hopefully they can learn from seeing some other examples of where target leakage might
[2061.22 --> 2065.52]  occur and they don't actually have to go through the pain themselves of experiencing it.
[2066.10 --> 2070.54]  Awesome. And we'll make sure and link that in our show notes as well. I think that's great and
[2070.54 --> 2074.90]  something I want to go through as well. So yeah, I mean, there's a couple of rules of thumb,
[2074.90 --> 2080.68]  right, about just partitioning that data early, using all the interpretability and explainability
[2080.68 --> 2086.12]  tools to understand what are those factors in your model. There's having the domain knowledge.
[2086.12 --> 2090.56]  So making sure you're understanding what you're trying to predict, what are all the predictors,
[2091.14 --> 2095.78]  you know, is there anything that's kind of leaking in, understanding your IT system,
[2096.24 --> 2101.54]  making sure that, for example, records aren't being updated, using good press practices for,
[2101.70 --> 2105.94]  you know, creating features for training your models. We talked a little bit about nested cross
[2105.94 --> 2111.80]  validation. So another common mistake data scientists will do is on their hyper parameter tuning.
[2111.80 --> 2118.50]  So algorithms, for example, have some of them literally have tens, maybe hundreds of different
[2118.50 --> 2123.86]  knobs and levers, hyper parameters that we can kind of turn and modify when we're building out
[2123.86 --> 2128.86]  our models. A lot of data scientists, not all, a lot of them like to spend a ton of time,
[2129.26 --> 2135.30]  wait, if you ask me, way too much time on hyper parameter tuning. But a common thing that can happen is
[2135.30 --> 2139.56]  what you're doing is you're testing, you're moving the knob, you're moving the switch,
[2140.06 --> 2145.18]  one position, you test the model, you move it another position, you test it, and you literally
[2145.18 --> 2152.92]  do this hundreds, thousands of times. And if you're doing all of this and using the exact same data set
[2152.92 --> 2159.24]  to test it on, what can happen is you can actually do what's called overfitting to your model,
[2159.24 --> 2165.64]  you can essentially kind of learn that validation data set that you're using to test it on by testing
[2165.64 --> 2171.70]  it a thousand times. And that is another form of kind of leakage that can happen, where then you've
[2171.70 --> 2178.18]  kind of built a model that's much more optimistic that you have much that has memorized its testing
[2178.18 --> 2183.66]  data. And so you think it's working quite well, but actually it isn't, you just kind of got the
[2183.66 --> 2186.60]  figured out the one lucky one that understands this testing data.
[2186.60 --> 2188.76]  It's memorized rather than generalized.
[2188.94 --> 2189.46]  Exactly.
[2189.46 --> 2190.02]  Exactly.
[2216.60 --> 2236.10]  So, once again, that's changelog.com slash plus plus.
[2236.10 --> 2239.86]  T's log plus plus. It's better.
[2257.70 --> 2265.36]  So, Raj, it's been great to talk a lot about the sort of practicalities of this issue. I know
[2265.36 --> 2271.22]  there's things even, you know, we've talked about that are for sure, you know, things that I want to
[2271.22 --> 2278.00]  help better integrate into our team structure as well. I was curious now, you know, that you've been
[2278.00 --> 2284.72]  with DataRobot for a while, you've been in academia, you also have a sort of unique perspective,
[2284.72 --> 2290.60]  I think, on machine learning and AI and are concerned at the same time, very concerned with
[2290.60 --> 2295.88]  these sort of practical side of things and productizing things. What are some of the things
[2295.88 --> 2303.30]  that you're excited about exploring, you know, over the next year or so in terms of maybe it's new
[2303.30 --> 2308.86]  verticals that you think that AI or machine learning is really going to make an impact in,
[2308.94 --> 2314.52]  or maybe it's, you know, methodologies or even just like practical things that you're implementing
[2314.52 --> 2318.28]  that you think are going to make a big difference for you? What are some of those things? Like, what
[2318.28 --> 2324.34]  are you thinking about as you fall asleep in the evening, if you're thinking about machine learning
[2324.34 --> 2325.72]  and AI type things?
[2326.52 --> 2331.64]  There's two pieces for me for this question. One is just for like the techno side of my data science
[2331.64 --> 2336.86]  of just like feeding me in terms of like the cool things on Twitter, like cool, like little
[2336.86 --> 2341.58]  visualization blog posts to kind of play around with. I think there's, right, there's a ton of good
[2341.58 --> 2348.60]  stuff out there that I kind of like playing around with, right? So transformers and NLP is an easy one.
[2348.90 --> 2354.16]  In visualizations, you see things like Deck GL that you can just make the coolest kind of visualization
[2354.16 --> 2360.08]  pieces around. So I think there's a lot of cool stuff there as part of it. But I will tell you,
[2360.16 --> 2364.50]  part of it is, as I always tell people, they're kind of getting into data science. Don't get suckeded
[2364.50 --> 2369.78]  in by that, right? Most of the data science that you can use that's useful in an enterprise hasn't come
[2369.78 --> 2372.26]  out in the last three years, right? It's been around for much longer.
[2372.56 --> 2373.48]  That's a really good point.
[2373.62 --> 2379.16]  Don't get into reading, you know, the latest archive posts and trying to take those account,
[2379.26 --> 2384.40]  right? Because going back to those kind of classic problems, those classic either Kaggle
[2384.40 --> 2388.72]  competitions or other projects, and learning those techniques is going to get you much further along
[2388.72 --> 2390.88]  than kind of following the latest pieces.
[2390.88 --> 2394.18]  Don't start with GPT-3. It's the very first thing.
[2394.18 --> 2401.32]  I kind of have maybe a follow-up to that, which is like, you know, you're talking about
[2401.32 --> 2407.38]  like those Kaggle datasets or other things. And you've emphasized previously in the conversation,
[2407.38 --> 2413.80]  like one of the like really important pieces of this whole puzzle in terms of creating value is
[2413.80 --> 2420.76]  like understanding infrastructure, understanding like production systems. What do you recommend to like,
[2420.76 --> 2426.00]  because sometimes I talk to new people getting into data science about this very thing, right? Like,
[2426.54 --> 2433.02]  is it more useful for me to learn this sort of state-of-the-art models or what should I learn?
[2433.22 --> 2439.04]  What do you tell people that are sort of just getting into the field in terms of how heavy they need to,
[2439.04 --> 2447.38]  you know, jump into things like databases, like, you know, DevOps and CICD, like, you know,
[2447.38 --> 2454.50]  those things that are kind of common software engineering world things. How do you kind of
[2454.50 --> 2456.42]  prep people that you talk to?
[2456.84 --> 2462.84]  It's tough, right? Because the expectation now for data scientists is that they have to know it all,
[2463.20 --> 2467.14]  right? That you, especially if you're going out on the job market, if you don't know all the pieces,
[2467.22 --> 2472.64]  you really feel like I'm not measuring up. But then when you go actually study and work with data
[2472.64 --> 2477.78]  scientists in an enterprise, most of them are very kind of in a very narrow piece there. And they're
[2477.78 --> 2482.14]  complaining that they'd like more challenges and like to do different things. When people are first
[2482.14 --> 2489.06]  getting into the field, I encourage them to know a little bit about everything. So, you know, spend a
[2489.06 --> 2494.10]  weekend just playing around with Spark. So you kind of have some idea of what Spark is, like, don't
[2494.10 --> 2499.76]  spend two months on Spark, but just a weekend. So you have some kind of ability to kind of know what the
[2499.76 --> 2506.18]  tool is and where it fits in to all of that. And kind of go down the road like that for a lot of these
[2506.18 --> 2511.58]  kind of technologies, databases, is just have a little bit of understanding. So if you're at a conference,
[2511.58 --> 2517.20]  you could have a conversation and know, you know, what are the things you'd want to go to versus not. But I think
[2517.20 --> 2522.40]  you can't go deep in all of them, right? There's just not enough time to go deep into all of them. And what I
[2522.40 --> 2527.70]  always encourage people to do is a much more project-focused way of learning data science, where you solve
[2527.70 --> 2533.42]  some type of project. Hopefully, it's a passion project, something you care about. But you solve
[2533.42 --> 2537.98]  that end to end. And along the way, you're going to learn a lot of those subtle skills of, right,
[2538.06 --> 2543.66]  how to, you know, set up a web page or how to kind of fire up a web server in Python, whatever. But
[2543.66 --> 2547.92]  you'll pick up those skills along the way to kind of solve the problem. And then you'll really
[2547.92 --> 2553.28]  own those skills. Because if you solve a problem with it, you really kind of, for that domain,
[2553.28 --> 2558.28]  you totally understand how to solve the problem. And you can go deep with somebody on that.
[2559.06 --> 2563.88]  Yeah, because if it's a like, even if it's a side project or a passion project, what you're saying,
[2563.92 --> 2567.96]  which I definitely agree, I think, like, if you're going to get into this, like, choose something
[2567.96 --> 2573.78]  that you're going to want to work on, because it makes it just so much easier to, to put in that that
[2573.78 --> 2579.96]  time. But yeah, it's not going to be like, you know, let's say that I'm creating like a special
[2579.96 --> 2588.28]  webcam or a camera, you know, detect my pets versus like, you know, raccoons or, you know,
[2588.32 --> 2592.58]  something that, you know, is like bothering my trash or like,
[2592.90 --> 2594.70]  You have a problem with raccoons, Daniel?
[2594.84 --> 2599.80]  Yeah. Well, actually, right now, we have a mouse hanging around, but I don't know if I could catch
[2599.80 --> 2600.64]  that on the camera.
[2601.18 --> 2602.68]  Sorry, didn't mean to mess you up.
[2602.68 --> 2608.74]  Yeah, no, if you do that, like the, you know, the solution to that isn't going to be a Jupiter
[2608.74 --> 2614.06]  notebook, right? You may want to like play around with your video and whatever in a notebook.
[2614.42 --> 2618.74]  I'm not saying anything actually bad about Jupiter notebooks, because they use them every day.
[2619.14 --> 2624.52]  But at the end of the day, like, how you're going to solve that, it may be specific, maybe you want
[2624.52 --> 2630.62]  something like that you can look at on your phone, like a phone app, or maybe it's a web page or a
[2630.62 --> 2636.60]  dashboard or something that you want to look at with that. And so it forces you to think about some of
[2636.60 --> 2645.24]  these intricacies of like integrating a model into other things, which is something I don't know if
[2645.24 --> 2652.38]  you agree, Raj, but it's something I see missing in a lot of, in a lot of training is like, a lot of
[2652.38 --> 2658.32]  build up around, even sometimes around model management, which is some people are getting a
[2658.32 --> 2663.68]  little bit more into that, but not as much into sort of integration and, and that sort of world.
[2663.68 --> 2668.32]  Yeah. And just to insert before you answer there, I mean, I think that's a surprise for a lot of data
[2668.32 --> 2673.78]  scientists is that, to your point, Daniel, is that at the end of the day, a model that's going into
[2673.78 --> 2677.56]  production is a software component that has to be deployed. So.
[2677.84 --> 2681.64]  No, it is a good point, because, and it's been often missed in data science, right, where the
[2681.64 --> 2686.70]  conversation has been around algorithms and not necessarily what's going to take to kind of work
[2686.70 --> 2693.92]  with IT to get your model being used. And you're right. I mean, IT often has specific requirements
[2693.92 --> 2698.88]  that you want. And, you know, going back to your earlier thing about the Jupyter notebook, I'd say,
[2699.00 --> 2703.98]  go ahead and try running your Jupyter notebook and, you know, using your production model off that.
[2704.08 --> 2706.16]  And that way you'll learn what can go wrong.
[2706.56 --> 2707.02]  Why it doesn't.
[2707.56 --> 2711.48]  Right. Sometimes the best way to learn is to kind of fall down a little bit.
[2711.48 --> 2711.96]  True.
[2712.22 --> 2719.76]  But no, absolutely. Often I think about data science as kind of the webmasters of 2020,
[2720.14 --> 2724.22]  right? When I remember there was, when the internet was coming along, there was kind of the webmasters
[2724.22 --> 2728.58]  that they did everything, right? They designed the webpage, they run the networking switch,
[2728.60 --> 2733.80]  they kind of came to your house, solved your modem issues. And data scientists often kind of are put
[2733.80 --> 2739.32]  into that same category of having to fix every problem. And like the piece there where we're talking
[2739.32 --> 2743.64]  about productionizing, this is where, right, many places now have said, hey, you know, right,
[2743.68 --> 2747.68]  if you're a data scientist, you're going to explore data, you'll be on this part of the data science
[2747.68 --> 2753.44]  team. If you're the software engineer type that is good at coding, that knows how to take that and
[2753.44 --> 2758.64]  put it into production, you'll be, let's say, an ML engineer or data engineer and do that. So,
[2758.96 --> 2763.18]  you know, as kind of data science matures, and we get a little bit more of these specializations,
[2763.18 --> 2767.78]  and hopefully boundaries around this to help kind of do that. Because you're right,
[2767.92 --> 2771.20]  we need those skills at the end of the day to kind of get your model working.
[2771.76 --> 2778.62]  For sure. I think it's a great message to end out with here on, because, you know, as the name
[2778.62 --> 2784.74]  suggests, Chris and I are both concerned with sort of the practicalities of this and bringing a
[2784.74 --> 2790.58]  practical side to AI. So I really appreciate your perspective there. And, you know, perspective from
[2790.58 --> 2797.20]  really spending time building, you know, data products and productionizing models, it's really
[2797.20 --> 2804.64]  useful. We're going to link to those things that you mentioned during the show, the webinar and all
[2804.64 --> 2810.20]  of that. And so I encourage our listeners to definitely check that out. Also check out, you know,
[2810.26 --> 2816.08]  like we mentioned, Raj and I have talked a bit on Twitter, so you can connect to him and I and Chris
[2816.08 --> 2822.36]  in the show there. We've got our community on Slack. If you go to changelog.com slash community,
[2822.60 --> 2828.88]  you can talk about, you know, join our community and talk more about the topics there. And LinkedIn,
[2829.16 --> 2834.12]  we just had someone from LinkedIn on our show last week. And that's another place where you can find us.
[2834.66 --> 2839.28]  So make sure and connect with us. And I really appreciate you coming on, Raj. It was a great
[2839.28 --> 2844.62]  discussion and appreciate the very practical ideas that you've given me as well.
[2846.08 --> 2855.80]  If you enjoy Practical AI, we would enjoy a five-star review on Apple Podcasts, a blog post in response
[2855.80 --> 2860.52]  to something said on the show, and or a recommendation to a friend or colleague. Those
[2860.52 --> 2865.48]  word of mouth recommendations really do make a difference. Practical AI is hosted by Chris Benson
[2865.48 --> 2870.76]  and Daniel Whitenack. It is produced by Jared Santo with music by the mysterious Breakmaster Cylinder.
[2871.20 --> 2875.36]  Thanks again to our partners who support this show's existence. Shout out to Fastly,
[2875.36 --> 2879.62]  Linode, and Robar. That's all we have for you today. We'll talk to you again next week.
[2905.36 --> 2907.36]  Thank you.
