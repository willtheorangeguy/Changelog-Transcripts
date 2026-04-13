[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 --> 17.66]  on Linode servers. Head to linode.com slash Changelog. This episode of Practical AI is
[17.66 --> 23.28]  brought to you by Hired. One thing people hate doing is searching for a new job. It's so painful
[23.28 --> 28.32]  to search through open positions on every job board under the sun. The process to find a new
[28.32 --> 33.94]  job is such a mess. If only there was an easier way. Well, I'm here to tell you there is. Our
[33.94 --> 38.64]  friends at Hired have made it so that companies send you offers with salary, benefits, and even
[38.64 --> 44.04]  equity up front. All you have to do is answer a few questions to showcase who you are and what type
[44.04 --> 48.90]  of job you're looking for. They work with more than 6,000 companies from startups to large publicly
[48.90 --> 53.88]  traded companies in 14 major tech hubs in North America and Europe. You get to see all of your
[53.88 --> 58.88]  interview requests. You can accept, reject, or make changes to their offer even before you talk
[58.88 --> 62.68]  with anyone. And it's totally free. This isn't going to cost you anything. It's not like you have
[62.68 --> 66.52]  to go there and spend money to get this opportunity. And if you get a job through Hired, they're even
[66.52 --> 70.46]  going to give you a bonus. Normally it's $300, but because you're a listener of Practical AI,
[70.82 --> 75.74]  it's $600 instead. Even if you're not looking for a job, you can refer a friend and Hired will send
[75.74 --> 81.48]  you a check for $1,337 when they accept the job. As you can see, Hired makes it too easy.
[81.48 --> 84.72]  Get started at Hired.com slash Practical AI.
[97.92 --> 103.32]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[103.76 --> 109.26]  productive, and accessible to everyone. This is where conversations around AI, machine learning,
[109.26 --> 113.38]  and data science happen. Join the community and snag with us around various topics of the show
[113.38 --> 119.22]  at changelog.com slash community. Follow us on Twitter. We're at Practical AI FM. And now onto the show.
[123.40 --> 130.18]  Well, this is Daniel Whitenack, your data scientist co-host, and I'm joined by Chris Benson,
[130.18 --> 137.62]  who is the esteemed AI strategist specializing in deep learning. Chris, how are you doing?
[137.62 --> 145.28]  I'm doing great today. How are you, Daniel? Doing great. And today we have a very special guest I'm
[145.28 --> 152.28]  excited about. So tell me, Chris, if you opened up your editor, whatever that might be, what language
[152.28 --> 158.46]  would you start programming in? Well, usually it's going to be either Python or Go for me most of the
[158.46 --> 162.66]  time. But I understand we're going to do a different language today, which I'm looking forward to.
[162.66 --> 169.56]  We're going in a different direction, actually. Well, I started out, you know, back in the day
[169.56 --> 177.30]  doing Fortran and then kind of moved into the Python world eventually to Go. But then every
[177.30 --> 183.76]  once in a while, I kind of dabble in this other language called R. And I'm very happy that we have
[183.76 --> 191.64]  one of the great people from that community, the R language community with us. We have Jared Lander.
[191.64 --> 199.38]  Welcome. Hi, folks. It's wonderful to be here. Hey, thanks for coming. Yeah. Thank you for having me.
[200.24 --> 206.44]  So, Jared, tell us, give us a little bit of background about yourself. Where are you coming from and what do you do?
[207.58 --> 214.10]  So I am what I would like to call, depending on the audience, either a statistician, a data scientist.
[214.10 --> 217.00]  I do machine learning or AI, depending on who's listening.
[218.62 --> 224.08]  And that also depends on if you're on a plane and if you actually want to talk to the person next to you,
[224.24 --> 228.62]  then probably you say AI. And if not, then you say statistician. Is that how that works?
[228.74 --> 229.52]  That's pretty accurate.
[230.64 --> 232.38]  Hey, I think I did meet you before.
[235.18 --> 243.32]  Awesome. Well, what are you working on right now? And I understand you have your own business, right?
[243.32 --> 250.30]  Yeah. Yes, I do. It's Lander Analytics. We are a data science consulting training and events company.
[250.60 --> 255.04]  So at any given moment, we have many different things happening, whether it's client projects,
[255.04 --> 258.28]  we're teaching people how to use R or putting on events.
[259.34 --> 265.38]  Awesome. Yeah. And actually, is it one of those events that I met you and it was a great event?
[265.38 --> 273.30]  It was the NYC R conference or the R conference NYC. Which one of those is right? I forget.
[273.70 --> 274.80]  We call it NYR.
[275.66 --> 284.10]  NYR. Ah, even better. Yeah. No, this is a really great event. I have to say, not only was the content
[284.10 --> 290.42]  amazing, the technical content, but the catering was the best out of any conference I've been to.
[290.42 --> 295.80]  So round of applause on that. Nice. Thank you. Yeah. We pride ourselves on the food.
[296.16 --> 300.74]  This year, we stepped it up a notch. We had baristas on site. We had ice cream sandwiches,
[301.52 --> 305.82]  pizza delivered in waves. We really try to make it a party more than a conference.
[306.08 --> 307.82]  You mean the food doesn't all have to start with R?
[308.70 --> 314.10]  Yeah, that's a fair one. Maybe you could try next year, find round pizzas only.
[314.10 --> 321.34]  Well, I mean, there is an impressive number of puns in the R community, as I've learned.
[321.74 --> 321.98]  Yes.
[322.76 --> 325.50]  That seems to be a point of pride as well.
[326.38 --> 330.22]  Yes, they are. We are. And not only puns, but people are to double puns.
[330.74 --> 335.40]  They really go deep in how much they pun things.
[335.40 --> 344.18]  Yeah. So maybe we'll just devote a show to data science puns one of these days,
[344.18 --> 346.96]  and we can have you back on to discuss that.
[347.22 --> 348.02]  That would be great.
[348.60 --> 348.94]  Yeah.
[349.06 --> 350.12]  I'm looking forward to that show.
[350.78 --> 352.10]  Yeah, I am too.
[352.62 --> 357.98]  But also, so tell us a little bit. So you're involved in the conference, the New York R conference.
[357.98 --> 364.10]  You also are really involved in the meetup scene in New York, I know.
[364.46 --> 368.56]  I'm actually, even though I'm not in New York, I'm part of the Slack that you guys have going there,
[368.60 --> 370.06]  and it's very, very active.
[370.78 --> 375.42]  And I just appreciate, I think, how much the community there,
[375.54 --> 382.52]  even though I'm not a really heavy R person, was very welcoming to me when I was there.
[382.52 --> 388.92]  And I think in general, it's just a really welcoming and awesome community for newcomers to data science
[388.92 --> 390.12]  and machine learning and AI.
[390.48 --> 395.04]  Why don't you tell us a little bit more about that community and what you guys do and how that came about?
[395.60 --> 400.94]  Absolutely. One of the hallmarks of the R community in general is its friendliness.
[401.80 --> 403.96]  And not just, you know, hey, how are you doing?
[403.96 --> 410.32]  But it's a welcoming environment that really tries to, it really strives to make everyone who walks in the door,
[410.64 --> 416.70]  either physically or virtually, feel welcome and happy and like you're a part of the community.
[417.18 --> 421.78]  And I do think that is one of the strengths of the R language is this community behind it.
[422.40 --> 428.10]  So the meetup was actually founded back in 2009 by Josh Reich.
[428.10 --> 434.24]  And shortly thereafter, by the second meetup, it was a monthly meetup, Drew Conway had taken over.
[434.88 --> 437.66]  And every good scientist knows Drew Conway.
[437.78 --> 438.80]  He's one of the luminaries.
[438.90 --> 442.08]  He's one of the original, I'm going to call him the old guard of data science.
[443.06 --> 447.08]  And after running it for about two years and growing it to 1,800 members,
[447.82 --> 449.64]  Drew asked me to take over the meetup.
[450.08 --> 454.80]  I actually took over at the time with Wes McKinney, who's technically my co-organizer,
[454.80 --> 460.88]  the New York R meetup, which is now called the Open Statistical Programming Meetup,
[461.28 --> 462.96]  so that it is welcome to all languages.
[463.14 --> 467.18]  And indeed, we've had Python, we've had Go, we've had SQL.
[467.56 --> 470.38]  We've done a number of different languages as long as they're open source.
[470.74 --> 475.96]  It is primarily focused on R, but we do allow R and friends.
[476.38 --> 477.34]  Same with the conference.
[478.54 --> 483.72]  It started in a room at NYU back in 2009, founded by Josh Reich.
[483.72 --> 487.40]  And it was quickly organized by Drew Conway.
[488.02 --> 489.08]  And everyone knows him.
[489.12 --> 490.70]  He's one of the old guards at data science.
[491.82 --> 496.20]  So after about two years of running it and growing it to about 1,800 members,
[496.70 --> 498.48]  he turned over the reins.
[499.00 --> 503.84]  And I am very proud to say we are now about to cross 10,000 members.
[504.40 --> 505.24]  That's crazy.
[505.50 --> 505.74]  Wow.
[506.36 --> 506.62]  Yeah.
[506.62 --> 512.16]  So how many of those 10,000 show up at an event?
[512.26 --> 519.68]  I know the proportion on meetups is smaller, but you still must have a lot at the in-person events.
[520.34 --> 520.80]  We do.
[521.04 --> 524.48]  And since we're in New York, space is our limiting factor.
[524.92 --> 525.48]  Ah.
[525.48 --> 534.02]  So in our normal venue, and we have a rotation of a few venues, we can hold about 120, 150 people in the room.
[534.94 --> 535.76]  That's awesome.
[536.08 --> 543.58]  Other venues, when we know we're going to sell out, we have other venues that can hold 200 and even 300, depending on who's speaking.
[543.58 --> 547.30]  We need to go to New York, Chris.
[547.56 --> 548.14]  Yeah, we do.
[548.78 --> 549.08]  Yes.
[549.32 --> 556.46]  And it's so much fun being here in person, but we do try to make the meetup a global community.
[556.92 --> 559.82]  I don't mean meetups in general, but I mean specifically the New York meetup.
[560.20 --> 565.12]  So we have the Slack that Daniel mentioned that is open to anyone from all over the world.
[565.42 --> 568.08]  And we now live stream all of the meetups.
[568.22 --> 572.28]  So if someone can't be in New York, they can see it live wherever they happen to be.
[572.28 --> 573.88]  That's fantastic.
[574.18 --> 574.82]  Quick question.
[574.98 --> 578.84]  Has that impacted attendance in any way, or has it just enhanced it?
[580.08 --> 585.42]  Our numbers for attendance have been pretty steady at sellout size before and after the live stream.
[585.60 --> 590.24]  So it looks like it's just people who can't physically be here or who couldn't fit in the room.
[590.74 --> 591.38]  That's awesome.
[591.50 --> 593.68]  I know I've appreciated being on the Slack.
[593.90 --> 596.16]  And like I say, I've felt very welcome there.
[596.16 --> 600.48]  So we'll post some of those links in the show notes.
[600.48 --> 606.74]  Because if people, even if they're not in New York, sounds like there's a lot of opportunities to get involved.
[607.30 --> 607.74]  Absolutely.
[607.90 --> 615.10]  There's always a way somehow that we just want everyone to be happy doing data science together.
[615.62 --> 616.64]  That's great.
[616.80 --> 618.48]  And I really appreciate that.
[618.58 --> 621.36]  I mean, that's at the heart of what this show is as well.
[621.36 --> 626.96]  Making data science and AI and machine learning accessible to people and practical.
[627.26 --> 629.30]  So really appreciate your work there.
[629.30 --> 630.16]  Thank you.
[630.54 --> 630.84]  Yeah.
[631.06 --> 639.38]  So we're going to get back to our kind of the other AI language to steal some puns from your community.
[639.66 --> 642.66]  But yeah, I kind of wanted to get into a little bit.
[642.84 --> 648.38]  I think you're a great person since you've been at the forefront of data science for quite a while.
[648.90 --> 654.52]  And I know that we've talked about different AI techniques and deep learning and other things.
[654.52 --> 667.24]  And I also saw while the New York R conference was going on, some people tweeting out about how you were talking about deep learning and how we can understand it as kind of extreme nonlinear modeling.
[667.24 --> 684.48]  So we've had some comments in our Slack, the changelog Slack, about wanting to get some perspective from one of the guests on the different kind of landscape, the landscape of AI and ML techniques and how deep learning fits into that.
[684.48 --> 688.00]  So I think you would be a great person to give us that context.
[688.08 --> 688.80]  Would you mind doing that?
[689.16 --> 689.56]  Absolutely.
[690.26 --> 700.56]  This one of the key things about learning is what I've seen from teaching both private clients and up at Columbia is that you have to disambiguate terminology.
[700.56 --> 704.78]  And people often just drown in the different terminology.
[705.38 --> 713.70]  In fact, the talk I gave the most recent New York R conference was comparing ML to deep learning in R.
[714.36 --> 728.20]  And the first thing I started with was just the vocab because the different people from different fields will call the same exact thing with different words like an intercept versus a bias or coefficients versus weights.
[728.20 --> 733.70]  Yeah, that was actually super confusing to me when I was starting to get into data science.
[733.86 --> 738.46]  I was like, oh, if I just would have known this was an intercept, then that would have made things so much easier.
[739.36 --> 739.76]  Exactly.
[740.20 --> 740.56]  Exactly.
[740.68 --> 747.76]  And it's almost as if you have people at different universities doing the research, not reading each other's papers and not knowing that these other terms exist.
[748.56 --> 748.78]  Yeah.
[748.94 --> 749.72]  Yeah, for sure.
[749.98 --> 753.28]  So help us disambiguate some of that.
[753.28 --> 761.72]  You know, how do you see the the AI ML landscape in general and kind of some of the major categories within that?
[762.26 --> 769.74]  So I think first of the AI buzz, a lot of half the time when someone says they have an AI, they mean they have an if else statement.
[771.44 --> 772.98]  Yeah, that's that's true.
[772.98 --> 780.38]  And then beyond that, the majority I do still believe in from what I've seen in practice, the majority after that is logistic regression.
[781.06 --> 786.32]  And half of what you see is coming out here is automagical is the words they use.
[787.12 --> 793.32]  It's it's basically stuff that we've been doing for its tools we've been using for 100 years.
[793.32 --> 798.30]  And I've been attending a number of Capitol Hill events about AI.
[799.16 --> 801.72]  And I heard someone make a really good point.
[802.02 --> 804.56]  He said everyone's sort of up in arms right now about AI.
[804.94 --> 807.78]  But no one was concerned when we called it logistic regression.
[809.46 --> 819.00]  So, yeah, that's that's definitely I think everyone wants to add AI to the tag of their project now.
[819.16 --> 819.36]  Right.
[819.36 --> 819.84]  Yes.
[820.28 --> 820.56]  Yes.
[820.68 --> 822.94]  There's been a run on dot AI domains.
[823.52 --> 824.16]  There sure have.
[824.52 --> 826.06]  You can't get anything anymore.
[826.14 --> 827.58]  And they've only been out for the last year or so.
[828.06 --> 828.50]  Exactly.
[828.94 --> 829.88]  It's very difficult.
[830.42 --> 832.86]  I managed to get a few domains for myself.
[832.96 --> 834.72]  I'm very happy about that I'm going to start using.
[835.24 --> 836.50]  But of course, you have to jump on the bandwagon.
[837.28 --> 837.62]  Yeah.
[837.78 --> 848.58]  I contemplated writing an AI that would would, you know, generate both startup names and then search for the AI domain.
[848.58 --> 850.50]  And just register a bunch of them.
[851.04 --> 854.96]  And then I would raise venture capital and and sell out and retire.
[855.30 --> 856.56]  How's that going for you, Daniel?
[857.08 --> 859.34]  You know, I didn't make it too far.
[859.54 --> 861.60]  It was mostly a theoretical construct.
[862.14 --> 864.76]  So is PiedPiper.ai still available?
[866.22 --> 867.18]  I don't know.
[867.30 --> 868.18]  I hope so.
[868.18 --> 876.60]  But to the question you asked where the different parts fall in, I see AI in a few in a few different segments.
[877.86 --> 882.16]  There's automation, which could just be scripting, writing scripts.
[882.28 --> 889.94]  We've been doing a lot of work with some companies automating their data processes where people were literally copying and pasting from one spreadsheet to the other.
[889.94 --> 891.76]  And now doing all through scripts.
[891.86 --> 893.64]  And that's seen as AI by some people.
[893.78 --> 894.74]  It's made their lives easier.
[895.42 --> 901.84]  That's interesting that we're kind of seeing kind of a crossover of, you know, I would only think of that as automation.
[902.14 --> 908.14]  But I guess if it is something you didn't have before, some people may define it that way in a very loose way.
[908.52 --> 908.94]  Exactly.
[909.02 --> 911.32]  It's like automated car production lines.
[911.32 --> 914.42]  That is a form of artificial intelligence, how to put the cars together.
[914.42 --> 919.38]  It's not thinking for itself, but it's doing tasks that humans used to do.
[920.62 --> 923.82]  So let me kind of ask a follow-up on that.
[924.12 --> 926.34]  And, you know, how do you think of AI?
[926.86 --> 929.82]  How does deep learning fit into that context?
[930.46 --> 934.50]  And, you know, how would you differentiate them?
[935.02 --> 941.40]  So the next step up from this automation is learning from data to make decisions for you.
[941.40 --> 949.12]  So first we have our linear models, our generalized linear models, including binary regression, Poisson regression, whatever you may have,
[949.46 --> 956.20]  to learn and do things not just based on hard set rules, but to learn from context.
[956.70 --> 963.00]  Now, linear models were simplifications to make the math easy because they were invented 100 years ago or so.
[963.00 --> 970.76]  Then you get into nonlinear models, which at first were similar to linear models, but had a nonlinear construction.
[971.60 --> 980.82]  But then they got into trees and tree-based models, whether they are random forests or boosted trees.
[981.88 --> 987.56]  And boosted trees, especially XGBoost, were the darling of the machine learning community for years.
[988.34 --> 989.02]  And Kaggle.
[989.02 --> 990.10]  And Kaggle.
[990.30 --> 993.62]  Almost every Kaggle competition was won using XGBoost.
[994.30 --> 994.94]  Yeah.
[995.20 --> 1000.32]  With a very narrow margin between the other similar methods, right?
[1000.78 --> 1001.06]  Right.
[1001.18 --> 1002.94]  So random forests was the rage.
[1003.28 --> 1006.22]  And then XGBoost came on top of random forests.
[1006.38 --> 1010.06]  And then it turns out, even if XGBoost, you could do a boosted random forest.
[1010.80 --> 1012.00]  Boost all the boosts.
[1012.36 --> 1012.88]  Exactly.
[1014.84 --> 1015.44]  Nice.
[1015.44 --> 1019.52]  So then beyond XGBoost, we have deep learning.
[1020.56 --> 1024.02]  And this is essentially a neural network that just has many layers.
[1024.14 --> 1027.10]  And neural networks have been around since at least the 50s.
[1027.56 --> 1031.34]  And they were cool, then they weren't cool, then they were cool again, then not cool,
[1031.44 --> 1032.68]  and now they're cool yet again now.
[1033.84 --> 1041.14]  And when you say a layer in the neural network, could you just explain a little bit what you mean by layer?
[1041.14 --> 1047.86]  So when you have a neural network, you have all of your input variables, and you have weights for them or coefficients for them.
[1048.20 --> 1049.92]  And you multiply those weights by the coefficients.
[1050.54 --> 1053.78]  And then you take that and do a nonlinear transformation.
[1054.62 --> 1055.56]  That is a layer.
[1056.36 --> 1060.08]  That is a set of now almost new inputs.
[1060.16 --> 1064.44]  They're not inputs, but they're new variables, if you could say so.
[1064.68 --> 1066.94]  But they've been transformed of a two-step process.
[1067.22 --> 1068.16]  And that is a layer.
[1068.16 --> 1073.16]  And you can repeat these layers again and again until you finally get to a point where you get to your output.
[1074.04 --> 1079.76]  And that's where the power of these neural networks are coming from today, having many of these hidden layers.
[1079.96 --> 1082.18]  And these are just transformations of your input variables.
[1082.56 --> 1085.02]  And the next hidden layer is a transformation of the first layer.
[1085.28 --> 1087.10]  And you can keep transforming on and on.
[1087.10 --> 1097.68]  So let me ask, one of the things that I've seen you talk about is extreme nonlinear modeling in reference to deep learning.
[1097.68 --> 1104.88]  And I was kind of wondering if you would kind of take us into what the difference is between those or if it's the same and how you see deep learning.
[1104.88 --> 1113.16]  So with a linear model, the reason we made it linear is because it was a simplification so that way they could do the math.
[1113.48 --> 1115.12]  But nowadays we have more powerful computers.
[1115.54 --> 1119.28]  And most things in life don't follow a linear relationship.
[1119.48 --> 1121.08]  They follow a nonlinear relationship.
[1121.62 --> 1125.54]  Now when I say nonlinear, that could have different meanings depending on the technicality.
[1125.54 --> 1134.64]  But you can imagine if you had a cloud of points with a x and y axis, instead of fitting a straight line through those points, if you fit a step function.
[1135.34 --> 1139.24]  Maybe for the first segment, it's about a third of the way up the y axis.
[1139.44 --> 1143.36]  The second segment, the straight line would go two thirds up.
[1143.42 --> 1146.20]  And the last segment, it would be back down to the bottom of the y axis.
[1147.02 --> 1150.72]  And that's a simple step function that is nonlinear.
[1151.26 --> 1152.80]  It doesn't fit a nice straight line.
[1152.88 --> 1154.88]  It doesn't even fit a curvy linear line.
[1154.88 --> 1156.54]  It fits a step function.
[1157.84 --> 1162.06]  And that's somewhat the idea behind a tree somewhat.
[1163.20 --> 1173.12]  And the ability to capture these nonlinear relationships, regardless of the method, allows us to really model reality better.
[1173.88 --> 1175.24]  That's why trees are really great.
[1175.40 --> 1176.52]  They have high predictive power.
[1177.08 --> 1179.20]  And why random forests and boosted trees.
[1179.82 --> 1184.62]  That's also why deep learning is powerful because it is nonlinear.
[1184.88 --> 1187.56]  It has a lot of nonlinearities.
[1187.56 --> 1195.88]  So when you're going from your inputs to your first hidden layer, and then on to subsequent hidden layers, there are two steps.
[1196.52 --> 1204.14]  There is a matrix multiplication of the inputs by their weights or coefficients.
[1204.14 --> 1205.60]  And that's linear.
[1205.80 --> 1210.92]  If you just did that, a deep learning model would just be a linear model.
[1211.70 --> 1213.92]  You could even stack many more layers.
[1214.10 --> 1222.32]  And if you just did these multiplications by the weights, it would just be a series of linear models, which would become one large linear model.
[1222.32 --> 1225.76]  And then you essentially have a straight line or a curvy linear line.
[1226.08 --> 1230.84]  But it's that next step at each layer, the activation function.
[1231.60 --> 1234.82]  That is a nonlinear function you are applying.
[1234.82 --> 1245.82]  So whether it is a tanh or it's a relu or a sigmoid, which is just a fancy word for inverse logit, regardless of which one you're doing, you are doing a nonlinear transformation.
[1246.78 --> 1251.90]  And that puts a nonlinearity in your model, which allows you to capture more complex relationships.
[1252.46 --> 1255.02]  And if you do more layers, you have more nonlinearities.
[1255.14 --> 1259.72]  So you can capture really interesting separations between your data.
[1259.72 --> 1263.78]  So, yeah, that's that's a really, really great context.
[1263.78 --> 1264.54]  And I wonder.
[1264.68 --> 1278.72]  So, like, sometimes when I'm thinking about these problems solved by deep learning, I think about them in terms of, you know, I know that there must be these relationships between what I'm putting in and what I want to get out.
[1278.72 --> 1285.24]  But I have a really hard time understanding what those relationships are in your thought process.
[1285.24 --> 1293.28]  When you're doing this sort of deep learning technique, does that put you kind of further away from actually getting insight into those relationships?
[1293.92 --> 1296.40]  Or does it I mean, does it really matter at that point?
[1296.84 --> 1297.74]  That's an interesting question.
[1297.84 --> 1298.56]  Does it matter?
[1299.14 --> 1300.34]  Depends on your goal.
[1300.78 --> 1309.36]  If you're doing a study on a medical trial, you really want to know what's happening because, you know, is the drug helping or hurting?
[1309.66 --> 1315.04]  You could do that with prediction, but you really want to know what's happening with the treatment.
[1315.24 --> 1316.76]  What type of effect is it having?
[1316.88 --> 1317.66]  Is it a large effect?
[1317.72 --> 1318.62]  Is it a small effect?
[1319.06 --> 1325.48]  And while there are ways to get that from purely predictive methods like trees and deep learning, it's not as explanatory.
[1325.64 --> 1331.42]  If, on the other hand, you're just trying to make a prediction and you don't necessarily care why, then it doesn't matter.
[1331.98 --> 1344.12]  But the idea of understanding it, though, even with a logistic regression that is complex with lots of interaction terms, could be hard to interpret.
[1344.12 --> 1348.90]  So, yes, we are losing more of that interpretation with a deep learning model.
[1349.58 --> 1354.42]  But depending on what you're doing, that's not terrible if you don't need to understand what's happening.
[1354.94 --> 1355.42]  Gotcha.
[1355.64 --> 1368.96]  So, as we've been kind of talking about, you know, how we're approaching AI and deep learning specifically and such, one of the things that comes to mind is I'm curious if you're actually using deep learning with your clients.
[1368.96 --> 1371.94]  And if so, if you can kind of tell us what that looks like a little bit.
[1372.98 --> 1375.42]  Yes, we have a few clients we do deep learning with.
[1375.60 --> 1381.22]  In fact, we became NVIDIA partners because they are really pushing the forefront of deep learning.
[1381.44 --> 1383.14]  They have a vested interest with their GPUs.
[1383.14 --> 1389.86]  So, we work with some of our own clients and some of NVIDIA's clients on specifically deep learning problems.
[1390.74 --> 1397.12]  So, let me ask another question, especially coming as a newbie to the R community.
[1397.58 --> 1407.30]  What are some of the strengths that R have that you specifically find really help you in the development of AI or ML technologies?
[1408.18 --> 1411.78]  R was written from the ground up as a data language.
[1411.78 --> 1419.18]  It was meant for handling data of different types, whether they are numbers or text or dates or logicals.
[1419.50 --> 1420.90]  It was designed for data.
[1421.70 --> 1428.24]  And beyond that, it was designed for statistics, which is data science, ML, AI by another name.
[1428.72 --> 1431.16]  It was meant for doing matrix algebra.
[1431.56 --> 1433.66]  It was meant for mathematical programming.
[1434.22 --> 1439.88]  So, anything involving data just comes so naturally to the R language that it's a joy to work with.
[1439.88 --> 1452.86]  So, with respect to that, I mean, I think my kind of stereotypes before I was involved with the R community was that R was used by these kind of people at universities.
[1452.86 --> 1459.70]  And they wrote kind of one-off things to do nifty visualization stuff and data munching.
[1460.18 --> 1467.24]  But it wasn't really like a production language, you know, that people are using for AI in production at companies.
[1467.24 --> 1469.42]  But that's not quite true, is it?
[1469.98 --> 1471.04]  Not true at all.
[1471.04 --> 1475.80]  There's a number of companies that I know are using in production, which I can't name here.
[1476.14 --> 1477.12]  They're my clients.
[1477.32 --> 1483.38]  But I've also seen other companies, not my clients, who do use R in production on a daily basis.
[1483.82 --> 1487.28]  And it is a full, robust language, just like any other.
[1487.28 --> 1497.18]  Where do you see the largest kind of interest in R industry-wise, you know, whether that's like finance or healthcare?
[1497.30 --> 1499.90]  I know you're in New York, so maybe like finance is a big one.
[1500.46 --> 1505.44]  Do you also kind of like, what do you see as the main industries that have that interest?
[1505.48 --> 1509.66]  And kind of, is it also geographically distributed?
[1510.18 --> 1513.98]  I know you're in R and maybe there's difference kind of on the West Coast or something.
[1513.98 --> 1524.68]  So for industries, I see the most adoption from personal experiences in finance, in pharmaceuticals and healthcare, and in defense.
[1525.50 --> 1526.14]  Interesting.
[1526.40 --> 1527.78]  I didn't expect defense.
[1528.38 --> 1537.36]  Is that just because you think that's because those are communities that are being fed from kind of R-heavy academic fields?
[1537.36 --> 1540.36]  Or what do you think is the reasoning behind that?
[1540.98 --> 1542.94]  It really depends how you come up.
[1542.94 --> 1546.98]  If you come up thinking about math and statistics, you're going to be an R person.
[1547.42 --> 1551.42]  If you come up thinking about engineering, computer science, you're going to be a Python person.
[1552.18 --> 1562.18]  So a lot of the government agencies I've seen, whether they are defense-related or even stuff such as the National Institutes for Standards of Technology or the Census Bureau,
[1562.62 --> 1565.78]  a lot of them are going to be trained as statisticians, mathematicians.
[1566.12 --> 1567.80]  So R comes naturally to that community.
[1567.80 --> 1569.68]  Yeah, that's fine.
[1569.82 --> 1571.00]  So you mentioned NIST.
[1571.72 --> 1576.48]  And I just had like a total flashback when I was in grad school, I think.
[1576.96 --> 1579.86]  So I had a part-time appointment there.
[1580.10 --> 1586.80]  And I think all I did was like spill nanotubes all over the floor everywhere at NIST.
[1586.80 --> 1592.86]  And that's where I found out that I should not be in an actual lab, that I should just work on a computer.
[1593.50 --> 1593.64]  Yeah.
[1593.76 --> 1594.86]  No wet lab work for you.
[1595.38 --> 1595.62]  Yeah.
[1595.62 --> 1600.14]  So I have a follow-up question to that last answer you gave us.
[1600.64 --> 1607.96]  You kind of talked about how depending on what field people are in, they naturally gravitate to this language or that.
[1608.68 --> 1613.36]  And, you know, but we're kind of in this age of polyglot programmers.
[1613.90 --> 1615.52]  And so if you're...
[1615.52 --> 1616.44]  It is a hard word to say.
[1616.58 --> 1617.74]  It's a hard word to say.
[1617.74 --> 1622.70]  So if you're one of those people and you start in...
[1622.70 --> 1628.24]  Maybe you start in R and then you also pick up Python or anything.
[1628.42 --> 1628.94]  Could be Julia.
[1629.10 --> 1629.56]  Could be Go.
[1629.64 --> 1630.18]  Could be whatever.
[1630.58 --> 1641.96]  Do you have any advice on if you have multiple languages in your capability when you might go to R and when you might not go to R and go to a different language instead?
[1642.08 --> 1642.78]  Any thoughts on that?
[1643.84 --> 1644.28]  Yeah.
[1644.28 --> 1651.46]  I see you going to R when you want to get something done quickly and it's really data machine learning focused.
[1652.24 --> 1656.52]  It's, like I said, it's natural to be used for that stuff.
[1657.60 --> 1662.04]  If you need something that's blazing fast, then you're going to do C++ or Go.
[1662.74 --> 1670.90]  If you need something that is out of your wheelhouse in R that is more, let's say, building a web server, even though you could do that in R,
[1670.90 --> 1674.84]  you might go to do that in a language that's more natural for a web server.
[1675.66 --> 1680.00]  So in my mind, it's really what is your goal and what is your broader ecosystem?
[1680.48 --> 1682.12]  It depends how does your company work.
[1682.20 --> 1688.14]  Do you have a pipelining tool that can pull from different resources or does everything have to be monolithic?
[1688.96 --> 1694.40]  So it really depends on all those factors around you and what the task at hand really is.
[1694.40 --> 1694.84]  Yeah.
[1695.52 --> 1702.74]  And I think even to that point, there's a lot of interaction with other communities and programming languages as well.
[1702.84 --> 1705.86]  I know that you're pretty good friends with Wes McKinney, right?
[1706.20 --> 1706.46]  Yes.
[1706.54 --> 1706.76]  Yes.
[1706.76 --> 1708.20]  We are very good friends.
[1708.20 --> 1709.12]  Yeah.
[1709.32 --> 1727.46]  And I remember, I think it was at the R conference there in New York that he was giving a talk about some of these layers that actually bridge the gap between the data science and AI languages like Apache Arrow and other things.
[1728.36 --> 1731.74]  Could you kind of share some of those kind of intersection points?
[1731.80 --> 1732.84]  I think those are really exciting.
[1732.84 --> 1733.10]  Yeah.
[1733.80 --> 1741.24]  So Wes has been working on Apache Arrow, which has many things, but one of the key points to it is an interoperable data frame.
[1741.68 --> 1749.70]  So you have a data frame in R, you save it to disk, and you can open that binary file in Python or Julia or any other language that supports it.
[1750.42 --> 1751.36]  And that's fantastic.
[1751.78 --> 1760.84]  Even deeper than that, all these interpreted languages, particularly R and Python, are really just high-level bindings for C and Fortran.
[1760.84 --> 1768.68]  So the same libraries are doing all the work, and there's just a different flavored wrapper on top of it to suit different people's needs.
[1769.52 --> 1774.74]  I think you just shook some people's worlds that maybe didn't know that they were using Fortran.
[1775.58 --> 1781.22]  And when Daniel said he did Fortran, I always say that anyone who knows Fortran is awesome.
[1781.22 --> 1785.44]  Well, I don't know that I would say I know Fortran.
[1785.78 --> 1799.46]  When I quote-unquote wrote Fortran, I mostly wrote Python around Fortran because I didn't want to actually touch the Fortran for fear of breaking all sorts of large code bases that were beyond my scope.
[1799.84 --> 1801.60]  But occasional dabbling, maybe.
[1801.76 --> 1802.84]  I'll leave it at that.
[1802.84 --> 1811.08]  Now, Jared, I've got to say, you just made my day, though, because my mother, who is now retired, taught Fortran at Georgia Tech back in the 1980s.
[1811.18 --> 1816.28]  And the fact that she is—that compliment you just offered for Fortran, she's going to love that.
[1816.40 --> 1818.24]  I might even get her to listen to the podcast now.
[1818.68 --> 1819.46]  Oh, that's fantastic.
[1819.60 --> 1820.34]  I love hearing that.
[1821.44 --> 1827.10]  I'm really happy that our guest unknowingly complimented Chris's mom.
[1828.38 --> 1829.28]  Can't beat that.
[1829.72 --> 1830.70]  No, that's the best.
[1830.70 --> 1834.00]  Yeah, that's awesome.
[1834.36 --> 1839.62]  Yeah, that's great to hear about those kind of intersection points.
[1839.62 --> 1860.22]  I think more and more I'm seeing, which I'm really happy to see, I'm seeing kind of, you know, hopefully less of these language war sort of competitions or discussions on Twitter and other places and more intersection points between language communities, whether that be Apache Arrow, like you were just saying.
[1860.22 --> 1870.14]  Or whether that be something like the ONIX neural network formats that exchange between different frameworks and all of that is really exciting to me.
[1870.14 --> 1877.74]  As long as you're doing just machine learning, doing AI, doing data science, people shouldn't care how you're doing it.
[1878.20 --> 1883.66]  Do whichever way works best for you and for the problem you have and use the tools that feel comfortable to you.
[1883.66 --> 1890.64]  So I have a question that's especially for me and maybe a few listeners out there in the same boat as me.
[1891.14 --> 1906.76]  Since I'm brand new to R and haven't used it in the past like you guys have, I want to ask you, you know, for AI ML context here, how should I on day one kind of get started with machine learning in mind?
[1906.76 --> 1908.20]  What do you recommend?
[1908.68 --> 1913.08]  Well, of course, the first step of your just learning R, you have to get a copy of my book R for everyone, obviously.
[1913.78 --> 1914.18]  Perfect.
[1915.46 --> 1915.82]  Exactly.
[1916.18 --> 1917.02]  You have to do it.
[1917.08 --> 1918.06]  I mean, there's no other way.
[1918.76 --> 1919.30]  Done deal.
[1919.62 --> 1923.94]  We'll for sure put that link in the show notes.
[1924.38 --> 1925.58]  I even have evidence.
[1925.72 --> 1930.36]  I've seen the lines at conferences to get Jared's signature on his book.
[1930.58 --> 1934.76]  And it must be awesome if the lines are that long.
[1934.76 --> 1939.42]  So it's always very flattering when I see a long line of people lined up to come get my autograph.
[1939.52 --> 1941.22]  I'm like, I could do this all day long.
[1942.02 --> 1946.38]  Then beyond that, you want to start getting more specifically into ML.
[1946.78 --> 1948.68]  Of course, you have to show up to the meetups and the conferences.
[1948.68 --> 1950.70]  That's your in-person experience.
[1950.78 --> 1956.64]  And that's not just for the knowledge, which you do get a lot of knowledge, but it's to be around other like-minded people.
[1957.32 --> 1958.00]  And for the pizza.
[1958.50 --> 1959.12]  And for the pizza.
[1959.18 --> 1960.14]  Yes, we do pride ourselves.
[1960.14 --> 1965.70]  In fact, every month we try to get pizza from a different place and we have a data set running.
[1965.78 --> 1966.84]  People rate the pizza.
[1967.20 --> 1968.24]  We can go pull that data.
[1968.36 --> 1971.04]  It's a live feed and see how it's going over time.
[1971.84 --> 1980.54]  I'm assuming that you haven't brought in some Chicago-style pizza yet, which is my favorite, but probably less exciting in New York.
[1980.82 --> 1982.42]  So you mean casserole?
[1982.42 --> 1987.18]  I think we should move on to the next question.
[1987.18 --> 1987.38]  Yes.
[1987.64 --> 1989.90]  But finish answering the question about statistics.
[1990.64 --> 1995.98]  Then once you've already got a basis in R, the question becomes, do you already know the math, the statistics?
[1996.64 --> 2003.14]  If you don't, there's great books out there written by Andrew Gellman and Hasty, Chibshani, and Friedman and Jennifer Hill.
[2003.66 --> 2005.42]  Those are great books to learn about the statistics.
[2005.42 --> 2009.56]  And then once you, if you have a grounding in that, it's about how do you do it in R.
[2010.24 --> 2012.92]  Now, how do you define ML?
[2013.44 --> 2015.00]  Well, you want to learn linear regression.
[2015.80 --> 2017.58]  That's, you know, a simple one line of code.
[2018.08 --> 2023.08]  Then if you get into penalize regression and XGBoost, you could do that all natively in R.
[2023.58 --> 2025.50]  Or you could use a package called caret.
[2026.26 --> 2033.40]  And caret was a unified interface for machine learning in R written about 10 years ago.
[2033.40 --> 2035.44]  And it's just gotten better and better since then.
[2035.84 --> 2037.66]  And that was written by a guy named Max Kuhn.
[2037.82 --> 2041.18]  And he has a companion book called Applied Predictive Modeling.
[2041.58 --> 2046.24]  And then when you're ready to get into the deep learning part of your R experience,
[2046.66 --> 2049.10]  there's the older packages like neural net.
[2049.44 --> 2051.68]  And there's newer packages like MX net.
[2052.46 --> 2058.24]  And JJ Allaire, the head of R studio, wrote a couple packages called TensorFlow and Keras.
[2058.84 --> 2062.46]  And he wrote a book to go along with that called Deep Learning in R.
[2062.46 --> 2068.70]  So if you go through all of these books and go through using the functions yourself to Keras,
[2068.94 --> 2072.30]  you'll have the whole spectrum of doing AI all within R.
[2072.76 --> 2072.96]  Yeah.
[2073.14 --> 2077.02]  And I think, you know, I had a great time learning some R.
[2077.12 --> 2078.20]  I'm by no means an expert.
[2078.40 --> 2080.78]  But I think, like Jared kind of already mentioned,
[2081.02 --> 2087.28]  it's a pretty quick way to get from nothing to something working in a short period of time.
[2087.32 --> 2088.90]  And I think that makes it a lot of fun.
[2088.90 --> 2091.80]  But you mentioned TensorFlow, Jared.
[2092.20 --> 2097.62]  What is the state of interaction between R and TensorFlow?
[2097.78 --> 2104.10]  I know it's kind of been a long time coming, for example, in the Go community where you can do inference.
[2105.06 --> 2109.88]  You know, it's recommended that you do inference in Go with TensorFlow, but not necessarily training.
[2109.88 --> 2113.96]  What's kind of the state of interaction between R and TensorFlow?
[2114.28 --> 2124.50]  And are there other kind of larger frameworks that are that are integratable with R, like, you know, maybe PyTorch or other things?
[2125.26 --> 2131.38]  So with the TensorFlow and Keras packages, you get the full functionality of TensorFlow and Keras.
[2131.60 --> 2132.38]  That's awesome.
[2132.38 --> 2133.72]  Yeah, it's really amazing.
[2133.92 --> 2141.66]  I sit on my computer, even on my actually my Windows laptop, and I can build TensorFlow models thanks to the Keras interface in R.
[2142.18 --> 2142.96]  That's awesome.
[2143.12 --> 2144.16]  Who did that work?
[2144.64 --> 2148.94]  So it was mainly J.J. Allaire from the he's the head of R studio.
[2149.90 --> 2154.94]  And Francois Chollet was also involved and the team at Google.
[2155.08 --> 2155.80]  That's awesome.
[2155.80 --> 2157.44]  It's really amazing.
[2157.56 --> 2165.02]  Now, it has TensorFlow as the default, but you can plug in other compatible Keras frameworks.
[2165.62 --> 2174.62]  So it really gives you a broad spectrum of what you can do, though I would say that 99% of the people using Keras and R are using TensorFlow as a framework underneath.
[2175.02 --> 2175.48]  That makes sense.
[2175.72 --> 2176.42]  That's pretty cool.
[2176.42 --> 2192.88]  So I guess as you look forward in R at this point and as we are surging forward for the years to come in AI and ML and stuff, what are you excited about right now in the R community and in your own projects, for that matter, where R is intersecting AI and ML?
[2193.58 --> 2194.76]  So it's kind of funny.
[2194.88 --> 2198.96]  You see other communities and they are super excited about all the different machine learning stuff they can do.
[2199.64 --> 2203.00]  In the R community, it's sort of largely like been there, done that.
[2203.12 --> 2204.28]  R's been doing it for decades.
[2204.28 --> 2208.18]  They're already on to better things.
[2208.46 --> 2210.98]  Not to say better things, but different fun things.
[2211.06 --> 2223.84]  Like we're all super excited about using R Markdown to automate slideshows and reports or HTML widgets to have interactive JavaScript embedded in your R report or different types of graphics or data manipulation or network analysis.
[2223.94 --> 2227.26]  All this other fun stuff that like, yeah, we've been doing machine learning forever.
[2227.42 --> 2229.08]  Look at all this other cool, fun stuff.
[2229.08 --> 2234.94]  Yeah, and I guess at this point, I mean, you have awesome support for things like TensorFlow, like you already said.
[2235.16 --> 2242.82]  And, you know, those sorts of interactions with JavaScript widgets or whatever it might be are really, I think they're really interesting.
[2242.82 --> 2245.78]  And they're really, really cool and fun stuff.
[2245.78 --> 2254.78]  Because let's be honest, the vast majority of time a data scientist spends is not doing all the really cool modeling that we all want to do.
[2254.86 --> 2258.72]  It's doing the data prep, the manipulation, reporting, graphing.
[2258.72 --> 2261.98]  And that's 80 to 90 percent of the job now.
[2262.36 --> 2268.90]  Because now it's become so easy to do the modeling, to do the true AI part that everything else takes up so much time.
[2269.50 --> 2275.94]  So I have a confession that I need to make probably early on in this podcast.
[2276.58 --> 2281.40]  And that's all of this data munging and cleaning and all of that.
[2281.58 --> 2283.78]  I really, really enjoy that.
[2284.44 --> 2285.62]  There's something fun about it.
[2285.62 --> 2288.14]  It's like this problem solving, getting to patch things together.
[2288.14 --> 2296.14]  I don't know what makes me weird in that way, but I just I could spend just days heads down cleaning data.
[2296.50 --> 2297.24]  I really like it.
[2298.04 --> 2299.68]  We need more people like that.
[2300.04 --> 2301.38]  I'll tell you what I know.
[2301.54 --> 2306.10]  I don't know whether to praise you, Daniel, or just to say, wow, that's that's a little bit crazy.
[2306.72 --> 2317.26]  Well, yeah, pair me with with one of you guys and I'll do the data cleaning and you can, you know, add an awesome JavaScript widget powered by TensorFlow or something.
[2318.14 --> 2320.52]  It's funny you make that joke.
[2320.52 --> 2323.54]  But, you know, there's now JavaScript bindings for TensorFlow.
[2324.36 --> 2327.52]  Yeah, that's that's a really a really interesting topic.
[2327.52 --> 2335.10]  And I think that there's like some very subtle but really important implications of things like that.
[2335.24 --> 2338.34]  And that's, you know, around like privacy and other stuff like that.
[2338.52 --> 2352.60]  If you're if you're actually embedding a model in JavaScript and running it on someone's device in their browser or whatever it might be, and maybe even updating a model in the browser, you know, then data never has to leave that person's device.
[2352.60 --> 2357.36]  I think that's like a really important and interesting implication of stuff like that.
[2357.48 --> 2359.34]  I sense a show coming up on that topic.
[2359.84 --> 2361.10]  I would love to have that.
[2361.16 --> 2362.84]  I saw the so there's a demo.
[2363.14 --> 2368.44]  Maybe we'll we'll find the link and put it in the show notes of the recent TensorFlow Dev Summit.
[2368.44 --> 2375.36]  They had a web app that you could play Pac-Man with like your head movements running in the in the browser.
[2375.60 --> 2380.78]  And you would just have to calibrate it by moving your head, you know, a certain number of times.
[2380.78 --> 2388.82]  And it would actually, you know, online update the model and then use your particular head movements to control the game.
[2388.82 --> 2398.88]  And then after you played the game, they had chiropractors and people giving massages, you know, just to it's probably not a game that you're going to want to, you know, want to play all night.
[2399.26 --> 2403.62]  But Jared, so that's all that's a lot of interesting stuff.
[2403.62 --> 2413.28]  But before we go too far down the Pac-Man hole, is there is there anything else that you wanted to mention that you're excited about or things coming up?
[2413.28 --> 2421.64]  So something I'm seeing a lot in the data science community in general, but particularly the R community, is what to do with these models after you've built them.
[2422.04 --> 2424.42]  And in the past, I came up with all sorts of workarounds.
[2424.54 --> 2431.22]  I'd take a model, save it as a binary and then have an R session running and people would have to interact with that using R script.
[2431.90 --> 2439.88]  And now it's becoming so easy through various different tools for other people to now consume the results of the model,
[2439.88 --> 2447.14]  particularly with predictions or scoring, depending on the word you want to use, or even inference as the deep learning community uses,
[2447.36 --> 2449.28]  even though that means something else in the stats community.
[2449.64 --> 2457.00]  It's now become so easy with different tools such as the Plumber API package in R, which turns your R scripts into APIs,
[2457.38 --> 2458.94]  or even third party solutions.
[2459.06 --> 2463.14]  There's a company out there called Algorithmia, and they take your models regardless of the language.
[2463.48 --> 2466.10]  Then you build a API that anyone can hit.
[2466.10 --> 2471.34]  So these tools, we can productionalize our model so easily.
[2471.90 --> 2473.44]  And I can write my code in R.
[2473.70 --> 2481.34]  I could use either Algorithmia or Plumber to create a simple RESTful API, have it running on a server or even a microservice.
[2481.76 --> 2484.52]  Then someone else can go hit that and get the results of my model.
[2484.62 --> 2486.76]  So it really creates this accessibility.
[2487.30 --> 2490.56]  And it's so exciting seeing this happening faster and faster these days.
[2490.56 --> 2491.20]  Yeah.
[2491.20 --> 2502.16]  So I was actually, it's funny that you mentioned that because this morning on my drive in, I was listening to the ChangeLog episode,
[2502.16 --> 2508.88]  which is our Overlords podcast, which you should definitely check out.
[2509.10 --> 2512.08]  But, you know, our kind Overlords podcast.
[2512.08 --> 2517.28]  And they were talking to, I think it was the VP of AI at Microsoft.
[2517.60 --> 2518.98]  We'll link the show in the show notes.
[2519.52 --> 2523.08]  But he was using this terminology around democratizing AI.
[2523.26 --> 2528.84]  And essentially that what we're seeing built now with these tools, like you mentioned, like Plumber and Algorithmia,
[2529.00 --> 2532.54]  and I think other things like Machine Box, like we had on another episode,
[2532.54 --> 2541.38]  is actually creating a layer, a new layer in the software stack, which is making machine learning and AI techniques, you know,
[2541.40 --> 2551.30]  available to, you know, developers that might not have any interest or ability to go deep into the math of the model that they're using.
[2551.98 --> 2556.46]  Yeah, it's making our results accessible to other people to consume.
[2556.46 --> 2560.60]  And that makes it easier to say, they can do their job and I can do my job.
[2560.98 --> 2563.50]  And then we both get a benefit from each other's work.
[2564.50 --> 2565.04]  Yeah, exactly.
[2565.22 --> 2574.56]  And you can say, hey, we are exposing the ability for your program to recognize things or understand speech or whatever it is.
[2574.62 --> 2584.32]  And all they have to do is think about implementing that functionality within their software stack now via a nice API, like a REST API or whatever it is.
[2584.92 --> 2585.40]  Exactly.
[2585.40 --> 2591.96]  And they could be that much more efficient and consume these things that they had no chance of before they would have had to spend all the time building it.
[2592.52 --> 2595.62]  It's specialization in a very great way.
[2596.24 --> 2598.40]  Well, I am super psyched up, Jared.
[2598.66 --> 2608.04]  I am going to have to, as soon as we finish up recording, I'm going to have to go grab your book and start my own journey into R and try to catch up, at least with Daniel at some point here.
[2608.04 --> 2620.14]  And so thank you so much for taking us through this and for me kind of giving me a path forward on how I can start learning R and using it for AI and machine learning.
[2621.14 --> 2622.18]  Great. Thank you for having me.
[2622.26 --> 2623.68]  It's been real fun for me, too.
[2624.28 --> 2624.94]  Awesome. Thanks.
[2624.94 --> 2630.16]  All right. Thank you for tuning into this episode of Practical AI.
[2630.42 --> 2631.90]  If you enjoyed this show, do us a favor.
[2632.00 --> 2633.40]  Go on iTunes and give us a rating.
[2633.66 --> 2635.54]  Go in your podcast app and favorite it.
[2635.62 --> 2638.36]  If you are on Twitter or social network, share a link with a friend.
[2638.42 --> 2640.78]  Whatever you got to do, share the show with a friend if you enjoyed it.
[2641.08 --> 2643.74]  And bandwidth for ChangeLog is provided by Fastly.
[2643.88 --> 2645.30]  Learn more at Fastly.com.
[2645.30 --> 2648.70]  And we catch our errors before our users do here at ChangeLog because of Rollbar.
[2648.96 --> 2651.32]  Check them out at Rollbar.com slash ChangeLog.
[2651.60 --> 2654.12]  And we're hosted on Linode cloud servers.
[2654.48 --> 2656.10]  Head to Linode.com slash ChangeLog.
[2656.18 --> 2656.64]  Check them out.
[2656.72 --> 2657.54]  Support this show.
[2657.96 --> 2661.16]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2661.64 --> 2663.06]  Editing is done by Tim Smith.
[2663.28 --> 2665.34]  The music is by Breakmaster Cylinder.
[2665.76 --> 2669.16]  And you can find more shows just like this at ChangeLog.com.
[2669.38 --> 2671.32]  When you go there, pop in your email address.
[2671.32 --> 2677.64]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2677.96 --> 2678.80]  Thanks for tuning in.
[2678.94 --> 2679.72]  We'll see you next week.
