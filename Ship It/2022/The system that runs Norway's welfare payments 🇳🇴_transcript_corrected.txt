[0.08 → 5.92] I'm Gerhard Laser, and you're listening to Ship It. Show, a podcast about ops, infrastructure,
[6.24 → 7.66] and application platforms.
[8.24 → 13.46] In today's episode, we have the pleasure of Odin Fogholtstrand, Principal Software Engineer
[13.46 → 17.60] at nav.no, Norway's Labour and Welfare Administration.
[18.04 → 23.96] We will be talking about nace.io, the application platform that runs on-prem, as well as on
[23.96 → 24.62] the public cloud.
[24.62 → 31.92] Imagine hundreds of developers shipping, on an average day, 300 changes into a system
[31.92 → 36.80] which processes $100 million worth of transactions on a quiet week.
[37.26 → 39.72] And if you think this is hard, consider the context.
[40.30 → 44.38] A government institution which must comply with our laws and regulations.
[45.20 → 47.68] Big thanks to our partners Vastly and Fly.
[48.02 → 52.66] This MP3 is served with minimum latency from the Vastly Edge location, which is closest
[52.66 → 53.08] to you.
[53.08 → 58.96] Our app and database run on fly.io because it keeps things simple.
[83.08 → 88.16] Joel, the way teams can use Code Insights seems to pretty much be limitless, but a particular
[88.16 → 92.70] problem every engineering team has is tracking versions of languages or packages.
[93.22 → 95.90] How big of a deal is it actually to track versions for teams?
[96.34 → 98.08] Yeah, it's a big deal for a couple of reasons.
[98.26 → 100.08] The first is, of course, just compatibility.
[100.34 → 103.54] You don't want things to break when you're testing locally or to break on your CI systems
[103.54 → 104.22] or test systems.
[104.56 → 108.68] You need to have some sort of level of version unification, minimum version support, and all
[108.68 → 110.86] of that needs to be compatible forward.
[110.86 → 114.98] But the other thing we learned was that for a lot of customers, especially engineer organizations
[114.98 → 119.32] that are pretty established, they have older versions of things or even older versions of
[119.32 → 122.50] like SaaS tools they don't use anymore that they haven't fully removed because they're
[122.50 → 125.02] like not sure if it's still in use, or they lost focus on that.
[125.32 → 128.14] And they're spinning up old virtual machines that they're still paying for.
[128.24 → 131.50] They're using old SaaS subscriptions they're afraid to cancel because they're not sure if anyone's
[131.50 → 132.26] actually using it.
[132.26 → 135.92] And so getting off of those versions not just like saves you the headaches and the risks
[135.92 → 139.92] and the vulnerabilities of being on old versions, but also literally the money of, you know,
[139.98 → 144.44] older systems running more slowly or the build times or, you know, virtual machines and SaaS
[144.44 → 145.66] tools that you're no longer using.
[145.88 → 147.84] Before you had this ability, we talked to teams.
[148.14 → 149.52] There are basically three ways you could do this.
[149.78 → 153.24] You could slack a million people and ask for just like an update point in time.
[153.50 → 157.90] You could have sort of one human in one spreadsheet where like it's somebody's job every Friday
[157.90 → 161.44] or every two weeks to just like search all the code and find all the versions and write
[161.44 → 162.50] it down in a Google sheet.
[162.78 → 166.42] Or there were a couple of companies that I came across with in-house systems that were
[166.42 → 167.02] sort of complicated.
[167.22 → 170.16] You had to know, you know, maybe Kotlin, but you didn't know Kotlin.
[170.22 → 173.00] But if you want to use this system, you had to learn Kotlin, and you'd have to sort of
[173.00 → 176.92] build the whole world from scratch and run basically a tool like this with a pretty steep
[176.92 → 177.42] learning curve.
[177.78 → 181.56] And now for all three of those, you can replace it with a single line source graph search,
[181.70 → 184.28] which is basically just the name of the thing you're trying to track and the version
[184.28 → 185.36] string in the right format.
[185.60 → 188.88] And then we have templates that'll help you get started if you're not sure what that format is.
[188.98 → 191.24] And then it'll automatically track all the different versions for you.
[191.44 → 192.14] Both historically.
[192.30 → 194.46] So even if you start using it today, you can see your historical patterns.
[194.84 → 195.94] And then, of course, going forward.
[196.44 → 196.72] Very cool.
[196.80 → 197.18] Thank you, Joel.
[197.28 → 201.72] So right now there is a treasure trove of insights just waiting for you.
[202.06 → 208.58] Living inside your code base right now, teams are tracking migrations, adoption, deprecations.
[208.82 → 211.76] They're detecting and tracking versions of languages and packages.
[211.76 → 215.74] They're removing or ensuring the removal of security vulnerabilities.
[216.12 → 217.68] They understand their code by team.
[217.68 → 219.46] They can track their code smells and health.
[219.68 → 224.00] And they can visualize configurations and services and so much more with code insights.
[224.24 → 230.66] A good next step is to go to about.sourcegraph.com slash code dash insights.
[230.92 → 233.48] See how other teams are using this awesome feature.
[233.78 → 238.54] Again, about.sourcegraph.com slash code dash insights.
[238.54 → 240.58] This link is in the show notes.
[247.24 → 248.84] We are going to shift.
[249.02 → 251.52] Three, two, one.
[251.52 → 267.64] I've heard about NACE.io.
[268.00 → 271.02] That's N-A-I-S dot I-O.
[271.52 → 277.62] An application infrastructure service built on Kubernetes from Vincent Ammo, our guest from episode 37.
[277.62 → 286.90] This application platform was built specifically to increase the rate of shipping code from a few times a week to hundreds of times each day.
[287.32 → 292.32] The surprising part is that this application platform is running Norway's welfare payments.
[292.86 → 298.56] So we are talking about many billions of dollars worth of transactions every year.
[298.88 → 299.48] It's huge.
[300.04 → 304.24] One of the masterminds behind it is joining us today to talk about it.
[304.86 → 306.32] Odin, welcome to Ship It.
[306.32 → 307.84] Hi, thank you.
[308.00 → 308.74] Thanks for having me.
[309.68 → 313.06] So who is the other mastermind behind this application platform?
[313.28 → 314.26] I know there's two of you.
[314.60 → 319.58] Well, actually, the application platform is, there's a team, I think.
[320.10 → 327.08] So I think there's two of us working as principal engineers at NAV, but the application platform is built by a team.
[327.08 → 331.24] And I was a part of that team when I started.
[331.36 → 335.02] And then I've kind of, I worked there for two or three years full-time.
[335.12 → 339.74] And now I'm more like everywhere in the company because there's so many things to do.
[339.82 → 341.34] And the application platform works so well.
[341.40 → 342.68] We need to fix all the other stuff.
[342.68 → 345.72] But I know there's like you and this other person.
[345.90 → 348.08] I've even seen like your talks that talk about that deck.
[348.12 → 351.60] You're like most like the public figures when it comes to this, right?
[351.64 → 354.34] And the ones that have a lot to do with it.
[354.52 → 356.22] So who is your partner in crime?
[356.22 → 357.26] Oh, yeah.
[357.32 → 358.90] His name is Truly Jørgensen.
[359.10 → 369.86] We had this big change of strategy in our company, NAV, five years ago, where we went from fully outsourced to trying to in source and hire our own developers.
[370.12 → 371.24] And Truly was the first one.
[371.30 → 373.78] And I was like the sixth or seventh one, I think.
[374.22 → 378.92] And now we are three or 400, depending a bit on what you count as a developer.
[379.32 → 382.64] But if you say product developers, I think we're up to 400 people.
[382.64 → 388.74] That is a lot of people to be working on a lot of applications and a lot of code, manage a lot of complexity.
[389.64 → 400.52] So before we start recording, you've described the two of you as Waldorf and Stadler, the two angry old men from The Muppet Show that constantly complain about everything.
[401.06 → 403.94] What is the most recent thing that you complained about?
[404.54 → 410.10] Well, today we had a discussion about GDPR and the streams too.
[410.10 → 419.26] And it's easy to, although it's really important, sometimes it feels like there's so much the technologist says something and the lawyer says another thing.
[419.42 → 422.24] And the trick is to kind of balance the two out.
[422.28 → 428.62] And that's always difficult because a lot of the time one of the sides kind of says, well, everything has to be like I say.
[428.62 → 435.76] But you have to balance the value of using cloud technology with the risk of privacy.
[436.42 → 436.52] Yeah.
[436.98 → 441.10] And I'm assuming that running everything in-house is not an option.
[441.84 → 442.00] No.
[442.10 → 444.82] Well, we used to have that when we started.
[445.44 → 449.62] And NICE was, first iteration of NICE was basically running on-prem.
[449.62 → 464.96] And then I think we have a strategy where we go quite slowly, both going from our old legacy systems to NICE, the Kubernetes platform, but at the same time also going quite slowly from on-prem to cloud.
[465.04 → 466.28] We don't want to do lift and shift.
[466.52 → 474.34] We want to modernize our applications and to get the full value of actually using, both of using Kubernetes, but also of using the cloud.
[474.34 → 480.70] Because we don't see, well, there's not that much value to gain from just moving old stuff to new infrastructure.
[480.88 → 483.72] You need to modernize the applications and make better applications.
[484.08 → 489.30] Because we always say there's none of the users of NAV care about their application platform.
[489.54 → 491.60] We're not here to make better application platforms.
[491.74 → 493.24] We're here to make better services.
[493.90 → 496.18] And better services comes from better applications.
[496.96 → 498.98] And then the platform can, of course, help with that.
[499.06 → 503.28] But that's not why NAV is NAV, to make application platforms.
[503.28 → 505.18] Although that would have been quite cool, actually.
[506.88 → 510.20] So what is the difference between NAV and NACE?
[510.70 → 515.52] Well, NAV is the biggest governmental agency in Norway.
[515.82 → 520.60] We have, as you mentioned, we pay out about a third of the federal budget in Norway.
[521.12 → 526.74] We have everything from age-related pensions to parental benefits to sickness benefits.
[526.74 → 535.36] And we also have a responsibility of helping people get back into work and kind of have the whole working system working as good as possible.
[535.88 → 536.70] So that's NAV.
[536.86 → 540.28] And we used to be many different organizations.
[540.50 → 548.16] And then we had a big merger in 2006, where the politicians thought that if you just put all these different organizations into one organization,
[548.16 → 553.60] then everybody will start to cooperate and data will flow between the different systems and everything.
[554.54 → 558.06] Turns out that wasn't that easy as just putting them into the same organization.
[558.34 → 561.82] There's still monolithic software causing problems.
[562.06 → 565.06] Or three monoliths aren't necessarily better than one monolith.
[565.86 → 567.50] So we still have that.
[567.50 → 569.16] And so that's NAV.
[569.32 → 574.86] And NICE is basically our open source platform that we started building in 2017,
[575.52 → 579.18] which was kind of a kickstart of the whole in sourcing process,
[579.48 → 583.60] where we thought that we should...
[583.60 → 589.10] Because when we go from none or almost non-developers and want to hire a lot,
[589.10 → 594.54] we needed to make it visible and clear that being a developer in our company is good.
[594.54 → 600.20] It's possible to work with good technology and have development speed and have all the good things.
[600.44 → 601.26] So we kind of...
[601.26 → 609.42] We used it as a branding exercise as well as a technology platform to help us get people or developers in.
[609.54 → 616.08] So five years, well, 2016, six years almost now, it will be since NICE has been around.
[616.32 → 620.32] What are the benefits that you've seen in this time of having NICE?
[621.10 → 622.42] I think there's multiple.
[622.42 → 626.00] Well, maybe the clearest one is what you said before.
[626.18 → 631.64] We used to deploy at nighttime and have manual testing periods.
[631.96 → 638.76] And so deployments was maybe something that happened, well, 2005 or 60 was four times a year,
[638.82 → 639.90] and then it grew very slowly.
[640.34 → 643.12] But it was always coordinated, always the big releases.
[643.12 → 648.70] But what NICE did was make it possible for the teams to handle this whole process themselves.
[648.88 → 650.30] And they didn't have to do...
[650.30 → 658.62] There was no technical reason from the platform or infrastructure side that made it necessary for them to coordinate with anyone when they wanted to deploy.
[658.82 → 663.68] Of course, there might be dependencies between applications, but that's a different thing to fix.
[663.68 → 667.88] So now we're up to 1,500 releases a week.
[668.58 → 672.44] I mean, we've been quite steady on that for a few years, I think.
[673.16 → 676.30] We have about 1,300, 1,400 applications.
[676.30 → 680.60] So on average, there's one deployment per application per week.
[680.72 → 687.20] But we have some data showing that most of the employees come from a smaller part of the applications.
[687.44 → 691.56] There are a few of the applications that change a lot and some that hardly changes at all.
[691.56 → 699.24] I think that's a logical consequence of doing microservices, because some is more support and some is more core.
[699.72 → 706.38] But the other side, which is, I think, have taken me a bit by surprise, is the fact that we have this platform,
[706.58 → 707.56] which has very...
[708.24 → 710.74] You can say it has quite tight entry conditions.
[710.96 → 717.10] Although we say it's only Docker containers, but we say you have to do stateless, be stateless,
[717.10 → 723.38] so we can deploy, because Kubernetes can move the application, and we do log collection this way,
[723.50 → 725.50] and metrics this way, and alerts this way.
[725.94 → 727.50] It's quite unifying.
[727.86 → 729.32] We kind of have...
[729.32 → 735.74] We try to do what Spotify called kind of making a golden path to make it easy to do it the right way.
[736.56 → 739.16] And that works almost too well.
[739.30 → 742.28] We have almost all the teams do almost everything the same way.
[742.28 → 749.84] And so we have, although we say there's no real guardrails on programming language, for instance,
[750.00 → 751.28] or stuff like that, people tend to...
[751.88 → 755.66] They copy from each other and learn from each other, so it's quite unified how we do development.
[755.94 → 762.42] And we have a limited number of external services that's available to us.
[762.52 → 763.60] We have Postgres and Kafka.
[763.84 → 770.00] And that means that Postgres and Kafka are basically the two most important architectural parts of our relation database.
[770.00 → 774.04] And we have events, streams of events.
[774.20 → 776.16] And that makes it...
[776.16 → 781.16] That drives the technology development in a quite clear direction, I would say.
[781.32 → 781.60] We have...
[781.60 → 784.22] So we have a quite consistent architecture.
[784.44 → 785.00] And I didn't...
[785.60 → 787.80] I thought that almost the opposite would happen,
[788.00 → 790.78] because you can do whatever programming language wants.
[790.84 → 792.44] You can do...
[792.44 → 793.16] There's...
[793.16 → 796.24] The organization is so big, and there are so many different problems to solve.
[796.28 → 798.30] I thought the diversity would almost be bigger.
[798.30 → 802.56] But it turns out it's quite unified, our architecture.
[802.76 → 808.80] And I think that's a good thing, although I'm always a bit scared of what that means.
[809.58 → 812.14] I don't want us to relax either.
[812.22 → 817.38] I want us to be able to see when there's new interesting stuff happening that we need to use.
[817.90 → 818.08] Yeah.
[818.58 → 818.88] Okay.
[818.88 → 825.08] So going back to how many deploys you do, there's data.nav.no.
[825.38 → 830.30] And I'll put a link in the show notes that shows how these deploys have changed over the years.
[830.66 → 831.88] And I think it starts in 2009.
[832.62 → 838.48] So there's a lot of data, 13 years worth of data, to see how many services you had, how often you deploy.
[838.64 → 839.86] That is so insightful.
[840.10 → 842.46] I was surprised that this data is public, by the way.
[842.46 → 850.56] This is amazing for anyone to see just, you know, how big this platform is in terms of applications, in terms of deploys.
[850.84 → 851.92] That was fascinating.
[852.44 → 854.34] So I have to ask this.
[855.02 → 856.06] Why Kubernetes?
[856.78 → 858.20] What drove you to Kubernetes?
[858.98 → 862.02] Well, I think there are two answers to this.
[862.02 → 868.72] It's kind of the one, when we look back on it, I think we want to use open source technology.
[869.10 → 875.18] We want to have, although we're not, it's not important for us to use many clouds at the same time.
[875.28 → 878.90] I think we think that probably costs more than it gives.
[879.90 → 890.12] But to have kind of a to use open source as the main, or open source APIs as the main boundary between the application and the platform,
[890.12 → 895.54] makes it easier to move and makes a better distinction between the application and the platform.
[896.08 → 903.52] So we use, so Kubernetes, when I started to make application platforms in 2000, I think it's 2014,
[904.38 → 905.36] Mess was the thing.
[905.82 → 908.60] So we used Mess and Marathon.
[908.90 → 913.82] I can't even remember all the things we used, but it was kind of a completely different platform.
[913.82 → 920.20] And we had this, then we had the problems of, they weren't really, they weren't cooperating.
[920.32 → 926.60] Well, there were just a bunch of open source projects, and we had to spend a lot of time just updating everything and figuring out how to use them.
[926.74 → 931.38] And then at that time, I think 0.8 or something or Kubernetes was released.
[931.52 → 936.52] And we, someone in our team knew someone from Google and said, well, this is good.
[936.90 → 941.18] So we looked at it, and it did all the things good that the Mess universe did badly.
[941.18 → 942.96] Everything was one big package.
[943.12 → 947.18] You could just do, you just had to figure out how this worked, and then it solved everything.
[947.56 → 951.56] So after that, it feels like Kubernetes basically won that space.
[951.84 → 956.68] And then all the cloud vendors came running or offered that as a service as well.
[956.78 → 963.48] So I think the main, doesn't seem to be that many alternatives that are as open source.
[963.74 → 969.02] You could go all the way to some kind of serverless thing and then be more cloud dependent.
[969.02 → 974.52] But I'm not sure if I see that as a good move for, at least not for organizations of our size.
[975.04 → 975.18] Yeah.
[975.38 → 975.62] Yeah.
[975.76 → 976.18] That's right.
[976.28 → 976.44] Okay.
[976.90 → 980.76] So I'm looking at Nase.io, and I see a lot of great components there.
[981.34 → 983.10] Grafana, InfluxDB, Linked.
[983.48 → 984.98] A few that I do not recognize.
[985.20 → 988.56] There's Collide with a K, OS Query, Unleash.
[988.92 → 990.90] How close are you to those components?
[992.02 → 994.20] Well, there are different things.
[994.38 → 996.16] Unleash is a feature toggle system.
[996.16 → 1001.24] It was basically, actually, it was created initially in the company I worked for before
[1001.24 → 1004.32] now, a company called Fin, which is basically a Norwegian eBay.
[1005.02 → 1007.42] And it's now a big open source project.
[1007.56 → 1012.02] I think it's one of the two big players in the feature toggle system.
[1012.60 → 1017.64] So a lot of our teams need feature toggles to be able to handle their deployment speed.
[1017.64 → 1025.94] And then Collide and OS Query is part of a feature we developed quite late in NICE, where
[1025.94 → 1031.34] we say, where it's more about handling, controlling the laptops we use and how the laptops connect
[1031.34 → 1031.92] to our clusters.
[1032.22 → 1034.46] So we call that NICE device.
[1034.70 → 1042.98] And Collide is basically, it's a hosted service that glues together OS Query, which is an agent
[1042.98 → 1047.06] that runs on the laptop and checks if everything is up-to-date and the laptop is sound.
[1048.22 → 1053.34] And handles the management of that and how to communicate with users, telling them, well,
[1053.34 → 1056.14] you need to update macOS or you need to do a Chrome upgrade.
[1056.32 → 1061.78] And then we build some gateways ourselves that kind of does the last bit.
[1061.94 → 1067.72] So we use so we can control exactly how our laptops access our production environments.
[1067.72 → 1068.24] Hmm.
[1068.68 → 1069.08] Interesting.
[1069.56 → 1072.92] So which of these components do you use most often?
[1073.20 → 1075.40] Because there's quite a few, and it's not an exhaustive list.
[1075.54 → 1077.54] Is there something that you use on a daily basis?
[1077.62 → 1081.94] I'm assuming Collide, OS Query, because that must be running on your laptop.
[1082.04 → 1087.08] But what else that is more like you're more like hands-on, you're more aware that is there?
[1087.40 → 1091.74] Because I think Collide, OS Query, install them, they provide connectivity and they just
[1091.74 → 1093.06] kind of get out of the way.
[1093.06 → 1099.80] I would say my favourite tool of all the tools of Nice is probably Grafana.
[1100.02 → 1100.42] Really?
[1100.88 → 1101.14] Okay.
[1101.34 → 1108.24] Ever since I used to be a backend developer making applications and just the sheer joy
[1108.24 → 1113.24] and all the interesting things you get out of looking into what happens in production
[1113.24 → 1119.56] and making graphs of everything and trying to figure out why stuff is happening and what
[1119.56 → 1121.74] does this mean when this goes up and this goes down.
[1121.74 → 1126.50] And then whenever I, at least when I was a developer, application developer, whenever
[1126.50 → 1132.18] I didn't know what to do, I could always find something to measure and try to get more
[1132.18 → 1134.62] insight into what's actually happening in our application.
[1135.24 → 1140.58] Interestingly, we kind of, as a platform, at least as a company, we moved a bit away or
[1140.58 → 1140.84] not.
[1141.30 → 1142.94] We've extended how we do that.
[1142.94 → 1150.54] So now we roll some more into getting the data out of the databases as well, trying to
[1150.54 → 1155.92] think of that data as a product and not just do the real-time monitoring, but also try to
[1155.92 → 1159.34] do more aggregated monitoring or reports even.
[1159.34 → 1168.18] So we use, it's kind of a sister platform of nice, our data platform called Nada, which we kind of try to make, try to do that with.
[1168.18 → 1175.96] So help the teams to be even more conscious of all the data they have and what they can learn from looking at the data.
[1176.10 → 1177.30] Do you say Nada?
[1177.30 → 1177.42] Yeah.
[1178.06 → 1178.32] Yeah.
[1178.96 → 1179.58] Like nothing?
[1180.08 → 1180.56] Yeah.
[1180.60 → 1181.30] That means nothing.
[1181.52 → 1181.70] Okay.
[1182.18 → 1183.32] That's an interesting name.
[1184.08 → 1192.50] The reason for that name, at least my, my version of the history of the reason of that name is that we didn't want the platform to own the data.
[1192.50 → 1200.76] We wanted to, because traditionally the data warehouse is a central team and the data warehouse team owns both the platform and the data.
[1200.94 → 1205.80] But we wanted to do the same thing with nice because nice doesn't own the applications running on them.
[1205.86 → 1207.14] And we wanted the data platform.
[1207.52 → 1210.76] That's a platform and the teams should own the data.
[1211.26 → 1213.00] The application teams should own the data.
[1213.48 → 1217.72] So basically the Nada name is, or also it's Nav Data, of course.
[1217.72 → 1224.84] So it's an yeah, but we wanted it to be clear that the platform is a platform and the teams own the data.
[1225.46 → 1225.80] Okay.
[1226.08 → 1226.40] Okay.
[1226.66 → 1227.30] That's a good one.
[1227.30 → 1235.40] So I know that you run other services, other components, as you call them, which are not listed on the nice IO website.
[1235.92 → 1239.14] There is a tweet, which I noticed three hours ago, very recent.
[1239.72 → 1240.58] Do you know what's cool?
[1241.20 → 1243.40] Keeping your Kubernetes cluster secure.
[1243.40 → 1249.18] At Nav Norge, we use Tavern to ensure no pod runs unchecked.
[1249.44 → 1253.14] And the question is, what is your best tip securing Kubernetes clusters we want to hear?
[1253.42 → 1254.62] I'll put a link in the tweets.
[1254.78 → 1259.78] I mean, when this comes out, if you want to answer, it will be, you know, a few weeks later, but still it will be around.
[1260.42 → 1263.02] What do you think about Tavern, and how do you think about securing things?
[1263.02 → 1270.18] Because this must be a very important topic considering the data and the transactions and what is happening in your applications.
[1270.18 → 1277.28] I would say going, answering that question from a more of a top-down perspective.
[1277.42 → 1286.58] First, I think the main thing with security, when you're making an application platform, and you want to help the team secure their applications,
[1286.84 → 1294.62] it's really important to understand the needs of the developers to make sure that any security feature you add is usable.
[1294.62 → 1305.10] Because in my experience, there's been loads of security people that are so into security that they make this principle that is almost impossible to adhere to.
[1305.68 → 1314.18] So at some time in the process, there will be something where the developer has to choose, should I follow the principle, or should I deliver on time?
[1314.96 → 1317.04] Most of the time, they will deliver on time.
[1317.04 → 1320.74] So you have to make the security things easy to use.
[1321.06 → 1326.18] In my experience, it's more important that it's usable than it's 100% secure.
[1327.12 → 1332.34] Because if you make all the principles and all the things that are needed to make it 100% secure,
[1332.72 → 1334.88] and the team doesn't follow that because it's impossible,
[1335.34 → 1340.22] then you have the worst situation at all when there's the people responsible for security think everything is okay.
[1340.86 → 1345.52] And the people in the teams doesn't want to tell the security team what they haven't done.
[1345.52 → 1349.44] So, for instance, we used service mesh.
[1349.78 → 1354.84] Before, we used to have these network zones in our on-prem architecture where we had two zones,
[1354.98 → 1359.70] one for the internal applications and one for external applications, and basically perimeter safety.
[1359.86 → 1363.06] So if you came inside the firewall, you had access to everything.
[1363.78 → 1371.96] But instead, we used service mesh and zero trust principles to basically put a small firewall around every application
[1371.96 → 1376.52] and make it the team's responsibility of configuring this firewall.
[1377.34 → 1381.42] So the teams, and it's a part of the configuration of the application,
[1381.68 → 1386.12] what applications can talk to you, and what applications do you need to talk to.
[1386.66 → 1392.98] So instead of a central firewall and some kind of person in the middle that always has too much to do,
[1393.34 → 1397.92] you make it a team's responsibility to configure this, and then everything works better.
[1397.92 → 1427.90] So, let's go.
[1427.92 → 1431.26] This episode is brought to you by our friends at Ray gun.
[1431.40 → 1437.10] Get instant visibility into the health of your software, actionable, real-time insights into the quality
[1437.10 → 1439.82] and the performance of your web and mobile apps.
[1440.24 → 1444.80] And I'm here with John Daniel Track, co-founder and CEO of Ray gun.
[1445.20 → 1449.32] JD, how does the interface of Ray gun help a team see progress?
[1449.42 → 1453.18] Because sometimes progress is better than simply goals.
[1453.18 → 1456.40] You know, the goal is to have high-performing software, of course,
[1456.58 → 1461.26] but the progress to get there is not easily measured or celebrated along the way.
[1461.46 → 1467.32] Yeah, this is something that I often find I end up speaking with more at the executive level with some customers,
[1467.32 → 1472.98] because it's also important to remind folks that aren't necessarily software engineers that, you know, bugs are common.
[1472.98 → 1475.02] You know, it's not the team's fault that there are bugs.
[1475.16 → 1477.36] And that's where we go back to the trajectory thing.
[1477.44 → 1478.94] Like, are we actually making progress?
[1479.36 → 1484.70] So, sometimes the work we're doing with folks, we present like an error inbox where we group things up
[1484.70 → 1487.04] so that you're not having to deal with every single instance.
[1487.26 → 1489.14] You can work at the sort of root cause level.
[1489.14 → 1492.60] And so, that just looks really familiar, almost a little bit like Gmail,
[1492.86 → 1496.32] but you've got some charts, some beautiful, attractive charts that will show you how you're going.
[1496.56 → 1498.16] It could be an engineering manager.
[1498.30 → 1499.14] It could be a QA leader.
[1499.14 → 1503.48] It could be anybody that can kind of say, look, the chart is going down towards the right.
[1503.72 → 1505.06] You know, that's what we want to be doing.
[1505.18 → 1507.84] Fewer errors or we want to get the response times up.
[1508.28 → 1511.84] Similarly, you want to make sure that you're presenting that data in the most scientific way.
[1511.90 → 1515.28] So, no averages, you know, just use medians, P99s.
[1515.28 → 1518.14] I want to understand the outliers, you know, averages are just lies.
[1518.14 → 1522.00] So, get the real data, understand where you are, and just start chipping away at it.
[1522.40 → 1523.44] Very cool. Thank you, JD.
[1523.62 → 1528.64] All right, head to Raygun.com to learn more and start your free 14-day trial.
[1528.74 → 1529.88] No credit card required.
[1530.24 → 1534.84] Join thousands of customer-centric software teams who use Ray gun every single day
[1534.84 → 1537.08] to deliver flawless experiences to their customers.
[1537.28 → 1539.68] Again, Raygun.com.
[1548.14 → 1552.32] What about the data?
[1552.32 → 1558.24] How do you secure the stateful data that is persisted at rest?
[1558.84 → 1563.46] Postgres SQL, for example, or anything else that's used like for persistence?
[1563.96 → 1566.10] Flat files, maybe you have those as well.
[1566.22 → 1566.58] I don't know.
[1566.58 → 1573.88] Well, there isn't one way we're doing it because we're so big, and we have a gazillion different requirements.
[1574.30 → 1576.96] But for Postgres, we used...
[1576.96 → 1579.22] Nice now runs on GCP.
[1580.08 → 1584.52] So, we basically used a managed GCP service for Postgres.
[1584.52 → 1586.24] And we have...
[1586.24 → 1590.30] We considered bringing our own key architectures.
[1590.44 → 1599.88] But right now, it feels like that increases the risk of us losing the key more and thus losing the data
[1599.88 → 1602.16] than actually losing the data.
[1602.54 → 1606.48] So, although that's something we consistently rethink,
[1606.64 → 1610.74] right now we mostly use the normal features of GCP.
[1610.74 → 1614.82] And then we have some extra backup things because we want to have...
[1614.82 → 1617.74] Make sure we have everything running inside Norway as well.
[1617.90 → 1619.96] Or have the data accessible inside Norway.
[1620.50 → 1620.78] Right.
[1621.08 → 1621.94] Okay, that makes sense.
[1622.56 → 1629.32] Do you make use of anything like EPF to secure or at least have visibility all the way down into system calls?
[1629.62 → 1631.56] Not just like network traffic?
[1632.24 → 1632.62] Yeah.
[1633.32 → 1635.74] I know the plan is for us to...
[1635.74 → 1638.08] I'm not entirely sure right now.
[1638.08 → 1643.58] But our plan is to go to Cilium as a service mesh from LinkedIn.
[1643.96 → 1645.36] We were first on Into.
[1645.94 → 1649.24] And then Into felt like it was a bit too much for our needs.
[1649.46 → 1650.62] And then we went to LinkedIn.
[1650.80 → 1653.04] And now we're looking at Cilium, which is EPF.
[1653.24 → 1654.12] So, I think...
[1654.12 → 1656.00] But that's how we approach that problem.
[1656.20 → 1656.94] That's interesting.
[1656.94 → 1664.90] It's great that using a platform that promotes open source and has a very rich ecosystem.
[1665.46 → 1674.16] It allows you without, you know, too much investment to be able to go from one provider to another, from one solution to another.
[1674.28 → 1676.78] Which, by the way, there's open source versions of it.
[1676.84 → 1677.62] You can try it out.
[1677.88 → 1679.08] There's paid for versions.
[1679.08 → 1682.36] And so, it's nice that you can switch between these things.
[1682.70 → 1684.52] How did that work out for you in practice?
[1684.64 → 1687.70] How did it work out for you going from Into to Linked?
[1688.14 → 1691.32] Was that, would you say, a seamless migration or transition?
[1691.64 → 1695.50] Or were there complications that you couldn't foresee?
[1696.26 → 1699.46] First, I just wanted to say we blogged about that.
[1699.58 → 1703.10] There's a blog, which I presume you can put in the show notes after.
[1703.10 → 1705.94] So, I wasn't the main part of that process.
[1706.02 → 1708.40] But as far as I can tell, it wasn't that difficult.
[1708.74 → 1714.00] It took some time because you had to change something in all the applications.
[1714.26 → 1718.80] But we have a perfect dev environment that we can do these things in.
[1718.88 → 1723.38] And I think, as far as I remember, it was something you did in approximately one day.
[1723.54 → 1726.70] Moving all the several hundred applications from one to another.
[1727.16 → 1727.92] That's impressive.
[1727.92 → 1728.24] Yeah.
[1728.24 → 1733.20] And I think, more or less, going all the way back to the questions I had about why Kubernetes,
[1733.34 → 1736.68] one of the main reasons Kubernetes is so good is you have all this.
[1736.82 → 1740.94] You have this API, which is incredibly well thought through.
[1741.86 → 1745.48] And they kind of, they made this in, I don't know, 2015 or something.
[1745.58 → 1751.10] And it still kind of makes sense as an API, even though they changed a lot of the things behind it.
[1751.34 → 1752.64] And they made it extensible.
[1752.64 → 1754.90] But you have this API that's so good.
[1755.44 → 1759.74] And it matches so well with what an application and an infrastructure does.
[1759.92 → 1762.88] So, it makes it possible to create tools like a service mesh.
[1763.20 → 1768.30] And it makes it possible to change implementations, even of the service mesh.
[1768.54 → 1771.46] Or the implementation of the Docker runtime.
[1771.74 → 1773.72] Or the container runtime or whatever.
[1774.28 → 1778.30] With almost no disruptions to the actual uses of the platform.
[1778.30 → 1783.72] So, I remember in the old days, this was, most of the things was almost impossible.
[1783.92 → 1786.16] And it took weeks and months to plan and do.
[1786.78 → 1787.66] Yeah, that's right.
[1787.84 → 1788.80] Yeah, I remember the pain.
[1788.88 → 1789.78] It was like so hard.
[1789.86 → 1791.90] Like, you wouldn't even think like, no, no, too expensive.
[1792.04 → 1792.86] Let's just not do that.
[1793.16 → 1796.06] And that's how like a lot of the great ideas would end up.
[1796.32 → 1798.36] Because the implementation was just not worth it.
[1798.74 → 1802.48] And now you can even buy it hosted.
[1802.48 → 1810.10] So, most of the stuff you don't even have to think about, like updating or changing nodes or increasing the capacity.
[1810.32 → 1812.50] It's just not even clicking a button.
[1813.38 → 1814.90] Yeah, that's amazing.
[1815.18 → 1816.54] I love that part too.
[1817.08 → 1824.66] So, if anyone is curious to learn more about this platform, there is some great content on docs.nace.io.
[1824.66 → 1826.78] There are references with diagrams.
[1827.22 → 1828.82] There are step-by-step guides.
[1829.14 → 1834.38] There's even 300 lines of YAML for the nice application example.
[1834.86 → 1839.56] There's a lot of Kubernetes YAML, best practices and other content worth reading.
[1840.00 → 1841.72] I enjoyed digging into the deployment section.
[1842.00 → 1842.84] I was really surprised.
[1842.90 → 1844.96] There's like so much good stuff there.
[1845.30 → 1846.54] So, have a look if you're curious.
[1846.72 → 1847.84] We'll add a link in the show notes.
[1848.00 → 1849.92] But it's docs.nace.io.
[1849.92 → 1854.70] So, before we change subjects, there's something that I wanted to ask you since the beginning.
[1855.54 → 1858.64] I know that you've been in tech for quite a few decades.
[1859.02 → 1861.98] So, how long has it been that you've been in tech?
[1862.30 → 1863.98] Do you remember when you started?
[1864.64 → 1867.48] I left university in 2003, I think.
[1867.62 → 1868.84] So, I've basically been working.
[1869.06 → 1870.30] I started as a consultant.
[1870.56 → 1874.02] And then I realized consultancy isn't what I want to do.
[1874.10 → 1877.24] I want to be part of the company that owns the product.
[1877.24 → 1879.76] So, well, it's almost 20 years.
[1880.42 → 1881.12] 20, yeah.
[1881.58 → 1881.90] Okay.
[1882.32 → 1888.62] So, in a few sentences, as a very brief summary, what were the last 10 years in tech?
[1889.08 → 1890.60] What were your last 10 years in tech?
[1890.70 → 1892.08] There was Kubernetes part of it.
[1892.16 → 1897.70] But what else happened that brought you to where you are today, a principal engineer at NAV?
[1898.34 → 1901.42] Well, I used to be a Java developer.
[1901.42 → 1905.10] I was really identified as a Java developer.
[1905.46 → 1911.52] And a bit by chance, I got the role as a lead developer for the infrastructure and operations teams at one company.
[1911.66 → 1918.04] And then I realized I could use all the experience I had as a frustrated backend developer to make application platforms.
[1918.28 → 1923.24] And basically, I've been doing a lot of that since then, just figuring out, doing all the things I learned.
[1923.24 → 1927.56] Or I couldn't do easy before trying to make that possible.
[1927.86 → 1939.62] And then for the last few years, it's been more and more about making everything fit together, not just the application platform, but making the management understand what's important.
[1939.98 → 1948.32] And why making software is completely different from building, doing other things that the Norwegian government does and finances, for instance.
[1948.94 → 1949.18] Yeah.
[1949.46 → 1950.10] Yeah, that's right.
[1950.10 → 1954.48] So if you were to write an application today, would you still pick Java?
[1955.04 → 1956.88] No, I would probably do Kotlin.
[1957.20 → 1963.36] I think I don't program as much as I want to anymore, but mostly I program in Kotlin and Golang.
[1963.72 → 1967.22] And I think programming in Kotlin is more fun.
[1967.84 → 1975.96] But I might think that programming in Golang is a bit frustrating, but it feels like it will last longer and be stable for longer.
[1976.28 → 1976.56] I see.
[1976.56 → 1982.00] And so if it's my decision, I would probably still go for Kotlin because that's more fun.
[1982.12 → 1985.88] And you can feel more clever when you write Kotlin than when you write Golang.
[1986.40 → 1986.78] Okay.
[1986.94 → 1987.28] Okay.
[1987.36 → 1988.04] That's a good one.
[1988.54 → 1993.58] And if you were to choose where to run this application, what would your choice be?
[1993.58 → 1995.76] Nice, probably.
[1996.20 → 2001.00] Well, I mostly would write things for Java and then the question is similar.
[2001.14 → 2006.70] But I've always thought I mostly worked at big companies with hundreds of developers.
[2006.70 → 2015.58] And I have this lingering thing in my head where maybe all the things I think is good for those companies might not be good for small companies.
[2015.88 → 2026.08] So probably try to figure out some other ways of doing it more serverless or higher level abstractions from some of the cloud vendors, for instance, just to make sure.
[2026.08 → 2032.62] I have this suspicion that at some point in the future, that's going to be even easier, even for the big organizations.
[2032.94 → 2035.58] But I'm not necessarily sure we're there yet.
[2035.76 → 2037.20] But it's difficult to say.
[2037.96 → 2038.10] Okay.
[2038.10 → 2047.34] So the last few years have been really challenging for governments around the world, especially welfare systems around the world.
[2047.50 → 2049.64] And obviously we're talking about COVID, about the pandemic.
[2049.94 → 2051.12] It's been really, really tough.
[2051.78 → 2057.04] So what challenges did COVID bring for your platform for NACE?
[2057.94 → 2066.40] Well, the very first challenge was, I think, I think this was the 11th, 10th or 11th of March in 2020.
[2066.40 → 2067.66] That's very specific.
[2068.10 → 2068.40] Okay.
[2068.44 → 2069.24] This has got to be good.
[2069.76 → 2070.42] All right.
[2070.88 → 2076.70] Because that's when basically the prime minister of Norway said, well, everybody has to stay at home.
[2077.00 → 2083.06] And unless you have a perfect reason to, basically, if you're a fireman or work at a hospital or something, you have to work from home.
[2083.88 → 2086.60] Before that, most people went to the office most days.
[2086.96 → 2090.22] And all the tech and all the infrastructure was basically built around that.
[2090.22 → 2097.40] So luckily we had just enough, we had the necessary things to be able to start working from home.
[2097.40 → 2099.34] But it was kind of a challenge.
[2099.34 → 2106.20] And you had to relearn how to communicate and how to work as a team, basically.
[2106.20 → 2111.20] And I think that was interesting.
[2111.38 → 2113.04] It worked quite well when everybody was at home.
[2113.08 → 2117.88] And I think it's an even more interesting challenge now when some people want to stay home.
[2117.88 → 2125.20] And some people want to go to the office because it's much more difficult to solve this challenge when the teams are more hybrid.
[2125.98 → 2129.68] But that wasn't the most difficult thing that happened during the pandemic.
[2129.68 → 2138.60] Because of this order from the prime minister, we had a lot of, and I think the English word here is furloughed.
[2138.72 → 2142.14] We had lots of workers in Norway, not that now, but in Norway furloughed.
[2142.68 → 2147.48] And according to the rules of Norway, then you're supposed to get a benefit.
[2148.12 → 2151.66] I think there was normally there's around a thousand of those applications a day.
[2151.72 → 2155.72] And now we had like several hundred thousand furloughed people in a week or so.
[2155.72 → 2159.12] So we were still early in our transformation.
[2159.32 → 2163.64] And so most of those applications would normally be handled by manual caseworkers.
[2164.54 → 2166.04] So our estimates was this.
[2166.52 → 2174.72] It's going to take a year for us to handle in the current systems to handle all of these applications before everybody get their money.
[2175.32 → 2176.74] And people needed money.
[2177.62 → 2182.30] So the government in Norway tried to make some alternative ways of handling this.
[2182.30 → 2184.84] So they had a list of 12 different things, I think.
[2184.84 → 2192.46] And me and a team and Truly and others started working on one of them where we wanted to kind of have a...
[2192.46 → 2200.68] At the same time, we wanted to make the laws describing this benefit, which basically was an advance of the normal unemployment benefit.
[2201.24 → 2202.42] So we had to make the law.
[2202.80 → 2205.62] And then we had to make a system that implemented that law.
[2206.12 → 2207.78] And we had to do it really quickly.
[2207.78 → 2215.20] So I still remember we had stand-up meetings at 8 o'clock in the morning, 4 o'clock in the afternoon, and 10 o'clock at night.
[2215.86 → 2221.24] Every day for two weeks or something, where we tried to figure out what the law...
[2221.24 → 2227.28] What we could put in the law, because that was limited by what is smart to put in the law and what we could implement.
[2227.28 → 2239.34] So we had to balance kind of what's possible to implement in a week or so and what's necessary to put in the law to reduce the risk of people misusing this opportunity.
[2240.06 → 2240.96] That's amazing.
[2241.44 → 2243.20] And this is a country we're talking about.
[2243.30 → 2245.14] This is not like a big tech company.
[2245.36 → 2249.42] This is like you're dealing with the benefits of a whole country, right?
[2249.46 → 2250.90] Like that's like your responsibility.
[2251.66 → 2252.88] Wow, that is big.
[2252.88 → 2258.54] So we had the law was ready on a Thursday, I think.
[2258.74 → 2262.70] And then we managed to build the system in basically three days.
[2263.34 → 2267.42] And I'm really proud to say we built that system using PERF programming.
[2268.24 → 2271.80] And we had the user testing late Sunday night.
[2272.42 → 2275.02] And then we went live on...
[2275.02 → 2276.82] I can't remember if it was the Monday or the Tuesday.
[2277.38 → 2280.72] And then we had a gradual rollout using Unleash, actually.
[2280.72 → 2285.64] So we could make sure that the system kind of worked well.
[2285.72 → 2286.82] We had the increased pressure.
[2287.08 → 2291.38] And then in a week, we had paid out 1 billion Norwegian kroner.
[2291.94 → 2298.06] A week from the law was ready till we had 1 billion Norwegian kroner paid out.
[2298.20 → 2298.54] Okay.
[2299.10 → 2300.08] That was a good system.
[2300.36 → 2301.76] Why did you write it in by any chance?
[2301.80 → 2302.36] Was it Kotlin?
[2302.76 → 2303.48] This was Kotlin.
[2303.80 → 2304.32] Really?
[2304.32 → 2306.52] It was running a nice Anaposkres database.
[2306.76 → 2307.00] Wow.
[2307.00 → 2308.12] We actually...
[2308.12 → 2309.64] It was a lot of reuse.
[2310.50 → 2314.50] We had some strange components.
[2314.66 → 2321.30] We had the calculator that people used to figure out what they could get in a benefit if they needed to.
[2321.76 → 2326.30] But that calculator kind of had the functionality we needed to get the data.
[2326.54 → 2330.28] The data to calculate what the people should get in these new benefits.
[2330.60 → 2333.60] So basically, you used the calculator as an API.
[2333.60 → 2336.84] So we kind of grabbed things from everywhere.
[2336.84 → 2341.30] And the payment system had this old file-based interface that we used.
[2341.56 → 2342.94] So instead of...
[2342.94 → 2343.84] We had some really...
[2344.66 → 2348.18] Some of the integrations was like totally modern with Kafka and asynchronous.
[2348.44 → 2353.44] Another one was writing files to disk and a bash script moving that file to another disk.
[2353.48 → 2353.88] That's crazy.
[2353.88 → 2359.16] And then the payment system picking up the file and putting it into making payments.
[2359.16 → 2360.68] So it was everything.
[2361.22 → 2361.84] We kind of...
[2361.84 → 2363.84] We took whatever we could find, basically.
[2364.42 → 2366.34] Lots of respect to the people that built that.
[2366.48 → 2369.48] Because as cobbled together as it was, it worked.
[2369.80 → 2370.00] Right?
[2370.12 → 2371.62] Are we talking billions?
[2371.82 → 2372.66] Like with a big B.
[2373.26 → 2377.26] One billion króna, I'm pretty sure it's like at least as much as like one billion dollars.
[2377.46 → 2379.26] No, I think it's a tenth.
[2379.82 → 2382.44] Yeah, I think one dollar is ten million króna.
[2382.52 → 2384.54] But still, it's loads of money in Norway.
[2384.68 → 2384.80] Right.
[2384.94 → 2386.56] So just a hundred million, right?
[2386.60 → 2387.16] Like in a week.
[2387.24 → 2388.72] Just a hundred million dollars.
[2389.22 → 2389.96] That's okay.
[2390.08 → 2394.18] Like some bash scripts and some code load and some like Postgres and some Kafka.
[2394.32 → 2395.32] That's just amazing.
[2395.76 → 2396.78] And it all worked.
[2396.86 → 2397.06] Okay.
[2397.38 → 2399.56] And how long have you been using that system for?
[2399.92 → 2404.32] Well, of course, when we built it, we said, well, this isn't going to last long.
[2404.32 → 2407.80] And I think we turned it off a few months ago.
[2408.38 → 2408.78] Okay.
[2409.10 → 2410.28] It served its purpose.
[2410.64 → 2411.66] It served its purpose.
[2412.02 → 2412.28] Wow.
[2412.98 → 2413.34] Okay.
[2413.64 → 2415.66] Sometimes it's just like have to make it work.
[2415.78 → 2417.72] And that's all the time that you have.
[2417.94 → 2420.20] So it's not like we'll ship it next week.
[2420.30 → 2424.90] It's not an option, you know, especially if like the prime minister says, okay, a week
[2424.90 → 2427.08] from now, those payments will start going out.
[2427.26 → 2428.30] You have to deliver.
[2428.80 → 2429.24] Wow.
[2429.24 → 2429.68] Wow.
[2429.72 → 2430.60] That's amazing.
[2430.96 → 2436.26] Do you imagine that being a success story if you didn't have the platform that you had
[2436.26 → 2436.80] at the time?
[2437.44 → 2440.38] Can you imagine like making it work without it?
[2441.10 → 2445.22] Not in the timeframe and maybe not as secure because we could probably make something like
[2445.22 → 2449.50] that work quickly, but then we would have to build even more stuff.
[2450.00 → 2454.70] And in that timeframe, the less you have to build, the better because you're bound to
[2454.70 → 2457.98] make mistakes and cut corners and everything when you have to do things that quickly.
[2457.98 → 2462.70] So the more things you could use that are hardened and works, the better.
[2463.04 → 2468.74] So I think the security part is probably what we earned or what we got from using the platform.
[2469.76 → 2473.26] How many people were involved in this project in that one week?
[2474.18 → 2477.70] I think we were maybe 20 people.
[2477.84 → 2482.98] I think we had around 10 developers and lawyers and yeah, everything.
[2483.16 → 2483.32] Wow.
[2483.42 → 2483.62] Okay.
[2483.94 → 2484.56] That's amazing.
[2484.56 → 2488.38] And we had, we had, this was one of the things we had to make.
[2488.52 → 2494.34] We had like, I think Norway had a 12 point plan or something and NAV implemented a few
[2494.34 → 2499.42] of them and then other, other parts of the government implemented the rest of them.
[2499.68 → 2503.68] So today, how many developers are working on the platform and using the platform?
[2503.68 → 2506.10] I think you mentioned 400 roughly?
[2506.10 → 2512.04] Well, yeah, we have 400 in-source developers, and then we have a few hundred consultants as well.
[2512.14 → 2516.88] So I think we're up to six, 700 product developers at NAV in big.
[2516.94 → 2520.30] I think you have, I think we have 800 seats on GitHub.
[2521.44 → 2521.84] Wow.
[2522.10 → 2522.98] That's a big org.
[2523.14 → 2523.38] Okay.
[2523.52 → 2523.78] Yeah.
[2524.10 → 2524.44] Okay.
[2525.42 → 2526.74] And how are they structured?
[2527.20 → 2528.44] Like how many teams do you have?
[2528.56 → 2530.10] Or do you even have teams?
[2530.64 → 2531.44] Yeah, we have teams.
[2531.44 → 2534.04] We have, well, it kind of depends.
[2534.22 → 2539.92] I think we have about a hundred actual teams doing product development, and then we have
[2539.92 → 2541.40] some management structures and everything.
[2542.14 → 2545.20] That kind of are teams, but not that kind of teams.
[2545.38 → 2548.90] And as we're that big, we try to organize even more.
[2549.00 → 2554.04] So we have what we call product areas where we kind of divide NAV into, some teams work
[2554.04 → 2557.46] with the work stuff and some people work with the health stuff and some people work with
[2557.46 → 2558.22] the family benefits.
[2558.22 → 2563.84] So we need to split NAV up into smaller parts for it to be comprehensible.
[2564.70 → 2564.80] Okay.
[2565.06 → 2565.36] Okay.
[2565.42 → 2566.10] It makes sense.
[2566.20 → 2569.98] I mean, there's like a lot of people obviously organizing that and being aware of what everyone
[2569.98 → 2572.40] does and, you know, not duplicating efforts.
[2572.62 → 2574.30] Like I did this way, and you did that way.
[2574.38 → 2574.52] Okay.
[2574.52 → 2577.16] We have to reconcile all that good stuff.
[2577.70 → 2580.78] I'm wondering just how big is this platform in terms of resources?
[2580.78 → 2583.54] I'm thinking CPUs, memory, things like that.
[2583.54 → 2591.38] Well, at least our production cluster running in TCP has 50 nodes, which has a total of almost
[2591.38 → 2595.88] 800 virtual CPUs and 1.6 terabytes of memory.
[2596.30 → 2596.68] So it's...
[2596.68 → 2597.52] That is a big cluster.
[2597.86 → 2598.08] Okay.
[2598.26 → 2598.94] And we have...
[2598.94 → 2601.82] Our architecture is one big cluster instead of multiple small ones.
[2601.96 → 2604.20] It's kind of a religious question, I think.
[2604.48 → 2610.12] How are we finding that configuration, having one big cluster versus a couple of smaller ones?
[2610.12 → 2613.10] Well, of course, we do divide this.
[2613.18 → 2616.04] We have namespaces for each team and stuff.
[2616.18 → 2621.04] So the question is probably, do you want to have more separation?
[2621.20 → 2625.70] But I find that it's easier to manage one cluster.
[2625.92 → 2631.18] Although lately, we've been working more on making it possible to make more clusters because
[2631.18 → 2636.40] we're experimenting with providing nice clusters to other government agencies as well in Norway.
[2636.40 → 2643.66] And to be able to do that, we have to automate or making it more robust and more automated
[2643.66 → 2647.44] the process of making new clusters because we want the different other companies to have
[2647.44 → 2649.00] their own clusters and other setups.
[2650.00 → 2654.72] One thing which I remember when we were using Kubernetes, I mean, again, the scale was very
[2654.72 → 2659.80] different, but upgrades sometimes, you know, wouldn't go as smoothly.
[2660.26 → 2661.74] And then what do you do?
[2661.74 → 2665.48] What do you do if you have a single cluster that you do an in-place upgrade that doesn't
[2665.48 → 2666.40] go out as smoothly?
[2667.12 → 2670.14] Like, you know, some component doesn't interact well with other components.
[2670.46 → 2671.38] What do you do then?
[2671.88 → 2673.92] Did you have any such problems in the past?
[2674.70 → 2677.64] We had more problems or maybe not problems.
[2677.72 → 2680.20] It was more work when it was on-prem.
[2680.64 → 2683.82] But this, I think, is one of the good things of the managed service.
[2684.00 → 2685.46] Google does everything for us.
[2685.46 → 2692.68] So either we decide when to do it manually, which is probably for major upgrades or minor
[2692.68 → 2695.86] upgrades, it's just a maintenance window and it kind of happens.
[2696.04 → 2700.76] And I think one of the reasons it's important for us to modernize the applications before
[2700.76 → 2705.86] we migrate to Kubernetes is then this kind of operations becomes easier as well.
[2705.88 → 2710.80] Because if the application is robust enough to be able to handle that and no dice because
[2710.80 → 2715.06] it's moved to another node, then upgrading the cluster is also much easier.
[2715.46 → 2716.34] Okay, I see.
[2716.50 → 2717.04] That makes sense.
[2717.08 → 2721.86] Especially if the applications are stateless, and you can run more than one instance, then
[2721.86 → 2724.42] you know, you have reduced capacity for a while.
[2724.92 → 2730.84] But then if you have like, you know, nice, you're basically draining a node, the application
[2730.84 → 2734.18] knows like to spin extra, you know, instances somewhere else.
[2734.18 → 2734.92] And that's okay.
[2734.92 → 2736.14] It's like minimal disruption.
[2736.72 → 2738.76] It's no different to a scale up in a way.
[2739.20 → 2741.80] And it's no different to a deployment or whatever.
[2741.80 → 2747.88] So I think that's one of the again, the value for this, for our sake is better applications.
[2748.24 → 2750.56] That's the core value of doing all of this.
[2756.84 → 2759.34] So you've been using GCP for a few years now.
[2759.86 → 2762.44] How was it like in practice to use them?
[2762.44 → 2769.78] Well, I think before we started our, or before we went too far into the cloud journey, we
[2769.78 → 2777.30] kind of had a small, we checked the different cloud vendors, at least the three big ones.
[2777.54 → 2780.86] We realized Alibaba isn't for us right now.
[2781.04 → 2784.56] So it's basically Azure AWS or GCP.
[2784.56 → 2791.90] And then we looked a bit at the offerings, and we focused mostly on hosted Kubernetes because
[2791.90 → 2793.66] we knew that was the big thing we had.
[2794.34 → 2800.80] And especially at the time, I think this was 2019, the difference in quality was quite
[2800.80 → 2801.16] big.
[2801.56 → 2803.24] I think they're closer now.
[2803.42 → 2809.94] I probably think it would be a closer, more different or more difficult comparison now.
[2809.94 → 2815.20] But at that time, it felt like Google had by far the best hosted Kubernetes, which kind
[2815.20 → 2820.20] of makes sense because they're the most, they're the biggest, or they're the fathers of Kubernetes.
[2820.72 → 2821.06] So yeah.
[2821.44 → 2821.74] Yeah.
[2822.04 → 2822.76] I know what you mean.
[2823.18 → 2825.78] Do you feel like there's something missing in GCP?
[2826.34 → 2827.66] Something that you would want to have?
[2828.42 → 2831.62] Well, we're quite conservative in what we use.
[2831.88 → 2833.16] So I'm not really sure.
[2833.16 → 2839.68] We, as I said, we want to focus on using open source components or at least the APIs of open
[2839.68 → 2840.08] source components.
[2840.18 → 2845.32] There seems to be a trend where the cloud vendors say, well, this database is Postgres compatible,
[2845.56 → 2847.18] but we won't tell you what's behind.
[2848.18 → 2849.68] And that's kind of okay.
[2849.80 → 2855.74] But as long as we want to use open source APIs and open source components, the number of services
[2855.74 → 2856.86] we use are quite small.
[2857.64 → 2859.44] So I'm not really sure.
[2859.44 → 2864.66] We could probably get, well, Kafka, for instance, we're buying from a different vendor running
[2864.66 → 2871.72] on GCP, but we're buying it from a company called Avon, which is a Finnish company hosting
[2871.72 → 2872.76] open source databases.
[2873.40 → 2874.10] So yeah.
[2874.34 → 2879.30] And that's not really a problem, but we're not that, we're quite conservative in the technologies
[2879.30 → 2879.72] we use.
[2879.78 → 2884.98] So I'm not really sure if I can answer what I need other than more open source, well, Elastic
[2884.98 → 2886.02] and Kafka and everything.
[2886.20 → 2887.70] But Avon gives us that.
[2887.70 → 2889.92] I think that's a good strategy, right?
[2890.14 → 2895.04] The boring technology is what you would want to have considering the stability that you
[2895.04 → 2896.20] require, right?
[2896.26 → 2898.04] Like you don't want to be on the cutting edge.
[2898.12 → 2899.64] You don't want to be trying things out.
[2899.72 → 2905.36] You want to go with a proven, tested, reliable software that is open source, preferably so
[2905.36 → 2909.32] that if you want to, or if you need to make a change, you can contribute that.
[2909.70 → 2914.38] And something that you can trust that will be around for the next 10, 20 years, right?
[2914.44 → 2915.32] Ideally, at least.
[2915.32 → 2920.38] Yeah, because we know startup and basically we're not in a competitive marketplace.
[2921.02 → 2922.36] We are part of the nation.
[2922.72 → 2927.98] So we have systems not running on nice, but mainframe systems that are 40 years old.
[2928.44 → 2933.44] I'm not necessarily sure that the code right now will run for 40 years.
[2933.54 → 2938.26] But the problem we're solving is going to be needed to be solved for many, many decades
[2938.26 → 2938.70] to come.
[2938.70 → 2945.02] So it's better to spend some more time doing it properly now than trying to redo everything
[2945.02 → 2948.00] every 50 years because we hurried when we started.
[2948.96 → 2949.32] That's right.
[2949.76 → 2955.08] So are there any migration plans for the older services that have been around for decades?
[2955.86 → 2956.04] Yeah.
[2956.40 → 2960.74] But then again, we're basically rewriting everything.
[2961.44 → 2962.54] Well, that's not true.
[2962.54 → 2964.62] For some of the systems, we're rewriting them.
[2964.82 → 2969.18] For some of them, we're looking into more different migration strategies.
[2970.70 → 2977.00] Like, I didn't know this was possible before, but you can take COBOL code and translate it
[2977.00 → 2977.58] into Java.
[2978.16 → 2979.06] Really strange.
[2979.20 → 2979.96] I looked at the Java.
[2980.08 → 2982.98] It looks really strange, but it looks like COBOL, but it is Java.
[2982.98 → 2986.84] And then you can run it on normal servers.
[2987.74 → 2992.36] And then you can reduce the cost of the infrastructure quite a lot because mainframes are really expensive
[2992.36 → 2994.50] and Linux servers aren't.
[2995.82 → 3001.14] But of course, there are risks involved because we have systems that have to work, and you're
[3001.14 → 3002.84] making them run on a new technology.
[3003.08 → 3010.60] But our main strategy is to basically recreate the products that run on the old systems, on
[3010.60 → 3016.68] new architecture and build them again with teams and basically try to frame the problems
[3016.68 → 3021.48] with an organization that can live as long as the problems needs to be solved.
[3022.28 → 3029.60] Because I think the biggest thing is to have the teams knowing the domain, not having the
[3029.60 → 3034.74] systems being able to solve it because of the timeframe we're working in.
[3035.32 → 3038.98] And what would a COBOL job ad even look like these days?
[3038.98 → 3040.64] It's like, where would you find those people?
[3041.08 → 3042.92] That would be really, really hard.
[3043.70 → 3043.86] Okay.
[3044.14 → 3048.98] One could imagine that because as far as I understand, there are loads of important stuff
[3048.98 → 3050.68] running on COBOL in the world.
[3051.22 → 3051.40] Yeah.
[3051.56 → 3057.28] And a lot of the people who wrote them and know COBOL is getting old and ready for retirement.
[3057.84 → 3063.82] So at some point, I presume it's going to be very lucrative to learn COBOL because not
[3063.82 → 3067.00] everybody has the opportunities we have to modernize.
[3067.00 → 3068.68] So yeah, that's true.
[3069.02 → 3069.80] That's a good point.
[3069.96 → 3070.16] Okay.
[3070.74 → 3072.04] COBOL owned Kubernetes.
[3072.46 → 3074.42] That is a startup idea right there.
[3075.16 → 3075.48] Yeah.
[3076.34 → 3081.70] Well, I've always, when we started introducing Kubernetes, I think I had the argument at least
[3081.70 → 3086.40] five different times of how Kubernetes is basically exactly like the mainframe.
[3086.40 → 3091.64] And there are obvious similarities, but it's also the clear differences.
[3092.20 → 3092.30] Okay.
[3092.84 → 3095.32] What does a good day for Auden look like?
[3096.44 → 3098.20] Yeah, that's a perfect question.
[3098.84 → 3100.28] I had a perfect summer holiday.
[3101.54 → 3101.76] Okay.
[3102.14 → 3102.58] No.
[3103.54 → 3105.54] The funniest thing in the world is to code.
[3105.54 → 3106.30] Mm-hmm.
[3106.64 → 3112.92] But then again, whenever I'm coding, I realize there's, at least most of the time, there's
[3112.92 → 3116.74] bigger problems that need to be solved to make it fun to code.
[3117.42 → 3123.88] And I spent a lot of my time trying to fix the big problems and then hoping at some point
[3123.88 → 3125.04] we can code again.
[3126.04 → 3128.24] But of course, it's also important to code.
[3128.24 → 3134.76] So I try to, or me and Tries and a few other people, we try to code a bit every week.
[3135.58 → 3140.70] And then the important thing is to make, find the things you can make that aren't important.
[3140.82 → 3146.26] That's valuable, but not important because sometimes we spend, we haven't got the time
[3146.26 → 3146.84] to deliver.
[3147.44 → 3151.82] We can't promise when anything will be finished, but it's fun to make things that people like.
[3152.32 → 3154.94] So trying to find kind of the small things.
[3154.94 → 3161.16] Right now we are, we are working on trying to make the take the application configuration
[3161.16 → 3167.54] in nice, the nice YAML file, which basically says what applications do you need access to
[3167.54 → 3172.54] and what applications have access to you and what Kafka topics do you need to write or read
[3172.54 → 3178.74] access to and take this information out of the cluster and make an make a visualization
[3178.74 → 3181.12] of all the applications and who talks to whom.
[3181.12 → 3183.40] And that's fun.
[3183.50 → 3186.60] And I think it's going to be useful, but no one's asked for it.
[3186.62 → 3188.88] So no one, no one can tell us we're late.
[3189.32 → 3193.32] Well, as you know, a lot of the time it's the ideas or the things that no one asks for
[3193.32 → 3195.72] that's proved to be the game changing ones.
[3195.72 → 3199.82] Like, you know, no one needs this until like, how did we live without it?
[3199.90 → 3202.26] Like we, we need, like everyone needs that.
[3202.26 → 3203.88] So, and yeah.
[3204.32 → 3210.20] And just the other thing that's part of a perfect day is when we managed to get all the
[3210.20 → 3215.00] other disciplines of NAV to understand that we learn something that's important to them,
[3215.04 → 3217.16] the lawyers or the management or whatever.
[3217.16 → 3222.52] And they also understand a bit more about what, what's important to do.
[3222.84 → 3226.44] What's the important frameworks to have in place to do modern software development.
[3226.72 → 3231.30] That's not necessarily the same as running other parts of the government because the soft part of
[3231.30 → 3233.82] software makes everything a bit different.
[3234.44 → 3235.42] Yeah, for sure.
[3235.68 → 3239.56] So talking about frameworks, I know that you mentioned security a few times.
[3239.76 → 3241.64] I've seen a blog post about Salsa.
[3241.64 → 3248.38] Where do you stand on the whole supply chain security, the Salsa model, things like that?
[3248.76 → 3253.28] Well, I think it's, at least for us, it was an important next step.
[3253.46 → 3257.78] I think you're kind of building, building blocks from kind of the basic stuff.
[3257.86 → 3263.94] And then you go further up, and you realize there's always more problems to solve and to be able to,
[3264.66 → 3268.08] when we open source and when we trust the teams as much as we do,
[3268.08 → 3275.14] it's important to make the systems that can basically prove that the trust we've given them was okay.
[3275.48 → 3281.06] That we can say, well, we can see that this happened from that team, and we know that this is okay.
[3281.06 → 3286.32] And for instance, when Log4Shell came, and although we managed to get a handle on it,
[3286.48 → 3291.12] there was obvious that we could have responded even quicker by saying, well,
[3291.22 → 3293.42] what applications are affected by this?
[3293.42 → 3299.78] And to automate that, this kind of feels like the next big thing or the next thing, at least.
[3299.92 → 3301.38] One of the next things.
[3301.82 → 3303.22] There's always multiple things.
[3304.42 → 3309.82] So is there something more significant than this that you are working on in the context of NAV?
[3310.02 → 3311.88] Something that is important to you?
[3311.88 → 3319.12] Well, the one thing I mentioned a bit, trying to see if we can make nice and platform for more than NAV.
[3319.92 → 3327.00] Because I think we're one of the biggest organizations in Norway, and we have 25 people working on platforms.
[3327.18 → 3330.94] And some of the smaller government agencies maybe have 10 developers.
[3331.38 → 3336.94] And there's no reason to believe that they have the capacity to make as good a platform
[3336.94 → 3341.06] or think through enough of the security aspect as good as we do.
[3341.06 → 3348.22] So if you can manage to make that possible for them and help them as well, I think that's perfect for Norway.
[3349.06 → 3352.42] I know the UK had something similar with Go.uk.
[3353.02 → 3356.16] They had this platform as a service.
[3356.34 → 3361.16] I think they had almost 30 different organizations running on this central platform.
[3362.08 → 3362.80] Yes, that's right.
[3363.22 → 3364.52] Alpha Gov, I remember that.
[3364.88 → 3369.34] I haven't checked it recently to see where they are at now, but I remember that.
[3369.34 → 3370.86] That was a very interesting model.
[3371.04 → 3373.70] I know that the US government was doing something similar.
[3374.24 → 3377.18] And that was like a reference at the time.
[3377.34 → 3379.50] That was many years ago, five, six, maybe more.
[3380.02 → 3380.30] Okay.
[3380.82 → 3383.18] Was that by any chance an inspiration for NAV?
[3383.46 → 3388.24] Well, one thing we really learned from Go.uk was the open sourcing.
[3388.24 → 3395.76] I remember reading the principles on open sourcing from Go.uk and basically, well, we started translating it.
[3395.86 → 3399.70] We realized we could just link to it and say, we agree totally with this.
[3399.88 → 3399.94] Yeah.
[3399.94 → 3411.34] So, and basically because of that, I think we've been, we open source almost all the code we write, not just the application platform, but everything we write at NAV is open.
[3411.50 → 3420.64] Almost everything is open sourced, except for like fraud detection and some experiments with the laws that aren't finished yet.
[3420.76 → 3423.68] And of course, some security aspects like passwords and everything.
[3423.68 → 3426.34] Most of the code we write now is open source.
[3427.02 → 3431.22] Do you find that other people contribute to that or comment?
[3431.50 → 3435.42] Like what is the interaction with that open source code from the public?
[3436.02 → 3443.12] Most of the interaction and most of the use of the open source platform is like kind of obscure libraries.
[3443.12 → 3452.36] So, we have one small, I think, Kubernetes operator that talks to Azure AD, which is used by multiple companies.
[3453.10 → 3463.28] And then you have a Kafka testing library that someone used, but it turns out that there aren't much of a market for open source unemployment benefit systems, for instance.
[3463.96 → 3464.28] Right.
[3464.42 → 3465.24] I see what you mean.
[3465.40 → 3465.56] Okay.
[3465.76 → 3465.94] Okay.
[3466.54 → 3467.88] So, not much competition there.
[3468.60 → 3468.74] No.
[3468.88 → 3469.14] Okay.
[3469.46 → 3472.74] It's more about openness than about people.
[3472.74 → 3478.92] And we think that people should, we code or implement the laws that are public.
[3479.14 → 3481.38] So, the code should be open and public as well.
[3481.80 → 3481.96] Yeah.
[3482.14 → 3482.64] That's right.
[3483.00 → 3486.20] Do you find it helps when it comes to hiring, when it comes to recruiting?
[3486.76 → 3486.92] Yeah.
[3487.40 → 3487.84] Absolutely.
[3488.20 → 3494.36] I think that's, it feels like a value proposition that software developers really like that we say, well, we do it.
[3494.52 → 3495.58] We code open.
[3495.84 → 3498.12] You're attracting a certain type of developer.
[3498.48 → 3499.96] I think it's very good to have.
[3500.22 → 3500.48] Okay.
[3500.76 → 3500.98] Okay.
[3500.98 → 3506.90] Are there any talks that you or someone else from your team gave recently that you would like us to link in the show notes?
[3506.90 → 3517.94] Well, Truly, and I was at Icon in London in May talking about how we do, about NICE and how we do technical governance, basically.
[3518.76 → 3522.40] That's probably the best one from an international audience.
[3522.76 → 3523.90] Is it public, the talk?
[3524.30 → 3525.22] I think so.
[3526.18 → 3527.58] There's Info and Icon.
[3527.58 → 3533.12] And if it isn't public, I think it's going to be public at some point, but I'm not entirely sure when.
[3533.20 → 3533.46] Okay.
[3534.06 → 3534.88] I'll check it out.
[3535.14 → 3535.36] Okay.
[3535.38 → 3535.90] I'll check it out.
[3535.96 → 3536.10] Okay.
[3536.90 → 3540.66] I know that you have a very good blog, the NICE.io blog.
[3540.78 → 3542.26] There's a post on Sales.
[3542.26 → 3543.20] There are a few others.
[3543.66 → 3545.40] I think you mentioned service meshes.
[3545.68 → 3547.02] There's a post there too.
[3547.40 → 3548.04] I really like it.
[3548.16 → 3551.58] I mean, there's not too many posts there, so it doesn't feel overwhelming.
[3552.12 → 3554.98] But what is there, it's like very compressed.
[3555.24 → 3555.68] It's very good.
[3555.72 → 3559.72] Like the learnings from this or this is what we're thinking about that.
[3559.84 → 3562.46] And there's not a lot, but it's very valuable.
[3562.64 → 3564.70] I found it just like browsing through it.
[3565.00 → 3568.28] The newest post is about Elm as a front-end platform.
[3568.28 → 3570.96] So kind of the application front-end framework.
[3571.14 → 3574.62] So the application platform concept is kind of a bit stretched now.
[3575.28 → 3575.76] Okay.
[3575.76 → 3580.60] So as we are preparing to wrap this conversation up,
[3581.16 → 3586.20] is there a takeaway that you'd like our listeners to have from today?
[3586.86 → 3591.46] I think for big organizations, I think an application platform is really valuable.
[3591.46 → 3596.38] And I think the main thing to think about in the make application platforms
[3596.38 → 3600.46] is to treat the internal developers of your company as users
[3600.46 → 3604.78] and basically make an application platform the same way as you make an application.
[3604.78 → 3610.44] Do experiments and think of the product and try to figure out
[3610.44 → 3614.60] how can you solve the problems of your users and then solve them.
[3615.22 → 3615.46] Yeah.
[3615.82 → 3616.88] And write good docs.
[3617.18 → 3619.50] Like the docs, NACE.io, they're really, perfect.
[3619.56 → 3620.86] There's so much good stuff there.
[3621.50 → 3622.28] I really like that.
[3622.72 → 3622.98] Okay.
[3622.98 → 3625.52] I haven't written any of it because I'm not a good writer.
[3625.80 → 3627.78] I think I have one chapter somewhere in there,
[3627.82 → 3629.12] but most of it is written by other people.
[3629.24 → 3630.06] But I agree.
[3630.14 → 3630.76] It's perfect.
[3631.26 → 3631.54] All right.
[3631.66 → 3635.40] Any shout-outs that you want to give to anyone from NICE, from NAV,
[3635.90 → 3638.96] people that you work with that, you know, are doing amazing work
[3638.96 → 3640.38] and you want to give a shout-out to them?
[3640.38 → 3645.58] No, maybe I think the shout-outs could maybe go to our NAV,
[3645.74 → 3649.44] A-I-K-T GitHub profile,
[3649.58 → 3652.90] where you see all the other open source code with not just NICE.
[3653.04 → 3654.48] I think that's a good place to start.
[3654.98 → 3655.24] Okay.
[3655.94 → 3656.34] Excellent.
[3657.00 → 3657.40] All right, Open.
[3657.82 → 3659.26] Well, I had a lot of fun today.
[3659.40 → 3662.12] Thank you very much for sharing so many amazing things with us
[3662.12 → 3663.72] and I'm looking forward to next time.
[3663.82 → 3664.12] Thank you.
[3664.46 → 3664.98] Thank you.
[3664.98 → 3671.06] Thank you for tuning into another episode of Ship It.
[3671.42 → 3676.22] Check out our other podcasts for developers at changelog.com slash master.
[3676.80 → 3681.40] You can connect with like-minded developers via changelog.com slash community.
[3681.84 → 3685.72] Thank you, Vastly, for the worldwide low-latency changelog.com.
[3685.72 → 3689.22] Our listeners love those blazing-fast MP3s.
[3689.78 → 3694.46] The Firecracker VMs and that WireGuard integration are really sweet, flooded IO.
[3694.98 → 3695.90] That's it for this week.
[3696.12 → 3696.96] See you all next week,
[3697.16 → 3700.16] when we'll be talking about developer experience infrastructure
[3700.16 → 3702.02] with Kenneth Greenberg.
[3702.02 → 3712.36] Gang on.
[3712.36 → 3713.40] Gang on.
