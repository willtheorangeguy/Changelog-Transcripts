[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.24 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[17.46 --> 20.04]  This episode is brought to you by DigitalOcean.
[20.38 --> 25.14]  DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.14 --> 29.14]  They have an intuitive control panel, predictable pricing, team accounts,
[29.14 --> 36.82]  worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.06 --> 42.54]  DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 --> 46.34]  Head to do.co slash Changelog to get started with a $100 credit.
[46.64 --> 48.80]  Again, do.co slash Changelog.
[59.14 --> 66.00]  Welcome to Practical AI, a weekly podcast that makes artificial intelligence practical, productive, and accessible to everyone.
[66.42 --> 70.40]  This is where conversations around AI, machine learning, and data science happen.
[70.82 --> 75.42]  Join the community and Slack with us around various topics of the show at Changelog.com slash community.
[75.78 --> 76.76]  And follow us on Twitter.
[76.90 --> 78.54]  We're at Practical AI FM.
[78.92 --> 79.20]  Okay.
[79.38 --> 80.24]  Here's Daniel and Chris.
[80.24 --> 88.46]  Welcome to another episode of Practical AI.
[88.84 --> 92.78]  I'm Daniel Whitenack, a data scientist with SIL International.
[93.12 --> 99.74]  And I'm joined as always by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[100.02 --> 100.72]  How are you doing, Chris?
[101.08 --> 101.64]  Doing great.
[101.70 --> 102.52]  How's it going today, Daniel?
[102.52 --> 103.66]  It's going well.
[103.76 --> 110.22]  Coming off of vacation, it only took me just about till 2 p.m. on Monday to catch up on email.
[110.44 --> 111.76]  So, not too bad.
[111.98 --> 114.30]  Had to jump in early and catch up from things.
[114.64 --> 115.34]  But all is good.
[115.42 --> 115.84]  How about you?
[116.24 --> 117.94]  Just slaving away while you're on vacation.
[118.10 --> 120.72]  My wife and daughter actually went to Disney World without me.
[120.90 --> 121.20]  Oh, no.
[121.22 --> 123.96]  So, they left me at home with the pups and doing work.
[124.16 --> 124.58]  Gotcha.
[124.72 --> 127.46]  Didn't go to see the new Star Wars deal.
[127.88 --> 130.52]  Star Wars World, or I don't know what it's called, actually.
[130.82 --> 134.10]  No, I think they saw Harry Potter, but not Star Wars this time.
[134.10 --> 134.82]  Yeah, Universal.
[135.16 --> 135.34]  Cool.
[135.98 --> 138.36]  Well, I'm excited to be back from vacation.
[138.36 --> 142.32]  I'm excited to have with us today an awesome guest.
[142.50 --> 149.76]  Today we have with us Craig Wiley, who is Director of Product Management for Google Cloud AI Platform.
[150.42 --> 151.02]  Welcome, Craig.
[151.56 --> 151.98]  Thank you.
[152.10 --> 153.08]  Very excited to be here.
[153.08 --> 160.80]  Yeah, excited to talk to you today about a lot of TensorFlow-related things and a lot of Google Cloud-related things.
[160.96 --> 169.72]  But before we get into that, could you just give us a little bit of your background and how you got into AI and eventually ended up at Google?
[170.16 --> 170.52]  Sure.
[170.52 --> 175.38]  So, you know, as you said, I run product management for our AI platform here at Google.
[175.70 --> 181.70]  Previous to that, I spent a couple of years at AWS building Amazon SageMaker.
[181.70 --> 194.38]  And then previous to that, I spent a number of years in Amazon's supply chain group doing kind of optimizations and, you know, starting with pivot tables and moving on to classic econometric regression.
[194.38 --> 204.80]  And then moving on to kind of, you know, more and more unsupervised and more and more, you know, deeper and deeper learning as we tried to solve some of these kind of unbelievably complex problems.
[204.80 --> 214.14]  And that the ever-present goal of trying to make all of this go faster and yield stronger results got me just super interested in the tooling space.
[214.14 --> 230.24]  And so since SageMaker and now at Google, I've been really focused on how it is that we can unlock the power of data within the enterprise and give companies and enterprises the ability to, you know, gain full benefit from the data sets they're collecting.
[230.90 --> 235.52]  So then is your background more on the, did you do like software engineering before that?
[235.56 --> 242.66]  Or is your background more in science in terms of how you got into working on supply chain stuff at Amazon and all that?
[242.66 --> 249.48]  Yeah. So I was a philosophy major who believes deeply that the world can be regressed.
[249.82 --> 253.38]  You know, if you had all the information, then I think you could kind of predict anything, right?
[253.46 --> 256.08]  And so it kind of followed that sense.
[256.18 --> 263.62]  And as I joined Amazon, I found myself, you know, at a data-driven company, increasingly trying to answer the questions deeply with data.
[263.62 --> 272.46]  And that, you know, next thing I knew, I was leading a team of machine learning engineers trying to do this at a scale that I had never imagined.
[272.66 --> 280.94]  So does your philosophy major, do you feel like that gives you a unique perspective on AI-related things?
[280.94 --> 288.02]  Or do you feel like you're pretty much in the weeds of the technical stuff and you're not thinking about philosophy too much?
[288.56 --> 289.98]  You know, it's a little of both.
[289.98 --> 299.72]  There's times when I'm pretty deep in the details here and there's other times when I think that ability can lend some context around some of the work we're doing in responsible AI.
[299.72 --> 310.80]  And under just, I mean, fundamentally, you know, if we can think about these problems as, you know, here's the input and from this input we can determine an output.
[310.80 --> 321.34]  You know, when we break the problem down into something that's that simple, I really think that we can broaden the customer group who we reach out to with regards to building these types of models.
[321.34 --> 338.36]  I know one of the things that I really appreciated for quite a while is, and you probably know more of the background on this, but I remember that someone in Google came out with this sort of, I think it was called machine learning guidelines or rules for engineers or something like that.
[338.42 --> 343.68]  I remember seeing it as a PDF originally, and I think now it's actually got a nice website and everything.
[343.68 --> 351.04]  But it was a very practical set of guidelines for engineers getting into machine learning problems and all of that.
[351.30 --> 352.32]  And I found that really useful.
[352.64 --> 360.02]  Maybe we can link that in the show notes, but I definitely think that, you know, your background probably has helped you dig into some of those problems.
[360.02 --> 363.06]  And I really appreciate a lot of what Google has done in that area.
[363.62 --> 367.78]  As a leader in this space, you know, with kind of with great power comes great responsibility.
[367.78 --> 380.14]  And so we find ourselves, you know, building things like our AI principles in an effort to try and ensure that we're proud of the work we're doing and that our customers are doing and that others in this industry are doing.
[380.38 --> 383.02]  So it's a deep area of passion for many involved here.
[383.02 --> 384.64]  Yeah, I'm not surprised.
[384.82 --> 397.26]  It's I know that kind of going to following up on what Daniel was saying a moment ago, as Google has published various principles and in terms of how to do machine learning, how to do ethics, which is a hot topic now that we talk about quite a bit.
[397.46 --> 400.10]  All these things are certainly very much leading edge.
[400.30 --> 409.18]  And the rest of us in the industry are constantly looking to see what you guys are putting out there, which kind of, you know, leads to transitions us to another topic, which is TensorFlow,
[409.18 --> 418.20]  which obviously being, you know, certainly one of the two dominant, maybe the dominant tool out there, TensorFlow to be able to do machine learning in this space.
[418.46 --> 422.18]  Probably the vast majority of our listeners are quite aware of it by this time.
[422.38 --> 425.68]  I'm kind of curious, though, what is the relationship?
[425.86 --> 432.32]  Could you kind of tell us what TensorFlow is and what is the relationship between TensorFlow and Google at large?
[432.32 --> 445.26]  And, you know, how do those communities interact and kind of maybe give us a little bit about the origins of TensorFlow at Google, how it got kicked off, you know, how people opted into that and how the ecosystem started developing on that?
[445.82 --> 446.02]  Yeah.
[446.18 --> 461.98]  So, you know, TensorFlow is for those who aren't as aware is, you know, kind of the premier deep learning framework for building these neural networks that have become so transformational in the kind of journey of artificial intelligence and machine learning.
[461.98 --> 473.30]  And, you know, TensorFlow is it's an open source project, you know, kind of started and led by Google, but with contributors from all over the world and for many different companies and corporations and organizations.
[474.12 --> 490.02]  And, you know, at the end of the day, I think when I think about TensorFlow, I think about the ability for people to do increasingly complex tasks easily so that they can get to the point of value creation faster.
[490.02 --> 493.88]  Now, you know, you asked about kind of how we sit organizationally and things.
[494.32 --> 509.58]  TensorFlow is a part of our research group and, you know, internally kind of has a charter or mandate to ensure that Googlers have the best tools they need in order to build the kinds of assets, the kinds of machine learning tools and assets that they want.
[509.58 --> 519.66]  Having said that, in cloud, we work hand in hand with this group, to be honest, probably of folks who are not in my direct kind of, you know, org.
[520.00 --> 534.98]  This is probably the org I am closest with meeting with them kind of on a daily basis to figure out how we can provide more value to TensorFlow users and how TensorFlow can provide increasing value to Google and Google's cloud customers when need be.
[534.98 --> 555.56]  Yeah. And I know, I mean, even though I guess a lot of the decisions around TensorFlow and maybe the roadmap are made by people within Google, I know that, for example, TensorFlow 2.0, there was a lot of community involvement in that and community feedback that led to more usability and that sort of thing.
[555.82 --> 557.56]  TensorFlow 2.0 was a pretty big deal.
[557.56 --> 566.46]  I think maybe you could kind of remind us what happened with TensorFlow 2.0 and how that was driven by a lot of this user feedback and that sort of thing.
[566.46 --> 585.26]  Yeah, you know, I think you're right that TensorFlow continues to be an active open source program and is one that, you know, the TensorFlow, both the Google TensorFlow community and the open source community are kind of constantly seeking a wide variety of, you know, kind of input and contributions.
[585.26 --> 615.24]  You know, one of the things that I was most excited about within this same development time period, just as TensorFlow 2.0 was starting to really take shape and get to a point where it would be nearing release, is at that same moment that we started to come together and bring TensorFlow Enterprise to our customers, which is, you know, our basically offering for enterprises to be able to have a rich TensorFlow experience with the requirements of the
[615.24 --> 619.08]  that they need kind of front and center in a cloud environment.
[619.08 --> 631.82]  And what are those, could you just kind of briefly describe what are some of those requirements that are unique to like a production enterprise setting that maybe are harder to deal with in an open source setting?
[632.24 --> 641.26]  Yeah, I mean, so, you know, TensorFlow Enterprise, you know, it's really designed to accelerate the software development experience and improve the reliability for AI applications of the enterprise.
[641.26 --> 645.10]  And, you know, it starts really first with enterprise grade support.
[645.68 --> 654.06]  And when I say enterprise grade support, really what I mean there is a lengthening of the support window for previous versions, right?
[654.12 --> 666.46]  We know that folks have developed, you know, exciting models and models that create a lot of value for their organizations on, you know, 114 or TensorFlow 115 or something like that.
[666.46 --> 674.38]  And, you know, and, you know, when, you know, TensorFlow as an open source project, they only support older releases for one year.
[675.20 --> 693.82]  And what we've done in cloud is we've come through and said we will extend that by an additional two years so that you get a full three years of support so that these models that you've built in, you know, TensorFlow 114, you know, you're not feeling pressure to move them out of production and replace them with newer models.
[693.82 --> 709.20]  You can keep them in their environment producing value, knowing that security patches will still be deployed and kind of, you know, fundamental functionality patches or bugs will still be fixed if you should incur them even after that one year window has elapsed.
[709.20 --> 727.20]  We also, we focus deeply on cloud scale performance and ensuring that the TensorFlow enterprise binaries are highly optimized for Google's cloud environment and as well as for running on Kubernetes should folks want to run it in a hybrid or on-prem installation.
[727.68 --> 736.64]  And then finally, we believe there is a ecosystem of apps that are going to be critical for customers to gain the most value out of TensorFlow.
[736.64 --> 742.30]  And so, you know, for instance, we've launched a public-facing, you know, TensorBoard experience.
[742.98 --> 749.48]  And, you know, we've been open about the fact that we're working on an enterprise version of that TensorBoard experience as well.
[749.98 --> 766.46]  So, you know, it's really not kind of one thing, but it's kind of a series of pieces that together we find we can kind of piece together and build a comprehensive, you know, edition of TensorFlow that can really speak to the needs and requirements of these enterprises.
[766.64 --> 779.38]  So, you have customers that are engaging in TensorFlow in the enterprise model and recognizing that the core TensorFlow project is open source led by your internal Google team.
[779.38 --> 794.80]  From a customer perspective, if they're opting into the enterprise version, what is the relationship like for the customer between engaging you with the additional support that you just talked about in the enterprise model versus that open source community?
[795.14 --> 802.86]  How do those two separate sides of the TensorFlow world at large interact with each other for that customer who has access to both?
[802.86 --> 808.06]  Sure. So, I mean, it really comes down to, you know, TensorFlow is an open source project.
[808.34 --> 816.20]  Anyone can go and download TensorFlow, run it on their laptop, run it on their own data center, or run it on their cloud of choice.
[816.62 --> 827.00]  You know, TensorFlow Enterprise, having been built and highly optimized for Google Cloud, is designed, you know, so we have a series of products such as our deep learning virtual machines,
[827.00 --> 833.82]  which are basically, you know, VMs within Google Cloud that are pre-configured to run TensorFlow Enterprise on them.
[833.90 --> 839.50]  So, all you have to do is come in, pick an instance size, you know, do you want a small CPU or do you want a giant GPU?
[839.88 --> 850.06]  And, you know, say which version of TensorFlow Enterprise you want installed, and we will outfit you with a machine so you'll be up and running instantly with everything you need pre-installed.
[850.06 --> 862.64]  And then we have containers for folks who want to use any of our managed services, our Kubernetes managed services, or if they're running their own clusters, you know, using Kubeflow or other Kubernetes frameworks for managing AI.
[863.00 --> 871.44]  It gives them the opportunity to get closer to their app if that's what they need to do or move into an on-prem environment if that's a priority for them.
[871.44 --> 879.94]  So, really, you know, the way they can engage in TensorFlow Enterprise is by, it's kind of the default engagement when you work with Google Cloud.
[880.46 --> 886.40]  So, I'm curious, we've talked about open source TensorFlow, we've talked about the various elements of TensorFlow Enterprise.
[886.84 --> 901.78]  I was wondering also if you could mention a bit about what TensorFlow Hub is, since a lot of people, I think, part of their first interaction with TensorFlow and maybe the problems that they're working on can be solved by pre-trained models.
[902.14 --> 908.02]  So, I was wondering if you could kind of give us a glimpse into that world and what's available and how that works.
[908.02 --> 918.44]  Yeah. So, you know, I mean, TensorFlow Hub is a library for the publication and discovery and consumption of reusable parts of machine learning models, right?
[918.44 --> 932.78]  So, you know, users can create modules, which are kind of a self-contained TensorFlow graph, along with its weights and assets that can be reused across different tasks and, you know, or different applications.
[932.78 --> 952.62]  And so, really, the idea here, and, you know, I think this is, we're increasingly seeing this both within TF Hub as well as other locations, is this idea of kind of composable AI, where folks can build small pieces, that others can then take those pieces, leverage them, and make them, you know, more broadly available.
[952.62 --> 960.06]  And so, TensorFlow Hub is really a collection of those modules to help accelerate the machine learning process.
[960.18 --> 976.36]  I'll tell you, as someone who has worked for a number of years and continues to work in cloud machine learning, a huge percentage of, you know, of my kind of thinking is spent on how can we, you know, improve the cycle time of building machine learning models and getting them into production.
[976.36 --> 981.72]  Because for so many companies, it comes down to a, hey, I have a team of data scientists.
[982.16 --> 987.12]  That team of data scientists today can get me, you know, 10 models a year.
[987.82 --> 1002.88]  And if I can come through and with the tooling that we put together, we can help them double, triple, you know, 10x their velocity, then the kind of the ROI of machine learning in that organization, you know, increases substantively.
[1002.88 --> 1008.56]  And now the problems that they're willing to attack with machine learning, you know, gets much broader.
[1009.12 --> 1024.88]  And so, I think any, you know, I'm super excited about all of these technologies that give customers the ability to save time and effort and thought, you know, really kind of like time of thinking and thought energy on these problems that have been solved by someone else.
[1025.08 --> 1026.62]  And you don't need to reinvent the wheel.
[1026.88 --> 1030.00]  You just need to go get their wheel, drop it in, and use it in your case.
[1030.00 --> 1034.44]  And I think that's what TF Hub has shown, you know, such a strong ability to do.
[1042.00 --> 1050.84]  If you like this show and you aren't listening to The Change Log, hey, let's fix that bug.
[1051.20 --> 1055.06]  The Change Log is our flagship show, and we've been doing it for over a decade.
[1055.06 --> 1060.14]  Adam and I seek out and interview the people who are pushing the world forward with software.
[1060.96 --> 1066.92]  We dive deep into the hacks, the innovations, and the leadership required to do what these amazing people do.
[1067.16 --> 1078.78]  One recent example is our conversation with Anders Damsgaard, a climate scientist from Denmark who gave us a peek inside his work and how he scratched a common itch he has when gathering academic research from around the web.
[1078.78 --> 1080.92]  Here's a dorky moment from that episode.
[1081.84 --> 1084.72]  Are you trying to be right or are you trying to solve the world's problems?
[1084.94 --> 1085.32]  Exactly.
[1085.70 --> 1089.74]  If you're a scientist trying to be right, well, then your right may not actually be the right.
[1089.90 --> 1090.94]  Yeah, exactly.
[1091.20 --> 1094.24]  There's another saying, all models are wrong, but some are useful.
[1095.00 --> 1096.34]  I like that one.
[1096.84 --> 1099.40]  There's another saying, all models are wrong, except for mine.
[1099.56 --> 1099.98]  Mine's correct.
[1101.74 --> 1102.48]  Good one, Jared.
[1102.48 --> 1105.32]  We had a lot of fun with Anders.
[1105.50 --> 1106.52]  He's a fascinating guy.
[1107.20 --> 1118.72]  Continue listening at changelog.com slash podcast slash 378 or search for The Change Log on your favorite podcast app and find the episode called Open Source Meets Climate Science.
[1118.72 --> 1118.84]  Thank you.
[1132.48 --> 1157.02]  So, Craig, if you are a practitioner out there and you're, you know, you're using Google's cloud AI services in the enterprise, you know, what are some of the things that you're seeing pop up over and over again in terms of use cases, in terms of applications that are kind of clearly leaning toward what your services are able to provide?
[1157.02 --> 1170.24]  Are there certain use cases that you're seeing come up over and over again are fairly common to the platform where people are able to bring value fairly quickly to AI, you know, using TensorFlow in this context of cloud AI?
[1170.54 --> 1173.04]  Or, you know, is it just everything is different?
[1173.36 --> 1174.54]  What kind of trends are you seeing?
[1174.78 --> 1178.86]  Yeah, you know, this is one of these questions that gets harder every month for me to answer.
[1178.86 --> 1191.40]  You know, like, you know, I mean, if you had asked me this question a couple of years ago, I would have kind of said, oh, you know, people build great recommendation systems and, you know, and people build great forecasts or great, you know, vision models or something like that.
[1191.40 --> 1197.26]  And the kind of, you know, application of models was still relatively narrow.
[1197.68 --> 1211.66]  But today with, you know, if I look at company like Unity, so Unity uses Google Cloud and TensorFlow Enterprise to quickly test, build and scale out ML models at a massive scale, right?
[1211.86 --> 1216.10]  Allowing them to serve up kind of the most relevant ads and drive revenue for game developers.
[1216.10 --> 1235.44]  And so, you know, we don't think about, you know, when we kind of turn on the game on our phone or, you know, light up the most recent, you know, kind of game that we're excited about, you know, we don't think about the fact that there is tremendous technology going on behind the scenes to target those ads to pay for that game so that it can continue to be free for us.
[1235.44 --> 1241.52]  And, you know, this is something that is very important to Unity and its developers and customers.
[1241.80 --> 1261.06]  And they have found tremendous success using TensorFlow, using TensorFlow Enterprise and using Google Cloud to, you know, kind of be able to scale this problem that, you know, requires them to kick off kind of hundreds, thousands or tens of thousands of models kind of, you know, in an effort to kind of highly target their advertising and what have you.
[1261.06 --> 1262.30]  So I take that as one example.
[1262.30 --> 1266.24]  And then on the other end, I can call out a company like GM Cruise, right?
[1266.30 --> 1272.88]  So GM Cruise is, you know, a strong leader in autonomous vehicles and is a TensorFlow Enterprise customer.
[1273.78 --> 1286.64]  And, you know, the deep collaborations between Google Cloud, TensorFlow and GM Cruise have given us the ability to reduce their training times from, you know, I think when they arrived, it was something along the order of four days.
[1286.64 --> 1288.04]  And now it's less than a day.
[1288.04 --> 1303.18]  And so, you know, when you're able to achieve, you know, a 4x reduction in cycle time, now all of a sudden they can potentially move four times faster in trying to get to their solution to their problem.
[1303.18 --> 1312.08]  And as the father of a young child, I have to say the idea that he'll never drive a car is a very exciting idea to me.
[1312.54 --> 1319.10]  And so I'm more than willing to help all of these folks get as far down that path as they can as quickly as possible.
[1319.44 --> 1321.18]  It's funny you say that, by the way.
[1321.24 --> 1327.70]  I was just going to say because I also have a young child and I try to tell her the same thing and other people and they struggle to believe it.
[1327.80 --> 1330.46]  I just found it very curious that you jumped in on that.
[1330.46 --> 1339.28]  My son has even said, you know, at 17, I'm not sure I'll get my driver's license because I'm not sure those will still exist, you know, and things like this.
[1339.98 --> 1345.78]  But, you know, those two problems are, you know, about as different from one another as could be.
[1345.92 --> 1351.28]  And certainly we see, you know, problems across industries, whether it's fintech, retail, manufacturing.
[1351.28 --> 1364.50]  You know, I continue to be humbled by the creativity that folks have in finding ways to utilize this technology to create value for their companies.
[1364.50 --> 1379.76]  So I'm kind of interested, since you see so many use cases in your day to day and have seen so much variety, I'm kind of curious to get your perspective on actually how enterprises are leveraging AI.
[1379.76 --> 1394.12]  And what I mean by that is kind of in my mind, how I see various companies approaching AI is you've got on one end of the spectrum, you've got companies that are like really investing in intense research and development.
[1394.12 --> 1405.50]  And maybe they're actually, you know, have their own AI team and they're developing their own model architectures and very unique models, very unique combinations of models and doing those sorts of things.
[1405.50 --> 1413.16]  You've got other groups that are what I would consider more kind of like doing AI cooking in the sense that they get like a recipe.
[1413.16 --> 1417.20]  They get an existing neural network architecture or something like that.
[1417.20 --> 1421.78]  They plug in their own data to create their own model and then go from there.
[1421.88 --> 1426.82]  And then there's other end of the spectrum, definitely a lot of people that are just scaling up inference.
[1426.98 --> 1437.96]  So they might be using a pre-trained model or a combination of pre-trained models or modules, or maybe they're just doing a bit of transfer learning or something like that based on what someone else has previously done.
[1437.96 --> 1442.58]  And so they're not even contributing a ton of data to the situation in terms of training.
[1442.58 --> 1448.56]  I was wondering from your perspective, where are you seeing the biggest investment from enterprises these days?
[1448.72 --> 1451.90]  Or is there a shift one direction or the other on that spectrum?
[1452.40 --> 1453.72]  You know, it's a really good question.
[1454.10 --> 1459.86]  And, you know, it's one that we spend a lot of time thinking about and working with companies on how they're thinking about this problem.
[1460.40 --> 1471.42]  You know, I'll say the companies who I've been most impressed when I hear their strategy around these things, it really comes down to where they choose to buy versus build.
[1471.42 --> 1496.26]  And, you know, from that perspective, you know, one of the things that I think deeply about and that I think others do as well is this idea that, you know, if you can buy a solution, right, you know, whether it's a, you know, contact center AI, our kind of intelligent, you know, virtual assistant or contact agent in your call center, our document understanding.
[1496.26 --> 1509.30]  These technologies that are powered by AI, you know, like these make a ton of sense for companies to buy because for most folks, you know, your contact center isn't the primary point of differentiation for you.
[1509.30 --> 1525.92]  And now, you know, as you move kind of further down the stack, you know, I think the question becomes, you know, where are you comfortable using AI to accelerate your business and gain efficiencies in your business?
[1525.92 --> 1528.90]  And where does that do those efficiencies?
[1529.42 --> 1532.90]  Where are they tied to your competitive advantage as a company?
[1533.36 --> 1542.22]  And fundamentally, the idea of buying your AI makes a ton of sense if it's something that you're very comfortable with your competitor buying as well.
[1542.22 --> 1554.96]  But when it comes to what you should build, it really comes down to where are the unique areas that you think you could kind of, you know, express some differentiation in that industry.
[1554.96 --> 1571.88]  And, you know, so if I take retail as an example, we'll see retailers who are, you know, happy to buy a recommendation system, but they want to optimize the back end and their supply chain deeply because that's how they believe they can stand out.
[1571.90 --> 1578.78]  Or maybe they'll want to highly optimize their promotional capabilities or something along or their forecasting capabilities.
[1578.78 --> 1588.88]  Whereas others may say, you know, listen, you know, forecasting and supply chain, I'm happy to kind of work with a partner and get the best in class that is easily available to me.
[1588.88 --> 1594.18]  But I really want to stand out on our usability or our recommendations and things of that nature.
[1594.66 --> 1597.28]  And that's how I plan on setting us apart from others.
[1597.42 --> 1603.68]  And, you know, I think that that's a conversation that companies have been having for a long time with regards to the software they're building.
[1603.68 --> 1618.42]  And, you know, if I think over the last decade of the number of industries where the leader in that industry has almost become a, you know, hybrid software company, right?
[1618.46 --> 1629.70]  Whether it's a retailer who's become more or less a software company or a healthcare provider who has a giant software investment, you know, those same decisions that have powered that kind of investment over the last decade.
[1629.70 --> 1638.94]  I think now we're seeing that same set of decisions being applied to how they'll invest in intelligent computing and where they'll choose to build versus buy.
[1639.10 --> 1646.26]  So I'm not seeing kind of a wholesale like, hey, people are, you know, giving up notebooks and are only going to go buy from now on or vice versa.
[1646.26 --> 1654.92]  It's really around how companies will choose where they, you know, are willing to build versus where they're willing to buy and how that aligns to their strategy.
[1655.48 --> 1657.50]  So I love your perspective there.
[1657.50 --> 1669.82]  You know, kind of the business take on where you're going to choose to invest in adding value and how you create competitive advantage using these types of AI tools for your own organization.
[1669.82 --> 1688.28]  And so I found myself, as you were saying that, I found myself wondering, you know, what do you think some of the big challenges that you see people trying to create competitive advantage for themselves where it's not the run of the mill stuff where they're just, you know, taking their data and doing, you know, doing a little bit transfer learning and creating their own version of the same model.
[1688.28 --> 1693.26]  But the things where people are saying, this is where our organization wants to make a mark.
[1693.42 --> 1701.60]  Are there any examples that have particularly surprised you or caught your attention in terms of big challenges that organizations are staking themselves on?
[1702.30 --> 1703.62]  You know, it's an interesting one.
[1704.06 --> 1707.32]  You know, my life is spent trying to make it easier for them.
[1707.32 --> 1707.80]  Right.
[1708.24 --> 1719.02]  And so, you know, and I'll say I continue to believe that one of the biggest challenges in this space is actually far to the left of machine learning.
[1719.02 --> 1747.04]  And, you know, when I say left, I kind of mean in a workflow, you know, if I start with kind of data acquisition at the left hand side and I end up with a model and production at the right hand side, you know, that kind of data acquisition, that data cleansing, you know, I'll tell you the number of organizations who are, you know, where I'll talk to data scientists and they'll say, yeah, the data is decently clean and I know where to get it, but I can't get it because there's organizational silos and this other organization owns the data.
[1747.04 --> 1749.36]  And I can't do machine learning on it or something like that.
[1749.60 --> 1750.60]  Really common problem, too.
[1750.74 --> 1751.10]  Yeah.
[1751.24 --> 1753.48]  And these are the things that just break my heart.
[1753.48 --> 1769.22]  And, you know, one of the exciting things for me about working with Google Cloud is that the tight integration between our AI team and our analytics team results in some opportunities for customers to much more easily do these things.
[1769.34 --> 1771.26]  So a great example would be BigQuery.
[1771.26 --> 1787.40]  So BigQuery is Google's hyperscale data warehouse product that I'll say, if you haven't played with it, you should, because it is, you know, an order of magnitude kind of faster and more scalable than anything I've gotten an opportunity to play with.
[1787.46 --> 1791.44]  And I came into machine learning by running data warehouses in many ways.
[1791.44 --> 1793.76]  And so, you know, it's close to home for me.
[1793.90 --> 1802.42]  And so, but, you know, today you can build machine learning models in BigQuery using SQL as your programming language.
[1802.66 --> 1812.62]  And so, like, you can train an XGBoost model or train a TensorFlow model all from kind of the SQL UI that data analysts would be accustomed to.
[1812.62 --> 1829.78]  And so, you know, it's integrations like that that I hope can help us break down some of these barriers that are, you know, I'll say often they're blamed on tech, but often the problems are as much policy as they are tech.
[1829.78 --> 1844.86]  And, you know, I think the key is, can we simplify the governance for folks, not remove it by any means, but simplify it so that it becomes much easier and much less scary so that they can get to the point of extracting value from their data even more quickly.
[1844.86 --> 1857.32]  I know one of the things that I've hit occasionally is, you know, because you're working in the cloud and people, you know, in large enterprises have traditionally had their data in their local data centers.
[1857.32 --> 1862.26]  And maybe there's restrictions like governance things like you were talking about around moving that data around.
[1862.70 --> 1871.22]  Do you still see that popping up in terms of people being hesitant to utilize cloud resources for AI just because they have to move the data around?
[1871.22 --> 1882.24]  Or do you see any progress on that front in terms of people being more willing to invest in moving their training data set to the cloud and managing it there?
[1882.98 --> 1883.54]  Absolutely.
[1884.22 --> 1886.46]  You know, customers are getting more comfortable.
[1886.54 --> 1888.84]  I think this problem is being solved in two directions.
[1888.84 --> 1903.20]  One is, you know, the clouds in general and Google in specific with Google's Anthos, which is our ability to run a Kubernetes cluster across a data center and cloud as if it were kind of one Kubernetes cluster.
[1903.34 --> 1905.10]  Sort of like a hybrid deal.
[1905.74 --> 1915.90]  You know, technologies like that start to, you know, diminish the damage of saying, hey, I can only have my data here and I can't move it elsewhere kind of thing.
[1915.90 --> 1919.00]  Right. And so, you know, in one direction, there are strategies like that.
[1919.00 --> 1934.48]  And then, you know, in the other direction, as cloud continues to grow and, you know, I will routinely meet companies who will say, you know, well, my industry and, you know, you can fill in with whatever industry doesn't allow me to put data in the cloud.
[1934.48 --> 1941.66]  And, you know, we'll talk to them about how many references we have in their industry who are putting data in the cloud.
[1941.84 --> 1957.30]  And, you know, it very quickly, they realize that it's not their industry, it's their company or even their department that has built these rules probably years ago before it was understood the benefits of things like cloud security and reliability and resiliency.
[1957.30 --> 1967.58]  And so, you know, I think those kinds of blockers are kind of falling by the wayside, either because companies are realizing that the cloud is not as scary as maybe they imagined.
[1967.80 --> 1971.44]  And then secondly, because the cloud is coming to the customers in a big way.
[1971.44 --> 1977.56]  So, you know, one of the things is we kind of talk about Google's cloud AI and using TensorFlow in the cloud.
[1977.88 --> 1982.26]  I know for me, using Colab has been a real game changer.
[1982.76 --> 1987.48]  It is, I will just go ahead and say it is my favorite cloud environment to work in.
[1987.80 --> 1989.90]  And I know a lot of other people who feel the same way.
[1990.10 --> 1992.74]  And so I've kind of stuck my own bias out there.
[1992.74 --> 2007.46]  You know, what kind of insights have you had into the future of how we're going to use these tools in the cloud, where Colab might be going specifically, and what kinds of, you know, integrations will we continue to see and accelerators will we continue to see in these types of environments?
[2007.94 --> 2021.18]  Yeah, you know, whether it's Colab, or whether it's notebooks on Kaggle, or whether it's Google's own Google Clouds, you know, Jupiter as a service or Jupiter notebook service, you know, I continue to be excited.
[2021.18 --> 2021.78]  Excited.
[2022.28 --> 2024.94]  And I'll be honest, slightly disappointed.
[2025.08 --> 2026.04]  And I'll get into that in a moment.
[2026.30 --> 2031.52]  I continue to be excited by the evolution of tooling for machine learning.
[2031.90 --> 2034.46]  You know, I say slightly disappointed, I wish it were moving faster.
[2035.00 --> 2050.94]  And, you know, I think you're starting to see that with more and more kind of opinionated workflows, right, around, you know, whether it's AutoML type of workflows, or, you know, kind of rich templates, to your point of the cooking recipes, right, that,
[2051.18 --> 2056.58]  can kind of get people 90% of the way there, and then let them adjust the part that matters to them.
[2056.58 --> 2064.74]  I, you know, I continue to believe that the way we're doing machine learning today probably isn't the way we'll be doing machine learning a decade from now.
[2064.80 --> 2067.08]  And, you know, I often think about software development.
[2067.08 --> 2080.74]  And, you know, if we were to rewind the clock on software development by, you know, 20 years, you know, concepts like regression testing and unit testing and these kinds of things, you know, weren't a part of the everyday software development lifecycle.
[2081.02 --> 2090.58]  Today, you know, if you went to go deploy something and you hadn't done, you hadn't passed it through a regression testing suite, you know, we would kind of think you're irresponsible.
[2090.58 --> 2095.16]  And, you know, we don't have those same concepts yet for machine learning.
[2095.52 --> 2109.88]  And, you know, to me, one of the reasons why it's so exciting to work in this space is that I feel like we are getting to develop the kind of, you know, next generation of standards around how people will develop machine learning.
[2109.88 --> 2124.32]  And, you know, whether it's, you know, things like, you know, pipeline technology to improve CICD experiences, you know, whether it's specific TensorFlow modules built into TF Hub or notebooks, you know, notebook examples on Colab or on Kaggle.
[2124.42 --> 2130.72]  This is an area that you can feel is, you know, very likely going to evolve very quickly over the next few years.
[2130.72 --> 2136.22]  Yeah, I was just going to mention before we get off of Colab and some of the things there.
[2136.52 --> 2143.24]  There's certainly, as you mentioned, there's standards that need to be developed and rigorous things that need to be developed.
[2143.34 --> 2147.20]  And I know guests like Joel Gruse and others on the podcast have talked about that.
[2147.20 --> 2163.00]  But on the other side of things, like I've been working with this Masakane collaboration recently, which is trying to involve research groups and people on the African continent into developing machine translation technology for the languages that they care about.
[2163.00 --> 2176.02]  And a central piece of that is the fact that they're able to very quickly onboard participants into their working group because they have a set of Google Colab notebooks that they're able to spin up.
[2176.14 --> 2177.56]  They're able to run in their browser.
[2177.80 --> 2182.20]  They're able to have access to a GPU to get them started on training baselines.
[2182.54 --> 2185.68]  And they don't have to have access to their own GPU.
[2185.68 --> 2195.12]  They don't have to even have a lot of experience in a local environment set up with a IDE that's all set up to do certain things and all of that.
[2195.28 --> 2203.68]  So that's really, I think, been crucial to that collaboration is the fact that they are able to onboard quickly into that.
[2203.78 --> 2213.58]  Now, obviously, as you productize things, as you were mentioning, as you work with enterprises that have certain concerns, there's definitely a matter, matters of integrity and that sort of thing.
[2213.58 --> 2217.46]  And robustness that need to be dealt with.
[2217.56 --> 2220.24]  But I think some of those concerns are being addressed.
[2220.36 --> 2231.26]  But also on the other side, there's a lot of tooling that's being developed out there that's really helping make this technology more accessible to more groups of people, which is really exciting for me.
[2231.26 --> 2243.82]  Absolutely. And I couldn't be more excited to be a part of the kind of the work that is going into this democratization process and widening the field of machine learning developers and creators.
[2244.30 --> 2251.84]  And then, you know, fundamentally, though, I'll say I always worry about whether or not those models are going to get into production.
[2251.84 --> 2262.90]  Right. Because one of the things we know is that the vast majority of machine learning that gets built never makes it into the kind of, you know, the area where the inferences can now start creating value.
[2262.98 --> 2268.02]  Right. All too often it gets built, gets built on someone's laptop or maybe in the cloud.
[2268.02 --> 2275.92]  And then, you know, they're never able to actually integrate it into the application or integrate it into that point where it could create value.
[2276.12 --> 2293.84]  And, you know, this is an area where we invest deeply to try and ensure that, like, hey, once I've built that model, whether it's in Colab or, you know, wherever I built it, that I can easily put it into a place where I can call it for inference and kind of gain the full value of the model.
[2293.84 --> 2304.62]  As data scientists, I think it's very easy to become attached to the training as the, you know, the training and kind of the AUC curves or what have you as the point of success.
[2304.62 --> 2316.10]  But, you know, for me, really, the success comes when those inferences are creating the value that we all set out to or the goal we all set out to achieve when we first started trying to build the model.
[2316.76 --> 2317.96]  That's a great point that you're making.
[2317.96 --> 2326.86]  We do tend to get caught up in our own training and thinking of as the training is the thing versus the value that you're creating with the model after you deploy it.
[2327.18 --> 2327.84]  I would feel remiss.
[2327.94 --> 2328.90]  I'm kind of curious.
[2329.26 --> 2334.96]  I just wanted to go back a little bit to your personal bio for a minute and definitely not wanting to get into the politics of competition and stuff.
[2335.10 --> 2337.84]  But coming from AWS, you came into Google.
[2337.84 --> 2341.64]  You had a hand, obviously, in creating SageMaker.
[2342.06 --> 2349.02]  And obviously, like you would with any job moving to another, you learn and you get better and you gain knowledge as you do that.
[2349.02 --> 2360.16]  Is there anything that comes to mind that you learned from that previous experience and, you know, and definitely not putting down SageMaker, but just like, you know, you went through that process and you gained expertise.
[2360.48 --> 2363.26]  And then you came to Google and you started working on Google AI.
[2363.62 --> 2366.50]  Is there anything that really helped you as you came across there?
[2366.50 --> 2376.86]  You know, I was unprepared for the benefit of sitting side by side with the Google's research groups.
[2377.22 --> 2383.24]  You know, Google is clearly a leader, if not the leader in AI and machine learning.
[2383.24 --> 2392.42]  And to get to, you know, sit shoulder to shoulder with Jeff Dean and others as they solve some of the most complex machine learning problems in the world.
[2392.42 --> 2416.34]  And then taking the components with the kind of fundamentals or the, you know, the primitives that they've had to use, you know, extracting those out of some of these world class problems, you know, and putting them into an environment where enterprises of all levels can interact with them is something that, you know, I was just unprepared for it.
[2416.34 --> 2424.24]  And to, you know, to give an example, you know, we're using, you know, if you look at DeepMind and what DeepMind has done with AlphaGo and with StarCraft.
[2424.24 --> 2432.14]  And then, you know, we use that same technology for optimizing manufacturing facilities, right?
[2432.26 --> 2436.54]  And, you know, optimizing the control systems in manufacturing facilities.
[2437.24 --> 2452.70]  And, you know, that kind of research, the tight connection between kind of research and the practical applications and practical tools we're building is just something I don't think you could get anywhere in the world like you can get it at Google.
[2452.70 --> 2466.66]  I know one of the things that I feel a lot as someone who isn't at Google but keeps a close eye on what's going on in AI, it often seems like there's just so much happening so quickly.
[2467.10 --> 2469.16]  And obviously, Google is doing a lot.
[2469.62 --> 2472.48]  Other groups are doing a huge amount of research.
[2472.68 --> 2480.46]  And it just seems like, oh, you know, like recently I remember Facebook released this like multi-language question answering data set.
[2480.46 --> 2481.80]  And I was like, oh, this is really cool.
[2481.88 --> 2485.10]  This is like something I wanted to see for a while.
[2485.20 --> 2486.40]  And so I started playing with it.
[2486.48 --> 2496.48]  And before I even got done, like, you know, figuring out some of what they had done and how it worked in the format, there were already at like, I think Google came out with another one.
[2496.48 --> 2504.90]  And there was like another, there's been like three or four non-English question answering data sets and models that have come out after that.
[2504.90 --> 2520.88]  As someone who is kind of helping shape the future of Google Cloud AI and in those discussions, how do you parse through all of the advances that are just happening so quick and what people are wanting to do?
[2520.88 --> 2523.14]  How do you keep from getting left behind?
[2523.26 --> 2528.86]  I guess that tight integration is part of it, but it still seems like a hard thing to keep up with.
[2528.94 --> 2533.32]  Yeah, herding ducks, I think, would probably be the right idea here, right?
[2533.60 --> 2541.60]  I mean, you know, it is amazing because you'll sit there and think, you know, my goodness, I couldn't be any deeper on this topic than I am today.
[2541.74 --> 2549.22]  And then you'll find, you know, a team will announce that they've done something that's, you know, two orders of magnitude deeper than where we were.
[2549.22 --> 2551.76]  And it's kind of, you know, you just sit there and are like, wow.
[2552.28 --> 2561.16]  And so, you know, really it's, you know, getting to know all those folks and keeping close with them so that we can look at not what they're doing today, but where are they going?
[2561.84 --> 2567.78]  And where are they going to be six months from now, 18 months from now, and 36 months from now?
[2567.78 --> 2572.06]  And how do we ensure that we're building towards that fact?
[2572.16 --> 2584.32]  I mean, and, you know, in kind of cloud where I sit, you know, I look at things like GANs or things like, you know, reinforcement learning and say, you know, well, listen, most enterprises aren't running machine learning.
[2584.60 --> 2589.38]  You know, most enterprises, if they're running machine learning, they're, you know, they're running scikit models at this point.
[2589.38 --> 2594.92]  And so, like, you know, what is the value of GANs to me right now outside of an academic environment?
[2595.34 --> 2602.30]  But then, you know, what we find is very quickly, you know, far more quickly than I would have imagined, companies start jumping on some of these technologies.
[2602.62 --> 2604.58]  And we find new and exciting ways.
[2604.58 --> 2612.06]  And, you know, so, for example, we are running a Kaggle competition, a reinforcement learning Kaggle competition right now, first of its kind within Kaggle.
[2612.54 --> 2621.28]  And, you know, seeing some really interesting ways in which users and developers who have never done reinforcement learning before are starting to interact with this.
[2621.44 --> 2629.56]  And by watching the conversations they're having and the challenges they're having, I think it allows us to build better products, you know, as we come out of that.
[2629.56 --> 2634.76]  So, I guess, you know, as we kind of work our way to the end here, people are listening to this.
[2635.08 --> 2639.98]  They've gotten a little bit of knowledge about cloud AI, if they haven't already, and TensorFlow.
[2640.58 --> 2651.04]  What would you recommend is the best way for people to get their hands started in TensorFlow and TensorFlow in the context of cloud AI as an enterprise customer?
[2651.04 --> 2655.96]  You know, obviously, there's the crash course that Google has, which kind of gets you started there.
[2655.96 --> 2661.14]  But could you take us a little deeper into how people can steer into all these tools and get started with you?
[2661.38 --> 2672.08]  Yeah, I mean, so, you know, I think if you're getting started fresh and, you know, haven't touched this technology before, then I would certainly recommend heading towards Kaggle and some of their educational resources.
[2672.08 --> 2686.18]  I think, you know, they have things like, you know, 10 weeks to, you know, coding and Python, coding and Python in 10 weeks, and, you know, other things around, you know, learning a number of the basics and starting to get engaged with kind of machine learning.
[2686.42 --> 2688.72]  And so, you know, I think that's a great place to start if you're newer.
[2688.72 --> 2701.06]  If this is an area where you have kind of skills and expertise, then absolutely, you know, continuing to, you know, utilize Kaggle and their competitions and their wide variety of code samples, CoLab as well.
[2701.42 --> 2713.92]  But then, you know, going to cloud.google.com and our heading to our AI tab, and then, you know, honestly, going to our deep learning environments and spinning up a VM with deep learning on it.
[2713.92 --> 2721.92]  But, you know, I remember years ago when I was kind of working in supply chain, I had a really strong kind of econometrician on the team.
[2721.96 --> 2725.14]  And I said, hey, why don't you go install a deep learning package?
[2725.44 --> 2731.20]  I can't remember if at that point it was, you know, Theano or TensorFlow or, you know, kind of earlier days.
[2731.88 --> 2736.18]  And, you know, install a package, get it going and, you know, let me know what you think.
[2736.18 --> 2741.50]  And, you know, the next week I met with him and he said, you know, I worked at it for a number of hours, couldn't get it running.
[2741.50 --> 2745.60]  And so, you know, I went back to the stuff I know because I knew I could create value there.
[2745.70 --> 2751.08]  Well, with our deep learning environments, our deep learning VMs and what have you, all you have to do is click on the thing.
[2751.30 --> 2761.82]  And now you have a TensorFlow experience or, you know, open a notebook with a GPU as a back end and you have everything you need to run, you know, strong and run fast there.
[2761.94 --> 2768.44]  And so I would just tell people, dive in, find some code samples, try and break them, try and mess them up and go from there.
[2768.78 --> 2771.16]  Awesome. Well, appreciate that perspective.
[2771.50 --> 2776.02]  And we appreciate you taking time from all of your work to come and chat with us.
[2776.08 --> 2777.60]  It's been been a great time.
[2777.68 --> 2782.52]  I know I've learned a lot and excited to continue exploring what's what's coming out of Google.
[2782.70 --> 2784.76]  And thank you so much for for joining us.
[2784.76 --> 2792.04]  We'll mention all the things that you just did in our show notes and hope to stay in contact and see you at a conference or something soon.
[2792.50 --> 2793.20]  Yep. Thanks a lot.
[2793.62 --> 2794.88]  Absolutely. Thank you.
[2794.88 --> 2800.46]  Thank you for listening to Practical AI.
[2800.46 --> 2810.84]  If you're not following Practical AI FM on Twitter, you're missing out on clips and highlights from past episodes, links and repos from around the AI and data science community and more.
[2811.26 --> 2811.80]  Follow us.
[2811.94 --> 2813.20]  Practical AI FM.
[2813.36 --> 2814.12]  You won't regret it.
[2814.52 --> 2817.20]  Practical AI is hosted by Daniel Whitenack and Chris Benson.
[2817.20 --> 2818.96]  It's produced by me, Jared Santo.
[2819.36 --> 2822.16]  And our music is brought to you by the Beat Freak, Breakmaster Cylinder.
[2822.64 --> 2823.82]  We have awesome sponsors.
[2823.98 --> 2824.56]  Support them.
[2824.72 --> 2825.50]  They support the show.
[2825.50 --> 2830.16]  So special thanks to Fastly, Linode and Rollbar for helping us do what we do.
[2830.50 --> 2833.86]  If you aren't receiving ChangeLog Weekly every Sunday, you are missing out.
[2834.24 --> 2836.42]  It's our take on this week in the world of software.
[2836.78 --> 2838.20]  What's interesting and why?
[2838.56 --> 2841.60]  Head to changelog.com slash weekly to subscribe.
[2842.00 --> 2843.66]  Get it for the price of a free cheeseburger.
[2844.44 --> 2845.36]  Thanks again for listening.
[2845.68 --> 2846.68]  We'll talk to you next week.
[2855.50 --> 2856.50]  Bye.
[2856.50 --> 2857.50]  Bye.
