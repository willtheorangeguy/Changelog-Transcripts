[0.00 → 10.60] Welcome back, everyone.
[10.78 → 13.34] This is the Changelog, and I'm your host, Adam Stachowiak.
[13.66 → 19.66] This is episode 168, and we're joined today by Julius Vols from SoundCloud to talk about
[19.66 → 23.54] Prometheus, an open-source service monitoring system written in Go.
[24.28 → 25.68] Super awesome conversation today.
[25.74 → 28.40] We talked about the data model, the query language, and all the in-between.
[28.40 → 33.74] We have three awesome sponsors for the show, Code Ship, Top Tile, and DigitalOcean.
[34.28 → 36.48] Our first sponsor is Code Ship.
[36.60 → 37.20] They're yet hosted.
[37.80 → 43.04] Continuous delivery service focusing on speed, security, and customizability, and they've
[43.04 → 45.28] launched a brand-new feature called Organizations.
[45.92 → 51.70] Now you can create teams, set permissions for specific team members, and improve collaboration
[51.70 → 53.78] in your continuous delivery workflows.
[53.78 → 60.38] Maintain centralized control over your organization's projects and teams with Code Ship's new organization's
[60.38 → 60.76] plans.
[61.52 → 66.50] You can save 20% off any premium plan you choose for three months by using this code,
[66.70 → 67.60] the Changelog Podcast.
[68.32 → 74.10] Again, that code is the Changelog Podcast, and you'll save 20% off any premium plan you choose
[74.10 → 74.76] for three months.
[75.24 → 77.86] Head to CodeShip.com slash the Changelog to get started.
[77.86 → 79.52] And now, on to the show.
[87.20 → 87.82] Alright, everybody.
[87.88 → 88.34] We're back.
[88.44 → 89.70] We've got a great show lined up today.
[89.80 → 91.40] One we've actually been waiting for a bit.
[91.48 → 93.68] It was recommended by Peter Bergen.
[93.78 → 97.64] We just talked about him and Go Kid and Go For Con and all that stuff, but Peter was
[97.64 → 98.46] recommending this.
[98.70 → 104.80] Jared, our last guest, was saying that this was their, you know, Prometheus was their tech
[104.80 → 107.82] to play with, so we had to get Julius Vols on the line here.
[107.90 → 108.92] So, Julius, welcome to the show.
[109.86 → 110.12] Hi.
[110.50 → 111.34] Pleasure to be here.
[111.82 → 114.24] And also, we got Jared hanging out in the wings there.
[114.30 → 114.86] Say what's up, Jared.
[115.36 → 115.98] What's up, Jared?
[117.18 → 122.82] So, Jared, we were at Go For Con not long ago, so we met Julius and also Bjorn, who couldn't
[122.82 → 129.88] make this call, but we were excited to finally get a chance to get Prometheus in this conversation
[129.88 → 133.64] talking about metrics tracking and stuff like that on this show.
[133.86 → 136.50] So, what's the best way to open this one up?
[136.54 → 139.22] You want to talk about Julius a bit, or you want to go right into the tech?
[139.86 → 143.66] Well, first, let me say that, you know, we kind of did the hallway track at Go For Con
[143.66 → 145.66] and we were out interviewing people and talking with everybody.
[146.02 → 148.66] And there was two things people were excited about.
[148.78 → 153.08] One was Ben Johnson, who we lined up to come out here pretty soon and the stuff that he's
[153.08 → 153.48] been up to.
[153.88 → 156.86] And the other one that everybody was excited about was Prometheus.
[157.16 → 157.42] Yes.
[157.42 → 161.68] In fact, I think, Julius, you guys even got a shout-out during one of the keynotes.
[161.70 → 162.20] Is that correct?
[162.94 → 168.36] Yeah, we got a bunch of shout-outs, I think from Peter's talk, from Tomas's talk, the
[168.36 → 168.64] keynote.
[169.02 → 170.08] So, yeah, really, really exciting.
[170.72 → 171.10] Very cool.
[171.20 → 172.84] So, we're excited to hear about it.
[172.88 → 176.38] We want to know all the details, but I think, Adam, maybe if we start with the history,
[176.84 → 179.98] we can kind of see why Prometheus even exists.
[180.08 → 180.58] Do you want to start there?
[180.88 → 181.90] Let's do that.
[181.90 → 182.38] Yeah.
[183.34 → 186.82] So, Julius, you've been with SoundCloud for a bit.
[186.96 → 188.08] Before that, you were with Google.
[188.74 → 192.14] What was going on to make Prometheus a thing for you?
[193.04 → 193.46] Yeah.
[193.54 → 196.60] So, when I was at Google, I was actually doing something completely different.
[196.84 → 200.78] I was in Google's production offline storage system.
[200.78 → 207.18] So, basically, we had many tens of data centres with huge tape libraries backing up all production
[207.18 → 208.60] data that Google had.
[209.14 → 212.48] So, basically, exabyte scale backup system globally.
[213.76 → 220.22] So, monitoring wasn't really my specialty there, but I definitely came in contact with it as
[220.22 → 222.44] a site reliability engineer on that service.
[222.44 → 232.88] And when I left Google and joined SoundCloud back in 2012, it went as it often goes when
[232.88 → 234.66] Googlers left SoundCloud.
[234.66 → 240.44] When Googlers left Google at around that time, especially, they felt a bit naked in terms
[240.44 → 244.62] of what the open source world provided them in terms of infrastructure.
[245.74 → 248.48] Because at Google, you have an awesome cluster scheduler.
[248.58 → 251.88] You've got awesome monitoring systems, awesome storage systems, and so on.
[251.88 → 256.54] Suddenly, you get thrown out into the wild, and you miss all of that stuff, and you feel
[256.54 → 260.04] just this urgent need to be building a lot of that yourself again.
[261.50 → 267.20] But when I joined SoundCloud, a month prior to that, another ex-Google was also joining
[267.20 → 271.46] SoundCloud, Matt Proud, and he felt even more strongly about this.
[271.60 → 276.58] And he was particularly unhappy with the state of open source monitoring systems.
[276.58 → 284.56] So he had actually already, in his free time, started building client libraries for instrumenting
[284.56 → 286.10] services with metrics.
[286.64 → 289.84] And his grand vision was to build a whole monitoring system.
[290.50 → 296.46] So when I joined a month later, he kind of pulled me on board, and we started building
[296.46 → 300.56] something in our free time that eventually became Prometheus.
[300.56 → 306.02] So just in the first month, end of 2012, that was really just our free time.
[306.50 → 314.02] Finally, we got enough of it working in such a way that we could expose data from services,
[314.32 → 318.98] collect it, query it, and maybe even show it in a graph.
[319.50 → 323.18] And that was the point when we decided, okay, this is actually going somewhere.
[323.36 → 324.14] Let's give this a name.
[324.32 → 325.30] Let's call it Prometheus.
[325.30 → 330.98] And briefly afterwards, we started formally introducing that at SoundCloud.
[332.00 → 337.06] And yeah, nowadays, it has become SoundCloud's standard monitoring system and time series
[337.06 → 337.52] database.
[338.62 → 343.94] Now, deep topic aside, I got to ask, which is one of my favourite movies out there
[343.94 → 346.98] by Ridley Scott is a movie called Prometheus.
[347.58 → 348.82] Is there any correlation?
[349.46 → 351.16] I have never watched that movie, actually.
[351.28 → 353.08] Well, we see aliens come out of the code at some point.
[353.08 → 353.56] Right.
[354.24 → 355.56] So that was actually funny.
[355.66 → 358.16] I think it actually came out around the same time.
[358.30 → 358.46] Okay.
[358.60 → 360.32] But it wasn't really on my radar back then.
[361.36 → 367.40] I think I just briefly had heard about it, but it wasn't really any, it wasn't really
[367.40 → 368.30] connected to this.
[368.44 → 368.60] Okay.
[368.72 → 369.26] All right.
[369.54 → 369.72] Yeah.
[370.02 → 373.12] Prometheus, the movie came out in 2012.
[373.70 → 377.76] And I remember loving the name and not loving the movie so much, Adam.
[377.84 → 379.36] So maybe that's a separate show, but we could.
[379.50 → 379.82] Yeah.
[379.82 → 383.36] I heard a lot of bad things about that movie.
[383.36 → 384.46] We could pause this for a minute.
[384.58 → 385.06] Let me rant.
[385.26 → 387.52] I mean, we could just go start another show.
[387.72 → 388.16] I'm just kidding.
[388.30 → 393.26] Maybe I should go a bit more into what we had at SoundCloud back then, because that was
[393.26 → 396.62] kind of the big motivation to build Prometheus.
[396.80 → 398.58] Well, you said that you felt naked.
[398.64 → 402.94] As a Googler, you felt naked coming out of Google and some of the things missing.
[403.10 → 404.82] So this was obviously one of those things missing.
[404.82 → 405.30] Right.
[405.30 → 405.66] Right.
[405.80 → 405.96] Yeah.
[406.16 → 406.30] Yeah.
[406.52 → 410.84] But you might ask, there were many open source monitoring systems, right?
[410.98 → 412.68] Why were we not happy with those?
[412.68 → 413.38] We're asking that question.
[413.46 → 414.24] I like that question.
[414.60 → 416.08] I actually had that question queued up.
[416.10 → 416.46] Yes.
[416.54 → 417.36] That's the next question.
[418.44 → 418.60] Cool.
[418.78 → 424.04] So, I mean, back then, SoundCloud was doing this migration that a lot of companies do,
[424.58 → 430.88] migrating from one monolithic web application to a set of microservices, just because the initial
[430.88 → 433.90] monolithic application has grown too big, too complex.
[434.36 → 436.08] People don't want to maintain it anymore.
[436.20 → 439.18] You can't have independent groups deploying independent things.
[440.46 → 447.14] So SoundCloud pretty early on, actually, started adopting Go and built their own kind of Heroku
[447.14 → 451.02] style in-house cluster scheduler called Bazooka.
[451.84 → 456.48] And that was already a container scheduling system, a very early form.
[456.94 → 458.12] We're still using that, actually.
[458.12 → 463.08] Before Docker came out, before Kubernetes and so on came out.
[463.72 → 469.22] And the challenge was now that we had these hundreds of microservices running on these
[469.22 → 472.34] Bazooka clusters with thousands of instances.
[473.16 → 480.12] And developers, whenever they built a new revision, maybe every day even, scaled down the old revision
[480.12 → 481.48] and scaled up the new revisions.
[481.66 → 486.04] And all these instances would land on random hosts and on random ports.
[486.04 → 489.28] And somehow we needed to monitor them.
[489.96 → 497.18] So what we did back then was, what SoundCloud did back then was use Stated and Graphite as
[497.18 → 502.00] the main time series-based monitoring system.
[503.18 → 506.86] So Stated and Graphite had several problems.
[506.86 → 512.78] So when I joined, I remember the Stated server almost falling over because it was a single-threaded
[512.78 → 517.56] node application running on a huge, beefy machine, but it could only use one core.
[518.00 → 521.48] So it was actually throwing away UDP packets left and right.
[521.58 → 523.26] I don't know if you know how Stated works.
[523.26 → 530.10] The general working model is that, let's say you have a set of web servers, let's say an
[530.10 → 532.80] API server, and you have 100 instances of that.
[534.40 → 541.44] Then if you want to count the number of HTTP requests that happen in that entire service,
[542.00 → 549.22] every one of these instances, for every request that they handle, send a UDP packet to Stated.
[549.22 → 556.18] And Stated will count from all these 100 instances, will count up all these counter packets from
[556.18 → 561.42] these different instances over usually a 10 seconds interval, and then finally sum them
[561.42 → 566.68] all up and write a single data point out to Graphite at the time.
[567.30 → 572.14] So Graphite is a time series storage system, and Stated is kind of in front of it to aggregate
[572.14 → 576.78] counter data into a final count per 10 seconds.
[576.78 → 584.32] And you can do some stuff there, like you can say on the service side, please only send
[584.32 → 587.36] every 10th UDP packet or something.
[587.46 → 589.06] So you alleviate the load somewhat.
[590.40 → 595.88] But the main pattern is here that you're doing the counting in the Stated site.
[596.98 → 600.42] And yeah, that Stated wasn't really scalable.
[600.86 → 604.06] It was throwing away UDP packets, wasn't really working that well anymore.
[604.06 → 609.72] And the other problem was Graphite's inherent data model.
[609.92 → 617.06] So in Graphite, if you store a metric, a time series, it's only a single metric name with
[617.06 → 617.78] no dimensions.
[618.14 → 623.76] So it has some dots in the middle that allow you to separate components of a metric name.
[624.02 → 627.60] And people use that to encode implicit dimensions.
[627.60 → 640.60] So for example, you might have a metric named API.http.get.200 to count the successfully handled
[640.60 → 642.78] get requests of an API server.
[643.70 → 645.30] And that works, kind of.
[645.40 → 646.44] It doesn't scale too well.
[646.56 → 651.10] Graphite doesn't deal very well with you going wild with these dimensions.
[651.10 → 657.96] It doesn't allow you in the query language to be particularly flexible about how you query
[657.96 → 658.94] for these dimensions.
[659.20 → 659.98] And they're also implicit.
[660.46 → 664.94] So you look at one of these dot-separated components, and you can kind of guess what
[664.94 → 667.28] it would mean, but you only see the value.
[667.40 → 668.64] You don't see the key, usually.
[668.64 → 676.30] Another problem there was that due to this limited dimensionality, it was really hard
[676.30 → 686.90] to figure out which particular host or which particular service instance a metric was coming
[686.90 → 687.12] from.
[687.22 → 690.00] So let's say you have a global latency spike.
[691.64 → 697.88] So if you have these counters over 100 instances, they all get counted into one metric in the end,
[697.88 → 700.38] and you don't really see if there's a spike.
[700.48 → 701.64] Was it only in one instance?
[701.90 → 703.58] Was it in all instances?
[704.00 → 705.78] You can't really drill down there anymore.
[706.32 → 713.20] Some teams have actually then encoded the instance and the port, like the host and the port of an
[713.20 → 717.28] instance into the metric name, into one of these dot-separated components.
[718.04 → 724.58] But Graphite is not really meant for that, and it blew up pretty quickly.
[724.58 → 729.56] So they had to run their own Graphite server, but that is not particularly fun because Graphite
[729.56 → 730.88] is not so fun to run either.
[732.10 → 737.98] So yeah, these were kind of the problems we encountered with the Stated and Graphite combination.
[738.14 → 739.38] That was for service monitoring.
[739.38 → 745.98] So when I say monitoring, actually, I kind of mean, I mean, different people mean different
[745.98 → 746.64] things with that.
[746.86 → 750.78] I mean both time series collection and trending and alerting.
[751.08 → 755.32] Some people, when they say monitoring, they think of only something like Nagios, only something
[755.32 → 756.60] that alerts people.
[756.60 → 757.02] See, Jared?
[758.24 → 758.50] What?
[758.70 → 759.54] Did you hear that?
[759.82 → 760.26] Nagios.
[761.64 → 762.94] Oh, how do you pronounce it?
[763.06 → 764.74] That's the European take on it.
[764.74 → 772.44] I took a break there to butt in, but pre-call, you can mention it, Jared, but he set up some
[772.44 → 774.04] Nagios servers.
[775.60 → 777.16] So anyway, you said Nagios.
[777.16 → 778.48] So Nagios is the way you pronounce it?
[778.48 → 779.92] Well, I don't know how to pronounce it.
[779.94 → 784.42] That's just, you know, I used to be a network administrator back in the day, and I was the
[784.42 → 786.38] only one doing it, so you never say it out loud.
[786.46 → 789.46] But I just thought it was Nagios, because it nags you all the time.
[789.82 → 791.14] I thought they had a play on words.
[791.94 → 793.36] That makes so much more sense.
[793.36 → 794.74] But Nagios could be right.
[794.86 → 795.48] I mean, I don't know.
[795.76 → 796.00] See?
[796.12 → 796.92] That makes sense, yeah.
[796.92 → 797.24] There you go.
[798.08 → 801.08] But yeah, I mean, when I think of alerting, I think of something more like that.
[801.14 → 803.16] But you actually say service monitoring.
[803.30 → 804.98] You include alerting in your definition.
[805.12 → 805.54] Is that what you're saying?
[805.54 → 807.42] I include time series collection.
[807.80 → 809.34] I include the graphing.
[809.46 → 810.42] I include the alerting.
[810.80 → 815.46] So the whole complex of getting metrics from your systems and acting on it and notifying
[815.46 → 815.80] someone.
[816.08 → 816.30] Okay.
[817.90 → 820.42] It's kind of just a question of definition, I guess.
[820.42 → 820.74] Sure.
[820.74 → 820.78] Sure.
[821.58 → 822.10] Yeah.
[822.16 → 825.06] So we used Nagios back then.
[825.24 → 825.86] Oh, whatever you like.
[825.96 → 826.08] Yeah.
[827.02 → 831.94] Partially just running completely these stateless checks that you run on a host to see if things
[831.94 → 833.36] are good right now.
[833.80 → 836.60] And partially based on graphite-based time series.
[837.60 → 839.90] And yeah, that was fine.
[840.00 → 842.22] But Nagios is kind of also from the 90s.
[842.90 → 845.14] Its data model is very limited.
[845.14 → 848.82] I mean, it knows about hosts and services on those hosts.
[849.52 → 854.38] And if you have something like a cluster-wide check or things that just don't fit into that
[854.38 → 857.32] pattern, you kind of have to squeeze them into that pattern.
[857.56 → 859.80] And that sometimes works, sometimes not that great.
[860.30 → 865.80] It's really hard to silence by any arbitrary dimensions in Nagios.
[866.48 → 869.92] So yeah, the data model there is also a bit painful.
[870.08 → 872.00] The UI, I think we don't even need to talk about.
[872.00 → 876.44] But nowadays, we're actually using Using, which has a bit better UI.
[876.62 → 877.08] What's it called?
[877.96 → 881.70] Using is basically a drop-in replacement for Nagios.
[882.06 → 884.44] So it uses the same database.
[884.74 → 886.04] I don't think you have to change much.
[886.12 → 887.74] It's just kind of a new UI.
[887.92 → 892.74] And I think it has a bit of a different, more scalable mechanism for executing checks.
[892.74 → 896.88] But I'm not really an expert in that area.
[898.66 → 898.82] Yeah.
[899.02 → 901.12] So that was for service monitoring.
[901.42 → 903.90] And for host monitoring, we had Ganglia.
[904.30 → 909.82] And Ganglia is pretty much completely, you know, you have the host as a dimensional key
[909.82 → 911.10] there, but not much else.
[911.20 → 912.70] Of course, also the metric name.
[913.04 → 914.30] But there's no query language.
[914.54 → 917.54] There's no nice graphing interface and so on.
[917.54 → 920.58] You get these pretty static dashboards with host metrics.
[921.52 → 922.66] And yeah.
[922.74 → 926.64] So we used also Nagios, of course, for the host alerting then.
[928.34 → 932.24] This might be a little bit premature, but I just went to the Nagios.
[932.68 → 934.28] And we're all going to say it different ways, by the way.
[935.04 → 936.58] Nagios, Nagios, Nagios.
[936.58 → 940.52] Nagios, they say they're the industry standard for IT infrastructure monitoring.
[941.00 → 943.48] What is the goal, or what was the goal with Prometheus?
[943.60 → 947.60] Was it to, you know, redo what everyone had been doing?
[947.72 → 953.80] Not quite so well because you have opinions and, you know, obviously some skills to do
[953.80 → 954.00] it.
[954.14 → 958.38] But was it, is it the goal to sort of unseat some of these existing players?
[958.38 → 961.76] Or is it to just sort of like rebuild something new that made sense for SoundCloud?
[963.02 → 963.76] Yeah, definitely.
[963.76 → 969.08] So for us, it was the goal to replace Stated, to replace Graphite, to replace Nagios in the
[969.08 → 976.26] end with a new kind of ecosystem that is more powerful and more integrated and allows you
[976.26 → 978.42] to do more stuff in a more modern way.
[979.74 → 981.22] So yeah, definitely.
[981.40 → 985.94] We hope to make people depend less on those old tools, I would say.
[986.02 → 990.94] So we kind of sometimes jokingly call it a next generation monitoring system.
[990.94 → 996.88] And it does try to cover all the aspects from instrumenting your services, collecting the
[996.88 → 1003.44] data, showing the data in the dashboard, alerting on the data if something is wrong and then
[1003.44 → 1005.18] sending those notifications to you.
[1005.96 → 1008.30] So yeah, it tries to cover basically the whole field.
[1008.88 → 1012.54] What it does not do is event-based monitoring.
[1012.54 → 1021.58] So if you want to do per-request accounting, let's say, you want to really collect every
[1021.58 → 1028.30] individual event, you know, a use case like logging or a use case like Elasticsearch, where
[1028.30 → 1031.48] you can really put every individual record of what happened in there.
[1031.84 → 1033.34] That's not really what we're trying to do.
[1033.34 → 1039.86] And Prometheus is really in the business of collecting purely numeric time series that
[1039.86 → 1043.16] have a metric name and a set of key value dimensions.
[1044.18 → 1050.22] And the metric name and the key value dimensions uniquely identify every series.
[1050.52 → 1055.44] And that you can then actually use together with a query language to do really powerful
[1055.44 → 1060.72] queries, to aggregate and slice and dice based on whatever dimension you're currently interested
[1060.72 → 1062.22] in during the query, actually.
[1063.20 → 1063.82] And yeah.
[1065.22 → 1069.02] So you started building this in your free time, or you and your buddy started building
[1069.02 → 1069.28] it.
[1069.50 → 1074.74] I'm curious, just kind of the inner workings of SoundCloud, where they're at with open
[1074.74 → 1077.14] source and how much freedom they give you as an engineer.
[1077.28 → 1081.28] Was this something that you had to sell to your boss or to the company?
[1081.60 → 1086.12] Or was it just like, well, we're doing this now and whatever you guys think is the best
[1086.12 → 1087.28] solution must be right?
[1088.32 → 1088.48] Yeah.
[1088.48 → 1090.44] So this was definitely an interesting history.
[1090.76 → 1095.24] I think at the beginning, we just took the liberty ourselves to do that in our free time.
[1095.98 → 1100.88] There was a lot of resistance at the beginning to introduce that at SoundCloud, which totally
[1100.88 → 1102.80] makes sense to me, especially in retrospect.
[1103.46 → 1107.10] Because to be honest, at the beginning, nothing was really working.
[1107.10 → 1111.28] It was, I mean, late 2012, early 2013.
[1112.22 → 1115.36] The main server was pretty immature.
[1115.36 → 1117.40] It wasn't really performing well.
[1117.60 → 1120.52] A lot of ecosystem components were missing.
[1121.72 → 1124.72] And there was no real dash boarding solution yet, and so on.
[1125.08 → 1131.70] But as time went on, we just kind of, you know, I think we took quite some liberties there
[1131.70 → 1134.96] in just pushing this project on.
[1134.96 → 1137.58] And it became better and better.
[1137.58 → 1144.06] And I would say like probably one and a half years in, we had the main server that collects
[1144.06 → 1145.72] the time series and makes them curable.
[1145.92 → 1147.94] We had that pretty mature and stable.
[1148.92 → 1153.44] We had Prom dash, which is the Prometheus dashboard builder.
[1153.44 → 1159.42] So finally, people were actually able to build dashboards on top of the data that they collected.
[1159.76 → 1166.52] And we also had one of our really first killer use cases where we got instrumentation about
[1166.52 → 1170.58] all the containers that were running on Bazooka or in-house Heroku system.
[1170.58 → 1179.32] So you could get for every application revision and proc type keyed by those dimensions and more actually
[1179.32 → 1184.58] the current CPU usage, the memory usage, the memory limit, and so on and so on.
[1185.12 → 1188.80] And that really started convincing people that this was really worth it.
[1189.02 → 1196.12] And then I think that was kind of the tipping point where shortly after the strategic bet was made in SoundCloud
[1196.12 → 1197.68] to really switch to that.
[1197.68 → 1203.60] And in terms of open sourcing, that was interesting because when we started this initially,
[1203.86 → 1207.76] we just put it up on GitHub without asking anyone on its own organization.
[1209.04 → 1213.92] And so it's kind of a weird status, I guess.
[1215.36 → 1216.90] It was a private project.
[1217.24 → 1221.34] It's still arguably, I mean, it was definitely started in the free time.
[1221.50 → 1223.60] Matt even started before he joined SoundCloud.
[1223.60 → 1230.12] And we've been trying since then to keep it as independent as possible from any single company.
[1230.56 → 1237.80] So we really want this to be an open community project without one company controlling too much of the direction and so on.
[1239.28 → 1245.08] And before, so we put it on GitHub back then, but we really didn't make any noise about it.
[1245.08 → 1249.66] So we only told a couple of friends, especially also other ex-Googles.
[1249.98 → 1258.02] Because, so I guess I have to say, Prometheus is kind of inspired by a lot of what we learned about monitoring at Google.
[1258.28 → 1263.26] And a lot of people who quit Google then either asked us, hey, do you know anything similar?
[1263.64 → 1269.16] Or they just discovered Prometheus and kind of noticed that it was very similar to what they've been used to.
[1269.16 → 1278.42] So before we even, you know, went more public about Prometheus, we had a kind of insider circle of people using it, testing it.
[1278.48 → 1284.50] Already at one of our ex-colleagues from SoundCloud who then went to Docker, he started using it at Docker.
[1285.10 → 1289.92] And another colleague used it at Box Ever, which is a Dublin-based company.
[1290.78 → 1292.16] And so he's in Dublin.
[1292.16 → 1302.96] And in terms of open sourcing, so it was open source, but only in the beginning of this year, for the record, since it's a podcast, this year is 2015.
[1303.90 → 1309.38] In January, we decided, okay, it's finally, it's really ready enough to share with a broader audience.
[1310.36 → 1320.34] So just leading up to that, we had a lot of discussions with, you know, internal departments about how we should communicate this and what's the legal status around that.
[1320.34 → 1322.26] In the end, everything was pretty relaxed.
[1322.90 → 1334.12] And we had, you know, blog posts on the SoundCloud backstage blog and on Box Ever's blog and I think on my Docker colleague's private blog back then.
[1335.00 → 1337.04] And yeah, and then it really took off.
[1337.76 → 1338.34] And that was...
[1339.26 → 1340.14] So it took some work then, though.
[1340.18 → 1346.46] It took some commitment from you and Matt and others that were sort of seeing the light of where this can go and then...
[1346.46 → 1353.36] I was going to say, did you just run it concurrently alongside your Stated stuff until it showed its value, and then you were able to eventually cut over?
[1353.48 → 1355.16] Or are you still running your Stated stuff as well?
[1356.62 → 1358.16] So yeah, that's what we did.
[1358.62 → 1362.84] And Stated is still running because, you know, you never turn off old systems in practice.
[1365.02 → 1367.36] But practically nobody's using that anymore.
[1367.52 → 1368.86] Very few people are using that.
[1368.98 → 1372.60] So if you're building a new service at SoundCloud, it's going to use Prometheus.
[1372.60 → 1377.44] There's some legacy stuff on Stated and Graphite still.
[1377.68 → 1379.60] And there's some stuff that was hard to convert.
[1379.92 → 1383.40] But yeah, for the most part, it's all Prometheus now.
[1384.48 → 1392.04] And yeah, it's been really a riot, especially since being more vocal about it beginning of the year.
[1393.44 → 1394.30] We've really...
[1394.30 → 1396.70] I mean, the community has grown crazily.
[1397.18 → 1399.74] We have contributors from all kinds of companies.
[1399.74 → 1404.16] We get a lot of contributions.
[1404.30 → 1407.20] Basically, we get contributions almost every day, if not multiple.
[1408.16 → 1409.74] I think Google is now...
[1410.26 → 1413.98] Google's Kubernetes is now natively instrumented with Prometheus metrics.
[1414.28 → 1422.26] So if you want to monitor Kubernetes, you don't even need to have any kind of adapter to get Prometheus metrics out of there.
[1423.54 → 1427.12] You have CoreOS adopting it quite a lot for their components.
[1427.12 → 1433.36] So etc is one notable mention there that is already sprinkled with Prometheus metrics.
[1433.96 → 1439.38] Then you have DigitalOcean completely adopting it for their internal monitoring right now.
[1440.54 → 1442.46] I don't know how much I can say about that.
[1442.68 → 1448.48] But I think these are the three companies where they're like reasonably public about what they're doing with Prometheus.
[1448.72 → 1453.58] I know of a bunch more, but I'm not sure how much you can say about those.
[1453.58 → 1462.08] Sure. Well, there are definitely tons of details that any system that looks to replace a handful of legacy systems will have many moving parts.
[1462.34 → 1466.24] And you have an architecture, you have a data model, there's a query language, there are lots of details.
[1466.32 → 1468.36] We want to ask you about all of them.
[1468.66 → 1470.80] First, we're going to take a quick sponsor break.
[1471.14 → 1472.96] Hear a word from our awesome sponsor.
[1472.96 → 1477.70] And then we will be back with all the nitty-gritty details of Prometheus.
[1477.86 → 1478.20] Be right back.
[1479.72 → 1484.26] Top Tile is by far the best place to work as a freelance software developer.
[1484.66 → 1489.58] I had a chance to sit down and talk with Brendan Bene shot, the co-founder and COO of Top Tile.
[1489.92 → 1493.88] And I asked Brendan to share some details about the foundation of Top Tile.
[1494.16 → 1495.56] What makes Top Tile different?
[1495.88 → 1499.16] And what makes their network of elite engineers so strong?
[1499.52 → 1500.06] Take a listen.
[1500.06 → 1504.02] I mean, I'm one of the co-founders, and I'm an engineer.
[1504.80 → 1510.26] I studied chemical engineering and to pay for this super expensive degree, I was freelancing as a software developer.
[1510.42 → 1514.76] And by the time I finished, I realized that being a software developer was pretty awesome.
[1514.88 → 1515.96] And so I kept doing that.
[1516.56 → 1520.22] And my co-founder is in a similar situation as well.
[1520.22 → 1528.08] And so we wanted to solve a problem as engineers and do it as a network of engineers, kind of for engineers, by engineers.
[1528.78 → 1537.78] And having that perspective and consistently bringing on new team members who also share this really makes Top Tile different.
[1537.78 → 1543.66] And that it's a network of engineers, not kind of like you have Top Tile and then the developers.
[1543.90 → 1545.20] It's never about us and them.
[1545.38 → 1546.58] It's always us.
[1546.78 → 1550.78] Like everybody at Top Tile, for the most part, refers to Top Tile as their company.
[1550.86 → 1552.12] And they feel like it's their company.
[1552.20 → 1556.68] And everybody acts like a core team member, even though they're freelancers within the Top Tile network.
[1556.68 → 1560.08] And all of these things are extremely important to us.
[1560.48 → 1560.68] All right.
[1560.72 → 1566.92] If you're interested in learning more about what Top Tile is all about, head to TopTile.com slash developers.
[1567.36 → 1571.62] That's T-O-P-T-A-L dot com slash developers to learn more.
[1572.02 → 1574.14] And make sure you tell them the changelog sent you.
[1576.00 → 1576.64] All right.
[1576.66 → 1584.94] We are back talking to Julius Bowles about Prometheus, the data monitoring system out of, well, kind of out of SoundCloud,
[1584.94 → 1588.46] maintained by some SoundCloud people, used by SoundCloud and others,
[1588.88 → 1592.34] and really making a name for itself in the industry.
[1593.00 → 1596.48] Julius, we want to talk to you about the details of Prometheus.
[1597.04 → 1601.42] You talked about some of the problems that you guys have run up against in different systems.
[1601.70 → 1605.42] And you obviously look to solve those problems with Prometheus.
[1606.26 → 1611.20] So maybe take us through the high-level points, and we'll dig down as we find them interesting,
[1611.72 → 1612.96] starting with the architecture.
[1612.96 → 1617.12] I know it's kind of hard without visualizations, but if you could lay it out in words,
[1617.40 → 1619.50] what are all the moving parts, and how do they fit together?
[1620.40 → 1620.74] Sure.
[1621.94 → 1625.70] I actually have the advantage that I have the architecture diagram in front of me.
[1625.94 → 1626.34] There you go.
[1626.36 → 1631.88] But if you as a podcast listener also want to view it, head over to prometheus.io
[1631.88 → 1634.62] and scroll down in the overview section.
[1634.62 → 1639.78] So I think the heart of Prometheus is the Prometheus server,
[1640.00 → 1644.60] which is really you run one or multiple of those in your company,
[1644.60 → 1648.32] and you configure it to scrape targets.
[1648.76 → 1651.34] So basically services that you're interested in.
[1652.14 → 1656.66] Prometheus is kind of believes in the church of pull.
[1656.84 → 1660.58] That means it pulls data rather than having data sent to it.
[1660.58 → 1664.72] And actually we should really go into why we decided to do that,
[1664.82 → 1667.08] because that's an interesting religious kind of point.
[1667.62 → 1669.22] But let's do that later, maybe.
[1670.00 → 1673.44] So you configure that server to scrape your services.
[1673.84 → 1677.74] And these services can be one of three different things.
[1677.74 → 1683.82] So it could either be your own service that you can instrument with one of our client libraries.
[1684.18 → 1693.70] And the client libraries allow you to expose things such as countermetrics, gauges, histograms, and summaries.
[1693.92 → 1700.32] The latter two are kind of hybrid metric types that give you either, you know, like bucketed histograms or quantiles.
[1700.32 → 1710.36] And so the client libraries give you programming language objects that allow you to track counter state and so on,
[1710.50 → 1712.86] and then also expose it over HTTP.
[1714.02 → 1718.38] And Prometheus server, the Prometheus server then comes by regularly,
[1718.64 → 1721.92] usually every 15, 30, or one minute or whatever you configure,
[1722.64 → 1726.92] and scrapes that endpoint, gets only the current state of the metric.
[1727.06 → 1728.56] So there's no history in the client.
[1728.56 → 1730.22] It only gets the current state.
[1730.32 → 1739.08] So let's say for a counter, it would just get how many requests have happened since this service instance started.
[1739.46 → 1740.76] And the counters never reset.
[1741.14 → 1747.94] So you could have two totally independent Prometheus servers scraping the same target and getting the identical data.
[1750.08 → 1754.84] And so Prometheus does that, stores these metrics locally in a local storage.
[1754.84 → 1764.64] I should say that currently, we only really, for the querying, we only really have a local on-disk storage.
[1764.86 → 1773.44] Our goal was to have single server nodes, which are completely independent of any other thing on the network.
[1773.44 → 1780.60] When things really go awry, and you need to figure out what's going on during an outage,
[1781.16 → 1789.76] you really can go to that one server and look at your metrics without having to depend on complex distributed backend storage and so on.
[1789.76 → 1798.66] We do have experimental support for writing to OpenBSD and InfluxDB at the moment.
[1799.04 → 1806.02] But it's not possible yet to read back from those through Prometheus, via Prometheus's query language.
[1806.16 → 1811.40] So if you want to get data out of those again, currently you would still have to then head to those other systems.
[1811.40 → 1813.20] But that's on the long-term roadmap.
[1813.38 → 1819.76] We definitely want to have a long-term storage that we can read back from.
[1820.22 → 1826.14] The local storage is good for a couple of weeks or maybe even months, maybe longer, depending on how much data you have.
[1826.24 → 1829.28] But it's not really meant as a forever storage.
[1830.26 → 1830.80] So that's how it stores.
[1830.80 → 1834.90] Is that just a simplicity decision just because you guys want it to be simple?
[1834.90 → 1840.70] Yeah, on one hand, it's much simpler to implement, of course, than a distributed system.
[1841.30 → 1849.60] And we also believe that through the simplicity, hopefully, you'll get more reliability out of this in the end.
[1849.70 → 1858.02] So if, let's say, you wanted to have HA, high availability, you would simply run two identically configured Prometheus servers,
[1858.34 → 1859.86] scraping exactly the same data.
[1859.86 → 1862.96] And if one goes down, you still have the other one to go to.
[1863.24 → 1865.12] But they're not clustered.
[1865.34 → 1867.20] So they're completely independent of each other.
[1867.60 → 1871.86] And if you want to investigate state during an outage, you just need one of them up.
[1872.04 → 1875.00] And you can go to either one and see what's actually happening.
[1876.78 → 1884.82] Okay, so normally instrumented jobs are one of the three types of things that Prometheus can collect data from.
[1884.82 → 1891.84] But you might also have something like a Linux host machine or HA proxy or Nginx,
[1892.34 → 1896.00] things that you cannot easily at least instrument directly.
[1896.12 → 1902.80] You probably wouldn't want to go into the Linux kernel and build a module that exports Prometheus metrics over HTTP, right?
[1902.80 → 1912.40] So for that, we have a set of export servers, we call them exporters, which are just basically little jobs,
[1912.58 → 1917.54] little binaries that you run close to whatever you're interested in monitoring.
[1917.90 → 1922.70] And they know how to extract the native metrics from that system.
[1922.70 → 1934.16] So for example, in the case of the host exporter, it would go to the proc file system and give you a lot of information about the networking and the disks and so on and so on.
[1934.78 → 1941.76] And these little exporters then transform what they collect locally into a set of Prometheus metrics,
[1942.00 → 1946.06] which they again expose on an HTTP endpoint for Prometheus to scrape.
[1946.76 → 1950.20] And that's how Prometheus can get information from these kinds of systems.
[1950.20 → 1954.46] And we have a lot of exporters for all kinds of systems there already.
[1956.10 → 1970.52] Finally, the third kind of thing you might want to monitor and which can be a challenge is things like batch jobs or things that are just too short-lived to be exposing metrics and to be scraped reliably by Prometheus.
[1971.36 → 1977.00] So in that case, let's say you have a daily batch job which deletes some users or so on.
[1977.00 → 1982.00] And you want to track the last time it ran successfully and how many users it deleted.
[1982.56 → 1991.34] For that, we have something called the push gateway, which is kind of the glue between the push and the pull world, which you're only really supposed to be using when you really have to.
[1992.10 → 2001.32] And the batch job could then push at the end of its run, usually these metrics, the last run and the deleted users to that push gateway.
[2001.32 → 2005.56] And the push gateway would simply hold on to those metrics forever.
[2006.36 → 2010.34] And the Prometheus server can then come by and scrape it from the push gateway.
[2011.44 → 2015.34] And yeah, so this is kind of the data ingestion side of things.
[2015.34 → 2026.76] In the architecture further there, so after the data is collected and stored, we can do two interesting things with the data.
[2026.88 → 2031.64] We can look at it as a human on the dashboard or directly on the Prometheus server.
[2032.30 → 2035.68] So for dash boarding, we have a couple of solutions.
[2035.68 → 2044.32] We have Prom dash, the Prometheus dashboard builder is really kind of a UI-based, click-based dashboard builder similar to Grafana.
[2044.78 → 2049.94] When I started building Prom dash, Grafana, to my knowledge, didn't really exist yet or not at all.
[2050.76 → 2053.38] But it's roughly comparable to that.
[2054.04 → 2059.58] But since then, Grafana now also has experimental Prometheus graphing support.
[2059.58 → 2071.14] And there's a third visualization option where you can serve dynamic HTML templates directly from the Prometheus server.
[2071.66 → 2076.98] That's kind of a power user use case where you can build any kinds of HTML-based dashboards.
[2078.12 → 2081.54] And these templates then have access to the query language of Prometheus.
[2081.54 → 2091.40] So they allow you to build even dynamic layouts depending on the data that you have in your Prometheus instance.
[2092.70 → 2094.06] So that's visualization.
[2094.92 → 2099.34] And then the last part that we do in Prometheus is alerting.
[2100.98 → 2106.78] So you have collected a lot of data now about all your systems, your hosts, and your services.
[2106.78 → 2111.52] And now you can actually make use of that data to see if something is wrong somewhere.
[2112.38 → 2115.02] To see if a batch job hasn't run for a while.
[2115.18 → 2120.44] To see if the request rate of some services are too low or errors are spiking up.
[2121.02 → 2127.24] And you can actually use the same powerful query language that you can use to display stuff.
[2127.50 → 2134.36] You can use the same language to formulate alert conditions under which people should get notified.
[2134.36 → 2142.74] And since you might have multiple of these Prometheus servers that each compute these alert conditions in the company,
[2143.00 → 2147.18] you might want to do some correlation between them and alert routing and so on.
[2147.24 → 2149.32] And that's better done in a central place.
[2149.84 → 2155.14] So you usually have one or a few alert managers in your company.
[2155.14 → 2158.38] That's a separate binary again that you usually run once.
[2158.38 → 2164.48] That all the Prometheus in your organization send currently firing alerts to.
[2165.62 → 2172.38] And the alert manager then can do things like inhibit one alert if another one is firing.
[2172.38 → 2184.52] It knows how to route alerts based on the key value dimensions on the alerts to specific notification configurations to specific teams and so on.
[2184.52 → 2191.68] And it supports a range of notification mechanisms like pager duty, email, Slack, and so on.
[2192.18 → 2195.74] So that's kind of the overall overview over Prometheus.
[2196.12 → 2198.12] Just one question on the visualization side.
[2198.22 → 2206.16] What's the purpose of having a separate, like the prom dash aspect and then also built-in graphing and querying?
[2206.92 → 2209.52] Is one for a certain use case and one for a different use case?
[2210.06 → 2210.64] Yeah, definitely.
[2210.64 → 2219.78] So the built-in graphing is really more useful for ad hoc exploration, really off data that is in one Prometheus server.
[2220.14 → 2227.72] And that's good, you know, even if your prom dash is down, and you really just want to see what's happening in one Prometheus server, you can go there.
[2228.02 → 2232.74] You can do very rudimentary graphing so it doesn't have all the bells and whistles that prom dash has.
[2232.74 → 2242.06] You know, like stacked, it does have stacked graphs, but it doesn't have like multiple axes, multiple expressions in one graph, different colour schemes and things like that.
[2242.06 → 2250.50] So it's quite simple, but it allows you, in the worst case, to still, you know, explore the data in that Prometheus server.
[2251.30 → 2253.20] And prom dash is really a dashboard builder.
[2253.34 → 2259.20] So that's for when you really want to persist a dashboard forever and for other people to see and to share.
[2259.20 → 2266.52] And especially it's very useful, let's say, I think in SoundCloud we have maybe roughly 50 Prometheus servers.
[2267.86 → 2273.44] And we have one central prom dash installation which just knows about all these Prometheus servers.
[2273.44 → 2285.30] And in there you can then have dashboards or even single graphs where you show time series or query expressions from multiple different servers in one graph.
[2286.54 → 2291.40] So, yeah, it's more of this nice wall dashboard use case.
[2291.64 → 2294.90] So the alert management would be part of the built-in UI.
[2296.20 → 2299.70] The configuration of your alerts and stuff would be what you'd use the built-in UI for?
[2300.76 → 2301.78] Or use prom dash for that?
[2301.78 → 2301.90] Yeah.
[2302.42 → 2309.08] So for alerting, that's actually part of, that's partially in the Prometheus server and partially in the alert manager.
[2309.30 → 2309.58] Okay.
[2309.80 → 2312.90] So in the Prometheus server you can define rules.
[2314.06 → 2322.24] Basically rules that, alerting rules that get executed, let's say, every 30 seconds or one minute commonly, depending on what you configure.
[2322.24 → 2332.70] And what happens there is that it really just executes a query expression and sees if there are any results from that expression.
[2332.86 → 2335.62] We maybe should go a bit into how the query language works.
[2335.62 → 2348.48] And if there are any results from that expression, they get transformed into labelled alerts and get transferred to the alert manager where they can then be deduped, silenced, rooted, and so on.
[2348.48 → 2362.18] And this is kind of interesting because this whole labelled key value data model goes all the way from the instrumented services to the storage, to the querying, and all the way to the alert manager.
[2362.18 → 2371.00] So you really have that chain of dimensional information to work with at every point in the chain.
[2371.64 → 2371.76] Yeah.
[2371.80 → 2376.06] I mean, it sounds like everything builds off the query language and the query language builds off of the data model.
[2376.62 → 2376.98] Exactly.
[2376.98 → 2388.42] So maybe the data model is probably the next place to dig in and tell us what it is, how it all works, and maybe if that's unique to Prometheus or something you took from somewhere else.
[2388.52 → 2391.82] Just go into the details on how the actual data is modelled.
[2392.58 → 2392.88] Sure.
[2393.90 → 2396.02] So Prometheus stores time series.
[2396.66 → 2405.06] And time series have a metric name, and they have a set of key value dimensions, which we just call labels.
[2405.06 → 2418.48] So you might have something like a metric name, HTTP requests total, which tracks the total number of HTTP requests that have been handled by a certain service instance since it started.
[2419.50 → 2421.92] But then you might be interested in drilling down, right?
[2421.94 → 2430.56] You would want to know which of these are get requests, which path handlers have been hit, and so on.
[2431.14 → 2433.20] And for that, you can use the labelled dimensions.
[2433.20 → 2443.46] So, for example, you might have method equals get on there, and you might have status equals 200 for the outcome, and so on.
[2444.02 → 2455.18] And these dimensions then get stored, and they allow you to query time series by these dimensions.
[2455.18 → 2460.96] So you could say, you know, sum over all the dimensions except the status code dimension.
[2461.10 → 2470.72] Then you would get the total number of requests over all your service instances, but keyed by the status code.
[2470.82 → 2472.36] So that dimension would be preserved.
[2472.80 → 2475.46] Or you could just select a specific dimension.
[2475.46 → 2484.82] Or you can even do, so let's say you have one metric, and you have all this kind of sub-dimensional instantiations of that metric.
[2485.22 → 2492.12] You know, one for method equals get, one for method equals put, and then under these you have, you know, the other labelled dimensions.
[2492.84 → 2497.72] So for one metric name, you actually get a lot of time series with all these different label sets.
[2497.72 → 2509.98] And now if I just query for just the metric name, I get all these time series back if I don't filter, if I don't aggregate, and so on.
[2510.58 → 2512.84] And that's actually, that can be very useful.
[2513.14 → 2523.30] So let's say on Bazooka, we have a use case where we have one set of these time series just describing for every instance running on Bazooka.
[2523.30 → 2526.36] What is the memory limit?
[2526.48 → 2530.78] How much memory can it use before the cluster manager kills it, right?
[2531.16 → 2536.20] And we have another metric called basically the current memory usage.
[2537.04 → 2549.60] And if we just have these two metric names, we can actually, in the query language, just put a minus in between them to subtract the current usage from the limit to get kind of the headroom.
[2549.60 → 2558.26] You know, the memory that they can still use before they would get killed, if we wanted to know, like, how well do instances utilize their memory.
[2558.60 → 2569.64] And what would actually happen if we just put a minus between these two metric names is that not only a single number, there's not only a single number on the left or a single number on the right.
[2569.64 → 2576.18] But you have these whole, let's say, vectors of time series on each side of this binary maturation.
[2576.78 → 2580.08] And they get matched on identical label sets.
[2580.74 → 2588.10] So the usage of one instance is matched with the limit of another instance and so on and so on.
[2588.10 → 2598.54] And in the end, as the output of the expression, you get, again, the current headroom per instance with all the dimensional labels still preserved.
[2599.18 → 2601.68] And, you know, you can go more fancy than that.
[2601.78 → 2603.68] You don't need to have an exact match there.
[2603.78 → 2613.64] There's like several language constructs that allow you to do one to N or N to one matches and so on and specify how exactly to match things.
[2613.64 → 2621.50] But this kind of vector-based matching algebra, I think, is quite unique to Prometheus, at least in the open source world.
[2622.36 → 2625.88] Yeah, so you give it a name and then a series of labels.
[2626.00 → 2635.28] And it sounds like the labels, that's what you refer to as the multidimensional aspect because each label you add a dimension to that particular time series.
[2635.80 → 2643.38] And then your guys' built-in querying for that construct is really where it gets, sounds like the flexibility is coming from.
[2643.38 → 2644.06] Am I following you?
[2644.78 → 2646.14] Yep, that's totally correct.
[2646.82 → 2648.96] And maybe one word of warning for the labels.
[2648.96 → 2658.80] They're really meant to be kind of dimensions, but they're not meant to be of arbitrary cardinality.
[2658.94 → 2671.98] So let's say if you wanted to store a user ID of a service with millions of users, you probably would not want to use a label value for that because you would suddenly get millions of time series for this one metric.
[2671.98 → 2680.66] So you really have to be aware of that every combination of labels on a metric creates one new time series automatically.
[2681.86 → 2686.50] And these time series are indexed and so on, and they need to be managed.
[2686.50 → 2705.06] So if you really want to have that kind of highly arbitrarily high cardinality dimensional insight, like storing email addresses or storing user IDs and so on, or the content of MySQL queries, the actual query string,
[2705.06 → 2719.64] then you're probably better served with something like a log-based system, InfluxDB or Elasticsearch and so on, that really can store individual events, individual things with arbitrary metadata.
[2719.64 → 2729.20] So I can see where the labels might get a little bit where there's better and worse practices with them.
[2729.36 → 2736.04] Whereas, you know, with a more just a key value name spacing thing, it's pretty easy to just come up with the next name.
[2736.10 → 2740.62] You drill down one dimension, but as you add dimensions, I can see where it gets difficult.
[2740.86 → 2742.90] And you're in fact warning against things not to do.
[2742.90 → 2747.62] Is there a place to go where it's like, hey, how would I do this in a typical situation?
[2747.90 → 2751.76] Because I think across many organizations, the type of metrics are similar.
[2752.14 → 2756.94] Do you guys have best practices or things you've learned at SoundCloud, the best ways to use Prometheus labels?
[2757.64 → 2758.20] Oh yeah, definitely.
[2758.56 → 2769.12] So we actually have a whole section on best practices at the very bottom of our website about metric and label naming and how to build good consoles, dashboards and alerting and so on.
[2769.12 → 2786.98] I think, yeah, one thing that really just sometimes happens at SoundCloud is that people mistakenly, either by not yet knowing the Prometheus data model well enough or just by making a simple mistake in the code, have set some of these label dimensions, let's say, to a track ID or a user ID.
[2787.68 → 2791.70] And that then creates, you know, millions and millions of time series.
[2792.46 → 2796.10] I mean, Prometheus, a single Prometheus server can handle millions of time series.
[2796.10 → 2806.14] But, you know, if you just overdo it a bit, and you're not careful about what you stick into label values, then you can really easily blow up a Prometheus server.
[2807.18 → 2812.94] And, yeah, so keep those label dimensions to sane, bounded things.
[2813.34 → 2817.80] So, you know, you always have Prometheus automatically attaches some of them anyway.
[2817.98 → 2821.20] So you get the name of the job, which is kind of the name of the service.
[2821.20 → 2822.98] It's just terminology, I guess.
[2822.98 → 2830.28] The name of the service, which we call job, the host and port of the instance by default.
[2831.02 → 2839.26] And that already gives you some dimensionality, even if you don't have any labels on the side of your service, right?
[2839.32 → 2847.06] So you at least get, if you have 100 instances, you get 100 time series for this one metric, which could be the number of HTTP requests.
[2847.06 → 2851.84] And then you have to multiply that by all the other dimensions that you add.
[2852.50 → 2858.56] And that can easily end up, for a single metric, you can easily get, you know, thousands or even ten thousand time series.
[2858.56 → 2863.08] Well, certainly lots of moving parts when we talk about Prometheus.
[2863.32 → 2870.46] So I'm going to assume that based on this conversation, so many people are like, I want to try it out.
[2870.76 → 2871.78] I want to get started.
[2872.50 → 2873.82] So we're going to take a quick break.
[2873.86 → 2876.48] And when we come back, we're going to talk about just that.
[2876.54 → 2877.26] We'll be right back.
[2877.26 → 2882.72] I have yet to meet a single person who doesn't love DigitalOcean.
[2882.92 → 2886.04] If you've tried DigitalOcean, you know how awesome it is.
[2886.32 → 2892.80] And here at the Changelog, everything we have runs on blazing fast SSD cloud servers from DigitalOcean.
[2893.32 → 2898.48] And I want you to use the code Changelog when you sign up today to get a free month.
[2898.48 → 2904.74] Run a server with 1 gig of RAM and 30 gigs of SSD drive space totally for free on DigitalOcean.
[2904.74 → 2906.92] Use the code Changelog.
[2907.16 → 2909.32] Again, that code is Changelog.
[2909.60 → 2911.24] Use that when you sign up for a new account.
[2911.66 → 2915.34] Head to DigitalOcean.com to sign up and tell them the Changelog sent you.
[2917.20 → 2921.70] All right, we're back with Julius Vols talking about Prometheus.
[2922.94 → 2927.44] And while we were on that break, we realized that getting started is a good step to go towards next.
[2927.44 → 2933.62] But we forgot we want to kind of go back a little bit on this religious piece of push versus pull when it comes to Prometheus.
[2933.62 → 2935.58] So Julius, why don't you lead us through that piece there?
[2936.44 → 2936.80] Sure.
[2937.46 → 2940.50] So this is funny because it's a bit of a religious thing.
[2941.34 → 2949.60] And push can be, you know, pull can be sometimes better, sometimes push is better, depending on the type of environment you're using Prometheus in.
[2950.98 → 2955.92] But one of our team members even wrote a blog post about push versus pull for monitoring.
[2955.92 → 2958.66] He's Brian from Dublin.
[2959.24 → 2961.30] And you can find that in our FAQ, actually.
[2963.02 → 2964.74] But I think some points are interesting.
[2965.08 → 2969.06] So if you do, so I think first let's start with one advantage of push.
[2969.32 → 2975.46] Push is really easy to get through firewalls if your monitoring system is easily reachable from everywhere.
[2975.46 → 2984.80] You know, you only need to make one point, one network point available on the Internet or in your local, in your company's network or whatever.
[2985.62 → 2988.82] And then everyone just needs to be able to push somehow to that.
[2989.68 → 3003.30] With pull, sometimes people run into the problem that, let's say, you know, if they have setups where they need to pull from various endpoints on the Internet, and they should be secured and so on.
[3003.30 → 3009.64] You know, they have to have a bit more, they need to now secure and make available N endpoints instead of one.
[3011.02 → 3016.80] So that's often what pains people when they can't use pull.
[3017.18 → 3030.18] But for us, especially in this kind of modern web company environments where you have your own data centres or your own virtual private clouds, and you have internally trusted environments where you can just pull from every target.
[3030.18 → 3033.58] And pull really has a number of advantages.
[3034.04 → 3045.94] So one thing that's really, really nice is that you can just manually go per HTTP to a target and get the current state of the target.
[3046.10 → 3055.92] So by default, if you go to a Prometheus endpoint on a service, you will get a text-based format that will tell you the current state of all the metrics.
[3055.92 → 3058.74] And you don't even need a server for that.
[3058.80 → 3059.98] So that's one nice thing.
[3060.90 → 3067.34] You can run a complete copy of production monitoring on your laptop or anywhere.
[3067.74 → 3073.48] You can just bring up a second copy of all of it to do experiments, to try out new alerting rules and so on.
[3073.76 → 3078.58] And that copy will get the exact same data as your production version of monitoring.
[3078.58 → 3084.20] Without you having to configure the actual services to send data somewhere else.
[3085.14 → 3097.34] And we kind of argued that if you're doing service monitoring and alerting, you kind of need to know, your monitoring system kind of needs to know anyway where your services live.
[3097.34 → 3100.60] And which services should currently be there.
[3100.78 → 3105.96] Because otherwise, it can't really alert you about a target being down or so on.
[3106.02 → 3112.72] Because it doesn't know if it should be gone, if it was provisioned, or if it's just crash looping, for example.
[3113.20 → 3119.72] So with that kind of argument, the monitoring system should be knowing what your targets are anyway.
[3119.72 → 3121.32] So the knowledge is already there.
[3121.32 → 3130.60] So that also makes it easier to pull the data and makes it easier to tell in monitoring and alerting whether a target is currently down.
[3132.02 → 3138.58] And yeah, so we don't think otherwise that it's like a huge issue whether you do push or pull.
[3139.08 → 3142.92] Especially in terms of scalability, it doesn't really matter that much.
[3143.88 → 3147.00] But yeah, it kind of depends on your environment.
[3147.00 → 3151.18] I think there would be some scalability aspects of pulling.
[3151.52 → 3153.38] You had more services, more hosts.
[3154.94 → 3158.88] I guess you had your Stated servers dropping UDP packets.
[3159.02 → 3164.16] It seems like catching UDP packets is a lot easier than going out and requesting data.
[3164.94 → 3166.98] Have you found in practice that that's just not a big issue?
[3167.86 → 3169.92] Yeah, so that's actually an interesting point.
[3170.04 → 3171.86] So that's really not an issue at all.
[3171.86 → 3176.76] So the actual pulling side of things has never been a bottleneck for us.
[3177.00 → 3186.44] But it's also very important to point out here that the whole fundamental way of how data is transferred is quite different in the Stated model to the Prometheus model.
[3186.44 → 3195.46] As I said earlier, in the Stated model, you send UDP packets basically proportionally to the amount of user traffic you get, right?
[3195.50 → 3199.60] Like for every HTTP request or every 10th or so on, you send a UDP packet.
[3199.84 → 3200.56] Please count this.
[3200.64 → 3201.18] Please count this.
[3201.26 → 3201.86] Please count this.
[3202.38 → 3208.82] Why don't you just increment a number in memory on your web server?
[3208.82 → 3214.12] And then every 15 seconds or so, you know, transfer the current counter state.
[3214.32 → 3215.74] So that's Prometheus's philosophy.
[3217.20 → 3223.46] The nice thing is there it uses way less traffic, like orders of magnitude less traffic.
[3223.46 → 3232.32] It uses less computation in the client, especially if you have services that, you know, do many thousands or even more requests per seconds.
[3232.52 → 3240.36] You might have some multicore high-performance rep routers which can do hundreds of thousands or more requests.
[3241.20 → 3247.18] And they're, you know, sending a UDP packet for every request would actually be quite prohibitive.
[3247.18 → 3257.54] And the other thing is that if these counter UDP packets in the Stated world get lost, you just get a lower total request rate displayed in your monitoring system.
[3257.62 → 3259.82] And you have no clue that these packets were actually lost.
[3260.80 → 3269.08] With the Prometheus model, if a scrape fails one time, it doesn't really matter so much because let's say the next scrape works.
[3269.36 → 3276.62] You will still not lose any of these counter increments that have happened because they are tracked on the service side, right?
[3276.62 → 3283.68] In every instance, these counters are just continuously incrementing from the start of the instance.
[3284.26 → 3287.20] And every time I come by, I just see what's the current state.
[3287.98 → 3298.32] And that's also a very good argument for not doing any kind of rate pre-computation on the service side, but doing that on the Prometheus server side.
[3298.52 → 3301.36] So in your service, really just count things up.
[3301.36 → 3308.98] Don't expose rates because let's say if you do expose rates, you know, there's just kind of a derivative of a counter.
[3309.70 → 3315.88] Then you might really, if you miss a scrape, then you might really miss a peak in a rate.
[3316.62 → 3324.58] And if you miss a scrape with a counter, you just get a bit less, a bit worse time resolution over that data.
[3324.58 → 3327.96] But you would never miss any increments of that counter after Y.
[3328.04 → 3328.32] That makes sense.
[3329.56 → 3336.92] That certainly makes sense on the theory of Y you go which path because on one side you can lose data, on the other side you're just kind of missing some time.
[3337.48 → 3337.82] Exactly.
[3338.20 → 3338.32] Yeah.
[3338.76 → 3340.10] And that was actually interesting.
[3340.68 → 3349.42] The way I fixed this whole Stated dilemma before we had Prometheus in SoundCloud was actually quite similar to what Prometheus is doing now.
[3349.42 → 3359.88] So I actually put a local Stated on every host where services were running and services were just sending local UDP packets to those Stats Ds.
[3360.64 → 3369.82] And then these local Stats Ds would pre-aggregate those counters over, you know, half a second or so and then send that resulting counter to the global Stated.
[3370.26 → 3371.92] So that's kind of similar.
[3372.06 → 3377.90] You're already kind of moving the aggregation to the individual hosts, but you're not having it in the same process.
[3377.90 → 3382.40] And Prometheus is even moving that into your process and into your memory space.
[3382.76 → 3388.16] And yeah, you don't need to create a network package just to counter request or something else.
[3389.28 → 3390.64] I don't know if that's interesting.
[3391.00 → 3395.30] There are other types of metrics that Prometheus supports besides counters.
[3395.52 → 3396.66] So we have gauges.
[3397.64 → 3402.62] Maybe I should go into what these are, depending on where you want to go now.
[3402.62 → 3408.20] I think it would be awesome to go that much deeper, but I think we're getting close to our time.
[3408.48 → 3411.62] So what I'd like to do is cap there.
[3411.86 → 3414.56] Maybe you will write an awesome blog post.
[3414.64 → 3416.06] We'll dive deeper into that or something like that.
[3416.06 → 3417.58] Or maybe we can have you back on at some point.
[3418.82 → 3421.56] But I think at this point, let's dive into getting started.
[3421.56 → 3426.30] So for those that are going to Prometheus and thinking, like, man, this is really awesome.
[3426.34 → 3427.22] I want to check this out.
[3428.16 → 3431.86] If you go into the documentation area, there's a getting started.
[3432.20 → 3434.48] I think that's actually what the button on the homepage takes you to.
[3434.54 → 3434.98] Is that right?
[3435.88 → 3437.32] The getting started button.
[3437.42 → 3437.70] Yes.
[3437.80 → 3438.50] Takes you right there.
[3438.50 → 3447.32] So if you go to Prometheus.io, and you click the button on the homepage, which says get started, you actually get started, which is kind of nice.
[3447.34 → 3454.58] But you get this really awesome guide, a Hello World style guide that sort of takes you through from zero to running a Prometheus server.
[3454.78 → 3459.08] So what is it like to get started, I guess, maybe moving away from other monitoring services?
[3459.42 → 3464.46] Can you walk through some of the pains potentially or the process to get started with Prometheus?
[3465.16 → 3465.42] Sure.
[3465.42 → 3472.44] I think one of the most consistent feedbacks we have gotten about Prometheus is how easy it is to get started.
[3472.62 → 3473.92] So that's actually quite nice.
[3475.00 → 3478.84] The reason is that Prometheus is written mostly in Go.
[3479.04 → 3480.90] I mean, the server is written completely in Go.
[3481.20 → 3484.22] There are client libraries for different languages and so on.
[3484.98 → 3495.34] But especially the server being written in Go and Go producing, you know, statically compiled binaries that you can just deploy on a machine without having to think about
[3495.34 → 3499.50] run times or shared libraries and so on.
[3499.72 → 3502.12] That makes it very easy to get started and deploy.
[3502.66 → 3507.40] We have pre-built binaries that you can download for the major architectures.
[3507.40 → 3522.60] It's also very easy with our make file to download all dependencies in a hermetically contained environment to just start building Go from head yourself or from some release version if you want to.
[3522.60 → 3525.82] You need to create a configuration file.
[3526.02 → 3528.42] There's one in the getting started guide here, of course.
[3529.02 → 3530.16] That's just one file.
[3530.44 → 3535.98] You point to it and then by default Prometheus will just store all your data in a local directory.
[3537.06 → 3540.50] And yeah, and it will just start scraping data.
[3540.70 → 3545.32] So you can, I mean, it takes roughly, if you're fast, it takes maybe five minutes to get started.
[3545.32 → 3548.22] And then you have a running Prometheus server.
[3548.84 → 3556.28] Of course, for that to be interesting, you need some example services that you can scrape and so on and there.
[3556.46 → 3560.24] Of course, it depends a bit on what you want to instrument.
[3561.56 → 3568.28] Prom dash is the one exception in the whole ecosystem which is not written in Go.
[3568.84 → 3571.36] It's actually a Rails application.
[3571.36 → 3575.50] But it's really more of a light backend.
[3575.66 → 3583.60] I mean, the whole Rails backend really only stores the dashboards as JSON blobs and could theoretically pretty easily be replaced by something else.
[3584.12 → 3586.64] All the logic is in the JavaScript frontend.
[3587.66 → 3592.10] And yeah, but we have Docker containers for everything as well, like for all the components.
[3592.10 → 3599.06] So if you really feel like, oh, I really don't want to set up Rails, you know, just use the Prom dash Docker container.
[3599.06 → 3601.82] And hopefully that will be less painful.
[3604.32 → 3605.80] And let's see.
[3607.34 → 3609.90] Yeah, but I mean, that's basically as easy as it is.
[3610.08 → 3617.24] You need to download the latest binary, unpack it, drop in a config file and just start it, and it's running.
[3617.24 → 3628.50] And by default, one of the default configuration files here is set up in such a way that Prometheus collects data on its own metrics exposition endpoint.
[3628.92 → 3634.20] So Prometheus instruments itself via one of the Prometheus client libraries.
[3634.40 → 3636.66] So it can monitor itself basically.
[3636.66 → 3644.14] So that's a nice use case to get started if you just want to look at some very simple Prometheus metrics without having any services.
[3645.00 → 3654.70] Another thing that's really nice to get started with is, because everyone has this, is the Node Exporter, which basically, by the way, has nothing to do with Node.js.
[3654.70 → 3656.72] But a host.
[3657.12 → 3660.58] So the Node Exporter is a host exporter.
[3660.70 → 3663.04] It exports host metrics.
[3664.54 → 3666.78] And that's a really nice thing to get started with.
[3667.26 → 3668.52] You just start it.
[3668.70 → 3673.68] You don't, I mean, you can set a lot of command line flags, but if you don't specify anything by default, it will do the right thing.
[3673.68 → 3680.74] And you configure Prometheus to scrape that, either statically or via some kind of service discovery.
[3681.72 → 3689.62] And yeah, and then you get host metrics about either your local machine or your data centre machines and so on.
[3689.76 → 3690.60] That's pretty easy, too.
[3691.14 → 3697.08] While we're talking about getting started, I've got to imagine that people are saying, okay, when I get started, I also want to have a community to sort of hang around.
[3697.32 → 3699.42] So you've got a Twitter handle, of course.
[3699.46 → 3700.70] You've got a mailing list.
[3700.78 → 3701.90] And you've got IRC.
[3701.90 → 3705.46] So those are three ways that people can hang out and sort of catch up.
[3705.60 → 3709.66] I was on the mailing list recently and just see that it's pretty lively and active.
[3710.08 → 3717.62] So when you're getting started, if you have any questions, then there's this mailing list to look at as well, which we'll link up in the show notes, of course.
[3718.70 → 3720.74] And definitely stop by the IRC channel.
[3720.84 → 3723.52] So we're there basically every day, very active.
[3723.94 → 3728.02] A lot of people are coming there asking questions, and we're always super happy to answer.
[3728.02 → 3733.44] And yeah, so that's kind of the fastest channel to reach us.
[3733.66 → 3738.34] And the mailing list is good for longer questions and more persistent communication.
[3739.92 → 3747.06] So it's Prometheus on Free node and then Prometheus Developers as a Google group, which we'll link out to.
[3747.12 → 3750.20] So you don't have to worry about trying to say that URL.
[3750.50 → 3751.18] That's not readable.
[3752.16 → 3753.18] That's not pretty.
[3753.78 → 3754.20] Which URL?
[3754.20 → 3754.40] Cool.
[3755.20 → 3758.70] Well, the Google group, it's not quite as easy to spread out.
[3758.70 → 3761.00] Yeah, you don't want to read that out in a podcast, no.
[3761.12 → 3762.38] No, that's boring.
[3762.80 → 3765.20] ChangeLog.com slash 168.
[3765.40 → 3766.86] You'll get all the links.
[3767.22 → 3772.78] We even found that blog post of push versus pull that he referenced, so we'll have that in there as well.
[3773.18 → 3773.34] Yeah.
[3773.40 → 3773.54] Yep.
[3773.92 → 3778.82] Or just head over to Prometheus.io, click on the Community tab, and you have all the channels there.
[3779.30 → 3779.66] That's true.
[3779.66 → 3782.36] And yeah, we're very, very happy about any contributors.
[3782.36 → 3790.80] And I think who we could especially use, because we're all back-end people, is someone who really likes doing front-end stuff.
[3791.70 → 3795.46] That's traditionally what's always lacking in these kinds of infrastructure projects.
[3795.88 → 3798.32] That's a good segue there, Jared, to the call to arms, then.
[3798.70 → 3799.10] That's right.
[3799.18 → 3799.72] Sounds like one.
[3799.72 → 3809.80] Julius, if you were going to request help or give a call to arms of the open-source community, would you say front-end developers is what we're after?
[3809.88 → 3811.98] What would you say to the open-source community, how we can help you out?
[3812.74 → 3818.48] Yeah, in general, it would be great to have more front-end interested people in the infrastructure world, right?
[3818.60 → 3820.62] And that goes for Prometheus as well.
[3820.62 → 3829.60] We've been coding a lot of the, you know, Prom Dash is very front-end-y and the graphing interface in Prometheus itself.
[3830.62 → 3838.70] But it would be really great to get people who feel like really strongly about infrastructure and nice front-ends.
[3839.28 → 3844.86] And help us, you know, refactor a lot of things there, improve the UI, make it shiny.
[3844.86 → 3848.92] That's definitely always a nice thing to have.
[3849.42 → 3851.82] But, you know, any other kinds of contributions are great, too.
[3851.94 → 3861.86] I think two of the areas that are currently still lacking and that will get the most attention in the future are the alert manager,
[3862.12 → 3870.64] which we are currently redesigning and re-implementing over the next months to be more production-ready and more powerful.
[3871.18 → 3874.46] But also some kind of long-term storage integration.
[3874.46 → 3879.98] So we have these ways of writing out data to currently OpenBSD or InfluxDB.
[3880.30 → 3888.54] But it would be really great to have a full read back implementation where you can query the long-term storage through the Prometheus server again.
[3889.14 → 3893.74] And, you know, if either someone wants to implement that for an existing backend system
[3893.74 → 3901.12] or wants to even maybe create a completely new Prometheus-specific long-term storage, that would be interesting as well.
[3901.12 → 3904.04] But there's a lot of stuff to do.
[3904.38 → 3912.76] Maybe head to the different issue trackers on the various Prometheus GitHub projects, which are all under GitHub.com slash Prometheus.
[3913.14 → 3916.04] And check out if there's anything that looks interesting to you.
[3916.90 → 3917.82] So there you have it.
[3917.84 → 3920.18] Sounds like lots of different ways to get involved.
[3920.18 → 3927.92] And while we're asking our closing questions, Julius, we would be remiss not to ask the one everybody loves, which is, who is your programming hero?
[3928.92 → 3930.76] I hoped you would not ask that one.
[3930.92 → 3930.98] Okay.
[3932.18 → 3932.32] No.
[3932.52 → 3932.72] Bjorn.
[3934.04 → 3935.02] Definitely Bjorn.
[3935.66 → 3936.52] There you go.
[3937.10 → 3941.60] Bjorn is one of my partners in crime on Prometheus.
[3941.60 → 3943.14] We're quite a bunch now, actually.
[3944.04 → 3952.80] Also, actually, this is funny because we also hired an intern right now who we are going to transform to be a full-timer at SoundCloud.
[3953.16 → 3955.24] And we found him through Prometheus contributions.
[3955.62 → 3957.74] And he's very young, like 23.
[3958.28 → 3960.74] And he outcomes me every day.
[3960.88 → 3963.14] He's very, very, very smart.
[3963.54 → 3966.62] And I actually am every day astounded by the…
[3966.62 → 3967.14] What's his name?
[3967.56 → 3968.16] Fabian.
[3968.16 → 3978.60] And, yeah, I'm every day astounded by the quality and the quantity of his coding, but also of his communication in the community.
[3979.30 → 3981.22] Really, really great person.
[3981.96 → 3992.40] I guess more in terms of traditional programming heroes, I guess when I was a child, I really was, like, had a bit of a coding crush on John Carmack.
[3992.40 → 3998.62] You know, with the early IT games in the 90s, Doom and so on.
[4000.12 → 4003.74] Definitely in the Go community, Rob Pike.
[4004.08 → 4009.64] And you probably have heard or even met at Go4Con about Dimitri Yoko.
[4010.98 → 4011.94] He's from Google.
[4012.06 → 4016.88] He's not really on the Go team, but he's on the Dynamic Tools team of Google.
[4016.88 → 4024.46] But he has contributed so many awesome, awesome features to the Go runtime and tooling around that.
[4024.64 → 4033.24] The race detector, the new tracing framework, this fuzzing framework that also just now found actually a bug in Prometheus' query language.
[4033.34 → 4033.80] Really great.
[4035.38 → 4042.86] And a lot of these really hardcore tools for getting, you know, dynamic information about your code.
[4042.86 → 4046.14] And he found hundreds of bugs with that.
[4046.24 → 4049.00] So I was really impressed when I heard about that.
[4049.10 → 4054.46] And he also gave a really great talk about that at Go4Con that I can highly recommend.
[4055.56 → 4058.04] Yeah, that was another one I didn't mention on top of the show.
[4058.36 → 4060.44] Ben Johnson and his open source database stuff.
[4060.92 → 4069.24] And then Dimitri, specifically his talk on Marion, like you just said, was one that everybody was kind of raving about as they came out of the conference room.
[4069.24 → 4073.08] So you're not the only one who thinks he's pretty awesome.
[4073.98 → 4074.14] Yep.
[4075.26 → 4076.02] All right, Julius.
[4076.16 → 4078.16] Well, it was great having you on the show.
[4078.30 → 4085.84] Definitely something we've been wanting to get you on the show before to talk about Prometheus and everything it's doing and what you're all doing at SoundCloud.
[4086.02 → 4088.14] So definitely fun having you on the show today.
[4089.42 → 4096.04] I want to thank our awesome sponsors for the show, Code Ship, Top Tile, and DigitalOcean, making this show possible.
[4096.04 → 4101.68] I also want to thank our awesome listeners and remind everyone that's not a member yet that we are member supported.
[4102.28 → 4108.60] You can join the community and get access to the members only Slack channel as well as many other awesome benefits of supporting the Change Law.
[4108.72 → 4110.82] Go to changelaw.com slash membership.
[4111.74 → 4120.06] And while you're there, you might as well sign up for Change Law Weekly and Change Law Nightly, which is our weekly and nightly emails, both respectively at slash weekly and slash nightly.
[4121.00 → 4122.16] Jared, what's the next week's show?
[4122.24 → 4124.00] We do have one show scheduled.
[4124.00 → 4125.14] What is that next week's show?
[4126.04 → 4128.10] I'm going to put me on the spot, man.
[4129.06 → 4131.36] I think it might be Ben Johnson.
[4132.72 → 4134.30] I know we've got a couple of databases.
[4135.10 → 4136.08] I know he's coming up.
[4136.42 → 4136.96] Give me two seconds.
[4139.20 → 4139.92] He's on August.
[4140.06 → 4141.80] He records on August 14th.
[4141.88 → 4145.32] So we'll have a show between him and now, but we don't know who it is.
[4145.38 → 4146.16] We don't know who it is.
[4146.20 → 4151.06] Okay, we're going to try and tease out what the next show is, but nonetheless, we have lots of awesome shows coming up soon.
[4151.06 → 4154.28] But until then, let's say goodbye.
[4155.18 → 4155.58] See ya.
[4156.04 → 4156.60] See ya.
[4156.76 → 4157.16] Thank you.
[4160.16 → 4160.56] Bye.
[4170.06 → 4170.62] Bye.
[4170.64 → 4170.74] Bye.
[4170.76 → 4172.24] Bye.
[4172.24 → 4172.68] Bye.
[4172.72 → 4173.22] Bye.
[4174.84 → 4174.90] Bye.
[4174.98 → 4176.78] Bye.
[4180.78 → 4181.18] Bye.
[4183.18 → 4184.26] Bye.
[4184.38 → 4184.44] Bye.
[4184.44 → 4214.42] I'm out.
