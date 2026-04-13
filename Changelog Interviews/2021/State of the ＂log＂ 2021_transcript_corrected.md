[0.00 → 20.98] Welcome, friends. You are listening to The Changelog, a podcast featuring the hackers,
[21.44 → 27.90] the leaders, and the innovators of the software world. This is our fourth annual year-end wrap-up
[27.90 → 33.08] episode. Adam and I don't like to navel-gaze too often around here, but when we do, we try to make
[33.08 → 39.28] sure you get your money's worth. Join us to reflect on the good, the bad, and the googly of what we're
[39.28 → 45.10] up to. We also run down the most popular episodes of the year, share our personal favourites, and hear
[45.10 → 50.30] from some loyal listeners as well. Special thanks to our partners for sticking by our side all year
[50.30 → 56.42] long. Thanks to Vastly for providing our bandwidth. Check them out at fastly.com. To Linde for their
[56.42 → 61.82] Kubernetes engine, we appreciate you. Learn more at linode.com slash changelog. And to launch
[61.82 → 67.18] Darkly, get your feature flags powered by Launch Darkly. Get a demo at launchdarkly.com.
[71.52 → 78.12] This episode is brought to you by Influx Data, the makers of InfluxDB, a time series platform for
[78.12 → 83.30] building and operating time series applications. And I'm here with Josh Vander from Network to Code.
[83.62 → 85.84] Josh, tell me about how you're using InfluxDB and Telegraph.
[85.84 → 91.12] Thanks, Adam. Network to Code helps enterprises bring DevOps ideas into network organizations. We love
[91.12 → 96.52] using open source tools like InfluxDB and Telegraph to help our clients collect, enrich, and analyze
[96.52 → 100.86] their data on their networks. Normally, we would have to build out this type of tooling, but InfluxDB
[100.86 → 105.86] and Telegraph meet all of our requirements. Plus, InfluxDB and Telegraph are open source, so we're able
[105.86 → 110.40] to contribute changes and use their SDKs to write custom plugins whenever we have specific needs.
[110.76 → 115.24] All right, learn more about the wide range of use cases of InfluxDB at influxdata.com
[115.24 → 119.68] slash changelog. Network monitoring, IoT monitoring, infrastructure and application monitoring.
[120.02 → 124.76] InfluxDB does it all. To get started, head to influxdata.com slash changelog. Again,
[124.76 → 127.04] influxdata.com slash changelog.
[127.04 → 148.90] State of the log 2021. Here we are.
[148.90 → 153.82] We're back. Yes. Gosh, it's been a year later, I guess. I guess, right?
[154.22 → 158.22] I think this is fourth annual State of the Log at this point. This is like a thing we do.
[158.68 → 165.06] This is a thing we do. It's something I actually really look forward to. It's a time of reflections.
[165.74 → 170.72] It's a time of thanks. It's a time of, and you know, I've probably said this a thousand times in
[170.72 → 174.08] the last four years. I'm a big fan of retrospectives.
[174.82 → 175.54] I do know that.
[175.90 → 182.62] You know, so I think it's really important to be aware of where you've been and just take stock in the ups and the downs.
[182.90 → 183.04] Yeah.
[183.20 → 187.94] You know, honestly, it can't just be the ups. It's got to be the downs too because you learn from your fails.
[188.18 → 191.16] Oh, we should edit our doc because they're mostly ups in here.
[191.24 → 191.60] Okay.
[191.84 → 192.72] You want to add some downs?
[192.72 → 193.40] You want to add some downs?
[194.02 → 197.00] Oh, man. What are some downs? What would be downs?
[197.60 → 198.64] Brain science hiatus.
[199.16 → 199.42] Yeah.
[199.96 → 200.22] Yeah.
[200.30 → 200.96] That's a downer.
[201.12 → 201.80] That is a downer.
[202.34 → 213.18] I would say the constant treadmill of creating content and the inconsistency consistency of inconsistency or however you play that out.
[213.28 → 213.60] Right.
[213.60 → 219.64] You know, like I just so much desire, you know, for this show to be perfectly on time every single week.
[219.64 → 224.56] But for some reason, it, you know, it's its certainly my bucket of things to do.
[224.96 → 226.12] It just never gets there.
[226.42 → 229.88] Somehow something happens to make it impossible.
[231.14 → 232.78] Operation operational groove.
[232.92 → 233.82] That was a thing this year.
[234.24 → 234.48] Yeah.
[235.08 → 235.72] Oh, oh, gee.
[236.24 → 236.74] Oh, gee.
[236.98 → 237.30] Dog.
[238.14 → 239.22] We love acronyms.
[239.60 → 240.14] We'll get there.
[240.24 → 240.74] We'll get there.
[240.78 → 241.50] Always a striving.
[241.68 → 242.22] We'll get there.
[242.76 → 243.64] I would say that's a down though.
[243.72 → 244.26] That's a down.
[244.38 → 244.92] That is a down.
[245.02 → 247.78] I want this show to be like, if it's going to be Friday, fine.
[247.90 → 249.12] If it's going to be Monday, fine.
[249.12 → 249.94] Pick a day.
[250.82 → 251.94] Ship it no matter what.
[253.60 → 257.58] Like if that thing hasn't shipped at the time it should have shipped.
[257.90 → 259.08] Like it's a fail.
[259.30 → 264.54] And I feel like we probably hit 10 weeks this year, if that many, on a Monday.
[265.42 → 268.72] Should we admit to the people that our goal is to ship the changelog on Mondays?
[268.84 → 269.56] Should we admit that?
[269.76 → 271.72] Or should we just keep that one to ourselves?
[271.80 → 273.82] Because I don't think we ever ship it on Mondays.
[273.90 → 276.52] I think, yeah, maybe half, maybe half a dozen or so.
[276.98 → 277.48] If that.
[277.48 → 278.98] Yeah, I'd say maybe 10 max.
[279.12 → 280.10] It's usually Friday.
[280.54 → 280.96] Mm-hmm.
[281.16 → 281.48] You know.
[281.72 → 283.52] And you know, it's because I wear a lot of hats.
[284.04 → 286.80] And hey, developers aren't supposed to ship things on Fridays, you know.
[286.94 → 288.84] So we're breaking that law too.
[289.10 → 289.34] Yeah.
[290.30 → 293.18] But even brain science, like that's been such a great show.
[293.40 → 295.66] I mean, let's share some details behind this.
[295.66 → 302.80] So we track our own stats thanks to our awesome partners, Vastly, and mugging of the logs essentially.
[303.30 → 306.72] And some wizardry to make it happen.
[307.36 → 313.34] And then Spotify is the biggest place that show got listened to in addition to, you know, our normal feed.
[313.46 → 316.66] So Shopify, I always mix the two up, Shopify and Spotify.
[316.88 → 317.60] That's really a shame.
[317.60 → 322.22] But on Spotify, they have their own tracking, their own stats.
[322.38 → 326.40] So they take our MP3, they put it in their own bucket, and they track it independently of us.
[326.64 → 328.04] They repost your files.
[328.64 → 328.78] Right.
[329.10 → 330.56] So does Google Podcasts.
[330.62 → 333.34] But who cares about Google Podcasts?
[333.58 → 334.70] No offence, Google.
[334.94 → 335.68] A lot of people do.
[336.54 → 337.44] I'm just kidding.
[337.66 → 338.68] For Practical AI at least.
[338.68 → 342.86] In terms of the pool of listens, Spotify is significant.
[343.12 → 347.68] Whereas Google Podcasts, although Practical AI is huge on Google Podcasts.
[347.70 → 348.08] That's true.
[348.56 → 350.38] And brain science is?
[350.66 → 351.44] Huge on Spotify.
[351.82 → 352.76] It's huge, yeah.
[352.94 → 360.24] So the most recent episode on the feed has been listened to more than 60,000 times.
[360.24 → 368.90] And like across the rest of the catalogue, it's like 20,000 plus, 30,000-ish when you add the two stats buckets together.
[369.00 → 369.30] Right.
[369.54 → 370.44] Ours and theirs.
[370.94 → 373.16] Now this is a phenomenon with podcasts.
[373.16 → 375.62] When you leave an episode in the feed and don't ship a new one.
[375.82 → 376.14] Right.
[376.30 → 377.72] That one gathers listens.
[378.56 → 381.64] The first episode always gathers listens, and the last one always does.
[381.64 → 387.22] That being said, it's growing like wildfire over there on Spotify without us doing anything.
[387.22 → 391.60] Yeah, and it's such a perplexing thing, honestly.
[392.44 → 398.48] And I look at that, so I agree 100% with the whole first episode, last episode, and the feed gets the most listens.
[398.68 → 401.44] But I look at that like missed opportunities.
[402.04 → 406.50] Like if that show was going still yet, like how many of those 60,000 people?
[407.24 → 412.78] Because like on Spotify, they're pretty, I would say it's probably in their best interest to be super accurate.
[413.04 → 413.36] Oh, yeah.
[413.36 → 417.60] Right, because they want you to know so you can grow there and to be aware.
[418.08 → 419.64] And so I look at that as like missed opportunity.
[420.46 → 420.48] But.
[421.14 → 425.92] So tell the people why it's on hiatus because, you know, missed opportunity.
[426.02 → 426.42] But why?
[426.86 → 427.34] Why is it?
[427.38 → 430.24] Because a lot of people have asked, why isn't Brain Science shipping new episodes?
[430.84 → 431.06] Yeah.
[431.22 → 432.98] And it's my favourite thing to do, honestly.
[433.04 → 435.08] And it's the hardest thing to do in life.
[435.62 → 436.82] And it's basically no.
[437.48 → 438.64] The response of no.
[439.36 → 439.76] Because.
[440.46 → 440.84] Focus.
[441.30 → 442.20] Right, focus.
[442.20 → 444.22] So you have to say no to focus.
[444.52 → 446.42] And a quick rewind on this.
[446.54 → 452.58] Like the reason I think we're sitting here is that I said no to even Founders Talk.
[452.74 → 453.00] Yeah.
[453.24 → 456.66] For several years to totally focus on this show.
[457.22 → 461.02] To totally focus on the relationship that we've been building over the years.
[461.02 → 465.30] And to turn this thing into a business and generate revenue to make it sustainable.
[465.30 → 468.48] And I think that that's why it's on hiatus.
[468.48 → 473.26] Because I was spending a lot of time, obviously, on Brain Science.
[473.58 → 478.96] And while there's been success with it, it wasn't in our main thing.
[479.16 → 482.68] So we have a saying called keep the main thing the main thing.
[482.68 → 487.50] And when you do that, I think in anything in life, you see the results you want to see.
[487.60 → 491.86] Because that's, you're optimizing, you're doing the work for what you're optimizing for.
[492.52 → 496.32] And I saw myself putting a lot of work out there into this show.
[496.40 → 497.84] But I kept getting pulled into it.
[497.88 → 498.66] I enjoyed doing it.
[498.70 → 499.46] And it's a great show.
[499.46 → 506.32] And not enough into, I kept like seeing myself being mediocre in other places.
[506.32 → 509.58] Not that I didn't show up and do my job and deliver.
[509.82 → 513.36] It just was, I was like mediocre in the results of like sales.
[513.46 → 516.42] And the results of like delivering this podcast and others.
[516.90 → 518.88] So I had to get that time back.
[518.88 → 523.20] So basically the reason why I was on hiatus is to give me my time back to focus.
[523.20 → 530.38] And I think to get us to a point where we can bring it back in a manner where it would be more sustainable.
[530.74 → 530.96] Yeah.
[531.26 → 533.14] Rather than being a burden.
[533.68 → 538.42] Despite it being an awesome show and Mariel being an awesome co-host and all the things.
[538.48 → 541.22] And plus she has some things in her life too, which made it easier to do that.
[541.68 → 542.96] And sometimes it's just the right timing.
[543.90 → 548.70] Seth Godwin's book, The Dip, will teach you when to quit essentially.
[548.90 → 550.20] Sometimes you got to quit.
[550.82 → 552.92] Sometimes you got to put things on the shelf for a bit and come back to it.
[552.92 → 555.00] And this is one of those things where you got to put it on the shelf and come back to it.
[555.66 → 559.80] So the upside of that focus is it allowed us to ship, ship it.
[561.08 → 562.56] Which has been a wild success.
[563.02 → 563.24] Yeah.
[563.96 → 567.38] A show that I love with a person that we both love, Gerhard Leon.
[568.38 → 572.28] And that's our, that's really the new thing for 2021 is shipped it.
[572.66 → 572.98] Yeah.
[573.32 → 577.24] And then operation, operational groove and a couple other things.
[577.28 → 582.74] We've been doing some more specials, trying to like to put a little bit more polish on certain things and always improving.
[582.92 → 586.98] Our workflow is always trying to improve our sound, our music.
[587.24 → 591.56] But ship it was the big thing that we added to our catalogue this year.
[591.72 → 592.00] Yeah.
[592.08 → 593.28] And we've done 33 episodes.
[593.52 → 596.08] So, I mean, that one's in a groove.
[596.96 → 601.42] It's gotten over 100,000 listens since I think May.
[601.64 → 603.10] When did we launch, ship it?
[603.18 → 603.36] May?
[603.90 → 604.22] May.
[604.42 → 604.82] End of May.
[605.30 → 605.50] Yeah.
[605.54 → 606.36] Over 100,000 listens.
[606.46 → 607.60] And that's just on our platform.
[607.70 → 610.36] So that excludes Spotify and Google.
[610.56 → 612.10] And it's doing well over there as well.
[612.18 → 614.70] I just didn't log in to check out how well.
[615.18 → 615.52] Mm-hmm.
[615.52 → 617.72] And the people are loving it.
[617.78 → 621.98] So that brings us to our first listener message.
[625.34 → 627.62] Hi, this is Brendan from Boston.
[627.94 → 632.46] My favourite thing about Changelog in 2021 was the new podcast, Ship It.
[632.96 → 636.84] I've been doing more cloud infrastructure work lately, and I learned a lot from the podcast.
[637.06 → 640.52] My favourite episode was episode 15 on Cross plane.
[640.52 → 645.26] I thought it was a very clear and articulate explanation of an interesting product.
[645.46 → 647.12] And I work primarily with Terraform.
[647.48 → 650.26] So the comparisons between Cross plane and Terraform are helpful.
[650.88 → 652.78] Thanks to Gerhard for hosting.
[653.02 → 654.16] Thanks to all the guests.
[654.50 → 656.08] And let's keep shipping it in 2022.
[659.74 → 664.72] Also in your feed, you'll see a, I think we're going to call it Merry Shipman.
[664.88 → 665.34] Is that right?
[665.48 → 666.10] Merry Shipman.
[666.34 → 666.54] Yeah.
[666.54 → 671.90] So you might see a Christmas gifts, in quotes, Christmas gifts episode in the feed.
[672.60 → 678.20] And yeah, I think Dan Magnum and Jerry Watts was awesome on that show.
[678.78 → 679.58] It was good.
[680.46 → 680.60] Yeah.
[680.68 → 682.14] Thank you, Brendan, for writing in.
[682.24 → 686.58] And here is a sample of his favourite episode about Cross plane.
[690.00 → 691.04] Why Cross plane?
[691.24 → 692.16] Why is it important?
[692.62 → 693.34] Why does it matter?
[694.12 → 694.40] Yeah.
[694.50 → 695.30] Great question.
[695.30 → 701.00] And, you know, I think there's kind of maybe two different branches of thought there to perhaps explore.
[701.54 → 707.20] So the first one is that some of us that created the Cross plane project, we also created the Rook project as well, too.
[707.62 → 710.48] And Rook is storage orchestration for Kubernetes.
[711.02 → 716.40] And so we found there that in the early days of persistent storage for Kubernetes, you know,
[716.40 → 725.16] the story needed to evolve a little bit there before people started to become more comfortable running storage or, you know, data persistence sort of things inside the cluster.
[725.16 → 732.22] So we found there that some of the work that the special interest group for storage and Kubernetes had done was really, really strong.
[732.30 → 734.64] Persistent volume claims, storage classes, things like that.
[734.64 → 748.22] And we found very early on that applying those same patterns for being able to dynamically provision storage would also work very well for other types of infrastructure platform resources, such as databases and buckets and even clusters themselves.
[748.22 → 753.66] And so that was the original why of Cross plane is, hey, we've done great things in Kubernetes for storage.
[753.92 → 762.32] Let's do more infrastructure resources inside of Kubernetes and bring them into being managed and provisioned and controlled by the control plane itself.
[762.32 → 772.32] And then beyond that, we found that there's a very strong story, too, for businesses that are starting to have their own shared services, infrastructure platform teams as well, too.
[772.32 → 780.52] They have a responsibility to provision infrastructure and, you know, get new services up and running for a whole set of application teams around them.
[780.52 → 800.02] And so being able to have some reproducibility, being able to enable self-service for the application teams is a really strong story to be able to make their jobs easier and for the application teams to be able to get to production faster and have, you know, reliable infrastructure and, you know, normalizing on a standard set of practices for the whole organization.
[800.02 → 805.70] It just makes the software delivery story that it has a huge dependency on infrastructure all the more strong.
[805.70 → 818.16] So Brandon knows this as a fan of Ship It and maybe you all know this, but if you don't, Adam and I also get to be on Ship It every 10th episode.
[819.50 → 822.10] So we have this Kaiden idea.
[822.18 → 824.62] This is all Gerhard's grand plan.
[824.62 → 832.46] He brings us on to work on continuously improving our platform, our workflows, our podcasts.
[832.46 → 841.34] And we do it in the open, and we discuss it quite openly, even to my shame sometimes as we discuss my bugs and whatnot.
[842.22 → 850.84] And I believe Cross plane is very much in Gerhard's plans for integration into what the future of the Changelog platform looks like.
[850.92 → 853.82] He's always Wizening our platform.
[854.84 → 859.24] And Cross plane, I believe, is at least in the running to be part of that platform.
[860.10 → 860.76] So cool stuff.
[860.76 → 874.84] If this is the first time you're hearing about Ship It or maybe just a second or third, potentially, if you haven't listened yet, and you want to get deeper into it, I would suggest, honestly, episode number one, because you'll get to hear where we began.
[875.56 → 878.58] And obviously the ones Gerhard's mentioning is every 10 episodes.
[878.58 → 885.80] So episode 10, episode 20, episode 30, you'll get a behind the scenes look at what we're doing on Ship It.
[885.80 → 887.94] So those would be good places to start.
[888.06 → 891.34] And we often point out to other episodes on those shows.
[891.44 → 894.32] So it's probably a good guide to Ship It.
[895.04 → 895.88] Yes, yes.
[896.28 → 898.76] But this show is about the Changelog.
[898.84 → 899.78] It's not about Ship It.
[899.96 → 902.00] It's becoming less about the Changelog, honestly.
[902.28 → 907.66] As we grow and explore and succeed and fail, we tend to point elsewhere.
[907.76 → 908.66] It's becoming the hub.
[909.00 → 909.26] Yeah.
[909.26 → 910.72] And not only just the spoke.
[911.16 → 912.44] Well, this was very intentional by us.
[912.50 → 914.76] So for many years, we have a lot of episode requests.
[914.88 → 916.70] We still get lots of episode requests.
[917.22 → 917.92] And we love those.
[918.00 → 920.70] And we do a lot of episodes, honestly, just because somebody asked us to.
[920.80 → 921.72] We love to do that.
[922.14 → 931.66] That being said, for a long time, people would ask us to do specific shows and hear more about their favourite thing or their niche inside of software.
[931.66 → 936.22] And, you know, we only get to shoot one shot once a week for the Changelog, right?
[936.24 → 938.72] We got 50 episodes a year.
[939.32 → 945.44] And we just didn't feel like we should put a bunch of episodes about Go in the Changelog feed.
[945.52 → 947.48] It wouldn't be serving our listeners.
[947.70 → 949.36] It'd be serving some of them, but not all.
[950.38 → 959.62] And so that was why the strategy was to strategically add new shows that can go super deep on these subgenres inside of software.
[959.62 → 969.82] And I'm really happy that we finally have an operation, infrastructure, DevOps, shipping it, podcast.
[970.20 → 978.98] We can have those conversations each and every week without feeling like we're having to avoid other potential awesome conversations on the Changelog.
[979.40 → 981.36] I think, too, also to add more voices.
[981.86 → 987.86] You know, while I really do enjoy your voice, Jared, and I really do enjoy your company,
[987.86 → 994.92] and sharing, you know, in the successes and the fails with you, I think it's also more fun to incorporate others.
[995.00 → 1001.06] And I think having worked with Gerhard for many years, you know, we – it just made sense.
[1001.20 → 1005.66] Because we were doing that, I guess, a small snippet of where that show came from.
[1005.80 → 1008.50] We had done this for years, once a year.
[1008.64 → 1009.42] Once a year, yeah.
[1009.42 → 1009.46] Yeah.
[1010.08 → 1015.28] And so it was just natural to grow by one more voice and one more people.
[1015.42 → 1019.18] And as we have said before, we came for the tech, but we stayed for the humans.
[1019.22 → 1024.50] And I think for us, this isn't just simply about the progress and innovation of software.
[1025.00 → 1026.26] Of course, that is it.
[1026.30 → 1028.70] It's the linchpin of the reason we're here.
[1028.70 → 1030.46] But it's really about the people.
[1030.58 → 1035.12] And I think we – and maybe we'll mention this when Laura – when we mention Laura's show, Laura Hogan,
[1035.84 → 1042.36] we get a chance to sponsor some people, you know, to give Gerhard the platform of Ship It.
[1042.46 → 1047.72] He's doing all the work, but, you know, if we hadn't put the work in to build changel.com,
[1047.98 → 1050.74] the open source that's behind it, all the podcasts involved in it,
[1050.78 → 1053.54] then that show wouldn't have a home here necessarily.
[1053.92 → 1054.70] So it's –
[1054.70 → 1054.76] Right.
[1055.02 → 1058.50] It's a lot of – it's a multilayered onion, basically.
[1059.26 → 1059.96] It's a multilayer.
[1060.06 → 1060.92] It's like a tour network.
[1061.58 → 1063.18] So I couldn't agree more.
[1063.38 → 1070.20] I love the diversity of voices and our opportunity to give people a voice on our different shows.
[1070.52 → 1074.46] I think that not only is it the spice of life to have variety,
[1074.86 → 1078.62] but there's also just like we couldn't do that show as well as he can.
[1079.10 → 1080.60] You know, I've heard him ask questions.
[1080.70 → 1083.70] I'm like I never would have been able to – you just can't know it all.
[1083.70 → 1084.74] We couldn't do a Go show.
[1084.84 → 1085.98] You and I couldn't do a show about Go.
[1086.16 → 1088.68] We couldn't do – I can barely do a show.
[1088.70 → 1090.46] I don't know about JavaScript on JS Party.
[1090.60 → 1092.60] I'm just one of ten on that show.
[1092.72 → 1093.58] That makes it awesome.
[1093.72 → 1094.56] Just one of ten.
[1094.82 → 1095.14] Yes.
[1095.34 → 1095.70] Yes.
[1096.08 → 1096.48] Precisely.
[1096.74 → 1096.94] Yeah.
[1097.06 → 1103.14] So the expertise spread around as well because there's just so many facets to this industry
[1103.14 → 1106.54] and you can dive so deep into these little camps.
[1106.54 → 1110.28] And I know there are other areas of the software world that we are not providing for.
[1111.06 → 1113.72] Some of them are well served by other podcasters for sure.
[1114.64 → 1115.70] Others, not so much.
[1115.80 → 1122.02] So I think we have some other places we can go, but I'm happy that we have more than just the changelog now.
[1122.02 → 1122.14] Yeah.
[1122.46 → 1122.72] Yeah.
[1122.94 → 1123.70] I agree with that.
[1124.32 → 1124.44] Yeah.
[1124.52 → 1124.84] Ship it.
[1125.08 → 1131.24] Well, we'll receive this year 33 episodes, three Kaiden episodes, lots of listens as Jared had mentioned,
[1131.34 → 1134.82] and obviously a blossoming relationship even deeper with Gerhard.
[1135.20 → 1136.88] Our infrastructure has improved.
[1137.02 → 1138.32] Our partnerships have improved.
[1138.74 → 1138.98] Yes.
[1138.98 → 1140.58] You know, we've gained new partners.
[1141.00 → 1150.36] I think in the most recent episode of Kaiden on Ship It, we thanked some particular partners over this past year for doing that with us.
[1150.56 → 1152.40] So I encourage you to listen to episode 30.
[1152.48 → 1154.04] That's where that's mentioned right at the very end.
[1154.44 → 1156.62] So if you want to know more about that, listen to that.
[1157.04 → 1161.68] And if you listen to the very, very, very end of that episode, we basically just laugh for three straight minutes.
[1161.68 → 1172.94] So I try to ring lead back into normality and I failed because Gerhard just was laughing so hard and you were laughing so hard right along with him.
[1173.00 → 1174.22] I think even crying.
[1174.42 → 1175.46] He was just making me laugh.
[1175.62 → 1177.72] Like cry laughing because it was just so much laughing.
[1177.94 → 1178.22] Yes.
[1178.56 → 1179.22] Tears in the eyes.
[1179.46 → 1179.94] That's fun.
[1180.52 → 1184.08] Not every day you get to cry podcasting, but that was that day.
[1184.36 → 1184.56] Yeah.
[1184.70 → 1185.36] Good moments.
[1185.44 → 1186.42] You need a good belly laugh.
[1186.78 → 1187.46] I encourage a good.
[1187.48 → 1187.88] Sometimes.
[1188.16 → 1190.78] A good belly laugh every once in a while is a good thing.
[1190.78 → 1191.14] Sure.
[1191.68 → 1208.26] More and more startups are using retool to focus their time on their core product.
[1208.26 → 1210.88] And that's exactly why they launched retool for startups.
[1211.12 → 1217.02] This is a program that gives early stage founders free access to a lot of the software needed for great internal tooling.
[1217.42 → 1219.00] And retools work with thousands of startups.
[1219.00 → 1224.20] And the trend line they noticed was technical founders spending tons of time building internal tools.
[1224.74 → 1229.12] That means at this critical stage, these founders were distracted from their core product.
[1229.48 → 1230.34] The goal is simple.
[1230.60 → 1236.50] Make it 10 times faster to build the admin panels, CRUD apps, and the dashboards most early stage teams need.
[1236.90 → 1246.90] And retool has bundled together a year of free access to retool with over $160,000 in partner discounts to save you money while building retool apps with common integrations like AWS,
[1246.90 → 1249.72] MongoDB, MongoDB, Bred, and Segment.
[1250.10 → 1251.60] There is so much you can do with retool.
[1251.88 → 1256.20] You can use these free credits to build tools that join product and building data into a single customer view.
[1256.58 → 1260.46] Tools that convert manual workflows into fully featured apps for your team.
[1260.68 → 1266.36] Or tools that help non-technical teammates get access to your database to read and write data, analyze, and query.
[1266.66 → 1268.00] These are just a few examples.
[1268.54 → 1272.78] Learn more, apply, and join lightning demos at retool.com slash startups.
[1272.78 → 1275.14] Again, retool.com slash startups.
[1275.14 → 1305.12] So as we dive into now focusing in on the changelog, we have for this show, every year we do the most popular episode.
[1305.12 → 1306.54] We talked through a few of those.
[1306.90 → 1313.36] Our favourite episodes this year, we've also asked listeners to basically leave us voice messages.
[1313.80 → 1315.60] We appreciate each one that did.
[1316.26 → 1321.32] So we will play those and, of course, clips from episodes that they appreciated.
[1322.06 → 1323.50] We do have a list of reflections.
[1324.40 → 1324.48] Yeah.
[1324.96 → 1325.94] Do you want to hop into popular?
[1326.06 → 1327.38] Should we hop into some reflections first?
[1327.46 → 1328.60] We kind of reflected a little bit.
[1328.96 → 1329.60] A little bit, yeah.
[1330.14 → 1331.40] Well, there are a couple of things I want to point out.
[1331.40 → 1334.70] So I think this will dovetail into some of the ones I'll mention later on.
[1334.84 → 1338.94] But this year we got to get our merch store out there more often.
[1340.24 → 1345.06] We have a fulfillment centre in Orlando, Florida now.
[1345.06 → 1349.32] Our store is obviously a Shopify store.
[1349.76 → 1353.86] We're using Theme Kit to deliver that theme easily to Shopify.
[1354.06 → 1364.34] Maybe in the future we'll do something that we talked about in the Ilya show when we talked about all the cool things they're doing around React and React server components and all those fun things.
[1364.34 → 1369.14] But the merch store is in place, and we've shipped more tees this year than any other year.
[1369.46 → 1373.64] And a large majority of those t-shirts are free to guests.
[1374.06 → 1380.04] So if you're listening to this, if you're ever a guest on the show, when your show goes live, we email you immediately.
[1380.28 → 1382.50] Our robot called Law bot emails you.
[1383.50 → 1387.80] And along with that, Jared, you can mention some of the code you wrote for this if you'd like to.
[1387.80 → 1395.12] But we generate a coupon code based on your name and some other fun stuff, and it gives you a free t-shirt, literally free, shipping and all.
[1395.74 → 1398.94] All you got to do is go to our Shopify store, plug in the coupon code.
[1399.14 → 1400.98] I guess you just click the link, right?
[1401.04 → 1403.02] And it's free just in your checkout process.
[1403.22 → 1405.58] Yeah, the link will actually auto-apply the discount.
[1405.98 → 1406.20] Yeah.
[1406.70 → 1409.46] But if it doesn't work, you can type in the code.
[1409.52 → 1412.58] But I think it pretty much always does because Shopify knows what they're doing.
[1413.16 → 1414.38] And that's yours in the making, right?
[1414.46 → 1415.74] Like you've wanted that.
[1415.74 → 1420.60] I wanted that feature for so many years because our shipping process was so manual.
[1420.72 → 1425.24] And we've given away free t-shirts to all of our guests since I can't remember when we didn't do that.
[1425.46 → 1428.26] But I can remember when we had a giant spreadsheet with a backlog.
[1428.82 → 1428.98] Yes.
[1429.12 → 1436.74] And it was just such a manual process, and it relied upon us or replied upon Adam and his wife Heather to get that stuff done.
[1437.78 → 1440.40] And we weren't in that operational groove.
[1440.66 → 1445.28] And I always just wanted to just like, can we just auto-generate a coupon code?
[1445.28 → 1446.30] How cool would that be?
[1447.32 → 1448.18] And just like.
[1448.86 → 1450.12] And somebody else does all the work.
[1450.22 → 1450.52] Yes.
[1450.90 → 1452.60] That's what fulfillment's for, man.
[1452.68 → 1453.24] I think, you know.
[1453.28 → 1453.92] And it's so cool.
[1454.16 → 1456.22] The hard part of that is finding the right partners.
[1456.22 → 1466.68] And I think another part of that is wanting so badly to own the process of something like that because you care deeply about the people you're sending them to.
[1467.34 → 1469.92] And then, you know, but then you have so many things to do.
[1469.98 → 1473.24] And it's like it eventually falls by the wayside somehow, some way.
[1473.68 → 1474.92] And trying to keep up with everything.
[1475.12 → 1477.70] And so I'm so thankful for our fulfillment team doing that stuff.
[1477.78 → 1478.80] Like it's all warehouse.
[1479.00 → 1479.88] We don't have to touch a thing.
[1480.04 → 1482.96] You know, we just have to do the fun stuff now, which is super cool.
[1482.96 → 1484.66] But yeah, come on our show.
[1484.82 → 1485.86] And I did get to code it up.
[1485.96 → 1491.90] I got to, you know, plug into the Shopify API and auto-generate coupon codes.
[1492.06 → 1503.42] We had to figure out a way of making the discount 100% off because the discounts themselves inside of Shopify do not apply to shipping.
[1503.42 → 1510.64] And especially in today's society, shipping is expensive and slow around globally, especially.
[1511.54 → 1515.68] And there's no way of you don't want to give somebody a free T-shirt, but then require them to pay shipping.
[1516.18 → 1517.02] Yeah, it's like the worst.
[1517.22 → 1519.78] And so it actually took somebody gave me advice.
[1519.88 → 1520.86] I can't remember who it was.
[1521.68 → 1524.58] I had tried to figure this out for a long time.
[1524.64 → 1526.16] And there's a lot of people that struggle with this with Shopify.
[1526.34 → 1527.52] It's like a feature everybody wants.
[1527.58 → 1530.62] It's like, give me a coupon code that just adds free shipping to it.
[1530.62 → 1534.80] And finally, somebody, I think it might have been the Nginx folks.
[1535.48 → 1539.20] Somebody had sent me a free T-shirt via Shopify, and they got it done.
[1539.42 → 1540.60] And I wrote to them immediately.
[1540.72 → 1541.82] I'm like, how the heck did you do this?
[1541.84 → 1544.08] Because I didn't have to pay shipping, but we can't figure it out.
[1544.48 → 1553.76] And there's basically a particular setting inside your store where as long as the cart total is $0, it'll apply free shipping.
[1553.88 → 1555.00] But if it's not, it won't.
[1555.30 → 1558.84] So if our coupon code brings you to zero, which it does, then you get free shipping.
[1558.84 → 1561.08] But if you add another shirt, like you're like, oh, I'll get two.
[1561.18 → 1562.00] Now you got to pay shipping.
[1562.32 → 1564.60] So it's kind of lame in that way, but it's better than it was before.
[1564.70 → 1568.16] So lots of like little intricacies in getting this done.
[1568.56 → 1569.88] Just so happy to have it done.
[1570.22 → 1577.76] And yeah, you can also just buy a shirt, merch.changewall.com if you want a sweet T-shirt or come on a show.
[1578.22 → 1579.16] That's the easy button.
[1579.38 → 1581.80] Maybe a little bit harder because you have to like talk and stuff, but.
[1581.96 → 1582.82] It's the easy hard button.
[1583.54 → 1584.58] It's the easy hard button.
[1584.98 → 1585.82] It's the cheaper button.
[1585.82 → 1593.94] And on that note, so we'll mention maintainer week and every commit is a gift later on as we get to our shows.
[1594.08 → 1601.26] But as a predecessor to that, we had the maintainer, maintainer, maintainer T-shirt come out as part of that, which was.
[1601.48 → 1602.06] Yeah, that was fun.
[1602.54 → 1609.18] Worn by Daniel Steinberg and the one of the core members behind Pinhole on Twitter.
[1609.18 → 1611.04] And I'm sure several others.
[1611.16 → 1613.90] Those are the two I remember most recently.
[1614.08 → 1621.36] But I was just so stoked to see that because like even outside the whole maintainer week stuff, Daniel was sharing like an update about curl recently.
[1621.36 → 1631.26] And for those who may be catching up, Daniel Steinberg is the maintainer of curl, and he's been doing so for 23 years as of the most recent recording.
[1631.26 → 1641.72] And this is probably, you know, I think he said like 10 billion uses or installations even on Mars of the most recent.
[1642.20 → 1653.54] And so he's wearing our maintainer, maintainer, maintainer shirt, which is a play on, you know, Beetlejuice and also Stephen, Steve Ballmer.
[1653.70 → 1653.94] Is that right?
[1654.20 → 1654.76] Steve Ballmer.
[1655.14 → 1655.84] Steve Ballmer.
[1656.10 → 1656.60] Steve Ballmer.
[1656.74 → 1658.38] Developer, developer, developer, developer.
[1658.38 → 1659.86] Yeah, we were trying to.
[1660.02 → 1662.54] So behind the scenes, we were trying to get Nat Friedman.
[1662.66 → 1667.58] So Nat, if you're listening to this or somebody's listening to this, you know, you know, Nat, Nat, you missed out, man.
[1667.66 → 1671.70] We were going to do a show called Maintainers, Maintainers, Maintainers with you.
[1671.76 → 1679.26] And it would have been a nice dovetail to the future of software and GitHub and the Microsoft roots and all the fun stuff.
[1679.26 → 1688.58] But anyway, we want to do a show titled Maintainer, Maintainer, Maintainer in light of Steve Ballmer's developers, developers, developers.
[1688.78 → 1691.78] And if you want to play a clip of that, Jared, I don't know if you want to have a clip of that pulled up.
[1691.82 → 1692.24] Probably not.
[1692.76 → 1694.20] But you get it.
[1694.36 → 1695.14] You heard the chant.
[1695.56 → 1697.56] So that shirt is super cool.
[1697.74 → 1698.72] And it's warm.
[1698.78 → 1700.08] We got some stickers out there.
[1700.08 → 1703.52] And all that was done by our fulfillment team.
[1703.82 → 1705.90] And we didn't have to ship any that late.
[1706.50 → 1710.14] You know, the only hard part really was getting the shirts printed on time.
[1710.22 → 1711.96] It took like a month and a half to get the shirts printed.
[1712.46 → 1714.78] We want to do one large batch and send them all at once.
[1714.92 → 1717.28] And yeah, so that's a lot of fun.
[1718.56 → 1721.20] So look out for this coming June.
[1721.20 → 1723.14] I believe we will have Maintainer week again.
[1723.52 → 1726.60] And we will definitely try to put out another limited run.
[1726.86 → 1727.68] Different, I hope.
[1727.68 → 1730.42] T-shirt specifically for Maintainers.
[1730.78 → 1732.90] I heard it might be Maintainer month.
[1733.04 → 1733.38] Oh.
[1733.62 → 1733.88] Potentially.
[1734.66 → 1740.02] We're not sure if the timelines are overlapping enough to make it, to force it to be Maintainer month.
[1740.20 → 1741.58] Typical feature bloat, you know.
[1741.80 → 1742.16] Mm-hmm.
[1742.30 → 1745.62] Goes well, and we're like, well, can we just squeeze in a few more weeks into that month?
[1745.98 → 1746.28] Yeah.
[1747.02 → 1751.32] Lastly on Reflections, you want to mention Changelog++ because we've been doing that for a little while now.
[1751.82 → 1752.20] Yeah.
[1752.20 → 1755.42] We did an episode on this, and I'll do a micro version of this.
[1755.42 → 1761.94] So we have a membership called Changelog++ because, you know, why not increment things and make it better?
[1762.72 → 1767.76] As we say at the end of some shows, Changelog++ is better.
[1768.16 → 1768.96] Changelog++.
[1769.50 → 1770.24] It's better.
[1770.24 → 1775.02] Now, if you've heard that clip, it doesn't sound like me, but that is me.
[1775.28 → 1775.76] Yes, it is.
[1776.10 → 1777.98] So I did that in a funny voice.
[1778.30 → 1781.34] I think a Finnish voice and then did some tweaking to it.
[1781.48 → 1781.88] Auto-tune.
[1782.04 → 1782.68] You auto-tuned it.
[1782.76 → 1783.84] Yeah, I auto-tuned myself.
[1784.46 → 1788.06] And so Changelog++ is better because it's fun to say, like, it's better.
[1788.44 → 1789.56] It's better.
[1790.00 → 1792.16] But that's been in place for a little more than a year now.
[1792.16 → 1795.82] We've got – it's not a blow-up success, and it's not meant to be.
[1795.90 → 1803.64] It's just meant to be an avenue for mainly people who want to support us and maybe don't want the ad versions of our show.
[1803.74 → 1806.34] And in many cases do want the ad version.
[1806.44 → 1811.80] They're upset because they want to buy++ and also still get ads too, which is basically impossible at this point.
[1812.98 → 1814.30] But it's been there for a year.
[1814.30 → 1821.20] Justin Dorfman has been a long-time friend, and he sent us a clip where he gave us a little bit of praise.
[1824.92 → 1827.86] Adam, Jared, it's Justin Dorfman.
[1828.12 → 1829.42] Happy holidays, my friends.
[1829.86 → 1833.22] Just want to say how much I love you guys and the media you produce.
[1833.84 → 1842.24] I'm looking forward to what Changelog has in store for 2022 as well as renewing my Changelog++ membership.
[1842.84 → 1843.48] See you next year.
[1844.30 → 1848.04] We love you too, Justin.
[1848.10 → 1850.42] And we will see you next year because we're not going anywhere.
[1850.68 → 1855.00] I think the fun part about this is like this is 12-ish years.
[1855.18 → 1857.12] This next year will be 13 years of doing this.
[1858.06 → 1862.40] And I feel like we've just begun in a lot of ways.
[1862.40 → 1864.98] I feel like we've hit the dog, Jared.
[1865.70 → 1866.22] You know what I mean?
[1866.32 → 1867.80] Like I feel like –
[1867.80 → 1868.56] We're getting there, yeah.
[1868.80 → 1871.32] I'm not even – I mean there are days that I'm definitely winded.
[1871.54 → 1873.66] I mean there's definitely days when I'm like, oh my gosh.
[1874.30 → 1876.00] Please go back to bed instead, you know?
[1876.68 → 1878.40] And it's not because it's not for the love.
[1878.48 → 1882.48] It's because like it is a lot of work running your own thing and showing up every day.
[1882.54 → 1883.24] It does take a lot of work.
[1883.32 → 1884.66] But yeah, we're not going anywhere.
[1885.40 → 1888.90] And I do really feel like we've just begun, and we have so much more to do.
[1888.90 → 1892.54] So – and I'm thankful for Plus and all the members who support that.
[1893.20 → 1898.22] But if you don't care for our ads, then $10 a month, $100 a year.
[1898.84 → 1899.34] There you go.
[1899.34 → 1899.70] Yeah.
[1899.90 → 1902.18] ChangeLog.com slash Plus if you want to check it out.
[1902.96 → 1904.76] It is easy to get winded, but I will just say this.
[1904.88 → 1906.52] I don't think I've told you this yet, Adam.
[1906.58 → 1908.96] But just the other day, I was putting together –
[1908.96 → 1912.48] I'm putting together a special episode of Go Time called The Funny Bits.
[1912.56 → 1913.30] That's the working title.
[1913.38 → 1914.58] I'm not sure what it's going to be exactly.
[1915.00 → 1915.66] But it's coming.
[1915.92 → 1919.72] It'll drop into your feed soon for Changelog Plus subscribers
[1919.72 → 1921.32] as well as Master Feed subscribers.
[1921.48 → 1924.16] Or if you are a Go Time listener, there as well.
[1924.92 → 1927.16] And it's just like all the funny parts from the last year, basically.
[1927.68 → 1929.24] People being silly on Go Time.
[1930.10 → 1934.04] And there's a really great clip between Matt Refer and Johnny Portico
[1934.04 → 1938.42] where Matt is just messing with him and saying things like,
[1938.46 → 1939.84] I'll do anything you tell me to do, Johnny.
[1939.92 → 1940.64] He's just being weird.
[1941.42 → 1944.56] It reminded me of Brian Adams or Brian Adams.
[1944.64 → 1945.68] And I always get the two confused.
[1945.68 → 1948.96] I think it's Brian Adams, Everything I Do, I Do It For You,
[1949.52 → 1952.76] off of the Robin Hood, Prince of Thieves soundtrack.
[1952.76 → 1956.10] And so I thought, well, what's the appropriate thing to do here?
[1956.18 → 1958.74] Well, I have to splice their voices into this song
[1958.74 → 1960.70] in order just to spice it up a notch.
[1961.20 → 1964.52] Yeah, I'd die for you.
[1965.40 → 1966.38] I would die for you, Johnny.
[1967.82 → 1969.06] You know it's true.
[1969.48 → 1971.26] I will release anything you tell me to.
[1971.52 → 1973.16] Everything I do.
[1973.16 → 1979.08] So I'm sitting there putting together this montage of Matt Refer
[1979.08 → 1983.38] professing these feelings for Johnny Portico
[1983.38 → 1986.38] over this sounded of Brian Adams singing
[1986.38 → 1988.54] that he would die for you.
[1989.12 → 1992.18] And I just thought, I love this job.
[1992.38 → 1994.26] This is like the most amazing thing ever.
[1994.90 → 1995.02] Yeah.
[1995.48 → 1997.80] In fact, that's exactly what I would have been doing
[1997.80 → 1999.20] if I just had a free day.
[1999.20 → 2001.36] I probably would have been taking some music
[2001.36 → 2004.02] and making some silly thing to make people laugh
[2004.02 → 2005.04] and have a good time.
[2005.22 → 2008.38] So we don't take it for granted how amazing it is
[2008.38 → 2009.88] that we aren't going anywhere
[2009.88 → 2012.12] and that we get to make podcasts for you all
[2012.12 → 2014.50] and that we get to have these conversations
[2014.50 → 2017.24] and have fun and learn and grow.
[2017.90 → 2018.52] It's amazing.
[2019.60 → 2020.38] Yeah, I concur.
[2020.86 → 2022.86] Definitely surreal.
[2022.86 → 2025.86] I mean, I didn't begin my career in software thinking
[2025.86 → 2028.46] I'll one day be a full-time podcaster
[2028.46 → 2030.34] running a podcast network
[2030.34 → 2031.98] with a bunch of awesome people
[2031.98 → 2033.78] and enjoying it every single day.
[2034.14 → 2036.26] Not just the people that are involved in the shows,
[2036.34 → 2037.38] but the people who come on the shows
[2037.38 → 2038.82] and the people who support the shows
[2038.82 → 2040.26] as partners and sponsors.
[2040.56 → 2043.52] Like, it's pretty profound
[2043.52 → 2046.74] and would have never necessarily guessed it.
[2046.86 → 2048.18] My whole life I spent thinking,
[2048.64 → 2050.36] like I had other friends who had radio voices
[2050.36 → 2053.58] and I never thought I had a voice for radio by any means.
[2054.76 → 2055.46] Clearly I do.
[2055.68 → 2056.56] I didn't think I did.
[2056.68 → 2057.62] I always hated my voice
[2057.62 → 2059.22] like most people do until they hear it enough.
[2059.28 → 2061.86] I guess it just eventually you love it at some point.
[2063.52 → 2066.14] But yeah, man, like I'm so thankful to get to do this.
[2066.22 → 2068.60] And the reason why, just a pause a moment,
[2068.68 → 2069.94] because I want to do this early in the show,
[2070.02 → 2073.24] but it just didn't come out quite as part of our flow.
[2073.32 → 2074.92] But I'm just so thankful for our listeners.
[2074.92 → 2077.70] Like if you listen to this show right now,
[2077.70 → 2080.66] we're not sharing your attention with us
[2080.66 → 2082.12] and sharing your time with us.
[2082.48 → 2084.36] This would just be an MP3 on the internet,
[2084.48 → 2085.72] not getting listened to.
[2085.92 → 2088.74] So we appreciate you sharing your time with us
[2088.74 → 2090.26] and listening to our shows.
[2090.82 → 2092.82] And I would say even more importantly,
[2093.18 → 2094.98] sharing this episode or others
[2094.98 → 2097.22] that you really enjoy with your friends.
[2097.42 → 2099.14] Word of mouth is one of the best ways
[2099.14 → 2100.20] to help us grow our shows.
[2100.78 → 2102.48] We would love you to be a Plus member,
[2102.48 → 2103.66] but not because we want your money,
[2103.84 → 2107.10] just because it gets you deeper into the community.
[2107.86 → 2109.84] But really, honestly, skip the money.
[2110.10 → 2111.86] Just share our stuff with your friends
[2111.86 → 2113.12] that you really care about.
[2113.68 → 2115.46] And that is enough for us.
[2115.52 → 2117.06] But just showing up to do this every single day,
[2117.12 → 2119.30] it's such a profound blessing.
[2119.42 → 2120.14] Would have never guessed it.
[2121.04 → 2121.40] Absolutely.
[2121.74 → 2126.64] So let's hop in to our most popular episodes of 2021.
[2127.16 → 2128.24] Finally, some shows.
[2129.04 → 2131.18] The pre-roll of all this is getting deeper, you know,
[2131.18 → 2133.16] all the reflections and all the new stuff.
[2133.34 → 2135.18] This episode is getting longer and longer.
[2135.18 → 2136.72] It is.
[2137.22 → 2139.26] Well, then we'll just edit ourselves way down.
[2140.08 → 2140.68] Probably not.
[2140.76 → 2141.50] It's just going to be long.
[2141.96 → 2142.46] That's okay.
[2143.26 → 2144.12] Most popular.
[2144.24 → 2147.50] Well, let's start off with another listener clip here
[2147.50 → 2149.24] because we have a good one
[2149.24 → 2151.76] who loves not just a specific episode,
[2151.98 → 2153.98] but a specific part of all of our episodes.
[2154.22 → 2157.44] This is Aaron Shitake calling in.
[2157.44 → 2162.20] Hey, change loggers.
[2162.40 → 2164.52] Thanks for all the awesome content over the year.
[2165.16 → 2167.06] I've really enjoyed a lot of different episodes,
[2167.54 → 2169.28] but to be honest,
[2169.42 → 2171.28] one of my favourite parts of every episode
[2171.28 → 2173.52] is the amazing beats that you've gotten,
[2173.76 → 2176.32] the intros and outros and the ads.
[2176.56 → 2178.98] So huge shout out to Break master Cylinder
[2178.98 → 2181.54] for creating all these awesome songs.
[2181.76 → 2183.20] My favourite is Solfeggio,
[2183.62 → 2186.18] which used to be the changelog end credits.
[2186.18 → 2187.24] I've downloaded that
[2187.24 → 2188.58] and I listen to it all the time now.
[2189.36 → 2189.60] Cheers.
[2193.82 → 2194.80] Cheers to you, Aaron.
[2195.06 → 2197.26] Thank you for leaving us that message.
[2197.86 → 2198.08] Yeah.
[2199.16 → 2199.60] Break master.
[2199.90 → 2200.94] Gosh, Break master Cylinder.
[2201.10 → 2201.94] So, I mean, obviously,
[2202.72 → 2203.70] we just need some listeners
[2203.70 → 2206.14] and Aaron, you called in, of course,
[2206.20 → 2207.22] and we thank you for that.
[2207.68 → 2209.44] But like, I could not,
[2210.04 → 2211.26] I couldn't imagine
[2211.26 → 2212.88] what we do
[2212.88 → 2214.86] without Break master Cylinder beats.
[2214.86 → 2217.74] Like, Break master is just such a staple
[2217.74 → 2219.24] for our stuff.
[2219.96 → 2221.24] More auto-tuned Adam tracks?
[2221.64 → 2222.20] Yeah, potentially.
[2222.36 → 2223.00] I mean, yeah, I mean,
[2223.04 → 2225.34] we're just terrible attempts at music, essentially.
[2226.26 → 2229.00] But like, I love Break master's beats.
[2229.34 → 2230.40] They work with us closely.
[2231.20 → 2233.20] As a plus to being a Plus member
[2233.20 → 2234.48] or a community member,
[2234.52 → 2235.24] which is totally free,
[2236.08 → 2237.04] you could be in Slack
[2237.04 → 2238.56] and Break master is in Slack.
[2238.70 → 2239.42] Now, I don't know
[2239.42 → 2241.32] if they'll talk to you.
[2241.32 → 2242.52] I'm sure they would via DM,
[2242.66 → 2244.14] but like, they hang out in Maine
[2244.14 → 2245.82] and some other channels
[2245.82 → 2246.48] and stuff like that.
[2246.58 → 2248.64] But like, Break master's in our Slack
[2248.64 → 2249.76] and hangs out with us.
[2249.90 → 2252.20] We always throw different ideas.
[2252.70 → 2253.98] It's so, especially the
[2253.98 → 2256.32] the, the Merry Shipman episode.
[2257.26 → 2258.32] We had them do a special
[2258.88 → 2262.56] Christmas-flavoured intro music
[2262.56 → 2263.30] for the show.
[2263.38 → 2264.44] And I just like, I love that.
[2264.48 → 2265.22] It's just so special.
[2265.44 → 2266.38] It really is just so special.
[2266.38 → 2267.78] And that, I think,
[2267.88 → 2269.26] the important thing there
[2269.26 → 2270.62] is less just about the music.
[2270.80 → 2271.86] It's about the detail, Jared.
[2271.92 → 2272.66] You know this, right?
[2272.74 → 2274.22] Like, if we have
[2274.22 → 2276.52] sweated the details for so long,
[2277.12 → 2278.30] and I think that's,
[2278.42 → 2279.86] I think that's what helps
[2279.86 → 2281.10] me show up more
[2281.10 → 2282.76] is like sweating those details
[2282.76 → 2283.66] and enjoying those details
[2283.66 → 2285.68] because some people will just,
[2285.84 → 2287.34] and it's not bad to say this,
[2287.38 → 2287.90] but like some people
[2287.90 → 2289.28] just throw music on their podcast
[2289.28 → 2289.86] and move along.
[2290.48 → 2292.62] It's just native to us
[2292.62 → 2295.44] to like eke out the nuance
[2295.44 → 2296.56] of a title of a show,
[2296.98 → 2299.00] eke out the nuance of the beats
[2299.00 → 2302.14] in a music track for our shows
[2302.14 → 2303.36] to get the very right music
[2303.36 → 2305.12] for practical AI.
[2305.26 → 2306.86] Like, I love that theme.
[2306.96 → 2308.06] Like, it's such a perfect theme
[2308.06 → 2308.68] for that show.
[2308.98 → 2309.24] It is.
[2309.34 → 2310.58] Brain science and change,
[2310.64 → 2311.38] like all of them.
[2311.46 → 2311.98] Like, obviously,
[2312.68 → 2313.54] GS Party, like it's,
[2313.56 → 2314.12] it's a party.
[2314.48 → 2315.68] Like, it brings the theme
[2315.68 → 2316.82] to the show.
[2316.88 → 2317.62] It brings things to life.
[2317.70 → 2318.90] So I'm happy that Aaron
[2318.90 → 2320.52] and I'm sure others appreciate
[2320.52 → 2322.44] the work we put into that music.
[2322.44 → 2323.66] Along with Brake Master Cylinder.
[2324.42 → 2325.60] So Solfège,
[2325.80 → 2326.80] this outro,
[2327.24 → 2328.64] which ran on the changelog
[2328.64 → 2329.70] for years.
[2351.20 → 2352.00] No longer.
[2352.00 → 2353.14] And this actually started
[2353.14 → 2355.08] with our most popular episode
[2355.08 → 2356.40] of 2021,
[2356.90 → 2359.66] which is Why We Love Vim,
[2360.12 → 2363.76] which was a changelog special.
[2363.88 → 2365.34] This is something new for us,
[2365.56 → 2366.68] kind of breaking out of the mould
[2366.68 → 2369.16] and doing a non-normal
[2369.16 → 2372.02] people sit and talk episode.
[2372.40 → 2372.46] Right?
[2372.52 → 2372.96] Like, that's our,
[2373.00 → 2373.66] that's our style.
[2373.76 → 2374.48] It's like, it's an interview.
[2374.60 → 2375.24] It's a conversation.
[2375.86 → 2376.90] And this was different.
[2376.98 → 2378.58] We had four guests,
[2379.32 → 2380.14] four different interviews.
[2380.14 → 2383.54] We had a long production process.
[2383.54 → 2384.10] I actually,
[2384.48 → 2385.84] there's a lot more work than I,
[2385.92 → 2387.28] I knew it was going to be a lot of work,
[2387.40 → 2388.88] but it's always more work than you think.
[2389.08 → 2389.30] Yeah.
[2389.46 → 2390.86] And it was always off schedule
[2390.86 → 2391.86] because it was a special.
[2391.98 → 2392.44] It wasn't like,
[2392.48 → 2394.02] had to fit in to a certain week.
[2394.08 → 2394.64] So we actually,
[2394.76 → 2396.04] it took me a long time to reduce it,
[2396.08 → 2397.32] mostly because I'm a procrastinator.
[2397.32 → 2400.44] But on that episode,
[2400.44 → 2402.98] we wanted to have a very special outro
[2402.98 → 2405.34] and we put in a new track,
[2405.78 → 2407.20] not Selfridge.
[2407.90 → 2409.42] And it's such a banger
[2409.42 → 2410.56] that we fell in love with it
[2410.56 → 2413.60] and just started replacing that outright.
[2414.04 → 2416.58] Although of all of our songs,
[2416.84 → 2418.22] of all of our outros,
[2418.34 → 2419.78] I'll say this doesn't,
[2419.96 → 2421.16] this doesn't go for the theme songs,
[2421.20 → 2421.86] but for our outros,
[2422.02 → 2423.52] that's the one that most people ask about.
[2423.82 → 2424.06] Yeah.
[2424.06 → 2425.82] It is a Selfridge, like Aaron said.
[2426.34 → 2427.54] And they love that track,
[2427.92 → 2430.32] but we love this new track quite a bit.
[2430.48 → 2432.14] Both Adam and I separately
[2432.14 → 2433.12] kind of fell in love with it.
[2433.56 → 2435.50] The interesting thing about the song is that,
[2435.50 → 2437.88] so Break master works with a DJ,
[2438.02 → 2438.98] I don't know if you can call him a DJ
[2438.98 → 2440.26] or vocalist or a rapper.
[2440.38 → 2441.34] I'm not sure how you would,
[2441.46 → 2444.32] an artist named Disco Tech.
[2445.36 → 2448.56] And so Break master is beyond just podcast famous
[2448.56 → 2450.12] in terms of music production.
[2450.68 → 2452.66] They produce music with,
[2452.66 → 2454.10] I think at least Disco Tech,
[2454.18 → 2455.30] I'm not sure if it's others,
[2455.44 → 2456.88] but I'm sure they would if they did.
[2457.08 → 2460.66] But so this song in particular has,
[2460.94 → 2463.34] it's just the music of that track.
[2463.42 → 2465.48] So there's a whole track out there
[2465.48 → 2467.88] with Disco Tech rapping with,
[2467.88 → 2469.76] you know, lyrics of chorus
[2469.76 → 2470.70] and all that fun stuff.
[2470.76 → 2474.10] Like this is just the music of that song.
[2474.48 → 2474.78] Yes.
[2474.94 → 2476.12] And so I think that's what made it
[2476.12 → 2477.84] also stand above others too.
[2478.60 → 2479.90] And it's also a classical,
[2479.90 → 2482.92] it's like a sample and a remake
[2482.92 → 2484.60] of a classical Bach track,
[2485.12 → 2487.50] which I learned through Inquiries.
[2488.24 → 2490.72] And yeah, the actual lyrical one
[2490.72 → 2493.62] would not make it on our shows
[2493.62 → 2494.96] because of explicit content.
[2495.20 → 2497.24] Although we did do one episode this year,
[2497.32 → 2498.14] our first time ever,
[2498.30 → 2500.64] with nonblended explicit content.
[2500.84 → 2503.08] That was an artistic choice.
[2503.98 → 2507.06] But yeah, so this Why We Love Vim episode,
[2507.06 → 2509.04] this one, you know,
[2509.06 → 2510.36] we put a lot of work into this one.
[2511.06 → 2512.74] And I guess we're just really happy
[2512.74 → 2513.74] that everybody liked it.
[2513.92 → 2517.08] I mean, we had Julia Evans,
[2517.20 → 2518.14] Drew Neal, Size Hinton,
[2518.32 → 2521.40] and Gary Bernhardt on that show.
[2522.08 → 2526.28] All experienced, smart, well-spoken people
[2526.28 → 2528.62] who have just amazing things to say.
[2528.80 → 2529.68] And they really delivered
[2529.68 → 2532.42] and just highlighted an editor
[2532.42 → 2533.94] that so many people use
[2533.94 → 2536.64] and so many people love that.
[2536.92 → 2537.52] It really resonated
[2537.52 → 2538.86] with a lot of folks out there.
[2539.02 → 2539.96] So it felt perfect
[2539.96 → 2542.94] because when you put extra attention
[2542.94 → 2543.60] into an episode,
[2543.80 → 2545.98] you want it to be well-received.
[2546.12 → 2547.02] And it was well-received.
[2547.26 → 2548.78] And just really grateful
[2548.78 → 2550.76] that all that extra work paid off.
[2550.84 → 2552.52] It was the most listened-to episode
[2552.52 → 2554.06] of the entire year,
[2554.18 → 2554.92] which is pretty cool.
[2555.80 → 2557.10] It also influenced me, man.
[2557.12 → 2558.02] I'm a Vim user now.
[2558.44 → 2559.06] There you go.
[2559.24 → 2560.10] I had to convert.
[2560.10 → 2560.94] I was, you know,
[2561.00 → 2562.28] like on my Linux box
[2562.28 → 2563.30] or my Raspberry Pi,
[2563.38 → 2565.56] I would often just use NATO
[2565.56 → 2567.52] because it's just there.
[2567.76 → 2568.80] I can get out of it.
[2568.90 → 2570.46] Mainly because I can exit it.
[2570.90 → 2571.96] You know, mainly.
[2572.32 → 2573.60] Well, you can exit Vim now, right?
[2573.64 → 2574.14] You learned it.
[2574.36 → 2575.78] But I've learned Vim, you know,
[2575.84 → 2576.76] and I think the hardest thing
[2576.76 → 2577.38] to learn about Vim
[2577.38 → 2578.60] might be how to exit it.
[2579.34 → 2579.66] I know.
[2579.72 → 2580.20] They would do well
[2580.20 → 2581.80] just to have the thing at the bottom
[2581.80 → 2583.04] that just tells you how or something,
[2583.20 → 2583.52] you know.
[2583.64 → 2585.16] And just insert in visual mode
[2585.16 → 2586.92] and so much so that I even have
[2586.92 → 2588.28] a Vim RC file.
[2588.28 → 2589.98] You know, like you don't have to have
[2589.98 → 2591.92] a Vim RC file just by using Vim.
[2592.30 → 2593.08] No, you do not.
[2593.34 → 2593.96] You have to elect.
[2594.14 → 2595.06] And not only that,
[2595.12 → 2596.64] but I have my colour scheme
[2596.64 → 2597.72] set to Dracula Pro.
[2598.32 → 2598.70] Nice.
[2598.78 → 2599.38] So when I have Vim,
[2599.44 → 2600.64] I have Dracula Pro.
[2600.80 → 2601.52] Thank you, Zeno,
[2602.40 → 2604.54] as my theme for it.
[2605.04 → 2605.88] And so, yeah,
[2605.94 → 2607.20] I mean, I love that episode too.
[2608.42 → 2609.76] And I think when you don't have deadlines,
[2609.96 → 2610.12] right,
[2610.14 → 2612.90] when you don't have a constraint,
[2613.24 → 2615.52] it's possible to meander
[2615.52 → 2618.26] to your finish line unless...
[2618.26 → 2618.60] It is.
[2618.62 → 2619.56] You know, we had Source graph.
[2619.80 → 2620.88] That was one of our first,
[2620.96 → 2621.28] I think,
[2621.38 → 2622.72] interruption-free sponsors this year.
[2622.88 → 2623.10] Yep.
[2623.60 → 2625.10] Source graph obviously did a lot
[2625.10 → 2626.40] of great fundraising this year
[2626.40 → 2628.20] to bolster their company.
[2628.32 → 2629.38] They're now a unicorn,
[2630.04 → 2631.34] at least by Silicon Valley
[2631.34 → 2633.26] valuation standards.
[2634.16 → 2636.08] Love the team behind that company.
[2636.08 → 2637.00] Thanks also to them
[2637.00 → 2638.66] to support that.
[2638.96 → 2640.64] And wasn't it
[2640.64 → 2644.02] the Neovim fella?
[2644.76 → 2645.48] Forget his name.
[2645.88 → 2646.08] TJ?
[2646.08 → 2646.16] TJ?
[2646.54 → 2648.24] He works at Source graph.
[2648.34 → 2648.96] He does, yeah.
[2649.12 → 2649.72] I didn't even know that
[2649.72 → 2650.72] until we did that show.
[2650.78 → 2650.88] I'm like,
[2650.94 → 2651.70] this is so cool.
[2651.96 → 2652.32] And I'm like,
[2653.04 → 2653.92] it was so awesome to have him
[2653.92 → 2654.38] as a...
[2654.38 → 2655.22] Yeah, close the loop.
[2655.46 → 2656.44] ...interruption-free sponsor.
[2656.94 → 2657.32] And then...
[2657.32 → 2657.90] Yeah, that is cool.
[2657.94 → 2659.26] ...how that show turned around.
[2659.50 → 2661.38] And this is the...
[2661.38 → 2663.44] This is not the We Love Vim episode.
[2663.64 → 2664.86] It's a counterpart to it,
[2664.90 → 2665.88] but still quite as popular.
[2666.14 → 2666.36] Yeah.
[2666.48 → 2667.12] Why Neovim,
[2667.18 → 2668.16] which was very popular as well.
[2668.22 → 2668.78] We'll get to that one.
[2668.92 → 2669.32] So...
[2669.32 → 2669.52] Yeah.
[2670.18 → 2672.08] Awesome that you got influenced...
[2672.08 → 2672.32] Yeah.
[2672.42 → 2674.00] ...to adopt Vim.
[2674.10 → 2675.82] That makes us official influencers,
[2676.18 → 2676.38] but...
[2676.38 → 2676.94] And no plugins.
[2677.48 → 2679.10] Okay, I'm going the Gary route.
[2679.22 → 2680.00] I'm going no plugins.
[2680.08 → 2680.94] I was trying to keep it vanilla.
[2681.72 → 2682.50] Vim RC only.
[2682.72 → 2684.42] A few things like syntax on
[2684.42 → 2685.18] and a couple other things.
[2685.24 → 2687.08] Just like settings, essentially.
[2687.08 → 2688.44] What every Vim user might do,
[2688.50 → 2689.74] and I'm just trying to avoid plugins
[2689.74 → 2691.78] except for my colour scheme,
[2691.90 → 2693.40] which you have to do that.
[2694.06 → 2695.34] So the number one Vim influencer
[2695.34 → 2696.72] might be Gary Bernhardt.
[2696.82 → 2698.12] We gave him the mic drop
[2698.12 → 2699.44] at the very end of the episode.
[2699.90 → 2701.28] He gives three reasons
[2701.28 → 2702.94] why you might want to use Vim.
[2703.14 → 2703.98] Here's the clip.
[2704.60 → 2705.54] It's very compelling.
[2709.04 → 2710.92] I absolutely would recommend it.
[2711.00 → 2712.04] I also would recommend people
[2712.04 → 2713.90] not to beat themselves up over it
[2713.90 → 2715.04] if they decide they don't like it.
[2715.36 → 2716.56] There's kind of this weird
[2716.56 → 2717.52] sort of, you know,
[2717.56 → 2718.62] you have to use the hard thing
[2718.62 → 2720.14] or you're not a real programmer
[2720.14 → 2720.46] or whatever.
[2720.60 → 2721.50] Don't worry about any of that,
[2721.58 → 2722.30] but give it a try.
[2722.50 → 2724.66] And I can name three different reasons
[2724.66 → 2725.66] to do it,
[2726.02 → 2726.88] and I think all of them
[2726.88 → 2727.90] are sufficient on their own.
[2728.10 → 2729.04] So first, RSI.
[2729.20 → 2730.00] It'll prevent injury.
[2730.20 → 2731.80] It's a really important thing
[2731.80 → 2732.44] as a programmer
[2732.44 → 2733.30] if you want to make a career
[2733.30 → 2733.74] out of this.
[2733.86 → 2734.76] The second is speed.
[2735.22 → 2736.80] Vim is unambiguously faster
[2736.80 → 2737.92] than other editors.
[2738.12 → 2739.80] It's not even remotely controversial
[2739.80 → 2740.62] to say that.
[2740.74 → 2742.12] But the question, of course,
[2742.16 → 2742.54] is going to be
[2742.54 → 2743.98] whether you value speed
[2743.98 → 2745.28] over what you may be giving up,
[2745.28 → 2747.06] things like deep language support
[2747.06 → 2748.26] from something like Visual Studio
[2748.26 → 2750.28] or JetBrains IDE or whatever.
[2750.52 → 2751.74] So you're making a tradeoff there.
[2751.90 → 2752.50] But for me,
[2752.74 → 2754.02] speed is even sufficient on its own
[2754.02 → 2754.94] because every time
[2754.94 → 2755.54] you have to stop
[2755.54 → 2756.80] and like slowly make some edits
[2756.80 → 2757.72] is a chance for you
[2757.72 → 2758.94] to forget what you were doing,
[2758.98 → 2760.24] to lose the state in your brain.
[2760.30 → 2760.86] And maybe you're like
[2760.86 → 2762.24] eight levels deep in your stack
[2762.24 → 2763.16] and you're going to start
[2763.16 → 2764.42] losing those levels
[2764.42 → 2765.90] if you have to get distracted.
[2766.10 → 2766.92] It's also just fun,
[2767.08 → 2767.90] honestly, to be fast.
[2768.12 → 2769.92] And then the third reason
[2769.92 → 2771.28] is that Vim,
[2771.46 → 2772.80] unlike most other editors,
[2773.00 → 2774.06] is not going to go away.
[2774.06 → 2775.54] The Vim keystrokes in particular,
[2775.78 → 2776.70] so many people have them
[2776.70 → 2778.32] so deep in their brains
[2778.32 → 2779.52] that 30 years from now,
[2779.64 → 2780.66] you will absolutely be able
[2780.66 → 2781.14] to get an editor
[2781.14 → 2782.06] that has those keystrokes.
[2782.18 → 2783.24] I don't know whether it'll be Vim.
[2783.50 → 2783.98] I don't know whether
[2783.98 → 2785.78] Bram Molina will be maintaining it,
[2785.96 → 2787.16] but you will be able
[2787.16 → 2788.12] to use those keystrokes.
[2788.24 → 2788.92] So any of those,
[2789.02 → 2790.02] for me, is sufficient,
[2790.22 → 2791.20] especially for the last one.
[2791.24 → 2792.38] If you think about the timeline,
[2792.58 → 2793.42] just for me, right?
[2793.46 → 2794.06] 15 years.
[2794.20 → 2795.04] At the beginning of that time,
[2795.14 → 2796.34] TextMate was just becoming popular.
[2796.58 → 2798.28] Then it was Sublime Text,
[2798.28 → 2798.78] was cool.
[2799.10 → 2800.00] Then Atom was cool.
[2800.34 → 2801.34] Then VS Code was cool.
[2801.34 → 2803.02] A lot of people switched
[2803.02 → 2803.94] between two of those,
[2804.02 → 2804.38] three of those,
[2804.46 → 2805.42] maybe all four of those.
[2805.54 → 2806.34] And that whole time,
[2806.40 → 2807.18] I was just getting better
[2807.18 → 2808.26] and better and better at Vim.
[2808.40 → 2809.46] And you multiply that out
[2809.46 → 2810.42] by the length of a career,
[2810.54 → 2811.94] use Vim for 40 years,
[2812.04 → 2812.80] you're going to be
[2812.80 → 2814.34] so good at it by the end,
[2814.38 → 2815.50] and it's still going to be
[2815.50 → 2816.72] totally relevant, I think.
[2816.72 → 2822.18] So when he said the 15 years thing
[2822.18 → 2823.18] with the different editors,
[2823.78 → 2825.14] I was like,
[2825.22 → 2826.16] you got me, Gary.
[2827.70 → 2828.58] You got me.
[2828.62 → 2829.66] Because I was the hopper.
[2829.78 → 2830.78] I hopped from different thing
[2830.78 → 2831.48] to different thing.
[2832.00 → 2832.34] And he's like,
[2832.36 → 2833.46] I'm just getting better and better.
[2833.62 → 2834.30] That just, to me,
[2834.36 → 2834.84] was like,
[2835.26 → 2836.96] developer gotcha.
[2838.08 → 2839.30] You moved around,
[2839.44 → 2840.26] I stay consistent,
[2840.70 → 2842.08] and I reap the benefits
[2842.08 → 2842.90] of that consistency.
[2843.62 → 2844.94] So you switched your editor.
[2846.72 → 2847.04] All right.
[2847.04 → 2847.96] Number two,
[2848.64 → 2849.88] Modern Unix Tools
[2849.88 → 2851.74] with Nick Nunataks.
[2851.88 → 2852.60] This was actually
[2852.60 → 2853.82] the next episode
[2853.82 → 2854.48] right after
[2854.48 → 2855.80] Why We Love Vim.
[2855.84 → 2857.08] I think it may have benefited
[2857.08 → 2857.72] a bit from
[2857.72 → 2859.06] Why We Love Vim's success.
[2859.18 → 2860.32] This is 451.
[2861.38 → 2862.52] And this is one of those shows
[2862.52 → 2863.18] where it's just like,
[2863.26 → 2863.46] hey,
[2864.10 → 2865.20] let's look at a repo
[2865.20 → 2867.24] and talk down
[2867.24 → 2868.12] a list of things on a repo.
[2868.54 → 2869.86] So it's kind of the opposite
[2869.86 → 2871.54] from Why We Love Vim,
[2871.60 → 2872.02] which was like
[2872.02 → 2872.98] a six-month production.
[2874.24 → 2875.30] This was
[2875.30 → 2877.00] find a cool repo,
[2877.40 → 2878.42] invite a friend on the show,
[2878.74 → 2880.38] and just talk about it.
[2880.86 → 2881.62] And that was Nick,
[2881.76 → 2882.24] and that was
[2882.24 → 2883.32] Modern Unix Tools,
[2883.94 → 2884.92] which just lists out
[2884.92 → 2886.30] replacements for
[2886.30 → 2888.18] older Unix tools.
[2888.74 → 2890.22] And just have a fun conversation
[2890.22 → 2890.88] needing out
[2890.88 → 2892.50] all about the command line.
[2892.50 → 2894.00] Not that I think
[2894.00 → 2895.02] this was a bad show
[2895.02 → 2896.34] by any means,
[2896.88 → 2897.68] but I'm surprised.
[2898.34 → 2899.84] And I love that about
[2899.84 → 2901.10] when we do
[2901.10 → 2901.98] this at the end of the year.
[2902.42 → 2903.66] Because wasn't it last year
[2903.66 → 2904.54] it was a bunch of authors?
[2904.60 → 2905.66] We had a bunch of authors on
[2905.66 → 2906.46] in that year,
[2906.52 → 2907.48] and almost everybody
[2907.48 → 2908.12] unanimously was
[2908.12 → 2909.02] a book author.
[2909.38 → 2909.72] Yeah.
[2910.00 → 2910.68] And this year,
[2910.78 → 2911.14] it's like,
[2911.20 → 2911.42] okay,
[2911.48 → 2912.54] this is all kind of tooling.
[2912.96 → 2913.94] Why Neo Vim?
[2914.22 → 2914.94] Unix tooling,
[2915.38 → 2916.14] Vim itself.
[2916.52 → 2916.86] Right.
[2917.02 → 2917.94] 10,000 hours of programming.
[2918.06 → 2918.86] I'm sort of like
[2918.86 → 2920.18] spoiling some of the next
[2920.18 → 2921.14] mentions.
[2921.50 → 2922.10] Spoilers, man.
[2922.52 → 2922.70] Yeah.
[2922.98 → 2923.88] And then Oath even.
[2924.12 → 2924.14] Like,
[2924.34 → 2925.22] who would have thought that?
[2925.60 → 2926.62] Now you spoil the whole list.
[2926.72 → 2927.50] You have just gone through it.
[2928.46 → 2928.98] That's all right.
[2929.00 → 2929.88] We needed to move faster.
[2930.12 → 2930.48] But yeah,
[2930.58 → 2930.74] I mean,
[2930.74 → 2931.54] I was surprised.
[2932.10 → 2932.90] I'll spoil the next one then.
[2932.92 → 2933.22] So, okay,
[2933.34 → 2933.84] Oath,
[2934.00 → 2934.86] It's Complicated
[2934.86 → 2935.68] was the next one.
[2935.78 → 2936.08] And that,
[2936.48 → 2937.60] I love that show
[2937.60 → 2938.94] for a nickname,
[2939.10 → 2939.38] really.
[2939.86 → 2940.94] All Business Bart.
[2941.54 → 2941.70] Like,
[2941.74 → 2942.10] when you said
[2942.10 → 2943.12] All Business Bart
[2943.12 → 2943.84] at the end of the show,
[2943.94 → 2944.02] like,
[2944.08 → 2945.14] that made it for me, man.
[2945.64 → 2946.28] It made it for me.
[2946.28 → 2946.84] That made it.
[2946.94 → 2947.84] When I said that,
[2947.94 → 2949.50] you looked off-put almost.
[2949.68 → 2949.86] Oh,
[2949.96 → 2950.74] I loved it, man.
[2951.14 → 2951.58] At the moment,
[2951.64 → 2952.00] I was like,
[2952.04 → 2952.90] that's so good.
[2953.04 → 2953.38] Okay.
[2953.54 → 2953.78] Okay,
[2953.78 → 2954.74] so this is a little
[2954.74 → 2955.44] insider baseball.
[2955.60 → 2955.80] Yes.
[2956.00 → 2957.64] Bart is a good friend of ours.
[2957.72 → 2958.76] We met him at Microsoft
[2958.76 → 2959.52] years ago
[2959.52 → 2960.66] and he brought us out
[2960.66 → 2961.60] for Build
[2961.60 → 2962.94] in Seattle
[2962.94 → 2963.98] and also New York.
[2964.30 → 2965.30] And he's become
[2965.30 → 2966.02] a great friend.
[2966.52 → 2967.98] And what I love most
[2967.98 → 2968.64] about this business
[2968.64 → 2969.84] and I think what makes me
[2969.84 → 2970.80] not just say,
[2970.86 → 2971.36] but feel
[2971.36 → 2972.20] we came for the Type,
[2972.22 → 2973.02] we stayed for the humans
[2973.02 → 2974.80] is because of relationships
[2974.80 → 2975.60] like Bart.
[2976.08 → 2977.84] Because Bart no longer works
[2977.84 → 2978.72] at Microsoft.
[2979.02 → 2979.46] Now he,
[2980.02 → 2980.46] at the time,
[2980.46 → 2981.28] he worked for Okta,
[2981.64 → 2983.20] which recently acquired
[2983.20 → 2983.68] All Zero.
[2984.20 → 2984.72] Now he,
[2985.40 → 2986.00] now I didn't,
[2986.12 → 2986.70] I don't know if I showed you
[2986.70 → 2987.48] this with you, Jared,
[2987.60 → 2988.58] but he works at
[2988.58 → 2989.62] Influx Data now.
[2990.74 → 2991.54] As you may know,
[2991.60 → 2992.78] Influx Data is one of our partners.
[2993.02 → 2993.78] We love them very much.
[2993.82 → 2994.88] They're awesome people over there.
[2995.12 → 2995.56] Paul Dix,
[2995.64 → 2996.32] the rest of the team,
[2996.70 → 2997.16] Maria,
[2997.42 → 2997.78] Chris,
[2997.92 → 2998.54] a lot of people.
[2999.10 → 3000.10] Tom Crow used to be there.
[3000.18 → 3001.34] He was from Equinix Metal.
[3001.66 → 3002.54] I just love the people.
[3002.70 → 3003.06] Like it's,
[3003.06 → 3003.54] it's really
[3003.54 → 3004.86] that kind of thing.
[3004.86 → 3005.54] So long story short,
[3005.64 → 3006.06] Bart,
[3006.38 → 3008.00] not even about Oath at this point yet,
[3008.06 → 3008.64] but Bart,
[3008.74 → 3009.42] uh,
[3009.42 → 3010.66] helped us coordinate this show
[3010.66 → 3011.52] with Aaron Prequel.
[3011.80 → 3013.60] And Aaron is,
[3013.72 → 3014.00] uh,
[3014.30 → 3016.58] deep in the throes of Oath,
[3017.10 → 3019.12] came on and schooled us.
[3019.60 → 3020.88] Like absolutely schooled us.
[3020.98 → 3021.60] Maybe less you,
[3021.64 → 3022.16] but more me.
[3022.30 → 3022.56] Okay.
[3022.80 → 3023.20] Oh yeah.
[3023.20 → 3023.44] Uh,
[3023.44 → 3026.12] but schooled us on all things Oath
[3026.12 → 3027.74] and the details of where things are at
[3027.74 → 3030.22] and why it's so complicated.
[3030.44 → 3030.80] Right.
[3031.48 → 3034.24] It was funny because as you were telling that,
[3034.30 → 3035.32] I was looking at our transcript
[3035.32 → 3036.84] trying to find that quote.
[3036.96 → 3038.02] And I was like,
[3038.06 → 3039.28] maybe it got cut from the show
[3039.28 → 3040.38] because it's not anywhere in here,
[3040.40 → 3040.80] but no,
[3040.84 → 3041.92] it turns out it's unintelligible.
[3042.20 → 3043.58] So near the end of the show,
[3043.58 → 3045.02] I thanked Bart.
[3045.38 → 3045.74] I said,
[3045.82 → 3045.88] well,
[3045.90 → 3047.74] we do want to give a shout-out to unintelligible
[3047.74 → 3049.60] for introducing us to you,
[3049.68 → 3049.78] Aaron.
[3049.88 → 3051.00] So I'll go fix that after this.
[3051.08 → 3052.68] But what I said was all business Bart.
[3052.68 → 3053.52] And so tell,
[3053.82 → 3055.52] tell me why that was funny to you.
[3055.66 → 3055.90] Like,
[3055.92 → 3056.34] what's the
[3056.44 → 3058.18] what's the inside story?
[3058.46 → 3058.56] Well,
[3058.58 → 3058.86] I mean,
[3059.02 → 3061.42] this is a bit of insider baseball again,
[3061.42 → 3062.04] but like,
[3062.36 → 3063.52] I know when we went to,
[3063.68 → 3063.80] okay,
[3063.80 → 3065.96] so a bit about maybe how we work,
[3066.26 → 3068.30] where we're not put your quarter in kind of
[3068.30 → 3069.44] dance monkey kind of people.
[3069.66 → 3070.10] Right.
[3070.28 → 3074.14] And so even though we went to Seattle in New York
[3074.14 → 3075.26] on Microsoft's dime,
[3075.68 → 3076.16] thank you.
[3076.62 → 3076.86] Uh,
[3076.86 → 3078.04] that didn't mean that we went there
[3078.04 → 3079.64] and we're going to do the shows they want us to do.
[3079.82 → 3080.22] Right.
[3080.32 → 3081.54] And so Bart has an agenda
[3081.54 → 3082.50] and for sure,
[3082.50 → 3082.82] he does,
[3082.88 → 3085.86] he's a marketer, and he's trying to connect us with the right people
[3085.86 → 3088.00] and get the right message out there about Microsoft and build.
[3088.12 → 3088.82] And this,
[3089.00 → 3089.16] you know,
[3089.16 → 3090.06] this is years in the making,
[3090.16 → 3091.92] but they hadn't acquired GitHub then.
[3092.04 → 3095.94] So we're different Microsoft in terms of like the community perception of them.
[3095.94 → 3099.42] And so I think we play maybe not a significant,
[3099.42 → 3102.88] but a key role in many of the key roles that were played to,
[3102.88 → 3103.70] I guess,
[3103.78 → 3104.78] reshape their narrative.
[3104.78 → 3108.98] And so rather than just going to this conference or conferences and just saying,
[3109.36 → 3109.56] great,
[3109.66 → 3109.90] Bart,
[3110.00 → 3110.90] who are we talking to?
[3110.98 → 3112.40] Just make us a list, and we'll just,
[3112.60 → 3113.52] we'll just dance.
[3113.94 → 3115.12] We push back on him.
[3115.72 → 3115.96] You know,
[3115.96 → 3116.72] we push back and said,
[3116.74 → 3117.68] we want this kind of person.
[3117.72 → 3118.52] We want that kind of person.
[3118.58 → 3119.72] We want to talk at this level.
[3120.14 → 3121.00] We want to talk about AI.
[3121.12 → 3121.74] We want to talk about,
[3122.06 → 3122.38] you know,
[3122.48 → 3123.78] Python and the different things we did.
[3123.80 → 3125.94] And we pushed just as much as he pushed us.
[3126.48 → 3129.92] And so I think that's why I thought it was funny because Bart is fun,
[3130.02 → 3131.06] but he's also business.
[3131.38 → 3132.86] And so because of the
[3132.86 → 3133.82] the deeper relationship,
[3134.00 → 3134.06] it,
[3134.42 → 3135.86] when you said that it just was like,
[3136.12 → 3136.64] yes,
[3136.68 → 3138.76] that's the perfect nickname for Bart.
[3138.80 → 3140.02] And I think he actually likes it a lot.
[3140.08 → 3141.78] So he doesn't take it as like an offence by any means.
[3141.80 → 3141.90] No,
[3141.94 → 3144.00] it was not meant to offend by any means.
[3144.08 → 3144.26] No.
[3144.48 → 3145.32] And because he's always,
[3145.82 → 3150.06] he brings his entire person to our relationship and our conversations.
[3150.36 → 3151.86] And I can actually get to be,
[3152.10 → 3153.36] to where in certain contexts,
[3153.36 → 3154.40] I am kind of all business.
[3154.40 → 3154.80] I'm like,
[3155.16 → 3155.48] all right,
[3155.48 → 3156.44] we've got a show to start,
[3156.52 → 3158.18] but you and Bart are talking and you guys can,
[3158.28 → 3159.84] you guys will talk for hours,
[3159.92 → 3160.06] you know,
[3160.08 → 3162.76] I'll be there for the first 90 minutes, and I'll kind of check out,
[3163.00 → 3163.70] go check my email.
[3164.08 → 3164.80] And so,
[3165.08 → 3165.96] you know,
[3165.96 → 3169.30] it was kind of actually tongue in cheek about him being all business because I,
[3169.46 → 3170.82] he tends to think I am all business,
[3170.94 → 3171.18] you know,
[3171.20 → 3172.86] so a little bit of that as well is all,
[3173.06 → 3174.82] all in good fun,
[3174.82 → 3176.38] but also just a deep dive on OAuth,
[3176.46 → 3176.80] which is,
[3177.20 → 3178.06] it is complicated.
[3178.06 → 3180.86] That's one of my favourite episode titles of the year.
[3180.98 → 3181.38] OAuth,
[3181.50 → 3184.06] it's complicated with quotes,
[3184.20 → 3184.36] you know,
[3184.36 → 3185.14] like the relationship.
[3185.14 → 3185.58] Yeah.
[3186.16 → 3187.46] I like that so much too.
[3187.50 → 3187.76] And that's,
[3188.02 → 3189.28] I think that really is,
[3189.74 → 3193.50] I don't know what number in terms of unity for this job is fun,
[3193.60 → 3196.68] but like titling shows is extremely challenging.
[3196.94 → 3197.24] Yes.
[3197.30 → 3198.66] But also very fun.
[3199.02 → 3200.08] It's sometimes just pain,
[3200.28 → 3201.88] pure pain when you can't think of a good one.
[3201.88 → 3204.44] But I think the next one might be an example that like,
[3204.56 → 3205.30] why Neo Vim?
[3205.48 → 3206.96] I think we went back and forth.
[3207.38 → 3207.70] Yeah.
[3208.04 → 3208.36] And like,
[3208.36 → 3209.94] this was a very much a settling moment.
[3209.94 → 3210.24] Like,
[3210.56 → 3210.78] okay,
[3210.82 → 3211.06] why,
[3211.16 → 3211.80] why Neo Vim?
[3211.94 → 3212.52] Question mark.
[3212.68 → 3212.78] Yeah.
[3213.02 → 3213.32] Yeah.
[3213.60 → 3214.52] It was almost giving up,
[3214.56 → 3215.20] but it's perfect.
[3215.70 → 3218.26] Kind of was because that was kind of the point of the show was like,
[3218.26 → 3220.14] we just did this big Vim episode.
[3220.32 → 3222.02] And then everybody's asking us like,
[3222.36 → 3222.64] you know,
[3222.70 → 3224.32] when's the Neo Vim show going to come?
[3224.56 → 3224.86] Right.
[3225.04 → 3225.64] And so,
[3225.80 → 3226.04] okay,
[3226.08 → 3227.22] we're doing the Neo Vim show.
[3227.30 → 3227.50] In fact,
[3227.54 → 3229.14] this one was joined.
[3230.02 → 3233.02] This one was joined by Nick Needed co-hosting with me.
[3233.08 → 3234.20] So you weren't there for this one.
[3234.46 → 3234.64] Well,
[3234.66 → 3235.98] he's such a Vim lover.
[3236.20 → 3236.46] You know what I mean?
[3236.46 → 3237.12] Like he is.
[3237.26 → 3238.34] There's even memes about it.
[3238.50 → 3238.62] Yeah.
[3238.66 → 3239.98] He's the quintessential Vim lover.
[3241.12 → 3244.98] And the question a lot of Vim users ask themselves is why Neo Vim?
[3245.06 → 3245.20] Like,
[3245.28 → 3245.92] why was it created?
[3246.02 → 3246.78] Why do I care?
[3247.06 → 3248.40] Should I be checking it out?
[3248.50 → 3250.62] And so number four,
[3250.74 → 3252.60] most popular episode of the year,
[3252.66 → 3254.46] why Neo Vim with TJ Decries of,
[3254.46 → 3258.88] of source graph and a core member of the Neo Vim team.
[3259.44 → 3260.48] Number five.
[3260.72 → 3260.82] Wait,
[3260.84 → 3260.92] wait,
[3260.92 → 3261.00] wait,
[3261.02 → 3261.70] before we move on.
[3261.80 → 3262.02] Yes.
[3262.22 → 3265.50] Can I mention a couple non-landed titles?
[3265.90 → 3266.06] Oh,
[3266.08 → 3266.72] you have for that one.
[3267.04 → 3267.26] Yeah.
[3267.28 → 3268.96] I did the search in our Slack.
[3269.22 → 3269.44] Oh,
[3269.46 → 3269.64] okay.
[3269.92 → 3270.74] So Jared and I,
[3270.78 → 3272.92] we DM like just in time,
[3273.00 → 3273.32] essentially,
[3273.50 → 3274.54] if not right after the show,
[3274.62 → 3276.06] just in time of the show shipping.
[3276.20 → 3276.58] Right.
[3276.64 → 3277.68] And we'll go back and forth.
[3277.68 → 3279.68] And because the show ship on Friday afternoons,
[3280.44 → 3280.62] you know,
[3280.64 → 3282.68] I'm usually on the back patio,
[3283.30 → 3283.56] you know,
[3283.56 → 3289.10] having a barley pop on my phone and Adam's still working because that's the way we work sometimes.
[3289.10 → 3289.62] And so I'm,
[3289.76 → 3289.94] yeah,
[3290.20 → 3290.80] I'm DMing.
[3290.88 → 3291.30] So go ahead.
[3291.46 → 3294.22] So my picks were Timing with Neo Vim.
[3294.72 → 3297.00] Let there be Neo Vim with an exclamation point.
[3297.10 → 3298.42] Let there be Neo Vim.
[3298.70 → 3299.60] Like let there be light.
[3299.72 → 3299.88] Yeah.
[3299.98 → 3300.08] Yeah.
[3300.08 → 3300.20] Yeah.
[3300.78 → 3302.06] Neo Vim on the rise.
[3302.56 → 3305.08] And then you said there's a Neo Vim in town.
[3305.78 → 3306.92] Neo Vim on the block.
[3307.00 → 3307.08] Oh,
[3307.10 → 3307.86] like a new Vim,
[3308.00 → 3309.14] like Neo Vim on the block.
[3309.20 → 3309.50] Yeah.
[3309.94 → 3310.96] Like Jenny from the block.
[3311.04 → 3311.48] And then we were like,
[3311.48 → 3313.32] we didn't want it to be like a takeover of,
[3313.32 → 3314.44] of Vim itself.
[3314.44 → 3315.30] Like it wasn't a replacement.
[3315.42 → 3316.52] I think that's even said.
[3316.70 → 3316.98] Yeah,
[3317.42 → 3317.86] exactly.
[3318.14 → 3318.54] And then we,
[3318.68 → 3320.24] then we missed words over like,
[3320.30 → 3324.50] would it be V I M apostrophe I N G with Neo Vim?
[3324.54 → 3324.86] And you're like,
[3324.88 → 3327.14] I think it'd be Timing like V I M M I N G.
[3327.14 → 3327.52] And I'm like,
[3327.52 → 3327.62] well,
[3327.62 → 3329.56] that just doesn't work with me.
[3329.56 → 3330.98] Like it's just too many M's,
[3330.98 → 3332.60] even though it made sense.
[3332.96 → 3335.08] And you said V Vim's been verbified.
[3335.34 → 3335.54] And like,
[3335.58 → 3335.76] we just,
[3335.88 → 3337.00] this is us going back and forth,
[3337.06 → 3337.70] back and forth.
[3338.04 → 3338.18] Right.
[3338.38 → 3339.30] About the word Vim.
[3339.60 → 3342.50] And this is probably a good 15 is minutes.
[3342.80 → 3343.58] And I'm like,
[3343.62 → 3346.58] it's kind of lame to be one word kind of a thing.
[3346.66 → 3347.00] I don't know.
[3347.06 → 3347.66] Not creative at all.
[3347.68 → 3347.86] And you're like,
[3347.90 → 3348.14] I agree.
[3348.18 → 3348.66] It's not creative.
[3349.10 → 3350.50] And then I think you finally said,
[3350.54 → 3351.04] um,
[3351.52 → 3352.44] why Neo Vim eventually?
[3352.60 → 3352.76] And,
[3352.86 → 3353.04] uh,
[3353.04 → 3353.54] I'm just like,
[3353.58 → 3353.86] and you're like,
[3353.86 → 3354.70] just give me some options.
[3354.78 → 3355.16] Why Neo Vim?
[3355.16 → 3355.42] I'm like,
[3355.48 → 3355.62] okay,
[3355.62 → 3355.84] cool.
[3356.12 → 3356.66] That works for me.
[3357.22 → 3357.92] And that's how we ended it.
[3357.92 → 3358.02] Yeah.
[3358.04 → 3360.42] Sometimes a tile just strikes you, and you just know it.
[3360.48 → 3361.68] I think a lot of it's complicated.
[3361.78 → 3364.20] I think I put that in their even before we recorded the show.
[3364.24 → 3364.50] Because I,
[3364.58 → 3366.78] that was my feelings about it and you just left it.
[3366.82 → 3367.10] So I'll,
[3367.18 → 3367.42] I'll,
[3367.42 → 3368.94] I'll throw in some title options sometimes.
[3368.94 → 3370.76] And then Adam ships the episode usually.
[3371.06 → 3372.92] And so he kind of has final call on that.
[3372.92 → 3374.62] And sometimes he just uses it.
[3374.68 → 3376.00] Sometimes he asks for replacements,
[3376.16 → 3377.16] but yeah.
[3377.54 → 3379.96] Other times it's just like pulling teeth to get an episode.
[3379.96 → 3380.14] Well,
[3380.16 → 3382.68] let's move on to number five,
[3382.78 → 3384.06] most popular of the year.
[3384.32 → 3386.88] We'll talk about this in more depth in a minute,
[3386.88 → 3388.14] because it's one of my favourites as well.
[3388.72 → 3393.78] This is episode four 63 with Matt record lessons from 10,000 hours of
[3393.78 → 3394.28] programming.
[3395.10 → 3399.96] Another tried and true show style for us is found an awesome blog post and
[3399.96 → 3402.18] then have the person come on and talk to us about it.
[3402.18 → 3404.86] But let's not go too far into details on that one.
[3404.94 → 3405.84] Quite yet.
[3405.96 → 3407.46] Honourable mentions most popular.
[3407.90 → 3409.36] Didn't quite make the top five,
[3409.56 → 3410.98] but still got a lot of listens.
[3410.98 → 3413.94] The business model of open source with Adam Jacob,
[3413.94 → 3419.18] this insane tech hiring market with Gary Gabbros and leading leaders who lead
[3419.18 → 3420.36] engineers with Laura Hogan.
[3420.90 → 3421.80] Definitely some of my favourites.
[3422.38 → 3422.70] Yep.
[3423.36 → 3423.54] I mean,
[3423.56 → 3424.56] I concur with the listeners.
[3424.80 → 3425.20] So do I.
[3425.40 → 3429.80] It's nice to see that like we have certain feelings about an episode and then
[3429.80 → 3433.00] the listeners respond in the same way.
[3433.08 → 3433.28] Like,
[3433.56 → 3433.92] you know,
[3433.92 → 3435.40] having Laura on the show,
[3435.58 → 3439.58] I mentioned that in the deeply human conversation we had on,
[3439.58 → 3441.74] on dev discuss and,
[3441.82 → 3442.14] uh,
[3442.14 → 3444.00] which was a few episodes back.
[3444.02 → 3445.24] So go back in your feed,
[3445.28 → 3446.50] just like one or two shows.
[3446.78 → 3447.54] You'll see that.
[3447.60 → 3448.60] But like,
[3448.62 → 3450.84] I had imposter syndrome inviting her on.
[3450.84 → 3453.26] Because I was like such a fan of her work.
[3453.26 → 3453.70] I was like,
[3453.74 → 3454.32] you know,
[3454.32 → 3455.60] like I'm a little,
[3455.72 → 3456.70] I'm a little intimidated.
[3457.06 → 3457.94] She's so cool.
[3459.14 → 3460.22] Can we match up?
[3460.26 → 3461.40] And then Adam coming back.
[3461.40 → 3461.58] I mean,
[3461.60 → 3462.86] we had Adam on the show 2017,
[3462.86 → 3464.34] I think in,
[3464.40 → 3464.58] uh,
[3464.58 → 3466.04] in line with Ozcon.
[3466.56 → 3469.32] And then it was the war for the soul of open source.
[3469.34 → 3470.42] Like what a dramatic title.
[3470.52 → 3470.74] Right.
[3471.26 → 3472.78] And then Gary is another B back.
[3472.84 → 3474.02] We had a lot of B backs this year,
[3474.08 → 3474.44] Adam,
[3474.82 → 3475.06] Gary,
[3475.42 → 3476.80] or was the first time.
[3477.12 → 3477.52] Um,
[3477.88 → 3478.14] you know,
[3478.14 → 3478.98] that was super cool.
[3479.54 → 3480.70] Big fan of all those,
[3480.84 → 3481.26] those shows.
[3481.32 → 3481.96] I agree with the
[3481.96 → 3482.82] the audience.
[3483.44 → 3483.80] Well,
[3483.82 → 3484.72] let's get into our favourites.
[3484.72 → 3486.64] Then I think you just hit on a few.
[3486.70 → 3487.34] Do you want to go first?
[3487.96 → 3488.32] Well,
[3488.44 → 3491.38] I like all the ones that are as most popular,
[3491.40 → 3498.10] based upon our numbers to go one layer deeper in terms of a non B back.
[3498.18 → 3499.14] This is a first timer.
[3499.78 → 3502.98] Can you believe Ryan doll spent his whole career without coming on the show?
[3503.20 → 3504.24] I know for shame.
[3504.50 → 3504.74] Right.
[3504.88 → 3505.02] Well,
[3505.06 → 3505.44] come on,
[3505.46 → 3505.64] Ryan.
[3505.74 → 3506.54] Thank you so much though,
[3506.54 → 3508.70] for coming on exploring Dino land with us.
[3508.80 → 3509.16] Yes.
[3509.20 → 3509.62] Thank you.
[3509.74 → 3510.84] Which was quite fun.
[3510.88 → 3511.24] Honestly,
[3511.38 → 3512.86] I was even with that one too.
[3512.90 → 3514.06] I was a little nervous because like,
[3514.62 → 3519.66] we should have done that show in terms of like how rooted we were in early JavaScript,
[3519.88 → 3521.74] early node and express.
[3521.74 → 3522.00] Even,
[3522.40 → 3522.68] you know,
[3522.72 → 3524.06] we had Tim Caswell on the
[3524.34 → 3524.88] as alum,
[3525.46 → 3526.82] as a logger way back.
[3527.08 → 3527.28] All right.
[3527.34 → 3528.42] Tim Caswell is the
[3528.92 → 3530.96] I believe he's the original author of express.
[3531.26 → 3532.32] If I can recall correctly,
[3532.90 → 3533.92] if not a maintainer,
[3533.98 → 3535.18] I think he created it.
[3535.70 → 3537.20] Maybe it could have been TJ Hollywood.
[3537.30 → 3538.96] Chuck fact check me on that,
[3539.04 → 3539.34] please.
[3539.56 → 3540.10] But okay.
[3540.30 → 3541.08] It's one of those two.
[3541.48 → 3541.78] Yeah.
[3541.90 → 3542.40] Keep going.
[3543.36 → 3546.80] But finally having Ryan doll on is one of my favourites.
[3546.80 → 3548.40] Like just exploring dealing with him.
[3548.64 → 3548.98] I think,
[3549.04 → 3550.50] you know,
[3551.06 → 3552.50] without going into all the details,
[3552.60 → 3554.14] obviously Dino is a
[3554.66 → 3555.02] what is it?
[3555.06 → 3555.78] An anagram?
[3555.96 → 3556.12] Is that,
[3556.22 → 3556.74] is that the right word?
[3556.80 → 3557.24] One of those,
[3557.34 → 3558.14] whenever you take the word,
[3558.18 → 3558.80] you jumble it up.
[3558.84 → 3559.30] Is it an anagram?
[3559.88 → 3560.12] Uh,
[3560.18 → 3560.40] sure.
[3560.74 → 3560.98] Sure.
[3561.10 → 3561.36] Okay.
[3561.40 → 3563.38] So Dino is node spelled differently,
[3563.46 → 3563.82] obviously.
[3564.00 → 3564.28] Yes,
[3564.28 → 3564.64] exactly.
[3564.76 → 3567.22] And I think they did it accidentally, and then I'm like,
[3567.26 → 3567.38] Oh,
[3567.52 → 3567.84] Dino,
[3567.94 → 3568.60] like a dinosaur.
[3568.70 → 3568.82] And then,
[3568.88 → 3571.58] so they went the whole D E N O route,
[3571.74 → 3571.96] Dino,
[3571.96 → 3572.60] like a dinosaur.
[3573.00 → 3577.76] And so this is Ryan's new take essentially on all that he did with.
[3577.78 → 3577.94] No,
[3578.00 → 3580.22] there's a lot of interesting history around.
[3580.28 → 3580.52] No,
[3580.58 → 3581.20] there was a
[3581.20 → 3583.00] a fork called IO JS,
[3583.56 → 3583.98] you know,
[3583.98 → 3585.20] just a lot of interesting,
[3585.36 → 3590.42] I would say maturity in governance of open source community around open source
[3590.42 → 3595.84] and how you lead a project like node that took off quite well to allow
[3595.84 → 3597.72] JavaScript to go beyond,
[3597.86 → 3598.44] you know,
[3598.48 → 3600.38] the front end to go to the backend as well.
[3600.38 → 3602.50] So just having him on finally,
[3602.62 → 3603.82] I think after 12 years,
[3603.90 → 3604.32] basically,
[3605.06 → 3607.14] I think nodes have been around for almost as long as we have.
[3607.34 → 3608.78] So it's a long,
[3608.88 → 3610.04] long time in the making basically.
[3610.42 → 3614.84] So I have done some background now and confirmed that express,
[3615.22 → 3617.70] initial author of Express.js was TJ Hollywood.
[3617.80 → 3618.00] Chuck.
[3618.32 → 3618.60] Okay.
[3618.94 → 3619.18] Sorry,
[3619.22 → 3619.46] TJ,
[3619.82 → 3620.08] my bad.
[3620.08 → 3625.08] Tim Caswell creation X created many node things.
[3625.80 → 3626.12] Uh,
[3626.12 → 3627.20] one of which was connected,
[3627.36 → 3628.88] which is a middleware for node,
[3629.08 → 3630.16] which was very,
[3630.16 → 3630.90] uh,
[3630.90 → 3631.38] popular.
[3631.38 → 3634.12] And I think built it with TJ.
[3634.12 → 3634.26] Okay.
[3634.84 → 3636.68] And then also JS,
[3636.92 → 3638.20] get to edit,
[3638.68 → 3639.26] uh,
[3639.38 → 3639.90] Jack,
[3640.22 → 3641.26] many things,
[3642.00 → 3643.06] NBM perhaps.
[3643.40 → 3643.84] Right.
[3644.06 → 3645.50] So now I'm starting to guess things,
[3645.60 → 3647.12] but lots of things.
[3647.34 → 3651.86] And now I believe he works at Tercel according to this website called LinkedIn.
[3651.86 → 3652.84] And he needs to,
[3653.14 → 3656.62] because Tim is such a tools toolmaker.
[3656.94 → 3657.28] Yeah.
[3657.62 → 3658.26] You know,
[3658.76 → 3659.16] he,
[3659.40 → 3663.10] he goes deeper than deep can go when it comes.
[3663.20 → 3673.56] I think we had him on the show three or four years back, and we were talking about like IDEs and like all this stuff he's doing with get and just a super deep stuff like above,
[3673.56 → 3676.98] above my head in terms of like where I need tooling at.
[3677.28 → 3680.12] Like he's a toolmaker for toolmakers essentially.
[3680.50 → 3680.58] Yeah.
[3680.58 → 3684.24] So Tim makes a lot of sense in light of Tercel.
[3684.44 → 3687.16] And especially with a lot of the talent acquisition they've been doing,
[3687.42 → 3689.52] like just so much happening at Tercel there.
[3689.66 → 3690.74] They're really scooping up a lot of talent.
[3691.10 → 3691.22] Yeah.
[3691.48 → 3693.08] I think Tim is the one who I told him,
[3693.26 → 3699.60] somebody should just give you money and let you do whatever you want to do with technology.
[3699.86 → 3700.88] Like just be a
[3700.88 → 3702.86] a patron back before Patreon.
[3703.04 → 3703.66] They should be like,
[3704.20 → 3704.66] you know how,
[3704.82 → 3705.12] you know,
[3705.12 → 3707.56] rich people used to just like commission someone to make art.
[3707.82 → 3708.02] Yeah.
[3708.10 → 3708.42] You know,
[3708.42 → 3709.84] and of course they would want to picture themselves,
[3709.84 → 3710.70] but they'd also say,
[3710.86 → 3711.46] do whatever you want,
[3711.86 → 3712.12] you know,
[3712.24 → 3713.44] create whatever art you're going to create.
[3713.90 → 3717.60] Tim Caswell is one of those guys that just creates art with code.
[3718.10 → 3721.06] And so I'm happy to hear that he's doing well.
[3721.58 → 3724.12] Hopefully Tercel is letting him get that done.
[3724.12 → 3726.14] So let's go back and forth on these.
[3726.20 → 3726.92] So that was one.
[3727.02 → 3728.78] I'll just say also in my list,
[3728.88 → 3730.20] exploring D&L and with Ryan Dahl.
[3730.34 → 3732.18] So that was a highlight for both of us.
[3732.28 → 3732.36] Oh,
[3732.38 → 3732.98] it is in your list.
[3733.04 → 3733.26] Cool.
[3733.44 → 3733.62] Yep.
[3733.68 → 3734.38] I do see that now.
[3735.08 → 3736.10] The other one for me,
[3736.14 → 3738.26] I think I have a theme except for one,
[3738.40 → 3740.32] which is like when we step outside the normal,
[3740.52 → 3741.40] I'm enjoying myself.
[3741.40 → 3749.34] So the first time we did that this year was the elastic versus AWS episode where we got community perspectives.
[3749.34 → 3758.00] We put out a call to our listeners to call in as well as invited a bunch of people from around the community.
[3758.62 → 3759.52] And I think we had one,
[3759.64 → 3759.80] two,
[3759.96 → 3760.16] three,
[3760.32 → 3760.54] four,
[3760.64 → 3760.88] five.
[3760.96 → 3764.20] We had six voices on that episode,
[3764.34 → 3764.84] including our,
[3764.94 → 3766.10] not including our own eight.
[3766.20 → 3766.86] If you count us,
[3767.54 → 3768.48] Adam Jacob,
[3769.18 → 3769.86] Heather Meeker,
[3770.44 → 3771.04] Monique Jane,
[3771.16 → 3771.76] Paul Dix,
[3772.04 → 3772.76] the embrace or,
[3773.02 → 3774.38] and Marcus Steepest,
[3774.88 → 3776.42] which was just cool.
[3776.56 → 3777.22] A lot of work,
[3777.50 → 3778.80] a lot of interviews.
[3779.48 → 3783.78] I think you had some post-production on this work that I didn't have to bear the brunt of.
[3784.08 → 3786.28] So good on you for that.
[3786.48 → 3792.56] But I thought this was really cool because it's such a big conversation that is plus one person,
[3792.66 → 3794.74] I just didn't feel like would have done it justice.
[3794.98 → 3797.56] This was all the way back in published in February.
[3797.56 → 3800.18] I think we recorded these late January,
[3800.70 → 3801.46] early February,
[3802.22 → 3803.86] a deep dive on the business of open source.
[3804.16 → 3806.16] And I thought it turned out really well.
[3806.16 → 3812.20] I just liked hearing different people have different takes, and they're all well-reasoned, and they all come from these different perspectives.
[3812.64 → 3812.78] Yeah.
[3812.94 → 3813.96] So that was one of my favourites.
[3814.64 → 3817.64] What I liked most about this was it was a community well-rounded,
[3817.98 → 3819.64] like not just practitioners.
[3819.64 → 3823.36] Paul Dix is a CTO,
[3823.82 → 3825.60] founder of InfluxDB,
[3825.88 → 3827.02] Influx Data is the company,
[3827.12 → 3827.72] but InfluxDB,
[3827.88 → 3829.00] the technology,
[3829.46 → 3830.64] permissively open sourced.
[3830.64 → 3835.88] They have built a business around it, and he's been in the ups and downs of the business out of open source.
[3837.32 → 3845.24] Heather Meeker is a well-known lawyer who's assisted many companies in establishing their licenses.
[3845.86 → 3847.34] So the SSPL,
[3848.04 → 3850.80] she's done a lot of work in different licensing and stuff like that.
[3851.34 → 3854.40] I'm probably leaving out lots because it's just meant to be light,
[3854.56 → 3856.08] but a legal side,
[3856.08 → 3856.30] even,
[3856.52 → 3856.68] you know,
[3856.72 → 3858.48] Adam Jacob built a company around it.
[3858.60 → 3858.86] Chef,
[3858.98 → 3859.32] obviously,
[3859.44 → 3860.02] Finish John.
[3860.52 → 3860.86] D-Graph.
[3861.22 → 3861.58] Same,
[3861.86 → 3862.26] you know,
[3862.44 → 3863.36] and then Vicky Bras sore,
[3863.50 → 3864.44] who's very much,
[3864.60 → 3865.06] you know,
[3865.12 → 3865.60] in the
[3865.68 → 3871.44] in the weeds of what is and what is not open source and just kind of helping lead communities through the process of open source.
[3871.62 → 3872.36] And Marcus,
[3872.50 → 3872.92] a listener,
[3873.22 → 3873.50] you know,
[3873.50 → 3876.40] sharing his thoughts on like how this played out for him,
[3876.66 → 3876.80] you know,
[3876.82 → 3879.60] what his perspective was as an everyday developer,
[3879.74 → 3880.02] essentially.
[3880.20 → 3882.54] So multi-angled for that show.
[3882.54 → 3884.44] I just love how that came together.
[3884.76 → 3885.04] Honestly.
[3901.20 → 3904.50] This episode is brought to you by our friends at Launch Darkly,
[3904.66 → 3906.62] feature management for the modern enterprise,
[3906.96 → 3909.16] power testing in production at any scale.
[3909.42 → 3910.18] Here's how it works.
[3910.58 → 3912.22] Launch Darkly enables development teams,
[3912.22 → 3915.12] and operation teams to deploy code at any time.
[3915.38 → 3917.66] Even if a feature isn't ready to release to users,
[3918.02 → 3925.92] wrapping code with feature flags gives you the safety to test new features and infrastructure in your production environments without impacting the wrong end users.
[3926.34 → 3927.62] When you're ready to release more widely,
[3927.92 → 3932.68] update the flag status and the changes are made instantaneously by the real-time streaming architecture.
[3933.14 → 3933.86] Eliminate risk,
[3934.02 → 3934.66] deliver value,
[3934.80 → 3937.38] get started for free today at LaunchDarkly.com.
[3937.70 → 3938.18] Again,
[3938.50 → 3939.38] LaunchDarkly.com.
[3942.22 → 3959.32] All right,
[3959.38 → 3961.26] you want to go back and do one of your favourites?
[3961.26 → 3962.74] Oh,
[3962.74 → 3964.20] back to my list.
[3964.32 → 3965.46] Which one shall I pick?
[3965.54 → 3965.66] Okay,
[3965.70 → 3968.68] so I'll just go with the next one in line with this then.
[3968.80 → 3970.50] Not so much next one in terms of favourites,
[3970.70 → 3972.44] but back to Adam,
[3972.66 → 3974.60] the business model of open source.
[3975.22 → 3975.28] And,
[3975.38 → 3976.30] you know,
[3976.34 → 3977.04] Adam was on.
[3977.04 → 3983.42] So this is funny because we actually pulled the Adam Jacob clip for the show we just talked about.
[3984.20 → 3984.78] You know,
[3984.80 → 3987.32] this community perspectives on Elastic versus AWS.
[3987.96 → 3991.84] We pulled that Adam clip from the conversation we had with him way back,
[3992.26 → 3994.16] I think in like 2017 or 2018.
[3994.78 → 3995.84] And it was still accurate,
[3995.90 → 3996.34] still true.
[3996.52 → 3998.14] And we said that again in,
[3998.68 → 3998.82] you know,
[3998.84 → 4000.30] the business model for open source.
[4000.48 → 4002.12] I pay attention to Adam Jacob on Twitter.
[4002.12 → 4006.30] I always appreciate his perspective on like hard things in life,
[4006.44 → 4007.74] like hard decisions,
[4008.00 → 4009.96] hard emotional thoughts on software,
[4010.48 → 4011.80] hard things in terms of like,
[4011.84 → 4012.62] even when Docker,
[4012.72 → 4014.26] when Docker took their,
[4014.34 → 4016.28] their thing that I think everybody thought should be open source.
[4016.34 → 4017.36] There were a lot of thoughts around this.
[4017.42 → 4019.44] And Adam just has this different perspective on it.
[4019.86 → 4021.24] So I always appreciate like the
[4021.24 → 4023.00] the Adam word of wisdom essentially.
[4023.14 → 4027.46] And so the business model of open source was a good show to kind of go into,
[4027.62 → 4029.86] into that because Adam's cool.
[4030.28 → 4030.60] There's a clip.
[4032.12 → 4035.68] I'm so hopeful.
[4035.96 → 4036.18] Yeah,
[4036.46 → 4036.90] no,
[4036.98 → 4037.20] look,
[4037.28 → 4038.18] how can you not be hopeful?
[4038.74 → 4039.46] Look at people,
[4039.84 → 4041.76] look at this thing that we do all the time.
[4042.00 → 4043.88] It's insane that it exists at all.
[4044.00 → 4048.84] And it exists because we've all decided it should like literally all of us
[4048.84 → 4052.56] decided that this was the coolest thing we'd seen, and we wanted to keep
[4052.56 → 4054.40] doing it, and we do it every day.
[4054.54 → 4055.90] And it's such a blessing.
[4056.22 → 4060.60] And that like mass group decision that this is how it's going to go.
[4060.60 → 4061.28] And that's,
[4061.44 → 4063.74] and that we can all have lives because of it.
[4063.74 → 4064.20] And we can,
[4064.38 → 4067.86] we can spend our time on earth doing this work.
[4067.86 → 4069.42] That is such a beautiful thing.
[4069.66 → 4073.16] And I fundamentally believe that that is that,
[4073.28 → 4074.48] that is who people really are.
[4074.68 → 4077.76] There are so many things that divide us and make us awful.
[4077.76 → 4079.80] And those are awful things.
[4079.80 → 4081.56] And I see them and I don't want them.
[4081.70 → 4082.20] And do you know what I mean?
[4082.28 → 4082.46] Like,
[4082.74 → 4082.86] yeah.
[4083.02 → 4085.88] And also at the core of what we all hope for,
[4086.28 → 4088.00] I think that's really what we all hope for.
[4088.12 → 4091.70] And we've got this little pocket of the universe where there's this precious
[4091.70 → 4092.48] thing.
[4092.48 → 4094.32] And we happen to have done it in software.
[4094.48 → 4097.54] I think that happened in software because the resources are infinite.
[4097.82 → 4099.34] If you have power in a computer,
[4100.00 → 4100.86] you can do what you want.
[4101.20 → 4103.74] So it's effectively infinite within its own sphere.
[4103.76 → 4106.88] It's not because power and access to computers and all that stuff.
[4106.94 → 4108.58] But if you put that stuff aside,
[4108.58 → 4114.14] like it is this infinite resource where it costs nothing to let other people have
[4114.14 → 4114.30] it.
[4114.54 → 4115.80] That is a beautiful thing.
[4115.86 → 4116.70] It's a lovely vision.
[4116.70 → 4117.20] And it's,
[4117.34 → 4117.44] yeah,
[4117.48 → 4120.10] it makes me infinitely hopeful for what it can do and be.
[4123.28 → 4125.86] It's obviously Adam's talking about open source.
[4126.86 → 4127.26] Obviously.
[4127.46 → 4127.62] Right.
[4127.74 → 4128.02] Just to,
[4128.10 → 4128.74] just to be clear,
[4128.88 → 4129.52] you're listening to the thing.
[4129.60 → 4129.66] Like,
[4129.72 → 4130.52] what is Adam talking about?
[4130.58 → 4131.82] It's open source that we,
[4132.20 → 4132.36] yeah.
[4132.56 → 4136.64] And I even got to say this recently on the deeply human episode we did with
[4136.64 → 4137.06] Dev discuss.
[4137.78 → 4138.92] I think I said,
[4139.02 → 4139.22] I don't,
[4139.36 → 4142.26] I didn't remember saying this until I saw the clip on Twitter later on.
[4142.46 → 4143.24] Cause sometimes you,
[4143.32 → 4145.24] you stay things in life, and you're like,
[4145.58 → 4146.38] I don't recall saying that.
[4146.38 → 4146.52] Okay.
[4146.70 → 4147.30] That's true.
[4147.40 → 4148.00] It's true.
[4148.58 → 4151.36] That open source is the most important thing we have going on right now.
[4151.44 → 4151.70] And now,
[4151.70 → 4155.26] obviously there are a lot of important things going on right now beyond simply
[4155.26 → 4155.68] open source.
[4155.80 → 4156.86] But I mean,
[4157.18 → 4157.74] if,
[4157.86 → 4159.08] if software is eating the world,
[4159.22 → 4160.16] open source ate software,
[4160.58 → 4160.72] right?
[4160.74 → 4165.30] Everything is built on the backs of open source software.
[4165.94 → 4169.34] And Adam's just describing a world where we all get to show up, and it's this
[4169.34 → 4171.22] precious thing, and it's worth protecting.
[4171.30 → 4172.24] It's worth showing up for.
[4172.84 → 4177.60] And that's the origination of everything we've done here is the movement of
[4177.60 → 4178.58] open source in 20,
[4178.92 → 4179.56] 2009,
[4179.76 → 4180.82] GitHub just come around.
[4180.82 → 4183.54] And open source is moving so fast.
[4183.88 → 4185.02] And yeah,
[4185.22 → 4185.92] so cool.
[4186.46 → 4187.70] Adam is a special human being.
[4188.50 → 4188.62] You know,
[4188.64 → 4189.90] he really is a special human being.
[4190.24 → 4190.92] I like,
[4191.00 → 4191.86] he doesn't pull any punches.
[4192.14 → 4193.50] He'll tell you exactly what he's thinking.
[4193.84 → 4197.66] And so it's always fun to ask him questions because he'll just tell you exactly
[4197.66 → 4198.64] what he thinks about it.
[4199.08 → 4200.48] He is not shy about his opinion.
[4200.68 → 4201.30] He really is not.
[4201.40 → 4201.50] No.
[4201.50 → 4201.82] And,
[4201.88 → 4203.24] and he's a special human.
[4203.34 → 4204.08] I love his spirit.
[4204.72 → 4205.32] What about you?
[4205.36 → 4205.88] What's next for you?
[4205.96 → 4206.18] All right.
[4206.18 → 4209.30] Back to me is back to one of our most popular episodes.
[4209.64 → 4212.84] The one mentioned lessons from 10,000 hours of programming.
[4212.84 → 4217.14] And this one very much reminded me of one of my favourite episodes from last year,
[4217.24 → 4219.02] which is laws for hackers to live by,
[4219.40 → 4223.44] which is where we just have a list of,
[4223.96 → 4224.44] in this case,
[4224.50 → 4230.30] reflections from Matt after he's gone through his commensurate 10,000 hours to become an expert.
[4230.30 → 4233.18] things he's picked up along the way.
[4233.78 → 4239.20] And we just go deep and discuss and react to those things.
[4239.28 → 4242.20] We did that with the hacker laws episode last year.
[4242.26 → 4243.28] This one's not laws.
[4243.38 → 4245.56] It's just things he's found to be true.
[4246.22 → 4248.58] And I just really enjoy those conversations.
[4248.86 → 4249.00] You know,
[4249.06 → 4249.36] they're,
[4249.40 → 4251.00] they're deep in the weeds of,
[4251.00 → 4252.42] of software engineering,
[4252.70 → 4254.82] best practices and worst practices,
[4255.14 → 4256.74] but they're also,
[4256.74 → 4261.02] they fly above any sort of particular technology.
[4261.32 → 4261.58] You know,
[4261.60 → 4262.90] we're not talking about Jira.
[4263.06 → 4264.56] We're not talking about Python.
[4264.90 → 4266.76] We're not talking about Kubernetes.
[4267.86 → 4272.92] Maybe those things weave in and out because those are ultimately the things that we're using to build things.
[4273.34 → 4276.68] But we're talking about how we go about doing what we do.
[4277.28 → 4280.22] And those to me are just very enjoyable conversations.
[4280.90 → 4281.02] Yeah.
[4281.58 → 4282.44] It's the craft,
[4282.88 → 4283.02] right?
[4283.10 → 4284.02] It's the craft.
[4284.24 → 4284.60] Exactly.
[4284.82 → 4285.34] What's funny too,
[4285.40 → 4285.96] is that this,
[4286.32 → 4286.46] you know,
[4286.46 → 4287.46] his title was reflections.
[4288.24 → 4288.58] Yeah.
[4288.70 → 4288.92] Like,
[4289.06 → 4289.28] you know,
[4289.30 → 4289.90] his post was,
[4290.02 → 4291.34] and we try to turn them into lessons.
[4291.68 → 4292.00] Right.
[4292.28 → 4292.48] Well,
[4292.48 → 4293.44] they were lessons for us.
[4293.48 → 4293.96] He kept saying,
[4294.08 → 4294.20] Hey,
[4294.26 → 4294.44] Hey,
[4294.44 → 4295.18] this isn't a lesson.
[4297.16 → 4297.52] Yeah.
[4297.72 → 4298.76] Which was fun.
[4298.84 → 4299.54] And I think that's,
[4299.60 → 4300.10] that's so true.
[4300.10 → 4300.38] It's,
[4300.44 → 4302.40] it's definitely the human side of things.
[4302.46 → 4302.54] Like,
[4302.60 → 4304.12] how did this really matter to me?
[4304.88 → 4306.10] Given my context,
[4306.20 → 4307.58] given my know-how,
[4307.74 → 4308.80] given the things I'm building,
[4309.56 → 4311.78] given even my experience level.
[4312.24 → 4313.22] And I think that's,
[4313.38 → 4313.58] uh,
[4314.22 → 4315.96] when you get into that kind of detail like that,
[4315.96 → 4319.34] I think special things come out because you're right.
[4319.38 → 4322.06] It's not just about like a particular language we may have.
[4322.54 → 4324.14] And something even ML said recently,
[4324.14 → 4324.66] uh,
[4324.66 → 4329.16] I think it was in the JavaScript channel where it was like conversation back and forth about like different frameworks for JavaScript.
[4329.98 → 4332.28] And I think she was even saying like to remove the emotion out of it.
[4332.32 → 4334.90] Like it's more about what tool do you need today to get the job done?
[4335.26 → 4336.48] Not what are you in love with?
[4337.22 → 4337.54] Right.
[4337.54 → 4338.14] Because I think we could say,
[4338.22 → 4338.28] Oh,
[4338.30 → 4341.26] we love Ruby, or we love Python, or we love Elixir.
[4341.34 → 4341.48] We,
[4341.60 → 4341.78] you know,
[4341.82 → 4342.60] love JavaScript.
[4343.62 → 4343.90] Well,
[4344.40 → 4344.80] you know,
[4344.92 → 4346.30] do you have to love the tool you're using?
[4346.42 → 4352.24] Sometimes you just need to use the thing that works best for your team and the product and what you're trying to do at the time.
[4352.34 → 4352.54] Right.
[4352.66 → 4353.04] It's not like,
[4353.16 → 4353.26] well,
[4353.26 → 4354.86] I need this because I love this thing.
[4354.90 → 4356.84] It's more like what works right now.
[4356.84 → 4359.98] And that might've been one of his lessons is like use the right tool,
[4360.40 → 4361.02] not the one you love.
[4361.02 → 4364.48] So clearly I wasn't the only one who enjoyed this episode.
[4364.58 → 4365.68] It was one of our most populars.
[4365.82 → 4369.30] And we had a listener call in and tell us about it as well.
[4373.14 → 4373.80] Hi there.
[4374.14 → 4374.58] Change log.
[4374.58 → 4376.68] My name is Rusted Globulin,
[4377.06 → 4381.76] which Microsoft speech recognition system recognizes me as Austin Glue.
[4382.12 → 4383.08] So you can call me that.
[4383.64 → 4385.10] I'm a data scientist from Russia.
[4385.58 → 4387.80] Currently I work in the UAE.
[4387.80 → 4393.12] And my favourite episode of 2021 is with Matt Sickert,
[4393.38 → 4397.12] about his 10,000 hours of deliberate programming.
[4397.98 → 4400.24] And my favourite points are number three,
[4400.46 → 4402.18] delete as much code as you can,
[4402.88 → 4407.62] which is quite funny because he mentioned that he predominantly deleted other people's code,
[4407.80 → 4410.60] which I feel so compelled to do sometimes.
[4411.12 → 4412.46] And the other point is number 10.
[4412.56 → 4413.46] If it looks ugly,
[4413.52 → 4415.24] it's most likely a terrible mistake.
[4415.24 → 4419.42] And I go back to my code before I listened to that podcast.
[4420.18 → 4423.22] And I find so many quote unquote terrible mistakes.
[4423.94 → 4424.42] Well,
[4424.92 → 4426.36] I'm finished of the show.
[4426.56 → 4430.30] Thanks a lot for your work and have a good new year.
[4430.30 → 4434.52] I love that.
[4435.24 → 4438.16] He pulls in how the
[4438.28 → 4438.66] what was it?
[4438.68 → 4439.14] The machine learning,
[4439.20 → 4440.08] the Microsoft thing that,
[4440.08 → 4441.56] you know,
[4441.72 → 4442.82] kind of converted his name,
[4442.94 → 4443.52] Austin Glue.
[4443.88 → 4444.42] That was,
[4444.48 → 4445.04] that was hilarious.
[4445.52 → 4445.70] Yeah.
[4446.06 → 4447.52] Good sense of humour on you,
[4447.58 → 4447.82] Austin.
[4447.94 → 4448.10] I,
[4448.22 → 4451.98] I appreciate your insights on those two particular aspects for me.
[4452.04 → 4452.34] Actually,
[4452.42 → 4452.64] the
[4452.64 → 4454.34] the part about if it's,
[4454.42 → 4455.38] if it's ugly,
[4455.44 → 4458.34] it's most likely a terrible mistake was probably the best part of that.
[4458.34 → 4460.46] I just got so many kicks out of that.
[4460.72 → 4462.26] Just thinking about it in different contexts,
[4462.44 → 4462.74] you know?
[4463.60 → 4464.00] Ah,
[4464.30 → 4464.82] yes.
[4465.66 → 4467.08] I love that we're getting,
[4467.08 → 4467.92] uh,
[4468.24 → 4471.10] beyond our opinions now into state of law,
[4471.18 → 4472.50] because like it could be,
[4472.50 → 4475.18] and has been just you and I sharing our,
[4475.26 → 4475.90] our thoughts.
[4475.90 → 4479.66] And now we have some fans reaching in and sharing their thoughts too.
[4479.72 → 4480.24] By the way,
[4480.48 → 4480.90] uh,
[4481.46 → 4484.08] everyone who participated and got their clip mentioned,
[4484.20 → 4484.66] what are they getting,
[4484.78 → 4484.88] Jerry?
[4485.00 → 4486.14] What are they getting a special prize?
[4486.20 → 4486.52] What are they getting?
[4486.52 → 4487.76] They're going to get a free,
[4487.76 → 4489.26] changelog t-shirt.
[4489.40 → 4492.32] We're going to use our handy dandy coupon code generator,
[4492.32 → 4495.46] or just go into the Shopify admin and do it manually this time.
[4495.50 → 4495.88] Who knows?
[4496.66 → 4499.46] And we're going to ship them off a free t-shirt for sending those in.
[4499.52 → 4500.54] So we appreciate that.
[4501.14 → 4502.14] I also have,
[4502.26 → 4505.28] for those who did not check out that particular episode,
[4505.42 → 4506.98] that's 463,
[4507.06 → 4507.34] of course,
[4507.42 → 4508.34] links in the show notes.
[4508.70 → 4511.26] Here is a sample from our conversation with Matt Sickert.
[4511.26 → 4519.38] One that we touched on with the Drag Prog fellas themselves around dry.
[4519.54 → 4520.86] This is always controversial dry.
[4521.88 → 4524.34] And it's because we all think about it a little bit differently,
[4524.44 → 4526.68] or I think that we all misunderstand what their point was.
[4526.74 → 4529.98] They did point out on that episode when we had their 20th anniversary show,
[4530.10 → 4537.30] that one of the most misunderstood points in the Drag Prog book is the chapter on dry.
[4537.30 → 4538.32] So they tried to rewrite it.
[4538.38 → 4543.88] I haven't read the rewrite very closely to know if they accomplished clarifying that.
[4543.96 → 4544.96] But you have a point here.
[4545.08 → 4547.42] One of your reflections says,
[4547.66 → 4550.64] know when to break the rules for rules like don't repeat yourself.
[4550.76 → 4554.44] Sometimes a little repetition is better than a bit of dependency.
[4554.62 → 4558.64] And you link to another blog post of yours called dry considered harmful.
[4558.80 → 4560.04] You want to unpack that one for us?
[4560.42 → 4560.62] Yeah.
[4560.74 → 4561.06] I mean,
[4561.16 → 4562.20] the dry consider harmful,
[4562.36 → 4564.34] maybe that's a clickbaity.
[4564.52 → 4564.68] Yeah.
[4564.68 → 4565.50] A little clickbaity.
[4565.50 → 4567.18] And, you know,
[4567.24 → 4568.70] I don't think it's actually that harmful.
[4568.90 → 4573.88] I think the way that it's been dogmatically used is sometimes a little dangerous.
[4574.16 → 4577.10] But it's just more of a point about how as programmers,
[4577.40 → 4579.54] we have a bias for abstraction.
[4580.24 → 4583.64] So understanding that we have that bias and trying to keep it in check,
[4583.96 → 4588.84] especially when it comes to duplication versus encapsulation.
[4588.84 → 4601.72] And I just think that it's a path that I've gone down too many times of carving out microservices or creating service boundaries where there really shouldn't be or prematurely optimizing when requirements aren't really finalized.
[4601.72 → 4602.38] And, you know,
[4602.42 → 4604.10] the requirements are never finalized.
[4604.10 → 4605.52] And, you know,
[4605.52 → 4613.72] just the wrong abstraction at a low level can really cause a lot of issues in terms of refactoring and just added work down the line.
[4614.48 → 4614.50] Yeah.
[4614.54 → 4616.88] I think we fall prey to this because we're such pattern matchers.
[4616.88 → 4621.62] And as soon as you spot that pattern, you're like, ooh, opportunity.
[4622.28 → 4626.72] Some of that, those abstraction layers are the power in software, right?
[4626.76 → 4629.44] Like the ability to build those abstractions are what give us leverage.
[4629.62 → 4633.50] And so every time we see one, we think, boom, I'm not going to repeat myself.
[4633.62 → 4635.58] I'm going to dry this sucker up.
[4635.58 → 4649.42] But like you point out, oftentimes that second iteration, that second usage is not actually generalizable, or it looks generalizable until you find the third one, which, you know, just throw another parameter on the function.
[4649.76 → 4651.20] You know, it's what we do.
[4651.30 → 4653.48] We're like, well, I'll just throw a true false at the end of this thing.
[4653.62 → 4660.00] And then I have this extra branch in my function because it didn't actually map onto the use case like I thought it did.
[4660.20 → 4661.80] So a lot of it's just that enthusiasm.
[4661.80 → 4663.94] I think of like, ah, here we go.
[4663.94 → 4666.24] Oh, I'm going to dry this sucker up.
[4666.30 → 4666.88] It feels so good.
[4667.62 → 4668.66] But it does come back to bite.
[4668.96 → 4669.14] Yeah.
[4669.36 → 4670.90] I don't really know how to get around it.
[4670.94 → 4674.20] It's just, you know, I keep on falling prey to it over and over again.
[4674.52 → 4676.40] But maybe that's just kind of the name of the game.
[4679.60 → 4681.56] Having Matt on the show was cool.
[4681.64 → 4685.74] I don't think he's, I think he said he didn't podcast too often, but I think he did a great job with that.
[4685.74 → 4692.46] And I think that's as the source of encouragement and maybe even one that didn't necessarily make the list, but not.
[4692.46 → 4695.36] And I kind of even feel bad about saying that was the Six episode.
[4695.46 → 4696.52] It kind of reminded me of that.
[4696.72 → 4699.96] Like he is taking the Six advice where he's learning in public essentially.
[4700.88 → 4705.04] And so I'm an advocate now having a conversation with Sean Six Wang.
[4705.04 → 4709.88] And I think that Matt had definitely put these thoughts out there.
[4709.88 → 4719.20] And I would say as a source of encouragement for our audience and listeners, like whether you're new to programming or you're new to the show, or you're new to software development, or you're an old hat, and you've been around for years.
[4719.56 → 4726.88] We all have something to share that levels up the next person right behind us or even old Adam, old Jared or old you.
[4726.88 → 4732.20] And I think that's what Matt did here was he shared his reflection on it probably to kind of come back a year later.
[4732.32 → 4735.68] Like this blog post may serve him just as much as it served us.
[4735.78 → 4736.14] Yeah.
[4736.34 → 4740.84] For him to come back to in a year or months later to say, how do I really feel?
[4740.90 → 4746.58] Because sometimes you don't know what you think you know until you say it out loud, or you put it in black and white.
[4746.58 → 4752.26] Like there's something that happens in your own mind about what you believe when you declare it.
[4752.48 → 4758.62] And that's what Matt did here was he declared things he reflected on or lessons for us, but reflections for him.
[4758.90 → 4763.94] And I just want to encourage everyone to listen to the show to try to do more of that in this next year.
[4764.16 → 4768.52] What you think you know that is insignificant, it's probably pretty significant.
[4768.74 → 4770.22] And so just find ways to share it.
[4771.06 → 4772.42] I'll leave you all with that.
[4772.72 → 4774.82] And what next?
[4774.82 → 4778.78] Okay, so a surprising, a surprising hard like for me.
[4779.46 → 4785.48] And I would even say must listen would be the Louis Villa show on GS Party.
[4786.04 → 4791.06] And so that show is titled We Ask a Lawyer About GitHub Copilot.
[4791.16 → 4797.84] Now this actually, if I'm splitting hairs here, this was better suited to be an episode of the changelog.
[4797.84 → 4804.62] However, I will say that Nick Geese and Bone skull did a phenomenal job hosting this.
[4804.62 → 4807.36] And I would dare even say better than maybe you and I might have.
[4807.40 → 4813.06] And I'm actually thankful they did it instead of us because, again, back to that shared perspective, shared voices.
[4813.06 → 4820.68] I was so happy to listen to the show and hear that the perspective Louis brought.
[4820.92 → 4825.88] So from what I understand, Louis is a lawyer by trade, but he's in software.
[4826.54 → 4827.60] And I'm sure he does programming.
[4827.68 → 4829.56] I'm just not sure what his full background is.
[4829.56 → 4831.16] But he works at Tile Lift.
[4831.44 → 4834.24] And as you know, Tile Lift is very much fighting to pay the maintainers.
[4834.46 → 4845.34] They're finding ways to create a sustainable ecosystem of enterprise-ready open source that's secure, that's maintained by the maintainers, and that the maintainers aren't starving.
[4845.46 → 4847.70] They're actually getting money for their hard work.
[4847.90 → 4850.74] And the enterprises that are using it are finding ways to support it.
[4850.74 → 4852.18] And that's very much Tile Lift's mission.
[4852.36 → 4855.98] And so Louis is coming from that perspective like what is fair use?
[4856.08 → 4860.18] What does the law say about how this works in terms of copyright, legal licenses?
[4860.18 → 4867.82] And so as you know whether it's proprietary software or open source software, there is a legal license in place that says what you can and can't do with it.
[4868.38 → 4877.20] And so when it comes to the court of law, he really, I think, brought a great perspective on how we should detach emotionally from this and look at it from the law.
[4877.46 → 4881.58] And if we don't like how it's working, that doesn't mean that, okay, deal with it.
[4881.62 → 4883.42] It's just more like this is how the law works.
[4883.42 → 4898.94] And so I think as people who live in the U.S. legal system or legal systems anywhere throughout the world, if you want to change how this works when it comes to fair use or copyright, then the way to change is through legal processes and stuff like that.
[4899.36 → 4905.16] But I just really appreciate the lawyer perspective of this conversation.
[4905.56 → 4906.64] So play the clip.
[4906.64 → 4913.62] It's actually been sort of interesting and honestly a little frustrating for me.
[4913.70 → 4923.66] Some of the same people who came out strongly in favour of fair use when it was or when it was Google saying, yeah, re-implementation should be fair use.
[4923.94 → 4929.18] Like basically when it was Oracle stuff getting copied, everybody was like, hell yeah, copying is awesome.
[4929.98 → 4934.74] And now when it's GPL stuff, like I get the emotional valence there, right?
[4934.74 → 4948.44] But from a lawyer perspective, like GPL is a copyright license and Oracle's, you know, grungy, terrible, every lawyer hates it terms of service or, you know, standard EULA around their code.
[4949.02 → 4951.76] Copyright perspective, those are both copyright licenses, right?
[4951.96 → 4959.50] Courts don't, you know, courts aren't in the business of saying, oh, yes, but we really like Richard Stallman and we really don't like Larry Ellison.
[4959.76 → 4962.76] So, one of these is fair use and the other isn't, right?
[4962.76 → 4972.02] Like there's been some, to me, sort of frustrating inconsistency about people who until a month ago were like big fair use proponents.
[4972.48 → 4976.40] We can get into the nuances of that because it is really complicated.
[4976.68 → 4981.34] Like the question of fair use and machine learning is in fact a really complicated one.
[4981.34 → 4987.84] And anyone who tells you that it's black and white, like courts don't know what machine learning is.
[4988.84 → 4993.86] So like the idea that you can say, oh, yeah, this is definitely fair use or definitely not fair use.
[4994.10 → 4995.82] There's so much gray area in there.
[4995.82 → 5007.30] So, yeah, I mean, one, I'll say from one perspective, I really appreciated listening back to that because I didn't listen to it when I was on the GS Party feed.
[5007.76 → 5008.90] No offence to GS Party, Derek.
[5008.92 → 5009.82] Come on, man.
[5009.86 → 5010.60] I love the show.
[5010.68 → 5011.04] I know.
[5011.14 → 5011.48] I know.
[5011.54 → 5012.06] I should have.
[5012.14 → 5012.66] I should have.
[5013.20 → 5016.80] But obviously, hey, I'm the one who elected it to be the crossover.
[5017.64 → 5017.96] Okay.
[5017.96 → 5019.76] You know, I'm the one who said that, right?
[5019.86 → 5021.88] Like, like totally redeemed yourself.
[5022.00 → 5022.40] Totally redeemed.
[5022.94 → 5026.74] Just when I think you couldn't possibly be any dumber.
[5028.22 → 5030.16] You go and do something like this.
[5032.70 → 5034.90] And totally redeem yourself.
[5036.82 → 5038.28] Maybe because I really want to listen to it.
[5038.30 → 5040.52] I'm like, I'll listen to it if it's on the change log speed.
[5040.66 → 5041.48] Okay, fine.
[5042.16 → 5043.84] But like I got to listen to this show.
[5043.96 → 5046.38] I think I may have been washing dishes or doing some housework.
[5046.38 → 5051.08] Like that whole one hour blitz you do at the end of the day after the house is turned upside down because of the kids or whatever.
[5051.62 → 5053.52] Let's kind of collect this thing together.
[5054.02 → 5058.82] I put that show on, and I just couldn't stop cleaning because it was a great show and I couldn't stop listening because it was a great show.
[5059.48 → 5061.00] And so I think Louis really brought it.
[5061.18 → 5071.24] But in particular, I'm really thankful for the perspective that Chris and the perspective that Nick brought to this show because they really helped shape that show.
[5071.24 → 5077.56] I just love the way that they, the way they, they sort of like danced around the conversation and brought it to life.
[5077.62 → 5079.06] It was really a great job.
[5079.12 → 5080.22] I was very impressed by them.
[5080.48 → 5080.60] Yeah.
[5080.98 → 5081.64] One hundred percent.
[5082.02 → 5089.90] I listened to it a couple of times, both on the JS Party feed and on the change log feed because I'm a loyal listener of all of our shows.
[5090.16 → 5090.98] I'm not loyal.
[5090.98 → 5092.74] I didn't say anything about you.
[5092.84 → 5093.76] Because I'm a loyal listener.
[5093.94 → 5095.12] I just talked about myself.
[5095.42 → 5095.64] Zing.
[5095.98 → 5096.76] Didn't talk about you.
[5097.48 → 5097.76] All right.
[5097.80 → 5103.24] I'm on my last favourite here because I also exercise self-control and selected five.
[5103.38 → 5105.36] Unlike yourself, who has quite a few left.
[5105.50 → 5106.00] I've got eight.
[5106.18 → 5108.06] Too many favourites to pick from.
[5108.52 → 5113.36] And this last one for me is the other time I went really outside our wheelhouse.
[5113.48 → 5117.16] In addition to why we love BIM episode, this one's even further away for what we normally do.
[5117.16 → 5123.42] This new change log special song encoder with standard out the rapper.
[5123.58 → 5130.48] Now, unlike the BIM episode, which went bonkers on the downloads, this one didn't particularly hit like that one did.
[5130.98 → 5134.52] But I don't even care because I freaking loved this episode.
[5134.64 → 5135.88] I had so much fun making it.
[5136.34 → 5143.36] If I have to go back to one episode and listen to it over and over again, it's the one that I will go and listen to because I love the music.
[5143.76 → 5145.74] I love what he does.
[5145.74 → 5151.38] And it was definitely one of my favourite things that we worked on this year.
[5151.84 → 5153.68] And I look forward to doing some more song encoders.
[5153.80 → 5158.22] It's funny because on that episode, we talk about how he hasn't really blown up as an artist.
[5158.96 → 5160.28] And maybe I asked him why.
[5160.36 → 5167.76] And it's kind of like, well, maybe the cross-section of people who write software and people who love rap music is just like a very small group of people.
[5167.76 → 5172.34] And maybe that's the same case with our listeners because we had good listens.
[5172.52 → 5176.60] You know, it's a respectable show, but it wasn't like dropping fire like the BIM episode was.
[5177.32 → 5180.16] And then maybe it's because, you know, some of us love hip hop.
[5180.24 → 5182.90] I know we've had a few huge compliments from that episode.
[5183.50 → 5189.26] People are like, this is fire, but not in the numbers that we got with the other special.
[5189.26 → 5191.68] Yeah, you know, I think that's going to be the case.
[5191.98 → 5198.06] You know, I have to concur that that was one of those shows I could definitely and have gone back and listened to it a few times.
[5198.58 → 5203.14] Something about just his story and even his natural non-singing voice.
[5203.50 → 5203.74] Yeah.
[5204.10 → 5207.30] Like he says angsty teenager a couple of times in there.
[5207.36 → 5211.22] Like you can almost hear the angst in his voice.
[5211.30 → 5211.62] Right.
[5211.62 → 5212.94] Just as normal talking.
[5213.82 → 5221.80] And I what I love most is that somehow he found a way to turn that angst into creation.
[5222.44 → 5228.44] He tells a story about his brother got him, you know, the microphone and the whole just the just viral.
[5229.06 → 5230.56] Hell dot JS was his first one.
[5230.92 → 5231.08] Yeah.
[5231.30 → 5231.98] Yeah, exactly.
[5232.66 → 5236.24] But how that turned into like, let me just put it out there because I think that's what happens.
[5236.24 → 5242.34] Like somehow we all get a chance to to to in quotes put it out there and that it is art.
[5243.18 → 5249.52] And I remember back in the day I would tell Heather, my wife, early in my podcast or even like this is my art.
[5249.52 → 5255.98] You know, even like with software design, like obviously that's more art than this might be, you know, literally art.
[5256.24 → 5259.06] I'm like I just feel like I got to show up every day and put out this art.
[5259.20 → 5265.48] And like, you know, I want to encourage everybody who's out there listening, like fall in his footsteps and put out your art, whatever that art is.
[5265.48 → 5272.88] And 3 a.m. in San Francisco was a perfect track, in my opinion.
[5273.12 → 5276.86] And one where I was like, you know, we got angels who invest.
[5277.20 → 5278.10] They don't protect.
[5278.86 → 5282.20] Like the lyrics he put in that was just really, really magical.
[5282.56 → 5284.88] And so I'm I'm thankful for Stand Out the Rapper.
[5285.46 → 5291.60] In my original idea of that episode, that was the final track that played it out.
[5291.60 → 5298.70] And then as we went, we got going, it ended up that he had this brand-new track that he came up with, Integrations.
[5299.42 → 5301.72] And he was going to drop it the same day we dropped the episode.
[5301.82 → 5302.98] I'm like, how cool is that?
[5303.04 → 5305.68] So like that I saved instead for the ending.
[5305.80 → 5308.54] Like let's end on this brand-new joint from Stand Out.
[5308.54 → 5311.78] But yeah, 3 a.m. in San Francisco was so poignant.
[5312.18 → 5317.60] And this other stuff is so funny that it's like, wow, all of a sudden, like he said, like the funny guy has things to say all of a sudden.
[5317.96 → 5321.08] And so I was going to end the show with that track because I agree.
[5321.18 → 5322.56] It's its awesome.
[5322.88 → 5324.96] But yeah, at the end of the day, don't make me feel it.
[5325.08 → 5326.36] Just make me laugh, you know.
[5326.68 → 5326.98] Totally.
[5326.98 → 5329.74] But a little bit of behind the scenes on this one.
[5329.94 → 5333.74] So I pitched this idea and I very much was like, what are you talking about?
[5334.70 → 5334.94] Yeah.
[5335.16 → 5349.06] You know, it's sometimes where I think and as a thankful bit to you and a source of encouragement even to me, sometimes I think I saw a ticktock on this recently, where it's like you can't tell somebody your vision.
[5349.18 → 5353.96] Sometimes you have to show them your vision before they can follow you because only you can see your vision.
[5353.96 → 5354.32] Yeah.
[5354.32 → 5362.42] And so I would, you know, as an encouragement to you, like you're going to do this anyway, but always, you know, show up with your vision, like just because I don't agree with it.
[5362.42 → 5368.34] And the same thing for me, like if you don't agree with my vision early, put a bit more work into it till it's enough to see more of.
[5368.78 → 5378.86] Because once I got a glimpse further into what this could be, not just stand out the wrapper and what they brought to, you know, making this cool and interesting is like showing that.
[5378.86 → 5381.80] And I think that's something I think you've developed this year was this.
[5382.12 → 5382.28] Yeah.
[5382.44 → 5396.60] Between the Vim episode and this like you, you definitely have a storyteller heart, and you're able to take all of this widespread story and somehow condense it into an edit, which I think is very much a skill.
[5396.96 → 5398.80] And you've definitely developed that skill.
[5399.28 → 5399.84] Oh, thank you.
[5399.96 → 5401.14] I'm definitely working on it.
[5401.14 → 5405.92] And I should say that this whole song encoder thing, I do say it in the outro, but I'll say it again.
[5406.04 → 5410.92] It's like completely inspired by Song Exploder podcast, which I've listened to for years.
[5410.92 → 5413.50] And I've always thought this is such a cool podcast.
[5413.64 → 5414.94] I love the way he does it.
[5415.44 → 5421.24] Now he's focusing in on a single song and I just didn't feel like we had the meat to do that.
[5421.34 → 5423.50] So I was like, well, let's focus on the single person and make a show.
[5423.62 → 5427.46] But, you know, I like to be inspired by other people's cool art and put out our own cool art.
[5427.46 → 5434.58] And so, you know, as a fan of podcasts, I was just like, this is what, you know, we need something like this, but like put our spin on it.
[5434.64 → 5443.06] So I'm looking forward to doing more things in that vein, you know, being inspired and hopefully inspiring others to make cool stuff.
[5444.08 → 5450.46] I couldn't imagine a podcast world where this episode didn't exist, like for programmers.
[5450.46 → 5463.24] For programmers, like, like I think part of our job and what makes this, so fun is that we find out what needs to exist to encourage the future generation of developers, current and future.
[5463.24 → 5481.48] And I think it's part of our duty and part of the thing we our mission to find out what that those beautiful gems are hidden in the veils of the programming world and the world of software, whether it's startups, whether it's the next framework, whether it's the next language, the next paradigm shift, the next disruption.
[5481.96 → 5482.36] Yeah.
[5482.54 → 5483.98] And help it exist.
[5484.78 → 5486.70] Well, when you say it like that, sounds like a lot of pressure.
[5486.70 → 5495.74] Well, I think it is, but I think, you know, the way you dismiss pressure or distill pressure like that is, is just show up and do what he's done every single day.
[5495.90 → 5496.30] Oh, yeah.
[5496.72 → 5497.72] You know, that's how you do it.
[5497.80 → 5499.00] And it's a day by day thing.
[5510.74 → 5513.46] This episode is brought to you by Fire hydrant.
[5513.46 → 5516.74] Fire hydrant is the reliability platform for teams of all sizes.
[5517.24 → 5524.38] With Fire hydrant, teams achieve reliability at scale by enabling speed and consistency from your service deployment to an unexpected outage.
[5524.72 → 5529.16] When your team learns from an incident, you can codify those learnings into repeatable automated run books.
[5529.44 → 5537.16] These run books can create a Slack incident channel, notify particular team members, create tickets, schedule a Zoom meeting, execute a script or send a webhook.
[5537.16 → 5542.96] For example, your app goes down, an alert gets sent to a specific Slack channel, which can then be turned into an incident.
[5543.26 → 5546.04] That will trigger a workflow you define in a run book.
[5546.30 → 5553.00] A pin message inside Slack will show off all the details, the deer ticket, the clubhouse ticket, the Zoom meeting.
[5553.24 → 5558.56] And all of this is contained in your dedicated incident channel everyone on the team pays attention to.
[5558.84 → 5562.96] Spend less time thinking about what to do next and get to work actually resolving the issue faster.
[5562.96 → 5569.34] What would normally be multiple manual tasks across the entire spectrum of responding to an incident can be automated in every way with Fire hydrant.
[5569.52 → 5571.40] Give them a try for free for 14 days.
[5571.66 → 5573.06] Get access to every feature.
[5573.34 → 5574.30] No credit card required.
[5574.72 → 5576.50] Get started at Firehydrant.io.
[5576.82 → 5578.88] Again, Firehydrant.io.
[5578.88 → 5579.50] Firehydrant.io.
[5598.64 → 5599.16] All right.
[5599.20 → 5600.56] So I shot my favourites out there.
[5600.64 → 5602.58] You got a long list of more.
[5602.74 → 5602.86] Yeah.
[5603.06 → 5605.66] Why don't you go ahead and do them as quickly or slowly as you like?
[5606.16 → 5606.58] I'll rattle.
[5606.94 → 5607.76] Here's what we'll do.
[5607.76 → 5614.02] I'll rattle a few of them off that are left over, and I'll let you choose which one we dive deeper into.
[5614.44 → 5619.74] So the first one of the list that didn't get spoken of yet on my list, which is eight.
[5620.50 → 5621.66] The norm is five.
[5621.78 → 5627.36] However, last year we did come up with, you know, these are our favourites and then these were our must listens.
[5627.68 → 5628.68] And I had to explain.
[5628.92 → 5629.60] Oh, that's right.
[5629.72 → 5631.54] The nuance of what must listen is.
[5631.66 → 5633.48] We had arbitrary distinction between the two.
[5633.60 → 5633.84] Yes.
[5633.84 → 5636.70] So I think that these are all my favourites.
[5636.98 → 5637.40] Not necessarily.
[5637.60 → 5639.50] I didn't choose what was a must-listen this year, though.
[5639.70 → 5639.90] OK.
[5640.14 → 5646.30] But the next list is leading a nonprofit unicorn with our good friend Quincy Larson.
[5646.84 → 5651.30] Let's mint some NFTs with Michael Rogers, longtime friend of the show.
[5652.02 → 5655.08] Every commit is a gift in line of maintain a week.
[5655.08 → 5660.20] And with our good friend Brett Cannon, Shopify's vision for the future of commerce.
[5661.04 → 5663.44] And that was with Ilya Gorgon, longtime friend as well.
[5664.04 → 5665.36] Gosh, a lot of longtime friends here.
[5666.08 → 5667.72] And Oh My ZSH with Robbie Russell.
[5667.98 → 5669.30] Again, longtime friend.
[5669.44 → 5671.30] And Oh My ZSH is a must and solve for me.
[5671.40 → 5675.84] I do not stand up a new Mac instance without installing.
[5676.24 → 5680.26] Actually, I should say anything Linux, really, without doing Oh My ZSH.
[5680.26 → 5684.70] Life is just not OK unless it's got ZSH and Oh My ZSH in place.
[5685.24 → 5685.68] I'm sorry.
[5686.28 → 5688.98] So with that being said, a lot of be backs in there.
[5689.18 → 5689.34] Yep.
[5689.48 → 5691.46] A lot of longtime friends in there.
[5691.96 → 5694.20] Which of those stand out most to you?
[5694.60 → 5698.26] So we've discussed every commit is a gift recently on Dev Discuss.
[5698.78 → 5700.58] Shopify was just a few weeks ago.
[5700.74 → 5702.10] That episode dropped.
[5702.82 → 5705.34] And Oh My ZSH was just a couple of weeks before that.
[5705.44 → 5709.04] So let's go back in time and let's talk about minting some NFTs.
[5709.04 → 5709.96] Oh yeah.
[5710.58 → 5711.54] Controversial subject.
[5711.68 → 5711.90] Yeah.
[5712.10 → 5712.70] Hot topic.
[5712.88 → 5713.10] Yeah.
[5713.56 → 5714.32] Love them and hate them.
[5714.88 → 5719.32] What's interesting about NFTs, I think, is that it's currently you got some people who
[5719.32 → 5727.36] are sort of like anti-crypto because of climate change and things like that.
[5727.52 → 5733.16] And I think the sad and challenging thing of that is that we're mixing this paradigm shift
[5733.16 → 5737.34] in humanity, the way we exchange value essentially.
[5737.34 → 5740.30] We're mixing that with a current problem.
[5740.38 → 5744.32] And I think that'll eventually get panned out somehow, some way.
[5744.42 → 5748.44] I think we always innovate to a point somehow that this is no longer a bad thing for the
[5748.44 → 5749.70] human race and the earth.
[5749.70 → 5753.12] And I'm hopeful that that one day that will become a thing.
[5753.24 → 5759.28] But the NFT idea is often in this faddish, this weirdest because you got people on Twitter
[5759.28 → 5765.40] with, you know, Adam stack.ETH, for example, or, you know, Jared Leto.ETH, for example, because
[5765.40 → 5769.54] you got to like to put your identity out there in this crypto world.
[5769.54 → 5774.46] And NFTs is the vehicle, I think, that is propelling Web3 forward.
[5775.24 → 5778.98] You know, we got the old web, which is Web1, where it was like everybody's invited.
[5779.08 → 5779.56] You can publish.
[5779.66 → 5784.96] And Web2 was more on like Web2.io was more on like, OK, now we have social networks.
[5785.04 → 5787.08] Now we have communication down.
[5787.08 → 5792.76] And Web3 is about how do we enable everyone to own a part of the Internet and command a
[5792.76 → 5793.22] part of the Internet.
[5793.38 → 5795.18] And that's very much what Web3 is about.
[5795.78 → 5798.56] And NFTs is exactly that.
[5799.18 → 5805.78] But coming to that show with Michael Rogers, I was very, I would say, green on the NFT subject.
[5806.16 → 5808.28] Very not schooled.
[5808.34 → 5810.54] And that episode very much schooled me.
[5810.92 → 5810.94] Yeah.
[5811.26 → 5813.12] So real quick, let me tell you this.
[5813.12 → 5817.54] I did not make this up, but I heard this, this casting of Web1, 2 and 3, which I thought
[5817.54 → 5821.18] was an interesting way of thinking about it, not in terms of technology.
[5821.94 → 5830.20] But Web1 is when corporations made the content and made the money or they create.
[5830.28 → 5831.94] They were the creators and the value captures.
[5832.60 → 5839.00] Web2, the people created the content and the corporations captured the value or made the
[5839.00 → 5839.24] money.
[5839.24 → 5845.64] And Web3 is when the people will create the content and the people will capture the value
[5845.64 → 5846.96] or make the money.
[5847.28 → 5851.00] I think that's an interesting way of thinking about it versus like trying to define it based
[5851.00 → 5853.58] on is it centralized or decentralized?
[5853.84 → 5854.98] Anyway, that was interesting.
[5855.06 → 5857.86] So I'm just throwing that out there as something that I found interesting.
[5857.96 → 5858.80] Maybe you will as well.
[5859.38 → 5859.54] Totally.
[5860.02 → 5862.52] I, I, that resonates with me very much.
[5862.60 → 5867.24] So Gary See said recently, and I, I mean, seriously, a lot of this stuff was faddish to me for
[5867.24 → 5867.54] a while.
[5867.54 → 5869.16] Like I was like, this is going to blow over.
[5869.36 → 5870.36] I'm not really sure about this.
[5870.42 → 5874.20] But then you got people that like Gary See who look into this further and even like Jack
[5874.20 → 5879.56] Dorsey recently with, you know, stepping down as CEO of, of, of Twitter and doing something
[5879.56 → 5880.16] different basically.
[5880.16 → 5884.60] And he's very much putting it down when it comes to crypto and turning square into a block.
[5884.74 → 5885.28] That's right.
[5885.84 → 5891.40] But it was, it was this idea that, okay, the future, my future network won't just simply
[5891.40 → 5893.64] be, you know, who follows me on Twitter.
[5893.64 → 5900.54] It's, it's somehow involved in like, you know, if we as change, like creative NFTs, for example,
[5900.68 → 5903.32] like the people who've bought will essentially be our followers.
[5904.14 → 5907.86] They can invest in our future, and they can share in the wealth of that future.
[5907.86 → 5910.66] And we can as well through royalties and whatnot.
[5911.78 → 5914.10] It's, it's still very, very early.
[5914.48 → 5914.88] Yeah.
[5914.88 → 5922.60] But a lot of the direction it can take resonates with me in terms of how we can be essentially
[5922.60 → 5925.36] capitalized by our most low list fans.
[5925.88 → 5929.52] People listen to this show, this particular show, this particular episode, not our shows
[5929.52 → 5935.38] in general, this far in, for example, like if, if we wanted to do something where it wasn't
[5935.38 → 5938.18] like, Hey, let's go raise some money from venture capitalists.
[5938.50 → 5940.98] It's almost like Silicon Valley that, that episode.
[5940.98 → 5944.94] And I know you don't listen or watch the show very much, but there is, no, I just hear
[5944.94 → 5945.78] about it from you.
[5945.84 → 5947.08] So I don't even have to watch it anymore.
[5947.26 → 5948.38] I just get all the synopses.
[5948.50 → 5948.60] That's right.
[5948.64 → 5949.22] I'll just tell you.
[5949.54 → 5950.56] Well, there was an episode.
[5951.06 → 5955.28] I think it was called like an ICO or death or something like that.
[5955.32 → 5959.64] I don't have to, I have to look it up, but it was, they were going to ICO because they
[5959.64 → 5961.48] were, they saw, okay.
[5961.58 → 5962.44] It was a long story short.
[5962.52 → 5964.76] I should even go into this, but I'm going to have to really quickly.
[5965.08 → 5965.96] I'll keep it short.
[5965.96 → 5973.20] They accidentally gave away credits on their network and outside their control, they
[5973.20 → 5977.78] got into the open market, and they couldn't get those credits back because they had given
[5977.78 → 5980.28] them away, and they traded hands a few different times.
[5980.40 → 5984.46] And when they finally caught up with it, the credits were worth millions of dollars.
[5984.46 → 5993.14] And so like any good HBO show on current trends and technology, you know, they had to go the
[5993.14 → 6000.80] route of essentially finding out like, how could Icon fit into, into this world is the episode
[6000.80 → 6002.28] was called initial coin offering.
[6002.70 → 6005.58] And so they just dove into it.
[6005.58 → 6007.42] Basically they had some value out there.
[6007.42 → 6014.32] I think it's interesting how you can be fuelled by your most loyalist fans versus simply the
[6014.32 → 6015.86] incumbents of venture capital.
[6016.46 → 6019.94] Not that those are bad people by any means, or there's one mall that's better than the
[6019.94 → 6020.14] other.
[6020.42 → 6021.90] It's just a new avenue.
[6022.22 → 6025.00] It's a new reduction in the barrier to entry.
[6025.32 → 6025.76] Right.
[6026.24 → 6032.48] You know, or a new way to enable your fans to participate because it's, it's not all about
[6032.48 → 6032.96] participation.
[6033.36 → 6034.40] It's what the web's about.
[6034.54 → 6035.38] It's about participation.
[6035.38 → 6036.30] And identification.
[6036.30 → 6037.64] I think.
[6038.06 → 6038.28] For sure.
[6038.52 → 6038.94] Yeah, of course.
[6039.22 → 6042.52] Who I am, what I'm with, who I support, what I represent.
[6042.90 → 6043.06] Right.
[6043.12 → 6044.06] What brands do I wear?
[6044.12 → 6047.22] It's almost like Gucci bag, Nike shoes.
[6047.40 → 6047.72] Right.
[6047.84 → 6048.58] It's very much like that.
[6048.66 → 6053.30] Like, you know, do I own an NFT of changelog's brand-new artwork for their shows?
[6053.46 → 6053.76] Right.
[6053.98 → 6055.36] Well, I don't own it because I like the JPEG.
[6055.60 → 6056.06] Yeah, exactly.
[6056.26 → 6063.08] I own it because I value them so much, and I want to own stock in the future of whatever
[6063.08 → 6064.10] we are via NFT.
[6064.46 → 6065.96] That's what's interesting about this model.
[6066.30 → 6066.80] I agree.
[6067.20 → 6068.62] I do think NFTs are in a bubble.
[6068.88 → 6072.74] I do think it will probably pop and many will fall by the wayside.
[6072.74 → 6076.70] And then we'll have the leftovers are the ones that are actually doing things that are
[6076.70 → 6077.62] interesting and innovative.
[6078.52 → 6082.38] And I think the cool thing is the programmability of it.
[6082.38 → 6083.00] Mm-hmm.
[6083.00 → 6088.94] And if you can imagine that relationship, you can codify that relationship and then you can
[6088.94 → 6091.94] offer that relationship out to the world and see if other people are interested.
[6092.48 → 6093.68] That is new and different.
[6093.94 → 6098.44] I mean, some of these things like, well, you could already support us by going to changelov.com
[6098.44 → 6100.56] slash plus and typing in your credit card or whatever.
[6100.56 → 6103.62] Like that's the payment rails is not the innovation.
[6103.94 → 6107.94] You know, now we have counterparty risk and blah, blah, blah.
[6108.36 → 6110.82] You know, if Stripe kicks us out, you can't do that anymore.
[6111.02 → 6111.82] There's all that kind of stuff.
[6111.92 → 6113.14] So that's there as well.
[6113.14 → 6113.46] Right.
[6113.46 → 6115.20] The permissionless aspect is a part of it.
[6115.26 → 6123.68] But I think really just the ability to imagine a financial relationship between multiple parties
[6123.68 → 6128.36] and codify it and then see if there's interest.
[6128.36 → 6132.50] I think that that's going to create new things that don't exist yet.
[6133.02 → 6137.04] Like right now, we're just kind of like, hey, you can donate through this, or you can
[6137.04 → 6139.82] sign your name on this as the original owner.
[6140.38 → 6141.86] And it's like, it's a JPEG.
[6141.86 → 6144.44] Like I can right-click and download it as the naysayers all say.
[6145.00 → 6148.88] But there's going to be things that you're doing with NFTs five years from now that are
[6148.88 → 6151.02] impossible without them, I believe.
[6151.46 → 6155.38] But there's probably going to be a bubble bust between now and then because it is pretty
[6155.38 → 6156.26] frothy right now.
[6156.88 → 6163.36] You know, it's definitely the beginning, the early innings of what will become of this
[6163.36 → 6166.66] way to create and share the value of what is created out there.
[6167.28 → 6171.46] And I think what's more what's happening now, like any.
[6171.86 → 6177.26] Like any gold rush or any rush of sorts, there's going to be bad actors and there's going
[6177.26 → 6184.46] to be people that are just in it to create like scarcity, you know, and get that value.
[6184.46 → 6188.84] Like I actually saw TikTok recently where I was like, you want to get rich?
[6188.84 → 6194.44] Go to Canva and whatever this and then go to this marketplace and find somebody to create you
[6194.44 → 6201.04] 1000 NFTs or 1000 pieces of artwork and then put those out there as NFTs and this and that.
[6201.08 → 6205.52] And it's like, OK, well, like you're not really bringing anything of value, really.
[6205.58 → 6207.08] You're just selling at that point.
[6207.14 → 6207.78] That's just JPEGs.
[6207.78 → 6213.58] So maybe it's maybe that's the, you know, the code smell, so to speak, is if you're just
[6213.58 → 6216.02] buying a JPEG, you're doing it wrong.
[6216.38 → 6223.72] Like because like if we ever got into the NFT space, it wouldn't be to sell a JPEG.
[6223.88 → 6227.16] That might be the thing you can look at and say, I own this thing.
[6227.30 → 6228.52] And I put it in your gallery.
[6228.64 → 6233.12] You know, there's the other example where like you buy stock in a company on the open
[6233.12 → 6235.70] market, but you can't see that stock.
[6236.06 → 6237.14] You see the value.
[6237.26 → 6238.32] It's the same concept, though.
[6238.34 → 6244.74] It's like instead of it's a way to essentially issue stock to our little fan base, and we give
[6244.74 → 6245.58] them a JPEG to look at.
[6245.64 → 6247.60] But if you're just buying a JPEG, you're probably doing it wrong.
[6247.96 → 6252.34] In our case, we would probably, you know, attach the JPEG just because that's the way
[6252.34 → 6253.12] you visualize it.
[6253.18 → 6256.16] I mean, you literally do buy a JPEG, but what you're buying isn't.
[6256.28 → 6256.40] Right.
[6256.62 → 6258.10] If you're just buying the JPEG, you're doing it wrong.
[6258.52 → 6262.72] But Michael Rogers called us, you know, we should get Wombat back on the show.
[6262.72 → 6264.10] It's been way too many years.
[6264.44 → 6267.64] We talked about the interplanetary file system.
[6267.86 → 6268.08] That's right.
[6268.16 → 6271.16] We even brought the Beastie Boys into that episode.
[6271.28 → 6272.22] It was super cool to do that.
[6272.40 → 6272.90] Oh, that's right.
[6273.08 → 6279.76] But IPS and the fun things they're doing over there, very much investing in the necessary
[6279.76 → 6285.00] infrastructure for what is going to become, you know, the direction of Web3, if it actually
[6285.00 → 6285.76] plays out or not.
[6285.96 → 6287.22] That's what they're investing in.
[6287.28 → 6288.44] That's where Michael Rogers works at.
[6288.64 → 6288.76] Yep.
[6289.18 → 6290.96] Good to have him back on the show.
[6291.26 → 6291.54] Absolutely.
[6291.54 → 6293.92] So that's episode 438.
[6294.34 → 6296.74] And that concludes our faves.
[6297.24 → 6297.80] Mm hmm.
[6298.36 → 6299.10] Long list.
[6299.70 → 6300.46] Long conversation.
[6300.60 → 6303.28] Should we talk future at all, or should we just save it and just call it a day?
[6303.68 → 6307.56] I think if somebody is listening to this, and we didn't share the future with them in any
[6307.56 → 6308.78] way, shape or form, they'd be upset.
[6308.82 → 6309.74] They made it this far.
[6309.86 → 6310.02] Yeah.
[6310.08 → 6315.36] I think if they made it this far, we owe them five more minutes of something that depicts
[6315.36 → 6315.90] where we're going.
[6316.32 → 6316.66] All right.
[6316.68 → 6317.34] Where are we going?
[6317.34 → 6321.28] I don't know if we actually have a lot of ground to share in terms of where we're going.
[6321.36 → 6322.88] We have some loose ideas.
[6323.00 → 6329.52] Jared mentioned, and I even complimented him on his editability of the We Love Vim episode
[6329.52 → 6331.30] and the Song Coder episode.
[6331.50 → 6332.58] And I think we'll do more of those.
[6332.58 → 6334.70] So more specials.
[6334.96 → 6341.30] We have obviously other ideas around podcasts, but we're not exactly excited to move into
[6341.30 → 6345.84] a new space unless it's specific, and we think we can add some value there.
[6345.96 → 6351.06] And there's one in particular that we have some ideas on, but that's to be seen essentially.
[6351.06 → 6353.50] Not to be announced by any means right now.
[6354.50 → 6355.18] I agree.
[6355.28 → 6360.66] More specials, perhaps a new podcast in the next year if that shakes out.
[6360.80 → 6367.52] We're also long overdue for some refreshed looks, maybe some new merch.
[6368.32 → 6375.76] These are things that we're actively pursuing, but also not ready to put a ship date on those
[6375.76 → 6378.90] things yet because, hey, why do that when we don't have to?
[6378.90 → 6387.88] I'd say the most pertinent place that where we're really optimizing for is on the DOG,
[6388.42 → 6388.64] right?
[6388.76 → 6390.48] The operation, operational groove.
[6390.74 → 6395.00] I mean, we had very much put that in place and started working towards that this last year.
[6395.16 → 6396.40] We have a new hire.
[6397.84 → 6399.08] Jason is now on the team.
[6399.60 → 6400.14] Please clap.
[6400.14 → 6409.26] And, you know, I just I think the thing we should project for the future is even greater
[6409.26 → 6411.64] consistency across the board.
[6412.70 → 6416.46] I think that that would be what would make me the most happy for all of 2022.
[6416.62 → 6418.08] We cannot ship a whole new show.
[6418.36 → 6420.52] We could not ship one more special.
[6420.52 → 6428.80] But if we delivered on consistency as it should be, I would count 2022 as a success.
[6429.06 → 6432.40] Now, if we could do that, plus some things, all the better.
[6432.60 → 6435.98] If you're listening this far, I want to mention a few links to you.
[6436.10 → 6438.64] Change law dot com slash community free to enter.
[6438.96 → 6439.64] Everyone's welcome.
[6440.10 → 6442.86] No matter where you're at on your hacker path, you are welcome.
[6442.96 → 6443.74] Hang your hat here.
[6443.74 → 6446.12] Come call our Slack, your home.
[6446.26 → 6452.34] Lots of people in there talking about, you know, Apple stuff, Vim stuff, Linux stuff,
[6452.80 → 6454.32] Unix tooling.
[6455.34 → 6456.76] Lots of conversations in there.
[6457.02 → 6458.46] JS Party is live every week.
[6458.50 → 6459.76] There's lots of conversation there.
[6460.48 → 6463.88] Go Time happens to have a whole separate Slack that is part of the Gopher community.
[6464.36 → 6465.76] So you have to go to that one for that.
[6465.84 → 6467.26] But we'd offer it if it was there.
[6467.58 → 6469.68] So call our community, your home.
[6469.68 → 6480.32] If you're missing some friends, if you're in the middle of Omaha, Nebraska, like Jared once was and needed a home for his hacker heart.
[6481.10 → 6483.24] Come call ours, your home and you will be welcome.
[6483.50 → 6484.38] Change law dot com slash community.
[6484.48 → 6484.94] Totally free.
[6485.42 → 6488.32] Again, hey, if you're a longtime listener, you're like, I want to support these guys.
[6488.86 → 6489.90] The NFTs aren't out there yet.
[6490.00 → 6491.36] I might buy one if there was one.
[6491.54 → 6492.42] They're not there yet.
[6493.40 → 6494.50] Check out plus.
[6494.50 → 6503.50] If you love our ads, don't check it out because we get lots of feedback from people that say, yeah, I love change law plus and I love supporting you.
[6503.80 → 6507.04] But I really like your ads, too, because they help me stay grounded and like what's out there.
[6507.44 → 6509.60] We do put a ton of effort into our ad ops.
[6510.40 → 6512.96] So change law dot com slash plus.
[6513.04 → 6519.30] If you want to support us in that way or get our ad free shows, plus some bonus content behind the scenes, fun things like that.
[6519.30 → 6521.76] That only hits the plus feed.
[6522.42 → 6524.06] Sorry, nonplus plus subscribers.
[6524.18 → 6524.82] That's how it works.
[6525.64 → 6530.54] And then I would say, you know, last, obviously, the Galaxy brand move.
[6531.34 → 6531.98] Master feed.
[6533.02 → 6534.14] Change law dot com slash master.
[6534.18 → 6536.30] If you listen to this show all the way to this point, you're hearing my voice.
[6536.84 → 6538.06] You should be getting our shows.
[6538.50 → 6540.68] And if you don't like one to swipe left and delete it.
[6540.70 → 6541.08] That's right.
[6541.14 → 6542.22] You know, out of the list for you.
[6542.28 → 6543.44] That way you get everything we ship.
[6543.72 → 6544.90] You never miss anything.
[6544.90 → 6549.96] You get the bonus stuff from backstage, which we have some awesome conversations on backstage.
[6550.72 → 6555.30] We've talked about Tenet recently with heavy spoilers.
[6555.70 → 6559.42] Our good friend, Paul, who helped us spoil a bunch of stuff on Tenet.
[6559.58 → 6562.60] We talked about other things around programming and just it's off.
[6562.84 → 6563.52] It's off angle.
[6563.86 → 6564.68] And it's a lot of fun.
[6564.80 → 6567.54] So check that out as well.
[6567.68 → 6568.26] What else, Jared?
[6569.12 → 6570.02] Thanks for listening.
[6570.14 → 6572.80] Thanks for being a part of what makes Changelog awesome.
[6572.80 → 6575.06] We appreciate you spending time with us.
[6575.80 → 6577.26] Have a great new year.
[6577.34 → 6579.02] We'll see you in 2022.
[6579.62 → 6580.44] That's so weird to say, right?
[6580.52 → 6581.70] We'll see you next year.
[6582.08 → 6582.26] Yeah.
[6582.54 → 6582.72] Yeah.
[6582.78 → 6583.42] We'll see you next year.
[6583.88 → 6585.48] Listeners, thank you so much for listening to the show.
[6586.60 → 6588.00] Sponsors who have sponsored the show.
[6588.38 → 6589.02] Thank you so much.
[6589.08 → 6589.78] You know who you are.
[6590.46 → 6591.76] And we'll see you next year.
[6594.72 → 6595.98] We'll see you next year.
[6596.40 → 6600.68] Here's to an awesome time with family, friends at work or at play.
[6600.68 → 6608.90] Whatever you're doing to round out the year, we hope you are thriving, enjoying life and getting ready for whatever it is 2022 has in store for you.
[6609.20 → 6616.12] Since you dig this show, you'll probably love Go Time, JS Party, Ship It, Practical AI or Founders Talk.
[6616.24 → 6617.74] That's a lot of subscriptions.
[6618.24 → 6624.14] But you can get every episode of every podcast we ship in one easy feed at changelog.com slash master.
[6624.50 → 6625.34] It's your one-stop shop.
[6625.76 → 6628.10] I know we say it a lot, but we can't say it enough.
[6628.26 → 6629.22] Thank you for listening.
[6629.22 → 6634.26] We know you only have 24 hours in a day, and we appreciate it that you spend some of it with us.
[6634.70 → 6640.72] Stay tuned in 2022 for more awesome conversations, a few surprises and who knows what else.
[6641.08 → 6641.96] That's all for now.
[6642.14 → 6643.30] But we'll talk to you again next year.
[6643.30 → 6656.46] Thank you.
[6656.46 → 6686.44] Thank you.
[6686.46 → 6716.44] Thank you.
