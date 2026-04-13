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
[86.78 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[106.66 → 111.26] Welcome to another fully connected episode of Practical AI,
[111.64 → 117.90] where my co-host Chris and I keep you fully connected with everything that's happening in the AI community.
[118.44 → 121.94] We're going to take some time to discuss the latest AI news,
[121.94 → 126.58] and we'll dig into some learning resources to help you level up your machine learning game.
[126.58 → 132.48] So I'm joined today by my co-host, Chris Benson, who's a chief strategist for AI,
[132.74 → 136.24] high-performance computing, and AI ethics at Lockheed Martin.
[136.76 → 138.18] And I'm Daniel Whiten ack.
[138.28 → 140.78] I'm a data scientist with SIL International.
[141.24 → 142.02] How's it going, Chris?
[142.32 → 143.30] It's going great.
[143.40 → 144.50] I'm excited today.
[145.06 → 146.10] Yeah, me too.
[146.48 → 148.22] How's the week been for you?
[148.54 → 149.58] The week's been good.
[149.58 → 152.50] I've been doing lots of stuff at work.
[152.80 → 154.68] I was travelling about a week ago.
[154.76 → 156.14] I was up in Boston at Lifeworks.
[157.40 → 162.28] And I've been doing lots of interesting stuff in high-performance computing and AI ethics.
[163.04 → 167.86] And artificial intelligence as a field just keeps getting more and more interesting in terms of what we're doing,
[168.02 → 171.44] and just at large, and all the places you can go in it.
[171.52 → 172.66] So great time to be in it.
[172.66 → 173.18] Yeah.
[173.52 → 175.80] Well, hopefully I'll survive.
[176.00 → 178.48] I'm working on a little bit of a jet lag right now.
[178.98 → 182.30] As you know, last week I was in India, which was great.
[183.10 → 184.62] I was in Bangalore.
[185.18 → 187.02] But India was great.
[187.20 → 189.80] But getting back from India was quite a chore.
[190.38 → 193.30] So it turns out I was on an Air India flight,
[193.56 → 200.46] which they don't fly through Pakistani airspace because of obvious reasons.
[200.46 → 206.22] But then while I was in India, this tension happened between the U.S. and Iran.
[206.58 → 212.62] And the U.S. put restrictions on planes coming to and fro over Iranian airspace,
[212.74 → 219.00] which is the reroute that Air India does as it kind of goes around Pakistan
[219.00 → 222.52] and then over the Arctic back to Chicago.
[222.84 → 228.82] So finding a route back to where I needed to get turned out to be rather interesting.
[228.82 → 232.58] So I got back a lot later than expected.
[232.96 → 235.70] And yeah, it's I think 2 a.m.
[235.88 → 238.90] About 2 a.m. now in Bangalore.
[239.10 → 243.36] So hopefully bear with me if I start going off on a tangent.
[243.96 → 244.92] Not a problem.
[245.06 → 248.70] We'll wake you up, though, because this is a special episode for us.
[248.74 → 249.70] It's our 50th episode.
[249.82 → 250.44] It is.
[250.70 → 253.58] Congratulations on the 50th episode.
[253.72 → 254.28] Pretty crazy.
[254.28 → 255.64] It does.
[255.78 → 258.08] So it's gone by so fast over the past year.
[258.38 → 262.44] And, you know, just the idea that we've put out that much content
[262.44 → 266.26] and that we actually have people that still want to listen to us after doing that.
[267.16 → 269.00] I'm amazed by that every day.
[269.54 → 270.26] Yeah, definitely.
[270.50 → 272.26] Thank you to all the listeners.
[272.26 → 276.86] It's been great to kind of gradually get more and more connected to the listeners
[276.86 → 281.84] and listeners engaging on our Slack channel on LinkedIn and other places.
[282.18 → 285.82] It's just really great to hear that you're appreciating some of the content,
[285.82 → 290.70] but also great to hear some of your ideas that we've been able to filter into the show.
[290.90 → 292.22] So keep those coming.
[292.38 → 293.92] Thank you so much for listening.
[294.14 → 299.94] We really appreciate all of you and really want to engage with all of you in our community.
[299.94 → 304.02] So make sure and check that out at changelog.com slash community.
[304.56 → 308.36] Yeah, I just got to say when we get messages from people out there
[308.36 → 310.74] or people engaging us in the communities and stuff,
[311.06 → 316.72] it is just enormously exciting because it's kind of the reason that we're doing it.
[316.88 → 319.24] And the fact that people are out there, not only are they listening,
[319.44 → 321.04] but they're saying, hey, what about this?
[321.06 → 322.00] I'd love to hear that.
[322.08 → 323.46] And hey, here's a suggestion.
[323.46 → 326.08] Or hey, I know somebody who would be great on your show.
[326.32 → 329.02] It's just it makes the whole thing wonderful.
[329.02 → 331.88] I know that sounds a little corny, but it's true.
[332.62 → 334.74] Yeah, it is super encouraging.
[335.32 → 336.50] So keep that coming.
[336.62 → 338.86] We're really excited about episode 50.
[339.46 → 341.58] This is kind of a celebration for us.
[341.76 → 344.56] And so we were talking before the show of like how,
[345.30 → 348.46] what should we do to celebrate episode number 50?
[348.86 → 356.42] And what we came up with was kind of to loop all the way back to kind of where things started,
[356.42 → 360.96] you know, with AI and with practical AI.
[361.52 → 367.28] And that's to devote this kind of celebratory episode to one of our favourite things,
[367.28 → 369.56] which is the neural net.
[370.20 → 370.72] Absolutely.
[371.24 → 371.42] Yeah.
[371.50 → 372.60] So we thought we would.
[372.94 → 375.60] So we've talked about a lot of neural nets on the show, obviously,
[375.60 → 381.12] and many advanced sort of architectures and applications and all of that.
[381.52 → 387.64] But we've never actually just talked about the neural net itself, where it came from.
[387.70 → 394.40] And just kind of in brief and from scratch, what a neural net is, what makes it a neural net.
[394.40 → 399.68] And we thought this would be a great episode to kind of circle back to that starting point.
[400.32 → 401.10] Yep, I absolutely.
[401.26 → 406.66] One of the kind of one of the common comments that we get back that I've had conversations
[406.66 → 412.54] with several people about, including the young man that is at the Chinese restaurant two miles
[412.54 → 417.16] from my house, because he actually listens to the podcast, but he's not a data scientist.
[417.16 → 419.44] And he made some comments to me a while back.
[419.44 → 423.34] He said, you know, you guys are perfect as long as you don't do jargon.
[423.42 → 427.62] And we've been, and we took that as a point to not be very careful about that.
[427.70 → 432.02] But he said that, you know, sometimes we get a little bit out there for where he's at.
[432.04 → 433.72] And he's very interested in the topic.
[434.08 → 439.02] But we've never really done a true intro to neural net type of show.
[439.24 → 443.42] And it occurred to me that for those people out there who are trying to jump in and may
[443.42 → 447.56] find it a little bit intimidating, I can't think of a better way to celebrate kind of a
[447.56 → 448.34] milestone episode.
[448.34 → 449.64] Yep, sounds great.
[449.74 → 456.32] So why don't we start with giving just a little bit of history about the neural net itself?
[456.54 → 458.54] So neural nets are not new.
[458.64 → 461.32] They've actually been around for quite some time.
[461.40 → 464.28] Do you know when sort of neural nets came onto the scene, Chris?
[465.24 → 469.72] Sometime around World War II, if I recall correctly.
[470.10 → 470.56] Yeah.
[470.80 → 471.64] Do you have the specifics?
[471.64 → 472.20] Yeah.
[472.32 → 477.88] So if you just you can just search Google for like neural net history.
[478.18 → 484.22] And, you know, there are several lists that come up that have varying, you know, variations
[484.22 → 487.82] of the various dates and facts and all of that.
[487.82 → 496.06] But generally people include kind of a date around the mid 1940s when the first kind of computational
[496.06 → 498.42] model for neural networks came out.
[498.42 → 501.74] There's a guy named I'm sorry if I'm mispronouncing this.
[501.84 → 504.12] I don't really hear this name too much.
[504.22 → 511.02] But Warren McCulloch and Walter Pitts created these computational models.
[511.02 → 518.52] really that paved the way for both sort of modelling biological processes like actually neurons in
[518.52 → 525.68] our brain or neural networks in our brain and then kind of more practical applications
[525.68 → 527.50] of neural networks.
[528.08 → 528.22] Yeah.
[528.38 → 533.74] And then I think there was a kind of the next major step was when the perceptron was invented
[533.74 → 537.42] and that was by a guy named Frank Greenblatt in 1958.
[537.42 → 542.08] So we're getting for me, we're getting a little bit closer to my year of birth.
[542.26 → 543.30] Not quite there yet.
[543.44 → 544.46] Not quite that old.
[545.36 → 551.04] But that really set off kind of, you know, one of the early waves of research in this
[551.04 → 551.30] area.
[551.82 → 556.60] Yeah, people are sometimes surprised because there's a lot been a lot of talk about neural
[556.60 → 560.58] networks recently, but maybe they didn't hear it a while back.
[560.58 → 565.66] So these sorts of things have been around for quite some time in research.
[565.66 → 571.46] And like you were saying, moving up through like the 60s and 70s, they were a topic of
[571.46 → 571.92] research.
[571.92 → 578.86] But I think that a big shift happened in the 1980s, kind of up to the mid 90s.
[579.16 → 583.28] And this is where things like deep learning and back propagation.
[583.28 → 590.20] So this kind of larger neural networks and applications to different types of data
[590.20 → 591.62] came around.
[591.62 → 597.52] So up until this point, people were researching neural networks, but they hadn't really figured
[597.52 → 603.36] out a way to kind of make them bigger and learn more complicated patterns.
[603.36 → 610.52] So before that, they were pretty limited towards like linear divisions between class, you know,
[610.76 → 613.20] linear class boundaries and these different things.
[613.20 → 618.60] But as they saw that they needed to model more complicated relationships, they saw that
[618.60 → 622.16] kind of the size of the networks needed to increase, but they didn't really have a good
[622.16 → 625.24] way of training those sorts of neural networks.
[625.24 → 627.26] And that that kind of changed in the 80s.
[627.76 → 628.14] That's true.
[628.22 → 634.52] And that's there's I have a special affinity for that time period, because in 1992 is actually
[634.52 → 636.84] when I first became aware of neural networks.
[636.84 → 641.04] And that's before like the the the name deep learning was applied to it.
[641.04 → 643.94] And it was before anyone was calling them deep neural networks necessarily.
[644.64 → 648.34] My father worked for Lockheed Martin, just like I do.
[648.62 → 650.30] He would have been shocked that I do at this point.
[650.40 → 652.40] But he worked there.
[652.60 → 656.98] And there was an event that really affected me in a very personal way.
[657.36 → 661.50] And that was that there was a fighter plane called the F-22.
[661.50 → 666.88] At the time, it was the YF-22, which is still kind of the world's top air superiority fighter,
[666.98 → 668.78] in other words, for dogfighting, you might say.
[669.36 → 671.02] And there were two prototypes.
[671.44 → 676.32] And one of those prototypes was doing some testing at Edwards Air Force Base.
[676.36 → 678.66] And they were testing avionics on it.
[678.68 → 679.64] And there was a malfunction.
[680.48 → 682.96] And fortunately, it was close to the ground.
[682.96 → 687.58] And the plane slammed into the ground and went skidding in a fiery ball down the runway
[687.58 → 688.68] for quite a ways.
[688.68 → 692.06] And the pilot got out, the test pilot got out and got away safely.
[692.80 → 698.48] But as the aftermath of that, both of my parents were on the F-22 team,
[698.56 → 701.06] the core team that built the avionics for the plane.
[701.44 → 705.84] And my father was assigned to help solve that avionics thing.
[706.02 → 710.06] And as part of that, he was using neural networks of the day.
[710.18 → 714.62] And he started with feed forward and back propagation, which we'll talk about in a few minutes,
[715.04 → 716.86] and moved on to other architectures.
[716.86 → 720.42] But that was really special because he would come home.
[720.52 → 722.98] And there are all sorts of classified stuff he would not talk about.
[723.34 → 727.00] But in terms of the actual science, we'd come home.
[727.06 → 728.46] And he introduced me to neural networks.
[728.54 → 730.48] And this was our dinner table talk for a while.
[731.06 → 735.76] And as he made progress into different areas, and he would explain it to me at night.
[735.86 → 736.82] And I would ask questions.
[737.70 → 738.74] But, you know, before...
[739.34 → 741.98] So that's going back to when I was a college student at the time.
[741.98 → 747.20] And so it was a fascinating way for me to kind of get into it in a very practical problem.
[747.34 → 751.38] And obviously, the problem was solved, and the F-22 is in service today.
[751.70 → 755.44] And so anyway, but that's how I originally came to be aware of them.
[756.24 → 756.36] Yeah.
[756.50 → 762.18] And that's where you first started getting the ideas for this great podcast, Practical AI, I'm sure.
[762.52 → 765.68] I don't know if podcasting was not a thing.
[765.68 → 774.18] But yeah, this time was really where some interesting things came on the scene.
[774.30 → 785.68] That was recognized actually this year with this year's Turing Award, which went to Lagoon, Hinton, and Begin for things like backpropagation and the sort of ideas around deep learning.
[786.76 → 788.62] And that was big news recently.
[788.62 → 798.64] But there was this kind of time period of the 1980s and kind of up to the mid-1990s where things were getting really exciting.
[798.94 → 803.06] And then there was a sort of die-off of interest in these sorts of methods.
[803.20 → 805.76] Some people call this the AI winter.
[807.34 → 813.12] And that kind of led up almost to the mid-2000s.
[813.12 → 818.68] So this was a time when kind of these methodologies were known.
[819.42 → 826.68] But the problem was that as these networks got larger and larger, of course, they had more parameters that needed to be fitted.
[827.66 → 830.72] And that required more data and more compute.
[830.90 → 835.24] And so there was kind of this lag of the actual data and compute that was needed.
[835.24 → 838.40] And along with that, the adoption that we've seen recently.
[838.40 → 851.30] So that really kicked into gear maybe in the mid-2000s and on where people really had access to a lot of compute, a lot of data, and really were able to plug that into these advanced methods.
[852.14 → 860.72] Yeah, it really got kicked off by a guy who had been in the field for a while kind of coming out of this AI winter by Jeffrey Hinton.
[861.26 → 864.68] And he's kind of one of the legends in this field.
[864.68 → 867.36] And he started research.
[867.48 → 872.58] And at first people as he kind of – and I think he continued through that AI winter.
[872.84 → 885.34] But while everybody else was turning to other things, I would argue that it was really some of his initial – kind of in this latest wave since the mid-2000s that kind of kicked it off.
[885.84 → 893.20] And he is really – I credit him with coming out of the AI winter and kind of being at the moment that we're at now.
[893.20 → 904.92] Yeah, and recently, of course, Google has switched kind of from a mobile-first to AI-first approach to their business in general.
[904.92 → 911.54] And that's kind of sparked a lot of interest from a lot of other industry leaders as well.
[911.72 → 928.86] So pretty much all the big tech companies now, along with a host of startups and smaller companies, have really switched to a focus on AI in terms of research and development and the methodologies that are powering their products.
[928.86 → 938.82] So AI has kind of, at this point, become a new layer in the software stack that's enabling new sorts of functionalities in applications.
[939.60 → 946.26] And, you know, at the core of most all of those AI systems are neural networks.
[946.26 → 951.88] These things that started back in the 40s that were kind of envisioned and built up over time.
[952.06 → 955.38] But the core idea is there.
[955.66 → 957.42] It is the neural network.
[957.58 → 965.24] Now, a lot of people will kind of argue about what AI encompasses and the sorts of methods that are AI and aren't AI.
[965.72 → 969.80] And there are certainly a lot of methods that aren't just kind of simple neural networks.
[969.98 → 972.72] There's non-neural network methodologies.
[972.72 → 975.58] There's a lot of other machine learning type of methodologies.
[975.76 → 991.26] But really, the neural network is kind of the core piece that's powering a bunch of things in industry now and really is the focus of a lot of the AI research that's going on, which is why we're focusing on them.
[991.36 → 992.02] That's true.
[992.02 → 994.80] And that was, I have to say, that was very well said.
[994.80 → 1008.68] Because the reality is when you put different people in this field, data scientists and deep learning engineers, and you ask them what AI is, you're going to get a lot of different answers.
[1009.02 → 1015.40] And I was actually at an event where it almost comically, you know, demonstrated itself in that way.
[1015.40 → 1020.44] It was an Adobe event, which was a live broadcast on Facebook.
[1020.78 → 1024.78] And I was one of 10 people that came and participated.
[1025.00 → 1026.44] And there was a lot of stuff we agreed on.
[1026.50 → 1034.04] But the one thing that all of us had different viewpoints on was exactly what constituted artificial intelligence today.
[1034.04 → 1046.64] And without delving any further, I just found that fascinating that they introduced us as experts, whether we were or not, but that we were positioned in that way.
[1046.80 → 1049.76] And yet none of us could agree on the basic definition of the field.
[1049.76 → 1065.78] The Data Engineering Podcast is a weekly deep dive on modern data management with the engineers and entrepreneurs who are shaping the industry.
[1065.78 → 1074.36] Go behind the scenes on the tools, techniques, and difficulties of data engineering so you can learn and keep up with the knowledge to make you and your business successful.
[1074.36 → 1082.24] Can you give a bit of an outline about the motivation for choosing Jupyter Notebooks in particular as the core interface for your data teams?
[1082.62 → 1086.92] Yeah. And actually, when I first joined Netflix, it was sort of tossed at me.
[1087.10 → 1088.70] And I was definitely like, well, are we crazy?
[1088.92 → 1090.60] And the answer was like, we might be a little crazy.
[1091.10 → 1097.42] Go to dataengineeringpodcast.com to listen, subscribe, and share it with your friends and colleagues.
[1104.36 → 1121.84] Okay. So we've talked about kind of a little bit of the history of neural networks, and we've talked about, you know, how they came onto the scene and really that they're powering a lot of these big tech innovations.
[1121.84 → 1139.34] But before we jump into kind of the very, very specifics of a neural network and what it is, I think it would be useful to kind of just give a real broad definition of supervised learning.
[1139.34 → 1148.04] And there's, you know, a lot of different types of machine learning models out there, some of which are kind of unsupervised and semi-supervised.
[1148.20 → 1156.10] But the bulk of models that people kind of get into when they're first getting into AI and machine learning are supervised learning models.
[1156.52 → 1161.04] And I think that would be a good framework for us to talk about neural networks within.
[1161.04 → 1161.74] Yeah.
[1162.18 → 1172.94] I was just going to say, when I'm talking about neural networks in an introductory thing, I pretty much, I may allude to some other things that are out there, but supervised learning is definitely the place to start.
[1173.58 → 1177.84] It's kind of the basics, and you learn the basics, and then you can build on it in a lot of different directions.
[1178.36 → 1178.56] Yep.
[1179.00 → 1189.32] So lets kind of, when I'm teaching classes, I normally try to introduce some type of kind of model problem that people can have in the back of their minds.
[1189.32 → 1204.62] When I'm thinking about supervised learning, you might think about, like, let's try to model the number of, or let's say, let's try to model our sales for the month based on the number of users on our website or something like that.
[1205.14 → 1215.70] Now, one way you could do that is by creating a sort of function, like a function and code that would take in your number of users and output your sales.
[1215.70 → 1221.94] And most often that would include some type of, like, model definition and some parameters.
[1222.18 → 1229.98] So it's like, you might input a number of users and then multiply that by a parameter or a coefficient, and outcomes your sales.
[1230.44 → 1232.56] So that's a model definition with a parameter.
[1232.56 → 1248.22] Now, the big thing that separates kind of machine learning functions versus kind of regular code functions is that regular code functions, that definition and parameters are kind of set by domain knowledge and someone coding them in.
[1248.22 → 1269.86] Whereas in a machine learning context, I like to think about those parameters being set by kind of trial and error or an iterative process of looking at a bunch of examples and trying to make predictions for all of those examples and then fitting or setting those parameters based on this sort of iterative process.
[1270.26 → 1273.04] Overall, that's kind of how I have the picture in my mind.
[1273.20 → 1274.80] Does that kind of make sense, Chris?
[1274.80 → 1276.96] Or do you have a sort of different view?
[1277.06 → 1279.54] No, I think I would see it the same way.
[1279.54 → 1290.10] I think one easy way to think about it is if you look at solving problems programmatically up until you get to deep learning.
[1290.18 → 1300.18] In other words, just using kind of more traditional programming, you explicitly are going and giving the program commands on what you're going to do.
[1300.18 → 1308.24] And you might think of it in a very simplistic way as lots of if-then type statements, lots of case statements, and you're having to think of all the things.
[1308.40 → 1316.58] Whereas this way of doing it where machine learning, the model is learning what it needs to do, is sort of implicit.
[1316.78 → 1318.20] It's figuring it out for you.
[1318.20 → 1325.74] And it's kind of a different programming paradigm in large in computer science beyond just what deep learning is.
[1325.84 → 1337.66] So if you think of it as the job of training the model is now to go figure out what it needs as opposed to being told what it needs, it kind of puts you in the right frame for learning this.
[1337.66 → 1353.56] I would say some people, when we use the words like the computer figures it out or the computer learns, they kind of have this view of like, oh, I'm going to go put my laptop in the corner of my office and then kind of sprinkle some special fairy dust on it.
[1353.94 → 1358.16] And it's going to kind of spontaneously start learning things about the world.
[1359.58 → 1360.46] Fairy dust?
[1360.76 → 1361.08] Yeah.
[1362.52 → 1366.08] You don't have some of that lying around in your kitchen or something?
[1366.08 → 1368.16] Yeah, I'll borrow it from my seven-year-old daughter.
[1368.52 → 1369.28] Yeah, yeah, maybe.
[1370.06 → 1374.90] So in reality, what there is, is there's always a sort of model definition.
[1375.14 → 1382.74] Remember thinking of our kind of users to sales, there's some definition and there's some number of parameters that parameterize that model definition.
[1383.42 → 1393.28] It might be the, you know, the coefficients, multiplication, or what we call a bias, which is kind of a number that we add on to the definition.
[1393.28 → 1396.50] But there's some model definition in those parameters.
[1396.68 → 1407.56] And what we mean by learning or training isn't just that it kind of, our computer has, it's at the right temperature and the right conditions and year of the month and the stars align, and it starts learning.
[1407.56 → 1419.92] It's that these parameters are set through an iterative process of looking at a bunch of training examples of what input is and should be and what output should be.
[1420.02 → 1424.32] So there are a bunch of examples of there's this input and this should be the output.
[1424.46 → 1426.30] There's this input and this should be the output.
[1426.30 → 1444.94] And there's a training process, which is just another function written in code that iteratively looks over all of these examples and fits these parameters such that the model can then make predictions on new examples that it hasn't seen yet.
[1445.02 → 1448.58] So it isn't that there's kind of the spontaneous learning that happens.
[1448.76 → 1451.52] It's really kind of something much more benign.
[1451.52 → 1456.98] It's that there are a bunch of examples and computers are good at repetitive tasks, right?
[1457.36 → 1467.54] And so we just have the computer look at these examples over and over again and tweak these parameters until we get a good set of parameters to parameterize this model definition.
[1467.86 → 1470.66] And then we can make a new prediction.
[1470.84 → 1473.54] So that first process is called the training process.
[1473.54 → 1478.72] And then when we make new predictions, that's called the inference or prediction process.
[1479.40 → 1485.58] So in the training process, we've talked about making the little tweaks and that's called error correction.
[1485.86 → 1494.36] And so as Daniel was talking about, we already when we're in training, we already know what the ground truth is for any given example.
[1494.36 → 1501.44] And the model is essentially trying to find that with where it's trained to up to that point.
[1501.88 → 1507.50] And then it actually, it says, okay, I have a result in this training cycle.
[1507.50 → 1511.54] And then I have the ground truth.
[1511.62 → 1512.98] And there's a difference in the two.
[1513.10 → 1517.48] And I'm going to use an error correction algorithm to say, what should I do?
[1517.48 → 1524.26] What tweaking should I do in this case when my result isn't what I know to be the ground truth in the training set?
[1524.64 → 1528.88] So it is an algorithm that is driving that tweaking.
[1529.36 → 1535.34] But it is able to use that algorithm based on the data that it's come upon on that particular cycle.
[1535.88 → 1540.12] So let's maybe make this a little bit more concrete now.
[1540.20 → 1546.32] So we've talked about, you know, supervised learning in general and that there's this definition and parameters that are set.
[1546.32 → 1549.28] So what does that look like for a neural network?
[1549.80 → 1554.04] So in a neural network, there's this kind of subunits.
[1554.18 → 1555.78] I have an overall definition.
[1555.78 → 1559.76] And then I have a bunch of kinds of sub definitions within that.
[1559.76 → 1565.58] Or you could think about it if you're a programmer, like a function that calls a bunch of kinds of sub functions underneath it.
[1565.68 → 1569.24] And these subunits or sub definitions are called neurons.
[1569.24 → 1577.82] And so each of these neurons kind of have its own inputs and outputs with its own definition and its own set of parameters.
[1577.82 → 1583.64] And these parameters for the neuron are often called weights and biases.
[1583.64 → 1594.64] So again, you can kind of think of my overall definition of my model containing a bunch of these sub definitions of neurons that are linked together in some way.
[1594.72 → 1601.36] And that together, that assembly of neurons make up what's called a neural network architecture.
[1601.36 → 1605.82] So that just that architecture just means there's a bunch of this kind of subunits.
[1605.82 → 1612.04] Each of them have a definition and some parameters that that can be set.
[1612.04 → 1617.86] Now, now there are a lot of different ways that you can set up those neurons.
[1617.86 → 1623.00] So, so maybe we should look at, you know, a kind of common way to set up fully neurons.
[1623.34 → 1626.04] Yeah, like a fully connected feed forward is a good starting point.
[1626.38 → 1629.36] Yep. So maybe do you want to do you want to start there, Chris?
[1629.82 → 1633.46] Sure. So Daniel is just talking about these units of neurons.
[1633.46 → 1641.86] And if you're is you want to paint a picture in your mind as you listen, you could think of each one of those the way they're usually depicted graphically is as a little circle.
[1641.86 → 1646.76] And you could think of it as a little circle that has some stuff inside it, which we'll talk about in a moment.
[1647.08 → 1652.32] But you take each of those circles, and you like you line a few circles up into a row.
[1652.32 → 1655.40] And you and so you have a row of circles.
[1655.58 → 1660.70] And then at that point, you line up a second row and maybe a third row.
[1660.80 → 1664.52] And so there's some number of rows in number of rows that you have there.
[1664.76 → 1667.70] And there are some special relationships between each of those layers.
[1667.70 → 1677.78] So if you take for every neuron in that first layer, it is connected to each of the neurons in the second layer, but to none of the neurons in its own layer.
[1678.32 → 1681.50] And so in that second layer, you recreate that.
[1681.58 → 1690.96] And so each neuron in a given layer is connected to all the neurons in the previous layer and all the neurons in the next layer, but none of the neurons in its own layer.
[1690.96 → 1698.32] And so you can kind of envision this mesh of rows of little circles in that way.
[1698.40 → 1701.02] And you start from one side to go in as an input.
[1701.18 → 1702.72] And then you come out the other side.
[1702.72 → 1709.32] And that that is the basic image in your mind of how you might think about a fully connected feed forward network.
[1709.32 → 1715.82] And I'll note one of the thing is these shows where Daniel and I talk about topics on our own without a guest.
[1715.96 → 1718.32] You may have noticed that they're called fully connected episodes.
[1718.32 → 1719.70] This is what we're referring to.
[1719.76 → 1720.58] It was named after this.
[1721.04 → 1721.44] How clever.
[1721.90 → 1722.20] Mm hmm.
[1722.42 → 1731.38] You mentioned that each of these nodes or neurons is fully connected in this sort of is in this sort of network.
[1731.38 → 1734.44] And each one has its own inputs and outputs.
[1734.76 → 1740.88] Now, if we dig into one of these neurons to think about kind of what's inside that bubble.
[1740.88 → 1745.42] And again, you know, you can think about that visually like a bubble or a node.
[1745.42 → 1752.00] Or if you're kind of a programmer, you might think about it as one of these kind of sub functions under a big function.
[1752.42 → 1754.94] But it has its own inputs and outputs.
[1754.94 → 1759.26] And if we think about it maybe as just having a couple inputs, let's say X one and two.
[1759.44 → 1763.34] Now, what happens inside that circle or inside that neuron?
[1763.86 → 1767.86] Well, there's some kind of simple things that happen often.
[1767.86 → 1774.38] So one way we could think about processing these inputs in the neuron is to just add them up.
[1774.38 → 1774.80] Right.
[1774.80 → 1783.82] And so in a kind of linear regression sort of way, we could multiply each of my inputs X one and X two by a couple coefficients.
[1784.36 → 1786.34] Let's say W one and W two.
[1786.56 → 1787.70] Those are often called weights.
[1787.70 → 1791.70] So I just add up the two things after I multiply them by coefficients.
[1792.02 → 1796.50] And then I might add in like a intercept or a constant.
[1797.50 → 1801.14] And, you know, so just X one, X two plus something.
[1801.28 → 1802.82] And that's often called a bias.
[1802.82 → 1810.40] So in this case, I would have like three parameters that I am parametrized the way I'm combining these inputs.
[1810.40 → 1815.42] And so each of my X one and X two come in, I combine them together in this way.
[1815.52 → 1821.82] And that's all good and fine, except, you know, most relationships in our world aren't linear.
[1822.68 → 1827.62] So it might be good to introduce some non-linearity into this combination.
[1827.62 → 1838.52] And that's where a thing called an activation function comes in, which is just a non-linear function that's kind of applied to this combination of inputs to give it some non-linearity.
[1838.52 → 1849.74] And common functions that are used are like sigmoid or Rely or other functions, hyperbolic tangent that are applied to this combination of inputs.
[1849.94 → 1857.92] So when my inputs come into that node or that circle, they're just kind of added up in a special way and then output out the other end.
[1858.28 → 1867.54] And all of my neurons in my network kind of do similar sorts of simple operations that are parametrized similarly.
[1867.54 → 1870.48] So each neuron has a certain number of inputs.
[1870.60 → 1875.24] They're combined using some parameters and then output is a number.
[1875.42 → 1878.28] And that's kind of what each neuron does.
[1878.42 → 1880.36] That was a very good explanation there.
[1880.92 → 1888.36] And so as you as these inputs start flowing through these layers, and they're doing this concurrently.
[1888.36 → 1890.10] So the inputs come in.
[1890.10 → 1892.98] It hits all the neurons in that first layer.
[1893.88 → 1898.42] Simultaneously, everything that Daniel was just talking about happens in each of those neurons in that first layer.
[1899.00 → 1911.32] And as they go through their transfer function that adds the non-linearity, and then they go out and the output of each one of those neurons in that first layer goes to all the neurons in the second layer.
[1911.32 → 1919.08] And as combined, remember, since they're fully connected, there are lots of inputs potentially coming in, and they're all summed up again in each neuron just the way Daniel described.
[1919.68 → 1927.44] And so this happens concurrently in concurrency at each layer, and it goes through layer by layer till you get to an output.
[1927.44 → 1940.64] And then you either you discover at that point that if you're while you're going through this training process that you have some values coming out, and you compare that against what you know to be the ground truth that's in your training data set.
[1940.74 → 1943.16] You know what the result is while you're trying to train.
[1943.16 → 1951.96] And that's when your error correction comes in where you have to say, OK, well, I've ended up with an output, and it's not quite what I was hoping it would be.
[1951.96 → 1953.50] So I need to change.
[1953.62 → 1958.46] I need to change the values throughout the architecture.
[1959.02 → 1965.38] There's the initial thing that most people learn and is most widely used is called back propagation.
[1965.38 → 1973.40] And that's where you work your way back through the layers, through a set of algorithms that make little tweaks all the way through your layers.
[1973.60 → 1974.76] And then, hey, guess what?
[1974.82 → 1979.40] You've done one full cycle, and it's time to go to the next row of your data to train that.
[1979.46 → 1982.12] And you do that whole process over and over again.
[1982.32 → 1982.80] Yep.
[1982.92 → 1990.50] It's its kind of like you might think about if you're trying to set these weights and biases manually as a human.
[1990.50 → 2003.34] And then what we would do is just kind of try to make, you know, make an initial choice for them, try to make some predictions and then see if our predictions were good or bad and kind of adjust the parameters accordingly and then just do that over and over.
[2003.34 → 2006.88] So that's what the computer is doing is essentially a bunch of trial and error.
[2007.08 → 2008.42] It's making some predictions.
[2008.42 → 2017.90] And of course, there's more sophisticated ways of updating the weights and biases rather than just kind of randomly making choices for updates.
[2017.90 → 2021.02] And that's where kind of this gradient descent comes in.
[2021.16 → 2023.52] But essentially, we're just making those corrections.
[2023.92 → 2035.70] Now, I think a kind of interesting thing to add in here is we're always talking about models and like what, you know, we have a neural network model.
[2035.82 → 2036.98] We have this type of model.
[2037.10 → 2040.82] So here we've talked about the kind of definition of the neural network.
[2040.94 → 2045.34] We've talked about all the parameters that need to be fit for this neural network.
[2045.34 → 2050.04] We've talked about the training process that trains or fits all of these parameters.
[2050.24 → 2056.58] And then we've talked about the inference or prediction phase in which we use all of that to make predictions.
[2057.54 → 2062.08] So I'm kind of curious in your mind, Chris, what do you consider the model?
[2062.32 → 2064.90] Like what is the model in your mind amongst all of that?
[2064.90 → 2075.96] So the way I would think of a model is I think of it when you start out with these layers of neurons lined up, and we're talking about the simplest use case, obviously.
[2076.22 → 2083.84] And there are you can add a lot of different complexity to this over time to achieve different architectures.
[2083.84 → 2085.48] And there are many, many architectures out there.
[2085.48 → 2090.36] When someone talks about a model, though, I typically think of a trained architecture.
[2090.36 → 2098.26] If you think of a fully connected feed forward architecture as being something you're training when it gets done, it has a purpose.
[2098.26 → 2105.80] It's trying to create its purpose is to make inferences about a particular set of inputs to give you an output.
[2106.26 → 2108.00] And that's what I would call a trained model.
[2108.12 → 2111.94] It's the architecture at work that is deployable.
[2111.94 → 2120.08] One thing that we did mention briefly is that is when you're training a model, how do you know when you've gotten there?
[2120.36 → 2138.06] And I just wanted to note that it's its it's arbitrary based on your use case in that we've been talking about the fact that when you get to each the end of each cycle in training, you have some sort of delta between what you have and what you know to be the truth.
[2138.38 → 2140.72] And so that is an error that you have there.
[2140.72 → 2143.78] There's an it's an it's an it's a degree of error.
[2143.78 → 2147.94] And you have to decide for your use case, how much error can you tolerate?
[2148.44 → 2153.16] If you can tolerate more error because it's not a very critical need.
[2153.16 → 2157.06] And, you know, if it happened to be wrong, it might not it might not be a terrible thing.
[2157.10 → 2163.96] Then you can probably achieve training quicker and deploy because it's not if it's a life and death thing, and it has to be extremely accurate.
[2163.96 → 2167.74] Then you need a very small error in your final product.
[2167.74 → 2171.06] And therefore, you may take quite a bit more training to achieve that.
[2171.06 → 2178.58] And I just wanted to note that's how you know when your training is over is that you achieved an acceptable level of error for your use case.
[2178.58 → 2184.76] Chris, you were just talking about kind of the acceptable level of error with a neural network.
[2184.76 → 2196.50] And I think something that, you know, needs to be understood here is that these nodes or these neurons can be assembled in all sorts of from simple to very complicated ways.
[2196.50 → 2203.72] And you could have sort of layer after layer of these that might be fully connected, might not be fully connected.
[2204.50 → 2216.92] But as soon as you start adding these things up or putting them, assembling them in all sorts of complicated ways, which is really what's done in deep learning, then you start accumulating a ton of parameters.
[2216.92 → 2229.10] So in some of these, you know, in some of these recent models, let's say like transformer models that have come out for language, there are millions, in fact, hundreds of millions of parameters that need to be set.
[2229.62 → 2242.08] And so when you're thinking about the compute and the data that's needed to actually train these models or fit all of those parameters, now you can kind of understand why a lot of data and a lot of compute is needed.
[2242.08 → 2260.14] Because you can't have like 300 million parameters, and then like 2000 training examples and call it good and say that's going to set all of your parameters, you have to have a significant amount of data for you to be able to kind of learn the complicated patterns and fit all these parameters.
[2260.14 → 2265.06] So a ton of compute and a ton of data is needed.
[2265.66 → 2266.06] Absolutely.
[2266.06 → 2279.82] I think calling out the scale that you're talking about there is important because it is a distinguishing factor between this particular tool in data science and other tools that we've all worked with previously.
[2280.64 → 2284.44] I think it's, you know, and people say, well, okay, I understand that.
[2285.00 → 2291.76] And shortly upon coming into the field, you learn that there is special hardware used for the computation.
[2292.28 → 2294.82] And people have often asked me, why is that?
[2294.82 → 2296.54] I've heard GPU and stuff like that.
[2296.54 → 2306.44] And that is the fact that to do these computations, which are actually, they're not complex, but it is a field of linear algebra.
[2306.72 → 2307.78] It's called matrix multiplication.
[2308.64 → 2320.82] And as Daniel just pointed out when he was talking about the scale of the parameters, and you might have very large architectures with many, many neurons that are all concurrently doing these mathematical operations.
[2320.82 → 2332.82] It lends to efficiency to have hardware that is able to do this type of computation much faster than the hardware that came before.
[2333.00 → 2341.54] And that's why you hear about GPUs and TPUs versus something that we may have all grown up with, which was the CPU, you know, driving our laptop and stuff.
[2341.54 → 2349.04] And that is that this hardware enables the mathematical operations that have to happen at such scale.
[2349.94 → 2360.08] And the fact that you have that relationship there really distinguishes this particular data science toolbox from others.
[2360.08 → 2362.96] And makes it expensive in some cases.
[2363.14 → 2363.48] Oh, boy.
[2364.80 → 2365.48] Yeah.
[2365.64 → 2369.78] So we've talked about the neural or neurons.
[2369.78 → 2373.78] We've talked about architectures or combinations of these neurons.
[2373.78 → 2378.32] We've talked about what it takes to fit all of these parameters of the neurons.
[2378.32 → 2387.34] But we haven't actually got to maybe what's the most important point, which is why do neural networks work?
[2387.76 → 2401.44] So if you think about kind of what we've done, it's somewhat arbitrary in some ways in the sense that we've just put a bunch of functions all together in a row that combine things over and over.
[2401.44 → 2405.68] That's kind of simplifying things, but it's really what we're doing.
[2405.92 → 2413.84] There are inputs and those are fed through a bunch of things that combine them over and over and then output something that combines that output over and over.
[2414.94 → 2418.40] And, you know, why does that sort of thing work?
[2418.88 → 2424.22] And the way I kind of like to think about it, I'm curious about, you know, how you think about it.
[2424.30 → 2426.74] And I know there are more formalisms we can put around it.
[2426.74 → 2440.70] But the way I like to think about it is, you know, if I have a relationship, let's say, between some input and output, and I'm thinking of like, again, the users and sales example, that might be a fairly, you know, simple relationship.
[2440.70 → 2446.18] It might just be a proportional one that I can that I can model via one or two parameters.
[2446.44 → 2450.46] And I just put that in and, you know, there's a simple relationship there.
[2450.46 → 2463.64] But there's a lot more complicated relationships in our world, like, you know, if I'm trying to detect a face in an image, there are a lot of important things there from colour to edges to certain features of the face.
[2464.06 → 2473.66] And it's really hard for me to write down a definition using my own domain knowledge that kind of is the definition of a model of a face.
[2473.66 → 2503.64] And so the way I think about neural networks is kind of just saying, well, okay, I'm not even going to try to write down this sort of domain knowledge definition, what I'm going to do is make my model definition as complicated as it needs to be such that whatever the relationships are between my input and output, whatever those happen to be, I'm able to account for those complexities, because my model is parameterized in such a complex way.
[2503.66 → 2514.40] And so this takes some of some of the burden off of the programmer, the domain expert, and really puts it on the computer in terms of computation and data.
[2515.32 → 2520.56] Because I all the assumption I'm making is that there is a relationship between my input and output.
[2521.04 → 2529.04] And if my definition is complicated enough, I'm going to be able to parameterize it to model that, that that is actually a great explanation.
[2529.04 → 2530.52] I really like how you said that.
[2530.52 → 2537.22] And it's, I think it differentiates from a number of other approaches one might take.
[2537.32 → 2548.50] And so, you know, when we are using neural networks to solve really complex problems, we'll try it, there's a balancing act that we're trying to do.
[2548.50 → 2554.92] So the bigger the architecture, the more computation you're introducing into it by default.
[2554.92 → 2557.26] But you need it.
[2557.26 → 2566.32] And you can actually have there's actually mathematically the ability you could have a feed forward network with a single hidden layer.
[2566.44 → 2572.60] And since we haven't specifically mentioned the word hidden, think about this neural network architecture that we talked about.
[2572.66 → 2574.38] And you had that input layer of neurons.
[2574.38 → 2579.10] And then the second layer only takes the output from the first layer.
[2579.22 → 2582.96] And then it passes its output to a third layer, which is your output.
[2583.08 → 2586.56] So you have a hidden, I'm sorry, an input, a hidden, and an output.
[2586.80 → 2591.66] And there is a mathematical equation called the universal approximation theorem.
[2591.90 → 2593.44] So you can go look it up on Wikipedia.
[2593.44 → 2603.28] And it notes that a feed forward network with a single hidden layer containing a finite number of neurons can approximate continuous functions.
[2603.54 → 2607.60] And that sounds like, you know, not a very impressive statement to make.
[2607.64 → 2614.08] But I think it's pretty amazing in that there's, it's saying you can approximate all sorts of different functions out there.
[2614.42 → 2617.92] And I think that's really important because it lends itself to why this is so powerful.
[2617.92 → 2622.78] And going back to what you said a moment ago, Daniel, you mentioned the fact that we'll add complexity.
[2622.78 → 2628.40] Because if you have a really complex function, that one hidden layer might eventually get there.
[2628.48 → 2635.86] But it may be unreasonable in terms of its, the time it takes to train it to get there, to get within what is an allowable error for you.
[2636.18 → 2642.22] And so the way we get around that is we either add more neurons or we add more layers to it.
[2642.30 → 2645.94] And we, so we deliberately add complexity before we know what the solution is.
[2645.94 → 2654.46] And in doing that, it gives, it gives the this matrix multiplication a lot more options on finding all those little things.
[2654.58 → 2660.08] The, you know, here's a line and here's how, here's a line with another line that creates a shape.
[2660.08 → 2664.62] And, you know, and lo and behold, it turns into a part of the face or something eventually.
[2664.84 → 2670.88] And so by having these layers, that complexity allows you to pick apart pieces of it and do it.
[2670.88 → 2679.04] And so you're balancing how big of a neural, how big of a network do I want for computational expense versus what does my problem require?
[2679.04 → 2684.04] And so it's, it's, when you get into this field, you learn that you have to balance that.
[2684.14 → 2689.12] And then you, and then obviously have various architectures that lend themselves to solving particular problems.
[2689.12 → 2709.26] Speaking of getting into this field, I think maybe, you know, with the few minutes that we have left here, Chris, it might be good to just talk about, you know, if you're getting into this field or if you really, like you've done some tutorials with neural networks, but you don't kind of have this fundamental understanding of how they operate.
[2709.26 → 2714.44] How can you get some of that intuition about how neural networks operate?
[2714.76 → 2725.70] I know one of the things that I did in the past that was really, really helpful for me was implementing kind of a simple feed forward neural network from scratch.
[2725.70 → 2740.22] And I did that just for the iris classification problem, which is kind of a very well-defined classic problem in machine learning where you're trying to classify types of iris flowers based on the measurements of their petals.
[2740.96 → 2748.60] And I did this in, in the go language because I was also interested in, in that and using that.
[2748.60 → 2764.10] But I think whatever language you use, it doesn't really matter, but just kind of introducing each of these components, like the neuron, the activation function, this loop of training is really, really useful to gain a fundamental understanding.
[2764.28 → 2773.02] And one, one way, if that's kind of intimidating to you, I might recommend the great book from Joel Grus's called Data Science from Scratch.
[2773.02 → 2782.48] He just released a second edition of that book, and he added in a bunch of things about neural networks, deep learning, recurrent neural networks.
[2782.60 → 2789.38] But in that book, he kind of walks you through some implementations of neural networks from scratch using Python.
[2790.04 → 2802.46] And so I think that's a it's a really great way to gain this fundamental intuition and something that I think would be even good for, for me to do occasionally in different languages
[2802.46 → 2805.78] or in different ways to kind of help me keep that, that intuition.
[2806.66 → 2810.62] Yeah, not only that, there are so many, there are so many approaches.
[2810.76 → 2814.50] I really think it's such a great time to get into this field right now.
[2814.96 → 2820.88] It's, it's, it has, I won't call it mature, but it has matured a lot in the last few years.
[2821.02 → 2825.60] And back when you and I were first looking at it, incidentally, that's, that's what I did as well.
[2825.60 → 2836.06] In, in, in same programming language, I, I created a toy neural network in Go just to make sure that I understood where, where I wanted to start from.
[2836.06 → 2838.38] And, you know, all the pieces made sense to me.
[2838.70 → 2842.10] It was, it was more of a, a science, you know, experiment kind of thing.
[2842.68 → 2846.00] And, and before moving into frameworks, which is where the real action is.
[2846.06 → 2847.76] But there's a lot of learning.
[2847.88 → 2850.36] So if you're into books, there are all sorts of different books.
[2850.36 → 2858.40] Um, there's the, uh, there's the deep learning textbook, uh, which is, uh, which was written by several of the, the luminaries in the field.
[2858.90 → 2862.52] Uh, you, you have to love your math if you want to jump into that one.
[2862.58 → 2866.76] If you're very comfortable with your linear algebra and your calculus, then that's a great place to go.
[2866.86 → 2869.76] If you're not so, then it's a good reference to try to work toward.
[2869.88 → 2875.40] But you might want to find some, some books that, uh, cater toward whatever your knowledge level is.
[2875.40 → 2880.20] And also there, there's a bunch of, of really fantastic courses online.
[2880.36 → 2884.74] Coursera has them, Microsoft, Google, um, there's a bunch out there.
[2884.74 → 2898.16] And so whatever your approach to learning is, however you consume, uh, new information best, uh, I can almost guarantee there's, there's a high value way of doing that, uh, that, that you can cater it around yourself.
[2898.16 → 2902.16] I know that didn't really exist when we were, uh, doing ours originally.
[2902.48 → 2905.58] Um, but the last two, three years, it's just exploded.
[2905.70 → 2906.18] Yeah.
[2906.26 → 2908.10] There's, there's great online resources.
[2908.46 → 2912.44] Um, I really liked the machine learning crash course, uh, from Google.
[2912.62 → 2912.98] Yeah.
[2913.00 → 2917.30] There's of course the fast.ai material that's all online that people love.
[2917.32 → 2919.66] So it's a great time to get into the field.
[2919.66 → 2934.28] And, um, this is, you know, hopefully this has given you a sense of what neural networks are or given you a refresher in that, um, to really encourage you that like we, we can, you know, get some intuition about what's going on under the hood here.
[2934.28 → 2936.32] And, and that's not too far away from you.
[2936.40 → 2937.08] It's within reach.
[2937.20 → 2945.38] So if you have a passion about this stuff, you know, get involved, dive into some resources, let us know if you need help, uh, finding those resources.
[2945.38 → 2953.20] Um, and yeah, I'm, I'm just, uh, excited about the next 50 episodes that we get to dive into more about AI, Chris.
[2953.52 → 2954.06] I am too.
[2954.12 → 2958.66] I hope, I hope, uh, people listening out there will join us in the various communities.
[2958.66 → 2961.88] We're on Slack, we're on LinkedIn, we're on Twitter.
[2962.28 → 2964.88] Uh, and, and we really do have a lot of great conversations.
[2965.10 → 2968.48] And as we look toward the next 50 episodes, we really want your input.
[2968.48 → 2969.84] What do you want to hear about?
[2970.16 → 2971.56] Who do you want to hear from?
[2971.74 → 2973.66] What topics are of interest to you?
[2973.66 → 2978.04] Um, and, and we really want to build the next 50 episodes around you.
[2978.32 → 2978.72] Yep.
[2978.84 → 2980.68] And, uh, congrats again, Chris.
[2980.94 → 2987.74] Uh, great, great, uh, to be doing this with you and, uh, looking forward to, to the future episodes.
[2987.74 → 2988.70] We'll see you next week.
[2989.02 → 2989.72] See you next week.
[2989.76 → 2990.16] Thank you.
[2992.42 → 2992.98] All right.
[2993.00 → 2995.64] Thank you for tuning into this episode of Practical AI.
[2995.64 → 3001.00] If you enjoyed this show, do us a favour, go on iTunes, give us a rating, go in your podcast app and favourite it.
[3001.00 → 3005.56] If you are on Twitter or social network, share a link with a friend, whatever you got to do, share the show with a friend.
[3005.56 → 3010.78] If you enjoyed it and bandwidth for change log is provided by fast learn more at fastly.com.
[3010.78 → 3014.22] And we catch our errors before our users do here at change log because of roll bar.
[3014.48 → 3016.80] Check them out at robot.com slash change log.
[3016.80 → 3021.56] And we're hosted on Linde cloud servers and a leno.com slash change log.
[3021.66 → 3022.12] Check them out.
[3022.18 → 3023.04] Support this show.
[3023.18 → 3026.64] This episode is hosted by Daniel Whiten ack and Chris Benson.
[3026.86 → 3032.92] The music is by break master cylinder, and you can find more shows just like this at change law.com.
[3032.92 → 3041.42] When you go there, pop in your email address, get our weekly email, keeping you up to date with the news and podcasts for developers in your inbox every single week.
[3041.58 → 3042.58] Thanks for tuning in.
[3042.74 → 3043.50] We'll see you next week.
[3046.80 → 3047.80] Bye.
[3047.80 → 3048.80] Bye.
