[0.08 → 6.02] Welcome to another episode of Ship It. I'm Gerhard Lasso, and today I'm chatting with Romano Roth,
[6.40 → 13.62] head of DevOps at Rule, a company founded by Gerhard Rule in 1968. They help companies
[13.62 → 20.82] all over the world build, ship and run anything from factory robots to AI assistants in complex
[20.82 → 26.02] regulatory environments and even medical devices that perform autonomous robotic surgery.
[26.02 → 30.74] Besides leading a team of 30 software engineers that specialize in operations,
[31.22 → 38.28] infrastructure and cloud, Romano is one of the organizers of DevOps at Rule and also the DevOps
[38.28 → 45.30] meetup group, which is how we met in 2019. Having started his career as a .NET developer back in 2002,
[45.88 → 51.76] Romano had his fair share of dev and ops challenges, and he always enjoys seeing real business value
[51.76 → 58.74] delivered continuously in an automated way. In recent years, his perspectives broadened and now
[58.74 → 64.76] he sees DevOps challenges and wins across many companies. If you are curious about what good
[64.76 → 69.78] DevOps looks like and what are the real challenges, then Romano has some good insights for you.
[70.14 → 75.96] Big thanks to our partners Vastly, Launch Darkly and Linde. Thank you for the great band with Vastly.
[75.96 → 82.30] You can learn more at Fastly.com, ship new features with confidence by getting your feature flags powered
[82.30 → 89.68] by LaunchDarkly.com, and thank you Linde for keeping our Kubernetes fast and simple. You, too, can run our
[89.68 → 94.58] infrastructure as we do via Linode.com forward slash changelog.
[94.58 → 107.96] This episode is brought to you by Honeycomb. Honeycomb is built on the belief that there's a more
[107.96 → 113.04] efficient way to understand exactly what is happening in production right now. When production
[113.04 → 117.96] is running slow, it's hard to know exactly where problems originate. Is it your application code,
[117.96 → 123.66] your users, or the underlying systems? Teams who don't use Honeycomb scroll through endless dashboards
[123.66 → 129.08] guessing at what they mean. They deal with alert floods, guessing which ones matter, and go from tool
[129.08 → 133.80] to tool, guessing at how the puzzle pieces all fit together. It's this context switching and tool
[133.80 → 138.80] sprawl that are slowly killing your teams and your business. With Honeycomb, you get a fast, unified,
[139.12 → 144.28] and clear understanding of the one thing driving your business, production. Honeycomb quickly shows you the
[144.28 → 149.82] correct source of issues, discover hidden problems, even in the most complex stacks, understand why your app
[149.82 → 156.06] feels slow to only some users. With Honeycomb, you guess less and no more. Join the swarm and try
[156.06 → 162.38] Honeycomb free today at honeycomb.io slash changelog. Again, honeycomb.io slash changelog.
[162.38 → 178.84] We are going to ship in 3, 2, 1.
[178.84 → 199.62] So two years ago in 2019, I gave a talk about making your system observable.
[200.36 → 202.96] And that was DevOps Meet Albuterol.
[203.50 → 205.58] And I'll add a link in the show notes.
[205.58 → 209.32] And Romano was the organizer, and he put up quite the events.
[209.40 → 210.58] I'd like you to thank you for that.
[210.66 → 211.76] It was a great experience.
[212.14 → 212.52] Welcome.
[212.90 → 217.68] And this year, my intention was to join DevOps Days Zurich, but timing wasn't right.
[217.68 → 219.38] So I couldn't make it work.
[219.84 → 222.00] But again, Romano was one of the organizers.
[222.44 → 224.60] And I'm wondering, how did the event go?
[224.86 → 227.04] Oh, it was absolutely great.
[227.32 → 230.62] So it was in the beginning of September when we had that event.
[230.62 → 236.02] It was also one of the first events which we could do in person.
[236.60 → 238.30] And that was amazing.
[239.00 → 249.38] The only thing was it was quite frustrating in the beginning to organize all of that because you need to look at the COVID numbers.
[249.58 → 253.92] You needed to create a concept for COVID.
[254.34 → 256.14] And that was quite stressful.
[256.70 → 260.26] But in the end, we could manage to do the event.
[260.26 → 263.12] We had a COVID security concept.
[263.82 → 267.42] Everybody needed to line up, needed to have the certificates.
[268.40 → 273.68] And it also worked with all the people which were coming from around the world.
[273.80 → 278.42] We had people from the U.S. coming and also from Israel.
[279.26 → 281.30] And everything worked well.
[281.50 → 283.96] We had 250 people in there.
[284.36 → 286.64] And it was absolutely great.
[286.64 → 289.14] And this was a two-day event.
[289.32 → 292.98] So it wasn't just like one day, which makes things slightly more complicated, right?
[293.32 → 293.44] Yeah.
[293.64 → 293.90] Okay.
[294.30 → 295.56] How many talks did you have?
[295.72 → 297.70] I don't know the correct number.
[298.02 → 300.90] But what we have is always a keynote.
[301.20 → 303.42] Then we had a set of talks.
[303.42 → 305.88] I think it was three or four talks.
[305.88 → 310.24] And then in the afternoon, we had the Ignite talks.
[310.56 → 314.76] So that's the five-minute talks which we have.
[315.18 → 318.66] And then we usually have workshops and open spaces.
[318.92 → 321.64] And that's over the whole two days.
[322.12 → 326.86] So I would say roughly 20 talks altogether.
[326.86 → 328.76] And was it single track?
[328.88 → 330.12] Always single track, yeah.
[330.28 → 330.58] Okay.
[330.70 → 330.92] Okay.
[330.92 → 331.48] That's nice.
[331.58 → 331.98] That's nice.
[332.04 → 334.80] Because you just have to sit there and enjoy, right?
[334.82 → 338.10] Like you don't have to change rooms, meeting rooms.
[338.52 → 338.70] Yeah.
[338.74 → 338.96] Okay.
[339.26 → 340.36] Which was your favourite talk?
[340.42 → 340.90] Do you remember?
[341.32 → 342.12] I'm sure there were many.
[342.30 → 344.02] But any one talk that stood out?
[344.02 → 344.50] Yeah.
[344.66 → 348.74] I liked very much the talk about, what was it?
[348.88 → 351.94] Better, sooner, happier from Jonathan Smart.
[352.48 → 354.24] I liked that quite a lot.
[354.36 → 357.96] Because during the talk, he asked always questions.
[358.32 → 361.92] And one of the questions was, are you doing IT transformation?
[362.44 → 363.58] Please, hands up.
[363.78 → 366.24] And everybody was putting their hands up.
[366.28 → 367.62] And he said, don't.
[368.84 → 370.26] And that was absolutely amazing.
[370.58 → 372.74] And he continued with these questions.
[372.74 → 376.20] For example, are you using a scaled HL framework?
[376.84 → 377.28] Don't.
[378.24 → 379.28] And so on and so on.
[379.58 → 381.32] And that was quite good.
[381.46 → 388.02] Because he was going back to what really matters when you are doing an HL transformation.
[388.54 → 389.98] And that was cool stuff.
[390.38 → 392.96] Like, I want to ask you what that is.
[393.26 → 397.28] If you don't want to spoil that talk for you, you can skip maybe a few minutes.
[397.68 → 398.40] So what is it?
[399.62 → 400.60] Can you tell us?
[400.92 → 401.76] Yeah, sure, sure.
[401.76 → 405.68] The thing is, you really, really need to focus on the people.
[405.68 → 410.24] You don't need to focus only on doing the transformation.
[410.42 → 412.12] Because you want to do a transformation.
[412.38 → 417.12] It is more focusing on what do you really want to achieve.
[417.64 → 420.94] And focus on changing these things.
[420.94 → 425.74] And that's also why he said, don't use a scaled HL framework.
[425.74 → 432.76] Because there you focus on the process and on changing terminology.
[433.16 → 437.20] It is more shifting to what do you really want to achieve.
[437.62 → 439.72] Identify really what you want.
[439.98 → 441.84] And then changing these things.
[441.84 → 447.04] Not having that huge IT transformation that many people are doing.
[447.04 → 451.40] So really focusing on what really matters for you.
[451.40 → 452.96] I think I seem to remember.
[453.36 → 453.68] Well, no.
[453.98 → 459.00] I remember that in the Agile Manifesto, as we initially captured, one of the core principles
[459.00 → 461.18] were people over processes.
[461.80 → 462.14] Exactly.
[462.46 → 462.70] Okay.
[462.80 → 463.72] So that's what this is.
[463.78 → 463.98] Okay.
[464.10 → 464.80] That makes sense.
[465.62 → 467.60] So that was an interesting one.
[467.78 → 472.42] Now, I know that all the talks are available online as videos to catch up on demand.
[472.60 → 474.48] Again, I'll add a link in the show notes.
[474.48 → 475.90] I've also seen the pictures.
[476.10 → 481.08] So if you want to see how this meetup was, you can go and look at those pictures.
[481.42 → 483.72] I'm wondering, this is a yearly thing, right?
[483.78 → 485.32] So next year, it's going to happen again.
[485.52 → 485.70] Yeah.
[485.78 → 487.48] Also in person, I'm imagining.
[487.86 → 488.28] Exactly.
[488.40 → 488.76] Exactly.
[489.00 → 493.80] I think the next one will be on the 31st of May.
[494.48 → 497.08] And we will do it again in person.
[497.50 → 502.92] And it will be again in Zurich or in Winterthur, as we call it.
[502.92 → 505.24] And in the same building.
[505.62 → 505.76] Okay.
[505.98 → 509.18] When do you open Call for Papers?
[509.30 → 511.54] When can people start submitting their talk proposals?
[512.58 → 513.84] Very good question.
[513.98 → 514.70] We don't know yet.
[514.74 → 521.52] We are currently closing off all the stuff which we need to do for the past conference.
[522.10 → 529.54] But my opinion, I think it will be perhaps December, or it will be January round where we
[529.54 → 531.62] will open up the Call for Papers.
[531.62 → 531.86] When they open up.
[532.10 → 532.22] Yeah.
[532.22 → 532.62] Okay.
[532.92 → 540.54] Are there any specific topics that you'd like to see more of in the next DevOps Days conference?
[540.94 → 541.62] What do you call it?
[541.66 → 541.92] Conference?
[542.28 → 542.52] Summit?
[542.80 → 543.22] Conference.
[543.48 → 543.76] Conference.
[543.78 → 544.02] Conference.
[544.44 → 544.64] Yeah.
[544.92 → 545.30] Yeah.
[545.76 → 547.20] Don't come with the Kubernetes.
[548.10 → 548.58] Okay.
[549.10 → 550.06] No Kubernetes.
[550.52 → 550.68] No.
[551.06 → 551.62] All good.
[551.74 → 551.96] All good.
[552.62 → 556.10] We have so many proposals on Kubernetes usually.
[556.10 → 556.72] No.
[556.72 → 556.74] No.
[556.92 → 563.56] What I really liked about the past conference or what we are focusing on is diversity.
[563.56 → 567.18] And not only diversity, women or men.
[567.18 → 571.24] It's all about diversity also in different mindsets.
[571.24 → 573.86] That's why we also have different talks.
[573.86 → 576.90] And that's what I also like to see.
[577.70 → 580.36] Big diversity on different topics.
[580.36 → 582.36] We had talks on culture.
[582.36 → 590.56] We had talks on, for example, the role of UX in DevOps, which is also quite a special topic,
[590.56 → 593.24] but it's an important topic.
[593.24 → 594.54] And that's my wish.
[594.70 → 603.40] I have that diversity on topics and not only focusing, for example, on technology or only on the process.
[603.72 → 606.70] It's more also on the people side.
[606.98 → 607.42] I love that.
[607.56 → 612.62] I mean, that really speaks to my heart because we keep forgetting its human beings, fallible,
[613.00 → 615.76] that get easily bored, and they keep chasing shiny new things.
[616.18 → 620.56] And granted, Kubernetes may not be the shiny new thing anymore, but then it's comfort, right?
[620.60 → 621.56] People are comfortable with that.
[621.56 → 625.06] So, yeah, there's a lot there.
[625.50 → 631.08] Now, I know that you're into DevOps, like big time into DevOps, but I don't know why.
[631.38 → 632.48] Why are you into DevOps?
[633.98 → 635.12] Very good point.
[635.60 → 639.74] When I started my career, I was a .NET developer.
[640.46 → 643.32] And this was back in 2002.
[644.34 → 650.04] And we were doing their development of application of rich client applications.
[650.04 → 658.88] And one of the things also in the early times which struck me is how can I ensure the quality of what I'm doing?
[659.40 → 665.78] And yeah, of course, you could do testing also there, but it was not so automated.
[665.78 → 669.84] And I was always a little bit lazy and I wanted to automate things.
[669.84 → 678.06] So, I went into this area where we were starting automating the tests and then also the deployment.
[678.24 → 681.20] So, I went into continuous integration, continuous deployment.
[681.20 → 685.28] And the applications were getting bigger and distributed.
[685.64 → 687.64] I was becoming an architect.
[688.14 → 693.34] And slowly, I moved into the direction of these continuous delivery pipelines.
[694.06 → 708.76] And when the whole DevOps movement started, I jumped on that because this was really one of my hard topics where I wanted to create these pipelines to continuously deliver value to the customer.
[708.76 → 721.68] So, my understanding is that you were passionate about how value gets delivered, which got you into DevOps, which seems to have made that almost like at the centre of its activity.
[722.02 → 727.90] How do you move this code from a repository into customer hands, wherever that may be?
[728.12 → 732.14] And there's like a lot of automation because you can do it manually, but there is a better way.
[732.36 → 733.32] And automating that.
[733.52 → 734.22] Okay, interesting.
[734.62 → 737.04] Which was your first CI-CD system that you used?
[737.14 → 737.52] Do you remember?
[737.52 → 746.38] The absolute first CI-CD system was actually a command line that I used.
[746.60 → 747.70] Yeah, definitely.
[748.02 → 753.76] But I think what you want to ask is more the first product that I used.
[753.90 → 757.34] And this was, I think it was the team foundation server.
[757.70 → 761.82] So, when you mentioned the command line, did you mean like sync or FTP or SCP?
[762.20 → 764.04] What exactly did you do on the command line?
[764.28 → 765.38] Different things.
[765.38 → 774.38] For example, I had some scripts, mount line scripts, which I used to just compile or execute the test.
[774.38 → 782.28] So, my first build system was a batch file on my local computer, which I just could double-click.
[782.74 → 785.24] And then it executed the tests.
[785.24 → 789.98] It compiled my code, and it says, yeah, everything is okay.
[789.98 → 792.60] And there is the deployable artifact.
[793.10 → 802.38] And when it went into the distributed system, I usually added also an FTP where I just could move the code to the server.
[802.58 → 804.88] And then it was on the server.
[805.10 → 805.38] Okay.
[805.58 → 806.70] What about today?
[806.84 → 807.60] What do you use today?
[807.60 → 811.48] Today, I use quite a variety of systems.
[811.92 → 816.42] One of the products which I love is still Team City.
[816.62 → 820.58] I love that quite a lot because you can do a lot of configuration.
[820.96 → 827.48] I usually use Team City together with Octopus Deploy, which I also love as a tool.
[827.48 → 836.60] But I see quite a strong movement at the moment into the direction of platforms like GitHub and GitLab.
[837.04 → 853.90] So, at the moment, when I look at the clients which I'm working for, they are moving into this direction away from Jenkins, Octopus Deploy, Team City, and all the Circle CI and into the direction of GitLab and GitHub.
[853.90 → 855.92] So, these are now the big players.
[856.60 → 859.78] Customers are going into this direction because there you have a platform.
[860.30 → 867.06] Everything is there, and you don't need to deal with different tools which you need to stick together.
[867.50 → 868.28] That's interesting.
[868.72 → 878.32] So, I think that now we are starting to discover another side of Romano because we know that you can put up a conference really well as a meetup.
[878.44 → 879.50] But you also do other things.
[879.50 → 883.90] So, when you don't organize various DevOps-related events, what do you do?
[883.96 → 884.94] Because you mentioned customers.
[885.06 → 887.32] There's more to it, right, than organizing events.
[887.52 → 888.72] What exactly do you do?
[889.78 → 890.08] Yeah.
[890.32 → 893.18] I'm the head of DevOps at Kyle.
[893.72 → 898.66] And there I have a whole unit of DevOps engineers and DevOps consultants.
[899.32 → 902.50] And I bring DevOps forward at Kyle.
[902.50 → 905.28] So, there is one side at Kyle.
[905.56 → 914.40] I do a lot of trainings of people in the direction of DevOps so that we can deliver better quality, better software to our clients.
[914.88 → 918.10] And on the other side, I'm also in client projects.
[918.76 → 928.72] And there I are usually in projects where we are doing an IT or an HR transformation or where we are doing a DevOps transformation.
[928.72 → 933.76] And I consult their different clients into this direction.
[933.76 → 936.48] And I also educate their people.
[936.84 → 936.92] Okay.
[937.20 → 938.62] So, how large is your team?
[938.72 → 944.58] The team is roughly, at the moment, I think, 31 people at Kyle.
[944.72 → 947.08] But this is only in Switzerland.
[947.32 → 950.98] Of course, there are other people around the world which are also doing DevOps.
[950.98 → 951.48] Yeah.
[951.84 → 961.22] So, your team is 31 DevOps engineers that work with various customers that you consult, help with DevOps-related projects.
[961.46 → 962.70] How many projects do you have?
[962.92 → 963.52] Quite a lot.
[963.74 → 971.18] And the different people which are in my team, they work for different customers and also with different engineers.
[971.18 → 979.42] So, it is not only that these projects are under my responsibility, they are under different people's responsibility.
[979.84 → 984.04] But my team members are working in these projects.
[984.58 → 984.84] Okay.
[985.28 → 994.24] So, I'm thinking that you must have seen many projects this year that went well, as well as many projects which didn't go so well.
[994.50 → 997.24] Is it something that you can talk about without giving any names?
[997.24 → 1000.74] We don't have to give any names, but things that worked well, things that didn't go so well.
[1000.94 → 1001.70] What do you think about that?
[1001.94 → 1002.56] Yeah, sure.
[1002.86 → 1013.24] When we think about things that went well, there is, especially at one customer where we are creating a whole transformation.
[1014.04 → 1019.26] And what we did there is they are going through an agile transformation.
[1020.20 → 1025.58] And one of the things you need to have for an agile transformation is technical fundament.
[1025.58 → 1029.42] So, that you can do this transformation.
[1030.42 → 1033.72] And we were thinking how we can do that.
[1033.98 → 1043.10] And we built up an agile release train for that with different teams in there, which were focusing on different aspects of this transformation.
[1043.10 → 1048.14] There is one team which is more focusing on the governance part.
[1048.26 → 1055.46] One team which is more focusing on, for example, the continuous integration and continuous delivery pipeline.
[1055.66 → 1060.12] And one team which is more focusing on the containerization.
[1060.52 → 1061.68] So, it's about that.
[1062.16 → 1064.32] And that worked very well.
[1064.60 → 1068.18] We are now in the fourth PI, which we are doing.
[1068.18 → 1070.44] And that's quite cool.
[1070.82 → 1074.84] And we had also a very, very, very good learning in there.
[1075.06 → 1078.70] From the beginning, we identified who the customer is.
[1078.78 → 1082.28] And we said, we want to deliver to this customer.
[1082.60 → 1090.56] And we said, okay, everything what we are doing must be something that the customer can use.
[1090.56 → 1091.88] And we started with that.
[1092.62 → 1101.92] The thing was that in the first sprints, which we did, we saw that we were delivering to the customer, but only to the customer.
[1102.22 → 1103.94] But the customer was not using it.
[1104.14 → 1105.12] So, we changed that.
[1105.26 → 1106.38] And we said, no, no.
[1106.62 → 1110.08] From now on, the customer needs to use it.
[1110.16 → 1115.64] So, we put that in the definition of done, that the customer needs to take that over.
[1115.64 → 1124.04] But that was also not enough because we also had our system demos or our review meetings where we showed that.
[1124.34 → 1125.82] And that was not enough.
[1126.16 → 1133.16] And now we said, okay, when we are demoing stuff, not our people are demoing it.
[1133.44 → 1138.14] The customer needs to do the demonstration how he uses it.
[1138.60 → 1141.90] And that's a very strong thing you can do.
[1141.90 → 1145.48] So, always deliver directly to the customer.
[1145.70 → 1150.24] Let the customer show what you have delivered and how he is using it.
[1150.48 → 1155.26] And that would also be one of my recommendations to do in the future.
[1155.26 → 1172.16] What's going on, shippers?
[1172.34 → 1177.98] Our friends at Vastly are running an amazing promo with massive savings on Compute at Edge.
[1178.16 → 1182.46] They're inviting our entire listener base to move latency-sensitive workloads to the edge.
[1182.46 → 1188.44] Compute at Edge free for three months, plus up to $100,000 a month in credit for an additional six months.
[1188.94 → 1196.90] This is a limited-time offer, so head to Fastly.com slash podcast as soon as you can to check it out and get all the details.
[1197.34 → 1198.26] Here's the TLDR.
[1198.80 → 1205.18] Vastly's Edge Cloud Network and modern approach to serverless computing allows you to deploy and run complex logic at the edge
[1205.18 → 1209.16] with unparalleled security and blazing fast computational speed.
[1209.16 → 1216.72] Scale instantly and globally, reduce origin load, get real-time observability, and get seamless integration with your existing tech stack.
[1217.08 → 1220.96] Head to Fastly.com slash podcast to get Compute at Edge free for three months,
[1221.12 → 1224.60] plus up to $100,000 a month in credit for an additional six months.
[1225.08 → 1227.46] Once again, Fastly.com slash podcast.
[1227.56 → 1229.56] Fastly.com slash podcast.
[1229.56 → 1231.56] Fastly.com slash podcast.
[1231.56 → 1233.56] Fastly.com slash podcast.
[1233.56 → 1235.56] Fastly.com slash podcast.
[1235.56 → 1237.56] Fastly.com slash podcast.
[1237.56 → 1238.56] Fastly.com slash podcast.
[1238.56 → 1253.70] So when it comes to the biggest obstacles, the biggest challenges to driving DevOps transformations or successful DevOps projects,
[1254.32 → 1254.96] what are they?
[1255.06 → 1256.82] What did you come across in your experience, Romano?
[1256.82 → 1264.02] So one of the biggest obstacles that is out there is actually the middle management.
[1264.02 → 1271.10] What you can see is you have a lot of companies which are organized in different units.
[1271.58 → 1274.96] And these units, they have goals.
[1275.20 → 1277.98] And of course, there is a head of this unit.
[1278.30 → 1283.62] And he has built that unit up, and he is chasing his goals.
[1284.36 → 1291.00] But one of the problems that we usually see is that there is a lot of misalignment between these units,
[1291.00 → 1293.62] or you can also call it silos.
[1293.62 → 1298.16] So now with the HR transformation, you or with the DevOps transformation,
[1298.36 → 1303.64] you are starting to align the people around the value stream.
[1304.14 → 1306.28] And you bring people together.
[1306.86 → 1315.76] And this means that some of these heads of these units, they are losing power.
[1315.76 → 1318.56] And they know that.
[1318.76 → 1319.60] They see that.
[1320.18 → 1324.02] And this is something they don't want to have.
[1324.38 → 1326.80] So they want to still be in charge.
[1326.90 → 1328.36] They want to have their budget.
[1328.88 → 1333.32] They want to say how things are done.
[1334.10 → 1336.28] And that's a big challenge.
[1336.28 → 1340.78] And I can also fully understand these people.
[1341.44 → 1344.42] But sometimes they are completely in the way.
[1345.02 → 1351.42] Or they are also attacking an HR transformation or a DevOps transformation.
[1351.86 → 1357.48] Or that they are doing stuff, which makes it very difficult to bring that through.
[1358.06 → 1361.46] And that's a big obstacle that I see.
[1361.46 → 1366.68] And it is very important to bring them on board, to educate them,
[1367.00 → 1373.30] and to also show them how their new job looks like in the future.
[1373.68 → 1376.86] So how do you succeed with that, like bringing them on board?
[1377.16 → 1378.36] How does that even look like?
[1378.68 → 1385.44] So one of the things you need to analyze is what are the goals these peoples have.
[1385.44 → 1391.56] And usually it's not their goals, it's the goals of their bosses.
[1391.96 → 1394.26] And you need to change these goals.
[1394.90 → 1399.18] So when we look at an HR transformation or a DevOps transformation,
[1399.76 → 1403.60] it is very crucial that it comes from the top management.
[1404.36 → 1410.92] And the top management has a clear vision and also clear guidance what they want to do
[1410.92 → 1412.78] and in which direction they want to go.
[1412.78 → 1416.76] And they need to change the goals of these people.
[1417.22 → 1422.24] Only by doing that, you can change how these people are behaving.
[1422.98 → 1423.58] Okay.
[1424.22 → 1428.18] And what about the type of person that doesn't want to change?
[1428.52 → 1429.22] What do you do then?
[1429.42 → 1433.26] This is a very difficult case when you have that.
[1433.64 → 1440.50] The only thing you can do in that case is try to educate, try to convince.
[1440.50 → 1445.88] But if you can't, he potentially, or she potentially needs to leave the company.
[1446.14 → 1446.36] I see.
[1446.94 → 1447.20] Okay.
[1447.82 → 1453.00] So coming back to the agile transformation and the DevOps transformation that you mentioned ,
[1453.40 → 1458.34] the first example that you gave us of what good looks like in practice
[1458.34 → 1465.72] is when you connect the value that the team builds to the customer or customers they build it for
[1465.72 → 1471.30] and have the customer not even verify, but make sure the value is what they expect it to be.
[1471.78 → 1472.78] So that's what good looks like.
[1472.90 → 1474.44] So is there more to it?
[1474.80 → 1480.42] Or is this basically the core of what you're referring to when you say agile and DevOps transformation?
[1480.42 → 1481.50] It's more.
[1481.66 → 1488.50] One of the most important things that I always say is what you usually have is you have bright ideas.
[1489.04 → 1490.24] The business has ideas.
[1490.48 → 1492.80] The customer has bright ideas.
[1493.26 → 1496.18] And usually you have a lot of these ideas.
[1496.80 → 1501.74] And what you want to do is you want to transform these ideas into value.
[1501.96 → 1504.44] Value for the customer, value for the company.
[1504.44 → 1509.26] So behind an idea, there is always a hypothesis.
[1509.88 → 1515.62] And you need to identify this hypothesis, which is behind this idea.
[1515.74 → 1521.18] For example, a hypothesis can be when we bring this feature or this shiny new mobile app,
[1521.46 → 1525.84] then we can have 10% more turnover.
[1526.74 → 1529.64] So that could be the hypothesis behind that.
[1529.64 → 1538.84] And now the important thing is to find out what is the minimal thing we need to do to prove this hypothesis.
[1539.94 → 1547.38] And this is a very important thing to do because with that, you can reduce the batch sizes which you have.
[1547.72 → 1554.48] So by analyzing what is the minimal thing, you identify the minimal viable product.
[1554.48 → 1563.28] And you need to also identify what are the leading indicators which indicate us that we are on the right track
[1563.28 → 1568.96] and that this hypothesis is true, and we should invest more money into that.
[1569.90 → 1579.66] And by doing that, you can reduce massively the batch size and also the amount of work which is going through your value stream.
[1580.26 → 1583.08] And that's what you really need to do.
[1583.08 → 1589.88] You need to do less, but you need to do the things which you are doing in the right way.
[1590.66 → 1602.36] And by having these hypotheses and identifying them and also having an evaluation on is it the right thing which we are doing
[1602.36 → 1612.76] and early also stop doing things, you can massively change the things you are doing, and you can create more value for the cost.
[1612.76 → 1619.82] The way I understand that is ship less, more often and check if it works.
[1620.34 → 1620.48] True.
[1621.44 → 1621.96] Absolutely.
[1621.96 → 1622.90] That's the way I'll summarize it.
[1623.08 → 1623.82] Yeah, perfect.
[1623.82 → 1630.54] And in that case, you want to optimize the shipping cycle as much as you can.
[1630.72 → 1633.36] If it takes a day, try to go for an hour.
[1633.70 → 1635.60] And if it takes an hour, try to go in for a minute.
[1636.10 → 1637.16] No, that doesn't work.
[1637.58 → 1639.76] I don't think you can ship it like in a minute.
[1639.84 → 1641.26] Maybe if you have a function, maybe.
[1641.64 → 1646.72] The point being, go as quickly as you can, but still it should feel like a comfortable pace.
[1646.90 → 1647.00] Yeah.
[1647.00 → 1650.10] You shouldn't feel like you're rushing things out.
[1650.60 → 1652.94] The scientific method is really important.
[1653.62 → 1655.00] Everything that you think is an assumption.
[1655.48 → 1657.52] And by the way, it's most likely wrong.
[1657.78 → 1662.86] But that's okay because the quicker you can iterate on that, the quicker you'll figure out what right looks like.
[1663.00 → 1663.06] Yeah.
[1663.06 → 1667.62] And once you know one right, then you'll have two, three.
[1667.74 → 1670.52] And before you know it, you have like a set of things which work well together.
[1670.78 → 1672.96] And that's the value that I see.
[1673.20 → 1673.50] Absolutely.
[1674.00 → 1678.88] One thing that I also find important, you said, yeah, go quicker.
[1679.40 → 1680.60] Yes, this is right.
[1680.88 → 1685.08] But you also need to recognize when it is enough.
[1685.34 → 1688.02] And I think this is also quite an important thing.
[1688.02 → 1691.46] You don't need to chase Google, Netflix or so.
[1691.46 → 1701.32] It can be perfectly fine in your context to, for example, ship every day or every week or so.
[1701.50 → 1707.64] You don't need to deploy to production every second like Amazon is doing it.
[1708.12 → 1713.52] So I think there is always a sweet spot, and you need to identify this sweet spot.
[1714.24 → 1714.38] Yeah.
[1714.76 → 1720.60] In my mind, any code, any feature that is built, and it's not out there, it's inventory.
[1720.60 → 1724.18] And we all know that zero inventory is the best type of inventory.
[1724.44 → 1726.64] So whatever you have, just make sure it's out there.
[1726.76 → 1728.32] Make sure people can start using it.
[1728.32 → 1730.28] Even if it's not complete, it doesn't really matter.
[1730.50 → 1731.42] Does it look right?
[1731.92 → 1734.74] And if it looks right, you have a confidence, okay, I'm walking in the right direction.
[1734.86 → 1736.14] Let's just keep adding on top of it.
[1736.14 → 1745.56] But if you can verify those assumptions as early as possible, the chances of you going terribly wrong are much less.
[1745.94 → 1748.56] You're less likely to go terribly wrong if you have that approach.
[1748.80 → 1754.28] You will still go wrong, but that's okay as long as you can do those small course adjustments.
[1754.28 → 1755.88] It's like driving on a motorway, right?
[1755.92 → 1758.22] You do like a little bit of left and a little bit of right.
[1758.22 → 1765.68] And if you have an autopilot, because we were talking about your Tesla, you can see those like very small steering wheel changes without you doing anything.
[1766.04 → 1769.76] So that's what you want, like the small course adjustments continues.
[1770.22 → 1772.28] And they happen every few seconds, and it's okay.
[1772.62 → 1772.96] Absolutely.
[1773.28 → 1780.30] And one of the things that I usually see, many companies, it is not allowed to make failures.
[1780.30 → 1789.28] And this is a huge pity because when you always need to do things right, you cannot go that fast.
[1789.94 → 1791.56] That's a huge problem.
[1791.78 → 1797.78] And this is also a cultural shift and cultural shifts, they take a lot of time.
[1798.32 → 1803.36] Can you think of an example when making a mistake was a great thing?
[1803.44 → 1808.20] When making a mistake or failure, people have learned from that failure.
[1808.20 → 1813.10] And if they weren't allowed to make it in the first place, they wouldn't have had those learnings.
[1813.34 → 1814.52] Can you think of such an example?
[1814.96 → 1816.90] Yeah, of course I have such an example.
[1817.24 → 1821.78] So in one of the projects, we needed to move fast.
[1822.28 → 1831.26] And in order to move fast, we said, okay, we have already an application in place, which we're using server-side rendering.
[1831.86 → 1834.48] But that was an old technology.
[1834.48 → 1840.22] And we said, okay, we can use that, but the user experience will not be that good.
[1840.42 → 1841.96] But we need to move fast.
[1842.56 → 1854.22] So we made an architectural decision together with the business and said, okay, we will use this old technology and move on so that we can learn.
[1854.64 → 1857.62] And we were building up the user interface with that.
[1857.62 → 1864.16] But soon the business said, yeah, it looks okay, but we want to have a better user experience.
[1864.88 → 1868.50] So a user experience specialist came to the project.
[1868.64 → 1872.78] He designed quite some very nice user interfaces.
[1872.78 → 1877.40] And we said, poor, we don't know if we can implement that with this old technology.
[1877.40 → 1880.34] But we tried and we failed.
[1880.44 → 1881.56] We failed very hard.
[1881.68 → 1882.84] We had a lot of bugs.
[1883.72 → 1891.98] And this was the time when I went to the management and I said, look, management, we have the iceberg in front of us.
[1892.46 → 1894.26] Now we have three possibilities.
[1894.60 → 1895.18] We go left.
[1895.18 → 1904.42] And this would mean we need to change the UI technology of the whole application to a modern UI technology.
[1904.98 → 1907.14] I think it was Angular in that time.
[1907.14 → 1908.68] Or we go right.
[1909.20 → 1918.18] And right is we stay with this technology, which we are having, but it will not look fancy.
[1918.18 → 1922.54] And we remove everything that we just added, all that fanciness.
[1923.12 → 1928.02] And it's just user interfaces with loading time and so on.
[1928.10 → 1934.80] Or we go straight through the iceberg and say, no, we want that with this old technology.
[1935.26 → 1938.40] But it can be that we will fail very hard.
[1939.04 → 1941.46] And we had a very good discussion about that.
[1941.66 → 1943.82] And we said, we take the risk.
[1944.14 → 1946.18] We go to a new UI technology.
[1946.18 → 1952.36] Of course, we made some silly estimations, which were absolutely wrong.
[1952.94 → 1955.04] We completely underestimated it.
[1955.48 → 1959.70] But in the end, it was the right decision, which we did.
[1960.10 → 1961.94] And the thing is, is the following.
[1962.32 → 1965.40] In the beginning, we started with this old technology.
[1965.84 → 1969.78] And that was, of course, when you look back, a bad decision.
[1969.78 → 1978.38] But it enabled us to learn very fast what we really wanted or what the customer really wanted.
[1979.08 → 1982.54] And we were able to see, okay, it looks like that.
[1982.82 → 1985.24] We added the whole user experience.
[1985.44 → 1988.66] We saw with this technology, we were not able to do it.
[1988.66 → 1993.26] And we were able to see that we now need to change.
[1993.54 → 1998.04] Of course, now you can say, yeah, you could see that already in the beginning.
[1998.04 → 2000.64] And you could change that already in the beginning.
[2000.86 → 2002.86] But in my opinion, it was not feasible.
[2003.46 → 2003.58] Yeah.
[2003.82 → 2005.82] That's a fascinating story.
[2005.82 → 2015.60] And I'm wondering what the story would have been had the developers maybe stumbled across something like Live View, which is server-side rendering.
[2015.92 → 2020.38] But it's a modern server-side rendering, which exists in the Elixir ecosystem.
[2020.72 → 2022.04] It's all running on the Erlang VM.
[2022.30 → 2023.08] Very efficient.
[2023.46 → 2025.98] It keeps JavaScript at a minimum.
[2026.38 → 2030.32] So you don't have to end up in the NPM hell, as some call it.
[2030.48 → 2031.46] You can keep things simple.
[2031.56 → 2033.68] You can keep things server-side rendered.
[2034.12 → 2034.96] But it's still fast.
[2035.02 → 2035.54] It's still modern.
[2035.54 → 2038.40] So I'm wondering what that would have looked like with this technology.
[2038.52 → 2040.44] But obviously, you need to know your technology.
[2040.62 → 2042.06] You need to know what suits you.
[2042.20 → 2043.34] And you need to own it.
[2043.60 → 2047.70] So whatever you decide to use, you need to be confident that I will make this work.
[2047.86 → 2049.62] And if it doesn't work, I will course correct.
[2050.08 → 2051.38] Because, hey, I was wrong.
[2051.50 → 2052.38] And that's perfectly fine.
[2052.46 → 2059.90] Saying I was wrong, I think a lot of people are so afraid of saying they were wrong that they never admit that in the first place.
[2060.18 → 2061.72] And as a result, they can never course correct.
[2062.14 → 2063.18] And then they hit the iceberg.
[2063.38 → 2064.78] And then we know what happens next.
[2064.78 → 2065.38] Right?
[2065.92 → 2066.18] Yeah.
[2066.30 → 2066.54] Okay.
[2066.94 → 2072.16] And one of the important thing is you should not be afraid of the sunk cost.
[2072.30 → 2074.82] Because that's always a bad thing.
[2074.90 → 2078.78] And you always hear that term quite a lot.
[2078.86 → 2078.96] Yeah.
[2079.04 → 2080.60] But then we have sunk cost.
[2081.36 → 2081.50] Yeah.
[2081.50 → 2083.40] Of course, you have sunk cost.
[2083.40 → 2091.00] But throwing more money after a bad idea or a bad solution is also a very, very bad thing.
[2091.20 → 2091.36] Yeah.
[2091.42 → 2092.74] It's not going to make it better, right?
[2092.74 → 2094.66] Like, the focus is on learning.
[2095.14 → 2098.14] The focus is not on the time spent to learn.
[2098.44 → 2099.12] What did you learn?
[2099.20 → 2100.04] Is this a good thing?
[2100.22 → 2101.60] And can you build on top of that?
[2101.98 → 2105.16] So if you switch your mindset, and you think, well, that's okay.
[2105.26 → 2106.56] We know not to do that again.
[2106.56 → 2110.08] And we know that that's like an area that we're not comfortable with.
[2110.24 → 2112.68] And the longer you delay it, the worse it gets.
[2113.10 → 2114.04] We all know that, right?
[2114.34 → 2116.72] Like, just stop thinking about things like that.
[2117.10 → 2117.26] Okay.
[2117.26 → 2124.22] Now, talking about technology, I'm wondering what role does specific technology play in
[2124.22 → 2124.78] these decisions?
[2125.22 → 2129.82] So I know that many teams get excited about something like Kubernetes, or they get excited
[2129.82 → 2131.20] about, you mentioned Angular.
[2131.48 → 2134.92] I'm not sure who gets excited about Angular these days, but I'm sure there are people out
[2134.92 → 2138.68] there which love it or some other, you know, JavaScript framework.
[2138.68 → 2140.28] And they say, no, we have to use this.
[2140.62 → 2143.86] How do you deal with those types of scenarios?
[2143.94 → 2146.64] Well, first, have you been in those types of scenarios?
[2146.64 → 2149.10] And if you have, how did you deal with them successfully?
[2149.38 → 2153.62] I have been in these types of scenarios quite a lot.
[2153.82 → 2155.04] The thing is the following.
[2155.38 → 2162.16] It's what you need to do is you need to understand what the real need is, what you need to do.
[2162.80 → 2166.16] So getting excited about the technology is a great thing.
[2166.62 → 2173.32] Trying out this technology is also a great thing, but you should not do that in a huge
[2173.32 → 2173.90] project.
[2174.34 → 2176.22] So trying out things.
[2176.64 → 2184.40] So what I usually do is I really want to understand what exactly our need is and what
[2184.40 → 2186.66] problem we are trying to solve.
[2186.78 → 2191.06] So what is the underlying problem we are trying to solve with this technology?
[2191.06 → 2196.32] And there is technology out there which perfectly fits the problem.
[2196.52 → 2204.72] But just looking at the technology and not knowing what problems we are trying to solve is a very
[2204.72 → 2205.50] bad thing.
[2205.96 → 2212.58] So what I do is when we have such a case, I really try to identify what the problem is.
[2212.58 → 2217.90] And of course, you then have different technology or different decisions you can do.
[2218.34 → 2228.94] And what I then do is I do sort of an analysis of the different possibilities where I say, OK,
[2229.14 → 2230.62] this is technology.
[2230.62 → 2231.62] technology, why?
[2231.62 → 2234.22] And this has these advantages.
[2234.22 → 2236.86] It solves us these problems.
[2236.86 → 2240.64] But it also could potentially introduce these problems.
[2240.64 → 2244.14] And this is the other technology which we are having.
[2244.14 → 2251.02] And then you have something which you can compare and which you also can say, OK, should we go
[2251.02 → 2254.80] into this direction, or should we go in more in this direction?
[2254.80 → 2264.16] And after that, I usually also do some prototypes on these technologies to get my hands dirty on that so
[2264.16 → 2267.92] that I can see, does it really work or does it not work?
[2268.48 → 2271.06] Who decides which technology should be used?
[2271.12 → 2276.22] Do you let the developers decide the ones doing the work or do you let the architects decide or the
[2276.22 → 2276.56] management?
[2276.92 → 2277.68] How does that look like?
[2277.80 → 2282.64] In my opinion, it should always be a decision of the team.
[2282.64 → 2289.76] The team which needs to work with this technology, they need to take the decision.
[2290.40 → 2297.62] Because if someone else takes the decision, the team does not stand behind this decision.
[2297.86 → 2306.36] So that's why I usually want that the team takes the decision and also does the analysis and
[2306.36 → 2306.94] everything.
[2306.94 → 2313.90] And so they sort of need to come up with the idea and also with the decision.
[2314.26 → 2318.40] Of course, there are companies out there where this is not really possible.
[2319.32 → 2322.16] And then I also try to do that.
[2322.42 → 2328.98] But then I try to convince, for example, the central architecture or the management about
[2328.98 → 2331.24] this solution which we should do.
[2336.94 → 2342.90] Hey, shippers.
[2343.06 → 2346.42] This episode is brought to you by our friends at Equinix Metal.
[2346.72 → 2351.02] If you want the choice and control of hardware with low overhead and the developer experience
[2351.02 → 2353.32] of the cloud, check out Equinix Metal.
[2353.72 → 2357.78] Deploying minutes across 18 global locations from Silicon Valley to Sydney.
[2358.22 → 2363.16] Visit metal.equinix.com slash just add metal and receive $100 in credit to play with.
[2363.16 → 2367.12] Again, metal.equinix.com slash just add metal.
[2367.34 → 2369.84] And by our friends at Fire Hydrant.
[2369.98 → 2372.88] Fire Hydrant is the reliability platform for teams of all sizes.
[2373.40 → 2378.62] With Fire Hydrant, teams achieve reliability at scale by enabling speed and consistency from
[2378.62 → 2381.08] a service deployment to an unexpected outage.
[2381.42 → 2381.86] Here's the thing.
[2381.92 → 2385.18] When your team learns from an incident, you can codify those learnings into repeatable
[2385.18 → 2386.28] automated run books.
[2386.64 → 2390.88] And these run books can create a Slack incident channel, notify particular team members, create
[2390.88 → 2395.00] tickets, schedule a Zoom meeting, execute a script, or send a web hook.
[2395.32 → 2396.06] Here's how it works.
[2396.24 → 2399.98] Your app goes down, an alert gets sent to a specific Slack channel, which can then be
[2399.98 → 2400.98] turned into an incident.
[2401.36 → 2404.48] That will trigger a workflow you've created already in a run book.
[2404.78 → 2409.44] A pinned message inside Slack will show all the details, the Jira or Clubhouse ticket,
[2409.74 → 2410.48] the Zoom meeting.
[2410.78 → 2415.32] And all of this is contained in your dedicated incident channel that everyone on the team
[2415.32 → 2416.10] pays attention to.
[2416.36 → 2419.46] Now you're spending less time thinking about what to do next, and you're getting to work
[2419.46 → 2421.44] actually resolving the issue faster.
[2422.02 → 2425.70] What would normally be manual tickets across the entire spectrum of responding to an incident
[2425.70 → 2429.18] can now be automated in every single way with Fire Hydrant.
[2429.46 → 2430.56] And here's the best part.
[2430.74 → 2432.52] You can try it free for 14 days.
[2432.64 → 2434.40] You get access to every single feature.
[2434.78 → 2436.02] No credit card required at all.
[2436.28 → 2439.54] That way you can prove to yourself and your team that this works for you.
[2439.54 → 2441.98] Get started at FireHydrant.io.
[2442.34 → 2444.70] Again, FireHydrant.io.
[2444.70 → 2466.60] I know, Romano, that you have a YouTube channel, which is growing in popularity.
[2466.86 → 2468.18] I've seen some perfect videos.
[2468.18 → 2475.46] And I've checked today, and your most popular video today is what are the DevOps trends that
[2475.46 → 2477.12] you have seen in 2021.
[2477.62 → 2479.80] I think 2021 DevOps trends, something like that.
[2479.86 → 2482.54] I forget the exact title, but it was DevOps trends for 2021.
[2483.22 → 2485.70] So why do you think that video is so popular?
[2486.02 → 2488.94] Actually, I really don't know why it is so popular.
[2488.94 → 2495.08] But I made some analysis, and it looks like people are Googling this title.
[2495.36 → 2498.32] So they want to know what the trends are.
[2498.58 → 2499.12] So what are they?
[2499.22 → 2500.60] Can you tell us what they are?
[2500.94 → 2501.54] Yeah, of course.
[2501.74 → 2508.24] So the trends which I brought up in 2021 was it's all about automation.
[2508.72 → 2511.02] So we need to automate more.
[2511.02 → 2514.70] So that's one of the trends that I pointed out.
[2515.04 → 2515.52] Security.
[2515.88 → 2520.50] So the whole Develops, that was a huge one.
[2520.88 → 2525.50] And IOPS, that was also one of the trends that I pointed out.
[2525.74 → 2529.86] So we have a lot of data, and we need to deal with this data.
[2530.08 → 2532.96] So AI is a very good match for that.
[2533.26 → 2536.74] And these are the things that I see are coming up.
[2536.74 → 2544.02] So when I look back to the statements that I did, I think I was absolutely right with these trends.
[2544.22 → 2549.72] For example, when I look at IOPS, this is something that's coming quite huge.
[2549.98 → 2557.72] I also started using IOPS in some areas, and the results are really amazing.
[2558.20 → 2560.30] First, what is IOPS?
[2560.60 → 2562.84] And second of all, how do you make use of that?
[2562.94 → 2564.84] What does it look like in practice for you?
[2564.84 → 2571.36] So IOPS, as I said, usually you log out quite a lot of data.
[2571.70 → 2573.12] So you have a lot of log statements.
[2573.26 → 2577.28] And when you have a distributed system, you have distributed log files.
[2577.50 → 2584.20] So first, you need to put that all together into one logging system, which you can have.
[2584.34 → 2587.16] But then you have a lot of logging statements in there.
[2587.16 → 2594.86] And it's impossible to really see where problems are or where trends are.
[2595.58 → 2601.44] And here comes IOPS into play because IOPS can do pattern matching.
[2601.66 → 2604.16] And there is a ton of tools out there.
[2604.38 → 2606.90] I don't want to do advertising here.
[2607.50 → 2608.26] But they are...
[2608.26 → 2609.04] What do you use?
[2609.18 → 2609.70] What do you use?
[2609.74 → 2610.10] That's something...
[2610.10 → 2614.06] I use, for example, I use quite a lot Dynamists.
[2614.06 → 2622.12] And I'm a huge fan of Dynamists because we have some very difficult projects out there.
[2622.58 → 2630.60] And we were chasing some performance problems and also some problems where suddenly something didn't work.
[2630.96 → 2632.24] And we were not finding it.
[2632.24 → 2636.08] And also with log file analysis, we were not finding it.
[2636.20 → 2645.76] But by using Dynamists, Dynamists was able in minutes to point us to the correct server where the problem was.
[2645.80 → 2649.32] And it was just a configuration problem on that server.
[2649.72 → 2653.22] And we were like, whoa, how did that go?
[2653.34 → 2659.56] And that's quite amazing how good these IOPS systems are already.
[2659.56 → 2660.16] Okay.
[2661.16 → 2663.52] Anything other than Dynamists that you've used, and you've liked?
[2663.66 → 2665.36] I also use Datadog.
[2665.96 → 2667.24] I like that also.
[2667.74 → 2669.88] Beside of that, no, I cannot.
[2670.46 → 2670.68] Okay.
[2670.94 → 2675.72] So Datadog, we're using it in the same way in that you were shipping logs to Datadog.
[2675.80 → 2679.90] And then Datadog figured out what was going on in the system based on the logs?
[2680.16 → 2680.60] Exactly.
[2681.24 → 2681.54] Okay.
[2682.16 → 2682.58] Interesting.
[2682.84 → 2683.04] Okay.
[2683.38 → 2684.80] We talked about IOPS.
[2684.80 → 2692.28] Now, in automation, what tools do you find yourself reaching out for when you're automating things?
[2692.66 → 2697.42] What is in your toolbox, or what do you find maybe that your team likes to use?
[2697.80 → 2697.96] Yeah.
[2698.08 → 2708.16] What we quite often use when it comes to automation, when it comes to deployment automation, we use quite a lot of Octopus Deploy, of course.
[2708.16 → 2721.08] And when it comes to CI, CD pipelines, then, of course, we use Jenkins, but also Team City, Azure DevOps is also a huge thing.
[2721.32 → 2724.50] And, of course, GitHub and GitLab.
[2724.74 → 2724.92] Okay.
[2725.22 → 2725.46] Okay.
[2726.04 → 2729.08] And other category was Develops.
[2729.18 → 2731.14] I think I would call it like supply chain security.
[2731.66 → 2735.78] What tools do you use for supply chain, for securing the supply chain?
[2735.78 → 2741.94] We need to understand that there are different aspects of security when we talk about Develops.
[2742.36 → 2745.10] One thing is the application security.
[2745.42 → 2754.82] So, when we do continuous integration and our continuous integration server is compiling our source code, we do static code analysis.
[2755.52 → 2757.78] There, for example, we use, of course, Sonar Cube.
[2758.68 → 2762.80] Checkmarks is also one of the things you can use.
[2762.80 → 2766.26] And, of course, there are other tools.
[2767.02 → 2771.40] Like, I think there is an OWASP tool, but I don't know the name anymore.
[2771.98 → 2776.54] A ton of tools is out there to do just static code analysis.
[2777.04 → 2784.98] And what you also need to do is you not only need to analyze your code, you also need to analyze the libraries.
[2785.70 → 2788.02] And the libraries of the libraries and of the libraries.
[2788.14 → 2788.62] Oh, yes.
[2788.94 → 2789.40] Exactly.
[2789.52 → 2790.14] That's a big one.
[2790.14 → 2791.18] That's a big one.
[2791.32 → 2794.06] And you need to identify these vulnerabilities there.
[2794.24 → 2797.82] And there I usually use White Source to do that.
[2798.48 → 2805.98] Which is also quite good because you also get the information about the licensing, which is also a difficult thing.
[2806.18 → 2806.64] Oh, yes.
[2806.98 → 2807.48] Oh, yes.
[2807.50 → 2808.20] That's a big one.
[2808.30 → 2808.60] You're right.
[2808.70 → 2814.22] Like, once you enter the enterprise world, these things, like, you don't even think about them as a startup.
[2814.22 → 2817.94] But when you go in the enterprise, this is a big ticket item.
[2818.14 → 2819.26] Really very important.
[2819.76 → 2820.08] Exactly.
[2820.32 → 2820.48] Exactly.
[2820.98 → 2825.94] And the second thing you need to think of is, of course, when you are in production.
[2826.48 → 2830.96] First, what you need to do is monitor your system.
[2830.96 → 2836.42] And therefore, you need to have these enterprise security monitoring systems.
[2836.88 → 2839.22] There is also a ton of products out there.
[2839.48 → 2841.82] But usually what you use is Splunk.
[2842.02 → 2850.14] You configure quite a good alerting together with the security experts so that you get alerted about any security vulnerabilities.
[2850.14 → 2851.18] That's interesting.
[2851.44 → 2855.60] So we have heard about the trends, the DevOps trends for 2021.
[2856.18 → 2861.16] And you give us some great examples, some tools that, you know, you use in the various spaces.
[2861.68 → 2865.50] I'm wondering, first, will you create a video for 2022?
[2866.18 → 2866.50] Sure.
[2866.68 → 2867.18] Of course.
[2867.48 → 2867.78] Okay.
[2867.78 → 2869.64] I'm currently preparing it.
[2869.84 → 2873.32] I'm gathering all the trends that I see at the moment.
[2873.58 → 2877.76] And at the end of the year, I will create that video and publish it.
[2877.76 → 2881.10] Can you give us a couple of hints as to what you're thinking about?
[2881.30 → 2882.34] Again, this is a draft.
[2882.44 → 2885.70] This is not a finished version, but a few things that you're thinking for this video.
[2885.94 → 2886.08] Yeah.
[2886.56 → 2893.32] So first, what I will do is I will look back to what I said in my 2021 video.
[2893.32 → 2895.64] And I will have a look at that.
[2895.78 → 2899.66] And then I will say what kind of trends I see in the future.
[2900.06 → 2904.20] And one of the huge trends that I see is hyperautomation.
[2904.20 → 2908.54] So it's not only about automating stuff.
[2908.82 → 2911.84] It's about automating nearly everything.
[2912.34 → 2916.84] So this is a huge trend that I'm seeing coming.
[2917.56 → 2922.56] And with the hyperautomation, there is also another thing coming.
[2922.76 → 2927.10] And this is you get a lot of data out of that, and you need to monitor that.
[2927.10 → 2930.94] And then you have, again, that big data problem.
[2931.18 → 2939.34] And again, IOPS comes into play because with all of that automation, you also need to maintain that, and you need to operate that.
[2939.80 → 2944.16] So your topic observability will be quite a huge thing.
[2944.80 → 2945.40] Interesting.
[2945.96 → 2949.16] So hyperautomation, that is a great title.
[2949.84 → 2952.36] I'm sure that we could do an episode just on that.
[2952.58 → 2953.22] What it is?
[2953.32 → 2954.24] Why is it important?
[2954.70 → 2956.04] What elements do you see in that?
[2956.04 → 2956.52] Interesting.
[2957.24 → 2958.84] Okay, that's a great idea, I think.
[2959.30 → 2962.06] Let's run it by the product team, I think.
[2962.76 → 2964.92] Because you were talking about ideas, everybody has one.
[2965.02 → 2968.62] So how do you figure out whether the ideas are you for a related hypothesis?
[2969.32 → 2969.82] Is that something?
[2969.92 → 2974.14] So maybe anyone listening to this can tell us if that's something they're excited about.
[2974.58 → 2977.44] We can connect it to the users, to the end users, the ones listening.
[2977.60 → 2980.52] And if they would want to for us to do an episode on that.
[2980.70 → 2981.36] I'm excited.
[2981.36 → 2989.14] What the next thing is, which we'll have, and this is the whole cyber resilience topic.
[2989.14 → 2994.92] So, of course, we have on one side, we have that Develops thing.
[2995.06 → 2999.22] So we bring security into the whole DevOps cycle.
[2999.22 → 3011.64] But when you look at all the attacks that are out there on companies, I think cyber resilience will be one of the big, big topics.
[3011.64 → 3023.34] And I think together with Develops, we will be able to give the companies this cyber resilience in their application, but also in their infrastructure.
[3024.62 → 3025.10] Interesting.
[3025.50 → 3028.24] I don't know enough about that topic, but it's something I'd like to do.
[3028.44 → 3031.56] I would like to research just to understand it a bit better.
[3031.56 → 3039.00] I know all the ransomware attacks and all the cyberattacks, they're becoming more and more prevalent and bigger, and they effect more and more users.
[3039.50 → 3046.00] But I don't know enough about more details other than what you just get from afar.
[3046.38 → 3049.60] So I think that's something I'd like to spend a bit more time in.
[3049.92 → 3058.08] I know that switching subjects, because I know that one topic that was top of your mind recently was how to allocate budget.
[3058.08 → 3058.52] Yeah.
[3058.82 → 3061.56] And I forget the exact phrase that you used.
[3061.60 → 3062.42] It was a perfect one.
[3062.66 → 3063.58] Let me check that, actually.
[3063.96 → 3065.06] Or you can tell me what it is.
[3065.22 → 3065.36] Sure.
[3065.58 → 3067.94] It's participatory budgeting.
[3068.40 → 3068.76] Okay.
[3068.84 → 3069.56] What is that?
[3070.02 → 3071.82] What is participatory budgeting?
[3072.36 → 3072.84] Exactly.
[3073.50 → 3080.14] So participatory budgeting is a thing you can do to allocate budget.
[3080.74 → 3085.90] So what is one of the big problems that we have when allocating a budget?
[3085.90 → 3090.58] Usually, you have people who want to do stuff.
[3090.90 → 3099.26] And on the other side, you have people who have the budget and who say where, which kind or which amount of budget gets.
[3099.76 → 3109.78] The problem is that the people who have the budget don't really know what exactly the impact is of the certain topic.
[3109.78 → 3114.50] The people who want to do something really has.
[3115.16 → 3116.46] And that's a huge problem.
[3116.82 → 3124.76] And what you usually get is the people who have the budget will just say, yeah, we divide everything apart.
[3125.06 → 3128.16] And everybody gets the same amount.
[3128.48 → 3132.10] And then everybody is sort of happy.
[3132.66 → 3135.10] That's quite a bad thing you usually have.
[3135.10 → 3139.72] And the better thing is to have that participatory budgeting.
[3139.80 → 3140.60] That's an event.
[3141.04 → 3147.64] And in this event, everybody who wants to have a budget and is part of a value stream comes together.
[3148.34 → 3150.90] And they get allocated the budget.
[3151.08 → 3152.28] They sit on a table.
[3152.64 → 3155.06] They get the budget pot.
[3155.06 → 3160.50] And then they on the table need to pitch for their budget.
[3160.88 → 3170.40] And then they have together, participatory, a discussion on in which area are we going to invest the money.
[3170.96 → 3181.84] And that's a very, very cool thing because then the people are discussing impact on value, how much value this topic brings.
[3181.84 → 3195.86] And especially when you have, of course, OKR or a strategy, they are also coming up with the strategy and are saying, hey, look, this initiative buys more into the strategy than the other one.
[3195.86 → 3200.32] So there is that entrepreneurial thinking which is coming up.
[3200.76 → 3205.86] And they start to think like it is their own enterprise.
[3206.50 → 3208.74] And they are more emotionally attached.
[3208.92 → 3210.96] And in the end, you get a better budget.
[3210.96 → 3212.94] That was a great summary.
[3213.22 → 3215.10] I know that you gave a whole talk on this.
[3215.58 → 3217.78] And based on that summary, I'm going to watch it.
[3218.00 → 3218.70] So thank you for that.
[3220.54 → 3220.98] Great.
[3221.90 → 3223.84] So we are just about to wrap up.
[3224.10 → 3226.48] I have one last very important question.
[3227.00 → 3230.88] What is the most important takeaway for our listeners from our conversation?
[3231.32 → 3232.68] What would you like them to remember?
[3233.06 → 3234.34] A very good question.
[3234.34 → 3240.04] I would say don't be afraid to take decisions.
[3240.42 → 3245.30] Don't be afraid to make a bad decision.
[3245.70 → 3250.82] Just constantly learn and react and constantly adapt.
[3251.18 → 3251.60] I love that.
[3251.96 → 3252.86] That's amazing, Roman.
[3252.96 → 3253.74] Thank you very much.
[3254.00 → 3254.58] This was a pleasure.
[3254.84 → 3255.40] Thank you also.
[3255.40 → 3261.64] Thank you for tuning in to another episode of Ship It.
[3261.88 → 3263.68] I enjoyed making it for you.
[3263.96 → 3267.42] This is just one of the podcasts for developers that we ship.
[3267.80 → 3271.12] Go to changelog.com forward slash master for the rest.
[3271.50 → 3276.64] You can join me and the rest of our community at changelog.com forward slash community.
[3277.14 → 3278.86] There are no imposters in our Slack.
[3279.20 → 3280.46] Everyone is welcome.
[3280.46 → 3284.76] Huge thanks to our partners Vastly, Launch Darkly and The Note.
[3285.08 → 3288.30] Thank you, Break master Cylinder for all our awesome things.
[3288.78 → 3289.78] That's it for this week.
[3290.04 → 3290.66] See you next week.
[3310.46 → 3321.24] Game on.
