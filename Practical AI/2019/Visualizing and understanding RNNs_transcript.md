[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.04]  And unlike standard droplets, which use shared virtual CPU threads,
[29.04 --> 32.88]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.42 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.34 --> 45.20]  So if you have build boxes, CICD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.22 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 --> 88.54]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.28]  And now onto the show.
[106.94 --> 110.88]  Welcome to another episode of Practical AI.
[111.34 --> 115.20]  I'm Daniel Leitnack, a data scientist with SIL International,
[115.54 --> 121.70]  and I'm joined by my co-host, Chris Benson, who's a chief AI strategist at Lockheed Martin.
[122.02 --> 122.86]  How are you doing, Chris?
[123.04 --> 123.78]  Doing great today.
[123.84 --> 124.52]  How's it going, Daniel?
[124.52 --> 126.02]  It's going good.
[126.08 --> 130.14]  It was a long weekend here in the U.S., a holiday weekend.
[130.40 --> 137.58]  So I know you're a vegan, but I don't know if you barbecued anything,
[137.98 --> 141.46]  but that's kind of the tradition in the U.S. here on this weekend.
[141.80 --> 144.06]  Well, I didn't barbecue, but we ate far too much.
[144.58 --> 146.10]  So, yes, definitely feeling that.
[146.18 --> 149.50]  Need to get out there and walk or run a bit to work off the calories.
[149.50 --> 151.02]  Yeah, definitely.
[151.90 --> 154.14]  Well, we'll jump right into it.
[154.52 --> 155.42]  I'm really excited.
[155.92 --> 158.60]  Last, you know, I don't know when it was.
[158.68 --> 160.04]  It was a little bit ago.
[160.54 --> 164.50]  I usually like to watch this publication called Distill.
[164.94 --> 172.16]  So you can go to distill.pub, and it's a really great resource to kind of learn about various topics in machine learning.
[172.16 --> 182.24]  And they have really great articles that give explanations of various topics and kind of state-of-the-art research and all sorts of things.
[182.86 --> 190.18]  And recently I saw a great article on there about visualizing memorization in recurrent neural networks.
[190.66 --> 196.94]  And the author of that publication of that article is with us here today, Andreas Masson.
[197.42 --> 198.24]  Welcome, Andreas.
[198.70 --> 199.16]  Hello.
[199.16 --> 209.50]  Yeah, so we're really excited to have you and really excited to dig a little bit into RNNs and visualizing neural networks and all of those things.
[210.06 --> 220.50]  But if you could just give us a little bit of background about how you ended up in AI and what you're doing now.
[220.50 --> 227.90]  Oh, so like eight years ago, I think, like many others, I read the book Programming Collective Intelligence.
[229.16 --> 231.32]  And that was before university.
[231.60 --> 234.66]  So at that point, I sort of knew what I wanted to do.
[234.92 --> 238.62]  So I just took like mathematical engineering at a university.
[239.68 --> 242.04]  And that was sort of before machine learning came a thing.
[242.04 --> 248.32]  And now like, yeah, after five years of education, I had my master's degree in that.
[249.02 --> 253.26]  And now I've been doing freelancing and machine learning for like two years.
[253.26 --> 261.98]  So I like to do like more like heavy science in AI or deep learning.
[262.94 --> 266.56]  But sort of it's a little difficult for me right now.
[266.62 --> 270.24]  So what I'm doing right now is just like do freelance some months of the year.
[270.44 --> 275.22]  And then the rest, I just do like volunteer research with the university.
[275.22 --> 277.06]  Yeah, that's great.
[277.30 --> 287.86]  I know, you know, it's sometimes it's hard to navigate the the roadmap into the specific area of AI that you're interested in.
[287.92 --> 296.92]  But it's awesome to see, you know, that you're you're contributing in a great way to the community, but also doing freelancing and all of that sort of stuff.
[296.92 --> 300.74]  How how has freelancing as a machine learning and AI person?
[301.04 --> 302.56]  How how has that been?
[302.56 --> 310.74]  What what sort of insight can you give those out there that might be be thinking about about doing that sort of thing?
[312.04 --> 314.20]  I don't know if I would recommend it.
[314.98 --> 322.46]  And the thing about freelancing is, you know, your clients, they they don't pay the hours, they pay the product, right?
[322.64 --> 325.98]  And deep learning is very much a research field right now.
[326.02 --> 328.76]  So it's very hard to guarantee anything.
[329.68 --> 330.84]  And they don't like that.
[330.84 --> 339.32]  And so the typical solution, you sort of end up with solutions where you have a very good idea that this is going to work.
[339.32 --> 353.94]  And that is sort of more statistical solutions or like already like this kind of like a cycle learn solutions or yeah, those more like traditional solutions rather than deep learning.
[353.94 --> 356.62]  And this is not that exciting for me.
[356.62 --> 358.16]  So that's why I like to do the research.
[358.16 --> 360.26]  But I mean, it's good for the money.
[362.02 --> 367.82]  So I actually have a quick follow up question about that before we dive, you know, fully into the questions.
[367.82 --> 378.80]  And that is, you mentioned that it was as a freelancer, and I've done freelancing in terms of being like a programmer in the past, but never freelancing in this particular industry.
[379.30 --> 381.82]  And I was just curious, you mentioned paying by the project.
[381.96 --> 388.60]  Is that do they do you do like a fixed fee for a project or do people pay you by the hour kind of in more of a traditional freelance way?
[388.60 --> 390.34]  Like, I'm paid by the day.
[390.78 --> 393.78]  But they get really upset if they don't get like a product, right?
[393.80 --> 398.98]  If you come out with this and say, okay, after three months, like this was the contract.
[399.56 --> 403.96]  And I made this amazing deep learning system.
[404.14 --> 407.48]  Unfortunately, it doesn't work because deep learning in this research, right?
[408.04 --> 409.20]  And but I learned a lot.
[409.26 --> 411.48]  And I think like, next time is going to be better.
[411.48 --> 414.04]  I totally understand what you're saying.
[414.30 --> 416.06]  Like, this doesn't work, right?
[416.12 --> 419.92]  Because I learned something, they don't feel that has any value at all.
[420.48 --> 421.86]  Totally, totally get it.
[422.12 --> 430.86]  It's probably hard to manage expectations to when, you know, a client comes and they say, oh, you know, we've heard deep learning solves everything.
[430.86 --> 434.16]  So I'm assuming you'll be able to solve this problem with deep learning.
[434.42 --> 439.32]  And in the back of your mind, you're thinking either, you know, I'm not sure if it could be solved.
[439.32 --> 444.52]  Or maybe like just random forest with scikit-learn is probably better for these people.
[444.72 --> 446.98]  It's always hard to kind of crush those expectations.
[447.74 --> 448.08]  Exactly.
[448.36 --> 448.90]  Yeah, yeah, yeah.
[449.12 --> 452.28]  And that's whether you're a freelancer or a permanent employee at a company.
[452.50 --> 454.60]  It's that's the same situation.
[455.92 --> 466.56]  So like to dive in, I just wanted to know kind of how you originally got interested in the visualizing aspect of deep networks and, you know, neural units specifically.
[466.56 --> 470.00]  What drew you into that particular subfield?
[471.12 --> 475.92]  I've always sort of been interested in sort of design aspects and that kind of thing.
[476.42 --> 482.52]  Like before I started university, I did a lot of JavaScript and web development, that kind of thing.
[482.52 --> 493.28]  But what sort of really kicked my interest was that I was like a conference some years ago and there was this bank here in Denmark.
[493.42 --> 498.00]  And they said, OK, we have this amazing machine learning model and probably should take that with a grain of salt.
[498.48 --> 506.32]  But they have this amazing machine learning model for predicting whether or not a client or a customer, I should say, could pay back a lot.
[506.32 --> 506.80]  Right.
[508.24 --> 511.68]  And they were super happy about this model.
[511.82 --> 516.78]  It outperformed their typical advisors who had like a master bachelor's degree in finance.
[517.60 --> 518.58]  So that's great.
[518.84 --> 523.04]  But the really big challenge was actually that they couldn't communicate it.
[523.70 --> 526.26]  So in the end, it's the advisor who had to make the decision.
[526.44 --> 528.24]  Should this customer get a loan or not?
[528.24 --> 533.74]  And this advisor have his own education that contradicts the machine learning model.
[535.00 --> 537.18]  And so they didn't trust it.
[537.84 --> 541.84]  And actually, sometimes they just say, OK, I'm not going to listen to the machine learning model.
[542.80 --> 544.00]  That in itself is a problem.
[544.14 --> 552.22]  But also, even if you choose to listen to the machine learning model, how do you explain to the customer that they cannot get the loan?
[553.12 --> 556.26]  Like that's really upsetting for the customer.
[556.26 --> 575.82]  And certainly I don't want to live in this future where as AI become increasingly, increasingly more integrated into our lives, into our lives, maybe we get to the point where also these consequences happen and we cannot really fight against it.
[575.82 --> 579.58]  It's just sort of this machine learning model that end up controlling our life.
[579.58 --> 588.94]  Not because of some dystopian Skynet future, but just because we have learned that we should trust the machine learning model.
[589.12 --> 591.84]  And when we don't agree with it, that's just how it is.
[591.84 --> 601.00]  So you kind of hit right off the bat as you were diving into this, kind of the issue around trust and issues around explainability.
[601.64 --> 607.56]  And then as a consequence of that, the necessity to communicate the value right off the bat.
[607.88 --> 613.44]  So that kind of drove you into this focus on visualizing so that people could kind of get it.
[614.00 --> 614.24]  Yeah.
[614.60 --> 615.66]  I talked to him later.
[615.66 --> 617.42]  So, okay, how do you solve this issue?
[617.62 --> 621.52]  And amazingly, like they didn't take it seriously at all.
[621.80 --> 627.16]  They just said, we do some quantization and with some colors and some arrows and that's sort of it.
[627.16 --> 627.56]  Yeah.
[627.56 --> 628.40]  Yeah.
[628.40 --> 628.56]  Yeah.
[628.78 --> 639.22]  Do you think, like I definitely see it from that perspective that you guys are talking about in terms of like, you know, communicating the value and giving an interpretation.
[639.54 --> 651.72]  Do you think that there is value as well on the like AI practitioner side as far as understanding the types of things that we're doing when we're training a neural network?
[651.72 --> 659.30]  You know, in addition to kind of communicating those results, what do you think are the benefits on the practitioner side?
[660.02 --> 660.88]  Oh, absolutely.
[661.00 --> 664.76]  I think this is actually more what my distill publication is about.
[666.12 --> 669.14]  Because we create all these models here, right?
[669.24 --> 676.36]  And we benchmark them on the same data set and then we clap our hands when we get 0.1% better performance, right?
[676.36 --> 682.02]  But we don't really have a very good understanding about what changed.
[683.24 --> 691.38]  And so, for example, in my publication, right, I show that I have one model that is in another model and they get pretty much the same performance.
[691.80 --> 698.50]  But actually, one model is really good at a long-term contextual understanding and one model is really good at a short-term contextual understanding.
[698.50 --> 709.22]  And if you just always look at the accuracy scores or cross-interpeat laws or whatever, you don't get into that, right?
[709.46 --> 721.68]  So, I think it's really fundamentally necessary to do like good science to look into these things and not just say, okay, this time I worked for half a year.
[721.76 --> 723.82]  We got the 1% better performance.
[723.82 --> 729.90]  I think you need to look into like where did this 1% better performance come from?
[730.16 --> 733.86]  Is it the place that is actually relevant for the task at hand?
[734.82 --> 741.90]  So, how do you accomplish that in the sense of what tools are you using to visualize neural networks in the way that you're doing?
[742.34 --> 746.28]  And obviously, there are things that we're familiar with, you know, like TensorBoard and such.
[746.28 --> 756.58]  You know, kind of as an addendum to that, how does design and understand user interactivity play into your ability to do that?
[758.04 --> 762.64]  Yeah, I think for me, like TensorBoard is a lot more about debugging.
[764.06 --> 768.58]  And it's really difficult to answer the other question, right?
[768.58 --> 774.26]  Because fundamentally, it's about how do we understand how our deep learning model works.
[774.40 --> 783.26]  And that is something that's really complicated because it's like about you take a brain, you slice it up and you look at the individual neurons.
[783.78 --> 788.12]  And somehow you have to ask this person, what is your favorite color, right?
[788.62 --> 789.94]  Just from looking at the neurons.
[789.94 --> 797.52]  And I mean, I don't think we can imagine that technology in the next 10 years when it comes to humans.
[797.76 --> 804.18]  And it's the same kind of complexity that we have when working with these kind of deep learning models.
[804.96 --> 809.82]  So, you somehow have to like aggregate all this information in some smart way.
[810.76 --> 814.94]  And that in itself is not just enough.
[814.94 --> 818.80]  So, I think there's like three components to make to really understand something.
[818.80 --> 822.78]  One is you need a data set that you can understand.
[823.58 --> 831.12]  So, for example, if you talk about like natural language processing, like sometimes we just use Chinese poetry generation, right?
[831.70 --> 837.00]  It's really hard to understand how well it creates Chinese poetry, right?
[839.12 --> 841.14]  I certainly couldn't understand that.
[841.82 --> 847.82]  I mean, I think the overlap between Chinese poetry writers and machine learning enthusiasts is probably quite small.
[848.80 --> 852.26]  That's true.
[852.48 --> 853.80]  We need more of them.
[854.26 --> 854.38]  Yeah.
[855.80 --> 872.44]  So, like maybe just to follow up on that, like when you're talking about kind of the, as you put together your data set, as you use these models, there's the need to kind of visualize and understand what's going on at a lower level.
[872.44 --> 885.88]  How did, like where, where the workflow of being an AI practitioner, like if I'm approaching a problem, where do you think I need to be thinking about these things on a little bit deeper level?
[885.88 --> 893.86]  Is it like just at the learning time, like when I learn about RNNs, then I need to kind of learn about these things and then move on?
[893.98 --> 907.02]  Or is there an ongoing need to kind of run these sorts of visualizations or maybe more controlled experiments to understand at a deeper level or at a more intuitive level what's happening?
[907.02 --> 914.48]  Yeah, I think like once you have your model and you think that it works okay, like look into what does it actually do.
[916.24 --> 929.42]  It's really hard as a debugging tool to use this kind of visualization because if you have a model that doesn't really work that well, you sort of just get nonsense out of your visualization.
[929.42 --> 930.42]  Right.
[930.42 --> 930.78]  Right.
[931.78 --> 938.22]  So you need, like in the end, you have a nice model, it works, and you want to show maybe it's better than this other model.
[938.46 --> 941.46]  Like okay, compare them up against the same kind of visualization.
[942.00 --> 944.46]  Does it show what you would expect?
[944.46 --> 954.98]  So as you're going through this process, you kind of mentioned earlier that you, prior to getting into the field, that you had used things like web development tools and you were using JavaScript and such.
[955.60 --> 964.22]  Are those skills that you developed ahead of time playing in to kind of like when you actually are producing a visualization or using those kinds of tools?
[964.30 --> 965.08]  Like which ones?
[965.08 --> 979.76]  Are there things you could point to somebody else who is kind of getting into, they're interested in this subfield of visualizing and you would say, hey, go use tools A, B, and C, and then this is the workflow through it.
[979.86 --> 981.24]  Is there something you can point to in that way?
[983.08 --> 983.48]  No.
[983.68 --> 990.80]  I mean, there's some tools like out there like LSTMVS, I think is a tool that I've seen some use.
[990.80 --> 995.76]  All the tools you're seeing in the Distilled article, I just programmed them from scratch.
[998.16 --> 1005.84]  I use these three for visualization, which basically gives you nothing but a few access and some like data management tools.
[1007.16 --> 1009.82]  But like I said, like there's these three points.
[1010.00 --> 1014.94]  Like one is the data set and then the other part is like having a good visualization.
[1014.94 --> 1029.34]  But then the third really important part is having sort of the feedback loop where like you can very quickly ask a question or like in this case you hover or a character and then you get some sort of visual feedback.
[1030.30 --> 1039.22]  And because this is like an interactive part, you get this sort of feedback loop and that is really what generates your intuitive understanding.
[1039.22 --> 1043.34]  And I mean, you don't need to use web development tool for this.
[1043.42 --> 1046.48]  I'm sure you can use it in, do it in pure Python.
[1047.58 --> 1050.36]  Like you can do some pretty funny things in Matplotlib.
[1051.02 --> 1051.66]  Yeah, absolutely.
[1052.30 --> 1052.72]  Yeah, yeah.
[1052.90 --> 1061.26]  But you definitely lead this kind of interactive piece here in order to get this feedback loop,
[1061.26 --> 1065.82]  which is really what's fundamentally creating your intuitive understanding, I think.
[1069.22 --> 1076.48]  This episode is brought to you by Discover.Bot.
[1076.68 --> 1080.66]  Learn everything there is to know about bots at Discover.Bot slash PracticalAI.
[1081.20 --> 1088.90]  Discover.Bot was built by Amazon Registry Services as an online community for bot creators and makers of all skill levels to learn from one another, to share stories.
[1089.02 --> 1095.26]  And they regularly publish guides and resources to answer questions like how to set up payments to your bot, how to stop shopping cart abandonment,
[1095.26 --> 1099.30]  what KPIs are worth measuring, how to write an engaging chatbot dialogue.
[1099.74 --> 1101.68]  You can even register .bot domains there.
[1101.96 --> 1106.54]  Learn more and explore this huge library of bot resources at discover.bot slash PracticalAI.
[1107.02 --> 1109.40]  Again, discover.bot slash PracticalAI.
[1109.40 --> 1139.38]  So, Andreas, you mentioned right before when you were talking about the type of tooling that you're using that interactivity is really a key piece of this puzzle in kind of developing good visualizations of complicated things like neural networks.
[1139.38 --> 1155.04]  I know that that sort of interactivity and kind of interactive visual forward sort of idea is behind this Distill publication that we've been talking about.
[1155.22 --> 1166.60]  So, could you describe a little bit kind of how you got interested in this Distill publication, maybe what it is, maybe orient people to how it's different from kind of a normal academic type journal article?
[1166.60 --> 1167.24]  Right.
[1167.24 --> 1167.36]  Right.
[1168.40 --> 1172.80]  So, normal academic journals, you know, it's a PDF.
[1173.16 --> 1173.90]  Why is it a PDF?
[1174.08 --> 1175.96]  It's because we used to print everything.
[1175.96 --> 1185.38]  So, I think they still have this interesting thought that we really want to explain and visualize things better.
[1185.92 --> 1203.82]  And we actually, what about that we don't take the PDF format, but we use sort of the interactive capabilities of the web platform in order to visualize and explain on a completely different level than what you can normally do in a PDF document.
[1203.82 --> 1207.76]  I think that's really like the core philosophy of Distill.
[1208.70 --> 1215.02]  So, if you're out there doing some work and that feels like, what does it take to get published on that?
[1215.22 --> 1216.72]  How do you get into the process?
[1217.92 --> 1221.86]  And is it, you know, how does it differ from, say, doing academic publishing?
[1221.86 --> 1226.00]  Well, it's a volunteer organization, right?
[1226.14 --> 1229.00]  So, I think you have to be a patient person.
[1229.80 --> 1237.84]  This one took like almost a year from, I will say, eight months from I finished writing it to it getting published.
[1237.84 --> 1247.42]  And that part is just a lot of feedback that you get from Ludwig and Chris who runs Distill.
[1247.76 --> 1250.72]  And they do this on a volunteer time.
[1251.84 --> 1256.30]  So, you get amazing feedback from them, like almost on a mental level.
[1256.30 --> 1264.02]  But it takes a long time and they can go months where you don't get anything and you have no idea if you're going to get published or not.
[1264.84 --> 1268.84]  Considering how fast the field is moving, does that cause any kind of concern for you?
[1268.94 --> 1275.86]  Just going that length of time, considering that somebody else may publish something similar to what you're working on in that time frame?
[1276.54 --> 1277.50]  Not in that field, no.
[1278.14 --> 1279.78]  Like visualization, no.
[1279.92 --> 1281.12]  Not a lot of people do that.
[1281.12 --> 1285.70]  But I know it's something they want to improve.
[1285.82 --> 1287.30]  They want to get it down to three months.
[1287.42 --> 1289.40]  And I think they're going to get there with some more help.
[1290.82 --> 1293.92]  So, yeah, it's not something I would worry so much about.
[1294.38 --> 1299.78]  In terms of how you get into it, like you just go to the website under a publication and you send a new thing.
[1301.56 --> 1303.82]  But, I mean, just know like they don't do anything.
[1303.82 --> 1307.72]  All these amazing visualizations that you see is something you create yourself.
[1307.72 --> 1308.32]  Yeah.
[1309.64 --> 1316.36]  So, I mean, it sounds like there's a real, maybe there's a need for more people doing this.
[1316.54 --> 1325.84]  If, you know, more people doing this and also developing good tools around it, you know, since there is a fairly small group of people doing this.
[1325.84 --> 1335.48]  I know that your, so your Distill publication was specifically focused on recurrent neural networks and recurrent units.
[1335.82 --> 1338.70]  So, LSTMs and other things.
[1339.20 --> 1347.58]  I was wondering, you know, on the podcast, we've talked about a lot of different type architectures, neural network architectures.
[1347.58 --> 1357.02]  So, maybe you could just give us kind of a brief crash course in recurrent neural networks, just a brief description of what those are.
[1357.30 --> 1360.40]  Because I don't think we've actually done that on this show yet.
[1360.40 --> 1369.50]  So, in relation to kind of maybe what we would consider like a quote unquote basic neural network.
[1369.50 --> 1378.40]  So, like a fully connected neural network where inputs come in and then they're added together and an activation function is applied.
[1379.34 --> 1383.60]  And then they're passed off to a next layer where the kind of the same thing happens.
[1383.60 --> 1386.88]  And they eventually get to the other side of the neural network as output.
[1387.42 --> 1399.54]  How do recurrent neural networks and the units that are used in those neural networks, how do they differ from the kind of basic fully connected situation?
[1400.62 --> 1400.80]  Yeah.
[1400.96 --> 1408.78]  So, like you said, like in a typical neural network, you have some sort of like fixed input, right?
[1408.78 --> 1417.04]  So, you have like maybe 10 input elements or maybe a picture of some fixed size and you pass this through your network and you get an output.
[1418.22 --> 1428.74]  That doesn't really apply that well to text or audio, for example, because sentences, they have different number of characters or different number of words.
[1428.92 --> 1434.90]  So, you don't have the same number of input values really every time.
[1434.90 --> 1445.14]  So, instead you do this as a sequence of input vectors and you just start from like the first part of the sequence.
[1445.46 --> 1450.22]  So, it could be the first word and you put this, you describe that with some input.
[1450.46 --> 1455.98]  Like maybe you have a really big dictionary where you just assign one number to every single word.
[1455.98 --> 1465.38]  And then you pass this through your network and then you go to the next word in your sequence and you pass this through.
[1465.78 --> 1468.66]  But how do you then combine that with the previous word?
[1468.76 --> 1481.18]  So, you just take every sort of intermediate output that you have in your network and you concatenate that with every intermediate output for this next word here.
[1481.18 --> 1494.52]  So, by concatenating like what you got from the previous word to with this word here, you can really sort of in theory memorize something from the entire sequence.
[1494.52 --> 1500.24]  So, it's like, let's say if we have the example of words, one word.
[1500.86 --> 1511.82]  So, word one comes in, but then when we process word two, we process word two along with something that was output the first time.
[1511.92 --> 1514.04]  Is that kind of the basic flow or?
[1514.48 --> 1515.80]  Yeah, that's the basic flow, right?
[1515.80 --> 1527.38]  And then sort of your intuitive idea might be, okay, as I go through this sequence of characters, I would be likely to forget something from the very beginning.
[1528.86 --> 1532.30]  And so, this is sort of what's called the vanishing gradient problem.
[1533.28 --> 1541.00]  And that is solved through this thing called LSTM, for example, with sort of trance.
[1541.00 --> 1550.42]  And we've mentioned LSTM several times in the podcast, but for those who aren't familiar, can you just quickly define that as just a quick one-off and then continue your thought?
[1551.14 --> 1551.40]  Yeah.
[1551.86 --> 1556.38]  So, LSTM is basically just trying to simulate a memory cell in a computer.
[1556.64 --> 1560.56]  So, it has like the capacity to memorize something for a long period of time.
[1562.56 --> 1564.38]  And that's how I would describe it.
[1564.38 --> 1571.86]  And similarly, we have the GRU, which is just a different variation of that, but it uses less memory, let's say.
[1573.14 --> 1574.38]  Like physical memory.
[1575.30 --> 1575.46]  Yeah.
[1575.66 --> 1584.26]  And so, those long, short-term memories, so the LSTM and the gated recurrent units or GRUs, you talk about those a lot.
[1584.62 --> 1587.94]  I mean, that's kind of part of the focus of your publication, right?
[1588.38 --> 1592.96]  Yeah, because they really solve the same issue, just in different ways.
[1592.96 --> 1597.92]  They solve this vanishing gradient issue, or forgetting in long sequences, right?
[1598.38 --> 1603.92]  And so, just to position it, those are specific types of recurrent neural networks, right?
[1604.64 --> 1609.18]  There's specific components in recurrent neural networks, I would say.
[1609.20 --> 1609.38]  Yep.
[1609.88 --> 1610.40]  Fair enough.
[1611.14 --> 1612.32]  Yeah, specific units of it.
[1612.32 --> 1624.50]  So, when you're saying the vanishing gradient problem, and you also mentioned memorization in recurrent neural networks, are we talking about the same thing?
[1624.60 --> 1625.30]  Are those different?
[1625.30 --> 1631.92]  Well, they're sort of like part of the same coin, as you say.
[1633.66 --> 1637.32]  Like, if you have a vanishing gradient problem, that certainly means that you cannot memorize.
[1637.32 --> 1644.88]  But you can have issues with memorization, even if you theoretically don't have an vanishing gradient problem.
[1647.58 --> 1655.12]  So, for example, what we see in this publication I've written, right, is basically just autocomplete, like you have on your phone.
[1655.12 --> 1664.94]  And so, as you type, it sort of catches on from the previous words that you put in, and it tries to guess the next word.
[1665.44 --> 1668.88]  Or if you're in this word here, you put in a few characters.
[1668.88 --> 1677.04]  Then you might just use the last few characters instead of the previous words to guess what it is that you want to type.
[1678.68 --> 1682.60]  And so, here we sort of have two different concepts.
[1683.10 --> 1687.44]  One is long-term memorization, where we use previous words.
[1687.60 --> 1691.96]  And another is short-term memorization, where we just use the previous characters from the same word.
[1691.96 --> 1709.22]  And what I've sort of seen is, and I think this is very specific to sort of your data set, but at least for this application and data set, the LSTM shows that it's better at short-term memorization, where the guru shows it's better at long-term memorization.
[1709.64 --> 1712.78]  But if you look into, like, the theory, there's no reason for that.
[1713.10 --> 1716.38]  They both solve the vanishing gradient problem in their own ways.
[1717.54 --> 1719.12]  So, where did that leave you?
[1719.12 --> 1724.80]  It sounds like that's kind of the summary of what you took away from that.
[1725.26 --> 1735.14]  And so, recognizing that you had the LSTM architecture was great for that short-term character-by-character approach, whereas the GRU was better at word-by-word.
[1736.92 --> 1745.10]  Presumably in an architecture where you do some combinations and stuff, I mean, what learnings did you take away that you would use in things going forward with that?
[1745.32 --> 1745.84]  Right.
[1745.84 --> 1753.86]  I think the wrong learning is to take that, okay, GRU is better at long-term memorization, because I don't think that's the case.
[1754.26 --> 1754.46]  Okay.
[1754.46 --> 1763.04]  But if you just look at, for example, the accuracy or the cross-entropy, you get almost the same value, right?
[1763.04 --> 1771.96]  But we see such a huge difference in how they actually behave.
[1773.30 --> 1780.30]  And that is, like, the LSTM is really good at the short-term local characters, right?
[1780.36 --> 1784.74]  So, it gets its score from that, and the GRU gets its score from the long-term.
[1784.74 --> 1789.00]  So, what kind of practical thing, I mean, how would you use that?
[1789.08 --> 1798.12]  If you were going to go into your next project, how would that influence the next thing that you're going to do in the space?
[1798.86 --> 1799.24]  Right.
[1799.36 --> 1805.32]  So, like, let's say I have a customer, right, and they want an autocomplete function or whatever.
[1805.32 --> 1810.36]  I mean, it might be worth to ask them, okay, I mean, what is important for you?
[1810.50 --> 1815.30]  Is it that it understands the full context or is that it understands the locality?
[1817.30 --> 1820.32]  Of course, it would be nice to get the best of both worlds, right?
[1820.72 --> 1823.68]  And probably you can do that if you do some more advanced stuff.
[1823.68 --> 1828.72]  But it's not always that you have the data in order to make that choice.
[1829.46 --> 1837.94]  And maybe, you know, maybe it's like a, you know, I don't want to put words in your mouth, so give me your thought on this.
[1837.94 --> 1853.26]  But it seems like recently, like, people like Allen AI Institute or Spacey or even, like, OpenAI coming out with GPT-2 and all of these kind of text models.
[1853.26 --> 1869.80]  It seems like there is a trend to show visually, like, you know, things like co-reference and, like, visual examples of how, like, BERT, for example, is embedding words and, like, all of these different kind of visual ways.
[1869.88 --> 1878.84]  It seems like people are really seeking after kind of visual tools that they can utilize, like, on, for example, on their next BERT project where they're utilizing BERT.
[1878.84 --> 1884.84]  They want to have a tool in their tool set to kind of visualize how, visualize the embeddings.
[1885.56 --> 1888.58]  Or, like, in this case, maybe you're using an RNN model.
[1888.76 --> 1894.44]  Maybe for that particular data set, you do try a bunch of different models.
[1894.62 --> 1902.88]  But then you kind of have this visualization tool in your toolbox to be able to understand for this particular problem,
[1902.88 --> 1909.08]  what are the memorization implications of these different architectures that I'm trying.
[1909.26 --> 1914.46]  Would that be a good way to kind of utilize, maybe leverage some of the stuff that you've done and say, you know,
[1914.50 --> 1919.96]  this is a tool that I can use to visualize these sorts of memory issues for my particular problem?
[1920.86 --> 1930.18]  Yeah, I think what was really important for me in this publication was to create a tool that is so general that you can really compare many different kind of architectures.
[1930.18 --> 1934.66]  Like, does it have an attention or is it bidirectional, right?
[1936.20 --> 1943.06]  That was really what was important for me here because that creates, like, a really strong scientific tool for comparing different models.
[1945.78 --> 1955.70]  If you look at, for example, like, in some cases, you just look at an attention mechanism in a network and that is a different way of visualizing.
[1955.70 --> 1957.62]  Or you look at embedding, as you talked about.
[1958.66 --> 1964.56]  So this is what I would call internal visualization, where what I've done is what I would call external visualization.
[1965.04 --> 1971.82]  Because the sort of visualization strategy I have only looks at the output with respect to the input.
[1971.94 --> 1974.02]  It doesn't look at anything in the middle.
[1974.80 --> 1977.12]  And I think there's space for both things.
[1977.12 --> 1978.12]  Yeah.
[1978.12 --> 1979.12]  Yeah.
[1979.12 --> 1980.12]  Yeah.
[1980.12 --> 1981.12]  Yeah.
[1981.12 --> 1982.12]  Yeah.
[1982.12 --> 1983.12]  Yeah.
[1983.12 --> 1995.98]  I think the sort of the input-output part, the not intermediate part is perhaps mostly for arguing or explaining your model rather.
[1995.98 --> 2002.68]  And the sort of intermediate part is really for, like, validating your model that it did come up with something meaningful.
[2002.68 --> 2012.12]  This episode is brought to you by StrongDM.
[2012.46 --> 2020.74]  StrongDM makes it easy for DevOps to enforce the controls InfoSec teams require, manage access to any database, server, and any environment.
[2021.22 --> 2024.74]  And in this segment, we're talking to Jim Mortco, VP of Engineering at Hearst.
[2024.86 --> 2028.68]  He's sharing how they're using StrongDM within their team of 90-plus engineers.
[2028.68 --> 2034.62]  It now takes them just 60 seconds to off-board a team member from a data source.
[2034.92 --> 2038.46]  We have an engineering team of somewhere in the area of 80 or 90 engineers.
[2038.84 --> 2045.60]  Because we've got so many services and many databases and so many developers, we need a reasonable way to manage access to them.
[2046.02 --> 2049.62]  It was a somewhat painful and, you know, labor-intensive process.
[2050.28 --> 2056.02]  Our DevOps team would literally have to manage every one of the permissions for everybody who wanted access.
[2056.02 --> 2059.66]  So StrongDM has been a real godsend in that area for us.
[2060.02 --> 2063.50]  Requests for access to specific databases were pretty much manual.
[2063.70 --> 2065.08]  Now we've adopted StrongDM.
[2065.30 --> 2067.30]  It's something that you don't even know is there.
[2067.42 --> 2068.88]  Once it's installed, it just works.
[2068.96 --> 2069.56]  It's very simple.
[2069.88 --> 2075.86]  We've set up a multitude of data sources so that when somebody's onboarded, we just give them access to StrongDM.
[2076.14 --> 2076.96]  It's pretty simple.
[2076.96 --> 2083.54]  Our DevOps team, they have a very minimal effort required to enable each data source to be connected to StrongDM.
[2083.76 --> 2087.48]  And then installing the client software is very, very simple and straightforward.
[2087.72 --> 2090.08]  You can use whatever client you want to to talk to the database.
[2090.22 --> 2091.66]  So there's really no training necessary.
[2092.16 --> 2092.46]  All right.
[2092.48 --> 2098.10]  If your team can benefit from nearly instant onboarding and offboarding that's fully SOC2 compliant,
[2098.42 --> 2102.02]  head to StrongDM.com to learn more and request a free demo.
[2102.34 --> 2104.40]  Again, StrongDM.com.
[2106.96 --> 2107.96]  StrongDM.com
[2107.96 --> 2122.96]  So, Andreas, how did you get interested into diving into unique neural units?
[2123.28 --> 2130.12]  I know you've studied some different types of neural units such as SparseMax and NALU and things like that.
[2130.22 --> 2131.88]  Could you kind of tell us how you got into it?
[2131.88 --> 2137.92]  I mean, I just got into it through my university.
[2138.88 --> 2147.28]  And I like sort of these kind of like very fundamental things that where we can actually understand them.
[2147.40 --> 2151.98]  Like if you have a 30 layer network, it can be really hard to understand how it works.
[2151.98 --> 2161.36]  But if you focus on like a specific unit and try to really understand that, that can give you a lot.
[2161.46 --> 2162.86]  And for example, the SparseMax.
[2163.10 --> 2165.36]  So most of you are probably familiar with the SoftMax.
[2165.48 --> 2171.06]  The SparseMax is just a version of that is capable of predicting zero probability, one probability.
[2171.74 --> 2175.06]  That can also be a great tool for understanding something.
[2175.06 --> 2179.90]  Because you get a much higher contrast in your visualizations.
[2181.30 --> 2181.78]  Awesome.
[2181.96 --> 2191.12]  So what do you think in light of these kind of fundamental things that you like exploring, what are you wanting to explore next?
[2191.22 --> 2197.24]  Do you have any interesting new neural units or anything that you're trying to visualize right now?
[2197.24 --> 2211.40]  I don't know so much about visualization, but I've done a lot of work on this NALO that is really just trying to do mathematical operations like addition and multiplication and learn that.
[2212.14 --> 2220.10]  And they have this gating mechanism in NALO that like can either choose addition or multiplication and it doesn't work at all.
[2220.10 --> 2226.46]  But I think it's a really interesting concept and I think that's something I would like to look more into.
[2226.68 --> 2234.80]  Like these like fundamental gating mechanisms that we have in LSTM and GRU and also these more specialized things such as NALO.
[2235.12 --> 2237.06]  Like what is it really that drives them?
[2237.14 --> 2240.58]  What is it really that makes them choose either this or that?
[2240.58 --> 2240.68]  Yeah.
[2241.58 --> 2241.88]  Yeah.
[2242.02 --> 2251.84]  So could you could you maybe dig into that a little bit in terms of what you mean by this sort of gating mechanism in terms of maybe.
[2252.28 --> 2259.82]  So you were saying this NALO, which is the neural arithmetic logic unit.
[2259.82 --> 2270.04]  I think if if I have that right, it kind of has a it has a gate between the like you were saying addition or multiplication.
[2270.04 --> 2270.66]  What is it?
[2270.72 --> 2273.00]  What is that gating kind of mean and why?
[2273.18 --> 2274.22]  Why would it be useful?
[2275.50 --> 2283.12]  I mean, so the sort of idea is that you have some kind of maybe physical model, but you don't know what the physical model is.
[2283.12 --> 2289.62]  And physical models typically are composed of additions and multiplications.
[2290.32 --> 2297.36]  And so you would like to learn what is sort of the appropriate order of addition and multiplications that needs to be performed.
[2298.66 --> 2299.16]  I gotcha.
[2299.24 --> 2305.54]  So it's like in a it's like in a in a the most simple of neural networks that we're thinking about.
[2305.54 --> 2311.58]  Maybe you have one operation that's repeated over and over in the different different nodes of the network.
[2311.58 --> 2317.56]  Here you're saying, well, I don't know exactly what combination of operations is the best combination.
[2317.56 --> 2322.12]  So I'm going to have a mechanism to switch between between them.
[2322.22 --> 2322.70]  Is that right?
[2323.10 --> 2323.26]  Yeah.
[2323.36 --> 2325.68]  I mean, I mean, in fear, you could go crazy.
[2325.80 --> 2325.98]  Right.
[2326.00 --> 2329.48]  You could also have something that could switch between LSTM and GRU.
[2330.18 --> 2330.40]  Right.
[2332.00 --> 2334.34]  It's a bit crazy, perhaps.
[2334.34 --> 2342.40]  But like a getting mechanism is really just something that can switch either completely or partially between two very different things.
[2344.16 --> 2355.02]  It's sort of what I've done in the last couple of months of my research here is I sort of discovered that in order to do this kind of switch, they need to actually be to be quite similar.
[2355.02 --> 2358.92]  Like in LSTM, the different parts you switch between are very similar.
[2359.38 --> 2365.24]  But in Nalo, one part is addition and one part is multiplication, which have completely different behaviors.
[2365.90 --> 2368.78]  And that actually makes it a really big challenge.
[2368.78 --> 2384.68]  So if you're listening to this and you're getting interested in unique neural units and you want to kind of dive into it yourself or maybe even get ambitious and design some of your own or something, do you have any tips for people on how to explore this particular area?
[2386.08 --> 2394.36]  I think there's always like a few things to consider when designing like a custom neural unit, right?
[2394.36 --> 2402.28]  One is the gradients, like you can maybe come up with something, but then the gradients are zero in many cases.
[2402.42 --> 2403.00]  That's not great.
[2403.52 --> 2406.24]  And the other part is how are you going to initialize the weights?
[2408.68 --> 2418.42]  And so those are like two quite big challenges and something that probably wants that you should think about when designing these kind of units.
[2419.62 --> 2422.30]  Beyond that, I mean, do whatever you like.
[2422.30 --> 2433.28]  So what have been useful ways for you to kind of understand kind of some of the best ways to initialize weights and those sorts of things?
[2433.32 --> 2444.08]  Has it been mostly trial and error or is there any sort of kind of, you know, systematic way you can go about exploring the certain ways to initialize and best ways to do that?
[2444.46 --> 2448.64]  I know that can be a particularly challenging element of this.
[2448.64 --> 2452.78]  About 10 pages of probability, I would say.
[2455.32 --> 2457.14]  Like that's really the strategy.
[2457.32 --> 2464.92]  Like sometimes you're stuck and you don't really know how to sort of calculate the expectation of the variance of this particular structure.
[2464.92 --> 2470.00]  In that case, like Taylor approximations can be really nice.
[2470.50 --> 2474.98]  You can go on Wikipedia and so it's for like Taylor approximation of moments.
[2474.98 --> 2481.96]  So that can be quite helpful to at least come up with some reasonable initialization.
[2484.06 --> 2484.50]  Yeah.
[2485.46 --> 2488.30]  Beyond that, like just run your model quite a lot of time.
[2488.44 --> 2492.46]  See, does this initialization scheme, does it like converge consistently?
[2492.46 --> 2492.54]  Totally.
[2493.34 --> 2498.36]  So I kind of have a follow up from that and I really, really like what you're saying.
[2498.46 --> 2516.28]  And I also find it encouraging that, you know, the you've kind of you found your way into this and are publishing in like really great places like Distill, you know, and you kind of develop this passion while you were doing sort of web development and and other things.
[2516.28 --> 2533.20]  I imagine that there's some listeners out there that are maybe doing like web development things right now and have a really big interest in in AI, but maybe are somewhat frightened by like Taylor approximation of moments and other things like this.
[2533.58 --> 2546.20]  As you know, I think it's encouraging, first of all, that like just to see the great things that you're doing and that you came kind of from that background and you have that passion and that's really driven you to to do these things.
[2546.28 --> 2565.00]  And I'm just wondering kind of is there any encouragement that you can give to those sorts of people or resources that have been helpful for you along the way and kind of going from sort of a different sort of engineering and getting interested in AI to doing some of this more more detailed work?
[2565.88 --> 2572.40]  I mean, so between the web development and now I had like five years of mathematical education, right?
[2572.40 --> 2578.22]  And so that's certainly a journey that you have to take.
[2578.36 --> 2586.86]  I think if you want encouragement, like you don't need that kind of mathematical education just to do some neural networks.
[2586.86 --> 2595.46]  But if you really want to to get into that kind of like really difficult stuff and publish, it's a long journey and just be patient, I think.
[2595.46 --> 2605.04]  Yeah. And I think that you obviously have a passion for these things and that can really, really drive you drive you forward.
[2605.22 --> 2615.26]  I think that, yeah, these certain mathematical pieces aren't out of people's grasp, but it does take some some work to put put the time in.
[2615.26 --> 2628.64]  And I know continually as things like new topics come out and all of those things, I have a whole list of things that I that I need to brush up on and and and learn learn more about it.
[2628.72 --> 2636.70]  And I imagine if you want to get into AI, it's kind of like a lifelong thing of learning about all of these sorts of random things.
[2636.70 --> 2645.16]  I don't know if you can you can sympathize with that, Chris, but that's certainly how I felt every time I knock one thing off my list.
[2645.16 --> 2648.36]  There's by the time I look up again, there's three more to jump into.
[2648.56 --> 2658.14]  So I think for me, at least the question is trying to figure out how to how to shortcut as much as I can to get where it is that I want to go in particular.
[2658.96 --> 2659.56]  All right. Yeah.
[2659.56 --> 2668.64]  So, well, thank you so much for, you know, for for taking the time to walk us through some of these things.
[2668.64 --> 2679.18]  We're definitely going to post the link to your to your distill publication and our show notes so everyone can can read the great article there.
[2679.92 --> 2687.68]  Any any other ways that we can connect people with to you on on the web or other things you'd like to point to?
[2687.68 --> 2691.08]  I mean, you can find me on Twitter.
[2691.66 --> 2695.18]  I still have my what is called private messages open.
[2696.04 --> 2700.60]  So Andreas underscore Madsen and I'm also on GitHub as Andreas Madsen.
[2701.24 --> 2702.88]  Awesome. Well, thank you so much.
[2703.42 --> 2707.02]  This has been this has been really a great conversation.
[2707.24 --> 2711.72]  I know I've learned a lot and really appreciate you taking time.
[2711.82 --> 2712.56]  Thanks for joining us.
[2712.86 --> 2713.96]  Yeah, thank you. It was great.
[2716.48 --> 2717.06]  All right.
[2717.06 --> 2719.74]  Thank you for tuning into this episode of Practical AI.
[2720.00 --> 2721.44]  If you enjoyed the show, do us a favor.
[2721.56 --> 2722.16]  Go on iTunes.
[2722.28 --> 2722.96]  Give us a rating.
[2723.26 --> 2725.08]  Go in your podcast app and favorite it.
[2725.20 --> 2727.92]  If you are on Twitter or social network, share a link with a friend.
[2727.98 --> 2728.66]  Whatever you got to do.
[2728.90 --> 2730.36]  Share the show with a friend if you enjoyed it.
[2730.64 --> 2733.30]  And bandwidth for changelog is provided by Fastly.
[2733.42 --> 2734.86]  Learn more at fastly.com.
[2735.04 --> 2738.24]  And we catch our errors before our users do here at changelog because of Rollbar.
[2738.48 --> 2740.86]  Check them out at rollbar.com slash changelog.
[2741.16 --> 2743.06]  And we're hosted on Linode cloud servers.
[2744.02 --> 2745.06]  Head to linode.com slash changelog.
[2745.06 --> 2746.18]  Check them out.
[2746.26 --> 2747.10]  Support this show.
[2747.50 --> 2750.68]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2751.12 --> 2753.20]  The music is by Breakmaster Cylinder.
[2753.64 --> 2757.02]  And you can find more shows just like this at changelog.com.
[2757.22 --> 2759.16]  When you go there, pop in your email address.
[2759.44 --> 2765.48]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2765.88 --> 2766.64]  Thanks for tuning in.
[2766.80 --> 2767.56]  We'll see you next week.
[2767.56 --> 2797.54]  We'll see you next week.
