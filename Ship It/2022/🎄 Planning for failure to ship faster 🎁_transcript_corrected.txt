[0.08 → 5.98] I'm Gerhard Lanza, and you're listening to Ship It. Show, a podcast about ops, infrastructure,
[6.44 → 8.08] and shipping physical goods.
[8.56 → 15.42] Eight months ago, in episode 49, Alex Sims, solutions architect and senior software engineer
[15.42 → 21.36] at James & James, shared with us his ambition to help migrate a monolithic PHP app running
[21.36 → 24.28] on AWS EC2 to more modern architecture.
[24.28 → 30.42] The idea was some serverless, some EKS, and many incremental improvements.
[30.86 → 32.86] So how did all of this work out in practice?
[33.24 → 38.44] How did the improved system cope with the Black Friday peak, as well as all the following
[38.44 → 39.18] Christmas orders?
[39.76 → 43.72] Thank you, Alex, for sharing with us your Ship It-inspired Kaiden story.
[43.96 → 45.72] It's a wonderful Christmas present.
[46.18 → 48.58] Big thanks to our partners Vastly and Fly.
[48.88 → 54.04] This MP3 is served with minimal latency from the Vastly edge location, which is closest
[54.04 → 54.48] to you.
[54.78 → 60.06] Our app and database run on fly.io, because it keeps things simple.
[65.40 → 68.20] This episode is brought to you by Source graph.
[68.82 → 73.20] Source graph is universal code search to let you move fast, even in big code bases.
[73.68 → 79.42] Here's CTO and co-founder, Bing Lu, explaining how Source graph helps you to get into that ideal
[79.42 → 80.46] state of flow and coding.
[80.46 → 85.62] The ideal state of software development is really being in that state of flow.
[85.84 → 90.68] It's that state where all the relevant context and information that you need to build whatever
[90.68 → 95.46] feature or bug that you're focused on building or fixing at the moment, that's all readily
[95.46 → 95.94] available.
[96.10 → 99.44] Now, the question is, how do you get into that state where, you know, you don't know anything
[99.44 → 101.48] about the code necessarily that you're going to modify?
[101.80 → 104.14] That's where Source graph comes in.
[104.14 → 107.50] And so what you do with Source graph is you jump into Source graph.
[107.62 → 110.94] It provides a single portal into that universe of code.
[111.06 → 114.58] You search for the string literal, the pattern, whatever it is you're looking for.
[114.68 → 117.76] You dive right into the specific part of code that you want to understand.
[118.04 → 120.36] And then you have all these code navigation capabilities.
[120.48 → 124.96] Jump to definition, find references that work across repository boundaries that work without
[124.96 → 129.78] having to clone the code to your local machine and set up and mess around with editor
[129.78 → 130.88] config and all that.
[130.88 → 134.82] Everything is just designed to be seamless and to aid in that task of, you know, code
[134.82 → 136.34] spelunking or source diving.
[136.66 → 140.30] And once you've acquired that understanding, then you can hop back in your editor, dive right
[140.30 → 144.54] back into that flow state of, hey, all the information I need is readily accessible.
[144.76 → 149.02] Let me just focus on writing the code that influenced the feature or fixes the bug that I'm working
[149.02 → 149.22] on.
[149.56 → 149.84] All right.
[149.88 → 154.78] Learn more at Sourcegraph.com and also check out their bi-monthly virtual series called DevTools
[154.78 → 159.84] Time covering all things DevTools at Sourcegraph.com slash DevToolTime.
[160.88 → 168.30] We are going to ship it.
[168.30 → 170.84] Three, two, one.
[184.66 → 186.64] Alex, welcome back to Ship It.
[187.14 → 188.18] It's great to be back.
[188.40 → 190.20] It doesn't feel that long since our last chat.
[190.20 → 191.50] No, it wasn't.
[191.74 → 193.32] It was episode 49.
[193.98 → 195.22] Priggish.
[195.88 → 196.82] Six months, actually.
[196.96 → 197.58] Six, seven months.
[197.66 → 198.24] Six, seven months.
[198.64 → 199.64] So much has changed.
[199.90 → 200.28] Yes.
[200.52 → 203.72] The title is Improving an E-commerce Fulfillment Platform.
[204.24 → 205.36] A lot of big words there.
[205.86 → 207.86] The important one is the improving part, right?
[208.34 → 208.68] Indeed.
[208.94 → 209.04] Yeah.
[209.14 → 210.20] So much has changed.
[210.44 → 211.62] And it's fascinating.
[211.70 → 214.60] I think last time we spoke, we fulfilled about 15 million orders.
[214.60 → 217.84] And we're closely approaching 20 million.
[217.84 → 222.02] So almost another 5 million orders in six months.
[222.16 → 225.84] It's just crazy how the pace we're moving at this year.
[226.26 → 226.86] That's nice.
[226.86 → 233.24] It's so rare to have someone be able to count things so precisely as you are.
[233.48 → 233.84] Okay.
[234.02 → 235.82] And it's a meaningful thing, right?
[235.82 → 241.90] It's literally shipping physical things to people around the world, right?
[241.90 → 246.24] Because you're not just in the UK, even though the company, the main company is based in the UK.
[246.24 → 248.44] You have fulfillment centres around the world.
[248.96 → 249.06] Yeah.
[249.14 → 250.56] We've now got four sites.
[250.80 → 252.20] We're in the UK.
[252.68 → 258.36] We've got two sites in the US in Columbus, Ohio, and just opened one up in Vegas.
[258.74 → 260.40] And we've got another site in Auckland.
[260.92 → 262.24] So it's growing pretty quick.
[262.30 → 264.10] And I think this year we're opening two more sites.
[265.18 → 265.46] So...
[265.46 → 266.96] We say this year, 2022?
[267.56 → 268.08] Oh, sorry.
[268.14 → 268.24] Yeah.
[268.26 → 272.04] We opened one site this year, which is the Vegas one.
[272.12 → 272.74] Oh, and Venlo.
[273.02 → 274.68] So that's Netherlands.
[274.68 → 278.28] And yeah, we've got plans for two more sites next year, I believe.
[278.80 → 279.04] Nice.
[279.50 → 286.96] So an international shipping company that shipped 5 million orders in the last six, seven months?
[287.60 → 287.80] Yeah.
[287.90 → 288.42] Very nice.
[288.98 → 290.62] And a funny story on that.
[291.32 → 295.96] I'd love to imagine it was just me sat there sort of counting orders as they go out the door.
[296.08 → 300.56] But we've actually got a big LED sign that's mounted to the wall.
[300.92 → 303.56] And every time an order dispatches, it ticks up.
[303.56 → 306.08] And it's a nice bit of fun.
[306.24 → 310.10] There's one in the office and there's one mounted on the wall in the fulfillment centre.
[310.80 → 315.92] And it's quite interesting to see that ticking up, especially this time of year when the numbers really start to move.
[316.48 → 316.52] Yeah.
[316.74 → 317.04] Okay.
[317.20 → 317.46] Okay.
[317.76 → 324.76] So for the listeners that haven't listened to episode 49 yet, and the keyword is yet, right?
[324.82 → 325.42] That's a nudge.
[325.72 → 326.60] Go and check it out.
[326.60 → 329.12] What is it that you do?
[329.50 → 329.72] Yeah.
[329.84 → 332.82] So I mischaracterized myself last time as a 4PL.
[333.04 → 335.14] We're actually a 3PL, I was corrected.
[335.64 → 339.02] And essentially, we act on behalf of our clients.
[339.02 → 345.80] So imagine you're somebody that sells socks, and you have a Shopify account.
[346.56 → 349.50] And you come to us, and we connect to your Shopify account.
[349.88 → 361.98] We ingest your orders, and we send them out to your customers via the cheapest shipping method, whether that be like Royal Mail in the UK or even like FedEx going on international service to the US.
[361.98 → 369.22] We handle all that, and then we provide tracking information back to your customers and give you insights on your stock management.
[369.80 → 373.62] And there are tons of moving parts outside just the fulfillment part.
[373.72 → 382.20] It's all about how much information can we provide you on your stock to help you inform the decisions on when you restock with us.
[382.68 → 382.74] Okay.
[382.94 → 384.58] So that are James and James.
[384.68 → 387.32] James and James, the company, that's what the company does.
[387.94 → 389.04] How about you?
[389.12 → 390.86] What do you do in the company?
[390.86 → 396.06] Yeah, so I've transitioned through many roles over the last few years.
[396.26 → 404.04] Started this year, I was sort of like senior engineer, and I've transitioned to a solution architect role this year.
[404.30 → 407.96] Main motivation for that is we've predominantly been a monolithic.
[408.54 → 414.76] We had a big monolith that was on a very legacy version of Symphony, Symphony 1.4 to be specific.
[414.76 → 430.72] And we want to start making tactical incisions to start breaking some of those core parts of our application now into additional services that use slightly more up-to-date frameworks that aren't going to take us years to upgrade, say, from a 1.4 version of Symphony to something modern.
[430.72 → 439.16] And it's probably, we decided it's going to be easier to extract services out and put them into new frameworks that we can upgrade as we need to.
[439.16 → 448.84] And it's sort of my job to oversee all the technical decisions we're taking in framework, but also how we plan upgrades, how we stitch all these new systems together.
[449.12 → 453.48] And most importantly, how we provide sort of like a cohesive experience to the end user.
[453.58 → 456.36] So they don't think there are six services running behind the scenes.
[456.36 → 460.18] And to them, it's just one sort of UI that's a portal into it all.
[460.82 → 460.92] Yeah.
[461.38 → 466.24] When you say end users, this is both your staff and your customers, right?
[466.38 → 466.72] Exactly.
[467.28 → 476.30] We have two applications, one called Command Port, which is our sort of internal tool where we capture orders and pick and pack them and dispatch them.
[476.30 → 488.46] And then we have Control Port, which is what our clients use, which is their sort of portal into what's going on inside the warehouse without all the extra information that they don't really care about.
[488.88 → 488.94] Okay.
[489.48 → 496.22] And where do these services, I say services, I mean, where do these applications run?
[496.28 → 499.04] Because as you mentioned, there are multiple services behind them.
[499.18 → 501.14] So these two applications, where do they run?
[501.14 → 501.86] Yep.
[501.94 → 510.74] So they run in AWS on some EC2 instances, but we have recently created an EKS cluster for all of our new services.
[511.04 → 521.34] And we're slowly trying to think about how we can transition our legacy application into the cluster and start spinning down some of these old EC2 instances.
[521.92 → 522.52] Okay.
[523.08 → 526.94] So I remember in episode 49, that's what we started talking about, right?
[526.94 → 535.82] Like the very early steps towards the Kubernetes architecture or like Kubernetes-based architecture to see what makes sense.
[536.10 → 537.20] What should you pick?
[537.30 → 539.84] Why would you pick one thing over another thing?
[540.18 → 541.76] That's been six months ago.
[542.50 → 545.84] How did it work in practice, that migration, that transition?
[546.46 → 546.64] Yeah.
[546.82 → 548.08] So it worked pretty well.
[548.08 → 557.88] So one of our biggest projects over this last six months has been to rewrite PIC, which is one of our largest parts of our operation, into a new application.
[558.14 → 562.96] So what we ended up doing, we created a Remix application, which is a React framework.
[563.20 → 570.42] And that's deployed on the edge using Lambda, just so you get pretty much fast response times from whatever you're requesting it from.
[570.96 → 572.18] So that sits outside the cluster.
[572.18 → 577.48] And then we have a new PIC API, which is built using Laravel.
[577.90 → 584.20] That's deployed inside EKS and also a new auth service, which is deployed inside EKS as well.
[584.38 → 589.34] So currently the shape of our cluster is two services running inside EKS.
[590.22 → 593.64] And our EC2 instances make requests into the cluster.
[594.22 → 597.26] And that Lambda function also makes requests into the cluster.
[597.26 → 602.22] We have, I think, three nodes in there operating on a blue-green deploy strategy.
[602.98 → 604.52] It was actually fascinating.
[604.78 → 608.26] We got bitten by a configuration error.
[609.52 → 610.60] This might make you laugh.
[610.90 → 613.78] So to set the scene, it's Friday night.
[614.40 → 617.90] The shift is just handed over to the next shift manager in the FC.
[618.48 → 627.02] We've been Canary releasing one or two operators for the last two weeks doing some testing in production on the new PIC service.
[627.26 → 628.84] And everything's been going flawlessly.
[629.04 → 630.58] We're like, this is such a great deployment.
[631.00 → 631.62] We're happy.
[631.80 → 632.60] There's been no errors.
[632.82 → 636.66] Let's roll it out to 30% of everybody that's running on tonight's shift.
[637.28 → 641.52] And earlier that day, I was speaking with one of our ops engineers.
[641.52 → 644.96] And I said, oh, it's really bugging me that we only have one node in our cluster.
[645.14 → 646.30] It doesn't really make much sense.
[646.56 → 651.88] Could we scale it to three nodes and then also do blue-green deploy on that?
[652.48 → 653.40] He was like, yeah, sure.
[653.46 → 653.90] No worries.
[654.64 → 656.32] We added two more nodes to the cluster.
[656.66 → 662.64] We deployed the app over those three nodes and sort of looked at the state of Kubernetes and was like, yeah, that's great.
[662.72 → 664.12] I can see all three instances running.
[664.46 → 665.98] I can see traffic going to all of them.
[666.26 → 667.06] Yeah, no worries.
[667.26 → 667.96] Call it a day.
[667.96 → 672.98] I started getting pinged on WhatsApp, and they're saying everything in PIC's broken.
[673.12 → 675.96] If we refresh the page, it takes us back to the start of our PIC route.
[676.16 → 678.12] We're having to rescan all the items again.
[678.40 → 681.60] Someone's got a trolley with 100 stops on it, and they're having to go to the start.
[681.80 → 683.98] And I'm like, what the is going on?
[683.98 → 693.06] And it turned out that in the environment variables that we'd set for the application, that we'd set the cache driver to be filed instead of Regis.
[693.06 → 700.38] So as soon as someone got directed to another node, they lost all of their progress, and they were getting reset.
[700.72 → 706.06] So, yeah, that taught me to not just deploy on a Friday night and be happy that the test passed because...
[706.06 → 707.14] Oh, yes.
[707.34 → 712.24] And then I think because you've been testing with like a single instance, right?
[712.26 → 713.12] And everything looked good.
[713.42 → 716.80] So going from one to three, you seem like, sure, this is going to work.
[716.80 → 717.56] Like, no big deal.
[717.86 → 720.56] It's so easy to scale, right?
[720.62 → 721.98] Things in Kubernetes when you have that.
[722.10 → 722.26] Yeah.
[722.58 → 723.46] And then things like this.
[723.52 → 724.32] Ah, okay.
[724.96 → 726.60] That sounds like a gun to your foot.
[726.96 → 728.42] What could possibly happen?
[728.74 → 729.08] Okay.
[729.26 → 729.66] Wow.
[729.88 → 730.08] Okay.
[730.24 → 732.84] It was really nice to have an escape patch though.
[732.90 → 735.06] So we deployed everything behind Launch Darkly.
[735.06 → 736.42] So we had feature flags in there.
[736.88 → 739.06] And literally what I did, switched off the...
[739.74 → 741.56] Scaled the rollout down to 0%.
[741.56 → 743.74] Everyone fell back to the old system.
[744.50 → 747.82] And it was only the cache state that was poisoned.
[748.46 → 752.58] So their actual state of what they picked had all been committed to the database.
[752.84 → 757.16] So as soon as I scaled that down to 0%, they fell back to the old system and were able to continue.
[757.38 → 760.18] And I think we only really had like 10 minutes of downtime.
[760.48 → 764.20] So it was really, really nice to have that back out method.
[764.20 → 766.86] But I mean, you say downtime.
[767.14 → 769.26] To me, that sounds like degradation, right?
[769.32 → 772.20] 30% of requests were degraded.
[772.28 → 775.42] I mean, they behaved in a way that was not expected.
[776.24 → 782.20] So did, again, I'm assuming, did the majority of users have a good experience?
[782.20 → 786.20] No, everybody that was being targeted at the...
[786.20 → 790.20] So the 30% of operators that were going to the new service, everyone had a bad experience.
[790.20 → 790.38] Right.
[790.48 → 792.78] But the 70% of operators, they were okay.
[793.02 → 793.34] Which I say...
[793.34 → 793.64] Oh, yeah.
[793.76 → 794.42] Yeah, exactly.
[794.64 → 794.80] Yeah.
[794.80 → 796.04] So the majority was okay.
[796.10 → 796.36] Okay.
[796.36 → 799.76] Well, feature flags for the win, right?
[799.76 → 804.82] And yeah, it was really nice because this is the first time we've deployed a new service like this.
[805.26 → 807.12] And it was the first time trying feature flags.
[807.98 → 815.46] And even though we had an incident, it was really nice to have that graceful back out and be confident that we could still roll forward.
[815.46 → 821.84] And yeah, like in the WhatsApp chat with our operations manager, we'd be just sending emojis, roll forward.
[821.92 → 823.60] And there's this like rolling panda down a hill.
[823.76 → 825.20] He was just like, yeah, no worries.
[826.74 → 827.76] That's what you want.
[827.90 → 828.46] That's it.
[828.58 → 829.66] That's the mindset, right?
[829.72 → 833.28] That's like the mindset of trying something new.
[833.66 → 835.22] You think it's going to work.
[835.70 → 836.98] You can never be too confident.
[837.62 → 844.70] Things even like the more confident you are, the more, I know, the more painful, I think, the failure.
[844.70 → 849.00] Like if you're 100% confident it's going to work, and it doesn't, what then?
[849.82 → 852.14] Versus I think it's going to work.
[852.46 → 853.48] Let's try it.
[853.56 → 855.66] I mean, if it won't, this is the blast radius.
[855.86 → 866.94] I'm very aware of the worst possible scenario, and I'm okay with that risk, especially when it comes to production, especially when it comes to systems that, you know, cost money when they're down.
[867.40 → 871.40] So imagine if this had happened to 100% of the staff.
[871.40 → 874.50] I mean, you would be basically stopped, right, for like 10 minutes.
[874.70 → 875.82] And that is very costly.
[876.30 → 876.38] Yeah.
[876.50 → 885.22] And it's been really nice to see the mindset of people outside of tech evolve over the past couple of years.
[885.44 → 892.80] There was a time when we would code freeze, everything would be locked down and nothing would happen for sort of two months.
[892.80 → 901.92] And slowly, as we've started to be able to introduce things that mitigate risk, the mindset of those people external to us has also changed.
[902.04 → 907.18] And it's just a really nice thing to see that we can keep iterating and innovating through those busy periods.
[907.18 → 911.74] Once you replace fear with courage, amazing things happen.
[912.06 → 920.78] You know, have the courage to figure out how to apply a change like this, risky, because all changes are risky if you think about it, production.
[921.02 → 926.14] The bigger it is, the hotter it runs, the more important, you know, blast radius becomes.
[926.84 → 928.80] And don't think that you'll never make a mistake.
[929.02 → 929.34] You will.
[929.58 → 930.18] No, exactly.
[930.36 → 933.52] Sooner or later, you know, the odds are in your favour.
[933.52 → 936.20] But sometimes, things go wrong.
[936.50 → 936.68] Cool.
[937.00 → 937.22] Okay.
[937.34 → 944.50] I mean, I was very confident with this until I realized I'd broken all the reporting on that service that I shared in the last episode.
[944.64 → 946.14] It just completely fell on its face.
[946.32 → 946.60] Really?
[946.68 → 950.76] Because I did one save, because I found in the old system, it did two saves.
[951.08 → 957.82] And we use change data capture to basically analyze the changes on the record as they happen in real time with Kafka.
[958.82 → 961.06] And the old system did two saves.
[961.06 → 965.98] It did one to change the status of a trolley from a picking state to an end shift state.
[966.30 → 969.66] And one change to divorce the relationship of the operator from that trolley.
[970.26 → 978.62] And in the application that consumes it, it checks for the presence of the operator ID needs to be on the trolley and the status needs to change in that row.
[978.62 → 982.16] If that case wasn't satisfied, it would skip it.
[982.56 → 985.80] And that trolley would never be released, which means the report would never be generated.
[986.56 → 997.16] And what ended up happening is I saw that old code and went, why would I want to do two saves back to back when I can just bundle it all up into one and be like micro efficient?
[998.00 → 998.40] Of course.
[998.40 → 999.20] Oh, okay.
[999.32 → 999.44] Yeah.
[999.44 → 1002.00] I've just got to take it down like weeks worth of reporting.
[1002.26 → 1002.70] Yeah.
[1002.74 → 1003.34] That wasn't fun.
[1003.86 → 1004.70] All great ideas.
[1004.82 → 1006.00] We could live without it though.
[1006.12 → 1007.26] It's all edge stuff.
[1007.46 → 1010.46] And yeah, we can live without it if it's fixed now.
[1010.60 → 1015.94] But it's just, yeah, finding those things and going, oh my God, I can't believe that's a thing.
[1015.94 → 1016.06] Okay.
[1016.42 → 1016.74] Okay.
[1017.06 → 1017.34] Okay.
[1017.44 → 1019.00] So that's a good one.
[1019.12 → 1023.14] So you had two possibly the biggest events.
[1023.34 → 1025.36] Now, I think they're probably the biggest events.
[1025.42 → 1035.68] I mean, I don't work in the physical shipping world, but I imagine that Black Friday and Christmas are the busiest periods for the shipping industry as a whole.
[1036.06 → 1037.52] I think it's like the run-up, right?
[1037.52 → 1040.20] Because the things have to be there by Black Friday.
[1040.32 → 1042.28] Things have to be there by Christmas.
[1042.28 → 1051.60] How did those two major events work out for you with all these changes to the new system that started six months ago?
[1052.26 → 1056.48] So to give an idea of what our normal sort of daily volume is and maybe set the scene a bit.
[1056.82 → 1060.10] We were normally about 12,000 orders a day, I think.
[1060.66 → 1066.26] And on the ramp up to Black Friday from about the 20th of November, we were up to at least 20,000 a day.
[1066.74 → 1070.60] And on Black Friday, I think 31,000 was our biggest day of orders.
[1070.60 → 1076.02] And to also set the picture a little bit better is that in the last six months, I said we've done about 5 million orders.
[1076.50 → 1082.38] In the last 15 days, we've done about 400,000 orders across all of our sites.
[1082.78 → 1083.26] That's a lot.
[1083.54 → 1085.82] So, yeah, volume really ramps up.
[1086.52 → 1092.42] And we were really, really confident this year going in from like a system architecture perspective.
[1092.42 → 1097.40] We'd had a few days when we had some spiky volume and nothing seemed to let up.
[1097.98 → 1103.12] But it just seemed to all not start going wrong because we never really had a huge amount of downtime.
[1103.38 → 1109.34] But a lot of our alarms in Datadog were going off and Slack was getting really like bombarded.
[1109.52 → 1113.76] And we had a few pages that were 503ing because they were just like timing out.
[1114.42 → 1115.98] We were like, what's going on?
[1116.04 → 1118.86] Why is the system all of a sudden going really slow?
[1118.86 → 1124.14] Yeah. And we'd released this change recently called Label at Pack.
[1124.72 → 1131.06] And essentially what it did is as you're packing an order, previously you'd have to like to pack all the items.
[1131.20 → 1133.84] And then once you've packed all the items, you weigh the order.
[1134.20 → 1137.20] And then once you've weighed the order, you'd wait for a label to get printed.
[1137.68 → 1141.08] But it was really slow because that weighing step you don't need.
[1141.18 → 1142.82] You already know what's going in the box.
[1143.18 → 1144.32] You know what box you're choosing.
[1144.32 → 1146.16] So you don't need that weigh step.
[1146.48 → 1154.30] And it means as soon as you start packing that order, we can in the background go off and make a request to all of our carriers, quote for a label and print it.
[1154.84 → 1158.66] So at the time that you finish packing all the stuff in the box, you've got a label ready to go.
[1159.40 → 1163.20] But what we didn't realize is that AJAX request wasn't getting fired just once.
[1163.92 → 1166.00] It was getting fired multiple times.
[1166.00 → 1173.00] And that would lead to requests taking upwards of sometimes 30 or 40 seconds to print a label.
[1173.48 → 1179.38] But if you had tens of these requests going off, and we've got 80 packing desks, that's a lot of requests that the system's making.
[1179.72 → 1183.30] And it really started to slow down other areas of the system.
[1183.30 → 1192.94] So we ended up putting some Los in, which would basically tell us if a request takes longer than eight seconds to fire, we'll burn some of the error budget.
[1193.22 → 1199.48] And we said, oh, we want 96% of all of our labels to be printed within eight seconds.
[1199.48 → 1204.20] And I think within an hour, we burnt all of our budget.
[1204.40 → 1206.16] And we were like, what's going on?
[1206.74 → 1208.04] How is this happening?
[1208.22 → 1213.46] And it was only when we realized that the AJAX request was getting fired multiple times that we changed it.
[1213.46 → 1219.06] And as soon as that fix went out, the graph was like up here, and it just took a most dive.
[1219.28 → 1221.40] And everything was sort of printing within eight or nine seconds.
[1222.12 → 1224.12] And the system seemed to be a lot more stable.
[1224.60 → 1227.92] There are also a few pages that are used for reporting.
[1227.92 → 1230.16] And they're like our internal KPIs.
[1230.28 → 1234.92] They say how many units and orders we've picked at an operator level by day, week, month.
[1235.32 → 1239.08] And they're used a lot by shift managers in the FC.
[1239.78 → 1242.24] And historically, they're a bit slow.
[1242.64 → 1248.32] But in peak, when we're doing a lot more queries than normal, we're going really slow.
[1248.46 → 1252.42] I think what was happening, I'm not sure how much technical detail you want to go into.
[1252.84 → 1253.24] Go for it.
[1253.68 → 1253.92] Yeah.
[1253.92 → 1260.66] We use an ORM in our legacy application and we greedy fetch a lot of stuff.
[1260.92 → 1261.22] Okay.
[1261.48 → 1262.54] And we definitely overfetch.
[1262.96 → 1264.02] From the database, right?
[1264.18 → 1265.08] From the database.
[1265.34 → 1269.30] You're getting a lot of records from the data, a lot of rows, any scanning, anything?
[1269.74 → 1270.88] Yeah, just tons of rows.
[1271.16 → 1273.16] And we've got a reasonably sized buffer pool.
[1273.66 → 1275.78] So like everything, all those queries run in memory.
[1275.78 → 1282.48] But what happens is when the memory in the buffer pool is used up, those queries will start running on disk.
[1283.12 → 1288.74] And once they start running on disk, they get significantly degraded performance.
[1288.90 → 1288.98] Yeah.
[1289.16 → 1289.50] Let me guess.
[1289.54 → 1290.16] Spinning disks?
[1290.76 → 1291.24] HDDs?
[1291.84 → 1295.20] So I thought we'd upgraded to SSDs on our IDS instance.
[1295.64 → 1298.18] But I need to go back and clarify that.
[1298.24 → 1299.34] That will make a big difference.
[1299.60 → 1301.52] And then there's another step up.
[1301.74 → 1303.44] So you go from HDDs to SSDs.
[1303.50 → 1305.26] Then you go from SSDs to Names.
[1305.26 → 1307.24] Yeah, I think that's where we might need to go.
[1307.36 → 1308.72] I think we're at SSD.
[1309.00 → 1316.38] But it's still on those scanning millions of rows queries and overfetching like 100 columns or more at a time.
[1316.94 → 1319.58] Maybe 200 columns, the amount of joins that those queries are doing.
[1320.00 → 1322.52] Yeah, they're going straight into a table.
[1323.02 → 1329.66] But yeah, they were essentially taking the system offline because they would just run for like 10, 15 minutes,
[1329.82 → 1331.36] eat a connection up for that entire time.
[1331.52 → 1333.32] Then you've got someone out there hitting refresh.
[1333.32 → 1336.70] So you've got 30 or 40 of these queries being run.
[1337.16 → 1339.20] And no one else can make requests of the database.
[1339.44 → 1340.08] And it chokes.
[1340.72 → 1346.24] So we ended up finding that if we changed or forced different indexes to be used on some of those queries
[1346.24 → 1348.82] and reduced the column, the breadth of the columns,
[1349.20 → 1352.44] they were able to still run within tens of seconds.
[1352.44 → 1353.46] So it's still not ideal.
[1353.62 → 1355.94] But it was enough to not check the system out.
[1355.94 → 1360.60] And luckily, these things all started happening just ahead of Black Friday.
[1360.82 → 1364.02] So then we were in a much better position by the time Black Friday came along.
[1364.70 → 1373.16] We also found that we accidentally, three years ago, used Regis keys command to do some lookups from Regis.
[1373.16 → 1377.98] And didn't realize in the documentation it says, use this with extreme care in production.
[1378.38 → 1381.50] Because it does an ON scan over the entire set.
[1381.72 → 1382.30] Oh, yeah.
[1382.50 → 1382.62] Okay.
[1382.84 → 1386.44] When you've got 50 million keys in there, it blocks Regis for a while.
[1386.62 → 1387.88] And then things also don't work.
[1388.00 → 1389.68] So we swapped that scan.
[1389.68 → 1392.84] And that alleviated a ton of stress on Regis.
[1393.56 → 1402.06] So, you know, there's some really pivotal changes that we made this year that they weren't massive in terms of like a commit from a commit perspective.
[1402.34 → 1405.72] But they made a huge difference on the performance of our system.
[1406.28 → 1406.50] That's it.
[1406.56 → 1407.62] I mean, that's the key, right?
[1407.64 → 1410.44] It doesn't matter how many lines of code you write.
[1410.86 → 1414.82] People that still think in lines of code, and they're like, how big is this change?
[1414.82 → 1421.70] You actually want the tiny, tiny decisions that don't change a lot at the surface, but have a huge impact.
[1422.20 → 1423.80] Some call them the low-hanging fruit.
[1424.52 → 1426.96] I think that's almost like it doesn't do them justice.
[1427.46 → 1430.36] I think like the big, fat, juicy fruit, which are down.
[1430.80 → 1434.08] Those are the ones that you're going to pick because they make a huge difference to everything.
[1434.22 → 1434.36] Okay.
[1434.40 → 1435.12] Go for those.
[1435.84 → 1441.46] So how did you, I'm wondering, how did you figure out that it was the database?
[1441.46 → 1444.32] It was like this buffer pool, and it was the disks.
[1444.86 → 1450.90] Like, how did you, what did it look like from we have a problem to we have a solution and the solution works?
[1451.00 → 1452.48] What did that journey look like for you?
[1452.68 → 1452.90] Yeah.
[1453.00 → 1460.04] So I'm not sure how much of this was sort of attributed to luck, but we sort of dove straight into the database.
[1460.04 → 1460.90] There's no coincidence.
[1461.10 → 1461.96] There's no coincidence.
[1462.20 → 1463.32] I'm convinced of that.
[1463.46 → 1464.60] Everything happens for a reason.
[1464.82 → 1465.76] There's no correlation.
[1466.14 → 1467.12] Just don't know it yet.
[1467.12 → 1467.56] Yeah.
[1468.14 → 1474.66] But yeah, we just connected to the database, to the show process list and saw the queries that had been running for a long time.
[1474.74 → 1479.76] It's like, hmm, should probably start killing off all these that have been sat there for like a thousand seconds.
[1479.98 → 1480.92] They don't look healthy.
[1481.40 → 1481.66] Okay.
[1482.06 → 1491.92] So before we killed them, we sort of copied the contents of that query, pasted it back in and put an explain before it and just sort of had a look at the execution plan.
[1491.92 → 1498.36] And then saw how many rows it was considering, saw the breadth of the columns that are being used by that query.
[1498.76 → 1504.22] And then when we tried to run it again, it gives you sort of status updates of what the query is doing.
[1504.38 → 1512.14] And when it's just like copying to temp table for about over two minutes, you're like, hmm, that's probably running in disk and not in memory.
[1512.14 → 1518.90] So there's a bit of an educated assumption there of we were 100% confident that's what's happening.
[1519.18 → 1524.54] But based on what the database is telling us it's doing, we're probably assuming that's what's happening.
[1524.80 → 1527.60] None of us are DBA's, just want to sort of clear that up.
[1528.38 → 1532.14] But that was our best educated guess correlated with what we could find online.
[1532.14 → 1544.58] This episode is brought to you by our friends at Ray gun.
[1544.66 → 1550.20] They give software teams instant visibility into the quality and the performance of their software.
[1550.72 → 1554.82] And I'm here with John Daniel Track, co-founder and CEO of Ray gun.
[1555.28 → 1560.14] JD, would you say Ray gun is focused on monitoring or in quotes, observability?
[1560.14 → 1563.78] How do you draw the line? Is it monitoring or is it observability?
[1564.08 → 1568.40] Yeah, I tend to find our industry gets super hung up on labels and what their definitions are.
[1568.52 → 1574.50] You know, you see the constant battle of, you know, is observability really just traces, logs and metrics or is it more?
[1574.62 → 1582.26] And it's like, well, to me, at the end of the day, I think of it as the objective, which is allowed me to fix issues fast and understand how to debug them quickly.
[1582.34 → 1585.86] And if I can do that, I don't really care if it was from a metric, a log or whatnot.
[1586.12 → 1588.18] You know, just help me solve problems quickly.
[1588.18 → 1591.88] And so Ray gun absolutely provides a level of observability.
[1592.34 → 1594.94] And I would class it as the classical term of monitoring.
[1595.16 → 1601.84] But say our APM product, you know, most Arms these days are doing great stuff with things like spans and, you know, measure these things.
[1602.10 → 1606.56] Ray gun's APM does method level profiling right down to it very low overhead.
[1606.56 → 1610.92] You know, and when people bring that in, and they go, hang on, so this integrates with my source control.
[1611.26 → 1612.26] I can look at the code.
[1612.42 → 1615.84] I can see down to the lines of how long this is taking to execute.
[1616.30 → 1621.54] That's actually a level I find of observability that isn't in a lot of the observability companies capabilities.
[1621.72 → 1622.04] Right.
[1622.08 → 1624.76] They have high level of span saying, well, this service took this long.
[1624.86 → 1625.34] It's like, cool.
[1625.42 → 1627.22] But how long did the methods inside it take?
[1627.22 → 1630.38] You know, I want to understand more than just the slow SQL statements.
[1630.52 → 1636.22] I want it to proactively identify code smells, which is, again, another difference that Ray gun's APM has.
[1636.46 → 1643.96] Our vision is to try and have Ray gun feel like it's a virtual team member working 24-7 on your side, identifying things and helping give you the context to fix them.
[1644.18 → 1645.70] To me, that's observability.
[1645.70 → 1646.66] Well said, JD.
[1646.98 → 1647.26] All right.
[1647.30 → 1650.46] Head to Raygun.com to learn more and start your free 14-day trial.
[1650.58 → 1651.56] No credit card required.
[1652.00 → 1658.76] Join thousands of customer-centric software teams who use Ray gun every single day to deliver flawless experiences to their customers.
[1659.06 → 1660.70] Again, Raygun.com.
[1660.70 → 1680.94] Is there something that you think you could have had in place or are thinking of putting in place to make this sort of troubleshooting easier?
[1681.50 → 1686.62] To make this sort of, first, figuring out there is a problem and the problem is most likely in the database.
[1686.78 → 1687.26] Are you thinking?
[1687.78 → 1690.14] So we already have some of that.
[1690.14 → 1697.48] So we use APM in Datadog, and it automatically breaks out queries as their own spans on a trace.
[1697.86 → 1700.82] So you can see when you've got a slow running query.
[1701.28 → 1707.24] And we do have some monitors, alarms that go off if queries exceed a certain breakpoint.
[1707.48 → 1716.80] But there are certain pages and certain queries that we understand as slow, and we kick those into like a known slow page dashboard that we don't tend to look at as much.
[1716.80 → 1722.44] And we don't want to bombard slack because we don't want to be getting all these alarms going off things we know are historically slow.
[1722.94 → 1724.14] There's a few of us on the team.
[1724.68 → 1725.52] A shout-out to George.
[1725.78 → 1731.42] He's a bit of a wizard on Datadog at the moment and really gets stuck in there and building his dashboards.
[1731.42 → 1735.12] And those are the dashboards that we tend to lean towards first.
[1735.20 → 1739.62] You can sort of correlate slow queries with when like disk usage goes up on the database.
[1739.76 → 1741.48] And those dashboards are really helpful.
[1741.48 → 1745.84] But normally when we're in the thick of it, the first thing that I don't run to is Datadog.
[1745.90 → 1748.92] And I don't know why, because it paints a really clear picture of what's going on.
[1749.48 → 1751.90] I tend to, I think it's just muscle memory.
[1752.70 → 1760.64] And just like over the past five years, and we didn't have Datadog, I would run straight to the database first and start doing like show the process log.
[1760.78 → 1761.56] And what's in there?
[1761.60 → 1762.62] And why is that slow?
[1762.62 → 1765.58] And then I forget to go check on my own tool.
[1766.02 → 1774.92] So I think for me, there's a bit more of a learning curve of how do I retrain myself to approach the problem looking at tooling first rather than at the database.
[1776.44 → 1777.00] Okay.
[1777.40 → 1782.30] So Datadog has the APM stuff from the application perspective.
[1782.70 → 1787.94] What other integrations do you use to get a better understanding of the different layers in the system?
[1788.28 → 1789.36] Obviously, there's the application.
[1789.90 → 1791.96] There's the database server itself.
[1791.96 → 1795.06] Then there's the MySQL or PostgreSQL.
[1795.44 → 1796.22] We use MariaDB.
[1796.62 → 1797.10] MariaDB.
[1797.34 → 1797.44] Okay.
[1797.70 → 1799.08] So it's a variant of MySQL.
[1799.42 → 1800.50] In my head, MySQL.
[1800.80 → 1801.72] Legacy, MySQL.
[1801.98 → 1802.16] Okay.
[1802.22 → 1803.42] It's like a fork.
[1803.58 → 1804.14] Which one is it?
[1804.16 → 1804.32] Yeah.
[1804.68 → 1804.92] Okay.
[1805.64 → 1807.16] So the MySQL fork.
[1807.60 → 1816.80] So I don't know, does Datadog have some integration for MySQL, MariaDB so that you can look inside what's happening in the database?
[1817.24 → 1817.86] I believe it.
[1817.92 → 1819.42] And I think we actually integrate with it.
[1819.42 → 1820.88] I just never looked.
[1820.98 → 1821.32] Oh, right.
[1821.32 → 1822.24] I never looked at it.
[1822.28 → 1824.08] You're just like not opening the right tab.
[1824.38 → 1824.64] I see.
[1825.42 → 1825.78] Yeah.
[1825.78 → 1828.54] Because if I look at integrations, we've got like 15 things enabled.
[1828.70 → 1830.24] And it's like, we've got one for EKS.
[1830.88 → 1831.98] Oh, we do have one for RDS.
[1832.42 → 1833.98] So we should be able to see in there.
[1834.06 → 1835.74] We have it for Kafka as well.
[1835.74 → 1839.60] So we can see like any lag on topics and when consumers stop responding.
[1839.60 → 1843.32] So those sorts of things alert us when our edge services are down.
[1843.40 → 1843.96] Yeah.
[1843.96 → 1844.40] Yeah.
[1844.40 → 1845.44] I think we monitor a lot.
[1845.44 → 1846.48] We monitor a lot.
[1846.48 → 1853.02] But we haven't yet fully embraced the culture of let's get everyone to learn what's available to them.
[1853.02 → 1856.10] And that's something that I hope we sort of shift more towards in 23.
[1856.10 → 1861.98] That sounds like a great improvement because each of you having almost like a source of truth.
[1861.98 → 1864.98] Like when something is wrong, where do I go first?
[1865.32 → 1865.70] Great.
[1865.70 → 1868.40] And then when I'm here, what happens next?
[1868.88 → 1873.26] So having almost like a, I want to call it like play by play, but it's a bit more than that.
[1873.26 → 1879.58] It's a bit of what are the important things, like the forks, if you wish, in the road, where I know it's the app.
[1880.16 → 1885.24] Or it's the instance, like the front end instances, if you have such a thing, or it's the database.
[1885.68 → 1889.92] And then even though you have services, I think services make things a little bit more interesting
[1889.92 → 1893.66] because then you have to look at services themselves rather than the applications.
[1893.66 → 1897.90] And then I know there are tools like service meshes come to mind.
[1897.90 → 1901.66] If anything, that's the one thing that, you know, service meshes should help with
[1901.66 → 1907.58] is understood the interaction between services when they degrade automatic Slip, Los, all that stuff.
[1908.12 → 1916.66] So that's something that at least one person would care about full-time and spend, you know, full-time.
[1916.72 → 1921.76] And like they know it outside in or inside out, however you want to look at it, doesn't really matter.
[1921.76 → 1926.02] But they understand it, and they share it with everyone so that people know where to go.
[1926.46 → 1927.82] And they go, that's the entry point.
[1928.28 → 1929.10] Follow this.
[1929.48 → 1932.88] If it doesn't work, let us know how we can improve it, so on and so forth.
[1932.94 → 1937.08] But that sounds, it's like that shared knowledge, which is so important.
[1937.50 → 1940.54] It's a bit of an interesting place because we have a wiki in our GitHub.
[1941.06 → 1944.76] And in that wiki, there are some play-by-plays of common issues that occur.
[1944.76 → 1947.96] I think we've got playbooks for like six or seven of them.
[1948.78 → 1953.22] And when the alarm goes off in Datadog, there's a reference to that wiki document.
[1953.56 → 1958.36] So for those six or seven things, anybody can respond to that alarm and confidently solve the issue.
[1958.74 → 1965.32] But we haven't continued to do that because there aren't that many common issues that frequently occur
[1965.32 → 1968.72] that we've actually then gone and applied a permanent fix for.
[1968.72 → 1971.54] But yeah, we've got a few of these alarms that have been going off for years.
[1971.60 → 1975.52] And it's just like, hey, when this happens, go and do these steps, and you can resolve it.
[1976.08 → 1982.04] And as a solution architect, one of my things that I really want to tackle next year is providing
[1982.04 → 1989.72] more documentation over the entire platform to sort of give people a resource of something's happened in production.
[1990.10 → 1992.72] How do I start tracing the root cause of that?
[1992.72 → 1997.62] And then verifying that what I've done has fixed it for any service that sort of talks to that.
[1997.62 → 1999.50] But yeah, we're not yet.
[2000.34 → 2004.24] Hopefully in our next call, we touch on my documentation.
[2005.00 → 2005.70] Yeah, of course.
[2006.06 → 2008.52] The only thing that matters is that you keep improving.
[2009.04 → 2014.62] I mean, to be honest, everything else, any incidents that come your way, any issues, opportunities to learn.
[2014.94 → 2015.30] That's it.
[2015.36 → 2018.44] Have you improved having had that opportunity to learn?
[2018.62 → 2019.92] And if you have, that's great.
[2020.56 → 2022.12] There'll be many others.
[2022.30 → 2023.36] They just keep coming at you.
[2023.36 → 2026.78] All you have to do is just be ready for them.
[2026.78 → 2027.32] That's it.
[2027.54 → 2028.58] And have an open mind.
[2029.48 → 2039.60] And I'm wondering, so I can see, I know that like the play-by-plays and like playbooks are only so useful because almost every new issue is like a new one, right?
[2039.60 → 2040.64] You haven't seen that before.
[2041.12 → 2044.76] Would it help if you're able to isolate which part of the system is the problem?
[2044.76 → 2051.58] The database versus the CDN, if you have such a thing, network, firewall, things like that.
[2051.58 → 2053.22] Yeah, it would be really useful.
[2053.34 → 2059.36] And one thing we're trying to do to help us catalogue all of these is anytime we have an incident.
[2059.56 → 2061.56] We've not gone for a proper incidents partner yet.
[2061.62 → 2063.00] We were looking at incident IO.
[2063.26 → 2064.56] We haven't sprung for it yet.
[2064.88 → 2066.98] We just have an incidents channel inside of Slack.
[2066.98 → 2075.88] And we essentially start a topic there, and we record all the steps that happened through that incident inside that log.
[2075.88 → 2085.78] So if we ever need to go back and revisit it, we can see exactly what caused the issue and also what services or pieces of infrastructure were affected.
[2086.44 → 2088.16] Because Slack search is pretty nice.
[2088.30 → 2090.00] You can jump into the instance channel.
[2090.52 → 2091.28] Something's gone wrong.
[2091.40 → 2097.40] You do a search, and can normally find something that might point you in the right direction of where you need to steer your investigation.
[2098.06 → 2102.06] We know it's not the most perfect solution, but it's worked so far.
[2102.06 → 2103.28] If it works, it works.
[2103.78 → 2105.34] If it works, that's it.
[2105.72 → 2111.90] You mentioned Slip and Los and how they helped you understand better what is happening.
[2112.00 → 2116.34] I mean, first, signalling there's a problem with something that affects users.
[2116.84 → 2120.34] And then, you know, being able to dig into it and troubleshoot and fix it.
[2121.24 → 2123.78] Are Slip and Los a new thing that you started using?
[2124.10 → 2132.04] Yeah, we're really sort of dipping our toes in the water and starting to get used to, starting to implement them across our services.
[2132.06 → 2135.08] I think we currently have just two Los.
[2135.18 → 2135.98] It's better than zero.
[2136.26 → 2136.62] Exactly.
[2137.08 → 2139.64] We haven't yet decided on Slip.
[2139.82 → 2150.50] We've got a chat next week with George, and we're going to sit down and think what components make up this SLO that can sort of give us an indication before it starts triggering that we've burnt too much of our budget.
[2150.50 → 2157.60] So we've both got like a shared interest in SRE, and we're trying to translate that into James and James.
[2158.26 → 2162.00] But yeah, still very much amateur and just experimenting as we go.
[2162.12 → 2168.58] But it's nice to see a peak this year that the SLO that we did create give us some real value back.
[2169.28 → 2174.00] Whereas previously we would have just let it silently fail in the background and be none the wiser.
[2174.84 → 2175.50] Yeah, that's amazing.
[2175.68 → 2178.26] It is just like another tool in your toolbox, I suppose.
[2178.68 → 2179.76] I don't think you want too many.
[2179.96 → 2182.54] They're not supposed to use like alarms, right?
[2182.58 → 2186.60] Especially when, you know, you know, like thousands and thousands of engineers.
[2186.90 → 2189.70] But by the way, how many are you now in the engineering department?
[2189.70 → 2195.72] Ooh, I think we're eight permanent and four contract, I believe.
[2196.54 → 2198.62] Okay, so 12 people in total.
[2199.16 → 2201.06] That's, again, that's not a big team.
[2201.44 → 2207.74] And it means that everyone, you know, gets to experience pretty much everything that happens, some shape or form.
[2208.08 → 2210.90] I think you're slightly bigger than a two pizza team, I think.
[2211.50 → 2213.36] Unless the pizzas are really, really large.
[2213.36 → 2218.00] So you're not like, you know, sure, you can be one team.
[2218.04 → 2223.98] And I can imagine that like retros, if you have them, or stand-ups or things like that are getting a bit more complicated with 12 people.
[2224.26 → 2227.00] Still manageable, but 20, forget about it.
[2227.00 → 2227.82] It's just like too much.
[2227.98 → 2229.60] Yeah, it was getting a bit tough.
[2229.78 → 2235.16] And what we do now is we have a single, like, huddle, single stand-up once a week, an hour long.
[2235.42 → 2238.54] Everyone gets in and sort of unites their teams and what we've been doing.
[2239.14 → 2241.52] And then we have like breakout teams.
[2241.52 → 2243.22] So we've got four subteams.
[2243.52 → 2243.86] That makes sense.
[2244.02 → 2245.40] And yeah, we have our dailies with them.
[2245.52 → 2247.04] And that seems way more manageable.
[2247.64 → 2248.28] That makes sense.
[2248.32 → 2248.78] Yeah, exactly.
[2249.24 → 2254.38] But still, you're like small enough, again, to have a good understanding of most of the system, right?
[2254.42 → 2258.00] I mean, once you get like 20, 30, 40, it just becomes a lot more difficult.
[2258.22 → 2261.86] Because the system grows, more services, different approaches.
[2262.36 → 2265.40] And maybe you don't want consensus, because that's very expensive, right?
[2265.40 → 2267.04] The more you get, the more expensive that gets.
[2267.18 → 2268.74] It just doesn't scale very well.
[2268.74 → 2272.68] But what I'm thinking is Slip and Los are a great tool.
[2273.32 → 2277.36] A few of them that you can all agree on, all understand.
[2277.96 → 2279.24] And at least like focus on that.
[2279.38 → 2282.02] You know, focus on delivering good Los.
[2282.50 → 2284.44] Now, actually good Slip, right?
[2284.58 → 2285.74] Slip that match.
[2286.44 → 2287.64] That everyone can agree on.
[2288.00 → 2288.94] Everyone understands.
[2289.44 → 2294.60] And you know, it's a bit of clarity in what is a chaotic.
[2294.60 → 2295.88] Because it is, right?
[2295.94 → 2299.24] Like when you have two, three incidents happening at the same time, it does happen.
[2299.98 → 2300.36] Okay.
[2300.68 → 2300.90] Okay.
[2301.34 → 2305.10] So these past few weeks have been fascinating for you.
[2305.32 → 2306.80] Because it's been the run-up to Christmas.
[2307.14 → 2308.36] More orders, as you mentioned.
[2308.46 → 2309.70] The system was getting very busy.
[2310.30 → 2312.46] What was the day-to-day like for you?
[2312.48 → 2318.02] Because I think you're mentioning at some point that you were with the staff on the picking floor.
[2318.02 → 2322.60] You're using the system that you have improved over those months.
[2322.76 → 2323.56] What was that like?
[2323.88 → 2325.60] Yeah, it was fascinating.
[2325.86 → 2329.52] This year, I really wanted to just use pick part of the system.
[2329.88 → 2331.62] So last year, I did a bunch of packing of orders.
[2331.76 → 2332.44] And that was fine.
[2332.82 → 2335.44] But after spending sort of like four months free writing pick,
[2335.94 → 2340.50] I really wanted to just take a trolley out and just go pick a ton of orders and experience it for myself.
[2341.20 → 2343.92] So yeah, I did three days, three full days down there.
[2344.28 → 2345.14] Picked, what was it?
[2345.26 → 2346.32] A thousand orders.
[2346.48 → 2346.80] Wow.
[2346.80 → 2348.58] Lots of socks.
[2348.68 → 2349.80] Too many socks to...
[2349.80 → 2350.40] Okay.
[2351.82 → 2354.02] I don't want to see another pair of socks for a while.
[2356.16 → 2359.98] But yeah, it was really nice to sort of get down there and involve everybody
[2359.98 → 2363.22] and sort of going around and talking to operators
[2363.22 → 2367.02] and sort of saying parts of the system they liked,
[2367.10 → 2368.28] but also parts they didn't like.
[2368.44 → 2371.96] And parts they felt slowed them down versus what the old one did.
[2371.96 → 2374.54] And it got some really, really useful feedback
[2374.54 → 2378.08] and what we could then put into the system going into 2023.
[2378.58 → 2380.64] And we try and do...
[2380.64 → 2385.52] We have like two or three motored days a year when we will all go down into the FC
[2385.52 → 2391.48] and we'll just pick in and pack in or booking in just so we can get a feel for what's going on down there
[2391.48 → 2393.52] and how well the system's behaving.
[2393.52 → 2396.80] But like peak, when it's our most busy time of year,
[2396.80 → 2398.92] it's sort of like everybody, all hands on deck.
[2399.06 → 2400.50] We all get down there, all muddle in.
[2401.02 → 2406.16] DJ plays like some music in the warehouse, and we've got donuts and stuff going around.
[2406.40 → 2408.08] Yeah, so it's a nice time of year.
[2408.18 → 2412.08] Everybody sort of gets together and muddles in and makes sure that we get all the orders out in time.
[2412.08 → 2420.12] And yeah, I did some statistics earlier and out of the 300,000 orders that left our UK warehouse,
[2420.30 → 2422.06] we processed them all within a day.
[2422.90 → 2430.20] So yeah, it gives you an idea of how quickly those orders need to come in and get out once we receive them.
[2431.12 → 2432.76] That's a lot of like 300 a day.
[2432.84 → 2434.88] This is like, how many hours do you work?
[2435.10 → 2436.50] So 24-7 operation.
[2436.90 → 2437.90] 24-7, okay.
[2437.90 → 2441.32] So that is 12,500 per hour.
[2442.40 → 2447.24] That is 3.5 orders per second.
[2447.66 → 2448.60] That's crazy, isn't it?
[2449.30 → 2453.04] Every second, 3.5 orders get ready.
[2453.28 → 2454.14] Can you imagine that?
[2454.44 → 2455.64] And that's like 24-7.
[2456.38 → 2457.26] That's crazy.
[2457.64 → 2457.94] Wow.
[2458.34 → 2460.88] And we're still quite small in the e-com space.
[2461.20 → 2463.30] It's going to be interesting to see where we are this time next year.
[2463.30 → 2471.00] So six months ago, you were thinking of starting to use Kubernetes.
[2472.06 → 2474.22] You have some services now running.
[2474.54 → 2477.18] You even got to experience what the end users see.
[2478.02 → 2479.92] What are you thinking in terms of improvements?
[2480.20 → 2481.00] What is on your list?
[2481.64 → 2483.30] Oh, that's a really hard one.
[2483.60 → 2488.68] I want to get more tests of our legacy system to run.
[2488.68 → 2499.14] So we had another incident where we'd essentially deployed a change, and it took production down for like six or seven minutes for our internal staff.
[2499.78 → 2502.16] And it would have been caught by a smoke test.
[2502.64 → 2505.70] Like outright, the system just wouldn't have booted.
[2506.22 → 2511.54] And we've now put deployment pipeline in place, which will run those smoke tests and ensure the application boots.
[2511.54 → 2513.98] And it would just run through a couple of common pages.
[2514.30 → 2517.22] And that was a result of that incident.
[2517.64 → 2525.46] But what we really want to do is gain more confidence that when we deploy anything into production for that existing system,
[2525.80 → 2532.36] we're not going to degrade performance or take down certain core parts of the application.
[2532.90 → 2538.10] What we want to probably do is come up with a reasonable time to deploy.
[2538.10 → 2544.18] Maybe we say the test harness that runs can't take more than 10 minutes to deploy to production.
[2544.56 → 2547.12] Because we still want to keep that agility that we've got.
[2547.28 → 2555.00] One of the real benefits that we've got working here is deployment and turn into production is under sort of two or three minutes.
[2555.70 → 2561.44] And if we have a bug, we can revert really quickly, or we can iterate on it quickly and push out.
[2561.68 → 2567.66] So having a deployment pipeline that sits in the way and takes over 10 minutes to run, that's really going to affect your agility.
[2567.66 → 2573.74] So yeah, next year, I really want the team to work on hardening our deployment pipeline,
[2574.08 → 2576.22] just so we can keep gaining confidence in what we're releasing.
[2576.60 → 2582.30] Especially as we plan to scale our team out, we're going to have much more commits going through on a daily basis.
[2583.20 → 2589.16] Now, when you say deploying, I'm wondering, do you use Blue green for your legacy app?
[2589.40 → 2590.60] No, not yet.
[2590.60 → 2597.86] Because if you had two versions running at any given point in time, so the old one, the legacy one,
[2597.98 → 2605.20] and, you know, just basically change traffic the way it's spread, then rollbacks would be nearly instant.
[2605.96 → 2610.56] I mean, the connections, obviously, they would have to maybe reconnect depending on how the app works,
[2610.64 → 2615.26] whether persistent, whether, you know, retry, and everything goes back as it was.
[2615.26 → 2620.90] And if it's a new one, if it doesn't boot, so if it can't boot in your incidents case,
[2621.14 → 2625.50] then it never gets promoted to live because it never came up, and it's not healthy.
[2625.96 → 2628.84] Yeah, that would be really nice if we could get that in place.
[2629.22 → 2633.34] I think our deployment pipeline for legacy at the moment is just,
[2633.92 → 2637.82] hey, push these new changes to these 12 nodes and do it all in one go.
[2637.82 → 2642.20] And then, yeah, flush the cache on the last node that you deploy to.
[2642.70 → 2649.00] It's very basic, whereas the newer services do have, like, all the bells and whistles of Blue green
[2649.00 → 2653.36] and, like, integration and unit tests that run against it to give us that confidence.
[2654.20 → 2657.80] Would migrating the legacy app to Kubernetes be an option?
[2658.24 → 2659.18] We're thinking about it.
[2659.34 → 2665.44] So only one issue that I've run up to so far, so I've voucherized the application, runs locally.
[2665.44 → 2671.16] The one annoying thing where it can't request assets, and this is probably, like,
[2671.78 → 2678.66] some gap in my knowledge in docker, is it runs all in its, like, docker network.
[2679.00 → 2684.68] And then when it tries to go out to fetch assets, it's referencing the docker container name
[2684.68 → 2688.16] where it should actually be referencing something else, which should be, like,
[2688.58 → 2691.94] outside that docker network, and that causes assets to not load.
[2691.94 → 2696.50] So once I fix that, we'll be able to move it into production.
[2696.80 → 2699.20] But that's a pretty big dealbreaker at the moment.
[2699.72 → 2700.36] Yeah, of course.
[2700.84 → 2705.66] When you say assets, do you mean static assets like JavaScript, CSS, images, things like that?
[2705.90 → 2709.20] Yeah, like PDFs and those sorts of things.
[2709.34 → 2710.60] Okay, yeah, okay, okay.
[2710.68 → 2712.84] So, like, the static files, okay, okay, interesting.
[2713.64 → 2718.96] I remember, I mean, that took us a while because the static assets, I mean, in our case,
[2718.96 → 2725.00] the changelog app before it went onto Kubernetes, it had volume requirements, right, the persistent
[2725.00 → 2725.92] volume requirement.
[2726.40 → 2732.94] And the thing which enabled us to consider, just consider scaling to more than one, was
[2732.94 → 2737.34] decoupling the static assets from the volume from the app.
[2737.40 → 2741.14] If the app needs to mount a volume, it just makes things very, very difficult.
[2741.28 → 2745.00] So moving those to S3 made a huge, huge difference.
[2745.00 → 2749.72] So then, you know, I mean, in your case, I'm assuming it's another service that has to
[2749.72 → 2750.52] be running, right?
[2750.54 → 2753.18] It's trying to access another service that has the assets.
[2753.62 → 2753.76] Yeah.
[2754.02 → 2757.02] Yeah, because we've got a bunch of stuff in S3 and requesting that's fine.
[2757.40 → 2761.20] But it's any time it needs to request something that's on that host.
[2761.38 → 2764.54] And then it's using the Docker container name rather than the host name.
[2765.22 → 2768.72] And the whole reason is just because of the way that legacy application is written.
[2769.04 → 2773.40] It's a configuration variable that says, what's the name of my service that I need to reach
[2773.40 → 2778.48] out to, but when you're accessing it externally into the container, you can resolve it with
[2778.48 → 2779.22] the container name.
[2779.44 → 2784.62] But when the container tries to resolve it internally to itself, it then falls over and
[2784.62 → 2785.64] doesn't work.
[2786.28 → 2787.40] Oh, I see what you mean.
[2787.50 → 2787.76] Okay.
[2787.84 → 2788.10] Okay.
[2788.58 → 2791.08] And you can't make it like local host or something like that.
[2791.18 → 2791.52] Exactly.
[2791.68 → 2796.00] Because I have like on my local machine, it's like manager.controlport.local.
[2796.00 → 2801.44] But then internally, Docker would see that as deepworld.php, which is the name of the
[2801.44 → 2801.82] container.
[2802.08 → 2807.18] But it's trying to go through manager.controlport.local, which doesn't exist on that network.
[2807.42 → 2809.56] So then it just goes, I don't know what you're talking about.
[2809.84 → 2811.84] And yeah, that's the end of it.
[2812.28 → 2819.82] Well, as it's becoming obvious, I am like a how should I say, how should I say this?
[2819.94 → 2820.72] I'm like a magpie.
[2820.84 → 2821.70] It's a shiny thing.
[2821.86 → 2823.44] I have to understand, like, what's the problem?
[2823.44 → 2824.18] Oh, problem?
[2824.50 → 2825.58] Like, oh, I love this.
[2825.74 → 2826.76] Like, tell me more about it.
[2826.86 → 2831.18] I'm like basically sucked into troubleshooting your problem live as we're recording this.
[2831.50 → 2832.78] So, okay.
[2832.88 → 2837.44] I think we'll put a pin in it for now and change the subject.
[2837.70 → 2838.94] This is really fascinating.
[2839.56 → 2842.38] But let's go to a different place.
[2842.70 → 2842.94] Okay.
[2843.84 → 2849.76] What are the things that went well for you and for your team in the last six months as
[2849.76 → 2851.72] you've been improving various parts of your system?
[2852.00 → 2852.52] Yeah.
[2852.52 → 2857.68] So I think the biggest thing that's been really our biggest success in this year is that whole
[2857.68 → 2859.56] rewrite of the PIC application.
[2860.18 → 2863.20] The fact we went from no services.
[2863.70 → 2865.20] I just sort of want to be clear as well.
[2865.28 → 2868.96] When I talk about services, how we're planning to structure application.
[2869.22 → 2875.18] We're not going like true microservice, like hundreds of services under each domain part
[2875.18 → 2875.76] of the system.
[2875.76 → 2880.98] What we're really striving to do is say, we have this specific part of domain knowledge
[2880.98 → 2881.48] in our system.
[2881.60 → 2882.70] So PIC, for example.
[2883.18 → 2885.90] We also have PAC and maybe Goodwin.
[2886.36 → 2890.62] And we want to split those like three core services out into their own applications.
[2891.18 → 2897.00] And as we scale the team, we've then got the ability to say, right, team X looks after
[2897.00 → 2897.34] PIC.
[2897.74 → 2899.14] Team Y looks after PAC.
[2899.14 → 2901.08] And they're discrete and standalone.
[2901.58 → 2905.00] So yeah, we can just manage them as their own separate applications.
[2905.00 → 2906.22] Is there a POC?
[2906.56 → 2907.36] I had to ask that.
[2907.48 → 2909.38] There's PIC, there's PAC, there has to be a POC.
[2910.48 → 2911.78] Those are some great names.
[2912.62 → 2913.66] Ha, no POC.
[2914.82 → 2915.22] Okay.
[2915.26 → 2916.82] There's lots and lots of POCs, right?
[2916.86 → 2918.36] Lots of proof of concepts.
[2918.80 → 2919.02] Yeah.
[2919.76 → 2924.16] Well, we had a POC six months ago and it's now actual real production.
[2924.50 → 2925.24] It's now PIC.
[2925.78 → 2927.52] It evolves from a POC to a PIC.
[2927.94 → 2928.28] Right.
[2930.02 → 2930.42] Right.
[2930.42 → 2930.78] Yeah.
[2931.58 → 2937.68] But it was really fascinating to sort of go from, we've never put a microservice out
[2937.68 → 2938.16] into production.
[2938.48 → 2945.10] And we've now somehow got this cluster that's running two microservices and the user experience
[2945.10 → 2950.54] from the operator's perspective, they either go to the old legacy application that has its
[2950.54 → 2952.68] front end or the new remix application.
[2953.34 → 2956.58] And regardless of which one you go to, it feels like the same user experience.
[2956.58 → 2962.10] And to build that in six months and have a cohesive end-to-end experience, just, yeah,
[2962.16 → 2965.10] it's something that we're sort of really, really proud of for delivering that in such
[2965.10 → 2966.08] a short period of time.
[2966.32 → 2973.10] And also to like not have that many catastrophic failures on something so big, like it was really
[2973.10 → 2978.90] nerve wracking being responsible for carving out something that's used every single day,
[2979.68 → 2984.40] building a new variance of it that performs like significantly better, but also introduces
[2984.40 → 2987.52] some new ideas to actually gain operational efficiency.
[2988.34 → 2993.12] And then to see it like out in the wild and people are using it and the operation's still
[2993.12 → 2996.80] running, nothing's full on that space apart from when we didn't set the cache driver to
[2996.80 → 2997.22] be Regis.
[2997.82 → 3000.80] But apart from that, it felt seamless.
[3001.24 → 3006.82] And sort of re-educating the team as well to start thinking about feature flags and the
[3006.82 → 3011.38] benefits of Canary releases and how that gives external stakeholders confidence.
[3011.38 → 3015.40] Yeah, there's a lot of new tooling that's came in, and I'm really happy with how the team
[3015.40 → 3016.32] started to adopt it.
[3016.88 → 3016.98] Yeah.
[3017.24 → 3022.32] Not to mention Slip and Los that the business cares about and the users care about and you
[3022.32 → 3023.30] can say, hey, look at this.
[3023.44 → 3023.86] We're good.
[3024.36 → 3025.34] The system is too stable.
[3025.42 → 3026.22] We have to break something.
[3027.06 → 3027.46] Yeah.
[3027.56 → 3032.46] I think the next stage is to put a status page up so that our like stakeholders and clients
[3032.46 → 3036.86] can sort of see uptime of the service and sort of gain an understanding of what's going
[3036.86 → 3037.60] on behind the scenes.
[3037.60 → 3042.40] But we'll only really be able to do that once we've got a list of Slip and Los in
[3042.40 → 3043.76] place that will drive those.
[3043.96 → 3044.98] Only if it's real time.
[3045.36 → 3049.66] The most annoying thing is when you know GitHub is down, but GitHub doesn't know it's down.
[3049.98 → 3050.68] It's like, damn it.
[3051.20 → 3053.68] It's not, I can guarantee that GitHub is down.
[3054.08 → 3056.28] Five minutes later, status page, of course, is down.
[3057.24 → 3061.50] So that's the most annoying thing about status pages is when they're not real time.
[3061.62 → 3063.68] I know there will be a little bit of a delay, right?
[3063.68 → 3066.28] It's like seconds, even 30 seconds is okay.
[3066.80 → 3072.38] But I think if it's SLI and SLO driven, that's a lot better because you start seeing that
[3072.38 → 3076.96] degradation as it happens with like some delay, 15, 30 seconds.
[3076.96 → 3077.76] That's acceptable.
[3078.14 → 3081.98] Any more than a minute, and it's masking too many things.
[3081.98 → 3082.46] Yeah.
[3082.72 → 3085.82] So do you, I'm completely new to all this stuff.
[3085.98 → 3089.52] I thought the status page was driven by those Slip and Los.
[3089.60 → 3092.10] Is that not something like, that'd be really cool.
[3092.10 → 3096.66] It depends, which, I mean, there's obviously various services that do this, you know, you
[3096.66 → 3098.86] pay for them, and it's like a service which is provided.
[3099.72 → 3102.32] Sometimes it can be a dashboard, a status page.
[3102.44 → 3104.78] I mean, you know, like a read only thing.
[3105.22 → 3106.82] They are somewhat better.
[3106.94 → 3110.20] It's just like deciding what to put on it, you know?
[3110.24 → 3113.70] And then when you have an incident, how do you summarize that?
[3113.76 → 3114.64] How do you capture that?
[3114.72 → 3120.58] How do you communicate to people that maybe don't need to know all the details, but they
[3120.58 → 3121.80] should just know there's a problem.
[3122.32 → 3126.80] So it's almost like you would much rather have almost like checks, you know, like when
[3126.80 → 3128.96] a check fails, it goes from green to red.
[3129.08 → 3131.06] You know, there's a problem with a thing.
[3131.24 → 3137.36] It's near real time, but you hide like, because to be honest, I don't care why it's down.
[3137.48 → 3141.90] I just want confirmation that there's a problem on your end, and it's not a problem on my end
[3141.90 → 3144.14] or somewhere in between, right?
[3145.12 → 3145.46] Okay.
[3146.12 → 3147.92] So we talked about the status page.
[3148.36 → 3151.24] We talked about, what else did we talk about?
[3152.22 → 3154.62] Things that are, that you would like to improve.
[3154.96 → 3155.16] Yeah.
[3155.40 → 3155.56] Yeah.
[3155.64 → 3156.92] It's about Slip, Slip.
[3157.28 → 3157.70] Slip.
[3157.78 → 3157.88] Yeah.
[3158.04 → 3158.40] That's right.
[3158.58 → 3159.98] The deployment pipeline for legacy.
[3160.24 → 3160.80] Ah, yes.
[3160.88 → 3161.52] That was the one.
[3161.60 → 3162.64] How could I forget that?
[3162.90 → 3163.62] Deployment pipeline.
[3163.92 → 3164.42] Okay, cool.
[3164.42 → 3171.76] So these seem very specific things, very almost like it's easy to imagine, easy to, you know,
[3171.90 → 3172.68] work with.
[3173.08 → 3177.64] What about some, some higher level things that you have planned for 2023?
[3178.18 → 3179.78] The year will be long for sure.
[3180.24 → 3180.42] Yeah.
[3180.60 → 3186.34] So we sort of had a big change this year when we've spoken about, we got pick, changes
[3186.34 → 3191.10] to pick, and we're changing pack next year, but we're trying to think from like an operational
[3191.10 → 3196.26] perspective, how can we gain more efficiency out of our sort of packers?
[3197.02 → 3203.04] And right now, when you finished picking a trolley, you put it in like a drop zone and
[3203.04 → 3207.26] then someone called, who's called a water spider, they come in, they grab the trolley,
[3207.36 → 3212.62] they shimmy it off to the packing desk and then the packer puts it into a bin and that
[3212.62 → 3215.82] water spider comes back and takes the bin that's full of orders over to a dispatch
[3215.82 → 3216.18] desk.
[3216.18 → 3223.18] And what we want to do is start automating that last bit of the journey from the pack
[3223.18 → 3225.48] station to dispatch and labelling.
[3226.18 → 3230.16] And essentially what we'll do then is an operator will finish packing their order.
[3230.68 → 3236.06] They'll put it onto a conveyor belt and that conveyor belt will have a bunch of like sensors
[3236.06 → 3242.14] on it, which will sort of do weighing as the order is like conveyancing from the pack
[3242.14 → 3243.92] desk to the outbound desk.
[3243.92 → 3249.84] And if the order is not within like a valid tolerance that we're happy with, we will kick
[3249.84 → 3255.38] it back into a like problem order bin, which will be like re-weighed and re-labelled.
[3255.54 → 3261.14] Because I said earlier, we got rid of the weighing step and there's a certain variance that our
[3261.14 → 3263.36] carriers will tolerate saying, yep, that's fine.
[3263.42 → 3264.80] It's within like X amount of grams.
[3264.94 → 3265.88] We'll still process it.
[3265.88 → 3271.54] But if we go like too much under or too much over, we can get chargebacks from the carrier
[3271.54 → 3275.38] to say, hey, you sent us this order, and it didn't have the correct weight.
[3275.72 → 3277.64] So we want to start like handling those in-house.
[3278.34 → 3282.36] And what's going to be fascinating is like building the Los and Slip around that.
[3282.36 → 3286.46] Like how many orders are we weighing at pack?
[3286.52 → 3288.88] Are we skipping weighing at pack, putting on the conveyancing system?
[3288.98 → 3290.24] And how many orders are we kicking out?
[3290.60 → 3295.32] And to have like an error budget on that and seeing like how accurate our product weights
[3295.32 → 3300.12] are in the system, how accurate our like packaging weights are, it's going to be fascinating
[3300.12 → 3301.70] to see that in operation next year.
[3301.70 → 3307.08] So I think the plan is we'll probably like to get an independent contractor to come in and
[3307.08 → 3307.94] set up the conveyancing.
[3308.20 → 3313.74] But then we want our own bespoke software running in that pipeline that we can hook into and
[3313.74 → 3315.22] start like pulling data out of that.
[3315.36 → 3319.04] And I'm really, really excited to start working on some of those automation pieces.
[3319.40 → 3324.98] It's fascinating how you're combining the software with the real world, right?
[3325.06 → 3330.32] So how everything you do, like you can literally can go in the warehouse and see how the software
[3330.32 → 3334.72] is being used, what is missing, what software is missing, what can be made more efficient.
[3335.04 → 3339.80] Because what you just described is a real world process that can be simplified, can be made
[3339.80 → 3344.20] more efficient by adding a bit more software and that belt.
[3344.34 → 3345.04] Very important.
[3345.24 → 3345.62] Okay.
[3345.66 → 3346.50] With the right senses.
[3347.16 → 3347.64] Okay.
[3347.64 → 3352.90] I think one of the fascinating parts about our company is everything end to end is
[3352.90 → 3357.80] bespoke from like order ingest to order being dispatched from the warehouse.
[3358.12 → 3360.22] We control everything in that pipeline.
[3360.96 → 3363.32] The only things we depend on is buying labels from carriers.
[3363.58 → 3369.82] I mean, we spoke at some point about managing our own like price matrices in real time of
[3369.82 → 3372.58] the carriers and doing our own quoting and printing our own labels.
[3373.24 → 3377.06] Maybe one day we'll go in that direction, but it's a lot of work and there are companies
[3377.06 → 3378.64] out there that are dedicated to doing that.
[3378.76 → 3380.92] So we have those as partners for now.
[3381.20 → 3386.04] But yeah, apart from that, pretty much everything out in the FC is completely bespoke.
[3386.04 → 3386.48] Hmm.
[3386.88 → 3388.68] You mentioned FC a couple of times.
[3388.88 → 3389.60] Fulfillment Centre.
[3389.88 → 3390.02] Yes.
[3390.02 → 3390.72] That's what it is.
[3390.86 → 3391.00] Yes.
[3391.00 → 3391.10] Okay.
[3391.10 → 3392.24] I was thinking, what is it?
[3392.30 → 3393.02] What is FC?
[3393.36 → 3394.56] It's not a football club.
[3395.80 → 3397.50] Because it's like the World Cup is on.
[3397.70 → 3399.84] So FC, though, like we, it's easy to associate.
[3399.96 → 3401.80] We're primed to associate with a football club.
[3401.80 → 3402.82] So it's not that.
[3403.22 → 3404.04] Fulfillment Centre.
[3404.20 → 3404.78] That's what it is.
[3404.98 → 3405.14] Yeah.
[3405.24 → 3409.46] We used to, we used to be warehouses, but I think fulfillment centre is more accurate
[3409.46 → 3410.06] to what we do.
[3410.84 → 3413.02] Do you see more Kubernetes in your future?
[3413.50 → 3415.04] Just about the same amount or less?
[3415.28 → 3415.82] What do you think?
[3416.20 → 3421.56] So I think purely because we're moving to a more service oriented architecture, we're
[3421.56 → 3424.36] probably going to continue to depend on Kubernetes.
[3424.36 → 3432.48] I can't see how practical a world would be where we have to keep like provisioning new
[3432.48 → 3437.84] EC2 instances and like setting up our deployment pipelines to have specific EC2 instances as
[3437.84 → 3442.70] targets and managing all the ingress to those instances like manually through route.
[3442.86 → 3444.70] It just feels a bit messy.
[3445.38 → 3451.08] Having one point of entry to the cluster and also being able to like port that from AWS
[3451.08 → 3456.92] to like GCP in future, if we ever wanted to move cloud providers, I think for us, it
[3456.92 → 3459.36] makes more sense to stay on Kubernetes.
[3460.14 → 3460.50] Okay.
[3460.98 → 3463.80] Technology wise, Datadog was also mentioned.
[3463.98 → 3468.18] So I'm feeling a lot of love for Datadog coming from you because it just makes a lot
[3468.18 → 3472.98] of things simpler, even though easier to understand, even though it's not muscle memory just yet.
[3473.88 → 3477.48] Are there other services that you quite enjoyed using recently?
[3478.18 → 3478.50] Yeah.
[3478.50 → 3483.04] So, I mean, I'm shouting out to Datadog again, but it's just, it's another part of their ecosystem.
[3483.54 → 3486.08] They have something called RUM, real-time user monitoring.
[3486.96 → 3491.30] And when we actually deployed the PIC service, we were getting tons of feedback, but there
[3491.30 → 3495.04] was not real way to like to correlate the weird edge cases people were having.
[3495.48 → 3497.30] And we installed RUM.
[3497.30 → 3505.10] And basically like what it does is it records the user session end to end, takes like screenshots
[3505.10 → 3506.88] and then uploads it to Datadog.
[3507.54 → 3509.70] And you can play that session back and watch it through.
[3509.96 → 3513.98] But it will also have like a timeline of all the different events that that operator clicked
[3513.98 → 3514.66] on through that timeline.
[3514.66 → 3520.08] So you can scrub through it and attach as much meta information to that trace as you'd like,
[3520.16 → 3522.38] just like with any other like open telemetry trace.
[3522.38 → 3528.10] So in our example, we would get a bit lost because we couldn't correlate a screen recording
[3528.10 → 3530.96] to some actual like PIC root data that was stored in S3.
[3531.66 → 3537.16] Whereas now like we store the PIC root into S3, which is like all the raw data that the
[3537.16 → 3539.26] operator interacts with from an API perspective.
[3539.26 → 3544.94] But we also take that PIC root ID and attach it to the trace along with their user ID and
[3544.94 → 3546.50] along with the trolley they were picking on.
[3547.06 → 3552.16] So now we can just go into Datadog and say, hey, give me all the traces for this user that
[3552.16 → 3552.96] on this trolley.
[3553.28 → 3557.16] And if they said like they had a problem on Sunday with that trolley, we can now easily
[3557.16 → 3559.22] find that screen recording and watch it back.
[3559.70 → 3564.68] And then we can also then correlate out of all the backend traces that happened in that
[3564.68 → 3565.18] time period.
[3565.18 → 3572.74] So like we used to use Datadog and Sentry and even though I don't have like any, like
[3572.74 → 3577.34] not, I don't have a lot of love for Sentry and I think they're a great product, having
[3577.34 → 3581.14] it all under one roof and being able to tie all your traces together and get an end-to-end
[3581.14 → 3583.54] picture of exactly what a journey looked like.
[3583.90 → 3586.44] I'm really starting to enjoy that experience with Datadog.
[3586.82 → 3587.22] Nice.
[3587.56 → 3588.18] Very nice.
[3588.32 → 3588.58] Okay.
[3589.52 → 3590.14] That makes sense.
[3590.18 → 3591.30] I mean, it makes sense.
[3591.52 → 3592.84] I would want to use that, right?
[3592.84 → 3596.12] If I were in that position, like why wouldn't I want that?
[3596.80 → 3598.22] Sounds super, super helpful.
[3598.68 → 3601.92] And if it works for you, you know, it's most likely to work for others.
[3602.32 → 3602.68] Interesting.
[3603.62 → 3605.50] Anything else apart from these two?
[3606.50 → 3608.56] I'm trying to think what else I've used.
[3608.66 → 3612.34] I mean, I was looking a bit at Honeycomb and I really wanted to get it up and running
[3612.34 → 3614.72] for us, but they don't yet have a PHP SDK.
[3615.50 → 3619.30] You know, you have to sort of set it up with an experimental one that's sort of community
[3619.30 → 3619.54] driven.
[3619.74 → 3621.38] I just haven't had the time to plug into it.
[3621.38 → 3627.78] I went through their interactive demos online and I really, really, really want to try it.
[3627.98 → 3630.64] It's bugging me that we can't make it work for us just yet.
[3631.06 → 3632.48] But no additional tooling.
[3632.74 → 3634.36] Those are the two that's on my list.
[3634.94 → 3635.18] Okay.
[3635.86 → 3642.14] So as we prepare to wrap up for those that stuck with us all the way to the end, is there
[3642.14 → 3645.48] a key takeaway that you'd like them to have from this conversation?
[3646.20 → 3649.70] Something that if they were to remember one thing, what would that thing be?
[3649.70 → 3656.56] Yeah, I think don't be scared to keep moving the needle and keep iterating on what you've
[3656.56 → 3656.80] got.
[3656.98 → 3662.30] Even if you want to try a new service in production, having the sort of foresight to
[3662.30 → 3667.50] say we can gracefully roll this out and scale it out, but also gracefully roll it back if
[3667.50 → 3668.16] we've got issues.
[3668.16 → 3669.48] It's really powerful.
[3670.04 → 3675.08] And from my experience, like I've touched on today, the more you do it, the more confidence
[3675.08 → 3678.72] you can get the rest of your business to have in your deployments.
[3679.04 → 3684.06] And that sort of leads to being able to keep iterating and deploying more frequently.
[3684.30 → 3685.88] And that's what we all want to do, right?
[3685.88 → 3689.74] We want to just keep making change and seeing positive effects in production.
[3689.74 → 3693.30] How do you replace fear with courage?
[3693.88 → 3694.92] How do you keep improving?
[3695.48 → 3696.66] Just keep failing.
[3697.00 → 3698.78] But like failing and learning from it.
[3698.86 → 3701.48] Like there's no real like secret formula.
[3701.80 → 3707.38] The first time you fail, as long as you can retrospect on that failure and take some key
[3707.38 → 3708.28] learnings away from it.
[3708.76 → 3710.76] I think the more you fail, the better.
[3710.76 → 3714.34] Because as long as you're not failing to the point where you're like taking production
[3714.34 → 3719.08] completely offline and costing your business like thousands of pounds and maybe like making
[3719.08 → 3723.38] all your customers lose confidence in your product, as long as you've risk assessed what
[3723.38 → 3728.90] you're deploying, and you have a blackout strategy, I think that's how you replace like fear of
[3728.90 → 3729.20] courage.
[3729.36 → 3732.16] Just knowing you've got that safety blanket of being able to eject.
[3732.74 → 3732.94] Yeah.
[3733.68 → 3740.04] Well, it's been a great pleasure, Alex, to watch you go from April when we first talked
[3740.04 → 3742.78] and we posted some diagrams to now December.
[3743.32 → 3747.02] You successfully sailed through Black Friday, Christmas as well.
[3747.20 → 3749.54] A lot of orders, physical orders have been shipped.
[3749.64 → 3751.44] A lot of socks by the sound of it.
[3751.78 → 3753.34] Everyone's getting socks for Christmas this year.
[3753.42 → 3753.84] Exactly.
[3753.98 → 3754.22] Yeah.
[3754.32 → 3754.80] Apparently.
[3755.90 → 3763.62] It's great to see from afar and, you know, for those brief moments from closer up to understand
[3763.62 → 3768.10] what you're doing, how you're doing it, how you're approaching problems that I think
[3768.10 → 3770.18] they're fairly universal, right?
[3770.32 → 3771.42] Taking production down.
[3771.66 → 3772.90] Everyone is afraid of that.
[3773.48 → 3777.22] Different stakes based on your company, but still, you know, taking production down is
[3777.22 → 3777.74] a big deal.
[3778.46 → 3780.58] Learning from when things fail.
[3781.08 → 3782.12] Trying new things out.
[3782.74 → 3786.18] It's okay if it's not going to work out, but at least you've tried, you've learned and
[3786.18 → 3787.14] you know, okay, it's not that.
[3787.36 → 3789.12] It's maybe something else, right?
[3789.14 → 3789.76] Most probably.
[3790.46 → 3792.68] And not accepting the status quo.
[3792.84 → 3793.88] Each of us have a legacy.
[3793.88 → 3797.92] Our best idea six months ago is today's legacy, right?
[3798.78 → 3800.10] And it is what it is.
[3800.20 → 3803.88] You know, it served its purpose, and now it's time for something new.
[3804.42 → 3804.94] Keep moving.
[3805.12 → 3805.74] Keep improving.
[3806.12 → 3809.50] There's always something more, something better that you can do.
[3809.84 → 3810.32] Completely agree.
[3810.46 → 3814.92] It's been great to come back on and look forward to sharing the automation piece sometime next
[3814.92 → 3815.14] year.
[3815.68 → 3815.98] Yeah.
[3816.18 → 3820.32] And I'm looking forward to adding some more diagrams in the show notes because I remember
[3820.32 → 3822.42] your 10-year roadmap.
[3822.98 → 3823.76] That was a great one.
[3823.82 → 3826.78] I'm wondering how that has changed, if at all.
[3827.22 → 3827.30] Yeah.
[3827.36 → 3831.94] And what is new in your current architecture compared to what we had?
[3832.24 → 3834.46] I think this is like the second wave of improvements.
[3835.24 → 3836.92] Six months ago, we had the first wave.
[3837.10 → 3839.68] We could see how well that worked in production.
[3840.32 → 3842.08] And now we have the second wave of improvements.
[3842.08 → 3842.98] So very exciting.
[3842.98 → 3843.40] Yeah.
[3843.52 → 3845.64] I'll send those over as of when I have them.
[3845.82 → 3846.52] Thank you, Alex.
[3846.72 → 3847.36] Thank you.
[3847.92 → 3849.66] That's a Merry Christmas present for sure.
[3849.66 → 3850.82] Merry Christmas, everyone.
[3851.20 → 3851.90] See you in the new year.
[3852.14 → 3852.84] Merry Christmas.
[3853.52 → 3853.74] Cheers.
[3857.10 → 3860.06] Thank you for tuning into another episode of Ship It.
[3860.32 → 3865.54] Check out our other podcasts for developers at changelog.com slash master.
[3865.88 → 3871.00] You can connect with like-minded developers via changelog.com slash community.
[3871.00 → 3875.66] Thank you, Vastly, for the worldwide, low-latency changelog.com.
[3876.06 → 3879.58] Our listeners love those blazing fast MP3s.
[3880.26 → 3884.52] Your Firecracker VMs and that WireGuard integration are really sweet.
[3885.04 → 3885.68] Flat.io.
[3885.98 → 3888.86] This was the last Ship It episode for 2022.
[3889.52 → 3892.28] I wish you all a great holiday season.
[3892.72 → 3893.56] Happy New Year.
[3893.92 → 3897.96] And I look forward to being back with you in January for more Ship It.
[3897.96 → 3898.96] Okay.
[3898.96 → 3908.72] Hey, man.
[3908.72 → 3938.70] Thank you.
