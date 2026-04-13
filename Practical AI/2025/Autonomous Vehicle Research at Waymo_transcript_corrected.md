[0.00 → 8.74] Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 → 13.64] of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 → 19.14] Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 → 23.54] Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 → 25.12] buzz, you're in the right place.
[25.12 → 29.84] Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 → 33.02] drops, behind-the-scenes content, and AI insights.
[33.36 → 35.88] You can learn more at practicalai.fm.
[36.20 → 37.50] Now, on to the show.
[39.76 → 44.38] Well, friends, when you're building and shipping AI products at scale, there's one constant.
[45.00 → 45.48] Complexity.
[45.90 → 50.64] Yes, you're wrangling models, data pipelines, deployment infrastructure, and then someone
[50.64 → 53.12] says, let's turn this into a business.
[53.62 → 54.88] Cue the chaos.
[55.08 → 59.70] That's where Shopify steps in, whether you're spinning up a storefront for your AI-powered
[59.70 → 62.82] app or launching a brand around the tools you've built.
[63.20 → 68.56] Shopify is the commerce platform trusted by millions of businesses and 10% of all U.S.
[68.66 → 73.56] e-commerce, from names like Mattel, Gymshark, to founders just like you.
[74.12 → 79.76] With literally hundreds of ready-to-use templates, powerful built-in marketing tools, and AI that
[79.76 → 84.34] writes product descriptions for you, headlines, even polishes your product photography.
[84.34 → 88.38] Shopify doesn't just get you selling, it makes you look good doing it.
[88.78 → 89.50] And we love it.
[89.72 → 90.90] We use it here at Changelog.
[91.12 → 93.52] Check us out, merch.changelog.com.
[93.72 → 95.02] That's our storefront.
[95.42 → 97.34] And it handles the heavy lifting, too.
[97.68 → 101.84] Payments, inventory, returns, shipping, even global logistics.
[102.50 → 106.40] It's like having an ops team built into your stack to help you sell.
[106.40 → 109.56] So, if you're ready to sell, you are ready for Shopify.
[110.20 → 116.86] Sign up now for your $1 per month trial and start selling today at Shopify.com slash practical
[116.86 → 117.28] AI.
[117.98 → 122.50] Again, that is Shopify.com slash practical AI.
[136.40 → 140.32] Welcome to another episode of the Practical AI Podcast.
[140.72 → 142.12] This is Daniel Whiten ack.
[142.22 → 148.32] I am CEO at Prediction Guard, and I'm joined, as always, by my co-host, Chris Benson, who is
[148.32 → 151.26] a principal AI research engineer at Lockheed Martin.
[151.48 → 152.20] How are you doing, Chris?
[152.62 → 154.28] Doing great today, Daniel.
[154.82 → 159.16] Lots of, as always, lots of AI and autonomy to talk about.
[159.26 → 159.80] And you know what?
[160.20 → 162.18] We have Waymo to talk about as well.
[162.32 → 164.02] We have Waymo to talk about.
[164.02 → 164.34] Yeah.
[164.34 → 171.66] Speaking of Waymo, we're very excited to welcome back Drag Angelo, who is the vice president
[171.66 → 175.00] and head of the AI Foundations team at Waymo.
[175.18 → 175.78] Welcome, Drag.
[176.32 → 177.00] Thank you, guys.
[177.06 → 180.00] It's great to be back after five years or so, right?
[180.24 → 181.28] After five years.
[181.38 → 188.00] Yeah, we were commenting before we started the recording that the last episode with Drag
[188.00 → 191.28] was on September 1st of 2020.
[191.74 → 193.96] So, that was episode 103.
[194.34 → 201.58] So, a few things have changed in the world generally, but certainly in relation to AI.
[202.24 → 209.56] I'm wondering if you could maybe just catch us up at a high level, Drag, in terms of driverless
[209.56 → 211.76] cars, autonomous vehicles.
[212.16 → 215.94] Like, how do you see the world differently now than you did in 2020?
[215.94 → 225.62] So, one thing I would say is in October 2020, we opened our Waymo 1 service in Phoenix East
[225.62 → 226.98] Valley to everybody.
[227.34 → 229.74] So, you know, just one month after we talked.
[229.74 → 238.98] But since then, we have launched and scaled quite dramatically in now five major metros.
[239.66 → 246.32] And this is San Francisco, Los Angeles, Phoenix, Atlanta, and Austin.
[246.32 → 254.22] And we are also serving hundreds of thousands of rides a week to paying customers.
[254.96 → 256.40] We are expanding.
[256.80 → 263.14] We announced expansion to at least half a dozen or no more cities that will be going on through
[263.14 → 263.92] next year.
[264.38 → 265.94] And we may announce yet more.
[265.94 → 274.28] In the cities we were at, we continue reporting the safety performance of our autonomous driver.
[275.08 → 281.16] And we are over 100 million autonomous miles driven on the road at this point.
[281.26 → 283.08] So, it's fairly statistically significant.
[283.08 → 292.04] And in those miles, our safety study at close to 100 million miles showed that we are five
[292.04 → 299.12] times less likely to get into accidents with critical injuries and over 10 times, I think
[299.12 → 305.34] 12 potentially, less likely to get into collisions or injured pedestrians.
[306.28 → 308.46] So, that has been happening.
[309.32 → 312.22] And we are on to doing more and more right now.
[312.22 → 314.56] I think we work on improving the driver further.
[315.28 → 320.28] We have a sixth generation vehicle coming up.
[321.14 → 324.82] We have started partnering with different companies.
[325.06 → 329.38] For example, we're partnering with Uber in Austin, Atlanta.
[329.60 → 334.30] So, our vehicles show up on their app in those cities.
[334.76 → 338.52] We have partnered actually with Lyft in Nashville, if I believe.
[338.52 → 341.84] And we partnered with DoorDash to explore delivery.
[342.36 → 347.84] So, we're exploring and expanding the scope and the partnerships that we are doing as well.
[348.40 → 357.36] But I think in 25, I would say a lot more people have had and continue having the opportunity
[357.36 → 358.38] to try Waymo.
[358.38 → 361.14] I'm quite a convert myself.
[361.44 → 371.92] To me, probably the aha moment, the big aha moment was in 22 when I got riding in San Francisco by myself fully autonomously.
[372.54 → 375.70] And so, since then, it took some time for more people to get exposed.
[375.70 → 378.58] But now, I think the phenomenon is out there.
[378.66 → 383.62] And I think also, the autonomous vehicle industry went through cycles.
[384.12 → 391.26] There was certainly around 22, 23 time of pessimism in autonomous vehicles.
[391.26 → 398.24] But I think through our success, through generative AI, and I think there are other companies now.
[398.36 → 400.00] It's, again, a very lively space.
[400.66 → 405.64] There are others that are also trying to push what's possible with autonomous driving and robotics.
[405.96 → 408.16] So, it's, again, very, very happening place.
[408.90 → 411.14] And, yeah, we are contributing probably.
[411.60 → 417.98] I would like to think the most advanced version of an embodied physical AI today that you can do without.
[418.56 → 419.36] That's fantastic.
[419.36 → 424.34] I got to say, as a native Atlanta, I'm so happy that you guys are in my city.
[424.86 → 428.30] And we're a very, very car-centric city as well.
[428.48 → 431.52] You know, you really have to have a vehicle to get around.
[432.12 → 438.16] And I noticed, you know, as you were naming the cities that you guys are in, that tended to be the case in terms of variate.
[438.48 → 446.40] Does that play into any of the way that you guys think about testing in terms of being, you know, like Atlanta traffic for its size is notoriously bad.
[446.40 → 460.10] And I would love to see ever more Waymo and other autonomous vehicles here because I am terrified of all the surrounding drivers with our daily collage of traffic accidents and stuff like that.
[460.10 → 464.62] So, I keep telling everyone, just wait, autonomous vehicles are coming.
[464.72 → 470.92] I'm kind of curious how you pick these different testing cities that you guys engage in.
[471.08 → 478.46] And what are some of the things that you're testing for that maybe those locations are particularly apt for helping out on?
[478.46 → 482.52] So, I mean, it's a bit of a combination of both technical and business reasons.
[482.72 → 489.50] I think we are trying to do large metros where, you know, autonomous vehicles can be a big market and help a lot of people.
[489.66 → 490.32] So, that's one.
[490.88 → 496.00] And also, we've intentionally been growing our ODD, so to speak, operational design domain.
[496.62 → 500.94] Our first service, Waymo One in Phoenix East Valley, Chandler.
[500.94 → 507.34] That's maybe a bit suburban with up to 45-hour sartorial roads.
[508.20 → 511.74] And we learned to master it and then went to San Francisco.
[512.10 → 521.30] There is dense urban with fog and some rain and hills and windy roads and narrow roads and, you know, tons of pedestrians downtown.
[521.68 → 522.78] So, we dealt with that.
[523.54 → 524.90] And then we started expanding.
[525.72 → 529.52] I think some of this is Atlanta is a big city, also different state.
[529.52 → 537.52] There are some differences across the various states in both how people instrument the roadway and how people drive, right?
[537.58 → 539.76] So, we're spreading geographically more and more.
[539.92 → 542.84] I think also we're spreading to other domains.
[543.14 → 546.16] A few that are really top of mind is highways.
[546.90 → 549.70] We have been working on highways for a long time.
[550.56 → 552.84] We've gotten to a certain point with highways.
[553.50 → 556.48] Generally, to have a good taxi service, you need highways, right?
[556.48 → 560.36] And it turns out that's a very fascinating, interesting problem.
[560.60 → 567.46] They're difficult because whenever you move at high enough speeds, like 65 miles an hour or so, right?
[567.56 → 570.58] The consequences of any mistake are really high.
[571.60 → 573.10] And many things can happen.
[573.40 → 577.74] And so, it pushes your, I mean, robustness and safety capability there.
[577.74 → 581.00] So, we've been doing highways, but one thing I did do is I rode.
[581.22 → 584.96] Now, we can give highway rides to employees.
[585.54 → 590.34] And I rode one to Millay Station to get to the airport.
[591.26 → 592.36] And it's fantastic.
[592.58 → 596.42] So, I hope to be able to bring it in the future to more and more people.
[596.60 → 598.98] I think that will make the service a lot more useful.
[598.98 → 605.72] Also, we announced that we will drive in other cities that have snow.
[606.26 → 608.46] So, potentially even in 26, right?
[608.58 → 615.70] So, our sixth generation platform is designed after the Jaguar, right?
[615.90 → 618.04] It's a Zika vehicle.
[618.94 → 625.80] And that Zika is designed with our hardware suite to be able to handle snow.
[625.80 → 629.54] And we are also heading out to other countries.
[629.74 → 636.22] So, we announced that we intend to launch driverless capabilities in London next year.
[636.58 → 640.12] And London is left-side driving city.
[640.56 → 644.74] And so, it's Tokyo where we currently have vehicles, and we're testing, right?
[644.94 → 653.16] So, you can see we're trying to cover little by little the operational design domain of most large metros with all of their properties.
[653.16 → 654.56] We're, of course, also in Texas.
[654.56 → 656.02] That's its own unique state.
[656.34 → 660.26] But we started with most southern states, large metros.
[660.50 → 662.58] So, you don't have to worry about snow, at least.
[662.88 → 668.42] Like, you want to tackle these challenges in some order, not just try to do everything at the same time.
[668.48 → 674.80] It's very difficult to validate your ability to do well in everything all at the same time, right?
[674.84 → 683.16] So, we're just taking – we're kind of mixing what makes business sense with actually expanding the capabilities to become truly global driverless.
[683.16 → 686.90] And you started – you mentioned the driver, the car.
[686.90 → 694.12] I'm wondering if for those out there, those listening, which this is kind of maybe hard to do just from an audio standpoint.
[694.12 → 706.26] But if you kind of imagine the driverless car as a system in 2025, how would you kind of describe that architecture, that system?
[706.40 → 708.56] What are the kind of main components?
[708.56 → 713.14] Like, I imagine, you know, the sensors, the actual car, the computer.
[713.46 → 716.36] Like, what does that system look like in 2025?
[716.98 → 717.92] Just at a high level.
[718.04 → 723.76] And then, of course, I'm sure we'll get into some of the modelling things and foundation models and all of those things.
[723.76 → 727.48] I mean, the car is – you know, ultimately, it's a robot on wheels, right?
[727.56 → 731.46] The main distinguishing capabilities are that it has a set of sensors.
[731.70 → 735.94] In our case, camera, lighter, radar, and microphones.
[736.50 → 743.72] Our microphones are quite helpful for many things, including listening to sirens, right, and occasional instructions.
[744.26 → 747.12] Then you have computed on the car.
[747.28 → 748.82] It's a non-trivial amount of compute.
[749.04 → 751.32] It's more than you can put on a phone, right?
[751.32 → 753.94] And all our vehicles are electric.
[754.16 → 756.42] That was an explicit choice of the company.
[757.28 → 759.38] I'm personally quite proud of this choice.
[759.52 → 770.34] I think that's good for the environment to actually have such cars and I think can accelerate, I think, transition to more electric vehicles, which I think is good, personally.
[771.10 → 774.12] And so they have this robot on wheels with compute and sensors.
[774.80 → 776.22] And then you have actuators, right?
[776.22 → 782.56] Then there is a lot of system design engineering to make sure, you know, steering and brakes and all these things.
[782.88 → 793.26] They need redundancy and robustness to make sure that if any system goes wrong, or we need to think also if compute parts of it can go down, that you have contingencies.
[793.44 → 795.20] So it needs to be designed with redundancy.
[795.34 → 803.68] You need to think of what if, you know, steering wheel column, like there can be also issues with steering.
[803.68 → 804.94] What is the redundancy?
[805.12 → 809.76] So for autonomous vehicle, you need to think additionally and build these things into the hardware.
[809.96 → 815.90] So it's a robot designed for safe transportation from the ground up, even though we're built using.
[816.58 → 819.04] We're just extending existing platform.
[819.54 → 821.88] And we work with the various automakers to do this.
[821.88 → 840.20] As you're doing this and you guys have progressed over these five years, you know, since we last talked, you know, one of the challenges is not – probably not every person out there is a Chris or a Daniel who's very invested in this kind of technology, you know, going forward.
[840.30 → 841.40] You have a lot of people out there.
[841.74 → 847.10] Here in the South, we joke that, you know, every other driver thinks they're a NASCAR driver and stuff.
[847.10 → 861.44] And that notion of control and safety and, you know, the general population may not have as much confidence in some of these technologies because they're not following it closely and living it the way you do all the time.
[861.84 → 863.98] How do you approach that?
[863.98 → 890.10] And how has that changed over these last five years since we talked to you last in terms of getting buy-in from the public and getting them feeling, you know, like it's – as you talk about the safety statistics, which are amazing, but getting them to really feel that deep down, you know, inside that they can – that they know they can trust and believe in this mode and that it is, in fact, much, much safer than what they're typically doing on a day-to-day basis.
[890.44 → 892.66] So there is – you know, people do not feel statistics.
[892.66 → 895.86] It's hard, right, because they're a product of many, many rides.
[896.40 → 900.48] You're doing 10 or even 100 safely is not enough.
[900.78 → 912.90] I think what people feel is when they get into the vehicles – and this worked for me in my – in my high moment, even though even before, and also my wife and friends of mine – people get comfortable really, really fast.
[913.32 → 917.78] You need to pass a certain bar where they feel, okay, this thing actually is a really, perfect driver.
[917.78 → 925.26] My mother-in-law sat in it just a few weeks ago for the first time, and she – she rolled around.
[925.36 → 928.36] She's like, this car drives much better than me, right?
[928.56 → 931.74] And once she thinks this way, she's immediately at ease, I think.
[931.88 → 936.60] And I think people relax after the first several minutes are very exciting.
[936.60 → 945.26] And then they relax and enjoy the experience and mind whatever they like to mind, either the environment or their phone or other things.
[945.80 → 950.54] People get really used to it if you cross this threshold of can I trust you?
[951.10 → 953.86] And I think your driving immediately shows this.
[953.86 → 960.12] Now, us in the industry also understand that, you know, coming back to statistics, you need to back it up.
[960.96 → 971.70] And so in regard to backing up, Waymo, right, has – we believe in transparency, and we're quite open with the incidents that happen.
[971.92 → 977.62] We file the details, and we also track the statistics and do our best estimate.
[977.82 → 978.98] We have a great safety team.
[979.08 → 981.26] They publish these reports in them.
[981.26 → 992.42] We evaluate and try to estimate how are we doing compared to a fleet of human taxi drivers or human drivers driving in our area that we are handling.
[992.94 → 999.96] And this is both by us but also like their studies done by insurance companies who, of course, want to quantify this very well.
[1000.48 → 1003.52] And so there is a Swiss REST study also proving our numbers.
[1003.52 → 1011.38] They also believe we significantly can decrease claims of different kinds for injuries, for accidents, and so on as well.
[1011.74 → 1015.82] So that's another external validation for the kind of thing we provide.
[1016.44 → 1018.02] So that's what I would say to people.
[1018.16 → 1019.76] Now, you know, it's a process.
[1019.90 → 1021.68] You need to work with the local communities.
[1021.88 → 1023.60] You need to work with police.
[1023.80 → 1027.76] You need to work with, you know, the various city stewards, officers.
[1028.16 → 1029.54] We train a lot of people.
[1029.70 → 1030.68] We engage with them.
[1030.76 → 1031.70] We work over time.
[1031.70 → 1039.26] I think you can see that in the cities we have been over time, I believe generally the trust in us increases.
[1040.24 → 1051.38] And I think that the satisfaction of Waymo by the users, if you look at the apps like in the stores, so I think on the App Store, we had a five-star rating, right?
[1051.38 → 1058.82] So there is a lot of, a bit of almost like people that would just use Waymo now.
[1059.34 → 1060.74] It's if they could.
[1061.26 → 1064.90] And that's a testament to the value that people see in the rights.
[1065.40 → 1071.78] But it drives, of course, to safety and, you know, ultimately engaging these people, getting them comfortable.
[1071.78 → 1076.48] Often when people experience this, many of them become converts.
[1077.00 → 1078.84] So I encourage people, try it.
[1079.32 → 1081.52] You may be the next convert if you have not yet.
[1081.80 → 1082.90] I personally love it.
[1083.00 → 1085.02] I take it as much as I can.
[1085.54 → 1089.32] And it's always a pleasure working on a product you enjoy yourself.
[1089.46 → 1091.06] So I feel blessed that way.
[1091.06 → 1112.98] Well, friends, it is time to let go of the old way of exploring your data.
[1113.26 → 1114.18] It's holding you back.
[1114.52 → 1116.54] But what exactly is the old way?
[1116.54 → 1123.82] Well, I'm here with Mark Duppy, co-founder and CEO of FBI, a collaborative analytics platform designed to help big explorers like yourself.
[1124.26 → 1126.10] So, Mark, tell me about this old way.
[1126.60 → 1136.90] So the old way, Adam, if you're a product manager or a founder, and you're trying to get insights from your data, you're wrestling with your Postgres instance or Snowflake or your spreadsheets.
[1137.00 → 1142.62] Or if you are, and you don't maybe even have the support of a data analyst or data scientist to help you with that word.
[1142.62 → 1157.72] Or if you are, for example, a data scientist or engineer or analyst, you're wrestling with a bunch of different tools, local Jupyter notebooks, Google Cola, or even your legacy BI to try to build these dashboards that someone may or may not go and look at.
[1157.72 → 1168.90] And in this new way that we're building at FBI, we are creating this all-in-one environment where product managers and founders can very quickly go and explore data regardless of where it is.
[1169.02 → 1169.08] Right.
[1169.12 → 1169.90] So it can be in a spreadsheet.
[1170.08 → 1170.80] It can be an Airtable.
[1170.94 → 1172.12] It can be in Postgres, Snowflake.
[1172.28 → 1178.78] Really easy to do everything from an ad hoc analysis to much more advanced analysis if, again, you're more experienced.
[1179.26 → 1186.36] So with Python built in, you know, Python built in right there and our AI assistant, you can move very quickly through advanced analysis.
[1186.36 → 1204.52] And a really cool part is that you can go from ad hoc analysis and data science to publishing these as interactive data apps and dashboards, or better yet, at delivering insights as automated workflows to meet your stakeholders where they are in, say, Slack or email or spreadsheets.
[1204.52 → 1218.04] So, you know, if this is something that you're experiencing, if you're a founder or a product manager trying to get more from your data or for your data team today, you're just underwater and feel like you're wrestling with your legacy, you know, BI tools and notebooks, come check out the new way and come try out FBI.
[1218.24 → 1218.92] There you go.
[1219.08 → 1222.40] Well, friends, if you're trying to get more insights from your data, stop resting with it.
[1222.74 → 1225.36] Start exploring it the new way with FBI.
[1225.66 → 1228.66] Learn more and get started for free at Fabi.ai.
[1228.66 → 1231.94] That's F-A-B-I dot A-I.
[1232.06 → 1234.44] Again, FBI dot A-I.
[1239.16 → 1249.08] Well, Drag, I understand that every driverless car company is going to have a different, you know, approach to modelling and all of those sorts of things.
[1249.08 → 1256.02] You've talked a little bit about the hardware and the car, but we just, I think it would be good for people to understand.
[1256.38 → 1260.28] We talk about this driver, or you mentioned the driver.
[1260.46 → 1269.44] People might have in their mind, because we do talk a lot about models now after the generative AI boom, that there's this model that can reason and blah, blah, blah.
[1269.44 → 1274.20] And so people might have this view of like, there is a model that drives the car.
[1274.32 → 1287.84] Could you help us really break down like in 2025, is this a system of models, models that do different things, a kind of combination of different types of models and even non-AI pieces?
[1288.14 → 1294.32] Could you just help us kind of generally understand how that works?
[1294.32 → 1299.04] So when you think of the stack, right, let's talk first about what it needs to do.
[1300.10 → 1302.70] It needs to perceive the environment using the sensors.
[1302.96 → 1305.76] It needs to build some representation of this environment.
[1306.38 → 1311.56] It needs to use this representation of the environment to make a set of decisions.
[1312.54 → 1317.02] And so traditionally, I mean, autonomous vehicles are around a long time.
[1317.14 → 1319.56] We are around over 15 years already, right?
[1319.56 → 1329.22] So it's a rapidly developing technology space, but traditionally you can think of there's this historical people thought, okay, there are these models.
[1329.34 → 1333.76] There's a perception model that builds a representation of the world that can be useful for certain things.
[1333.76 → 1341.40] And then there is some kind of behaviour prediction and planning module that reasons what we could do.
[1341.52 → 1349.60] And potentially some people like to also reason what others could do to cross-reference our behaviour with the other folks.
[1349.82 → 1354.48] And then based on all this information, eventually select promising decisions, right?
[1354.56 → 1357.82] So that's what the stack normally does.
[1358.24 → 1360.08] Now, there are different ways to implement it.
[1360.08 → 1371.96] Generally, the trend has been to have few, and in some cases people claim they have one, large models, AI models on the car.
[1372.08 → 1373.50] And you can say ML or AI.
[1373.68 → 1374.84] For a while it was called ML.
[1375.10 → 1378.52] When the models became big enough, people called it AI, right?
[1379.54 → 1381.92] So you have these large AI models on the car.
[1382.46 → 1385.62] A few or one, depending on the various companies.
[1385.80 → 1387.94] And they're connected in certain ways.
[1387.94 → 1390.16] You can train them end-to-end or not.
[1391.08 → 1392.12] That's also an option.
[1392.28 → 1393.54] Different companies can choose.
[1393.66 → 1395.06] The two are orthogonal concepts.
[1395.20 → 1400.04] Whether you have models and whether you can train them end-to-end is different concepts, right?
[1400.48 → 1402.30] So it can be structured end-to-end.
[1402.66 → 1404.62] So essentially you have models end-to-end, end-to-end.
[1404.88 → 1405.46] These are two.
[1405.84 → 1412.60] And so different companies on this very coarse taxonomy fall somewhere in this bucket, right?
[1412.60 → 1420.98] And I think Waymo, I mean, always has used AI or ML since I've been there, and it's been the backbone of our tech.
[1421.62 → 1425.92] I think over time our models have streamlined and become fewer and fewer.
[1426.14 → 1427.04] I can say that.
[1427.04 → 1438.28] I think off-board, what my team does is build these large foundation models for Waymo that are not limited by how much computer latency constraints you have.
[1438.42 → 1446.70] And they can be quite helpful to essentially curate data or teach the models that actually run on the car in the simulator.
[1446.82 → 1448.24] We can get to simulators later.
[1448.24 → 1456.00] So we have experience with most aspects of these options, whether it's end-to-end and whether they're structured or not, right?
[1456.16 → 1462.32] I think off-board, I can definitely tell you we've explored a lot with large vision language models.
[1462.46 → 1465.90] That's one of the latest technologies that's relevant to us.
[1466.04 → 1473.88] I think in the field of robotics, people talk also about vision language action models because you can tie in one model, you know,
[1473.88 → 1482.00] both understanding vision and language inputs and potentially ask for certain actions as outputs, right?
[1482.04 → 1484.24] Which is ultimately what the robot needs to generate.
[1484.66 → 1488.40] So that's an exciting area that has developed in 25.
[1488.40 → 1497.78] I think in our foundation model, Waymo foundation model, we combine like benefits of these vision language models,
[1498.08 → 1502.18] but also combine it with some bespoke Waymo architecture innovations.
[1502.18 → 1508.98] I think in areas such as, you know, fusing these new modalities that vision language models typically are not trained on,
[1509.12 → 1512.40] like LIDAR and radar is one.
[1512.76 → 1517.76] Another one is modelling the evolution, future potential evolutions of the world.
[1518.04 → 1522.56] There is some interesting Waymo technology on how to do this well that we also use.
[1522.56 → 1529.22] But we fuse all of this and VLM technology, world knowledge from also other bases,
[1529.36 → 1538.36] whether it's a world model or visual language model into something that then is able to do well on autonomous driving tasks.
[1538.88 → 1539.86] So that's off board.
[1540.02 → 1543.22] On board, we don't typically talk exactly what is there,
[1543.22 → 1551.60] but I think we're trying to get state-of-the-art the best architectures that we believe solve the problem
[1551.60 → 1553.88] and put them together on the car.
[1554.52 → 1564.86] I think it's a really, really high bar to have a model perform in all the conditions and all the situations we need it to, right?
[1564.86 → 1571.12] And so we also have some notion of, as you know, VLMs also have this weakness of hallucination.
[1572.10 → 1579.44] So we have the safety harness around them to prevent hallucination, to double-check what they're predicting, right?
[1579.46 → 1584.94] So we also have that aspect in our style as well, which we have worked on historically.
[1585.52 → 1587.74] So that's what I can say on a high level.
[1587.86 → 1589.56] I hope that's not too scattered.
[1589.56 → 1595.04] Maybe you guys, if you want anything specific, we can discuss that in a little bit more detail.
[1595.78 → 1597.68] So I do have a follow-up to that.
[1598.00 → 1607.52] And recognizing that you're not able to get into the specifics of how, of the architectural decisions and model decisions that Waymo is engaged in,
[1607.76 → 1613.04] if you could abstract it a little bit and maybe just talk about the space a little bit.
[1613.04 → 1622.12] But, you know, I'm curious, as you talk about world models, you know, and having representation of the environment that brings in not only AI,
[1622.26 → 1628.50] but the notion of simulation as, you know, one of the tools in the tool chest, if you will.
[1628.86 → 1634.90] I suspect, like, we have a lot of listeners that are hearing lots of different AI use cases in general,
[1634.90 → 1638.06] but may not have as much expertise in autonomy.
[1638.06 → 1644.26] And so as you talk about that notion of representation of that environment,
[1644.60 → 1647.92] could you talk a little bit about, like, what that problem looks like
[1647.92 → 1651.76] and what are different things that you might think of to solve it,
[1652.18 → 1654.42] without having to get into how you guys have done it,
[1654.46 → 1659.22] but just kind of, like, what is that juxtaposition of simulation, AI,
[1659.62 → 1662.96] and representation of the world and the surrounding environment look like?
[1662.96 → 1668.60] So maybe, I mean, simulation, if we're going to go there, maybe I can just juxtapose two things there.
[1668.92 → 1670.74] I like saying this historically.
[1670.90 → 1672.00] I've been doing this for a while.
[1672.52 → 1675.02] There are two main problems in autonomy.
[1675.20 → 1678.06] One is to build this onboard driver.
[1679.12 → 1683.44] And another one is to test and validate this onboard driver.
[1684.18 → 1686.06] And both are really, really hard problems.
[1686.14 → 1687.84] And people usually talk about the first one.
[1687.84 → 1694.08] But I think, imagine there is some collection of models
[1694.08 → 1699.24] and you need to prove that it's safe enough to put them out in the real world.
[1699.72 → 1702.02] That's in itself a really challenging problem,
[1702.14 → 1706.26] arguably no simpler than putting the model, the first model together.
[1706.42 → 1711.58] And that one, ultimately, because you need to be a bit more exhaustive,
[1711.58 → 1717.78] potentially takes even longer time to build the full recipe to validate things properly, right?
[1718.16 → 1719.44] So these are the two problems.
[1719.58 → 1727.98] Now, in autonomy, what is different maybe than the standard AI models is there are a few things.
[1728.52 → 1734.16] One is, I mean, ultimately output actions that are commands to a robot
[1734.16 → 1741.02] that are a different type of data than traditionally, say, text and images, right?
[1741.08 → 1741.92] I think that's one.
[1742.08 → 1746.60] Another one is we operate under strict latency constraints.
[1746.72 → 1747.74] You need to react quickly.
[1748.56 → 1752.76] For us, what is also interested in AV is this is probably the first serious domain
[1752.76 → 1756.30] where we had to really learn how to interact with humans in the same environment.
[1756.90 → 1760.64] So it's highly interactive multi-agent setup, right?
[1761.02 → 1764.38] And then we have additionally, if we choose to add additional sensors and cameras,
[1764.48 → 1767.26] we have a lot more modalities coming in, and we have a ton of data.
[1767.26 → 1776.90] So essentially, the way to think of it is imagined you get maybe billions of sensor reading per second
[1776.90 → 1779.74] or even tens of billions, a lot.
[1779.74 → 1782.80] And you need to make a decision.
[1782.80 → 1791.50] You need to have a context of many seconds of these sensor inputs, maybe a dozen cameras, half a dozen lighter and radar.
[1791.50 → 1795.42] And so you need to collect, you know, maybe five to 10 seconds.
[1795.42 → 1798.92] Some can argue 20, 30 of context to make a decision.
[1800.38 → 1800.52] Right?
[1800.52 → 1802.74] So, and the decision is fairly low dimensional.
[1802.94 → 1805.86] It's like, okay, steering or, you know, acceleration.
[1805.86 → 1810.66] But the inputs are incredibly bulky.
[1810.92 → 1815.10] And so you need to somehow learn the mapping from this extremely high dimensional space,
[1815.66 → 1817.54] representational space to decisions.
[1818.34 → 1820.30] That's very hard, right?
[1820.40 → 1824.20] Under latency constraints, under safety critical constraints.
[1824.62 → 1826.50] That's what makes our domain interesting.
[1826.70 → 1832.06] Now, a lot of the things that work in machine learning in one domain transfer to the other, right?
[1832.06 → 1841.28] So, yes, there is, for example, very similar scaling law findings that if you have cutting edge architectures
[1841.28 → 1846.58] and you do proper, you know, studies and scaling, and you have a lot more data and compute
[1846.58 → 1848.68] and you feed it to these architectures.
[1849.38 → 1852.78] And now for every class of algorithms, there's a bit different scaling laws.
[1852.90 → 1858.46] But even the simpler imitative algorithms that people also did in language predict next token,
[1858.54 → 1860.62] we can predict next action, right?
[1860.62 → 1861.94] There is these direct parallels.
[1862.08 → 1864.24] You can do reinforcement learning in language.
[1864.40 → 1867.48] We can do reinforcement learning in our simulator, right?
[1868.28 → 1869.38] These are the parallels.
[1869.58 → 1871.74] But how exactly things translate is interesting.
[1872.02 → 1873.26] The ideas translate.
[1873.42 → 1876.24] The implementation is a little more creative than the usual,
[1876.66 → 1881.54] just staying on the internet because there is a bit of a domain jump to the real world, right?
[1881.54 → 1882.44] So that's interesting.
[1883.30 → 1886.18] The other part is compared to, say, language, LLMs,
[1886.50 → 1890.44] you can actually have a paper, Motion, from two or three years ago.
[1890.62 → 1896.18] Where it was, the idea was, hey, why don't we talk in those motions to make them like language?
[1896.90 → 1898.90] It turns out it's a very effective idea.
[1899.10 → 1903.16] Now, it models that architecture, which is very LLM-inspired.
[1903.30 → 1908.22] It models future interactions of agents in the environment very well.
[1908.30 → 1914.86] Like you can think of agents talk to each other with these motions they execute simultaneously in an environment.
[1914.86 → 1917.02] And now you can leverage the machinery.
[1917.02 → 1917.96] We have this paper.
[1918.22 → 1920.54] It's quite effective, right?
[1921.06 → 1923.76] So that's an example of this.
[1924.20 → 1928.48] Now, one other interesting point, though, is text is its own simulator.
[1928.70 → 1932.26] Essentially, you know, you speak text to each other.
[1932.36 → 1933.40] That's the full environment.
[1933.82 → 1936.34] You spit out text tokens, text tokens, and text tokens.
[1936.34 → 1941.76] In our case, we, well, we predict actions.
[1942.02 → 1943.12] We execute actions.
[1943.94 → 1947.82] Imagine now, but you need the simulator because now, based on these actions,
[1947.94 → 1950.58] you need to envision what the whole environment looks like
[1950.58 → 1955.28] and how your, whatever, hundreds of millions to billions of sensor points look like.
[1955.90 → 1958.36] So now you need something that generates them as you act
[1958.36 → 1960.62] so you can test yourself how you behave over time.
[1960.62 → 1964.24] As you make decisions at a fairly high frequency,
[1965.06 → 1967.92] then there is a known problem, which is called covariate shift.
[1968.08 → 1972.14] Essentially, decisions can take you to places you may not have seen before in the data.
[1973.02 → 1976.78] And there you may have particular failure things that you may not observe
[1976.78 → 1980.50] unless you push yourself and drive on policy to those places in the data.
[1980.62 → 1982.42] But to drive there, now you need the simulator.
[1982.56 → 1986.22] The simulator needs to be realistic enough where, you know,
[1986.22 → 1990.10] you don't go somewhere else entirely as opposed to the actual place
[1990.10 → 1991.88] you will end up with decision-making.
[1992.30 → 1993.90] So that's another very interesting point.
[1994.04 → 1995.12] Like simulation is hard.
[1995.22 → 1999.32] If you want robust testing, simply having drivers on the road
[1999.32 → 2003.96] is not a particularly scalable solution if you want to keep it a rating on your stack
[2003.96 → 2007.28] because some of the events happen once in a million miles or more.
[2007.82 → 2009.96] And you would much rather test them in the simulator.
[2010.12 → 2012.40] But for the simulator, now you have to solve this problem,
[2012.50 → 2013.92] which is interesting and challenging.
[2013.92 → 2015.84] So that's unique in our domain.
[2016.22 → 2033.52] What if AI agents could work together just like developers do?
[2033.72 → 2037.30] That's exactly what agency is making possible.
[2037.82 → 2042.48] Spelled A-G-N-T-C-Y, agency is now an open source collective
[2042.48 → 2046.52] under the Linux Foundation, building the Internet of Agents.
[2046.94 → 2050.94] This is a global collaboration layer where the AI agents can discover each other,
[2051.32 → 2056.04] connect, and execute multi-agent workflows across any framework.
[2056.04 → 2060.36] Everything engineers need to build and deploy multi-agent software
[2060.36 → 2063.74] is now available to anyone building on agency,
[2063.96 → 2066.62] including trusted identity and access management,
[2066.98 → 2068.48] open standards for agent discovery,
[2068.86 → 2070.68] agent-to-agent communication protocols,
[2070.68 → 2074.72] and modular pieces you can remix for scalable systems.
[2075.14 → 2079.70] This is a true collaboration from Cisco, Dell, Google Cloud,
[2080.00 → 2083.42] Red Hat, Oracle, and more than 75 other companies
[2083.42 → 2086.06] all contributing to the next-gen AI stack.
[2086.28 → 2089.20] The code, the specs, the services, they're dropping.
[2089.36 → 2090.28] No strings attached.
[2090.28 → 2092.38] Visit agency.org.
[2092.50 → 2097.02] That's A-G-N-T-C-Y.org to learn more and get involved.
[2097.40 → 2102.14] Again, that's agency, A-G-N-T-C-Y.org.
[2106.88 → 2112.98] Well, Drag, I'm really intrigued by how you kind of helped me form a mental model
[2112.98 → 2117.68] for the types of problems that are part of the research in this area.
[2117.68 → 2123.14] Yeah, I would definitely encourage our listeners to go check out waymo.com slash research.
[2123.14 → 2127.88] There are a bunch of papers there that people can find and read,
[2128.04 → 2131.14] but also there's even Waymo Open Dataset,
[2131.32 → 2135.40] which supports research and autonomous driving.
[2135.40 → 2137.82] So that's really cool to see.
[2138.00 → 2138.72] It's amazing.
[2139.18 → 2142.30] I'm wondering, Drag, as you look at this kind of,
[2142.38 → 2145.70] I see all sorts of things from, you know,
[2145.92 → 2150.90] scene editing to forecasting and planning to, you know...
[2150.90 → 2153.90] Did I mention you need to embody the agents in the simulator too?
[2154.02 → 2155.24] They're not deterministic.
[2155.60 → 2156.02] Oh, yeah, yeah.
[2156.02 → 2157.56] Because if you start doing different things,
[2157.62 → 2158.90] you need to, well,
[2159.52 → 2162.36] guide the agents to react to you in reasonable ways as well.
[2162.36 → 2166.88] Otherwise, you know, they'll be reacting to an empty spot where you're no longer,
[2167.42 → 2170.32] even if you collected the situation with your sensors,
[2170.80 → 2172.72] as you start deviating from it in the simulator,
[2172.96 → 2175.04] you still need the agents to do reasonable things, right?
[2175.06 → 2175.46] Yeah, yeah.
[2175.48 → 2176.78] Yeah, yeah.
[2176.80 → 2177.40] That makes sense.
[2177.52 → 2181.12] And I guess that really kind of gets to my question a little bit,
[2181.18 → 2185.16] which is, I assume over the last five years, as we haven't chatted,
[2185.16 → 2191.88] there's been a lot of progress in certain areas and maybe certain challenges that are kind of
[2191.88 → 2197.54] holdouts that remain very, very challenging and maybe not as much progress as made.
[2197.66 → 2201.38] So in this kind of autonomous driving research world,
[2201.94 → 2210.02] can you paint in broad strokes kind of where there has been very rapid progress as things
[2210.02 → 2216.22] have advanced and maybe some of those of the hardest problems to solve that still remains
[2216.22 → 2218.94] kind of at arm's length, if you will?
[2219.54 → 2224.38] I mean, I would say one thing for folks that especially are closer to robotics,
[2224.56 → 2229.92] they will see just like the field of AI is going through some crazy inflection point of,
[2230.00 → 2234.12] I mean, both methods people develop and popularity.
[2234.12 → 2237.60] I think the same is true in robotics and the same is true in AV.
[2238.02 → 2242.18] I've been in the space over 10 years now, just doing AVs.
[2242.90 → 2250.12] And I would say every couple of years, our capabilities with AI and machine learning
[2250.12 → 2253.32] dramatically expand due to innovations.
[2253.74 → 2256.22] And this innovation train has not stopped.
[2256.48 → 2260.56] So like where we are five years later compared to five years before in terms of modelling,
[2260.56 → 2265.36] I think is still a huge improvements possible.
[2265.58 → 2270.78] I think we're moving more and more to machine learn power stacks.
[2271.28 → 2280.42] And I think ultimately understanding how to leverage, I mean, data-driven, right?
[2281.02 → 2285.42] Elegantly, scalably handle this problem with data-driven solutions.
[2285.90 → 2288.28] And so that's been generally an evolution.
[2288.28 → 2291.18] And I think we understand how models behave better.
[2291.38 → 2297.34] I think these latest architectures and the scaling that we mentioned is a fascinating domain.
[2297.46 → 2299.98] We started studying it, for example, for a while back.
[2300.48 → 2305.32] So there's this paper we have, for example, of scaling laws of motion LLM architecture.
[2305.48 → 2307.46] So it's an LLM-like architecture.
[2307.68 → 2310.30] So you say, oh, what are its scaling laws?
[2310.34 → 2311.78] How does it compare to LLMs?
[2311.84 → 2313.72] We have a tech report on this, for example.
[2313.72 → 2319.96] Still similar kind of learnings transfer as LLMs, but there's some bespoke fascinating things.
[2320.06 → 2326.98] For example, for that architecture, improving what's called open loop prediction performance seems to correlate to improving closed loop performance.
[2327.14 → 2329.54] That's not always true, right?
[2329.54 → 2333.30] And we see different scaling factors compared to language.
[2333.30 → 2339.10] Like our motion space is nowhere near as diverse as language tokens, right?
[2339.14 → 2347.56] So we need actually, for the same set of parameters model, we need a lot more data of examples of how the world behaves to scale.
[2347.68 → 2349.84] These are interesting findings generally, right?
[2349.84 → 2351.16] So that's one.
[2351.64 → 2363.34] I think now, as the architectures keep evolving, now there's diffusion and autoregressive models, and now how do each compare, and how do they compare in open loop and closed loop?
[2363.60 → 2366.62] These are all very interesting areas people are studying.
[2367.18 → 2375.96] I think generally there's this question lately as well of how do you build the best simulator with machine learning and what kind of models are there?
[2375.96 → 2383.72] And, you know, most recently there's some groundbreaking work, like the Genie model by Google.
[2384.32 → 2385.78] I don't know if you guys saw it.
[2385.82 → 2387.40] It's a controllable video, essentially.
[2387.78 → 2394.02] You can, like, give motion controls, and it dreams the video close to real time of what it should look like.
[2394.06 → 2399.60] So essentially, you're controlling the world you're imagining a bit, right?
[2399.60 → 2407.58] And you can do this in real time, or you can do it, of course, off-board to or offline with even larger, potentially, models.
[2408.36 → 2413.64] And so now these models are pre-trained on a large amount of video and text.
[2413.96 → 2424.38] And so they capture a lot of knowledge of how the real world behaves, and it's somewhat complementing the knowledge that vision language models capture from the internet corpuses.
[2424.38 → 2426.56] And so how do these two relate?
[2426.74 → 2428.44] How do you mix them, right?
[2428.62 → 2432.64] Which one is beneficial for which type of tasks?
[2433.02 → 2438.44] These are all interesting capabilities that people are doing.
[2438.86 → 2446.76] And maybe one other interesting topic is there's a lot of talk about architectures for robots that are some combination of system two and system one architecture.
[2446.76 → 2449.78] So you guys may have heard it, right?
[2449.90 → 2454.52] Now, we know that large models are more capable when trained on more data and more compute.
[2454.72 → 2461.58] But in latency-sensitive situations, you can't, if they're too big, you can't run them in real time.
[2462.66 → 2468.10] So now the question is, okay, well, what if you have a real-time model that handles most cases,
[2468.10 → 2482.02] but then you have a slower model that does better high-level reasoning, that runs at some slower hertz, that helps guide and understand additionally and provide this to the fast model well-needed,
[2482.16 → 2485.88] while still keeping this reflexive capability?
[2486.08 → 2488.22] If someone jumps in front of you, you still respond, right?
[2488.30 → 2491.36] Like these are interesting questions in our domain as well.
[2491.42 → 2492.44] So there's many, actually.
[2492.44 → 2500.68] It's a really, really fascinating time, and I think we're studying a lot of these questions, just as the whole field is.
[2500.74 → 2503.62] And we have some very interesting findings, some of them not published yet.
[2503.74 → 2506.36] Generally, I would encourage people, come join us.
[2506.56 → 2517.96] You can, well, you know, contribute to the premier embodiment of physical AI currently out there, and you can do interesting research.
[2519.12 → 2519.24] Right?
[2519.46 → 2520.26] Sounds like fun.
[2520.26 → 2523.48] But, yes, these are all fascinating topics.
[2523.56 → 2527.30] And, of course, how to control hallucinations in all these models.
[2527.76 → 2537.00] How do you determine when these models are out of domain and potentially making clear mistakes, right?
[2537.08 → 2537.92] This can happen.
[2538.18 → 2545.16] We have research experience with VLMs like, you know, like many of the current ones.
[2545.16 → 2552.84] But we have a paper called EMMA where we tried to fine-tune VLM for driving tasks, got a bunch of learnings.
[2553.08 → 2556.78] It can be quite good, but it has limitations too, right?
[2556.94 → 2561.26] So how do you overcome these limitations with additional system design is very interesting.
[2561.26 → 2567.66] I'm curious as we're talking about this, and I'm really enjoying the conversation.
[2567.66 → 2573.30] And I work for another company in autonomy, but in a slightly different context.
[2573.30 → 2581.50] And I'm curious, one of the things that is popular in the industry I'm in right now is solving for swarming behaviours.
[2581.50 → 2589.22] As you're talking about many autonomous vehicles that are having to collaborate in certain ways.
[2589.32 → 2593.48] I'm curious from your take, that may or may not be an interesting problem for Waymo.
[2593.60 → 2599.14] I don't know what your thinking is on that, but I would love to know when you look at that space,
[2599.74 → 2608.10] what are some of the things that you think about and are interesting to you about the notion of many autonomous vehicles collaborating together?
[2608.10 → 2620.32] That's been a very interesting area that actually there was early research that I was impressed with where people proved that if you can control groups of vehicles, you can improve traffic flow.
[2620.94 → 2625.20] So to me, we're not exactly swarming yet, autonomous vehicles.
[2625.36 → 2629.48] They're still a subset, a relatively small subset of the whole traffic.
[2629.48 → 2638.34] So it's mostly when I think of swarming, I imagine, say, a crowd of 200 people on Halloween all around the car and stuff like this.
[2638.40 → 2639.08] That's swarming.
[2639.18 → 2646.64] Or you go downtown after a Giants game, and they're exiting and that is swarming, right?
[2647.06 → 2652.52] They're the human agents, so to speak, more prone these days to swarming than AVs still.
[2652.64 → 2653.88] Maybe we'll get more prominent.
[2653.88 → 2661.66] I think when you think of coordinating multiple AVs, in our domain already, they do send each other valuable information.
[2661.82 → 2669.78] For example, if one of our vehicles encounters some very complex construction, it can help pass information about it to the others.
[2669.84 → 2679.08] If we encounter potentially slowdowns or vehicles getting stuck, that kind of information can be passed.
[2679.08 → 2686.02] I think controlling jointly vehicles starts becoming interesting now that we're getting to some kind of scale.
[2686.96 → 2691.58] I think one of the interesting domains where this is interesting is when you want to charge them.
[2692.60 → 2695.74] So imagine you need to charge now hundreds of vehicles in a location.
[2695.86 → 2702.04] How do you control all these vehicles so that they all get to the right place and don't block each other?
[2702.70 → 2703.96] And it's all very efficient.
[2703.96 → 2707.86] That's one example of where you're fairly swarmed.
[2708.04 → 2709.64] It's your own warehouse, right?
[2709.70 → 2712.58] Or a garage where this comes up.
[2712.66 → 2718.42] And then down the line, potentially, there are opportunities to improve traffic flow for everyone.
[2718.60 → 2721.82] But that's still maybe in the future.
[2722.38 → 2724.46] Well, you took us right there, Drag.
[2724.68 → 2729.72] As we're kind of getting close to an end here, I'd love to talk about that future.
[2729.72 → 2734.76] And we were talking beforehand, and I was saying I'd love for you to share just what you're excited about.
[2734.92 → 2741.34] And that could be, of course, in general related to driverless research.
[2741.68 → 2750.72] It could be kind of in the AI ecosystem generally, something that you're excited about as you look forward to or are thinking about a lot.
[2751.20 → 2753.80] Does anything stand out so that we can ask you about it?
[2753.80 → 2761.28] Hopefully not in five years from now, but maybe the next time you're on in less than five years, we can ask you about it.
[2761.64 → 2762.34] Sounds good.
[2762.44 → 2767.42] Well, I'm around, so I could come probably faster than in five years' time.
[2767.76 → 2768.60] In a Waymo.
[2769.18 → 2769.34] Yeah.
[2770.46 → 2771.28] Potentially, yes.
[2771.42 → 2774.44] I think maybe let's go in a couple areas.
[2774.44 → 2781.64] First, maybe as to parallel this chat we had earlier, maybe first about the product and then a bit about the AI.
[2782.28 → 2785.48] I think in terms of the product, I'm excited.
[2785.76 → 2791.42] In a way, with the safety studies we've shown, these are significant improvements over the baseline.
[2791.42 → 2803.40] And I think we've shown it already at scale with some fairly, starts to become fairly good confidence or some statistical significance at this point.
[2804.46 → 2819.02] And maybe your listeners, I'm not sure if they understand, but even just on the U.S. roads alone, I'm not talking world roads, U.S. roads, 40,000 people die every year from accidents.
[2819.02 → 2820.04] That's a lot.
[2820.50 → 2823.76] And I think these gains are starting to become somewhat meaningful.
[2823.76 → 2828.14] So it starts becoming thinking, hey, maybe we have a mandate to expand.
[2829.08 → 2830.44] We should be expanding.
[2830.62 → 2832.12] It will save people's lives.
[2833.50 → 2835.04] And you think about it.
[2835.08 → 2841.08] And then the question is, how can I contribute to expanding?
[2841.46 → 2845.46] I mean, ignore all the of course, I believe it's a great service.
[2845.74 → 2847.90] A lot of people love it for a lot of good reasons.
[2847.90 → 2851.84] We could potentially go into some reasons people found where they love it, right?
[2851.88 → 2857.94] But like, I think even just from the mandate, okay, you know, it's helping in meaningful way.
[2857.94 → 2862.56] And I think being out there can make quite a dent against some of these numbers.
[2863.50 → 2866.06] And so, yes, I would love it to expand more.
[2866.22 → 2867.56] Now, we're doing that.
[2867.76 → 2871.30] I think to me, then, the question is, what can I do to contribute to it, right?
[2871.30 → 2882.38] And I think one of the most scalable solutions to tackling dozens of new cities and, you know, conditions and countries is machine learning and AI, right?
[2882.92 → 2889.60] And so now, for me, what I'm excited about is harness all the positive latest trends.
[2889.60 → 2910.44] I think, I think, for me, more directly first into the Waymo Foundation model work we're doing, where we can directly experiment and deploy them and then try to push more and more of them to contribute similar benefits and to the main production systems, which is the onboard driver and the simulator, right?
[2910.44 → 2912.02] So that's what I think about.
[2912.16 → 2927.50] Now, more specifically, if you don't want to go into AI techniques, I think this question of, okay, how do I endow vision language models with more modalities, right?
[2927.54 → 2928.66] It's a fascinating one.
[2928.70 → 2930.50] We actually have some good results already.
[2931.06 → 2936.98] Like, how do you expand to new modalities, say, right, LiDAR and RAID?
[2936.98 → 2940.04] How do you connect it to actions, the model?
[2940.04 → 2949.40] What's an effective way to do this while preserving all the world knowledge that's present in the model that you're trying to build on top of?
[2949.46 → 2952.72] It's an interesting model and system design challenge.
[2953.16 → 2956.24] And then what I'm also excited is building the simulator.
[2956.56 → 2960.00] I think, right, as realistic, as scalable as possible.
[2960.00 → 2968.62] I think the modern technologies, like the Gini model that I mentioned, these world models that are still relatively few and far between,
[2968.62 → 2972.24] but I think it's a ton of labs are working on them today.
[2972.24 → 2983.64] I think taking that kind of technology and build the most generalizable possible simulator with it, I think is fascinating.
[2983.64 → 2987.98] Now, the interesting thing is you could do that, but they can still be very expensive to run.
[2988.12 → 2996.86] So you still need to show, it's not just enough to show that it can handle very realistic, interesting cases.
[2997.20 → 3000.50] You still need to show how you can run it without breaking the bank.
[3000.50 → 3009.30] The amount of simulation Waymo does today to ensure that we're safe, we run like millions of virtual miles every day.
[3009.64 → 3016.68] That's a lot of things to simulate potentially with, you know, so many sensors on board and so on.
[3016.98 → 3020.00] So there needs to be, there's some very interesting question in that space.
[3020.06 → 3022.64] How do we get the maximum possible simulator realism?
[3022.74 → 3026.20] And how do we get the maximum possible scalable simulator?
[3026.20 → 3030.18] And there's a very interesting mix of technologies getting involved to do that.
[3030.64 → 3031.06] That's awesome.
[3031.24 → 3034.88] Well, I certainly, I'm certainly excited about that.
[3035.00 → 3038.78] Like I say, I encourage our listeners to check out Waymo's research page.
[3038.92 → 3041.40] Lots of amazing stuff to explore there.
[3042.00 → 3044.28] And folks can see our history, right?
[3044.38 → 3050.68] Like I think you can see the kind of work and papers people did from, I think, 2019 to now.
[3050.68 → 3052.90] And there's almost 100 papers there now.
[3053.08 → 3057.84] And maybe it's not 100 only because we may not have uploaded the most recent ones.
[3057.96 → 3061.36] I'll try to make sure we do soon if we're missing any.
[3061.48 → 3065.42] So if the readers go there, they can see the full set.
[3066.08 → 3066.98] That sounds great.
[3067.08 → 3069.22] Well, thank you for joining us again, Drag.
[3069.52 → 3071.94] It was a real pleasure to have you on the show again.
[3072.04 → 3075.48] And let's not make it five years next time.
[3075.58 → 3079.24] We'll try to get you on and hear the update sooner than that, for sure.
[3079.24 → 3080.28] Don't be a stranger.
[3080.68 → 3081.32] Thank you, guys.
[3082.06 → 3083.34] Pleasure to be on the show.
[3090.56 → 3091.20] All right.
[3091.38 → 3092.80] That's our show for this week.
[3093.16 → 3096.94] If you haven't checked out our website, head to practicalai.fm.
[3097.08 → 3100.06] And be sure to connect with us on LinkedIn, X, or Blue Sky.
[3100.34 → 3103.68] You'll see us posting insights related to the latest AI developments.
[3104.02 → 3106.04] And we would love for you to join the conversation.
[3106.22 → 3110.32] Thanks to our partner, Prediction Guard, for providing operational support for the show.
[3110.32 → 3112.66] Check them out at predictionguard.com.
[3113.12 → 3116.68] Also, thanks to Break master Cylinder for the beats and to you for listening.
[3117.04 → 3117.84] That's all for now.
[3118.16 → 3119.86] But you'll hear from us again next week.
