[0.00 --> 8.66]  Welcome to Practical AI.
[9.14 --> 19.56]  If you work in artificial intelligence, aspire to, or are curious how AI-related tech is changing the world, this is the show for you.
[20.22 --> 24.92]  Thank you to our partners at Fly.io, the home of changelog.com.
[24.92 --> 32.38]  Fly transforms containers into micro VMs that run on their hardware in 30 plus regions on six continents.
[32.80 --> 35.44]  So you can launch your app near your users.
[35.84 --> 37.84]  Learn more at Fly.io.
[42.74 --> 48.16]  Welcome to another fully connected episode of the Practical AI podcast.
[48.16 --> 55.86]  This is the episode in which Chris and I keep you fully connected with everything that's happening in the AI world.
[55.98 --> 62.58]  We'll hopefully talk through some of the news and also keep you up to date with some of the latest learning materials.
[63.14 --> 67.06]  I'm Daniel Whitenack. I am CEO and founder at Prediction Guard.
[67.28 --> 74.62]  I'm joined as always by my co-host, Chris Benson, who is a principal AI research engineer at Lockheed Martin.
[74.98 --> 75.68]  How are you doing, Chris?
[75.68 --> 77.34]  Doing well today, Daniel. How's it going?
[77.34 --> 84.58]  Oh, it's going great. My wife and I have been traveling a bit around the UK, which has been enjoyable.
[84.88 --> 99.56]  Other than the train delays and rain and wetness, I think today we saw all of the above of sunshine, rain, hail, snow, the full gamut of things.
[100.50 --> 103.36]  It's amazing how you can have so much weather in one little island.
[103.46 --> 104.44]  Exactly, exactly.
[104.44 --> 104.86]  They do it all.
[105.08 --> 105.46]  Variety.
[105.46 --> 107.00]  Just go a few miles and it changes.
[107.00 --> 108.52]  Yeah, yeah, variety.
[108.86 --> 117.14]  Well, there have definitely been a good variety also of interesting AI things happening, as there always are.
[117.58 --> 127.72]  One of the things that was kind of interesting to me, which was circulating around my feeds, was NVIDIA generally because they had their GTC.
[127.72 --> 139.04]  I always want to say GTX, I always want to say GTX, but I think that's the card GTC event, which is their kind of innovation, a yearly conference sort of thing.
[139.04 --> 151.28]  But Jensen, the CEO, was making some comments.
[151.28 --> 152.84]  And his comment was related to AI, I don't know.
[152.84 --> 164.08]  And his comment was related to, I forget how he phrased it, but basically the gist being kids shouldn't learn to code anymore because AI is going to do that fairly well.
[164.64 --> 165.30]  So I don't know.
[165.30 --> 171.08]  I don't have kids, Chris, but what is your thought as a parent?
[171.26 --> 173.50]  As the designated father on this podcast?
[173.50 --> 173.58]  Yes, exactly.
[173.58 --> 178.16]  Well, I think he's right in the long run.
[178.32 --> 180.54]  I think he mentioned that in the keynote.
[180.72 --> 182.34]  There was a little section where he covered that.
[182.40 --> 187.08]  And he said, always in the past, we've taught our kids they need to code, you know, in recent years.
[187.08 --> 189.38]  And he said, now AI is changing all that.
[189.48 --> 192.50]  And I don't think that's news to anybody in the larger sense.
[192.60 --> 197.40]  You know, we use AI for coding and technical controls and all sorts of stuff all the time.
[197.40 --> 202.10]  And that's just built into our ecosystem over the last few years and is increasing constantly.
[202.10 --> 208.74]  I have to admit that he was kind of like, we're at the moment, you know, and I'm not quoting him, but, you know, he was kind of like, this is the moment.
[208.84 --> 209.76]  We're not teaching him anymore.
[209.82 --> 219.22]  And I'm kind of like, maybe, maybe, because I know that even with us as adopters of AI technology, you know, for coding all the time.
[219.28 --> 222.24]  I mean, if there's anything that we do, it has to do with that.
[222.48 --> 227.38]  And there's all sorts of complexities and bumps in the road and things like that.
[227.46 --> 229.44]  So in the large, is it moving that way?
[229.76 --> 231.72]  Of course, I think everybody would agree with that.
[232.30 --> 237.06]  But I don't think that we've all just arrived there because Jensen just said it in a keynote, personally.
[237.60 --> 238.58]  I have great respect.
[238.72 --> 239.84]  I don't mean to be negative.
[240.00 --> 242.80]  It was like flipping a light switch, kind of the way he put it.
[242.94 --> 246.90]  And I don't think we, I think it's a very, very slow flip with lots of nuance.
[246.90 --> 265.00]  I guess one way to rephrase the question would be, at this moment, were you to have a child going into college, let's say, would you encourage them to pursue software engineering or computer science or this sort of thing?
[265.00 --> 265.68]  I would.
[265.68 --> 274.16]  I think that in the future, and actually I've spent a lot of time thinking about this topic in general, hundreds and hundreds of hours.
[274.16 --> 279.90]  And this is one of those things where I think we're accelerating into the future.
[279.90 --> 289.86]  And I think with AI capabilities year by year making massive changes to how we live and work, humans are going to have to be fairly dynamic in how they do things.
[289.86 --> 295.92]  And one of those skills continues to be various technology, you know, orientations.
[296.18 --> 301.28]  And I don't think that's going away anytime soon, though AI will continue to change where those boundaries are.
[301.50 --> 315.54]  So in the spirit of we're always going to have to learn new things anyway, I don't see any problem in diving into technology and coding today with the recognition that the technology will constantly change underfoot and you're going to have to change with it.
[315.54 --> 325.20]  So I don't think I would recommend, and actually I do, for Georgia State University, I'm one of their advisors in industry for their computer science school.
[325.58 --> 332.14]  And I would not dissuade any of those students from pursuing a computer science curriculum at this time.
[332.56 --> 335.16]  They just need to be dynamic enough to change over the years.
[335.16 --> 359.20]  Yeah, and maybe part of it is also these tasks that, like if you go to a three-week boot camp on front-end engineering or something like that, probably many of the things that you would learn in such a boot camp, even though I think there will be a need for front-end engineers for some time also.
[359.20 --> 360.46]  I think that's true.
[360.46 --> 380.62]  But that sort of basic level that you would get is maybe at the level where it's going to be more and more cookie-cutter sort of things that an AI system is going to be able to do guided by the hand of maybe a less technical person like a designer rather than a front-end engineer.
[380.62 --> 381.22]  Right?
[381.38 --> 388.60]  But I run an AI company, and we really need software engineering and programming.
[389.26 --> 396.70]  So I think at the minimum, all of these AI systems that are coming about are going to need people to build them and maintain them.
[396.82 --> 403.12]  And infrastructure that operates well and scales, systems are still going to have to scale.
[403.12 --> 411.60]  And people are going to have to worry about distributed systems and all of these sorts of things that are really hard engineering problems from my perspective.
[412.28 --> 412.56]  I agree.
[412.76 --> 419.18]  The human-algorithm partnership is going to go a long way for many years, but it will change all the time.
[419.32 --> 422.48]  But that's not limited to our fields here.
[422.66 --> 428.26]  This is something that all industries are going to be facing is that constant change on what the partnership looks like.
[428.26 --> 440.98]  So I'm not inclined, unless somebody sees an area where AI is in the next very few years going to completely take over all human activities in it, I don't see any reason to avoid these things.
[441.10 --> 443.62]  I think we're in a perpetual learning mode going forward.
[443.62 --> 468.92]  Yeah, I've actually been thinking about this sort of dynamic a little bit after we've had a couple of guests on the show that are working on these systems like prompt layer and other ones where they're managing prompts and reasoning workflows at the intersection of domain experts and software engineers.
[468.92 --> 473.26]  So the technical side, kind of where software meets domain expertise.
[473.40 --> 478.36]  I was on a panel at Purdue University speaking of students and that sort of thing.
[478.48 --> 487.78]  And one of the questions was around this, you know, well, hey, I went into this program thinking maybe I would try to become a data scientist.
[488.22 --> 493.08]  Is that still a thing or should I be thinking about something else?
[493.08 --> 505.78]  I think one encouraging thing for people is if you're a data person, no one really has more than a year of experience architecting and building these type of generative AI systems.
[505.98 --> 514.38]  So in a sense, you could do one really compelling project and be ahead of most of the people trying to get these jobs.
[514.48 --> 514.56]  Right.
[514.62 --> 516.68]  So in one respect, that's really encouraging.
[516.68 --> 526.40]  I think it is shifting, though, what a data scientist means and this coming from a data scientist that has been a data scientist for 10 plus years.
[526.80 --> 539.96]  I think there is this kind of hollowing out of the middle where you had the three things where on one side you had software engineering and infrastructure, and that was the land of sort of software engineers and DevOps and all that.
[539.96 --> 551.00]  And on the other side, you had domain experts and in the middle, you had data scientists who kind of translated the domain expertise into predictive models and machine learning and such.
[551.12 --> 555.60]  The thing got handed off on the other side to integrate into software.
[556.18 --> 565.50]  And I think what you see is kind of this hollowing out of that middle where domain experts are getting much closer to the software side.
[565.50 --> 571.12]  And so I think there's kind of two maybe takeaways from that from my perspective.
[571.12 --> 590.74]  Either you could go into the AI engineering side, which is maybe less hardcore infrastructure, low level programming and more almost narrative writing of prompts and creating of these reasoning chains and all of that sort of thing and become amazingly good at that.
[590.74 --> 595.70]  And rely on good software and infrastructure people on the other side.
[596.28 --> 600.98]  Or there's still going to be a need because everything is still software.
[601.38 --> 613.58]  There's still going to be a really heavy need for people that can make your chains of reasoning and hosted models and software deployments actually go well.
[613.98 --> 614.10]  Right.
[614.38 --> 615.04]  Totally agree.
[615.04 --> 619.62]  You said one thing in there as well that really, really resonated with me.
[619.62 --> 620.94]  You said several things that did.
[621.00 --> 628.58]  But one thing that jumped out that I'd like to reiterate is the notion that if you do that one big project, you're really out in front again.
[628.76 --> 639.92]  It's one of those things where because it changes so fast right now from month to month that it doesn't take much to do the new thing that's just coming out.
[640.04 --> 646.70]  And the people that might have had many years of experience in the title haven't had experience in this new thing.
[646.70 --> 648.42]  And that keeps on happening.
[648.90 --> 657.54]  And so the notion of being a title, whatever your title is, for X number of years is really losing a lot of meaning in that.
[657.76 --> 665.50]  And that you might have been in the space, but with the space increasingly evolving, you can kind of catch up into modern experience pretty quick.
[665.50 --> 680.56]  So people are very worried about jobs in this space, but that's a little bit of a way where you can be super competitive and jump up in the area of your interest by leaping into the front and disregarding the traditional metrics that we tend to use on that.
[680.56 --> 699.74]  If you're anything like me, you have a certain tendency to put things off until the very last minute.
[700.06 --> 706.32]  Seeing the dentist, going to the doctor, home improvements, that never ending chore list of yours.
[706.32 --> 715.14]  And while most of the time it works out just fine, the one thing in life that you really cannot afford to wait on is setting up term coverage life insurance.
[715.60 --> 720.64]  You've probably seen life insurance commercials on TV and thought, yeah, I'll look into that later.
[721.04 --> 722.54]  No, later doesn't come.
[722.90 --> 724.18]  This really isn't something you can wait on.
[724.52 --> 726.98]  Choose life insurance through a ladder today.
[727.48 --> 730.88]  Here's what we love about ladder and why we allow them as a sponsor.
[730.88 --> 738.48]  They are 100% digital, no doctors, no needles, no paperwork when you apply for $3 million in coverage or less.
[738.58 --> 741.18]  Just answer a few questions about your health in an application.
[741.78 --> 745.86]  Ladder's customers rate them 4.8 out of 5 stars on Trustpilot.
[746.22 --> 749.04]  And they made Forbes best life insurance 2021 list.
[749.38 --> 752.20]  You just need a few minutes and a phone or laptop to apply.
[752.58 --> 755.02]  Ladder's smart algorithm works in real time.
[755.08 --> 757.06]  So you'll find out if you're instantly approved.
[757.16 --> 758.16]  No hidden fees.
[758.16 --> 764.00]  You can came to any time, get a full refund if you change your mind in the first 30 days.
[764.38 --> 769.98]  Ladder policies are issued by insurers with long proven histories of paying claims.
[770.34 --> 774.10]  They're rated A and A plus by A and best.
[774.48 --> 778.02]  Finally, since life insurance costs more as you age now.
[778.44 --> 779.06]  Yeah, right now.
[779.34 --> 781.04]  Now's the time to cross it off your list.
[781.04 --> 788.36]  So go to ladderlife.com slash practical AI today to see if you're instantly approved.
[788.36 --> 793.08]  Again, that's ladder.com slash practical AI.
[793.26 --> 798.60]  L-A-D-D-E-R life.com slash practical AI.
[811.04 --> 828.52]  Well, Chris, as people are diving into their first projects and areas of interest and new
[828.52 --> 835.66]  things in the field, one of the interesting things and kind of learning resources that
[835.66 --> 842.60]  we don't maybe spend a ton of time talking about, although we are actively engaged in it,
[842.72 --> 851.34]  is community around the AI space and where people can connect with that sort of community.
[851.70 --> 858.04]  We've produced a lot of content, but we've also engaged in various spheres over the years.
[858.04 --> 864.46]  And there might be a lot of new people, let's say they're web developers or they're backend engineers or whatever,
[864.58 --> 867.00]  and they're getting into the space, they're doing projects.
[867.74 --> 874.08]  And their kind of normal programming conference isn't, or maybe has some AI topics,
[874.12 --> 883.10]  but they're wondering, is there a better place to find people that are doing these sorts of projects and that sort of thing?
[883.60 --> 887.50]  I know you were at one point involved in kind of the meetup space,
[887.50 --> 893.96]  although COVID maybe had a little bit to do with the downgrade of some of those communities.
[894.58 --> 896.16]  Yeah, it's a great point.
[896.28 --> 900.06]  And it's evolved in interesting ways, kind of what you're getting at there.
[900.40 --> 904.16]  And to start with the last thing that you said, I was, for a number of years,
[904.24 --> 909.42]  I ran the Atlanta deep learning meetup and the phrase deep learning is kind of antiquated now as well.
[909.56 --> 912.28]  And the learning, and it kind of fell off when COVID hit,
[912.28 --> 918.66]  but we were really the preeminent kind of AI oriented community in the Atlanta area, which is where I'm at.
[918.98 --> 924.14]  It's interesting as another counterpoint to go into this, you and I met in a different community.
[924.14 --> 928.64]  We met in the Go language community because we were both Go programmers.
[928.64 --> 934.10]  And we were kind of the two people thinking a lot about AI and data science in that community.
[934.10 --> 937.02]  So it was a natural thing for us to gravitate together.
[937.64 --> 944.00]  But interestingly, if you're really focused on different aspects of AI, whether it be generative AI or other fields of AI,
[944.14 --> 950.10]  since we've recently pointed out that not all things are just generative AI, even though that's the hot thing right now.
[950.10 --> 953.82]  There are many vendor specific communities.
[954.44 --> 958.54]  We have a podcast specific community here where we engage our listeners all the time.
[958.78 --> 962.08]  And there are some platform specific communities.
[962.78 --> 967.58]  But there is kind of a, like where we met in the Go community, there was an overall,
[967.72 --> 972.08]  whatever you were doing in the Go space, there was a larger community.
[972.08 --> 977.84]  And you kind of knew all the people and all the names that were there and would follow that and be participant in it.
[978.14 --> 979.84]  Here, we don't really have that.
[979.84 --> 982.82]  We have many, many fragmented AI communities.
[983.02 --> 988.84]  And we'll go to a hugging face for us, you know, to get open source models and to see what's going on there.
[988.98 --> 991.98]  And, you know, there are lots of these smaller communities.
[991.98 --> 999.52]  But I would imagine if you're coming into the space today and you're one of those people who really want to dive into AI here in 2024,
[999.52 --> 1006.80]  it must be very hard to figure out what space you should be in to make all the connections and to ramp up.
[1006.96 --> 1008.06]  Any thoughts on that?
[1008.06 --> 1012.18]  What would you recommend to somebody, Daniel, if somebody were to come into the space today?
[1012.62 --> 1017.70]  Yeah, it is a bit of a challenge because it is a bit fragmented.
[1017.70 --> 1027.20]  And maybe we could split this up into a couple of kinds of engagement, maybe one from a more technical side and one from a less technical side.
[1027.20 --> 1038.48]  So in terms of architecting and building generative AI apps or other kind of AI apps or fine tuning models and that sort of thing.
[1038.48 --> 1059.18]  I think what I would generally recommend is starting out with some sort of learning resource that is probably going to be on Hugging Face, Langchain, Llama Index, LanceDB, one of the other vector database providers.
[1059.18 --> 1066.56]  These sorts of projects have really good tutorials and guides associated with them.
[1066.56 --> 1069.80]  Starting out more project related.
[1069.80 --> 1078.96]  Those are trusted projects in the AI space and trusted platforms in the AI space.
[1079.36 --> 1097.94]  And then looking at one of those projects, like let's say you go and you find a guide that is setting up multimodal rag system to search over videos or images with Llama Index or something like that.
[1097.94 --> 1111.72]  Right. Well, a lot of these projects, not all of them, but a lot of them have some type of forum or chat kind of interface that the community around those projects gathers in.
[1111.72 --> 1118.62]  So oftentimes it's either Discord or Slack or a forum type of thing.
[1118.62 --> 1133.50]  So I think if you start kind of in those spaces like Llama Index or LanceDB and look at a guide that is something similar to what you want to build, you try going through the guide.
[1133.50 --> 1146.46]  But you also look to see if those projects have a Discord associated with them or a Slack channel associated with them and go ahead and log into those.
[1146.68 --> 1148.90]  And, you know, it's OK to lurk for a while.
[1149.04 --> 1157.44]  But as you're going through your example and, you know, you don't understand this or you're getting that error, just go ahead and be brave and put something in those spaces.
[1157.44 --> 1160.28]  I've generally found them to be fairly welcoming.
[1160.86 --> 1167.20]  For example, if you go to Llama Index, there's a community page and you'll see right away join Discord.
[1167.78 --> 1170.02]  There's many other of these spaces.
[1170.42 --> 1178.92]  So like our friends over at the Latent Space podcast have a very, very active Discord server that they're running.
[1178.92 --> 1186.68]  We have a Slack channel associated with this podcast, but there's other projects like LanceDB has a Discord channel.
[1186.68 --> 1194.64]  And these are generally people that are building projects within this sort of space, within this sort of topic.
[1195.06 --> 1206.58]  And they're generally open to, hey, I might not only be using Llama Index, but I could ask a question about choices of vector databases or choices of models.
[1206.66 --> 1213.04]  And everyone in there is kind of working in this space and may have biased or opinionated thoughts on that.
[1213.12 --> 1216.36]  But you gradually kind of learn and meet people in that way.
[1216.36 --> 1223.46]  So I think it's in some ways, it's a little bit more project related than kind of overall community related.
[1223.46 --> 1229.60]  And Hugging Face is a great community in the sense of GitHub being a community.
[1230.08 --> 1238.82]  But it's not where people are having all of these different conversations about specific projects and guides and that sort of thing.
[1238.82 --> 1246.88]  They're collaborating on models and data sets and that sort of thing, but maybe not in a kind of asynchronous chat sort of way.
[1247.58 --> 1249.82]  So what do you think about the social element?
[1249.92 --> 1256.24]  Because there's some great guidance there on learning and kind of connecting on a project basis and stuff.
[1256.24 --> 1261.94]  But where would you go for the personalities, you know, for the friendships that you develop?
[1262.28 --> 1263.34]  How would you approach that, Daniel?
[1263.70 --> 1272.00]  Yeah, it might depend on people's personality and what opportunities kind of present themselves to those people.
[1272.24 --> 1276.50]  There are a good number of events that are gradually happening.
[1276.50 --> 1283.96]  Like our friends over at the ML Ops community have had a series of online virtual events.
[1284.24 --> 1288.40]  I know there was an AI engineering event out on the West Coast.
[1288.62 --> 1297.54]  There are events like Hugging Face, I think, is doing some type of Hugging Face tour with demos at various locations in person.
[1297.54 --> 1308.24]  So that's a really great place to kind of meet face to face with people and interact and build relationships in terms of personalities and that sort of thing.
[1308.60 --> 1314.94]  One thing you could do is look at our previous episodes of this podcast and go.
[1315.18 --> 1324.08]  And even if you don't listen to all the episodes, which, of course, you should because they're all great or maybe some are better than others, but they're all pretty good, I think.
[1324.08 --> 1337.42]  But you could look at the guests from the previous podcast and go to LinkedIn, go to Twitter, go to Blue Sky, whatever your favorite social is, and see if you can find some of those people on those platforms.
[1338.00 --> 1342.10]  And those are trusted people that, you know, we've met over the years.
[1342.44 --> 1348.92]  And so in an online sense, you can start following them and see who they are kind of reposting and interacting with online.
[1349.20 --> 1353.54]  And that's kind of how your web of connections can form a little bit.
[1354.08 --> 1360.30]  So I want to turn from the community questions that we were just talking about and spread it out.
[1360.30 --> 1370.20]  The community, you know, notion that we were just discussing was really, you know, focused on those of us who are embedded in AI work.
[1370.30 --> 1371.54]  We probably do it for a living.
[1371.86 --> 1373.88]  This is kind of very central to us.
[1373.98 --> 1379.00]  But there is most of the world out there that does not fall into that category.
[1379.00 --> 1384.74]  And yet AI is still impacting their lives in tremendous ways increasingly.
[1385.22 --> 1397.60]  And one of the things that I have been keenly interested in lately is for the rest of the 99% out there that are not building their professional lives on AI in every moment the way we are,
[1397.60 --> 1403.10]  they still need some, you know, entrances into how to use this in a productive way.
[1403.28 --> 1411.44]  We are getting on the podcast and with our audience and the listeners talking about Gemini and ChatGPT all the time.
[1411.80 --> 1417.44]  And there are these other 99% they're hearing this too in the news, but they don't really understand it.
[1417.50 --> 1419.58]  They're probably not using it.
[1419.90 --> 1425.88]  They might have tested out one of the free interfaces here or there to see what it was like, but it's not part of their workflow.
[1425.88 --> 1436.74]  Right now we're seeing a period in 2024 where organizations are starting to explore and even demand that their employees start using these tools.
[1436.96 --> 1440.36]  They're making them available, but they're really struggling with adoption.
[1440.68 --> 1448.96]  I've run across all sorts of issues where hitting mainstream adoption with generative AI tools has been a tremendous challenge.
[1449.50 --> 1455.12]  And so I'd like to dive into that for a couple of moments and kind of talk it over where we're going,
[1455.12 --> 1459.04]  because that's certainly, I know the organization I'm part of is interested in this topic.
[1459.26 --> 1466.16]  And I talk to people every day that are trying to figure out how do we get it out there beyond our software developers and our data scientists.
[1466.68 --> 1471.68]  What are your, any thoughts you have there in terms of, if you have your typical non-technical worker,
[1472.22 --> 1476.52]  they're a knowledge worker and they have a set of tasks every day.
[1476.52 --> 1486.92]  How do you start to break that nut in terms of getting those people recognizing where some of these generative AI tools can help them do their own?
[1486.98 --> 1491.20]  I have a couple of examples I'll go to in a moment, but I'm curious what you've seen out there, Daniel.
[1491.58 --> 1498.00]  Yeah, I think there's one side of it, which is maybe places for those people to start,
[1498.00 --> 1504.54]  but also an interesting piece of this is a mechanism for how that knowledge trickles into an organization,
[1504.54 --> 1507.76]  which I think is an interesting topic in and of itself.
[1507.76 --> 1518.56]  One pattern that I've seen a little bit at organizations is maybe a couple of champions that are higher up on the ladder
[1518.56 --> 1525.28]  that see the vision of transformation and see that this is going to be a transformative technology for their organization.
[1525.28 --> 1536.78]  And those leaders might take some type of courses or certification or crash course type of thing in the topic.
[1537.00 --> 1547.96]  So MIT has some kind of AI for digital transformation or AI, generative AI related things for non-technical people that they offer online.
[1547.96 --> 1557.76]  And I think maybe some even live NVIDIA has some courses like what is generative AI, generative AI explained.
[1558.28 --> 1560.96]  NVIDIA has some of those types of things.
[1561.08 --> 1567.06]  So there might be these leaders who see the vision for how this is going to be a transformative technology.
[1567.46 --> 1572.32]  They might do one of those things to understand at a level that makes them comfortable.
[1572.32 --> 1577.48]  And I think part of the trickle down is leading by example in that.
[1577.60 --> 1582.74]  So when they're having interactions with their team and or other teams,
[1582.74 --> 1589.78]  I think it can literally be, you know, something comes up in a meeting and you're sharing your screen
[1589.78 --> 1596.06]  and you literally you just have a tab open that is chat GPT or Claude or Gemini or whatever.
[1596.06 --> 1603.04]  And you go over there and you literally just you answer a question or you get something done immediately
[1603.04 --> 1608.24]  because you know how to interact with those tools to do something quickly.
[1608.40 --> 1614.14]  And that can be a light bulb moment for other people where they see a person leading by example,
[1614.34 --> 1619.22]  using a tool and not like here's how you use this tool sort of way,
[1619.30 --> 1623.50]  but really in the flow of how they're doing their own work.
[1623.50 --> 1627.78]  And I think that seeps through that's really impactful because it shows,
[1627.98 --> 1633.86]  oh, this person who is maybe influential in my organization is operating in this way
[1633.86 --> 1637.26]  and able to do these cool things with these tools.
[1637.66 --> 1639.08]  Can I, you know, do that?
[1639.32 --> 1644.20]  I think some of it can also be a little bit directed where you're having your one-on-ones
[1644.20 --> 1647.74]  maybe with your direct reports, right?
[1647.74 --> 1652.86]  And they're asking questions that they should be able to source the answer to
[1652.86 --> 1655.44]  or accomplish very quickly with these tools.
[1656.12 --> 1662.34]  And you can tell them, hey, you know, there's a pretty quick way that you can get this summary
[1662.34 --> 1666.34]  or develop this outline for your presentation out of this article.
[1666.82 --> 1671.32]  Let me show you how to do that and actually have them go to the site,
[1671.52 --> 1675.40]  generate the outline for the presentation based on some article or something.
[1675.40 --> 1680.74]  And actually do that in your one-on-ones, even to the point of encouraging people like,
[1680.86 --> 1685.10]  hey, you should maybe just have this bookmarked or have it up on your tab.
[1685.24 --> 1690.32]  So I think that's kind of how some of that trickle down could happen.
[1690.46 --> 1696.16]  And how I've seen it happening is kind of a foothold in these influential people within an organization.
[1696.16 --> 1703.20]  And then leading by example and kind of in a one-on-one sort of way rather than a top-down directive of,
[1703.72 --> 1706.20]  we shall now do things this way, right?
[1706.66 --> 1707.00]  Understood.
[1707.26 --> 1711.90]  I actually have an example to illustrate one of the things that you were talking about there.
[1712.10 --> 1719.24]  In my own employment, we have both access to ChatGBT and we also host internal models,
[1719.36 --> 1721.52]  internal open source models, which we love.
[1721.52 --> 1727.36]  Because that way you don't have to worry about if you're sending proprietary information out, things like that.
[1727.80 --> 1732.80]  And so this morning in my day job, I was working with a team of people.
[1733.32 --> 1735.60]  There's a presentation that has to come out of that,
[1735.68 --> 1739.86]  a PowerPoint presentation that has to come out as one of the deliverables of that.
[1739.86 --> 1749.62]  And as we were having a group discussion, sharing screen, was able to type in some of the things that we wanted to talk about into the model,
[1750.08 --> 1753.30]  generated dynamically while we were on a group call,
[1753.48 --> 1758.32]  I generated a set of talking points to the various issues that we were addressing.
[1758.92 --> 1762.86]  Basically, kind of a presentation within the prompts, if you will.
[1762.86 --> 1769.92]  I was then able to turn that presentation into VBA code, Visual Basic for Applications code,
[1770.04 --> 1773.14]  where it embedded the content in that VBA code.
[1773.34 --> 1777.92]  Then I was able to open up PowerPoint right there, copy and paste out of the prompt.
[1778.38 --> 1780.66]  This is totally non-technical, what we're talking about here.
[1781.04 --> 1785.34]  Go to the Tools tab, down to Macros, and open the Visual Basic Editor in PowerPoint,
[1785.64 --> 1786.88]  which is available to everybody.
[1786.88 --> 1794.18]  We pasted in the code as a new module and ran it, and it produced our PowerPoint for our team right there.
[1794.28 --> 1798.86]  The whole thing took five minutes to get a 30-page PowerPoint set up.
[1798.96 --> 1804.14]  Now, there was a lot of manual tweaking to be done afterwards and adding some graphics and stuff like that,
[1804.40 --> 1809.56]  but we probably cut five, eight hours worth of work out of our workflow
[1809.56 --> 1814.92]  by tossing the critical ideas into the prompt, turning them into that code, and copying and pasting in.
[1814.92 --> 1818.16]  It doesn't take a developer to do that, that anybody could do that.
[1818.34 --> 1822.84]  So that's one of many possible use cases where you're using it.
[1822.90 --> 1829.04]  You haven't replaced any of the workers, but you're accelerating everybody's productivity dramatically at that point
[1829.04 --> 1830.86]  and saving a lot of time to do it.
[1831.04 --> 1837.96]  So as I've been thinking about how we get more people in the world to use these technologies to their benefit,
[1837.96 --> 1846.44]  I think having a number of different kind of typical persona use cases like that that many people might need.
[1847.00 --> 1849.08]  So there's your PowerPoint strategy, folks.
[1849.34 --> 1854.54]  Right now, in whatever job you're in, you can do that if you have access to one of these larger models.
[1855.22 --> 1859.60]  And then the other thing I wanted to dive into was it's interesting the emotional quirks.
[1859.60 --> 1865.24]  People are worried about everything from, will this take my job if I start using it and make me irrelevant?
[1865.48 --> 1868.74]  They wonder, who's watching when I do this?
[1868.80 --> 1872.36]  Can my boss see if I stumble, if I'm struggling with something?
[1872.68 --> 1875.30]  Who in my company is aware of what I'm doing?
[1875.74 --> 1880.56]  So there's kind of a lot of FUD, fear, uncertainty, doubt associated with the use of the tools.
[1880.56 --> 1889.20]  And I think part of that is just kind of in these trainings that you were alluding to earlier to be able to have discussions with people about their fears
[1889.20 --> 1895.84]  and see if you can get some interest in uptake by going right at the thing that's holding them back.
[1896.28 --> 1898.00]  And a lot of times people think it's technical.
[1898.18 --> 1898.54]  It's not.
[1898.64 --> 1906.56]  The PowerPoint thing, you can have zero technical training and go do that if you just know to open up that single thing in the PowerPoint deck
[1906.56 --> 1911.48]  deck and type in, not type in, but copy and paste the code that was produced at the prompt.
[1911.66 --> 1919.12]  So I think that there are hundreds or thousands of opportunities along this line that people could take advantage of.
[1919.32 --> 1921.60]  Any thoughts on what you might do in that way?
[1922.00 --> 1928.86]  It's interesting that you bring up the fear and uncertainty piece because there are a lot of misconceptions.
[1928.86 --> 1935.42]  And it doesn't often work to just straight up invalidate those.
[1935.42 --> 1951.86]  So somehow I think if you're thinking about this adoption in your organization and you're working with people, to some degree, you kind of have to find an entry point where there's less of this fear and uncertainty.
[1951.86 --> 1964.16]  Because I think all of us that are working with these models and have been working with these models recognize that working with generative AI models, prompting them, integrating them into your workflow,
[1964.42 --> 1968.24]  it isn't often what you expect it to be getting into it.
[1968.24 --> 1973.40]  And you kind of have to build up your own intuition of, oh, this is kind of how this model behaves.
[1973.44 --> 1975.16]  And this is kind of how this model behaves.
[1975.16 --> 1977.32]  And this is kind of how the prompting works.
[1977.32 --> 1982.86]  And oh, this you kind of have to build up some of that intuition before you get a sense of how they operate.
[1982.86 --> 1997.70]  But you're never going to build up that intuition if you just focus on the use case that people have some fear over, like generating, putting in customer information into the interface or something like that.
[1997.70 --> 2006.84]  So I think to some degree, you have to find some use cases where people are able to safely interact with these models.
[2007.08 --> 2011.00]  And it could be private chat interface that you allow people to use.
[2011.08 --> 2021.02]  It could be a local chat interface like LM Studio or something like that, that you encourage people to use because it's local and there's nothing going anywhere.
[2021.14 --> 2023.04]  And you can tell people, oh, yeah, this is fine.
[2023.38 --> 2026.16]  And then they get a sense of the models and you can go from there.
[2026.16 --> 2030.18]  So I think it's about finding that foothold to some degree.
[2030.72 --> 2036.18]  One of the interesting things that I've found is people sort of expect these models.
[2036.80 --> 2044.40]  They get disillusioned when they ask like a search engine like question into these models and they just don't find what they need.
[2044.52 --> 2047.52]  And so that's kind of some of that intuition that I was talking about.
[2047.52 --> 2051.62]  Like these models operate slightly different than a search engine.
[2052.04 --> 2052.84]  That's a great point.
[2052.84 --> 2060.76]  And so everyone kind of had to build up a little bit of intuition, I think, when they learned about, you know, how to Google things.
[2060.94 --> 2065.22]  I think there is a like there is a skill of how to Google things.
[2065.22 --> 2065.54]  Right.
[2065.62 --> 2068.16]  And so there is a similar intuition.
[2068.16 --> 2071.80]  I still, you know, I'm sure you've run into this many times.
[2071.80 --> 2077.24]  Like people ask questions in a business context and you're like, why didn't you just Google that?
[2077.46 --> 2081.44]  Well, maybe they don't have the intuition around how to like properly.
[2081.68 --> 2083.38]  I've definitely seen this before.
[2083.46 --> 2087.34]  Properly search the Internet to find answers and self-serve themselves.
[2087.86 --> 2088.66]  Actually, it's interesting.
[2088.66 --> 2096.46]  I found an article this week that talked about why AI search engines really can't kill Google.
[2096.68 --> 2099.40]  This was from The Verge publication.
[2099.92 --> 2109.40]  And so it talks about search engines like Perplexity and U.com and Google Gemini and ChatGPT to some degree.
[2109.40 --> 2111.76]  It goes through, it's a really interesting article.
[2112.02 --> 2115.14]  People should look it up and we'll include it in our show notes.
[2115.28 --> 2129.42]  But it talks through some of the kind of main use cases that you might have learned to do in Google, like navigation or something, navigation questions that don't really work so well in chat and in the current chat interfaces.
[2129.64 --> 2132.56]  So there's a different sort of intuition that needs to be built up.
[2132.66 --> 2135.88]  And one isn't just a drop-in replacement for the other.
[2136.18 --> 2136.86]  That's a great point.
[2136.86 --> 2146.70]  And not only are they distinct skill sets, but there is a superset of how you use them together for their strengths along the way.
[2146.98 --> 2154.84]  And with the notion that search engines' primary job, as the article notes there, is to get you to a website.
[2155.38 --> 2161.52]  And when I talk, I'm still old school and I don't just go to a website that I already know through Google.
[2161.70 --> 2164.78]  I will actually just type it in directly because I know it.
[2164.78 --> 2168.58]  But my daughter, who is 11, she knows the website.
[2168.74 --> 2171.80]  She knows where it's at, but she still puts it in Google to go there.
[2171.90 --> 2173.06]  And her friends do that too.
[2173.22 --> 2177.84]  She uses it as a navigation tool to the point that you just made a moment ago.
[2178.08 --> 2185.22]  Whereas when we're prompting in these models, we're really seeking information in a lot of ways.
[2185.22 --> 2192.52]  Instead of getting to a website that has information, we're kind of getting the model to feed that information to us directly.
[2192.74 --> 2195.42]  And I personally tend to use both.
[2195.92 --> 2203.00]  It's very common for me to flip back and forth between Google and a large language model and use them each for what I want.
[2203.00 --> 2207.06]  Or if I don't know exactly where to go for Google, I'll learn a bit from the model.
[2207.06 --> 2214.52]  And then I'll do a deep dive on a website that's specific to what I just learned from the model and get there that way.
[2214.52 --> 2218.56]  So it's an evolving landscape of tools to get these things done now.
[2218.56 --> 2223.40]  Yeah. And I would definitely encourage people to check out this article.
[2223.56 --> 2224.30]  It's quite interesting.
[2224.50 --> 2238.06]  They go through different types of queries, like navigational queries, what they call buried information queries, exploration queries, evergreen information, like how many weeks in a year or when is Mother's Day.
[2238.58 --> 2244.04]  Real-time queries like sports scores and that sort of thing.
[2244.04 --> 2248.86]  The exploration questions that I mentioned, like why were chainsaws invented?
[2249.48 --> 2252.76]  It's like exploration and learning sort of thing.
[2252.90 --> 2255.80]  So and they compare some of the answers from different ones.
[2255.86 --> 2270.62]  So if you're struggling maybe with this intuition, maybe that's a good place to jump in and try some of those queries yourself that are there and see what comes back from the various chat GPT or Gemini or u.com and those sorts of things.
[2270.62 --> 2280.46]  And then circling back on our community idea before, try those things, hop into our community here at the Change Log and share what you've done with that.
[2280.54 --> 2286.06]  We're very curious to see what people choose to do coming out of these discussions that we've had today.
[2286.18 --> 2290.76]  I'm looking for the most creative ideas to inspire me myself.
[2290.98 --> 2292.88]  So please send what you got.
[2293.16 --> 2293.88]  Sounds great, Chris.
[2293.88 --> 2303.02]  Well, it's been fun exploring this topic with you and look forward to many further exploration questions in the future.
[2303.24 --> 2304.52]  Hope you have a great evening.
[2304.90 --> 2305.22]  You too.
[2305.32 --> 2305.92]  Take care, Daniel.
[2313.20 --> 2314.20]  All right.
[2314.40 --> 2316.90]  That is Practical AI for this week.
[2317.70 --> 2318.72]  Subscribe now.
[2318.72 --> 2330.32]  If you haven't already, head to PracticalAI.fm for all the ways and join our free Slack team where you can hang out with Daniel, Chris, and the entire Change Log community.
[2330.88 --> 2335.52]  Sign up today at PracticalAI.fm slash community.
[2336.08 --> 2343.06]  Thanks again to our partners at Fly.io, to our Beat Freaking Residence, Breakmaster Cylinder, and to you for listening.
[2343.42 --> 2345.16]  We appreciate you spending time with us.
[2345.54 --> 2346.70]  That's all for now.
[2346.96 --> 2348.60]  We'll talk to you again next time.
[2348.72 --> 2378.70]  We'll talk to you again next time.
