[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[17.46 → 20.04] This episode is brought to you by DigitalOcean.
[20.36 → 25.14] DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.14 → 36.82] They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.08 → 42.54] DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 → 46.34] Head to do.co slash Changelog to get started with a $100 credit.
[46.72 → 48.80] Again, do.co slash Changelog.
[55.14 → 66.00] Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[66.44 → 70.40] This is where conversations around AI, machine learning, and data science happen.
[70.80 → 75.42] Join the community and Slack with us around various topics of the show at Changelog.com slash community.
[75.64 → 76.76] And follow us on Twitter.
[76.90 → 78.56] We're at Practical AI FM.
[78.80 → 80.26] Okay, take it away, guys.
[80.26 → 87.68] Welcome to another episode of the Practical AI Podcast.
[88.08 → 89.44] This is Chris Benson speaking.
[89.62 → 92.02] I'm a principal AI strategist at Lockheed Martin.
[92.62 → 98.34] And with me, as always, is my co-host, Daniel Whiten ack, who is a data scientist with SIL International.
[98.82 → 99.68] How's it going today, Daniel?
[100.04 → 100.92] It's going great.
[101.16 → 107.80] I've already been a busy Monday with a lot of prep for training stuff that I'm doing.
[107.80 → 111.50] And, you know, also training people and training models.
[111.62 → 112.82] That's been my day so far.
[113.10 → 114.46] So that's a pretty good day, I guess.
[115.02 → 115.72] I'm not surprised.
[115.86 → 119.64] You are a ferociously busy person, as I have known.
[119.86 → 123.26] Between your classes and your day job and the podcast.
[123.70 → 126.36] And I know your wife has a business which you help out in.
[126.74 → 128.90] Yeah, it's actually over the weekend.
[128.90 → 138.92] We were rearranging stuff in her factory there to make sure when some essential people come back that they're six feet away and all that good stuff.
[139.08 → 143.90] So, yeah, it's been a range of things over these weeks, which makes things interesting, that's for sure.
[144.54 → 144.84] Gotcha.
[145.06 → 146.74] Well, I'm here in Atlanta, Georgia.
[146.74 → 150.62] And we have officially opened up from sheltering in place.
[150.74 → 152.82] But I am more cautious than that.
[152.88 → 155.28] And I expect we're going to keep doing it for quite some time.
[155.38 → 160.16] But I'm looking with envy at neighbours who are having parties and stuff at this point.
[160.18 → 161.54] So I'm afraid to go over.
[161.76 → 162.26] But we'll see.
[162.48 → 164.52] So hopefully everyone stays well.
[165.02 → 171.62] So, you know, I wanted to talk a little bit today about AI for good topics and adjacent.
[171.88 → 172.16] Good timing.
[172.46 → 173.26] This is great stuff.
[173.26 → 174.02] I know.
[174.16 → 176.38] And we have a pretty awesome guest for that.
[176.72 → 181.92] With us today is Chandler McCann, who is the General Manager of Data Robot for Federal.
[182.48 → 184.36] And Chandler, welcome to the show.
[184.88 → 186.10] Hey, thanks, Chris and Daniel.
[186.20 → 186.92] Thanks for having me.
[187.00 → 187.58] Great to be here.
[188.06 → 198.70] I was wondering if you could give us a little bit of background about yourself and how you came to be General Manager at Data Robot and your background before we dive into the topic today.
[199.28 → 199.98] Sure, sure.
[200.04 → 200.52] I would love to.
[200.52 → 205.60] So about myself, you know, like a lot of data scientists, I'm a recovering engineer.
[205.94 → 215.34] So my undergrad was in material science engineering and spent a few years in the flash and DRAM manufacturing space as an engineer.
[215.52 → 220.82] And then from there kind of flowed into statistical consulting, largely focused on the Department of Defence.
[220.82 → 227.50] And that's where I really kind of fell in love with data science and got exposed to more modern machine learning techniques.
[228.00 → 231.02] And after that, you know, pursued my master's at Berkeley.
[231.02 → 235.96] And during that time, became an employee of, at that point, a fairly young data robot.
[235.96 → 241.38] And by the time at Data Robot began as a customer-facing data scientist.
[242.02 → 249.50] And over the course of the years, have evolved to lead various teams, including the AI for Good program, which I still oversee.
[249.88 → 252.86] And now our federal practice today.
[252.86 → 261.88] And I know, so just in terms of Data Robot and the world you live in, I know when I was starting out in data science, it was definitely very much the Wild West.
[262.02 → 269.34] There wasn't a lot of, you know, platforms or systems to manage your data science work and other things.
[269.34 → 279.78] And I remember distinctly kind of going to conferences frequently, but then there was like a certain year when I remember there's all these companies sort of popping up in this space.
[279.90 → 287.22] Data Robot was one of those early ones that I remember popping up and just kind of being consistently present in the data science world.
[287.40 → 292.26] Maybe just mention kind of the premise behind how Data Robot got started and what you do.
[292.26 → 300.54] Sure. Yeah. So Data Robot, and I actually found Data Robot through one of those conferences at Strata in 2016.
[300.96 → 301.76] That's a funny story.
[301.96 → 311.58] But, you know, Data Robot was born from our co-founders, Jeremy H. and Tom Deadly, who were early Hagglers in addition to working in the insurance space.
[311.76 → 316.02] But, you know, during their Kaggle days, they realized that they could benefit from automation.
[316.02 → 321.94] They could automate a lot of the tasks that data scientists were doing, not to replace them, but to just streamline the workflow.
[322.26 → 327.52] So, you know, following some funding, Data Robot and automated machine learning were born.
[327.92 → 330.22] So today, you know, that was back in 2012.
[330.98 → 334.90] Today, Data Robot is a full end-to-end enterprise AI platform.
[335.16 → 343.34] And that means really going from the whole value chain of data, from I have an idea and, you know, raw unstructured data set,
[343.34 → 349.66] all the way through model building and monitoring and deployment and even consumption into automated applications,
[349.98 → 354.62] Data Robot provides a very high level of automation all the way across the spectrum.
[354.62 → 357.12] So it's been a lot of fun to be part of that ride.
[357.12 → 359.26] And what do you see?
[359.38 → 367.22] I'm kind of curious as to what you see about the receptivity of data scientists and AI people towards automation,
[367.22 → 376.86] maybe now, as opposed to like, like when you joined in 2016, it seems like, you know, there has been a shift that I've sort of observed.
[376.86 → 380.58] But I was wondering, you know, what are your conversations about automation?
[380.58 → 389.40] How do they typically go down when you're talking to a data science team or to even a software engineering and data science team combined?
[389.62 → 394.64] What's the feeling about automation these days and what should be automated, maybe what shouldn't be automated?
[395.44 → 396.60] Yeah, that's a great question.
[396.94 → 398.70] I think, to your point, it's definitely shifted.
[399.12 → 408.28] You know, I think there was more resistance earlier, 2016, 2017 phase where there weren't that many full-on enterprise AutoML platforms.
[408.28 → 413.24] But I don't think the world's ever really looked back from automation, right?
[413.28 → 419.06] If you look at anything from iPods to digital cameras, it's hard to reverse that.
[419.32 → 425.36] And I think data scientists are kind of coming to grips with this is not something that's replacing me, but it's something that's augmenting my workflow.
[425.36 → 440.52] So while, you know, Data Robot certainly has a complete GUI-based platform for our users to do or to work within for our advanced data scientists, they mainly interact with our API in Python or R.
[440.84 → 447.10] And that just scales a data scientist in a way that's just not feasibly tractable otherwise, right?
[447.10 → 459.98] So a data scientist can quite comfortably build, manage, and deploy, you know, potentially thousands of models by themselves in a way that, you know, manages risk and is still interpretable.
[460.22 → 462.66] So I think that's appealing to most data scientists that get it.
[462.66 → 475.16] So I had noticed that prior to you moving into the federal practice that you had been a practitioner and probably still are a practitioner, you know, as a data scientist and kind of built-up your career that way.
[475.30 → 480.92] I'm kind of curious as you get into federal, you know, what have you discovered about that?
[480.96 → 484.24] And I'm obviously working for Lockheed Martin, I have an interest in federal.
[484.38 → 486.90] So I was just curious about your perspective as you've moved into that role.
[486.90 → 491.00] Yeah, I mean, I think within the federal space, there's a lot of opportunity.
[491.50 → 503.24] And I'm intrigued by helping the federal government and, you know, particularly Department of Defence leverage automation in a way that, you know, kind of unlocks the potential AI and organization.
[503.48 → 507.62] I think a bottleneck has been the ability to get human talent, right?
[507.76 → 513.90] So acquiring data science talent has been historically really competitive, and that can be a challenge for the government.
[513.90 → 517.62] So tools like Data Robot really help up-level an organization.
[518.36 → 520.84] So that's one way I see it as helping a lot.
[521.02 → 526.14] And two, it's just being able to solve problems that were typically very hard and intractable before.
[526.38 → 536.24] So, you know, Data Robot, in addition to just, you know, time series and classification regression, also handles visual AI problems now and computer vision issues.
[536.24 → 541.88] So being able to bring that to fair in the broader marketplace in the federal government, it's been fun to watch.
[541.88 → 553.50] And how does someone working on the sort of this sort of federal problems at Data Robot, how do you get routed to this sort of AI for good effort?
[553.64 → 559.10] Is that something that, you know, was a specific passion for you or kind of came up unexpectedly?
[559.52 → 560.52] Or how did that happen?
[560.56 → 562.14] And what's the story behind that initiative?
[562.14 → 563.90] Yeah, that's a great question.
[564.10 → 569.18] So when I joined Data Robot, I was working largely on the commercial team at that time.
[569.58 → 576.92] And I had had a relationship with the Global Water Challenge, which is a nonprofit based here in DC.
[577.24 → 578.64] I'd met them when I was at Berkeley.
[579.08 → 585.56] And their mission is to help invest and manage investments in large-scale water projects across the developing world.
[585.56 → 592.86] And so at Data Robot, I brought them on and talked to my CEO, Jeremy, about bringing them on as a pro bono customer.
[592.86 → 594.70] And he was very supportive of that.
[595.44 → 601.68] And, you know, following the work we had done together, the AI for good program was really born.
[601.68 → 619.98] So I remember vividly being on a plane, coming home after a trip to Sierra Leone with Brian Banks, our customer at the Global Water Challenge, and receiving an email from my CEO saying, you know, what if you had a instead of doing this project by yourself, what if you had a team to help you do that?
[620.02 → 620.80] What would that look like?
[620.80 → 632.86] And from there, I was able to kind of take all the lessons learned that gathered from my discussions with Brian about the challenges that nonprofits and NGOs face and build a program around that to address those.
[633.58 → 645.24] And for those who aren't necessarily familiar with the Global Water Challenge, could you kind of talk a little bit about what that is in, you know, in general before we fully dive into how you were interacting with that?
[645.30 → 648.84] Just so that people who haven't heard of it before have a reference point.
[649.24 → 649.58] Sure.
[649.58 → 649.98] Yeah.
[650.08 → 658.80] So the Global Water Challenge is a nonprofit based here in Washington, D.C. with the mission of helping bring water to communities and developing nations.
[659.32 → 666.68] So roughly one in four people around the world are dependent on nontraditional water sources like hand pumps or wells.
[667.26 → 672.24] And the Global Water Challenge sets out to help direct investment to countries in need.
[672.24 → 677.60] And so is that investment, are those projects seeking to like to upgrade those water systems?
[677.60 → 686.76] Or just when you say it's not available, I guess what I'm trying to work through is it sounds like part of it is maybe clean water and good sources and part of it is just access at all?
[686.82 → 688.62] Or what sort of projects do they work on?
[689.10 → 689.30] Yeah.
[689.30 → 689.74] Yeah.
[689.74 → 698.36] They have a wide portfolio, but the ones that we've been focusing on with Data Robot have been around typically new construction and rehabilitation of water points.
[698.36 → 702.96] So, for example, you have a community that may not have an infrastructure for running water.
[702.96 → 710.80] So they may look to direct investment to drill new wells or repair new pumps for people in these communities.
[710.80 → 721.74] So you'll have villages that don't have access to water, and they will help direct investment with other NGOs or large corporations to either drill or build new water points.
[721.74 → 722.58] Yeah.
[722.58 → 722.68] Yeah.
[722.68 → 722.90] Yeah.
[722.90 → 732.80] And I guess this problem has probably become increasingly evident even more so over these recent times because I guess, you know, of course, disease spreads in various ways.
[732.80 → 746.68] But if people aren't able to access water and, you know, for cleaning and all of those things, then I'm sure it further exacerbates many things related to disease spread and health and a lot of different things.
[746.68 → 776.66] Yeah, absolutely.
[776.68 → 777.84] What is their focus on data?
[778.30 → 785.42] So around the world, there are, you know, hundreds of thousands of these water points, but there is no centralized repository.
[786.04 → 793.50] And Brian from the Global Water Challenge set out to build the first standardized and normalized database for water points around the world.
[801.16 → 806.34] We deserve a better internet and the Brave team has the recipe for bringing it to us.
[806.34 → 807.48] Start with Google Chrome.
[807.72 → 811.44] Keep the extensions, the dev tools, and the rendering engine that make Chrome great.
[811.62 → 812.50] Rip out the Google bits.
[812.64 → 813.30] We don't need them.
[813.64 → 816.14] Mix in ad and tracker blocking by default.
[816.42 → 823.82] Quick access to the Tor network for true private browsing and an opt-in reward system so you can get paid to view privacy-respecting ads.
[824.04 → 827.78] Then turn around and use those rewards to support your favourite web creators like us.
[828.12 → 832.68] Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[832.68 → 844.24] So Chandler, I'm interested.
[844.48 → 850.12] You just started talking about the focus of data that Global Water Challenge has.
[850.12 → 859.84] I assume that that focus on data and the data that they've gathered in this repository is central to the solution that you built for them.
[860.30 → 863.38] But I was wondering if you could maybe describe that data a little bit more.
[863.46 → 864.34] What does it represent?
[864.68 → 866.16] What is the scale of it?
[866.22 → 868.98] And what sort of information is included in that data?
[869.64 → 870.02] Absolutely.
[870.02 → 880.48] So the Global Water Challenge and Brian Banks, the person driving this project, they set out to build a standardized database of water points around the world.
[881.12 → 885.50] And the reason they did this was because the water points kept breaking, right?
[885.62 → 893.88] So around the world, after a few years of being installed and having such a positive impact on the community, these water points would break.
[893.96 → 897.72] And they had kind of no idea what was going on and why.
[897.72 → 904.32] When you say water point, you're meaning like a tap or a water main or a well, or what's included in these?
[904.84 → 905.36] Sure. Yeah.
[905.54 → 919.84] Typically, so when I say a water point, these can refer to a few things that they generally fall in the categories of a well or a tap or a rain harvesting system where they can either get groundwater or purified rainwater.
[919.84 → 928.02] Gotcha. And so this repository includes information about where those are at or what sort of information is included about those water points?
[928.82 → 929.84] Exactly. Yes.
[929.96 → 939.76] So as I was saying before, the challenge we were trying to solve was why do these water points, either wells or taps or rain harvesting systems, break?
[939.76 → 945.98] So the data set that he set to normalize includes things around the location of the water point.
[946.50 → 952.12] So there's cell phone applications that can take a picture, capture a lot of long and geolocation.
[952.66 → 954.96] So there's also image data to some degree.
[954.96 → 960.02] Then there's information on the source of the water as well as technology.
[960.40 → 964.96] So whether it's coming from a river or groundwater or if it's a tap stand itself or a pump.
[965.58 → 973.72] And then it's got information about the country and region it's in, as well as the installation year, who installed it.
[974.10 → 978.60] And then some interesting factors such as are the communities paying for it?
[978.60 → 984.42] And is there a management structure in place in the community to maintain the well or water point itself?
[984.98 → 993.90] So I'm curious what kind of solution, you know, as you got involved in this, what kind of solutions you had envisioned that might be able to help them?
[994.30 → 999.20] What was the motivation for you to get involved and for them to work with you?
[999.22 → 1000.16] I think you said it was Brian.
[1000.34 → 1004.76] So kind of how did that get going, and what was the vision that ended up being implemented?
[1004.96 → 1005.86] Where did that come from?
[1005.92 → 1006.74] How did it start?
[1006.74 → 1009.42] What was the collaboration that got all that going?
[1010.14 → 1010.32] Yeah.
[1010.44 → 1014.72] So the vision when we started working with Brian was really his.
[1014.94 → 1017.58] So he had had a vision for this data from day one.
[1017.84 → 1025.46] And as the person who built the database, he knew they could do something with the data, but he wasn't sure just exactly what that looked like.
[1026.26 → 1034.52] Aspirationally, they wanted to be able to predict which water points were going to break in the future or at least understand which ones were going to break.
[1034.52 → 1040.72] And in parallel, they also wanted to understand if they could identify a priority to these water points.
[1040.72 → 1042.86] So which communities are not being served?
[1043.16 → 1046.24] Where would it make sense to build or construct new water points?
[1046.24 → 1050.84] Because it's non-trivial to set up construction of these things in a developing nation.
[1050.84 → 1061.68] And for me, the appeal was, wow, there is this relatively clean data set on a fascinating problem that's out there with the potential for a huge impact.
[1062.14 → 1063.50] So that's what drew me to it.
[1063.84 → 1074.22] And our main focus when we set out was, can we, given data on which water points have broken in the past, can we predict which water points are going to break at some point in time in the future?
[1074.22 → 1079.54] Gotcha. And so, yeah, it seems like there's really a lot to tackle there.
[1079.98 → 1083.24] Non-profits, I'm guessing, typically have resource constraints.
[1083.50 → 1087.94] And so being able to understand where they should put their investment is definitely important.
[1088.32 → 1095.62] But for this particular first project in terms of predicting where a water point is going to break,
[1095.96 → 1103.58] what is the sort of, like, out of all water points in the database, how many are breaking on any given point?
[1103.58 → 1105.44] Like, what's the distribution like here?
[1105.50 → 1110.10] Is this something that happens fairly rarely, or it's something that happens, like, all the time?
[1110.50 → 1115.42] Is it more compared to something like fraud detection where you're trying to detect something that happens rarely?
[1115.60 → 1117.40] Or what's the situation like on that front?
[1117.88 → 1118.60] Sure, sure.
[1118.74 → 1121.30] Yeah, it's more frequent than fraud, unfortunately.
[1121.52 → 1129.46] So the distribution of things that are broken is around 25%, you know, on average compared to 75% functioning.
[1130.14 → 1130.24] Gotcha.
[1130.24 → 1136.50] Gotcha. And that's due to just the, you know, obviously what Global Water Challenge is trying to address,
[1136.58 → 1141.16] just the old systems and systems that aren't being maintained and that sort of thing?
[1141.74 → 1148.00] Yeah, there are a slew of potential reasons, some of which could be maintenance, some of which could be environmental.
[1148.00 → 1151.52] You know, perhaps a water point wasn't dug deep enough.
[1151.70 → 1157.88] So you have a well that becomes dried out, you know, six months out of the year during the dry season.
[1157.88 → 1159.32] So that could have an impact.
[1159.64 → 1166.42] So there are geographical inputs, there are community-based inputs, as well as maintenance-based, you know, kind of failure modes that are out there.
[1167.04 → 1167.16] Gotcha.
[1167.16 → 1177.02] Gotcha. And so when you first saw this data and what was included in it, where did your mind go in terms of, you know, an approach that you could take to solving this?
[1177.44 → 1188.38] So when I first saw the data set, I was at one time impressed by how standardized it was, but at the same time digging into it, realized there were a lot of nuances and challenges.
[1188.38 → 1199.46] And I'm sure, Daniel, working with nonprofit data yourself, you have been exposed to this, but whenever you're dealing with human data collection, there are always some challenges that are out there.
[1199.60 → 1206.40] And one of which on our side, a big one, was the ability to enter free-form text for the same thing.
[1207.36 → 1214.38] So there are obviously a few key pieces of data to solve this problem, particularly what type of technology is it?
[1214.44 → 1217.22] So is it a pump? What brand of pump is it, for example?
[1217.22 → 1218.76] Those things all matter.
[1219.28 → 1230.78] And when we started looking at the data set, there was roughly 1,600, you know, unique values for the type of technology when we knew that it really boiled down to about 12 or 14.
[1231.46 → 1239.96] So one of the first problems that we tackled with that was, you know, just some basic natural language processing to try to match categories together.
[1240.56 → 1244.80] And that was something that we had done by hand originally.
[1244.80 → 1251.80] And today we're actually automating that process now through the use of Pax Auto, which is our automated data prep tool.
[1251.94 → 1260.80] So that's been kind of a big step forward as we move from this sort of, you know, version 1.0 of the solution to kind of version 2.0 in the future.
[1260.80 → 1264.78] So, you know, back to your original question.
[1265.32 → 1268.14] My first thought was we need to kind of organize and clean the data.
[1268.40 → 1272.60] And the second one is how do we frame this to make it a useful problem, you know, down the road?
[1272.60 → 1277.18] And so we had to identify what variables would be really important to this.
[1277.36 → 1287.06] And a couple of things jump out that are available to us, namely location, the age of the water point, as well as technology and the source and the community interaction with it.
[1287.48 → 1289.54] So from there, we built our first predictive model.
[1289.54 → 1302.24] Gotcha. And you did mention the sort of problems with data and like in the nonprofit world and people sort of humans gathering this data, which I guess isn't also specific to the nonprofit world.
[1302.24 → 1306.70] But I know like for us, a lot of times it's hard, especially in developing countries.
[1306.70 → 1316.76] You know, you wonder about like if I want this data, but it was the only access I have to that type of data was data that was gathered, you know, four years ago or something.
[1316.92 → 1319.68] You wonder about, you know, what's updated since then.
[1320.02 → 1322.92] So in this case, like how is this data being generated?
[1322.92 → 1328.54] Is it people just going out into the field and like marking down where the water points and that sort of thing are?
[1328.74 → 1331.26] Are there actual instrumentation on some of this stuff?
[1331.72 → 1334.86] Yeah, that's a fantastic and very important question.
[1335.04 → 1336.16] And it was subtle in the data.
[1336.16 → 1340.14] So that was one of the first things I asked Brian is how does this data come about?
[1340.56 → 1342.28] And there are a couple of different ways.
[1342.28 → 1347.10] One way is from large national efforts like national assessments.
[1348.00 → 1351.96] And this is something that we came across in countries like Swaziland and Sierra Leone.
[1352.32 → 1358.66] But also you have manual input by smaller groups like local NGOs or local nonprofits.
[1358.98 → 1360.16] They're uploading it.
[1360.16 → 1367.64] So what kind of was the magic behind Brian's idea was he was going to build a standardized way of capturing this information.
[1368.28 → 1374.40] So no matter how they were keeping their own records, they had a common format to upload it in that maintained these key fields.
[1374.40 → 1378.06] I'm curious as some of that data was coming in.
[1378.22 → 1381.40] You know, we talked a bit here so far about the textual data.
[1381.56 → 1386.24] I remember earlier in the conversation, you mentioned something about images as well.
[1386.34 → 1388.66] Did you have a mixture of different types of data?
[1388.78 → 1392.74] Like was imagery used as input or did it mostly text oriented?
[1392.74 → 1396.54] Yeah, so the image data has always been there.
[1396.88 → 1402.28] So there's, you know, S3 buckets or Dropbox files that are storing this image data.
[1402.50 → 1409.08] But we really haven't leveraged that much until I guess within the last two months or so at Data Robot.
[1409.54 → 1414.98] So at first, our original models were contained by text, numeric and categorical data.
[1414.98 → 1428.64] And as we've expanded, we've begun to integrate image data as, like I said, we've released our visual AI platform and Data Robot, which allows us to incorporate images into the modelling, which is something we're currently exploring and is fascinating.
[1428.94 → 1444.48] And in fact, kind of interesting use case from that is, you know, if I have an image that's uploaded, but perhaps someone forgot to fill out the field of the technology, can we train a classifier to say that this image is actually a hand pump, or it's a rain stand?
[1444.48 → 1451.66] So can we use, you know, image analysis as an intermediate step into, you know, data augmentation and cleaning?
[1452.22 → 1473.88] Yeah, so on that front, you know, at least in, let's say, version one of what you did in predicting these water point failures, after you had done some of this NLP and you started getting into thinking about how to predict these failures, what ended up being a good way to do that or a way that you found out how to do that?
[1473.88 → 1479.64] And what portions of the data ended up being good predictors of that behaviour?
[1480.34 → 1482.50] So we're looking at the problem.
[1482.62 → 1487.06] We realized that there was some country to country variation, but some common things popped out.
[1487.26 → 1494.10] So the data that was turned out to be the most predictive kind of across the board was the age of the water point.
[1494.10 → 1503.26] So certainly its function over time was certainly dependent on there was a strong relationship to how old it was, who installed it.
[1503.66 → 1513.36] So whether it was from a private government or sometimes a nonprofit was also predictive in certain areas, as well as also strong local effects.
[1513.36 → 1518.90] So we saw things like, you know, the region of the water point having a relationship to life.
[1518.98 → 1526.80] So places that were far away from, say, the large city in that country may have low access to parts.
[1527.54 → 1532.52] And in some places, you know, they would tend to have a shorter life, all else being equal.
[1533.12 → 1535.42] So those were some of the things that kind of jumped out at us.
[1535.42 → 1558.44] I'm kind of curious, as you were engaging in this process and recognizing some of these constraints that you've talked about, was this particular engagement, you know, in this kind of AI for good charitable approach, was it more or less the same as other data science projects in terms of you're still getting data, and you're doing the normal prepping the data and running it through your model?
[1558.44 → 1568.24] Or was there anything in your mind that distinguished it as something unto itself, something a bit different from your typical business scenario that you might otherwise be engaged in?
[1568.48 → 1574.68] I was kind of curious if they were essentially all the same or if there was something that made that stick out from a process standpoint.
[1575.50 → 1582.62] Yeah. So when we began engaging with the Global Water Challenge, we were just treating them like a regular customer.
[1583.00 → 1585.94] You know, there was no AI for good program formally at that time.
[1585.94 → 1588.30] They were just being treated like a regular customer.
[1588.44 → 1596.48] And our job at Data Robot at the time as customer-facing data scientists was to enable them to own their own solutions, right?
[1596.54 → 1599.48] So that involved kind of teaching them how to fish, right?
[1599.48 → 1612.94] Working with Brian to help frame his problem better, understand the data with him, and then talking through all the blind spots and gaps in the modelling process that would come up along the way, along with helping him interpret his model.
[1612.94 → 1616.98] So in that sense, it wasn't unique from a process perspective.
[1616.98 → 1623.48] But it was unique in sort of the level of access to the data that I could get with clients.
[1623.48 → 1628.66] So with Brian's data, you know, it was a side-by-side partnership.
[1629.34 → 1630.84] Everything was available to me.
[1630.92 → 1638.84] And obviously, there can be restrictions when you're dealing with, you know, certain private companies when it comes to the level of access to the data you can get.
[1639.22 → 1640.14] So that was nuanced.
[1640.14 → 1656.40] But I think the takeaway for me and what really helped us when we built the AI for Good program was that, you know, if we treat these nonprofits just using the same process we do with our customers, they can own and build these solutions over time themselves.
[1656.98 → 1658.86] And that was something that was really inspiring to me.
[1658.86 → 1666.08] What's up?
[1666.18 → 1673.90] This is Daniel Whiten ack, one of your Practical AI co-hosts, and I hope you're enjoying this episode and staying healthy during these crazy times.
[1674.44 → 1687.30] I'm working on some pretty cool AI stuff here from my home office, but I've also found that I'm having to get a bit creative and be intentional when it comes to honing my AI skills and virtually connecting with the AI community.
[1687.30 → 1699.70] If you're in a similar situation, or you've been inspired by the practical AI we talk about on this show, I want to invite you to a live online AI training event I'm hosting this May called AI Classroom.
[1700.04 → 1707.54] In AI Classroom, I'm going to teach you the practical skills I've learned over the years using the latest open-source AI technology.
[1707.84 → 1713.68] You'll learn AI theory along with practical hands-on implementations in both PyTorch and TensorFlow.
[1713.68 → 1729.30] And after the training, you'll be able to understand the latest AI models, implement your own models in code, train computer vision and NLP models, create model inference servers, and experiment with state-of-the-art methods like reinforcement learning.
[1729.96 → 1732.34] AI Classroom is taking place this May.
[1732.74 → 1739.32] It'll be taking place live and completely online in a high-quality virtual classroom, so no travel is required.
[1739.32 → 1744.54] There'll also be two cohorts with convenient time zones for Eastern and Western hemispheres.
[1745.08 → 1750.30] Don't miss out. Tickets and more information are available at datadan.io.
[1750.80 → 1752.54] That's datadan.io.
[1752.96 → 1758.60] And practical AI listeners can use the code practicalAI10 for 10% off.
[1758.84 → 1760.94] See you online in AI Classroom.
[1760.94 → 1784.40] As we get into, I guess, you know, how this inspired, you know, more AI for good efforts at Data Robot and also, like, your learnings from how to work with a nonprofit and that sort of thing,
[1784.40 → 1794.82] I would love to hear about, like, I guess, where this project ended up in terms of, you know, positive or negative results and then how that inspired further work.
[1794.88 → 1796.94] It sounds like things have expanded past that.
[1797.10 → 1798.76] So I'd love to hear about that story.
[1799.36 → 1803.66] So where it ended up with the Global Water Challenge was fascinating.
[1803.92 → 1806.14] And to be fair, it's still an ongoing story.
[1806.14 → 1812.40] So during, I guess, 2019, we were able to go to both Sierra Leone and Liberia.
[1812.54 → 1814.96] First, just with Data Robot to Sierra Leone.
[1815.08 → 1822.98] And the second time to Liberia on behalf of the State Department, where I was asked to be a part of the Water Expert Program.
[1823.30 → 1827.98] And I went with GWC to participate in a water data workshop in Liberia.
[1828.56 → 1828.96] That's great.
[1829.44 → 1830.38] It was very cool.
[1830.38 → 1839.40] And it was just an awesome experience from both, you know, data science perspective, where I'm working over here, I'm pulling data, you know, out of a table,
[1839.68 → 1844.54] to actually going on the ground and meeting the people who are collecting it and having conversations with them
[1844.54 → 1852.50] and trying to communicate the power of machine learning and the importance of the data they were collecting and how it could be used.
[1852.70 → 1857.34] It was just, you know, a humbling and awesome experience all wrapped up into one.
[1857.34 → 1864.20] So following those two trips, we had very positive relationships with the government in Sierra Leone.
[1864.64 → 1869.82] And in 2019, the Ministry of Water, you know, kind of reaffirmed their commitment to evidence-based decision
[1869.82 → 1876.54] and actually passed a national policy requiring the use of data and decisions about water services, which is pretty cool.
[1876.60 → 1878.88] I mean, and also, again, humbling.
[1879.14 → 1885.90] If you think about it, I think the story of this project is the story of the power of data and what it can do.
[1885.90 → 1895.12] And if you think about it, in 2018, you know, the use of data at the national level in Sierra Leone to kind of inform decision-making by policymakers,
[1895.70 → 1899.04] again, with very constrained budgets, was very low.
[1899.38 → 1903.84] And then in 2019, we do know that working with the Ministry of Water,
[1903.96 → 1910.52] they're able to use some of the insights from our tool to inform decision-making and budgeting that year.
[1910.52 → 1916.36] So that was definitely, you know, exciting and a near-term win for us in the project.
[1916.98 → 1926.68] And that helped kind of shift things out of this R&D phase to where Brian and the Global Water Challenge are in the process of pursuing more funding.
[1926.90 → 1929.02] And if you want to contribute, feel free to them.
[1929.26 → 1935.36] But we're looking to build a much more sustainable tool that can be deployed to many countries around the world.
[1935.48 → 1937.64] So it kind of was the launching point for the project.
[1937.64 → 1940.22] Yeah, that's a super cool story.
[1940.32 → 1947.86] And I just wanted to note to listeners that Data Robot, on its AI for Good Page, has a video of you and Brian doing this work together.
[1948.22 → 1950.80] And I wanted to call that out, and we'll include it in the show notes.
[1951.02 → 1957.82] It's just a few minutes long, and I would urge anyone to take a look at it just to kind of, you know, get the imagery of what you went through.
[1957.82 → 1964.42] I think you surprised me a second ago when you were talking about, you know, being able to shift national policy.
[1964.56 → 1973.24] That intrigues me because we have the privilege of talking to people that engage in AI for Good on a fairly regular basis and hear about cool projects.
[1973.24 → 1981.42] But most of them don't change a country's policy towards evidence-based action, you know, from the work they've done.
[1981.42 → 1995.02] And I kind of wanted to get a sense of how did that feel when you realized that not only had you had the specific impact that you had on by providing the service that you walked into the engagement with,
[1995.06 → 2005.98] but when you realized as well that you were actually changing the way a country was thinking about using data to affect good for its population, what was that like?
[2006.20 → 2008.52] I'll let you answer that, and then I have another follow-up.
[2008.52 → 2023.24] Yeah, I remember getting the email saying that they were leveraging the insights from, you know, our models and even the simple data visualizations was a huge leap ahead for them, right?
[2023.44 → 2031.46] And I remember hearing that and being told that it was being used to inform the budgeting process for the following year, and I was just floored.
[2031.46 → 2039.74] And that made me, you know, a little, I don't know if scared is the right word, but I was just like, wow, I did not realize this was going to be happening so quickly.
[2040.14 → 2046.00] But at the same time, it was just another proof point that people were starving for information, right?
[2046.04 → 2057.18] You have people that are trying to make decisions that impact a lot of people in their citizen base, and, you know, the ability to just synthesize a little bit of information can go such a long way.
[2057.18 → 2066.60] So I think we're just on the front end of the wave when it comes to the way to leverage data, you know, across these developing nations for water policy.
[2066.60 → 2070.32] Yeah, just to interject there, I totally echo what you're saying.
[2070.72 → 2084.92] And I know that like, some of the proof of concepts that we've done around like dialogue systems and chat interfaces in emerging markets, to be honest, like the interface has not been that great, like it probably wouldn't fly in the US.
[2084.92 → 2093.60] But people are so hungry for information, accurate, good information in certain contexts that, to some degree, that doesn't matter.
[2093.70 → 2095.98] Although we, of course, strive for good interfaces.
[2096.38 → 2109.06] But yeah, I totally resonate with what you're saying that, yeah, it just can be so powerful to be in these situations where you're creating something that allows a new view onto information that people are so hungry for.
[2109.22 → 2110.64] So yeah, it's really cool.
[2110.86 → 2112.32] Chris, did you have a follow-up?
[2112.32 → 2116.72] Yeah, I was just, I wanted to actually reference another thing, you know, that you had done.
[2116.82 → 2122.70] And that was, I know you have a blog post called Why Most Tech for Good Campaigns Fail and How We Can Fix Them.
[2123.18 → 2129.56] And I was wondering if you could kind of address those steps that you take us through and why that works.
[2129.56 → 2143.38] But also, you know, if you have any thoughts about how, you know, people or organizations like yours that are trying to do this AI for good projects might be able to influence or impact policy going forward.
[2143.50 → 2145.26] I know it kind of surprised you in this case.
[2145.26 → 2154.22] But if you have any thoughts toward even how to extend this so that you think you might get systemic change for the long term and how a government thinks about this.
[2154.22 → 2156.64] I'd love to know that what your advice is in general.
[2157.38 → 2157.74] Sure. Yeah.
[2157.80 → 2158.40] So two parts.
[2158.46 → 2166.36] How do we, you know, look at delivering this in the most effective way for nonprofits and then, you know, for companies interested in this space?
[2166.36 → 2170.00] How do they think about potentially impacting policy?
[2170.14 → 2171.44] I mean, I'll tackle the first one.
[2171.64 → 2181.38] So when it comes to why we were observing a lot of these tech for good initiatives, and I hate to say failing, but just not delivering the results they intended.
[2182.02 → 2191.62] A lot of that was just based off experience from Brian and what we heard and his just life at the Global Water Challenge and his exposure to people in the sector.
[2191.62 → 2199.98] So the big idea is that you need to partner with these nonprofits and NGOs and help them build solutions that they can maintain.
[2200.26 → 2211.62] So hackathons are all well-intentioned, but it's probably not realistic to expect a small nonprofit without a big data science team to maintain a code base over time.
[2212.60 → 2212.74] Right.
[2212.96 → 2218.64] So like even if they build an app, you know, models to get stale, models need to be refreshed.
[2218.64 → 2228.70] So our idea was, you know, we happen to have the benefit of, you know, a very powerful enterprise AI platform behind us, but just help them understand how to think through their problems.
[2228.70 → 2229.10] Right.
[2229.12 → 2233.22] So how do we appropriately identify use cases that matter to them?
[2233.58 → 2234.86] How do we frame them?
[2235.28 → 2238.72] How do we think about sort of the ethical considerations for what we're doing?
[2239.38 → 2242.08] You know, how do we think about acquiring data for it appropriately?
[2242.08 → 2246.30] And then how do we go through the iterative model building process?
[2246.58 → 2250.96] And then, you know, how do we deploy things in a way that are useful to people?
[2251.36 → 2259.14] So the truth with data is that I'm of the opinion that value really isn't realized until it's consumed by somebody.
[2259.34 → 2259.54] Right.
[2259.90 → 2269.62] So we can build models to a blue in the face, but until someone's doing something with it, it may not be super useful outside of perhaps, you know, insights,
[2269.62 → 2272.00] which I would still argue is still consumption.
[2273.00 → 2286.66] So, you know, our process is structured to, you know, within the AI for Good program today, help nonprofits go from this is my big vision to how do we deconstruct this to, you know, a machine learning problem.
[2286.66 → 2298.28] And then how do we go from this is my idea to this is my deployed model in a structured way and then teach them how to learn the process, you know, through each of those tollgates.
[2299.52 → 2303.20] Yeah, it sounds like good advice for really any data science program.
[2304.04 → 2306.36] In my opinion, a lot of those things ring true.
[2306.36 → 2307.36] Yeah.
[2307.74 → 2316.60] On the second part on the policy side, I hope that more companies continue to provide resources to nonprofits and NGOs.
[2316.90 → 2327.68] I think what's true in this space is that they may be a little bit behind than other private companies when it comes to collecting data and storing it and organizing it.
[2327.68 → 2330.22] But they're coming along and times are changing quickly.
[2330.22 → 2338.48] So the situation where you have a lot of nonprofits with potentially a lot of very rich, interesting data that aren't sure what to do with it, that grows a lot.
[2338.64 → 2342.78] So I would love for other companies to continue to get involved and offer their services.
[2342.78 → 2351.10] And I would just say that, you know, again, we just have to account for the fact that machine learning models are sort of living things that go stale over time.
[2351.10 → 2355.38] And we need to help our end users build solutions that account for that.
[2355.38 → 2363.80] And I'm curious, as we get to a point of sort of closing things out, I know you mentioned earlier, you know, getting that email.
[2363.94 → 2368.68] I think it was asking about, you know, what if you had more people to work with on this initiative?
[2368.90 → 2373.08] Where are things at right now with the AI for Good initiative at Data Robot?
[2373.26 → 2376.06] And what are things you're looking at in the future?
[2376.86 → 2378.70] Yeah, so that was very exciting.
[2378.70 → 2383.94] And I can't thank Jeremy and team enough for supporting us to build out this vision.
[2384.60 → 2389.66] But June of last year, we sort of launched our program and opened up our application process.
[2389.66 → 2397.76] And we actually got applications from 10 countries and five continents, which was pretty exciting for our first year of the program and its inception.
[2398.28 → 2400.10] Since then, we've been working with six nonprofits.
[2400.10 → 2406.68] So Diva, which is obviously a large lending platform in the nonprofit space right now.
[2406.84 → 2411.22] So helping them predict the likelihood of which loans will go unfunded or not.
[2411.78 → 2415.28] Donors Choose, helping provide supplies to teachers and classrooms.
[2415.90 → 2424.08] And it costs your River keeper here in Washington, D.C., helping them forecast E. coli levels in the river, given some sensor data that's being read.
[2424.08 → 2432.46] And two, some very interesting healthcare use cases with the University of California, San Francisco, Spinal Cord, Zuckerberg Spinal Cord Institute.
[2432.78 → 2438.94] So where we're looking at ways to use OR data to help improve outcomes for spinal cord surgery.
[2439.24 → 2452.84] And then finally, working with the University Hospital of Mannheim over in Germany, where we've been forecasting top World Health Organization causes of death, as well as predicting patient mortality given people that come into the hospital.
[2452.84 → 2455.64] So those are some of the use cases we're working on now.
[2455.96 → 2464.28] And we're excited to just continue to broaden the impact that people are working with and keep the program growing.
[2465.12 → 2465.44] Fantastic.
[2465.70 → 2475.18] Well, Chandler, thank you so much for coming on to the show and telling us about Data Robot and the things that you're doing or have done with the Global Water Challenge.
[2475.62 → 2477.70] It was really fascinating and inspiring.
[2477.94 → 2479.22] And thank you for doing that work.
[2479.38 → 2480.30] I really appreciate it.
[2480.62 → 2481.02] Absolutely.
[2481.32 → 2482.38] Thanks for having me on the show.
[2482.38 → 2484.52] Really been fun talking to you.
[2484.64 → 2487.00] And let me know if you guys ever want to catch up again.
[2488.04 → 2488.60] Will do.
[2488.72 → 2489.12] Thank you.
[2492.84 → 2494.98] Thank you for listening to Practical AI.
[2495.44 → 2497.52] We appreciate your time and your attention.
[2498.08 → 2499.64] Next up, let your voice be heard.
[2499.78 → 2501.90] Please leave us a comment on the episode page.
[2501.98 → 2503.90] There's a link in your show notes for easy clickings.
[2504.20 → 2505.10] We'd love to hear from you.
[2505.78 → 2509.08] Word of mouth is the number one way people find new podcasts.
[2509.08 → 2513.14] If Practical AI has helped you on your AI journey, please do tell a friend.
[2513.26 → 2514.50] Hey, they'll thank you later.
[2515.14 → 2519.68] Special thanks to Break master Cylinder for the beats and to our awesome partners for their support.
[2520.06 → 2522.56] Shout out to Vastly, Linde, and Rollbar.
[2522.56 → 2524.46] That's all for now.
[2524.84 → 2526.08] We'll talk to you again next week.
[2526.60 → 2528.98] We'll see you next week.
[2528.98 → 2558.96] Thank you.
