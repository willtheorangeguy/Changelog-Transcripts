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
[86.78 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.28]  And now onto the show.
[106.66 --> 109.88]  Welcome to another episode of the Practical AI podcast.
[110.38 --> 112.18]  I'm your host, Chris Benson.
[112.56 --> 116.22]  I am the chief AI strategist at Lockheed Martin.
[116.62 --> 122.10]  Today, I am recording live from the O'Reilly AI conference in New York City.
[122.10 --> 126.68]  The date is Wednesday, April 17th, when we're doing the recording.
[127.20 --> 131.72]  And I have the great privilege today of having a conversation with Ben Lorica.
[131.88 --> 133.64]  And did I get your last name pronounced correctly?
[133.96 --> 134.90]  That's perfect, Chris.
[135.02 --> 135.28]  Okay.
[135.52 --> 138.86]  And Ben is the chief data scientist for O'Reilly Media.
[139.34 --> 143.90]  He is also the program chair for the Strata conference and this AI conference.
[143.90 --> 146.56]  And it's a pleasure to have you on the show.
[147.08 --> 148.30]  Thanks for having me.
[148.56 --> 153.20]  So really hoping to cover a bunch of different topics and stuff.
[153.34 --> 156.32]  But I noticed I wanted to start out with that.
[156.50 --> 162.80]  I noticed that you had put out a publication through O'Reilly called AI Adoption in the Enterprise.
[163.04 --> 167.30]  It's an e-book that I know that our listeners can go and download.
[167.46 --> 169.18]  And we'll put a link to that in the show notes.
[169.18 --> 175.90]  And I was just wanting to see if you could kind of give us a little overview of what you're covering
[175.90 --> 181.34]  and maybe do a couple of deep dives, enough to at least tease everyone on what you've hit in the book.
[181.64 --> 188.58]  So I think at a high level, we wanted to understand the state of adoption of AI,
[189.26 --> 193.68]  which for the most part, these days, refers to machine learning technologies.
[193.68 --> 202.32]  And so the first thing we did was we tried to get people to kind of self-describe their level of maturity.
[202.94 --> 212.42]  So at a high level, so we consider people with mature practice to be companies
[212.42 --> 216.28]  that have a certain number of years of having models in production.
[217.10 --> 222.88]  And then on the lower end, we have companies who are just at the evaluation and exploring stage.
[222.88 --> 229.42]  So if you take these two buckets, mature and exploring, so a couple of interesting things that jump out.
[229.52 --> 234.98]  One is level of investments, plan level of investments.
[236.30 --> 243.08]  The people, the organizations with mature practice plan to invest a substantial amount of money
[243.08 --> 247.52]  compared to the ones who are still in the exploratory stage.
[247.52 --> 250.76]  And do you think that's mainly just because they're still kind of convincing themselves,
[250.92 --> 252.86]  proving out the technology and its usefulness?
[253.16 --> 254.64]  Yeah, I think so.
[255.54 --> 263.16]  But so before I dive into that, so for us, that seems to indicate that maybe the gap between the leaders
[263.16 --> 267.90]  and the laggards may widen a little more as far as machine learning.
[267.90 --> 274.48]  So as far as what are some of the key bottlenecks that the respondents cited.
[274.94 --> 279.80]  So again, there's a distinction between those in the exploratory stage and those with mature practice.
[280.32 --> 289.60]  The ones in the exploratory stage cited problems identifying the right use cases and company culture, right?
[289.62 --> 293.30]  So convincing people to invest in AI technologies.
[293.30 --> 299.84]  The ones who consider themselves more mature cite lack of data.
[300.06 --> 306.28]  So they may have an idea, but they haven't quite collected the right data to execute on that project,
[306.66 --> 307.84]  and lack of skilled people.
[308.24 --> 308.48]  Gotcha.
[309.68 --> 315.02]  So are you saying that even the more mature ones are struggling with lack of data at this point in the survey?
[315.02 --> 325.86]  I think that companies always, you know, so once you start down the machine learning and AI path,
[326.28 --> 332.06]  you probably start generating ideas and use cases because you gain more confidence.
[333.38 --> 339.74]  And for many of these use cases, you may not have the right data yet, right?
[339.74 --> 340.00]  Gotcha.
[340.18 --> 343.02]  You have to start generating the data and then execute.
[343.02 --> 349.88]  So could you kind of just taking that a little farther, could you kind of describe maybe what a typical,
[350.58 --> 354.08]  on the forefront, those who are kind of leading the way and are making the investments,
[354.46 --> 363.52]  what some of those may look like based on what the survey results showed in terms of did you go into use cases in it at all
[363.52 --> 365.72]  or just talking about whether or not they were making the investment?
[365.72 --> 368.64]  So we didn't have them describe their use cases.
[368.64 --> 379.72]  So, but I think at a high level, so the more advanced companies are probably using more deep learning these days, right?
[379.72 --> 379.84]  Sure.
[380.00 --> 386.64]  So I think that companies who have existing machine learning products or applications
[386.64 --> 394.38]  have been evaluating how deep learning can either augment or replace their existing systems.
[394.50 --> 394.76]  Sure.
[394.76 --> 402.66]  So this applies not to kind of the traditional areas that you associate deep learning with,
[402.72 --> 406.38]  like computer vision or speech or even text,
[406.56 --> 413.74]  but problems that involve structured data, like recommender systems and time series forecasting.
[413.74 --> 422.54]  So I think companies are beginning to examine whether or not deep learning can play a role in improving those systems.
[423.74 --> 432.46]  And then the really bleeding edge companies, I think, are beginning to examine machine learning against live data,
[432.56 --> 435.52]  and now you're starting to enter the world of reinforcement learning.
[435.52 --> 448.84]  So I don't know if you were in the keynotes this morning, but Tony Jabara from Netflix talked about their work in adding contextual bandits to their recommender systems.
[449.22 --> 455.76]  So now you're beginning to enter the world of reinforcement learning, which I think is super interesting.
[456.42 --> 463.62]  At this conference, we had a tutorial on an open source project from UC Berkeley called Ray from Rice Lab.
[463.62 --> 475.00]  And it's a distributed computing framework that you can use for a lot of things because it's got a certain amount of flexibility.
[475.96 --> 483.42]  So the Rice Lab team have written some libraries on top of it, including one for hyperparameter tuning.
[484.48 --> 487.78]  They have a library on top of it called Moden,
[487.78 --> 493.62]  which for people who are listening who are familiar with pandas in the Python world.
[494.14 --> 500.94]  So Moden is basically pandas on Ray, which means it runs faster on your laptop,
[501.46 --> 504.34]  and it automatically scales a cluster if you need it to.
[504.40 --> 506.06]  All you need is to add one line of code.
[506.70 --> 513.78]  And then it turns out the most popular library on top of Ray is RLLib,
[513.78 --> 517.00]  which is the reinforcement learning library.
[517.68 --> 524.46]  And so what's nice about this is now reinforcement learning becomes a library that you can just use.
[524.46 --> 527.34]  If you're a developer, you don't need to write your own algorithms.
[527.86 --> 531.52]  So the experts can use Ray to write algorithms.
[531.68 --> 538.72]  And in fact, what they've designed Ray so that both users and reinforcement learning researchers
[538.72 --> 542.18]  can find utility in it.
[542.40 --> 545.70]  So it's a great new project to pay attention to.
[545.90 --> 546.70]  No, that sounds great.
[547.20 --> 551.12]  Oh, so one thing I should add is that actually Ant Finance,
[551.78 --> 554.40]  which is the largest unicorn company in the world,
[554.54 --> 556.54]  it's a financial services in China.
[557.80 --> 561.18]  I don't know the exact valuation, but I think it's over $100 billion.
[561.64 --> 562.44]  Wow, big.
[562.44 --> 568.58]  Yeah, and so they're using Ray in production in multiple use cases.
[569.14 --> 572.44]  One of them is real-time personalization recommendation.
[573.10 --> 573.66]  Okay.
[574.24 --> 578.90]  Well, you talked also about some of the ones that we're just exploring still.
[579.68 --> 582.24]  And I know in this book that you guys put out,
[582.32 --> 585.74]  you also talk about some of the things that are holding back adoption of AI.
[586.06 --> 587.62]  Can you kind of talk a little bit about that?
[587.62 --> 591.14]  Because actually, you know, I know that we have a lot of listeners,
[591.56 --> 593.58]  and some of them have been doing it for a while,
[593.88 --> 595.40]  but we also have listeners who are trying,
[595.60 --> 599.28]  one of the reasons they listen is to try to kind of figure their way into the space.
[599.42 --> 602.40]  What have you found on things that are holding back adoption of AI?
[602.84 --> 610.26]  So as I said, the people in the valuation stage cite problems identifying the right use cases.
[610.54 --> 610.76]  Yep.
[610.76 --> 616.36]  Which to me points to one thing Chris said I think sometimes we undervalue,
[616.56 --> 623.30]  which is the need to educate not just your developers and engineers about machine learning,
[623.42 --> 625.08]  but your organization, right?
[625.12 --> 626.84]  So your managers and decision makers.
[627.26 --> 633.72]  Think about when we started talking about big data and how data can drive decision making.
[634.14 --> 638.78]  Well, you had to educate your workforce about how to make decisions using data.
[638.78 --> 641.94]  So I think the same thing with machine learning and AI.
[642.70 --> 651.38]  There's a certain amount of education that needs to be done so that your organization is aware about what's possible,
[651.76 --> 659.72]  what are the limitations, and what are the requirements for the technologies that we have today.
[659.72 --> 666.08]  And then the second main bottleneck they cite is related to this as well,
[666.16 --> 669.72]  which is basically just convincing the rest of the company.
[670.56 --> 673.58]  So company culture about investing in AI.
[673.94 --> 674.06]  Sure.
[674.06 --> 686.58]  And so one of the things that we found is that the companies that seem to have taken initial steps and succeeded in terms of using machine learning and AI,
[687.04 --> 692.82]  they tended to build on existing analytics infrastructure.
[693.48 --> 695.60]  Just kind of iteratively moving it on.
[695.60 --> 698.36]  Yeah, so you have data that you were using for something else.
[698.52 --> 701.16]  Maybe you start using it for machine learning and AI.
[702.76 --> 707.86]  Layer a bit of machine learning on top of your decision making.
[708.18 --> 711.74]  So doing that iteratively in that way is probably kind of one of those success factors
[711.74 --> 716.02]  and that instead of starting something entirely new, you take an existing team.
[716.22 --> 720.74]  Yeah, you might tell yourself, oh, this computer vision is cool.
[720.88 --> 722.64]  Let's do a project in computer vision.
[722.78 --> 729.20]  But then now you have to gather the data, develop kind of the expertise on how to store that data.
[729.66 --> 734.88]  And so maybe you're better off starting with things you're already familiar with.
[735.68 --> 741.14]  And the rest of the organization already appreciates whatever KPIs you have.
[741.14 --> 745.70]  So maybe improve those KPIs by layering in this new technology.
[746.08 --> 752.94]  I know speaking from personal experience in industry, getting the data that you need.
[753.98 --> 757.10]  I have one without naming the company.
[757.36 --> 759.92]  It was a company that I was working for.
[760.50 --> 764.98]  And the CTO of the company said, we have all the data you could ever want.
[765.34 --> 770.74]  The thing that I found in reality was it wasn't the right data for doing the kinds of projects that we wanted.
[771.14 --> 776.40]  And then a lot of other companies simply don't have the data pipelining at all in position.
[776.40 --> 786.24]  Any thoughts toward what companies can do in terms of getting that kind of prerequisite work done so that they can get to productive machine learning?
[786.24 --> 786.76]  Absolutely.
[786.76 --> 799.40]  So one of the things that I've been trying to socialize and evangelize is that if you want to build an organization where you can have a sustainable machine learning practice,
[799.40 --> 802.92]  you can't ignore some of these foundational technologies that you described.
[802.92 --> 808.94]  So things that you might find, what does this have to do with AI?
[809.28 --> 816.22]  So like data integration and ETL, data governance, data lineage.
[818.28 --> 823.46]  And then that's the data aspect of what you need to do.
[823.46 --> 831.22]  But then it turns out machine learning, people are realizing, requires some special tools for machine learning development.
[831.86 --> 840.74]  So one of the most popular open source projects over the last year is a project called MLflow out of Databricks,
[840.80 --> 842.74]  which full disclosure, I'm an advisor to.
[843.60 --> 843.92]  Okay.
[843.92 --> 854.40]  It's a 10-month-old project, and it's basically a project which has three components, and you can use any of the components.
[854.90 --> 858.02]  But it's meant to facilitate ML development.
[858.36 --> 858.50]  Okay.
[858.50 --> 862.72]  So within 10 months, over 200 companies are using it.
[862.82 --> 863.54]  Oh, that's fantastic.
[863.54 --> 865.84]  They have contributors from over 40 companies.
[865.84 --> 875.44]  And then what they're finding is one of the most popular components of MLflow is the component that helps you track and manage machine learning experiments.
[877.08 --> 883.60]  And so then there's the whole tooling for helping you develop machine learning.
[883.60 --> 892.88]  But I think if you look ahead, if you use more and more machine learning, and machine learning becomes more and more important to your company,
[894.24 --> 897.82]  the models themselves will become kind of assets that you have to manage.
[897.94 --> 904.42]  Just like you have data and data assets and a chief data officer or data governance, data catalog,
[904.90 --> 910.72]  will have to have tools for model governance, model operations, right?
[910.72 --> 916.88]  So monitoring, tracking, alerts, dashboards for different personas, right?
[916.98 --> 921.88]  So business users may have a dashboard for tracking models.
[922.20 --> 924.60]  The data engineers may have their own dashboard.
[925.04 --> 926.98]  The data scientists may have their own dashboard.
[927.34 --> 933.80]  But also just a catalog listing all of the models, their state, who built them, all these things.
[933.80 --> 943.22]  This episode is brought to you by StrongDM.
[943.48 --> 948.18]  StrongDM makes it easy for DevOps to enforce the controls InfoSec teams require,
[948.52 --> 951.82]  manage access to any database, server, and any environment.
[952.30 --> 955.82]  And in this segment, we're talking to Jim Mortco, VP of Engineering at Hearst.
[955.96 --> 959.80]  He's sharing how they're using StrongDM within their team of 90 plus engineers.
[959.80 --> 965.72]  It now takes them just 60 seconds to off-board a team member from a data source.
[966.00 --> 969.54]  We have an engineering team of somewhere in the area of 80 or 90 engineers.
[969.80 --> 974.30]  Because we've got so many services and many databases and so many developers,
[974.30 --> 976.66]  we need a reasonable way to manage access to them.
[977.12 --> 980.70]  It was a somewhat painful and labor-intensive process.
[981.38 --> 985.56]  Our DevOps team would literally have to manage every one of the permissions
[985.56 --> 987.10]  for everybody who wanted access.
[987.98 --> 990.72]  So StrongDM has been a real godsend in that area for us.
[991.10 --> 994.58]  Requests for access to specific databases were pretty much manual.
[994.78 --> 996.18]  Now we've adopted StrongDM.
[996.38 --> 998.38]  It's something that you don't even know is there.
[998.52 --> 999.96]  Once it's installed, it just works.
[1000.04 --> 1000.64]  It's very simple.
[1000.96 --> 1004.82]  We've set up a multitude of data sources so that when somebody's onboarded,
[1004.86 --> 1006.94]  we just give them access to StrongDM.
[1007.20 --> 1008.04]  It's pretty simple.
[1008.40 --> 1011.60]  Our DevOps team, they have a very minimal effort required
[1011.60 --> 1014.64]  to enable each data source to be connected to StrongDM.
[1014.84 --> 1018.56]  And then installing the client software is very, very simple and straightforward.
[1018.80 --> 1021.16]  You can use whatever client you want to to talk to the database.
[1021.30 --> 1022.72]  So there's really no training necessary.
[1023.24 --> 1023.54]  All right.
[1023.56 --> 1027.22]  If your team can benefit from nearly instant onboarding and offboarding
[1027.22 --> 1029.20]  that's fully SOC2 compliant,
[1029.52 --> 1033.10]  head to StrongDM.com to learn more and request a free demo.
[1033.46 --> 1035.46]  Again, StrongDM.com.
[1041.60 --> 1050.66]  To extend that a little bit,
[1051.24 --> 1053.64]  I've also seen that people,
[1054.82 --> 1058.16]  not only are they not necessarily ready for that
[1058.16 --> 1060.02]  as they're trying to get an operation up and running,
[1060.16 --> 1063.44]  but they'll also not have really thought their way through
[1063.44 --> 1066.76]  how do you get the model back into a software stack
[1066.76 --> 1069.24]  and usable out there in a product service,
[1069.24 --> 1072.34]  whatever your target environment is
[1072.34 --> 1073.50]  that you're going to get that model into
[1073.50 --> 1074.40]  and what's the process.
[1074.62 --> 1078.40]  And so not only is there a whole aggregate the data you need,
[1078.48 --> 1079.28]  get the right data,
[1079.60 --> 1082.44]  get it into the right form so that you can use it for training,
[1082.76 --> 1085.28]  but then afterwards when you have a model
[1085.28 --> 1087.42]  that presumably you may be iterating on,
[1087.68 --> 1091.38]  having that feedback loop that not only places the model out there
[1091.38 --> 1092.08]  into the target,
[1092.20 --> 1094.50]  but also is pulling it back in.
[1094.50 --> 1096.92]  Any advice on how people should be thinking
[1096.92 --> 1100.28]  about actually productizing their model,
[1100.36 --> 1101.14]  putting it into production?
[1101.66 --> 1103.14]  Yeah, that's an interesting question
[1103.14 --> 1106.54]  because traditionally data scientists
[1106.54 --> 1110.28]  have been somewhat not involved
[1110.28 --> 1112.02]  with deploying these models
[1112.02 --> 1115.80]  and these analytic products into production.
[1117.26 --> 1119.80]  And in fact, a couple of years ago,
[1119.80 --> 1123.76]  we started noticing in the Bay Area a new job role
[1123.76 --> 1126.66]  with the title machine learning engineer.
[1127.36 --> 1131.16]  And this role sits somewhere in between data science
[1131.16 --> 1135.40]  and data engineering and data ops.
[1135.96 --> 1140.30]  So the focus of this machine learning engineer
[1140.30 --> 1143.66]  is to productionize ML models.
[1144.18 --> 1145.96]  And so that means that they're stronger
[1145.96 --> 1147.84]  on the software engineering side
[1147.84 --> 1149.02]  and data engineering side,
[1149.32 --> 1152.08]  but they have enough data science knowledge
[1152.08 --> 1155.86]  to build some of the more routine models.
[1156.50 --> 1159.96]  And then, so we started hearing about this role
[1159.96 --> 1160.78]  a couple of years ago.
[1160.96 --> 1162.62]  And then about a month ago,
[1162.96 --> 1165.98]  before our Strata data conference in San Francisco,
[1166.08 --> 1167.16]  I threw up a Twitter poll
[1167.16 --> 1171.10]  because I've been hearing that data scientists
[1171.10 --> 1173.10]  were rebranding themselves somewhat
[1173.10 --> 1174.64]  into a machine learning engineer
[1174.64 --> 1176.34]  because the machine learning engineer,
[1176.34 --> 1178.86]  anecdotally I think is higher compensated.
[1179.48 --> 1183.56]  So the poll question was clear and simple,
[1183.72 --> 1186.00]  which was if two years ago
[1186.00 --> 1189.16]  you were describing yourself as a data scientist
[1189.16 --> 1191.00]  or using the title data scientist,
[1191.68 --> 1192.92]  what are you using today?
[1193.42 --> 1196.82]  And so I found over a third said
[1196.82 --> 1199.12]  they're now using the job title machine learning engineer.
[1199.82 --> 1201.64]  So now it might be the case
[1201.64 --> 1204.60]  that some of the data scientists
[1204.60 --> 1208.36]  have upskilled their software engineering skills
[1208.36 --> 1209.98]  and become machine learning engineers,
[1210.16 --> 1212.92]  but there might also be a cohort of them
[1212.92 --> 1216.36]  who have rebranded themselves.
[1216.86 --> 1218.22]  Now the other thing too is that
[1218.22 --> 1222.62]  the tools for going from a model
[1222.62 --> 1224.46]  that's a prototype to production,
[1224.46 --> 1228.90]  so there are startups and companies
[1228.90 --> 1231.92]  trying to build tools to kind of
[1231.92 --> 1235.38]  blur that distinction
[1235.38 --> 1236.68]  so that data scientists
[1236.68 --> 1240.48]  who are working on an internal data science platform
[1240.48 --> 1241.70]  where they can collaborate
[1241.70 --> 1243.98]  can take those models
[1243.98 --> 1245.92]  and deploy them into production systems.
[1245.92 --> 1248.68]  But traditionally the production systems
[1248.68 --> 1253.40]  are run and managed by a different team
[1253.40 --> 1258.90]  and data scientists don't normally wear pagers
[1258.90 --> 1261.56]  and get paged when something goes wrong.
[1261.72 --> 1262.16]  That's true.
[1263.16 --> 1266.16]  So I think that whenever someone tells me
[1266.16 --> 1268.54]  that you don't need to make this distinction,
[1268.80 --> 1269.94]  I always ask them,
[1270.02 --> 1271.76]  so do your data scientists wear pagers?
[1272.58 --> 1274.08]  That's pretty funny actually.
[1274.08 --> 1276.04]  Yeah, so you've kind of gone into
[1276.04 --> 1278.36]  talking about how roles are changing
[1278.36 --> 1279.62]  and so I'm going to ask you
[1279.62 --> 1282.38]  a little bit about skills and skill gaps
[1282.38 --> 1285.34]  and I actually want to lead in a little bit.
[1285.68 --> 1287.92]  One of the things that I have noticed in recent years
[1287.92 --> 1290.38]  as I've been part of organizations
[1290.38 --> 1293.06]  that have started to turn that corner
[1293.06 --> 1296.06]  and try to set up their own AI operations
[1296.06 --> 1298.26]  and make those happen
[1298.26 --> 1300.70]  was that in a lot of cases
[1300.70 --> 1302.54]  the data scientists that were already there
[1302.54 --> 1304.98]  had no experience or real understanding
[1304.98 --> 1305.80]  about deep learning
[1305.80 --> 1307.52]  as they were trying to ramp up
[1307.52 --> 1309.96]  and that it was certainly a distinct skill set
[1309.96 --> 1311.52]  from things that they had done in the past.
[1312.36 --> 1314.34]  What, you know, speaking towards that
[1314.34 --> 1317.72]  and as well as the general set of skills
[1317.72 --> 1319.56]  that it takes to make all this stuff happen
[1319.56 --> 1320.44]  in this space,
[1320.90 --> 1321.64]  what are you seeing?
[1321.70 --> 1322.36]  What are the gaps?
[1322.62 --> 1324.60]  How are people managing that?
[1324.60 --> 1325.78]  So first off,
[1326.28 --> 1327.98]  the job title data scientist
[1327.98 --> 1331.28]  has kind of become confusing to some people
[1331.28 --> 1336.12]  so I will not name these companies
[1336.12 --> 1337.76]  but they're in the Bay Area,
[1337.92 --> 1339.06]  one is in social media,
[1339.40 --> 1343.88]  one is in ride sharing
[1343.88 --> 1345.12]  so I'm not going to name them
[1345.12 --> 1348.60]  but inside many companies
[1348.60 --> 1350.34]  the term data scientist
[1350.34 --> 1354.16]  increasingly refers to two types of people, right?
[1354.22 --> 1356.06]  So one is a business analyst,
[1356.26 --> 1357.22]  business analytics,
[1357.92 --> 1360.82]  mostly does SQL type of work
[1360.82 --> 1364.06]  and then the actual data scientist
[1364.06 --> 1365.20]  who does machine learning.
[1365.60 --> 1365.62]  Yeah.
[1365.78 --> 1367.16]  But to us on the outside
[1367.16 --> 1370.46]  when we see Ben is from company X,
[1370.56 --> 1371.46]  he's a data scientist,
[1372.28 --> 1373.98]  so I've complained to my friends,
[1374.06 --> 1375.94]  I said it's confusing for us on the outside
[1375.94 --> 1378.58]  because if you guys have really
[1378.58 --> 1380.12]  two different types of personas
[1380.12 --> 1381.30]  then you should give them
[1381.30 --> 1382.48]  two different titles, right?
[1382.78 --> 1384.70]  But I think the fact that
[1384.70 --> 1387.10]  data scientist is a hot title
[1387.10 --> 1389.36]  so then they have to kind of
[1389.36 --> 1391.96]  incentivize their employees, right?
[1392.22 --> 1393.58]  Yeah, one of the things,
[1393.74 --> 1394.50]  it's interesting,
[1394.66 --> 1396.18]  I think when people talk about
[1396.18 --> 1397.90]  the need for skills in this area
[1397.90 --> 1399.88]  and that they need more people to do it,
[1399.94 --> 1401.72]  I certainly sympathize with that
[1401.72 --> 1402.76]  but I've also,
[1403.10 --> 1405.68]  I've come to a perspective
[1405.68 --> 1407.02]  where I'll disagree with people
[1407.02 --> 1407.94]  who say there's not enough
[1407.94 --> 1408.96]  data scientists in the world
[1408.96 --> 1410.60]  because I think that's fragmenting.
[1410.68 --> 1413.10]  I think this kind of catch-all position
[1413.10 --> 1414.16]  called data scientist
[1414.16 --> 1416.02]  that was once one thing
[1416.02 --> 1417.66]  and now that we're moving into the space
[1417.66 --> 1419.88]  is becoming a number of different,
[1419.96 --> 1421.18]  you know, specific roles
[1421.18 --> 1422.78]  that people are taking on in the future.
[1423.02 --> 1423.78]  Right, right, right.
[1423.90 --> 1426.26]  So, and then to answer your question
[1426.26 --> 1427.32]  about deep learning, right?
[1427.40 --> 1430.96]  So when I first started focusing
[1430.96 --> 1432.66]  on deep learning in 2013,
[1432.66 --> 1436.72]  so there weren't the open source libraries
[1436.72 --> 1437.52]  we have today
[1437.52 --> 1439.14]  that are well documented
[1439.14 --> 1442.66]  with easy to use examples
[1442.66 --> 1444.16]  that you can get started with.
[1444.90 --> 1448.56]  So it was mostly confined
[1448.56 --> 1449.78]  to a few research groups.
[1449.92 --> 1451.88]  You literally had to apprentice
[1451.88 --> 1454.00]  with one of these research groups
[1454.00 --> 1454.78]  because a lot of it,
[1455.06 --> 1455.88]  a lot of the knowledge
[1455.88 --> 1457.30]  was passed through oral tradition.
[1457.72 --> 1457.80]  Yeah.
[1457.80 --> 1459.16]  So these days, of course,
[1459.24 --> 1461.08]  we have good libraries
[1461.08 --> 1462.72]  like TensorFlow and PyTorch
[1462.72 --> 1463.74]  and Big DL
[1463.74 --> 1465.24]  and a bunch of other libraries
[1465.24 --> 1467.08]  that have documentation
[1467.08 --> 1468.96]  and the researchers
[1468.96 --> 1473.16]  in the academic and industry labs
[1473.16 --> 1475.56]  tend to publish their papers
[1475.56 --> 1477.04]  and have code
[1477.04 --> 1479.72]  that you can start to play with.
[1480.14 --> 1482.80]  So there's some notion
[1482.80 --> 1484.50]  of a running start.
[1484.76 --> 1486.20]  You have, I was just going to say,
[1486.20 --> 1488.16]  since I can say that for you,
[1488.20 --> 1489.22]  you have media companies
[1489.22 --> 1490.20]  like O'Reilly Media
[1490.20 --> 1491.76]  that are putting out great material
[1491.76 --> 1492.58]  on this to learn by.
[1492.68 --> 1493.42]  Right, exactly.
[1493.86 --> 1494.36]  And then,
[1495.04 --> 1496.42]  so then the question is,
[1496.66 --> 1497.16]  are those,
[1497.80 --> 1499.18]  is that material enough
[1499.18 --> 1500.84]  for companies?
[1500.98 --> 1501.74]  I think that
[1501.74 --> 1503.32]  to the extent
[1503.32 --> 1506.96]  that the pre-built models,
[1507.24 --> 1508.36]  pre-built architectures
[1508.36 --> 1509.54]  and pre-trained models
[1509.54 --> 1512.34]  apply to their domains,
[1512.80 --> 1513.36]  yes.
[1513.36 --> 1514.08]  So for example,
[1515.00 --> 1516.38]  if what you need
[1516.38 --> 1520.12]  is a speech-to-text tool,
[1520.24 --> 1522.38]  maybe many of the existing
[1522.38 --> 1523.54]  off-the-shelf
[1523.54 --> 1524.76]  or cloud services
[1524.76 --> 1525.58]  will be enough.
[1526.06 --> 1526.66]  But, you know,
[1526.72 --> 1528.92]  take a data type
[1528.92 --> 1529.98]  like text, right?
[1530.10 --> 1531.84]  So last year
[1531.84 --> 1533.06]  was a big, big year
[1533.06 --> 1535.34]  for natural language models
[1535.34 --> 1536.70]  and research, right?
[1536.70 --> 1538.56]  But if you dig,
[1538.74 --> 1540.24]  if you drill down, right?
[1540.34 --> 1542.38]  So many of the models
[1542.38 --> 1543.16]  were published
[1543.16 --> 1544.16]  with code.
[1544.80 --> 1547.30]  Some of the models
[1547.30 --> 1548.46]  are even pre-trained
[1548.46 --> 1549.38]  so you can use them.
[1549.64 --> 1551.88]  But then they may not be
[1551.88 --> 1553.88]  quite tuned to your domain.
[1554.22 --> 1554.38]  Sure.
[1554.56 --> 1555.30]  So for example,
[1555.30 --> 1556.36]  if you're in healthcare
[1556.36 --> 1558.38]  and you want to use
[1558.38 --> 1559.72]  one of these pre-trained models,
[1559.88 --> 1560.06]  well,
[1560.58 --> 1561.34]  even within,
[1561.34 --> 1562.98]  even within healthcare
[1562.98 --> 1563.62]  and medicine,
[1563.62 --> 1565.24]  different areas
[1565.24 --> 1566.14]  of specialization
[1566.14 --> 1567.70]  have very different lingo
[1567.70 --> 1568.58]  and shortcuts
[1568.58 --> 1569.74]  for how they communicate
[1569.74 --> 1570.54]  with each other, right?
[1570.54 --> 1571.14]  Yes, that's true.
[1571.20 --> 1572.92]  So you might still need
[1572.92 --> 1573.88]  staff
[1573.88 --> 1575.12]  who are capable
[1575.12 --> 1576.62]  of doing some of this
[1576.62 --> 1577.18]  tuning
[1577.18 --> 1579.02]  and retraining
[1579.02 --> 1581.02]  and things like this.
[1581.40 --> 1581.54]  So,
[1581.72 --> 1583.12]  and how does domain knowledge
[1583.12 --> 1583.78]  about that,
[1583.80 --> 1584.36]  since that's kind of
[1584.36 --> 1585.14]  what we're getting into
[1585.14 --> 1585.70]  at this point,
[1586.10 --> 1587.42]  how do you overcome that?
[1587.84 --> 1588.04]  You know,
[1588.10 --> 1589.68]  my next question
[1589.68 --> 1590.22]  was going to be,
[1590.26 --> 1590.40]  you know,
[1590.40 --> 1591.26]  how are organizations
[1591.26 --> 1592.40]  kind of using AI
[1592.40 --> 1593.16]  and all that,
[1593.24 --> 1594.02]  but you're kind of
[1594.02 --> 1595.92]  pointing out another one,
[1596.00 --> 1596.12]  you know,
[1596.12 --> 1596.62]  we've talked about
[1596.62 --> 1597.62]  several of the challenges
[1597.62 --> 1599.02]  on making all this stuff happen
[1599.02 --> 1600.44]  and that is one,
[1600.54 --> 1601.70]  is being able to marry
[1601.70 --> 1602.84]  your domain knowledge
[1602.84 --> 1604.28]  in very specific areas
[1604.28 --> 1605.78]  to the people,
[1605.96 --> 1606.54]  the teams
[1606.54 --> 1608.84]  of people
[1608.84 --> 1610.50]  in the data science space,
[1610.66 --> 1611.52]  whatever your team is
[1611.52 --> 1612.28]  calling those,
[1612.60 --> 1613.44]  that are doing this,
[1613.50 --> 1614.16]  ML engineers.
[1614.94 --> 1615.48]  How do you,
[1615.48 --> 1616.10]  how do you make
[1616.10 --> 1617.70]  that domain knowledge
[1617.70 --> 1618.86]  transfer happen
[1618.86 --> 1620.28]  in an efficient way
[1620.28 --> 1621.46]  that keeps the business
[1621.46 --> 1622.18]  pushing forward?
[1622.40 --> 1622.76]  So,
[1622.84 --> 1624.10]  this is part of the,
[1624.20 --> 1626.14]  kind of the evolution
[1626.14 --> 1628.86]  of how some of these
[1628.86 --> 1629.92]  software systems
[1629.92 --> 1630.78]  are going to be built.
[1630.98 --> 1631.08]  If,
[1631.18 --> 1632.40]  if machine learning
[1632.40 --> 1633.64]  will play a role
[1633.64 --> 1634.72]  moving forward
[1634.72 --> 1635.86]  in many of these systems,
[1635.96 --> 1638.42]  then a lot of,
[1638.42 --> 1639.78]  a lot of software development
[1639.78 --> 1640.94]  may start resembling
[1640.94 --> 1642.20]  ML development,
[1642.34 --> 1642.84]  which means,
[1642.92 --> 1643.18]  you know,
[1643.26 --> 1644.02]  gather data,
[1644.56 --> 1645.32]  train a model,
[1645.86 --> 1647.10]  evaluate the results,
[1647.66 --> 1648.44]  and then,
[1648.44 --> 1649.68]  and then repeat,
[1649.68 --> 1650.34]  rinse,
[1650.42 --> 1651.22]  rinse and repeat.
[1651.44 --> 1651.94]  But then,
[1652.04 --> 1653.38]  that might also mean
[1653.38 --> 1654.76]  consulting with
[1654.76 --> 1655.90]  domain experts
[1655.90 --> 1656.80]  who know,
[1657.34 --> 1659.34]  who know what data
[1659.34 --> 1660.16]  might be useful.
[1660.92 --> 1661.12]  And,
[1661.20 --> 1662.68]  and actually,
[1662.92 --> 1663.30]  honestly,
[1663.52 --> 1665.10]  in many cases,
[1665.64 --> 1668.74]  data is not
[1668.74 --> 1669.90]  perfectly cleaned
[1669.90 --> 1670.90]  in the beginning.
[1670.90 --> 1671.56]  You have to,
[1671.64 --> 1672.04]  kind of,
[1672.08 --> 1673.48]  clean the data
[1673.48 --> 1674.34]  and prepare it.
[1674.86 --> 1675.24]  And there,
[1675.96 --> 1676.42]  again,
[1676.54 --> 1676.94]  that's where
[1676.94 --> 1678.30]  the domain experts
[1678.30 --> 1679.52]  might be helpful
[1679.52 --> 1679.94]  to you.
[1680.34 --> 1680.84]  So then,
[1680.92 --> 1681.78]  one trend
[1681.78 --> 1682.80]  that I am seeing
[1682.80 --> 1683.38]  is that
[1683.38 --> 1684.50]  in the,
[1684.60 --> 1685.70]  in the case
[1685.70 --> 1686.78]  of data preparation
[1686.78 --> 1688.80]  and data cleaning,
[1689.24 --> 1690.84]  companies are
[1690.84 --> 1692.06]  starting to use tools
[1692.06 --> 1693.40]  that actually use
[1693.40 --> 1694.02]  machine learning
[1694.02 --> 1695.26]  because you have
[1695.26 --> 1696.44]  a set of domain experts,
[1696.58 --> 1697.38]  they can label
[1697.38 --> 1698.30]  a few examples,
[1698.64 --> 1699.50]  and then maybe
[1699.50 --> 1699.96]  a system
[1699.96 --> 1700.86]  will automatically,
[1700.86 --> 1701.38]  kind of,
[1701.38 --> 1702.34]  go through
[1702.34 --> 1703.26]  the rest of the data
[1703.26 --> 1704.26]  and try to
[1704.26 --> 1706.44]  extract similar examples.
[1708.18 --> 1708.52]  And so,
[1708.66 --> 1708.90]  yes,
[1709.00 --> 1709.98]  so I think that
[1709.98 --> 1711.34]  domain knowledge
[1711.34 --> 1711.98]  at least
[1711.98 --> 1713.42]  is going to be
[1713.42 --> 1713.76]  essential
[1713.76 --> 1714.50]  to the extent
[1714.50 --> 1716.94]  that we're not
[1716.94 --> 1718.24]  talking about
[1718.24 --> 1720.44]  general intelligence here,
[1720.50 --> 1721.16]  we're talking about
[1721.16 --> 1721.96]  very fine,
[1722.48 --> 1722.80]  narrow,
[1723.26 --> 1724.32]  and tuned
[1724.32 --> 1725.52]  systems
[1725.52 --> 1727.34]  that can help
[1727.34 --> 1728.32]  companies
[1728.32 --> 1729.86]  automate
[1729.86 --> 1730.98]  many,
[1731.08 --> 1731.68]  many very
[1731.68 --> 1732.68]  specific workflows.
[1733.14 --> 1733.94]  So another example
[1733.94 --> 1735.34]  I like to cite
[1735.34 --> 1736.82]  is robotic
[1736.82 --> 1737.84]  process automation.
[1738.00 --> 1738.32]  I don't know
[1738.32 --> 1738.94]  if you're familiar
[1738.94 --> 1740.64]  with this term,
[1740.70 --> 1740.82]  right?
[1741.20 --> 1742.92]  So I think
[1742.92 --> 1744.30]  it's a mistake
[1744.30 --> 1744.80]  to think that
[1744.80 --> 1746.52]  robotic process automation
[1746.52 --> 1747.04]  is something
[1747.04 --> 1749.36]  that will be
[1749.36 --> 1750.34]  directed from above,
[1750.40 --> 1750.58]  right?
[1750.66 --> 1751.50]  Because I think
[1751.50 --> 1752.34]  it's got to be
[1752.34 --> 1752.92]  a ground
[1752.92 --> 1754.78]  from the ground up.
[1754.78 --> 1756.32]  I think it's
[1756.32 --> 1756.96]  a terribly
[1756.96 --> 1757.58]  name field,
[1757.70 --> 1757.86]  though.
[1758.06 --> 1759.24]  It's very confusing
[1759.24 --> 1759.78]  for most people
[1759.78 --> 1760.34]  to understand it.
[1760.36 --> 1760.78]  Because it's
[1760.78 --> 1763.70]  those workers
[1763.70 --> 1764.26]  who are in
[1764.26 --> 1765.92]  the front lines
[1765.92 --> 1766.68]  who know
[1766.68 --> 1767.28]  which tasks
[1767.28 --> 1767.90]  are repetitive.
[1768.18 --> 1768.52]  Absolutely.
[1768.58 --> 1769.56]  And if you explain
[1769.56 --> 1770.70]  to them enough
[1770.70 --> 1771.50]  about
[1771.50 --> 1773.26]  at a high level
[1773.26 --> 1773.96]  what the current
[1773.96 --> 1774.52]  technologies
[1774.52 --> 1775.66]  are capable of doing,
[1775.80 --> 1776.44]  they can help you
[1776.44 --> 1777.20]  identify which
[1777.20 --> 1778.14]  of these workflows
[1778.14 --> 1779.68]  lend themselves
[1779.68 --> 1780.56]  to automation
[1780.56 --> 1781.62]  or partial automation,
[1781.82 --> 1781.92]  right?
[1781.92 --> 1782.08]  Sure.
[1782.08 --> 1782.88]  because maybe
[1782.88 --> 1784.18]  it won't be
[1784.18 --> 1784.86]  full automation,
[1785.04 --> 1785.20]  right?
[1785.44 --> 1787.04]  So one of the things
[1787.04 --> 1788.22]  that I'm kind of
[1788.22 --> 1789.52]  extracting from
[1789.52 --> 1790.56]  your explanation
[1790.56 --> 1791.58]  is there's this
[1791.58 --> 1792.74]  kind of democratization
[1792.74 --> 1793.80]  of the technology
[1793.80 --> 1794.40]  as it's becoming
[1794.40 --> 1794.92]  widespread
[1794.92 --> 1796.10]  and finding
[1796.10 --> 1797.36]  many, many use cases
[1797.36 --> 1798.22]  even within
[1798.22 --> 1799.20]  a given organization.
[1799.34 --> 1799.80]  But you're seeing
[1799.80 --> 1800.30]  it all over.
[1801.00 --> 1801.32]  I think,
[1801.72 --> 1803.44]  is it fair to say
[1803.44 --> 1805.70]  that this field,
[1805.80 --> 1806.26]  and I'm kind of
[1806.26 --> 1806.92]  talking about
[1806.92 --> 1807.36]  deep learning
[1807.36 --> 1808.08]  as it's finding
[1808.08 --> 1809.18]  more and more use cases,
[1809.70 --> 1810.58]  it's going to become
[1810.58 --> 1811.54]  somewhat synonymous
[1811.54 --> 1812.94]  with software development
[1812.94 --> 1814.26]  in the sense that
[1814.26 --> 1816.52]  as you have
[1816.52 --> 1817.62]  ML engineers
[1817.62 --> 1819.92]  become part of that team
[1819.92 --> 1821.06]  as a standard thing,
[1821.08 --> 1821.62]  it's no longer
[1821.62 --> 1822.74]  the cool new
[1822.74 --> 1824.02]  hotness that you're
[1824.02 --> 1824.70]  doing,
[1824.82 --> 1825.18]  but it's just
[1825.18 --> 1826.10]  an everyday thing
[1826.10 --> 1826.86]  down the road
[1826.86 --> 1828.52]  that you're really
[1828.52 --> 1828.86]  going to have,
[1828.94 --> 1829.50]  neural computing
[1829.50 --> 1830.20]  is really kind of
[1830.20 --> 1830.60]  the future
[1830.60 --> 1831.80]  versus the deterministic,
[1831.98 --> 1832.16]  you know,
[1832.20 --> 1832.88]  I have all my
[1832.88 --> 1833.24]  if, then,
[1833.28 --> 1833.92]  and case statements
[1833.92 --> 1834.84]  of the past
[1834.84 --> 1835.72]  that neural computing
[1835.72 --> 1836.96]  will be part of
[1836.96 --> 1837.78]  many, many
[1837.78 --> 1838.46]  software stacks
[1838.46 --> 1838.84]  out there?
[1838.84 --> 1840.38]  I would say
[1840.38 --> 1841.12]  machine learning
[1841.12 --> 1841.54]  because,
[1842.10 --> 1842.74]  as you know,
[1843.48 --> 1844.12]  right now,
[1844.20 --> 1844.46]  of course,
[1844.54 --> 1845.02]  deep learning
[1845.02 --> 1847.84]  is very successful
[1847.84 --> 1848.38]  in many,
[1848.46 --> 1849.14]  many areas
[1849.14 --> 1849.46]  of,
[1849.46 --> 1850.66]  of,
[1852.80 --> 1854.24]  that affect companies
[1854.24 --> 1855.22]  like computer vision,
[1855.36 --> 1856.04]  speech recognition,
[1856.04 --> 1856.62]  and text,
[1857.14 --> 1857.48]  but,
[1857.98 --> 1858.92]  you know,
[1859.16 --> 1860.76]  if you follow
[1860.76 --> 1861.26]  the history
[1861.26 --> 1862.04]  of machine learning,
[1862.80 --> 1863.52]  there are,
[1863.58 --> 1864.62]  there are things
[1864.62 --> 1865.20]  that go in
[1865.20 --> 1865.94]  and out of fashion,
[1865.94 --> 1866.76]  although right now
[1866.76 --> 1868.36]  we're not seeing
[1868.36 --> 1869.62]  anything coming
[1869.62 --> 1870.42]  close to challenging
[1870.42 --> 1871.02]  deep learning
[1871.02 --> 1871.60]  in a variety
[1871.60 --> 1872.08]  of tasks,
[1872.16 --> 1872.28]  right?
[1872.44 --> 1872.66]  Sure,
[1872.88 --> 1873.38]  but that's probably,
[1873.62 --> 1874.08]  I agree with you.
[1874.36 --> 1875.20]  That's not a given.
[1875.36 --> 1876.16]  I think the,
[1876.16 --> 1876.28]  the,
[1876.38 --> 1876.98]  the,
[1876.98 --> 1878.06]  the workflow
[1878.06 --> 1879.14]  will probably
[1879.14 --> 1879.94]  remain the same
[1879.94 --> 1880.52]  to the extent
[1880.52 --> 1881.34]  that machine learning
[1881.34 --> 1882.26]  is part of
[1882.26 --> 1883.52]  software development,
[1883.66 --> 1884.20]  that workflow
[1884.20 --> 1884.90]  will be the same.
[1884.92 --> 1885.34]  It's becoming
[1885.34 --> 1886.50]  a part of everyday life
[1886.50 --> 1887.02]  that companies
[1887.02 --> 1888.08]  are using in production
[1888.08 --> 1888.44]  for,
[1888.50 --> 1889.34]  for all these areas.
[1889.48 --> 1889.66]  Yeah,
[1889.70 --> 1890.00]  and so,
[1890.08 --> 1890.36]  actually,
[1890.44 --> 1891.10]  one of the things
[1891.10 --> 1892.48]  that we aspire for
[1892.48 --> 1893.32]  in this conference
[1893.32 --> 1896.54]  is to kind of,
[1898.08 --> 1898.80]  so we have,
[1898.94 --> 1899.48]  so we have,
[1899.58 --> 1900.30]  in this conference,
[1900.62 --> 1901.42]  the AI conference,
[1901.54 --> 1902.56]  the O'Reilly AI conference,
[1902.84 --> 1904.10]  we have a business summit,
[1904.72 --> 1906.16]  so we have content
[1906.16 --> 1907.40]  for decision makers
[1907.40 --> 1908.00]  and managers,
[1908.20 --> 1909.84]  so they know
[1909.84 --> 1912.50]  what other people
[1912.50 --> 1912.92]  are doing,
[1913.02 --> 1913.84]  so case studies,
[1914.36 --> 1915.78]  but also give them
[1915.78 --> 1917.00]  high level overviews
[1917.00 --> 1918.46]  of important topics
[1918.46 --> 1919.68]  through executive briefings.
[1920.48 --> 1921.86]  But we also have content
[1921.86 --> 1922.88]  for developers,
[1922.88 --> 1924.80]  who are not data experts,
[1925.12 --> 1925.84]  who just want
[1925.84 --> 1926.32]  to build,
[1926.64 --> 1927.60]  build things.
[1928.76 --> 1929.70]  But then also,
[1930.08 --> 1930.42]  you know,
[1930.48 --> 1932.98]  we want to show people
[1932.98 --> 1933.68]  the bleeding edge,
[1933.72 --> 1934.76]  so we have researchers
[1934.76 --> 1936.42]  and machine learning experts.
[1937.18 --> 1937.70]  So one,
[1937.76 --> 1938.74]  one other area
[1938.74 --> 1939.48]  I think that
[1939.48 --> 1941.46]  I've been trying
[1941.46 --> 1941.90]  to emphasize
[1941.90 --> 1942.78]  is this notion
[1942.78 --> 1944.44]  that when it comes
[1944.44 --> 1945.12]  to machine learning,
[1945.20 --> 1945.78]  I think companies
[1945.78 --> 1946.84]  are coming to realize
[1946.84 --> 1949.12]  that it's not a simple,
[1949.88 --> 1951.76]  trying to optimize
[1951.76 --> 1952.70]  some business metric
[1952.70 --> 1955.28]  or some statistical metric,
[1955.38 --> 1955.52]  right?
[1955.58 --> 1956.30]  So there's other
[1956.30 --> 1957.44]  important considerations,
[1958.22 --> 1959.26]  which over the last year
[1959.26 --> 1960.12]  I've been giving these,
[1960.78 --> 1961.54]  I've been trying
[1961.54 --> 1962.12]  to give talks
[1962.12 --> 1962.84]  around this notion
[1962.84 --> 1963.86]  of managing risk,
[1963.86 --> 1965.04]  and I've been collecting
[1965.04 --> 1965.96]  a bunch of these
[1965.96 --> 1967.50]  other considerations
[1967.50 --> 1968.44]  like fairness
[1968.44 --> 1969.56]  and bias,
[1970.28 --> 1971.70]  privacy and security,
[1972.50 --> 1973.64]  safety and reliability,
[1974.34 --> 1975.08]  explainability,
[1975.08 --> 1975.40]  right?
[1975.40 --> 1977.66]  So if you take
[1977.66 --> 1979.36]  any one of these
[1979.36 --> 1980.54]  considerations
[1980.54 --> 1982.76]  and risks
[1982.76 --> 1985.68]  and you imagine
[1985.68 --> 1986.32]  yourself
[1986.32 --> 1988.00]  as a company
[1988.00 --> 1989.42]  that has begun
[1989.42 --> 1990.10]  to use more
[1990.10 --> 1991.02]  and more machine learning,
[1991.54 --> 1993.22]  then you start realizing,
[1993.52 --> 1993.60]  oh,
[1993.64 --> 1994.38]  I really need
[1994.38 --> 1996.12]  the foundational technologies,
[1996.68 --> 1996.88]  right?
[1996.96 --> 1997.76]  So for example,
[1998.08 --> 2000.30]  you look at security,
[2000.80 --> 2000.98]  right?
[2001.04 --> 2002.52]  So your machine learning model
[2002.52 --> 2003.22]  gets attacked
[2003.22 --> 2004.16]  by an adversary
[2004.16 --> 2006.88]  or starts behaving weirdly.
[2007.38 --> 2007.58]  Well,
[2007.64 --> 2008.12]  now you've got
[2008.12 --> 2009.06]  to retrace back.
[2009.44 --> 2010.30]  So I need tools
[2010.30 --> 2011.32]  that will allow me
[2011.32 --> 2013.24]  to go all the way
[2013.24 --> 2013.90]  back and audit.
[2014.42 --> 2015.30]  Maybe now we're talking
[2015.30 --> 2016.26]  about data governance,
[2016.48 --> 2017.18]  data lineage,
[2017.32 --> 2017.46]  right?
[2017.50 --> 2018.34]  So where did this data
[2018.34 --> 2018.92]  come from
[2018.92 --> 2020.16]  and things like this.
[2020.16 --> 2021.30]  So a lot of these
[2021.30 --> 2022.38]  foundational technologies
[2022.38 --> 2025.52]  are not just important
[2025.52 --> 2026.66]  because you want
[2026.66 --> 2029.32]  to do more
[2029.32 --> 2030.18]  and more machine learning,
[2030.18 --> 2031.10]  but it also
[2031.10 --> 2032.08]  will allow you
[2032.08 --> 2033.32]  to manage risks
[2033.32 --> 2034.28]  that come with
[2034.28 --> 2035.14]  having a lot
[2035.14 --> 2035.80]  of machine learning.
[2043.86 --> 2044.70]  This episode
[2044.70 --> 2045.24]  is brought to you
[2045.24 --> 2046.24]  by Discover.Bot.
[2046.44 --> 2046.98]  Learn everything
[2046.98 --> 2047.66]  there is to know
[2047.66 --> 2048.30]  about bots
[2048.30 --> 2049.42]  at discover.bot
[2049.42 --> 2050.62]  slash practical AI.
[2050.98 --> 2051.52]  Discover.Bot
[2051.52 --> 2052.18]  was built by
[2052.18 --> 2053.38]  Amazon Registry Services
[2053.38 --> 2054.78]  as an online community
[2054.78 --> 2055.38]  for bot creators
[2055.38 --> 2055.72]  and makers
[2055.72 --> 2056.68]  of all skill levels
[2056.68 --> 2057.72]  to learn from one another,
[2057.86 --> 2058.84]  to share stories,
[2059.00 --> 2059.60]  and they regularly
[2059.60 --> 2060.34]  publish guides
[2060.34 --> 2060.86]  and resources
[2060.86 --> 2061.66]  to answer questions
[2061.66 --> 2062.66]  like how to set up
[2062.66 --> 2063.48]  payments to your bot,
[2063.56 --> 2063.98]  how to stop
[2063.98 --> 2065.02]  shopping cart abandonment,
[2065.18 --> 2065.78]  what KPIs
[2065.78 --> 2066.50]  are worth measuring,
[2066.66 --> 2067.38]  how to write
[2067.38 --> 2069.06]  an engaging chat bot dialogue.
[2069.52 --> 2070.38]  You can even register
[2070.38 --> 2071.44]  .bot domains there.
[2071.72 --> 2072.12]  Learn more
[2072.12 --> 2072.52]  and explore
[2072.52 --> 2073.36]  this huge library
[2073.36 --> 2074.10]  of bot resources
[2074.10 --> 2075.50]  at discover.bot
[2075.50 --> 2076.48]  slash practical AI.
[2076.82 --> 2077.16]  Again,
[2077.16 --> 2078.08]  discover.bot
[2078.08 --> 2079.32]  slash practical AI.
[2091.60 --> 2092.20]  So,
[2092.52 --> 2093.30]  referencing back
[2093.30 --> 2094.40]  to the e-book,
[2094.54 --> 2095.12]  I was noticing
[2095.12 --> 2095.74]  that you had
[2095.74 --> 2096.32]  some sections
[2096.32 --> 2097.20]  on building block
[2097.20 --> 2097.84]  technologies
[2097.84 --> 2099.08]  and data types,
[2099.58 --> 2100.34]  and I was noticing
[2100.34 --> 2101.08]  within that,
[2101.16 --> 2101.88]  you kind of list
[2101.88 --> 2103.82]  kind of the respondents,
[2104.00 --> 2104.80]  what they were using,
[2104.80 --> 2106.60]  and some of them,
[2106.76 --> 2106.90]  you know,
[2106.94 --> 2107.62]  like supervised learning
[2107.62 --> 2108.12]  was right there
[2108.12 --> 2108.54]  at the top
[2108.54 --> 2109.10]  and deep learning,
[2109.54 --> 2110.94]  and then it kind of shows
[2110.94 --> 2112.12]  the usage of each.
[2112.36 --> 2113.72]  I noticed down here
[2113.72 --> 2115.92]  that reinforcement learning
[2115.92 --> 2117.30]  was still fairly low
[2117.30 --> 2117.96]  on the list,
[2118.00 --> 2119.18]  and yet we're talking
[2119.18 --> 2120.18]  about it so much,
[2120.54 --> 2121.18]  you know,
[2121.20 --> 2122.54]  out there in conferences
[2122.54 --> 2123.26]  and talks.
[2123.38 --> 2123.50]  You know,
[2123.52 --> 2124.38]  we've really seen
[2124.38 --> 2125.66]  an enormous interest
[2125.66 --> 2126.72]  over the last year or so,
[2126.86 --> 2127.64]  maybe two years,
[2127.98 --> 2129.08]  in reinforcement learning.
[2129.44 --> 2130.90]  Do you see deep learning
[2130.90 --> 2131.96]  and reinforcement learning
[2131.96 --> 2132.66]  kind of together
[2132.66 --> 2133.38]  going forward?
[2133.48 --> 2134.08]  Do you think we'll see
[2134.08 --> 2135.60]  that rise up on the list?
[2135.78 --> 2136.78]  Or what other,
[2136.92 --> 2137.76]  I'll leave it a little bit
[2137.76 --> 2138.24]  more open-ended,
[2138.34 --> 2139.10]  what other technologies
[2139.10 --> 2139.84]  are you seeing
[2139.84 --> 2140.88]  in the future
[2140.88 --> 2142.48]  as likely use cases?
[2143.08 --> 2143.26]  So,
[2143.36 --> 2143.90]  I think that,
[2143.96 --> 2145.34]  I think that,
[2145.42 --> 2147.54]  I would say
[2147.54 --> 2148.48]  reinforcement learning
[2148.48 --> 2149.04]  right now,
[2149.44 --> 2150.70]  as I mentioned earlier,
[2151.18 --> 2152.96]  the tools are improving
[2152.96 --> 2155.74]  and becoming more accessible,
[2155.98 --> 2157.92]  so that might let companies
[2157.92 --> 2159.82]  play around with it
[2159.82 --> 2160.24]  some more.
[2160.38 --> 2161.14]  And then I think
[2161.14 --> 2163.16]  over the next
[2163.16 --> 2164.78]  six to 12 months,
[2164.80 --> 2165.58]  we're going to hear
[2165.58 --> 2166.46]  companies share
[2166.46 --> 2167.84]  what they've done,
[2167.98 --> 2168.80]  and so that's always
[2168.80 --> 2169.30]  inspiring,
[2169.38 --> 2170.02]  because it's one thing
[2170.02 --> 2171.58]  to hear that
[2171.58 --> 2172.78]  reinforcement learning
[2172.78 --> 2173.42]  is being used
[2173.42 --> 2174.22]  for AlphaGo
[2174.22 --> 2175.92]  or for a self-driving car,
[2176.26 --> 2177.38]  but if you hear
[2177.38 --> 2178.46]  an enterprise
[2178.46 --> 2180.28]  in your own industry
[2180.28 --> 2181.16]  using it,
[2181.44 --> 2182.22]  so that may
[2182.22 --> 2183.76]  cause you to take pause
[2183.76 --> 2186.90]  and try to understand,
[2187.08 --> 2187.20]  okay,
[2187.20 --> 2189.02]  so how did they do it,
[2189.46 --> 2190.38]  what did they use,
[2190.48 --> 2191.78]  and can we do it ourselves,
[2191.96 --> 2192.16]  right?
[2192.24 --> 2192.38]  So,
[2192.78 --> 2194.02]  I think
[2194.02 --> 2196.14]  we need companies
[2196.14 --> 2197.06]  to start talking
[2197.06 --> 2198.76]  about how they use
[2198.76 --> 2199.66]  reinforcement learning,
[2199.78 --> 2201.14]  and we're going to begin
[2201.14 --> 2201.72]  to see that.
[2201.80 --> 2201.88]  So,
[2201.94 --> 2202.78]  as I mentioned earlier,
[2202.88 --> 2203.00]  right,
[2203.10 --> 2205.80]  so Ray already has
[2205.80 --> 2208.30]  use cases in production.
[2208.56 --> 2209.38]  They're going to start,
[2209.84 --> 2210.56]  the team from
[2210.56 --> 2211.54]  Berkeley Rice Lab
[2211.54 --> 2212.40]  is going to start
[2212.40 --> 2213.98]  trying to convince
[2213.98 --> 2214.86]  some of these users
[2214.86 --> 2215.96]  to write blog posts,
[2216.64 --> 2217.80]  and some of them
[2217.80 --> 2218.86]  are enterprise users,
[2219.06 --> 2220.52]  so that might inspire
[2220.52 --> 2222.76]  people to jump in,
[2222.88 --> 2224.80]  but I think
[2224.80 --> 2225.94]  in the short term,
[2226.42 --> 2228.72]  more companies
[2228.72 --> 2229.54]  are probably going to
[2229.54 --> 2230.66]  start playing around
[2230.66 --> 2231.46]  with deep learning,
[2231.68 --> 2232.74]  because that seems
[2232.74 --> 2234.30]  to be at a point
[2234.30 --> 2234.86]  where you can
[2234.86 --> 2235.84]  really relate,
[2236.12 --> 2236.38]  you can,
[2236.38 --> 2237.98]  if you're in
[2237.98 --> 2239.22]  a specific industry,
[2239.54 --> 2240.12]  chances are
[2240.12 --> 2240.84]  there's a company
[2240.84 --> 2242.06]  who's using it
[2242.06 --> 2242.50]  that you can
[2242.50 --> 2243.52]  really relate to.
[2243.92 --> 2244.02]  So,
[2244.16 --> 2244.98]  it sounds like
[2244.98 --> 2245.74]  you kind of mentioned
[2245.74 --> 2246.44]  that you went back
[2246.44 --> 2247.14]  into tools
[2247.14 --> 2248.44]  and having those
[2248.44 --> 2249.60]  use cases
[2249.60 --> 2250.14]  that companies
[2250.14 --> 2250.84]  are doing out there,
[2251.32 --> 2252.26]  so would it be fair
[2252.26 --> 2252.94]  to say that
[2252.94 --> 2254.24]  one of the reasons
[2254.24 --> 2254.94]  for deep learning
[2254.94 --> 2255.90]  that maybe things
[2255.90 --> 2256.82]  like reinforcement learning
[2256.82 --> 2257.86]  need and probably
[2257.86 --> 2258.86]  will get in the near future
[2258.86 --> 2260.06]  are having
[2260.06 --> 2261.04]  a set of tools
[2261.04 --> 2261.44]  out there
[2261.44 --> 2262.00]  that are easy,
[2262.32 --> 2262.86]  accessible,
[2263.08 --> 2263.86]  and easy to use
[2263.86 --> 2264.74]  so they can start
[2264.74 --> 2265.24]  experimenting
[2265.24 --> 2266.46]  along with that
[2266.46 --> 2267.52]  probably data sets
[2267.52 --> 2268.06]  that are applicable
[2268.06 --> 2268.70]  to that.
[2269.50 --> 2269.72]  So,
[2270.08 --> 2270.76]  with reinforcement
[2270.76 --> 2271.28]  learning,
[2271.44 --> 2271.78]  actually,
[2272.48 --> 2273.40]  usually you need,
[2273.82 --> 2274.74]  usually involves
[2274.74 --> 2276.08]  a simulation environment.
[2276.26 --> 2276.52]  Yeah,
[2276.60 --> 2277.02]  that's true.
[2277.02 --> 2279.22]  Because it's more
[2279.22 --> 2281.02]  of an agent
[2281.02 --> 2282.94]  interacting
[2282.94 --> 2283.82]  with an environment
[2283.82 --> 2284.34]  and you have
[2284.34 --> 2285.34]  a reward function
[2285.34 --> 2287.14]  and you're trying
[2287.14 --> 2288.14]  to learn a policy
[2288.14 --> 2289.24]  which is basically
[2289.24 --> 2290.44]  what to do
[2290.44 --> 2291.58]  given the certain
[2291.58 --> 2292.66]  settings of the environment.
[2293.30 --> 2293.40]  Right?
[2293.52 --> 2293.70]  So,
[2293.86 --> 2294.30]  I think,
[2294.30 --> 2296.00]  so it's a combination
[2296.00 --> 2296.68]  of tools,
[2296.78 --> 2296.94]  right?
[2296.98 --> 2297.10]  So,
[2297.18 --> 2297.72]  you have
[2297.72 --> 2299.88]  Ray,
[2300.04 --> 2300.72]  which I mentioned
[2300.72 --> 2301.04]  earlier,
[2301.12 --> 2302.06]  which will give you
[2302.06 --> 2302.92]  the RL,
[2303.08 --> 2303.92]  which will allow you
[2303.92 --> 2304.54]  to learn
[2304.54 --> 2306.40]  the policy,
[2306.72 --> 2307.66]  but you need to have
[2307.66 --> 2308.82]  a simulation environment
[2308.82 --> 2309.66]  in order to
[2309.66 --> 2310.74]  play around
[2310.74 --> 2311.98]  or the ability
[2311.98 --> 2313.08]  to simulate data.
[2313.08 --> 2313.64]  Right?
[2313.64 --> 2315.78]  But I think
[2315.78 --> 2317.28]  the main thing
[2317.28 --> 2318.10]  is that
[2318.10 --> 2321.06]  what motivates
[2321.06 --> 2321.56]  companies
[2321.56 --> 2322.24]  is seeing
[2322.24 --> 2323.20]  their peers
[2323.20 --> 2324.56]  use something
[2324.56 --> 2325.44]  and
[2325.44 --> 2327.96]  seeing how
[2327.96 --> 2330.32]  much reward,
[2330.56 --> 2331.26]  so the reward
[2331.26 --> 2331.76]  function
[2331.76 --> 2333.08]  of their peers.
[2333.28 --> 2333.32]  Right?
[2333.38 --> 2333.48]  So,
[2333.56 --> 2333.92]  if you see,
[2334.20 --> 2334.64]  if you're in
[2334.64 --> 2335.50]  financial services
[2335.50 --> 2336.18]  and you hear
[2336.18 --> 2337.16]  Ant Finance
[2337.16 --> 2338.20]  has used
[2338.20 --> 2338.54]  Ray
[2338.54 --> 2339.86]  to do
[2339.86 --> 2340.94]  real-time
[2340.94 --> 2341.74]  recommendations
[2341.74 --> 2343.48]  of users
[2343.48 --> 2344.16]  interacting
[2344.16 --> 2346.18]  and learning
[2346.18 --> 2347.08]  from live data,
[2347.46 --> 2348.06]  then you might
[2348.06 --> 2348.94]  be more motivated,
[2349.06 --> 2349.26]  right?
[2349.32 --> 2350.10]  As opposed to
[2350.10 --> 2351.26]  hearing about it
[2351.26 --> 2352.58]  being used
[2352.58 --> 2353.50]  for AlphaGo.
[2353.94 --> 2354.30]  Gotcha.
[2354.30 --> 2356.00]  I want to
[2356.00 --> 2356.44]  actually also
[2356.44 --> 2356.78]  go back
[2356.78 --> 2357.16]  to something
[2357.16 --> 2357.58]  else you
[2357.58 --> 2358.40]  mentioned earlier.
[2358.86 --> 2359.18]  You were
[2359.18 --> 2359.60]  talking about
[2359.60 --> 2360.58]  risk in general
[2360.58 --> 2362.18]  and there are
[2362.18 --> 2363.04]  different variations.
[2363.40 --> 2364.18]  There's bias,
[2365.22 --> 2366.10]  there's the
[2366.10 --> 2366.74]  ethical and
[2366.74 --> 2367.64]  moral considerations
[2367.64 --> 2368.38]  of how you're
[2368.38 --> 2368.84]  using data.
[2368.84 --> 2369.92]  There's security
[2369.92 --> 2371.54]  and adversaries
[2371.54 --> 2372.96]  and privacy.
[2373.26 --> 2373.76]  Absolutely.
[2374.14 --> 2374.88]  The concept
[2374.88 --> 2376.54]  of AI safety
[2376.54 --> 2378.68]  or how you use
[2378.68 --> 2379.48]  it in benevolent
[2379.48 --> 2379.80]  ways.
[2380.84 --> 2381.52]  Or not just
[2381.52 --> 2382.28]  benevolent ways.
[2382.44 --> 2382.46]  So,
[2382.54 --> 2383.04]  AI safety
[2383.04 --> 2383.82]  also refers
[2383.82 --> 2384.90]  to safe
[2384.90 --> 2385.34]  systems.
[2386.00 --> 2386.24]  So,
[2386.38 --> 2387.04]  if you have
[2387.04 --> 2388.22]  AI in
[2388.22 --> 2388.88]  mission-critical
[2388.88 --> 2389.58]  situations,
[2390.30 --> 2391.04]  we don't have
[2391.04 --> 2391.50]  them yet.
[2391.90 --> 2392.70]  And I probably
[2392.70 --> 2394.52]  won't ride
[2394.52 --> 2395.18]  a plane yet
[2395.18 --> 2396.80]  that completely
[2396.80 --> 2397.82]  relies just on
[2397.82 --> 2398.30]  deep learning
[2398.30 --> 2398.96]  and not control
[2398.96 --> 2399.34]  theory.
[2399.56 --> 2401.14]  But you can
[2401.14 --> 2402.54]  imagine deploying
[2402.54 --> 2403.26]  these systems
[2403.26 --> 2403.98]  in environments
[2403.98 --> 2404.80]  where they can
[2404.80 --> 2405.70]  kill people.
[2405.96 --> 2406.08]  Sure.
[2406.28 --> 2407.70]  You need
[2407.70 --> 2408.52]  error bars
[2408.52 --> 2409.72]  and robustness
[2409.72 --> 2410.32]  and really
[2410.32 --> 2411.36]  the same
[2411.36 --> 2412.00]  types of
[2412.00 --> 2412.84]  discipline
[2412.84 --> 2413.64]  that a lot
[2413.64 --> 2414.16]  of these
[2414.16 --> 2415.52]  fields of
[2415.52 --> 2415.98]  engineering
[2415.98 --> 2416.64]  have had
[2416.64 --> 2416.92]  to go
[2416.92 --> 2417.14]  through
[2417.14 --> 2417.56]  and learn.
[2417.82 --> 2418.18]  That's true.
[2418.28 --> 2418.56]  And for
[2418.56 --> 2418.88]  what it's
[2418.88 --> 2419.10]  worth,
[2419.28 --> 2420.10]  for the record,
[2420.24 --> 2420.66]  the FAA
[2420.66 --> 2421.32]  doesn't actually
[2421.32 --> 2421.74]  allow,
[2421.86 --> 2423.26]  they will not
[2423.26 --> 2425.68]  certify a
[2425.68 --> 2426.20]  neural network
[2426.20 --> 2426.66]  at this point
[2426.66 --> 2427.12]  because of the
[2427.12 --> 2427.60]  black box
[2427.60 --> 2428.02]  component.
[2428.38 --> 2428.48]  So,
[2428.56 --> 2428.82]  that's one
[2428.82 --> 2429.14]  of the big
[2429.14 --> 2429.58]  challenges.
[2429.74 --> 2430.32]  Working for
[2430.32 --> 2431.12]  a company
[2431.12 --> 2431.86]  that's in
[2431.86 --> 2432.62]  aeronautical
[2432.62 --> 2433.12]  at Lockheed
[2433.12 --> 2433.36]  Martin,
[2433.58 --> 2434.18]  that's certainly
[2434.18 --> 2435.34]  a big challenge
[2435.34 --> 2435.90]  is being able
[2435.90 --> 2436.34]  to say,
[2437.12 --> 2438.56]  to pass all
[2438.56 --> 2439.34]  the certifications
[2439.34 --> 2440.86]  well enough
[2440.86 --> 2441.30]  both for
[2441.30 --> 2441.58]  ourselves
[2441.58 --> 2441.94]  and for
[2441.94 --> 2442.18]  FAA
[2442.18 --> 2442.68]  requirements.
[2442.84 --> 2442.96]  So,
[2443.02 --> 2443.28]  actually,
[2444.24 --> 2446.22]  the notion
[2446.22 --> 2447.16]  of explainability
[2447.16 --> 2447.74]  is interesting
[2447.74 --> 2448.82]  because people
[2448.82 --> 2449.50]  think about it
[2449.50 --> 2450.30]  in terms of
[2450.30 --> 2451.96]  the need
[2451.96 --> 2452.54]  to understand
[2452.54 --> 2453.76]  what the
[2453.76 --> 2454.28]  black box
[2454.28 --> 2454.72]  is doing
[2454.72 --> 2456.60]  from a
[2456.60 --> 2457.04]  variety of
[2457.04 --> 2457.36]  angles.
[2457.58 --> 2457.74]  So,
[2457.82 --> 2458.24]  one is
[2458.24 --> 2459.46]  think about
[2459.46 --> 2459.80]  it from
[2459.80 --> 2460.22]  the end
[2460.22 --> 2460.70]  user's
[2460.70 --> 2461.16]  perspective.
[2461.16 --> 2461.68]  So,
[2462.24 --> 2463.92]  if the
[2463.92 --> 2464.46]  end user
[2464.46 --> 2466.16]  has some
[2466.16 --> 2466.88]  level of
[2466.88 --> 2467.52]  understanding
[2467.52 --> 2468.60]  about what
[2468.60 --> 2469.02]  the system
[2469.02 --> 2469.44]  is doing,
[2469.56 --> 2469.84]  they're more
[2469.84 --> 2470.64]  likely to use
[2470.64 --> 2470.80]  it,
[2470.86 --> 2471.52]  probably more
[2471.52 --> 2472.00]  comfortable.
[2473.72 --> 2474.30]  But also,
[2474.46 --> 2476.04]  maybe explainability
[2476.04 --> 2477.12]  might help you
[2477.12 --> 2478.02]  if things go
[2478.02 --> 2478.68]  wrong and you
[2478.68 --> 2479.42]  have to audit
[2479.42 --> 2480.08]  the system
[2480.08 --> 2480.78]  and go back
[2480.78 --> 2481.56]  and understand
[2481.56 --> 2482.48]  how you can
[2482.48 --> 2483.16]  improve it
[2483.16 --> 2484.42]  and things
[2484.42 --> 2484.88]  like this.
[2485.98 --> 2486.54]  So,
[2486.68 --> 2487.10]  there's a
[2487.10 --> 2487.50]  bunch of
[2487.50 --> 2487.84]  startups
[2487.84 --> 2488.78]  working on
[2488.78 --> 2489.78]  explainability
[2489.78 --> 2490.46]  for
[2490.46 --> 2491.60]  machine
[2491.60 --> 2491.96]  learning
[2491.96 --> 2492.40]  and deep
[2492.40 --> 2492.70]  learning.
[2494.44 --> 2495.92]  And I've
[2495.92 --> 2496.44]  always tried
[2496.44 --> 2497.78]  to get
[2497.78 --> 2498.28]  them to
[2498.28 --> 2498.82]  think about
[2498.82 --> 2499.50]  it more
[2499.50 --> 2499.98]  ambitiously,
[2500.22 --> 2500.52]  which is,
[2500.62 --> 2500.80]  you know,
[2500.86 --> 2501.94]  don't aim
[2501.94 --> 2502.44]  your tools
[2502.44 --> 2502.90]  at the
[2502.90 --> 2503.78]  model builders
[2503.78 --> 2504.32]  and the
[2504.32 --> 2505.02]  data engineers
[2505.02 --> 2505.44]  and machine
[2505.44 --> 2506.10]  learning engineers
[2506.10 --> 2506.50]  and data
[2506.50 --> 2506.98]  scientists in
[2506.98 --> 2507.34]  the back
[2507.34 --> 2507.62]  end and
[2507.62 --> 2508.20]  helping them
[2508.20 --> 2509.30]  understand how
[2509.30 --> 2509.80]  their model
[2509.80 --> 2510.30]  is working
[2510.30 --> 2511.74]  and therefore
[2511.74 --> 2512.64]  help them
[2512.64 --> 2513.16]  improve their
[2513.16 --> 2513.44]  model,
[2513.52 --> 2513.80]  which is
[2513.80 --> 2514.08]  great.
[2514.64 --> 2516.06]  But make
[2516.06 --> 2517.90]  yourself have
[2517.90 --> 2518.96]  a role for
[2518.96 --> 2519.64]  the end user,
[2519.84 --> 2519.98]  right?
[2520.10 --> 2520.24]  So,
[2520.46 --> 2522.12]  if I have
[2522.12 --> 2522.48]  a machine
[2522.48 --> 2522.86]  learning
[2522.86 --> 2524.56]  product or
[2524.56 --> 2525.20]  a product
[2525.20 --> 2525.52]  in the
[2525.52 --> 2526.46]  enterprise that
[2526.46 --> 2527.64]  I want more
[2527.64 --> 2528.66]  people in the
[2528.66 --> 2529.22]  company to
[2529.22 --> 2529.54]  use,
[2529.66 --> 2530.38]  maybe there's
[2530.38 --> 2531.70]  an explainability
[2531.70 --> 2532.96]  widget that
[2532.96 --> 2533.62]  allows them to
[2533.62 --> 2533.98]  get more
[2533.98 --> 2535.34]  comfortable so
[2535.34 --> 2535.86]  that they end
[2535.86 --> 2536.40]  up using the
[2536.40 --> 2536.92]  system more.
[2537.22 --> 2537.46]  Gotcha.
[2538.12 --> 2539.26]  And as we
[2539.26 --> 2539.74]  kind of wind
[2539.74 --> 2540.20]  up here,
[2540.82 --> 2541.14]  I wanted to
[2541.14 --> 2541.76]  ask kind of a
[2541.76 --> 2543.26]  very high-in-the-sky
[2543.26 --> 2543.74]  open-ended
[2543.74 --> 2544.34]  question and
[2544.34 --> 2545.18]  just kind of
[2545.18 --> 2546.34]  where you have
[2546.34 --> 2546.94]  this opportunity
[2546.94 --> 2548.02]  to talk to so
[2548.02 --> 2548.48]  many different
[2548.48 --> 2549.82]  companies and
[2549.82 --> 2550.44]  get perspectives.
[2550.66 --> 2551.52]  I'd love it if
[2551.52 --> 2552.02]  you would just
[2552.02 --> 2552.90]  kind of share
[2552.90 --> 2553.52]  where you think,
[2553.88 --> 2555.06]  how you think
[2555.06 --> 2555.70]  this field is
[2555.70 --> 2556.36]  going to evolve
[2556.36 --> 2558.12]  over the
[2558.12 --> 2559.24]  relatively near
[2559.24 --> 2559.82]  future over the
[2559.82 --> 2560.32]  next few years.
[2560.38 --> 2560.82]  I'm not asking
[2560.82 --> 2561.42]  for long-term
[2561.42 --> 2562.62]  prediction,
[2562.82 --> 2564.04]  but where do you
[2564.04 --> 2564.64]  think we're going
[2564.64 --> 2565.90]  as a kind of
[2565.90 --> 2566.44]  in an overview,
[2566.56 --> 2567.10]  as a summary?
[2567.36 --> 2568.38]  How do you see
[2568.38 --> 2569.14]  this field evolving?
[2569.14 --> 2570.60]  So I think on
[2570.60 --> 2571.64]  the research side,
[2571.78 --> 2572.54]  the researchers
[2572.54 --> 2573.80]  will continue to
[2573.80 --> 2574.94]  publish at a
[2574.94 --> 2575.98]  furious pace,
[2576.24 --> 2576.40]  right?
[2577.66 --> 2579.76]  And a lot of
[2579.76 --> 2582.38]  that research is
[2582.38 --> 2583.10]  now in the
[2583.10 --> 2583.52]  open,
[2584.00 --> 2585.10]  usually with
[2585.10 --> 2587.18]  code using
[2587.18 --> 2588.42]  open-source
[2588.42 --> 2589.02]  libraries so
[2589.02 --> 2589.68]  people can take
[2589.68 --> 2590.38]  advantage of that
[2590.38 --> 2590.84]  research.
[2591.98 --> 2593.32]  On the
[2593.32 --> 2594.34]  enterprise side,
[2594.46 --> 2594.92]  I think
[2594.92 --> 2597.64]  companies will
[2597.64 --> 2599.16]  continue to
[2599.16 --> 2600.48]  struggle if
[2600.48 --> 2600.98]  they don't
[2600.98 --> 2601.80]  understand the
[2601.80 --> 2602.52]  limitations of
[2602.52 --> 2603.44]  these technologies
[2603.44 --> 2604.66]  and understand
[2604.66 --> 2606.90]  how they work
[2606.90 --> 2609.80]  and how these
[2609.80 --> 2610.70]  models get built.
[2612.28 --> 2613.10]  So I think
[2613.10 --> 2613.80]  there's a certain
[2613.80 --> 2614.80]  level of education
[2614.80 --> 2615.92]  that needs to
[2615.92 --> 2616.80]  take place across
[2616.80 --> 2617.46]  the company,
[2617.96 --> 2618.94]  not just the
[2618.94 --> 2619.60]  technologists.
[2621.62 --> 2622.42]  And then I
[2622.42 --> 2623.40]  think as
[2623.40 --> 2625.08]  companies become
[2625.08 --> 2625.78]  more comfortable
[2625.78 --> 2626.56]  with machine
[2626.56 --> 2627.42]  learning and AI,
[2627.42 --> 2628.90]  they'll realize
[2628.90 --> 2629.66]  they need to
[2629.66 --> 2630.64]  build some of
[2630.64 --> 2631.20]  these foundational
[2631.20 --> 2631.82]  pieces.
[2632.82 --> 2633.52]  But also the
[2633.52 --> 2634.52]  industry needs to
[2634.52 --> 2636.04]  help companies
[2636.04 --> 2636.64]  by building
[2636.64 --> 2637.70]  better tools for
[2637.70 --> 2638.82]  machine learning
[2638.82 --> 2639.44]  development,
[2640.34 --> 2641.20]  model governance,
[2641.58 --> 2642.46]  model operations,
[2643.22 --> 2644.34]  and frankly
[2644.34 --> 2645.24]  automation as
[2645.24 --> 2645.44]  well.
[2647.84 --> 2648.70]  It's no
[2648.70 --> 2649.78]  surprise that
[2649.78 --> 2650.90]  one of the
[2650.90 --> 2651.76]  areas in
[2651.76 --> 2652.56]  technology where
[2652.56 --> 2653.20]  you're seeing a
[2653.20 --> 2654.02]  lot of automation
[2654.02 --> 2654.76]  is in data
[2654.76 --> 2655.60]  science and data
[2655.60 --> 2656.56]  engineering itself.
[2656.56 --> 2658.36]  because these
[2658.36 --> 2659.14]  are the people
[2659.14 --> 2660.02]  who understand
[2660.02 --> 2660.78]  this technology
[2660.78 --> 2661.44]  and what are
[2661.44 --> 2661.82]  they going to
[2661.82 --> 2662.00]  do?
[2662.10 --> 2662.48]  They're going to
[2662.48 --> 2663.06]  automate the
[2663.06 --> 2663.66]  things that they
[2663.66 --> 2664.24]  can automate.
[2664.50 --> 2664.88]  Absolutely.
[2665.14 --> 2667.12]  So to the
[2667.12 --> 2668.04]  extent that
[2668.04 --> 2670.26]  you're studying
[2670.26 --> 2671.30]  data science
[2671.30 --> 2671.94]  today,
[2672.78 --> 2674.12]  don't be surprised
[2674.12 --> 2675.18]  if by the time
[2675.18 --> 2675.80]  you graduate,
[2675.96 --> 2676.34]  some of the
[2676.34 --> 2676.66]  things you
[2676.66 --> 2677.32]  studied have been
[2677.32 --> 2677.80]  automated.
[2678.16 --> 2678.42]  Yes.
[2678.68 --> 2679.42]  I would agree
[2679.42 --> 2679.78]  with that.
[2679.94 --> 2680.36]  I think that
[2680.36 --> 2680.92]  process is
[2680.92 --> 2681.82]  accelerating too.
[2681.82 --> 2683.48]  Well, thank you
[2683.48 --> 2683.90]  very much.
[2683.94 --> 2684.34]  It's been a great
[2684.34 --> 2685.12]  conversation with
[2685.12 --> 2685.28]  you.
[2685.82 --> 2686.24]  I know you
[2686.24 --> 2686.68]  have been,
[2686.84 --> 2687.82]  as I've watched,
[2688.12 --> 2688.90]  you've been very
[2688.90 --> 2689.54]  busy through this
[2689.54 --> 2690.66]  conference as the
[2690.66 --> 2691.30]  program chair,
[2691.38 --> 2691.88]  so thanks for
[2691.88 --> 2692.38]  taking a few
[2692.38 --> 2694.24]  minutes to talk
[2694.24 --> 2694.70]  with me about
[2694.70 --> 2695.04]  this.
[2695.42 --> 2696.40]  And if listeners
[2696.40 --> 2699.08]  want to reach out
[2699.08 --> 2700.08]  to you, how can
[2700.08 --> 2701.02]  they access you?
[2701.08 --> 2701.52]  Are you out on
[2701.52 --> 2702.04]  social media?
[2702.42 --> 2702.80]  Yes.
[2702.88 --> 2703.60]  So my Twitter
[2703.60 --> 2704.16]  handle is
[2704.16 --> 2704.96]  impossible to
[2704.96 --> 2705.30]  remember.
[2705.46 --> 2705.96]  It's at
[2705.96 --> 2706.58]  big data.
[2706.58 --> 2707.92]  And then if
[2707.92 --> 2708.32]  you want to
[2708.32 --> 2709.10]  reach me on
[2709.10 --> 2711.00]  email, I have
[2711.00 --> 2711.78]  an impossibly
[2711.78 --> 2712.76]  hard to remember
[2712.76 --> 2713.84]  email address,
[2714.46 --> 2716.90]  datascientist.gmail.com.
[2717.32 --> 2718.68]  Those are two
[2718.68 --> 2720.32]  fantastic handles
[2720.32 --> 2720.62]  there.
[2721.28 --> 2721.96]  So, well, thank
[2721.96 --> 2722.60]  you very much,
[2722.74 --> 2723.62]  and I'll let you
[2723.62 --> 2724.08]  get back to the
[2724.08 --> 2724.36]  conference.
[2724.84 --> 2725.28]  Thank you.
[2727.78 --> 2728.30]  All right.
[2728.36 --> 2728.78]  Thank you for
[2728.78 --> 2729.46]  tuning into this
[2729.46 --> 2730.36]  episode of
[2730.36 --> 2731.02]  Practically I.
[2731.20 --> 2731.64]  If you enjoyed
[2731.64 --> 2732.28]  the show, do us
[2732.28 --> 2733.04]  a favor, go on
[2733.04 --> 2733.74]  iTunes, give us
[2733.74 --> 2734.66]  a rating, go in
[2734.66 --> 2735.62]  your podcast app
[2735.62 --> 2736.32]  and favorite it.
[2736.32 --> 2737.00]  If you are on
[2737.00 --> 2737.74]  Twitter or social
[2737.74 --> 2738.54]  network, share a
[2738.54 --> 2739.16]  link with a friend,
[2739.24 --> 2739.66]  whatever you got to
[2739.66 --> 2740.54]  do, share the show
[2740.54 --> 2741.00]  with a friend if
[2741.00 --> 2741.60]  you enjoyed it.
[2741.88 --> 2742.56]  And bandwidth for
[2742.56 --> 2743.36]  changelog is
[2743.36 --> 2744.00]  provided by
[2744.00 --> 2744.56]  Fastly.
[2744.68 --> 2745.24]  Learn more at
[2745.24 --> 2746.10]  fastly.com.
[2746.30 --> 2747.00]  And we catch our
[2747.00 --> 2747.68]  errors before our
[2747.68 --> 2748.34]  users do here at
[2748.34 --> 2749.10]  changelog because of
[2749.10 --> 2749.50]  Rollbar.
[2749.74 --> 2750.60]  Check them out at
[2750.60 --> 2751.44]  rollbar.com slash
[2751.44 --> 2752.12]  changelog.
[2752.40 --> 2753.64]  And we're hosted on
[2753.64 --> 2754.92]  Linode cloud servers
[2754.92 --> 2756.38]  at linode.com slash
[2756.38 --> 2756.90]  changelog.
[2757.00 --> 2757.44]  Check them out.
[2757.52 --> 2758.34]  Support this show.
[2758.76 --> 2759.78]  This episode is
[2759.78 --> 2760.66]  hosted by Daniel
[2760.66 --> 2761.38]  Whitenack and
[2761.38 --> 2761.92]  Chris Benson.
[2762.38 --> 2763.42]  The music is by
[2763.42 --> 2764.44]  Breakmaster Cylinder.
[2764.82 --> 2765.44]  And you can find
[2765.44 --> 2766.20]  more shows just
[2766.20 --> 2767.12]  like this at
[2767.12 --> 2768.26]  changelog.com.
[2768.46 --> 2769.12]  When you go there,
[2769.20 --> 2769.92]  pop in your email
[2769.92 --> 2770.96]  address, get our
[2770.96 --> 2771.94]  weekly email, keeping
[2771.94 --> 2772.66]  you up to date with
[2772.66 --> 2773.48]  the news and
[2773.48 --> 2774.14]  podcasts for
[2774.14 --> 2775.24]  developers in your
[2775.24 --> 2776.38]  inbox every single
[2776.38 --> 2776.74]  week.
[2777.10 --> 2777.92]  Thanks for tuning in.
[2778.08 --> 2778.56]  We'll see you next
[2778.56 --> 2778.84]  week.
[2778.84 --> 2789.22]  Congratulations.
[2789.22 --> 2791.20]  You've listened all the
[2791.20 --> 2792.20]  way to the end of the
[2792.20 --> 2792.54]  show.
[2792.54 --> 2793.66]  And guess what?
[2793.92 --> 2794.68]  Got a little surprise
[2794.68 --> 2794.96]  for you.
[2795.30 --> 2796.14]  Here's a preview of
[2796.14 --> 2796.92]  Brain Science, our
[2796.92 --> 2798.04]  upcoming podcast coming
[2798.04 --> 2798.90]  out very soon.
[2799.22 --> 2800.14]  The easiest way to
[2800.14 --> 2801.32]  subscribe is to
[2801.32 --> 2801.98]  subscribe to our
[2801.98 --> 2803.44]  master feed at the
[2803.44 --> 2805.20]  changelog.com slash
[2805.20 --> 2805.70]  master.
[2805.70 --> 2806.72]  Get all of our
[2806.72 --> 2808.14]  podcasts in one
[2808.14 --> 2809.52]  single feed, plus
[2809.52 --> 2810.20]  some extras that
[2810.20 --> 2811.00]  only hit the
[2811.00 --> 2812.48]  master feed, including
[2812.48 --> 2813.34]  Brain Science.
[2813.74 --> 2815.08]  Brain Science is a
[2815.08 --> 2815.84]  podcast for the
[2815.84 --> 2816.18]  curious.
[2816.40 --> 2816.92]  We're exploring the
[2816.92 --> 2817.88]  inner workings of the
[2817.88 --> 2818.82]  human brain so we can
[2818.82 --> 2819.52]  understand things like
[2819.52 --> 2821.12]  behavior change, habit
[2821.12 --> 2822.66]  formation, mental
[2822.66 --> 2823.94]  health, and this thing
[2823.94 --> 2824.62]  we call the human
[2824.62 --> 2825.08]  condition.
[2825.34 --> 2826.40]  It's hosted by myself,
[2826.52 --> 2827.84]  Adam Stachowiak, and
[2827.84 --> 2829.70]  Meryl Reese, a doctor in
[2829.70 --> 2830.52]  clinical psychology.
[2830.98 --> 2831.80]  It's brain science
[2831.80 --> 2832.84]  applied, not just how does
[2832.84 --> 2834.08]  the brain work, but how
[2834.08 --> 2835.22]  do we apply what we
[2835.22 --> 2836.52]  know about the brain to
[2836.52 --> 2837.44]  better our lives?
[2837.98 --> 2838.38]  Here we go.
[2840.28 --> 2841.76]  As humans, one of the
[2841.76 --> 2843.08]  things that separates us
[2843.08 --> 2844.32]  from any other animal
[2844.32 --> 2846.14]  out there is the fact
[2846.14 --> 2847.04]  that we have language,
[2847.24 --> 2848.80]  we have words, and we
[2848.80 --> 2849.82]  have super powerful words
[2849.82 --> 2851.02]  that truly change how we
[2851.02 --> 2851.94]  feel and how we make
[2851.94 --> 2852.84]  other people feel.
[2853.18 --> 2855.42]  If the words we say have
[2855.42 --> 2856.48]  so much potential to
[2856.48 --> 2858.46]  influence ourselves and
[2858.46 --> 2859.48]  the world around us, how
[2859.48 --> 2860.14]  do we begin to
[2860.14 --> 2861.02]  understand the power of
[2861.02 --> 2861.38]  words?
[2861.38 --> 2863.50]  So words really are the
[2863.50 --> 2864.50]  thing that separates us
[2864.50 --> 2866.22]  from all other animals
[2866.22 --> 2868.40]  because, right, sharks,
[2868.58 --> 2870.50]  bats, dogs, lizards, they
[2870.50 --> 2871.10]  don't talk.
[2871.60 --> 2873.48]  And this is really
[2873.48 --> 2875.00]  critical when it comes to
[2875.00 --> 2877.44]  managing our moods and
[2877.44 --> 2878.36]  our feelings.
[2879.00 --> 2881.06]  One of the things that I
[2881.06 --> 2882.14]  sort of talk about or even
[2882.14 --> 2883.34]  I mentioned earlier about
[2883.34 --> 2884.52]  the way in which we file
[2884.52 --> 2885.56]  things in our mind
[2885.56 --> 2887.52]  according to feelings, this
[2887.52 --> 2888.40]  is exactly how we
[2888.40 --> 2889.58]  differentiate it too.
[2889.58 --> 2891.76]  Thinking about an
[2891.76 --> 2893.38]  example like with
[2893.38 --> 2894.84]  professional athletes,
[2895.52 --> 2896.60]  they, you might say that
[2896.60 --> 2897.68]  they get anxious like
[2897.68 --> 2899.10]  before a race or before,
[2899.32 --> 2901.42]  you know, a run or a
[2901.42 --> 2901.74]  dive.
[2901.98 --> 2904.28]  But using that word, it's
[2904.28 --> 2906.04]  not really a threat, right?
[2906.10 --> 2907.16]  But their brain would be
[2907.16 --> 2908.30]  like, oh, I'm nervous and
[2908.30 --> 2909.10]  now I start this whole
[2909.10 --> 2910.86]  sequence of events in my
[2910.86 --> 2911.18]  body.
[2911.38 --> 2912.80]  Whereas if I just change
[2912.80 --> 2914.20]  the word to like I'm
[2914.20 --> 2916.16]  anticipating or I'm
[2916.16 --> 2918.86]  excited, it creates a
[2918.86 --> 2920.94]  different sort of rollout
[2920.94 --> 2922.46]  of emotions as well as
[2922.46 --> 2923.70]  physiological responses.
[2924.20 --> 2926.04]  I mean, I'm anxious about
[2926.04 --> 2927.40]  going to Disneyland is not
[2927.40 --> 2929.06]  usually what we say, right?
[2929.26 --> 2929.80]  I'm excited.
[2931.08 --> 2931.56]  Exactly.
[2932.20 --> 2932.56]  Exactly.
[2932.72 --> 2934.84]  So it then puts a lid on or
[2934.84 --> 2937.04]  files things differently in
[2937.04 --> 2938.74]  our mind, which then
[2938.74 --> 2939.86]  changes how we feel about
[2939.86 --> 2940.08]  it.
[2940.46 --> 2942.18]  So in my field in
[2942.18 --> 2943.38]  psychology, I would say,
[2943.76 --> 2944.64]  we would say name it to
[2944.64 --> 2945.02]  tame it.
[2945.02 --> 2946.38]  The better I can name
[2946.38 --> 2948.00]  different feelings, the
[2948.00 --> 2949.54]  more I can tame whatever
[2949.54 --> 2950.56]  emotion that is.
[2951.06 --> 2952.26]  And so then I'm not really
[2952.26 --> 2954.16]  stuck living in this sort of
[2954.16 --> 2955.48]  mammal and reptile lane
[2955.48 --> 2956.46]  where I'm always just
[2956.46 --> 2957.46]  flipping my lid.
[2957.54 --> 2958.32]  I'm reactive.
[2958.64 --> 2960.36]  I'm angry or I'm sad.
[2960.76 --> 2962.64]  But rather I can go, I
[2962.64 --> 2964.40]  recognize this is how I'm
[2964.40 --> 2966.22]  feeling or like I'm afraid
[2966.22 --> 2968.78]  of some other threat, like
[2968.78 --> 2969.94]  losing my job.
[2970.22 --> 2971.92]  And I can go, you know
[2971.92 --> 2972.26]  what?
[2972.26 --> 2973.70]  Here's the words I can use
[2973.70 --> 2975.12]  to talk to myself about
[2975.12 --> 2976.72]  that fear so that I'm not
[2976.72 --> 2978.70]  just stuck feeling
[2978.70 --> 2980.56]  afraid of a possible
[2980.56 --> 2981.40]  threat, which has never
[2981.40 --> 2981.94]  occurred yet.
[2982.60 --> 2983.78]  You use this concept to
[2983.78 --> 2984.90]  to say customized
[2984.90 --> 2985.62]  thinking.
[2987.02 --> 2988.12]  I'm not sure I fully
[2988.12 --> 2988.90]  understand what you mean
[2988.90 --> 2989.96]  by customized thinking.
[2990.04 --> 2990.72]  What do you mean by that?
[2991.36 --> 2993.00]  Well, because
[2993.00 --> 2994.96]  we are human, we do
[2994.96 --> 2996.10]  have the power of choice,
[2996.16 --> 2996.64]  which is
[2996.64 --> 2998.44]  super powerful.
[2998.44 --> 2999.62]  Like nobody has to tell
[2999.62 --> 3000.74]  you how you need to think
[3000.74 --> 3001.68]  or how you need to feel.
[3002.22 --> 3002.42]  Right.
[3002.52 --> 3003.92]  And like your version of
[3003.92 --> 3005.36]  success might be very
[3005.36 --> 3006.72]  different than mine, which
[3006.72 --> 3008.32]  is going to impact my
[3008.32 --> 3010.46]  decision, my choices and
[3010.46 --> 3011.36]  the direction I'm headed.
[3011.68 --> 3013.68]  And so when you think about
[3013.68 --> 3014.90]  customized, right, I mean,
[3014.94 --> 3016.50]  you can customize a car.
[3017.00 --> 3018.68]  You can customize your order
[3018.68 --> 3019.46]  at a restaurant.
[3019.76 --> 3022.24]  Like it really is tailored
[3022.24 --> 3024.00]  specifically to you and
[3024.00 --> 3025.64]  going, how do I want to
[3025.64 --> 3026.60]  think and how do I want to
[3026.60 --> 3026.88]  feel?
[3026.88 --> 3030.06]  One example I consider is
[3030.06 --> 3032.60]  I want to always
[3032.60 --> 3034.26]  I want every day of the
[3034.26 --> 3035.60]  week to feel like I do on
[3035.60 --> 3037.66]  the weekend because to me
[3037.66 --> 3038.66]  the weekend feels great.
[3038.66 --> 3040.12]  I'm with my family.
[3040.26 --> 3042.06]  I don't I'm not sort of
[3042.06 --> 3043.86]  running things with such a
[3043.86 --> 3044.56]  tight timeline.
[3045.00 --> 3046.36]  And there's just a different
[3046.36 --> 3047.64]  sort of ethereal
[3047.64 --> 3049.84]  vibe to the weekend.
[3050.00 --> 3050.22]  Right.
[3050.42 --> 3051.94]  And I think why does that
[3051.94 --> 3052.94]  only have to exist on the
[3052.94 --> 3053.16]  weekend?
[3054.02 --> 3054.42]  Yeah.
[3054.42 --> 3055.48]  I want that every day.
[3055.48 --> 3056.10]  Why is that?
[3056.74 --> 3057.64]  I want that every day too.
[3059.50 --> 3060.78]  Well, and I think part of it
[3060.78 --> 3062.40]  is really our attitude and
[3062.40 --> 3063.20]  our expectations.
[3063.98 --> 3065.74]  I mean, there are legitimate
[3065.74 --> 3067.80]  threats all around us, but
[3067.80 --> 3070.40]  it doesn't help me do me or
[3070.40 --> 3072.50]  do my life any better if I am
[3072.50 --> 3074.50]  only focused on threats.
[3075.00 --> 3076.64]  So I want to practice changing
[3076.64 --> 3078.10]  the channel in my mind that
[3078.10 --> 3080.24]  says, hey, yeah, I see that
[3080.24 --> 3082.14]  potential job loss, but I also
[3082.14 --> 3084.06]  see I'm with my family right
[3084.06 --> 3084.34]  now.
[3084.52 --> 3087.00]  And right now, nobody can
[3087.00 --> 3089.10]  take sort of what I've been
[3089.10 --> 3090.96]  through and how I feel
[3090.96 --> 3091.66]  away from me.
[3091.96 --> 3093.46]  I'm in charge of how I feel.
[3093.84 --> 3095.28]  So I'm going to do things that
[3095.28 --> 3096.68]  actually contribute to
[3096.68 --> 3097.70]  feeling better.
[3098.08 --> 3099.64]  So how do we apply this
[3099.64 --> 3101.18]  name is the tame it idea to
[3101.18 --> 3102.20]  this model then?
[3102.56 --> 3104.26]  Because maybe if you name
[3104.26 --> 3106.20]  the week, the weekend, can
[3106.20 --> 3108.00]  you change how you feel about
[3108.00 --> 3108.28]  it?
[3108.52 --> 3109.40]  Because that's really what it's
[3109.40 --> 3109.58]  about.
[3109.64 --> 3111.90]  Like, how do we take, you
[3111.90 --> 3113.06]  know, the labels we apply
[3113.06 --> 3115.50]  things to things, the names
[3115.50 --> 3116.98]  we give things, the words we
[3116.98 --> 3118.34]  use, the choices, what I
[3118.34 --> 3119.46]  think we might call nuance.
[3119.72 --> 3120.76]  I'm not really sure how you
[3120.76 --> 3122.92]  how you put that into play
[3122.92 --> 3123.90]  with the power of words.
[3124.00 --> 3125.84]  But the difference between,
[3125.84 --> 3127.40]  like you said before, being
[3127.40 --> 3128.62]  anxious or being excited,
[3129.62 --> 3130.96]  you know, fundamentally, it's
[3130.96 --> 3132.22]  almost the same feeling.
[3132.36 --> 3133.80]  But, you know, from a nuance
[3133.80 --> 3135.56]  level, it's very different.
[3135.56 --> 3137.90]  You know, it's one direction
[3137.90 --> 3139.20]  or the other of excitement,
[3139.66 --> 3140.72]  you know, negative excitement
[3140.72 --> 3142.18]  potentially or positive
[3142.18 --> 3142.62]  excitement.
[3142.92 --> 3143.78]  How do we apply that to
[3143.78 --> 3144.72]  customized thinking?
[3145.46 --> 3146.84]  Well, I think that's a great
[3146.84 --> 3147.52]  way to say it, Adam.
[3147.60 --> 3148.78]  I really like that nuance
[3148.78 --> 3151.06]  because what we're looking
[3151.06 --> 3153.50]  for, even as I talk about
[3153.50 --> 3155.50]  the different brains, we want
[3155.50 --> 3156.12]  a symphony.
[3156.54 --> 3157.74]  I mean, I'm not going to fire
[3157.74 --> 3159.36]  the woodwind section because I
[3159.36 --> 3160.04]  don't like a violin.
[3160.40 --> 3160.80]  Right.
[3160.84 --> 3162.04]  So I don't want to fire a
[3162.04 --> 3163.28]  certain part of my brain like
[3163.28 --> 3164.18]  you're not really helpful.
[3164.18 --> 3165.62]  I don't need to see that.
[3166.24 --> 3168.88]  But what we need is a sense
[3168.88 --> 3170.40]  of congruence.
[3171.26 --> 3173.00]  And so, sure, not every day
[3173.00 --> 3174.68]  of the week can feel exactly
[3174.68 --> 3175.48]  like the weekend.
[3175.62 --> 3177.98]  So I'm not going to say this
[3177.98 --> 3180.68]  is how I feel, but I have to
[3180.68 --> 3182.72]  actually believe it for it to
[3182.72 --> 3186.80]  impact my mind, my brain and
[3186.80 --> 3188.10]  my body in the way in which I
[3188.10 --> 3188.86]  desire it to.
[3189.76 --> 3191.14]  And so I might use the words
[3191.14 --> 3194.16]  like I strive for every day
[3194.16 --> 3197.32]  to have a feeling that reminds
[3197.32 --> 3199.54]  me of exactly how I feel on
[3199.54 --> 3201.24]  the weekend so that I don't
[3201.24 --> 3202.74]  lose sight that like every day
[3202.74 --> 3204.68]  really is a gift and I get to
[3204.68 --> 3207.12]  enjoy every day of my life to
[3207.12 --> 3207.66]  some degree.
[3208.60 --> 3211.02]  And so another example might be
[3211.02 --> 3213.36]  I'm living out in the Pacific
[3213.36 --> 3213.76]  Northwest.
[3214.04 --> 3215.76]  A lot of people have negative
[3215.76 --> 3216.84]  feelings about the weather.
[3217.50 --> 3218.20]  Imagine that.
[3218.20 --> 3221.36]  But so if someone were to say
[3221.36 --> 3223.82]  that they just need to learn to
[3223.82 --> 3225.72]  love it, that's going to create
[3225.72 --> 3227.58]  what we call cognitive dissonance.
[3227.64 --> 3228.42]  It doesn't fit.
[3228.86 --> 3229.98]  So it doesn't matter how much I'm
[3229.98 --> 3232.62]  like, oh, I do love the gray.
[3232.78 --> 3234.00]  I do love the clouds.
[3234.20 --> 3236.32]  It's not going to jive with me.
[3236.40 --> 3237.46]  And so it won't stick.
[3237.92 --> 3241.34]  So instead, I can say I love the
[3241.34 --> 3244.16]  way in which the rain creates the
[3244.16 --> 3244.54]  green.
[3244.54 --> 3246.42]  And in the summer, when it is
[3246.42 --> 3247.64]  green, it is amazing.
[3248.38 --> 3250.00]  This idea of learning to live with
[3250.00 --> 3251.36]  it, though, get over it.
[3251.88 --> 3253.22]  It is what it is.
[3253.36 --> 3255.56]  Like there's so many phrases we
[3255.56 --> 3257.06]  use to say just that, like just
[3257.06 --> 3257.90]  learn to live with it.
[3258.18 --> 3258.90]  What is it called again?
[3259.52 --> 3260.64]  Cognitive dissonance.
[3260.98 --> 3261.88]  And what does that mean when you
[3261.88 --> 3262.38]  play it out?
[3262.88 --> 3264.04]  It doesn't go together.
[3264.18 --> 3267.18]  So that if you're like, oh, just
[3267.18 --> 3268.22]  just do it.
[3268.28 --> 3269.36]  You just need to get over it.
[3269.44 --> 3271.04]  Like that really isn't helpful
[3271.04 --> 3273.06]  either because your body is giving
[3273.06 --> 3274.92]  you a signal and your brain is
[3274.92 --> 3276.36]  telling you, I don't like this
[3276.36 --> 3276.84]  sensation.
[3277.10 --> 3278.64]  I don't like how this feel.
[3278.74 --> 3280.08]  I mean, a lot of people will say,
[3280.50 --> 3282.48]  oh, I just hate the gray and the
[3282.48 --> 3283.82]  gray is just overwhelming.
[3284.68 --> 3287.40]  And so we have to go, well, what's
[3287.40 --> 3288.78]  my emotional buy in?
[3289.12 --> 3291.30]  Like what what do I like?
[3291.30 --> 3294.60]  How does that even allow me to
[3294.60 --> 3295.76]  enjoy something else?
[3295.88 --> 3299.56]  And so I'm going to look at going,
[3299.76 --> 3300.08]  you know what?
[3300.08 --> 3301.44]  I really like that I get to wear
[3301.44 --> 3304.14]  warm clothes or I really do love
[3304.14 --> 3306.72]  my coffee because it's for such a
[3306.72 --> 3307.20]  long time.
[3307.24 --> 3308.02]  It's gray and rainy.
[3308.12 --> 3309.48]  I want to be inside by a fire
[3309.48 --> 3310.40]  drinking my coffee.
[3310.54 --> 3310.84]  Right.
[3311.02 --> 3313.06]  And so how can I look for going,
[3313.14 --> 3313.64]  you know what?
[3313.98 --> 3316.46]  If I do these things I might not
[3316.46 --> 3319.02]  want to do, I do get some more of
[3319.02 --> 3320.28]  what I do want to do.
[3320.64 --> 3322.68]  And so it's really almost like a
[3322.68 --> 3324.92]  bartering system in your brain of
[3324.92 --> 3326.40]  saying if you do this thing you
[3326.40 --> 3328.34]  don't like, you get this thing you
[3328.34 --> 3331.56]  you do like or, you know, I know
[3331.56 --> 3334.26]  you don't have to make yourself do
[3334.26 --> 3337.18]  this thing unless you can see a way
[3337.18 --> 3339.84]  in which it actually benefits you or
[3339.84 --> 3341.84]  speaks to you emotionally.
[3342.80 --> 3344.78]  Everything Adam really has to have
[3344.78 --> 3346.12]  this emotional buy in.
[3346.68 --> 3350.10]  And if there's no good emotion, no
[3350.10 --> 3352.74]  really the primary neuro neurochemical
[3352.74 --> 3354.86]  in our brain is dopamine for feeling
[3354.86 --> 3355.18]  good.
[3355.18 --> 3357.24]  I don't get some hit of dopamine.
[3357.84 --> 3359.36]  My brain's going to be like, it's not
[3359.36 --> 3361.10]  worth it and I'm not going to do it.
[3361.48 --> 3361.88]  Period.
[3365.38 --> 3367.28]  That's a preview of brain science.
[3367.40 --> 3368.54]  If you love where we're going with
[3368.54 --> 3371.04]  this, send us an email to get on the
[3371.04 --> 3373.76]  list to be notified the very moment
[3373.76 --> 3374.82]  this show gets released.
[3375.18 --> 3377.90]  Email us at editors at change law dot
[3377.90 --> 3379.90]  com in the subject line put in all
[3379.90 --> 3382.58]  caps brain science with a couple
[3382.58 --> 3383.00]  bangs.
[3383.00 --> 3384.54]  If you're really excited, you can
[3384.54 --> 3386.36]  also subscribe to our master feed to
[3386.36 --> 3388.18]  get all of our shows in one single
[3388.18 --> 3390.56]  feed at the change law dot com slash
[3390.56 --> 3393.64]  master or search in your podcast app
[3393.64 --> 3394.54]  for change all master.
[3394.66 --> 3395.82]  You'll find it subscribe.
[3396.02 --> 3398.04]  Get all of our shows and even those
[3398.04 --> 3400.32]  that only hit the master feed again.
[3400.44 --> 3401.88]  Change law dot com slash master.
[3401.88 --> 3403.34]  Fire with the
[3403.34 --> 3404.22]  number of agents who treat
[3404.22 --> 3405.78]  today.
[3405.78 --> 3407.28]  Bye-bye.
[3407.28 --> 3408.26]  So we find more
[3408.26 --> 3409.62]  questions.
[3409.68 --> 3410.78]  Have a lot of
[3410.82 --> 3411.26]  wynn.
[3411.26 --> 3412.02]  We'll see you travel
[3412.68 --> 3413.42]  here now.
[3414.42 --> 3415.40]  Viewers are
[3415.40 --> 3416.08]  s-cahn.
[3416.08 --> 3416.42]  The
[3416.42 --> 3417.50]  nosotros
[3417.50 --> 3418.40]  conoces
[3418.40 --> 3420.26]  makers
[3420.26 --> 3421.64]  matter all
[3421.64 --> 3422.26]  graduate
[3422.26 --> 3422.64]  story.
[3424.64 --> 3425.54]  For
[3425.54 --> 3426.54]  questions
[3426.54 --> 3427.70]  y
[3427.70 --> 3428.34]  porque
[3428.34 --> 3429.64]  once
[3429.64 --> 3429.92]  we've
[3429.92 --> 3431.06] wers
