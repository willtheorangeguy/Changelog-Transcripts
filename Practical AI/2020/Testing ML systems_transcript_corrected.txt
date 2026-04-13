[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.84] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.24 → 12.38] And we're hosted on Linde cloud servers.
[12.74 → 14.76] Head to Linode.com slash Changelog.
[17.72 → 19.56] Linde is our cloud server of choice.
[20.08 → 23.00] Grab the NATO plan for just $5 a month, just $5.
[23.38 → 28.56] That gets you a gig of RAM, a blazing fast 25 gig SSD, and one terabyte of transfer.
[28.56 → 31.32] Let's be honest, you can go a long ways on that $5.
[31.86 → 36.20] When you do need to scale up, their prices are predictable, so you can put your calculator down.
[36.30 → 36.86] You won't need it.
[37.16 → 42.34] We've been running Changelog.com on Linde for years, and we're always impressed by their award-winning support team.
[42.86 → 45.60] Check them out at Linode.com slash Changelog.
[45.78 → 48.96] Once again, that's Linode.com slash Changelog.
[58.56 → 65.64] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical, productive, and accessible to everyone.
[66.14 → 70.54] This is where conversations around AI, machine learning, and data science happen.
[71.04 → 75.28] Join the community and slack with us around various topics of the show at changelog.com slash community.
[75.60 → 76.44] Follow us on Twitter.
[76.54 → 78.04] We're at Practical AI FM.
[78.30 → 79.36] And now onto the show.
[79.36 → 88.34] All right, welcome to another episode of Practical AI.
[88.78 → 90.36] This is Daniel Whiten ack.
[90.48 → 100.08] I'm a data scientist with SIL International, and I'm joined, as always, by my co-host, Chris Benson, who is a principal AI strategist at Lockheed Martin.
[100.30 → 101.00] How's it going, Chris?
[101.28 → 102.30] Hey, it's going great, Daniel.
[102.32 → 102.78] How are you?
[103.18 → 104.68] Doing pretty good.
[104.68 → 112.30] The winter sickness is still going through our household, so still dealing with that, but otherwise doing pretty good.
[112.48 → 118.40] I think I've avoided most of it at this point, or at least got over the worst of it, so that's good.
[118.54 → 119.66] But how are things on your end?
[120.08 → 120.86] They're going well.
[121.28 → 128.80] You know, I wanted to note that thing from last week about us, because I had posted on some social media, and people were really surprised, so I thought I'd share it with the listeners.
[128.80 → 138.70] So, if you are a longtime listener of the podcast, we've been doing this for about a year and a half, and Daniel and I actually have never met in person until last week.
[139.02 → 140.96] We were at Project Voice in Chattanooga.
[141.26 → 142.40] The wonders of the internet.
[142.68 → 143.40] No kidding.
[143.60 → 152.46] And so, I had commented online how incredibly cool it is that you can develop such a great friendship and collaboration, and yet have never met each other in person.
[152.68 → 154.34] So, anyway, that's passed now.
[154.40 → 155.34] We've now met in person.
[155.60 → 157.52] It was like meeting family, I think, for us.
[157.52 → 158.32] Definitely.
[158.98 → 159.24] Yeah.
[159.42 → 161.06] And so, anyway, just a very cool thing.
[161.12 → 161.98] I just thought I'd relate that.
[162.20 → 163.30] So, yeah, doing great.
[163.68 → 164.32] Yeah, awesome.
[164.62 → 179.96] We're starting out, so this is one of our first episodes for the new year, a couple before this, but definitely want to start out this year promoting practical uses of AI and practicality in developing AI and machine learning systems.
[180.54 → 185.20] And I think we've got a great guest today to emphasize a lot of those things.
[185.20 → 195.58] So, we're joined by Tanya Allard, who's a developer advocate with Microsoft, a Google machine learning GDE, and a Python Software Foundation fellow.
[195.84 → 196.80] Thanks for joining us, Tanya.
[197.30 → 197.62] Hi.
[197.76 → 199.38] It's a pleasure joining you guys.
[199.90 → 200.26] Awesome.
[200.26 → 213.54] Well, maybe before we jump into some of the things you've been talking about and working on recently, if you could just give us a little bit of your background and how you got into machine learning and ended up at Microsoft.
[213.86 → 214.46] That would be awesome.
[214.46 → 219.38] Yeah, well, I started doing machine learning stuff during my PhD.
[220.10 → 229.84] I was using machine learning applied to material science, and it was basically to try and identify some materials that could be candidates for tissue replacement.
[229.84 → 234.42] So, it was a lot of optimization, a lot of material testing here and there.
[234.96 → 244.74] And over the course of my PhD, I realized that I really enjoyed the computational side of things much more than the experimental and research bit.
[244.74 → 254.40] So, after that, I transitioned into research software engineering, which was basically research engineering in research institutions in the UK.
[254.80 → 261.08] I then migrated into working for Hello Soda, that is a company that has machine learning as a service.
[261.86 → 266.94] And I was doing data engineering there, machine learning engineering, research engineering.
[266.94 → 271.28] So, it was pretty much everything as you normally do in a small company.
[271.64 → 286.24] And then that brought me into Microsoft because I was already doing a lot of community work, community engagement, doing GDE work with the GDE community in Google, all open source work that I do.
[286.72 → 289.86] And it's just the same line, perfect fit now for me.
[290.14 → 291.66] That's how I got into Microsoft.
[292.14 → 292.98] That's awesome.
[292.98 → 301.80] Yeah, and you mentioned a few things, like you held different positions like data engineering and machine learning engineering and data science and computational research.
[302.14 → 305.10] Sometimes this sort of titles gets a little bit fuzzy.
[305.26 → 315.54] I'm wondering from your perspective, I guess, one, how you would define what you did differently as a data engineer, maybe versus some of the more data science-y things.
[315.54 → 322.66] And then also, if that more focused engineering experience kind of influenced how you do machine learning.
[322.98 → 323.86] Yeah, right.
[324.16 → 328.42] I can say I've been working across the machine learning pipeline in all the different roles.
[329.04 → 334.64] And as you mentioned, a lot of these roles are very, very fuzzy or have a lot of things in common.
[334.64 → 346.36] So when people talk about, I don't know, data scientists and data engineering roles in machine learning research or machine learning engineer, rather, they try to use these Venn diagrams.
[346.36 → 351.02] And I found that this is not very descriptive.
[351.02 → 367.96] But rather, for example, if you're working on the data science side of the pipeline, you're focusing much more on the statistics, on developing novel algorithms or models that would help your business or your company to get most of their data or get good insights.
[367.96 → 380.96] But then you will probably have or need some software engineering skills as well to take that into a production format with the rest of your dev environment or your dev team.
[380.96 → 388.94] Whereas when you're working on the data engineering side of things, you're focusing much more on all the processes that are extraction, transform load.
[389.06 → 397.60] But sometimes you still have to know how that data is going to be integrated into your model so that the data is actually usable by the rest of the team.
[397.60 → 402.66] And then the machine learning engineer role is basically the one that binds it all together.
[402.86 → 418.54] It makes sure that everything is robust, accessible, that can be taken to production, that folks that are using the data that is being transformed or are being transformed by the data engineer is actually pulled into a reproducible manner.
[418.54 → 428.00] And you can always track where the data is coming to a problem at all times so that everything is tightly integrated within your data science infrastructure.
[428.64 → 439.10] So, you know, I was just looking, and I know Daniel had seen it already at your talks that you gave called what is your ML score that you went through at all things open in Anaconda Con.
[439.28 → 445.46] And in that talk, you were focused very much on kind of QA and testing of machine learning systems specifically.
[445.46 → 456.00] And I wanted to start off by just asking if, you know, as we've kind of talked about the roles there, if you could also talk a little bit about what is a machine learning system?
[456.24 → 458.90] You know, it's kind of a little bit of an ambiguous term.
[459.08 → 466.10] And could you kind of define what that means, and what types of things are included in a machine learning system or not?
[466.68 → 475.02] Yeah, well, it depends a lot on what data problems your company is working on or, sorry,
[475.02 → 477.78] or the kind of machine learning projects that you're normally working on.
[477.98 → 485.46] But normally the machine learning system is going to be comprised of wherever you're getting your data, which can be a canonical database.
[485.94 → 493.08] Then how the data is going to be pulled into your machine learning model or your prediction or classification model,
[493.16 → 495.40] whatever it is you're trying to do with that data.
[495.46 → 502.32] And then how you take that model into something usable by your customer or your teammates.
[502.32 → 506.06] And this can mean, are they going to access it through an API?
[506.56 → 508.96] Is this going to be a standalone web app?
[509.08 → 511.50] Is it going to be on a mobile device?
[511.72 → 513.64] And are you going to be accessing this model?
[513.96 → 520.28] So all of these apparently movable parts that conform to your data warehouse or your database,
[520.52 → 524.54] the infrastructure where you're running your prediction, where you're training your model,
[525.12 → 530.20] how you're collating your database, all of that forms your machine learning system.
[530.20 → 534.00] So it's a lot of data bits, a lot of infrastructure.
[534.60 → 540.10] And it could be like things on the cloud, for example, as well, like using the public cloud infrastructure.
[540.10 → 545.82] And I know like when you're talking about testing or validating the ML system,
[545.82 → 552.00] I was just thinking like if I was to ask, you know, a software engineer and ask them about testing,
[552.10 → 556.32] probably one of the things that comes to their mind is like unit testing or integration testing.
[556.32 → 562.22] Whereas if I ask a data scientist or maybe a machine learning engineer what they think about testing,
[562.36 → 567.60] probably the first thing that comes to their mind is testing of like a specific machine learning model,
[567.60 → 572.78] like the performance of that model in terms of accuracy or whatever the metric might be.
[573.24 → 577.64] And now we have this other kind of category of like machine learning system,
[577.64 → 582.44] which it sounds like is more broad than a machine learning model.
[582.70 → 589.10] How is the testing or validation of an ML system or a machine learning or AI system
[589.10 → 593.98] different from the testing of a specific machine learning model?
[593.98 → 601.10] Right. So I think because the ML, well, the machine learning system comprises all of your pipeline,
[601.30 → 606.90] it has to be a bit more holistic, a bit more integral and cover all the parts of that.
[607.06 → 610.00] So if we go back to traditional software engineering,
[610.36 → 616.96] during your testing that during your piece of software is returning the results that you're expecting it to do,
[617.16 → 620.72] because you already know what those results or those behaviours are,
[620.72 → 627.34] is it's relatively straightforward to design your test cases, create your unit test, your regression,
[627.60 → 628.90] and your smoke test cases.
[629.50 → 631.86] And they should always return the same thing, basically.
[632.42 → 636.00] Exactly. So it should be deterministic in that sense.
[636.10 → 639.40] When you're testing a machine learning system or a machine learning model,
[639.40 → 643.70] in many cases, you don't even know what that end result is,
[643.84 → 646.82] because you have your data, you have your labels,
[646.82 → 649.34] if you're doing, for example, a classification problem.
[649.76 → 653.74] But you need to make sure that your system is doing what it's meant to be doing,
[653.88 → 656.70] and that it's repeatable, that you can repeat all of that.
[657.42 → 663.24] So in that sense, you have to ensure that you're testing your data, your features,
[663.82 → 667.86] ensure that the data conforms to that distribution that you're expecting,
[668.00 → 669.56] and that behaviour that you're going to see.
[669.56 → 674.94] And also, the cost of adding more features to your predictive models is adding,
[675.12 → 679.96] because that's a major component, especially when you're doing things in the cloud.
[680.48 → 682.70] Sometimes, when you add one feature,
[683.16 → 687.30] you marginally increase that accuracy that you were talking about,
[687.58 → 692.52] but then your compute time or the use of resources that you're using doubles or triples.
[692.52 → 700.74] So you also have to take that into consideration to balance whether that very marginal increase in your accuracy
[700.74 → 705.14] is actually worth all that extra computes cost that you're incurring on.
[705.84 → 708.40] Also, when you're doing your model development,
[708.84 → 710.94] you have to look at things like your metrics,
[711.20 → 717.64] whether the impact of your hyperparameters is also causing impact on your compute resources,
[717.64 → 723.78] testing for implicit bias, testing for your staleness of your model,
[723.90 → 728.38] because you might then need to retrain your model after a certain period of time
[728.38 → 734.02] if you are acquiring new data or there are significant changes to the API.
[734.88 → 737.26] And then, again, you need to test your infrastructure.
[737.54 → 740.20] You need to make sure that you're able to deploy them,
[740.72 → 742.38] deploy your model, your infrastructure,
[742.72 → 746.88] probably using techniques like continuous integration and continuous delivery,
[746.88 → 750.64] because that's essential, especially if you release a new version of your model,
[750.98 → 753.72] although I just tested it before getting into production,
[753.72 → 758.68] it turns out that there is a bug or there's something that needs a rollback.
[758.78 → 764.84] Being able to know how long that rollback or that release is going to take you is crucial.
[765.32 → 770.06] So in that sense, you have to have integration tests against your entire pipeline,
[770.22 → 773.72] from data acquisition to data transformation, prediction,
[773.72 → 777.32] and then results serving, whatever that is for your system.
[777.32 → 780.30] So one of the things I wanted to ask, you know,
[780.42 → 783.26] I know that Daniel and I come from a software development background
[783.26 → 785.54] kind of before we were much into deep learning.
[785.74 → 789.16] And so it's kind of the idea of testing and why you test
[789.16 → 791.82] and the importance of testing is kind of second nature.
[791.82 → 795.38] But for somebody coming in to this, you know,
[795.42 → 798.48] into deep learning and trying to do these things, it may not be.
[798.58 → 800.38] So I'd like to ask you quite simply,
[800.38 → 805.76] why is testing or validation of machine learning systems so important?
[805.76 → 808.70] And what would be the downside of not doing that?
[808.70 → 814.90] I think one of the main advantages of you being able to test your machine learning model
[814.90 → 816.42] is explainability.
[816.76 → 820.22] As we're going into more complex frameworks
[820.22 → 823.50] or more complex deep learning algorithms,
[823.82 → 827.42] it starts becoming increasingly difficult to explain
[827.42 → 831.00] how to reach to a certain prediction and why.
[831.32 → 834.84] Especially when we're releasing machine learning out into the world
[834.84 → 836.30] and is affecting other people,
[836.30 → 838.22] I think it's crucial for us to know
[838.22 → 841.66] that it's actually predicting what we wanted to predict,
[841.90 → 844.20] that it's being transparent and clear,
[844.60 → 848.22] and that we can always trace all the predictions that we're doing.
[848.64 → 851.04] Also test for implicit bias is crucial,
[851.22 → 856.38] especially when we have data sets that are biased toward a certain feature
[856.38 → 859.18] or towards a certain portion of our population.
[859.74 → 863.02] Having tests in places throughout all of our pipeline ensures
[863.02 → 866.48] that we can mitigate those biases early on as well.
[866.96 → 869.92] So I think those are some of the most important reasons
[869.92 → 872.30] for us to be testing our algorithms.
[873.16 → 873.26] Yeah.
[873.38 → 874.72] And I mean, in certain cases,
[874.72 → 876.52] I know you're in Europe right now
[876.52 → 880.00] and there are certain regulations that have come down the pipeline there.
[880.06 → 881.96] And of course, you're influencing the rest of the world.
[881.96 → 885.48] So I guess it may be partly your own,
[886.12 → 889.38] you know, you're trying to create a development environment
[889.38 → 893.46] that is responsible, and you're able to repeat things
[893.46 → 896.34] and actually make incremental progress on things.
[896.42 → 899.10] But also, you might be under certain regulations, right?
[899.12 → 902.06] That you actually have to be able to, you know,
[902.16 → 904.88] give someone an explanation to some degree
[904.88 → 906.70] of what you did with their data.
[906.94 → 907.72] Is that right?
[908.08 → 908.78] That's correct.
[908.78 → 911.86] I think it was now over a year
[911.86 → 915.64] that all the things GDPR regulations took place.
[915.96 → 918.86] So one of the most significant things that this brings is
[918.86 → 922.90] that if a customer or someone from whom you're withholding
[922.90 → 924.72] any sort of data comes and tell you,
[925.44 → 927.36] hey, I want to see what you're doing with my data
[927.36 → 930.98] or I want to have access to all the data of myself
[930.98 → 931.96] that you're storing,
[932.58 → 937.34] you should be able to comply within a standard period of time.
[937.34 → 941.42] So if you don't have mechanisms in place for you to trace this data
[941.42 → 944.26] or trace what you were doing or even to delete,
[944.40 → 947.76] because now your customers should be able to ask you
[947.76 → 950.88] to delete all the data that you have in place for them,
[951.34 → 952.40] you should comply.
[952.58 → 953.74] That's now a regulation.
[954.08 → 957.06] And I think also having a better understanding,
[957.20 → 957.94] as I said before,
[958.28 → 960.42] of where your data sources are
[960.42 → 962.34] and what you're doing with the data
[962.34 → 964.74] and how you're moving it from one place to another
[964.74 → 968.38] is very, very important for reproducibility
[968.38 → 971.12] and assurance of our systems.
[971.82 → 977.00] So I know people that might be coming into AI and machine learning,
[977.00 → 978.56] maybe from a science background,
[979.14 → 981.88] or even, you know, there are a lot of different backgrounds,
[981.98 → 985.58] even things like economics or finance or that sort of thing.
[985.58 → 987.74] Some of these things around infrastructure,
[988.12 → 992.36] CCD monitoring might be sort of intimidating to them.
[992.72 → 994.98] I was wondering if you had any, you know,
[995.02 → 999.10] thoughts as far as who a data scientist needs to work with
[999.10 → 1001.86] to make sure that all the right testing is in place
[1001.86 → 1003.24] for a machine learning system,
[1003.30 → 1005.06] because it does impact,
[1005.22 → 1005.70] like you said,
[1005.78 → 1007.78] there are implications for infrastructure,
[1008.10 → 1009.04] for scaling up,
[1009.26 → 1010.88] for changes to data.
[1010.88 → 1014.04] Who does a data scientist need to be talking with
[1014.04 → 1016.16] to make sure that all the right testing
[1016.16 → 1018.30] and quality assurance pieces are in place?
[1018.90 → 1021.92] I think a good workflow would be to have
[1021.92 → 1025.78] the data science team working very, very closely
[1025.78 → 1028.22] with the machine learning engineering team,
[1028.30 → 1029.12] if there is one,
[1029.34 → 1031.86] or otherwise the software engineering team.
[1032.40 → 1034.00] If you have them sitting together
[1034.00 → 1036.22] or working very closely,
[1036.68 → 1038.48] it's easier for both teams,
[1038.58 → 1039.68] or the three teams,
[1039.68 → 1042.26] to better understand what the requirements are,
[1042.66 → 1044.52] how people are bringing things
[1044.52 → 1046.34] from research and development environments
[1046.34 → 1047.44] into production.
[1048.08 → 1049.30] Because something that I've noticed
[1049.30 → 1051.24] in some companies or in some teams
[1051.24 → 1054.02] is that you have the R&D or the machine learners
[1054.02 → 1055.28] sitting in a corner,
[1055.60 → 1056.74] doing all of their things,
[1056.80 → 1057.66] developing their models,
[1057.94 → 1060.58] and then they have to throw things over a wall
[1060.58 → 1062.96] and hope that the software engineer
[1062.96 → 1065.16] will take that into production.
[1065.84 → 1066.54] But in most cases,
[1066.70 → 1067.50] then the software engineer
[1067.50 → 1070.88] doesn't have an idea on how the model works,
[1071.26 → 1072.34] the canonical database,
[1072.72 → 1074.18] or the canonical data sources,
[1074.48 → 1075.42] and the transformations
[1075.42 → 1077.50] that need to take place
[1077.50 → 1078.78] for that data to be usable.
[1079.24 → 1081.02] And that's when you sometimes see
[1081.02 → 1083.70] that folks spend weeks or months
[1083.70 → 1084.58] working on a model,
[1084.76 → 1087.22] but then they spend another couple of months
[1087.22 → 1089.12] or weeks sitting on that model,
[1089.24 → 1091.86] just waiting for it to be taken into production.
[1091.86 → 1094.00] Having from day one
[1094.00 → 1095.48] a collaborative approach
[1095.48 → 1097.32] where folks define
[1097.32 → 1099.38] what resources are you going to need,
[1099.64 → 1101.50] how this algorithm is going to reach out
[1101.50 → 1102.22] to our customers,
[1102.72 → 1104.22] and what sort of data
[1104.22 → 1106.48] is going to be accessing to,
[1106.76 → 1108.68] is crucial for both teams
[1108.68 → 1110.50] to be able to take this
[1110.50 → 1113.42] from R&D into production
[1113.42 → 1114.66] in a seamless way.
[1114.74 → 1115.60] That doesn't mean that
[1115.60 → 1116.82] you as a data scientist
[1116.82 → 1118.32] need to do everything
[1118.32 → 1119.50] or need to be perfect
[1119.50 → 1121.28] at CI and CD and testing
[1121.28 → 1123.22] and no Kubernetes
[1123.22 → 1124.50] and all of these complex things.
[1124.66 → 1126.92] But if you have the seams together,
[1127.18 → 1128.54] it's easier for both
[1128.54 → 1129.36] to understand
[1129.36 → 1131.06] the world of the other one.
[1131.64 → 1131.76] Yep.
[1132.10 → 1133.10] So, you know,
[1133.30 → 1133.96] one of the things
[1133.96 → 1135.54] I'm really getting from you here
[1135.54 → 1136.74] is that when you're actually
[1136.74 → 1137.92] working on
[1137.92 → 1138.92] getting a model
[1138.92 → 1139.90] into your overall
[1139.90 → 1140.92] production lifecycle
[1140.92 → 1142.10] and you're integrating
[1142.10 → 1143.74] with the existing software
[1143.74 → 1144.66] development
[1144.66 → 1146.34] and deployment life cycles
[1146.34 → 1148.10] that you are moving into,
[1148.20 → 1149.00] it's really part
[1149.00 → 1150.10] of a larger effort,
[1150.24 → 1151.20] which kind of fits
[1151.20 → 1152.50] into what a lot of organizations
[1152.50 → 1153.66] are already doing
[1153.66 → 1155.20] as they kind of add this in.
[1155.52 → 1156.10] One of the things
[1156.10 → 1157.04] I'd like to know
[1157.04 → 1158.24] is given that kind of
[1158.24 → 1159.10] larger team
[1159.10 → 1160.34] that we've been talking about,
[1160.56 → 1162.10] how should different roles
[1162.10 → 1162.84] within that team
[1162.84 → 1163.62] think about
[1163.62 → 1164.72] their responsibility
[1164.72 → 1165.50] for testing?
[1165.68 → 1166.32] In other words,
[1166.58 → 1167.44] if you are
[1167.44 → 1168.88] an infrastructure engineer,
[1169.02 → 1169.90] what should you be testing?
[1170.02 → 1170.86] If you're a data scientist,
[1170.96 → 1171.82] what should you be testing?
[1172.36 → 1173.20] What should the
[1173.24 → 1173.46] you know,
[1173.50 → 1174.36] machine learning engineer
[1174.36 → 1174.90] be testing?
[1174.90 → 1176.60] How should testing
[1176.60 → 1177.60] be divided out
[1177.60 → 1178.70] among those different roles?
[1179.34 → 1179.76] I think,
[1180.14 → 1181.04] as you mentioned it,
[1181.62 → 1182.78] finding these roles
[1182.78 → 1184.72] and assigning responsibilities
[1184.72 → 1185.66] is crucial.
[1186.12 → 1187.20] You as a data scientist,
[1187.46 → 1188.66] you would mainly
[1188.66 → 1189.28] be in charge
[1189.28 → 1189.88] of assessing
[1189.88 → 1190.84] your data
[1190.84 → 1191.86] and your features.
[1192.36 → 1192.66] So again,
[1192.72 → 1193.78] this goes back to
[1193.78 → 1194.64] when you have
[1194.64 → 1195.30] your data set,
[1195.42 → 1196.10] make sure that
[1196.10 → 1196.70] the distribution
[1196.70 → 1197.80] of each feature
[1197.80 → 1198.96] match your expectations.
[1199.42 → 1201.24] This is a very basic
[1201.24 → 1202.14] sanity check,
[1202.28 → 1202.96] but sometimes
[1202.96 → 1203.76] because we do it
[1203.76 → 1204.14] so,
[1204.46 → 1205.14] so often,
[1205.26 → 1206.18] we don't think
[1206.18 → 1207.36] about documenting it
[1207.36 → 1208.80] or going in depth
[1208.80 → 1209.40] into that.
[1209.88 → 1209.98] Also,
[1210.08 → 1210.56] making sure
[1210.56 → 1211.52] that the relationship
[1211.52 → 1212.76] between your features
[1212.76 → 1214.00] and your targets
[1214.00 → 1215.20] and the correlations
[1215.20 → 1215.80] make sense
[1215.80 → 1216.62] and that sometimes
[1216.62 → 1218.10] it needs to go beyond
[1218.10 → 1219.06] creating just
[1219.06 → 1220.60] a correlation heat map
[1220.60 → 1221.08] as well.
[1221.24 → 1222.00] As I mentioned before,
[1222.12 → 1222.94] testing the cost
[1222.94 → 1224.36] of your features
[1224.36 → 1226.08] also is something
[1226.08 → 1226.66] that is very,
[1226.76 → 1227.68] very important
[1227.68 → 1228.66] and aligns
[1228.66 → 1229.48] very well
[1229.48 → 1230.64] with this GDPR.
[1230.64 → 1231.82] also ensuring
[1231.82 → 1232.96] that your system
[1232.96 → 1234.10] maintains privacy
[1234.10 → 1236.08] across the entire pipeline.
[1236.30 → 1236.62] Sometimes,
[1236.86 → 1237.46] we are very,
[1237.54 → 1238.20] very concerned
[1238.20 → 1239.26] about privacy
[1239.26 → 1241.06] of our raw data
[1241.06 → 1241.90] because that's
[1241.90 → 1243.44] our most valuable asset,
[1243.80 → 1244.22] but you need
[1244.22 → 1244.72] to ensure
[1244.72 → 1246.28] that your system
[1246.28 → 1248.00] or every transformation
[1248.00 → 1249.36] or every data manipulation
[1249.36 → 1250.14] that you're doing
[1250.14 → 1252.08] complies with that privacy
[1252.08 → 1252.68] as well.
[1253.34 → 1253.72] Also,
[1253.80 → 1254.14] make sure
[1254.14 → 1254.98] that you are aware
[1254.98 → 1256.24] of how much time
[1256.24 → 1256.98] it's taking you
[1256.98 → 1257.58] to develop
[1257.58 → 1258.56] a new feature
[1258.56 → 1259.84] or a new production model
[1259.84 → 1260.70] because that's also
[1260.70 → 1261.34] going to help
[1261.34 → 1262.90] a lot with time turn
[1262.90 → 1264.58] which also will prevent
[1264.58 → 1265.60] you from going
[1265.60 → 1267.32] into half-big features
[1267.32 → 1268.78] or having
[1268.78 → 1269.18] very,
[1269.30 → 1270.46] very tight
[1270.46 → 1271.78] data jungles
[1271.78 → 1272.64] as well.
[1272.98 → 1273.46] If you are,
[1273.52 → 1273.90] for example,
[1274.14 → 1275.04] the machine learning
[1275.04 → 1275.92] engineer,
[1276.56 → 1277.20] you're going to be
[1277.20 → 1278.08] testing for
[1278.08 → 1279.18] model development
[1279.18 → 1279.76] practices
[1279.76 → 1280.92] and monitoring
[1280.92 → 1281.88] those models.
[1282.98 → 1283.30] So again,
[1283.46 → 1284.14] making sure
[1284.14 → 1285.04] that everything
[1285.04 → 1285.90] is checked
[1285.90 → 1286.68] into a repository,
[1287.06 → 1287.38] that there is
[1287.38 → 1288.22] version control,
[1288.22 → 1289.30] making sure
[1289.30 → 1289.84] that there is
[1289.84 → 1291.12] a peer review process,
[1291.52 → 1292.80] that it not only
[1292.80 → 1293.44] has to be
[1293.44 → 1294.08] the data,
[1294.34 → 1295.36] the senior data scientist,
[1295.58 → 1296.18] but everyone
[1296.18 → 1297.30] in the team
[1297.30 → 1298.04] has to be
[1298.04 → 1299.24] responsible for that,
[1299.72 → 1300.70] making sure again
[1300.70 → 1302.08] that you're checking
[1302.08 → 1303.62] your impact metrics,
[1303.92 → 1304.86] checking the impact
[1304.86 → 1305.46] of your
[1305.46 → 1307.04] unable hyperparameters
[1307.04 → 1308.10] and also
[1308.10 → 1309.10] check against
[1309.10 → 1310.28] simpler models.
[1310.46 → 1311.20] Sometimes because
[1311.20 → 1312.58] we are so into
[1312.58 → 1313.48] deep learning
[1313.48 → 1314.52] and deep learning
[1314.52 → 1315.44] is the most popular
[1315.44 → 1316.00] framework
[1316.00 → 1317.14] or the most
[1317.14 → 1318.04] popular approach
[1318.04 → 1318.62] at the moment
[1318.62 → 1319.80] and we want
[1319.80 → 1320.06] to use
[1320.06 → 1320.68] very sophisticated
[1320.68 → 1321.26] models,
[1321.72 → 1322.88] sometimes it's
[1322.88 → 1323.50] also good
[1323.50 → 1324.14] to go back
[1324.14 → 1324.70] to the basics
[1324.70 → 1325.70] and compare
[1325.70 → 1327.22] against a much
[1327.22 → 1327.88] more simple
[1327.88 → 1328.96] or a simpler
[1328.96 → 1330.06] model just
[1330.06 → 1330.84] to have a baseline
[1330.84 → 1331.76] and ensure
[1331.76 → 1332.38] that we're
[1332.38 → 1333.30] actually going
[1333.30 → 1334.40] down the right
[1334.40 → 1335.42] path and that
[1335.42 → 1336.28] it makes sense
[1336.28 → 1337.24] the additional
[1337.24 → 1338.56] cost that we're
[1338.56 → 1339.66] going into compute.
[1340.06 → 1340.34] And again,
[1340.46 → 1341.04] test for your
[1341.04 → 1342.00] implicit bias.
[1342.30 → 1342.88] And finally,
[1343.22 → 1344.46] the fault that is
[1344.46 → 1345.14] in charge of
[1345.14 → 1345.90] our infrastructure,
[1346.40 → 1347.14] sometimes it's
[1347.14 → 1348.52] a DevOps person,
[1348.86 → 1349.38] check for the
[1349.38 → 1350.20] reproducibility of
[1350.20 → 1350.56] training,
[1351.14 → 1351.88] making sure
[1351.88 → 1352.82] that the model
[1352.82 → 1354.10] specification is
[1354.10 → 1354.68] up-to-date
[1354.68 → 1355.80] and correct
[1355.80 → 1356.44] and we have
[1356.44 → 1358.36] properly versioned
[1358.36 → 1359.02] all of our
[1359.02 → 1359.46] data,
[1359.78 → 1360.40] all of our
[1360.40 → 1361.58] hyperparameters,
[1362.10 → 1362.52] all of our
[1362.52 → 1363.00] models,
[1363.18 → 1363.70] the training
[1363.70 → 1364.56] and everything.
[1364.98 → 1365.60] And integrate
[1365.60 → 1366.56] the full,
[1366.92 → 1367.50] test for the
[1367.50 → 1368.22] integration of
[1368.22 → 1368.88] the full
[1368.88 → 1369.90] machine learning
[1369.90 → 1370.38] pipeline,
[1370.56 → 1371.26] making sure
[1371.26 → 1371.78] that again,
[1372.10 → 1372.78] everything is
[1372.78 → 1373.40] reproducible,
[1373.40 → 1375.42] whether jury
[1375.42 → 1376.02] infrastructure,
[1376.50 → 1377.96] sometimes you
[1377.96 → 1378.36] will have
[1378.36 → 1379.36] infrastructure that
[1379.36 → 1380.64] is jury
[1380.64 → 1381.08] development,
[1381.34 → 1381.84] jury staging
[1381.84 → 1382.22] and jury
[1382.22 → 1382.60] production,
[1382.80 → 1383.40] making sure
[1383.40 → 1383.98] that across
[1383.98 → 1384.64] those three
[1384.64 → 1385.22] environments,
[1385.22 → 1385.80] you can get
[1385.80 → 1386.56] reproducible
[1386.56 → 1387.86] results.
[1388.34 → 1389.44] Sometimes you'll
[1389.44 → 1390.28] have changes in
[1390.28 → 1391.74] infrastructure that
[1391.74 → 1393.30] will imply changes
[1393.30 → 1393.68] in your
[1393.68 → 1394.96] predictions that
[1394.96 → 1395.38] gives you
[1395.38 → 1396.26] indication that
[1396.26 → 1397.10] your infrastructure
[1397.10 → 1398.06] is not
[1398.06 → 1398.64] reproducible.
[1398.64 → 1399.24] So you'll
[1399.24 → 1400.38] have to make
[1400.38 → 1400.84] sure that
[1400.84 → 1401.32] that's not
[1401.32 → 1402.00] the case as
[1402.00 → 1402.22] well.
[1402.62 → 1402.90] And again,
[1402.94 → 1403.32] as I said
[1403.32 → 1403.68] before,
[1404.08 → 1404.66] test that you
[1404.66 → 1405.78] can do
[1405.78 → 1406.92] releases and
[1406.92 → 1408.08] rollbacks in
[1408.08 → 1409.10] a reproducible,
[1409.40 → 1410.32] reliable and
[1410.32 → 1411.02] robust manner.
[1411.38 → 1412.00] Because if it's
[1412.00 → 1413.36] only one person,
[1413.66 → 1414.02] for example,
[1414.10 → 1415.08] in charge of
[1415.08 → 1416.02] deploying things
[1416.02 → 1416.80] into production,
[1417.22 → 1417.84] what's going to
[1417.84 → 1418.48] happen when that
[1418.48 → 1419.56] person is on
[1419.56 → 1420.78] holidays, for
[1420.78 → 1421.06] example,
[1421.16 → 1421.54] you're not going
[1421.54 → 1421.96] to be calling
[1421.96 → 1422.58] them at three
[1422.58 → 1423.04] o'clock in the
[1423.04 → 1424.12] morning for them
[1424.12 → 1424.94] to revert
[1424.94 → 1425.48] to a previous
[1425.48 → 1425.98] version.
[1425.98 → 1427.34] So make sure
[1427.34 → 1427.92] that there is
[1427.92 → 1428.98] a robust way
[1428.98 → 1429.56] to do that
[1429.56 → 1430.60] without having
[1430.60 → 1431.40] a bottleneck.
[1431.60 → 1432.42] There is also
[1432.42 → 1434.20] very, very
[1434.20 → 1434.88] important in
[1434.88 → 1435.48] ensuring that
[1435.48 → 1436.26] this rollback
[1436.26 → 1436.98] can be done
[1436.98 → 1438.52] safely, you
[1438.52 → 1438.94] know, in a
[1438.94 → 1439.66] controlled manner
[1439.66 → 1441.14] so that anyone
[1441.14 → 1442.24] can do that.
[1442.52 → 1442.90] And ideally,
[1442.90 → 1443.50] you would have
[1443.50 → 1444.32] an automated
[1444.32 → 1444.94] pipeline that
[1444.94 → 1445.34] would take
[1445.34 → 1445.98] care of that.
[1446.30 → 1446.92] So testing
[1446.92 → 1447.62] all of these
[1447.62 → 1448.28] little bits
[1448.28 → 1449.42] will be assigned
[1449.42 → 1449.98] within the
[1449.98 → 1450.64] specific role
[1450.64 → 1451.24] responsibilities,
[1451.24 → 1452.50] and it makes
[1452.50 → 1453.30] everyone's lives
[1453.30 → 1454.14] easier as well.
[1454.74 → 1455.54] Yeah, and I'm
[1455.54 → 1456.22] so glad you
[1456.22 → 1457.14] went into the
[1457.14 → 1458.08] details of those
[1458.08 → 1458.86] different areas.
[1458.98 → 1459.32] It's really
[1459.32 → 1459.70] helpful.
[1460.12 → 1460.44] And there's
[1460.44 → 1461.46] definitely a lot
[1461.46 → 1462.28] there to work
[1462.28 → 1462.50] on.
[1462.60 → 1463.28] There's a lot
[1463.28 → 1464.02] probably for
[1464.02 → 1464.54] every team,
[1464.66 → 1465.46] whether a small
[1465.46 → 1466.36] organization or a
[1466.36 → 1467.12] large organization
[1467.12 → 1467.74] that they can
[1467.74 → 1468.58] always be
[1468.58 → 1469.78] improving on.
[1469.94 → 1470.74] I know a lot
[1470.74 → 1471.26] of the things
[1471.26 → 1471.88] that you talked
[1471.88 → 1472.96] about, I know
[1472.96 → 1474.34] I have work
[1474.34 → 1475.26] to do on my
[1475.26 → 1476.32] end, but one
[1476.32 → 1476.92] of the things I
[1476.92 → 1477.70] liked about the
[1477.70 → 1478.56] talk that you
[1478.56 → 1479.30] gave on this
[1479.30 → 1480.22] was that you
[1480.22 → 1481.30] developed a sort
[1481.30 → 1482.34] of very practical,
[1482.70 → 1483.08] I guess I would
[1483.08 → 1483.88] call it a rubric
[1483.88 → 1484.60] for kind of
[1484.60 → 1486.08] scoring yourself
[1486.08 → 1486.54] in these
[1486.54 → 1487.42] different areas,
[1487.42 → 1488.46] which is what
[1488.46 → 1488.92] you meant by
[1488.92 → 1489.58] giving yourself
[1489.58 → 1490.66] an ML score,
[1491.08 → 1492.06] and then kind
[1492.06 → 1492.74] of helping you
[1492.74 → 1493.66] focus your
[1493.66 → 1495.08] effort on where
[1495.08 → 1495.62] you're lacking
[1495.62 → 1496.08] and where you
[1496.08 → 1496.80] can improve on.
[1496.88 → 1497.16] I was wondering
[1497.16 → 1497.90] if you could go
[1497.90 → 1498.66] into a little bit
[1498.66 → 1499.42] of the details
[1499.42 → 1500.66] of that scoring
[1500.66 → 1501.48] system and that
[1501.48 → 1502.42] rubric to help
[1502.42 → 1503.36] me develop my
[1503.36 → 1504.40] own ML score
[1504.40 → 1505.26] and make sure
[1505.26 → 1506.02] I'm putting in
[1506.02 → 1506.68] effort where I
[1506.68 → 1507.14] can make the
[1507.14 → 1507.84] most difference.
[1508.56 → 1508.74] Sure.
[1509.14 → 1509.68] Throughout this
[1509.68 → 1510.22] conversation,
[1510.64 → 1511.86] I've placed a
[1511.86 → 1512.62] specific emphasis
[1512.62 → 1514.24] in data science
[1514.24 → 1515.26] testing, machine
[1515.26 → 1516.14] learning, engineering,
[1516.54 → 1517.10] and infrastructure
[1517.10 → 1517.70] testing.
[1518.70 → 1519.78] Within these
[1519.78 → 1520.84] three areas, you
[1520.84 → 1521.68] have the different
[1521.68 → 1522.50] steps that I've
[1522.50 → 1523.14] already mentioned,
[1523.26 → 1523.82] the things that you
[1523.82 → 1524.56] should be testing
[1524.56 → 1525.40] at a minimum.
[1526.28 → 1527.08] For example, if
[1527.08 → 1527.88] you have no
[1527.88 → 1528.82] testing in place
[1528.82 → 1529.56] for any of the
[1529.56 → 1530.62] steps, that would
[1530.62 → 1531.34] give you a zero
[1531.34 → 1532.02] point because you
[1532.02 → 1532.76] have no testing.
[1533.18 → 1534.14] If you're testing,
[1534.30 → 1535.14] let's say, from the
[1535.14 → 1535.66] data science
[1535.66 → 1536.62] perspective and
[1536.62 → 1537.36] you're manually
[1537.36 → 1538.54] testing the
[1538.54 → 1539.52] distributions or
[1539.52 → 1540.06] checking the
[1540.06 → 1540.80] distributions of
[1540.80 → 1541.92] your data and
[1541.92 → 1542.46] then ensuring
[1542.46 → 1543.14] that the training
[1543.14 → 1543.80] of your model
[1543.80 → 1544.74] is reproducible,
[1545.14 → 1545.82] but all of this
[1545.82 → 1546.80] is done manually,
[1547.02 → 1547.58] you can assign
[1547.58 → 1548.56] yourself probably
[1548.56 → 1549.24] one point.
[1549.58 → 1550.52] If you or your
[1550.52 → 1551.20] company has
[1551.20 → 1552.50] reached a more
[1552.50 → 1553.82] mature level where
[1553.82 → 1554.54] all of these
[1554.54 → 1555.52] tests are done
[1555.52 → 1557.26] in an automated
[1557.26 → 1558.20] fashion, probably
[1558.20 → 1559.44] through your
[1559.44 → 1560.60] favourite CI
[1560.60 → 1561.86] provider, it can
[1561.86 → 1562.68] be GitHub
[1562.68 → 1563.96] Actions, Travis,
[1564.60 → 1565.76] Azure Pipelines,
[1566.14 → 1567.24] or GitLab
[1567.24 → 1569.02] CI, then that
[1569.02 → 1569.70] would give you
[1569.70 → 1570.42] two points.
[1570.80 → 1571.42] And as you
[1571.42 → 1572.20] go creating
[1572.20 → 1573.06] your tests, you
[1573.06 → 1574.14] can add those
[1574.14 → 1575.38] points and then
[1575.38 → 1576.14] compare against
[1576.14 → 1577.22] the three stages,
[1577.48 → 1578.32] whether it's
[1578.32 → 1579.02] data science,
[1579.16 → 1580.10] infrastructure, and
[1580.10 → 1580.58] machine learning
[1580.58 → 1581.12] engineering.
[1581.84 → 1582.48] And more than
[1582.48 → 1583.28] likely is that
[1583.28 → 1583.70] you're going to
[1583.70 → 1585.28] be very good in
[1585.28 → 1585.90] one of these
[1585.90 → 1587.04] areas and not
[1587.04 → 1587.76] so good.
[1587.84 → 1588.34] You'll have a
[1588.34 → 1589.68] lower score in
[1589.68 → 1590.88] one or two
[1590.88 → 1591.34] areas.
[1591.70 → 1592.38] And the area
[1592.38 → 1592.88] where you have
[1592.88 → 1593.84] the lowest score
[1593.84 → 1595.26] is the one that
[1595.26 → 1595.90] you should be
[1595.90 → 1597.08] paying more
[1597.08 → 1597.92] immediate attention.
[1598.18 → 1599.18] Start trying to
[1599.18 → 1599.92] level up that
[1599.92 → 1600.32] score.
[1600.32 → 1601.28] Yeah, that's
[1601.28 → 1601.82] super helpful.
[1602.08 → 1602.48] I was just
[1602.48 → 1602.96] trying to think
[1602.96 → 1603.50] through while you
[1603.50 → 1604.32] were talking what
[1604.32 → 1605.28] my score would
[1605.28 → 1605.50] be.
[1605.74 → 1606.14] I don't know,
[1606.28 → 1607.52] Chris, if you
[1607.52 → 1608.46] were doing the
[1608.46 → 1608.74] same.
[1609.20 → 1609.90] Yeah, for me,
[1610.14 → 1611.18] so I guess there's
[1611.18 → 1611.90] the manual and
[1611.90 → 1612.32] the automated
[1612.32 → 1613.12] tests, and then
[1613.12 → 1613.62] there's the three
[1613.62 → 1615.06] sections, data
[1615.06 → 1616.78] science, machine
[1616.78 → 1617.42] learning development,
[1617.58 → 1618.22] and infrastructure.
[1618.84 → 1619.86] I think probably,
[1620.46 → 1621.12] at least in my
[1621.12 → 1622.40] organization, on the
[1622.40 → 1622.92] stuff I work
[1622.92 → 1623.94] directly in, I've
[1623.94 → 1625.44] got a fairly good
[1625.44 → 1626.42] amount of manual
[1626.42 → 1627.50] tests going, but
[1627.50 → 1628.22] definitely not
[1628.22 → 1628.80] everything's
[1628.80 → 1629.30] automated.
[1630.10 → 1631.72] And probably we
[1631.72 → 1632.36] have been more
[1632.36 → 1633.02] focused on the
[1633.02 → 1633.78] data science and
[1633.78 → 1634.32] machine learning
[1634.32 → 1635.12] development side
[1635.12 → 1635.72] than on the
[1635.72 → 1636.58] infrastructure side
[1636.58 → 1638.00] just because, you
[1638.00 → 1638.42] know, our
[1638.42 → 1640.20] organization being a
[1640.20 → 1641.64] non-profit isn't
[1641.64 → 1642.80] already operating a
[1642.80 → 1643.72] ton of infrastructure
[1643.72 → 1645.52] and have some of
[1645.52 → 1646.06] those things in
[1646.06 → 1646.68] place, although they
[1646.68 → 1647.66] do for a variety
[1647.66 → 1648.20] of projects.
[1648.44 → 1649.42] So I'm guessing I've
[1649.42 → 1651.00] got like a one
[1651.00 → 1651.98] going on and
[1651.98 → 1653.76] maybe a two in a
[1653.76 → 1654.28] couple of the
[1654.28 → 1655.46] first sections, and
[1655.46 → 1656.68] then maybe where
[1656.68 → 1657.62] things are needed
[1657.62 → 1658.50] is more on the
[1658.50 → 1659.88] infrastructure side.
[1659.96 → 1660.36] What about you,
[1660.42 → 1660.58] Chris?
[1661.22 → 1662.28] I think it's more
[1662.28 → 1662.82] or less the same.
[1662.94 → 1663.96] As you were saying
[1663.96 → 1664.96] that, I think the
[1664.96 → 1666.32] things that for me
[1666.32 → 1667.48] personally, and I'm
[1667.48 → 1668.08] part of a larger
[1668.08 → 1668.88] team, but the
[1668.88 → 1670.24] things personally, the
[1670.24 → 1671.30] closer we are to
[1671.30 → 1672.62] kind of what I grew
[1672.62 → 1673.12] up in the
[1673.12 → 1673.70] software development
[1673.70 → 1674.86] side, I think we're
[1674.86 → 1675.66] actually, and this is
[1675.66 → 1676.28] where I'm a little bit
[1676.28 → 1676.76] different from you,
[1677.04 → 1678.38] probably more automated
[1678.38 → 1679.50] and actually attending
[1679.50 → 1680.76] to tests on the
[1680.76 → 1681.94] infrastructure side, and
[1681.94 → 1683.20] as you move over
[1683.20 → 1683.78] toward the data
[1683.78 → 1684.58] science, it's
[1684.58 → 1685.98] probably, you know,
[1685.98 → 1686.96] pretty decent on
[1686.96 → 1687.90] manual tests, not
[1687.90 → 1688.72] probably not a lot of
[1688.72 → 1690.04] automated tests, and
[1690.04 → 1691.50] so I think it varies a
[1691.50 → 1692.66] lot for us, whether it
[1692.66 → 1694.20] is a team effort, and I
[1694.20 → 1694.90] think we probably get a
[1694.90 → 1695.70] little bit higher score
[1695.70 → 1696.64] because different people
[1696.64 → 1697.92] are attending to
[1697.92 → 1698.80] different parts of it
[1698.80 → 1700.32] versus when me or
[1700.32 → 1701.44] somebody else is doing
[1701.44 → 1702.78] something alone, and I'd
[1702.78 → 1703.72] say our scores probably
[1703.72 → 1705.00] fell off, so I think
[1705.00 → 1706.14] it's definitely probably a
[1706.14 → 1707.06] testament to throwing
[1707.06 → 1707.78] people from different
[1707.78 → 1709.12] perspectives on the
[1709.12 → 1710.64] team probably yields us a
[1710.64 → 1711.60] higher score since we're
[1711.60 → 1712.80] combining that, but boy,
[1712.86 → 1713.50] I'll tell you, after
[1713.50 → 1714.44] talking through this and
[1714.44 → 1715.68] then hearing Tanya talk
[1715.68 → 1716.92] about her scoring, I'm
[1716.92 → 1717.90] starting to realize all
[1717.90 → 1719.36] the places that I need a
[1719.36 → 1719.96] little bit of work.
[1720.26 → 1720.88] I think that's cool,
[1720.92 → 1721.68] though, because it's
[1721.68 → 1723.42] like, you know, if you
[1723.42 → 1724.38] were to just present all
[1724.38 → 1725.34] this, like what Tanya
[1725.34 → 1726.46] presented in general,
[1726.56 → 1727.48] like all the pieces of
[1727.48 → 1728.50] the machine learning
[1728.50 → 1729.38] system, it could be
[1729.38 → 1730.78] overwhelming and a bit
[1730.78 → 1731.70] crippling, but if you're
[1731.70 → 1733.10] able to kind of zero in
[1733.10 → 1734.66] on where you need to put
[1734.66 → 1735.74] the most effort, I think
[1735.74 → 1736.80] it's really helpful in
[1736.80 → 1738.24] terms of, you know,
[1738.30 → 1740.16] starting somewhere and at
[1740.16 → 1742.00] the least getting some more
[1742.00 → 1743.50] testing off the ground.
[1743.50 → 1744.86] I'm curious, Tanya, as
[1744.86 → 1745.58] you've kind of gone
[1745.58 → 1747.00] around and presented this
[1747.00 → 1748.82] to various groups, what's
[1748.82 → 1749.98] been the feedback that
[1749.98 → 1751.42] you've got in terms of
[1751.42 → 1752.92] where people, is there a
[1752.92 → 1754.20] consistent place that you
[1754.20 → 1756.12] think data science teams
[1756.12 → 1757.74] or like machine learning
[1757.74 → 1759.66] teams are maybe not
[1759.66 → 1761.04] putting a lot of effort
[1761.04 → 1761.84] where they need to?
[1762.40 → 1763.84] Has there been any sort of
[1763.84 → 1765.22] trends in that sense?
[1765.62 → 1767.40] I think something that has
[1767.40 → 1768.72] come up a lot is
[1768.72 → 1769.34] infrastructure.
[1769.34 → 1770.70] infrastructure, like in the
[1770.70 → 1772.52] sense of they have a
[1772.52 → 1773.84] DevOps person that normally
[1773.84 → 1774.76] takes care of the
[1774.76 → 1776.62] infrastructure, but
[1776.62 → 1778.36] everything is very flat
[1778.36 → 1779.82] in the sense of they
[1779.82 → 1780.84] always have the same
[1780.84 → 1782.18] tests, they always run
[1782.18 → 1783.70] the same processes
[1783.70 → 1786.32] without adapting to the
[1786.32 → 1787.36] specific cases or
[1787.36 → 1789.26] specific situations for
[1789.26 → 1789.94] machine learning.
[1790.06 → 1790.74] Because sometimes we
[1790.74 → 1791.80] would have a bit of
[1791.80 → 1793.36] different behaviours or we
[1793.36 → 1794.92] would need something a
[1794.92 → 1796.34] bit different if you are
[1796.34 → 1797.28] serving, for example, a
[1797.28 → 1798.20] model that is going to be
[1798.20 → 1799.24] accessed by a lot of
[1799.24 → 1802.42] people over a web app,
[1802.50 → 1803.56] for example, or a more
[1803.56 → 1805.92] simple e-commerce app that
[1805.92 → 1806.64] folks are going to be
[1806.64 → 1808.50] accessing to buy products
[1808.50 → 1809.48] or the such.
[1809.94 → 1810.74] So I think the
[1810.74 → 1811.54] understanding and the
[1811.54 → 1812.32] testing of machine
[1812.32 → 1813.76] learning infrastructure is
[1813.76 → 1815.96] very often overseen by a
[1815.96 → 1816.54] lot of teams.
[1821.20 → 1822.80] Have you heard of our
[1822.80 → 1823.56] the newest show called
[1823.56 → 1824.20] Brain Science?
[1824.66 → 1825.74] Yes, Brain Science.
[1825.86 → 1826.98] It's a different kind of
[1826.98 → 1828.56] show I know, and it's
[1828.56 → 1829.42] probably one of the ones
[1829.42 → 1830.98] that reaches the furthest
[1830.98 → 1832.16] out from our typical
[1832.16 → 1833.64] listener audience, but
[1833.64 → 1836.16] this podcast is what we
[1836.16 → 1837.50] call For the Curious.
[1838.04 → 1838.78] And what's cool about
[1838.78 → 1839.36] this show is we're
[1839.36 → 1840.20] exploring the inner
[1840.20 → 1841.84] workings of the human
[1841.84 → 1842.72] brain to understand
[1842.72 → 1843.62] things like behaviour
[1843.62 → 1844.88] change, habit
[1844.88 → 1846.42] formation, mental health,
[1846.50 → 1848.00] and pretty much what it
[1848.00 → 1849.04] means to be human.
[1849.38 → 1850.62] If you've ever thought
[1850.62 → 1851.56] about why you do what
[1851.56 → 1853.46] you do or why others do
[1853.46 → 1855.20] what they do, then this
[1855.20 → 1856.86] show is for you.
[1857.18 → 1858.20] Head to changelog.com
[1858.20 → 1859.86] slash brain science to
[1859.86 → 1861.16] listen, subscribe, and
[1861.16 → 1861.88] learn more about this
[1861.88 → 1862.56] awesome show.
[1862.90 → 1863.86] Here's a preview of a
[1863.86 → 1865.16] recent episode called
[1865.16 → 1866.10] One Small Act of
[1866.10 → 1867.30] Kindness, talking about
[1867.30 → 1868.58] empathy and mirror
[1868.58 → 1869.06] neurons.
[1869.74 → 1870.64] So it sounds like
[1870.64 → 1871.78] pliability and flexibility
[1871.78 → 1872.88] is a pretty crucial role
[1872.88 → 1873.82] too in relationships
[1873.82 → 1875.34] because if you're not
[1875.34 → 1876.62] flexible, bendable,
[1876.82 → 1877.54] pliable, whatever,
[1877.72 → 1878.32] however you want to
[1878.32 → 1880.32] phrase that, if you're
[1880.32 → 1882.12] rigid, that's only
[1882.12 → 1885.00] going to be difficult for
[1885.00 → 1886.36] you to flex.
[1886.60 → 1886.98] Right.
[1887.12 → 1889.18] To enable change or to
[1889.18 → 1890.40] what you've said before,
[1890.48 → 1891.28] recalculate.
[1891.62 → 1891.92] Yeah.
[1892.04 → 1893.00] You know, accept new
[1893.00 → 1895.36] data, you know, analyze
[1895.36 → 1896.42] that data, make a new
[1896.42 → 1897.24] plan, and iterate
[1897.24 → 1898.96] towards a new action.
[1899.68 → 1899.92] Yeah.
[1900.04 → 1901.10] And so on of the other
[1901.10 → 1902.42] things involved with
[1902.42 → 1904.48] this flexibility would be
[1904.48 → 1905.86] what researchers have
[1905.86 → 1906.94] discovered as mirror
[1906.94 → 1907.44] neurons.
[1908.10 → 1908.26] Right.
[1908.26 → 1909.70] And so mirror neurons
[1909.70 → 1911.40] are these neurons within
[1911.40 → 1913.14] the brain that help us
[1913.14 → 1915.22] sort of get access to
[1915.22 → 1917.40] another person's emotional
[1917.40 → 1918.64] experience.
[1919.36 → 1920.94] And so there's an action
[1920.94 → 1922.32] component in it that it
[1922.32 → 1923.12] was first discovered
[1923.12 → 1924.98] actually with monkeys and
[1924.98 → 1926.24] this sort of mimicry that
[1926.24 → 1927.82] occurred by watching
[1927.82 → 1929.26] somebody else do an
[1929.26 → 1929.70] action.
[1930.14 → 1932.56] Well, in the same way, I
[1932.56 → 1933.52] can sort of watch
[1933.52 → 1935.04] somebody else walk
[1935.04 → 1936.18] through something in
[1936.18 → 1938.08] terms of an emotional
[1938.08 → 1938.68] experience.
[1938.68 → 1939.80] and if I'm holding
[1939.80 → 1941.28] space for them in my
[1941.28 → 1942.62] mind, like my body
[1942.62 → 1944.00] physiologically, these
[1944.00 → 1945.28] mirror neurons come
[1945.28 → 1946.72] come to play.
[1947.46 → 1948.50] Is that why people cry
[1948.50 → 1949.70] when they watch movies or
[1949.70 → 1950.74] certain movies because
[1950.74 → 1952.64] their mirror neurons are
[1952.64 → 1953.60] firing because they're
[1953.60 → 1954.52] watching somebody go
[1954.52 → 1956.74] through a situation and
[1956.74 → 1958.12] they're empathizing with
[1958.12 → 1959.88] them and can't help but
[1959.88 → 1961.58] encapsulate themselves
[1961.58 → 1963.46] into their scenario and
[1963.46 → 1964.94] feel what they're feeling.
[1965.02 → 1965.96] Is that why?
[1966.28 → 1966.70] Yes.
[1966.70 → 1967.34] Okay.
[1967.64 → 1968.66] So is that why anybody
[1968.66 → 1969.60] cries at anything when
[1969.60 → 1970.46] it's like, say, movie
[1970.46 → 1972.12] related because that's
[1972.12 → 1972.56] what's happening?
[1972.72 → 1972.88] Yeah.
[1972.94 → 1973.58] Think about it sort of
[1973.58 → 1974.34] like this emotional
[1974.34 → 1975.86] contagion, right?
[1977.18 → 1978.20] That's interesting to put
[1978.20 → 1978.60] it that way.
[1979.14 → 1980.26] We've said mirror neurons
[1980.26 → 1981.14] several times, but this
[1981.14 → 1982.28] emotional contagion, I
[1982.28 → 1983.84] believe, is actually a
[1983.84 → 1984.82] better subtitle for
[1984.82 → 1985.36] mirror neurons.
[1985.74 → 1986.08] Mm-hmm.
[1986.68 → 1987.00] Yeah.
[1987.30 → 1988.76] And so some of this
[1988.76 → 1990.02] emotional contagion or
[1990.02 → 1991.06] mirror neurons, like the
[1991.06 → 1992.06] research has been rooted
[1992.06 → 1993.84] in aspects of pain
[1993.84 → 1995.86] because if I can
[1995.86 → 1997.14] recognize sort of the
[1997.14 → 1998.64] suffering from another.
[1998.74 → 1999.00] All right.
[1999.04 → 1999.86] To keep listening, head
[1999.86 → 2001.46] to changelaw.com slash
[2001.46 → 2002.92] brain science slash
[2002.92 → 2003.66] nine.
[2003.96 → 2005.14] That will take you to
[2005.14 → 2006.18] the episode titled
[2006.18 → 2007.96] One Small Act of
[2007.96 → 2008.54] Kindness.
[2009.18 → 2010.36] Mariel and I dig into
[2010.36 → 2011.08] this thing called
[2011.08 → 2012.08] empathy as a
[2012.08 → 2012.56] construct.
[2012.70 → 2014.40] We ask questions like
[2014.40 → 2015.24] what key brain
[2015.24 → 2016.28] structures are involved?
[2016.74 → 2017.36] How can we better
[2017.36 → 2018.58] understand empathy to
[2018.58 → 2019.46] be able to better
[2019.46 → 2021.10] navigate ourselves and
[2021.10 → 2021.92] our relationships with
[2021.92 → 2023.26] others, both at home
[2023.26 → 2024.30] and in the workplace?
[2024.30 → 2026.38] It's a deep subject, a
[2026.38 → 2027.40] very fun subject.
[2027.68 → 2029.74] Again, changelaw.com slash
[2029.74 → 2031.42] brain science slash nine
[2031.42 → 2032.68] or search for brain
[2032.68 → 2033.56] science on your favourite
[2033.56 → 2034.46] podcast app and
[2034.46 → 2034.82] subscribe.
[2035.36 → 2036.02] We'd love to have you as
[2036.02 → 2036.34] a listener.
[2036.34 → 2052.52] So on a slight change of
[2052.52 → 2054.06] topic here, Tanya, we
[2054.06 → 2055.46] certainly, I think, would
[2055.46 → 2056.64] be remiss if we ended our
[2056.64 → 2058.84] discussion about testing and
[2058.84 → 2060.74] machine learning systems and
[2060.74 → 2062.28] integrity without mentioning
[2062.28 → 2062.94] notebooks.
[2062.94 → 2064.92] I understand you gave a
[2064.92 → 2066.30] talk that was called
[2066.30 → 2066.94] Jupiter Notebooks,
[2067.06 → 2068.48] Friends or Foes recently.
[2068.84 → 2070.78] And I was wondering what
[2070.78 → 2071.96] was your conclusion in that
[2071.96 → 2073.48] talk, especially, you
[2073.48 → 2074.56] know, given the emphasis in
[2074.56 → 2076.24] this episode on integrity
[2076.24 → 2077.36] and reproducibility.
[2077.52 → 2078.18] Could you share some of your
[2078.18 → 2078.60] thoughts there?
[2079.10 → 2080.88] Yeah, I've given that talk a
[2080.88 → 2082.44] couple of times, and it's
[2082.44 → 2083.86] been very well received
[2083.86 → 2085.06] because Jupiter Notebooks
[2085.06 → 2087.22] are a tool very, very
[2087.22 → 2088.26] commonly used by data
[2088.26 → 2088.76] scientists.
[2089.04 → 2090.58] And I'm going to say I love
[2090.58 → 2093.30] Jupiter Notebooks, but I
[2093.30 → 2094.68] always try to use them
[2094.68 → 2095.64] within reasons.
[2095.64 → 2096.52] And even with the teams
[2096.52 → 2098.42] that I work, I try to
[2098.42 → 2100.12] have these standards on
[2100.12 → 2102.14] how I work with them, have
[2102.14 → 2103.78] processes again in place.
[2104.10 → 2105.06] There are a lot of very,
[2105.16 → 2106.58] very good things of the
[2106.58 → 2107.52] Notebooks, but there are
[2107.52 → 2109.78] also a lot of hidden
[2109.78 → 2111.52] things and caveats.
[2111.82 → 2113.26] So the more aware you are
[2113.26 → 2114.72] of this, the better use
[2114.72 → 2116.18] you can make of this tool.
[2116.48 → 2117.58] And then again, it comes to
[2117.58 → 2119.52] having these processes and
[2119.52 → 2120.96] these workflows in place,
[2121.00 → 2121.52] for example.
[2122.06 → 2123.70] Something that is relatively
[2123.70 → 2126.24] easy to do is if you have
[2126.24 → 2128.36] someone to help you or you
[2128.36 → 2130.02] spend some time is, for
[2130.02 → 2130.76] example, when you're working
[2130.76 → 2131.86] with Notebooks and then you
[2131.86 → 2133.44] check them into version
[2133.44 → 2135.36] control, having, for example,
[2135.44 → 2137.02] a GitHub that will make sure
[2137.02 → 2138.76] that all the outputs are
[2138.76 → 2140.72] cleared out, that you are
[2140.72 → 2141.78] conforming to certain
[2141.78 → 2144.02] standards, that your paths are
[2144.02 → 2146.20] not referencing to local paths
[2146.20 → 2147.58] before those are going to be
[2147.58 → 2149.44] checked into version control.
[2149.70 → 2151.02] And then again, having
[2151.02 → 2152.68] testing of your Notebooks,
[2152.90 → 2154.00] making sure that your
[2154.00 → 2155.80] environment is reproducible,
[2156.06 → 2157.78] that makes a very, very
[2157.78 → 2160.06] dramatic change in how folks
[2160.06 → 2160.76] are using it.
[2160.80 → 2163.00] Because I know some software
[2163.00 → 2165.02] engineering folks, they
[2165.02 → 2166.10] absolutely hate it.
[2166.34 → 2167.90] They absolutely hate Notebooks
[2167.90 → 2171.14] because it also allows for a
[2171.14 → 2173.26] lot of bad practices in the
[2173.26 → 2174.58] more traditional sense of
[2174.58 → 2175.50] software engineering.
[2175.50 → 2176.88] But I think, again, if you
[2176.88 → 2178.84] add theory to this, you know,
[2178.96 → 2181.70] style guides, having, enforcing
[2181.70 → 2183.66] workflows that will allow for
[2183.66 → 2185.82] this quality assurance, this
[2185.82 → 2186.74] goes a long way.
[2186.88 → 2189.16] And also being smart about what
[2189.16 → 2190.54] you're using the Notebooks for
[2190.54 → 2193.52] and when it's good or more
[2193.52 → 2195.92] advisable to move from Notebooks
[2195.92 → 2197.56] into a more traditional
[2197.56 → 2200.30] development practice as having
[2200.30 → 2203.60] your scripts and your tests and
[2203.60 → 2204.96] importing your modules.
[2204.96 → 2207.06] And being able to discern
[2207.06 → 2208.98] between these two use cases or
[2208.98 → 2210.22] these two different approaches
[2210.22 → 2212.22] rather is very, very valuable.
[2212.94 → 2213.86] So I'm curious.
[2214.22 → 2215.68] So I guess first, I have a
[2215.68 → 2216.64] couple of follow-up questions
[2216.64 → 2218.20] because there's so much here.
[2218.52 → 2219.22] And of course, Jupyter
[2219.22 → 2220.52] Notebooks are everywhere.
[2220.52 → 2222.18] So it really does influence a
[2222.18 → 2223.30] lot of people's workflow.
[2223.90 → 2225.34] I guess the first thing, so
[2225.34 → 2226.58] you mentioned a couple of the
[2226.58 → 2227.84] checks that you might do when
[2227.84 → 2228.86] you're checking your Notebook
[2228.86 → 2230.20] into version control.
[2230.20 → 2231.96] But you also mentioned maybe
[2231.96 → 2234.62] some caveats where Notebooks
[2234.62 → 2236.08] kind of can break down.
[2236.18 → 2237.46] I was wondering if you would go
[2237.46 → 2238.50] into that a little bit more.
[2238.62 → 2240.56] Maybe I know, for example, one
[2240.56 → 2242.66] area that I've seen is where,
[2243.16 → 2244.66] and this is something that Joel
[2244.66 → 2245.92] Ruse mentions.
[2246.30 → 2247.94] We had him on another episode and
[2247.94 → 2250.02] he gave a talk as well, more
[2250.02 → 2252.14] controversially titled, I guess,
[2252.24 → 2253.36] I don't like Notebooks.
[2253.36 → 2254.60] But he was saying, you know,
[2254.64 → 2255.88] there's a lot of hidden state
[2255.88 → 2257.74] in Notebooks where, you know,
[2257.90 → 2259.86] you might run things out of
[2259.86 → 2261.92] order, and it's hard for another
[2261.92 → 2264.00] person to jump in and actually
[2264.00 → 2266.00] recreate that state that you
[2266.00 → 2268.22] might have actually been a
[2268.22 → 2269.56] little bit, you might have had
[2269.56 → 2271.10] some misunderstanding of how you
[2271.10 → 2272.50] got to a certain place in the
[2272.50 → 2272.84] Notebook.
[2273.12 → 2273.88] I was wondering if you had
[2273.88 → 2275.10] similar experience.
[2275.60 → 2276.08] Yeah, right.
[2276.18 → 2278.28] I totally agree with him in that
[2278.28 → 2278.70] sense.
[2278.84 → 2280.32] There is a lot of hidden state
[2280.32 → 2282.38] because it gives you, Jupiter
[2282.38 → 2283.92] Notebooks gives you so much
[2283.92 → 2285.60] flexibility when it comes to
[2285.60 → 2287.44] executing itself and getting
[2287.44 → 2288.74] to output straight away and
[2288.74 → 2290.42] then going back and forth.
[2290.80 → 2292.46] But I think especially for
[2292.46 → 2294.16] people that are getting
[2294.16 → 2296.80] started or have never had
[2296.80 → 2298.80] proper software engineering
[2298.80 → 2301.10] practices, this is not
[2301.10 → 2301.56] obvious.
[2302.54 → 2304.66] So sometimes they will work in
[2304.66 → 2306.02] Notebooks, jump from one
[2306.02 → 2307.56] cell to another, get to a
[2307.56 → 2309.12] result, whatever that result
[2309.12 → 2311.42] is, that seems satisfactory for
[2311.42 → 2311.68] them.
[2311.68 → 2312.60] And they're like, okay, I'm
[2312.60 → 2312.84] done.
[2313.46 → 2315.14] And just check or share their
[2315.14 → 2317.00] Notebooks in the state that it
[2317.00 → 2317.32] is.
[2318.04 → 2320.10] But then if you go again a step
[2320.10 → 2321.84] further, and you have these
[2321.84 → 2323.86] practices of, okay, I finished
[2323.86 → 2325.64] this Notebook, so I'm going to
[2325.64 → 2327.46] clear everything, restart my
[2327.46 → 2330.00] kernel and run all the
[2330.00 → 2331.62] cells to make sure, again, that
[2331.62 → 2334.36] my results are reproducible, then
[2334.36 → 2336.54] you're adding these extra quality
[2336.54 → 2336.98] checks.
[2336.98 → 2338.42] There are tools, for example,
[2338.62 → 2342.44] like Naval that I love, and I've
[2342.44 → 2343.90] worked with a lot that allows you
[2343.90 → 2345.26] to do this regression test.
[2345.40 → 2346.48] And they're very, very useful
[2346.48 → 2348.50] because you've already had the
[2348.50 → 2350.28] state of your Notebook saved.
[2350.50 → 2352.46] So it runs again in background
[2352.46 → 2355.28] to your cells and checks whether
[2355.28 → 2357.56] what you're getting is the same
[2357.56 → 2358.84] what you get, what you got
[2358.84 → 2359.28] before.
[2359.28 → 2361.58] And this is very, very useful for
[2361.58 → 2363.20] regression tests, for validation
[2363.20 → 2365.76] of somebody else's work.
[2365.98 → 2367.48] But then again, something that is
[2367.48 → 2369.52] very, very obscure is the
[2369.52 → 2370.90] dependencies that you're using.
[2371.16 → 2373.78] Unless you are actively sharing
[2373.78 → 2376.32] your environment through pinned
[2376.32 → 2377.82] versions in a current environment
[2377.82 → 2380.82] or you're using PIPE for poetry or
[2380.82 → 2383.14] Docker or something of the such, it's
[2383.14 → 2383.90] very, very obscure.
[2384.40 → 2386.64] And a friend of mine has owned a lot
[2386.64 → 2389.04] of study around how it's like
[2389.04 → 2391.68] changes in packages version can
[2391.68 → 2394.46] actually change the result that
[2394.46 → 2396.34] you're getting in a workflow or
[2396.34 → 2397.28] in a study.
[2397.82 → 2400.00] And this is, I think, all the
[2400.00 → 2401.96] hidden state and all the weird
[2401.96 → 2402.42] practices.
[2402.68 → 2404.80] And then, especially when folks
[2404.80 → 2407.66] only learn to use, for example,
[2407.82 → 2409.44] Python through Jupyter Notebook,
[2409.78 → 2410.88] through Jupyter Notebooks, it
[2410.88 → 2412.50] becomes very problematic because
[2412.50 → 2414.18] then they're like, okay, so I
[2414.18 → 2415.70] normally pour it to a library like,
[2415.92 → 2416.64] let's say, Pandas.
[2416.88 → 2418.64] If I develop something in a Jupyter
[2418.64 → 2420.72] Notebook, how do I import this
[2420.72 → 2421.82] notebook into my notebook?
[2422.10 → 2426.64] So people started misusing the
[2426.64 → 2428.04] notebooks, if that makes sense.
[2428.42 → 2428.78] It does.
[2428.94 → 2429.34] It does.
[2429.42 → 2431.72] I think when in my own thought
[2431.72 → 2434.42] process, I think I have this bias
[2434.42 → 2435.48] where I'm coming from the software
[2435.48 → 2436.94] development background, as I had
[2436.94 → 2437.50] noted before.
[2438.08 → 2440.36] And so I do think Jupyter
[2440.36 → 2442.08] Remote are wonderful for kind of
[2442.08 → 2443.66] experimenting and trying and doing
[2443.66 → 2445.44] you're experimenting with feature
[2445.44 → 2446.60] selection, stuff like that.
[2446.60 → 2448.50] But I also know, speaking for
[2448.50 → 2450.60] myself, at the first point where
[2450.60 → 2453.20] my model starts to stabilize a bit
[2453.20 → 2455.38] and I'm doing less experimentation
[2455.38 → 2457.70] and variance from a minute-to-minute
[2457.70 → 2459.76] kind of thing, that's where I'm
[2459.76 → 2461.06] always looking for that first
[2461.06 → 2463.06] moment where I say, okay, it's time
[2463.06 → 2464.50] to get it out of the notebook at this
[2464.50 → 2466.38] point and really start wrapping it
[2466.38 → 2467.82] with software development best
[2467.82 → 2470.26] practices, as we've discussed.
[2470.26 → 2472.76] I'm kind of curious, what is that
[2472.76 → 2475.50] point in your own workflow, speaking
[2475.50 → 2477.76] for yourself, and also what would
[2477.76 → 2479.78] you definitely, as part of that, not
[2479.78 → 2481.48] want to see happening in a Jupyter
[2481.48 → 2481.82] notebook?
[2482.10 → 2483.58] You know, at what point would you be
[2483.58 → 2485.44] saying, I've stayed in a Jupyter
[2485.44 → 2487.56] notebook too long in your personal
[2487.56 → 2487.90] workflow?
[2488.48 → 2490.66] Yeah, I think I very much agree with
[2490.66 → 2491.70] what Judge said.
[2491.98 → 2493.78] Jupyter notebooks are excellent for
[2493.78 → 2496.32] prototyping, doing very fast things,
[2496.32 → 2498.96] and get the initial part of the R&D
[2498.96 → 2501.06] process off the ground.
[2501.20 → 2501.78] They're amazing.
[2502.38 → 2503.90] Another use case that I found that
[2503.90 → 2505.80] is perfect is parameterizing
[2505.80 → 2507.66] Jupyter notebooks using tools like
[2507.66 → 2508.26] paper mail.
[2508.68 → 2510.86] But then once my model starts
[2510.86 → 2512.54] stabilizing and I need to start,
[2512.62 → 2515.18] you know, making more consistent
[2515.18 → 2518.52] predictions or validations or
[2518.52 → 2521.46] proper training, I try to go into a
[2521.46 → 2522.94] more traditional software engineer
[2522.94 → 2523.48] practice.
[2523.48 → 2528.22] There is this tool by Fast.ai
[2528.22 → 2531.10] called MB Dev, where they try to bring
[2531.10 → 2533.54] all of this literate programming into
[2533.54 → 2535.42] Jupyter notebooks so you can have your
[2535.42 → 2538.92] code and your tests and then develop
[2538.92 → 2540.22] your library from there.
[2540.94 → 2544.68] I think it's good to start bringing the
[2544.68 → 2546.60] software engineering practices into the
[2546.60 → 2547.62] workflow of people.
[2547.98 → 2550.24] But then again, once I started finding
[2550.24 → 2553.34] myself that I am reusing and calling
[2553.34 → 2555.56] a lot of functions or methods that I've
[2555.56 → 2558.56] declared into a Jupyter notebook and I
[2558.56 → 2560.60] have to reuse it and probably for the
[2560.60 → 2563.34] same workflow or other workflows,
[2564.02 → 2565.84] that's also an indication that, okay,
[2566.12 → 2567.12] this isn't working.
[2567.36 → 2569.90] This has to become a standalone module
[2569.90 → 2572.98] or a standalone package that I can use
[2572.98 → 2575.92] and share and reuse and maintain
[2575.92 → 2578.78] separately rather than, you know, having
[2578.78 → 2581.52] bits and pieces in multiple codebases or
[2581.52 → 2584.08] multiple Jupyter notebooks and having to keep
[2584.08 → 2586.00] that updated if needed.
[2587.14 → 2587.74] Awesome.
[2588.28 → 2590.62] Yeah, I would definitely encourage everyone,
[2590.90 → 2593.72] all the listeners to go and listen to
[2593.72 → 2596.46] your talks, both on the ML scoring talk,
[2596.86 → 2598.70] but also this Jupyter talk.
[2598.92 → 2601.16] This is really useful and very practical
[2601.16 → 2601.78] things.
[2601.86 → 2603.50] So I would definitely encourage people to
[2603.50 → 2603.88] go there.
[2604.42 → 2606.56] Also, thank you for mentioning Fast.ai.
[2606.56 → 2608.78] We actually mentioned them, you know, a good
[2608.78 → 2611.30] bit on the podcast because they contribute
[2611.30 → 2611.92] so much.
[2612.08 → 2614.14] So, yeah, I think it's a testament to what
[2614.14 → 2615.72] they're doing that they're mentioned so
[2615.72 → 2616.02] much.
[2616.38 → 2618.22] I was wondering kind of to close us out
[2618.22 → 2618.42] here.
[2618.48 → 2620.48] So we've talked a lot about, you know,
[2620.74 → 2623.78] maybe some things that certain people,
[2624.52 → 2626.80] certain listeners, especially who maybe
[2626.80 → 2628.88] are newer to the software engineering side
[2628.88 → 2630.58] of things might be a little bit
[2630.58 → 2633.06] intimidated by whether that's like, you
[2633.06 → 2637.40] know, Python project structure and tests
[2637.40 → 2639.54] and automation and all of this stuff.
[2639.90 → 2642.24] I was wondering, because you're also,
[2642.56 → 2644.94] you know, in the role as a Python software
[2644.94 → 2646.74] foundation fellow, do you have any good
[2646.74 → 2649.44] recommendations for maybe people that are
[2649.44 → 2652.92] wanting to level up their ability to code
[2652.92 → 2656.10] good Python that has a lot of integrity
[2656.10 → 2659.82] and integrate tests and, you know, Python
[2659.82 → 2661.32] deployments and all those things?
[2661.32 → 2663.80] Do you have any good suggestions for people
[2663.80 → 2666.50] in terms of learning resources and ways
[2666.50 → 2668.28] for them to level up in that sense?
[2669.10 → 2671.74] Yeah, well, there are a ton of resources
[2671.74 → 2672.40] out there.
[2672.62 → 2675.74] That is the problem that it's always again
[2675.74 → 2678.72] to fall into this rabbit hole, right?
[2678.92 → 2681.10] There is, for example, if someone wants to
[2681.10 → 2684.28] get into more DevOps kind of thing, Emily
[2684.28 → 2687.02] Friedman, that is one of my colleagues in
[2687.02 → 2689.56] my team, she just released a book called
[2689.56 → 2690.72] DevOps for Domes.
[2690.72 → 2693.48] It's not focused on machine learning.
[2694.06 → 2696.36] It's a very, very good resource to get you
[2696.36 → 2699.46] into that DevOps mindset and understanding
[2699.46 → 2702.20] how you would integrate continuous integration
[2702.20 → 2703.92] and delivery into your projects.
[2704.16 → 2706.28] And then you can interpolate some of those
[2706.28 → 2708.58] things into your own data science stuff.
[2708.76 → 2710.40] Something else that I recommend is,
[2710.86 → 2712.96] I've talked a lot about collaborations
[2712.96 → 2714.76] across teams and team members.
[2714.76 → 2718.74] Sometimes just sitting down with the software engineer
[2718.74 → 2722.58] and have conversations or peer programming sessions
[2722.58 → 2726.20] where you both sit and start writing tests
[2726.20 → 2729.90] or just discussing continuous iteration,
[2730.20 → 2732.82] continuous testing, continuous deployment,
[2732.82 → 2737.50] testing of your programs and your models goes a long way.
[2737.70 → 2740.70] Because again, you're learning from the other one
[2740.70 → 2742.36] and getting things off the ground.
[2743.36 → 2743.64] Awesome.
[2744.08 → 2745.48] Yeah, those are great suggestions.
[2745.82 → 2747.24] I know for me personally,
[2747.50 → 2750.44] I was a little bit nervous to sit down
[2750.44 → 2754.10] and pair program or be next to some software engineers
[2754.10 → 2756.54] when I was first getting started out of grad school.
[2756.54 → 2758.48] But that's probably one of the ways
[2758.48 → 2761.08] that I learn the most the fastest.
[2761.42 → 2763.10] And so I can definitely recommend that.
[2763.30 → 2766.50] And hopefully you got some good engineers on your team
[2766.50 → 2768.46] that are receptive to that.
[2768.78 → 2771.36] Well, Tanya, it's been super instructive
[2771.36 → 2773.94] and really great to talk with you today.
[2774.28 → 2776.44] We'll have links to the various talks
[2776.44 → 2778.94] and the other things that we discussed in our show notes.
[2779.06 → 2781.54] And really, really appreciate you taking time
[2781.54 → 2782.50] out of your busy schedule
[2782.50 → 2784.64] to talk through some of these things with us.
[2784.64 → 2787.88] And I hope we can meet at a conference
[2787.88 → 2789.72] or somewhere in the near future.
[2789.96 → 2790.56] Thank you so much.
[2791.02 → 2792.00] Thank you for having me.
[2792.14 → 2792.96] It's been a pleasure.
[2795.04 → 2795.52] All right.
[2795.56 → 2798.18] Thank you for tuning into this episode of Practical AI.
[2798.44 → 2799.90] If you enjoyed the show, do us a favour,
[2800.02 → 2801.42] go on iTunes, give us a rating,
[2801.68 → 2803.54] go in your podcast app and favourite it.
[2803.66 → 2805.36] If you are on Twitter or social network,
[2805.48 → 2806.36] share a link with a friend,
[2806.44 → 2807.12] whatever you got to do,
[2807.32 → 2808.80] share the show with a friend if you enjoyed it.
[2809.10 → 2811.76] And bandwidth for Change Log is provided by Vastly.
[2811.88 → 2813.32] Learn more at fastly.com.
[2813.32 → 2815.88] And we catch our errors before our users do here at Change Log
[2815.88 → 2816.72] because of Rollbar.
[2816.94 → 2819.30] Check them out at rollbar.com slash Change Log.
[2819.66 → 2822.16] And we're hosted on Linde Cloud Servers.
[2822.48 → 2824.10] Head to linode.com slash Change Log.
[2824.20 → 2824.64] Check them out.
[2824.72 → 2825.56] Support this show.
[2825.96 → 2829.14] This episode is hosted by Daniel Whiten ack and Chris Benson.
[2829.60 → 2831.66] The music is by Break master Cylinder.
[2832.06 → 2835.50] And you can find more shows just like this at changelog.com.
[2835.56 → 2837.62] When you go there, pop in your email address,
[2837.90 → 2839.70] get our weekly email keeping you up to date
[2839.70 → 2841.74] with the news and podcasts for developers
[2841.74 → 2843.94] in your inbox every single week.
[2844.30 → 2845.12] Thanks for tuning in.
[2845.26 → 2846.00] We'll see you next week.
