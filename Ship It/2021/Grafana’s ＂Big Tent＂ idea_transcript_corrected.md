[0.00 → 4.78] Hey, how's it going? I'm your host, Gerhard Lasso, and you're listening to Ship It,
[5.04 → 9.96] a podcast about getting your best ideas into the world and seeing what happens.
[10.28 → 16.04] We talk about code, ops, infrastructure, and the people that make it happen. Yes,
[16.26 → 20.62] we focus on the people because everything else is an implementation detail.
[21.06 → 25.98] I last spoke to Tom in Changelog episode 375 when I went to my first Rubicon.
[25.98 → 31.38] So many things changed since then. The one thing that didn't change is me using Grafana on a daily
[31.38 → 38.30] basis. But what is this new thing called Loki? And what about Tempo? While the 2021 Changelog.com
[38.30 → 44.18] setup uses Grafana Agent with Prometheus and Loki via Grafana Cloud, we don't use Tempo. Yet.
[44.58 → 48.78] By the way, are you curious to know how Grafana Cloud can offer such a generous free tier?
[49.26 → 54.90] Tom has a perfect answer. The solution is built into the Cortex architecture. And yes,
[54.90 → 58.98] Cortex is the reason why we have a VP of product on Ship It in the first place.
[59.38 → 63.76] Anyway, would you like to watch me and Tom pair and build Grafana dashboards like pros?
[64.12 → 69.04] Tom has this fascinating approach that I would like to learn too. We can either live pair
[69.04 → 74.18] or record and then publish the video. Let me know your preference via our Changelog Slack
[74.18 → 79.62] or just plain Twitter. Otherwise, I'll just pick one at random. I recommend that you listen to this
[79.62 → 85.20] episode in combination with episodes three and 11. That's the best way to get a more complete
[85.20 → 90.72] picture of the topics that we discussed today. Big thanks to our partners Vastly, Launch Darkly,
[90.84 → 96.88] and Linde. Our bandwidth is provided by Vastly, learn more at Fastly.com, feature flags powered by
[96.88 → 103.70] LaunchDarkly.com, and we love Linde. They keep it fast and simple. Check them out at linode.com
[103.70 → 104.90] forward slash changelog.
[110.90 → 116.64] What's up, shippers? This episode is brought to you by our friends at Fly. Fly lets you deploy your
[116.64 → 123.98] apps and databases close to your users in minutes. You can run your Ruby, Go, Node, Demo, Python,
[124.48 → 130.48] or Elixir app and databases all over the world. No ops required. Fly's vision is that all apps should
[130.48 → 135.02] run close to their users. They have generous free tiers for most services, so you can easily prove
[135.02 → 139.68] to yourself and your team that the Fly platform has everything you need to run your app globally.
[140.10 → 144.74] Learn more at fly.io slash changelog and check out the speed run and their excellent docs.
[145.14 → 148.50] Again, fly.io slash changelog or check the show notes for links.
[151.68 → 155.60] We are going to shift in three, two, one.
[155.60 → 174.62] Last time that we spoke, Tom, was at Rubicon 2019 North America. That was actually my first
[174.62 → 180.50] Rubicon in San Diego, and it was an amazing one. I loved it. This was actually changelog episode
[180.50 → 187.98] 3.75. And again, it was one of my favourites. That was almost two years ago. I know that a lot of
[187.98 → 193.86] things have changed. First, Grafana was at version 6 back then. Now it's at version 8,
[194.10 → 198.70] which was a massive improvement from version 7, which was a massive improvement from version 6.
[199.58 → 204.14] What other things changed in the last two years, almost two years since we spoke?
[204.38 → 208.68] Oh, wow. Yeah. I mean, two years. How do we cover two years in five minutes?
[208.68 → 215.40] I think working backwards, we've launched Tempo, the tracing system from Grafana Labs, which is
[215.40 → 222.02] kind of cool. Slightly different take on distributed tracing, focusing on very efficient storage of the
[222.02 → 228.12] traces itself and very, very scalable. We've done Loki 2.0, our log aggregation systems,
[228.64 → 232.96] over two years old now. And with Loki 2.0 came a much more sophisticated query language.
[232.96 → 238.16] That's really cool because now you can start to use Loki and anger and really kind of
[238.16 → 243.52] extract metrics and really dig into your logs with it. That was a really exciting design process
[243.52 → 248.56] for the language as well, because we always wanted it to be really heavily inspired by Prometheus,
[248.82 → 253.24] but it's logs in the end. It's different to time series. So we actually collaborated with
[253.24 → 258.98] Frederick from the Prometheus team. And he really influenced the design. I remember one of the calls,
[258.98 → 264.32] we came up with one of the things that I think makes Local really cool, which are you've got the
[264.32 → 269.88] pipeline operator for filtering logs. So you use pipelines to filter your logs. And we kind of stuck
[269.88 → 274.08] with that for everything in the log space. And then the minute you start working with metrics,
[274.36 → 278.54] you start using brackets, and it looks like Promo, like the Prometheus query language.
[278.84 → 282.68] And it just means you look at a query, and it's really obvious that that part of the query deals
[282.68 → 287.68] with logs and that part of the query deals with metrics. Working backwards more exemplars in Prometheus
[287.68 → 292.66] and in Grafana. So you can link from metrics to traces. You put little dots on the graphs and
[292.66 → 296.24] the dots indicate a trace, and you can click on it. And that whole kind of experience works.
[296.66 → 302.74] And you bring up Rubicon 2019, right? I think that was the year Frederick and I gave a keynote address
[302.74 → 311.36] on the future of observability. And in that keynote, we predicted that linking metrics and logs and
[311.36 → 316.52] traces and correlating and building experiences that combine them would be the future. Now, of course,
[316.52 → 321.22] it's like a bit of tongue in cheek because I have the great opportunity, and I'm very lucky to be able
[321.22 → 325.72] to influence what we do at Grafana Labs. So, you know, we've kind of spent the last two years making
[325.72 → 331.78] that keynote happens and making it possible to combine those metrics and logs and traces in a
[331.78 → 335.12] single development experience, in a single on-call kind of instant response.
[335.66 → 340.96] I could go on. Like there's so many things that have changed, right? We've grown hugely at Grafana Labs.
[340.96 → 348.18] We're now over 400 people, which is just like I joined when we were about 25, 26 people three and
[348.18 → 354.68] a half years ago. So we launched a GEM, Grafana Enterprise Metrics, which is our kind of self-managed
[354.68 → 360.38] enterprise version of Cortex, the scalable version of Prometheus, the other CNCF project.
[360.74 → 364.60] Yeah, there's so many. And I'm really still only talking about kind of the second half of last year.
[364.60 → 368.88] And I guess, you know, when you ask that question, everyone always responds with pandemic as well.
[369.26 → 373.28] I kind of glossed over that, but we had a global pandemic. I think what's fascinating,
[373.34 → 378.80] obviously, is huge impact, but Grafana Labs was set up from day zero to be remote first.
[379.44 → 384.66] And so I think we've been super lucky that the impact has been less than it has been on other
[384.66 → 389.08] organizations. Yeah, like I could go into any more of those, but I'll stop there.
[389.08 → 393.70] Yeah. I think I remember that the future of observability keynote that you gave,
[393.94 → 399.86] that was a perfect one, inspirational one. And I could see it. I could see it just as like
[399.86 → 405.78] the vision that you shared. And I remember thinking, wow, if they pull it off, this is going
[405.78 → 410.28] to be amazing. And guess what? You did. And even more so.
[410.34 → 413.34] I can't take all the credit, right? Like we did, I did the keynote with Frederick.
[413.54 → 417.70] When I tell you, I mean Grafana Labs, like, you know, the whole org, right?
[417.70 → 422.96] That you're part of the whole team that you're part of. But you like, you know, you were there,
[423.44 → 427.90] you had this vision, you shared it. I'm sure everybody contributed to it. And then everybody
[427.90 → 434.12] made it happen. And I really love that journey, seeing how things have been happening with Loki.
[434.20 → 440.32] I remember when Loki version one came out, and I thought, wow, this makes so much sense. I was so
[440.32 → 445.14] keen to start using it. And we did, even for changelog. We used Grafana for a long time,
[445.14 → 451.32] Prometheus. Then we went to Loki and that was great. And then we thought, hmm, if only we could
[451.32 → 456.84] delegate this problem to someone else. And guess what? Grafana Cloud came along, the hosted managed
[456.84 → 462.32] service. You had some very generous tiers. Once that changed, everything changed. So all of a sudden,
[462.38 → 465.88] we no longer had to run our own Grafana and Prometheus. Not that it was difficult,
[465.88 → 472.94] but it's much easier to just run the Grafana agent. That's all you need. Send everything to
[472.94 → 479.80] Grafana Cloud, and it just works. And with the last changes of the alerts, like I think that was the
[479.80 → 484.72] weak point of Grafana for a long, long time. And now you saw that as well. So there are all these
[484.72 → 490.98] things just falling into place naturally and being able to know what's coming and seeing it happening
[490.98 → 496.30] every six months, right? There's like more and more and more. It's like, we know what to expect.
[496.76 → 499.86] You're delivering. Please carry on. That's what I'm thinking.
[500.54 → 504.52] Thank you very much. Yeah. You know, I miss so much out of my what's happened because yeah,
[504.66 → 511.42] unified alerting is a huge step in the Grafana story. I'm really pleased as the way the company
[511.42 → 515.22] came together. We used to have two alerting systems, right? We had the Grafana alerting system
[515.22 → 519.06] and the Prometheus alerting system. And they were worlds apart. You know, on one hand,
[519.06 → 523.22] the Grafana alerting system is probably the easiest one that exists out there, right? It's very
[523.22 → 527.50] accessible, very easy to get started with. And on the other hand, the Prometheus system is probably
[527.50 → 532.20] one of the most sophisticated and powerful ones. And so I think it was really exciting, right? How
[532.20 → 537.64] the team could combine the power of the Prometheus system, right? With multidimensional alerts,
[538.22 → 543.66] with alert managers, routing, grouping, and deduping, and silencing, and bundle all these features
[543.66 → 549.52] into Grafana in a way that makes them easy to use and gives you that level of user experience
[549.52 → 554.66] that people have come to expect. And best of all, like we haven't duplicated any features,
[554.72 → 559.08] right? We're just using Alert Manager under the hood. We're using the same API as Prometheus
[559.08 → 564.38] under the hood. So it's true to our open source routes as well. And that's like, the team did a
[564.38 → 569.98] fantastic job with unified alerting. I think the thing you say about cloud, right? The generous free
[569.98 → 574.40] tier, for instance, we launched that in January, I think. We've always had a kind of free tier.
[574.66 → 579.62] We've always allowed you to have a free Grafana instance, for instance. The work that goes into
[579.62 → 584.32] actually being able to offer a free tier, there's so much going on behind the scenes,
[584.38 → 588.86] right? Just at a very architectural level. The point I'd always make here is that
[588.86 → 595.80] you need the marginal cost of a new Prometheus instance, or of a new Loki instance, or a new
[595.80 → 599.96] Tempo instance. You need it to be effectively zero, right? You can't offer a free tier unless
[599.96 → 604.38] the cost of the thing you're offering is as close to zero as possible. So this means
[604.38 → 609.00] behind the scenes, right? We can't be spinning up a new Prometheus pod, or a new Loki pod,
[609.10 → 613.80] or a new Grafana pod, or a new Tempo pod for every customer that signs up, right? That would
[613.80 → 619.54] get too expensive for us to offer it. We're not that big a company yet. And so fundamentally,
[619.68 → 623.52] the architecture of all of these systems has to be multi-tenanted, right? And we've built,
[623.86 → 626.62] and this is where Cortex comes in, right? We've built this horizontally scalable,
[626.62 → 632.40] multi-tenant version of Prometheus, which means provisioning a new instance in that multi-tenant
[632.40 → 636.56] cluster is basically free. It doesn't really cost us anything. I mean, once you start sending
[636.56 → 641.26] metrics, there's some cost incurred, but because it's multi-tenanted, we can start to take advantage
[641.26 → 645.82] of kind of statistical multiplexing techniques and really get to a point and really drive down
[645.82 → 649.82] the cost of offering that service, which allows us to make the free tier so generous.
[649.82 → 655.68] And that architecture has been replicated in Loki. Well, not replicated. It uses the same code.
[655.76 → 660.52] It uses the same module system, the same ring, the same architecture, and the same techniques
[660.52 → 668.22] in Loki and in Tempo. And that consistency across the offerings just also carries over to the kind
[668.22 → 672.80] of operational and cognitive burden of running this because it's the same, because you scale it in
[672.80 → 677.70] the same way, and you do instant response in the same way. So yeah, it's incredibly exciting to
[677.70 → 683.60] finally feel like you're in the last mile of delivering on a vision that's been in progress
[683.60 → 688.00] for kind of five or six years. So everything that you've said makes a lot of sense to me,
[688.16 → 694.90] but I know that many people will be confused because you are VP of product. How on earth does a VP of
[694.90 → 700.90] product know so many things about code and how things actually work? And I know that you're one of
[700.90 → 705.52] the Cortex co-authors, right? You've started Cortex. I don't know who the other author is.
[705.52 → 711.30] It was Julius actually from the chap who was one of the original founders of the Prometheus project.
[711.68 → 712.30] Julius Waltz?
[712.64 → 713.24] Julius Waltz.
[713.56 → 721.94] Right. Okay. So you and Julius, you started Cortex, which went to grow. And I think it's part of the
[721.94 → 727.22] very important component of Grafana Cloud as an engine, an inspiration for Loki, which I think
[727.22 → 731.24] you also had something to do with, right? Like when you started the code base. So how does that work?
[731.24 → 736.68] How can you be VP of product and code go at a very advanced level? How does it work?
[737.10 → 742.92] Titles in the abstract, pretty meaningless, right? So yes, my title is VP of product. And I do have a
[742.92 → 747.74] lot of kind of product management responsibilities in the company, but my background is a software
[747.74 → 753.84] engineer. I've been a software engineer now for 15, 16 years. I've always worked on open source code
[753.84 → 758.52] bases, you know, straight out of university. I was kind of tangentially involved in the Zen
[758.52 → 763.38] hypervisor project. And so I worked a little bit on the kind of control tools there. I started a
[763.38 → 768.76] company that got involved in the Cassandra distributed database. And then, you know, then
[768.76 → 774.54] worked on Prometheus and Cortex. I've just always been a software engineer. I took a brief stint as
[774.54 → 779.42] doing some engineering management at Google, also some site reliability engineering, where I kind of
[779.42 → 784.34] learned a lot about the whole monitoring side of things. But yeah, at the end of the day, I've always
[784.34 → 789.76] been a software engineer. I've always been passionate about this kind of thing. And it's just, you know,
[789.76 → 795.58] I don't get to do as much software engineering now as it perhaps seems. You know, I have a large team
[795.58 → 800.08] of software engineers who do that and really should take a lot more of the credit than perhaps I do.
[800.52 → 805.48] But yeah, I still, you know, I was doing, I did a few PRs yesterday. That was mostly on some kind
[805.48 → 810.72] of continuous deployment for some internal SLO dashboards. But I still, you know, I still try and
[810.72 → 815.26] write bit of code. We had a hackathon recently internally where everyone in the company took a
[815.26 → 820.70] week to kind of just code on whatever their imagination had been, you know, noodling over
[820.70 → 825.66] for the past few months. And I took part. That was like, that was pretty cool. I managed to get a
[825.66 → 829.04] couple of days of solid coding in. I'm not going to tell you what the project was though, because
[829.04 → 834.68] that might become a future product. Who knows? Interesting. I was just going to ask that if any of
[834.68 → 840.30] those projects are public, but I'm sure the good ones will be, right? Oh, yeah. No, no. Some of them are,
[840.30 → 846.14] right. So Bjorn and Dieter and Ganesh were working on one of their hackathon projects was
[846.14 → 850.38] high definition histograms in Prometheus. And Ganesh has already tweeted about that and will
[850.38 → 854.60] be putting out more information and the codes out there in public. I've seen that. There's a few of
[854.60 → 859.62] them that are public and a lot of them are going to form future projects and potentially even future
[859.62 → 864.92] products. I can give you a bit of a hint what the project I was working on was. So not a lot of
[864.92 → 870.60] people know Grafana Labs, actually its first kind of time series database that it built for Grafana
[870.60 → 875.78] Cloud. It's called Metric Tank. Metric Tank is a graphite oriented, still written in Go,
[876.30 → 880.44] still using a lot of the same techniques from modern time series databases like the guerrilla
[880.44 → 886.48] encoding and so on, but mainly focused on building a kind of scalable multi-tenant cloud version of
[886.48 → 891.44] graphite. And that's what kind of bootstrapped Grafana Cloud before I joined the company.
[891.44 → 896.86] And then I joined and brought Cortex in with me. And since then, of course, the architecture has now
[896.86 → 901.58] kind of moved towards a Cortex style architecture. The Metric Tank team within Grafana Labs for the
[901.58 → 908.04] past year or so have actually been working on putting a graphite query engine on top of Cortex.
[908.72 → 912.12] And we've actually, I think the launch of that, you know, it'll be seamless launch. Customers
[912.12 → 917.34] shouldn't notice, right, that being moved off of Metric Tank and onto Graphite V5. That's actually
[917.34 → 922.12] happening very soon. And that's kind of to give you a bit of a hint in the direction we're going. Now,
[922.56 → 926.56] Grafana Enterprise Metrics and Grafana Cloud is a single time series database that you can query
[926.56 → 931.56] through multiple different query languages. That's fascinating. And now you reminded me
[931.56 → 938.84] the link between Lacuna Analytics, the company that you were part of at some point, and the startup that
[938.84 → 942.92] I was working for at the time, which was Go Squared, which was like real-time visitor analytics.
[942.92 → 948.90] So Go Squared, we were using, I think, MongoDB heavily, and we were starting to look into
[948.90 → 952.92] Cassandra. There was a Cassandra conference, and I thought you were presenting the analytic
[952.92 → 960.56] side of things. And at the time, I was heavily invested in Graphite. Ganglia are there as well.
[960.72 → 960.90] Yeah.
[961.02 → 965.88] And I thought like, wow, this Graphite and scaling, those like fun days, challenging days.
[966.54 → 970.72] And I looked at Lacuna, I thought, wow, this is interesting. So they're using Cassandra
[970.72 → 974.52] for the metrics, and it works really well. I remember even the demo that you gave.
[974.88 → 978.48] I forget the conference name. This was 2012, 2013.
[979.04 → 980.28] Yeah, I don't remember that then.
[980.28 → 985.90] A long time ago, something like that. Yes. And so Graphite, right, was a great system,
[986.04 → 990.76] but it didn't really scale. It was very problematic. And then Grafana came along,
[990.86 → 995.32] but Grafana on top of Prometheus. So Prometheus had something new with it. But Prometheus in its
[995.32 → 1001.32] incipient phase was, again, like single process, single instance. How do you scale that? Well,
[1001.40 → 1008.56] it's not as easy. And Cortex, as far as I know, scales the way anyone would expect, right? You can
[1008.56 → 1013.32] shard those metrics, you can replicate them, you have different backends for them. That was really,
[1013.48 → 1019.54] really nice. So I can see history in a way repeating itself with Prometheus and Graphite.
[1019.54 → 1024.62] And now I can see the link, right, where it's actually part of Cortex, or it will be part of
[1024.62 → 1028.24] Cortex. That's really fascinating. Well, so it's interesting you mentioned that, right? Because
[1028.24 → 1031.58] one of the things Acute did, one of its contributions to the Cassandra project
[1031.58 → 1036.42] was a technique called virtual nodes, right? Which is where in the earlier versions of Cassandra,
[1036.60 → 1040.78] each node basically owned a single range in its distributed hash ring. I remember that.
[1040.94 → 1044.36] The technique that Acute added, and has been in Cassandra for ages now,
[1044.66 → 1048.32] was the ability for a node to own multiple ranges, right? And the whole principle there being,
[1048.32 → 1053.00] once you can own multiple ranges, like hundreds, like you then just pick them at random,
[1053.36 → 1057.88] and you achieve a very good statistical kind of load balancing. What's maybe particularly
[1057.88 → 1063.42] interesting is exactly the same techniques in Cortex, in Loki, in Tempo. And that's the ring I was
[1063.42 → 1068.70] referring to earlier. This is like, it's basically just an almost identical copy, just in Go,
[1069.20 → 1070.36] of the Cassandra hash ring.
[1070.98 → 1074.86] This makes me think of the old Go Square team, because I remember Cassandra and how they were like,
[1074.92 → 1078.30] so excited about this. And this was mentioned, like, wow, this is amazing.
[1078.32 → 1085.36] Like MongoDB, I think rather Cassandra. I remember that. And it wasn't even like version one at the
[1085.36 → 1091.06] time. I know that Netflix were big on it as well. And Adrian Cockcroft had like a great talk about it.
[1091.20 → 1096.92] And like in that context, the AWS cloud came in. So many threads connecting in my head right now.
[1097.32 → 1104.08] Wow. Okay. So let's take a step back from all these, I want to say rabbit holes, but like reminiscing
[1104.08 → 1110.40] specific things, which are a thing of the past. And let's come back into the present with a question,
[1110.40 → 1115.74] which I know very many people are, I'm not sure what they're struggling with, but they are, you know,
[1116.30 → 1122.82] there are two sides to them. What is observability? Some say that it is not the three pillars, which is
[1122.82 → 1128.10] metrics, logs, and traces. Some say that's not what observability is. What do you think? What is
[1128.10 → 1133.08] observability to you, Tom? I mean, it's definitely a bit of an industry buzzword right now. The three
[1133.08 → 1137.92] pillars definition is not that useful as a definition, right? It doesn't really describe
[1137.92 → 1142.18] what you're trying to do or what the problem you're trying to solve. It more describes maybe
[1142.18 → 1147.48] how you're solving some other problem, right? So whilst I don't necessarily think it's wrong,
[1147.74 → 1153.36] like in a lot of places, in a lot of situations, observability does revolve around metrics and logs
[1153.36 → 1159.10] and traces. It's not an answer to the question, what is observability? I've always really liked
[1159.10 → 1166.12] the definition of observability is, you know, the name for the movement that is like helping
[1166.12 → 1172.18] engineers understand the behaviour of their applications and their infrastructure. It's about
[1172.18 → 1178.50] any tool, any source of data, any technique that helps you understand how a large and complicated
[1178.50 → 1185.80] distributed system is behaving and helps you analyze that. That's really my preference. I don't
[1185.80 → 1189.28] necessarily think I speak for many people though when I say that. I've been thinking about this for
[1189.28 → 1193.68] a couple of years. I had a couple of interesting discussions. Even the episode before this, that's
[1193.68 → 1198.14] a fascinating one. If this is the first one that you're listening to, check that out, see,
[1198.28 → 1205.80] you know, how the two compare for you. But I also agree that being curious about how things behave,
[1205.80 → 1209.82] I think that's like the first requirement for observability. Are you curious? Do you care?
[1210.38 → 1216.08] And if you care, great. So what are you going to do to understand your production or your system?
[1216.14 → 1219.48] It doesn't have to be production, but it typically is because that's where the most interesting
[1219.48 → 1226.42] things happen. So how do you do that? How do you take all those metrics, logs and traces or events,
[1226.66 → 1230.10] whatever you call them, it doesn't really matter, to understand how the system behaves?
[1230.50 → 1234.74] It's an interesting kind of way of phrasing it, right? Because what I think, what we really
[1234.74 → 1241.36] internalize at Grafana Labs is kind of avoiding a one size fits all solution, right? So I know there
[1241.36 → 1245.76] are some incredibly powerful solutions out there that are incredibly flexible, but at the end of the
[1245.76 → 1250.38] day, we internally call it this kind of big tent philosophy, right? Where we try and embrace multiple
[1250.38 → 1255.06] different solutions and multiple different combinations of solutions and really kind of focus
[1255.06 → 1260.72] on helping users get the best out of a wide variety of techniques. Because really, you go into any
[1260.72 → 1266.04] sufficiently large organization, it doesn't even have to be thousands of people, like even just hundreds
[1266.04 → 1271.36] of people. And there's going to be one team over there that uses one monitoring solution and a team over
[1271.36 → 1276.48] there that uses a different logging solution. And they're all going to be stuck in their own little silos, and they're
[1276.48 → 1281.80] all going to have their own, you know, tools to use to analyze their data. And really, what we're trying to do at
[1281.80 → 1286.82] Grafana is brought them all together into a single place and give them all the same experience. The way I've always
[1286.82 → 1291.46] thought about it is, you know, when you get paged in the middle of the night, I don't want a system to
[1291.46 → 1295.08] tell me necessarily what's wrong, because the reality is, if the system can tell me what's wrong,
[1295.34 → 1298.66] it should probably be able to fix it for me. And I probably should have thought of it ahead of time,
[1298.78 → 1302.64] and it probably should never have paged me. I only ever really want to get paged for things that I
[1302.64 → 1307.42] wasn't expecting, right? And therefore, you know, I want to engage that kind of creative part of my brain.
[1308.06 → 1314.18] And I want to come up with hypotheses as to why it's broken, right? And I'm going to, and then I want tools
[1314.18 → 1320.44] that help me test those hypotheses and develop new hypotheses. So really, I'm not looking for a tool
[1320.44 → 1326.06] that claims to automate kind of root cause analysis, or, or tell me exactly what's broken,
[1326.06 → 1329.88] because, you know, if it can do that, it probably shouldn't have broken in that,
[1330.06 → 1335.24] in that particular way. I'm looking for a tool that helps me test theories that I've got. Oh,
[1335.72 → 1339.46] is it broken because of this? Oh, I can, I can correlate some metrics and some logs,
[1339.46 → 1346.28] and I can see if that's the case. Is it broken because there's a tiny little service running on a
[1346.28 → 1350.14] computer under someone's desk that's gone down? Oh, I can go and look at a distributed trace and
[1350.14 → 1354.72] it will tell me if that's the case. Like I want a tool that helps me access data and test hypotheses.
[1355.22 → 1360.52] And the nice thing I think about that as a guiding principle is it doesn't say, well,
[1360.62 → 1364.54] the best way of doing that is with logs. It doesn't say the best way of doing that is with events.
[1364.54 → 1369.78] And it doesn't say the best way of doing it is with metrics. It says the best way of doing it is
[1369.78 → 1373.54] situational and depends on the problem and depends on the tools you've got available.
[1373.92 → 1374.68] That's great.
[1374.68 → 1394.90] This episode is brought to you by our friends at Launch Darkly, feature management for the modern
[1394.90 → 1400.32] enterprise, power testing in production at any scale. Here's how it works. Launch Darkly enables
[1400.32 → 1405.54] development teams and operation teams to deploy code at any time, even if a feature isn't ready
[1405.54 → 1410.24] to release to users. Wrapping code with feature flags gives you the safety to test new features
[1410.24 → 1415.48] and infrastructure in your production environments without impacting the wrong end users. When you're
[1415.48 → 1419.68] ready to release more widely, update the flag status and the changes are made instantaneously
[1419.68 → 1424.82] by the real-time streaming architecture. Eliminate risk, deliver value, get started for free today
[1424.82 → 1428.32] at LaunchDarkly.com. Again, LaunchDarkly.com.
[1430.32 → 1443.76] I really liked your last answer. And I think now is a great time to start looking at the Grafana
[1443.76 → 1451.04] ecosystem, the Grafana Labs Cloud, just because Grafana means many things. How would you solve
[1451.04 → 1457.30] specific problems with the tools that you have available in Grafana? So let's take a specific
[1457.30 → 1465.30] example. Let's imagine that sometimes, my website, some of the requests are slow. What
[1465.30 → 1470.74] would I do to understand why certain requests are slow? Let's imagine this is a monolithic application,
[1470.74 → 1476.42] changelog.com. I'm winking right now. It's a Phoenix app. So what would I do?
[1476.42 → 1478.18] Actually, I don't know what Phoenix is.
[1478.74 → 1483.46] It's a framework similar to Ruby on Rails, but it's based on Elixir, which is
[1484.18 → 1488.02] syntax is similar to Ruby, but it's really all running on the Erlang VM.
[1488.74 → 1489.22] Oh, wow.
[1489.22 → 1490.66] So it's like Ruby on Rails.
[1491.22 → 1496.02] Is that a particularly large user base? It seems very nice. I've not heard of that before. Cool.
[1496.02 → 1500.82] Right. So not necessarily. I mean, depending on what you mean by large,
[1500.82 → 1503.06] but it scales really well because it's the Erlang VM.
[1503.06 → 1504.26] Yeah, because it's Erlang. Yeah.
[1504.74 → 1506.10] Everything is message passing.
[1506.10 → 1506.58] Sweet.
[1506.58 → 1512.34] You can have a cluster. It clusters natively. It forms a cluster. Furthermore, it starts sending messages.
[1512.34 → 1518.74] I think one of the more popular apps that uses Erlang is WhatsApp. Everybody knows. Everybody uses.
[1519.30 → 1524.02] And RabbitMQ is another messaging queue that also uses the same Erlang VM.
[1524.02 → 1531.30] And I think the last one is React. It was like the database. I think it still exists. And it was by
[1531.30 → 1531.78] Basho.
[1531.78 → 1532.34] By Basho.
[1532.34 → 1535.78] I remember it was like in the same quadrant, right? Where Lacuna Analytics was there.
[1535.78 → 1541.70] Manu was there. I think he was their managing director for the EU team. And he was at Lacuna a
[1541.70 → 1542.34] long time ago. Yeah.
[1542.34 → 1544.58] There you go. So it's a small world, isn't it?
[1544.58 → 1548.74] I think he's now at one of the cryptocurrency companies, but yeah, sorry, unrelated.
[1548.74 → 1552.58] So coming back to this like Phoenix app. So the reason why I mentioned that it's a monolithic
[1552.58 → 1556.82] app. It's important because it's not microservices, right? You don't have HTTP calls or
[1556.82 → 1561.86] GRPS. There's no such thing. It's a single app. It's a monolithic app. Furthermore, it talks to a database. Furthermore, it
[1561.86 → 1566.98] has an Ingress Nginx actually in front. There's like a load balancer. And then in front of that,
[1566.98 → 1571.62] you have a CDN. So the request comes, and this is like very specific, and maybe this will help.
[1571.62 → 1577.94] The request goes through a CDN quickly. It hits a load balancer, which is a managed one,
[1577.94 → 1584.42] like your LB, whatever, the equivalent of that. Then it goes to Ingress Nginx. And then from Ingress
[1584.42 → 1590.26] Nginx, it gets proxy to the right pod. Well, service pods, I don't have to start decomposing
[1590.26 → 1594.74] this. And eventually it hits the database, and then it comes back in again. At any one point,
[1594.74 → 1601.22] it could be cached. Sometimes requests are slow. Why? How would we find out with the tools that exist
[1601.22 → 1606.58] in the Grafana ecosystem world? No, it's a great question. So you already know that requests are slow.
[1606.58 → 1610.90] So that's kind of interesting. I'm going to guess, or for the sake of this discussion,
[1610.90 → 1615.38] that you've been told by your users that your requests are slow. So I would actually say,
[1615.38 → 1620.34] first things first, let's kind of confirm that. We want to instrument the system. We want to get as
[1620.34 → 1627.22] many useful metrics as we can out of it. You mentioned in LB there, for instance, we put the
[1627.94 → 1632.18] CloudWatch exporter on there and get the LB metrics out into Prometheus. Now you can do that with the
[1632.18 → 1638.26] open source exporter. We're also working on a service in Grafana Cloud where effectively we run
[1638.26 → 1642.74] and manage that exporter for you just to reduce the number of things you need to run. This will give
[1642.74 → 1647.46] you access to some rudimentary metrics, but generally I don't find CloudWatch metrics to be super useful.
[1647.46 → 1652.26] I'm sorry, that was a bad example. So I gave an analogy. It's actually a Linde node balancer. I'm
[1652.26 → 1655.70] pretty sure you don't think to agree with that, but it's like a managed HA proxy.
[1655.70 → 1661.54] I wouldn't underestimate the Prometheus ecosystem. There's probably an exporter for Linde metrics
[1661.54 → 1666.26] that import them into. And if there isn't, there will be by the time you finish this recording,
[1666.26 → 1667.14] I imagine. I hope so.
[1667.14 → 1670.58] Yeah. So I get metrics on the load balancer because it's always good to start at the very edge.
[1670.58 → 1672.18] The CDN is first. What about the CDN?
[1672.18 → 1677.46] Yeah. I don't know enough about Vastly, I'm afraid to really comment, but I'm sure there's some way of
[1677.46 → 1683.22] getting logs or metrics from that. Okay. So we've hit something which I wasn't expecting to hit,
[1683.22 → 1689.06] but let's just go with it. Okay. I looked at integrating Vastly logs with Grafana Cloud.
[1689.70 → 1695.22] To do that, it only supports HTTPS, right? Because that's what Loki exposes, but we have to
[1695.78 → 1701.78] validate the HTTPS endpoint that we're going to send logs to. The problem is how do you validate
[1701.78 → 1707.94] that we own Grafana Cloud Loki? We can't do that. So what I'm saying is there's not a native
[1707.94 → 1712.50] integration between Vastly and Grafana Cloud. And I would really like that. Actually,
[1712.50 → 1715.62] there's something which we discussed in the previous episode, episode, no, two episodes
[1715.62 → 1722.10] ago, episode 10. So that's the first part. How do we get from Vastly sending logs to Grafana Cloud?
[1722.10 → 1726.66] It's not supported. What Vastly is telling us, you will need to have some sort of proxy
[1726.66 → 1732.90] that you can authenticate and then forward those logs to Grafana Cloud, to Loki specifically.
[1733.62 → 1737.30] It's okay. Not great. I would like just to send those metrics directly. Sorry,
[1737.30 → 1743.46] I keep saying metrics. I mean logs. Send the logs to Grafana Cloud. So that will be the first step.
[1743.46 → 1749.86] Great. So let's say we understand the part between the CDN and the load balancer. Let's say that we
[1749.86 → 1755.14] understand that path, and we have some logs to tell us something. What do we do with those logs?
[1755.14 → 1761.46] So this is, yeah. I mean, logs in and of themselves aren't seldom useful. So Loki in Local that I
[1761.46 → 1766.34] referenced earlier would be able to turn those into some usable metrics, right? You'd be able to turn
[1766.34 → 1773.38] them into request rates, error rates, and latencies if the log contains a latency. And you do that all
[1773.38 → 1777.86] with Loki. And you can even, with the more recent versions of Grafana and Loki, you can build dashboards
[1777.86 → 1782.18] out of those. And some of the cool stuff is like behind the scenes, there's a lot of caching going on
[1782.18 → 1788.18] so that those dashboard refreshes don't overwhelm the Loki. And I always say with metrics, it'll tell you
[1788.90 → 1793.86] when it happened. It'll tell you how much it happened. Maybe if you've got the granularity,
[1793.86 → 1798.10] it might tell you where, which service or which region it happened in, but it won't actually tell
[1798.10 → 1803.62] you what happened. It will just tell you that something was slow. So at that point, we start
[1803.62 → 1809.22] digging in and there are a couple of techniques we can use. So firstly, I would instrument everything
[1809.22 → 1812.98] in the stack. We talked about getting metrics from the CDN. We talked about getting metrics from the
[1812.98 → 1817.86] load balancer, getting your Ingress Engine X is running on Kubernetes.
[1817.86 → 1823.22] So it's trivial to deploy Prompt ail as a daemon set and get logs from every Kubernetes pod into
[1823.86 → 1827.94] Loki. So you've got the Engine X logs, which again, Loki can extract metrics from,
[1827.94 → 1834.42] really straightforward. Ward has a fantastic set of dashboards and examples of how to do that already.
[1834.42 → 1839.30] Then you've got your application, the Elixir application. Now, I don't know enough about that,
[1839.30 → 1843.38] but I'm going to assume there's a Prometheus client library out there. And so I would instrument
[1843.38 → 1847.46] that. And I would follow whenever I'm instrumenting my own application, I tend to follow
[1847.46 → 1852.66] a very simple method. If you've heard of Brendan Gregg's use method, then somewhat tongue in cheek,
[1852.66 → 1857.78] I coined this phrase called the red method, which is request rate, error rate, and request duration.
[1857.78 → 1862.18] Right? Red. Everything comes in threes, and it's really easy to remember. So I would just try and
[1862.18 → 1868.34] export a Prometheus histogram from the application with request rate, with error rate, and with duration.
[1868.34 → 1872.74] And the histogram will capture all three. Finally, you mentioned a database. Let's just for argument's
[1872.74 → 1877.22] sake, assume it's MySQL. They don't tend to actually export very good metrics. There is an exporter for
[1877.78 → 1882.98] it in Prometheus. And we actually bake that into the Grafana agent too just to simplify and make it
[1882.98 → 1888.10] easier and have less stuff to deploy. And so I would wire those up and get whatever metrics I can,
[1888.10 → 1891.62] but I'd also gather the logs because the database logs tend to be a little bit more interesting.
[1891.62 → 1897.06] Mm-hmm. So finally, this hasn't really caught on very much, but you see it in a lot of the dashboards that
[1897.06 → 1901.86] my team and I have built. I tend to always kind of traverse the system from top to bottom.
[1902.42 → 1909.22] I always have request rates on the left in panels on the left and durations like latency graphs on the
[1909.22 → 1914.10] right. Just as a quick glance in the dashboard, you can typically see where the latency is being
[1914.10 → 1919.62] introduced. Do you have a good dashboard that exemplifies this? Because what you say makes a lot
[1919.62 → 1924.02] of sense. Is there a good dashboard that we can use as a starting point?
[1924.02 → 1928.58] Mm-hmm. The Cortex ones are the ones that I've probably spent the most amount of time.
[1929.38 → 1935.30] We ship, again, a bit of work we did with the Prometheus community was this standard called
[1935.30 → 1940.42] Begins, right? Which is a packaging format for Grafana dashboards and Prometheus alerts.
[1940.42 → 1946.66] Mm-hmm. So we've built, there's 40 or 50 different mixins now from a lot of popular systems,
[1946.66 → 1951.94] but one of them is Cortex. And it's just a versioned set of dashboards and alerts that are very flexible,
[1952.90 → 1957.54] very easy to extend, which is kind of key, and very easy to kind of keep up to date with upstream.
[1958.34 → 1962.34] Actually, the most popular mixin would be the Kubernetes mixin. I would wager that virtually
[1962.34 → 1967.38] every Kubernetes cluster in the world is running the set of dashboards from the Kubernetes mixin,
[1967.38 → 1971.30] which is kind of cool because I helped write a lot of those in the very early days, at least.
[1971.30 → 1976.10] There's now a whole community that maintains and has taken them far beyond anything I could ever
[1976.10 → 1983.54] imagine. So dashboards, you'd have a row per service, and then you just do error rate and
[1983.54 → 1988.26] request rate and latency. And this will help you at a very quick glance. When you get used to kind of
[1988.90 → 1992.66] looking at dashboards in this format, and every service kind of looks the same, is in the same
[1992.66 → 1999.22] format, that consistency really helps reduce that cognitive load. You get to kind of pinpoint very
[1999.22 → 2003.14] quickly where that latency is being introduced. It's a very simple technique. It's not universally
[2003.14 → 2007.78] applicable, but it does help you know, well, this is coming in my application, or this is coming in
[2007.78 → 2012.42] my load balancer, or this is coming in my database. Is there a screenshot of such a dashboard that we
[2012.42 → 2016.58] can reference in the show notes? That would really, really help. I can just load up one of our internal
[2016.58 → 2022.34] dashboards and send it over. Yes, please. That would be great. The other thing is you mentioned mixins.
[2022.34 → 2028.26] Mixins in what context? I've terribly overloaded a term there because I just thought it was a cool term.
[2028.26 → 2034.82] Like I realize in CSS and in Python, mixins has a particular meaning. It bears no resemblance to
[2034.82 → 2040.98] the kind of language level primitive, right? It is just a cool name that we used for packaging up.
[2040.98 → 2045.38] We called them monitoring mixins because we use the language called JSON, well, we use a language
[2045.38 → 2052.58] called JSON to express a lot of our alerts and dashboards. And JSON is very much about adding together
[2052.58 → 2059.14] big structures of data. And it kind of looks a bit like a mixin in that respect. But that being said,
[2059.14 → 2065.30] most of the way people use mixins nowadays doesn't use that technique. We just use it as a packaging
[2065.30 → 2066.26] format. Okay.
[2066.26 → 2071.94] So it's just a name. There's a GitHub repo and a small website. And the nice thing about the tooling
[2072.50 → 2078.66] that's been developed, and the packaging format is very much we encourage people who publish exporters
[2078.66 → 2083.38] or people who build applications that are instrumented with Prometheus metrics to also
[2083.38 → 2088.82] distribute a mixin. So Prometheus has a mixin. Etc has a mixin. The Kubernetes mixins, part of the
[2088.82 → 2094.58] Kubernetes project, right? Cortex has a mixin. We just, they live alongside the code. They're version
[2094.58 → 2098.74] controlled and maintained in the same way as the code. And suddenly, you know how people talk about
[2098.74 → 2102.98] kind of test-driven development. Well, you almost have observability-driven development.
[2102.98 → 2109.62] That's interesting. So I know I've heard of mixins in the context of JSON. And I tried them when I was
[2109.62 → 2116.50] using the Prometheus stack. The one that I think it was Frederick. Yes, it was Frederick. While he was
[2116.50 → 2121.62] still at Red Hat, I know that he's not there anymore. But when he was there, he was pushing for this Prometheus
[2121.62 → 2128.34] operator. And in the context of the operator, we could get like the whole stack. Working with that,
[2128.34 → 2132.74] we used that for changelog was really hard because we had like the JSON. It was like,
[2132.74 → 2137.38] it was a specific version of JSON. It was just, there was a Go one. And there was,
[2137.38 → 2142.90] I think a Python one or a JavaScript one. I can't remember. But I know the Go one was much faster
[2142.90 → 2147.06] to regenerate all the JSON that you needed, all the YAML that you needed, like took a long,
[2147.06 → 2151.86] long time basically to get it into Kubernetes. So the mixins that you're talking about,
[2151.86 → 2156.18] how would you use them? Let's imagine that you're running on Kubernetes. How would you use those mixins?
[2156.18 → 2160.42] This is a fascinating point because the mixins are advanced mode. It's like hard mode,
[2160.42 → 2164.26] right? Like the mixins are solving a problem that software developers have. It's like,
[2164.26 → 2169.86] how do I package and redistribute and version control and keep up to date? Like, it's not really
[2169.86 → 2175.06] an end user format. Like I wouldn't expect that to happen, right? So just to address some of the
[2175.06 → 2179.62] initial challenges, it was a there's a C version and a Go version of JSON it. And they weren't quite
[2179.62 → 2184.74] the same. The Go version didn't have formatting, for instance. Go versions caught up and is now what most
[2184.74 → 2188.98] people use. That's kind of, we've solved that problem. We've also developed a lot more tooling,
[2188.98 → 2193.06] right? So there's Mix Tool and there's Grizzly and there's Tanker, and there's a whole kind of
[2193.06 → 2199.94] ecosystem, JSON it bundler of tools to use to manage these. And the way it works particularly well is if
[2199.94 → 2206.18] you're in an organization with kind of sophisticated config management, you know, we have a single repo
[2206.18 → 2211.94] that has all the config that describes pretty much our entire deployment of Grafana Cloud across 20
[2211.94 → 2215.46] something Kubernetes clusters. Is it public please? Can you add me to it?
[2215.46 → 2220.74] No, unfortunately not. But there are lots of examples we use from it. But yeah, we've got this one
[2220.74 → 2226.10] deployment, this one repo, and it's that mono repo approach to config management at least where
[2226.10 → 2230.98] mixing really fit nicely because you can use JSON its bundler to package manage them. And then the really
[2230.98 → 2235.54] cool thing comes in, you probably kind of got 90% of the way there, but then didn't have the last 10%.
[2235.54 → 2243.62] We use JSON it to also manage all of our Kubernetes jobs. So all our pods, stateful sets, config maps,
[2243.62 → 2248.18] services, you name it, it's all defined in the same language, in a single language for dashboards,
[2248.18 → 2255.62] for alerts, for any files, for config maps, for anything. It makes it really easy for us to deliver
[2255.62 → 2262.74] dashboards and alerts encoded as JSON, encoded as YAML inside a config map in the same language that's
[2262.74 → 2269.54] then uploaded with a single tool. And the whole process of updating an application and updating its
[2269.54 → 2275.38] config and updating its monitoring is a single PR, a single push and a single apply, which is all CD now.
[2275.38 → 2280.74] That's where the vision was. That's a bit advanced, right? It's a bit much to ask for most people. And also,
[2280.74 → 2285.14] it's a bit opinionated, right? You have to have the complete stack end-to-end bought into the whole thing
[2285.14 → 2292.26] to really realize that benefit. And let's face it, like other techniques, right? Customize and
[2292.26 → 2298.26] queue are gaining more popularity than JSON it ever did. And so I think the time's passed for that vision
[2298.26 → 2302.58] and that way that we're running things. And really, you kind of touched on something really important
[2302.58 → 2308.74] here. It was too hard to use. So what we've been doing in Grafana Cloud really for the past year or so,
[2308.74 → 2315.22] is trying to make a kind of more opinionated, more integrated, easier to use version of all of that.
[2315.86 → 2319.54] You sign up to Grafana Cloud, you deploy the agent, right? And so that's the first bit of
[2319.54 → 2323.62] simplification. The Grafana agent embeds, it's all open source, right? It embeds
[2324.26 → 2328.66] Prometheus remote write code and scraping code. It embeds Loki's Prompt ail, it embeds the open
[2328.66 → 2334.58] telemetry collector. It also embeds some 10 to 20 different exporters, all in a single binary,
[2334.58 → 2338.34] all with a single thing to deploy and a single thing to configure. And it scrapes and gathers
[2338.34 → 2343.14] metrics and logs and traces and sends them all to your Grafana Cloud instance. And then within that
[2343.14 → 2347.54] instance, we've built a service that it's almost like an app store, right? You can select the
[2347.54 → 2351.14] integration you want to install. I want to monitor some MySQL, I want to monitor some Kubernetes,
[2351.14 → 2354.82] I want to monitor Docker. And it will install the dashboards and the alerts, and it will keep them
[2354.82 → 2358.82] up to date for you. And it will connect them through to the integration in the agent.
[2358.82 → 2363.46] And behind the scenes, this is all mix-ins, right? This is all JSON it. This is all automation we've
[2363.46 → 2368.58] built to make this whole thing easy to use and integrated and opinionated. It's much harder to
[2368.58 → 2374.42] do, you know, to do that easy to use story in open source because the opinions change, right? And the
[2374.42 → 2379.78] integrations change. But in Cloud where it's a much more controlled environment, we can deliver that
[2379.78 → 2386.74] easy to use experience. This just means for people who maybe have seen me talk or seen someone else
[2386.74 → 2391.94] talk about Prometheus and talk about Grafana and talk about how easy it is to use and how powerful it is
[2391.94 → 2396.02] and how awesome it is and how much value they've got out of it. But maybe, you know,
[2396.02 → 2401.38] don't really have the time to jump into the intricacies of JSON it and learn 50 new tools.
[2401.38 → 2403.86] We're just trying to make that accessible to that group of people.
[2403.86 → 2419.46] This episode is brought to you by our friends at Cockroach Labs, the makers of Cockroach DB,
[2419.94 → 2425.94] the most highly evolved database on the planet. With Cockroach DB, you can scale fast, survive
[2425.94 → 2432.50] anything and thrive everywhere. It's open source, Postgres wire compatible and Kubernetes friendly,
[2432.50 → 2436.74] which means you can launch and run it anywhere. For those who need more, you can build and scale
[2436.74 → 2441.86] fast with Cockroach Cloud, which is Cockroach DB hosted as a service. It's the simplest way to
[2441.86 → 2447.38] deploy Cockroach DB and is available instantly on AWS and Google Cloud. With Cockroach Cloud,
[2447.38 → 2453.14] a team of world-class Sees maintains and manages your database infrastructure so you can focus less
[2453.14 → 2458.02] on ops and more on code. Get started for free with a 30-day free trial or try their new forever
[2458.02 → 2464.26] free tier that's super generous. Head to CockroachLabs.com to learn more. Again, CockroachLabs.com
[2464.26 → 2465.78] slash changelog.
[2474.74 → 2481.06] As I was saying, we use JSON it bundler, JB. I remember the cube Prometheus operator and the
[2481.06 → 2487.54] cube Prometheus stack, which was generated out of that. So we did away with all of that. We used to,
[2487.54 → 2494.42] obviously, set up our own Grafana, set up Loki, set up Prometheus. Now all we have is a Grafana
[2494.42 → 2500.34] agent, which is really nice. By the way, do you know that docs recommend two Grafana agents? One
[2500.34 → 2506.02] to scrape the logs, one to get the metrics. So I figured out how to get a single one, and that was
[2506.02 → 2513.78] okay because one can do both. But the thing which I still struggle with is how to get the dashboards
[2513.78 → 2518.10] working nicely together. I think that's the most important thing. We have Prometheus. That's the
[2518.10 → 2523.86] library that we use in Elixir and Phoenix to get the metrics out. And it's actually on the Grafana
[2523.86 → 2530.26] blog as well. So it was featured. Alex Utmost is working close with the Grafana team. He's also
[2530.26 → 2535.38] a friend of changelogs. Very close, a very close friend. We worked together. We even did a couple of
[2535.38 → 2541.70] episodes together, even a YouTube stream on how we upgraded Erlang 24, and we were using Grafana
[2541.70 → 2544.50] cloud to see the impact of that for changelog.com. Nice.
[2544.50 → 2549.46] It was a Friday evening deploy. Prometheus was there. It was a great one. We had great fun. It was a few
[2549.46 → 2557.54] weeks back. So in that world, the dashboards, I still feel they are the strongest thing that you,
[2557.54 → 2563.54] and the best thing that you have, but also the most difficult one to integrate. Because the Grafana
[2563.54 → 2568.26] agent doesn't really handle dashboards, right? It just like gets the logs and the metrics out.
[2568.26 → 2574.18] So we're using Prometheus, but it's really clunky because you're building your dashboards in Grafana
[2574.18 → 2580.58] cloud. A lot of the time they don't work because the metrics don't show up reasons. And then you
[2580.58 → 2586.02] adjust them. Then you have to export them. Then you have to version control them. And then Prometheus
[2586.02 → 2591.14] has to be configured to upload them to Grafana cloud. So it's just a bit clunky. So I'm wondering,
[2591.14 → 2593.86] how could that be done better? Do you have some ideas?
[2593.86 → 2596.90] David Polos There's some kind of guidelines for
[2596.90 → 2601.54] building dashboards in my opinion. First thing, you should always template out the data source,
[2602.18 → 2606.58] right? Different Grafana installations will name their data sources, different things. And so a
[2606.58 → 2611.30] dashboard imported from one might not necessarily work in another. So I always make sure my data
[2611.30 → 2616.58] sources are template out. Second thing, I always tend to template out the job and the instance labels,
[2616.58 → 2620.82] maybe with wildcard selectors. And again, same reason. This means the dashboard can effectively
[2621.38 → 2627.86] dynamically discover what jobs you've got with certain metrics. This actually fits a pattern
[2627.86 → 2632.98] in Prometheus really nicely where we have this Go build info if you're in Go and Java building for
[2632.98 → 2637.70] if you're in Java and so on, where every job exports a metric that tells you the version it was built
[2637.70 → 2645.46] with and so on. We call these info level metrics. I tend to add an info metric to every piece of software
[2645.46 → 2650.66] right, right. You know, maybe it's Cortex info, right? And then I'll tell the template selector
[2650.66 → 2656.18] for any Cortex dashboard to just look for all the unique jobs and instances that export a Cortex build.
[2656.18 → 2656.74] Mm-hmm.
[2656.74 → 2661.86] Right. And this again, this kind of turns a static dashboard that might have encoded to use a
[2661.86 → 2665.94] particular set of labels into a very dynamic dashboard, which allows you to select the job
[2665.94 → 2670.26] you want to look at and also means that the chances are when you load it, as long as there's some job
[2670.26 → 2674.50] exporting some relevant metrics, it will work. So first things first, template your dashboards.
[2674.50 → 2675.14] Right.
[2675.14 → 2680.18] Right. Second thing, I'm a big fan of dashboards as code, right? So I actually don't tend to build
[2680.18 → 2685.78] my dashboards in Grafana. I tend to build them in my text editor. And I tend to use JSON it,
[2685.78 → 2689.70] unfortunately. I tend to use a library called Grafana or there's another one called Grafana
[2689.70 → 2693.46] Builder. And if you don't like JSON it, there's a good library called Grafana Lib that helps you
[2693.46 → 2698.74] build them in Python. And yeah, I tend to build them there. I tend to version control them from the get-go.
[2698.74 → 2704.02] And really I tend to use a much more kind of Git Ops style approach. There are a couple of tools you can use to do
[2704.02 → 2708.58] this, but the one I've been using more recently is called Grizzly by Malcolm Holmes, and it's on the
[2708.58 → 2713.38] Grafana GitHub. And you can install that, and you can point to a JSON its definition of a dashboard
[2713.38 → 2719.06] and it will upload it to Grafana. And generally, you know, I do a kind of dev deploy cycle on my
[2719.06 → 2723.06] laptop as I'm developing these dashboards, uploading to Grafana, refreshing, seeing the change.
[2724.02 → 2728.90] That way, kind of the definition of the dashboard is already in Git, right? And because I'm version
[2728.90 → 2734.90] controlling source code and not a big blob of JSON, the code is much more reviewable, and I can create
[2734.90 → 2738.66] PRs and have someone else review those PRs, and it's meaningful to do that.
[2738.66 → 2743.70] That sounds exactly what I would want. I mean, you've described my ideal approach,
[2744.50 → 2750.10] but first, I didn't know about those tools. Second of all, I'm not aware of any article,
[2750.74 → 2755.62] any video, anything like this that runs you through how to do this.
[2755.62 → 2760.90] Yeah. So what I would want to do is to go through that and capture it.
[2760.90 → 2767.70] I think the reason we don't promote it too widely is because the 80% use case for Grafana is editing
[2767.70 → 2773.14] dashboards in Grafana, right? And that's the easy to access, easy to use. It's very visual. It's very
[2773.14 → 2780.10] kind of rewarding to do that, right? The 20% use case that I've just described is the serious SRE
[2780.10 → 2786.34] DevOps approach. And I think we've tried a bunch of different ways of doing it. We've settled on this
[2786.34 → 2791.94] way, but I don't think anyone is satisfied. I don't think we think this is as easy as it can be.
[2791.94 → 2798.34] I don't think anyone thinks that this is the final form. And so I'm not sure that anyone's kind of too
[2798.34 → 2803.54] eager to promote this as the advanced way of doing it. I referenced the hackathon earlier that we were
[2803.54 → 2808.26] doing internally. And I know that we've got some cool stuff coming out that maybe will be the final
[2808.26 → 2813.78] form of this. I know that I'm very excited about trying it out. This is a dream, and you can say,
[2813.78 → 2819.62] no, right? Or like not a dream, but like a crazy plan. What would it look like if we paired for an
[2819.62 → 2825.94] hour? I've been doing it for close to a decade. So I think I'm pretty good or so others say to have
[2825.94 → 2830.42] a go at this. Maybe half an hour will be enough just like to get a hang of things. So, okay.
[2830.42 → 2832.66] I'm thinking YouTube stream. I'm thinking...
[2832.66 → 2833.22] Yeah, let's do it.
[2833.22 → 2834.18] Wow. Okay.
[2834.18 → 2837.54] Can we use VS Code Sharing? Because I've always wanted to use that and
[2837.54 → 2839.06] and I haven't had an opportunity to.
[2839.06 → 2843.14] Anything you want. You're the driver. You're just showing me how it's done. And then maybe
[2843.14 → 2848.10] we can switch over, and I can have a go-to see if I understood it correctly in the context of
[2848.10 → 2852.90] changelog.com because we are already using Guyana Cloud. The integration is there. We're already using
[2852.90 → 2858.42] Guyana Agent. And who knows? Maybe there will be some interesting things to share, but the focus is on
[2858.42 → 2864.90] getting this nailed down because it sounds amazing. Why aren't more people doing this? And I don't think
[2864.90 → 2870.18] many know about it. Whatever comes after it, I think it's an important step to capture and to
[2870.18 → 2875.86] share widely because I don't think people know. I've never heard this before. Jason it, JB,
[2875.86 → 2879.54] but I was doing it wrong, and I didn't even know until today. So thank you, Tom.
[2879.54 → 2883.62] Oh yeah. I wouldn't say you're doing it wrong, but it was, yeah, you didn't see the full,
[2883.62 → 2886.34] didn't get an opportunity to use the full process.
[2886.34 → 2889.30] To do it right. I didn't have the opportunity to do it right. Okay.
[2889.30 → 2893.46] I mean, and that's one of the big challenges of this approach, right? Is it's, there's a lot to
[2893.46 → 2897.46] learn. There's a lot to consume, and you don't really see the benefits until you do it all,
[2897.46 → 2902.42] which is like from a, from a developer experience perspective is awful, right? Like there's no kind
[2902.42 → 2905.06] of incremental reward that goes with it, which is what we're missing.
[2905.06 → 2910.34] We talked about metrics quite a bit, which talked about logs, but we haven't talked about traces.
[2910.34 → 2910.90] Yeah.
[2910.90 → 2914.26] I think it's a very important element. We ourselves are not using traces.
[2914.26 → 2921.62] And I can see the traces being instrumental, critical, essential to understanding why our
[2921.62 → 2926.82] requests are slow. If you have a trace, you can understand where the time is being spent
[2927.62 → 2931.22] and the slow requests, you can see, well, actually, you know what? It was Proxy.
[2931.22 → 2935.94] Because I suspect based on the metrics that we have, which by the way, we have quite a few and
[2935.94 → 2941.14] everything's going to Grafana Cloud, all the logs, everything. Based on what I see, like what we have,
[2941.14 → 2950.90] it's all things point to Proxy. So how would we use traces to understand that? First,
[2950.90 → 2955.30] how does it work? This is tempo. I know that's the component. That's the would you call it a
[2955.30 → 2959.86] component? What, what would you call it? I tend to call it either a project or a service,
[2959.86 → 2964.66] like depending on the context. Okay. So like the, the tempo service, how would we use it
[2964.66 → 2969.54] for traces, and how would it integrate in the problem or how it solved the problem that I just described?
[2969.54 → 2973.30] So this is a fascinating one, right? Because in the metrics world,
[2973.30 → 2978.18] we develop exporters, right? Which gather numeric data from other systems and expose them as metrics.
[2978.18 → 2982.66] The barrier to entry for metrics is kind of medium, you know, maybe it's kind of three feet tall.
[2982.66 → 2987.14] You know, for logs, everything has logs, right? It's so easy to get logs from everything.
[2987.14 → 2991.86] So the barrier to entry for logs is kind of nowhere, like it's on the floor. The barrier to entry for
[2991.86 → 2996.34] traces is super high. You need to have systems that are instrumented. You need to correctly
[2996.34 → 3002.74] propagate the context, the trace ID, and you need to have a way of kind of distributing this
[3002.74 → 3007.86] telemetry data, right? So this is the challenge in the tracing space right now. And this is why I
[3007.86 → 3011.62] think it's always the, you know, to your point, right, you haven't adopted tracing yet. It's always
[3011.62 → 3016.90] the third thing people adopt. The investment is high. The good news is there's a huge reward for that
[3016.90 → 3021.70] investment. And particularly whenever you're looking at any kind of performance challenges,
[3021.70 → 3025.62] tracing is invaluable. We've been doing a lot of distributed tracing for a long time in Graphite
[3025.62 → 3029.86] Labs. We started with Jaeger and eventually did our own thing with Tempo. And it's been
[3029.86 → 3035.38] instrumental in kind of accelerating the query performance of every component. So that's the
[3035.38 → 3041.46] TLDR. How do you do it? So there's some good news here. One of them is open telemetry, very kind of
[3041.46 → 3048.10] cross-functional project from many different contributors and vendors that is designed really to make the whole
[3048.10 → 3054.26] telemetry journey better and easier and simpler. And the most well-developed bit of open telemetry
[3054.26 → 3059.78] and bit that is most widely adopted is their tracing stack, right? So we've put the open telemetry
[3059.78 → 3064.58] collector into the Grafana agent. So you can deploy that, and then you've got something you can just fire
[3064.58 → 3070.74] traces at in your local environment. You'll set up the Grafana Cloud agent, the Grafana agent to forward
[3070.74 → 3075.46] those traces up to Grafana Cloud to Tempo and then Tempo deals with the storage of them, right? And that's
[3075.46 → 3080.02] really the component of this. All that leaves is for you to deal with the instrumentation.
[3080.02 → 3085.46] Now, the good news is with a lot of high-level languages, a lot of dynamic languages, you can
[3085.46 → 3090.90] use auto-instrumentation. So this is part of open telemetry's client libraries that come along. And
[3090.90 → 3096.66] for instance, with most Java web frameworks, with most Python frameworks, it's like one line of code,
[3096.66 → 3102.34] or maybe it's even no code changes, and you can get reasonable traces out of the system. I don't
[3102.34 → 3106.58] think a system like that exists for Go. So it's a bit more work with Go, but it's still not that
[3106.58 → 3110.10] challenging. I unfortunately don't know enough about the Erlang VM, but I'm going to expect there's
[3110.10 → 3115.78] probably a pretty easy way of getting traces. It exists. So like the open telemetry integration
[3115.78 → 3121.62] exists in Erlang. It's not that mature, but it's improving. Like every month is getting better.
[3122.18 → 3128.66] And I think it's more around the queries that go all the way to PostgreSQL. So how does the request
[3128.66 → 3134.02] map to that? I mean, I know that the database has some impact on that, but right now, the most
[3134.02 → 3142.02] important one is between the app pod, the app instance, and the PostgreSQL pod, which they all
[3142.66 → 3147.62] exist in the same place. Now, maybe if PostgreSQL is like a managed service, we wouldn't have this
[3147.62 → 3153.14] problem. Maybe. But regardless of what the case would be, you'd want to know what is the problem.
[3153.14 → 3158.18] And if I change this, does it actually improve it? And by how much? If you have the trace,
[3158.18 → 3163.94] it's really easy to understand, well, I should, you know what, not Proxy, I should focus maybe
[3163.94 → 3168.98] on the load balancer. But I don't know where that request is stuck or like, you know, in that request,
[3168.98 → 3172.74] which is the longest portion. So where should I invest my time first?
[3173.38 → 3176.82] You've hit on the problem or one of the many problems with distributed tracing. Like
[3177.86 → 3182.58] you have to have the entire stack instrumented to really get a lot of value, right? And if you have
[3182.58 → 3187.78] holes in the middle or black blind spots from a kind of tracing perspective, the values greatly
[3187.78 → 3188.34] diminish. Yeah.
[3188.34 → 3188.50] Yeah.
[3188.50 → 3194.42] You can get tracing information out of load balancers, right? And I've never actually done
[3194.42 → 3198.58] it myself though, right? I've always kind of stopped there. I'm hoping that things like open
[3198.58 → 3203.62] telemetry, and I know Amazon are heavily investing in open telemetry. So I'm hoping that it will be
[3203.62 → 3209.46] possible if it isn't already to get open telemetry spans out of my Lbs, right? I think, you know,
[3209.46 → 3214.42] my Albs and so on. I think that's going to be really important. Furthermore, I'm hoping that things like the W3C
[3214.42 → 3221.54] trace context makes this easier. And maybe this even allows things like the CDN Vastly to also
[3221.54 → 3227.30] emit a span. That would be kind of cool being able to see a CDN and an ALB and your application.
[3227.30 → 3232.90] When it comes to Postgres and MySQL, I don't know. I'd love to see spans coming out of those systems,
[3232.90 → 3237.54] but I don't really know the status. I'm not really an expert on this side of things. A common
[3237.54 → 3242.58] misconception is that kind of every service emits one and only one span, right? It doesn't have to.
[3242.58 → 3246.42] You can emit as many spans as you like. You probably shouldn't emit too many, but you can
[3246.42 → 3250.90] do whatever you like. So one of the things where we do a lot of is kind of client-side spans.
[3250.90 → 3256.18] You know, whenever we do a request to a database in Cortex, in pretty much any of the systems I've
[3256.18 → 3262.42] worked on, they'll emit a client-side span. And this effectively gives you some insight into the
[3262.42 → 3267.54] latency that external systems are contributing. But it doesn't have to even just be two spans,
[3267.54 → 3271.54] right? A server span and a client span. You know, you can put spans in between. You know,
[3271.54 → 3276.98] so we will have spans around cache lookups. We will have spans around various kinds of
[3277.54 → 3282.74] areas inside a single service that parallelize, right? And we'll emit multiple spans. And it
[3282.74 → 3286.82] really helps you understand the flow of the request. Don't go crazy with it, but in general,
[3286.82 → 3292.34] it's possible. In your situation, because it's a monolith, I would instrument the Elixir server and
[3292.34 → 3298.66] client going out to Postgres. And that would probably give you enough information to know if it's Postgres,
[3298.66 → 3305.38] to know if it's the Proxy or the LB. You want to get a span from something further up the chain,
[3305.38 → 3306.74] and then start to look at the differences.
[3306.74 → 3311.30] Chris Ingress Nginx. Does Ingress Nginx and Nginx support spans? Do you know?
[3311.30 → 3315.86] I don't know off the top of my head. Like, one of the things I've definitely seen engineers go down
[3315.86 → 3321.30] this rathole of trying to get complete traces and spans from everywhere. And there's just a kind of,
[3321.30 → 3326.58] there's a, you know, effort reward trade-off to be made. Like, it might take a lot of effort to get
[3326.58 → 3331.30] a complete span from every single service. You know, if you're on a mobile app, like doing a
[3331.30 → 3335.06] client-side span might tell you everything you need to know, just, you know, emitting it from your
[3335.06 → 3336.02] mobile app.
[3336.02 → 3340.74] Chris I understand what you're saying. I think on the client side, that is less of an issue because
[3340.74 → 3346.18] the span, which is the longest one, happens server-side, where it's like waiting or processing,
[3346.18 → 3352.10] whatever the name may be. And that tends to sometimes be really long. So what happens inside
[3352.10 → 3359.22] of that span? So we know that it goes to, let's say, quickly. Great. We can remove that. We can go
[3359.22 → 3364.82] directly to the load balancer. Okay. I don't think there's much we can do about the load balancer. So
[3364.82 → 3372.18] let's say we ignore that. So our span really starts at possibly the Ingress Nginx. So that's the first
[3372.18 → 3377.30] starting point. Excellent. What happens inside Ingress Nginx maybe would be interesting. I mean,
[3377.30 → 3382.98] this is Nginx specifically, maybe it would be interesting. But the next hop will be into,
[3382.98 → 3389.62] as far as I know, this will be the entry points into Kubernetes. So that will be the service that's
[3389.62 → 3394.98] responsible for routing the traffic. I mean, that's actually even before the Ingress Nginx, right?
[3394.98 → 3400.98] It's a service. It hits the Nginx pod. And from the Nginx pod, it will need to talk to the other
[3400.98 → 3409.94] service, which is the application service. So having these first two, three steps in the span
[3409.94 → 3414.66] would be already helpful. But realistically, I think we can only start from the Kubernetes side.
[3415.14 → 3423.86] And that's okay. So from Nginx, the next hop would be really the application. So how does that span vary?
[3423.86 → 3427.54] And regardless of what happens inside, it doesn't matter. How does that duration change?
[3427.54 → 3434.50] From the application, again, it has to hit the database. And if we know the timings that it takes,
[3434.50 → 3439.46] that would be enough. So we have literally the three, four hops that we're really interested in.
[3439.46 → 3445.54] And then there's the cube proxy. So where does that happen? And how long does that span take?
[3446.18 → 3451.78] So it's just like, okay, together, maybe seven steps. And which is the step which is more variable?
[3451.78 → 3455.62] That's the way I think about it. Is that right? Does this sound right to you? With distributed tracing,
[3455.62 → 3459.94] you've always got to kind of see. The great thing about it is like being able to visualize the actual
[3459.94 → 3464.82] flow of the request. So yes, like, I'm agreeing with you. One of the things I will say is,
[3465.78 → 3470.74] it's probably not cube proxy. My understanding in most deployments is that is not a layer seven things,
[3470.74 → 3475.70] right? It's done at the TCP level, where it doesn't intercept any traffic, right? So it's not worth putting
[3475.70 → 3480.58] a, well, it's not even technically possible, I guess, to do a request level span there because
[3480.58 → 3482.34] it's very connection oriented. Right.
[3482.34 → 3486.10] You know, one of the promises of Open Telemetry, right, because it's so vendor neutral and because
[3486.10 → 3492.82] it's so open as a standard is that we might even be able to get spans into more established open
[3492.82 → 3498.10] source projects who don't want to pick favourites. So maybe one day we will be able to get spans into
[3498.10 → 3502.82] Postgres and into MySQL. Maybe it really exists. I'll admit to not knowing off the top of my head.
[3502.82 → 3508.50] Neither do I, but that's really fascinating. So this is what I'm thinking. First step is,
[3509.22 → 3516.02] let's pair up on what it looks like to do Grafana dashboards, Tom style. I'll call it Tom style. I
[3516.02 → 3522.02] know it isn't, but Grizzly style or whatever. The point being is the way you developed them. Big fan
[3522.02 → 3527.62] of GitHub, big fan of version controlling it. We're not using Argo CD yet, but I would love to put that
[3527.62 → 3532.58] in the mix. How does that play with the tools that you use? How does it integrate with Grafana Cloud?
[3532.58 → 3537.30] How can we control those dashboards in a way that is nicer than what we have today?
[3538.02 → 3543.94] And then this specific problem, once we have that iteration set up really nicely and those feedback
[3543.94 → 3548.02] loops set up really nicely so we can experiment, which goes back to what you were saying, being
[3548.02 → 3553.30] able to ask interesting questions, being able to figure things out, right? Like explore, which
[3553.94 → 3558.58] I'm a big fan of, right? Like figure out, like we don't know what the problem is, so let's figure out.
[3558.58 → 3563.70] So how can we very quickly iterate on solving that specific or like finding that answer?
[3564.34 → 3571.38] And then I think those spans, tempo and integrating with that, super valuable, long, long term.
[3571.38 → 3576.34] I'm expecting things to change along the way as the ecosystem matures, more libraries are getting
[3576.34 → 3582.58] instrumented, open telemetry becomes more mature. I think that's a great vision and a great
[3582.58 → 3586.66] direction towards where the industry is going. I'm very excited about that.
[3587.54 → 3593.70] As a listener, if I had to remember one thing from this conversation, what should that be, do you think?
[3593.70 → 3599.70] I go all the way back to the early comments about observability and about the big tent philosophy
[3599.70 → 3605.62] and about them not being one size fits all tooling. I know as a vendor here, like, you know, I have a
[3605.62 → 3610.34] preference for Prometheus and Loki and tempo, but honestly, like that's just a preference. That's just an
[3610.34 → 3617.54] opinion. Like an equally valid opinion is to use graphite and Jaeger and elastic, right? And they're very
[3617.54 → 3623.14] powerful systems. And it's our kind of mission at Grafana Labs to allow you to have the same
[3623.14 → 3629.22] experience, the same level of integration and ease of use, no matter what your choice of tooling is.
[3629.22 → 3635.54] I love that. So if we were to pick one title for this discussion, what do you think that should be?
[3635.54 → 3638.50] Observability and big tent, yeah. Big tent philosophy.
[3638.50 → 3643.06] Big tent philosophy. I like that. I like that big tent philosophy.
[3643.06 → 3646.50] I'm not sure where the term comes from, to be brutally honest. I should probably Google it.
[3646.50 → 3650.82] It's like, you know, I know how a lot of companies have internal mantras, right? You know,
[3650.82 → 3656.26] Google's mission was to organize the world's information, right? We are, you know, the internal
[3656.26 → 3659.94] mantra in Grafana Labs is this big tent philosophy. We apply it everywhere to everything we do.
[3659.94 → 3663.14] Who came with the idea of the big tent? Do you know?
[3663.14 → 3669.70] I think, I don't know where the term came from, but the idea was very early on in Grafana when
[3669.70 → 3675.30] Torque added support for multiple data sources, right? And very early on, Grafana started life
[3675.30 → 3680.66] visualizing graphite data. But very early on, support for other systems was added, right?
[3680.66 → 3686.98] And it's really that vision early on to bring together data for multiple systems in Grafana
[3686.98 → 3692.82] that seeded this idea. So the big tent, the way I understand it, is bringing all these,
[3693.62 → 3697.46] I want to say vendors, data sources. It's more than just data sources, right?
[3697.46 → 3701.14] More than just data sources, because it's data from anywhere and combining it in a single place,
[3701.14 → 3706.42] but building experiences that span multiple systems, integrating them in ways that didn't
[3706.42 → 3711.86] exist before. But it is not just a concept that applies to Grafana and the visualization, right?
[3711.86 → 3716.02] We apply it on the backend with supporting different query languages within the same
[3717.86 → 3724.82] time series database. You know, we support it in Tempo, being able to send traces formatted for
[3724.82 → 3729.38] Jaeger or formatted for Pipkin. You know, and it's kind of intrinsic in a lot of open telemetry as well,
[3729.38 → 3734.98] being very vendor neutral to a fault. Tom, I didn't think this was possible,
[3734.98 → 3738.02] but it happened. I have more questions at the end than at the beginning.
[3738.02 → 3743.46] I'm sorry about that. And I'm more excited to continue talking with you at the end than I was
[3743.46 → 3748.90] at the beginning. Again, that's not possible. I'm really looking forward to trying things which
[3748.90 → 3752.98] I've just said, and I'm really looking forward to next time. So thank you for today.
[3752.98 → 3754.26] Thank you very much, Gerhard.
[3754.26 → 3757.86] Thank you.
[3757.86 → 3759.86] That's it for this episode of Ship It.
[3759.86 → 3765.30] Thank you for tuning in. We have a bunch of podcasts for developers at Changelog that you
[3765.30 → 3771.46] should check out. Subscribe to the master feed at changelog.com forward slash master to get
[3771.46 → 3779.06] everything we ship. I want to personally invite you to join your fellow change loggers at changelog.com
[3779.06 → 3784.66] forward slash community. It's free to join and stay. Leaving, on the other hand, will cost you some
[3784.66 → 3791.22] happiness credits. Come hang with us on Slack. They're no imposters. Everyone is welcome. Huge
[3791.22 → 3798.26] thanks again to our partners Vastly, Launch Darkly and Winnowed. Also, thanks to Break master Cylinder
[3798.26 → 3811.86] for making all our awesome beats. That's it for this week. See you next week.
[3829.06 → 3833.94] I'll see you next week.
[3833.94 → 3836.36] ...
